"""
57_efficiency_acceleration — 3rd Derivatives (Acceleration)
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

def effa_176_asset_turnover_accel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_176_asset_turnover_accel_5d"""
    return (_safe_div(revenue, assets)).diff(5).diff(21)

def effa_177_asset_turnover_accel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_177_asset_turnover_accel_21d"""
    return (_safe_div(revenue, assets)).diff(21).diff(21)

def effa_178_asset_turnover_accel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_178_asset_turnover_accel_63d"""
    return (_safe_div(revenue, assets)).diff(63).diff(21)

def effa_179_asset_turnover_accel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_179_asset_turnover_accel_126d"""
    return (_safe_div(revenue, assets)).diff(126).diff(21)

def effa_180_asset_turnover_accel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_180_asset_turnover_accel_252d"""
    return (_safe_div(revenue, assets)).diff(252).diff(21)

def effa_181_inventory_turnover_accel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_181_inventory_turnover_accel_5d"""
    return (_safe_div(cor, inventory)).diff(5).diff(21)

def effa_182_inventory_turnover_accel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_182_inventory_turnover_accel_21d"""
    return (_safe_div(cor, inventory)).diff(21).diff(21)

def effa_183_inventory_turnover_accel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_183_inventory_turnover_accel_63d"""
    return (_safe_div(cor, inventory)).diff(63).diff(21)

def effa_184_inventory_turnover_accel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_184_inventory_turnover_accel_126d"""
    return (_safe_div(cor, inventory)).diff(126).diff(21)

def effa_185_inventory_turnover_accel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_185_inventory_turnover_accel_252d"""
    return (_safe_div(cor, inventory)).diff(252).diff(21)

def effa_186_sales_to_assets_chg_accel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_186_sales_to_assets_chg_accel_5d"""
    return (_safe_div(revenue, assets).diff(252)).diff(5).diff(21)

def effa_187_sales_to_assets_chg_accel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_187_sales_to_assets_chg_accel_21d"""
    return (_safe_div(revenue, assets).diff(252)).diff(21).diff(21)

def effa_188_sales_to_assets_chg_accel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_188_sales_to_assets_chg_accel_63d"""
    return (_safe_div(revenue, assets).diff(252)).diff(63).diff(21)

def effa_189_sales_to_assets_chg_accel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_189_sales_to_assets_chg_accel_126d"""
    return (_safe_div(revenue, assets).diff(252)).diff(126).diff(21)

def effa_190_sales_to_assets_chg_accel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_190_sales_to_assets_chg_accel_252d"""
    return (_safe_div(revenue, assets).diff(252)).diff(252).diff(21)

def effa_191_inventory_efficiency_accel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_191_inventory_efficiency_accel_5d"""
    return (_safe_div(revenue, inventory)).diff(5).diff(21)

def effa_192_inventory_efficiency_accel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_192_inventory_efficiency_accel_21d"""
    return (_safe_div(revenue, inventory)).diff(21).diff(21)

def effa_193_inventory_efficiency_accel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_193_inventory_efficiency_accel_63d"""
    return (_safe_div(revenue, inventory)).diff(63).diff(21)

def effa_194_inventory_efficiency_accel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_194_inventory_efficiency_accel_126d"""
    return (_safe_div(revenue, inventory)).diff(126).diff(21)

def effa_195_inventory_efficiency_accel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_195_inventory_efficiency_accel_252d"""
    return (_safe_div(revenue, inventory)).diff(252).diff(21)

def effa_196_efficiency_idx_accel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_196_efficiency_idx_accel_5d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(5).diff(21)

def effa_197_efficiency_idx_accel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_197_efficiency_idx_accel_21d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(21).diff(21)

def effa_198_efficiency_idx_accel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_198_efficiency_idx_accel_63d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(63).diff(21)

def effa_199_efficiency_idx_accel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_199_efficiency_idx_accel_126d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(126).diff(21)

def effa_200_efficiency_idx_accel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_200_efficiency_idx_accel_252d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V57_REGISTRY_ACCEL = {
    "effa_176_asset_turnover_accel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_176_asset_turnover_accel_5d},
    "effa_177_asset_turnover_accel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_177_asset_turnover_accel_21d},
    "effa_178_asset_turnover_accel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_178_asset_turnover_accel_63d},
    "effa_179_asset_turnover_accel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_179_asset_turnover_accel_126d},
    "effa_180_asset_turnover_accel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_180_asset_turnover_accel_252d},
    "effa_181_inventory_turnover_accel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_181_inventory_turnover_accel_5d},
    "effa_182_inventory_turnover_accel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_182_inventory_turnover_accel_21d},
    "effa_183_inventory_turnover_accel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_183_inventory_turnover_accel_63d},
    "effa_184_inventory_turnover_accel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_184_inventory_turnover_accel_126d},
    "effa_185_inventory_turnover_accel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_185_inventory_turnover_accel_252d},
    "effa_186_sales_to_assets_chg_accel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_186_sales_to_assets_chg_accel_5d},
    "effa_187_sales_to_assets_chg_accel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_187_sales_to_assets_chg_accel_21d},
    "effa_188_sales_to_assets_chg_accel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_188_sales_to_assets_chg_accel_63d},
    "effa_189_sales_to_assets_chg_accel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_189_sales_to_assets_chg_accel_126d},
    "effa_190_sales_to_assets_chg_accel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_190_sales_to_assets_chg_accel_252d},
    "effa_191_inventory_efficiency_accel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_191_inventory_efficiency_accel_5d},
    "effa_192_inventory_efficiency_accel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_192_inventory_efficiency_accel_21d},
    "effa_193_inventory_efficiency_accel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_193_inventory_efficiency_accel_63d},
    "effa_194_inventory_efficiency_accel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_194_inventory_efficiency_accel_126d},
    "effa_195_inventory_efficiency_accel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_195_inventory_efficiency_accel_252d},
    "effa_196_efficiency_idx_accel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_196_efficiency_idx_accel_5d},
    "effa_197_efficiency_idx_accel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_197_efficiency_idx_accel_21d},
    "effa_198_efficiency_idx_accel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_198_efficiency_idx_accel_63d},
    "effa_199_efficiency_idx_accel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_199_efficiency_idx_accel_126d},
    "effa_200_efficiency_idx_accel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_200_efficiency_idx_accel_252d},
}
