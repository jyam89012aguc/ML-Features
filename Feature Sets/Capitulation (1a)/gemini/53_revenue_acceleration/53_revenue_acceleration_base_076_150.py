"""
53_revenue_acceleration — Base Features 076-150
Domain: revenue_acceleration
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

def reva_076_rev_accel_63_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_076_rev_accel_63_lvl_5d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 5)

def reva_077_rev_accel_63_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_077_rev_accel_63_zscore_5d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 5)

def reva_078_rev_accel_63_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_078_rev_accel_63_rank_5d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 5)

def reva_079_rev_accel_63_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_079_rev_accel_63_lvl_21d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 21)

def reva_080_rev_accel_63_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_080_rev_accel_63_zscore_21d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 21)

def reva_081_rev_accel_63_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_081_rev_accel_63_rank_21d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 21)

def reva_082_rev_accel_63_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_082_rev_accel_63_lvl_63d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 63)

def reva_083_rev_accel_63_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_083_rev_accel_63_zscore_63d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 63)

def reva_084_rev_accel_63_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_084_rev_accel_63_rank_63d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 63)

def reva_085_rev_accel_63_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_085_rev_accel_63_lvl_126d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 126)

def reva_086_rev_accel_63_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_086_rev_accel_63_zscore_126d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 126)

def reva_087_rev_accel_63_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_087_rev_accel_63_rank_126d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 126)

def reva_088_rev_accel_63_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_088_rev_accel_63_lvl_252d"""
    base = revenue.pct_change(252).diff(63)
    return _rolling_mean(base, 252)

def reva_089_rev_accel_63_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_089_rev_accel_63_zscore_252d"""
    base = revenue.pct_change(252).diff(63)
    return _zscore_rolling(base, 252)

def reva_090_rev_accel_63_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_090_rev_accel_63_rank_252d"""
    base = revenue.pct_change(252).diff(63)
    return _rank_pct(base, 252)

def reva_091_rev_accel_21_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_091_rev_accel_21_lvl_5d"""
    base = revenue.pct_change(63).diff(21)
    return _rolling_mean(base, 5)

def reva_092_rev_accel_21_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_092_rev_accel_21_zscore_5d"""
    base = revenue.pct_change(63).diff(21)
    return _zscore_rolling(base, 5)

def reva_093_rev_accel_21_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_093_rev_accel_21_rank_5d"""
    base = revenue.pct_change(63).diff(21)
    return _rank_pct(base, 5)

def reva_094_rev_accel_21_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_094_rev_accel_21_lvl_21d"""
    base = revenue.pct_change(63).diff(21)
    return _rolling_mean(base, 21)

def reva_095_rev_accel_21_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_095_rev_accel_21_zscore_21d"""
    base = revenue.pct_change(63).diff(21)
    return _zscore_rolling(base, 21)

def reva_096_rev_accel_21_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_096_rev_accel_21_rank_21d"""
    base = revenue.pct_change(63).diff(21)
    return _rank_pct(base, 21)

def reva_097_rev_accel_21_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_097_rev_accel_21_lvl_63d"""
    base = revenue.pct_change(63).diff(21)
    return _rolling_mean(base, 63)

def reva_098_rev_accel_21_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_098_rev_accel_21_zscore_63d"""
    base = revenue.pct_change(63).diff(21)
    return _zscore_rolling(base, 63)

def reva_099_rev_accel_21_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_099_rev_accel_21_rank_63d"""
    base = revenue.pct_change(63).diff(21)
    return _rank_pct(base, 63)

def reva_100_rev_accel_21_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_100_rev_accel_21_lvl_126d"""
    base = revenue.pct_change(63).diff(21)
    return _rolling_mean(base, 126)

def reva_101_rev_accel_21_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_101_rev_accel_21_zscore_126d"""
    base = revenue.pct_change(63).diff(21)
    return _zscore_rolling(base, 126)

def reva_102_rev_accel_21_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_102_rev_accel_21_rank_126d"""
    base = revenue.pct_change(63).diff(21)
    return _rank_pct(base, 126)

def reva_103_rev_accel_21_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_103_rev_accel_21_lvl_252d"""
    base = revenue.pct_change(63).diff(21)
    return _rolling_mean(base, 252)

def reva_104_rev_accel_21_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_104_rev_accel_21_zscore_252d"""
    base = revenue.pct_change(63).diff(21)
    return _zscore_rolling(base, 252)

