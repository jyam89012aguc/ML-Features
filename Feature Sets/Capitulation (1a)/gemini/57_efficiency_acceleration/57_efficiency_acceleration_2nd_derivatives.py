"""
57_efficiency_acceleration — 2nd Derivatives (Velocity)
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

def effa_151_asset_turnover_vel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_151_asset_turnover_vel_5d"""
    return (_safe_div(revenue, assets)).diff(5)

def effa_152_asset_turnover_vel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_152_asset_turnover_vel_21d"""
    return (_safe_div(revenue, assets)).diff(21)

def effa_153_asset_turnover_vel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_153_asset_turnover_vel_63d"""
    return (_safe_div(revenue, assets)).diff(63)

def effa_154_asset_turnover_vel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_154_asset_turnover_vel_126d"""
    return (_safe_div(revenue, assets)).diff(126)

def effa_155_asset_turnover_vel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_155_asset_turnover_vel_252d"""
    return (_safe_div(revenue, assets)).diff(252)

def effa_156_inventory_turnover_vel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_156_inventory_turnover_vel_5d"""
    return (_safe_div(cor, inventory)).diff(5)

def effa_157_inventory_turnover_vel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_157_inventory_turnover_vel_21d"""
    return (_safe_div(cor, inventory)).diff(21)

def effa_158_inventory_turnover_vel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_158_inventory_turnover_vel_63d"""
    return (_safe_div(cor, inventory)).diff(63)

def effa_159_inventory_turnover_vel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_159_inventory_turnover_vel_126d"""
    return (_safe_div(cor, inventory)).diff(126)

def effa_160_inventory_turnover_vel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_160_inventory_turnover_vel_252d"""
    return (_safe_div(cor, inventory)).diff(252)

def effa_161_sales_to_assets_chg_vel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_161_sales_to_assets_chg_vel_5d"""
    return (_safe_div(revenue, assets).diff(252)).diff(5)

def effa_162_sales_to_assets_chg_vel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_162_sales_to_assets_chg_vel_21d"""
    return (_safe_div(revenue, assets).diff(252)).diff(21)

def effa_163_sales_to_assets_chg_vel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_163_sales_to_assets_chg_vel_63d"""
    return (_safe_div(revenue, assets).diff(252)).diff(63)

def effa_164_sales_to_assets_chg_vel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_164_sales_to_assets_chg_vel_126d"""
    return (_safe_div(revenue, assets).diff(252)).diff(126)

def effa_165_sales_to_assets_chg_vel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_165_sales_to_assets_chg_vel_252d"""
    return (_safe_div(revenue, assets).diff(252)).diff(252)

def effa_166_inventory_efficiency_vel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_166_inventory_efficiency_vel_5d"""
    return (_safe_div(revenue, inventory)).diff(5)

def effa_167_inventory_efficiency_vel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_167_inventory_efficiency_vel_21d"""
    return (_safe_div(revenue, inventory)).diff(21)

def effa_168_inventory_efficiency_vel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_168_inventory_efficiency_vel_63d"""
    return (_safe_div(revenue, inventory)).diff(63)

def effa_169_inventory_efficiency_vel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_169_inventory_efficiency_vel_126d"""
    return (_safe_div(revenue, inventory)).diff(126)

def effa_170_inventory_efficiency_vel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_170_inventory_efficiency_vel_252d"""
    return (_safe_div(revenue, inventory)).diff(252)

def effa_171_efficiency_idx_vel_5d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_171_efficiency_idx_vel_5d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(5)

def effa_172_efficiency_idx_vel_21d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_172_efficiency_idx_vel_21d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(21)

def effa_173_efficiency_idx_vel_63d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_173_efficiency_idx_vel_63d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(63)

def effa_174_efficiency_idx_vel_126d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_174_efficiency_idx_vel_126d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(126)

def effa_175_efficiency_idx_vel_252d(revenue: pd.Series, assets: pd.Series, inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """effa_175_efficiency_idx_vel_252d"""
    return (_safe_div(revenue, assets) * _safe_div(cor, inventory)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V57_REGISTRY_VEL = {
    "effa_151_asset_turnover_vel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_151_asset_turnover_vel_5d},
    "effa_152_asset_turnover_vel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_152_asset_turnover_vel_21d},
    "effa_153_asset_turnover_vel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_153_asset_turnover_vel_63d},
    "effa_154_asset_turnover_vel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_154_asset_turnover_vel_126d},
    "effa_155_asset_turnover_vel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_155_asset_turnover_vel_252d},
    "effa_156_inventory_turnover_vel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_156_inventory_turnover_vel_5d},
    "effa_157_inventory_turnover_vel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_157_inventory_turnover_vel_21d},
    "effa_158_inventory_turnover_vel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_158_inventory_turnover_vel_63d},
    "effa_159_inventory_turnover_vel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_159_inventory_turnover_vel_126d},
    "effa_160_inventory_turnover_vel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_160_inventory_turnover_vel_252d},
    "effa_161_sales_to_assets_chg_vel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_161_sales_to_assets_chg_vel_5d},
    "effa_162_sales_to_assets_chg_vel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_162_sales_to_assets_chg_vel_21d},
    "effa_163_sales_to_assets_chg_vel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_163_sales_to_assets_chg_vel_63d},
    "effa_164_sales_to_assets_chg_vel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_164_sales_to_assets_chg_vel_126d},
    "effa_165_sales_to_assets_chg_vel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_165_sales_to_assets_chg_vel_252d},
    "effa_166_inventory_efficiency_vel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_166_inventory_efficiency_vel_5d},
    "effa_167_inventory_efficiency_vel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_167_inventory_efficiency_vel_21d},
    "effa_168_inventory_efficiency_vel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_168_inventory_efficiency_vel_63d},
    "effa_169_inventory_efficiency_vel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_169_inventory_efficiency_vel_126d},
    "effa_170_inventory_efficiency_vel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_170_inventory_efficiency_vel_252d},
    "effa_171_efficiency_idx_vel_5d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_171_efficiency_idx_vel_5d},
    "effa_172_efficiency_idx_vel_21d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_172_efficiency_idx_vel_21d},
    "effa_173_efficiency_idx_vel_63d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_173_efficiency_idx_vel_63d},
    "effa_174_efficiency_idx_vel_126d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_174_efficiency_idx_vel_126d},
    "effa_175_efficiency_idx_vel_252d": {"inputs": ["revenue", "assets", "inventory", "cor"], "func": effa_175_efficiency_idx_vel_252d},
}
