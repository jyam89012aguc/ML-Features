"""
82_obvd_dynamics — Base Features 076-150
Domain: obvd_dynamics
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

def obvd_076_obv_rank_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_076_obv_rank_lvl_5d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rolling_mean(base, 5)

def obvd_077_obv_rank_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_077_obv_rank_zscore_5d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _zscore_rolling(base, 5)

def obvd_078_obv_rank_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_078_obv_rank_rank_5d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rank_pct(base, 5)

def obvd_079_obv_rank_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_079_obv_rank_lvl_21d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rolling_mean(base, 21)

def obvd_080_obv_rank_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_080_obv_rank_zscore_21d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _zscore_rolling(base, 21)

def obvd_081_obv_rank_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_081_obv_rank_rank_21d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rank_pct(base, 21)

def obvd_082_obv_rank_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_082_obv_rank_lvl_63d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rolling_mean(base, 63)

def obvd_083_obv_rank_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_083_obv_rank_zscore_63d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _zscore_rolling(base, 63)

def obvd_084_obv_rank_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_084_obv_rank_rank_63d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rank_pct(base, 63)

def obvd_085_obv_rank_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_085_obv_rank_lvl_126d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rolling_mean(base, 126)

def obvd_086_obv_rank_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_086_obv_rank_zscore_126d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _zscore_rolling(base, 126)

def obvd_087_obv_rank_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_087_obv_rank_rank_126d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rank_pct(base, 126)

def obvd_088_obv_rank_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_088_obv_rank_lvl_252d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rolling_mean(base, 252)

def obvd_089_obv_rank_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_089_obv_rank_zscore_252d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _zscore_rolling(base, 252)

def obvd_090_obv_rank_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_090_obv_rank_rank_252d"""
    base = _rank_pct((volume * np.sign(close.diff()).fillna(0)).cumsum(), 252)
    return _rank_pct(base, 252)

def obvd_091_obv_ema_rat_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_091_obv_ema_rat_lvl_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 5)

def obvd_092_obv_ema_rat_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_092_obv_ema_rat_zscore_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 5)

def obvd_093_obv_ema_rat_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_093_obv_ema_rat_rank_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 5)

def obvd_094_obv_ema_rat_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_094_obv_ema_rat_lvl_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 21)

def obvd_095_obv_ema_rat_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_095_obv_ema_rat_zscore_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 21)

def obvd_096_obv_ema_rat_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_096_obv_ema_rat_rank_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 21)

def obvd_097_obv_ema_rat_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_097_obv_ema_rat_lvl_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 63)

def obvd_098_obv_ema_rat_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_098_obv_ema_rat_zscore_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 63)

def obvd_099_obv_ema_rat_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_099_obv_ema_rat_rank_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 63)

def obvd_100_obv_ema_rat_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_100_obv_ema_rat_lvl_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 126)

def obvd_101_obv_ema_rat_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_101_obv_ema_rat_zscore_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 126)

def obvd_102_obv_ema_rat_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_102_obv_ema_rat_rank_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 126)

def obvd_103_obv_ema_rat_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_103_obv_ema_rat_lvl_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 252)

def obvd_104_obv_ema_rat_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_104_obv_ema_rat_zscore_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 252)

def obvd_105_obv_ema_rat_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_105_obv_ema_rat_rank_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _ewm_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 252)

def obvd_106_obv_accel_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_106_obv_accel_lvl_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rolling_mean(base, 5)

def obvd_107_obv_accel_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_107_obv_accel_zscore_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _zscore_rolling(base, 5)

def obvd_108_obv_accel_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_108_obv_accel_rank_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rank_pct(base, 5)

def obvd_109_obv_accel_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_109_obv_accel_lvl_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rolling_mean(base, 21)

def obvd_110_obv_accel_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_110_obv_accel_zscore_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _zscore_rolling(base, 21)

def obvd_111_obv_accel_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_111_obv_accel_rank_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rank_pct(base, 21)

