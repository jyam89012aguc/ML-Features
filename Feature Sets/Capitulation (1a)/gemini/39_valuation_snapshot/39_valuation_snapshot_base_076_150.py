"""
39_valuation_snapshot — Base Features 076-150
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

def valn_076_ev_rev_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_076_ev_rev_lvl_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rolling_mean(base, 5)

def valn_077_ev_rev_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_077_ev_rev_zscore_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _zscore_rolling(base, 5)

def valn_078_ev_rev_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_078_ev_rev_rank_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rank_pct(base, 5)

def valn_079_ev_rev_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_079_ev_rev_lvl_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rolling_mean(base, 21)

def valn_080_ev_rev_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_080_ev_rev_zscore_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _zscore_rolling(base, 21)

def valn_081_ev_rev_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_081_ev_rev_rank_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rank_pct(base, 21)

def valn_082_ev_rev_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_082_ev_rev_lvl_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rolling_mean(base, 63)

def valn_083_ev_rev_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_083_ev_rev_zscore_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _zscore_rolling(base, 63)

def valn_084_ev_rev_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_084_ev_rev_rank_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rank_pct(base, 63)

def valn_085_ev_rev_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_085_ev_rev_lvl_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rolling_mean(base, 126)

def valn_086_ev_rev_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_086_ev_rev_zscore_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _zscore_rolling(base, 126)

def valn_087_ev_rev_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_087_ev_rev_rank_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rank_pct(base, 126)

def valn_088_ev_rev_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_088_ev_rev_lvl_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rolling_mean(base, 252)

def valn_089_ev_rev_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_089_ev_rev_zscore_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _zscore_rolling(base, 252)

def valn_090_ev_rev_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_090_ev_rev_rank_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, revenue)
    return _rank_pct(base, 252)

def valn_091_ev_opinc_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_091_ev_opinc_lvl_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rolling_mean(base, 5)

def valn_092_ev_opinc_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_092_ev_opinc_zscore_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _zscore_rolling(base, 5)

def valn_093_ev_opinc_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_093_ev_opinc_rank_5d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rank_pct(base, 5)

def valn_094_ev_opinc_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_094_ev_opinc_lvl_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rolling_mean(base, 21)

def valn_095_ev_opinc_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_095_ev_opinc_zscore_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _zscore_rolling(base, 21)

def valn_096_ev_opinc_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_096_ev_opinc_rank_21d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rank_pct(base, 21)

def valn_097_ev_opinc_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_097_ev_opinc_lvl_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rolling_mean(base, 63)

def valn_098_ev_opinc_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_098_ev_opinc_zscore_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _zscore_rolling(base, 63)

def valn_099_ev_opinc_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_099_ev_opinc_rank_63d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rank_pct(base, 63)

def valn_100_ev_opinc_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_100_ev_opinc_lvl_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rolling_mean(base, 126)

def valn_101_ev_opinc_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_101_ev_opinc_zscore_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _zscore_rolling(base, 126)

def valn_102_ev_opinc_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_102_ev_opinc_rank_126d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rank_pct(base, 126)

def valn_103_ev_opinc_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_103_ev_opinc_lvl_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rolling_mean(base, 252)

def valn_104_ev_opinc_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_104_ev_opinc_zscore_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _zscore_rolling(base, 252)

def valn_105_ev_opinc_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_105_ev_opinc_rank_252d"""
    base = _safe_div(marketcap + debt - cashnequiv, opinc.abs())
    return _rank_pct(base, 252)

def valn_106_mkt_eq_rat_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_106_mkt_eq_rat_lvl_5d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 5)

def valn_107_mkt_eq_rat_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_107_mkt_eq_rat_zscore_5d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 5)

def valn_108_mkt_eq_rat_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_108_mkt_eq_rat_rank_5d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 5)

def valn_109_mkt_eq_rat_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_109_mkt_eq_rat_lvl_21d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 21)

def valn_110_mkt_eq_rat_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_110_mkt_eq_rat_zscore_21d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 21)

def valn_111_mkt_eq_rat_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_111_mkt_eq_rat_rank_21d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 21)

def valn_112_mkt_eq_rat_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_112_mkt_eq_rat_lvl_63d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 63)

