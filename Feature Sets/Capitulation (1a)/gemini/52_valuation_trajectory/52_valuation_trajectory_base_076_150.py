"""
52_valuation_trajectory — Base Features 076-150
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

def valt_076_evebitda_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_076_evebitda_lvl_5d"""
    base = _safe_div(marketcap, ebitda)
    return _rolling_mean(base, 5)

def valt_077_evebitda_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_077_evebitda_zscore_5d"""
    base = _safe_div(marketcap, ebitda)
    return _zscore_rolling(base, 5)

def valt_078_evebitda_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_078_evebitda_rank_5d"""
    base = _safe_div(marketcap, ebitda)
    return _rank_pct(base, 5)

def valt_079_evebitda_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_079_evebitda_lvl_21d"""
    base = _safe_div(marketcap, ebitda)
    return _rolling_mean(base, 21)

def valt_080_evebitda_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_080_evebitda_zscore_21d"""
    base = _safe_div(marketcap, ebitda)
    return _zscore_rolling(base, 21)

def valt_081_evebitda_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_081_evebitda_rank_21d"""
    base = _safe_div(marketcap, ebitda)
    return _rank_pct(base, 21)

def valt_082_evebitda_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_082_evebitda_lvl_63d"""
    base = _safe_div(marketcap, ebitda)
    return _rolling_mean(base, 63)

def valt_083_evebitda_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_083_evebitda_zscore_63d"""
    base = _safe_div(marketcap, ebitda)
    return _zscore_rolling(base, 63)

def valt_084_evebitda_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_084_evebitda_rank_63d"""
    base = _safe_div(marketcap, ebitda)
    return _rank_pct(base, 63)

def valt_085_evebitda_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_085_evebitda_lvl_126d"""
    base = _safe_div(marketcap, ebitda)
    return _rolling_mean(base, 126)

def valt_086_evebitda_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_086_evebitda_zscore_126d"""
    base = _safe_div(marketcap, ebitda)
    return _zscore_rolling(base, 126)

def valt_087_evebitda_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_087_evebitda_rank_126d"""
    base = _safe_div(marketcap, ebitda)
    return _rank_pct(base, 126)

def valt_088_evebitda_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_088_evebitda_lvl_252d"""
    base = _safe_div(marketcap, ebitda)
    return _rolling_mean(base, 252)

def valt_089_evebitda_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_089_evebitda_zscore_252d"""
    base = _safe_div(marketcap, ebitda)
    return _zscore_rolling(base, 252)

def valt_090_evebitda_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_090_evebitda_rank_252d"""
    base = _safe_div(marketcap, ebitda)
    return _rank_pct(base, 252)

def valt_091_mktcap_equity_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_091_mktcap_equity_lvl_5d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 5)

def valt_092_mktcap_equity_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_092_mktcap_equity_zscore_5d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 5)

def valt_093_mktcap_equity_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_093_mktcap_equity_rank_5d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 5)

def valt_094_mktcap_equity_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_094_mktcap_equity_lvl_21d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 21)

def valt_095_mktcap_equity_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_095_mktcap_equity_zscore_21d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 21)

def valt_096_mktcap_equity_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_096_mktcap_equity_rank_21d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 21)

def valt_097_mktcap_equity_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_097_mktcap_equity_lvl_63d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 63)

def valt_098_mktcap_equity_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_098_mktcap_equity_zscore_63d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 63)

def valt_099_mktcap_equity_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_099_mktcap_equity_rank_63d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 63)

def valt_100_mktcap_equity_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_100_mktcap_equity_lvl_126d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 126)

def valt_101_mktcap_equity_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_101_mktcap_equity_zscore_126d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 126)

def valt_102_mktcap_equity_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_102_mktcap_equity_rank_126d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 126)

def valt_103_mktcap_equity_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_103_mktcap_equity_lvl_252d"""
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 252)

def valt_104_mktcap_equity_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_104_mktcap_equity_zscore_252d"""
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 252)

def valt_105_mktcap_equity_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_105_mktcap_equity_rank_252d"""
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 252)

def valt_106_price_to_ocf_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_106_price_to_ocf_lvl_5d"""
    base = _safe_div(marketcap, ocf)
    return _rolling_mean(base, 5)

def valt_107_price_to_ocf_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_107_price_to_ocf_zscore_5d"""
    base = _safe_div(marketcap, ocf)
    return _zscore_rolling(base, 5)

def valt_108_price_to_ocf_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_108_price_to_ocf_rank_5d"""
    base = _safe_div(marketcap, ocf)
    return _rank_pct(base, 5)

