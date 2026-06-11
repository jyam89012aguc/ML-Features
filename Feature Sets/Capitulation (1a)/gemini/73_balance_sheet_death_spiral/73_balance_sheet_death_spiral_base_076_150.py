"""
73_balance_sheet_death_spiral — Base Features 076-150
Domain: Assets shrinking + Liabs growing
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

def bsds_076_asset_shrinkage_vel_5d(assets: pd.Series) -> pd.Series:
    """bsds_076_asset_shrinkage_vel_5d"""
    return (assets.pct_change(252).diff(63)).shift(5)

def bsds_077_asset_shrinkage_vel_21d(assets: pd.Series) -> pd.Series:
    """bsds_077_asset_shrinkage_vel_21d"""
    return (assets.pct_change(252).diff(63)).shift(21)

def bsds_078_asset_shrinkage_vel_63d(assets: pd.Series) -> pd.Series:
    """bsds_078_asset_shrinkage_vel_63d"""
    return (assets.pct_change(252).diff(63)).shift(63)

def bsds_079_asset_shrinkage_vel_126d(assets: pd.Series) -> pd.Series:
    """bsds_079_asset_shrinkage_vel_126d"""
    return (assets.pct_change(252).diff(63)).shift(126)

def bsds_080_asset_shrinkage_vel_252d(assets: pd.Series) -> pd.Series:
    """bsds_080_asset_shrinkage_vel_252d"""
    return (assets.pct_change(252).diff(63)).shift(252)

def bsds_081_liab_expansion_vel_5d(liabs: pd.Series) -> pd.Series:
    """bsds_081_liab_expansion_vel_5d"""
    return (liabs.pct_change(252).diff(63)).shift(5)

def bsds_082_liab_expansion_vel_21d(liabs: pd.Series) -> pd.Series:
    """bsds_082_liab_expansion_vel_21d"""
    return (liabs.pct_change(252).diff(63)).shift(21)

def bsds_083_liab_expansion_vel_63d(liabs: pd.Series) -> pd.Series:
    """bsds_083_liab_expansion_vel_63d"""
    return (liabs.pct_change(252).diff(63)).shift(63)

def bsds_084_liab_expansion_vel_126d(liabs: pd.Series) -> pd.Series:
    """bsds_084_liab_expansion_vel_126d"""
    return (liabs.pct_change(252).diff(63)).shift(126)

def bsds_085_liab_expansion_vel_252d(liabs: pd.Series) -> pd.Series:
    """bsds_085_liab_expansion_vel_252d"""
    return (liabs.pct_change(252).diff(63)).shift(252)

def bsds_086_death_spiral_velocity_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_086_death_spiral_velocity_5d"""
    return ((liabs.pct_change(252) - assets.pct_change(252)).diff(63)).shift(5)

def bsds_087_death_spiral_velocity_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_087_death_spiral_velocity_21d"""
    return ((liabs.pct_change(252) - assets.pct_change(252)).diff(63)).shift(21)

def bsds_088_death_spiral_velocity_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_088_death_spiral_velocity_63d"""
    return ((liabs.pct_change(252) - assets.pct_change(252)).diff(63)).shift(63)

def bsds_089_death_spiral_velocity_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_089_death_spiral_velocity_126d"""
    return ((liabs.pct_change(252) - assets.pct_change(252)).diff(63)).shift(126)

def bsds_090_death_spiral_velocity_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_090_death_spiral_velocity_252d"""
    return ((liabs.pct_change(252) - assets.pct_change(252)).diff(63)).shift(252)

def bsds_091_net_worth_acceleration_5d(equity: pd.Series) -> pd.Series:
    """bsds_091_net_worth_acceleration_5d"""
    return (equity.pct_change(252).diff(63)).shift(5)

def bsds_092_net_worth_acceleration_21d(equity: pd.Series) -> pd.Series:
    """bsds_092_net_worth_acceleration_21d"""
    return (equity.pct_change(252).diff(63)).shift(21)

