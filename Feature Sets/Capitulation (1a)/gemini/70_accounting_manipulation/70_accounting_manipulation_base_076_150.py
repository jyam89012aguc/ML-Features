"""
70_accounting_manipulation — Base Features 076-150
Domain: Beneish M-score proxies, Accruals/Assets
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

def acmn_076_ocf_ni_divergence_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_076_ocf_ni_divergence_5d"""
    return ((_safe_div(ocf, netinc)).diff(252)).shift(5)

def acmn_077_ocf_ni_divergence_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_077_ocf_ni_divergence_21d"""
    return ((_safe_div(ocf, netinc)).diff(252)).shift(21)

def acmn_078_ocf_ni_divergence_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_078_ocf_ni_divergence_63d"""
    return ((_safe_div(ocf, netinc)).diff(252)).shift(63)

def acmn_079_ocf_ni_divergence_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_079_ocf_ni_divergence_126d"""
    return ((_safe_div(ocf, netinc)).diff(252)).shift(126)

def acmn_080_ocf_ni_divergence_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """acmn_080_ocf_ni_divergence_252d"""
    return ((_safe_div(ocf, netinc)).diff(252)).shift(252)

def acmn_081_receivables_g_5d(receivables: pd.Series) -> pd.Series:
    """acmn_081_receivables_g_5d"""
    return (receivables.pct_change(252)).shift(5)

def acmn_082_receivables_g_21d(receivables: pd.Series) -> pd.Series:
    """acmn_082_receivables_g_21d"""
    return (receivables.pct_change(252)).shift(21)

def acmn_083_receivables_g_63d(receivables: pd.Series) -> pd.Series:
    """acmn_083_receivables_g_63d"""
    return (receivables.pct_change(252)).shift(63)

def acmn_084_receivables_g_126d(receivables: pd.Series) -> pd.Series:
    """acmn_084_receivables_g_126d"""
    return (receivables.pct_change(252)).shift(126)

def acmn_085_receivables_g_252d(receivables: pd.Series) -> pd.Series:
    """acmn_085_receivables_g_252d"""
    return (receivables.pct_change(252)).shift(252)

def acmn_086_inventory_g_5d(inventory: pd.Series) -> pd.Series:
    """acmn_086_inventory_g_5d"""
    return (inventory.pct_change(252)).shift(5)

def acmn_087_inventory_g_21d(inventory: pd.Series) -> pd.Series:
    """acmn_087_inventory_g_21d"""
    return (inventory.pct_change(252)).shift(21)

def acmn_088_inventory_g_63d(inventory: pd.Series) -> pd.Series:
    """acmn_088_inventory_g_63d"""
    return (inventory.pct_change(252)).shift(63)

def acmn_089_inventory_g_126d(inventory: pd.Series) -> pd.Series:
    """acmn_089_inventory_g_126d"""
    return (inventory.pct_change(252)).shift(126)

def acmn_090_inventory_g_252d(inventory: pd.Series) -> pd.Series:
    """acmn_090_inventory_g_252d"""
    return (inventory.pct_change(252)).shift(252)

def acmn_091_revenue_g_5d(revenue: pd.Series) -> pd.Series:
    """acmn_091_revenue_g_5d"""
    return (revenue.pct_change(252)).shift(5)

def acmn_092_revenue_g_21d(revenue: pd.Series) -> pd.Series:
    """acmn_092_revenue_g_21d"""
    return (revenue.pct_change(252)).shift(21)

def acmn_093_revenue_g_63d(revenue: pd.Series) -> pd.Series:
    """acmn_093_revenue_g_63d"""
    return (revenue.pct_change(252)).shift(63)

def acmn_094_revenue_g_126d(revenue: pd.Series) -> pd.Series:
    """acmn_094_revenue_g_126d"""
    return (revenue.pct_change(252)).shift(126)

def acmn_095_revenue_g_252d(revenue: pd.Series) -> pd.Series:
    """acmn_095_revenue_g_252d"""
    return (revenue.pct_change(252)).shift(252)

def acmn_096_cor_g_5d(cor: pd.Series) -> pd.Series:
    """acmn_096_cor_g_5d"""
    return (cor.pct_change(252)).shift(5)

def acmn_097_cor_g_21d(cor: pd.Series) -> pd.Series:
    """acmn_097_cor_g_21d"""
    return (cor.pct_change(252)).shift(21)

def acmn_098_cor_g_63d(cor: pd.Series) -> pd.Series:
    """acmn_098_cor_g_63d"""
    return (cor.pct_change(252)).shift(63)

def acmn_099_cor_g_126d(cor: pd.Series) -> pd.Series:
    """acmn_099_cor_g_126d"""
    return (cor.pct_change(252)).shift(126)

def acmn_100_cor_g_252d(cor: pd.Series) -> pd.Series:
    """acmn_100_cor_g_252d"""
    return (cor.pct_change(252)).shift(252)

def acmn_101_excess_accruals_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_101_excess_accruals_5d"""
    return (_safe_div(netinc - ocf, assets) - _rolling_mean(_safe_div(netinc - ocf, assets), 1260)).shift(5)

