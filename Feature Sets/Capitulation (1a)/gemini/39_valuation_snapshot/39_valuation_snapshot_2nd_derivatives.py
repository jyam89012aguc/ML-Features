"""
39_valuation_snapshot — 2nd Derivatives (Velocity)
Domain: valuation_snapshot
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

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def valn_151_ps_vel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_151_ps_vel_5d"""
    return (ps).diff(5)

def valn_152_ps_vel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_152_ps_vel_21d"""
    return (ps).diff(21)

def valn_153_ps_vel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_153_ps_vel_63d"""
    return (ps).diff(63)

def valn_154_ps_vel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_154_ps_vel_126d"""
    return (ps).diff(126)

def valn_155_ps_vel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_155_ps_vel_252d"""
    return (ps).diff(252)

def valn_156_pb_vel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_156_pb_vel_5d"""
    return (pb).diff(5)

def valn_157_pb_vel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_157_pb_vel_21d"""
    return (pb).diff(21)

def valn_158_pb_vel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_158_pb_vel_63d"""
    return (pb).diff(63)

def valn_159_pb_vel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_159_pb_vel_126d"""
    return (pb).diff(126)

def valn_160_pb_vel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_160_pb_vel_252d"""
    return (pb).diff(252)

def valn_161_pe_vel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_161_pe_vel_5d"""
    return (pe).diff(5)

def valn_162_pe_vel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_162_pe_vel_21d"""
    return (pe).diff(21)

def valn_163_pe_vel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_163_pe_vel_63d"""
    return (pe).diff(63)

def valn_164_pe_vel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_164_pe_vel_126d"""
    return (pe).diff(126)

def valn_165_pe_vel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_165_pe_vel_252d"""
    return (pe).diff(252)

def valn_166_evebitda_vel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_166_evebitda_vel_5d"""
    return (evebitda).diff(5)

def valn_167_evebitda_vel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_167_evebitda_vel_21d"""
    return (evebitda).diff(21)

def valn_168_evebitda_vel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_168_evebitda_vel_63d"""
    return (evebitda).diff(63)

def valn_169_evebitda_vel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_169_evebitda_vel_126d"""
    return (evebitda).diff(126)

def valn_170_evebitda_vel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_170_evebitda_vel_252d"""
    return (evebitda).diff(252)

def valn_171_earn_yield_vel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_171_earn_yield_vel_5d"""
    return (_safe_div(1.0, pe)).diff(5)

def valn_172_earn_yield_vel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_172_earn_yield_vel_21d"""
    return (_safe_div(1.0, pe)).diff(21)

def valn_173_earn_yield_vel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_173_earn_yield_vel_63d"""
    return (_safe_div(1.0, pe)).diff(63)

def valn_174_earn_yield_vel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_174_earn_yield_vel_126d"""
    return (_safe_div(1.0, pe)).diff(126)

def valn_175_earn_yield_vel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_175_earn_yield_vel_252d"""
    return (_safe_div(1.0, pe)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V39_REGISTRY_VEL = {
    "valn_151_ps_vel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_151_ps_vel_5d},
    "valn_152_ps_vel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_152_ps_vel_21d},
    "valn_153_ps_vel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_153_ps_vel_63d},
    "valn_154_ps_vel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_154_ps_vel_126d},
    "valn_155_ps_vel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_155_ps_vel_252d},
    "valn_156_pb_vel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_156_pb_vel_5d},
    "valn_157_pb_vel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_157_pb_vel_21d},
    "valn_158_pb_vel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_158_pb_vel_63d},
    "valn_159_pb_vel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_159_pb_vel_126d},
    "valn_160_pb_vel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_160_pb_vel_252d},
    "valn_161_pe_vel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_161_pe_vel_5d},
    "valn_162_pe_vel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_162_pe_vel_21d},
    "valn_163_pe_vel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_163_pe_vel_63d},
    "valn_164_pe_vel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_164_pe_vel_126d},
    "valn_165_pe_vel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_165_pe_vel_252d},
    "valn_166_evebitda_vel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_166_evebitda_vel_5d},
    "valn_167_evebitda_vel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_167_evebitda_vel_21d},
    "valn_168_evebitda_vel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_168_evebitda_vel_63d},
    "valn_169_evebitda_vel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_169_evebitda_vel_126d},
    "valn_170_evebitda_vel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_170_evebitda_vel_252d},
    "valn_171_earn_yield_vel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_171_earn_yield_vel_5d},
    "valn_172_earn_yield_vel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_172_earn_yield_vel_21d},
    "valn_173_earn_yield_vel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_173_earn_yield_vel_63d},
    "valn_174_earn_yield_vel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_174_earn_yield_vel_126d},
    "valn_175_earn_yield_vel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_175_earn_yield_vel_252d},
}