def valt_109_price_to_ocf_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_109_price_to_ocf_lvl_21d"""
    base = _safe_div(marketcap, ocf)
    return _rolling_mean(base, 21)

def valt_110_price_to_ocf_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_110_price_to_ocf_zscore_21d"""
    base = _safe_div(marketcap, ocf)
    return _zscore_rolling(base, 21)

def valt_111_price_to_ocf_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_111_price_to_ocf_rank_21d"""
    base = _safe_div(marketcap, ocf)
    return _rank_pct(base, 21)

def valt_112_price_to_ocf_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_112_price_to_ocf_lvl_63d"""
    base = _safe_div(marketcap, ocf)
    return _rolling_mean(base, 63)

def valt_113_price_to_ocf_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_113_price_to_ocf_zscore_63d"""
    base = _safe_div(marketcap, ocf)
    return _zscore_rolling(base, 63)

def valt_114_price_to_ocf_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_114_price_to_ocf_rank_63d"""
    base = _safe_div(marketcap, ocf)
    return _rank_pct(base, 63)

def valt_115_price_to_ocf_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_115_price_to_ocf_lvl_126d"""
    base = _safe_div(marketcap, ocf)
    return _rolling_mean(base, 126)

def valt_116_price_to_ocf_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_116_price_to_ocf_zscore_126d"""
    base = _safe_div(marketcap, ocf)
    return _zscore_rolling(base, 126)

def valt_117_price_to_ocf_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_117_price_to_ocf_rank_126d"""
    base = _safe_div(marketcap, ocf)
    return _rank_pct(base, 126)

def valt_118_price_to_ocf_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_118_price_to_ocf_lvl_252d"""
    base = _safe_div(marketcap, ocf)
    return _rolling_mean(base, 252)

def valt_119_price_to_ocf_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_119_price_to_ocf_zscore_252d"""
    base = _safe_div(marketcap, ocf)
    return _zscore_rolling(base, 252)

def valt_120_price_to_ocf_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_120_price_to_ocf_rank_252d"""
    base = _safe_div(marketcap, ocf)
    return _rank_pct(base, 252)

def valt_121_val_z_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_121_val_z_lvl_5d"""
    base = _zscore_rolling(ps, 252)
    return _rolling_mean(base, 5)

def valt_122_val_z_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_122_val_z_zscore_5d"""
    base = _zscore_rolling(ps, 252)
    return _zscore_rolling(base, 5)

def valt_123_val_z_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_123_val_z_rank_5d"""
    base = _zscore_rolling(ps, 252)
    return _rank_pct(base, 5)

def valt_124_val_z_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_124_val_z_lvl_21d"""
    base = _zscore_rolling(ps, 252)
    return _rolling_mean(base, 21)

def valt_125_val_z_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_125_val_z_zscore_21d"""
    base = _zscore_rolling(ps, 252)
    return _zscore_rolling(base, 21)

def valt_126_val_z_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_126_val_z_rank_21d"""
    base = _zscore_rolling(ps, 252)
    return _rank_pct(base, 21)

def valt_127_val_z_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_127_val_z_lvl_63d"""
    base = _zscore_rolling(ps, 252)
    return _rolling_mean(base, 63)

def valt_128_val_z_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_128_val_z_zscore_63d"""
    base = _zscore_rolling(ps, 252)
    return _zscore_rolling(base, 63)

def valt_129_val_z_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_129_val_z_rank_63d"""
    base = _zscore_rolling(ps, 252)
    return _rank_pct(base, 63)

def valt_130_val_z_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_130_val_z_lvl_126d"""
    base = _zscore_rolling(ps, 252)
    return _rolling_mean(base, 126)

def valt_131_val_z_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_131_val_z_zscore_126d"""
    base = _zscore_rolling(ps, 252)
    return _zscore_rolling(base, 126)

def valt_132_val_z_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_132_val_z_rank_126d"""
    base = _zscore_rolling(ps, 252)
    return _rank_pct(base, 126)

def valt_133_val_z_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_133_val_z_lvl_252d"""
    base = _zscore_rolling(ps, 252)
    return _rolling_mean(base, 252)

def valt_134_val_z_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_134_val_z_zscore_252d"""
    base = _zscore_rolling(ps, 252)
    return _zscore_rolling(base, 252)

