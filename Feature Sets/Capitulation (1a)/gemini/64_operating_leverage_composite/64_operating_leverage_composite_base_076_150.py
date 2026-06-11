"""
64_operating_leverage_composite — Base Features 076-150
Domain: OpInc growth vs Rev growth
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

def olec_076_opex_g_5d(sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_076_opex_g_5d"""
    return ((sga + rnd).pct_change(252)).shift(5)

def olec_077_opex_g_21d(sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_077_opex_g_21d"""
    return ((sga + rnd).pct_change(252)).shift(21)

def olec_078_opex_g_63d(sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_078_opex_g_63d"""
    return ((sga + rnd).pct_change(252)).shift(63)

def olec_079_opex_g_126d(sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_079_opex_g_126d"""
    return ((sga + rnd).pct_change(252)).shift(126)

def olec_080_opex_g_252d(sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_080_opex_g_252d"""
    return ((sga + rnd).pct_change(252)).shift(252)

def olec_081_rev_per_emp_proxy_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_081_rev_per_emp_proxy_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def olec_082_rev_per_emp_proxy_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_082_rev_per_emp_proxy_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def olec_083_rev_per_emp_proxy_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_083_rev_per_emp_proxy_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def olec_084_rev_per_emp_proxy_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_084_rev_per_emp_proxy_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def olec_085_rev_per_emp_proxy_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_085_rev_per_emp_proxy_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def olec_086_ebit_per_emp_proxy_5d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_086_ebit_per_emp_proxy_5d"""
    return (_safe_div(ebit, assets)).shift(5)

def olec_087_ebit_per_emp_proxy_21d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_087_ebit_per_emp_proxy_21d"""
    return (_safe_div(ebit, assets)).shift(21)

def olec_088_ebit_per_emp_proxy_63d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_088_ebit_per_emp_proxy_63d"""
    return (_safe_div(ebit, assets)).shift(63)

def olec_089_ebit_per_emp_proxy_126d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_089_ebit_per_emp_proxy_126d"""
    return (_safe_div(ebit, assets)).shift(126)

def olec_090_ebit_per_emp_proxy_252d(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """olec_090_ebit_per_emp_proxy_252d"""
    return (_safe_div(ebit, assets)).shift(252)

def olec_091_cost_of_rev_g_5d(cor: pd.Series) -> pd.Series:
    """olec_091_cost_of_rev_g_5d"""
    return (cor.pct_change(252)).shift(5)

def olec_092_cost_of_rev_g_21d(cor: pd.Series) -> pd.Series:
    """olec_092_cost_of_rev_g_21d"""
    return (cor.pct_change(252)).shift(21)

def olec_093_cost_of_rev_g_63d(cor: pd.Series) -> pd.Series:
    """olec_093_cost_of_rev_g_63d"""
    return (cor.pct_change(252)).shift(63)

def olec_094_cost_of_rev_g_126d(cor: pd.Series) -> pd.Series:
    """olec_094_cost_of_rev_g_126d"""
    return (cor.pct_change(252)).shift(126)

def olec_095_cost_of_rev_g_252d(cor: pd.Series) -> pd.Series:
    """olec_095_cost_of_rev_g_252d"""
    return (cor.pct_change(252)).shift(252)

def olec_096_margin_stability_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_096_margin_stability_5d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(ebit, revenue), 252))).shift(5)

def olec_097_margin_stability_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_097_margin_stability_21d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(ebit, revenue), 252))).shift(21)

def olec_098_margin_stability_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_098_margin_stability_63d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(ebit, revenue), 252))).shift(63)

def olec_099_margin_stability_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_099_margin_stability_126d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(ebit, revenue), 252))).shift(126)

def olec_100_margin_stability_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_100_margin_stability_252d"""
    return (_safe_div(1.0, _rolling_std(_safe_div(ebit, revenue), 252))).shift(252)

def olec_101_leverage_eff_5d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_101_leverage_eff_5d"""
    return (_safe_div(ebit.pct_change(252), (sga + rnd).pct_change(252))).shift(5)

