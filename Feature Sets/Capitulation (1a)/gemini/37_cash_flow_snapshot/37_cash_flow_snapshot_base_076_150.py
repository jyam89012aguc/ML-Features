"""
37_cash_flow_snapshot — Base Features 076-150
Domain: cash_flow_snapshot
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

def cflo_076_fcf_ocf_rat_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_076_fcf_ocf_rat_lvl_5d"""
    base = _safe_div(fcf, ocf.abs())
    return _rolling_mean(base, 5)

def cflo_077_fcf_ocf_rat_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_077_fcf_ocf_rat_zscore_5d"""
    base = _safe_div(fcf, ocf.abs())
    return _zscore_rolling(base, 5)

def cflo_078_fcf_ocf_rat_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_078_fcf_ocf_rat_rank_5d"""
    base = _safe_div(fcf, ocf.abs())
    return _rank_pct(base, 5)

def cflo_079_fcf_ocf_rat_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_079_fcf_ocf_rat_lvl_21d"""
    base = _safe_div(fcf, ocf.abs())
    return _rolling_mean(base, 21)

def cflo_080_fcf_ocf_rat_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_080_fcf_ocf_rat_zscore_21d"""
    base = _safe_div(fcf, ocf.abs())
    return _zscore_rolling(base, 21)

def cflo_081_fcf_ocf_rat_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_081_fcf_ocf_rat_rank_21d"""
    base = _safe_div(fcf, ocf.abs())
    return _rank_pct(base, 21)

def cflo_082_fcf_ocf_rat_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_082_fcf_ocf_rat_lvl_63d"""
    base = _safe_div(fcf, ocf.abs())
    return _rolling_mean(base, 63)

def cflo_083_fcf_ocf_rat_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_083_fcf_ocf_rat_zscore_63d"""
    base = _safe_div(fcf, ocf.abs())
    return _zscore_rolling(base, 63)

def cflo_084_fcf_ocf_rat_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_084_fcf_ocf_rat_rank_63d"""
    base = _safe_div(fcf, ocf.abs())
    return _rank_pct(base, 63)

def cflo_085_fcf_ocf_rat_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_085_fcf_ocf_rat_lvl_126d"""
    base = _safe_div(fcf, ocf.abs())
    return _rolling_mean(base, 126)

def cflo_086_fcf_ocf_rat_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_086_fcf_ocf_rat_zscore_126d"""
    base = _safe_div(fcf, ocf.abs())
    return _zscore_rolling(base, 126)

def cflo_087_fcf_ocf_rat_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_087_fcf_ocf_rat_rank_126d"""
    base = _safe_div(fcf, ocf.abs())
    return _rank_pct(base, 126)

def cflo_088_fcf_ocf_rat_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_088_fcf_ocf_rat_lvl_252d"""
    base = _safe_div(fcf, ocf.abs())
    return _rolling_mean(base, 252)

def cflo_089_fcf_ocf_rat_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_089_fcf_ocf_rat_zscore_252d"""
    base = _safe_div(fcf, ocf.abs())
    return _zscore_rolling(base, 252)

def cflo_090_fcf_ocf_rat_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_090_fcf_ocf_rat_rank_252d"""
    base = _safe_div(fcf, ocf.abs())
    return _rank_pct(base, 252)

def cflo_091_ocf_assets_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_091_ocf_assets_lvl_5d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 5)

def cflo_092_ocf_assets_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_092_ocf_assets_zscore_5d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 5)

def cflo_093_ocf_assets_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_093_ocf_assets_rank_5d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 5)

def cflo_094_ocf_assets_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_094_ocf_assets_lvl_21d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 21)

def cflo_095_ocf_assets_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_095_ocf_assets_zscore_21d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 21)

def cflo_096_ocf_assets_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_096_ocf_assets_rank_21d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 21)

def cflo_097_ocf_assets_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_097_ocf_assets_lvl_63d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 63)

def cflo_098_ocf_assets_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_098_ocf_assets_zscore_63d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 63)

def cflo_099_ocf_assets_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_099_ocf_assets_rank_63d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 63)

def cflo_100_ocf_assets_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_100_ocf_assets_lvl_126d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 126)

def cflo_101_ocf_assets_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_101_ocf_assets_zscore_126d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 126)

def cflo_102_ocf_assets_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_102_ocf_assets_rank_126d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 126)

