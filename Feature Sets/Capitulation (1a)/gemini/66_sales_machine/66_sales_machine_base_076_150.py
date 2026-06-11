"""
66_sales_machine — Base Features 076-150
Domain: Rev / (SGA + R&D)
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

def slsm_076_sga_acceleration_5d(sga: pd.Series) -> pd.Series:
    """slsm_076_sga_acceleration_5d"""
    return (sga.pct_change(252).diff(63)).shift(5)

def slsm_077_sga_acceleration_21d(sga: pd.Series) -> pd.Series:
    """slsm_077_sga_acceleration_21d"""
    return (sga.pct_change(252).diff(63)).shift(21)

def slsm_078_sga_acceleration_63d(sga: pd.Series) -> pd.Series:
    """slsm_078_sga_acceleration_63d"""
    return (sga.pct_change(252).diff(63)).shift(63)

def slsm_079_sga_acceleration_126d(sga: pd.Series) -> pd.Series:
    """slsm_079_sga_acceleration_126d"""
    return (sga.pct_change(252).diff(63)).shift(126)

def slsm_080_sga_acceleration_252d(sga: pd.Series) -> pd.Series:
    """slsm_080_sga_acceleration_252d"""
    return (sga.pct_change(252).diff(63)).shift(252)

def slsm_081_rev_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """slsm_081_rev_acceleration_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def slsm_082_rev_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """slsm_082_rev_acceleration_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def slsm_083_rev_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """slsm_083_rev_acceleration_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def slsm_084_rev_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """slsm_084_rev_acceleration_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def slsm_085_rev_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """slsm_085_rev_acceleration_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def slsm_086_sales_leverage_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_086_sales_leverage_5d"""
    return (_safe_div(revenue.pct_change(252), sga.pct_change(252))).shift(5)

def slsm_087_sales_leverage_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_087_sales_leverage_21d"""
    return (_safe_div(revenue.pct_change(252), sga.pct_change(252))).shift(21)

def slsm_088_sales_leverage_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_088_sales_leverage_63d"""
    return (_safe_div(revenue.pct_change(252), sga.pct_change(252))).shift(63)

def slsm_089_sales_leverage_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_089_sales_leverage_126d"""
    return (_safe_div(revenue.pct_change(252), sga.pct_change(252))).shift(126)

def slsm_090_sales_leverage_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_090_sales_leverage_252d"""
    return (_safe_div(revenue.pct_change(252), sga.pct_change(252))).shift(252)

def slsm_091_rnd_leverage_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_091_rnd_leverage_5d"""
    return (_safe_div(revenue.pct_change(252), rnd.pct_change(252))).shift(5)

def slsm_092_rnd_leverage_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_092_rnd_leverage_21d"""
    return (_safe_div(revenue.pct_change(252), rnd.pct_change(252))).shift(21)

def slsm_093_rnd_leverage_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_093_rnd_leverage_63d"""
    return (_safe_div(revenue.pct_change(252), rnd.pct_change(252))).shift(63)

def slsm_094_rnd_leverage_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_094_rnd_leverage_126d"""
    return (_safe_div(revenue.pct_change(252), rnd.pct_change(252))).shift(126)

def slsm_095_rnd_leverage_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_095_rnd_leverage_252d"""
    return (_safe_div(revenue.pct_change(252), rnd.pct_change(252))).shift(252)

def slsm_096_marketing_eff_proxy_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_096_marketing_eff_proxy_5d"""
    return _safe_div(revenue.diff(252), sga.shift(252))

def slsm_097_marketing_eff_proxy_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_097_marketing_eff_proxy_21d"""
    return _safe_div(revenue.diff(252), sga.shift(252))

def slsm_098_marketing_eff_proxy_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_098_marketing_eff_proxy_63d"""
    return _safe_div(revenue.diff(252), sga.shift(252))

def slsm_099_marketing_eff_proxy_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_099_marketing_eff_proxy_126d"""
    return _safe_div(revenue.diff(252), sga.shift(252))

