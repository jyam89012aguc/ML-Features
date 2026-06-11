"""
98_srrs_dynamics — Base Features 076-150
Domain: srrs_dynamics
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

def srrs_076_sec_rs_abs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_076_sec_rs_abs_lvl_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 5)

def srrs_077_sec_rs_abs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_077_sec_rs_abs_zscore_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 5)

def srrs_078_sec_rs_abs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_078_sec_rs_abs_rank_5d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 5)

def srrs_079_sec_rs_abs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_079_sec_rs_abs_lvl_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 21)

def srrs_080_sec_rs_abs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_080_sec_rs_abs_zscore_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 21)

def srrs_081_sec_rs_abs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_081_sec_rs_abs_rank_21d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 21)

def srrs_082_sec_rs_abs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_082_sec_rs_abs_lvl_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 63)

def srrs_083_sec_rs_abs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_083_sec_rs_abs_zscore_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 63)

def srrs_084_sec_rs_abs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_084_sec_rs_abs_rank_63d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 63)

def srrs_085_sec_rs_abs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_085_sec_rs_abs_lvl_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 126)

def srrs_086_sec_rs_abs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_086_sec_rs_abs_zscore_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 126)

def srrs_087_sec_rs_abs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_087_sec_rs_abs_rank_126d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 126)

def srrs_088_sec_rs_abs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_088_sec_rs_abs_lvl_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _rolling_mean(base, 252)

def srrs_089_sec_rs_abs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_089_sec_rs_abs_zscore_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _zscore_rolling(base, 252)

def srrs_090_sec_rs_abs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_090_sec_rs_abs_rank_252d"""
    base = _safe_div(close, mkt_close).abs()
    return _rank_pct(base, 252)

def srrs_091_sec_rs_sig_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_091_sec_rs_sig_lvl_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 5)

def srrs_092_sec_rs_sig_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_092_sec_rs_sig_zscore_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 5)

def srrs_093_sec_rs_sig_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_093_sec_rs_sig_rank_5d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 5)

def srrs_094_sec_rs_sig_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_094_sec_rs_sig_lvl_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 21)

def srrs_095_sec_rs_sig_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_095_sec_rs_sig_zscore_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 21)

def srrs_096_sec_rs_sig_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_096_sec_rs_sig_rank_21d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 21)

def srrs_097_sec_rs_sig_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_097_sec_rs_sig_lvl_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 63)

def srrs_098_sec_rs_sig_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_098_sec_rs_sig_zscore_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 63)

def srrs_099_sec_rs_sig_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_099_sec_rs_sig_rank_63d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 63)

def srrs_100_sec_rs_sig_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_100_sec_rs_sig_lvl_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 126)

def srrs_101_sec_rs_sig_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_101_sec_rs_sig_zscore_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 126)

def srrs_102_sec_rs_sig_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_102_sec_rs_sig_rank_126d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 126)

def srrs_103_sec_rs_sig_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_103_sec_rs_sig_lvl_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rolling_mean(base, 252)

def srrs_104_sec_rs_sig_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_104_sec_rs_sig_zscore_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _zscore_rolling(base, 252)

