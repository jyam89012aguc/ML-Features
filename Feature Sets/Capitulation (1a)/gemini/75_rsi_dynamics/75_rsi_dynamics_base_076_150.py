"""
75_rsi_dynamics — Base Features 076-150
Domain: rsi_dynamics
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

def rsid_076_rsi_os_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_076_rsi_os_lvl_5d"""
    base = _rsi(close, 14) - 30
    return _rolling_mean(base, 5)

def rsid_077_rsi_os_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_077_rsi_os_zscore_5d"""
    base = _rsi(close, 14) - 30
    return _zscore_rolling(base, 5)

def rsid_078_rsi_os_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_078_rsi_os_rank_5d"""
    base = _rsi(close, 14) - 30
    return _rank_pct(base, 5)

def rsid_079_rsi_os_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_079_rsi_os_lvl_21d"""
    base = _rsi(close, 14) - 30
    return _rolling_mean(base, 21)

def rsid_080_rsi_os_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_080_rsi_os_zscore_21d"""
    base = _rsi(close, 14) - 30
    return _zscore_rolling(base, 21)

def rsid_081_rsi_os_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_081_rsi_os_rank_21d"""
    base = _rsi(close, 14) - 30
    return _rank_pct(base, 21)

def rsid_082_rsi_os_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_082_rsi_os_lvl_63d"""
    base = _rsi(close, 14) - 30
    return _rolling_mean(base, 63)

def rsid_083_rsi_os_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_083_rsi_os_zscore_63d"""
    base = _rsi(close, 14) - 30
    return _zscore_rolling(base, 63)

def rsid_084_rsi_os_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_084_rsi_os_rank_63d"""
    base = _rsi(close, 14) - 30
    return _rank_pct(base, 63)

def rsid_085_rsi_os_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_085_rsi_os_lvl_126d"""
    base = _rsi(close, 14) - 30
    return _rolling_mean(base, 126)

def rsid_086_rsi_os_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_086_rsi_os_zscore_126d"""
    base = _rsi(close, 14) - 30
    return _zscore_rolling(base, 126)

def rsid_087_rsi_os_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_087_rsi_os_rank_126d"""
    base = _rsi(close, 14) - 30
    return _rank_pct(base, 126)

def rsid_088_rsi_os_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_088_rsi_os_lvl_252d"""
    base = _rsi(close, 14) - 30
    return _rolling_mean(base, 252)

def rsid_089_rsi_os_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_089_rsi_os_zscore_252d"""
    base = _rsi(close, 14) - 30
    return _zscore_rolling(base, 252)

def rsid_090_rsi_os_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_090_rsi_os_rank_252d"""
    base = _rsi(close, 14) - 30
    return _rank_pct(base, 252)

def rsid_091_rsi_63_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_091_rsi_63_lvl_5d"""
    base = _rsi(close, 63)
    return _rolling_mean(base, 5)

def rsid_092_rsi_63_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_092_rsi_63_zscore_5d"""
    base = _rsi(close, 63)
    return _zscore_rolling(base, 5)

def rsid_093_rsi_63_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_093_rsi_63_rank_5d"""
    base = _rsi(close, 63)
    return _rank_pct(base, 5)

def rsid_094_rsi_63_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_094_rsi_63_lvl_21d"""
    base = _rsi(close, 63)
    return _rolling_mean(base, 21)

def rsid_095_rsi_63_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_095_rsi_63_zscore_21d"""
    base = _rsi(close, 63)
    return _zscore_rolling(base, 21)

def rsid_096_rsi_63_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_096_rsi_63_rank_21d"""
    base = _rsi(close, 63)
    return _rank_pct(base, 21)

def rsid_097_rsi_63_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_097_rsi_63_lvl_63d"""
    base = _rsi(close, 63)
    return _rolling_mean(base, 63)

def rsid_098_rsi_63_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_098_rsi_63_zscore_63d"""
    base = _rsi(close, 63)
    return _zscore_rolling(base, 63)

def rsid_099_rsi_63_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_099_rsi_63_rank_63d"""
    base = _rsi(close, 63)
    return _rank_pct(base, 63)

def rsid_100_rsi_63_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_100_rsi_63_lvl_126d"""
    base = _rsi(close, 63)
    return _rolling_mean(base, 126)

