"""
63_cash_earnings_divergence — Base Features 076-150
Domain: OCF vs NetInc (Accrual tracking)
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

def cedv_076_ocf_yield_5d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_076_ocf_yield_5d"""
    return (_safe_div(ocf, marketcap)).shift(5)

def cedv_077_ocf_yield_21d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_077_ocf_yield_21d"""
    return (_safe_div(ocf, marketcap)).shift(21)

def cedv_078_ocf_yield_63d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_078_ocf_yield_63d"""
    return (_safe_div(ocf, marketcap)).shift(63)

def cedv_079_ocf_yield_126d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_079_ocf_yield_126d"""
    return (_safe_div(ocf, marketcap)).shift(126)

def cedv_080_ocf_yield_252d(ocf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_080_ocf_yield_252d"""
    return (_safe_div(ocf, marketcap)).shift(252)

def cedv_081_fcf_yield_5d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_081_fcf_yield_5d"""
    return (_safe_div(fcf, marketcap)).shift(5)

def cedv_082_fcf_yield_21d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_082_fcf_yield_21d"""
    return (_safe_div(fcf, marketcap)).shift(21)

def cedv_083_fcf_yield_63d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_083_fcf_yield_63d"""
    return (_safe_div(fcf, marketcap)).shift(63)

def cedv_084_fcf_yield_126d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_084_fcf_yield_126d"""
    return (_safe_div(fcf, marketcap)).shift(126)

def cedv_085_fcf_yield_252d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_085_fcf_yield_252d"""
    return (_safe_div(fcf, marketcap)).shift(252)

def cedv_086_ni_yield_5d(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_086_ni_yield_5d"""
    return (_safe_div(netinc, marketcap)).shift(5)