def reva_105_rev_accel_21_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_105_rev_accel_21_rank_252d"""
    base = revenue.pct_change(63).diff(21)
    return _rank_pct(base, 252)

def reva_106_rev_momentum_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_106_rev_momentum_lvl_5d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rolling_mean(base, 5)

def reva_107_rev_momentum_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_107_rev_momentum_zscore_5d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _zscore_rolling(base, 5)

def reva_108_rev_momentum_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_108_rev_momentum_rank_5d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rank_pct(base, 5)

def reva_109_rev_momentum_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_109_rev_momentum_lvl_21d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rolling_mean(base, 21)

def reva_110_rev_momentum_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_110_rev_momentum_zscore_21d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _zscore_rolling(base, 21)

def reva_111_rev_momentum_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_111_rev_momentum_rank_21d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rank_pct(base, 21)

def reva_112_rev_momentum_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_112_rev_momentum_lvl_63d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rolling_mean(base, 63)

def reva_113_rev_momentum_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_113_rev_momentum_zscore_63d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _zscore_rolling(base, 63)

def reva_114_rev_momentum_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_114_rev_momentum_rank_63d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rank_pct(base, 63)

def reva_115_rev_momentum_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_115_rev_momentum_lvl_126d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rolling_mean(base, 126)

def reva_116_rev_momentum_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_116_rev_momentum_zscore_126d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _zscore_rolling(base, 126)

def reva_117_rev_momentum_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_117_rev_momentum_rank_126d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rank_pct(base, 126)

def reva_118_rev_momentum_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_118_rev_momentum_lvl_252d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rolling_mean(base, 252)

def reva_119_rev_momentum_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_119_rev_momentum_zscore_252d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _zscore_rolling(base, 252)

def reva_120_rev_momentum_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_120_rev_momentum_rank_252d"""
    base = _safe_div(revenue, _rolling_mean(revenue, 252))
    return _rank_pct(base, 252)

def reva_121_rev_log_growth_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_121_rev_log_growth_lvl_5d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rolling_mean(base, 5)

def reva_122_rev_log_growth_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_122_rev_log_growth_zscore_5d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _zscore_rolling(base, 5)

def reva_123_rev_log_growth_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_123_rev_log_growth_rank_5d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rank_pct(base, 5)

def reva_124_rev_log_growth_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_124_rev_log_growth_lvl_21d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rolling_mean(base, 21)

def reva_125_rev_log_growth_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_125_rev_log_growth_zscore_21d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _zscore_rolling(base, 21)

def reva_126_rev_log_growth_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_126_rev_log_growth_rank_21d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rank_pct(base, 21)

def reva_127_rev_log_growth_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_127_rev_log_growth_lvl_63d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rolling_mean(base, 63)

def reva_128_rev_log_growth_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_128_rev_log_growth_zscore_63d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _zscore_rolling(base, 63)

def reva_129_rev_log_growth_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_129_rev_log_growth_rank_63d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rank_pct(base, 63)

def reva_130_rev_log_growth_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_130_rev_log_growth_lvl_126d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rolling_mean(base, 126)

def reva_131_rev_log_growth_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_131_rev_log_growth_zscore_126d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _zscore_rolling(base, 126)

def reva_132_rev_log_growth_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_132_rev_log_growth_rank_126d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rank_pct(base, 126)

def reva_133_rev_log_growth_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_133_rev_log_growth_lvl_252d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rolling_mean(base, 252)

def reva_134_rev_log_growth_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_134_rev_log_growth_zscore_252d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _zscore_rolling(base, 252)

def reva_135_rev_log_growth_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_135_rev_log_growth_rank_252d"""
    base = np.log1p(revenue.pct_change(252).clip(lower=-0.9))
    return _rank_pct(base, 252)

def reva_136_rev_stability_lvl_5d(revenue: pd.Series) -> pd.Series:
    """reva_136_rev_stability_lvl_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rolling_mean(base, 5)

def reva_137_rev_stability_zscore_5d(revenue: pd.Series) -> pd.Series:
    """reva_137_rev_stability_zscore_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _zscore_rolling(base, 5)

def reva_138_rev_stability_rank_5d(revenue: pd.Series) -> pd.Series:
    """reva_138_rev_stability_rank_5d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rank_pct(base, 5)

