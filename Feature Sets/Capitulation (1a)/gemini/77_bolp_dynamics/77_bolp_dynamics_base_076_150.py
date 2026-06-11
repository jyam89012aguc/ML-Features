"""
77_bolp_dynamics — Base Features 076-150
Domain: bolp_dynamics
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
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std().fillna(0)

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _rsi(s: pd.Series, w: int) -> pd.Series:
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w).mean()
    rs = _safe_div(gain, loss)
    return 100 - (100 / (1 + rs))

# ── Feature functions ────────────────────────────────────────────────────────

def bolp_076_bb_dist_l_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_076_bb_dist_l_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 5)

def bolp_077_bb_dist_l_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_077_bb_dist_l_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 5)

def bolp_078_bb_dist_l_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_078_bb_dist_l_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rank_pct(base, 5)

def bolp_079_bb_dist_l_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_079_bb_dist_l_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 21)

def bolp_080_bb_dist_l_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_080_bb_dist_l_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 21)

def bolp_081_bb_dist_l_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_081_bb_dist_l_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rank_pct(base, 21)

def bolp_082_bb_dist_l_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_082_bb_dist_l_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 63)

def bolp_083_bb_dist_l_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_083_bb_dist_l_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 63)

def bolp_084_bb_dist_l_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_084_bb_dist_l_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rank_pct(base, 63)

def bolp_085_bb_dist_l_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_085_bb_dist_l_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 126)

def bolp_086_bb_dist_l_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_086_bb_dist_l_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 126)

def bolp_087_bb_dist_l_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_087_bb_dist_l_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rank_pct(base, 126)

def bolp_088_bb_dist_l_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_088_bb_dist_l_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 252)

def bolp_089_bb_dist_l_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_089_bb_dist_l_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 252)

def bolp_090_bb_dist_l_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_090_bb_dist_l_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) - 2 * _rolling_std(close, 20))
    return _rank_pct(base, 252)

def bolp_091_bb_sma_dist_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_091_bb_sma_dist_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 5)

def bolp_092_bb_sma_dist_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_092_bb_sma_dist_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 5)

def bolp_093_bb_sma_dist_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_093_bb_sma_dist_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 5)

def bolp_094_bb_sma_dist_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_094_bb_sma_dist_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 21)

def bolp_095_bb_sma_dist_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_095_bb_sma_dist_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 21)

def bolp_096_bb_sma_dist_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_096_bb_sma_dist_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 21)

def bolp_097_bb_sma_dist_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_097_bb_sma_dist_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 63)

def bolp_098_bb_sma_dist_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_098_bb_sma_dist_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 63)

def bolp_099_bb_sma_dist_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_099_bb_sma_dist_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 63)

def bolp_100_bb_sma_dist_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_100_bb_sma_dist_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 126)

def bolp_101_bb_sma_dist_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_101_bb_sma_dist_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 126)

def bolp_102_bb_sma_dist_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_102_bb_sma_dist_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 126)

def bolp_103_bb_sma_dist_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_103_bb_sma_dist_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 252)

def bolp_104_bb_sma_dist_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_104_bb_sma_dist_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 252)

def bolp_105_bb_sma_dist_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_105_bb_sma_dist_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 252)

def bolp_106_bb_width_z_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_106_bb_width_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 5)

def bolp_107_bb_width_z_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_107_bb_width_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 5)

def bolp_108_bb_width_z_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_108_bb_width_z_rank_5d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 5)

def bolp_109_bb_width_z_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_109_bb_width_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 21)

def bolp_110_bb_width_z_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_110_bb_width_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 21)

def bolp_111_bb_width_z_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_111_bb_width_z_rank_21d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 21)

def bolp_112_bb_width_z_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_112_bb_width_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 63)

def bolp_113_bb_width_z_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_113_bb_width_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 63)

def bolp_114_bb_width_z_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_114_bb_width_z_rank_63d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 63)

def bolp_115_bb_width_z_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_115_bb_width_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 126)

def bolp_116_bb_width_z_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_116_bb_width_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 126)

def bolp_117_bb_width_z_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_117_bb_width_z_rank_126d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 126)

def bolp_118_bb_width_z_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_118_bb_width_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rolling_mean(base, 252)

def bolp_119_bb_width_z_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_119_bb_width_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _zscore_rolling(base, 252)

def bolp_120_bb_width_z_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_120_bb_width_z_rank_252d"""
    base = _zscore_rolling(_safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20)), 63)
    return _rank_pct(base, 252)

def bolp_121_bb_pctb_z_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_121_bb_pctb_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rolling_mean(base, 5)

def bolp_122_bb_pctb_z_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_122_bb_pctb_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _zscore_rolling(base, 5)

