"""
35_revenue_level — Base Features 076-150
Domain: revenue_level
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

def revl_076_liabs_rat_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_076_liabs_rat_lvl_5d"""
    base = _safe_div(revenue, liabs)
    return _rolling_mean(base, 5)

def revl_077_liabs_rat_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_077_liabs_rat_zscore_5d"""
    base = _safe_div(revenue, liabs)
    return _zscore_rolling(base, 5)

def revl_078_liabs_rat_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_078_liabs_rat_rank_5d"""
    base = _safe_div(revenue, liabs)
    return _rank_pct(base, 5)

def revl_079_liabs_rat_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_079_liabs_rat_lvl_21d"""
    base = _safe_div(revenue, liabs)
    return _rolling_mean(base, 21)

def revl_080_liabs_rat_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_080_liabs_rat_zscore_21d"""
    base = _safe_div(revenue, liabs)
    return _zscore_rolling(base, 21)

def revl_081_liabs_rat_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_081_liabs_rat_rank_21d"""
    base = _safe_div(revenue, liabs)
    return _rank_pct(base, 21)

def revl_082_liabs_rat_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_082_liabs_rat_lvl_63d"""
    base = _safe_div(revenue, liabs)
    return _rolling_mean(base, 63)

def revl_083_liabs_rat_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_083_liabs_rat_zscore_63d"""
    base = _safe_div(revenue, liabs)
    return _zscore_rolling(base, 63)

def revl_084_liabs_rat_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_084_liabs_rat_rank_63d"""
    base = _safe_div(revenue, liabs)
    return _rank_pct(base, 63)

def revl_085_liabs_rat_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_085_liabs_rat_lvl_126d"""
    base = _safe_div(revenue, liabs)
    return _rolling_mean(base, 126)

def revl_086_liabs_rat_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_086_liabs_rat_zscore_126d"""
    base = _safe_div(revenue, liabs)
    return _zscore_rolling(base, 126)

def revl_087_liabs_rat_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_087_liabs_rat_rank_126d"""
    base = _safe_div(revenue, liabs)
    return _rank_pct(base, 126)

def revl_088_liabs_rat_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_088_liabs_rat_lvl_252d"""
    base = _safe_div(revenue, liabs)
    return _rolling_mean(base, 252)

def revl_089_liabs_rat_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_089_liabs_rat_zscore_252d"""
    base = _safe_div(revenue, liabs)
    return _zscore_rolling(base, 252)

def revl_090_liabs_rat_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_090_liabs_rat_rank_252d"""
    base = _safe_div(revenue, liabs)
    return _rank_pct(base, 252)

def revl_091_equity_rat_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_091_equity_rat_lvl_5d"""
    base = _safe_div(revenue, equity)
    return _rolling_mean(base, 5)

def revl_092_equity_rat_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_092_equity_rat_zscore_5d"""
    base = _safe_div(revenue, equity)
    return _zscore_rolling(base, 5)

def revl_093_equity_rat_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_093_equity_rat_rank_5d"""
    base = _safe_div(revenue, equity)
    return _rank_pct(base, 5)

def revl_094_equity_rat_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_094_equity_rat_lvl_21d"""
    base = _safe_div(revenue, equity)
    return _rolling_mean(base, 21)

def revl_095_equity_rat_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_095_equity_rat_zscore_21d"""
    base = _safe_div(revenue, equity)
    return _zscore_rolling(base, 21)

def revl_096_equity_rat_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_096_equity_rat_rank_21d"""
    base = _safe_div(revenue, equity)
    return _rank_pct(base, 21)

def revl_097_equity_rat_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_097_equity_rat_lvl_63d"""
    base = _safe_div(revenue, equity)
    return _rolling_mean(base, 63)

def revl_098_equity_rat_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_098_equity_rat_zscore_63d"""
    base = _safe_div(revenue, equity)
    return _zscore_rolling(base, 63)

def revl_099_equity_rat_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_099_equity_rat_rank_63d"""
    base = _safe_div(revenue, equity)
    return _rank_pct(base, 63)

def revl_100_equity_rat_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_100_equity_rat_lvl_126d"""
    base = _safe_div(revenue, equity)
    return _rolling_mean(base, 126)

def revl_101_equity_rat_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_101_equity_rat_zscore_126d"""
    base = _safe_div(revenue, equity)
    return _zscore_rolling(base, 126)

def revl_102_equity_rat_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_102_equity_rat_rank_126d"""
    base = _safe_div(revenue, equity)
    return _rank_pct(base, 126)