def reva_139_rev_stability_lvl_21d(revenue: pd.Series) -> pd.Series:
    """reva_139_rev_stability_lvl_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rolling_mean(base, 21)

def reva_140_rev_stability_zscore_21d(revenue: pd.Series) -> pd.Series:
    """reva_140_rev_stability_zscore_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _zscore_rolling(base, 21)

def reva_141_rev_stability_rank_21d(revenue: pd.Series) -> pd.Series:
    """reva_141_rev_stability_rank_21d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rank_pct(base, 21)

def reva_142_rev_stability_lvl_63d(revenue: pd.Series) -> pd.Series:
    """reva_142_rev_stability_lvl_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rolling_mean(base, 63)

def reva_143_rev_stability_zscore_63d(revenue: pd.Series) -> pd.Series:
    """reva_143_rev_stability_zscore_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _zscore_rolling(base, 63)

def reva_144_rev_stability_rank_63d(revenue: pd.Series) -> pd.Series:
    """reva_144_rev_stability_rank_63d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rank_pct(base, 63)

def reva_145_rev_stability_lvl_126d(revenue: pd.Series) -> pd.Series:
    """reva_145_rev_stability_lvl_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rolling_mean(base, 126)

def reva_146_rev_stability_zscore_126d(revenue: pd.Series) -> pd.Series:
    """reva_146_rev_stability_zscore_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _zscore_rolling(base, 126)

def reva_147_rev_stability_rank_126d(revenue: pd.Series) -> pd.Series:
    """reva_147_rev_stability_rank_126d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rank_pct(base, 126)

def reva_148_rev_stability_lvl_252d(revenue: pd.Series) -> pd.Series:
    """reva_148_rev_stability_lvl_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rolling_mean(base, 252)