def valn_113_mkt_eq_rat_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_113_mkt_eq_rat_zscore_63d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 63)

def valn_114_mkt_eq_rat_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_114_mkt_eq_rat_rank_63d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 63)

def valn_115_mkt_eq_rat_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_115_mkt_eq_rat_lvl_126d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 126)

def valn_116_mkt_eq_rat_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_116_mkt_eq_rat_zscore_126d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 126)

def valn_117_mkt_eq_rat_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_117_mkt_eq_rat_rank_126d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 126)

def valn_118_mkt_eq_rat_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_118_mkt_eq_rat_lvl_252d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 252)

def valn_119_mkt_eq_rat_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_119_mkt_eq_rat_zscore_252d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 252)

def valn_120_mkt_eq_rat_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_120_mkt_eq_rat_rank_252d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 252)

def valn_121_ps_inv_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_121_ps_inv_lvl_5d"""
    base = _safe_div(1.0, ps)
    return _rolling_mean(base, 5)

def valn_122_ps_inv_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_122_ps_inv_zscore_5d"""
    base = _safe_div(1.0, ps)
    return _zscore_rolling(base, 5)

def valn_123_ps_inv_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_123_ps_inv_rank_5d"""
    base = _safe_div(1.0, ps)
    return _rank_pct(base, 5)

def valn_124_ps_inv_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_124_ps_inv_lvl_21d"""
    base = _safe_div(1.0, ps)
    return _rolling_mean(base, 21)

def valn_125_ps_inv_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_125_ps_inv_zscore_21d"""
    base = _safe_div(1.0, ps)
    return _zscore_rolling(base, 21)

def valn_126_ps_inv_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_126_ps_inv_rank_21d"""
    base = _safe_div(1.0, ps)
    return _rank_pct(base, 21)

def valn_127_ps_inv_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_127_ps_inv_lvl_63d"""
    base = _safe_div(1.0, ps)
    return _rolling_mean(base, 63)

def valn_128_ps_inv_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_128_ps_inv_zscore_63d"""
    base = _safe_div(1.0, ps)
    return _zscore_rolling(base, 63)

def valn_129_ps_inv_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_129_ps_inv_rank_63d"""
    base = _safe_div(1.0, ps)
    return _rank_pct(base, 63)

def valn_130_ps_inv_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_130_ps_inv_lvl_126d"""
    base = _safe_div(1.0, ps)
    return _rolling_mean(base, 126)

def valn_131_ps_inv_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_131_ps_inv_zscore_126d"""
    base = _safe_div(1.0, ps)
    return _zscore_rolling(base, 126)

def valn_132_ps_inv_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_132_ps_inv_rank_126d"""
    base = _safe_div(1.0, ps)
    return _rank_pct(base, 126)

def valn_133_ps_inv_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_133_ps_inv_lvl_252d"""
    base = _safe_div(1.0, ps)
    return _rolling_mean(base, 252)

def valn_134_ps_inv_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_134_ps_inv_zscore_252d"""
    base = _safe_div(1.0, ps)
    return _zscore_rolling(base, 252)

def valn_135_ps_inv_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_135_ps_inv_rank_252d"""
    base = _safe_div(1.0, ps)
    return _rank_pct(base, 252)

def valn_136_pb_inv_lvl_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_136_pb_inv_lvl_5d"""
    base = _safe_div(1.0, pb)
    return _rolling_mean(base, 5)

def valn_137_pb_inv_zscore_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_137_pb_inv_zscore_5d"""
    base = _safe_div(1.0, pb)
    return _zscore_rolling(base, 5)

def valn_138_pb_inv_rank_5d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_138_pb_inv_rank_5d"""
    base = _safe_div(1.0, pb)
    return _rank_pct(base, 5)

def valn_139_pb_inv_lvl_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_139_pb_inv_lvl_21d"""
    base = _safe_div(1.0, pb)
    return _rolling_mean(base, 21)

def valn_140_pb_inv_zscore_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_140_pb_inv_zscore_21d"""
    base = _safe_div(1.0, pb)
    return _zscore_rolling(base, 21)

