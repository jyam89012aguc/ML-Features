"""
99_vlrs_dynamics — Base Features 076-150
Domain: vlrs_dynamics
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

def vlrs_076_vol_rs_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_076_vol_rs_abs_lvl_5d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rolling_mean(base, 5)

def vlrs_077_vol_rs_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_077_vol_rs_abs_zscore_5d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _zscore_rolling(base, 5)

def vlrs_078_vol_rs_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_078_vol_rs_abs_rank_5d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rank_pct(base, 5)

def vlrs_079_vol_rs_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_079_vol_rs_abs_lvl_21d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rolling_mean(base, 21)

def vlrs_080_vol_rs_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_080_vol_rs_abs_zscore_21d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _zscore_rolling(base, 21)

def vlrs_081_vol_rs_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_081_vol_rs_abs_rank_21d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rank_pct(base, 21)

def vlrs_082_vol_rs_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_082_vol_rs_abs_lvl_63d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rolling_mean(base, 63)

def vlrs_083_vol_rs_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_083_vol_rs_abs_zscore_63d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _zscore_rolling(base, 63)

def vlrs_084_vol_rs_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_084_vol_rs_abs_rank_63d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rank_pct(base, 63)

def vlrs_085_vol_rs_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_085_vol_rs_abs_lvl_126d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rolling_mean(base, 126)

def vlrs_086_vol_rs_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_086_vol_rs_abs_zscore_126d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _zscore_rolling(base, 126)

def vlrs_087_vol_rs_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_087_vol_rs_abs_rank_126d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rank_pct(base, 126)

def vlrs_088_vol_rs_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_088_vol_rs_abs_lvl_252d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rolling_mean(base, 252)

def vlrs_089_vol_rs_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_089_vol_rs_abs_zscore_252d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _zscore_rolling(base, 252)

def vlrs_090_vol_rs_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_090_vol_rs_abs_rank_252d"""
    base = _safe_div(volume, mkt_volume).abs()
    return _rank_pct(base, 252)

def vlrs_091_vol_rs_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_091_vol_rs_sig_lvl_5d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rolling_mean(base, 5)

def vlrs_092_vol_rs_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_092_vol_rs_sig_zscore_5d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _zscore_rolling(base, 5)

def vlrs_093_vol_rs_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_093_vol_rs_sig_rank_5d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rank_pct(base, 5)

def vlrs_094_vol_rs_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_094_vol_rs_sig_lvl_21d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rolling_mean(base, 21)

def vlrs_095_vol_rs_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_095_vol_rs_sig_zscore_21d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _zscore_rolling(base, 21)

def vlrs_096_vol_rs_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_096_vol_rs_sig_rank_21d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rank_pct(base, 21)

def vlrs_097_vol_rs_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_097_vol_rs_sig_lvl_63d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rolling_mean(base, 63)

def vlrs_098_vol_rs_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_098_vol_rs_sig_zscore_63d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _zscore_rolling(base, 63)

def vlrs_099_vol_rs_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_099_vol_rs_sig_rank_63d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rank_pct(base, 63)

def vlrs_100_vol_rs_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_100_vol_rs_sig_lvl_126d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rolling_mean(base, 126)

def vlrs_101_vol_rs_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_101_vol_rs_sig_zscore_126d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _zscore_rolling(base, 126)

def vlrs_102_vol_rs_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_102_vol_rs_sig_rank_126d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rank_pct(base, 126)

def vlrs_103_vol_rs_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_103_vol_rs_sig_lvl_252d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rolling_mean(base, 252)

def vlrs_104_vol_rs_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_104_vol_rs_sig_zscore_252d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _zscore_rolling(base, 252)

