"""
40_leverage_and_solvency — Base Features 076-150
Domain: leverage_and_solvency
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

def solv_076_liabs_lvl_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_076_liabs_lvl_lvl_5d"""
    base = liabs
    return _rolling_mean(base, 5)

def solv_077_liabs_lvl_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_077_liabs_lvl_zscore_5d"""
    base = liabs
    return _zscore_rolling(base, 5)

def solv_078_liabs_lvl_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_078_liabs_lvl_rank_5d"""
    base = liabs
    return _rank_pct(base, 5)

def solv_079_liabs_lvl_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_079_liabs_lvl_lvl_21d"""
    base = liabs
    return _rolling_mean(base, 21)

def solv_080_liabs_lvl_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_080_liabs_lvl_zscore_21d"""
    base = liabs
    return _zscore_rolling(base, 21)

def solv_081_liabs_lvl_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_081_liabs_lvl_rank_21d"""
    base = liabs
    return _rank_pct(base, 21)

def solv_082_liabs_lvl_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_082_liabs_lvl_lvl_63d"""
    base = liabs
    return _rolling_mean(base, 63)

def solv_083_liabs_lvl_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_083_liabs_lvl_zscore_63d"""
    base = liabs
    return _zscore_rolling(base, 63)

def solv_084_liabs_lvl_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_084_liabs_lvl_rank_63d"""
    base = liabs
    return _rank_pct(base, 63)

def solv_085_liabs_lvl_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_085_liabs_lvl_lvl_126d"""
    base = liabs
    return _rolling_mean(base, 126)

def solv_086_liabs_lvl_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_086_liabs_lvl_zscore_126d"""
    base = liabs
    return _zscore_rolling(base, 126)

def solv_087_liabs_lvl_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_087_liabs_lvl_rank_126d"""
    base = liabs
    return _rank_pct(base, 126)

def solv_088_liabs_lvl_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_088_liabs_lvl_lvl_252d"""
    base = liabs
    return _rolling_mean(base, 252)

def solv_089_liabs_lvl_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_089_liabs_lvl_zscore_252d"""
    base = liabs
    return _zscore_rolling(base, 252)

def solv_090_liabs_lvl_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_090_liabs_lvl_rank_252d"""
    base = liabs
    return _rank_pct(base, 252)

def solv_091_assets_eq_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_091_assets_eq_lvl_5d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 5)

def solv_092_assets_eq_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_092_assets_eq_zscore_5d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 5)

def solv_093_assets_eq_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_093_assets_eq_rank_5d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 5)

def solv_094_assets_eq_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_094_assets_eq_lvl_21d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 21)

def solv_095_assets_eq_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_095_assets_eq_zscore_21d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 21)

def solv_096_assets_eq_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_096_assets_eq_rank_21d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 21)

def solv_097_assets_eq_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_097_assets_eq_lvl_63d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 63)

def solv_098_assets_eq_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_098_assets_eq_zscore_63d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 63)

def solv_099_assets_eq_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_099_assets_eq_rank_63d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 63)

def solv_100_assets_eq_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_100_assets_eq_lvl_126d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 126)

def solv_101_assets_eq_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_101_assets_eq_zscore_126d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 126)

def solv_102_assets_eq_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_102_assets_eq_rank_126d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 126)

def solv_103_assets_eq_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_103_assets_eq_lvl_252d"""
    base = _safe_div(assets, equity)
    return _rolling_mean(base, 252)

def solv_104_assets_eq_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_104_assets_eq_zscore_252d"""
    base = _safe_div(assets, equity)
    return _zscore_rolling(base, 252)

def solv_105_assets_eq_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_105_assets_eq_rank_252d"""
    base = _safe_div(assets, equity)
    return _rank_pct(base, 252)

def solv_106_debt_ocf_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_106_debt_ocf_lvl_5d"""
    base = _safe_div(debt, ocf.abs())
    return _rolling_mean(base, 5)

def solv_107_debt_ocf_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_107_debt_ocf_zscore_5d"""
    base = _safe_div(debt, ocf.abs())
    return _zscore_rolling(base, 5)

def solv_108_debt_ocf_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_108_debt_ocf_rank_5d"""
    base = _safe_div(debt, ocf.abs())
    return _rank_pct(base, 5)

def solv_109_debt_ocf_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_109_debt_ocf_lvl_21d"""
    base = _safe_div(debt, ocf.abs())
    return _rolling_mean(base, 21)

def solv_110_debt_ocf_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_110_debt_ocf_zscore_21d"""
    base = _safe_div(debt, ocf.abs())
    return _zscore_rolling(base, 21)