def rsid_101_rsi_63_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_101_rsi_63_zscore_126d"""
    base = _rsi(close, 63)
    return _zscore_rolling(base, 126)

def rsid_102_rsi_63_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_102_rsi_63_rank_126d"""
    base = _rsi(close, 63)
    return _rank_pct(base, 126)

def rsid_103_rsi_63_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_103_rsi_63_lvl_252d"""
    base = _rsi(close, 63)
    return _rolling_mean(base, 252)

def rsid_104_rsi_63_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_104_rsi_63_zscore_252d"""
    base = _rsi(close, 63)
    return _zscore_rolling(base, 252)

def rsid_105_rsi_63_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_105_rsi_63_rank_252d"""
    base = _rsi(close, 63)
    return _rank_pct(base, 252)

def rsid_106_rsi_ema_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_106_rsi_ema_lvl_5d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rolling_mean(base, 5)

def rsid_107_rsi_ema_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_107_rsi_ema_zscore_5d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _zscore_rolling(base, 5)

def rsid_108_rsi_ema_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_108_rsi_ema_rank_5d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rank_pct(base, 5)

def rsid_109_rsi_ema_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_109_rsi_ema_lvl_21d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rolling_mean(base, 21)

def rsid_110_rsi_ema_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_110_rsi_ema_zscore_21d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _zscore_rolling(base, 21)

def rsid_111_rsi_ema_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_111_rsi_ema_rank_21d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rank_pct(base, 21)

def rsid_112_rsi_ema_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_112_rsi_ema_lvl_63d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rolling_mean(base, 63)

def rsid_113_rsi_ema_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_113_rsi_ema_zscore_63d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _zscore_rolling(base, 63)

def rsid_114_rsi_ema_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_114_rsi_ema_rank_63d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rank_pct(base, 63)

def rsid_115_rsi_ema_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_115_rsi_ema_lvl_126d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rolling_mean(base, 126)

def rsid_116_rsi_ema_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_116_rsi_ema_zscore_126d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _zscore_rolling(base, 126)

def rsid_117_rsi_ema_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_117_rsi_ema_rank_126d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rank_pct(base, 126)

def rsid_118_rsi_ema_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_118_rsi_ema_lvl_252d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rolling_mean(base, 252)

def rsid_119_rsi_ema_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_119_rsi_ema_zscore_252d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _zscore_rolling(base, 252)

def rsid_120_rsi_ema_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_120_rsi_ema_rank_252d"""
    base = _ewm_mean(_rsi(close, 14), 9)
    return _rank_pct(base, 252)

def rsid_121_rsi_sma_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_121_rsi_sma_rat_lvl_5d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rolling_mean(base, 5)

def rsid_122_rsi_sma_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_122_rsi_sma_rat_zscore_5d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _zscore_rolling(base, 5)

def rsid_123_rsi_sma_rat_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_123_rsi_sma_rat_rank_5d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rank_pct(base, 5)

def rsid_124_rsi_sma_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_124_rsi_sma_rat_lvl_21d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rolling_mean(base, 21)

def rsid_125_rsi_sma_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_125_rsi_sma_rat_zscore_21d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _zscore_rolling(base, 21)

def rsid_126_rsi_sma_rat_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_126_rsi_sma_rat_rank_21d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rank_pct(base, 21)

def rsid_127_rsi_sma_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_127_rsi_sma_rat_lvl_63d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rolling_mean(base, 63)

def rsid_128_rsi_sma_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_128_rsi_sma_rat_zscore_63d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _zscore_rolling(base, 63)

def rsid_129_rsi_sma_rat_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_129_rsi_sma_rat_rank_63d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rank_pct(base, 63)

def rsid_130_rsi_sma_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_130_rsi_sma_rat_lvl_126d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rolling_mean(base, 126)

def rsid_131_rsi_sma_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_131_rsi_sma_rat_zscore_126d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _zscore_rolling(base, 126)

def rsid_132_rsi_sma_rat_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_132_rsi_sma_rat_rank_126d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rank_pct(base, 126)

def rsid_133_rsi_sma_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_133_rsi_sma_rat_lvl_252d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rolling_mean(base, 252)