def srrs_105_sec_rs_sig_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_105_sec_rs_sig_rank_252d"""
    base = _rolling_mean(_safe_div(close, mkt_close), 5)
    return _rank_pct(base, 252)

def srrs_106_sec_rs_accel_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_106_sec_rs_accel_lvl_5d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rolling_mean(base, 5)

def srrs_107_sec_rs_accel_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_107_sec_rs_accel_zscore_5d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _zscore_rolling(base, 5)

def srrs_108_sec_rs_accel_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_108_sec_rs_accel_rank_5d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rank_pct(base, 5)

def srrs_109_sec_rs_accel_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_109_sec_rs_accel_lvl_21d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rolling_mean(base, 21)

def srrs_110_sec_rs_accel_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_110_sec_rs_accel_zscore_21d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _zscore_rolling(base, 21)

def srrs_111_sec_rs_accel_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_111_sec_rs_accel_rank_21d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rank_pct(base, 21)

def srrs_112_sec_rs_accel_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_112_sec_rs_accel_lvl_63d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rolling_mean(base, 63)

def srrs_113_sec_rs_accel_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_113_sec_rs_accel_zscore_63d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _zscore_rolling(base, 63)

def srrs_114_sec_rs_accel_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_114_sec_rs_accel_rank_63d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rank_pct(base, 63)

def srrs_115_sec_rs_accel_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_115_sec_rs_accel_lvl_126d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rolling_mean(base, 126)

def srrs_116_sec_rs_accel_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_116_sec_rs_accel_zscore_126d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _zscore_rolling(base, 126)

def srrs_117_sec_rs_accel_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_117_sec_rs_accel_rank_126d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rank_pct(base, 126)

def srrs_118_sec_rs_accel_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_118_sec_rs_accel_lvl_252d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rolling_mean(base, 252)

def srrs_119_sec_rs_accel_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_119_sec_rs_accel_zscore_252d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _zscore_rolling(base, 252)

def srrs_120_sec_rs_accel_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_120_sec_rs_accel_rank_252d"""
    base = _safe_div(close, mkt_close).pct_change(21).diff()
    return _rank_pct(base, 252)

def srrs_121_sec_rs_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_121_sec_rs_log_lvl_5d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rolling_mean(base, 5)

def srrs_122_sec_rs_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_122_sec_rs_log_zscore_5d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def srrs_123_sec_rs_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_123_sec_rs_log_rank_5d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rank_pct(base, 5)

def srrs_124_sec_rs_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_124_sec_rs_log_lvl_21d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rolling_mean(base, 21)

def srrs_125_sec_rs_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_125_sec_rs_log_zscore_21d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def srrs_126_sec_rs_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_126_sec_rs_log_rank_21d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rank_pct(base, 21)

def srrs_127_sec_rs_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_127_sec_rs_log_lvl_63d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rolling_mean(base, 63)

def srrs_128_sec_rs_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_128_sec_rs_log_zscore_63d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def srrs_129_sec_rs_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_129_sec_rs_log_rank_63d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rank_pct(base, 63)

def srrs_130_sec_rs_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_130_sec_rs_log_lvl_126d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rolling_mean(base, 126)

def srrs_131_sec_rs_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_131_sec_rs_log_zscore_126d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def srrs_132_sec_rs_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_132_sec_rs_log_rank_126d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rank_pct(base, 126)

def srrs_133_sec_rs_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_133_sec_rs_log_lvl_252d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rolling_mean(base, 252)