def bolp_123_bb_pctb_z_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_123_bb_pctb_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rank_pct(base, 5)

def bolp_124_bb_pctb_z_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_124_bb_pctb_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rolling_mean(base, 21)

def bolp_125_bb_pctb_z_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_125_bb_pctb_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _zscore_rolling(base, 21)

def bolp_126_bb_pctb_z_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_126_bb_pctb_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rank_pct(base, 21)

def bolp_127_bb_pctb_z_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_127_bb_pctb_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rolling_mean(base, 63)

def bolp_128_bb_pctb_z_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_128_bb_pctb_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _zscore_rolling(base, 63)

def bolp_129_bb_pctb_z_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_129_bb_pctb_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rank_pct(base, 63)

def bolp_130_bb_pctb_z_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_130_bb_pctb_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rolling_mean(base, 126)

def bolp_131_bb_pctb_z_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_131_bb_pctb_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _zscore_rolling(base, 126)

def bolp_132_bb_pctb_z_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_132_bb_pctb_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rank_pct(base, 126)

def bolp_133_bb_pctb_z_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_133_bb_pctb_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rolling_mean(base, 252)

def bolp_134_bb_pctb_z_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_134_bb_pctb_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _zscore_rolling(base, 252)

def bolp_135_bb_pctb_z_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_135_bb_pctb_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20)), 63)
    return _rank_pct(base, 252)

def bolp_136_bb_sqz_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_136_bb_sqz_lvl_5d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rolling_mean(base, 5)

def bolp_137_bb_sqz_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_137_bb_sqz_zscore_5d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _zscore_rolling(base, 5)

def bolp_138_bb_sqz_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_138_bb_sqz_rank_5d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rank_pct(base, 5)

def bolp_139_bb_sqz_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_139_bb_sqz_lvl_21d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rolling_mean(base, 21)

def bolp_140_bb_sqz_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_140_bb_sqz_zscore_21d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _zscore_rolling(base, 21)

def bolp_141_bb_sqz_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_141_bb_sqz_rank_21d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rank_pct(base, 21)

def bolp_142_bb_sqz_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_142_bb_sqz_lvl_63d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rolling_mean(base, 63)

def bolp_143_bb_sqz_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_143_bb_sqz_zscore_63d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _zscore_rolling(base, 63)

def bolp_144_bb_sqz_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_144_bb_sqz_rank_63d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rank_pct(base, 63)

def bolp_145_bb_sqz_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_145_bb_sqz_lvl_126d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rolling_mean(base, 126)

def bolp_146_bb_sqz_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_146_bb_sqz_zscore_126d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _zscore_rolling(base, 126)

def bolp_147_bb_sqz_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_147_bb_sqz_rank_126d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rank_pct(base, 126)

def bolp_148_bb_sqz_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_148_bb_sqz_lvl_252d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rolling_mean(base, 252)

def bolp_149_bb_sqz_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_149_bb_sqz_zscore_252d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _zscore_rolling(base, 252)

