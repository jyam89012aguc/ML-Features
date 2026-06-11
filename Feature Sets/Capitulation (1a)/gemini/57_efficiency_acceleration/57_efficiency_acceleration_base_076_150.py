"""
57_efficiency_acceleration — Base Features 076-150
Domain: efficiency_acceleration
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def effa_076_efficiency_accel_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_076_efficiency_accel_lvl_5d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rolling_mean(base, 5)

def effa_077_efficiency_accel_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_077_efficiency_accel_zscore_5d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _zscore_rolling(base, 5)

def effa_078_efficiency_accel_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_078_efficiency_accel_rank_5d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rank_pct(base, 5)

def effa_079_efficiency_accel_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_079_efficiency_accel_lvl_21d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rolling_mean(base, 21)

def effa_080_efficiency_accel_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_080_efficiency_accel_zscore_21d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _zscore_rolling(base, 21)

def effa_081_efficiency_accel_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_081_efficiency_accel_rank_21d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rank_pct(base, 21)

def effa_082_efficiency_accel_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_082_efficiency_accel_lvl_63d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rolling_mean(base, 63)

def effa_083_efficiency_accel_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_083_efficiency_accel_zscore_63d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _zscore_rolling(base, 63)

def effa_084_efficiency_accel_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_084_efficiency_accel_rank_63d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rank_pct(base, 63)

def effa_085_efficiency_accel_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_085_efficiency_accel_lvl_126d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rolling_mean(base, 126)

def effa_086_efficiency_accel_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_086_efficiency_accel_zscore_126d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _zscore_rolling(base, 126)

def effa_087_efficiency_accel_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_087_efficiency_accel_rank_126d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rank_pct(base, 126)

def effa_088_efficiency_accel_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_088_efficiency_accel_lvl_252d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rolling_mean(base, 252)

def effa_089_efficiency_accel_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_089_efficiency_accel_zscore_252d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _zscore_rolling(base, 252)

def effa_090_efficiency_accel_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_090_efficiency_accel_rank_252d"""
    base = _safe_div(revenue, assets).diff(252).diff(63)
    return _rank_pct(base, 252)

def effa_091_asset_turnover_z_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_091_asset_turnover_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 5)

def effa_092_asset_turnover_z_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_092_asset_turnover_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 5)

def effa_093_asset_turnover_z_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_093_asset_turnover_z_rank_5d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 5)

def effa_094_asset_turnover_z_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_094_asset_turnover_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 21)

def effa_095_asset_turnover_z_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_095_asset_turnover_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 21)

def effa_096_asset_turnover_z_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_096_asset_turnover_z_rank_21d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 21)

def effa_097_asset_turnover_z_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_097_asset_turnover_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 63)

def effa_098_asset_turnover_z_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_098_asset_turnover_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 63)

def effa_099_asset_turnover_z_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_099_asset_turnover_z_rank_63d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 63)

def effa_100_asset_turnover_z_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_100_asset_turnover_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 126)

def effa_101_asset_turnover_z_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_101_asset_turnover_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 126)

def effa_102_asset_turnover_z_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_102_asset_turnover_z_rank_126d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 126)

def effa_103_asset_turnover_z_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_103_asset_turnover_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 252)

def effa_104_asset_turnover_z_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_104_asset_turnover_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 252)

