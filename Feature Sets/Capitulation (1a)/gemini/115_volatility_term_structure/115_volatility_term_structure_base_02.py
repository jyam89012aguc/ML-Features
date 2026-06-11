"""
115_volatility_term_structure — Base Features Part 2
Domain: volatility_term_structure
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

def vts_121_vol_acceleration_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_121_vol_acceleration_lvl_5d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rolling_mean(base, 5)

def vts_122_vol_acceleration_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_122_vol_acceleration_zscore_5d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _zscore_rolling(base, 5)

def vts_123_vol_acceleration_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_123_vol_acceleration_rank_5d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rank_pct(base, 5)

def vts_124_vol_acceleration_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_124_vol_acceleration_lvl_21d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rolling_mean(base, 21)

def vts_125_vol_acceleration_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_125_vol_acceleration_zscore_21d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _zscore_rolling(base, 21)

def vts_126_vol_acceleration_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_126_vol_acceleration_rank_21d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rank_pct(base, 21)

def vts_127_vol_acceleration_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_127_vol_acceleration_lvl_63d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rolling_mean(base, 63)

def vts_128_vol_acceleration_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_128_vol_acceleration_zscore_63d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _zscore_rolling(base, 63)

def vts_129_vol_acceleration_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_129_vol_acceleration_rank_63d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rank_pct(base, 63)

def vts_130_vol_acceleration_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_130_vol_acceleration_lvl_126d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rolling_mean(base, 126)

def vts_131_vol_acceleration_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_131_vol_acceleration_zscore_126d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _zscore_rolling(base, 126)

def vts_132_vol_acceleration_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_132_vol_acceleration_rank_126d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rank_pct(base, 126)

def vts_133_vol_acceleration_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_133_vol_acceleration_lvl_252d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rolling_mean(base, 252)

def vts_134_vol_acceleration_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_134_vol_acceleration_zscore_252d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _zscore_rolling(base, 252)

def vts_135_vol_acceleration_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_135_vol_acceleration_rank_252d
    ECONOMIC RATIONALE: Recent acceleration in realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().pct_change(5)
    return _rank_pct(base, 252)

def vts_136_vol_of_vol_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_136_vol_of_vol_lvl_5d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rolling_mean(base, 5)

def vts_137_vol_of_vol_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_137_vol_of_vol_zscore_5d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _zscore_rolling(base, 5)

def vts_138_vol_of_vol_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_138_vol_of_vol_rank_5d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rank_pct(base, 5)

def vts_139_vol_of_vol_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_139_vol_of_vol_lvl_21d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rolling_mean(base, 21)

def vts_140_vol_of_vol_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_140_vol_of_vol_zscore_21d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _zscore_rolling(base, 21)

def vts_141_vol_of_vol_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_141_vol_of_vol_rank_21d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rank_pct(base, 21)

def vts_142_vol_of_vol_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_142_vol_of_vol_lvl_63d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rolling_mean(base, 63)

def vts_143_vol_of_vol_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_143_vol_of_vol_zscore_63d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _zscore_rolling(base, 63)

def vts_144_vol_of_vol_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_144_vol_of_vol_rank_63d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rank_pct(base, 63)

def vts_145_vol_of_vol_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_145_vol_of_vol_lvl_126d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rolling_mean(base, 126)

def vts_146_vol_of_vol_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_146_vol_of_vol_zscore_126d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _zscore_rolling(base, 126)

def vts_147_vol_of_vol_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_147_vol_of_vol_rank_126d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rank_pct(base, 126)

def vts_148_vol_of_vol_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_148_vol_of_vol_lvl_252d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rolling_mean(base, 252)

def vts_149_vol_of_vol_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_149_vol_of_vol_zscore_252d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _zscore_rolling(base, 252)

def vts_150_vol_of_vol_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_150_vol_of_vol_rank_252d
    ECONOMIC RATIONALE: Volatility of the realized volatility.
    """
    base = close.pct_change(1).rolling(21).std().rolling(21).std()
    return _rank_pct(base, 252)

