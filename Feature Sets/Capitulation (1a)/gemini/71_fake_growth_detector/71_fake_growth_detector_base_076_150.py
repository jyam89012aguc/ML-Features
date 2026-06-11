"""
71_fake_growth_detector — Base Features 076-150
Domain: Debt-funded revenue growth signals
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

def fgrd_076_debt_funded_rev_g_z_5d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_076_debt_funded_rev_g_z_5d"""
    return (_zscore_rolling(_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252)), 1260)).shift(5)

def fgrd_077_debt_funded_rev_g_z_21d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_077_debt_funded_rev_g_z_21d"""
    return (_zscore_rolling(_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252)), 1260)).shift(21)

def fgrd_078_debt_funded_rev_g_z_63d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_078_debt_funded_rev_g_z_63d"""
    return (_zscore_rolling(_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252)), 1260)).shift(63)

def fgrd_079_debt_funded_rev_g_z_126d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_079_debt_funded_rev_g_z_126d"""
    return (_zscore_rolling(_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252)), 1260)).shift(126)

def fgrd_080_debt_funded_rev_g_z_252d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_080_debt_funded_rev_g_z_252d"""
    return (_zscore_rolling(_safe_div(revenue.diff(252), (debtn.fillna(0) + debtc.fillna(0)).diff(252)), 1260)).shift(252)

def fgrd_081_organic_growth_proxy_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_081_organic_growth_proxy_5d"""
    return (revenue.pct_change(252) - assets.pct_change(252)).shift(5)

def fgrd_082_organic_growth_proxy_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_082_organic_growth_proxy_21d"""
    return (revenue.pct_change(252) - assets.pct_change(252)).shift(21)

def fgrd_083_organic_growth_proxy_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_083_organic_growth_proxy_63d"""
    return (revenue.pct_change(252) - assets.pct_change(252)).shift(63)

def fgrd_084_organic_growth_proxy_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_084_organic_growth_proxy_126d"""
    return (revenue.pct_change(252) - assets.pct_change(252)).shift(126)

def fgrd_085_organic_growth_proxy_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_085_organic_growth_proxy_252d"""
    return (revenue.pct_change(252) - assets.pct_change(252)).shift(252)

def fgrd_086_burn_rate_growth_5d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_086_burn_rate_growth_5d"""
    return (_safe_div(ocf.diff(252), revenue.diff(252))).shift(5)

def fgrd_087_burn_rate_growth_21d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_087_burn_rate_growth_21d"""
    return (_safe_div(ocf.diff(252), revenue.diff(252))).shift(21)

def fgrd_088_burn_rate_growth_63d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_088_burn_rate_growth_63d"""
    return (_safe_div(ocf.diff(252), revenue.diff(252))).shift(63)

def fgrd_089_burn_rate_growth_126d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_089_burn_rate_growth_126d"""
    return (_safe_div(ocf.diff(252), revenue.diff(252))).shift(126)

def fgrd_090_burn_rate_growth_252d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_090_burn_rate_growth_252d"""
    return (_safe_div(ocf.diff(252), revenue.diff(252))).shift(252)

def fgrd_091_liab_acceleration_5d(liabs: pd.Series) -> pd.Series:
    """fgrd_091_liab_acceleration_5d"""
    return (liabs.pct_change(252).diff(63)).shift(5)

def fgrd_092_liab_acceleration_21d(liabs: pd.Series) -> pd.Series:
    """fgrd_092_liab_acceleration_21d"""
    return (liabs.pct_change(252).diff(63)).shift(21)

def fgrd_093_liab_acceleration_63d(liabs: pd.Series) -> pd.Series:
    """fgrd_093_liab_acceleration_63d"""
    return (liabs.pct_change(252).diff(63)).shift(63)

def fgrd_094_liab_acceleration_126d(liabs: pd.Series) -> pd.Series:
    """fgrd_094_liab_acceleration_126d"""
    return (liabs.pct_change(252).diff(63)).shift(126)