def solv_111_debt_ocf_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_111_debt_ocf_rank_21d"""
    base = _safe_div(debt, ocf.abs())
    return _rank_pct(base, 21)

def solv_112_debt_ocf_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_112_debt_ocf_lvl_63d"""
    base = _safe_div(debt, ocf.abs())
    return _rolling_mean(base, 63)

def solv_113_debt_ocf_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_113_debt_ocf_zscore_63d"""
    base = _safe_div(debt, ocf.abs())
    return _zscore_rolling(base, 63)

def solv_114_debt_ocf_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_114_debt_ocf_rank_63d"""
    base = _safe_div(debt, ocf.abs())
    return _rank_pct(base, 63)

def solv_115_debt_ocf_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_115_debt_ocf_lvl_126d"""
    base = _safe_div(debt, ocf.abs())
    return _rolling_mean(base, 126)

def solv_116_debt_ocf_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_116_debt_ocf_zscore_126d"""
    base = _safe_div(debt, ocf.abs())
    return _zscore_rolling(base, 126)

def solv_117_debt_ocf_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_117_debt_ocf_rank_126d"""
    base = _safe_div(debt, ocf.abs())
    return _rank_pct(base, 126)

def solv_118_debt_ocf_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_118_debt_ocf_lvl_252d"""
    base = _safe_div(debt, ocf.abs())
    return _rolling_mean(base, 252)

def solv_119_debt_ocf_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_119_debt_ocf_zscore_252d"""
    base = _safe_div(debt, ocf.abs())
    return _zscore_rolling(base, 252)

def solv_120_debt_ocf_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_120_debt_ocf_rank_252d"""
    base = _safe_div(debt, ocf.abs())
    return _rank_pct(base, 252)

def solv_121_debt_fcf_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_121_debt_fcf_lvl_5d"""
    base = _safe_div(debt, fcf.abs())
    return _rolling_mean(base, 5)

def solv_122_debt_fcf_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_122_debt_fcf_zscore_5d"""
    base = _safe_div(debt, fcf.abs())
    return _zscore_rolling(base, 5)

def solv_123_debt_fcf_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_123_debt_fcf_rank_5d"""
    base = _safe_div(debt, fcf.abs())
    return _rank_pct(base, 5)

def solv_124_debt_fcf_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_124_debt_fcf_lvl_21d"""
    base = _safe_div(debt, fcf.abs())
    return _rolling_mean(base, 21)

def solv_125_debt_fcf_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_125_debt_fcf_zscore_21d"""
    base = _safe_div(debt, fcf.abs())
    return _zscore_rolling(base, 21)

def solv_126_debt_fcf_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_126_debt_fcf_rank_21d"""
    base = _safe_div(debt, fcf.abs())
    return _rank_pct(base, 21)

def solv_127_debt_fcf_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_127_debt_fcf_lvl_63d"""
    base = _safe_div(debt, fcf.abs())
    return _rolling_mean(base, 63)

def solv_128_debt_fcf_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_128_debt_fcf_zscore_63d"""
    base = _safe_div(debt, fcf.abs())
    return _zscore_rolling(base, 63)

def solv_129_debt_fcf_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_129_debt_fcf_rank_63d"""
    base = _safe_div(debt, fcf.abs())
    return _rank_pct(base, 63)

def solv_130_debt_fcf_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_130_debt_fcf_lvl_126d"""
    base = _safe_div(debt, fcf.abs())
    return _rolling_mean(base, 126)

def solv_131_debt_fcf_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_131_debt_fcf_zscore_126d"""
    base = _safe_div(debt, fcf.abs())
    return _zscore_rolling(base, 126)

def solv_132_debt_fcf_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_132_debt_fcf_rank_126d"""
    base = _safe_div(debt, fcf.abs())
    return _rank_pct(base, 126)

def solv_133_debt_fcf_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_133_debt_fcf_lvl_252d"""
    base = _safe_div(debt, fcf.abs())
    return _rolling_mean(base, 252)

def solv_134_debt_fcf_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_134_debt_fcf_zscore_252d"""
    base = _safe_div(debt, fcf.abs())
    return _zscore_rolling(base, 252)

def solv_135_debt_fcf_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_135_debt_fcf_rank_252d"""
    base = _safe_div(debt, fcf.abs())
    return _rank_pct(base, 252)

def solv_136_liabs_assets_lvl_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_136_liabs_assets_lvl_5d"""
    base = _safe_div(liabs, assets)
    return _rolling_mean(base, 5)