def valn_141_pb_inv_rank_21d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_141_pb_inv_rank_21d"""
    base = _safe_div(1.0, pb)
    return _rank_pct(base, 21)

def valn_142_pb_inv_lvl_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_142_pb_inv_lvl_63d"""
    base = _safe_div(1.0, pb)
    return _rolling_mean(base, 63)

def valn_143_pb_inv_zscore_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_143_pb_inv_zscore_63d"""
    base = _safe_div(1.0, pb)
    return _zscore_rolling(base, 63)

def valn_144_pb_inv_rank_63d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_144_pb_inv_rank_63d"""
    base = _safe_div(1.0, pb)
    return _rank_pct(base, 63)

def valn_145_pb_inv_lvl_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_145_pb_inv_lvl_126d"""
    base = _safe_div(1.0, pb)
    return _rolling_mean(base, 126)

def valn_146_pb_inv_zscore_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_146_pb_inv_zscore_126d"""
    base = _safe_div(1.0, pb)
    return _zscore_rolling(base, 126)

def valn_147_pb_inv_rank_126d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_147_pb_inv_rank_126d"""
    base = _safe_div(1.0, pb)
    return _rank_pct(base, 126)

def valn_148_pb_inv_lvl_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_148_pb_inv_lvl_252d"""
    base = _safe_div(1.0, pb)
    return _rolling_mean(base, 252)