def slsm_100_marketing_eff_proxy_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_100_marketing_eff_proxy_252d"""
    return _safe_div(revenue.diff(252), sga.shift(252))

def slsm_101_innovation_eff_proxy_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_101_innovation_eff_proxy_5d"""
    return _safe_div(revenue.diff(504), rnd.shift(504))

def slsm_102_innovation_eff_proxy_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_102_innovation_eff_proxy_21d"""
    return _safe_div(revenue.diff(504), rnd.shift(504))

def slsm_103_innovation_eff_proxy_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_103_innovation_eff_proxy_63d"""
    return _safe_div(revenue.diff(504), rnd.shift(504))

def slsm_104_innovation_eff_proxy_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_104_innovation_eff_proxy_126d"""
    return _safe_div(revenue.diff(504), rnd.shift(504))

def slsm_105_innovation_eff_proxy_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_105_innovation_eff_proxy_252d"""
    return _safe_div(revenue.diff(504), rnd.shift(504))

def slsm_106_sga_m_chg_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_106_sga_m_chg_5d"""
    return ((_safe_div(sga, revenue)).diff(252)).shift(5)

def slsm_107_sga_m_chg_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_107_sga_m_chg_21d"""
    return ((_safe_div(sga, revenue)).diff(252)).shift(21)

def slsm_108_sga_m_chg_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_108_sga_m_chg_63d"""
    return ((_safe_div(sga, revenue)).diff(252)).shift(63)

def slsm_109_sga_m_chg_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_109_sga_m_chg_126d"""
    return ((_safe_div(sga, revenue)).diff(252)).shift(126)

def slsm_110_sga_m_chg_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_110_sga_m_chg_252d"""
    return ((_safe_div(sga, revenue)).diff(252)).shift(252)

def slsm_111_rnd_m_chg_5d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_111_rnd_m_chg_5d"""
    return ((_safe_div(rnd, revenue)).diff(252)).shift(5)

def slsm_112_rnd_m_chg_21d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_112_rnd_m_chg_21d"""
    return ((_safe_div(rnd, revenue)).diff(252)).shift(21)

def slsm_113_rnd_m_chg_63d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_113_rnd_m_chg_63d"""
    return ((_safe_div(rnd, revenue)).diff(252)).shift(63)

def slsm_114_rnd_m_chg_126d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_114_rnd_m_chg_126d"""
    return ((_safe_div(rnd, revenue)).diff(252)).shift(126)

def slsm_115_rnd_m_chg_252d(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_115_rnd_m_chg_252d"""
    return ((_safe_div(rnd, revenue)).diff(252)).shift(252)

def slsm_116_total_op_eff_5d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_116_total_op_eff_5d"""
    return (_safe_div(revenue, sga + rnd)).shift(5)

def slsm_117_total_op_eff_21d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_117_total_op_eff_21d"""
    return (_safe_div(revenue, sga + rnd)).shift(21)

def slsm_118_total_op_eff_63d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_118_total_op_eff_63d"""
    return (_safe_div(revenue, sga + rnd)).shift(63)

def slsm_119_total_op_eff_126d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_119_total_op_eff_126d"""
    return (_safe_div(revenue, sga + rnd)).shift(126)

def slsm_120_total_op_eff_252d(revenue: pd.Series, sga: pd.Series, rnd: pd.Series) -> pd.Series:
    """slsm_120_total_op_eff_252d"""
    return (_safe_div(revenue, sga + rnd)).shift(252)

def slsm_121_sga_persistence_5d(sga: pd.Series) -> pd.Series:
    """slsm_121_sga_persistence_5d"""
    return (_safe_div(sga, sga.rolling(252).mean())).shift(5)