def effa_105_asset_turnover_z_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_105_asset_turnover_z_rank_252d"""
    base = _zscore_rolling(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 252)

def effa_106_inventory_turnover_z_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_106_inventory_turnover_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rolling_mean(base, 5)

def effa_107_inventory_turnover_z_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_107_inventory_turnover_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _zscore_rolling(base, 5)

def effa_108_inventory_turnover_z_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_108_inventory_turnover_z_rank_5d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rank_pct(base, 5)

def effa_109_inventory_turnover_z_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_109_inventory_turnover_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rolling_mean(base, 21)

def effa_110_inventory_turnover_z_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_110_inventory_turnover_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _zscore_rolling(base, 21)

def effa_111_inventory_turnover_z_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_111_inventory_turnover_z_rank_21d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rank_pct(base, 21)

def effa_112_inventory_turnover_z_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_112_inventory_turnover_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rolling_mean(base, 63)

def effa_113_inventory_turnover_z_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_113_inventory_turnover_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _zscore_rolling(base, 63)

def effa_114_inventory_turnover_z_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_114_inventory_turnover_z_rank_63d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rank_pct(base, 63)

def effa_115_inventory_turnover_z_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_115_inventory_turnover_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rolling_mean(base, 126)

def effa_116_inventory_turnover_z_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_116_inventory_turnover_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _zscore_rolling(base, 126)

def effa_117_inventory_turnover_z_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_117_inventory_turnover_z_rank_126d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rank_pct(base, 126)

def effa_118_inventory_turnover_z_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_118_inventory_turnover_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rolling_mean(base, 252)

def effa_119_inventory_turnover_z_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_119_inventory_turnover_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _zscore_rolling(base, 252)

def effa_120_inventory_turnover_z_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_120_inventory_turnover_z_rank_252d"""
    base = _zscore_rolling(_safe_div(cor, inventory), 252)
    return _rank_pct(base, 252)

def effa_121_efficiency_rank_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_121_efficiency_rank_lvl_5d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 5)

def effa_122_efficiency_rank_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_122_efficiency_rank_zscore_5d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 5)

def effa_123_efficiency_rank_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_123_efficiency_rank_rank_5d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 5)

def effa_124_efficiency_rank_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_124_efficiency_rank_lvl_21d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 21)

def effa_125_efficiency_rank_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_125_efficiency_rank_zscore_21d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 21)

def effa_126_efficiency_rank_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_126_efficiency_rank_rank_21d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 21)

def effa_127_efficiency_rank_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_127_efficiency_rank_lvl_63d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 63)

def effa_128_efficiency_rank_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_128_efficiency_rank_zscore_63d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 63)

def effa_129_efficiency_rank_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_129_efficiency_rank_rank_63d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 63)

def effa_130_efficiency_rank_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_130_efficiency_rank_lvl_126d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 126)

def effa_131_efficiency_rank_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_131_efficiency_rank_zscore_126d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 126)

def effa_132_efficiency_rank_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_132_efficiency_rank_rank_126d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 126)

def effa_133_efficiency_rank_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_133_efficiency_rank_lvl_252d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rolling_mean(base, 252)

def effa_134_efficiency_rank_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_134_efficiency_rank_zscore_252d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _zscore_rolling(base, 252)

