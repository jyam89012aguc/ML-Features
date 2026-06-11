"""
54_margin_acceleration — 2nd Derivatives (Velocity)
Domain: margin_acceleration
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

def maga_151_net_margin_vel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_151_net_margin_vel_5d"""
    return (_safe_div(netinc, revenue)).diff(5)

def maga_152_net_margin_vel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_152_net_margin_vel_21d"""
    return (_safe_div(netinc, revenue)).diff(21)

def maga_153_net_margin_vel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_153_net_margin_vel_63d"""
    return (_safe_div(netinc, revenue)).diff(63)

def maga_154_net_margin_vel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_154_net_margin_vel_126d"""
    return (_safe_div(netinc, revenue)).diff(126)

def maga_155_net_margin_vel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_155_net_margin_vel_252d"""
    return (_safe_div(netinc, revenue)).diff(252)

def maga_156_op_margin_vel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_156_op_margin_vel_5d"""
    return (_safe_div(opinc, revenue)).diff(5)

def maga_157_op_margin_vel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_157_op_margin_vel_21d"""
    return (_safe_div(opinc, revenue)).diff(21)

def maga_158_op_margin_vel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_158_op_margin_vel_63d"""
    return (_safe_div(opinc, revenue)).diff(63)

def maga_159_op_margin_vel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_159_op_margin_vel_126d"""
    return (_safe_div(opinc, revenue)).diff(126)

def maga_160_op_margin_vel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_160_op_margin_vel_252d"""
    return (_safe_div(opinc, revenue)).diff(252)

def maga_161_gross_margin_vel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_161_gross_margin_vel_5d"""
    return (_safe_div(revenue - cor, revenue)).diff(5)

def maga_162_gross_margin_vel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_162_gross_margin_vel_21d"""
    return (_safe_div(revenue - cor, revenue)).diff(21)

def maga_163_gross_margin_vel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_163_gross_margin_vel_63d"""
    return (_safe_div(revenue - cor, revenue)).diff(63)

def maga_164_gross_margin_vel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_164_gross_margin_vel_126d"""
    return (_safe_div(revenue - cor, revenue)).diff(126)

def maga_165_gross_margin_vel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_165_gross_margin_vel_252d"""
    return (_safe_div(revenue - cor, revenue)).diff(252)

def maga_166_margin_yoy_chg_vel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_166_margin_yoy_chg_vel_5d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(5)

def maga_167_margin_yoy_chg_vel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_167_margin_yoy_chg_vel_21d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(21)

def maga_168_margin_yoy_chg_vel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_168_margin_yoy_chg_vel_63d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(63)

def maga_169_margin_yoy_chg_vel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_169_margin_yoy_chg_vel_126d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(126)

def maga_170_margin_yoy_chg_vel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_170_margin_yoy_chg_vel_252d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(252)

def maga_171_margin_qoq_chg_vel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_171_margin_qoq_chg_vel_5d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(5)

def maga_172_margin_qoq_chg_vel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_172_margin_qoq_chg_vel_21d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(21)

def maga_173_margin_qoq_chg_vel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_173_margin_qoq_chg_vel_63d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(63)

def maga_174_margin_qoq_chg_vel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_174_margin_qoq_chg_vel_126d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(126)

def maga_175_margin_qoq_chg_vel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_175_margin_qoq_chg_vel_252d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V54_REGISTRY_VEL = {
    "maga_151_net_margin_vel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_151_net_margin_vel_5d},
    "maga_152_net_margin_vel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_152_net_margin_vel_21d},
    "maga_153_net_margin_vel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_153_net_margin_vel_63d},
    "maga_154_net_margin_vel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_154_net_margin_vel_126d},
    "maga_155_net_margin_vel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_155_net_margin_vel_252d},
    "maga_156_op_margin_vel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_156_op_margin_vel_5d},
    "maga_157_op_margin_vel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_157_op_margin_vel_21d},
    "maga_158_op_margin_vel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_158_op_margin_vel_63d},
    "maga_159_op_margin_vel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_159_op_margin_vel_126d},
    "maga_160_op_margin_vel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_160_op_margin_vel_252d},
    "maga_161_gross_margin_vel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_161_gross_margin_vel_5d},
    "maga_162_gross_margin_vel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_162_gross_margin_vel_21d},
    "maga_163_gross_margin_vel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_163_gross_margin_vel_63d},
    "maga_164_gross_margin_vel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_164_gross_margin_vel_126d},
    "maga_165_gross_margin_vel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_165_gross_margin_vel_252d},
    "maga_166_margin_yoy_chg_vel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_166_margin_yoy_chg_vel_5d},
    "maga_167_margin_yoy_chg_vel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_167_margin_yoy_chg_vel_21d},
    "maga_168_margin_yoy_chg_vel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_168_margin_yoy_chg_vel_63d},
    "maga_169_margin_yoy_chg_vel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_169_margin_yoy_chg_vel_126d},
    "maga_170_margin_yoy_chg_vel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_170_margin_yoy_chg_vel_252d},
    "maga_171_margin_qoq_chg_vel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_171_margin_qoq_chg_vel_5d},
    "maga_172_margin_qoq_chg_vel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_172_margin_qoq_chg_vel_21d},
    "maga_173_margin_qoq_chg_vel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_173_margin_qoq_chg_vel_63d},
    "maga_174_margin_qoq_chg_vel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_174_margin_qoq_chg_vel_126d},
    "maga_175_margin_qoq_chg_vel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_175_margin_qoq_chg_vel_252d},
}