def obvd_112_obv_accel_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_112_obv_accel_lvl_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rolling_mean(base, 63)

def obvd_113_obv_accel_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_113_obv_accel_zscore_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _zscore_rolling(base, 63)

def obvd_114_obv_accel_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_114_obv_accel_rank_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rank_pct(base, 63)

def obvd_115_obv_accel_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_115_obv_accel_lvl_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rolling_mean(base, 126)

def obvd_116_obv_accel_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_116_obv_accel_zscore_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _zscore_rolling(base, 126)

def obvd_117_obv_accel_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_117_obv_accel_rank_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rank_pct(base, 126)

def obvd_118_obv_accel_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_118_obv_accel_lvl_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rolling_mean(base, 252)

def obvd_119_obv_accel_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_119_obv_accel_zscore_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _zscore_rolling(base, 252)

def obvd_120_obv_accel_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_120_obv_accel_rank_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5).diff(5)
    return _rank_pct(base, 252)

def obvd_121_obv_disp_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_121_obv_disp_lvl_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 5)

def obvd_122_obv_disp_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_122_obv_disp_zscore_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 5)

def obvd_123_obv_disp_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_123_obv_disp_rank_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 5)

def obvd_124_obv_disp_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_124_obv_disp_lvl_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 21)

def obvd_125_obv_disp_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_125_obv_disp_zscore_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 21)

def obvd_126_obv_disp_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_126_obv_disp_rank_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 21)

def obvd_127_obv_disp_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_127_obv_disp_lvl_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 63)

def obvd_128_obv_disp_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_128_obv_disp_zscore_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 63)

def obvd_129_obv_disp_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_129_obv_disp_rank_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 63)

def obvd_130_obv_disp_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_130_obv_disp_lvl_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 126)

def obvd_131_obv_disp_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_131_obv_disp_zscore_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 126)

def obvd_132_obv_disp_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_132_obv_disp_rank_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 126)

def obvd_133_obv_disp_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_133_obv_disp_lvl_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 252)

def obvd_134_obv_disp_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_134_obv_disp_zscore_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 252)

