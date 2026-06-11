"""
118_drawdown_recovery_asymmetry — Base Features Part 2
Domain: drawdown_recovery_asymmetry
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

def dras_121_drawdown_velocity_z_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_121_drawdown_velocity_z_lvl_5d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rolling_mean(base, 5)

def dras_122_drawdown_velocity_z_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_122_drawdown_velocity_z_zscore_5d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _zscore_rolling(base, 5)

def dras_123_drawdown_velocity_z_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_123_drawdown_velocity_z_rank_5d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rank_pct(base, 5)

def dras_124_drawdown_velocity_z_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_124_drawdown_velocity_z_lvl_21d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rolling_mean(base, 21)

def dras_125_drawdown_velocity_z_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_125_drawdown_velocity_z_zscore_21d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _zscore_rolling(base, 21)

def dras_126_drawdown_velocity_z_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_126_drawdown_velocity_z_rank_21d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rank_pct(base, 21)

def dras_127_drawdown_velocity_z_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_127_drawdown_velocity_z_lvl_63d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rolling_mean(base, 63)

def dras_128_drawdown_velocity_z_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_128_drawdown_velocity_z_zscore_63d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _zscore_rolling(base, 63)

def dras_129_drawdown_velocity_z_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_129_drawdown_velocity_z_rank_63d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rank_pct(base, 63)

def dras_130_drawdown_velocity_z_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_130_drawdown_velocity_z_lvl_126d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rolling_mean(base, 126)

def dras_131_drawdown_velocity_z_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_131_drawdown_velocity_z_zscore_126d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _zscore_rolling(base, 126)

def dras_132_drawdown_velocity_z_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_132_drawdown_velocity_z_rank_126d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rank_pct(base, 126)

def dras_133_drawdown_velocity_z_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_133_drawdown_velocity_z_lvl_252d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rolling_mean(base, 252)

def dras_134_drawdown_velocity_z_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_134_drawdown_velocity_z_zscore_252d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _zscore_rolling(base, 252)

def dras_135_drawdown_velocity_z_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_135_drawdown_velocity_z_rank_252d
    ECONOMIC RATIONALE: Severity of recent drop speed.
    """
    base = _zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)
    return _rank_pct(base, 252)

def dras_136_recovery_efficiency_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_136_recovery_efficiency_lvl_5d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dras_137_recovery_efficiency_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_137_recovery_efficiency_zscore_5d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dras_138_recovery_efficiency_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_138_recovery_efficiency_rank_5d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def dras_139_recovery_efficiency_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_139_recovery_efficiency_lvl_21d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dras_140_recovery_efficiency_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_140_recovery_efficiency_zscore_21d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dras_141_recovery_efficiency_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_141_recovery_efficiency_rank_21d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def dras_142_recovery_efficiency_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_142_recovery_efficiency_lvl_63d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dras_143_recovery_efficiency_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_143_recovery_efficiency_zscore_63d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dras_144_recovery_efficiency_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_144_recovery_efficiency_rank_63d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def dras_145_recovery_efficiency_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_145_recovery_efficiency_lvl_126d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dras_146_recovery_efficiency_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_146_recovery_efficiency_zscore_126d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dras_147_recovery_efficiency_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_147_recovery_efficiency_rank_126d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def dras_148_recovery_efficiency_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_148_recovery_efficiency_lvl_252d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dras_149_recovery_efficiency_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_149_recovery_efficiency_zscore_252d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dras_150_recovery_efficiency_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_150_recovery_efficiency_rank_252d
    ECONOMIC RATIONALE: Upside move normalized by volatility.
    """
    base = close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def dras_151_drawdown_efficiency_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_151_drawdown_efficiency_lvl_5d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dras_152_drawdown_efficiency_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_152_drawdown_efficiency_zscore_5d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dras_153_drawdown_efficiency_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_153_drawdown_efficiency_rank_5d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def dras_154_drawdown_efficiency_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_154_drawdown_efficiency_lvl_21d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dras_155_drawdown_efficiency_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_155_drawdown_efficiency_zscore_21d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dras_156_drawdown_efficiency_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_156_drawdown_efficiency_rank_21d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def dras_157_drawdown_efficiency_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_157_drawdown_efficiency_lvl_63d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dras_158_drawdown_efficiency_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_158_drawdown_efficiency_zscore_63d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dras_159_drawdown_efficiency_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_159_drawdown_efficiency_rank_63d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def dras_160_drawdown_efficiency_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_160_drawdown_efficiency_lvl_126d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dras_161_drawdown_efficiency_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_161_drawdown_efficiency_zscore_126d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dras_162_drawdown_efficiency_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_162_drawdown_efficiency_rank_126d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def dras_163_drawdown_efficiency_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_163_drawdown_efficiency_lvl_252d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dras_164_drawdown_efficiency_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_164_drawdown_efficiency_zscore_252d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dras_165_drawdown_efficiency_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_165_drawdown_efficiency_rank_252d
    ECONOMIC RATIONALE: Downside move normalized by volatility.
    """
    base = close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def dras_166_asymmetry_regime_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_166_asymmetry_regime_lvl_5d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rolling_mean(base, 5)

