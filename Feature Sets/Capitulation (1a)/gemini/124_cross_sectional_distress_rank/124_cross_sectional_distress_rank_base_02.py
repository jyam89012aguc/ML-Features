"""
124_cross_sectional_distress_rank — Base Features Part 2
Domain: cross_sectional_distress_rank
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

def csdr_121_xs_recovery_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_121_xs_recovery_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rolling_mean(base, 5)

def csdr_122_xs_recovery_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_122_xs_recovery_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _zscore_rolling(base, 5)

def csdr_123_xs_recovery_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_123_xs_recovery_rank_rank_5d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rank_pct(base, 5)

def csdr_124_xs_recovery_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_124_xs_recovery_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rolling_mean(base, 21)

def csdr_125_xs_recovery_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_125_xs_recovery_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _zscore_rolling(base, 21)

def csdr_126_xs_recovery_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_126_xs_recovery_rank_rank_21d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rank_pct(base, 21)

def csdr_127_xs_recovery_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_127_xs_recovery_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rolling_mean(base, 63)

def csdr_128_xs_recovery_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_128_xs_recovery_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _zscore_rolling(base, 63)

def csdr_129_xs_recovery_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_129_xs_recovery_rank_rank_63d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rank_pct(base, 63)

def csdr_130_xs_recovery_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_130_xs_recovery_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rolling_mean(base, 126)

def csdr_131_xs_recovery_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_131_xs_recovery_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _zscore_rolling(base, 126)

def csdr_132_xs_recovery_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_132_xs_recovery_rank_rank_126d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rank_pct(base, 126)

def csdr_133_xs_recovery_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_133_xs_recovery_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rolling_mean(base, 252)

def csdr_134_xs_recovery_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_134_xs_recovery_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _zscore_rolling(base, 252)

def csdr_135_xs_recovery_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_135_xs_recovery_rank_rank_252d
    ECONOMIC RATIONALE: Rank of recovery from annual lows.
    """
    base = _rank_pct(close / close.rolling(252).min() - 1, 252)
    return _rank_pct(base, 252)

def csdr_136_xs_liquidity_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_136_xs_liquidity_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rolling_mean(base, 5)

def csdr_137_xs_liquidity_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_137_xs_liquidity_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _zscore_rolling(base, 5)

def csdr_138_xs_liquidity_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_138_xs_liquidity_rank_rank_5d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rank_pct(base, 5)

def csdr_139_xs_liquidity_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_139_xs_liquidity_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rolling_mean(base, 21)

def csdr_140_xs_liquidity_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_140_xs_liquidity_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _zscore_rolling(base, 21)

def csdr_141_xs_liquidity_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_141_xs_liquidity_rank_rank_21d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rank_pct(base, 21)

def csdr_142_xs_liquidity_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_142_xs_liquidity_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rolling_mean(base, 63)

def csdr_143_xs_liquidity_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_143_xs_liquidity_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _zscore_rolling(base, 63)

def csdr_144_xs_liquidity_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_144_xs_liquidity_rank_rank_63d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rank_pct(base, 63)

def csdr_145_xs_liquidity_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_145_xs_liquidity_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rolling_mean(base, 126)

def csdr_146_xs_liquidity_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_146_xs_liquidity_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _zscore_rolling(base, 126)

def csdr_147_xs_liquidity_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_147_xs_liquidity_rank_rank_126d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rank_pct(base, 126)

def csdr_148_xs_liquidity_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_148_xs_liquidity_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rolling_mean(base, 252)

def csdr_149_xs_liquidity_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_149_xs_liquidity_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _zscore_rolling(base, 252)