def bsds_093_net_worth_acceleration_63d(equity: pd.Series) -> pd.Series:
    """bsds_093_net_worth_acceleration_63d"""
    return (equity.pct_change(252).diff(63)).shift(63)

def bsds_094_net_worth_acceleration_126d(equity: pd.Series) -> pd.Series:
    """bsds_094_net_worth_acceleration_126d"""
    return (equity.pct_change(252).diff(63)).shift(126)

def bsds_095_net_worth_acceleration_252d(equity: pd.Series) -> pd.Series:
    """bsds_095_net_worth_acceleration_252d"""
    return (equity.pct_change(252).diff(63)).shift(252)

def bsds_096_leverage_acceleration_5d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_096_leverage_acceleration_5d"""
    return ((_safe_div(liabs, assets)).diff(63).diff(21)).shift(5)

def bsds_097_leverage_acceleration_21d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_097_leverage_acceleration_21d"""
    return ((_safe_div(liabs, assets)).diff(63).diff(21)).shift(21)

def bsds_098_leverage_acceleration_63d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_098_leverage_acceleration_63d"""
    return ((_safe_div(liabs, assets)).diff(63).diff(21)).shift(63)

def bsds_099_leverage_acceleration_126d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_099_leverage_acceleration_126d"""
    return ((_safe_div(liabs, assets)).diff(63).diff(21)).shift(126)