def vts_151_vol_decay_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_151_vol_decay_lvl_5d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rolling_mean(base, 5)

def vts_152_vol_decay_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_152_vol_decay_zscore_5d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _zscore_rolling(base, 5)

def vts_153_vol_decay_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_153_vol_decay_rank_5d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rank_pct(base, 5)

def vts_154_vol_decay_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_154_vol_decay_lvl_21d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rolling_mean(base, 21)

def vts_155_vol_decay_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_155_vol_decay_zscore_21d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _zscore_rolling(base, 21)

def vts_156_vol_decay_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_156_vol_decay_rank_21d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rank_pct(base, 21)

def vts_157_vol_decay_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_157_vol_decay_lvl_63d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rolling_mean(base, 63)

def vts_158_vol_decay_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_158_vol_decay_zscore_63d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _zscore_rolling(base, 63)

def vts_159_vol_decay_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_159_vol_decay_rank_63d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rank_pct(base, 63)

def vts_160_vol_decay_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_160_vol_decay_lvl_126d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rolling_mean(base, 126)

def vts_161_vol_decay_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_161_vol_decay_zscore_126d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _zscore_rolling(base, 126)

def vts_162_vol_decay_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_162_vol_decay_rank_126d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rank_pct(base, 126)

def vts_163_vol_decay_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_163_vol_decay_lvl_252d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rolling_mean(base, 252)

def vts_164_vol_decay_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_164_vol_decay_zscore_252d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _zscore_rolling(base, 252)

def vts_165_vol_decay_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_165_vol_decay_rank_252d
    ECONOMIC RATIONALE: Smoothed volatility decay.
    """
    base = close.pct_change(1).rolling(21).std().ewm(span=63).mean()
    return _rank_pct(base, 252)

def vts_166_vol_term_inversion_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_166_vol_term_inversion_lvl_5d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 5)

def vts_167_vol_term_inversion_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_167_vol_term_inversion_zscore_5d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 5)

def vts_168_vol_term_inversion_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_168_vol_term_inversion_rank_5d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 5)

def vts_169_vol_term_inversion_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_169_vol_term_inversion_lvl_21d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 21)

def vts_170_vol_term_inversion_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_170_vol_term_inversion_zscore_21d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 21)

def vts_171_vol_term_inversion_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_171_vol_term_inversion_rank_21d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 21)

def vts_172_vol_term_inversion_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_172_vol_term_inversion_lvl_63d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 63)

def vts_173_vol_term_inversion_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_173_vol_term_inversion_zscore_63d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 63)

def vts_174_vol_term_inversion_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_174_vol_term_inversion_rank_63d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 63)

def vts_175_vol_term_inversion_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_175_vol_term_inversion_lvl_126d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 126)

def vts_176_vol_term_inversion_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_176_vol_term_inversion_zscore_126d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 126)

def vts_177_vol_term_inversion_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_177_vol_term_inversion_rank_126d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 126)

def vts_178_vol_term_inversion_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_178_vol_term_inversion_lvl_252d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rolling_mean(base, 252)

def vts_179_vol_term_inversion_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_179_vol_term_inversion_zscore_252d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _zscore_rolling(base, 252)

def vts_180_vol_term_inversion_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_180_vol_term_inversion_rank_252d
    ECONOMIC RATIONALE: Binary indicator of volatility term structure inversion.
    """
    base = (close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)
    return _rank_pct(base, 252)

def vts_181_vol_peak_dist_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_181_vol_peak_dist_lvl_5d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rolling_mean(base, 5)

def vts_182_vol_peak_dist_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_182_vol_peak_dist_zscore_5d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _zscore_rolling(base, 5)

def vts_183_vol_peak_dist_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_183_vol_peak_dist_rank_5d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rank_pct(base, 5)

def vts_184_vol_peak_dist_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_184_vol_peak_dist_lvl_21d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rolling_mean(base, 21)