def slsm_122_sga_persistence_21d(sga: pd.Series) -> pd.Series:
    """slsm_122_sga_persistence_21d"""
    return (_safe_div(sga, sga.rolling(252).mean())).shift(21)

def slsm_123_sga_persistence_63d(sga: pd.Series) -> pd.Series:
    """slsm_123_sga_persistence_63d"""
    return (_safe_div(sga, sga.rolling(252).mean())).shift(63)

def slsm_124_sga_persistence_126d(sga: pd.Series) -> pd.Series:
    """slsm_124_sga_persistence_126d"""
    return (_safe_div(sga, sga.rolling(252).mean())).shift(126)

def slsm_125_sga_persistence_252d(sga: pd.Series) -> pd.Series:
    """slsm_125_sga_persistence_252d"""
    return (_safe_div(sga, sga.rolling(252).mean())).shift(252)

def slsm_126_rnd_persistence_5d(rnd: pd.Series) -> pd.Series:
    """slsm_126_rnd_persistence_5d"""
    return (_safe_div(rnd, rnd.rolling(252).mean())).shift(5)

def slsm_127_rnd_persistence_21d(rnd: pd.Series) -> pd.Series:
    """slsm_127_rnd_persistence_21d"""
    return (_safe_div(rnd, rnd.rolling(252).mean())).shift(21)

def slsm_128_rnd_persistence_63d(rnd: pd.Series) -> pd.Series:
    """slsm_128_rnd_persistence_63d"""
    return (_safe_div(rnd, rnd.rolling(252).mean())).shift(63)

def slsm_129_rnd_persistence_126d(rnd: pd.Series) -> pd.Series:
    """slsm_129_rnd_persistence_126d"""
    return (_safe_div(rnd, rnd.rolling(252).mean())).shift(126)

def slsm_130_rnd_persistence_252d(rnd: pd.Series) -> pd.Series:
    """slsm_130_rnd_persistence_252d"""
    return (_safe_div(rnd, rnd.rolling(252).mean())).shift(252)

def slsm_131_efficiency_decay_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_131_efficiency_decay_5d"""
    return ((_safe_div(revenue, sga)).diff(504)).shift(5)

def slsm_132_efficiency_decay_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_132_efficiency_decay_21d"""
    return ((_safe_div(revenue, sga)).diff(504)).shift(21)

def slsm_133_efficiency_decay_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_133_efficiency_decay_63d"""
    return ((_safe_div(revenue, sga)).diff(504)).shift(63)

def slsm_134_efficiency_decay_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_134_efficiency_decay_126d"""
    return ((_safe_div(revenue, sga)).diff(504)).shift(126)

def slsm_135_efficiency_decay_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_135_efficiency_decay_252d"""
    return ((_safe_div(revenue, sga)).diff(504)).shift(252)

def slsm_136_new_rev_per_sga_5d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_136_new_rev_per_sga_5d"""
    return (_safe_div(revenue.diff(63), sga.rolling(63).sum())).shift(5)

def slsm_137_new_rev_per_sga_21d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_137_new_rev_per_sga_21d"""
    return (_safe_div(revenue.diff(63), sga.rolling(63).sum())).shift(21)

def slsm_138_new_rev_per_sga_63d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_138_new_rev_per_sga_63d"""
    return (_safe_div(revenue.diff(63), sga.rolling(63).sum())).shift(63)

def slsm_139_new_rev_per_sga_126d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_139_new_rev_per_sga_126d"""
    return (_safe_div(revenue.diff(63), sga.rolling(63).sum())).shift(126)

def slsm_140_new_rev_per_sga_252d(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """slsm_140_new_rev_per_sga_252d"""
    return (_safe_div(revenue.diff(63), sga.rolling(63).sum())).shift(252)

def slsm_141_sga_yield_5d(sga: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_141_sga_yield_5d"""
    return (_safe_div(sga, marketcap)).shift(5)