def revl_103_equity_rat_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_103_equity_rat_lvl_252d"""
    base = _safe_div(revenue, equity)
    return _rolling_mean(base, 252)

def revl_104_equity_rat_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_104_equity_rat_zscore_252d"""
    base = _safe_div(revenue, equity)
    return _zscore_rolling(base, 252)

def revl_105_equity_rat_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_105_equity_rat_rank_252d"""
    base = _safe_div(revenue, equity)
    return _rank_pct(base, 252)

def revl_106_ic_rat_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_106_ic_rat_lvl_5d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rolling_mean(base, 5)

def revl_107_ic_rat_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_107_ic_rat_zscore_5d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _zscore_rolling(base, 5)

def revl_108_ic_rat_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_108_ic_rat_rank_5d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rank_pct(base, 5)

def revl_109_ic_rat_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_109_ic_rat_lvl_21d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rolling_mean(base, 21)

def revl_110_ic_rat_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_110_ic_rat_zscore_21d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _zscore_rolling(base, 21)

def revl_111_ic_rat_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_111_ic_rat_rank_21d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rank_pct(base, 21)

def revl_112_ic_rat_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_112_ic_rat_lvl_63d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rolling_mean(base, 63)

def revl_113_ic_rat_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_113_ic_rat_zscore_63d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _zscore_rolling(base, 63)

def revl_114_ic_rat_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_114_ic_rat_rank_63d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rank_pct(base, 63)

def revl_115_ic_rat_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_115_ic_rat_lvl_126d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rolling_mean(base, 126)

def revl_116_ic_rat_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_116_ic_rat_zscore_126d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _zscore_rolling(base, 126)

def revl_117_ic_rat_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_117_ic_rat_rank_126d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rank_pct(base, 126)

def revl_118_ic_rat_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_118_ic_rat_lvl_252d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rolling_mean(base, 252)

def revl_119_ic_rat_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_119_ic_rat_zscore_252d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _zscore_rolling(base, 252)

def revl_120_ic_rat_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_120_ic_rat_rank_252d"""
    base = _safe_div(revenue, assets - cashnequiv)
    return _rank_pct(base, 252)

def revl_121_ppe_rat_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_121_ppe_rat_lvl_5d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rolling_mean(base, 5)

def revl_122_ppe_rat_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_122_ppe_rat_zscore_5d"""
    base = _safe_div(revenue, assets * 0.5)
    return _zscore_rolling(base, 5)

def revl_123_ppe_rat_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_123_ppe_rat_rank_5d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rank_pct(base, 5)

def revl_124_ppe_rat_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_124_ppe_rat_lvl_21d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rolling_mean(base, 21)

def revl_125_ppe_rat_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_125_ppe_rat_zscore_21d"""
    base = _safe_div(revenue, assets * 0.5)
    return _zscore_rolling(base, 21)

def revl_126_ppe_rat_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_126_ppe_rat_rank_21d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rank_pct(base, 21)

def revl_127_ppe_rat_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_127_ppe_rat_lvl_63d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rolling_mean(base, 63)

def revl_128_ppe_rat_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_128_ppe_rat_zscore_63d"""
    base = _safe_div(revenue, assets * 0.5)
    return _zscore_rolling(base, 63)

def revl_129_ppe_rat_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_129_ppe_rat_rank_63d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rank_pct(base, 63)

def revl_130_ppe_rat_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_130_ppe_rat_lvl_126d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rolling_mean(base, 126)

def revl_131_ppe_rat_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_131_ppe_rat_zscore_126d"""
    base = _safe_div(revenue, assets * 0.5)
    return _zscore_rolling(base, 126)

def revl_132_ppe_rat_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_132_ppe_rat_rank_126d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rank_pct(base, 126)

def revl_133_ppe_rat_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_133_ppe_rat_lvl_252d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rolling_mean(base, 252)

def revl_134_ppe_rat_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_134_ppe_rat_zscore_252d"""
    base = _safe_div(revenue, assets * 0.5)
    return _zscore_rolling(base, 252)

def revl_135_ppe_rat_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_135_ppe_rat_rank_252d"""
    base = _safe_div(revenue, assets * 0.5)
    return _rank_pct(base, 252)

def revl_136_opinc_rat_lvl_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_136_opinc_rat_lvl_5d"""
    base = _safe_div(revenue, opinc.abs())
    return _rolling_mean(base, 5)

def revl_137_opinc_rat_zscore_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_137_opinc_rat_zscore_5d"""
    base = _safe_div(revenue, opinc.abs())
    return _zscore_rolling(base, 5)