def vts_185_vol_peak_dist_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_185_vol_peak_dist_zscore_21d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _zscore_rolling(base, 21)

def vts_186_vol_peak_dist_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_186_vol_peak_dist_rank_21d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rank_pct(base, 21)

def vts_187_vol_peak_dist_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_187_vol_peak_dist_lvl_63d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rolling_mean(base, 63)

def vts_188_vol_peak_dist_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_188_vol_peak_dist_zscore_63d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _zscore_rolling(base, 63)

def vts_189_vol_peak_dist_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_189_vol_peak_dist_rank_63d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rank_pct(base, 63)

def vts_190_vol_peak_dist_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_190_vol_peak_dist_lvl_126d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rolling_mean(base, 126)

def vts_191_vol_peak_dist_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_191_vol_peak_dist_zscore_126d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _zscore_rolling(base, 126)

def vts_192_vol_peak_dist_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_192_vol_peak_dist_rank_126d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rank_pct(base, 126)

def vts_193_vol_peak_dist_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_193_vol_peak_dist_lvl_252d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rolling_mean(base, 252)

def vts_194_vol_peak_dist_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_194_vol_peak_dist_zscore_252d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _zscore_rolling(base, 252)

def vts_195_vol_peak_dist_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_195_vol_peak_dist_rank_252d
    ECONOMIC RATIONALE: Current volatility relative to its annual peak.
    """
    base = close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()
    return _rank_pct(base, 252)

def vts_196_vol_tail_spread_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_196_vol_tail_spread_lvl_5d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 5)

def vts_197_vol_tail_spread_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_197_vol_tail_spread_zscore_5d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 5)

def vts_198_vol_tail_spread_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_198_vol_tail_spread_rank_5d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 5)

def vts_199_vol_tail_spread_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_199_vol_tail_spread_lvl_21d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 21)

def vts_200_vol_tail_spread_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_200_vol_tail_spread_zscore_21d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 21)

def vts_201_vol_tail_spread_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_201_vol_tail_spread_rank_21d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 21)

def vts_202_vol_tail_spread_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_202_vol_tail_spread_lvl_63d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 63)

def vts_203_vol_tail_spread_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_203_vol_tail_spread_zscore_63d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 63)

def vts_204_vol_tail_spread_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_204_vol_tail_spread_rank_63d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 63)

def vts_205_vol_tail_spread_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_205_vol_tail_spread_lvl_126d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 126)

def vts_206_vol_tail_spread_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_206_vol_tail_spread_zscore_126d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 126)

def vts_207_vol_tail_spread_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_207_vol_tail_spread_rank_126d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 126)

def vts_208_vol_tail_spread_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_208_vol_tail_spread_lvl_252d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 252)

def vts_209_vol_tail_spread_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_209_vol_tail_spread_zscore_252d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 252)

def vts_210_vol_tail_spread_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_210_vol_tail_spread_rank_252d
    ECONOMIC RATIONALE: Volatility of the tails relative to the mean.
    """
    base = close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 252)

def vts_211_vol_structural_stability_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_211_vol_structural_stability_lvl_5d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 5)

def vts_212_vol_structural_stability_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_212_vol_structural_stability_zscore_5d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 5)

def vts_213_vol_structural_stability_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_213_vol_structural_stability_rank_5d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 5)

def vts_214_vol_structural_stability_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_214_vol_structural_stability_lvl_21d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 21)

def vts_215_vol_structural_stability_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_215_vol_structural_stability_zscore_21d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 21)

def vts_216_vol_structural_stability_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_216_vol_structural_stability_rank_21d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 21)

def vts_217_vol_structural_stability_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_217_vol_structural_stability_lvl_63d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 63)

def vts_218_vol_structural_stability_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_218_vol_structural_stability_zscore_63d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 63)

def vts_219_vol_structural_stability_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_219_vol_structural_stability_rank_63d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 63)