def vlrs_105_vol_rs_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_105_vol_rs_sig_rank_252d"""
    base = _rolling_mean(_safe_div(volume, mkt_volume), 5)
    return _rank_pct(base, 252)

def vlrs_106_vol_rs_accel_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_106_vol_rs_accel_lvl_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rolling_mean(base, 5)

def vlrs_107_vol_rs_accel_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_107_vol_rs_accel_zscore_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _zscore_rolling(base, 5)

def vlrs_108_vol_rs_accel_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_108_vol_rs_accel_rank_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rank_pct(base, 5)

def vlrs_109_vol_rs_accel_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_109_vol_rs_accel_lvl_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rolling_mean(base, 21)

def vlrs_110_vol_rs_accel_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_110_vol_rs_accel_zscore_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _zscore_rolling(base, 21)

def vlrs_111_vol_rs_accel_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_111_vol_rs_accel_rank_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rank_pct(base, 21)

def vlrs_112_vol_rs_accel_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_112_vol_rs_accel_lvl_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rolling_mean(base, 63)

def vlrs_113_vol_rs_accel_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_113_vol_rs_accel_zscore_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _zscore_rolling(base, 63)

def vlrs_114_vol_rs_accel_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_114_vol_rs_accel_rank_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rank_pct(base, 63)

def vlrs_115_vol_rs_accel_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_115_vol_rs_accel_lvl_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rolling_mean(base, 126)

def vlrs_116_vol_rs_accel_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_116_vol_rs_accel_zscore_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _zscore_rolling(base, 126)

def vlrs_117_vol_rs_accel_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_117_vol_rs_accel_rank_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rank_pct(base, 126)

def vlrs_118_vol_rs_accel_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_118_vol_rs_accel_lvl_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rolling_mean(base, 252)

def vlrs_119_vol_rs_accel_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_119_vol_rs_accel_zscore_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _zscore_rolling(base, 252)

def vlrs_120_vol_rs_accel_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_120_vol_rs_accel_rank_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21).diff()
    return _rank_pct(base, 252)

def vlrs_121_vol_rs_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_121_vol_rs_log_lvl_5d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rolling_mean(base, 5)

def vlrs_122_vol_rs_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_122_vol_rs_log_zscore_5d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def vlrs_123_vol_rs_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_123_vol_rs_log_rank_5d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rank_pct(base, 5)

def vlrs_124_vol_rs_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_124_vol_rs_log_lvl_21d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rolling_mean(base, 21)

def vlrs_125_vol_rs_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_125_vol_rs_log_zscore_21d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def vlrs_126_vol_rs_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_126_vol_rs_log_rank_21d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rank_pct(base, 21)

def vlrs_127_vol_rs_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_127_vol_rs_log_lvl_63d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rolling_mean(base, 63)

def vlrs_128_vol_rs_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_128_vol_rs_log_zscore_63d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def vlrs_129_vol_rs_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_129_vol_rs_log_rank_63d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rank_pct(base, 63)

def vlrs_130_vol_rs_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_130_vol_rs_log_lvl_126d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rolling_mean(base, 126)

def vlrs_131_vol_rs_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_131_vol_rs_log_zscore_126d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def vlrs_132_vol_rs_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_132_vol_rs_log_rank_126d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rank_pct(base, 126)

def vlrs_133_vol_rs_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_133_vol_rs_log_lvl_252d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rolling_mean(base, 252)

def vlrs_134_vol_rs_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_134_vol_rs_log_zscore_252d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def vlrs_135_vol_rs_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_135_vol_rs_log_rank_252d"""
    base = np.log(_safe_div(volume, mkt_volume).clip(lower=_EPS))
    return _rank_pct(base, 252)

def vlrs_136_vol_rs_std_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_136_vol_rs_std_lvl_5d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rolling_mean(base, 5)

def vlrs_137_vol_rs_std_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_137_vol_rs_std_zscore_5d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _zscore_rolling(base, 5)

def vlrs_138_vol_rs_std_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_138_vol_rs_std_rank_5d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rank_pct(base, 5)

def vlrs_139_vol_rs_std_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_139_vol_rs_std_lvl_21d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rolling_mean(base, 21)

def vlrs_140_vol_rs_std_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_140_vol_rs_std_zscore_21d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _zscore_rolling(base, 21)

def vlrs_141_vol_rs_std_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_141_vol_rs_std_rank_21d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rank_pct(base, 21)

