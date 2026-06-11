"""
54_margin_acceleration — 3rd Derivatives (Acceleration)
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

def maga_176_net_margin_accel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_176_net_margin_accel_5d"""
    return (_safe_div(netinc, revenue)).diff(5).diff(21)

def maga_177_net_margin_accel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_177_net_margin_accel_21d"""
    return (_safe_div(netinc, revenue)).diff(21).diff(21)

def maga_178_net_margin_accel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_178_net_margin_accel_63d"""
    return (_safe_div(netinc, revenue)).diff(63).diff(21)

def maga_179_net_margin_accel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_179_net_margin_accel_126d"""
    return (_safe_div(netinc, revenue)).diff(126).diff(21)

def maga_180_net_margin_accel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_180_net_margin_accel_252d"""
    return (_safe_div(netinc, revenue)).diff(252).diff(21)

def maga_181_op_margin_accel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_181_op_margin_accel_5d"""
    return (_safe_div(opinc, revenue)).diff(5).diff(21)

def maga_182_op_margin_accel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_182_op_margin_accel_21d"""
    return (_safe_div(opinc, revenue)).diff(21).diff(21)

def maga_183_op_margin_accel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_183_op_margin_accel_63d"""
    return (_safe_div(opinc, revenue)).diff(63).diff(21)

def maga_184_op_margin_accel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_184_op_margin_accel_126d"""
    return (_safe_div(opinc, revenue)).diff(126).diff(21)

def maga_185_op_margin_accel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_185_op_margin_accel_252d"""
    return (_safe_div(opinc, revenue)).diff(252).diff(21)

def maga_186_gross_margin_accel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_186_gross_margin_accel_5d"""
    return (_safe_div(revenue - cor, revenue)).diff(5).diff(21)

def maga_187_gross_margin_accel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_187_gross_margin_accel_21d"""
    return (_safe_div(revenue - cor, revenue)).diff(21).diff(21)

def maga_188_gross_margin_accel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_188_gross_margin_accel_63d"""
    return (_safe_div(revenue - cor, revenue)).diff(63).diff(21)

def maga_189_gross_margin_accel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_189_gross_margin_accel_126d"""
    return (_safe_div(revenue - cor, revenue)).diff(126).diff(21)

def maga_190_gross_margin_accel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_190_gross_margin_accel_252d"""
    return (_safe_div(revenue - cor, revenue)).diff(252).diff(21)

def maga_191_margin_yoy_chg_accel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_191_margin_yoy_chg_accel_5d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(5).diff(21)

def maga_192_margin_yoy_chg_accel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_192_margin_yoy_chg_accel_21d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(21).diff(21)

def maga_193_margin_yoy_chg_accel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_193_margin_yoy_chg_accel_63d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(63).diff(21)

def maga_194_margin_yoy_chg_accel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_194_margin_yoy_chg_accel_126d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(126).diff(21)

def maga_195_margin_yoy_chg_accel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_195_margin_yoy_chg_accel_252d"""
    return (_safe_div(netinc, revenue).diff(252)).diff(252).diff(21)

def maga_196_margin_qoq_chg_accel_5d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_196_margin_qoq_chg_accel_5d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(5).diff(21)

def maga_197_margin_qoq_chg_accel_21d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_197_margin_qoq_chg_accel_21d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(21).diff(21)

def maga_198_margin_qoq_chg_accel_63d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_198_margin_qoq_chg_accel_63d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(63).diff(21)

def maga_199_margin_qoq_chg_accel_126d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_199_margin_qoq_chg_accel_126d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(126).diff(21)

def maga_200_margin_qoq_chg_accel_252d(netinc: pd.Series, revenue: pd.Series, opinc: pd.Series, cor: pd.Series) -> pd.Series:
    """maga_200_margin_qoq_chg_accel_252d"""
    return (_safe_div(netinc, revenue).diff(63)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V54_REGISTRY_ACCEL = {
    "maga_176_net_margin_accel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_176_net_margin_accel_5d},
    "maga_177_net_margin_accel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_177_net_margin_accel_21d},
    "maga_178_net_margin_accel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_178_net_margin_accel_63d},
    "maga_179_net_margin_accel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_179_net_margin_accel_126d},
    "maga_180_net_margin_accel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_180_net_margin_accel_252d},
    "maga_181_op_margin_accel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_181_op_margin_accel_5d},
    "maga_182_op_margin_accel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_182_op_margin_accel_21d},
    "maga_183_op_margin_accel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_183_op_margin_accel_63d},
    "maga_184_op_margin_accel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_184_op_margin_accel_126d},
    "maga_185_op_margin_accel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_185_op_margin_accel_252d},
    "maga_186_gross_margin_accel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_186_gross_margin_accel_5d},
    "maga_187_gross_margin_accel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_187_gross_margin_accel_21d},
    "maga_188_gross_margin_accel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_188_gross_margin_accel_63d},
    "maga_189_gross_margin_accel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_189_gross_margin_accel_126d},
    "maga_190_gross_margin_accel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_190_gross_margin_accel_252d},
    "maga_191_margin_yoy_chg_accel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_191_margin_yoy_chg_accel_5d},
    "maga_192_margin_yoy_chg_accel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_192_margin_yoy_chg_accel_21d},
    "maga_193_margin_yoy_chg_accel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_193_margin_yoy_chg_accel_63d},
    "maga_194_margin_yoy_chg_accel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_194_margin_yoy_chg_accel_126d},
    "maga_195_margin_yoy_chg_accel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_195_margin_yoy_chg_accel_252d},
    "maga_196_margin_qoq_chg_accel_5d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_196_margin_qoq_chg_accel_5d},
    "maga_197_margin_qoq_chg_accel_21d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_197_margin_qoq_chg_accel_21d},
    "maga_198_margin_qoq_chg_accel_63d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_198_margin_qoq_chg_accel_63d},
    "maga_199_margin_qoq_chg_accel_126d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_199_margin_qoq_chg_accel_126d},
    "maga_200_margin_qoq_chg_accel_252d": {"inputs": ["netinc", "revenue", "opinc", "cor"], "func": maga_200_margin_qoq_chg_accel_252d},
}