def vts_220_vol_structural_stability_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_220_vol_structural_stability_lvl_126d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 126)

def vts_221_vol_structural_stability_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_221_vol_structural_stability_zscore_126d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 126)

def vts_222_vol_structural_stability_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_222_vol_structural_stability_rank_126d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 126)

def vts_223_vol_structural_stability_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_223_vol_structural_stability_lvl_252d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 252)

def vts_224_vol_structural_stability_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_224_vol_structural_stability_zscore_252d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 252)

def vts_225_vol_structural_stability_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_225_vol_structural_stability_rank_252d
    ECONOMIC RATIONALE: Stability of the long-term volatility structure.
    """
    base = close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V115_REGISTRY_2 = {
    "vts_121_vol_acceleration_lvl_5d": {"inputs": ["close"], "func": vts_121_vol_acceleration_lvl_5d},
    "vts_122_vol_acceleration_zscore_5d": {"inputs": ["close"], "func": vts_122_vol_acceleration_zscore_5d},
    "vts_123_vol_acceleration_rank_5d": {"inputs": ["close"], "func": vts_123_vol_acceleration_rank_5d},
    "vts_124_vol_acceleration_lvl_21d": {"inputs": ["close"], "func": vts_124_vol_acceleration_lvl_21d},
    "vts_125_vol_acceleration_zscore_21d": {"inputs": ["close"], "func": vts_125_vol_acceleration_zscore_21d},
    "vts_126_vol_acceleration_rank_21d": {"inputs": ["close"], "func": vts_126_vol_acceleration_rank_21d},
    "vts_127_vol_acceleration_lvl_63d": {"inputs": ["close"], "func": vts_127_vol_acceleration_lvl_63d},
    "vts_128_vol_acceleration_zscore_63d": {"inputs": ["close"], "func": vts_128_vol_acceleration_zscore_63d},
    "vts_129_vol_acceleration_rank_63d": {"inputs": ["close"], "func": vts_129_vol_acceleration_rank_63d},
    "vts_130_vol_acceleration_lvl_126d": {"inputs": ["close"], "func": vts_130_vol_acceleration_lvl_126d},
    "vts_131_vol_acceleration_zscore_126d": {"inputs": ["close"], "func": vts_131_vol_acceleration_zscore_126d},
    "vts_132_vol_acceleration_rank_126d": {"inputs": ["close"], "func": vts_132_vol_acceleration_rank_126d},
    "vts_133_vol_acceleration_lvl_252d": {"inputs": ["close"], "func": vts_133_vol_acceleration_lvl_252d},
    "vts_134_vol_acceleration_zscore_252d": {"inputs": ["close"], "func": vts_134_vol_acceleration_zscore_252d},
    "vts_135_vol_acceleration_rank_252d": {"inputs": ["close"], "func": vts_135_vol_acceleration_rank_252d},
    "vts_136_vol_of_vol_lvl_5d": {"inputs": ["close"], "func": vts_136_vol_of_vol_lvl_5d},
    "vts_137_vol_of_vol_zscore_5d": {"inputs": ["close"], "func": vts_137_vol_of_vol_zscore_5d},
    "vts_138_vol_of_vol_rank_5d": {"inputs": ["close"], "func": vts_138_vol_of_vol_rank_5d},
    "vts_139_vol_of_vol_lvl_21d": {"inputs": ["close"], "func": vts_139_vol_of_vol_lvl_21d},
    "vts_140_vol_of_vol_zscore_21d": {"inputs": ["close"], "func": vts_140_vol_of_vol_zscore_21d},
    "vts_141_vol_of_vol_rank_21d": {"inputs": ["close"], "func": vts_141_vol_of_vol_rank_21d},
    "vts_142_vol_of_vol_lvl_63d": {"inputs": ["close"], "func": vts_142_vol_of_vol_lvl_63d},
    "vts_143_vol_of_vol_zscore_63d": {"inputs": ["close"], "func": vts_143_vol_of_vol_zscore_63d},
    "vts_144_vol_of_vol_rank_63d": {"inputs": ["close"], "func": vts_144_vol_of_vol_rank_63d},
    "vts_145_vol_of_vol_lvl_126d": {"inputs": ["close"], "func": vts_145_vol_of_vol_lvl_126d},
    "vts_146_vol_of_vol_zscore_126d": {"inputs": ["close"], "func": vts_146_vol_of_vol_zscore_126d},
    "vts_147_vol_of_vol_rank_126d": {"inputs": ["close"], "func": vts_147_vol_of_vol_rank_126d},
    "vts_148_vol_of_vol_lvl_252d": {"inputs": ["close"], "func": vts_148_vol_of_vol_lvl_252d},
    "vts_149_vol_of_vol_zscore_252d": {"inputs": ["close"], "func": vts_149_vol_of_vol_zscore_252d},
    "vts_150_vol_of_vol_rank_252d": {"inputs": ["close"], "func": vts_150_vol_of_vol_rank_252d},
    "vts_151_vol_decay_lvl_5d": {"inputs": ["close"], "func": vts_151_vol_decay_lvl_5d},
    "vts_152_vol_decay_zscore_5d": {"inputs": ["close"], "func": vts_152_vol_decay_zscore_5d},
    "vts_153_vol_decay_rank_5d": {"inputs": ["close"], "func": vts_153_vol_decay_rank_5d},
    "vts_154_vol_decay_lvl_21d": {"inputs": ["close"], "func": vts_154_vol_decay_lvl_21d},
    "vts_155_vol_decay_zscore_21d": {"inputs": ["close"], "func": vts_155_vol_decay_zscore_21d},
    "vts_156_vol_decay_rank_21d": {"inputs": ["close"], "func": vts_156_vol_decay_rank_21d},
    "vts_157_vol_decay_lvl_63d": {"inputs": ["close"], "func": vts_157_vol_decay_lvl_63d},
    "vts_158_vol_decay_zscore_63d": {"inputs": ["close"], "func": vts_158_vol_decay_zscore_63d},
    "vts_159_vol_decay_rank_63d": {"inputs": ["close"], "func": vts_159_vol_decay_rank_63d},
    "vts_160_vol_decay_lvl_126d": {"inputs": ["close"], "func": vts_160_vol_decay_lvl_126d},
    "vts_161_vol_decay_zscore_126d": {"inputs": ["close"], "func": vts_161_vol_decay_zscore_126d},
    "vts_162_vol_decay_rank_126d": {"inputs": ["close"], "func": vts_162_vol_decay_rank_126d},
    "vts_163_vol_decay_lvl_252d": {"inputs": ["close"], "func": vts_163_vol_decay_lvl_252d},
    "vts_164_vol_decay_zscore_252d": {"inputs": ["close"], "func": vts_164_vol_decay_zscore_252d},
    "vts_165_vol_decay_rank_252d": {"inputs": ["close"], "func": vts_165_vol_decay_rank_252d},
    "vts_166_vol_term_inversion_lvl_5d": {"inputs": ["close"], "func": vts_166_vol_term_inversion_lvl_5d},
    "vts_167_vol_term_inversion_zscore_5d": {"inputs": ["close"], "func": vts_167_vol_term_inversion_zscore_5d},
    "vts_168_vol_term_inversion_rank_5d": {"inputs": ["close"], "func": vts_168_vol_term_inversion_rank_5d},
    "vts_169_vol_term_inversion_lvl_21d": {"inputs": ["close"], "func": vts_169_vol_term_inversion_lvl_21d},
    "vts_170_vol_term_inversion_zscore_21d": {"inputs": ["close"], "func": vts_170_vol_term_inversion_zscore_21d},
    "vts_171_vol_term_inversion_rank_21d": {"inputs": ["close"], "func": vts_171_vol_term_inversion_rank_21d},
    "vts_172_vol_term_inversion_lvl_63d": {"inputs": ["close"], "func": vts_172_vol_term_inversion_lvl_63d},
    "vts_173_vol_term_inversion_zscore_63d": {"inputs": ["close"], "func": vts_173_vol_term_inversion_zscore_63d},
    "vts_174_vol_term_inversion_rank_63d": {"inputs": ["close"], "func": vts_174_vol_term_inversion_rank_63d},
    "vts_175_vol_term_inversion_lvl_126d": {"inputs": ["close"], "func": vts_175_vol_term_inversion_lvl_126d},
    "vts_176_vol_term_inversion_zscore_126d": {"inputs": ["close"], "func": vts_176_vol_term_inversion_zscore_126d},
    "vts_177_vol_term_inversion_rank_126d": {"inputs": ["close"], "func": vts_177_vol_term_inversion_rank_126d},
    "vts_178_vol_term_inversion_lvl_252d": {"inputs": ["close"], "func": vts_178_vol_term_inversion_lvl_252d},
    "vts_179_vol_term_inversion_zscore_252d": {"inputs": ["close"], "func": vts_179_vol_term_inversion_zscore_252d},
    "vts_180_vol_term_inversion_rank_252d": {"inputs": ["close"], "func": vts_180_vol_term_inversion_rank_252d},
    "vts_181_vol_peak_dist_lvl_5d": {"inputs": ["close"], "func": vts_181_vol_peak_dist_lvl_5d},
    "vts_182_vol_peak_dist_zscore_5d": {"inputs": ["close"], "func": vts_182_vol_peak_dist_zscore_5d},
    "vts_183_vol_peak_dist_rank_5d": {"inputs": ["close"], "func": vts_183_vol_peak_dist_rank_5d},
    "vts_184_vol_peak_dist_lvl_21d": {"inputs": ["close"], "func": vts_184_vol_peak_dist_lvl_21d},
    "vts_185_vol_peak_dist_zscore_21d": {"inputs": ["close"], "func": vts_185_vol_peak_dist_zscore_21d},
    "vts_186_vol_peak_dist_rank_21d": {"inputs": ["close"], "func": vts_186_vol_peak_dist_rank_21d},
    "vts_187_vol_peak_dist_lvl_63d": {"inputs": ["close"], "func": vts_187_vol_peak_dist_lvl_63d},
    "vts_188_vol_peak_dist_zscore_63d": {"inputs": ["close"], "func": vts_188_vol_peak_dist_zscore_63d},
    "vts_189_vol_peak_dist_rank_63d": {"inputs": ["close"], "func": vts_189_vol_peak_dist_rank_63d},
    "vts_190_vol_peak_dist_lvl_126d": {"inputs": ["close"], "func": vts_190_vol_peak_dist_lvl_126d},
    "vts_191_vol_peak_dist_zscore_126d": {"inputs": ["close"], "func": vts_191_vol_peak_dist_zscore_126d},
    "vts_192_vol_peak_dist_rank_126d": {"inputs": ["close"], "func": vts_192_vol_peak_dist_rank_126d},
    "vts_193_vol_peak_dist_lvl_252d": {"inputs": ["close"], "func": vts_193_vol_peak_dist_lvl_252d},
    "vts_194_vol_peak_dist_zscore_252d": {"inputs": ["close"], "func": vts_194_vol_peak_dist_zscore_252d},
    "vts_195_vol_peak_dist_rank_252d": {"inputs": ["close"], "func": vts_195_vol_peak_dist_rank_252d},
    "vts_196_vol_tail_spread_lvl_5d": {"inputs": ["close"], "func": vts_196_vol_tail_spread_lvl_5d},
    "vts_197_vol_tail_spread_zscore_5d": {"inputs": ["close"], "func": vts_197_vol_tail_spread_zscore_5d},
    "vts_198_vol_tail_spread_rank_5d": {"inputs": ["close"], "func": vts_198_vol_tail_spread_rank_5d},
    "vts_199_vol_tail_spread_lvl_21d": {"inputs": ["close"], "func": vts_199_vol_tail_spread_lvl_21d},
    "vts_200_vol_tail_spread_zscore_21d": {"inputs": ["close"], "func": vts_200_vol_tail_spread_zscore_21d},
    "vts_201_vol_tail_spread_rank_21d": {"inputs": ["close"], "func": vts_201_vol_tail_spread_rank_21d},
    "vts_202_vol_tail_spread_lvl_63d": {"inputs": ["close"], "func": vts_202_vol_tail_spread_lvl_63d},
    "vts_203_vol_tail_spread_zscore_63d": {"inputs": ["close"], "func": vts_203_vol_tail_spread_zscore_63d},
    "vts_204_vol_tail_spread_rank_63d": {"inputs": ["close"], "func": vts_204_vol_tail_spread_rank_63d},
    "vts_205_vol_tail_spread_lvl_126d": {"inputs": ["close"], "func": vts_205_vol_tail_spread_lvl_126d},
    "vts_206_vol_tail_spread_zscore_126d": {"inputs": ["close"], "func": vts_206_vol_tail_spread_zscore_126d},
    "vts_207_vol_tail_spread_rank_126d": {"inputs": ["close"], "func": vts_207_vol_tail_spread_rank_126d},
    "vts_208_vol_tail_spread_lvl_252d": {"inputs": ["close"], "func": vts_208_vol_tail_spread_lvl_252d},
    "vts_209_vol_tail_spread_zscore_252d": {"inputs": ["close"], "func": vts_209_vol_tail_spread_zscore_252d},
    "vts_210_vol_tail_spread_rank_252d": {"inputs": ["close"], "func": vts_210_vol_tail_spread_rank_252d},
    "vts_211_vol_structural_stability_lvl_5d": {"inputs": ["close"], "func": vts_211_vol_structural_stability_lvl_5d},
    "vts_212_vol_structural_stability_zscore_5d": {"inputs": ["close"], "func": vts_212_vol_structural_stability_zscore_5d},
    "vts_213_vol_structural_stability_rank_5d": {"inputs": ["close"], "func": vts_213_vol_structural_stability_rank_5d},
    "vts_214_vol_structural_stability_lvl_21d": {"inputs": ["close"], "func": vts_214_vol_structural_stability_lvl_21d},
    "vts_215_vol_structural_stability_zscore_21d": {"inputs": ["close"], "func": vts_215_vol_structural_stability_zscore_21d},
    "vts_216_vol_structural_stability_rank_21d": {"inputs": ["close"], "func": vts_216_vol_structural_stability_rank_21d},
    "vts_217_vol_structural_stability_lvl_63d": {"inputs": ["close"], "func": vts_217_vol_structural_stability_lvl_63d},
    "vts_218_vol_structural_stability_zscore_63d": {"inputs": ["close"], "func": vts_218_vol_structural_stability_zscore_63d},
    "vts_219_vol_structural_stability_rank_63d": {"inputs": ["close"], "func": vts_219_vol_structural_stability_rank_63d},
    "vts_220_vol_structural_stability_lvl_126d": {"inputs": ["close"], "func": vts_220_vol_structural_stability_lvl_126d},
    "vts_221_vol_structural_stability_zscore_126d": {"inputs": ["close"], "func": vts_221_vol_structural_stability_zscore_126d},
    "vts_222_vol_structural_stability_rank_126d": {"inputs": ["close"], "func": vts_222_vol_structural_stability_rank_126d},
    "vts_223_vol_structural_stability_lvl_252d": {"inputs": ["close"], "func": vts_223_vol_structural_stability_lvl_252d},
    "vts_224_vol_structural_stability_zscore_252d": {"inputs": ["close"], "func": vts_224_vol_structural_stability_zscore_252d},
    "vts_225_vol_structural_stability_rank_252d": {"inputs": ["close"], "func": vts_225_vol_structural_stability_rank_252d},
}