def vlrs_142_vol_rs_std_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_142_vol_rs_std_lvl_63d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rolling_mean(base, 63)

def vlrs_143_vol_rs_std_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_143_vol_rs_std_zscore_63d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _zscore_rolling(base, 63)

def vlrs_144_vol_rs_std_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_144_vol_rs_std_rank_63d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rank_pct(base, 63)

def vlrs_145_vol_rs_std_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_145_vol_rs_std_lvl_126d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rolling_mean(base, 126)

def vlrs_146_vol_rs_std_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_146_vol_rs_std_zscore_126d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _zscore_rolling(base, 126)

def vlrs_147_vol_rs_std_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_147_vol_rs_std_rank_126d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rank_pct(base, 126)

def vlrs_148_vol_rs_std_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_148_vol_rs_std_lvl_252d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rolling_mean(base, 252)

def vlrs_149_vol_rs_std_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_149_vol_rs_std_zscore_252d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _zscore_rolling(base, 252)

def vlrs_150_vol_rs_std_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_150_vol_rs_std_rank_252d"""
    base = _rolling_std(_safe_div(volume, mkt_volume), 21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V99_REGISTRY_2 = {
    "vlrs_076_vol_rs_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_076_vol_rs_abs_lvl_5d},
    "vlrs_077_vol_rs_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_077_vol_rs_abs_zscore_5d},
    "vlrs_078_vol_rs_abs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_078_vol_rs_abs_rank_5d},
    "vlrs_079_vol_rs_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_079_vol_rs_abs_lvl_21d},
    "vlrs_080_vol_rs_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_080_vol_rs_abs_zscore_21d},
    "vlrs_081_vol_rs_abs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_081_vol_rs_abs_rank_21d},
    "vlrs_082_vol_rs_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_082_vol_rs_abs_lvl_63d},
    "vlrs_083_vol_rs_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_083_vol_rs_abs_zscore_63d},
    "vlrs_084_vol_rs_abs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_084_vol_rs_abs_rank_63d},
    "vlrs_085_vol_rs_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_085_vol_rs_abs_lvl_126d},
    "vlrs_086_vol_rs_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_086_vol_rs_abs_zscore_126d},
    "vlrs_087_vol_rs_abs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_087_vol_rs_abs_rank_126d},
    "vlrs_088_vol_rs_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_088_vol_rs_abs_lvl_252d},
    "vlrs_089_vol_rs_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_089_vol_rs_abs_zscore_252d},
    "vlrs_090_vol_rs_abs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_090_vol_rs_abs_rank_252d},
    "vlrs_091_vol_rs_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_091_vol_rs_sig_lvl_5d},
    "vlrs_092_vol_rs_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_092_vol_rs_sig_zscore_5d},
    "vlrs_093_vol_rs_sig_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_093_vol_rs_sig_rank_5d},
    "vlrs_094_vol_rs_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_094_vol_rs_sig_lvl_21d},
    "vlrs_095_vol_rs_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_095_vol_rs_sig_zscore_21d},
    "vlrs_096_vol_rs_sig_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_096_vol_rs_sig_rank_21d},
    "vlrs_097_vol_rs_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_097_vol_rs_sig_lvl_63d},
    "vlrs_098_vol_rs_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_098_vol_rs_sig_zscore_63d},
    "vlrs_099_vol_rs_sig_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_099_vol_rs_sig_rank_63d},
    "vlrs_100_vol_rs_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_100_vol_rs_sig_lvl_126d},
    "vlrs_101_vol_rs_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_101_vol_rs_sig_zscore_126d},
    "vlrs_102_vol_rs_sig_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_102_vol_rs_sig_rank_126d},
    "vlrs_103_vol_rs_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_103_vol_rs_sig_lvl_252d},
    "vlrs_104_vol_rs_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_104_vol_rs_sig_zscore_252d},
    "vlrs_105_vol_rs_sig_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_105_vol_rs_sig_rank_252d},
    "vlrs_106_vol_rs_accel_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_106_vol_rs_accel_lvl_5d},
    "vlrs_107_vol_rs_accel_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_107_vol_rs_accel_zscore_5d},
    "vlrs_108_vol_rs_accel_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_108_vol_rs_accel_rank_5d},
    "vlrs_109_vol_rs_accel_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_109_vol_rs_accel_lvl_21d},
    "vlrs_110_vol_rs_accel_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_110_vol_rs_accel_zscore_21d},
    "vlrs_111_vol_rs_accel_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_111_vol_rs_accel_rank_21d},
    "vlrs_112_vol_rs_accel_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_112_vol_rs_accel_lvl_63d},
    "vlrs_113_vol_rs_accel_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_113_vol_rs_accel_zscore_63d},
    "vlrs_114_vol_rs_accel_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_114_vol_rs_accel_rank_63d},
    "vlrs_115_vol_rs_accel_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_115_vol_rs_accel_lvl_126d},
    "vlrs_116_vol_rs_accel_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_116_vol_rs_accel_zscore_126d},
    "vlrs_117_vol_rs_accel_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_117_vol_rs_accel_rank_126d},
    "vlrs_118_vol_rs_accel_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_118_vol_rs_accel_lvl_252d},
    "vlrs_119_vol_rs_accel_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_119_vol_rs_accel_zscore_252d},
    "vlrs_120_vol_rs_accel_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_120_vol_rs_accel_rank_252d},
    "vlrs_121_vol_rs_log_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_121_vol_rs_log_lvl_5d},
    "vlrs_122_vol_rs_log_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_122_vol_rs_log_zscore_5d},
    "vlrs_123_vol_rs_log_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_123_vol_rs_log_rank_5d},
    "vlrs_124_vol_rs_log_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_124_vol_rs_log_lvl_21d},
    "vlrs_125_vol_rs_log_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_125_vol_rs_log_zscore_21d},
    "vlrs_126_vol_rs_log_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_126_vol_rs_log_rank_21d},
    "vlrs_127_vol_rs_log_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_127_vol_rs_log_lvl_63d},
    "vlrs_128_vol_rs_log_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_128_vol_rs_log_zscore_63d},
    "vlrs_129_vol_rs_log_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_129_vol_rs_log_rank_63d},
    "vlrs_130_vol_rs_log_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_130_vol_rs_log_lvl_126d},
    "vlrs_131_vol_rs_log_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_131_vol_rs_log_zscore_126d},
    "vlrs_132_vol_rs_log_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_132_vol_rs_log_rank_126d},
    "vlrs_133_vol_rs_log_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_133_vol_rs_log_lvl_252d},
    "vlrs_134_vol_rs_log_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_134_vol_rs_log_zscore_252d},
    "vlrs_135_vol_rs_log_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_135_vol_rs_log_rank_252d},
    "vlrs_136_vol_rs_std_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_136_vol_rs_std_lvl_5d},
    "vlrs_137_vol_rs_std_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_137_vol_rs_std_zscore_5d},
    "vlrs_138_vol_rs_std_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_138_vol_rs_std_rank_5d},
    "vlrs_139_vol_rs_std_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_139_vol_rs_std_lvl_21d},
    "vlrs_140_vol_rs_std_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_140_vol_rs_std_zscore_21d},
    "vlrs_141_vol_rs_std_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_141_vol_rs_std_rank_21d},
    "vlrs_142_vol_rs_std_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_142_vol_rs_std_lvl_63d},
    "vlrs_143_vol_rs_std_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_143_vol_rs_std_zscore_63d},
    "vlrs_144_vol_rs_std_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_144_vol_rs_std_rank_63d},
    "vlrs_145_vol_rs_std_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_145_vol_rs_std_lvl_126d},
    "vlrs_146_vol_rs_std_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_146_vol_rs_std_zscore_126d},
    "vlrs_147_vol_rs_std_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_147_vol_rs_std_rank_126d},
    "vlrs_148_vol_rs_std_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_148_vol_rs_std_lvl_252d},
    "vlrs_149_vol_rs_std_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_149_vol_rs_std_zscore_252d},
    "vlrs_150_vol_rs_std_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_150_vol_rs_std_rank_252d},
}