def solv_137_liabs_assets_zscore_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_137_liabs_assets_zscore_5d"""
    base = _safe_div(liabs, assets)
    return _zscore_rolling(base, 5)

def solv_138_liabs_assets_rank_5d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_138_liabs_assets_rank_5d"""
    base = _safe_div(liabs, assets)
    return _rank_pct(base, 5)

def solv_139_liabs_assets_lvl_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_139_liabs_assets_lvl_21d"""
    base = _safe_div(liabs, assets)
    return _rolling_mean(base, 21)

def solv_140_liabs_assets_zscore_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_140_liabs_assets_zscore_21d"""
    base = _safe_div(liabs, assets)
    return _zscore_rolling(base, 21)

def solv_141_liabs_assets_rank_21d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_141_liabs_assets_rank_21d"""
    base = _safe_div(liabs, assets)
    return _rank_pct(base, 21)

def solv_142_liabs_assets_lvl_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_142_liabs_assets_lvl_63d"""
    base = _safe_div(liabs, assets)
    return _rolling_mean(base, 63)

def solv_143_liabs_assets_zscore_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_143_liabs_assets_zscore_63d"""
    base = _safe_div(liabs, assets)
    return _zscore_rolling(base, 63)

def solv_144_liabs_assets_rank_63d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_144_liabs_assets_rank_63d"""
    base = _safe_div(liabs, assets)
    return _rank_pct(base, 63)

def solv_145_liabs_assets_lvl_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_145_liabs_assets_lvl_126d"""
    base = _safe_div(liabs, assets)
    return _rolling_mean(base, 126)

def solv_146_liabs_assets_zscore_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_146_liabs_assets_zscore_126d"""
    base = _safe_div(liabs, assets)
    return _zscore_rolling(base, 126)

def solv_147_liabs_assets_rank_126d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_147_liabs_assets_rank_126d"""
    base = _safe_div(liabs, assets)
    return _rank_pct(base, 126)

def solv_148_liabs_assets_lvl_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_148_liabs_assets_lvl_252d"""
    base = _safe_div(liabs, assets)
    return _rolling_mean(base, 252)