def csdr_150_xs_liquidity_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_150_xs_liquidity_rank_rank_252d
    ECONOMIC RATIONALE: Rank of dollar turnover.
    """
    base = _rank_pct(volume * close, 252)
    return _rank_pct(base, 252)

def csdr_151_xs_tail_risk_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_151_xs_tail_risk_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rolling_mean(base, 5)

def csdr_152_xs_tail_risk_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_152_xs_tail_risk_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _zscore_rolling(base, 5)

def csdr_153_xs_tail_risk_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_153_xs_tail_risk_rank_rank_5d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rank_pct(base, 5)

def csdr_154_xs_tail_risk_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_154_xs_tail_risk_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rolling_mean(base, 21)

def csdr_155_xs_tail_risk_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_155_xs_tail_risk_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _zscore_rolling(base, 21)

def csdr_156_xs_tail_risk_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_156_xs_tail_risk_rank_rank_21d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rank_pct(base, 21)

def csdr_157_xs_tail_risk_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_157_xs_tail_risk_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rolling_mean(base, 63)

def csdr_158_xs_tail_risk_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_158_xs_tail_risk_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _zscore_rolling(base, 63)

def csdr_159_xs_tail_risk_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_159_xs_tail_risk_rank_rank_63d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rank_pct(base, 63)

def csdr_160_xs_tail_risk_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_160_xs_tail_risk_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rolling_mean(base, 126)

def csdr_161_xs_tail_risk_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_161_xs_tail_risk_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _zscore_rolling(base, 126)

def csdr_162_xs_tail_risk_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_162_xs_tail_risk_rank_rank_126d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rank_pct(base, 126)

def csdr_163_xs_tail_risk_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_163_xs_tail_risk_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rolling_mean(base, 252)

def csdr_164_xs_tail_risk_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_164_xs_tail_risk_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _zscore_rolling(base, 252)

def csdr_165_xs_tail_risk_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_165_xs_tail_risk_rank_rank_252d
    ECONOMIC RATIONALE: Rank of tail risk severity.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)
    return _rank_pct(base, 252)

def csdr_166_xs_asymmetry_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_166_xs_asymmetry_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rolling_mean(base, 5)

def csdr_167_xs_asymmetry_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_167_xs_asymmetry_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _zscore_rolling(base, 5)

def csdr_168_xs_asymmetry_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_168_xs_asymmetry_rank_rank_5d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rank_pct(base, 5)

def csdr_169_xs_asymmetry_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_169_xs_asymmetry_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rolling_mean(base, 21)

def csdr_170_xs_asymmetry_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_170_xs_asymmetry_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _zscore_rolling(base, 21)

def csdr_171_xs_asymmetry_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_171_xs_asymmetry_rank_rank_21d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rank_pct(base, 21)

def csdr_172_xs_asymmetry_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_172_xs_asymmetry_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rolling_mean(base, 63)

def csdr_173_xs_asymmetry_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_173_xs_asymmetry_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _zscore_rolling(base, 63)

def csdr_174_xs_asymmetry_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_174_xs_asymmetry_rank_rank_63d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rank_pct(base, 63)

def csdr_175_xs_asymmetry_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_175_xs_asymmetry_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rolling_mean(base, 126)

def csdr_176_xs_asymmetry_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_176_xs_asymmetry_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _zscore_rolling(base, 126)

def csdr_177_xs_asymmetry_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_177_xs_asymmetry_rank_rank_126d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rank_pct(base, 126)

def csdr_178_xs_asymmetry_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_178_xs_asymmetry_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rolling_mean(base, 252)

def csdr_179_xs_asymmetry_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_179_xs_asymmetry_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _zscore_rolling(base, 252)

def csdr_180_xs_asymmetry_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_180_xs_asymmetry_rank_rank_252d
    ECONOMIC RATIONALE: Rank of return skewness.
    """
    base = _rank_pct(close.pct_change(1).rolling(252).skew(), 252)
    return _rank_pct(base, 252)

def csdr_181_xs_persistence_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_181_xs_persistence_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 5)

def csdr_182_xs_persistence_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_182_xs_persistence_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 5)

def csdr_183_xs_persistence_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_183_xs_persistence_rank_rank_5d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 5)

def csdr_184_xs_persistence_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_184_xs_persistence_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 21)

def csdr_185_xs_persistence_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_185_xs_persistence_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 21)

def csdr_186_xs_persistence_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_186_xs_persistence_rank_rank_21d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 21)

def csdr_187_xs_persistence_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_187_xs_persistence_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 63)

def csdr_188_xs_persistence_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_188_xs_persistence_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 63)

def csdr_189_xs_persistence_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_189_xs_persistence_rank_rank_63d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 63)

def csdr_190_xs_persistence_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_190_xs_persistence_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 126)

def csdr_191_xs_persistence_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_191_xs_persistence_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 126)

def csdr_192_xs_persistence_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_192_xs_persistence_rank_rank_126d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 126)

def csdr_193_xs_persistence_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_193_xs_persistence_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 252)

def csdr_194_xs_persistence_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_194_xs_persistence_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 252)