def fgrd_095_liab_acceleration_252d(liabs: pd.Series) -> pd.Series:
    """fgrd_095_liab_acceleration_252d"""
    return (liabs.pct_change(252).diff(63)).shift(252)

def fgrd_096_debt_acceleration_5d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_096_debt_acceleration_5d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252).diff(63)).shift(5)

def fgrd_097_debt_acceleration_21d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_097_debt_acceleration_21d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252).diff(63)).shift(21)

def fgrd_098_debt_acceleration_63d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_098_debt_acceleration_63d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252).diff(63)).shift(63)

def fgrd_099_debt_acceleration_126d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_099_debt_acceleration_126d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252).diff(63)).shift(126)

def fgrd_100_debt_acceleration_252d(debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_100_debt_acceleration_252d"""
    return ((debtn.fillna(0) + debtc.fillna(0)).pct_change(252).diff(63)).shift(252)

def fgrd_101_rev_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """fgrd_101_rev_acceleration_5d"""
    return (revenue.pct_change(252).diff(63)).shift(5)

def fgrd_102_rev_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """fgrd_102_rev_acceleration_21d"""
    return (revenue.pct_change(252).diff(63)).shift(21)

def fgrd_103_rev_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """fgrd_103_rev_acceleration_63d"""
    return (revenue.pct_change(252).diff(63)).shift(63)

def fgrd_104_rev_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """fgrd_104_rev_acceleration_126d"""
    return (revenue.pct_change(252).diff(63)).shift(126)

def fgrd_105_rev_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """fgrd_105_rev_acceleration_252d"""
    return (revenue.pct_change(252).diff(63)).shift(252)

def fgrd_106_fake_growth_z_5d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_106_fake_growth_z_5d"""
    return (_zscore_rolling(revenue.pct_change(252) - ocf.pct_change(252), 1260)).shift(5)

def fgrd_107_fake_growth_z_21d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_107_fake_growth_z_21d"""
    return (_zscore_rolling(revenue.pct_change(252) - ocf.pct_change(252), 1260)).shift(21)

def fgrd_108_fake_growth_z_63d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_108_fake_growth_z_63d"""
    return (_zscore_rolling(revenue.pct_change(252) - ocf.pct_change(252), 1260)).shift(63)

def fgrd_109_fake_growth_z_126d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_109_fake_growth_z_126d"""
    return (_zscore_rolling(revenue.pct_change(252) - ocf.pct_change(252), 1260)).shift(126)

def fgrd_110_fake_growth_z_252d(revenue: pd.Series, ocf: pd.Series) -> pd.Series:
    """fgrd_110_fake_growth_z_252d"""
    return (_zscore_rolling(revenue.pct_change(252) - ocf.pct_change(252), 1260)).shift(252)

def fgrd_111_dilution_acceleration_5d(shareswa: pd.Series) -> pd.Series:
    """fgrd_111_dilution_acceleration_5d"""
    return (shareswa.pct_change(252).diff(63)).shift(5)

def fgrd_112_dilution_acceleration_21d(shareswa: pd.Series) -> pd.Series:
    """fgrd_112_dilution_acceleration_21d"""
    return (shareswa.pct_change(252).diff(63)).shift(21)

def fgrd_113_dilution_acceleration_63d(shareswa: pd.Series) -> pd.Series:
    """fgrd_113_dilution_acceleration_63d"""
    return (shareswa.pct_change(252).diff(63)).shift(63)

def fgrd_114_dilution_acceleration_126d(shareswa: pd.Series) -> pd.Series:
    """fgrd_114_dilution_acceleration_126d"""
    return (shareswa.pct_change(252).diff(63)).shift(126)

def fgrd_115_dilution_acceleration_252d(shareswa: pd.Series) -> pd.Series:
    """fgrd_115_dilution_acceleration_252d"""
    return (shareswa.pct_change(252).diff(63)).shift(252)

def fgrd_116_asset_inflation_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_116_asset_inflation_5d"""
    return (assets.pct_change(252) / revenue.pct_change(252)).shift(5)

def fgrd_117_asset_inflation_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_117_asset_inflation_21d"""
    return (assets.pct_change(252) / revenue.pct_change(252)).shift(21)

def fgrd_118_asset_inflation_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_118_asset_inflation_63d"""
    return (assets.pct_change(252) / revenue.pct_change(252)).shift(63)

def fgrd_119_asset_inflation_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_119_asset_inflation_126d"""
    return (assets.pct_change(252) / revenue.pct_change(252)).shift(126)

def fgrd_120_asset_inflation_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_120_asset_inflation_252d"""
    return (assets.pct_change(252) / revenue.pct_change(252)).shift(252)

def fgrd_121_debt_to_ocf_5d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_121_debt_to_ocf_5d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), ocf)).shift(5)