def valn_149_pb_inv_zscore_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_149_pb_inv_zscore_252d"""
    base = _safe_div(1.0, pb)
    return _zscore_rolling(base, 252)

def valn_150_pb_inv_rank_252d(ps: pd.Series, pb: pd.Series, pe: pd.Series, evebitda: pd.Series, marketcap: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series, opinc: pd.Series, equity: pd.Series) -> pd.Series:
    """valn_150_pb_inv_rank_252d"""
    base = _safe_div(1.0, pb)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V39_REGISTRY_2 = {
    "valn_076_ev_rev_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_076_ev_rev_lvl_5d},
    "valn_077_ev_rev_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_077_ev_rev_zscore_5d},
    "valn_078_ev_rev_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_078_ev_rev_rank_5d},
    "valn_079_ev_rev_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_079_ev_rev_lvl_21d},
    "valn_080_ev_rev_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_080_ev_rev_zscore_21d},
    "valn_081_ev_rev_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_081_ev_rev_rank_21d},
    "valn_082_ev_rev_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_082_ev_rev_lvl_63d},
    "valn_083_ev_rev_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_083_ev_rev_zscore_63d},
    "valn_084_ev_rev_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_084_ev_rev_rank_63d},
    "valn_085_ev_rev_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_085_ev_rev_lvl_126d},
    "valn_086_ev_rev_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_086_ev_rev_zscore_126d},
    "valn_087_ev_rev_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_087_ev_rev_rank_126d},
    "valn_088_ev_rev_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_088_ev_rev_lvl_252d},
    "valn_089_ev_rev_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_089_ev_rev_zscore_252d},
    "valn_090_ev_rev_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_090_ev_rev_rank_252d},
    "valn_091_ev_opinc_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_091_ev_opinc_lvl_5d},
    "valn_092_ev_opinc_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_092_ev_opinc_zscore_5d},
    "valn_093_ev_opinc_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_093_ev_opinc_rank_5d},
    "valn_094_ev_opinc_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_094_ev_opinc_lvl_21d},
    "valn_095_ev_opinc_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_095_ev_opinc_zscore_21d},
    "valn_096_ev_opinc_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_096_ev_opinc_rank_21d},
    "valn_097_ev_opinc_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_097_ev_opinc_lvl_63d},
    "valn_098_ev_opinc_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_098_ev_opinc_zscore_63d},
    "valn_099_ev_opinc_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_099_ev_opinc_rank_63d},
    "valn_100_ev_opinc_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_100_ev_opinc_lvl_126d},
    "valn_101_ev_opinc_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_101_ev_opinc_zscore_126d},
    "valn_102_ev_opinc_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_102_ev_opinc_rank_126d},
    "valn_103_ev_opinc_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_103_ev_opinc_lvl_252d},
    "valn_104_ev_opinc_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_104_ev_opinc_zscore_252d},
    "valn_105_ev_opinc_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_105_ev_opinc_rank_252d},
    "valn_106_mkt_eq_rat_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_106_mkt_eq_rat_lvl_5d},
    "valn_107_mkt_eq_rat_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_107_mkt_eq_rat_zscore_5d},
    "valn_108_mkt_eq_rat_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_108_mkt_eq_rat_rank_5d},
    "valn_109_mkt_eq_rat_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_109_mkt_eq_rat_lvl_21d},
    "valn_110_mkt_eq_rat_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_110_mkt_eq_rat_zscore_21d},
    "valn_111_mkt_eq_rat_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_111_mkt_eq_rat_rank_21d},
    "valn_112_mkt_eq_rat_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_112_mkt_eq_rat_lvl_63d},
    "valn_113_mkt_eq_rat_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_113_mkt_eq_rat_zscore_63d},
    "valn_114_mkt_eq_rat_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_114_mkt_eq_rat_rank_63d},
    "valn_115_mkt_eq_rat_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_115_mkt_eq_rat_lvl_126d},
    "valn_116_mkt_eq_rat_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_116_mkt_eq_rat_zscore_126d},
    "valn_117_mkt_eq_rat_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_117_mkt_eq_rat_rank_126d},
    "valn_118_mkt_eq_rat_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_118_mkt_eq_rat_lvl_252d},
    "valn_119_mkt_eq_rat_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_119_mkt_eq_rat_zscore_252d},
    "valn_120_mkt_eq_rat_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_120_mkt_eq_rat_rank_252d},
    "valn_121_ps_inv_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_121_ps_inv_lvl_5d},
    "valn_122_ps_inv_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_122_ps_inv_zscore_5d},
    "valn_123_ps_inv_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_123_ps_inv_rank_5d},
    "valn_124_ps_inv_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_124_ps_inv_lvl_21d},
    "valn_125_ps_inv_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_125_ps_inv_zscore_21d},
    "valn_126_ps_inv_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_126_ps_inv_rank_21d},
    "valn_127_ps_inv_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_127_ps_inv_lvl_63d},
    "valn_128_ps_inv_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_128_ps_inv_zscore_63d},
    "valn_129_ps_inv_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_129_ps_inv_rank_63d},
    "valn_130_ps_inv_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_130_ps_inv_lvl_126d},
    "valn_131_ps_inv_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_131_ps_inv_zscore_126d},
    "valn_132_ps_inv_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_132_ps_inv_rank_126d},
    "valn_133_ps_inv_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_133_ps_inv_lvl_252d},
    "valn_134_ps_inv_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_134_ps_inv_zscore_252d},
    "valn_135_ps_inv_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_135_ps_inv_rank_252d},
    "valn_136_pb_inv_lvl_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_136_pb_inv_lvl_5d},
    "valn_137_pb_inv_zscore_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_137_pb_inv_zscore_5d},
    "valn_138_pb_inv_rank_5d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_138_pb_inv_rank_5d},
    "valn_139_pb_inv_lvl_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_139_pb_inv_lvl_21d},
    "valn_140_pb_inv_zscore_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_140_pb_inv_zscore_21d},
    "valn_141_pb_inv_rank_21d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_141_pb_inv_rank_21d},
    "valn_142_pb_inv_lvl_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_142_pb_inv_lvl_63d},
    "valn_143_pb_inv_zscore_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_143_pb_inv_zscore_63d},
    "valn_144_pb_inv_rank_63d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_144_pb_inv_rank_63d},
    "valn_145_pb_inv_lvl_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_145_pb_inv_lvl_126d},
    "valn_146_pb_inv_zscore_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_146_pb_inv_zscore_126d},
    "valn_147_pb_inv_rank_126d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_147_pb_inv_rank_126d},
    "valn_148_pb_inv_lvl_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_148_pb_inv_lvl_252d},
    "valn_149_pb_inv_zscore_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_149_pb_inv_zscore_252d},
    "valn_150_pb_inv_rank_252d": {"inputs": ["ps", "pb", "pe", "evebitda", "marketcap", "debt", "cashnequiv", "revenue", "opinc", "equity"], "func": valn_150_pb_inv_rank_252d},
}