def csdr_195_xs_persistence_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_195_xs_persistence_rank_rank_252d
    ECONOMIC RATIONALE: Rank of return autocorrelation.
    """
    base = _rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 252)

def csdr_196_xs_gap_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_196_xs_gap_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rolling_mean(base, 5)

def csdr_197_xs_gap_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_197_xs_gap_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _zscore_rolling(base, 5)

def csdr_198_xs_gap_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_198_xs_gap_rank_rank_5d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rank_pct(base, 5)

def csdr_199_xs_gap_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_199_xs_gap_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rolling_mean(base, 21)

def csdr_200_xs_gap_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_200_xs_gap_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _zscore_rolling(base, 21)

def csdr_201_xs_gap_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_201_xs_gap_rank_rank_21d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rank_pct(base, 21)

def csdr_202_xs_gap_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_202_xs_gap_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rolling_mean(base, 63)

def csdr_203_xs_gap_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_203_xs_gap_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _zscore_rolling(base, 63)

def csdr_204_xs_gap_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_204_xs_gap_rank_rank_63d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rank_pct(base, 63)

def csdr_205_xs_gap_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_205_xs_gap_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rolling_mean(base, 126)

def csdr_206_xs_gap_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_206_xs_gap_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _zscore_rolling(base, 126)

def csdr_207_xs_gap_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_207_xs_gap_rank_rank_126d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rank_pct(base, 126)

def csdr_208_xs_gap_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_208_xs_gap_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rolling_mean(base, 252)

def csdr_209_xs_gap_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_209_xs_gap_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _zscore_rolling(base, 252)

def csdr_210_xs_gap_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_210_xs_gap_rank_rank_252d
    ECONOMIC RATIONALE: Rank of overnight gap magnitude.
    """
    base = _rank_pct(abs(open/close.shift(1)-1), 252)
    return _rank_pct(base, 252)

def csdr_211_xs_composite_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_211_xs_composite_rank_lvl_5d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rolling_mean(base, 5)

def csdr_212_xs_composite_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_212_xs_composite_rank_zscore_5d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _zscore_rolling(base, 5)

def csdr_213_xs_composite_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_213_xs_composite_rank_rank_5d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rank_pct(base, 5)

def csdr_214_xs_composite_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_214_xs_composite_rank_lvl_21d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rolling_mean(base, 21)

def csdr_215_xs_composite_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_215_xs_composite_rank_zscore_21d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _zscore_rolling(base, 21)

def csdr_216_xs_composite_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_216_xs_composite_rank_rank_21d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rank_pct(base, 21)

def csdr_217_xs_composite_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_217_xs_composite_rank_lvl_63d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rolling_mean(base, 63)

def csdr_218_xs_composite_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_218_xs_composite_rank_zscore_63d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _zscore_rolling(base, 63)

def csdr_219_xs_composite_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_219_xs_composite_rank_rank_63d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rank_pct(base, 63)

def csdr_220_xs_composite_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_220_xs_composite_rank_lvl_126d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rolling_mean(base, 126)

def csdr_221_xs_composite_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_221_xs_composite_rank_zscore_126d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _zscore_rolling(base, 126)

def csdr_222_xs_composite_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_222_xs_composite_rank_rank_126d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rank_pct(base, 126)

def csdr_223_xs_composite_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_223_xs_composite_rank_lvl_252d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rolling_mean(base, 252)

def csdr_224_xs_composite_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_224_xs_composite_rank_zscore_252d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _zscore_rolling(base, 252)