def cflo_103_ocf_assets_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_103_ocf_assets_lvl_252d"""
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 252)

def cflo_104_ocf_assets_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_104_ocf_assets_zscore_252d"""
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 252)

def cflo_105_ocf_assets_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_105_ocf_assets_rank_252d"""
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 252)

def cflo_106_fcf_assets_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_106_fcf_assets_lvl_5d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 5)

def cflo_107_fcf_assets_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_107_fcf_assets_zscore_5d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 5)

def cflo_108_fcf_assets_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_108_fcf_assets_rank_5d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 5)

def cflo_109_fcf_assets_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_109_fcf_assets_lvl_21d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 21)

def cflo_110_fcf_assets_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_110_fcf_assets_zscore_21d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 21)

def cflo_111_fcf_assets_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_111_fcf_assets_rank_21d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 21)

def cflo_112_fcf_assets_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_112_fcf_assets_lvl_63d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 63)

def cflo_113_fcf_assets_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_113_fcf_assets_zscore_63d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 63)

def cflo_114_fcf_assets_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_114_fcf_assets_rank_63d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 63)

def cflo_115_fcf_assets_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_115_fcf_assets_lvl_126d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 126)

def cflo_116_fcf_assets_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_116_fcf_assets_zscore_126d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 126)

def cflo_117_fcf_assets_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_117_fcf_assets_rank_126d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 126)

def cflo_118_fcf_assets_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_118_fcf_assets_lvl_252d"""
    base = _safe_div(fcf, assets)
    return _rolling_mean(base, 252)

def cflo_119_fcf_assets_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_119_fcf_assets_zscore_252d"""
    base = _safe_div(fcf, assets)
    return _zscore_rolling(base, 252)

def cflo_120_fcf_assets_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_120_fcf_assets_rank_252d"""
    base = _safe_div(fcf, assets)
    return _rank_pct(base, 252)

def cflo_121_ocf_debt_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_121_ocf_debt_lvl_5d"""
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 5)

def cflo_122_ocf_debt_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_122_ocf_debt_zscore_5d"""
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 5)

def cflo_123_ocf_debt_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_123_ocf_debt_rank_5d"""
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 5)

def cflo_124_ocf_debt_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_124_ocf_debt_lvl_21d"""
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 21)

def cflo_125_ocf_debt_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_125_ocf_debt_zscore_21d"""
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 21)

def cflo_126_ocf_debt_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_126_ocf_debt_rank_21d"""
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 21)

def cflo_127_ocf_debt_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_127_ocf_debt_lvl_63d"""
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 63)

def cflo_128_ocf_debt_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_128_ocf_debt_zscore_63d"""
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 63)

def cflo_129_ocf_debt_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_129_ocf_debt_rank_63d"""
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 63)

def cflo_130_ocf_debt_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_130_ocf_debt_lvl_126d"""
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 126)

def cflo_131_ocf_debt_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_131_ocf_debt_zscore_126d"""
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 126)

def cflo_132_ocf_debt_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_132_ocf_debt_rank_126d"""
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 126)

def cflo_133_ocf_debt_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_133_ocf_debt_lvl_252d"""
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 252)

def cflo_134_ocf_debt_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_134_ocf_debt_zscore_252d"""
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 252)

def cflo_135_ocf_debt_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_135_ocf_debt_rank_252d"""
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 252)

def cflo_136_fcf_equity_lvl_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_136_fcf_equity_lvl_5d"""
    base = _safe_div(fcf, equity)
    return _rolling_mean(base, 5)

def cflo_137_fcf_equity_zscore_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_137_fcf_equity_zscore_5d"""
    base = _safe_div(fcf, equity)
    return _zscore_rolling(base, 5)

def cflo_138_fcf_equity_rank_5d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_138_fcf_equity_rank_5d"""
    base = _safe_div(fcf, equity)
    return _rank_pct(base, 5)

def cflo_139_fcf_equity_lvl_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_139_fcf_equity_lvl_21d"""
    base = _safe_div(fcf, equity)
    return _rolling_mean(base, 21)

def cflo_140_fcf_equity_zscore_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_140_fcf_equity_zscore_21d"""
    base = _safe_div(fcf, equity)
    return _zscore_rolling(base, 21)