def revl_138_opinc_rat_rank_5d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_138_opinc_rat_rank_5d"""
    base = _safe_div(revenue, opinc.abs())
    return _rank_pct(base, 5)

def revl_139_opinc_rat_lvl_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_139_opinc_rat_lvl_21d"""
    base = _safe_div(revenue, opinc.abs())
    return _rolling_mean(base, 21)

def revl_140_opinc_rat_zscore_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_140_opinc_rat_zscore_21d"""
    base = _safe_div(revenue, opinc.abs())
    return _zscore_rolling(base, 21)

def revl_141_opinc_rat_rank_21d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_141_opinc_rat_rank_21d"""
    base = _safe_div(revenue, opinc.abs())
    return _rank_pct(base, 21)

def revl_142_opinc_rat_lvl_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_142_opinc_rat_lvl_63d"""
    base = _safe_div(revenue, opinc.abs())
    return _rolling_mean(base, 63)

def revl_143_opinc_rat_zscore_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_143_opinc_rat_zscore_63d"""
    base = _safe_div(revenue, opinc.abs())
    return _zscore_rolling(base, 63)

def revl_144_opinc_rat_rank_63d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_144_opinc_rat_rank_63d"""
    base = _safe_div(revenue, opinc.abs())
    return _rank_pct(base, 63)

def revl_145_opinc_rat_lvl_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_145_opinc_rat_lvl_126d"""
    base = _safe_div(revenue, opinc.abs())
    return _rolling_mean(base, 126)

def revl_146_opinc_rat_zscore_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_146_opinc_rat_zscore_126d"""
    base = _safe_div(revenue, opinc.abs())
    return _zscore_rolling(base, 126)

def revl_147_opinc_rat_rank_126d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_147_opinc_rat_rank_126d"""
    base = _safe_div(revenue, opinc.abs())
    return _rank_pct(base, 126)

def revl_148_opinc_rat_lvl_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_148_opinc_rat_lvl_252d"""
    base = _safe_div(revenue, opinc.abs())
    return _rolling_mean(base, 252)

def revl_149_opinc_rat_zscore_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_149_opinc_rat_zscore_252d"""
    base = _safe_div(revenue, opinc.abs())
    return _zscore_rolling(base, 252)