def cedv_087_ni_yield_21d(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_087_ni_yield_21d"""
    return (_safe_div(netinc, marketcap)).shift(21)

def cedv_088_ni_yield_63d(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_088_ni_yield_63d"""
    return (_safe_div(netinc, marketcap)).shift(63)

def cedv_089_ni_yield_126d(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_089_ni_yield_126d"""
    return (_safe_div(netinc, marketcap)).shift(126)

def cedv_090_ni_yield_252d(netinc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_090_ni_yield_252d"""
    return (_safe_div(netinc, marketcap)).shift(252)

def cedv_091_working_cap_rev_5d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_091_working_cap_rev_5d"""
    return (_safe_div(workingcapital, revenue)).shift(5)

def cedv_092_working_cap_rev_21d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_092_working_cap_rev_21d"""
    return (_safe_div(workingcapital, revenue)).shift(21)

def cedv_093_working_cap_rev_63d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_093_working_cap_rev_63d"""
    return (_safe_div(workingcapital, revenue)).shift(63)

def cedv_094_working_cap_rev_126d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_094_working_cap_rev_126d"""
    return (_safe_div(workingcapital, revenue)).shift(126)

def cedv_095_working_cap_rev_252d(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """cedv_095_working_cap_rev_252d"""
    return (_safe_div(workingcapital, revenue)).shift(252)

def cedv_096_inv_ocf_5d(ocf: pd.Series, inventory: pd.Series) -> pd.Series:
    """cedv_096_inv_ocf_5d"""
    return (_safe_div(inventory, ocf)).shift(5)

def cedv_097_inv_ocf_21d(ocf: pd.Series, inventory: pd.Series) -> pd.Series:
    """cedv_097_inv_ocf_21d"""
    return (_safe_div(inventory, ocf)).shift(21)

def cedv_098_inv_ocf_63d(ocf: pd.Series, inventory: pd.Series) -> pd.Series:
    """cedv_098_inv_ocf_63d"""
    return (_safe_div(inventory, ocf)).shift(63)

def cedv_099_inv_ocf_126d(ocf: pd.Series, inventory: pd.Series) -> pd.Series:
    """cedv_099_inv_ocf_126d"""
    return (_safe_div(inventory, ocf)).shift(126)

def cedv_100_inv_ocf_252d(ocf: pd.Series, inventory: pd.Series) -> pd.Series:
    """cedv_100_inv_ocf_252d"""
    return (_safe_div(inventory, ocf)).shift(252)

def cedv_101_rec_ocf_5d(ocf: pd.Series, receivables: pd.Series) -> pd.Series:
    """cedv_101_rec_ocf_5d"""
    return (_safe_div(receivables, ocf)).shift(5)

def cedv_102_rec_ocf_21d(ocf: pd.Series, receivables: pd.Series) -> pd.Series:
    """cedv_102_rec_ocf_21d"""
    return (_safe_div(receivables, ocf)).shift(21)

def cedv_103_rec_ocf_63d(ocf: pd.Series, receivables: pd.Series) -> pd.Series:
    """cedv_103_rec_ocf_63d"""
    return (_safe_div(receivables, ocf)).shift(63)

def cedv_104_rec_ocf_126d(ocf: pd.Series, receivables: pd.Series) -> pd.Series:
    """cedv_104_rec_ocf_126d"""
    return (_safe_div(receivables, ocf)).shift(126)

def cedv_105_rec_ocf_252d(ocf: pd.Series, receivables: pd.Series) -> pd.Series:
    """cedv_105_rec_ocf_252d"""
    return (_safe_div(receivables, ocf)).shift(252)

def cedv_106_pay_ocf_5d(ocf: pd.Series, payables: pd.Series) -> pd.Series:
    """cedv_106_pay_ocf_5d"""
    return (_safe_div(payables, ocf)).shift(5)

def cedv_107_pay_ocf_21d(ocf: pd.Series, payables: pd.Series) -> pd.Series:
    """cedv_107_pay_ocf_21d"""
    return (_safe_div(payables, ocf)).shift(21)

def cedv_108_pay_ocf_63d(ocf: pd.Series, payables: pd.Series) -> pd.Series:
    """cedv_108_pay_ocf_63d"""
    return (_safe_div(payables, ocf)).shift(63)

def cedv_109_pay_ocf_126d(ocf: pd.Series, payables: pd.Series) -> pd.Series:
    """cedv_109_pay_ocf_126d"""
    return (_safe_div(payables, ocf)).shift(126)

def cedv_110_pay_ocf_252d(ocf: pd.Series, payables: pd.Series) -> pd.Series:
    """cedv_110_pay_ocf_252d"""
    return (_safe_div(payables, ocf)).shift(252)

def cedv_111_accrual_z_5d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_111_accrual_z_5d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(5)

def cedv_112_accrual_z_21d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_112_accrual_z_21d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(21)

def cedv_113_accrual_z_63d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_113_accrual_z_63d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(63)

def cedv_114_accrual_z_126d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_114_accrual_z_126d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(126)

def cedv_115_accrual_z_252d(netinc: pd.Series, ocf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_115_accrual_z_252d"""
    return (_zscore_rolling(_safe_div(netinc - ocf, assets), 1260)).shift(252)

def cedv_116_ocf_persistence_5d(ocf: pd.Series) -> pd.Series:
    """cedv_116_ocf_persistence_5d"""
    return _safe_div(ocf, ocf.shift(252))

def cedv_117_ocf_persistence_21d(ocf: pd.Series) -> pd.Series:
    """cedv_117_ocf_persistence_21d"""
    return _safe_div(ocf, ocf.shift(252))

def cedv_118_ocf_persistence_63d(ocf: pd.Series) -> pd.Series:
    """cedv_118_ocf_persistence_63d"""
    return _safe_div(ocf, ocf.shift(252))

def cedv_119_ocf_persistence_126d(ocf: pd.Series) -> pd.Series:
    """cedv_119_ocf_persistence_126d"""
    return _safe_div(ocf, ocf.shift(252))

def cedv_120_ocf_persistence_252d(ocf: pd.Series) -> pd.Series:
    """cedv_120_ocf_persistence_252d"""
    return _safe_div(ocf, ocf.shift(252))

def cedv_121_fcf_persistence_5d(fcf: pd.Series) -> pd.Series:
    """cedv_121_fcf_persistence_5d"""
    return _safe_div(fcf, fcf.shift(252))

def cedv_122_fcf_persistence_21d(fcf: pd.Series) -> pd.Series:
    """cedv_122_fcf_persistence_21d"""
    return _safe_div(fcf, fcf.shift(252))

def cedv_123_fcf_persistence_63d(fcf: pd.Series) -> pd.Series:
    """cedv_123_fcf_persistence_63d"""
    return _safe_div(fcf, fcf.shift(252))

def cedv_124_fcf_persistence_126d(fcf: pd.Series) -> pd.Series:
    """cedv_124_fcf_persistence_126d"""
    return _safe_div(fcf, fcf.shift(252))

def cedv_125_fcf_persistence_252d(fcf: pd.Series) -> pd.Series:
    """cedv_125_fcf_persistence_252d"""
    return _safe_div(fcf, fcf.shift(252))

def cedv_126_ni_persistence_5d(netinc: pd.Series) -> pd.Series:
    """cedv_126_ni_persistence_5d"""
    return _safe_div(netinc, netinc.shift(252))

def cedv_127_ni_persistence_21d(netinc: pd.Series) -> pd.Series:
    """cedv_127_ni_persistence_21d"""
    return _safe_div(netinc, netinc.shift(252))

def cedv_128_ni_persistence_63d(netinc: pd.Series) -> pd.Series:
    """cedv_128_ni_persistence_63d"""
    return _safe_div(netinc, netinc.shift(252))

def cedv_129_ni_persistence_126d(netinc: pd.Series) -> pd.Series:
    """cedv_129_ni_persistence_126d"""
    return _safe_div(netinc, netinc.shift(252))

def cedv_130_ni_persistence_252d(netinc: pd.Series) -> pd.Series:
    """cedv_130_ni_persistence_252d"""
    return _safe_div(netinc, netinc.shift(252))

def cedv_131_div_persistence_5d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_131_div_persistence_5d"""
    return _safe_div(netinc - ocf, (netinc - ocf).shift(252))

def cedv_132_div_persistence_21d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_132_div_persistence_21d"""
    return _safe_div(netinc - ocf, (netinc - ocf).shift(252))

def cedv_133_div_persistence_63d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_133_div_persistence_63d"""
    return _safe_div(netinc - ocf, (netinc - ocf).shift(252))

def cedv_134_div_persistence_126d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_134_div_persistence_126d"""
    return _safe_div(netinc - ocf, (netinc - ocf).shift(252))

def cedv_135_div_persistence_252d(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """cedv_135_div_persistence_252d"""
    return _safe_div(netinc - ocf, (netinc - ocf).shift(252))

def cedv_136_mc_rev_5d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_136_mc_rev_5d"""
    return (_safe_div(marketcap, revenue)).shift(5)

def cedv_137_mc_rev_21d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_137_mc_rev_21d"""
    return (_safe_div(marketcap, revenue)).shift(21)

def cedv_138_mc_rev_63d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_138_mc_rev_63d"""
    return (_safe_div(marketcap, revenue)).shift(63)

def cedv_139_mc_rev_126d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_139_mc_rev_126d"""
    return (_safe_div(marketcap, revenue)).shift(126)

def cedv_140_mc_rev_252d(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_140_mc_rev_252d"""
    return (_safe_div(marketcap, revenue)).shift(252)

def cedv_141_ev_ocf_5d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_141_ev_ocf_5d"""
    return (_safe_div(marketcap + debtn.fillna(0) - cashnequiv.fillna(0), ocf)).shift(5)

def cedv_142_ev_ocf_21d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_142_ev_ocf_21d"""
    return (_safe_div(marketcap + debtn.fillna(0) - cashnequiv.fillna(0), ocf)).shift(21)

def cedv_143_ev_ocf_63d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_143_ev_ocf_63d"""
    return (_safe_div(marketcap + debtn.fillna(0) - cashnequiv.fillna(0), ocf)).shift(63)

def cedv_144_ev_ocf_126d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_144_ev_ocf_126d"""
    return (_safe_div(marketcap + debtn.fillna(0) - cashnequiv.fillna(0), ocf)).shift(126)

def cedv_145_ev_ocf_252d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, marketcap: pd.Series) -> pd.Series:
    """cedv_145_ev_ocf_252d"""
    return (_safe_div(marketcap + debtn.fillna(0) - cashnequiv.fillna(0), ocf)).shift(252)

def cedv_146_fcf_accrual_rat_5d(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_146_fcf_accrual_rat_5d"""
    return (_safe_div(netinc - fcf, assets)).shift(5)

def cedv_147_fcf_accrual_rat_21d(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_147_fcf_accrual_rat_21d"""
    return (_safe_div(netinc - fcf, assets)).shift(21)

def cedv_148_fcf_accrual_rat_63d(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_148_fcf_accrual_rat_63d"""
    return (_safe_div(netinc - fcf, assets)).shift(63)

def cedv_149_fcf_accrual_rat_126d(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_149_fcf_accrual_rat_126d"""
    return (_safe_div(netinc - fcf, assets)).shift(126)

def cedv_150_fcf_accrual_rat_252d(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """cedv_150_fcf_accrual_rat_252d"""
    return (_safe_div(netinc - fcf, assets)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V63_REGISTRY = {
    "cedv_076_ocf_yield_5d": {"inputs": ['ocf', 'marketcap'], "func": cedv_076_ocf_yield_5d},
    "cedv_077_ocf_yield_21d": {"inputs": ['ocf', 'marketcap'], "func": cedv_077_ocf_yield_21d},
    "cedv_078_ocf_yield_63d": {"inputs": ['ocf', 'marketcap'], "func": cedv_078_ocf_yield_63d},
    "cedv_079_ocf_yield_126d": {"inputs": ['ocf', 'marketcap'], "func": cedv_079_ocf_yield_126d},
    "cedv_080_ocf_yield_252d": {"inputs": ['ocf', 'marketcap'], "func": cedv_080_ocf_yield_252d},
    "cedv_081_fcf_yield_5d": {"inputs": ['fcf', 'marketcap'], "func": cedv_081_fcf_yield_5d},
    "cedv_082_fcf_yield_21d": {"inputs": ['fcf', 'marketcap'], "func": cedv_082_fcf_yield_21d},
    "cedv_083_fcf_yield_63d": {"inputs": ['fcf', 'marketcap'], "func": cedv_083_fcf_yield_63d},
    "cedv_084_fcf_yield_126d": {"inputs": ['fcf', 'marketcap'], "func": cedv_084_fcf_yield_126d},
    "cedv_085_fcf_yield_252d": {"inputs": ['fcf', 'marketcap'], "func": cedv_085_fcf_yield_252d},
    "cedv_086_ni_yield_5d": {"inputs": ['netinc', 'marketcap'], "func": cedv_086_ni_yield_5d},
    "cedv_087_ni_yield_21d": {"inputs": ['netinc', 'marketcap'], "func": cedv_087_ni_yield_21d},
    "cedv_088_ni_yield_63d": {"inputs": ['netinc', 'marketcap'], "func": cedv_088_ni_yield_63d},
    "cedv_089_ni_yield_126d": {"inputs": ['netinc', 'marketcap'], "func": cedv_089_ni_yield_126d},
    "cedv_090_ni_yield_252d": {"inputs": ['netinc', 'marketcap'], "func": cedv_090_ni_yield_252d},
    "cedv_091_working_cap_rev_5d": {"inputs": ['revenue', 'workingcapital'], "func": cedv_091_working_cap_rev_5d},
    "cedv_092_working_cap_rev_21d": {"inputs": ['revenue', 'workingcapital'], "func": cedv_092_working_cap_rev_21d},
    "cedv_093_working_cap_rev_63d": {"inputs": ['revenue', 'workingcapital'], "func": cedv_093_working_cap_rev_63d},
    "cedv_094_working_cap_rev_126d": {"inputs": ['revenue', 'workingcapital'], "func": cedv_094_working_cap_rev_126d},
    "cedv_095_working_cap_rev_252d": {"inputs": ['revenue', 'workingcapital'], "func": cedv_095_working_cap_rev_252d},
    "cedv_096_inv_ocf_5d": {"inputs": ['ocf', 'inventory'], "func": cedv_096_inv_ocf_5d},
    "cedv_097_inv_ocf_21d": {"inputs": ['ocf', 'inventory'], "func": cedv_097_inv_ocf_21d},
    "cedv_098_inv_ocf_63d": {"inputs": ['ocf', 'inventory'], "func": cedv_098_inv_ocf_63d},
    "cedv_099_inv_ocf_126d": {"inputs": ['ocf', 'inventory'], "func": cedv_099_inv_ocf_126d},
    "cedv_100_inv_ocf_252d": {"inputs": ['ocf', 'inventory'], "func": cedv_100_inv_ocf_252d},
    "cedv_101_rec_ocf_5d": {"inputs": ['ocf', 'receivables'], "func": cedv_101_rec_ocf_5d},
    "cedv_102_rec_ocf_21d": {"inputs": ['ocf', 'receivables'], "func": cedv_102_rec_ocf_21d},
    "cedv_103_rec_ocf_63d": {"inputs": ['ocf', 'receivables'], "func": cedv_103_rec_ocf_63d},
    "cedv_104_rec_ocf_126d": {"inputs": ['ocf', 'receivables'], "func": cedv_104_rec_ocf_126d},
    "cedv_105_rec_ocf_252d": {"inputs": ['ocf', 'receivables'], "func": cedv_105_rec_ocf_252d},
    "cedv_106_pay_ocf_5d": {"inputs": ['ocf', 'payables'], "func": cedv_106_pay_ocf_5d},
    "cedv_107_pay_ocf_21d": {"inputs": ['ocf', 'payables'], "func": cedv_107_pay_ocf_21d},
    "cedv_108_pay_ocf_63d": {"inputs": ['ocf', 'payables'], "func": cedv_108_pay_ocf_63d},
    "cedv_109_pay_ocf_126d": {"inputs": ['ocf', 'payables'], "func": cedv_109_pay_ocf_126d},
    "cedv_110_pay_ocf_252d": {"inputs": ['ocf', 'payables'], "func": cedv_110_pay_ocf_252d},
    "cedv_111_accrual_z_5d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_111_accrual_z_5d},
    "cedv_112_accrual_z_21d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_112_accrual_z_21d},
    "cedv_113_accrual_z_63d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_113_accrual_z_63d},
    "cedv_114_accrual_z_126d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_114_accrual_z_126d},
    "cedv_115_accrual_z_252d": {"inputs": ['netinc', 'ocf', 'assets'], "func": cedv_115_accrual_z_252d},
    "cedv_116_ocf_persistence_5d": {"inputs": ['ocf'], "func": cedv_116_ocf_persistence_5d},
    "cedv_117_ocf_persistence_21d": {"inputs": ['ocf'], "func": cedv_117_ocf_persistence_21d},
    "cedv_118_ocf_persistence_63d": {"inputs": ['ocf'], "func": cedv_118_ocf_persistence_63d},
    "cedv_119_ocf_persistence_126d": {"inputs": ['ocf'], "func": cedv_119_ocf_persistence_126d},
    "cedv_120_ocf_persistence_252d": {"inputs": ['ocf'], "func": cedv_120_ocf_persistence_252d},
    "cedv_121_fcf_persistence_5d": {"inputs": ['fcf'], "func": cedv_121_fcf_persistence_5d},
    "cedv_122_fcf_persistence_21d": {"inputs": ['fcf'], "func": cedv_122_fcf_persistence_21d},
    "cedv_123_fcf_persistence_63d": {"inputs": ['fcf'], "func": cedv_123_fcf_persistence_63d},
    "cedv_124_fcf_persistence_126d": {"inputs": ['fcf'], "func": cedv_124_fcf_persistence_126d},
    "cedv_125_fcf_persistence_252d": {"inputs": ['fcf'], "func": cedv_125_fcf_persistence_252d},
    "cedv_126_ni_persistence_5d": {"inputs": ['netinc'], "func": cedv_126_ni_persistence_5d},
    "cedv_127_ni_persistence_21d": {"inputs": ['netinc'], "func": cedv_127_ni_persistence_21d},
    "cedv_128_ni_persistence_63d": {"inputs": ['netinc'], "func": cedv_128_ni_persistence_63d},
    "cedv_129_ni_persistence_126d": {"inputs": ['netinc'], "func": cedv_129_ni_persistence_126d},
    "cedv_130_ni_persistence_252d": {"inputs": ['netinc'], "func": cedv_130_ni_persistence_252d},
    "cedv_131_div_persistence_5d": {"inputs": ['netinc', 'ocf'], "func": cedv_131_div_persistence_5d},
    "cedv_132_div_persistence_21d": {"inputs": ['netinc', 'ocf'], "func": cedv_132_div_persistence_21d},
    "cedv_133_div_persistence_63d": {"inputs": ['netinc', 'ocf'], "func": cedv_133_div_persistence_63d},
    "cedv_134_div_persistence_126d": {"inputs": ['netinc', 'ocf'], "func": cedv_134_div_persistence_126d},
    "cedv_135_div_persistence_252d": {"inputs": ['netinc', 'ocf'], "func": cedv_135_div_persistence_252d},
    "cedv_136_mc_rev_5d": {"inputs": ['revenue', 'marketcap'], "func": cedv_136_mc_rev_5d},
    "cedv_137_mc_rev_21d": {"inputs": ['revenue', 'marketcap'], "func": cedv_137_mc_rev_21d},
    "cedv_138_mc_rev_63d": {"inputs": ['revenue', 'marketcap'], "func": cedv_138_mc_rev_63d},
    "cedv_139_mc_rev_126d": {"inputs": ['revenue', 'marketcap'], "func": cedv_139_mc_rev_126d},
    "cedv_140_mc_rev_252d": {"inputs": ['revenue', 'marketcap'], "func": cedv_140_mc_rev_252d},
    "cedv_141_ev_ocf_5d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'marketcap'], "func": cedv_141_ev_ocf_5d},
    "cedv_142_ev_ocf_21d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'marketcap'], "func": cedv_142_ev_ocf_21d},
    "cedv_143_ev_ocf_63d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'marketcap'], "func": cedv_143_ev_ocf_63d},
    "cedv_144_ev_ocf_126d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'marketcap'], "func": cedv_144_ev_ocf_126d},
    "cedv_145_ev_ocf_252d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'marketcap'], "func": cedv_145_ev_ocf_252d},
    "cedv_146_fcf_accrual_rat_5d": {"inputs": ['netinc', 'fcf', 'assets'], "func": cedv_146_fcf_accrual_rat_5d},
    "cedv_147_fcf_accrual_rat_21d": {"inputs": ['netinc', 'fcf', 'assets'], "func": cedv_147_fcf_accrual_rat_21d},
    "cedv_148_fcf_accrual_rat_63d": {"inputs": ['netinc', 'fcf', 'assets'], "func": cedv_148_fcf_accrual_rat_63d},
    "cedv_149_fcf_accrual_rat_126d": {"inputs": ['netinc', 'fcf', 'assets'], "func": cedv_149_fcf_accrual_rat_126d},
    "cedv_150_fcf_accrual_rat_252d": {"inputs": ['netinc', 'fcf', 'assets'], "func": cedv_150_fcf_accrual_rat_252d},
}