def bsds_100_leverage_acceleration_252d(assets: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_100_leverage_acceleration_252d"""
    return ((_safe_div(liabs, assets)).diff(63).diff(21)).shift(252)

def bsds_101_capital_deficiency_proxy_5d(equity: pd.Series) -> pd.Series:
    """bsds_101_capital_deficiency_proxy_5d"""
    return ((equity < 0).astype(float)).shift(5)

def bsds_102_capital_deficiency_proxy_21d(equity: pd.Series) -> pd.Series:
    """bsds_102_capital_deficiency_proxy_21d"""
    return ((equity < 0).astype(float)).shift(21)

def bsds_103_capital_deficiency_proxy_63d(equity: pd.Series) -> pd.Series:
    """bsds_103_capital_deficiency_proxy_63d"""
    return ((equity < 0).astype(float)).shift(63)

def bsds_104_capital_deficiency_proxy_126d(equity: pd.Series) -> pd.Series:
    """bsds_104_capital_deficiency_proxy_126d"""
    return ((equity < 0).astype(float)).shift(126)

def bsds_105_capital_deficiency_proxy_252d(equity: pd.Series) -> pd.Series:
    """bsds_105_capital_deficiency_proxy_252d"""
    return ((equity < 0).astype(float)).shift(252)

def bsds_106_asset_fire_sale_proxy_5d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """bsds_106_asset_fire_sale_proxy_5d"""
    return ((assets.diff(63) < 0) & (cashnequiv.diff(63) > 0)).shift(5)

def bsds_107_asset_fire_sale_proxy_21d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """bsds_107_asset_fire_sale_proxy_21d"""
    return ((assets.diff(63) < 0) & (cashnequiv.diff(63) > 0)).shift(21)

def bsds_108_asset_fire_sale_proxy_63d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """bsds_108_asset_fire_sale_proxy_63d"""
    return ((assets.diff(63) < 0) & (cashnequiv.diff(63) > 0)).shift(63)

def bsds_109_asset_fire_sale_proxy_126d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """bsds_109_asset_fire_sale_proxy_126d"""
    return ((assets.diff(63) < 0) & (cashnequiv.diff(63) > 0)).shift(126)

def bsds_110_asset_fire_sale_proxy_252d(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """bsds_110_asset_fire_sale_proxy_252d"""
    return ((assets.diff(63) < 0) & (cashnequiv.diff(63) > 0)).shift(252)

def bsds_111_debt_trap_index_5d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """bsds_111_debt_trap_index_5d"""
    return ((_safe_div(int_exp, ocf)).diff(63)).shift(5)

def bsds_112_debt_trap_index_21d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """bsds_112_debt_trap_index_21d"""
    return ((_safe_div(int_exp, ocf)).diff(63)).shift(21)

def bsds_113_debt_trap_index_63d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """bsds_113_debt_trap_index_63d"""
    return ((_safe_div(int_exp, ocf)).diff(63)).shift(63)

def bsds_114_debt_trap_index_126d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """bsds_114_debt_trap_index_126d"""
    return ((_safe_div(int_exp, ocf)).diff(63)).shift(126)

def bsds_115_debt_trap_index_252d(ocf: pd.Series, int_exp: pd.Series) -> pd.Series:
    """bsds_115_debt_trap_index_252d"""
    return ((_safe_div(int_exp, ocf)).diff(63)).shift(252)

def bsds_116_liquidation_value_proxy_5d(liabs: pd.Series, cashnequiv: pd.Series, marketcap: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """bsds_116_liquidation_value_proxy_5d"""
    return (_safe_div(cashnequiv + receivables + inventory - liabs, marketcap)).shift(5)

def bsds_117_liquidation_value_proxy_21d(liabs: pd.Series, cashnequiv: pd.Series, marketcap: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """bsds_117_liquidation_value_proxy_21d"""
    return (_safe_div(cashnequiv + receivables + inventory - liabs, marketcap)).shift(21)

def bsds_118_liquidation_value_proxy_63d(liabs: pd.Series, cashnequiv: pd.Series, marketcap: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """bsds_118_liquidation_value_proxy_63d"""
    return (_safe_div(cashnequiv + receivables + inventory - liabs, marketcap)).shift(63)

def bsds_119_liquidation_value_proxy_126d(liabs: pd.Series, cashnequiv: pd.Series, marketcap: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """bsds_119_liquidation_value_proxy_126d"""
    return (_safe_div(cashnequiv + receivables + inventory - liabs, marketcap)).shift(126)

def bsds_120_liquidation_value_proxy_252d(liabs: pd.Series, cashnequiv: pd.Series, marketcap: pd.Series, inventory: pd.Series, receivables: pd.Series) -> pd.Series:
    """bsds_120_liquidation_value_proxy_252d"""
    return (_safe_div(cashnequiv + receivables + inventory - liabs, marketcap)).shift(252)

def bsds_121_insolvency_velocity_5d(liabs: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_121_insolvency_velocity_5d"""
    return ((_safe_div(liabs, equity)).diff(63)).shift(5)

def bsds_122_insolvency_velocity_21d(liabs: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_122_insolvency_velocity_21d"""
    return ((_safe_div(liabs, equity)).diff(63)).shift(21)

def bsds_123_insolvency_velocity_63d(liabs: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_123_insolvency_velocity_63d"""
    return ((_safe_div(liabs, equity)).diff(63)).shift(63)

def bsds_124_insolvency_velocity_126d(liabs: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_124_insolvency_velocity_126d"""
    return ((_safe_div(liabs, equity)).diff(63)).shift(126)

def bsds_125_insolvency_velocity_252d(liabs: pd.Series, equity: pd.Series) -> pd.Series:
    """bsds_125_insolvency_velocity_252d"""
    return ((_safe_div(liabs, equity)).diff(63)).shift(252)

def bsds_126_asset_base_decay_5d(ppnent: pd.Series) -> pd.Series:
    """bsds_126_asset_base_decay_5d"""
    return (ppnent.pct_change(252)).shift(5)

def bsds_127_asset_base_decay_21d(ppnent: pd.Series) -> pd.Series:
    """bsds_127_asset_base_decay_21d"""
    return (ppnent.pct_change(252)).shift(21)

def bsds_128_asset_base_decay_63d(ppnent: pd.Series) -> pd.Series:
    """bsds_128_asset_base_decay_63d"""
    return (ppnent.pct_change(252)).shift(63)

def bsds_129_asset_base_decay_126d(ppnent: pd.Series) -> pd.Series:
    """bsds_129_asset_base_decay_126d"""
    return (ppnent.pct_change(252)).shift(126)

def bsds_130_asset_base_decay_252d(ppnent: pd.Series) -> pd.Series:
    """bsds_130_asset_base_decay_252d"""
    return (ppnent.pct_change(252)).shift(252)

def bsds_131_liability_burden_5d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_131_liability_burden_5d"""
    return (_safe_div(liabs, revenue)).shift(5)

def bsds_132_liability_burden_21d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_132_liability_burden_21d"""
    return (_safe_div(liabs, revenue)).shift(21)

def bsds_133_liability_burden_63d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_133_liability_burden_63d"""
    return (_safe_div(liabs, revenue)).shift(63)

def bsds_134_liability_burden_126d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_134_liability_burden_126d"""
    return (_safe_div(liabs, revenue)).shift(126)

def bsds_135_liability_burden_252d(revenue: pd.Series, liabs: pd.Series) -> pd.Series:
    """bsds_135_liability_burden_252d"""
    return (_safe_div(liabs, revenue)).shift(252)

def bsds_136_death_spiral_persistence_5d(revenue: pd.Series) -> pd.Series:
    """bsds_136_death_spiral_persistence_5d"""
    return _safe_div(death_spiral_index, death_spiral_index.shift(252))

def bsds_137_death_spiral_persistence_21d(revenue: pd.Series) -> pd.Series:
    """bsds_137_death_spiral_persistence_21d"""
    return _safe_div(death_spiral_index, death_spiral_index.shift(252))

def bsds_138_death_spiral_persistence_63d(revenue: pd.Series) -> pd.Series:
    """bsds_138_death_spiral_persistence_63d"""
    return _safe_div(death_spiral_index, death_spiral_index.shift(252))

def bsds_139_death_spiral_persistence_126d(revenue: pd.Series) -> pd.Series:
    """bsds_139_death_spiral_persistence_126d"""
    return _safe_div(death_spiral_index, death_spiral_index.shift(252))

def bsds_140_death_spiral_persistence_252d(revenue: pd.Series) -> pd.Series:
    """bsds_140_death_spiral_persistence_252d"""
    return _safe_div(death_spiral_index, death_spiral_index.shift(252))

def bsds_141_equity_wipeout_risk_5d(liabs: pd.Series, marketcap: pd.Series) -> pd.Series:
    """bsds_141_equity_wipeout_risk_5d"""
    return (_safe_div(marketcap, liabs)).shift(5)

def bsds_142_equity_wipeout_risk_21d(liabs: pd.Series, marketcap: pd.Series) -> pd.Series:
    """bsds_142_equity_wipeout_risk_21d"""
    return (_safe_div(marketcap, liabs)).shift(21)

def bsds_143_equity_wipeout_risk_63d(liabs: pd.Series, marketcap: pd.Series) -> pd.Series:
    """bsds_143_equity_wipeout_risk_63d"""
    return (_safe_div(marketcap, liabs)).shift(63)

def bsds_144_equity_wipeout_risk_126d(liabs: pd.Series, marketcap: pd.Series) -> pd.Series:
    """bsds_144_equity_wipeout_risk_126d"""
    return (_safe_div(marketcap, liabs)).shift(126)

def bsds_145_equity_wipeout_risk_252d(liabs: pd.Series, marketcap: pd.Series) -> pd.Series:
    """bsds_145_equity_wipeout_risk_252d"""
    return (_safe_div(marketcap, liabs)).shift(252)

def bsds_146_spiral_acceleration_5d(revenue: pd.Series) -> pd.Series:
    """bsds_146_spiral_acceleration_5d"""
    return (death_spiral_index.diff(63).diff(21)).shift(5)

def bsds_147_spiral_acceleration_21d(revenue: pd.Series) -> pd.Series:
    """bsds_147_spiral_acceleration_21d"""
    return (death_spiral_index.diff(63).diff(21)).shift(21)

def bsds_148_spiral_acceleration_63d(revenue: pd.Series) -> pd.Series:
    """bsds_148_spiral_acceleration_63d"""
    return (death_spiral_index.diff(63).diff(21)).shift(63)

def bsds_149_spiral_acceleration_126d(revenue: pd.Series) -> pd.Series:
    """bsds_149_spiral_acceleration_126d"""
    return (death_spiral_index.diff(63).diff(21)).shift(126)

def bsds_150_spiral_acceleration_252d(revenue: pd.Series) -> pd.Series:
    """bsds_150_spiral_acceleration_252d"""
    return (death_spiral_index.diff(63).diff(21)).shift(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V73_REGISTRY = {
    "bsds_076_asset_shrinkage_vel_5d": {"inputs": ['assets'], "func": bsds_076_asset_shrinkage_vel_5d},
    "bsds_077_asset_shrinkage_vel_21d": {"inputs": ['assets'], "func": bsds_077_asset_shrinkage_vel_21d},
    "bsds_078_asset_shrinkage_vel_63d": {"inputs": ['assets'], "func": bsds_078_asset_shrinkage_vel_63d},
    "bsds_079_asset_shrinkage_vel_126d": {"inputs": ['assets'], "func": bsds_079_asset_shrinkage_vel_126d},
    "bsds_080_asset_shrinkage_vel_252d": {"inputs": ['assets'], "func": bsds_080_asset_shrinkage_vel_252d},
    "bsds_081_liab_expansion_vel_5d": {"inputs": ['liabs'], "func": bsds_081_liab_expansion_vel_5d},
    "bsds_082_liab_expansion_vel_21d": {"inputs": ['liabs'], "func": bsds_082_liab_expansion_vel_21d},
    "bsds_083_liab_expansion_vel_63d": {"inputs": ['liabs'], "func": bsds_083_liab_expansion_vel_63d},
    "bsds_084_liab_expansion_vel_126d": {"inputs": ['liabs'], "func": bsds_084_liab_expansion_vel_126d},
    "bsds_085_liab_expansion_vel_252d": {"inputs": ['liabs'], "func": bsds_085_liab_expansion_vel_252d},
    "bsds_086_death_spiral_velocity_5d": {"inputs": ['assets', 'liabs'], "func": bsds_086_death_spiral_velocity_5d},
    "bsds_087_death_spiral_velocity_21d": {"inputs": ['assets', 'liabs'], "func": bsds_087_death_spiral_velocity_21d},
    "bsds_088_death_spiral_velocity_63d": {"inputs": ['assets', 'liabs'], "func": bsds_088_death_spiral_velocity_63d},
    "bsds_089_death_spiral_velocity_126d": {"inputs": ['assets', 'liabs'], "func": bsds_089_death_spiral_velocity_126d},
    "bsds_090_death_spiral_velocity_252d": {"inputs": ['assets', 'liabs'], "func": bsds_090_death_spiral_velocity_252d},
    "bsds_091_net_worth_acceleration_5d": {"inputs": ['equity'], "func": bsds_091_net_worth_acceleration_5d},
    "bsds_092_net_worth_acceleration_21d": {"inputs": ['equity'], "func": bsds_092_net_worth_acceleration_21d},
    "bsds_093_net_worth_acceleration_63d": {"inputs": ['equity'], "func": bsds_093_net_worth_acceleration_63d},
    "bsds_094_net_worth_acceleration_126d": {"inputs": ['equity'], "func": bsds_094_net_worth_acceleration_126d},
    "bsds_095_net_worth_acceleration_252d": {"inputs": ['equity'], "func": bsds_095_net_worth_acceleration_252d},
    "bsds_096_leverage_acceleration_5d": {"inputs": ['assets', 'liabs'], "func": bsds_096_leverage_acceleration_5d},
    "bsds_097_leverage_acceleration_21d": {"inputs": ['assets', 'liabs'], "func": bsds_097_leverage_acceleration_21d},
    "bsds_098_leverage_acceleration_63d": {"inputs": ['assets', 'liabs'], "func": bsds_098_leverage_acceleration_63d},
    "bsds_099_leverage_acceleration_126d": {"inputs": ['assets', 'liabs'], "func": bsds_099_leverage_acceleration_126d},
    "bsds_100_leverage_acceleration_252d": {"inputs": ['assets', 'liabs'], "func": bsds_100_leverage_acceleration_252d},
    "bsds_101_capital_deficiency_proxy_5d": {"inputs": ['equity'], "func": bsds_101_capital_deficiency_proxy_5d},
    "bsds_102_capital_deficiency_proxy_21d": {"inputs": ['equity'], "func": bsds_102_capital_deficiency_proxy_21d},
    "bsds_103_capital_deficiency_proxy_63d": {"inputs": ['equity'], "func": bsds_103_capital_deficiency_proxy_63d},
    "bsds_104_capital_deficiency_proxy_126d": {"inputs": ['equity'], "func": bsds_104_capital_deficiency_proxy_126d},
    "bsds_105_capital_deficiency_proxy_252d": {"inputs": ['equity'], "func": bsds_105_capital_deficiency_proxy_252d},
    "bsds_106_asset_fire_sale_proxy_5d": {"inputs": ['assets', 'cashnequiv'], "func": bsds_106_asset_fire_sale_proxy_5d},
    "bsds_107_asset_fire_sale_proxy_21d": {"inputs": ['assets', 'cashnequiv'], "func": bsds_107_asset_fire_sale_proxy_21d},
    "bsds_108_asset_fire_sale_proxy_63d": {"inputs": ['assets', 'cashnequiv'], "func": bsds_108_asset_fire_sale_proxy_63d},
    "bsds_109_asset_fire_sale_proxy_126d": {"inputs": ['assets', 'cashnequiv'], "func": bsds_109_asset_fire_sale_proxy_126d},
    "bsds_110_asset_fire_sale_proxy_252d": {"inputs": ['assets', 'cashnequiv'], "func": bsds_110_asset_fire_sale_proxy_252d},
    "bsds_111_debt_trap_index_5d": {"inputs": ['ocf', 'int_exp'], "func": bsds_111_debt_trap_index_5d},
    "bsds_112_debt_trap_index_21d": {"inputs": ['ocf', 'int_exp'], "func": bsds_112_debt_trap_index_21d},
    "bsds_113_debt_trap_index_63d": {"inputs": ['ocf', 'int_exp'], "func": bsds_113_debt_trap_index_63d},
    "bsds_114_debt_trap_index_126d": {"inputs": ['ocf', 'int_exp'], "func": bsds_114_debt_trap_index_126d},
    "bsds_115_debt_trap_index_252d": {"inputs": ['ocf', 'int_exp'], "func": bsds_115_debt_trap_index_252d},
    "bsds_116_liquidation_value_proxy_5d": {"inputs": ['liabs', 'cashnequiv', 'marketcap', 'inventory', 'receivables'], "func": bsds_116_liquidation_value_proxy_5d},
    "bsds_117_liquidation_value_proxy_21d": {"inputs": ['liabs', 'cashnequiv', 'marketcap', 'inventory', 'receivables'], "func": bsds_117_liquidation_value_proxy_21d},
    "bsds_118_liquidation_value_proxy_63d": {"inputs": ['liabs', 'cashnequiv', 'marketcap', 'inventory', 'receivables'], "func": bsds_118_liquidation_value_proxy_63d},
    "bsds_119_liquidation_value_proxy_126d": {"inputs": ['liabs', 'cashnequiv', 'marketcap', 'inventory', 'receivables'], "func": bsds_119_liquidation_value_proxy_126d},
    "bsds_120_liquidation_value_proxy_252d": {"inputs": ['liabs', 'cashnequiv', 'marketcap', 'inventory', 'receivables'], "func": bsds_120_liquidation_value_proxy_252d},
    "bsds_121_insolvency_velocity_5d": {"inputs": ['liabs', 'equity'], "func": bsds_121_insolvency_velocity_5d},
    "bsds_122_insolvency_velocity_21d": {"inputs": ['liabs', 'equity'], "func": bsds_122_insolvency_velocity_21d},
    "bsds_123_insolvency_velocity_63d": {"inputs": ['liabs', 'equity'], "func": bsds_123_insolvency_velocity_63d},
    "bsds_124_insolvency_velocity_126d": {"inputs": ['liabs', 'equity'], "func": bsds_124_insolvency_velocity_126d},
    "bsds_125_insolvency_velocity_252d": {"inputs": ['liabs', 'equity'], "func": bsds_125_insolvency_velocity_252d},
    "bsds_126_asset_base_decay_5d": {"inputs": ['ppnent'], "func": bsds_126_asset_base_decay_5d},
    "bsds_127_asset_base_decay_21d": {"inputs": ['ppnent'], "func": bsds_127_asset_base_decay_21d},
    "bsds_128_asset_base_decay_63d": {"inputs": ['ppnent'], "func": bsds_128_asset_base_decay_63d},
    "bsds_129_asset_base_decay_126d": {"inputs": ['ppnent'], "func": bsds_129_asset_base_decay_126d},
    "bsds_130_asset_base_decay_252d": {"inputs": ['ppnent'], "func": bsds_130_asset_base_decay_252d},
    "bsds_131_liability_burden_5d": {"inputs": ['revenue', 'liabs'], "func": bsds_131_liability_burden_5d},
    "bsds_132_liability_burden_21d": {"inputs": ['revenue', 'liabs'], "func": bsds_132_liability_burden_21d},
    "bsds_133_liability_burden_63d": {"inputs": ['revenue', 'liabs'], "func": bsds_133_liability_burden_63d},
    "bsds_134_liability_burden_126d": {"inputs": ['revenue', 'liabs'], "func": bsds_134_liability_burden_126d},
    "bsds_135_liability_burden_252d": {"inputs": ['revenue', 'liabs'], "func": bsds_135_liability_burden_252d},
    "bsds_136_death_spiral_persistence_5d": {"inputs": ['revenue'], "func": bsds_136_death_spiral_persistence_5d},
    "bsds_137_death_spiral_persistence_21d": {"inputs": ['revenue'], "func": bsds_137_death_spiral_persistence_21d},
    "bsds_138_death_spiral_persistence_63d": {"inputs": ['revenue'], "func": bsds_138_death_spiral_persistence_63d},
    "bsds_139_death_spiral_persistence_126d": {"inputs": ['revenue'], "func": bsds_139_death_spiral_persistence_126d},
    "bsds_140_death_spiral_persistence_252d": {"inputs": ['revenue'], "func": bsds_140_death_spiral_persistence_252d},
    "bsds_141_equity_wipeout_risk_5d": {"inputs": ['liabs', 'marketcap'], "func": bsds_141_equity_wipeout_risk_5d},
    "bsds_142_equity_wipeout_risk_21d": {"inputs": ['liabs', 'marketcap'], "func": bsds_142_equity_wipeout_risk_21d},
    "bsds_143_equity_wipeout_risk_63d": {"inputs": ['liabs', 'marketcap'], "func": bsds_143_equity_wipeout_risk_63d},
    "bsds_144_equity_wipeout_risk_126d": {"inputs": ['liabs', 'marketcap'], "func": bsds_144_equity_wipeout_risk_126d},
    "bsds_145_equity_wipeout_risk_252d": {"inputs": ['liabs', 'marketcap'], "func": bsds_145_equity_wipeout_risk_252d},
    "bsds_146_spiral_acceleration_5d": {"inputs": ['revenue'], "func": bsds_146_spiral_acceleration_5d},
    "bsds_147_spiral_acceleration_21d": {"inputs": ['revenue'], "func": bsds_147_spiral_acceleration_21d},
    "bsds_148_spiral_acceleration_63d": {"inputs": ['revenue'], "func": bsds_148_spiral_acceleration_63d},
    "bsds_149_spiral_acceleration_126d": {"inputs": ['revenue'], "func": bsds_149_spiral_acceleration_126d},
    "bsds_150_spiral_acceleration_252d": {"inputs": ['revenue'], "func": bsds_150_spiral_acceleration_252d},
}