def obvd_135_obv_disp_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_135_obv_disp_rank_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum() - _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20), _rolling_std((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 252)

def obvd_136_obv_flow_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_136_obv_flow_lvl_5d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rolling_mean(base, 5)

def obvd_137_obv_flow_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_137_obv_flow_zscore_5d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _zscore_rolling(base, 5)

def obvd_138_obv_flow_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_138_obv_flow_rank_5d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rank_pct(base, 5)

def obvd_139_obv_flow_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_139_obv_flow_lvl_21d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rolling_mean(base, 21)

def obvd_140_obv_flow_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_140_obv_flow_zscore_21d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _zscore_rolling(base, 21)

def obvd_141_obv_flow_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_141_obv_flow_rank_21d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rank_pct(base, 21)

def obvd_142_obv_flow_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_142_obv_flow_lvl_63d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rolling_mean(base, 63)

def obvd_143_obv_flow_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_143_obv_flow_zscore_63d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _zscore_rolling(base, 63)

def obvd_144_obv_flow_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_144_obv_flow_rank_63d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rank_pct(base, 63)

def obvd_145_obv_flow_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_145_obv_flow_lvl_126d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rolling_mean(base, 126)

def obvd_146_obv_flow_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_146_obv_flow_zscore_126d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _zscore_rolling(base, 126)

def obvd_147_obv_flow_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_147_obv_flow_rank_126d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rank_pct(base, 126)

def obvd_148_obv_flow_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_148_obv_flow_lvl_252d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rolling_mean(base, 252)

def obvd_149_obv_flow_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_149_obv_flow_zscore_252d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _zscore_rolling(base, 252)

def obvd_150_obv_flow_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_150_obv_flow_rank_252d"""
    base = _rolling_sum(volume * np.sign(close.diff()).fillna(0), 20)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V82_REGISTRY_2 = {
    "obvd_076_obv_rank_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_076_obv_rank_lvl_5d},
    "obvd_077_obv_rank_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_077_obv_rank_zscore_5d},
    "obvd_078_obv_rank_rank_5d": {"inputs": ["close", "volume"], "func": obvd_078_obv_rank_rank_5d},
    "obvd_079_obv_rank_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_079_obv_rank_lvl_21d},
    "obvd_080_obv_rank_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_080_obv_rank_zscore_21d},
    "obvd_081_obv_rank_rank_21d": {"inputs": ["close", "volume"], "func": obvd_081_obv_rank_rank_21d},
    "obvd_082_obv_rank_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_082_obv_rank_lvl_63d},
    "obvd_083_obv_rank_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_083_obv_rank_zscore_63d},
    "obvd_084_obv_rank_rank_63d": {"inputs": ["close", "volume"], "func": obvd_084_obv_rank_rank_63d},
    "obvd_085_obv_rank_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_085_obv_rank_lvl_126d},
    "obvd_086_obv_rank_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_086_obv_rank_zscore_126d},
    "obvd_087_obv_rank_rank_126d": {"inputs": ["close", "volume"], "func": obvd_087_obv_rank_rank_126d},
    "obvd_088_obv_rank_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_088_obv_rank_lvl_252d},
    "obvd_089_obv_rank_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_089_obv_rank_zscore_252d},
    "obvd_090_obv_rank_rank_252d": {"inputs": ["close", "volume"], "func": obvd_090_obv_rank_rank_252d},
    "obvd_091_obv_ema_rat_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_091_obv_ema_rat_lvl_5d},
    "obvd_092_obv_ema_rat_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_092_obv_ema_rat_zscore_5d},
    "obvd_093_obv_ema_rat_rank_5d": {"inputs": ["close", "volume"], "func": obvd_093_obv_ema_rat_rank_5d},
    "obvd_094_obv_ema_rat_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_094_obv_ema_rat_lvl_21d},
    "obvd_095_obv_ema_rat_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_095_obv_ema_rat_zscore_21d},
    "obvd_096_obv_ema_rat_rank_21d": {"inputs": ["close", "volume"], "func": obvd_096_obv_ema_rat_rank_21d},
    "obvd_097_obv_ema_rat_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_097_obv_ema_rat_lvl_63d},
    "obvd_098_obv_ema_rat_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_098_obv_ema_rat_zscore_63d},
    "obvd_099_obv_ema_rat_rank_63d": {"inputs": ["close", "volume"], "func": obvd_099_obv_ema_rat_rank_63d},
    "obvd_100_obv_ema_rat_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_100_obv_ema_rat_lvl_126d},
    "obvd_101_obv_ema_rat_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_101_obv_ema_rat_zscore_126d},
    "obvd_102_obv_ema_rat_rank_126d": {"inputs": ["close", "volume"], "func": obvd_102_obv_ema_rat_rank_126d},
    "obvd_103_obv_ema_rat_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_103_obv_ema_rat_lvl_252d},
    "obvd_104_obv_ema_rat_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_104_obv_ema_rat_zscore_252d},
    "obvd_105_obv_ema_rat_rank_252d": {"inputs": ["close", "volume"], "func": obvd_105_obv_ema_rat_rank_252d},
    "obvd_106_obv_accel_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_106_obv_accel_lvl_5d},
    "obvd_107_obv_accel_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_107_obv_accel_zscore_5d},
    "obvd_108_obv_accel_rank_5d": {"inputs": ["close", "volume"], "func": obvd_108_obv_accel_rank_5d},
    "obvd_109_obv_accel_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_109_obv_accel_lvl_21d},
    "obvd_110_obv_accel_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_110_obv_accel_zscore_21d},
    "obvd_111_obv_accel_rank_21d": {"inputs": ["close", "volume"], "func": obvd_111_obv_accel_rank_21d},
    "obvd_112_obv_accel_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_112_obv_accel_lvl_63d},
    "obvd_113_obv_accel_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_113_obv_accel_zscore_63d},
    "obvd_114_obv_accel_rank_63d": {"inputs": ["close", "volume"], "func": obvd_114_obv_accel_rank_63d},
    "obvd_115_obv_accel_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_115_obv_accel_lvl_126d},
    "obvd_116_obv_accel_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_116_obv_accel_zscore_126d},
    "obvd_117_obv_accel_rank_126d": {"inputs": ["close", "volume"], "func": obvd_117_obv_accel_rank_126d},
    "obvd_118_obv_accel_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_118_obv_accel_lvl_252d},
    "obvd_119_obv_accel_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_119_obv_accel_zscore_252d},
    "obvd_120_obv_accel_rank_252d": {"inputs": ["close", "volume"], "func": obvd_120_obv_accel_rank_252d},
    "obvd_121_obv_disp_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_121_obv_disp_lvl_5d},
    "obvd_122_obv_disp_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_122_obv_disp_zscore_5d},
    "obvd_123_obv_disp_rank_5d": {"inputs": ["close", "volume"], "func": obvd_123_obv_disp_rank_5d},
    "obvd_124_obv_disp_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_124_obv_disp_lvl_21d},
    "obvd_125_obv_disp_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_125_obv_disp_zscore_21d},
    "obvd_126_obv_disp_rank_21d": {"inputs": ["close", "volume"], "func": obvd_126_obv_disp_rank_21d},
    "obvd_127_obv_disp_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_127_obv_disp_lvl_63d},
    "obvd_128_obv_disp_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_128_obv_disp_zscore_63d},
    "obvd_129_obv_disp_rank_63d": {"inputs": ["close", "volume"], "func": obvd_129_obv_disp_rank_63d},
    "obvd_130_obv_disp_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_130_obv_disp_lvl_126d},
    "obvd_131_obv_disp_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_131_obv_disp_zscore_126d},
    "obvd_132_obv_disp_rank_126d": {"inputs": ["close", "volume"], "func": obvd_132_obv_disp_rank_126d},
    "obvd_133_obv_disp_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_133_obv_disp_lvl_252d},
    "obvd_134_obv_disp_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_134_obv_disp_zscore_252d},
    "obvd_135_obv_disp_rank_252d": {"inputs": ["close", "volume"], "func": obvd_135_obv_disp_rank_252d},
    "obvd_136_obv_flow_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_136_obv_flow_lvl_5d},
    "obvd_137_obv_flow_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_137_obv_flow_zscore_5d},
    "obvd_138_obv_flow_rank_5d": {"inputs": ["close", "volume"], "func": obvd_138_obv_flow_rank_5d},
    "obvd_139_obv_flow_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_139_obv_flow_lvl_21d},
    "obvd_140_obv_flow_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_140_obv_flow_zscore_21d},
    "obvd_141_obv_flow_rank_21d": {"inputs": ["close", "volume"], "func": obvd_141_obv_flow_rank_21d},
    "obvd_142_obv_flow_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_142_obv_flow_lvl_63d},
    "obvd_143_obv_flow_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_143_obv_flow_zscore_63d},
    "obvd_144_obv_flow_rank_63d": {"inputs": ["close", "volume"], "func": obvd_144_obv_flow_rank_63d},
    "obvd_145_obv_flow_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_145_obv_flow_lvl_126d},
    "obvd_146_obv_flow_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_146_obv_flow_zscore_126d},
    "obvd_147_obv_flow_rank_126d": {"inputs": ["close", "volume"], "func": obvd_147_obv_flow_rank_126d},
    "obvd_148_obv_flow_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_148_obv_flow_lvl_252d},
    "obvd_149_obv_flow_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_149_obv_flow_zscore_252d},
    "obvd_150_obv_flow_rank_252d": {"inputs": ["close", "volume"], "func": obvd_150_obv_flow_rank_252d},
}