def fgrd_122_debt_to_ocf_21d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_122_debt_to_ocf_21d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), ocf)).shift(21)

def fgrd_123_debt_to_ocf_63d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_123_debt_to_ocf_63d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), ocf)).shift(63)

def fgrd_124_debt_to_ocf_126d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_124_debt_to_ocf_126d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), ocf)).shift(126)

def fgrd_125_debt_to_ocf_252d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_125_debt_to_ocf_252d"""
    return (_safe_div(debtn.fillna(0) + debtc.fillna(0), ocf)).shift(252)

def fgrd_126_liab_to_ocf_5d(ocf: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_126_liab_to_ocf_5d"""
    return (_safe_div(liabs, ocf)).shift(5)

def fgrd_127_liab_to_ocf_21d(ocf: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_127_liab_to_ocf_21d"""
    return (_safe_div(liabs, ocf)).shift(21)

def fgrd_128_liab_to_ocf_63d(ocf: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_128_liab_to_ocf_63d"""
    return (_safe_div(liabs, ocf)).shift(63)

def fgrd_129_liab_to_ocf_126d(ocf: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_129_liab_to_ocf_126d"""
    return (_safe_div(liabs, ocf)).shift(126)

def fgrd_130_liab_to_ocf_252d(ocf: pd.Series, liabs: pd.Series) -> pd.Series:
    """fgrd_130_liab_to_ocf_252d"""
    return (_safe_div(liabs, ocf)).shift(252)

def fgrd_131_financing_dependency_5d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_131_financing_dependency_5d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), revenue)).shift(5)

def fgrd_132_financing_dependency_21d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_132_financing_dependency_21d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), revenue)).shift(21)

def fgrd_133_financing_dependency_63d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_133_financing_dependency_63d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), revenue)).shift(63)

def fgrd_134_financing_dependency_126d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_134_financing_dependency_126d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), revenue)).shift(126)

def fgrd_135_financing_dependency_252d(revenue: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_135_financing_dependency_252d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), revenue)).shift(252)

def fgrd_136_growth_efficiency_5d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_136_growth_efficiency_5d"""
    return (_safe_div(revenue.diff(252), assets.diff(252))).shift(5)

def fgrd_137_growth_efficiency_21d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_137_growth_efficiency_21d"""
    return (_safe_div(revenue.diff(252), assets.diff(252))).shift(21)

def fgrd_138_growth_efficiency_63d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_138_growth_efficiency_63d"""
    return (_safe_div(revenue.diff(252), assets.diff(252))).shift(63)

def fgrd_139_growth_efficiency_126d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_139_growth_efficiency_126d"""
    return (_safe_div(revenue.diff(252), assets.diff(252))).shift(126)

def fgrd_140_growth_efficiency_252d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """fgrd_140_growth_efficiency_252d"""
    return (_safe_div(revenue.diff(252), assets.diff(252))).shift(252)

def fgrd_141_leverage_decay_5d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_141_leverage_decay_5d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(5)

def fgrd_142_leverage_decay_21d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_142_leverage_decay_21d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(21)

def fgrd_143_leverage_decay_63d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_143_leverage_decay_63d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(63)

def fgrd_144_leverage_decay_126d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_144_leverage_decay_126d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(126)

def fgrd_145_leverage_decay_252d(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """fgrd_145_leverage_decay_252d"""
    return ((_safe_div(equity, assets)).diff(252)).shift(252)

def fgrd_146_ponzi_index_proxy_5d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_146_ponzi_index_proxy_5d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), ocf)).shift(5)

def fgrd_147_ponzi_index_proxy_21d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_147_ponzi_index_proxy_21d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), ocf)).shift(21)

def fgrd_148_ponzi_index_proxy_63d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_148_ponzi_index_proxy_63d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), ocf)).shift(63)

def fgrd_149_ponzi_index_proxy_126d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_149_ponzi_index_proxy_126d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), ocf)).shift(126)

def fgrd_150_ponzi_index_proxy_252d(ocf: pd.Series, debtn: pd.Series, debtc: pd.Series) -> pd.Series:
    """fgrd_150_ponzi_index_proxy_252d"""
    return (_safe_div((debtn.fillna(0) + debtc.fillna(0)).diff(252), ocf)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V71_REGISTRY = {
    "fgrd_076_debt_funded_rev_g_z_5d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_076_debt_funded_rev_g_z_5d},
    "fgrd_077_debt_funded_rev_g_z_21d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_077_debt_funded_rev_g_z_21d},
    "fgrd_078_debt_funded_rev_g_z_63d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_078_debt_funded_rev_g_z_63d},
    "fgrd_079_debt_funded_rev_g_z_126d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_079_debt_funded_rev_g_z_126d},
    "fgrd_080_debt_funded_rev_g_z_252d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_080_debt_funded_rev_g_z_252d},
    "fgrd_081_organic_growth_proxy_5d": {"inputs": ['revenue', 'assets'], "func": fgrd_081_organic_growth_proxy_5d},
    "fgrd_082_organic_growth_proxy_21d": {"inputs": ['revenue', 'assets'], "func": fgrd_082_organic_growth_proxy_21d},
    "fgrd_083_organic_growth_proxy_63d": {"inputs": ['revenue', 'assets'], "func": fgrd_083_organic_growth_proxy_63d},
    "fgrd_084_organic_growth_proxy_126d": {"inputs": ['revenue', 'assets'], "func": fgrd_084_organic_growth_proxy_126d},
    "fgrd_085_organic_growth_proxy_252d": {"inputs": ['revenue', 'assets'], "func": fgrd_085_organic_growth_proxy_252d},
    "fgrd_086_burn_rate_growth_5d": {"inputs": ['revenue', 'ocf'], "func": fgrd_086_burn_rate_growth_5d},
    "fgrd_087_burn_rate_growth_21d": {"inputs": ['revenue', 'ocf'], "func": fgrd_087_burn_rate_growth_21d},
    "fgrd_088_burn_rate_growth_63d": {"inputs": ['revenue', 'ocf'], "func": fgrd_088_burn_rate_growth_63d},
    "fgrd_089_burn_rate_growth_126d": {"inputs": ['revenue', 'ocf'], "func": fgrd_089_burn_rate_growth_126d},
    "fgrd_090_burn_rate_growth_252d": {"inputs": ['revenue', 'ocf'], "func": fgrd_090_burn_rate_growth_252d},
    "fgrd_091_liab_acceleration_5d": {"inputs": ['liabs'], "func": fgrd_091_liab_acceleration_5d},
    "fgrd_092_liab_acceleration_21d": {"inputs": ['liabs'], "func": fgrd_092_liab_acceleration_21d},
    "fgrd_093_liab_acceleration_63d": {"inputs": ['liabs'], "func": fgrd_093_liab_acceleration_63d},
    "fgrd_094_liab_acceleration_126d": {"inputs": ['liabs'], "func": fgrd_094_liab_acceleration_126d},
    "fgrd_095_liab_acceleration_252d": {"inputs": ['liabs'], "func": fgrd_095_liab_acceleration_252d},
    "fgrd_096_debt_acceleration_5d": {"inputs": ['debtn', 'debtc'], "func": fgrd_096_debt_acceleration_5d},
    "fgrd_097_debt_acceleration_21d": {"inputs": ['debtn', 'debtc'], "func": fgrd_097_debt_acceleration_21d},
    "fgrd_098_debt_acceleration_63d": {"inputs": ['debtn', 'debtc'], "func": fgrd_098_debt_acceleration_63d},
    "fgrd_099_debt_acceleration_126d": {"inputs": ['debtn', 'debtc'], "func": fgrd_099_debt_acceleration_126d},
    "fgrd_100_debt_acceleration_252d": {"inputs": ['debtn', 'debtc'], "func": fgrd_100_debt_acceleration_252d},
    "fgrd_101_rev_acceleration_5d": {"inputs": ['revenue'], "func": fgrd_101_rev_acceleration_5d},
    "fgrd_102_rev_acceleration_21d": {"inputs": ['revenue'], "func": fgrd_102_rev_acceleration_21d},
    "fgrd_103_rev_acceleration_63d": {"inputs": ['revenue'], "func": fgrd_103_rev_acceleration_63d},
    "fgrd_104_rev_acceleration_126d": {"inputs": ['revenue'], "func": fgrd_104_rev_acceleration_126d},
    "fgrd_105_rev_acceleration_252d": {"inputs": ['revenue'], "func": fgrd_105_rev_acceleration_252d},
    "fgrd_106_fake_growth_z_5d": {"inputs": ['revenue', 'ocf'], "func": fgrd_106_fake_growth_z_5d},
    "fgrd_107_fake_growth_z_21d": {"inputs": ['revenue', 'ocf'], "func": fgrd_107_fake_growth_z_21d},
    "fgrd_108_fake_growth_z_63d": {"inputs": ['revenue', 'ocf'], "func": fgrd_108_fake_growth_z_63d},
    "fgrd_109_fake_growth_z_126d": {"inputs": ['revenue', 'ocf'], "func": fgrd_109_fake_growth_z_126d},
    "fgrd_110_fake_growth_z_252d": {"inputs": ['revenue', 'ocf'], "func": fgrd_110_fake_growth_z_252d},
    "fgrd_111_dilution_acceleration_5d": {"inputs": ['shareswa'], "func": fgrd_111_dilution_acceleration_5d},
    "fgrd_112_dilution_acceleration_21d": {"inputs": ['shareswa'], "func": fgrd_112_dilution_acceleration_21d},
    "fgrd_113_dilution_acceleration_63d": {"inputs": ['shareswa'], "func": fgrd_113_dilution_acceleration_63d},
    "fgrd_114_dilution_acceleration_126d": {"inputs": ['shareswa'], "func": fgrd_114_dilution_acceleration_126d},
    "fgrd_115_dilution_acceleration_252d": {"inputs": ['shareswa'], "func": fgrd_115_dilution_acceleration_252d},
    "fgrd_116_asset_inflation_5d": {"inputs": ['revenue', 'assets'], "func": fgrd_116_asset_inflation_5d},
    "fgrd_117_asset_inflation_21d": {"inputs": ['revenue', 'assets'], "func": fgrd_117_asset_inflation_21d},
    "fgrd_118_asset_inflation_63d": {"inputs": ['revenue', 'assets'], "func": fgrd_118_asset_inflation_63d},
    "fgrd_119_asset_inflation_126d": {"inputs": ['revenue', 'assets'], "func": fgrd_119_asset_inflation_126d},
    "fgrd_120_asset_inflation_252d": {"inputs": ['revenue', 'assets'], "func": fgrd_120_asset_inflation_252d},
    "fgrd_121_debt_to_ocf_5d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_121_debt_to_ocf_5d},
    "fgrd_122_debt_to_ocf_21d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_122_debt_to_ocf_21d},
    "fgrd_123_debt_to_ocf_63d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_123_debt_to_ocf_63d},
    "fgrd_124_debt_to_ocf_126d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_124_debt_to_ocf_126d},
    "fgrd_125_debt_to_ocf_252d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_125_debt_to_ocf_252d},
    "fgrd_126_liab_to_ocf_5d": {"inputs": ['ocf', 'liabs'], "func": fgrd_126_liab_to_ocf_5d},
    "fgrd_127_liab_to_ocf_21d": {"inputs": ['ocf', 'liabs'], "func": fgrd_127_liab_to_ocf_21d},
    "fgrd_128_liab_to_ocf_63d": {"inputs": ['ocf', 'liabs'], "func": fgrd_128_liab_to_ocf_63d},
    "fgrd_129_liab_to_ocf_126d": {"inputs": ['ocf', 'liabs'], "func": fgrd_129_liab_to_ocf_126d},
    "fgrd_130_liab_to_ocf_252d": {"inputs": ['ocf', 'liabs'], "func": fgrd_130_liab_to_ocf_252d},
    "fgrd_131_financing_dependency_5d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_131_financing_dependency_5d},
    "fgrd_132_financing_dependency_21d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_132_financing_dependency_21d},
    "fgrd_133_financing_dependency_63d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_133_financing_dependency_63d},
    "fgrd_134_financing_dependency_126d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_134_financing_dependency_126d},
    "fgrd_135_financing_dependency_252d": {"inputs": ['revenue', 'debtn', 'debtc'], "func": fgrd_135_financing_dependency_252d},
    "fgrd_136_growth_efficiency_5d": {"inputs": ['revenue', 'assets'], "func": fgrd_136_growth_efficiency_5d},
    "fgrd_137_growth_efficiency_21d": {"inputs": ['revenue', 'assets'], "func": fgrd_137_growth_efficiency_21d},
    "fgrd_138_growth_efficiency_63d": {"inputs": ['revenue', 'assets'], "func": fgrd_138_growth_efficiency_63d},
    "fgrd_139_growth_efficiency_126d": {"inputs": ['revenue', 'assets'], "func": fgrd_139_growth_efficiency_126d},
    "fgrd_140_growth_efficiency_252d": {"inputs": ['revenue', 'assets'], "func": fgrd_140_growth_efficiency_252d},
    "fgrd_141_leverage_decay_5d": {"inputs": ['assets', 'equity'], "func": fgrd_141_leverage_decay_5d},
    "fgrd_142_leverage_decay_21d": {"inputs": ['assets', 'equity'], "func": fgrd_142_leverage_decay_21d},
    "fgrd_143_leverage_decay_63d": {"inputs": ['assets', 'equity'], "func": fgrd_143_leverage_decay_63d},
    "fgrd_144_leverage_decay_126d": {"inputs": ['assets', 'equity'], "func": fgrd_144_leverage_decay_126d},
    "fgrd_145_leverage_decay_252d": {"inputs": ['assets', 'equity'], "func": fgrd_145_leverage_decay_252d},
    "fgrd_146_ponzi_index_proxy_5d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_146_ponzi_index_proxy_5d},
    "fgrd_147_ponzi_index_proxy_21d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_147_ponzi_index_proxy_21d},
    "fgrd_148_ponzi_index_proxy_63d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_148_ponzi_index_proxy_63d},
    "fgrd_149_ponzi_index_proxy_126d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_149_ponzi_index_proxy_126d},
    "fgrd_150_ponzi_index_proxy_252d": {"inputs": ['ocf', 'debtn', 'debtc'], "func": fgrd_150_ponzi_index_proxy_252d},
}