def slsm_142_sga_yield_21d(sga: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_142_sga_yield_21d"""
    return (_safe_div(sga, marketcap)).shift(21)

def slsm_143_sga_yield_63d(sga: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_143_sga_yield_63d"""
    return (_safe_div(sga, marketcap)).shift(63)

def slsm_144_sga_yield_126d(sga: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_144_sga_yield_126d"""
    return (_safe_div(sga, marketcap)).shift(126)

def slsm_145_sga_yield_252d(sga: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_145_sga_yield_252d"""
    return (_safe_div(sga, marketcap)).shift(252)

def slsm_146_rnd_yield_5d(rnd: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_146_rnd_yield_5d"""
    return (_safe_div(rnd, marketcap)).shift(5)

def slsm_147_rnd_yield_21d(rnd: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_147_rnd_yield_21d"""
    return (_safe_div(rnd, marketcap)).shift(21)

def slsm_148_rnd_yield_63d(rnd: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_148_rnd_yield_63d"""
    return (_safe_div(rnd, marketcap)).shift(63)

def slsm_149_rnd_yield_126d(rnd: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_149_rnd_yield_126d"""
    return (_safe_div(rnd, marketcap)).shift(126)

def slsm_150_rnd_yield_252d(rnd: pd.Series, marketcap: pd.Series) -> pd.Series:
    """slsm_150_rnd_yield_252d"""
    return (_safe_div(rnd, marketcap)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V66_REGISTRY = {
    "slsm_076_sga_acceleration_5d": {"inputs": ['sga'], "func": slsm_076_sga_acceleration_5d},
    "slsm_077_sga_acceleration_21d": {"inputs": ['sga'], "func": slsm_077_sga_acceleration_21d},
    "slsm_078_sga_acceleration_63d": {"inputs": ['sga'], "func": slsm_078_sga_acceleration_63d},
    "slsm_079_sga_acceleration_126d": {"inputs": ['sga'], "func": slsm_079_sga_acceleration_126d},
    "slsm_080_sga_acceleration_252d": {"inputs": ['sga'], "func": slsm_080_sga_acceleration_252d},
    "slsm_081_rev_acceleration_5d": {"inputs": ['revenue'], "func": slsm_081_rev_acceleration_5d},
    "slsm_082_rev_acceleration_21d": {"inputs": ['revenue'], "func": slsm_082_rev_acceleration_21d},
    "slsm_083_rev_acceleration_63d": {"inputs": ['revenue'], "func": slsm_083_rev_acceleration_63d},
    "slsm_084_rev_acceleration_126d": {"inputs": ['revenue'], "func": slsm_084_rev_acceleration_126d},
    "slsm_085_rev_acceleration_252d": {"inputs": ['revenue'], "func": slsm_085_rev_acceleration_252d},
    "slsm_086_sales_leverage_5d": {"inputs": ['revenue', 'sga'], "func": slsm_086_sales_leverage_5d},
    "slsm_087_sales_leverage_21d": {"inputs": ['revenue', 'sga'], "func": slsm_087_sales_leverage_21d},
    "slsm_088_sales_leverage_63d": {"inputs": ['revenue', 'sga'], "func": slsm_088_sales_leverage_63d},
    "slsm_089_sales_leverage_126d": {"inputs": ['revenue', 'sga'], "func": slsm_089_sales_leverage_126d},
    "slsm_090_sales_leverage_252d": {"inputs": ['revenue', 'sga'], "func": slsm_090_sales_leverage_252d},
    "slsm_091_rnd_leverage_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_091_rnd_leverage_5d},
    "slsm_092_rnd_leverage_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_092_rnd_leverage_21d},
    "slsm_093_rnd_leverage_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_093_rnd_leverage_63d},
    "slsm_094_rnd_leverage_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_094_rnd_leverage_126d},
    "slsm_095_rnd_leverage_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_095_rnd_leverage_252d},
    "slsm_096_marketing_eff_proxy_5d": {"inputs": ['revenue', 'sga'], "func": slsm_096_marketing_eff_proxy_5d},
    "slsm_097_marketing_eff_proxy_21d": {"inputs": ['revenue', 'sga'], "func": slsm_097_marketing_eff_proxy_21d},
    "slsm_098_marketing_eff_proxy_63d": {"inputs": ['revenue', 'sga'], "func": slsm_098_marketing_eff_proxy_63d},
    "slsm_099_marketing_eff_proxy_126d": {"inputs": ['revenue', 'sga'], "func": slsm_099_marketing_eff_proxy_126d},
    "slsm_100_marketing_eff_proxy_252d": {"inputs": ['revenue', 'sga'], "func": slsm_100_marketing_eff_proxy_252d},
    "slsm_101_innovation_eff_proxy_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_101_innovation_eff_proxy_5d},
    "slsm_102_innovation_eff_proxy_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_102_innovation_eff_proxy_21d},
    "slsm_103_innovation_eff_proxy_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_103_innovation_eff_proxy_63d},
    "slsm_104_innovation_eff_proxy_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_104_innovation_eff_proxy_126d},
    "slsm_105_innovation_eff_proxy_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_105_innovation_eff_proxy_252d},
    "slsm_106_sga_m_chg_5d": {"inputs": ['revenue', 'sga'], "func": slsm_106_sga_m_chg_5d},
    "slsm_107_sga_m_chg_21d": {"inputs": ['revenue', 'sga'], "func": slsm_107_sga_m_chg_21d},
    "slsm_108_sga_m_chg_63d": {"inputs": ['revenue', 'sga'], "func": slsm_108_sga_m_chg_63d},
    "slsm_109_sga_m_chg_126d": {"inputs": ['revenue', 'sga'], "func": slsm_109_sga_m_chg_126d},
    "slsm_110_sga_m_chg_252d": {"inputs": ['revenue', 'sga'], "func": slsm_110_sga_m_chg_252d},
    "slsm_111_rnd_m_chg_5d": {"inputs": ['revenue', 'rnd'], "func": slsm_111_rnd_m_chg_5d},
    "slsm_112_rnd_m_chg_21d": {"inputs": ['revenue', 'rnd'], "func": slsm_112_rnd_m_chg_21d},
    "slsm_113_rnd_m_chg_63d": {"inputs": ['revenue', 'rnd'], "func": slsm_113_rnd_m_chg_63d},
    "slsm_114_rnd_m_chg_126d": {"inputs": ['revenue', 'rnd'], "func": slsm_114_rnd_m_chg_126d},
    "slsm_115_rnd_m_chg_252d": {"inputs": ['revenue', 'rnd'], "func": slsm_115_rnd_m_chg_252d},
    "slsm_116_total_op_eff_5d": {"inputs": ['revenue', 'sga', 'rnd'], "func": slsm_116_total_op_eff_5d},
    "slsm_117_total_op_eff_21d": {"inputs": ['revenue', 'sga', 'rnd'], "func": slsm_117_total_op_eff_21d},
    "slsm_118_total_op_eff_63d": {"inputs": ['revenue', 'sga', 'rnd'], "func": slsm_118_total_op_eff_63d},
    "slsm_119_total_op_eff_126d": {"inputs": ['revenue', 'sga', 'rnd'], "func": slsm_119_total_op_eff_126d},
    "slsm_120_total_op_eff_252d": {"inputs": ['revenue', 'sga', 'rnd'], "func": slsm_120_total_op_eff_252d},
    "slsm_121_sga_persistence_5d": {"inputs": ['sga'], "func": slsm_121_sga_persistence_5d},
    "slsm_122_sga_persistence_21d": {"inputs": ['sga'], "func": slsm_122_sga_persistence_21d},
    "slsm_123_sga_persistence_63d": {"inputs": ['sga'], "func": slsm_123_sga_persistence_63d},
    "slsm_124_sga_persistence_126d": {"inputs": ['sga'], "func": slsm_124_sga_persistence_126d},
    "slsm_125_sga_persistence_252d": {"inputs": ['sga'], "func": slsm_125_sga_persistence_252d},
    "slsm_126_rnd_persistence_5d": {"inputs": ['rnd'], "func": slsm_126_rnd_persistence_5d},
    "slsm_127_rnd_persistence_21d": {"inputs": ['rnd'], "func": slsm_127_rnd_persistence_21d},
    "slsm_128_rnd_persistence_63d": {"inputs": ['rnd'], "func": slsm_128_rnd_persistence_63d},
    "slsm_129_rnd_persistence_126d": {"inputs": ['rnd'], "func": slsm_129_rnd_persistence_126d},
    "slsm_130_rnd_persistence_252d": {"inputs": ['rnd'], "func": slsm_130_rnd_persistence_252d},
    "slsm_131_efficiency_decay_5d": {"inputs": ['revenue', 'sga'], "func": slsm_131_efficiency_decay_5d},
    "slsm_132_efficiency_decay_21d": {"inputs": ['revenue', 'sga'], "func": slsm_132_efficiency_decay_21d},
    "slsm_133_efficiency_decay_63d": {"inputs": ['revenue', 'sga'], "func": slsm_133_efficiency_decay_63d},
    "slsm_134_efficiency_decay_126d": {"inputs": ['revenue', 'sga'], "func": slsm_134_efficiency_decay_126d},
    "slsm_135_efficiency_decay_252d": {"inputs": ['revenue', 'sga'], "func": slsm_135_efficiency_decay_252d},
    "slsm_136_new_rev_per_sga_5d": {"inputs": ['revenue', 'sga'], "func": slsm_136_new_rev_per_sga_5d},
    "slsm_137_new_rev_per_sga_21d": {"inputs": ['revenue', 'sga'], "func": slsm_137_new_rev_per_sga_21d},
    "slsm_138_new_rev_per_sga_63d": {"inputs": ['revenue', 'sga'], "func": slsm_138_new_rev_per_sga_63d},
    "slsm_139_new_rev_per_sga_126d": {"inputs": ['revenue', 'sga'], "func": slsm_139_new_rev_per_sga_126d},
    "slsm_140_new_rev_per_sga_252d": {"inputs": ['revenue', 'sga'], "func": slsm_140_new_rev_per_sga_252d},
    "slsm_141_sga_yield_5d": {"inputs": ['sga', 'marketcap'], "func": slsm_141_sga_yield_5d},
    "slsm_142_sga_yield_21d": {"inputs": ['sga', 'marketcap'], "func": slsm_142_sga_yield_21d},
    "slsm_143_sga_yield_63d": {"inputs": ['sga', 'marketcap'], "func": slsm_143_sga_yield_63d},
    "slsm_144_sga_yield_126d": {"inputs": ['sga', 'marketcap'], "func": slsm_144_sga_yield_126d},
    "slsm_145_sga_yield_252d": {"inputs": ['sga', 'marketcap'], "func": slsm_145_sga_yield_252d},
    "slsm_146_rnd_yield_5d": {"inputs": ['rnd', 'marketcap'], "func": slsm_146_rnd_yield_5d},
    "slsm_147_rnd_yield_21d": {"inputs": ['rnd', 'marketcap'], "func": slsm_147_rnd_yield_21d},
    "slsm_148_rnd_yield_63d": {"inputs": ['rnd', 'marketcap'], "func": slsm_148_rnd_yield_63d},
    "slsm_149_rnd_yield_126d": {"inputs": ['rnd', 'marketcap'], "func": slsm_149_rnd_yield_126d},
    "slsm_150_rnd_yield_252d": {"inputs": ['rnd', 'marketcap'], "func": slsm_150_rnd_yield_252d},
}