def valt_135_val_z_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_135_val_z_rank_252d"""
    base = _zscore_rolling(ps, 252)
    return _rank_pct(base, 252)

def valt_136_val_rank_lvl_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_136_val_rank_lvl_5d"""
    base = _rank_pct(ps, 252)
    return _rolling_mean(base, 5)

def valt_137_val_rank_zscore_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_137_val_rank_zscore_5d"""
    base = _rank_pct(ps, 252)
    return _zscore_rolling(base, 5)

def valt_138_val_rank_rank_5d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_138_val_rank_rank_5d"""
    base = _rank_pct(ps, 252)
    return _rank_pct(base, 5)

def valt_139_val_rank_lvl_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_139_val_rank_lvl_21d"""
    base = _rank_pct(ps, 252)
    return _rolling_mean(base, 21)

def valt_140_val_rank_zscore_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_140_val_rank_zscore_21d"""
    base = _rank_pct(ps, 252)
    return _zscore_rolling(base, 21)

def valt_141_val_rank_rank_21d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_141_val_rank_rank_21d"""
    base = _rank_pct(ps, 252)
    return _rank_pct(base, 21)

def valt_142_val_rank_lvl_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_142_val_rank_lvl_63d"""
    base = _rank_pct(ps, 252)
    return _rolling_mean(base, 63)

def valt_143_val_rank_zscore_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_143_val_rank_zscore_63d"""
    base = _rank_pct(ps, 252)
    return _zscore_rolling(base, 63)

def valt_144_val_rank_rank_63d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_144_val_rank_rank_63d"""
    base = _rank_pct(ps, 252)
    return _rank_pct(base, 63)

def valt_145_val_rank_lvl_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_145_val_rank_lvl_126d"""
    base = _rank_pct(ps, 252)
    return _rolling_mean(base, 126)

def valt_146_val_rank_zscore_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_146_val_rank_zscore_126d"""
    base = _rank_pct(ps, 252)
    return _zscore_rolling(base, 126)

def valt_147_val_rank_rank_126d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_147_val_rank_rank_126d"""
    base = _rank_pct(ps, 252)
    return _rank_pct(base, 126)

def valt_148_val_rank_lvl_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_148_val_rank_lvl_252d"""
    base = _rank_pct(ps, 252)
    return _rolling_mean(base, 252)