def srrs_134_sec_rs_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_134_sec_rs_log_zscore_252d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def srrs_135_sec_rs_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_135_sec_rs_log_rank_252d"""
    base = np.log(_safe_div(close, mkt_close).clip(lower=_EPS))
    return _rank_pct(base, 252)

def srrs_136_sec_rs_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_136_sec_rs_vol_lvl_5d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rolling_mean(base, 5)

def srrs_137_sec_rs_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_137_sec_rs_vol_zscore_5d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _zscore_rolling(base, 5)

def srrs_138_sec_rs_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_138_sec_rs_vol_rank_5d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rank_pct(base, 5)

def srrs_139_sec_rs_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_139_sec_rs_vol_lvl_21d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rolling_mean(base, 21)

def srrs_140_sec_rs_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_140_sec_rs_vol_zscore_21d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _zscore_rolling(base, 21)

def srrs_141_sec_rs_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_141_sec_rs_vol_rank_21d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rank_pct(base, 21)

def srrs_142_sec_rs_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_142_sec_rs_vol_lvl_63d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rolling_mean(base, 63)

def srrs_143_sec_rs_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_143_sec_rs_vol_zscore_63d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _zscore_rolling(base, 63)

def srrs_144_sec_rs_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_144_sec_rs_vol_rank_63d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rank_pct(base, 63)

def srrs_145_sec_rs_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_145_sec_rs_vol_lvl_126d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rolling_mean(base, 126)

def srrs_146_sec_rs_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_146_sec_rs_vol_zscore_126d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _zscore_rolling(base, 126)

def srrs_147_sec_rs_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_147_sec_rs_vol_rank_126d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rank_pct(base, 126)

def srrs_148_sec_rs_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_148_sec_rs_vol_lvl_252d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rolling_mean(base, 252)

def srrs_149_sec_rs_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_149_sec_rs_vol_zscore_252d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _zscore_rolling(base, 252)

def srrs_150_sec_rs_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_150_sec_rs_vol_rank_252d"""
    base = _rolling_std(_safe_div(close, mkt_close), 21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V98_REGISTRY_2 = {
    "srrs_076_sec_rs_abs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_076_sec_rs_abs_lvl_5d},
    "srrs_077_sec_rs_abs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_077_sec_rs_abs_zscore_5d},
    "srrs_078_sec_rs_abs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_078_sec_rs_abs_rank_5d},
    "srrs_079_sec_rs_abs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_079_sec_rs_abs_lvl_21d},
    "srrs_080_sec_rs_abs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_080_sec_rs_abs_zscore_21d},
    "srrs_081_sec_rs_abs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_081_sec_rs_abs_rank_21d},
    "srrs_082_sec_rs_abs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_082_sec_rs_abs_lvl_63d},
    "srrs_083_sec_rs_abs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_083_sec_rs_abs_zscore_63d},
    "srrs_084_sec_rs_abs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_084_sec_rs_abs_rank_63d},
    "srrs_085_sec_rs_abs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_085_sec_rs_abs_lvl_126d},
    "srrs_086_sec_rs_abs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_086_sec_rs_abs_zscore_126d},
    "srrs_087_sec_rs_abs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_087_sec_rs_abs_rank_126d},
    "srrs_088_sec_rs_abs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_088_sec_rs_abs_lvl_252d},
    "srrs_089_sec_rs_abs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_089_sec_rs_abs_zscore_252d},
    "srrs_090_sec_rs_abs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_090_sec_rs_abs_rank_252d},
    "srrs_091_sec_rs_sig_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_091_sec_rs_sig_lvl_5d},
    "srrs_092_sec_rs_sig_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_092_sec_rs_sig_zscore_5d},
    "srrs_093_sec_rs_sig_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_093_sec_rs_sig_rank_5d},
    "srrs_094_sec_rs_sig_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_094_sec_rs_sig_lvl_21d},
    "srrs_095_sec_rs_sig_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_095_sec_rs_sig_zscore_21d},
    "srrs_096_sec_rs_sig_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_096_sec_rs_sig_rank_21d},
    "srrs_097_sec_rs_sig_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_097_sec_rs_sig_lvl_63d},
    "srrs_098_sec_rs_sig_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_098_sec_rs_sig_zscore_63d},
    "srrs_099_sec_rs_sig_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_099_sec_rs_sig_rank_63d},
    "srrs_100_sec_rs_sig_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_100_sec_rs_sig_lvl_126d},
    "srrs_101_sec_rs_sig_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_101_sec_rs_sig_zscore_126d},
    "srrs_102_sec_rs_sig_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_102_sec_rs_sig_rank_126d},
    "srrs_103_sec_rs_sig_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_103_sec_rs_sig_lvl_252d},
    "srrs_104_sec_rs_sig_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_104_sec_rs_sig_zscore_252d},
    "srrs_105_sec_rs_sig_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_105_sec_rs_sig_rank_252d},
    "srrs_106_sec_rs_accel_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_106_sec_rs_accel_lvl_5d},
    "srrs_107_sec_rs_accel_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_107_sec_rs_accel_zscore_5d},
    "srrs_108_sec_rs_accel_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_108_sec_rs_accel_rank_5d},
    "srrs_109_sec_rs_accel_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_109_sec_rs_accel_lvl_21d},
    "srrs_110_sec_rs_accel_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_110_sec_rs_accel_zscore_21d},
    "srrs_111_sec_rs_accel_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_111_sec_rs_accel_rank_21d},
    "srrs_112_sec_rs_accel_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_112_sec_rs_accel_lvl_63d},
    "srrs_113_sec_rs_accel_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_113_sec_rs_accel_zscore_63d},
    "srrs_114_sec_rs_accel_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_114_sec_rs_accel_rank_63d},
    "srrs_115_sec_rs_accel_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_115_sec_rs_accel_lvl_126d},
    "srrs_116_sec_rs_accel_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_116_sec_rs_accel_zscore_126d},
    "srrs_117_sec_rs_accel_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_117_sec_rs_accel_rank_126d},
    "srrs_118_sec_rs_accel_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_118_sec_rs_accel_lvl_252d},
    "srrs_119_sec_rs_accel_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_119_sec_rs_accel_zscore_252d},
    "srrs_120_sec_rs_accel_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_120_sec_rs_accel_rank_252d},
    "srrs_121_sec_rs_log_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_121_sec_rs_log_lvl_5d},
    "srrs_122_sec_rs_log_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_122_sec_rs_log_zscore_5d},
    "srrs_123_sec_rs_log_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_123_sec_rs_log_rank_5d},
    "srrs_124_sec_rs_log_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_124_sec_rs_log_lvl_21d},
    "srrs_125_sec_rs_log_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_125_sec_rs_log_zscore_21d},
    "srrs_126_sec_rs_log_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_126_sec_rs_log_rank_21d},
    "srrs_127_sec_rs_log_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_127_sec_rs_log_lvl_63d},
    "srrs_128_sec_rs_log_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_128_sec_rs_log_zscore_63d},
    "srrs_129_sec_rs_log_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_129_sec_rs_log_rank_63d},
    "srrs_130_sec_rs_log_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_130_sec_rs_log_lvl_126d},
    "srrs_131_sec_rs_log_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_131_sec_rs_log_zscore_126d},
    "srrs_132_sec_rs_log_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_132_sec_rs_log_rank_126d},
    "srrs_133_sec_rs_log_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_133_sec_rs_log_lvl_252d},
    "srrs_134_sec_rs_log_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_134_sec_rs_log_zscore_252d},
    "srrs_135_sec_rs_log_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_135_sec_rs_log_rank_252d},
    "srrs_136_sec_rs_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_136_sec_rs_vol_lvl_5d},
    "srrs_137_sec_rs_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_137_sec_rs_vol_zscore_5d},
    "srrs_138_sec_rs_vol_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_138_sec_rs_vol_rank_5d},
    "srrs_139_sec_rs_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_139_sec_rs_vol_lvl_21d},
    "srrs_140_sec_rs_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_140_sec_rs_vol_zscore_21d},
    "srrs_141_sec_rs_vol_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_141_sec_rs_vol_rank_21d},
    "srrs_142_sec_rs_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_142_sec_rs_vol_lvl_63d},
    "srrs_143_sec_rs_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_143_sec_rs_vol_zscore_63d},
    "srrs_144_sec_rs_vol_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_144_sec_rs_vol_rank_63d},
    "srrs_145_sec_rs_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_145_sec_rs_vol_lvl_126d},
    "srrs_146_sec_rs_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_146_sec_rs_vol_zscore_126d},
    "srrs_147_sec_rs_vol_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_147_sec_rs_vol_rank_126d},
    "srrs_148_sec_rs_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_148_sec_rs_vol_lvl_252d},
    "srrs_149_sec_rs_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_149_sec_rs_vol_zscore_252d},
    "srrs_150_sec_rs_vol_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_150_sec_rs_vol_rank_252d},
}