def rsid_134_rsi_sma_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_134_rsi_sma_rat_zscore_252d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _zscore_rolling(base, 252)

def rsid_135_rsi_sma_rat_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_135_rsi_sma_rat_rank_252d"""
    base = _safe_div(_rsi(close, 14), _rolling_mean(_rsi(close, 14), 14))
    return _rank_pct(base, 252)

def rsid_136_rsi_z_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_136_rsi_z_lvl_5d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rolling_mean(base, 5)

def rsid_137_rsi_z_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_137_rsi_z_zscore_5d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _zscore_rolling(base, 5)

def rsid_138_rsi_z_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_138_rsi_z_rank_5d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rank_pct(base, 5)

def rsid_139_rsi_z_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_139_rsi_z_lvl_21d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rolling_mean(base, 21)

def rsid_140_rsi_z_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_140_rsi_z_zscore_21d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _zscore_rolling(base, 21)

def rsid_141_rsi_z_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_141_rsi_z_rank_21d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rank_pct(base, 21)

def rsid_142_rsi_z_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_142_rsi_z_lvl_63d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rolling_mean(base, 63)

def rsid_143_rsi_z_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_143_rsi_z_zscore_63d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _zscore_rolling(base, 63)

def rsid_144_rsi_z_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_144_rsi_z_rank_63d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rank_pct(base, 63)

def rsid_145_rsi_z_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_145_rsi_z_lvl_126d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rolling_mean(base, 126)

def rsid_146_rsi_z_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_146_rsi_z_zscore_126d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _zscore_rolling(base, 126)

def rsid_147_rsi_z_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_147_rsi_z_rank_126d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rank_pct(base, 126)

def rsid_148_rsi_z_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_148_rsi_z_lvl_252d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rolling_mean(base, 252)

def rsid_149_rsi_z_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_149_rsi_z_zscore_252d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _zscore_rolling(base, 252)

def rsid_150_rsi_z_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_150_rsi_z_rank_252d"""
    base = _zscore_rolling(_rsi(close, 14), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V75_REGISTRY_2 = {
    "rsid_076_rsi_os_lvl_5d": {"inputs": ["close"], "func": rsid_076_rsi_os_lvl_5d},
    "rsid_077_rsi_os_zscore_5d": {"inputs": ["close"], "func": rsid_077_rsi_os_zscore_5d},
    "rsid_078_rsi_os_rank_5d": {"inputs": ["close"], "func": rsid_078_rsi_os_rank_5d},
    "rsid_079_rsi_os_lvl_21d": {"inputs": ["close"], "func": rsid_079_rsi_os_lvl_21d},
    "rsid_080_rsi_os_zscore_21d": {"inputs": ["close"], "func": rsid_080_rsi_os_zscore_21d},
    "rsid_081_rsi_os_rank_21d": {"inputs": ["close"], "func": rsid_081_rsi_os_rank_21d},
    "rsid_082_rsi_os_lvl_63d": {"inputs": ["close"], "func": rsid_082_rsi_os_lvl_63d},
    "rsid_083_rsi_os_zscore_63d": {"inputs": ["close"], "func": rsid_083_rsi_os_zscore_63d},
    "rsid_084_rsi_os_rank_63d": {"inputs": ["close"], "func": rsid_084_rsi_os_rank_63d},
    "rsid_085_rsi_os_lvl_126d": {"inputs": ["close"], "func": rsid_085_rsi_os_lvl_126d},
    "rsid_086_rsi_os_zscore_126d": {"inputs": ["close"], "func": rsid_086_rsi_os_zscore_126d},
    "rsid_087_rsi_os_rank_126d": {"inputs": ["close"], "func": rsid_087_rsi_os_rank_126d},
    "rsid_088_rsi_os_lvl_252d": {"inputs": ["close"], "func": rsid_088_rsi_os_lvl_252d},
    "rsid_089_rsi_os_zscore_252d": {"inputs": ["close"], "func": rsid_089_rsi_os_zscore_252d},
    "rsid_090_rsi_os_rank_252d": {"inputs": ["close"], "func": rsid_090_rsi_os_rank_252d},
    "rsid_091_rsi_63_lvl_5d": {"inputs": ["close"], "func": rsid_091_rsi_63_lvl_5d},
    "rsid_092_rsi_63_zscore_5d": {"inputs": ["close"], "func": rsid_092_rsi_63_zscore_5d},
    "rsid_093_rsi_63_rank_5d": {"inputs": ["close"], "func": rsid_093_rsi_63_rank_5d},
    "rsid_094_rsi_63_lvl_21d": {"inputs": ["close"], "func": rsid_094_rsi_63_lvl_21d},
    "rsid_095_rsi_63_zscore_21d": {"inputs": ["close"], "func": rsid_095_rsi_63_zscore_21d},
    "rsid_096_rsi_63_rank_21d": {"inputs": ["close"], "func": rsid_096_rsi_63_rank_21d},
    "rsid_097_rsi_63_lvl_63d": {"inputs": ["close"], "func": rsid_097_rsi_63_lvl_63d},
    "rsid_098_rsi_63_zscore_63d": {"inputs": ["close"], "func": rsid_098_rsi_63_zscore_63d},
    "rsid_099_rsi_63_rank_63d": {"inputs": ["close"], "func": rsid_099_rsi_63_rank_63d},
    "rsid_100_rsi_63_lvl_126d": {"inputs": ["close"], "func": rsid_100_rsi_63_lvl_126d},
    "rsid_101_rsi_63_zscore_126d": {"inputs": ["close"], "func": rsid_101_rsi_63_zscore_126d},
    "rsid_102_rsi_63_rank_126d": {"inputs": ["close"], "func": rsid_102_rsi_63_rank_126d},
    "rsid_103_rsi_63_lvl_252d": {"inputs": ["close"], "func": rsid_103_rsi_63_lvl_252d},
    "rsid_104_rsi_63_zscore_252d": {"inputs": ["close"], "func": rsid_104_rsi_63_zscore_252d},
    "rsid_105_rsi_63_rank_252d": {"inputs": ["close"], "func": rsid_105_rsi_63_rank_252d},
    "rsid_106_rsi_ema_lvl_5d": {"inputs": ["close"], "func": rsid_106_rsi_ema_lvl_5d},
    "rsid_107_rsi_ema_zscore_5d": {"inputs": ["close"], "func": rsid_107_rsi_ema_zscore_5d},
    "rsid_108_rsi_ema_rank_5d": {"inputs": ["close"], "func": rsid_108_rsi_ema_rank_5d},
    "rsid_109_rsi_ema_lvl_21d": {"inputs": ["close"], "func": rsid_109_rsi_ema_lvl_21d},
    "rsid_110_rsi_ema_zscore_21d": {"inputs": ["close"], "func": rsid_110_rsi_ema_zscore_21d},
    "rsid_111_rsi_ema_rank_21d": {"inputs": ["close"], "func": rsid_111_rsi_ema_rank_21d},
    "rsid_112_rsi_ema_lvl_63d": {"inputs": ["close"], "func": rsid_112_rsi_ema_lvl_63d},
    "rsid_113_rsi_ema_zscore_63d": {"inputs": ["close"], "func": rsid_113_rsi_ema_zscore_63d},
    "rsid_114_rsi_ema_rank_63d": {"inputs": ["close"], "func": rsid_114_rsi_ema_rank_63d},
    "rsid_115_rsi_ema_lvl_126d": {"inputs": ["close"], "func": rsid_115_rsi_ema_lvl_126d},
    "rsid_116_rsi_ema_zscore_126d": {"inputs": ["close"], "func": rsid_116_rsi_ema_zscore_126d},
    "rsid_117_rsi_ema_rank_126d": {"inputs": ["close"], "func": rsid_117_rsi_ema_rank_126d},
    "rsid_118_rsi_ema_lvl_252d": {"inputs": ["close"], "func": rsid_118_rsi_ema_lvl_252d},
    "rsid_119_rsi_ema_zscore_252d": {"inputs": ["close"], "func": rsid_119_rsi_ema_zscore_252d},
    "rsid_120_rsi_ema_rank_252d": {"inputs": ["close"], "func": rsid_120_rsi_ema_rank_252d},
    "rsid_121_rsi_sma_rat_lvl_5d": {"inputs": ["close"], "func": rsid_121_rsi_sma_rat_lvl_5d},
    "rsid_122_rsi_sma_rat_zscore_5d": {"inputs": ["close"], "func": rsid_122_rsi_sma_rat_zscore_5d},
    "rsid_123_rsi_sma_rat_rank_5d": {"inputs": ["close"], "func": rsid_123_rsi_sma_rat_rank_5d},
    "rsid_124_rsi_sma_rat_lvl_21d": {"inputs": ["close"], "func": rsid_124_rsi_sma_rat_lvl_21d},
    "rsid_125_rsi_sma_rat_zscore_21d": {"inputs": ["close"], "func": rsid_125_rsi_sma_rat_zscore_21d},
    "rsid_126_rsi_sma_rat_rank_21d": {"inputs": ["close"], "func": rsid_126_rsi_sma_rat_rank_21d},
    "rsid_127_rsi_sma_rat_lvl_63d": {"inputs": ["close"], "func": rsid_127_rsi_sma_rat_lvl_63d},
    "rsid_128_rsi_sma_rat_zscore_63d": {"inputs": ["close"], "func": rsid_128_rsi_sma_rat_zscore_63d},
    "rsid_129_rsi_sma_rat_rank_63d": {"inputs": ["close"], "func": rsid_129_rsi_sma_rat_rank_63d},
    "rsid_130_rsi_sma_rat_lvl_126d": {"inputs": ["close"], "func": rsid_130_rsi_sma_rat_lvl_126d},
    "rsid_131_rsi_sma_rat_zscore_126d": {"inputs": ["close"], "func": rsid_131_rsi_sma_rat_zscore_126d},
    "rsid_132_rsi_sma_rat_rank_126d": {"inputs": ["close"], "func": rsid_132_rsi_sma_rat_rank_126d},
    "rsid_133_rsi_sma_rat_lvl_252d": {"inputs": ["close"], "func": rsid_133_rsi_sma_rat_lvl_252d},
    "rsid_134_rsi_sma_rat_zscore_252d": {"inputs": ["close"], "func": rsid_134_rsi_sma_rat_zscore_252d},
    "rsid_135_rsi_sma_rat_rank_252d": {"inputs": ["close"], "func": rsid_135_rsi_sma_rat_rank_252d},
    "rsid_136_rsi_z_lvl_5d": {"inputs": ["close"], "func": rsid_136_rsi_z_lvl_5d},
    "rsid_137_rsi_z_zscore_5d": {"inputs": ["close"], "func": rsid_137_rsi_z_zscore_5d},
    "rsid_138_rsi_z_rank_5d": {"inputs": ["close"], "func": rsid_138_rsi_z_rank_5d},
    "rsid_139_rsi_z_lvl_21d": {"inputs": ["close"], "func": rsid_139_rsi_z_lvl_21d},
    "rsid_140_rsi_z_zscore_21d": {"inputs": ["close"], "func": rsid_140_rsi_z_zscore_21d},
    "rsid_141_rsi_z_rank_21d": {"inputs": ["close"], "func": rsid_141_rsi_z_rank_21d},
    "rsid_142_rsi_z_lvl_63d": {"inputs": ["close"], "func": rsid_142_rsi_z_lvl_63d},
    "rsid_143_rsi_z_zscore_63d": {"inputs": ["close"], "func": rsid_143_rsi_z_zscore_63d},
    "rsid_144_rsi_z_rank_63d": {"inputs": ["close"], "func": rsid_144_rsi_z_rank_63d},
    "rsid_145_rsi_z_lvl_126d": {"inputs": ["close"], "func": rsid_145_rsi_z_lvl_126d},
    "rsid_146_rsi_z_zscore_126d": {"inputs": ["close"], "func": rsid_146_rsi_z_zscore_126d},
    "rsid_147_rsi_z_rank_126d": {"inputs": ["close"], "func": rsid_147_rsi_z_rank_126d},
    "rsid_148_rsi_z_lvl_252d": {"inputs": ["close"], "func": rsid_148_rsi_z_lvl_252d},
    "rsid_149_rsi_z_zscore_252d": {"inputs": ["close"], "func": rsid_149_rsi_z_zscore_252d},
    "rsid_150_rsi_z_rank_252d": {"inputs": ["close"], "func": rsid_150_rsi_z_rank_252d},
}