def csdr_225_xs_composite_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_225_xs_composite_rank_rank_252d
    ECONOMIC RATIONALE: Average of momentum and drawdown ranks.
    """
    base = (_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V124_REGISTRY_2 = {
    "csdr_121_xs_recovery_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_121_xs_recovery_rank_lvl_5d},
    "csdr_122_xs_recovery_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_122_xs_recovery_rank_zscore_5d},
    "csdr_123_xs_recovery_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_123_xs_recovery_rank_rank_5d},
    "csdr_124_xs_recovery_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_124_xs_recovery_rank_lvl_21d},
    "csdr_125_xs_recovery_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_125_xs_recovery_rank_zscore_21d},
    "csdr_126_xs_recovery_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_126_xs_recovery_rank_rank_21d},
    "csdr_127_xs_recovery_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_127_xs_recovery_rank_lvl_63d},
    "csdr_128_xs_recovery_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_128_xs_recovery_rank_zscore_63d},
    "csdr_129_xs_recovery_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_129_xs_recovery_rank_rank_63d},
    "csdr_130_xs_recovery_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_130_xs_recovery_rank_lvl_126d},
    "csdr_131_xs_recovery_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_131_xs_recovery_rank_zscore_126d},
    "csdr_132_xs_recovery_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_132_xs_recovery_rank_rank_126d},
    "csdr_133_xs_recovery_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_133_xs_recovery_rank_lvl_252d},
    "csdr_134_xs_recovery_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_134_xs_recovery_rank_zscore_252d},
    "csdr_135_xs_recovery_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_135_xs_recovery_rank_rank_252d},
    "csdr_136_xs_liquidity_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_136_xs_liquidity_rank_lvl_5d},
    "csdr_137_xs_liquidity_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_137_xs_liquidity_rank_zscore_5d},
    "csdr_138_xs_liquidity_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_138_xs_liquidity_rank_rank_5d},
    "csdr_139_xs_liquidity_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_139_xs_liquidity_rank_lvl_21d},
    "csdr_140_xs_liquidity_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_140_xs_liquidity_rank_zscore_21d},
    "csdr_141_xs_liquidity_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_141_xs_liquidity_rank_rank_21d},
    "csdr_142_xs_liquidity_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_142_xs_liquidity_rank_lvl_63d},
    "csdr_143_xs_liquidity_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_143_xs_liquidity_rank_zscore_63d},
    "csdr_144_xs_liquidity_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_144_xs_liquidity_rank_rank_63d},
    "csdr_145_xs_liquidity_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_145_xs_liquidity_rank_lvl_126d},
    "csdr_146_xs_liquidity_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_146_xs_liquidity_rank_zscore_126d},
    "csdr_147_xs_liquidity_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_147_xs_liquidity_rank_rank_126d},
    "csdr_148_xs_liquidity_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_148_xs_liquidity_rank_lvl_252d},
    "csdr_149_xs_liquidity_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_149_xs_liquidity_rank_zscore_252d},
    "csdr_150_xs_liquidity_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_150_xs_liquidity_rank_rank_252d},
    "csdr_151_xs_tail_risk_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_151_xs_tail_risk_rank_lvl_5d},
    "csdr_152_xs_tail_risk_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_152_xs_tail_risk_rank_zscore_5d},
    "csdr_153_xs_tail_risk_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_153_xs_tail_risk_rank_rank_5d},
    "csdr_154_xs_tail_risk_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_154_xs_tail_risk_rank_lvl_21d},
    "csdr_155_xs_tail_risk_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_155_xs_tail_risk_rank_zscore_21d},
    "csdr_156_xs_tail_risk_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_156_xs_tail_risk_rank_rank_21d},
    "csdr_157_xs_tail_risk_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_157_xs_tail_risk_rank_lvl_63d},
    "csdr_158_xs_tail_risk_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_158_xs_tail_risk_rank_zscore_63d},
    "csdr_159_xs_tail_risk_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_159_xs_tail_risk_rank_rank_63d},
    "csdr_160_xs_tail_risk_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_160_xs_tail_risk_rank_lvl_126d},
    "csdr_161_xs_tail_risk_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_161_xs_tail_risk_rank_zscore_126d},
    "csdr_162_xs_tail_risk_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_162_xs_tail_risk_rank_rank_126d},
    "csdr_163_xs_tail_risk_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_163_xs_tail_risk_rank_lvl_252d},
    "csdr_164_xs_tail_risk_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_164_xs_tail_risk_rank_zscore_252d},
    "csdr_165_xs_tail_risk_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_165_xs_tail_risk_rank_rank_252d},
    "csdr_166_xs_asymmetry_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_166_xs_asymmetry_rank_lvl_5d},
    "csdr_167_xs_asymmetry_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_167_xs_asymmetry_rank_zscore_5d},
    "csdr_168_xs_asymmetry_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_168_xs_asymmetry_rank_rank_5d},
    "csdr_169_xs_asymmetry_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_169_xs_asymmetry_rank_lvl_21d},
    "csdr_170_xs_asymmetry_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_170_xs_asymmetry_rank_zscore_21d},
    "csdr_171_xs_asymmetry_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_171_xs_asymmetry_rank_rank_21d},
    "csdr_172_xs_asymmetry_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_172_xs_asymmetry_rank_lvl_63d},
    "csdr_173_xs_asymmetry_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_173_xs_asymmetry_rank_zscore_63d},
    "csdr_174_xs_asymmetry_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_174_xs_asymmetry_rank_rank_63d},
    "csdr_175_xs_asymmetry_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_175_xs_asymmetry_rank_lvl_126d},
    "csdr_176_xs_asymmetry_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_176_xs_asymmetry_rank_zscore_126d},
    "csdr_177_xs_asymmetry_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_177_xs_asymmetry_rank_rank_126d},
    "csdr_178_xs_asymmetry_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_178_xs_asymmetry_rank_lvl_252d},
    "csdr_179_xs_asymmetry_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_179_xs_asymmetry_rank_zscore_252d},
    "csdr_180_xs_asymmetry_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_180_xs_asymmetry_rank_rank_252d},
    "csdr_181_xs_persistence_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_181_xs_persistence_rank_lvl_5d},
    "csdr_182_xs_persistence_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_182_xs_persistence_rank_zscore_5d},
    "csdr_183_xs_persistence_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_183_xs_persistence_rank_rank_5d},
    "csdr_184_xs_persistence_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_184_xs_persistence_rank_lvl_21d},
    "csdr_185_xs_persistence_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_185_xs_persistence_rank_zscore_21d},
    "csdr_186_xs_persistence_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_186_xs_persistence_rank_rank_21d},
    "csdr_187_xs_persistence_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_187_xs_persistence_rank_lvl_63d},
    "csdr_188_xs_persistence_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_188_xs_persistence_rank_zscore_63d},
    "csdr_189_xs_persistence_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_189_xs_persistence_rank_rank_63d},
    "csdr_190_xs_persistence_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_190_xs_persistence_rank_lvl_126d},
    "csdr_191_xs_persistence_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_191_xs_persistence_rank_zscore_126d},
    "csdr_192_xs_persistence_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_192_xs_persistence_rank_rank_126d},
    "csdr_193_xs_persistence_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_193_xs_persistence_rank_lvl_252d},
    "csdr_194_xs_persistence_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_194_xs_persistence_rank_zscore_252d},
    "csdr_195_xs_persistence_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_195_xs_persistence_rank_rank_252d},
    "csdr_196_xs_gap_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_196_xs_gap_rank_lvl_5d},
    "csdr_197_xs_gap_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_197_xs_gap_rank_zscore_5d},
    "csdr_198_xs_gap_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_198_xs_gap_rank_rank_5d},
    "csdr_199_xs_gap_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_199_xs_gap_rank_lvl_21d},
    "csdr_200_xs_gap_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_200_xs_gap_rank_zscore_21d},
    "csdr_201_xs_gap_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_201_xs_gap_rank_rank_21d},
    "csdr_202_xs_gap_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_202_xs_gap_rank_lvl_63d},
    "csdr_203_xs_gap_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_203_xs_gap_rank_zscore_63d},
    "csdr_204_xs_gap_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_204_xs_gap_rank_rank_63d},
    "csdr_205_xs_gap_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_205_xs_gap_rank_lvl_126d},
    "csdr_206_xs_gap_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_206_xs_gap_rank_zscore_126d},
    "csdr_207_xs_gap_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_207_xs_gap_rank_rank_126d},
    "csdr_208_xs_gap_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_208_xs_gap_rank_lvl_252d},
    "csdr_209_xs_gap_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_209_xs_gap_rank_zscore_252d},
    "csdr_210_xs_gap_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_210_xs_gap_rank_rank_252d},
    "csdr_211_xs_composite_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_211_xs_composite_rank_lvl_5d},
    "csdr_212_xs_composite_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_212_xs_composite_rank_zscore_5d},
    "csdr_213_xs_composite_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_213_xs_composite_rank_rank_5d},
    "csdr_214_xs_composite_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_214_xs_composite_rank_lvl_21d},
    "csdr_215_xs_composite_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_215_xs_composite_rank_zscore_21d},
    "csdr_216_xs_composite_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_216_xs_composite_rank_rank_21d},
    "csdr_217_xs_composite_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_217_xs_composite_rank_lvl_63d},
    "csdr_218_xs_composite_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_218_xs_composite_rank_zscore_63d},
    "csdr_219_xs_composite_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_219_xs_composite_rank_rank_63d},
    "csdr_220_xs_composite_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_220_xs_composite_rank_lvl_126d},
    "csdr_221_xs_composite_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_221_xs_composite_rank_zscore_126d},
    "csdr_222_xs_composite_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_222_xs_composite_rank_rank_126d},
    "csdr_223_xs_composite_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_223_xs_composite_rank_lvl_252d},
    "csdr_224_xs_composite_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_224_xs_composite_rank_zscore_252d},
    "csdr_225_xs_composite_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_225_xs_composite_rank_rank_252d},
}