def cflo_141_fcf_equity_rank_21d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_141_fcf_equity_rank_21d"""
    base = _safe_div(fcf, equity)
    return _rank_pct(base, 21)

def cflo_142_fcf_equity_lvl_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_142_fcf_equity_lvl_63d"""
    base = _safe_div(fcf, equity)
    return _rolling_mean(base, 63)

def cflo_143_fcf_equity_zscore_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_143_fcf_equity_zscore_63d"""
    base = _safe_div(fcf, equity)
    return _zscore_rolling(base, 63)

def cflo_144_fcf_equity_rank_63d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_144_fcf_equity_rank_63d"""
    base = _safe_div(fcf, equity)
    return _rank_pct(base, 63)

def cflo_145_fcf_equity_lvl_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_145_fcf_equity_lvl_126d"""
    base = _safe_div(fcf, equity)
    return _rolling_mean(base, 126)

def cflo_146_fcf_equity_zscore_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_146_fcf_equity_zscore_126d"""
    base = _safe_div(fcf, equity)
    return _zscore_rolling(base, 126)

def cflo_147_fcf_equity_rank_126d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_147_fcf_equity_rank_126d"""
    base = _safe_div(fcf, equity)
    return _rank_pct(base, 126)

def cflo_148_fcf_equity_lvl_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_148_fcf_equity_lvl_252d"""
    base = _safe_div(fcf, equity)
    return _rolling_mean(base, 252)

