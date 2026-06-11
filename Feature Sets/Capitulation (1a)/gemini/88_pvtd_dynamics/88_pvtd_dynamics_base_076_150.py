"""
88_pvtd_dynamics — Base Features 076-150
Domain: pvtd_dynamics
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

def pvtd_076_pvt_level_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_076_pvt_level_lvl_5d"""
    base = volume * close.pct_change()
    return _rolling_mean(base, 5)

def pvtd_077_pvt_level_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_077_pvt_level_zscore_5d"""
    base = volume * close.pct_change()
    return _zscore_rolling(base, 5)

def pvtd_078_pvt_level_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_078_pvt_level_rank_5d"""
    base = volume * close.pct_change()
    return _rank_pct(base, 5)

def pvtd_079_pvt_level_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_079_pvt_level_lvl_21d"""
    base = volume * close.pct_change()
    return _rolling_mean(base, 21)

def pvtd_080_pvt_level_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_080_pvt_level_zscore_21d"""
    base = volume * close.pct_change()
    return _zscore_rolling(base, 21)

def pvtd_081_pvt_level_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_081_pvt_level_rank_21d"""
    base = volume * close.pct_change()
    return _rank_pct(base, 21)

def pvtd_082_pvt_level_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_082_pvt_level_lvl_63d"""
    base = volume * close.pct_change()
    return _rolling_mean(base, 63)

def pvtd_083_pvt_level_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_083_pvt_level_zscore_63d"""
    base = volume * close.pct_change()
    return _zscore_rolling(base, 63)

def pvtd_084_pvt_level_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_084_pvt_level_rank_63d"""
    base = volume * close.pct_change()
    return _rank_pct(base, 63)

def pvtd_085_pvt_level_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_085_pvt_level_lvl_126d"""
    base = volume * close.pct_change()
    return _rolling_mean(base, 126)

def pvtd_086_pvt_level_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_086_pvt_level_zscore_126d"""
    base = volume * close.pct_change()
    return _zscore_rolling(base, 126)

def pvtd_087_pvt_level_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_087_pvt_level_rank_126d"""
    base = volume * close.pct_change()
    return _rank_pct(base, 126)

def pvtd_088_pvt_level_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_088_pvt_level_lvl_252d"""
    base = volume * close.pct_change()
    return _rolling_mean(base, 252)

def pvtd_089_pvt_level_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_089_pvt_level_zscore_252d"""
    base = volume * close.pct_change()
    return _zscore_rolling(base, 252)

def pvtd_090_pvt_level_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_090_pvt_level_rank_252d"""
    base = volume * close.pct_change()
    return _rank_pct(base, 252)

def pvtd_091_pvt_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_091_pvt_dist_lvl_5d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rolling_mean(base, 5)

def pvtd_092_pvt_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_092_pvt_dist_zscore_5d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _zscore_rolling(base, 5)

def pvtd_093_pvt_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_093_pvt_dist_rank_5d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rank_pct(base, 5)

def pvtd_094_pvt_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_094_pvt_dist_lvl_21d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rolling_mean(base, 21)

def pvtd_095_pvt_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_095_pvt_dist_zscore_21d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _zscore_rolling(base, 21)

def pvtd_096_pvt_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_096_pvt_dist_rank_21d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rank_pct(base, 21)

def pvtd_097_pvt_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_097_pvt_dist_lvl_63d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rolling_mean(base, 63)

def pvtd_098_pvt_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_098_pvt_dist_zscore_63d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _zscore_rolling(base, 63)

def pvtd_099_pvt_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_099_pvt_dist_rank_63d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rank_pct(base, 63)

def pvtd_100_pvt_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_100_pvt_dist_lvl_126d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rolling_mean(base, 126)

def pvtd_101_pvt_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_101_pvt_dist_zscore_126d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _zscore_rolling(base, 126)

def pvtd_102_pvt_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_102_pvt_dist_rank_126d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rank_pct(base, 126)

def pvtd_103_pvt_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_103_pvt_dist_lvl_252d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rolling_mean(base, 252)

