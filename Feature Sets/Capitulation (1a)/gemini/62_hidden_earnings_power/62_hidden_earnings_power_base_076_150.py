"""
62_hidden_earnings_power — Base Features 076-150
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

def herp_076_hidden_m_5d(revenue: pd.Series, ebitda: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_076_hidden_m_5d"""
    return ((_safe_div(ebitda - taxexp, revenue))).shift(5)

def herp_077_hidden_m_21d(revenue: pd.Series, ebitda: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_077_hidden_m_21d"""
    return ((_safe_div(ebitda - taxexp, revenue))).shift(21)

def herp_078_hidden_m_63d(revenue: pd.Series, ebitda: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_078_hidden_m_63d"""
    return ((_safe_div(ebitda - taxexp, revenue))).shift(63)

def herp_079_hidden_m_126d(revenue: pd.Series, ebitda: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_079_hidden_m_126d"""
    return ((_safe_div(ebitda - taxexp, revenue))).shift(126)

def herp_080_hidden_m_252d(revenue: pd.Series, ebitda: pd.Series, taxexp: pd.Series) -> pd.Series:
    """herp_080_hidden_m_252d"""
    return ((_safe_div(ebitda - taxexp, revenue))).shift(252)

def herp_081_earnings_quality_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """herp_081_earnings_quality_5d"""
    return (_safe_div(ocf, netinc)).shift(5)

def herp_082_earnings_quality_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """herp_082_earnings_quality_21d"""
    return (_safe_div(ocf, netinc)).shift(21)

def herp_083_earnings_quality_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """herp_083_earnings_quality_63d"""
    return (_safe_div(ocf, netinc)).shift(63)

def herp_084_earnings_quality_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """herp_084_earnings_quality_126d"""
    return (_safe_div(ocf, netinc)).shift(126)

def herp_085_earnings_quality_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """herp_085_earnings_quality_252d"""
    return (_safe_div(ocf, netinc)).shift(252)

def herp_086_accrual_rat_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_086_accrual_rat_5d"""
    return (_safe_div(netinc - ocf, assets)).shift(5)

def herp_087_accrual_rat_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_087_accrual_rat_21d"""
    return (_safe_div(netinc - ocf, assets)).shift(21)

def herp_088_accrual_rat_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_088_accrual_rat_63d"""
    return (_safe_div(netinc - ocf, assets)).shift(63)

def herp_089_accrual_rat_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_089_accrual_rat_126d"""
    return (_safe_div(netinc - ocf, assets)).shift(126)

def herp_090_accrual_rat_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_090_accrual_rat_252d"""
    return (_safe_div(netinc - ocf, assets)).shift(252)

def herp_091_sga_g_5d(sga: pd.Series) -> pd.Series:
    """herp_091_sga_g_5d"""
    return (sga.pct_change(252)).shift(5)

def herp_092_sga_g_21d(sga: pd.Series) -> pd.Series:
    """herp_092_sga_g_21d"""
    return (sga.pct_change(252)).shift(21)

def herp_093_sga_g_63d(sga: pd.Series) -> pd.Series:
    """herp_093_sga_g_63d"""
    return (sga.pct_change(252)).shift(63)

def herp_094_sga_g_126d(sga: pd.Series) -> pd.Series:
    """herp_094_sga_g_126d"""
    return (sga.pct_change(252)).shift(126)

def herp_095_sga_g_252d(sga: pd.Series) -> pd.Series:
    """herp_095_sga_g_252d"""
    return (sga.pct_change(252)).shift(252)

def herp_096_rnd_g_5d(rnd: pd.Series) -> pd.Series:
    """herp_096_rnd_g_5d"""
    return (rnd.pct_change(252)).shift(5)

def herp_097_rnd_g_21d(rnd: pd.Series) -> pd.Series:
    """herp_097_rnd_g_21d"""
    return (rnd.pct_change(252)).shift(21)

def herp_098_rnd_g_63d(rnd: pd.Series) -> pd.Series:
    """herp_098_rnd_g_63d"""
    return (rnd.pct_change(252)).shift(63)

def herp_099_rnd_g_126d(rnd: pd.Series) -> pd.Series:
    """herp_099_rnd_g_126d"""
    return (rnd.pct_change(252)).shift(126)

def herp_100_rnd_g_252d(rnd: pd.Series) -> pd.Series:
    """herp_100_rnd_g_252d"""
    return (rnd.pct_change(252)).shift(252)

def herp_101_tax_z_5d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_101_tax_z_5d"""
    return (_zscore_rolling(_safe_div(taxexp, ebt), 1260)).shift(5)

def herp_102_tax_z_21d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_102_tax_z_21d"""
    return (_zscore_rolling(_safe_div(taxexp, ebt), 1260)).shift(21)

def herp_103_tax_z_63d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_103_tax_z_63d"""
    return (_zscore_rolling(_safe_div(taxexp, ebt), 1260)).shift(63)

def herp_104_tax_z_126d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_104_tax_z_126d"""
    return (_zscore_rolling(_safe_div(taxexp, ebt), 1260)).shift(126)

def herp_105_tax_z_252d(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """herp_105_tax_z_252d"""
    return (_zscore_rolling(_safe_div(taxexp, ebt), 1260)).shift(252)

def herp_106_ebit_g_5d(ebit: pd.Series) -> pd.Series:
    """herp_106_ebit_g_5d"""
    return (ebit.pct_change(252)).shift(5)

def herp_107_ebit_g_21d(ebit: pd.Series) -> pd.Series:
    """herp_107_ebit_g_21d"""
    return (ebit.pct_change(252)).shift(21)

def herp_108_ebit_g_63d(ebit: pd.Series) -> pd.Series:
    """herp_108_ebit_g_63d"""
    return (ebit.pct_change(252)).shift(63)

def herp_109_ebit_g_126d(ebit: pd.Series) -> pd.Series:
    """herp_109_ebit_g_126d"""
    return (ebit.pct_change(252)).shift(126)

def herp_110_ebit_g_252d(ebit: pd.Series) -> pd.Series:
    """herp_110_ebit_g_252d"""
    return (ebit.pct_change(252)).shift(252)

def herp_111_ni_g_5d(netinc: pd.Series) -> pd.Series:
    """herp_111_ni_g_5d"""
    return (netinc.pct_change(252)).shift(5)

def herp_112_ni_g_21d(netinc: pd.Series) -> pd.Series:
    """herp_112_ni_g_21d"""
    return (netinc.pct_change(252)).shift(21)

def herp_113_ni_g_63d(netinc: pd.Series) -> pd.Series:
    """herp_113_ni_g_63d"""
    return (netinc.pct_change(252)).shift(63)

def herp_114_ni_g_126d(netinc: pd.Series) -> pd.Series:
    """herp_114_ni_g_126d"""
    return (netinc.pct_change(252)).shift(126)

def herp_115_ni_g_252d(netinc: pd.Series) -> pd.Series:
    """herp_115_ni_g_252d"""
    return (netinc.pct_change(252)).shift(252)

def herp_116_op_leverage_5d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_116_op_leverage_5d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(5)

def herp_117_op_leverage_21d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_117_op_leverage_21d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(21)

def herp_118_op_leverage_63d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_118_op_leverage_63d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(63)

def herp_119_op_leverage_126d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_119_op_leverage_126d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(126)

def herp_120_op_leverage_252d(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """herp_120_op_leverage_252d"""
    return (_safe_div(ebit.pct_change(252), revenue.pct_change(252))).shift(252)

def herp_121_capex_m_5d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """herp_121_capex_m_5d"""
    return (_safe_div(capex, revenue)).shift(5)

def herp_122_capex_m_21d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """herp_122_capex_m_21d"""
    return (_safe_div(capex, revenue)).shift(21)

def herp_123_capex_m_63d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """herp_123_capex_m_63d"""
    return (_safe_div(capex, revenue)).shift(63)

def herp_124_capex_m_126d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """herp_124_capex_m_126d"""
    return (_safe_div(capex, revenue)).shift(126)

def herp_125_capex_m_252d(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """herp_125_capex_m_252d"""
    return (_safe_div(capex, revenue)).shift(252)

def herp_126_asset_util_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_126_asset_util_5d"""
    return (_safe_div(revenue, assets)).shift(5)

def herp_127_asset_util_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_127_asset_util_21d"""
    return (_safe_div(revenue, assets)).shift(21)

def herp_128_asset_util_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_128_asset_util_63d"""
    return (_safe_div(revenue, assets)).shift(63)

def herp_129_asset_util_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_129_asset_util_126d"""
    return (_safe_div(revenue, assets)).shift(126)

def herp_130_asset_util_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """herp_130_asset_util_252d"""
    return (_safe_div(revenue, assets)).shift(252)

def herp_131_inventory_turn_5d(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """herp_131_inventory_turn_5d"""
    return (_safe_div(revenue, inventory)).shift(5)

def herp_132_inventory_turn_21d(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """herp_132_inventory_turn_21d"""
    return (_safe_div(revenue, inventory)).shift(21)

def herp_133_inventory_turn_63d(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """herp_133_inventory_turn_63d"""
    return (_safe_div(revenue, inventory)).shift(63)

def herp_134_inventory_turn_126d(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """herp_134_inventory_turn_126d"""
    return (_safe_div(revenue, inventory)).shift(126)

def herp_135_inventory_turn_252d(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """herp_135_inventory_turn_252d"""
    return (_safe_div(revenue, inventory)).shift(252)

def herp_136_receivables_turn_5d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """herp_136_receivables_turn_5d"""
    return (_safe_div(revenue, receivables)).shift(5)

def herp_137_receivables_turn_21d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """herp_137_receivables_turn_21d"""
    return (_safe_div(revenue, receivables)).shift(21)

def herp_138_receivables_turn_63d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """herp_138_receivables_turn_63d"""
    return (_safe_div(revenue, receivables)).shift(63)

def herp_139_receivables_turn_126d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """herp_139_receivables_turn_126d"""
    return (_safe_div(revenue, receivables)).shift(126)

def herp_140_receivables_turn_252d(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """herp_140_receivables_turn_252d"""
    return (_safe_div(revenue, receivables)).shift(252)

def herp_141_payables_turn_5d(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """herp_141_payables_turn_5d"""
    return (_safe_div(revenue, payables)).shift(5)

def herp_142_payables_turn_21d(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """herp_142_payables_turn_21d"""
    return (_safe_div(revenue, payables)).shift(21)

def herp_143_payables_turn_63d(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """herp_143_payables_turn_63d"""
    return (_safe_div(revenue, payables)).shift(63)

def herp_144_payables_turn_126d(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """herp_144_payables_turn_126d"""
    return (_safe_div(revenue, payables)).shift(126)

def herp_145_payables_turn_252d(revenue: pd.Series, payables: pd.Series) -> pd.Series:
    """herp_145_payables_turn_252d"""
    return (_safe_div(revenue, payables)).shift(252)

def herp_146_working_cap_g_5d(workingcapital: pd.Series) -> pd.Series:
    """herp_146_working_cap_g_5d"""
    return (workingcapital.pct_change(252)).shift(5)

def herp_147_working_cap_g_21d(workingcapital: pd.Series) -> pd.Series:
    """herp_147_working_cap_g_21d"""
    return (workingcapital.pct_change(252)).shift(21)

def herp_148_working_cap_g_63d(workingcapital: pd.Series) -> pd.Series:
    """herp_148_working_cap_g_63d"""
    return (workingcapital.pct_change(252)).shift(63)

def herp_149_working_cap_g_126d(workingcapital: pd.Series) -> pd.Series:
    """herp_149_working_cap_g_126d"""
    return (workingcapital.pct_change(252)).shift(126)

def herp_150_working_cap_g_252d(workingcapital: pd.Series) -> pd.Series:
    """herp_150_working_cap_g_252d"""
    return (workingcapital.pct_change(252)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V62_REGISTRY = {
    "herp_076_hidden_m_5d": {"inputs": ['revenue', 'ebitda', 'taxexp'], "func": herp_076_hidden_m_5d},
    "herp_077_hidden_m_21d": {"inputs": ['revenue', 'ebitda', 'taxexp'], "func": herp_077_hidden_m_21d},
    "herp_078_hidden_m_63d": {"inputs": ['revenue', 'ebitda', 'taxexp'], "func": herp_078_hidden_m_63d},
    "herp_079_hidden_m_126d": {"inputs": ['revenue', 'ebitda', 'taxexp'], "func": herp_079_hidden_m_126d},
    "herp_080_hidden_m_252d": {"inputs": ['revenue', 'ebitda', 'taxexp'], "func": herp_080_hidden_m_252d},
    "herp_081_earnings_quality_5d": {"inputs": ['netinc', 'ocf'], "func": herp_081_earnings_quality_5d},
    "herp_082_earnings_quality_21d": {"inputs": ['netinc', 'ocf'], "func": herp_082_earnings_quality_21d},
    "herp_083_earnings_quality_63d": {"inputs": ['netinc', 'ocf'], "func": herp_083_earnings_quality_63d},
    "herp_084_earnings_quality_126d": {"inputs": ['netinc', 'ocf'], "func": herp_084_earnings_quality_126d},
    "herp_085_earnings_quality_252d": {"inputs": ['netinc', 'ocf'], "func": herp_085_earnings_quality_252d},
    "herp_086_accrual_rat_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": herp_086_accrual_rat_5d},
    "herp_087_accrual_rat_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": herp_087_accrual_rat_21d},
    "herp_088_accrual_rat_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": herp_088_accrual_rat_63d},
    "herp_089_accrual_rat_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": herp_089_accrual_rat_126d},
    "herp_090_accrual_rat_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": herp_090_accrual_rat_252d},
    "herp_091_sga_g_5d": {"inputs": ['sga'], "func": herp_091_sga_g_5d},
    "herp_092_sga_g_21d": {"inputs": ['sga'], "func": herp_092_sga_g_21d},
    "herp_093_sga_g_63d": {"inputs": ['sga'], "func": herp_093_sga_g_63d},
    "herp_094_sga_g_126d": {"inputs": ['sga'], "func": herp_094_sga_g_126d},
    "herp_095_sga_g_252d": {"inputs": ['sga'], "func": herp_095_sga_g_252d},
    "herp_096_rnd_g_5d": {"inputs": ['rnd'], "func": herp_096_rnd_g_5d},
    "herp_097_rnd_g_21d": {"inputs": ['rnd'], "func": herp_097_rnd_g_21d},
    "herp_098_rnd_g_63d": {"inputs": ['rnd'], "func": herp_098_rnd_g_63d},
    "herp_099_rnd_g_126d": {"inputs": ['rnd'], "func": herp_099_rnd_g_126d},
    "herp_100_rnd_g_252d": {"inputs": ['rnd'], "func": herp_100_rnd_g_252d},
    "herp_101_tax_z_5d": {"inputs": ['taxexp', 'ebt'], "func": herp_101_tax_z_5d},
    "herp_102_tax_z_21d": {"inputs": ['taxexp', 'ebt'], "func": herp_102_tax_z_21d},
    "herp_103_tax_z_63d": {"inputs": ['taxexp', 'ebt'], "func": herp_103_tax_z_63d},
    "herp_104_tax_z_126d": {"inputs": ['taxexp', 'ebt'], "func": herp_104_tax_z_126d},
    "herp_105_tax_z_252d": {"inputs": ['taxexp', 'ebt'], "func": herp_105_tax_z_252d},
    "herp_106_ebit_g_5d": {"inputs": ['ebit'], "func": herp_106_ebit_g_5d},
    "herp_107_ebit_g_21d": {"inputs": ['ebit'], "func": herp_107_ebit_g_21d},
    "herp_108_ebit_g_63d": {"inputs": ['ebit'], "func": herp_108_ebit_g_63d},
    "herp_109_ebit_g_126d": {"inputs": ['ebit'], "func": herp_109_ebit_g_126d},
    "herp_110_ebit_g_252d": {"inputs": ['ebit'], "func": herp_110_ebit_g_252d},
    "herp_111_ni_g_5d": {"inputs": ['netinc'], "func": herp_111_ni_g_5d},
    "herp_112_ni_g_21d": {"inputs": ['netinc'], "func": herp_112_ni_g_21d},
    "herp_113_ni_g_63d": {"inputs": ['netinc'], "func": herp_113_ni_g_63d},
    "herp_114_ni_g_126d": {"inputs": ['netinc'], "func": herp_114_ni_g_126d},
    "herp_115_ni_g_252d": {"inputs": ['netinc'], "func": herp_115_ni_g_252d},
    "herp_116_op_leverage_5d": {"inputs": ['revenue', 'ebit'], "func": herp_116_op_leverage_5d},
    "herp_117_op_leverage_21d": {"inputs": ['revenue', 'ebit'], "func": herp_117_op_leverage_21d},
    "herp_118_op_leverage_63d": {"inputs": ['revenue', 'ebit'], "func": herp_118_op_leverage_63d},
    "herp_119_op_leverage_126d": {"inputs": ['revenue', 'ebit'], "func": herp_119_op_leverage_126d},
    "herp_120_op_leverage_252d": {"inputs": ['revenue', 'ebit'], "func": herp_120_op_leverage_252d},
    "herp_121_capex_m_5d": {"inputs": ['revenue', 'capex'], "func": herp_121_capex_m_5d},
    "herp_122_capex_m_21d": {"inputs": ['revenue', 'capex'], "func": herp_122_capex_m_21d},
    "herp_123_capex_m_63d": {"inputs": ['revenue', 'capex'], "func": herp_123_capex_m_63d},
    "herp_124_capex_m_126d": {"inputs": ['revenue', 'capex'], "func": herp_124_capex_m_126d},
    "herp_125_capex_m_252d": {"inputs": ['revenue', 'capex'], "func": herp_125_capex_m_252d},
    "herp_126_asset_util_5d": {"inputs": ['revenue', 'assets'], "func": herp_126_asset_util_5d},
    "herp_127_asset_util_21d": {"inputs": ['revenue', 'assets'], "func": herp_127_asset_util_21d},
    "herp_128_asset_util_63d": {"inputs": ['revenue', 'assets'], "func": herp_128_asset_util_63d},
    "herp_129_asset_util_126d": {"inputs": ['revenue', 'assets'], "func": herp_129_asset_util_126d},
    "herp_130_asset_util_252d": {"inputs": ['revenue', 'assets'], "func": herp_130_asset_util_252d},
    "herp_131_inventory_turn_5d": {"inputs": ['revenue', 'inventory'], "func": herp_131_inventory_turn_5d},
    "herp_132_inventory_turn_21d": {"inputs": ['revenue', 'inventory'], "func": herp_132_inventory_turn_21d},
    "herp_133_inventory_turn_63d": {"inputs": ['revenue', 'inventory'], "func": herp_133_inventory_turn_63d},
    "herp_134_inventory_turn_126d": {"inputs": ['revenue', 'inventory'], "func": herp_134_inventory_turn_126d},
    "herp_135_inventory_turn_252d": {"inputs": ['revenue', 'inventory'], "func": herp_135_inventory_turn_252d},
    "herp_136_receivables_turn_5d": {"inputs": ['revenue', 'receivables'], "func": herp_136_receivables_turn_5d},
    "herp_137_receivables_turn_21d": {"inputs": ['revenue', 'receivables'], "func": herp_137_receivables_turn_21d},
    "herp_138_receivables_turn_63d": {"inputs": ['revenue', 'receivables'], "func": herp_138_receivables_turn_63d},
    "herp_139_receivables_turn_126d": {"inputs": ['revenue', 'receivables'], "func": herp_139_receivables_turn_126d},
    "herp_140_receivables_turn_252d": {"inputs": ['revenue', 'receivables'], "func": herp_140_receivables_turn_252d},
    "herp_141_payables_turn_5d": {"inputs": ['revenue', 'payables'], "func": herp_141_payables_turn_5d},
    "herp_142_payables_turn_21d": {"inputs": ['revenue', 'payables'], "func": herp_142_payables_turn_21d},
    "herp_143_payables_turn_63d": {"inputs": ['revenue', 'payables'], "func": herp_143_payables_turn_63d},
    "herp_144_payables_turn_126d": {"inputs": ['revenue', 'payables'], "func": herp_144_payables_turn_126d},
    "herp_145_payables_turn_252d": {"inputs": ['revenue', 'payables'], "func": herp_145_payables_turn_252d},
    "herp_146_working_cap_g_5d": {"inputs": ['workingcapital'], "func": herp_146_working_cap_g_5d},
    "herp_147_working_cap_g_21d": {"inputs": ['workingcapital'], "func": herp_147_working_cap_g_21d},
    "herp_148_working_cap_g_63d": {"inputs": ['workingcapital'], "func": herp_148_working_cap_g_63d},
    "herp_149_working_cap_g_126d": {"inputs": ['workingcapital'], "func": herp_149_working_cap_g_126d},
    "herp_150_working_cap_g_252d": {"inputs": ['workingcapital'], "func": herp_150_working_cap_g_252d},
}
