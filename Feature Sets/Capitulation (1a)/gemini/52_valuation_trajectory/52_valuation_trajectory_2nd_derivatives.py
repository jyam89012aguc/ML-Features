"""
52_valuation_trajectory — 2nd Derivatives (Velocity)
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

def valt_151_ps_ratio_vel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_151_ps_ratio_vel_5d"""
    return (ps).diff(5)

def valt_152_ps_ratio_vel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_152_ps_ratio_vel_21d"""
    return (ps).diff(21)

def valt_153_ps_ratio_vel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_153_ps_ratio_vel_63d"""
    return (ps).diff(63)

def valt_154_ps_ratio_vel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_154_ps_ratio_vel_126d"""
    return (ps).diff(126)

def valt_155_ps_ratio_vel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_155_ps_ratio_vel_252d"""
    return (ps).diff(252)

def valt_156_pb_ratio_vel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_156_pb_ratio_vel_5d"""
    return (pb).diff(5)

def valt_157_pb_ratio_vel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_157_pb_ratio_vel_21d"""
    return (pb).diff(21)

def valt_158_pb_ratio_vel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_158_pb_ratio_vel_63d"""
    return (pb).diff(63)

def valt_159_pb_ratio_vel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_159_pb_ratio_vel_126d"""
    return (pb).diff(126)

def valt_160_pb_ratio_vel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_160_pb_ratio_vel_252d"""
    return (pb).diff(252)

def valt_161_pe_ratio_vel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_161_pe_ratio_vel_5d"""
    return (_safe_div(marketcap, netinc)).diff(5)

def valt_162_pe_ratio_vel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_162_pe_ratio_vel_21d"""
    return (_safe_div(marketcap, netinc)).diff(21)

def valt_163_pe_ratio_vel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_163_pe_ratio_vel_63d"""
    return (_safe_div(marketcap, netinc)).diff(63)

def valt_164_pe_ratio_vel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_164_pe_ratio_vel_126d"""
    return (_safe_div(marketcap, netinc)).diff(126)

def valt_165_pe_ratio_vel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_165_pe_ratio_vel_252d"""
    return (_safe_div(marketcap, netinc)).diff(252)

def valt_166_ev_rev_vel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_166_ev_rev_vel_5d"""
    return (_safe_div(marketcap, revenue)).diff(5)

def valt_167_ev_rev_vel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_167_ev_rev_vel_21d"""
    return (_safe_div(marketcap, revenue)).diff(21)

def valt_168_ev_rev_vel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_168_ev_rev_vel_63d"""
    return (_safe_div(marketcap, revenue)).diff(63)

def valt_169_ev_rev_vel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_169_ev_rev_vel_126d"""
    return (_safe_div(marketcap, revenue)).diff(126)

def valt_170_ev_rev_vel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_170_ev_rev_vel_252d"""
    return (_safe_div(marketcap, revenue)).diff(252)

def valt_171_yield_ocf_vel_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_171_yield_ocf_vel_5d"""
    return (_safe_div(ocf, marketcap)).diff(5)

def valt_172_yield_ocf_vel_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_172_yield_ocf_vel_21d"""
    return (_safe_div(ocf, marketcap)).diff(21)

def valt_173_yield_ocf_vel_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_173_yield_ocf_vel_63d"""
    return (_safe_div(ocf, marketcap)).diff(63)

def valt_174_yield_ocf_vel_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_174_yield_ocf_vel_126d"""
    return (_safe_div(ocf, marketcap)).diff(126)

def valt_175_yield_ocf_vel_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_175_yield_ocf_vel_252d"""
    return (_safe_div(ocf, marketcap)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V52_REGISTRY_VEL = {
    "valt_151_ps_ratio_vel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_151_ps_ratio_vel_5d},
    "valt_152_ps_ratio_vel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_152_ps_ratio_vel_21d},
    "valt_153_ps_ratio_vel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_153_ps_ratio_vel_63d},
    "valt_154_ps_ratio_vel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_154_ps_ratio_vel_126d},
    "valt_155_ps_ratio_vel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_155_ps_ratio_vel_252d},
    "valt_156_pb_ratio_vel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_156_pb_ratio_vel_5d},
    "valt_157_pb_ratio_vel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_157_pb_ratio_vel_21d},
    "valt_158_pb_ratio_vel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_158_pb_ratio_vel_63d},
    "valt_159_pb_ratio_vel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_159_pb_ratio_vel_126d},
    "valt_160_pb_ratio_vel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_160_pb_ratio_vel_252d},
    "valt_161_pe_ratio_vel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_161_pe_ratio_vel_5d},
    "valt_162_pe_ratio_vel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_162_pe_ratio_vel_21d},
    "valt_163_pe_ratio_vel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_163_pe_ratio_vel_63d},
    "valt_164_pe_ratio_vel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_164_pe_ratio_vel_126d},
    "valt_165_pe_ratio_vel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_165_pe_ratio_vel_252d},
    "valt_166_ev_rev_vel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_166_ev_rev_vel_5d},
    "valt_167_ev_rev_vel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_167_ev_rev_vel_21d},
    "valt_168_ev_rev_vel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_168_ev_rev_vel_63d},
    "valt_169_ev_rev_vel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_169_ev_rev_vel_126d},
    "valt_170_ev_rev_vel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_170_ev_rev_vel_252d},
    "valt_171_yield_ocf_vel_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_171_yield_ocf_vel_5d},
    "valt_172_yield_ocf_vel_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_172_yield_ocf_vel_21d},
    "valt_173_yield_ocf_vel_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_173_yield_ocf_vel_63d},
    "valt_174_yield_ocf_vel_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_174_yield_ocf_vel_126d},
    "valt_175_yield_ocf_vel_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_175_yield_ocf_vel_252d},
}