def pvtd_104_pvt_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_104_pvt_dist_zscore_252d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _zscore_rolling(base, 252)

def pvtd_105_pvt_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_105_pvt_dist_rank_252d"""
    base = (volume * close.pct_change()) - _rolling_mean(volume * close.pct_change(), 21)
    return _rank_pct(base, 252)

def pvtd_106_pvt_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_106_pvt_abs_lvl_5d"""
    base = (volume * close.pct_change()).abs()
    return _rolling_mean(base, 5)

def pvtd_107_pvt_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_107_pvt_abs_zscore_5d"""
    base = (volume * close.pct_change()).abs()
    return _zscore_rolling(base, 5)

def pvtd_108_pvt_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_108_pvt_abs_rank_5d"""
    base = (volume * close.pct_change()).abs()
    return _rank_pct(base, 5)

def pvtd_109_pvt_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_109_pvt_abs_lvl_21d"""
    base = (volume * close.pct_change()).abs()
    return _rolling_mean(base, 21)

def pvtd_110_pvt_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_110_pvt_abs_zscore_21d"""
    base = (volume * close.pct_change()).abs()
    return _zscore_rolling(base, 21)

def pvtd_111_pvt_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_111_pvt_abs_rank_21d"""
    base = (volume * close.pct_change()).abs()
    return _rank_pct(base, 21)

def pvtd_112_pvt_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_112_pvt_abs_lvl_63d"""
    base = (volume * close.pct_change()).abs()
    return _rolling_mean(base, 63)

def pvtd_113_pvt_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_113_pvt_abs_zscore_63d"""
    base = (volume * close.pct_change()).abs()
    return _zscore_rolling(base, 63)

def pvtd_114_pvt_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_114_pvt_abs_rank_63d"""
    base = (volume * close.pct_change()).abs()
    return _rank_pct(base, 63)

def pvtd_115_pvt_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_115_pvt_abs_lvl_126d"""
    base = (volume * close.pct_change()).abs()
    return _rolling_mean(base, 126)

def pvtd_116_pvt_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_116_pvt_abs_zscore_126d"""
    base = (volume * close.pct_change()).abs()
    return _zscore_rolling(base, 126)

def pvtd_117_pvt_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_117_pvt_abs_rank_126d"""
    base = (volume * close.pct_change()).abs()
    return _rank_pct(base, 126)

def pvtd_118_pvt_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_118_pvt_abs_lvl_252d"""
    base = (volume * close.pct_change()).abs()
    return _rolling_mean(base, 252)

def pvtd_119_pvt_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_119_pvt_abs_zscore_252d"""
    base = (volume * close.pct_change()).abs()
    return _zscore_rolling(base, 252)

def pvtd_120_pvt_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_120_pvt_abs_rank_252d"""
    base = (volume * close.pct_change()).abs()
    return _rank_pct(base, 252)

def pvtd_121_pvt_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_121_pvt_log_lvl_5d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rolling_mean(base, 5)

def pvtd_122_pvt_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_122_pvt_log_zscore_5d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def pvtd_123_pvt_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_123_pvt_log_rank_5d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rank_pct(base, 5)

def pvtd_124_pvt_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_124_pvt_log_lvl_21d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rolling_mean(base, 21)

def pvtd_125_pvt_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_125_pvt_log_zscore_21d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def pvtd_126_pvt_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_126_pvt_log_rank_21d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rank_pct(base, 21)

def pvtd_127_pvt_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_127_pvt_log_lvl_63d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rolling_mean(base, 63)

def pvtd_128_pvt_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_128_pvt_log_zscore_63d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def pvtd_129_pvt_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_129_pvt_log_rank_63d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rank_pct(base, 63)

def pvtd_130_pvt_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_130_pvt_log_lvl_126d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rolling_mean(base, 126)

def pvtd_131_pvt_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_131_pvt_log_zscore_126d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def pvtd_132_pvt_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_132_pvt_log_rank_126d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rank_pct(base, 126)

def pvtd_133_pvt_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_133_pvt_log_lvl_252d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rolling_mean(base, 252)

