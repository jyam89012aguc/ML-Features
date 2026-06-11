"""
52_valuation_trajectory — 3rd Derivatives (Acceleration)
Domain: valuation_trajectory
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

def valt_176_ps_ratio_accel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_176_ps_ratio_accel_5d"""
    return (ps).diff(5).diff(21)

def valt_177_ps_ratio_accel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_177_ps_ratio_accel_21d"""
    return (ps).diff(21).diff(21)

def valt_178_ps_ratio_accel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_178_ps_ratio_accel_63d"""
    return (ps).diff(63).diff(21)

def valt_179_ps_ratio_accel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_179_ps_ratio_accel_126d"""
    return (ps).diff(126).diff(21)

def valt_180_ps_ratio_accel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_180_ps_ratio_accel_252d"""
    return (ps).diff(252).diff(21)

def valt_181_pb_ratio_accel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_181_pb_ratio_accel_5d"""
    return (pb).diff(5).diff(21)

def valt_182_pb_ratio_accel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_182_pb_ratio_accel_21d"""
    return (pb).diff(21).diff(21)

def valt_183_pb_ratio_accel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_183_pb_ratio_accel_63d"""
    return (pb).diff(63).diff(21)

def valt_184_pb_ratio_accel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_184_pb_ratio_accel_126d"""
    return (pb).diff(126).diff(21)

def valt_185_pb_ratio_accel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_185_pb_ratio_accel_252d"""
    return (pb).diff(252).diff(21)

def valt_186_pe_ratio_accel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_186_pe_ratio_accel_5d"""
    return (_safe_div(marketcap, netinc)).diff(5).diff(21)

def valt_187_pe_ratio_accel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_187_pe_ratio_accel_21d"""
    return (_safe_div(marketcap, netinc)).diff(21).diff(21)

def valt_188_pe_ratio_accel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_188_pe_ratio_accel_63d"""
    return (_safe_div(marketcap, netinc)).diff(63).diff(21)

def valt_189_pe_ratio_accel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_189_pe_ratio_accel_126d"""
    return (_safe_div(marketcap, netinc)).diff(126).diff(21)

def valt_190_pe_ratio_accel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_190_pe_ratio_accel_252d"""
    return (_safe_div(marketcap, netinc)).diff(252).diff(21)

def valt_191_ev_rev_accel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_191_ev_rev_accel_5d"""
    return (_safe_div(marketcap, revenue)).diff(5).diff(21)

def valt_192_ev_rev_accel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_192_ev_rev_accel_21d"""
    return (_safe_div(marketcap, revenue)).diff(21).diff(21)

def valt_193_ev_rev_accel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_193_ev_rev_accel_63d"""
    return (_safe_div(marketcap, revenue)).diff(63).diff(21)

def valt_194_ev_rev_accel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_194_ev_rev_accel_126d"""
    return (_safe_div(marketcap, revenue)).diff(126).diff(21)

def valt_195_ev_rev_accel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_195_ev_rev_accel_252d"""
    return (_safe_div(marketcap, revenue)).diff(252).diff(21)

def valt_196_yield_ocf_accel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_196_yield_ocf_accel_5d"""
    return (_safe_div(ocf, marketcap)).diff(5).diff(21)

def valt_197_yield_ocf_accel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_197_yield_ocf_accel_21d"""
    return (_safe_div(ocf, marketcap)).diff(21).diff(21)

def valt_198_yield_ocf_accel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_198_yield_ocf_accel_63d"""
    return (_safe_div(ocf, marketcap)).diff(63).diff(21)

def valt_199_yield_ocf_accel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_199_yield_ocf_accel_126d"""
    return (_safe_div(ocf, marketcap)).diff(126).diff(21)

def valt_200_yield_ocf_accel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_200_yield_ocf_accel_252d"""
    return (_safe_div(ocf, marketcap)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V52_REGISTRY_ACCEL = {
    "valt_176_ps_ratio_accel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_176_ps_ratio_accel_5d},
    "valt_177_ps_ratio_accel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_177_ps_ratio_accel_21d},
    "valt_178_ps_ratio_accel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_178_ps_ratio_accel_63d},
    "valt_179_ps_ratio_accel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_179_ps_ratio_accel_126d},
    "valt_180_ps_ratio_accel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_180_ps_ratio_accel_252d},
    "valt_181_pb_ratio_accel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_181_pb_ratio_accel_5d},
    "valt_182_pb_ratio_accel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_182_pb_ratio_accel_21d},
    "valt_183_pb_ratio_accel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_183_pb_ratio_accel_63d},
    "valt_184_pb_ratio_accel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_184_pb_ratio_accel_126d},
    "valt_185_pb_ratio_accel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_185_pb_ratio_accel_252d},
    "valt_186_pe_ratio_accel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_186_pe_ratio_accel_5d},
    "valt_187_pe_ratio_accel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_187_pe_ratio_accel_21d},
    "valt_188_pe_ratio_accel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_188_pe_ratio_accel_63d},
    "valt_189_pe_ratio_accel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_189_pe_ratio_accel_126d},
    "valt_190_pe_ratio_accel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_190_pe_ratio_accel_252d},
    "valt_191_ev_rev_accel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_191_ev_rev_accel_5d},
    "valt_192_ev_rev_accel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_192_ev_rev_accel_21d},
    "valt_193_ev_rev_accel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_193_ev_rev_accel_63d},
    "valt_194_ev_rev_accel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_194_ev_rev_accel_126d},
    "valt_195_ev_rev_accel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_195_ev_rev_accel_252d},
    "valt_196_yield_ocf_accel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_196_yield_ocf_accel_5d},
    "valt_197_yield_ocf_accel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_197_yield_ocf_accel_21d},
    "valt_198_yield_ocf_accel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_198_yield_ocf_accel_63d},
    "valt_199_yield_ocf_accel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_199_yield_ocf_accel_126d},
    "valt_200_yield_ocf_accel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_200_yield_ocf_accel_252d},
}