def revl_150_opinc_rat_rank_252d(revenue: pd.Series, sharesbas: pd.Series, assets: pd.Series, marketcap: pd.Series, liabs: pd.Series, equity: pd.Series, opinc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """revl_150_opinc_rat_rank_252d"""
    base = _safe_div(revenue, opinc.abs())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V35_REGISTRY_2 = {
    "revl_076_liabs_rat_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_076_liabs_rat_lvl_5d},
    "revl_077_liabs_rat_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_077_liabs_rat_zscore_5d},
    "revl_078_liabs_rat_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_078_liabs_rat_rank_5d},
    "revl_079_liabs_rat_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_079_liabs_rat_lvl_21d},
    "revl_080_liabs_rat_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_080_liabs_rat_zscore_21d},
    "revl_081_liabs_rat_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_081_liabs_rat_rank_21d},
    "revl_082_liabs_rat_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_082_liabs_rat_lvl_63d},
    "revl_083_liabs_rat_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_083_liabs_rat_zscore_63d},
    "revl_084_liabs_rat_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_084_liabs_rat_rank_63d},
    "revl_085_liabs_rat_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_085_liabs_rat_lvl_126d},
    "revl_086_liabs_rat_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_086_liabs_rat_zscore_126d},
    "revl_087_liabs_rat_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_087_liabs_rat_rank_126d},
    "revl_088_liabs_rat_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_088_liabs_rat_lvl_252d},
    "revl_089_liabs_rat_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_089_liabs_rat_zscore_252d},
    "revl_090_liabs_rat_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_090_liabs_rat_rank_252d},
    "revl_091_equity_rat_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_091_equity_rat_lvl_5d},
    "revl_092_equity_rat_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_092_equity_rat_zscore_5d},
    "revl_093_equity_rat_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_093_equity_rat_rank_5d},
    "revl_094_equity_rat_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_094_equity_rat_lvl_21d},
    "revl_095_equity_rat_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_095_equity_rat_zscore_21d},
    "revl_096_equity_rat_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_096_equity_rat_rank_21d},
    "revl_097_equity_rat_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_097_equity_rat_lvl_63d},
    "revl_098_equity_rat_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_098_equity_rat_zscore_63d},
    "revl_099_equity_rat_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_099_equity_rat_rank_63d},
    "revl_100_equity_rat_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_100_equity_rat_lvl_126d},
    "revl_101_equity_rat_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_101_equity_rat_zscore_126d},
    "revl_102_equity_rat_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_102_equity_rat_rank_126d},
    "revl_103_equity_rat_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_103_equity_rat_lvl_252d},
    "revl_104_equity_rat_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_104_equity_rat_zscore_252d},
    "revl_105_equity_rat_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_105_equity_rat_rank_252d},
    "revl_106_ic_rat_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_106_ic_rat_lvl_5d},
    "revl_107_ic_rat_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_107_ic_rat_zscore_5d},
    "revl_108_ic_rat_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_108_ic_rat_rank_5d},
    "revl_109_ic_rat_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_109_ic_rat_lvl_21d},
    "revl_110_ic_rat_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_110_ic_rat_zscore_21d},
    "revl_111_ic_rat_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_111_ic_rat_rank_21d},
    "revl_112_ic_rat_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_112_ic_rat_lvl_63d},
    "revl_113_ic_rat_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_113_ic_rat_zscore_63d},
    "revl_114_ic_rat_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_114_ic_rat_rank_63d},
    "revl_115_ic_rat_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_115_ic_rat_lvl_126d},
    "revl_116_ic_rat_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_116_ic_rat_zscore_126d},
    "revl_117_ic_rat_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_117_ic_rat_rank_126d},
    "revl_118_ic_rat_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_118_ic_rat_lvl_252d},
    "revl_119_ic_rat_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_119_ic_rat_zscore_252d},
    "revl_120_ic_rat_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_120_ic_rat_rank_252d},
    "revl_121_ppe_rat_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_121_ppe_rat_lvl_5d},
    "revl_122_ppe_rat_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_122_ppe_rat_zscore_5d},
    "revl_123_ppe_rat_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_123_ppe_rat_rank_5d},
    "revl_124_ppe_rat_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_124_ppe_rat_lvl_21d},
    "revl_125_ppe_rat_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_125_ppe_rat_zscore_21d},
    "revl_126_ppe_rat_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_126_ppe_rat_rank_21d},
    "revl_127_ppe_rat_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_127_ppe_rat_lvl_63d},
    "revl_128_ppe_rat_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_128_ppe_rat_zscore_63d},
    "revl_129_ppe_rat_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_129_ppe_rat_rank_63d},
    "revl_130_ppe_rat_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_130_ppe_rat_lvl_126d},
    "revl_131_ppe_rat_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_131_ppe_rat_zscore_126d},
    "revl_132_ppe_rat_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_132_ppe_rat_rank_126d},
    "revl_133_ppe_rat_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_133_ppe_rat_lvl_252d},
    "revl_134_ppe_rat_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_134_ppe_rat_zscore_252d},
    "revl_135_ppe_rat_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_135_ppe_rat_rank_252d},
    "revl_136_opinc_rat_lvl_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_136_opinc_rat_lvl_5d},
    "revl_137_opinc_rat_zscore_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_137_opinc_rat_zscore_5d},
    "revl_138_opinc_rat_rank_5d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_138_opinc_rat_rank_5d},
    "revl_139_opinc_rat_lvl_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_139_opinc_rat_lvl_21d},
    "revl_140_opinc_rat_zscore_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_140_opinc_rat_zscore_21d},
    "revl_141_opinc_rat_rank_21d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_141_opinc_rat_rank_21d},
    "revl_142_opinc_rat_lvl_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_142_opinc_rat_lvl_63d},
    "revl_143_opinc_rat_zscore_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_143_opinc_rat_zscore_63d},
    "revl_144_opinc_rat_rank_63d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_144_opinc_rat_rank_63d},
    "revl_145_opinc_rat_lvl_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_145_opinc_rat_lvl_126d},
    "revl_146_opinc_rat_zscore_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_146_opinc_rat_zscore_126d},
    "revl_147_opinc_rat_rank_126d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_147_opinc_rat_rank_126d},
    "revl_148_opinc_rat_lvl_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_148_opinc_rat_lvl_252d},
    "revl_149_opinc_rat_zscore_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_149_opinc_rat_zscore_252d},
    "revl_150_opinc_rat_rank_252d": {"inputs": ["revenue", "sharesbas", "assets", "marketcap", "liabs", "equity", "opinc", "cashnequiv"], "func": revl_150_opinc_rat_rank_252d},
}