def olec_102_leverage_eff_21d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_102_leverage_eff_21d"""
    return (_safe_div(ebit.pct_change(252), (sga + rnd).pct_change(252))).shift(21)

def olec_103_leverage_eff_63d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_103_leverage_eff_63d"""
    return (_safe_div(ebit.pct_change(252), (sga + rnd).pct_change(252))).shift(63)

def olec_104_leverage_eff_126d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_104_leverage_eff_126d"""
    return (_safe_div(ebit.pct_change(252), (sga + rnd).pct_change(252))).shift(126)

def olec_105_leverage_eff_252d(ebit: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_105_leverage_eff_252d"""
    return (_safe_div(ebit.pct_change(252), (sga + rnd).pct_change(252))).shift(252)

def olec_106_break_even_proxy_5d(gp: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_106_break_even_proxy_5d"""
    return (_safe_div(sga + rnd, gp)).shift(5)

def olec_107_break_even_proxy_21d(gp: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_107_break_even_proxy_21d"""
    return (_safe_div(sga + rnd, gp)).shift(21)

def olec_108_break_even_proxy_63d(gp: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_108_break_even_proxy_63d"""
    return (_safe_div(sga + rnd, gp)).shift(63)

def olec_109_break_even_proxy_126d(gp: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_109_break_even_proxy_126d"""
    return (_safe_div(sga + rnd, gp)).shift(126)

def olec_110_break_even_proxy_252d(gp: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_110_break_even_proxy_252d"""
    return (_safe_div(sga + rnd, gp)).shift(252)

def olec_111_margin_expansion_vel_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_111_margin_expansion_vel_5d"""
    return ((_safe_div(ebit, revenue)).diff(63)).shift(5)

def olec_112_margin_expansion_vel_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_112_margin_expansion_vel_21d"""
    return ((_safe_div(ebit, revenue)).diff(63)).shift(21)

def olec_113_margin_expansion_vel_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_113_margin_expansion_vel_63d"""
    return ((_safe_div(ebit, revenue)).diff(63)).shift(63)

def olec_114_margin_expansion_vel_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_114_margin_expansion_vel_126d"""
    return ((_safe_div(ebit, revenue)).diff(63)).shift(126)

def olec_115_margin_expansion_vel_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """olec_115_margin_expansion_vel_252d"""
    return ((_safe_div(ebit, revenue)).diff(63)).shift(252)

def olec_116_rev_growth_vel_5d(revenue: pd.Series) -> pd.Series:
    """olec_116_rev_growth_vel_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def olec_117_rev_growth_vel_21d(revenue: pd.Series) -> pd.Series:
    """olec_117_rev_growth_vel_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def olec_118_rev_growth_vel_63d(revenue: pd.Series) -> pd.Series:
    """olec_118_rev_growth_vel_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def olec_119_rev_growth_vel_126d(revenue: pd.Series) -> pd.Series:
    """olec_119_rev_growth_vel_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def olec_120_rev_growth_vel_252d(revenue: pd.Series) -> pd.Series:
    """olec_120_rev_growth_vel_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def olec_121_ebit_growth_vel_5d(ebit: pd.Series) -> pd.Series:
    """olec_121_ebit_growth_vel_5d"""
    return (ebit.pct_change(252).diff(63)).shift(5)

def olec_122_ebit_growth_vel_21d(ebit: pd.Series) -> pd.Series:
    """olec_122_ebit_growth_vel_21d"""
    return (ebit.pct_change(252).diff(63)).shift(21)

def olec_123_ebit_growth_vel_63d(ebit: pd.Series) -> pd.Series:
    """olec_123_ebit_growth_vel_63d"""
    return (ebit.pct_change(252).diff(63)).shift(63)

def olec_124_ebit_growth_vel_126d(ebit: pd.Series) -> pd.Series:
    """olec_124_ebit_growth_vel_126d"""
    return (ebit.pct_change(252).diff(63)).shift(126)

def olec_125_ebit_growth_vel_252d(ebit: pd.Series) -> pd.Series:
    """olec_125_ebit_growth_vel_252d"""
    return (ebit.pct_change(252).diff(63)).shift(252)

def olec_126_contribution_margin_5d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """olec_126_contribution_margin_5d"""
    return (_safe_div(revenue - cor, revenue)).shift(5)

def olec_127_contribution_margin_21d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """olec_127_contribution_margin_21d"""
    return (_safe_div(revenue - cor, revenue)).shift(21)

def olec_128_contribution_margin_63d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """olec_128_contribution_margin_63d"""
    return (_safe_div(revenue - cor, revenue)).shift(63)

def olec_129_contribution_margin_126d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """olec_129_contribution_margin_126d"""
    return (_safe_div(revenue - cor, revenue)).shift(126)

def olec_130_contribution_margin_252d(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """olec_130_contribution_margin_252d"""
    return (_safe_div(revenue - cor, revenue)).shift(252)

def olec_131_operating_efficiency_5d(revenue: pd.Series, cor: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_131_operating_efficiency_5d"""
    return (_safe_div(revenue, sga + rnd + cor)).shift(5)

def olec_132_operating_efficiency_21d(revenue: pd.Series, cor: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_132_operating_efficiency_21d"""
    return (_safe_div(revenue, sga + rnd + cor)).shift(21)

def olec_133_operating_efficiency_63d(revenue: pd.Series, cor: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_133_operating_efficiency_63d"""
    return (_safe_div(revenue, sga + rnd + cor)).shift(63)

def olec_134_operating_efficiency_126d(revenue: pd.Series, cor: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_134_operating_efficiency_126d"""
    return (_safe_div(revenue, sga + rnd + cor)).shift(126)

def olec_135_operating_efficiency_252d(revenue: pd.Series, cor: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """olec_135_operating_efficiency_252d"""
    return (_safe_div(revenue, sga + rnd + cor)).shift(252)

def olec_136_ni_growth_accel_5d(netinc: pd.Series) -> pd.Series:
    """olec_136_ni_growth_accel_5d"""
    return (netinc.pct_change(252).diff(63).diff(21)).shift(5)

def olec_137_ni_growth_accel_21d(netinc: pd.Series) -> pd.Series:
    """olec_137_ni_growth_accel_21d"""
    return (netinc.pct_change(252).diff(63).diff(21)).shift(21)

def olec_138_ni_growth_accel_63d(netinc: pd.Series) -> pd.Series:
    """olec_138_ni_growth_accel_63d"""
    return (netinc.pct_change(252).diff(63).diff(21)).shift(63)

def olec_139_ni_growth_accel_126d(netinc: pd.Series) -> pd.Series:
    """olec_139_ni_growth_accel_126d"""
    return (netinc.pct_change(252).diff(63).diff(21)).shift(126)

def olec_140_ni_growth_accel_252d(netinc: pd.Series) -> pd.Series:
    """olec_140_ni_growth_accel_252d"""
    return (netinc.pct_change(252).diff(63).diff(21)).shift(252)

def olec_141_ebit_growth_accel_5d(ebit: pd.Series) -> pd.Series:
    """olec_141_ebit_growth_accel_5d"""
    return (ebit.pct_change(252).diff(63).diff(21)).shift(5)

def olec_142_ebit_growth_accel_21d(ebit: pd.Series) -> pd.Series:
    """olec_142_ebit_growth_accel_21d"""
    return (ebit.pct_change(252).diff(63).diff(21)).shift(21)

def olec_143_ebit_growth_accel_63d(ebit: pd.Series) -> pd.Series:
    """olec_143_ebit_growth_accel_63d"""
    return (ebit.pct_change(252).diff(63).diff(21)).shift(63)

def olec_144_ebit_growth_accel_126d(ebit: pd.Series) -> pd.Series:
    """olec_144_ebit_growth_accel_126d"""
    return (ebit.pct_change(252).diff(63).diff(21)).shift(126)

def olec_145_ebit_growth_accel_252d(ebit: pd.Series) -> pd.Series:
    """olec_145_ebit_growth_accel_252d"""
    return (ebit.pct_change(252).diff(63).diff(21)).shift(252)

def olec_146_rev_growth_accel_5d(revenue: pd.Series) -> pd.Series:
    """olec_146_rev_growth_accel_5d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(5)

def olec_147_rev_growth_accel_21d(revenue: pd.Series) -> pd.Series:
    """olec_147_rev_growth_accel_21d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(21)

def olec_148_rev_growth_accel_63d(revenue: pd.Series) -> pd.Series:
    """olec_148_rev_growth_accel_63d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(63)

def olec_149_rev_growth_accel_126d(revenue: pd.Series) -> pd.Series:
    """olec_149_rev_growth_accel_126d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(126)

def olec_150_rev_growth_accel_252d(revenue: pd.Series) -> pd.Series:
    """olec_150_rev_growth_accel_252d"""
    return (revenue.pct_change(252).diff(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V64_REGISTRY = {
    "olec_076_opex_g_5d": {"inputs": ['sga', 'rnd'], "func": olec_076_opex_g_5d},
    "olec_077_opex_g_21d": {"inputs": ['sga', 'rnd'], "func": olec_077_opex_g_21d},
    "olec_078_opex_g_63d": {"inputs": ['sga', 'rnd'], "func": olec_078_opex_g_63d},
    "olec_079_opex_g_126d": {"inputs": ['sga', 'rnd'], "func": olec_079_opex_g_126d},
    "olec_080_opex_g_252d": {"inputs": ['sga', 'rnd'], "func": olec_080_opex_g_252d},
    "olec_081_rev_per_emp_proxy_5d": {"inputs": ['revenue', 'assets'], "func": olec_081_rev_per_emp_proxy_5d},
    "olec_082_rev_per_emp_proxy_21d": {"inputs": ['revenue', 'assets'], "func": olec_082_rev_per_emp_proxy_21d},
    "olec_083_rev_per_emp_proxy_63d": {"inputs": ['revenue', 'assets'], "func": olec_083_rev_per_emp_proxy_63d},
    "olec_084_rev_per_emp_proxy_126d": {"inputs": ['revenue', 'assets'], "func": olec_084_rev_per_emp_proxy_126d},
    "olec_085_rev_per_emp_proxy_252d": {"inputs": ['revenue', 'assets'], "func": olec_085_rev_per_emp_proxy_252d},
    "olec_086_ebit_per_emp_proxy_5d": {"inputs": ['ebit', 'assets'], "func": olec_086_ebit_per_emp_proxy_5d},
    "olec_087_ebit_per_emp_proxy_21d": {"inputs": ['ebit', 'assets'], "func": olec_087_ebit_per_emp_proxy_21d},
    "olec_088_ebit_per_emp_proxy_63d": {"inputs": ['ebit', 'assets'], "func": olec_088_ebit_per_emp_proxy_63d},
    "olec_089_ebit_per_emp_proxy_126d": {"inputs": ['ebit', 'assets'], "func": olec_089_ebit_per_emp_proxy_126d},
    "olec_090_ebit_per_emp_proxy_252d": {"inputs": ['ebit', 'assets'], "func": olec_090_ebit_per_emp_proxy_252d},
    "olec_091_cost_of_rev_g_5d": {"inputs": ['cor'], "func": olec_091_cost_of_rev_g_5d},
    "olec_092_cost_of_rev_g_21d": {"inputs": ['cor'], "func": olec_092_cost_of_rev_g_21d},
    "olec_093_cost_of_rev_g_63d": {"inputs": ['cor'], "func": olec_093_cost_of_rev_g_63d},
    "olec_094_cost_of_rev_g_126d": {"inputs": ['cor'], "func": olec_094_cost_of_rev_g_126d},
    "olec_095_cost_of_rev_g_252d": {"inputs": ['cor'], "func": olec_095_cost_of_rev_g_252d},
    "olec_096_margin_stability_5d": {"inputs": ['revenue', 'ebit'], "func": olec_096_margin_stability_5d},
    "olec_097_margin_stability_21d": {"inputs": ['revenue', 'ebit'], "func": olec_097_margin_stability_21d},
    "olec_098_margin_stability_63d": {"inputs": ['revenue', 'ebit'], "func": olec_098_margin_stability_63d},
    "olec_099_margin_stability_126d": {"inputs": ['revenue', 'ebit'], "func": olec_099_margin_stability_126d},
    "olec_100_margin_stability_252d": {"inputs": ['revenue', 'ebit'], "func": olec_100_margin_stability_252d},
    "olec_101_leverage_eff_5d": {"inputs": ['ebit', 'sga', 'rnd'], "func": olec_101_leverage_eff_5d},
    "olec_102_leverage_eff_21d": {"inputs": ['ebit', 'sga', 'rnd'], "func": olec_102_leverage_eff_21d},
    "olec_103_leverage_eff_63d": {"inputs": ['ebit', 'sga', 'rnd'], "func": olec_103_leverage_eff_63d},
    "olec_104_leverage_eff_126d": {"inputs": ['ebit', 'sga', 'rnd'], "func": olec_104_leverage_eff_126d},
    "olec_105_leverage_eff_252d": {"inputs": ['ebit', 'sga', 'rnd'], "func": olec_105_leverage_eff_252d},
    "olec_106_break_even_proxy_5d": {"inputs": ['gp', 'sga', 'rnd'], "func": olec_106_break_even_proxy_5d},
    "olec_107_break_even_proxy_21d": {"inputs": ['gp', 'sga', 'rnd'], "func": olec_107_break_even_proxy_21d},
    "olec_108_break_even_proxy_63d": {"inputs": ['gp', 'sga', 'rnd'], "func": olec_108_break_even_proxy_63d},
    "olec_109_break_even_proxy_126d": {"inputs": ['gp', 'sga', 'rnd'], "func": olec_109_break_even_proxy_126d},
    "olec_110_break_even_proxy_252d": {"inputs": ['gp', 'sga', 'rnd'], "func": olec_110_break_even_proxy_252d},
    "olec_111_margin_expansion_vel_5d": {"inputs": ['revenue', 'ebit'], "func": olec_111_margin_expansion_vel_5d},
    "olec_112_margin_expansion_vel_21d": {"inputs": ['revenue', 'ebit'], "func": olec_112_margin_expansion_vel_21d},
    "olec_113_margin_expansion_vel_63d": {"inputs": ['revenue', 'ebit'], "func": olec_113_margin_expansion_vel_63d},
    "olec_114_margin_expansion_vel_126d": {"inputs": ['revenue', 'ebit'], "func": olec_114_margin_expansion_vel_126d},
    "olec_115_margin_expansion_vel_252d": {"inputs": ['revenue', 'ebit'], "func": olec_115_margin_expansion_vel_252d},
    "olec_116_rev_growth_vel_5d": {"inputs": ['revenue'], "func": olec_116_rev_growth_vel_5d},
    "olec_117_rev_growth_vel_21d": {"inputs": ['revenue'], "func": olec_117_rev_growth_vel_21d},
    "olec_118_rev_growth_vel_63d": {"inputs": ['revenue'], "func": olec_118_rev_growth_vel_63d},
    "olec_119_rev_growth_vel_126d": {"inputs": ['revenue'], "func": olec_119_rev_growth_vel_126d},
    "olec_120_rev_growth_vel_252d": {"inputs": ['revenue'], "func": olec_120_rev_growth_vel_252d},
    "olec_121_ebit_growth_vel_5d": {"inputs": ['ebit'], "func": olec_121_ebit_growth_vel_5d},
    "olec_122_ebit_growth_vel_21d": {"inputs": ['ebit'], "func": olec_122_ebit_growth_vel_21d},
    "olec_123_ebit_growth_vel_63d": {"inputs": ['ebit'], "func": olec_123_ebit_growth_vel_63d},
    "olec_124_ebit_growth_vel_126d": {"inputs": ['ebit'], "func": olec_124_ebit_growth_vel_126d},
    "olec_125_ebit_growth_vel_252d": {"inputs": ['ebit'], "func": olec_125_ebit_growth_vel_252d},
    "olec_126_contribution_margin_5d": {"inputs": ['revenue', 'cor'], "func": olec_126_contribution_margin_5d},
    "olec_127_contribution_margin_21d": {"inputs": ['revenue', 'cor'], "func": olec_127_contribution_margin_21d},
    "olec_128_contribution_margin_63d": {"inputs": ['revenue', 'cor'], "func": olec_128_contribution_margin_63d},
    "olec_129_contribution_margin_126d": {"inputs": ['revenue', 'cor'], "func": olec_129_contribution_margin_126d},
    "olec_130_contribution_margin_252d": {"inputs": ['revenue', 'cor'], "func": olec_130_contribution_margin_252d},
    "olec_131_operating_efficiency_5d": {"inputs": ['revenue', 'cor', 'sga', 'rnd'], "func": olec_131_operating_efficiency_5d},
    "olec_132_operating_efficiency_21d": {"inputs": ['revenue', 'cor', 'sga', 'rnd'], "func": olec_132_operating_efficiency_21d},
    "olec_133_operating_efficiency_63d": {"inputs": ['revenue', 'cor', 'sga', 'rnd'], "func": olec_133_operating_efficiency_63d},
    "olec_134_operating_efficiency_126d": {"inputs": ['revenue', 'cor', 'sga', 'rnd'], "func": olec_134_operating_efficiency_126d},
    "olec_135_operating_efficiency_252d": {"inputs": ['revenue', 'cor', 'sga', 'rnd'], "func": olec_135_operating_efficiency_252d},
    "olec_136_ni_growth_accel_5d": {"inputs": ['netinc'], "func": olec_136_ni_growth_accel_5d},
    "olec_137_ni_growth_accel_21d": {"inputs": ['netinc'], "func": olec_137_ni_growth_accel_21d},
    "olec_138_ni_growth_accel_63d": {"inputs": ['netinc'], "func": olec_138_ni_growth_accel_63d},
    "olec_139_ni_growth_accel_126d": {"inputs": ['netinc'], "func": olec_139_ni_growth_accel_126d},
    "olec_140_ni_growth_accel_252d": {"inputs": ['netinc'], "func": olec_140_ni_growth_accel_252d},
    "olec_141_ebit_growth_accel_5d": {"inputs": ['ebit'], "func": olec_141_ebit_growth_accel_5d},
    "olec_142_ebit_growth_accel_21d": {"inputs": ['ebit'], "func": olec_142_ebit_growth_accel_21d},
    "olec_143_ebit_growth_accel_63d": {"inputs": ['ebit'], "func": olec_143_ebit_growth_accel_63d},
    "olec_144_ebit_growth_accel_126d": {"inputs": ['ebit'], "func": olec_144_ebit_growth_accel_126d},
    "olec_145_ebit_growth_accel_252d": {"inputs": ['ebit'], "func": olec_145_ebit_growth_accel_252d},
    "olec_146_rev_growth_accel_5d": {"inputs": ['revenue'], "func": olec_146_rev_growth_accel_5d},
    "olec_147_rev_growth_accel_21d": {"inputs": ['revenue'], "func": olec_147_rev_growth_accel_21d},
    "olec_148_rev_growth_accel_63d": {"inputs": ['revenue'], "func": olec_148_rev_growth_accel_63d},
    "olec_149_rev_growth_accel_126d": {"inputs": ['revenue'], "func": olec_149_rev_growth_accel_126d},
    "olec_150_rev_growth_accel_252d": {"inputs": ['revenue'], "func": olec_150_rev_growth_accel_252d},
}
