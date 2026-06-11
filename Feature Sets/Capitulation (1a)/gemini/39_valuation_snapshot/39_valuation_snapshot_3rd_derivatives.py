"""
39_valuation_snapshot — 3rd Derivatives (Acceleration)
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

def valn_176_ps_accel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_176_ps_accel_5d"""
    return (ps).diff(5).diff(21)

def valn_177_ps_accel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_177_ps_accel_21d"""
    return (ps).diff(21).diff(21)

def valn_178_ps_accel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_178_ps_accel_63d"""
    return (ps).diff(63).diff(21)

def valn_179_ps_accel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_179_ps_accel_126d"""
    return (ps).diff(126).diff(21)

def valn_180_ps_accel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_180_ps_accel_252d"""
    return (ps).diff(252).diff(21)

def valn_181_pb_accel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_181_pb_accel_5d"""
    return (pb).diff(5).diff(21)

def valn_182_pb_accel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_182_pb_accel_21d"""
    return (pb).diff(21).diff(21)

def valn_183_pb_accel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_183_pb_accel_63d"""
    return (pb).diff(63).diff(21)

def valn_184_pb_accel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_184_pb_accel_126d"""
    return (pb).diff(126).diff(21)

def valn_185_pb_accel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_185_pb_accel_252d"""
    return (pb).diff(252).diff(21)

def valn_186_pe_accel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_186_pe_accel_5d"""
    return (pe).diff(5).diff(21)

def valn_187_pe_accel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_187_pe_accel_21d"""
    return (pe).diff(21).diff(21)

def valn_188_pe_accel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_188_pe_accel_63d"""
    return (pe).diff(63).diff(21)

def valn_189_pe_accel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_189_pe_accel_126d"""
    return (pe).diff(126).diff(21)

def valn_190_pe_accel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_190_pe_accel_252d"""
    return (pe).diff(252).diff(21)

def valn_191_evebitda_accel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_191_evebitda_accel_5d"""
    return (evebitda).diff(5).diff(21)

def valn_192_evebitda_accel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_192_evebitda_accel_21d"""
    return (evebitda).diff(21).diff(21)

def valn_193_evebitda_accel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_193_evebitda_accel_63d"""
    return (evebitda).diff(63).diff(21)

def valn_194_evebitda_accel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_194_evebitda_accel_126d"""
    return (evebitda).diff(126).diff(21)

def valn_195_evebitda_accel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_195_evebitda_accel_252d"""
    return (evebitda).diff(252).diff(21)

def valn_196_earn_yield_accel_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_196_earn_yield_accel_5d"""
    return (_safe_div(1.0, pe)).diff(5).diff(21)

def valn_197_earn_yield_accel_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_197_earn_yield_accel_21d"""
    return (_safe_div(1.0, pe)).diff(21).diff(21)

def valn_198_earn_yield_accel_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_198_earn_yield_accel_63d"""
    return (_safe_div(1.0, pe)).diff(63).diff(21)

def valn_199_earn_yield_accel_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_199_earn_yield_accel_126d"""
    return (_safe_div(1.0, pe)).diff(126).diff(21)

def valn_200_earn_yield_accel_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_200_earn_yield_accel_252d"""
    return (_safe_div(1.0, pe)).diff(252).diff(21)

# ── Registry ──────────────────────────────────────────────────────────────────
V39_REGISTRY_ACCEL = {
    "valn_176_ps_accel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_176_ps_accel_5d},
    "valn_177_ps_accel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_177_ps_accel_21d},
    "valn_178_ps_accel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_178_ps_accel_63d},
    "valn_179_ps_accel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_179_ps_accel_126d},
    "valn_180_ps_accel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_180_ps_accel_252d},
    "valn_181_pb_accel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_181_pb_accel_5d},
    "valn_182_pb_accel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_182_pb_accel_21d},
    "valn_183_pb_accel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_183_pb_accel_63d},
    "valn_184_pb_accel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_184_pb_accel_126d},
    "valn_185_pb_accel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_185_pb_accel_252d},
    "valn_186_pe_accel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_186_pe_accel_5d},
    "valn_187_pe_accel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_187_pe_accel_21d},
    "valn_188_pe_accel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_188_pe_accel_63d},
    "valn_189_pe_accel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_189_pe_accel_126d},
    "valn_190_pe_accel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_190_pe_accel_252d},
    "valn_191_evebitda_accel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_191_evebitda_accel_5d},
    "valn_192_evebitda_accel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_192_evebitda_accel_21d},
    "valn_193_evebitda_accel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_193_evebitda_accel_63d},
    "valn_194_evebitda_accel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_194_evebitda_accel_126d},
    "valn_195_evebitda_accel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_195_evebitda_accel_252d},
    "valn_196_earn_yield_accel_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_196_earn_yield_accel_5d},
    "valn_197_earn_yield_accel_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_197_earn_yield_accel_21d},
    "valn_198_earn_yield_accel_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_198_earn_yield_accel_63d},
    "valn_199_earn_yield_accel_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_199_earn_yield_accel_126d},
    "valn_200_earn_yield_accel_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_200_earn_yield_accel_252d},
}