def bolp_150_bb_sqz_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_150_bb_sqz_rank_252d"""
    base = _safe_div(_rolling_std(close, 20), _rolling_std(close, 100))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V77_REGISTRY_2 = {
    "bolp_076_bb_dist_l_lvl_5d": {"inputs": ["close"], "func": bolp_076_bb_dist_l_lvl_5d},
    "bolp_077_bb_dist_l_zscore_5d": {"inputs": ["close"], "func": bolp_077_bb_dist_l_zscore_5d},
    "bolp_078_bb_dist_l_rank_5d": {"inputs": ["close"], "func": bolp_078_bb_dist_l_rank_5d},
    "bolp_079_bb_dist_l_lvl_21d": {"inputs": ["close"], "func": bolp_079_bb_dist_l_lvl_21d},
    "bolp_080_bb_dist_l_zscore_21d": {"inputs": ["close"], "func": bolp_080_bb_dist_l_zscore_21d},
    "bolp_081_bb_dist_l_rank_21d": {"inputs": ["close"], "func": bolp_081_bb_dist_l_rank_21d},
    "bolp_082_bb_dist_l_lvl_63d": {"inputs": ["close"], "func": bolp_082_bb_dist_l_lvl_63d},
    "bolp_083_bb_dist_l_zscore_63d": {"inputs": ["close"], "func": bolp_083_bb_dist_l_zscore_63d},
    "bolp_084_bb_dist_l_rank_63d": {"inputs": ["close"], "func": bolp_084_bb_dist_l_rank_63d},
    "bolp_085_bb_dist_l_lvl_126d": {"inputs": ["close"], "func": bolp_085_bb_dist_l_lvl_126d},
    "bolp_086_bb_dist_l_zscore_126d": {"inputs": ["close"], "func": bolp_086_bb_dist_l_zscore_126d},
    "bolp_087_bb_dist_l_rank_126d": {"inputs": ["close"], "func": bolp_087_bb_dist_l_rank_126d},
    "bolp_088_bb_dist_l_lvl_252d": {"inputs": ["close"], "func": bolp_088_bb_dist_l_lvl_252d},
    "bolp_089_bb_dist_l_zscore_252d": {"inputs": ["close"], "func": bolp_089_bb_dist_l_zscore_252d},
    "bolp_090_bb_dist_l_rank_252d": {"inputs": ["close"], "func": bolp_090_bb_dist_l_rank_252d},
    "bolp_091_bb_sma_dist_lvl_5d": {"inputs": ["close"], "func": bolp_091_bb_sma_dist_lvl_5d},
    "bolp_092_bb_sma_dist_zscore_5d": {"inputs": ["close"], "func": bolp_092_bb_sma_dist_zscore_5d},
    "bolp_093_bb_sma_dist_rank_5d": {"inputs": ["close"], "func": bolp_093_bb_sma_dist_rank_5d},
    "bolp_094_bb_sma_dist_lvl_21d": {"inputs": ["close"], "func": bolp_094_bb_sma_dist_lvl_21d},
    "bolp_095_bb_sma_dist_zscore_21d": {"inputs": ["close"], "func": bolp_095_bb_sma_dist_zscore_21d},
    "bolp_096_bb_sma_dist_rank_21d": {"inputs": ["close"], "func": bolp_096_bb_sma_dist_rank_21d},
    "bolp_097_bb_sma_dist_lvl_63d": {"inputs": ["close"], "func": bolp_097_bb_sma_dist_lvl_63d},
    "bolp_098_bb_sma_dist_zscore_63d": {"inputs": ["close"], "func": bolp_098_bb_sma_dist_zscore_63d},
    "bolp_099_bb_sma_dist_rank_63d": {"inputs": ["close"], "func": bolp_099_bb_sma_dist_rank_63d},
    "bolp_100_bb_sma_dist_lvl_126d": {"inputs": ["close"], "func": bolp_100_bb_sma_dist_lvl_126d},
    "bolp_101_bb_sma_dist_zscore_126d": {"inputs": ["close"], "func": bolp_101_bb_sma_dist_zscore_126d},
    "bolp_102_bb_sma_dist_rank_126d": {"inputs": ["close"], "func": bolp_102_bb_sma_dist_rank_126d},
    "bolp_103_bb_sma_dist_lvl_252d": {"inputs": ["close"], "func": bolp_103_bb_sma_dist_lvl_252d},
    "bolp_104_bb_sma_dist_zscore_252d": {"inputs": ["close"], "func": bolp_104_bb_sma_dist_zscore_252d},
    "bolp_105_bb_sma_dist_rank_252d": {"inputs": ["close"], "func": bolp_105_bb_sma_dist_rank_252d},
    "bolp_106_bb_width_z_lvl_5d": {"inputs": ["close"], "func": bolp_106_bb_width_z_lvl_5d},
    "bolp_107_bb_width_z_zscore_5d": {"inputs": ["close"], "func": bolp_107_bb_width_z_zscore_5d},
    "bolp_108_bb_width_z_rank_5d": {"inputs": ["close"], "func": bolp_108_bb_width_z_rank_5d},
    "bolp_109_bb_width_z_lvl_21d": {"inputs": ["close"], "func": bolp_109_bb_width_z_lvl_21d},
    "bolp_110_bb_width_z_zscore_21d": {"inputs": ["close"], "func": bolp_110_bb_width_z_zscore_21d},
    "bolp_111_bb_width_z_rank_21d": {"inputs": ["close"], "func": bolp_111_bb_width_z_rank_21d},
    "bolp_112_bb_width_z_lvl_63d": {"inputs": ["close"], "func": bolp_112_bb_width_z_lvl_63d},
    "bolp_113_bb_width_z_zscore_63d": {"inputs": ["close"], "func": bolp_113_bb_width_z_zscore_63d},
    "bolp_114_bb_width_z_rank_63d": {"inputs": ["close"], "func": bolp_114_bb_width_z_rank_63d},
    "bolp_115_bb_width_z_lvl_126d": {"inputs": ["close"], "func": bolp_115_bb_width_z_lvl_126d},
    "bolp_116_bb_width_z_zscore_126d": {"inputs": ["close"], "func": bolp_116_bb_width_z_zscore_126d},
    "bolp_117_bb_width_z_rank_126d": {"inputs": ["close"], "func": bolp_117_bb_width_z_rank_126d},
    "bolp_118_bb_width_z_lvl_252d": {"inputs": ["close"], "func": bolp_118_bb_width_z_lvl_252d},
    "bolp_119_bb_width_z_zscore_252d": {"inputs": ["close"], "func": bolp_119_bb_width_z_zscore_252d},
    "bolp_120_bb_width_z_rank_252d": {"inputs": ["close"], "func": bolp_120_bb_width_z_rank_252d},
    "bolp_121_bb_pctb_z_lvl_5d": {"inputs": ["close"], "func": bolp_121_bb_pctb_z_lvl_5d},
    "bolp_122_bb_pctb_z_zscore_5d": {"inputs": ["close"], "func": bolp_122_bb_pctb_z_zscore_5d},
    "bolp_123_bb_pctb_z_rank_5d": {"inputs": ["close"], "func": bolp_123_bb_pctb_z_rank_5d},
    "bolp_124_bb_pctb_z_lvl_21d": {"inputs": ["close"], "func": bolp_124_bb_pctb_z_lvl_21d},
    "bolp_125_bb_pctb_z_zscore_21d": {"inputs": ["close"], "func": bolp_125_bb_pctb_z_zscore_21d},
    "bolp_126_bb_pctb_z_rank_21d": {"inputs": ["close"], "func": bolp_126_bb_pctb_z_rank_21d},
    "bolp_127_bb_pctb_z_lvl_63d": {"inputs": ["close"], "func": bolp_127_bb_pctb_z_lvl_63d},
    "bolp_128_bb_pctb_z_zscore_63d": {"inputs": ["close"], "func": bolp_128_bb_pctb_z_zscore_63d},
    "bolp_129_bb_pctb_z_rank_63d": {"inputs": ["close"], "func": bolp_129_bb_pctb_z_rank_63d},
    "bolp_130_bb_pctb_z_lvl_126d": {"inputs": ["close"], "func": bolp_130_bb_pctb_z_lvl_126d},
    "bolp_131_bb_pctb_z_zscore_126d": {"inputs": ["close"], "func": bolp_131_bb_pctb_z_zscore_126d},
    "bolp_132_bb_pctb_z_rank_126d": {"inputs": ["close"], "func": bolp_132_bb_pctb_z_rank_126d},
    "bolp_133_bb_pctb_z_lvl_252d": {"inputs": ["close"], "func": bolp_133_bb_pctb_z_lvl_252d},
    "bolp_134_bb_pctb_z_zscore_252d": {"inputs": ["close"], "func": bolp_134_bb_pctb_z_zscore_252d},
    "bolp_135_bb_pctb_z_rank_252d": {"inputs": ["close"], "func": bolp_135_bb_pctb_z_rank_252d},
    "bolp_136_bb_sqz_lvl_5d": {"inputs": ["close"], "func": bolp_136_bb_sqz_lvl_5d},
    "bolp_137_bb_sqz_zscore_5d": {"inputs": ["close"], "func": bolp_137_bb_sqz_zscore_5d},
    "bolp_138_bb_sqz_rank_5d": {"inputs": ["close"], "func": bolp_138_bb_sqz_rank_5d},
    "bolp_139_bb_sqz_lvl_21d": {"inputs": ["close"], "func": bolp_139_bb_sqz_lvl_21d},
    "bolp_140_bb_sqz_zscore_21d": {"inputs": ["close"], "func": bolp_140_bb_sqz_zscore_21d},
    "bolp_141_bb_sqz_rank_21d": {"inputs": ["close"], "func": bolp_141_bb_sqz_rank_21d},
    "bolp_142_bb_sqz_lvl_63d": {"inputs": ["close"], "func": bolp_142_bb_sqz_lvl_63d},
    "bolp_143_bb_sqz_zscore_63d": {"inputs": ["close"], "func": bolp_143_bb_sqz_zscore_63d},
    "bolp_144_bb_sqz_rank_63d": {"inputs": ["close"], "func": bolp_144_bb_sqz_rank_63d},
    "bolp_145_bb_sqz_lvl_126d": {"inputs": ["close"], "func": bolp_145_bb_sqz_lvl_126d},
    "bolp_146_bb_sqz_zscore_126d": {"inputs": ["close"], "func": bolp_146_bb_sqz_zscore_126d},
    "bolp_147_bb_sqz_rank_126d": {"inputs": ["close"], "func": bolp_147_bb_sqz_rank_126d},
    "bolp_148_bb_sqz_lvl_252d": {"inputs": ["close"], "func": bolp_148_bb_sqz_lvl_252d},
    "bolp_149_bb_sqz_zscore_252d": {"inputs": ["close"], "func": bolp_149_bb_sqz_zscore_252d},
    "bolp_150_bb_sqz_rank_252d": {"inputs": ["close"], "func": bolp_150_bb_sqz_rank_252d},
}
