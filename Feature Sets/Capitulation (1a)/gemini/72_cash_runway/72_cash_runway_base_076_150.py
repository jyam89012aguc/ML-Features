"""
72_cash_runway — Base Features 076-150
Domain: Cash / Burn rate (OCF negative)
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

def runw_076_cash_burn_velocity_5d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_076_cash_burn_velocity_5d"""
    return ((_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).diff(63)).shift(5)

def runw_077_cash_burn_velocity_21d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_077_cash_burn_velocity_21d"""
    return ((_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).diff(63)).shift(21)

def runw_078_cash_burn_velocity_63d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_078_cash_burn_velocity_63d"""
    return ((_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).diff(63)).shift(63)

def runw_079_cash_burn_velocity_126d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_079_cash_burn_velocity_126d"""
    return ((_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).diff(63)).shift(126)

def runw_080_cash_burn_velocity_252d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_080_cash_burn_velocity_252d"""
    return ((_safe_div(cashnequiv, ocf.clip(upper=-_EPS).abs())).diff(63)).shift(252)

def runw_081_cash_decay_rat_5d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_081_cash_decay_rat_5d"""
    return (cashnequiv.diff(252) / assets).shift(5)

def runw_082_cash_decay_rat_21d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_082_cash_decay_rat_21d"""
    return (cashnequiv.diff(252) / assets).shift(21)

def runw_083_cash_decay_rat_63d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_083_cash_decay_rat_63d"""
    return (cashnequiv.diff(252) / assets).shift(63)

def runw_084_cash_decay_rat_126d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_084_cash_decay_rat_126d"""
    return (cashnequiv.diff(252) / assets).shift(126)

def runw_085_cash_decay_rat_252d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_085_cash_decay_rat_252d"""
    return (cashnequiv.diff(252) / assets).shift(252)

def runw_086_burn_acceleration_5d(ocf: pd.Series) -> pd.Series:
    """runw_086_burn_acceleration_5d"""
    return (ocf.diff(252).diff(63)).shift(5)

def runw_087_burn_acceleration_21d(ocf: pd.Series) -> pd.Series:
    """runw_087_burn_acceleration_21d"""
    return (ocf.diff(252).diff(63)).shift(21)

def runw_088_burn_acceleration_63d(ocf: pd.Series) -> pd.Series:
    """runw_088_burn_acceleration_63d"""
    return (ocf.diff(252).diff(63)).shift(63)

def runw_089_burn_acceleration_126d(ocf: pd.Series) -> pd.Series:
    """runw_089_burn_acceleration_126d"""
    return (ocf.diff(252).diff(63)).shift(126)

def runw_090_burn_acceleration_252d(ocf: pd.Series) -> pd.Series:
    """runw_090_burn_acceleration_252d"""
    return (ocf.diff(252).diff(63)).shift(252)

def runw_091_financing_runway_proxy_5d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_091_financing_runway_proxy_5d"""
    return (_safe_div(cashnequiv + (debtn.fillna(0) + debtc.fillna(0)), ocf.abs())).shift(5)

def runw_092_financing_runway_proxy_21d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_092_financing_runway_proxy_21d"""
    return (_safe_div(cashnequiv + (debtn.fillna(0) + debtc.fillna(0)), ocf.abs())).shift(21)

def runw_093_financing_runway_proxy_63d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_093_financing_runway_proxy_63d"""
    return (_safe_div(cashnequiv + (debtn.fillna(0) + debtc.fillna(0)), ocf.abs())).shift(63)

def runw_094_financing_runway_proxy_126d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_094_financing_runway_proxy_126d"""
    return (_safe_div(cashnequiv + (debtn.fillna(0) + debtc.fillna(0)), ocf.abs())).shift(126)

def runw_095_financing_runway_proxy_252d(ocf: pd.Series, cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_095_financing_runway_proxy_252d"""
    return (_safe_div(cashnequiv + (debtn.fillna(0) + debtc.fillna(0)), ocf.abs())).shift(252)