def dras_167_asymmetry_regime_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_167_asymmetry_regime_zscore_5d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _zscore_rolling(base, 5)

def dras_168_asymmetry_regime_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_168_asymmetry_regime_rank_5d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rank_pct(base, 5)

def dras_169_asymmetry_regime_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_169_asymmetry_regime_lvl_21d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rolling_mean(base, 21)

def dras_170_asymmetry_regime_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_170_asymmetry_regime_zscore_21d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _zscore_rolling(base, 21)

def dras_171_asymmetry_regime_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_171_asymmetry_regime_rank_21d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rank_pct(base, 21)

def dras_172_asymmetry_regime_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_172_asymmetry_regime_lvl_63d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rolling_mean(base, 63)

def dras_173_asymmetry_regime_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_173_asymmetry_regime_zscore_63d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _zscore_rolling(base, 63)

def dras_174_asymmetry_regime_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_174_asymmetry_regime_rank_63d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rank_pct(base, 63)

def dras_175_asymmetry_regime_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_175_asymmetry_regime_lvl_126d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rolling_mean(base, 126)

def dras_176_asymmetry_regime_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_176_asymmetry_regime_zscore_126d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _zscore_rolling(base, 126)

def dras_177_asymmetry_regime_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_177_asymmetry_regime_rank_126d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rank_pct(base, 126)

def dras_178_asymmetry_regime_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_178_asymmetry_regime_lvl_252d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rolling_mean(base, 252)

def dras_179_asymmetry_regime_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_179_asymmetry_regime_zscore_252d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _zscore_rolling(base, 252)

def dras_180_asymmetry_regime_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_180_asymmetry_regime_rank_252d
    ECONOMIC RATIONALE: Deviation from historical asymmetry.
    """
    base = recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()
    return _rank_pct(base, 252)

def dras_181_sequential_drop_count_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_181_sequential_drop_count_lvl_5d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rolling_mean(base, 5)

def dras_182_sequential_drop_count_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_182_sequential_drop_count_zscore_5d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _zscore_rolling(base, 5)

def dras_183_sequential_drop_count_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_183_sequential_drop_count_rank_5d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rank_pct(base, 5)

def dras_184_sequential_drop_count_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_184_sequential_drop_count_lvl_21d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rolling_mean(base, 21)

def dras_185_sequential_drop_count_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_185_sequential_drop_count_zscore_21d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _zscore_rolling(base, 21)

def dras_186_sequential_drop_count_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_186_sequential_drop_count_rank_21d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rank_pct(base, 21)

def dras_187_sequential_drop_count_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_187_sequential_drop_count_lvl_63d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rolling_mean(base, 63)

def dras_188_sequential_drop_count_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_188_sequential_drop_count_zscore_63d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _zscore_rolling(base, 63)

def dras_189_sequential_drop_count_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_189_sequential_drop_count_rank_63d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rank_pct(base, 63)

def dras_190_sequential_drop_count_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_190_sequential_drop_count_lvl_126d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rolling_mean(base, 126)

def dras_191_sequential_drop_count_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_191_sequential_drop_count_zscore_126d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _zscore_rolling(base, 126)

def dras_192_sequential_drop_count_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_192_sequential_drop_count_rank_126d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rank_pct(base, 126)

def dras_193_sequential_drop_count_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_193_sequential_drop_count_lvl_252d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rolling_mean(base, 252)

def dras_194_sequential_drop_count_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_194_sequential_drop_count_zscore_252d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _zscore_rolling(base, 252)

def dras_195_sequential_drop_count_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_195_sequential_drop_count_rank_252d
    ECONOMIC RATIONALE: Number of consecutive down days.
    """
    base = (close.diff(1) < 0).rolling(10).sum()
    return _rank_pct(base, 252)