def solv_149_liabs_assets_zscore_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_149_liabs_assets_zscore_252d"""
    base = _safe_div(liabs, assets)
    return _zscore_rolling(base, 252)

def solv_150_liabs_assets_rank_252d(debt: pd.Series, equity: pd.Series, assets: pd.Series, opinc: pd.Series, liabs: pd.Series, ocf: pd.Series, fcf: pd.Series) -> pd.Series:
    """solv_150_liabs_assets_rank_252d"""
    base = _safe_div(liabs, assets)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V40_REGISTRY_2 = {
    "solv_076_liabs_lvl_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_076_liabs_lvl_lvl_5d},
    "solv_077_liabs_lvl_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_077_liabs_lvl_zscore_5d},
    "solv_078_liabs_lvl_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_078_liabs_lvl_rank_5d},
    "solv_079_liabs_lvl_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_079_liabs_lvl_lvl_21d},
    "solv_080_liabs_lvl_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_080_liabs_lvl_zscore_21d},
    "solv_081_liabs_lvl_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_081_liabs_lvl_rank_21d},
    "solv_082_liabs_lvl_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_082_liabs_lvl_lvl_63d},
    "solv_083_liabs_lvl_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_083_liabs_lvl_zscore_63d},
    "solv_084_liabs_lvl_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_084_liabs_lvl_rank_63d},
    "solv_085_liabs_lvl_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_085_liabs_lvl_lvl_126d},
    "solv_086_liabs_lvl_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_086_liabs_lvl_zscore_126d},
    "solv_087_liabs_lvl_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_087_liabs_lvl_rank_126d},
    "solv_088_liabs_lvl_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_088_liabs_lvl_lvl_252d},
    "solv_089_liabs_lvl_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_089_liabs_lvl_zscore_252d},
    "solv_090_liabs_lvl_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_090_liabs_lvl_rank_252d},
    "solv_091_assets_eq_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_091_assets_eq_lvl_5d},
    "solv_092_assets_eq_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_092_assets_eq_zscore_5d},
    "solv_093_assets_eq_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_093_assets_eq_rank_5d},
    "solv_094_assets_eq_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_094_assets_eq_lvl_21d},
    "solv_095_assets_eq_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_095_assets_eq_zscore_21d},
    "solv_096_assets_eq_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_096_assets_eq_rank_21d},
    "solv_097_assets_eq_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_097_assets_eq_lvl_63d},
    "solv_098_assets_eq_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_098_assets_eq_zscore_63d},
    "solv_099_assets_eq_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_099_assets_eq_rank_63d},
    "solv_100_assets_eq_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_100_assets_eq_lvl_126d},
    "solv_101_assets_eq_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_101_assets_eq_zscore_126d},
    "solv_102_assets_eq_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_102_assets_eq_rank_126d},
    "solv_103_assets_eq_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_103_assets_eq_lvl_252d},
    "solv_104_assets_eq_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_104_assets_eq_zscore_252d},
    "solv_105_assets_eq_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_105_assets_eq_rank_252d},
    "solv_106_debt_ocf_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_106_debt_ocf_lvl_5d},
    "solv_107_debt_ocf_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_107_debt_ocf_zscore_5d},
    "solv_108_debt_ocf_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_108_debt_ocf_rank_5d},
    "solv_109_debt_ocf_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_109_debt_ocf_lvl_21d},
    "solv_110_debt_ocf_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_110_debt_ocf_zscore_21d},
    "solv_111_debt_ocf_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_111_debt_ocf_rank_21d},
    "solv_112_debt_ocf_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_112_debt_ocf_lvl_63d},
    "solv_113_debt_ocf_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_113_debt_ocf_zscore_63d},
    "solv_114_debt_ocf_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_114_debt_ocf_rank_63d},
    "solv_115_debt_ocf_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_115_debt_ocf_lvl_126d},
    "solv_116_debt_ocf_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_116_debt_ocf_zscore_126d},
    "solv_117_debt_ocf_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_117_debt_ocf_rank_126d},
    "solv_118_debt_ocf_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_118_debt_ocf_lvl_252d},
    "solv_119_debt_ocf_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_119_debt_ocf_zscore_252d},
    "solv_120_debt_ocf_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_120_debt_ocf_rank_252d},
    "solv_121_debt_fcf_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_121_debt_fcf_lvl_5d},
    "solv_122_debt_fcf_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_122_debt_fcf_zscore_5d},
    "solv_123_debt_fcf_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_123_debt_fcf_rank_5d},
    "solv_124_debt_fcf_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_124_debt_fcf_lvl_21d},
    "solv_125_debt_fcf_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_125_debt_fcf_zscore_21d},
    "solv_126_debt_fcf_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_126_debt_fcf_rank_21d},
    "solv_127_debt_fcf_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_127_debt_fcf_lvl_63d},
    "solv_128_debt_fcf_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_128_debt_fcf_zscore_63d},
    "solv_129_debt_fcf_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_129_debt_fcf_rank_63d},
    "solv_130_debt_fcf_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_130_debt_fcf_lvl_126d},
    "solv_131_debt_fcf_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_131_debt_fcf_zscore_126d},
    "solv_132_debt_fcf_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_132_debt_fcf_rank_126d},
    "solv_133_debt_fcf_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_133_debt_fcf_lvl_252d},
    "solv_134_debt_fcf_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_134_debt_fcf_zscore_252d},
    "solv_135_debt_fcf_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_135_debt_fcf_rank_252d},
    "solv_136_liabs_assets_lvl_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_136_liabs_assets_lvl_5d},
    "solv_137_liabs_assets_zscore_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_137_liabs_assets_zscore_5d},
    "solv_138_liabs_assets_rank_5d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_138_liabs_assets_rank_5d},
    "solv_139_liabs_assets_lvl_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_139_liabs_assets_lvl_21d},
    "solv_140_liabs_assets_zscore_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_140_liabs_assets_zscore_21d},
    "solv_141_liabs_assets_rank_21d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_141_liabs_assets_rank_21d},
    "solv_142_liabs_assets_lvl_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_142_liabs_assets_lvl_63d},
    "solv_143_liabs_assets_zscore_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_143_liabs_assets_zscore_63d},
    "solv_144_liabs_assets_rank_63d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_144_liabs_assets_rank_63d},
    "solv_145_liabs_assets_lvl_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_145_liabs_assets_lvl_126d},
    "solv_146_liabs_assets_zscore_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_146_liabs_assets_zscore_126d},
    "solv_147_liabs_assets_rank_126d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_147_liabs_assets_rank_126d},
    "solv_148_liabs_assets_lvl_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_148_liabs_assets_lvl_252d},
    "solv_149_liabs_assets_zscore_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_149_liabs_assets_zscore_252d},
    "solv_150_liabs_assets_rank_252d": {"inputs": ["debt", "equity", "assets", "opinc", "liabs", "ocf", "fcf"], "func": solv_150_liabs_assets_rank_252d},
}