def valt_149_val_rank_zscore_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_149_val_rank_zscore_252d"""
    base = _rank_pct(ps, 252)
    return _zscore_rolling(base, 252)

def valt_150_val_rank_rank_252d(ps: pd.Series, pb: pd.Series, marketcap: pd.Series, netinc: pd.Series, revenue: pd.Series, equity: pd.Series, ebitda: pd.Series, ocf: pd.Series) -> pd.Series:
    """valt_150_val_rank_rank_252d"""
    base = _rank_pct(ps, 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V52_REGISTRY_2 = {
    "valt_076_evebitda_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_076_evebitda_lvl_5d},
    "valt_077_evebitda_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_077_evebitda_zscore_5d},
    "valt_078_evebitda_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_078_evebitda_rank_5d},
    "valt_079_evebitda_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_079_evebitda_lvl_21d},
    "valt_080_evebitda_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_080_evebitda_zscore_21d},
    "valt_081_evebitda_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_081_evebitda_rank_21d},
    "valt_082_evebitda_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_082_evebitda_lvl_63d},
    "valt_083_evebitda_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_083_evebitda_zscore_63d},
    "valt_084_evebitda_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_084_evebitda_rank_63d},
    "valt_085_evebitda_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_085_evebitda_lvl_126d},
    "valt_086_evebitda_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_086_evebitda_zscore_126d},
    "valt_087_evebitda_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_087_evebitda_rank_126d},
    "valt_088_evebitda_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_088_evebitda_lvl_252d},
    "valt_089_evebitda_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_089_evebitda_zscore_252d},
    "valt_090_evebitda_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_090_evebitda_rank_252d},
    "valt_091_mktcap_equity_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_091_mktcap_equity_lvl_5d},
    "valt_092_mktcap_equity_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_092_mktcap_equity_zscore_5d},
    "valt_093_mktcap_equity_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_093_mktcap_equity_rank_5d},
    "valt_094_mktcap_equity_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_094_mktcap_equity_lvl_21d},
    "valt_095_mktcap_equity_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_095_mktcap_equity_zscore_21d},
    "valt_096_mktcap_equity_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_096_mktcap_equity_rank_21d},
    "valt_097_mktcap_equity_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_097_mktcap_equity_lvl_63d},
    "valt_098_mktcap_equity_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_098_mktcap_equity_zscore_63d},
    "valt_099_mktcap_equity_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_099_mktcap_equity_rank_63d},
    "valt_100_mktcap_equity_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_100_mktcap_equity_lvl_126d},
    "valt_101_mktcap_equity_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_101_mktcap_equity_zscore_126d},
    "valt_102_mktcap_equity_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_102_mktcap_equity_rank_126d},
    "valt_103_mktcap_equity_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_103_mktcap_equity_lvl_252d},
    "valt_104_mktcap_equity_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_104_mktcap_equity_zscore_252d},
    "valt_105_mktcap_equity_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_105_mktcap_equity_rank_252d},
    "valt_106_price_to_ocf_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_106_price_to_ocf_lvl_5d},
    "valt_107_price_to_ocf_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_107_price_to_ocf_zscore_5d},
    "valt_108_price_to_ocf_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_108_price_to_ocf_rank_5d},
    "valt_109_price_to_ocf_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_109_price_to_ocf_lvl_21d},
    "valt_110_price_to_ocf_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_110_price_to_ocf_zscore_21d},
    "valt_111_price_to_ocf_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_111_price_to_ocf_rank_21d},
    "valt_112_price_to_ocf_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_112_price_to_ocf_lvl_63d},
    "valt_113_price_to_ocf_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_113_price_to_ocf_zscore_63d},
    "valt_114_price_to_ocf_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_114_price_to_ocf_rank_63d},
    "valt_115_price_to_ocf_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_115_price_to_ocf_lvl_126d},
    "valt_116_price_to_ocf_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_116_price_to_ocf_zscore_126d},
    "valt_117_price_to_ocf_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_117_price_to_ocf_rank_126d},
    "valt_118_price_to_ocf_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_118_price_to_ocf_lvl_252d},
    "valt_119_price_to_ocf_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_119_price_to_ocf_zscore_252d},
    "valt_120_price_to_ocf_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_120_price_to_ocf_rank_252d},
    "valt_121_val_z_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_121_val_z_lvl_5d},
    "valt_122_val_z_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_122_val_z_zscore_5d},
    "valt_123_val_z_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_123_val_z_rank_5d},
    "valt_124_val_z_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_124_val_z_lvl_21d},
    "valt_125_val_z_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_125_val_z_zscore_21d},
    "valt_126_val_z_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_126_val_z_rank_21d},
    "valt_127_val_z_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_127_val_z_lvl_63d},
    "valt_128_val_z_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_128_val_z_zscore_63d},
    "valt_129_val_z_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_129_val_z_rank_63d},
    "valt_130_val_z_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_130_val_z_lvl_126d},
    "valt_131_val_z_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_131_val_z_zscore_126d},
    "valt_132_val_z_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_132_val_z_rank_126d},
    "valt_133_val_z_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_133_val_z_lvl_252d},
    "valt_134_val_z_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_134_val_z_zscore_252d},
    "valt_135_val_z_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_135_val_z_rank_252d},
    "valt_136_val_rank_lvl_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_136_val_rank_lvl_5d},
    "valt_137_val_rank_zscore_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_137_val_rank_zscore_5d},
    "valt_138_val_rank_rank_5d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_138_val_rank_rank_5d},
    "valt_139_val_rank_lvl_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_139_val_rank_lvl_21d},
    "valt_140_val_rank_zscore_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_140_val_rank_zscore_21d},
    "valt_141_val_rank_rank_21d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_141_val_rank_rank_21d},
    "valt_142_val_rank_lvl_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_142_val_rank_lvl_63d},
    "valt_143_val_rank_zscore_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_143_val_rank_zscore_63d},
    "valt_144_val_rank_rank_63d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_144_val_rank_rank_63d},
    "valt_145_val_rank_lvl_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_145_val_rank_lvl_126d},
    "valt_146_val_rank_zscore_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_146_val_rank_zscore_126d},
    "valt_147_val_rank_rank_126d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_147_val_rank_rank_126d},
    "valt_148_val_rank_lvl_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_148_val_rank_lvl_252d},
    "valt_149_val_rank_zscore_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_149_val_rank_zscore_252d},
    "valt_150_val_rank_rank_252d": {"inputs": ["ps", "pb", "marketcap", "netinc", "revenue", "equity", "ebitda", "ocf"], "func": valt_150_val_rank_rank_252d},
}