def effa_135_efficiency_rank_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_135_efficiency_rank_rank_252d"""
    base = _rank_pct(_safe_div(revenue, assets), 252)
    return _rank_pct(base, 252)

def effa_136_efficiency_vol_lvl_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_136_efficiency_vol_lvl_5d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rolling_mean(base, 5)

def effa_137_efficiency_vol_zscore_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_137_efficiency_vol_zscore_5d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _zscore_rolling(base, 5)

def effa_138_efficiency_vol_rank_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_138_efficiency_vol_rank_5d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rank_pct(base, 5)

def effa_139_efficiency_vol_lvl_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_139_efficiency_vol_lvl_21d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rolling_mean(base, 21)

def effa_140_efficiency_vol_zscore_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_140_efficiency_vol_zscore_21d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _zscore_rolling(base, 21)

def effa_141_efficiency_vol_rank_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_141_efficiency_vol_rank_21d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rank_pct(base, 21)

def effa_142_efficiency_vol_lvl_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_142_efficiency_vol_lvl_63d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rolling_mean(base, 63)

def effa_143_efficiency_vol_zscore_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_143_efficiency_vol_zscore_63d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _zscore_rolling(base, 63)

def effa_144_efficiency_vol_rank_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_144_efficiency_vol_rank_63d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rank_pct(base, 63)

def effa_145_efficiency_vol_lvl_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_145_efficiency_vol_lvl_126d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rolling_mean(base, 126)

def effa_146_efficiency_vol_zscore_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_146_efficiency_vol_zscore_126d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _zscore_rolling(base, 126)

def effa_147_efficiency_vol_rank_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_147_efficiency_vol_rank_126d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rank_pct(base, 126)

def effa_148_efficiency_vol_lvl_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_148_efficiency_vol_lvl_252d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rolling_mean(base, 252)

def effa_149_efficiency_vol_zscore_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_149_efficiency_vol_zscore_252d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _zscore_rolling(base, 252)

def effa_150_efficiency_vol_rank_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_150_efficiency_vol_rank_252d"""
    base = _rolling_std(_safe_div(revenue, assets), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V57_REGISTRY_2 = {
    "effa_076_efficiency_accel_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_076_efficiency_accel_lvl_5d},
    "effa_077_efficiency_accel_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_077_efficiency_accel_zscore_5d},
    "effa_078_efficiency_accel_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_078_efficiency_accel_rank_5d},
    "effa_079_efficiency_accel_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_079_efficiency_accel_lvl_21d},
    "effa_080_efficiency_accel_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_080_efficiency_accel_zscore_21d},
    "effa_081_efficiency_accel_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_081_efficiency_accel_rank_21d},
    "effa_082_efficiency_accel_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_082_efficiency_accel_lvl_63d},
    "effa_083_efficiency_accel_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_083_efficiency_accel_zscore_63d},
    "effa_084_efficiency_accel_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_084_efficiency_accel_rank_63d},
    "effa_085_efficiency_accel_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_085_efficiency_accel_lvl_126d},
    "effa_086_efficiency_accel_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_086_efficiency_accel_zscore_126d},
    "effa_087_efficiency_accel_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_087_efficiency_accel_rank_126d},
    "effa_088_efficiency_accel_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_088_efficiency_accel_lvl_252d},
    "effa_089_efficiency_accel_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_089_efficiency_accel_zscore_252d},
    "effa_090_efficiency_accel_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_090_efficiency_accel_rank_252d},
    "effa_091_asset_turnover_z_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_091_asset_turnover_z_lvl_5d},
    "effa_092_asset_turnover_z_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_092_asset_turnover_z_zscore_5d},
    "effa_093_asset_turnover_z_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_093_asset_turnover_z_rank_5d},
    "effa_094_asset_turnover_z_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_094_asset_turnover_z_lvl_21d},
    "effa_095_asset_turnover_z_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_095_asset_turnover_z_zscore_21d},
    "effa_096_asset_turnover_z_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_096_asset_turnover_z_rank_21d},
    "effa_097_asset_turnover_z_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_097_asset_turnover_z_lvl_63d},
    "effa_098_asset_turnover_z_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_098_asset_turnover_z_zscore_63d},
    "effa_099_asset_turnover_z_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_099_asset_turnover_z_rank_63d},
    "effa_100_asset_turnover_z_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_100_asset_turnover_z_lvl_126d},
    "effa_101_asset_turnover_z_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_101_asset_turnover_z_zscore_126d},
    "effa_102_asset_turnover_z_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_102_asset_turnover_z_rank_126d},
    "effa_103_asset_turnover_z_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_103_asset_turnover_z_lvl_252d},
    "effa_104_asset_turnover_z_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_104_asset_turnover_z_zscore_252d},
    "effa_105_asset_turnover_z_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_105_asset_turnover_z_rank_252d},
    "effa_106_inventory_turnover_z_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_106_inventory_turnover_z_lvl_5d},
    "effa_107_inventory_turnover_z_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_107_inventory_turnover_z_zscore_5d},
    "effa_108_inventory_turnover_z_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_108_inventory_turnover_z_rank_5d},
    "effa_109_inventory_turnover_z_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_109_inventory_turnover_z_lvl_21d},
    "effa_110_inventory_turnover_z_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_110_inventory_turnover_z_zscore_21d},
    "effa_111_inventory_turnover_z_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_111_inventory_turnover_z_rank_21d},
    "effa_112_inventory_turnover_z_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_112_inventory_turnover_z_lvl_63d},
    "effa_113_inventory_turnover_z_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_113_inventory_turnover_z_zscore_63d},
    "effa_114_inventory_turnover_z_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_114_inventory_turnover_z_rank_63d},
    "effa_115_inventory_turnover_z_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_115_inventory_turnover_z_lvl_126d},
    "effa_116_inventory_turnover_z_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_116_inventory_turnover_z_zscore_126d},
    "effa_117_inventory_turnover_z_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_117_inventory_turnover_z_rank_126d},
    "effa_118_inventory_turnover_z_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_118_inventory_turnover_z_lvl_252d},
    "effa_119_inventory_turnover_z_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_119_inventory_turnover_z_zscore_252d},
    "effa_120_inventory_turnover_z_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_120_inventory_turnover_z_rank_252d},
    "effa_121_efficiency_rank_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_121_efficiency_rank_lvl_5d},
    "effa_122_efficiency_rank_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_122_efficiency_rank_zscore_5d},
    "effa_123_efficiency_rank_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_123_efficiency_rank_rank_5d},
    "effa_124_efficiency_rank_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_124_efficiency_rank_lvl_21d},
    "effa_125_efficiency_rank_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_125_efficiency_rank_zscore_21d},
    "effa_126_efficiency_rank_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_126_efficiency_rank_rank_21d},
    "effa_127_efficiency_rank_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_127_efficiency_rank_lvl_63d},
    "effa_128_efficiency_rank_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_128_efficiency_rank_zscore_63d},
    "effa_129_efficiency_rank_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_129_efficiency_rank_rank_63d},
    "effa_130_efficiency_rank_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_130_efficiency_rank_lvl_126d},
    "effa_131_efficiency_rank_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_131_efficiency_rank_zscore_126d},
    "effa_132_efficiency_rank_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_132_efficiency_rank_rank_126d},
    "effa_133_efficiency_rank_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_133_efficiency_rank_lvl_252d},
    "effa_134_efficiency_rank_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_134_efficiency_rank_zscore_252d},
    "effa_135_efficiency_rank_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_135_efficiency_rank_rank_252d},
    "effa_136_efficiency_vol_lvl_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_136_efficiency_vol_lvl_5d},
    "effa_137_efficiency_vol_zscore_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_137_efficiency_vol_zscore_5d},
    "effa_138_efficiency_vol_rank_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_138_efficiency_vol_rank_5d},
    "effa_139_efficiency_vol_lvl_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_139_efficiency_vol_lvl_21d},
    "effa_140_efficiency_vol_zscore_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_140_efficiency_vol_zscore_21d},
    "effa_141_efficiency_vol_rank_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_141_efficiency_vol_rank_21d},
    "effa_142_efficiency_vol_lvl_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_142_efficiency_vol_lvl_63d},
    "effa_143_efficiency_vol_zscore_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_143_efficiency_vol_zscore_63d},
    "effa_144_efficiency_vol_rank_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_144_efficiency_vol_rank_63d},
    "effa_145_efficiency_vol_lvl_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_145_efficiency_vol_lvl_126d},
    "effa_146_efficiency_vol_zscore_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_146_efficiency_vol_zscore_126d},
    "effa_147_efficiency_vol_rank_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_147_efficiency_vol_rank_126d},
    "effa_148_efficiency_vol_lvl_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_148_efficiency_vol_lvl_252d},
    "effa_149_efficiency_vol_zscore_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_149_efficiency_vol_zscore_252d},
    "effa_150_efficiency_vol_rank_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_150_efficiency_vol_rank_252d},
}