def acmn_102_excess_accruals_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_102_excess_accruals_21d"""
    return (_safe_div(netinc - ocf, assets) - _rolling_mean(_safe_div(netinc - ocf, assets), 1260)).shift(21)

def acmn_103_excess_accruals_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_103_excess_accruals_63d"""
    return (_safe_div(netinc - ocf, assets) - _rolling_mean(_safe_div(netinc - ocf, assets), 1260)).shift(63)

def acmn_104_excess_accruals_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_104_excess_accruals_126d"""
    return (_safe_div(netinc - ocf, assets) - _rolling_mean(_safe_div(netinc - ocf, assets), 1260)).shift(126)

def acmn_105_excess_accruals_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """acmn_105_excess_accruals_252d"""
    return (_safe_div(netinc - ocf, assets) - _rolling_mean(_safe_div(netinc - ocf, assets), 1260)).shift(252)

def acmn_106_sales_manipulation_index_5d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_106_sales_manipulation_index_5d"""
    return (_safe_div(receivables.pct_change(252), revenue.pct_change(252))).shift(5)

def acmn_107_sales_manipulation_index_21d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_107_sales_manipulation_index_21d"""
    return (_safe_div(receivables.pct_change(252), revenue.pct_change(252))).shift(21)

def acmn_108_sales_manipulation_index_63d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_108_sales_manipulation_index_63d"""
    return (_safe_div(receivables.pct_change(252), revenue.pct_change(252))).shift(63)

def acmn_109_sales_manipulation_index_126d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_109_sales_manipulation_index_126d"""
    return (_safe_div(receivables.pct_change(252), revenue.pct_change(252))).shift(126)

def acmn_110_sales_manipulation_index_252d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_110_sales_manipulation_index_252d"""
    return (_safe_div(receivables.pct_change(252), revenue.pct_change(252))).shift(252)

def acmn_111_cost_manipulation_index_5d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_111_cost_manipulation_index_5d"""
    return (_safe_div(inventory.pct_change(252), cor.pct_change(252))).shift(5)

def acmn_112_cost_manipulation_index_21d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_112_cost_manipulation_index_21d"""
    return (_safe_div(inventory.pct_change(252), cor.pct_change(252))).shift(21)

def acmn_113_cost_manipulation_index_63d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_113_cost_manipulation_index_63d"""
    return (_safe_div(inventory.pct_change(252), cor.pct_change(252))).shift(63)

def acmn_114_cost_manipulation_index_126d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_114_cost_manipulation_index_126d"""
    return (_safe_div(inventory.pct_change(252), cor.pct_change(252))).shift(126)