def dras_196_sequential_rally_count_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_196_sequential_rally_count_lvl_5d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rolling_mean(base, 5)

def dras_197_sequential_rally_count_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_197_sequential_rally_count_zscore_5d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _zscore_rolling(base, 5)

def dras_198_sequential_rally_count_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_198_sequential_rally_count_rank_5d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rank_pct(base, 5)

def dras_199_sequential_rally_count_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_199_sequential_rally_count_lvl_21d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rolling_mean(base, 21)

def dras_200_sequential_rally_count_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_200_sequential_rally_count_zscore_21d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _zscore_rolling(base, 21)

def dras_201_sequential_rally_count_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_201_sequential_rally_count_rank_21d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rank_pct(base, 21)

def dras_202_sequential_rally_count_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_202_sequential_rally_count_lvl_63d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rolling_mean(base, 63)

def dras_203_sequential_rally_count_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_203_sequential_rally_count_zscore_63d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _zscore_rolling(base, 63)

def dras_204_sequential_rally_count_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_204_sequential_rally_count_rank_63d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rank_pct(base, 63)

def dras_205_sequential_rally_count_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_205_sequential_rally_count_lvl_126d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rolling_mean(base, 126)

def dras_206_sequential_rally_count_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_206_sequential_rally_count_zscore_126d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _zscore_rolling(base, 126)

def dras_207_sequential_rally_count_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_207_sequential_rally_count_rank_126d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rank_pct(base, 126)

def dras_208_sequential_rally_count_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_208_sequential_rally_count_lvl_252d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rolling_mean(base, 252)

def dras_209_sequential_rally_count_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_209_sequential_rally_count_zscore_252d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _zscore_rolling(base, 252)