def pvtd_134_pvt_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_134_pvt_log_zscore_252d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def pvtd_135_pvt_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_135_pvt_log_rank_252d"""
    base = np.log((volume * close.pct_change()).abs().clip(lower=_EPS))
    return _rank_pct(base, 252)

def pvtd_136_pvt_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_136_pvt_vol_lvl_5d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rolling_mean(base, 5)

def pvtd_137_pvt_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_137_pvt_vol_zscore_5d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _zscore_rolling(base, 5)

def pvtd_138_pvt_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_138_pvt_vol_rank_5d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rank_pct(base, 5)

def pvtd_139_pvt_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_139_pvt_vol_lvl_21d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rolling_mean(base, 21)

def pvtd_140_pvt_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_140_pvt_vol_zscore_21d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _zscore_rolling(base, 21)

def pvtd_141_pvt_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_141_pvt_vol_rank_21d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rank_pct(base, 21)

def pvtd_142_pvt_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_142_pvt_vol_lvl_63d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rolling_mean(base, 63)

def pvtd_143_pvt_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_143_pvt_vol_zscore_63d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _zscore_rolling(base, 63)

def pvtd_144_pvt_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_144_pvt_vol_rank_63d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rank_pct(base, 63)

def pvtd_145_pvt_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_145_pvt_vol_lvl_126d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rolling_mean(base, 126)

def pvtd_146_pvt_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_146_pvt_vol_zscore_126d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _zscore_rolling(base, 126)

def pvtd_147_pvt_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_147_pvt_vol_rank_126d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rank_pct(base, 126)

def pvtd_148_pvt_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_148_pvt_vol_lvl_252d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rolling_mean(base, 252)

def pvtd_149_pvt_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_149_pvt_vol_zscore_252d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _zscore_rolling(base, 252)

def pvtd_150_pvt_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_150_pvt_vol_rank_252d"""
    base = _safe_div(volume * close.pct_change(), _rolling_std(close, 21))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V88_REGISTRY_2 = {
    "pvtd_076_pvt_level_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_076_pvt_level_lvl_5d},
    "pvtd_077_pvt_level_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_077_pvt_level_zscore_5d},
    "pvtd_078_pvt_level_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_078_pvt_level_rank_5d},
    "pvtd_079_pvt_level_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_079_pvt_level_lvl_21d},
    "pvtd_080_pvt_level_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_080_pvt_level_zscore_21d},
    "pvtd_081_pvt_level_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_081_pvt_level_rank_21d},
    "pvtd_082_pvt_level_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_082_pvt_level_lvl_63d},
    "pvtd_083_pvt_level_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_083_pvt_level_zscore_63d},
    "pvtd_084_pvt_level_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_084_pvt_level_rank_63d},
    "pvtd_085_pvt_level_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_085_pvt_level_lvl_126d},
    "pvtd_086_pvt_level_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_086_pvt_level_zscore_126d},
    "pvtd_087_pvt_level_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_087_pvt_level_rank_126d},
    "pvtd_088_pvt_level_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_088_pvt_level_lvl_252d},
    "pvtd_089_pvt_level_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_089_pvt_level_zscore_252d},
    "pvtd_090_pvt_level_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_090_pvt_level_rank_252d},
    "pvtd_091_pvt_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_091_pvt_dist_lvl_5d},
    "pvtd_092_pvt_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_092_pvt_dist_zscore_5d},
    "pvtd_093_pvt_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_093_pvt_dist_rank_5d},
    "pvtd_094_pvt_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_094_pvt_dist_lvl_21d},
    "pvtd_095_pvt_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_095_pvt_dist_zscore_21d},
    "pvtd_096_pvt_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_096_pvt_dist_rank_21d},
    "pvtd_097_pvt_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_097_pvt_dist_lvl_63d},
    "pvtd_098_pvt_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_098_pvt_dist_zscore_63d},
    "pvtd_099_pvt_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_099_pvt_dist_rank_63d},
    "pvtd_100_pvt_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_100_pvt_dist_lvl_126d},
    "pvtd_101_pvt_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_101_pvt_dist_zscore_126d},
    "pvtd_102_pvt_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_102_pvt_dist_rank_126d},
    "pvtd_103_pvt_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_103_pvt_dist_lvl_252d},
    "pvtd_104_pvt_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_104_pvt_dist_zscore_252d},
    "pvtd_105_pvt_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_105_pvt_dist_rank_252d},
    "pvtd_106_pvt_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_106_pvt_abs_lvl_5d},
    "pvtd_107_pvt_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_107_pvt_abs_zscore_5d},
    "pvtd_108_pvt_abs_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_108_pvt_abs_rank_5d},
    "pvtd_109_pvt_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_109_pvt_abs_lvl_21d},
    "pvtd_110_pvt_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_110_pvt_abs_zscore_21d},
    "pvtd_111_pvt_abs_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_111_pvt_abs_rank_21d},
    "pvtd_112_pvt_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_112_pvt_abs_lvl_63d},
    "pvtd_113_pvt_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_113_pvt_abs_zscore_63d},
    "pvtd_114_pvt_abs_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_114_pvt_abs_rank_63d},
    "pvtd_115_pvt_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_115_pvt_abs_lvl_126d},
    "pvtd_116_pvt_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_116_pvt_abs_zscore_126d},
    "pvtd_117_pvt_abs_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_117_pvt_abs_rank_126d},
    "pvtd_118_pvt_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_118_pvt_abs_lvl_252d},
    "pvtd_119_pvt_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_119_pvt_abs_zscore_252d},
    "pvtd_120_pvt_abs_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_120_pvt_abs_rank_252d},
    "pvtd_121_pvt_log_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_121_pvt_log_lvl_5d},
    "pvtd_122_pvt_log_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_122_pvt_log_zscore_5d},
    "pvtd_123_pvt_log_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_123_pvt_log_rank_5d},
    "pvtd_124_pvt_log_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_124_pvt_log_lvl_21d},
    "pvtd_125_pvt_log_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_125_pvt_log_zscore_21d},
    "pvtd_126_pvt_log_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_126_pvt_log_rank_21d},
    "pvtd_127_pvt_log_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_127_pvt_log_lvl_63d},
    "pvtd_128_pvt_log_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_128_pvt_log_zscore_63d},
    "pvtd_129_pvt_log_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_129_pvt_log_rank_63d},
    "pvtd_130_pvt_log_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_130_pvt_log_lvl_126d},
    "pvtd_131_pvt_log_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_131_pvt_log_zscore_126d},
    "pvtd_132_pvt_log_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_132_pvt_log_rank_126d},
    "pvtd_133_pvt_log_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_133_pvt_log_lvl_252d},
    "pvtd_134_pvt_log_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_134_pvt_log_zscore_252d},
    "pvtd_135_pvt_log_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_135_pvt_log_rank_252d},
    "pvtd_136_pvt_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_136_pvt_vol_lvl_5d},
    "pvtd_137_pvt_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_137_pvt_vol_zscore_5d},
    "pvtd_138_pvt_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_138_pvt_vol_rank_5d},
    "pvtd_139_pvt_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_139_pvt_vol_lvl_21d},
    "pvtd_140_pvt_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_140_pvt_vol_zscore_21d},
    "pvtd_141_pvt_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_141_pvt_vol_rank_21d},
    "pvtd_142_pvt_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_142_pvt_vol_lvl_63d},
    "pvtd_143_pvt_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_143_pvt_vol_zscore_63d},
    "pvtd_144_pvt_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_144_pvt_vol_rank_63d},
    "pvtd_145_pvt_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_145_pvt_vol_lvl_126d},
    "pvtd_146_pvt_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_146_pvt_vol_zscore_126d},
    "pvtd_147_pvt_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_147_pvt_vol_rank_126d},
    "pvtd_148_pvt_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_148_pvt_vol_lvl_252d},
    "pvtd_149_pvt_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_149_pvt_vol_zscore_252d},
    "pvtd_150_pvt_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_150_pvt_vol_rank_252d},
}