def acmn_115_cost_manipulation_index_252d(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """acmn_115_cost_manipulation_index_252d"""
    return (_safe_div(inventory.pct_change(252), cor.pct_change(252))).shift(252)

def acmn_116_depreciation_manipulation_5d(ppnent: pd.Series) -> pd.Series:
    """acmn_116_depreciation_manipulation_5d"""
    return ((_safe_div(depamor, ppnent)).diff(252)).shift(5)

def acmn_117_depreciation_manipulation_21d(ppnent: pd.Series) -> pd.Series:
    """acmn_117_depreciation_manipulation_21d"""
    return ((_safe_div(depamor, ppnent)).diff(252)).shift(21)

def acmn_118_depreciation_manipulation_63d(ppnent: pd.Series) -> pd.Series:
    """acmn_118_depreciation_manipulation_63d"""
    return ((_safe_div(depamor, ppnent)).diff(252)).shift(63)

def acmn_119_depreciation_manipulation_126d(ppnent: pd.Series) -> pd.Series:
    """acmn_119_depreciation_manipulation_126d"""
    return ((_safe_div(depamor, ppnent)).diff(252)).shift(126)

def acmn_120_depreciation_manipulation_252d(ppnent: pd.Series) -> pd.Series:
    """acmn_120_depreciation_manipulation_252d"""
    return ((_safe_div(depamor, ppnent)).diff(252)).shift(252)

def acmn_121_tax_manipulation_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """acmn_121_tax_manipulation_5d"""
    return ((_safe_div(taxexp, ebt)).diff(252)).shift(5)

def acmn_122_tax_manipulation_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """acmn_122_tax_manipulation_21d"""
    return ((_safe_div(taxexp, ebt)).diff(252)).shift(21)

def acmn_123_tax_manipulation_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """acmn_123_tax_manipulation_63d"""
    return ((_safe_div(taxexp, ebt)).diff(252)).shift(63)

def acmn_124_tax_manipulation_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """acmn_124_tax_manipulation_126d"""
    return ((_safe_div(taxexp, ebt)).diff(252)).shift(126)

def acmn_125_tax_manipulation_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """acmn_125_tax_manipulation_252d"""
    return ((_safe_div(taxexp, ebt)).diff(252)).shift(252)

def acmn_126_off_bs_proxy_5d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """acmn_126_off_bs_proxy_5d"""
    return (_safe_div(assets, equity)).shift(5)

def acmn_127_off_bs_proxy_21d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """acmn_127_off_bs_proxy_21d"""
    return (_safe_div(assets, equity)).shift(21)

def acmn_128_off_bs_proxy_63d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """acmn_128_off_bs_proxy_63d"""
    return (_safe_div(assets, equity)).shift(63)

def acmn_129_off_bs_proxy_126d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """acmn_129_off_bs_proxy_126d"""
    return (_safe_div(assets, equity)).shift(126)

def acmn_130_off_bs_proxy_252d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """acmn_130_off_bs_proxy_252d"""
    return (_safe_div(assets, equity)).shift(252)

def acmn_131_intangible_g_5d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_131_intangible_g_5d"""
    return ((assets - ppnent - currentassets).pct_change(252)).shift(5)

def acmn_132_intangible_g_21d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_132_intangible_g_21d"""
    return ((assets - ppnent - currentassets).pct_change(252)).shift(21)

def acmn_133_intangible_g_63d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_133_intangible_g_63d"""
    return ((assets - ppnent - currentassets).pct_change(252)).shift(63)

def acmn_134_intangible_g_126d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_134_intangible_g_126d"""
    return ((assets - ppnent - currentassets).pct_change(252)).shift(126)

def acmn_135_intangible_g_252d(assets: pd.Series, ppnent: pd.Series, currentassets: pd.Series) -> pd.Series:
    """acmn_135_intangible_g_252d"""
    return ((assets - ppnent - currentassets).pct_change(252)).shift(252)

def acmn_136_working_cap_manipulation_5d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """acmn_136_working_cap_manipulation_5d"""
    return (workingcapital.diff(252) / revenue).shift(5)

def acmn_137_working_cap_manipulation_21d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """acmn_137_working_cap_manipulation_21d"""
    return (workingcapital.diff(252) / revenue).shift(21)

def acmn_138_working_cap_manipulation_63d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """acmn_138_working_cap_manipulation_63d"""
    return (workingcapital.diff(252) / revenue).shift(63)

def acmn_139_working_cap_manipulation_126d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """acmn_139_working_cap_manipulation_126d"""
    return (workingcapital.diff(252) / revenue).shift(126)

def acmn_140_working_cap_manipulation_252d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """acmn_140_working_cap_manipulation_252d"""
    return (workingcapital.diff(252) / revenue).shift(252)

def acmn_141_capitalization_index_5d(capex: pd.Series) -> pd.Series:
    """acmn_141_capitalization_index_5d"""
    return (_safe_div(capex, depamor)).shift(5)

def acmn_142_capitalization_index_21d(capex: pd.Series) -> pd.Series:
    """acmn_142_capitalization_index_21d"""
    return (_safe_div(capex, depamor)).shift(21)

def acmn_143_capitalization_index_63d(capex: pd.Series) -> pd.Series:
    """acmn_143_capitalization_index_63d"""
    return (_safe_div(capex, depamor)).shift(63)

def acmn_144_capitalization_index_126d(capex: pd.Series) -> pd.Series:
    """acmn_144_capitalization_index_126d"""
    return (_safe_div(capex, depamor)).shift(126)

def acmn_145_capitalization_index_252d(capex: pd.Series) -> pd.Series:
    """acmn_145_capitalization_index_252d"""
    return (_safe_div(capex, depamor)).shift(252)

def acmn_146_m_score_velocity_5d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_146_m_score_velocity_5d"""
    return ((_safe_div(receivables, revenue)).diff(63)).shift(5)

def acmn_147_m_score_velocity_21d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_147_m_score_velocity_21d"""
    return ((_safe_div(receivables, revenue)).diff(63)).shift(21)

def acmn_148_m_score_velocity_63d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_148_m_score_velocity_63d"""
    return ((_safe_div(receivables, revenue)).diff(63)).shift(63)

def acmn_149_m_score_velocity_126d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_149_m_score_velocity_126d"""
    return ((_safe_div(receivables, revenue)).diff(63)).shift(126)

def acmn_150_m_score_velocity_252d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """acmn_150_m_score_velocity_252d"""
    return ((_safe_div(receivables, revenue)).diff(63)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V70_REGISTRY = {
    "acmn_076_ocf_ni_divergence_5d": {"inputs": ['netinc', 'ocf'], "func": acmn_076_ocf_ni_divergence_5d},
    "acmn_077_ocf_ni_divergence_21d": {"inputs": ['netinc', 'ocf'], "func": acmn_077_ocf_ni_divergence_21d},
    "acmn_078_ocf_ni_divergence_63d": {"inputs": ['netinc', 'ocf'], "func": acmn_078_ocf_ni_divergence_63d},
    "acmn_079_ocf_ni_divergence_126d": {"inputs": ['netinc', 'ocf'], "func": acmn_079_ocf_ni_divergence_126d},
    "acmn_080_ocf_ni_divergence_252d": {"inputs": ['netinc', 'ocf'], "func": acmn_080_ocf_ni_divergence_252d},
    "acmn_081_receivables_g_5d": {"inputs": ['receivables'], "func": acmn_081_receivables_g_5d},
    "acmn_082_receivables_g_21d": {"inputs": ['receivables'], "func": acmn_082_receivables_g_21d},
    "acmn_083_receivables_g_63d": {"inputs": ['receivables'], "func": acmn_083_receivables_g_63d},
    "acmn_084_receivables_g_126d": {"inputs": ['receivables'], "func": acmn_084_receivables_g_126d},
    "acmn_085_receivables_g_252d": {"inputs": ['receivables'], "func": acmn_085_receivables_g_252d},
    "acmn_086_inventory_g_5d": {"inputs": ['inventory'], "func": acmn_086_inventory_g_5d},
    "acmn_087_inventory_g_21d": {"inputs": ['inventory'], "func": acmn_087_inventory_g_21d},
    "acmn_088_inventory_g_63d": {"inputs": ['inventory'], "func": acmn_088_inventory_g_63d},
    "acmn_089_inventory_g_126d": {"inputs": ['inventory'], "func": acmn_089_inventory_g_126d},
    "acmn_090_inventory_g_252d": {"inputs": ['inventory'], "func": acmn_090_inventory_g_252d},
    "acmn_091_revenue_g_5d": {"inputs": ['revenue'], "func": acmn_091_revenue_g_5d},
    "acmn_092_revenue_g_21d": {"inputs": ['revenue'], "func": acmn_092_revenue_g_21d},
    "acmn_093_revenue_g_63d": {"inputs": ['revenue'], "func": acmn_093_revenue_g_63d},
    "acmn_094_revenue_g_126d": {"inputs": ['revenue'], "func": acmn_094_revenue_g_126d},
    "acmn_095_revenue_g_252d": {"inputs": ['revenue'], "func": acmn_095_revenue_g_252d},
    "acmn_096_cor_g_5d": {"inputs": ['cor'], "func": acmn_096_cor_g_5d},
    "acmn_097_cor_g_21d": {"inputs": ['cor'], "func": acmn_097_cor_g_21d},
    "acmn_098_cor_g_63d": {"inputs": ['cor'], "func": acmn_098_cor_g_63d},
    "acmn_099_cor_g_126d": {"inputs": ['cor'], "func": acmn_099_cor_g_126d},
    "acmn_100_cor_g_252d": {"inputs": ['cor'], "func": acmn_100_cor_g_252d},
    "acmn_101_excess_accruals_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_101_excess_accruals_5d},
    "acmn_102_excess_accruals_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_102_excess_accruals_21d},
    "acmn_103_excess_accruals_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_103_excess_accruals_63d},
    "acmn_104_excess_accruals_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_104_excess_accruals_126d},
    "acmn_105_excess_accruals_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": acmn_105_excess_accruals_252d},
    "acmn_106_sales_manipulation_index_5d": {"inputs": ['revenue', 'receivables'], "func": acmn_106_sales_manipulation_index_5d},
    "acmn_107_sales_manipulation_index_21d": {"inputs": ['revenue', 'receivables'], "func": acmn_107_sales_manipulation_index_21d},
    "acmn_108_sales_manipulation_index_63d": {"inputs": ['revenue', 'receivables'], "func": acmn_108_sales_manipulation_index_63d},
    "acmn_109_sales_manipulation_index_126d": {"inputs": ['revenue', 'receivables'], "func": acmn_109_sales_manipulation_index_126d},
    "acmn_110_sales_manipulation_index_252d": {"inputs": ['revenue', 'receivables'], "func": acmn_110_sales_manipulation_index_252d},
    "acmn_111_cost_manipulation_index_5d": {"inputs": ['cor', 'inventory'], "func": acmn_111_cost_manipulation_index_5d},
    "acmn_112_cost_manipulation_index_21d": {"inputs": ['cor', 'inventory'], "func": acmn_112_cost_manipulation_index_21d},
    "acmn_113_cost_manipulation_index_63d": {"inputs": ['cor', 'inventory'], "func": acmn_113_cost_manipulation_index_63d},
    "acmn_114_cost_manipulation_index_126d": {"inputs": ['cor', 'inventory'], "func": acmn_114_cost_manipulation_index_126d},
    "acmn_115_cost_manipulation_index_252d": {"inputs": ['cor', 'inventory'], "func": acmn_115_cost_manipulation_index_252d},
    "acmn_116_depreciation_manipulation_5d": {"inputs": ['ppnent'], "func": acmn_116_depreciation_manipulation_5d},
    "acmn_117_depreciation_manipulation_21d": {"inputs": ['ppnent'], "func": acmn_117_depreciation_manipulation_21d},
    "acmn_118_depreciation_manipulation_63d": {"inputs": ['ppnent'], "func": acmn_118_depreciation_manipulation_63d},
    "acmn_119_depreciation_manipulation_126d": {"inputs": ['ppnent'], "func": acmn_119_depreciation_manipulation_126d},
    "acmn_120_depreciation_manipulation_252d": {"inputs": ['ppnent'], "func": acmn_120_depreciation_manipulation_252d},
    "acmn_121_tax_manipulation_5d": {"inputs": ['taxexp', 'ebt'], "func": acmn_121_tax_manipulation_5d},
    "acmn_122_tax_manipulation_21d": {"inputs": ['taxexp', 'ebt'], "func": acmn_122_tax_manipulation_21d},
    "acmn_123_tax_manipulation_63d": {"inputs": ['taxexp', 'ebt'], "func": acmn_123_tax_manipulation_63d},
    "acmn_124_tax_manipulation_126d": {"inputs": ['taxexp', 'ebt'], "func": acmn_124_tax_manipulation_126d},
    "acmn_125_tax_manipulation_252d": {"inputs": ['taxexp', 'ebt'], "func": acmn_125_tax_manipulation_252d},
    "acmn_126_off_bs_proxy_5d": {"inputs": ['assets', 'equity'], "func": acmn_126_off_bs_proxy_5d},
    "acmn_127_off_bs_proxy_21d": {"inputs": ['assets', 'equity'], "func": acmn_127_off_bs_proxy_21d},
    "acmn_128_off_bs_proxy_63d": {"inputs": ['assets', 'equity'], "func": acmn_128_off_bs_proxy_63d},
    "acmn_129_off_bs_proxy_126d": {"inputs": ['assets', 'equity'], "func": acmn_129_off_bs_proxy_126d},
    "acmn_130_off_bs_proxy_252d": {"inputs": ['assets', 'equity'], "func": acmn_130_off_bs_proxy_252d},
    "acmn_131_intangible_g_5d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_131_intangible_g_5d},
    "acmn_132_intangible_g_21d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_132_intangible_g_21d},
    "acmn_133_intangible_g_63d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_133_intangible_g_63d},
    "acmn_134_intangible_g_126d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_134_intangible_g_126d},
    "acmn_135_intangible_g_252d": {"inputs": ['assets', 'ppnent', 'currentassets'], "func": acmn_135_intangible_g_252d},
    "acmn_136_working_cap_manipulation_5d": {"inputs": ['revenue', 'workingcapital'], "func": acmn_136_working_cap_manipulation_5d},
    "acmn_137_working_cap_manipulation_21d": {"inputs": ['revenue', 'workingcapital'], "func": acmn_137_working_cap_manipulation_21d},
    "acmn_138_working_cap_manipulation_63d": {"inputs": ['revenue', 'workingcapital'], "func": acmn_138_working_cap_manipulation_63d},
    "acmn_139_working_cap_manipulation_126d": {"inputs": ['revenue', 'workingcapital'], "func": acmn_139_working_cap_manipulation_126d},
    "acmn_140_working_cap_manipulation_252d": {"inputs": ['revenue', 'workingcapital'], "func": acmn_140_working_cap_manipulation_252d},
    "acmn_141_capitalization_index_5d": {"inputs": ['capex'], "func": acmn_141_capitalization_index_5d},
    "acmn_142_capitalization_index_21d": {"inputs": ['capex'], "func": acmn_142_capitalization_index_21d},
    "acmn_143_capitalization_index_63d": {"inputs": ['capex'], "func": acmn_143_capitalization_index_63d},
    "acmn_144_capitalization_index_126d": {"inputs": ['capex'], "func": acmn_144_capitalization_index_126d},
    "acmn_145_capitalization_index_252d": {"inputs": ['capex'], "func": acmn_145_capitalization_index_252d},
    "acmn_146_m_score_velocity_5d": {"inputs": ['revenue', 'receivables'], "func": acmn_146_m_score_velocity_5d},
    "acmn_147_m_score_velocity_21d": {"inputs": ['revenue', 'receivables'], "func": acmn_147_m_score_velocity_21d},
    "acmn_148_m_score_velocity_63d": {"inputs": ['revenue', 'receivables'], "func": acmn_148_m_score_velocity_63d},
    "acmn_149_m_score_velocity_126d": {"inputs": ['revenue', 'receivables'], "func": acmn_149_m_score_velocity_126d},
    "acmn_150_m_score_velocity_252d": {"inputs": ['revenue', 'receivables'], "func": acmn_150_m_score_velocity_252d},
}