def reva_149_rev_stability_zscore_252d(revenue: pd.Series) -> pd.Series:
    """reva_149_rev_stability_zscore_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _zscore_rolling(base, 252)

def reva_150_rev_stability_rank_252d(revenue: pd.Series) -> pd.Series:
    """reva_150_rev_stability_rank_252d"""
    base = _safe_div(pd.Series(1.0, index=revenue.index), _rolling_std(revenue.pct_change(21), 63))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V53_REGISTRY_2 = {
    "reva_076_rev_accel_63_lvl_5d": {"inputs": ["revenue"], "func": reva_076_rev_accel_63_lvl_5d},
    "reva_077_rev_accel_63_zscore_5d": {"inputs": ["revenue"], "func": reva_077_rev_accel_63_zscore_5d},
    "reva_078_rev_accel_63_rank_5d": {"inputs": ["revenue"], "func": reva_078_rev_accel_63_rank_5d},
    "reva_079_rev_accel_63_lvl_21d": {"inputs": ["revenue"], "func": reva_079_rev_accel_63_lvl_21d},
    "reva_080_rev_accel_63_zscore_21d": {"inputs": ["revenue"], "func": reva_080_rev_accel_63_zscore_21d},
    "reva_081_rev_accel_63_rank_21d": {"inputs": ["revenue"], "func": reva_081_rev_accel_63_rank_21d},
    "reva_082_rev_accel_63_lvl_63d": {"inputs": ["revenue"], "func": reva_082_rev_accel_63_lvl_63d},
    "reva_083_rev_accel_63_zscore_63d": {"inputs": ["revenue"], "func": reva_083_rev_accel_63_zscore_63d},
    "reva_084_rev_accel_63_rank_63d": {"inputs": ["revenue"], "func": reva_084_rev_accel_63_rank_63d},
    "reva_085_rev_accel_63_lvl_126d": {"inputs": ["revenue"], "func": reva_085_rev_accel_63_lvl_126d},
    "reva_086_rev_accel_63_zscore_126d": {"inputs": ["revenue"], "func": reva_086_rev_accel_63_zscore_126d},
    "reva_087_rev_accel_63_rank_126d": {"inputs": ["revenue"], "func": reva_087_rev_accel_63_rank_126d},
    "reva_088_rev_accel_63_lvl_252d": {"inputs": ["revenue"], "func": reva_088_rev_accel_63_lvl_252d},
    "reva_089_rev_accel_63_zscore_252d": {"inputs": ["revenue"], "func": reva_089_rev_accel_63_zscore_252d},
    "reva_090_rev_accel_63_rank_252d": {"inputs": ["revenue"], "func": reva_090_rev_accel_63_rank_252d},
    "reva_091_rev_accel_21_lvl_5d": {"inputs": ["revenue"], "func": reva_091_rev_accel_21_lvl_5d},
    "reva_092_rev_accel_21_zscore_5d": {"inputs": ["revenue"], "func": reva_092_rev_accel_21_zscore_5d},
    "reva_093_rev_accel_21_rank_5d": {"inputs": ["revenue"], "func": reva_093_rev_accel_21_rank_5d},
    "reva_094_rev_accel_21_lvl_21d": {"inputs": ["revenue"], "func": reva_094_rev_accel_21_lvl_21d},
    "reva_095_rev_accel_21_zscore_21d": {"inputs": ["revenue"], "func": reva_095_rev_accel_21_zscore_21d},
    "reva_096_rev_accel_21_rank_21d": {"inputs": ["revenue"], "func": reva_096_rev_accel_21_rank_21d},
    "reva_097_rev_accel_21_lvl_63d": {"inputs": ["revenue"], "func": reva_097_rev_accel_21_lvl_63d},
    "reva_098_rev_accel_21_zscore_63d": {"inputs": ["revenue"], "func": reva_098_rev_accel_21_zscore_63d},
    "reva_099_rev_accel_21_rank_63d": {"inputs": ["revenue"], "func": reva_099_rev_accel_21_rank_63d},
    "reva_100_rev_accel_21_lvl_126d": {"inputs": ["revenue"], "func": reva_100_rev_accel_21_lvl_126d},
    "reva_101_rev_accel_21_zscore_126d": {"inputs": ["revenue"], "func": reva_101_rev_accel_21_zscore_126d},
    "reva_102_rev_accel_21_rank_126d": {"inputs": ["revenue"], "func": reva_102_rev_accel_21_rank_126d},
    "reva_103_rev_accel_21_lvl_252d": {"inputs": ["revenue"], "func": reva_103_rev_accel_21_lvl_252d},
    "reva_104_rev_accel_21_zscore_252d": {"inputs": ["revenue"], "func": reva_104_rev_accel_21_zscore_252d},
    "reva_105_rev_accel_21_rank_252d": {"inputs": ["revenue"], "func": reva_105_rev_accel_21_rank_252d},
    "reva_106_rev_momentum_lvl_5d": {"inputs": ["revenue"], "func": reva_106_rev_momentum_lvl_5d},
    "reva_107_rev_momentum_zscore_5d": {"inputs": ["revenue"], "func": reva_107_rev_momentum_zscore_5d},
    "reva_108_rev_momentum_rank_5d": {"inputs": ["revenue"], "func": reva_108_rev_momentum_rank_5d},
    "reva_109_rev_momentum_lvl_21d": {"inputs": ["revenue"], "func": reva_109_rev_momentum_lvl_21d},
    "reva_110_rev_momentum_zscore_21d": {"inputs": ["revenue"], "func": reva_110_rev_momentum_zscore_21d},
    "reva_111_rev_momentum_rank_21d": {"inputs": ["revenue"], "func": reva_111_rev_momentum_rank_21d},
    "reva_112_rev_momentum_lvl_63d": {"inputs": ["revenue"], "func": reva_112_rev_momentum_lvl_63d},
    "reva_113_rev_momentum_zscore_63d": {"inputs": ["revenue"], "func": reva_113_rev_momentum_zscore_63d},
    "reva_114_rev_momentum_rank_63d": {"inputs": ["revenue"], "func": reva_114_rev_momentum_rank_63d},
    "reva_115_rev_momentum_lvl_126d": {"inputs": ["revenue"], "func": reva_115_rev_momentum_lvl_126d},
    "reva_116_rev_momentum_zscore_126d": {"inputs": ["revenue"], "func": reva_116_rev_momentum_zscore_126d},
    "reva_117_rev_momentum_rank_126d": {"inputs": ["revenue"], "func": reva_117_rev_momentum_rank_126d},
    "reva_118_rev_momentum_lvl_252d": {"inputs": ["revenue"], "func": reva_118_rev_momentum_lvl_252d},
    "reva_119_rev_momentum_zscore_252d": {"inputs": ["revenue"], "func": reva_119_rev_momentum_zscore_252d},
    "reva_120_rev_momentum_rank_252d": {"inputs": ["revenue"], "func": reva_120_rev_momentum_rank_252d},
    "reva_121_rev_log_growth_lvl_5d": {"inputs": ["revenue"], "func": reva_121_rev_log_growth_lvl_5d},
    "reva_122_rev_log_growth_zscore_5d": {"inputs": ["revenue"], "func": reva_122_rev_log_growth_zscore_5d},
    "reva_123_rev_log_growth_rank_5d": {"inputs": ["revenue"], "func": reva_123_rev_log_growth_rank_5d},
    "reva_124_rev_log_growth_lvl_21d": {"inputs": ["revenue"], "func": reva_124_rev_log_growth_lvl_21d},
    "reva_125_rev_log_growth_zscore_21d": {"inputs": ["revenue"], "func": reva_125_rev_log_growth_zscore_21d},
    "reva_126_rev_log_growth_rank_21d": {"inputs": ["revenue"], "func": reva_126_rev_log_growth_rank_21d},
    "reva_127_rev_log_growth_lvl_63d": {"inputs": ["revenue"], "func": reva_127_rev_log_growth_lvl_63d},
    "reva_128_rev_log_growth_zscore_63d": {"inputs": ["revenue"], "func": reva_128_rev_log_growth_zscore_63d},
    "reva_129_rev_log_growth_rank_63d": {"inputs": ["revenue"], "func": reva_129_rev_log_growth_rank_63d},
    "reva_130_rev_log_growth_lvl_126d": {"inputs": ["revenue"], "func": reva_130_rev_log_growth_lvl_126d},
    "reva_131_rev_log_growth_zscore_126d": {"inputs": ["revenue"], "func": reva_131_rev_log_growth_zscore_126d},
    "reva_132_rev_log_growth_rank_126d": {"inputs": ["revenue"], "func": reva_132_rev_log_growth_rank_126d},
    "reva_133_rev_log_growth_lvl_252d": {"inputs": ["revenue"], "func": reva_133_rev_log_growth_lvl_252d},
    "reva_134_rev_log_growth_zscore_252d": {"inputs": ["revenue"], "func": reva_134_rev_log_growth_zscore_252d},
    "reva_135_rev_log_growth_rank_252d": {"inputs": ["revenue"], "func": reva_135_rev_log_growth_rank_252d},
    "reva_136_rev_stability_lvl_5d": {"inputs": ["revenue"], "func": reva_136_rev_stability_lvl_5d},
    "reva_137_rev_stability_zscore_5d": {"inputs": ["revenue"], "func": reva_137_rev_stability_zscore_5d},
    "reva_138_rev_stability_rank_5d": {"inputs": ["revenue"], "func": reva_138_rev_stability_rank_5d},
    "reva_139_rev_stability_lvl_21d": {"inputs": ["revenue"], "func": reva_139_rev_stability_lvl_21d},
    "reva_140_rev_stability_zscore_21d": {"inputs": ["revenue"], "func": reva_140_rev_stability_zscore_21d},
    "reva_141_rev_stability_rank_21d": {"inputs": ["revenue"], "func": reva_141_rev_stability_rank_21d},
    "reva_142_rev_stability_lvl_63d": {"inputs": ["revenue"], "func": reva_142_rev_stability_lvl_63d},
    "reva_143_rev_stability_zscore_63d": {"inputs": ["revenue"], "func": reva_143_rev_stability_zscore_63d},
    "reva_144_rev_stability_rank_63d": {"inputs": ["revenue"], "func": reva_144_rev_stability_rank_63d},
    "reva_145_rev_stability_lvl_126d": {"inputs": ["revenue"], "func": reva_145_rev_stability_lvl_126d},
    "reva_146_rev_stability_zscore_126d": {"inputs": ["revenue"], "func": reva_146_rev_stability_zscore_126d},
    "reva_147_rev_stability_rank_126d": {"inputs": ["revenue"], "func": reva_147_rev_stability_rank_126d},
    "reva_148_rev_stability_lvl_252d": {"inputs": ["revenue"], "func": reva_148_rev_stability_lvl_252d},
    "reva_149_rev_stability_zscore_252d": {"inputs": ["revenue"], "func": reva_149_rev_stability_zscore_252d},
    "reva_150_rev_stability_rank_252d": {"inputs": ["revenue"], "func": reva_150_rev_stability_rank_252d},
}