def dras_210_sequential_rally_count_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_210_sequential_rally_count_rank_252d
    ECONOMIC RATIONALE: Number of consecutive up days.
    """
    base = (close.diff(1) > 0).rolling(10).sum()
    return _rank_pct(base, 252)

def dras_211_drawdown_recovery_gap_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_211_drawdown_recovery_gap_lvl_5d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rolling_mean(base, 5)

def dras_212_drawdown_recovery_gap_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_212_drawdown_recovery_gap_zscore_5d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _zscore_rolling(base, 5)

def dras_213_drawdown_recovery_gap_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_213_drawdown_recovery_gap_rank_5d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rank_pct(base, 5)

def dras_214_drawdown_recovery_gap_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_214_drawdown_recovery_gap_lvl_21d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rolling_mean(base, 21)

def dras_215_drawdown_recovery_gap_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_215_drawdown_recovery_gap_zscore_21d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _zscore_rolling(base, 21)

def dras_216_drawdown_recovery_gap_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_216_drawdown_recovery_gap_rank_21d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rank_pct(base, 21)

def dras_217_drawdown_recovery_gap_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_217_drawdown_recovery_gap_lvl_63d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rolling_mean(base, 63)

def dras_218_drawdown_recovery_gap_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_218_drawdown_recovery_gap_zscore_63d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _zscore_rolling(base, 63)

def dras_219_drawdown_recovery_gap_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_219_drawdown_recovery_gap_rank_63d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rank_pct(base, 63)

def dras_220_drawdown_recovery_gap_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_220_drawdown_recovery_gap_lvl_126d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rolling_mean(base, 126)

def dras_221_drawdown_recovery_gap_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_221_drawdown_recovery_gap_zscore_126d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _zscore_rolling(base, 126)

def dras_222_drawdown_recovery_gap_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_222_drawdown_recovery_gap_rank_126d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rank_pct(base, 126)

def dras_223_drawdown_recovery_gap_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_223_drawdown_recovery_gap_lvl_252d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rolling_mean(base, 252)

def dras_224_drawdown_recovery_gap_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_224_drawdown_recovery_gap_zscore_252d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _zscore_rolling(base, 252)

def dras_225_drawdown_recovery_gap_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_225_drawdown_recovery_gap_rank_252d
    ECONOMIC RATIONALE: Distance from peak vs distance from trough.
    """
    base = (close.rolling(252).max() - close) - (close - close.rolling(252).min())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V118_REGISTRY_2 = {
    "dras_121_drawdown_velocity_z_lvl_5d": {"inputs": ["close"], "func": dras_121_drawdown_velocity_z_lvl_5d},
    "dras_122_drawdown_velocity_z_zscore_5d": {"inputs": ["close"], "func": dras_122_drawdown_velocity_z_zscore_5d},
    "dras_123_drawdown_velocity_z_rank_5d": {"inputs": ["close"], "func": dras_123_drawdown_velocity_z_rank_5d},
    "dras_124_drawdown_velocity_z_lvl_21d": {"inputs": ["close"], "func": dras_124_drawdown_velocity_z_lvl_21d},
    "dras_125_drawdown_velocity_z_zscore_21d": {"inputs": ["close"], "func": dras_125_drawdown_velocity_z_zscore_21d},
    "dras_126_drawdown_velocity_z_rank_21d": {"inputs": ["close"], "func": dras_126_drawdown_velocity_z_rank_21d},
    "dras_127_drawdown_velocity_z_lvl_63d": {"inputs": ["close"], "func": dras_127_drawdown_velocity_z_lvl_63d},
    "dras_128_drawdown_velocity_z_zscore_63d": {"inputs": ["close"], "func": dras_128_drawdown_velocity_z_zscore_63d},
    "dras_129_drawdown_velocity_z_rank_63d": {"inputs": ["close"], "func": dras_129_drawdown_velocity_z_rank_63d},
    "dras_130_drawdown_velocity_z_lvl_126d": {"inputs": ["close"], "func": dras_130_drawdown_velocity_z_lvl_126d},
    "dras_131_drawdown_velocity_z_zscore_126d": {"inputs": ["close"], "func": dras_131_drawdown_velocity_z_zscore_126d},
    "dras_132_drawdown_velocity_z_rank_126d": {"inputs": ["close"], "func": dras_132_drawdown_velocity_z_rank_126d},
    "dras_133_drawdown_velocity_z_lvl_252d": {"inputs": ["close"], "func": dras_133_drawdown_velocity_z_lvl_252d},
    "dras_134_drawdown_velocity_z_zscore_252d": {"inputs": ["close"], "func": dras_134_drawdown_velocity_z_zscore_252d},
    "dras_135_drawdown_velocity_z_rank_252d": {"inputs": ["close"], "func": dras_135_drawdown_velocity_z_rank_252d},
    "dras_136_recovery_efficiency_lvl_5d": {"inputs": ["close"], "func": dras_136_recovery_efficiency_lvl_5d},
    "dras_137_recovery_efficiency_zscore_5d": {"inputs": ["close"], "func": dras_137_recovery_efficiency_zscore_5d},
    "dras_138_recovery_efficiency_rank_5d": {"inputs": ["close"], "func": dras_138_recovery_efficiency_rank_5d},
    "dras_139_recovery_efficiency_lvl_21d": {"inputs": ["close"], "func": dras_139_recovery_efficiency_lvl_21d},
    "dras_140_recovery_efficiency_zscore_21d": {"inputs": ["close"], "func": dras_140_recovery_efficiency_zscore_21d},
    "dras_141_recovery_efficiency_rank_21d": {"inputs": ["close"], "func": dras_141_recovery_efficiency_rank_21d},
    "dras_142_recovery_efficiency_lvl_63d": {"inputs": ["close"], "func": dras_142_recovery_efficiency_lvl_63d},
    "dras_143_recovery_efficiency_zscore_63d": {"inputs": ["close"], "func": dras_143_recovery_efficiency_zscore_63d},
    "dras_144_recovery_efficiency_rank_63d": {"inputs": ["close"], "func": dras_144_recovery_efficiency_rank_63d},
    "dras_145_recovery_efficiency_lvl_126d": {"inputs": ["close"], "func": dras_145_recovery_efficiency_lvl_126d},
    "dras_146_recovery_efficiency_zscore_126d": {"inputs": ["close"], "func": dras_146_recovery_efficiency_zscore_126d},
    "dras_147_recovery_efficiency_rank_126d": {"inputs": ["close"], "func": dras_147_recovery_efficiency_rank_126d},
    "dras_148_recovery_efficiency_lvl_252d": {"inputs": ["close"], "func": dras_148_recovery_efficiency_lvl_252d},
    "dras_149_recovery_efficiency_zscore_252d": {"inputs": ["close"], "func": dras_149_recovery_efficiency_zscore_252d},
    "dras_150_recovery_efficiency_rank_252d": {"inputs": ["close"], "func": dras_150_recovery_efficiency_rank_252d},
    "dras_151_drawdown_efficiency_lvl_5d": {"inputs": ["close"], "func": dras_151_drawdown_efficiency_lvl_5d},
    "dras_152_drawdown_efficiency_zscore_5d": {"inputs": ["close"], "func": dras_152_drawdown_efficiency_zscore_5d},
    "dras_153_drawdown_efficiency_rank_5d": {"inputs": ["close"], "func": dras_153_drawdown_efficiency_rank_5d},
    "dras_154_drawdown_efficiency_lvl_21d": {"inputs": ["close"], "func": dras_154_drawdown_efficiency_lvl_21d},
    "dras_155_drawdown_efficiency_zscore_21d": {"inputs": ["close"], "func": dras_155_drawdown_efficiency_zscore_21d},
    "dras_156_drawdown_efficiency_rank_21d": {"inputs": ["close"], "func": dras_156_drawdown_efficiency_rank_21d},
    "dras_157_drawdown_efficiency_lvl_63d": {"inputs": ["close"], "func": dras_157_drawdown_efficiency_lvl_63d},
    "dras_158_drawdown_efficiency_zscore_63d": {"inputs": ["close"], "func": dras_158_drawdown_efficiency_zscore_63d},
    "dras_159_drawdown_efficiency_rank_63d": {"inputs": ["close"], "func": dras_159_drawdown_efficiency_rank_63d},
    "dras_160_drawdown_efficiency_lvl_126d": {"inputs": ["close"], "func": dras_160_drawdown_efficiency_lvl_126d},
    "dras_161_drawdown_efficiency_zscore_126d": {"inputs": ["close"], "func": dras_161_drawdown_efficiency_zscore_126d},
    "dras_162_drawdown_efficiency_rank_126d": {"inputs": ["close"], "func": dras_162_drawdown_efficiency_rank_126d},
    "dras_163_drawdown_efficiency_lvl_252d": {"inputs": ["close"], "func": dras_163_drawdown_efficiency_lvl_252d},
    "dras_164_drawdown_efficiency_zscore_252d": {"inputs": ["close"], "func": dras_164_drawdown_efficiency_zscore_252d},
    "dras_165_drawdown_efficiency_rank_252d": {"inputs": ["close"], "func": dras_165_drawdown_efficiency_rank_252d},
    "dras_166_asymmetry_regime_lvl_5d": {"inputs": ["close"], "func": dras_166_asymmetry_regime_lvl_5d},
    "dras_167_asymmetry_regime_zscore_5d": {"inputs": ["close"], "func": dras_167_asymmetry_regime_zscore_5d},
    "dras_168_asymmetry_regime_rank_5d": {"inputs": ["close"], "func": dras_168_asymmetry_regime_rank_5d},
    "dras_169_asymmetry_regime_lvl_21d": {"inputs": ["close"], "func": dras_169_asymmetry_regime_lvl_21d},
    "dras_170_asymmetry_regime_zscore_21d": {"inputs": ["close"], "func": dras_170_asymmetry_regime_zscore_21d},
    "dras_171_asymmetry_regime_rank_21d": {"inputs": ["close"], "func": dras_171_asymmetry_regime_rank_21d},
    "dras_172_asymmetry_regime_lvl_63d": {"inputs": ["close"], "func": dras_172_asymmetry_regime_lvl_63d},
    "dras_173_asymmetry_regime_zscore_63d": {"inputs": ["close"], "func": dras_173_asymmetry_regime_zscore_63d},
    "dras_174_asymmetry_regime_rank_63d": {"inputs": ["close"], "func": dras_174_asymmetry_regime_rank_63d},
    "dras_175_asymmetry_regime_lvl_126d": {"inputs": ["close"], "func": dras_175_asymmetry_regime_lvl_126d},
    "dras_176_asymmetry_regime_zscore_126d": {"inputs": ["close"], "func": dras_176_asymmetry_regime_zscore_126d},
    "dras_177_asymmetry_regime_rank_126d": {"inputs": ["close"], "func": dras_177_asymmetry_regime_rank_126d},
    "dras_178_asymmetry_regime_lvl_252d": {"inputs": ["close"], "func": dras_178_asymmetry_regime_lvl_252d},
    "dras_179_asymmetry_regime_zscore_252d": {"inputs": ["close"], "func": dras_179_asymmetry_regime_zscore_252d},
    "dras_180_asymmetry_regime_rank_252d": {"inputs": ["close"], "func": dras_180_asymmetry_regime_rank_252d},
    "dras_181_sequential_drop_count_lvl_5d": {"inputs": ["close"], "func": dras_181_sequential_drop_count_lvl_5d},
    "dras_182_sequential_drop_count_zscore_5d": {"inputs": ["close"], "func": dras_182_sequential_drop_count_zscore_5d},
    "dras_183_sequential_drop_count_rank_5d": {"inputs": ["close"], "func": dras_183_sequential_drop_count_rank_5d},
    "dras_184_sequential_drop_count_lvl_21d": {"inputs": ["close"], "func": dras_184_sequential_drop_count_lvl_21d},
    "dras_185_sequential_drop_count_zscore_21d": {"inputs": ["close"], "func": dras_185_sequential_drop_count_zscore_21d},
    "dras_186_sequential_drop_count_rank_21d": {"inputs": ["close"], "func": dras_186_sequential_drop_count_rank_21d},
    "dras_187_sequential_drop_count_lvl_63d": {"inputs": ["close"], "func": dras_187_sequential_drop_count_lvl_63d},
    "dras_188_sequential_drop_count_zscore_63d": {"inputs": ["close"], "func": dras_188_sequential_drop_count_zscore_63d},
    "dras_189_sequential_drop_count_rank_63d": {"inputs": ["close"], "func": dras_189_sequential_drop_count_rank_63d},
    "dras_190_sequential_drop_count_lvl_126d": {"inputs": ["close"], "func": dras_190_sequential_drop_count_lvl_126d},
    "dras_191_sequential_drop_count_zscore_126d": {"inputs": ["close"], "func": dras_191_sequential_drop_count_zscore_126d},
    "dras_192_sequential_drop_count_rank_126d": {"inputs": ["close"], "func": dras_192_sequential_drop_count_rank_126d},
    "dras_193_sequential_drop_count_lvl_252d": {"inputs": ["close"], "func": dras_193_sequential_drop_count_lvl_252d},
    "dras_194_sequential_drop_count_zscore_252d": {"inputs": ["close"], "func": dras_194_sequential_drop_count_zscore_252d},
    "dras_195_sequential_drop_count_rank_252d": {"inputs": ["close"], "func": dras_195_sequential_drop_count_rank_252d},
    "dras_196_sequential_rally_count_lvl_5d": {"inputs": ["close"], "func": dras_196_sequential_rally_count_lvl_5d},
    "dras_197_sequential_rally_count_zscore_5d": {"inputs": ["close"], "func": dras_197_sequential_rally_count_zscore_5d},
    "dras_198_sequential_rally_count_rank_5d": {"inputs": ["close"], "func": dras_198_sequential_rally_count_rank_5d},
    "dras_199_sequential_rally_count_lvl_21d": {"inputs": ["close"], "func": dras_199_sequential_rally_count_lvl_21d},
    "dras_200_sequential_rally_count_zscore_21d": {"inputs": ["close"], "func": dras_200_sequential_rally_count_zscore_21d},
    "dras_201_sequential_rally_count_rank_21d": {"inputs": ["close"], "func": dras_201_sequential_rally_count_rank_21d},
    "dras_202_sequential_rally_count_lvl_63d": {"inputs": ["close"], "func": dras_202_sequential_rally_count_lvl_63d},
    "dras_203_sequential_rally_count_zscore_63d": {"inputs": ["close"], "func": dras_203_sequential_rally_count_zscore_63d},
    "dras_204_sequential_rally_count_rank_63d": {"inputs": ["close"], "func": dras_204_sequential_rally_count_rank_63d},
    "dras_205_sequential_rally_count_lvl_126d": {"inputs": ["close"], "func": dras_205_sequential_rally_count_lvl_126d},
    "dras_206_sequential_rally_count_zscore_126d": {"inputs": ["close"], "func": dras_206_sequential_rally_count_zscore_126d},
    "dras_207_sequential_rally_count_rank_126d": {"inputs": ["close"], "func": dras_207_sequential_rally_count_rank_126d},
    "dras_208_sequential_rally_count_lvl_252d": {"inputs": ["close"], "func": dras_208_sequential_rally_count_lvl_252d},
    "dras_209_sequential_rally_count_zscore_252d": {"inputs": ["close"], "func": dras_209_sequential_rally_count_zscore_252d},
    "dras_210_sequential_rally_count_rank_252d": {"inputs": ["close"], "func": dras_210_sequential_rally_count_rank_252d},
    "dras_211_drawdown_recovery_gap_lvl_5d": {"inputs": ["close"], "func": dras_211_drawdown_recovery_gap_lvl_5d},
    "dras_212_drawdown_recovery_gap_zscore_5d": {"inputs": ["close"], "func": dras_212_drawdown_recovery_gap_zscore_5d},
    "dras_213_drawdown_recovery_gap_rank_5d": {"inputs": ["close"], "func": dras_213_drawdown_recovery_gap_rank_5d},
    "dras_214_drawdown_recovery_gap_lvl_21d": {"inputs": ["close"], "func": dras_214_drawdown_recovery_gap_lvl_21d},
    "dras_215_drawdown_recovery_gap_zscore_21d": {"inputs": ["close"], "func": dras_215_drawdown_recovery_gap_zscore_21d},
    "dras_216_drawdown_recovery_gap_rank_21d": {"inputs": ["close"], "func": dras_216_drawdown_recovery_gap_rank_21d},
    "dras_217_drawdown_recovery_gap_lvl_63d": {"inputs": ["close"], "func": dras_217_drawdown_recovery_gap_lvl_63d},
    "dras_218_drawdown_recovery_gap_zscore_63d": {"inputs": ["close"], "func": dras_218_drawdown_recovery_gap_zscore_63d},
    "dras_219_drawdown_recovery_gap_rank_63d": {"inputs": ["close"], "func": dras_219_drawdown_recovery_gap_rank_63d},
    "dras_220_drawdown_recovery_gap_lvl_126d": {"inputs": ["close"], "func": dras_220_drawdown_recovery_gap_lvl_126d},
    "dras_221_drawdown_recovery_gap_zscore_126d": {"inputs": ["close"], "func": dras_221_drawdown_recovery_gap_zscore_126d},
    "dras_222_drawdown_recovery_gap_rank_126d": {"inputs": ["close"], "func": dras_222_drawdown_recovery_gap_rank_126d},
    "dras_223_drawdown_recovery_gap_lvl_252d": {"inputs": ["close"], "func": dras_223_drawdown_recovery_gap_lvl_252d},
    "dras_224_drawdown_recovery_gap_zscore_252d": {"inputs": ["close"], "func": dras_224_drawdown_recovery_gap_zscore_252d},
    "dras_225_drawdown_recovery_gap_rank_252d": {"inputs": ["close"], "func": dras_225_drawdown_recovery_gap_rank_252d},
}