def cflo_149_fcf_equity_zscore_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_149_fcf_equity_zscore_252d"""
    base = _safe_div(fcf, equity)
    return _zscore_rolling(base, 252)

def cflo_150_fcf_equity_rank_252d(ocf: pd.Series, fcf: pd.Series, revenue: pd.Series, sharesbas: pd.Series, marketcap: pd.Series, assets: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """cflo_150_fcf_equity_rank_252d"""
    base = _safe_div(fcf, equity)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V37_REGISTRY_2 = {
    "cflo_076_fcf_ocf_rat_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_076_fcf_ocf_rat_lvl_5d},
    "cflo_077_fcf_ocf_rat_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_077_fcf_ocf_rat_zscore_5d},
    "cflo_078_fcf_ocf_rat_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_078_fcf_ocf_rat_rank_5d},
    "cflo_079_fcf_ocf_rat_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_079_fcf_ocf_rat_lvl_21d},
    "cflo_080_fcf_ocf_rat_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_080_fcf_ocf_rat_zscore_21d},
    "cflo_081_fcf_ocf_rat_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_081_fcf_ocf_rat_rank_21d},
    "cflo_082_fcf_ocf_rat_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_082_fcf_ocf_rat_lvl_63d},
    "cflo_083_fcf_ocf_rat_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_083_fcf_ocf_rat_zscore_63d},
    "cflo_084_fcf_ocf_rat_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_084_fcf_ocf_rat_rank_63d},
    "cflo_085_fcf_ocf_rat_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_085_fcf_ocf_rat_lvl_126d},
    "cflo_086_fcf_ocf_rat_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_086_fcf_ocf_rat_zscore_126d},
    "cflo_087_fcf_ocf_rat_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_087_fcf_ocf_rat_rank_126d},
    "cflo_088_fcf_ocf_rat_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_088_fcf_ocf_rat_lvl_252d},
    "cflo_089_fcf_ocf_rat_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_089_fcf_ocf_rat_zscore_252d},
    "cflo_090_fcf_ocf_rat_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_090_fcf_ocf_rat_rank_252d},
    "cflo_091_ocf_assets_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_091_ocf_assets_lvl_5d},
    "cflo_092_ocf_assets_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_092_ocf_assets_zscore_5d},
    "cflo_093_ocf_assets_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_093_ocf_assets_rank_5d},
    "cflo_094_ocf_assets_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_094_ocf_assets_lvl_21d},
    "cflo_095_ocf_assets_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_095_ocf_assets_zscore_21d},
    "cflo_096_ocf_assets_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_096_ocf_assets_rank_21d},
    "cflo_097_ocf_assets_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_097_ocf_assets_lvl_63d},
    "cflo_098_ocf_assets_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_098_ocf_assets_zscore_63d},
    "cflo_099_ocf_assets_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_099_ocf_assets_rank_63d},
    "cflo_100_ocf_assets_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_100_ocf_assets_lvl_126d},
    "cflo_101_ocf_assets_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_101_ocf_assets_zscore_126d},
    "cflo_102_ocf_assets_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_102_ocf_assets_rank_126d},
    "cflo_103_ocf_assets_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_103_ocf_assets_lvl_252d},
    "cflo_104_ocf_assets_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_104_ocf_assets_zscore_252d},
    "cflo_105_ocf_assets_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_105_ocf_assets_rank_252d},
    "cflo_106_fcf_assets_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_106_fcf_assets_lvl_5d},
    "cflo_107_fcf_assets_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_107_fcf_assets_zscore_5d},
    "cflo_108_fcf_assets_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_108_fcf_assets_rank_5d},
    "cflo_109_fcf_assets_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_109_fcf_assets_lvl_21d},
    "cflo_110_fcf_assets_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_110_fcf_assets_zscore_21d},
    "cflo_111_fcf_assets_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_111_fcf_assets_rank_21d},
    "cflo_112_fcf_assets_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_112_fcf_assets_lvl_63d},
    "cflo_113_fcf_assets_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_113_fcf_assets_zscore_63d},
    "cflo_114_fcf_assets_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_114_fcf_assets_rank_63d},
    "cflo_115_fcf_assets_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_115_fcf_assets_lvl_126d},
    "cflo_116_fcf_assets_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_116_fcf_assets_zscore_126d},
    "cflo_117_fcf_assets_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_117_fcf_assets_rank_126d},
    "cflo_118_fcf_assets_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_118_fcf_assets_lvl_252d},
    "cflo_119_fcf_assets_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_119_fcf_assets_zscore_252d},
    "cflo_120_fcf_assets_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_120_fcf_assets_rank_252d},
    "cflo_121_ocf_debt_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_121_ocf_debt_lvl_5d},
    "cflo_122_ocf_debt_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_122_ocf_debt_zscore_5d},
    "cflo_123_ocf_debt_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_123_ocf_debt_rank_5d},
    "cflo_124_ocf_debt_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_124_ocf_debt_lvl_21d},
    "cflo_125_ocf_debt_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_125_ocf_debt_zscore_21d},
    "cflo_126_ocf_debt_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_126_ocf_debt_rank_21d},
    "cflo_127_ocf_debt_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_127_ocf_debt_lvl_63d},
    "cflo_128_ocf_debt_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_128_ocf_debt_zscore_63d},
    "cflo_129_ocf_debt_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_129_ocf_debt_rank_63d},
    "cflo_130_ocf_debt_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_130_ocf_debt_lvl_126d},
    "cflo_131_ocf_debt_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_131_ocf_debt_zscore_126d},
    "cflo_132_ocf_debt_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_132_ocf_debt_rank_126d},
    "cflo_133_ocf_debt_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_133_ocf_debt_lvl_252d},
    "cflo_134_ocf_debt_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_134_ocf_debt_zscore_252d},
    "cflo_135_ocf_debt_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_135_ocf_debt_rank_252d},
    "cflo_136_fcf_equity_lvl_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_136_fcf_equity_lvl_5d},
    "cflo_137_fcf_equity_zscore_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_137_fcf_equity_zscore_5d},
    "cflo_138_fcf_equity_rank_5d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_138_fcf_equity_rank_5d},
    "cflo_139_fcf_equity_lvl_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_139_fcf_equity_lvl_21d},
    "cflo_140_fcf_equity_zscore_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_140_fcf_equity_zscore_21d},
    "cflo_141_fcf_equity_rank_21d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_141_fcf_equity_rank_21d},
    "cflo_142_fcf_equity_lvl_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_142_fcf_equity_lvl_63d},
    "cflo_143_fcf_equity_zscore_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_143_fcf_equity_zscore_63d},
    "cflo_144_fcf_equity_rank_63d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_144_fcf_equity_rank_63d},
    "cflo_145_fcf_equity_lvl_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_145_fcf_equity_lvl_126d},
    "cflo_146_fcf_equity_zscore_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_146_fcf_equity_zscore_126d},
    "cflo_147_fcf_equity_rank_126d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_147_fcf_equity_rank_126d},
    "cflo_148_fcf_equity_lvl_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_148_fcf_equity_lvl_252d},
    "cflo_149_fcf_equity_zscore_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_149_fcf_equity_zscore_252d},
    "cflo_150_fcf_equity_rank_252d": {"inputs": ["ocf", "fcf", "revenue", "sharesbas", "marketcap", "assets", "equity", "debt"], "func": cflo_150_fcf_equity_rank_252d},
}