def runw_096_net_cash_marketcap_5d(cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_096_net_cash_marketcap_5d"""
    return (_safe_div(cashnequiv - (debtn.fillna(0) + debtc.fillna(0)), marketcap)).shift(5)

def runw_097_net_cash_marketcap_21d(cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_097_net_cash_marketcap_21d"""
    return (_safe_div(cashnequiv - (debtn.fillna(0) + debtc.fillna(0)), marketcap)).shift(21)

def runw_098_net_cash_marketcap_63d(cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_098_net_cash_marketcap_63d"""
    return (_safe_div(cashnequiv - (debtn.fillna(0) + debtc.fillna(0)), marketcap)).shift(63)

def runw_099_net_cash_marketcap_126d(cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_099_net_cash_marketcap_126d"""
    return (_safe_div(cashnequiv - (debtn.fillna(0) + debtc.fillna(0)), marketcap)).shift(126)

def runw_100_net_cash_marketcap_252d(cashnequiv: pd.Series, debtn: pd.Series, debtc: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_100_net_cash_marketcap_252d"""
    return (_safe_div(cashnequiv - (debtn.fillna(0) + debtc.fillna(0)), marketcap)).shift(252)

def runw_101_cash_per_share_5d(cashnequiv: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_101_cash_per_share_5d"""
    return (_safe_div(cashnequiv, shareswa)).shift(5)

def runw_102_cash_per_share_21d(cashnequiv: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_102_cash_per_share_21d"""
    return (_safe_div(cashnequiv, shareswa)).shift(21)

def runw_103_cash_per_share_63d(cashnequiv: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_103_cash_per_share_63d"""
    return (_safe_div(cashnequiv, shareswa)).shift(63)

def runw_104_cash_per_share_126d(cashnequiv: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_104_cash_per_share_126d"""
    return (_safe_div(cashnequiv, shareswa)).shift(126)

def runw_105_cash_per_share_252d(cashnequiv: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_105_cash_per_share_252d"""
    return (_safe_div(cashnequiv, shareswa)).shift(252)

def runw_106_burn_per_share_5d(ocf: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_106_burn_per_share_5d"""
    return (_safe_div(ocf, shareswa)).shift(5)

def runw_107_burn_per_share_21d(ocf: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_107_burn_per_share_21d"""
    return (_safe_div(ocf, shareswa)).shift(21)

def runw_108_burn_per_share_63d(ocf: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_108_burn_per_share_63d"""
    return (_safe_div(ocf, shareswa)).shift(63)

def runw_109_burn_per_share_126d(ocf: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_109_burn_per_share_126d"""
    return (_safe_div(ocf, shareswa)).shift(126)

def runw_110_burn_per_share_252d(ocf: pd.Series, shareswa: pd.Series) -> pd.Series:
    """runw_110_burn_per_share_252d"""
    return (_safe_div(ocf, shareswa)).shift(252)

def runw_111_runway_stability_5d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_111_runway_stability_5d"""
    return (_rolling_std(_safe_div(cashnequiv, ocf.abs()), 252)).shift(5)

def runw_112_runway_stability_21d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_112_runway_stability_21d"""
    return (_rolling_std(_safe_div(cashnequiv, ocf.abs()), 252)).shift(21)

def runw_113_runway_stability_63d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_113_runway_stability_63d"""
    return (_rolling_std(_safe_div(cashnequiv, ocf.abs()), 252)).shift(63)

def runw_114_runway_stability_126d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_114_runway_stability_126d"""
    return (_rolling_std(_safe_div(cashnequiv, ocf.abs()), 252)).shift(126)

def runw_115_runway_stability_252d(ocf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_115_runway_stability_252d"""
    return (_rolling_std(_safe_div(cashnequiv, ocf.abs()), 252)).shift(252)

def runw_116_liquidity_acceleration_5d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_116_liquidity_acceleration_5d"""
    return ((_safe_div(cashnequiv, liabs)).diff(63)).shift(5)

def runw_117_liquidity_acceleration_21d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_117_liquidity_acceleration_21d"""
    return ((_safe_div(cashnequiv, liabs)).diff(63)).shift(21)

def runw_118_liquidity_acceleration_63d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_118_liquidity_acceleration_63d"""
    return ((_safe_div(cashnequiv, liabs)).diff(63)).shift(63)

def runw_119_liquidity_acceleration_126d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_119_liquidity_acceleration_126d"""
    return ((_safe_div(cashnequiv, liabs)).diff(63)).shift(126)

def runw_120_liquidity_acceleration_252d(liabs: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """runw_120_liquidity_acceleration_252d"""
    return ((_safe_div(cashnequiv, liabs)).diff(63)).shift(252)

def runw_121_insolvency_proxy_5d(equity: pd.Series) -> pd.Series:
    """runw_121_insolvency_proxy_5d"""
    return ((equity < 0).astype(float)).shift(5)

def runw_122_insolvency_proxy_21d(equity: pd.Series) -> pd.Series:
    """runw_122_insolvency_proxy_21d"""
    return ((equity < 0).astype(float)).shift(21)

def runw_123_insolvency_proxy_63d(equity: pd.Series) -> pd.Series:
    """runw_123_insolvency_proxy_63d"""
    return ((equity < 0).astype(float)).shift(63)

def runw_124_insolvency_proxy_126d(equity: pd.Series) -> pd.Series:
    """runw_124_insolvency_proxy_126d"""
    return ((equity < 0).astype(float)).shift(126)

def runw_125_insolvency_proxy_252d(equity: pd.Series) -> pd.Series:
    """runw_125_insolvency_proxy_252d"""
    return ((equity < 0).astype(float)).shift(252)

def runw_126_bankruptcy_risk_proxy_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """runw_126_bankruptcy_risk_proxy_5d"""
    return (_safe_div(liabs, assets)).shift(5)

def runw_127_bankruptcy_risk_proxy_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """runw_127_bankruptcy_risk_proxy_21d"""
    return (_safe_div(liabs, assets)).shift(21)

def runw_128_bankruptcy_risk_proxy_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """runw_128_bankruptcy_risk_proxy_63d"""
    return (_safe_div(liabs, assets)).shift(63)

def runw_129_bankruptcy_risk_proxy_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """runw_129_bankruptcy_risk_proxy_126d"""
    return (_safe_div(liabs, assets)).shift(126)

def runw_130_bankruptcy_risk_proxy_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """runw_130_bankruptcy_risk_proxy_252d"""
    return (_safe_div(liabs, assets)).shift(252)

def runw_131_cash_reinfusion_proxy_5d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """runw_131_cash_reinfusion_proxy_5d"""
    return (equity.diff(252) / assets).shift(5)

def runw_132_cash_reinfusion_proxy_21d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """runw_132_cash_reinfusion_proxy_21d"""
    return (equity.diff(252) / assets).shift(21)

def runw_133_cash_reinfusion_proxy_63d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """runw_133_cash_reinfusion_proxy_63d"""
    return (equity.diff(252) / assets).shift(63)

def runw_134_cash_reinfusion_proxy_126d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """runw_134_cash_reinfusion_proxy_126d"""
    return (equity.diff(252) / assets).shift(126)

def runw_135_cash_reinfusion_proxy_252d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """runw_135_cash_reinfusion_proxy_252d"""
    return (equity.diff(252) / assets).shift(252)

def runw_136_debt_refinance_risk_5d(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_136_debt_refinance_risk_5d"""
    return (_safe_div(debtc, cashnequiv)).shift(5)

def runw_137_debt_refinance_risk_21d(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_137_debt_refinance_risk_21d"""
    return (_safe_div(debtc, cashnequiv)).shift(21)

def runw_138_debt_refinance_risk_63d(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_138_debt_refinance_risk_63d"""
    return (_safe_div(debtc, cashnequiv)).shift(63)

def runw_139_debt_refinance_risk_126d(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_139_debt_refinance_risk_126d"""
    return (_safe_div(debtc, cashnequiv)).shift(126)

def runw_140_debt_refinance_risk_252d(cashnequiv: pd.Series, debtc: pd.Series) -> pd.Series:
    """runw_140_debt_refinance_risk_252d"""
    return (_safe_div(debtc, cashnequiv)).shift(252)

def runw_141_ocf_interest_cov_5d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """runw_141_ocf_interest_cov_5d"""
    return (_safe_div(ocf, int_exp)).shift(5)

def runw_142_ocf_interest_cov_21d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """runw_142_ocf_interest_cov_21d"""
    return (_safe_div(ocf, int_exp)).shift(21)

def runw_143_ocf_interest_cov_63d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """runw_143_ocf_interest_cov_63d"""
    return (_safe_div(ocf, int_exp)).shift(63)

def runw_144_ocf_interest_cov_126d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """runw_144_ocf_interest_cov_126d"""
    return (_safe_div(ocf, int_exp)).shift(126)

def runw_145_ocf_interest_cov_252d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """runw_145_ocf_interest_cov_252d"""
    return (_safe_div(ocf, int_exp)).shift(252)

def runw_146_fcf_yield_5d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_146_fcf_yield_5d"""
    return (_safe_div(fcf, marketcap)).shift(5)

def runw_147_fcf_yield_21d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_147_fcf_yield_21d"""
    return (_safe_div(fcf, marketcap)).shift(21)

def runw_148_fcf_yield_63d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_148_fcf_yield_63d"""
    return (_safe_div(fcf, marketcap)).shift(63)

def runw_149_fcf_yield_126d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_149_fcf_yield_126d"""
    return (_safe_div(fcf, marketcap)).shift(126)

def runw_150_fcf_yield_252d(fcf: pd.Series, marketcap: pd.Series) -> pd.Series:
    """runw_150_fcf_yield_252d"""
    return (_safe_div(fcf, marketcap)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V72_REGISTRY = {
    "runw_076_cash_burn_velocity_5d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_076_cash_burn_velocity_5d},
    "runw_077_cash_burn_velocity_21d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_077_cash_burn_velocity_21d},
    "runw_078_cash_burn_velocity_63d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_078_cash_burn_velocity_63d},
    "runw_079_cash_burn_velocity_126d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_079_cash_burn_velocity_126d},
    "runw_080_cash_burn_velocity_252d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_080_cash_burn_velocity_252d},
    "runw_081_cash_decay_rat_5d": {"inputs": ['assets', 'cashnequiv'], "func": runw_081_cash_decay_rat_5d},
    "runw_082_cash_decay_rat_21d": {"inputs": ['assets', 'cashnequiv'], "func": runw_082_cash_decay_rat_21d},
    "runw_083_cash_decay_rat_63d": {"inputs": ['assets', 'cashnequiv'], "func": runw_083_cash_decay_rat_63d},
    "runw_084_cash_decay_rat_126d": {"inputs": ['assets', 'cashnequiv'], "func": runw_084_cash_decay_rat_126d},
    "runw_085_cash_decay_rat_252d": {"inputs": ['assets', 'cashnequiv'], "func": runw_085_cash_decay_rat_252d},
    "runw_086_burn_acceleration_5d": {"inputs": ['ocf'], "func": runw_086_burn_acceleration_5d},
    "runw_087_burn_acceleration_21d": {"inputs": ['ocf'], "func": runw_087_burn_acceleration_21d},
    "runw_088_burn_acceleration_63d": {"inputs": ['ocf'], "func": runw_088_burn_acceleration_63d},
    "runw_089_burn_acceleration_126d": {"inputs": ['ocf'], "func": runw_089_burn_acceleration_126d},
    "runw_090_burn_acceleration_252d": {"inputs": ['ocf'], "func": runw_090_burn_acceleration_252d},
    "runw_091_financing_runway_proxy_5d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'debtc'], "func": runw_091_financing_runway_proxy_5d},
    "runw_092_financing_runway_proxy_21d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'debtc'], "func": runw_092_financing_runway_proxy_21d},
    "runw_093_financing_runway_proxy_63d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'debtc'], "func": runw_093_financing_runway_proxy_63d},
    "runw_094_financing_runway_proxy_126d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'debtc'], "func": runw_094_financing_runway_proxy_126d},
    "runw_095_financing_runway_proxy_252d": {"inputs": ['ocf', 'cashnequiv', 'debtn', 'debtc'], "func": runw_095_financing_runway_proxy_252d},
    "runw_096_net_cash_marketcap_5d": {"inputs": ['cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": runw_096_net_cash_marketcap_5d},
    "runw_097_net_cash_marketcap_21d": {"inputs": ['cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": runw_097_net_cash_marketcap_21d},
    "runw_098_net_cash_marketcap_63d": {"inputs": ['cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": runw_098_net_cash_marketcap_63d},
    "runw_099_net_cash_marketcap_126d": {"inputs": ['cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": runw_099_net_cash_marketcap_126d},
    "runw_100_net_cash_marketcap_252d": {"inputs": ['cashnequiv', 'debtn', 'debtc', 'marketcap'], "func": runw_100_net_cash_marketcap_252d},
    "runw_101_cash_per_share_5d": {"inputs": ['cashnequiv', 'shareswa'], "func": runw_101_cash_per_share_5d},
    "runw_102_cash_per_share_21d": {"inputs": ['cashnequiv', 'shareswa'], "func": runw_102_cash_per_share_21d},
    "runw_103_cash_per_share_63d": {"inputs": ['cashnequiv', 'shareswa'], "func": runw_103_cash_per_share_63d},
    "runw_104_cash_per_share_126d": {"inputs": ['cashnequiv', 'shareswa'], "func": runw_104_cash_per_share_126d},
    "runw_105_cash_per_share_252d": {"inputs": ['cashnequiv', 'shareswa'], "func": runw_105_cash_per_share_252d},
    "runw_106_burn_per_share_5d": {"inputs": ['ocf', 'shareswa'], "func": runw_106_burn_per_share_5d},
    "runw_107_burn_per_share_21d": {"inputs": ['ocf', 'shareswa'], "func": runw_107_burn_per_share_21d},
    "runw_108_burn_per_share_63d": {"inputs": ['ocf', 'shareswa'], "func": runw_108_burn_per_share_63d},
    "runw_109_burn_per_share_126d": {"inputs": ['ocf', 'shareswa'], "func": runw_109_burn_per_share_126d},
    "runw_110_burn_per_share_252d": {"inputs": ['ocf', 'shareswa'], "func": runw_110_burn_per_share_252d},
    "runw_111_runway_stability_5d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_111_runway_stability_5d},
    "runw_112_runway_stability_21d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_112_runway_stability_21d},
    "runw_113_runway_stability_63d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_113_runway_stability_63d},
    "runw_114_runway_stability_126d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_114_runway_stability_126d},
    "runw_115_runway_stability_252d": {"inputs": ['ocf', 'cashnequiv'], "func": runw_115_runway_stability_252d},
    "runw_116_liquidity_acceleration_5d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_116_liquidity_acceleration_5d},
    "runw_117_liquidity_acceleration_21d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_117_liquidity_acceleration_21d},
    "runw_118_liquidity_acceleration_63d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_118_liquidity_acceleration_63d},
    "runw_119_liquidity_acceleration_126d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_119_liquidity_acceleration_126d},
    "runw_120_liquidity_acceleration_252d": {"inputs": ['liabs', 'cashnequiv'], "func": runw_120_liquidity_acceleration_252d},
    "runw_121_insolvency_proxy_5d": {"inputs": ['equity'], "func": runw_121_insolvency_proxy_5d},
    "runw_122_insolvency_proxy_21d": {"inputs": ['equity'], "func": runw_122_insolvency_proxy_21d},
    "runw_123_insolvency_proxy_63d": {"inputs": ['equity'], "func": runw_123_insolvency_proxy_63d},
    "runw_124_insolvency_proxy_126d": {"inputs": ['equity'], "func": runw_124_insolvency_proxy_126d},
    "runw_125_insolvency_proxy_252d": {"inputs": ['equity'], "func": runw_125_insolvency_proxy_252d},
    "runw_126_bankruptcy_risk_proxy_5d": {"inputs": ['assets', 'liabs'], "func": runw_126_bankruptcy_risk_proxy_5d},
    "runw_127_bankruptcy_risk_proxy_21d": {"inputs": ['assets', 'liabs'], "func": runw_127_bankruptcy_risk_proxy_21d},
    "runw_128_bankruptcy_risk_proxy_63d": {"inputs": ['assets', 'liabs'], "func": runw_128_bankruptcy_risk_proxy_63d},
    "runw_129_bankruptcy_risk_proxy_126d": {"inputs": ['assets', 'liabs'], "func": runw_129_bankruptcy_risk_proxy_126d},
    "runw_130_bankruptcy_risk_proxy_252d": {"inputs": ['assets', 'liabs'], "func": runw_130_bankruptcy_risk_proxy_252d},
    "runw_131_cash_reinfusion_proxy_5d": {"inputs": ['assets', 'equity'], "func": runw_131_cash_reinfusion_proxy_5d},
    "runw_132_cash_reinfusion_proxy_21d": {"inputs": ['assets', 'equity'], "func": runw_132_cash_reinfusion_proxy_21d},
    "runw_133_cash_reinfusion_proxy_63d": {"inputs": ['assets', 'equity'], "func": runw_133_cash_reinfusion_proxy_63d},
    "runw_134_cash_reinfusion_proxy_126d": {"inputs": ['assets', 'equity'], "func": runw_134_cash_reinfusion_proxy_126d},
    "runw_135_cash_reinfusion_proxy_252d": {"inputs": ['assets', 'equity'], "func": runw_135_cash_reinfusion_proxy_252d},
    "runw_136_debt_refinance_risk_5d": {"inputs": ['cashnequiv', 'debtc'], "func": runw_136_debt_refinance_risk_5d},
    "runw_137_debt_refinance_risk_21d": {"inputs": ['cashnequiv', 'debtc'], "func": runw_137_debt_refinance_risk_21d},
    "runw_138_debt_refinance_risk_63d": {"inputs": ['cashnequiv', 'debtc'], "func": runw_138_debt_refinance_risk_63d},
    "runw_139_debt_refinance_risk_126d": {"inputs": ['cashnequiv', 'debtc'], "func": runw_139_debt_refinance_risk_126d},
    "runw_140_debt_refinance_risk_252d": {"inputs": ['cashnequiv', 'debtc'], "func": runw_140_debt_refinance_risk_252d},
    "runw_141_ocf_interest_cov_5d": {"inputs": ['ocf', 'int_exp'], "func": runw_141_ocf_interest_cov_5d},
    "runw_142_ocf_interest_cov_21d": {"inputs": ['ocf', 'int_exp'], "func": runw_142_ocf_interest_cov_21d},
    "runw_143_ocf_interest_cov_63d": {"inputs": ['ocf', 'int_exp'], "func": runw_143_ocf_interest_cov_63d},
    "runw_144_ocf_interest_cov_126d": {"inputs": ['ocf', 'int_exp'], "func": runw_144_ocf_interest_cov_126d},
    "runw_145_ocf_interest_cov_252d": {"inputs": ['ocf', 'int_exp'], "func": runw_145_ocf_interest_cov_252d},
    "runw_146_fcf_yield_5d": {"inputs": ['fcf', 'marketcap'], "func": runw_146_fcf_yield_5d},
    "runw_147_fcf_yield_21d": {"inputs": ['fcf', 'marketcap'], "func": runw_147_fcf_yield_21d},
    "runw_148_fcf_yield_63d": {"inputs": ['fcf', 'marketcap'], "func": runw_148_fcf_yield_63d},
    "runw_149_fcf_yield_126d": {"inputs": ['fcf', 'marketcap'], "func": runw_149_fcf_yield_126d},
    "runw_150_fcf_yield_252d": {"inputs": ['fcf', 'marketcap'], "func": runw_150_fcf_yield_252d},
}
