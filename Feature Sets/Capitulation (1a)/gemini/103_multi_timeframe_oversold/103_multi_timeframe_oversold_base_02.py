"""
103_multi_timeframe_oversold — Base Features Part 2
Domain: multi_timeframe_oversold
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

def mtfo_121_stoch_rsi_hybrid_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_121_stoch_rsi_hybrid_lvl_5d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rolling_mean(base, 5)

def mtfo_122_stoch_rsi_hybrid_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_122_stoch_rsi_hybrid_zscore_5d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _zscore_rolling(base, 5)

def mtfo_123_stoch_rsi_hybrid_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_123_stoch_rsi_hybrid_rank_5d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rank_pct(base, 5)

def mtfo_124_stoch_rsi_hybrid_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_124_stoch_rsi_hybrid_lvl_21d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rolling_mean(base, 21)

def mtfo_125_stoch_rsi_hybrid_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_125_stoch_rsi_hybrid_zscore_21d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _zscore_rolling(base, 21)

def mtfo_126_stoch_rsi_hybrid_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_126_stoch_rsi_hybrid_rank_21d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rank_pct(base, 21)

def mtfo_127_stoch_rsi_hybrid_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_127_stoch_rsi_hybrid_lvl_63d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rolling_mean(base, 63)

def mtfo_128_stoch_rsi_hybrid_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_128_stoch_rsi_hybrid_zscore_63d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _zscore_rolling(base, 63)

def mtfo_129_stoch_rsi_hybrid_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_129_stoch_rsi_hybrid_rank_63d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rank_pct(base, 63)

def mtfo_130_stoch_rsi_hybrid_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_130_stoch_rsi_hybrid_lvl_126d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rolling_mean(base, 126)

def mtfo_131_stoch_rsi_hybrid_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_131_stoch_rsi_hybrid_zscore_126d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _zscore_rolling(base, 126)

def mtfo_132_stoch_rsi_hybrid_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_132_stoch_rsi_hybrid_rank_126d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rank_pct(base, 126)

def mtfo_133_stoch_rsi_hybrid_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_133_stoch_rsi_hybrid_lvl_252d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rolling_mean(base, 252)

def mtfo_134_stoch_rsi_hybrid_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_134_stoch_rsi_hybrid_zscore_252d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _zscore_rolling(base, 252)

def mtfo_135_stoch_rsi_hybrid_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_135_stoch_rsi_hybrid_rank_252d
    ECONOMIC RATIONALE: Composite momentum oscillator.
    """
    base = (stoch_k + daily_rsi) / 2
    return _rank_pct(base, 252)

def mtfo_136_williams_r_multi_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_136_williams_r_multi_lvl_5d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mtfo_137_williams_r_multi_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_137_williams_r_multi_zscore_5d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mtfo_138_williams_r_multi_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_138_williams_r_multi_rank_5d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def mtfo_139_williams_r_multi_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_139_williams_r_multi_lvl_21d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mtfo_140_williams_r_multi_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_140_williams_r_multi_zscore_21d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mtfo_141_williams_r_multi_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_141_williams_r_multi_rank_21d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def mtfo_142_williams_r_multi_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_142_williams_r_multi_lvl_63d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mtfo_143_williams_r_multi_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_143_williams_r_multi_zscore_63d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mtfo_144_williams_r_multi_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_144_williams_r_multi_rank_63d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def mtfo_145_williams_r_multi_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_145_williams_r_multi_lvl_126d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mtfo_146_williams_r_multi_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_146_williams_r_multi_zscore_126d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mtfo_147_williams_r_multi_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_147_williams_r_multi_rank_126d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def mtfo_148_williams_r_multi_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_148_williams_r_multi_lvl_252d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mtfo_149_williams_r_multi_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_149_williams_r_multi_zscore_252d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mtfo_150_williams_r_multi_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_150_williams_r_multi_rank_252d
    ECONOMIC RATIONALE: 21-day Williams %R.
    """
    base = (high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def mtfo_151_rsi_acceleration_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_151_rsi_acceleration_lvl_5d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rolling_mean(base, 5)

def mtfo_152_rsi_acceleration_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_152_rsi_acceleration_zscore_5d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _zscore_rolling(base, 5)

def mtfo_153_rsi_acceleration_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_153_rsi_acceleration_rank_5d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rank_pct(base, 5)

def mtfo_154_rsi_acceleration_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_154_rsi_acceleration_lvl_21d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rolling_mean(base, 21)

def mtfo_155_rsi_acceleration_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_155_rsi_acceleration_zscore_21d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _zscore_rolling(base, 21)

def mtfo_156_rsi_acceleration_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_156_rsi_acceleration_rank_21d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rank_pct(base, 21)

def mtfo_157_rsi_acceleration_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_157_rsi_acceleration_lvl_63d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rolling_mean(base, 63)

def mtfo_158_rsi_acceleration_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_158_rsi_acceleration_zscore_63d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _zscore_rolling(base, 63)

def mtfo_159_rsi_acceleration_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_159_rsi_acceleration_rank_63d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rank_pct(base, 63)

def mtfo_160_rsi_acceleration_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_160_rsi_acceleration_lvl_126d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rolling_mean(base, 126)

def mtfo_161_rsi_acceleration_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_161_rsi_acceleration_zscore_126d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _zscore_rolling(base, 126)

def mtfo_162_rsi_acceleration_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_162_rsi_acceleration_rank_126d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rank_pct(base, 126)

def mtfo_163_rsi_acceleration_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_163_rsi_acceleration_lvl_252d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rolling_mean(base, 252)

def mtfo_164_rsi_acceleration_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_164_rsi_acceleration_zscore_252d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _zscore_rolling(base, 252)

def mtfo_165_rsi_acceleration_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_165_rsi_acceleration_rank_252d
    ECONOMIC RATIONALE: Speed of change in RSI levels.
    """
    base = daily_rsi.diff(5)
    return _rank_pct(base, 252)

def mtfo_166_cci_oversold_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_166_cci_oversold_lvl_5d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rolling_mean(base, 5)

def mtfo_167_cci_oversold_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_167_cci_oversold_zscore_5d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _zscore_rolling(base, 5)

def mtfo_168_cci_oversold_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_168_cci_oversold_rank_5d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rank_pct(base, 5)

def mtfo_169_cci_oversold_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_169_cci_oversold_lvl_21d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rolling_mean(base, 21)

def mtfo_170_cci_oversold_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_170_cci_oversold_zscore_21d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _zscore_rolling(base, 21)

def mtfo_171_cci_oversold_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_171_cci_oversold_rank_21d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rank_pct(base, 21)

def mtfo_172_cci_oversold_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_172_cci_oversold_lvl_63d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rolling_mean(base, 63)

def mtfo_173_cci_oversold_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_173_cci_oversold_zscore_63d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _zscore_rolling(base, 63)

def mtfo_174_cci_oversold_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_174_cci_oversold_rank_63d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rank_pct(base, 63)

def mtfo_175_cci_oversold_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_175_cci_oversold_lvl_126d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rolling_mean(base, 126)

def mtfo_176_cci_oversold_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_176_cci_oversold_zscore_126d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _zscore_rolling(base, 126)

def mtfo_177_cci_oversold_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_177_cci_oversold_rank_126d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rank_pct(base, 126)

def mtfo_178_cci_oversold_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_178_cci_oversold_lvl_252d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rolling_mean(base, 252)

def mtfo_179_cci_oversold_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_179_cci_oversold_zscore_252d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _zscore_rolling(base, 252)

def mtfo_180_cci_oversold_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_180_cci_oversold_rank_252d
    ECONOMIC RATIONALE: Commodity Channel Index.
    """
    base = (close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))
    return _rank_pct(base, 252)

def mtfo_181_ultimate_osc_proxy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_181_ultimate_osc_proxy_lvl_5d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rolling_mean(base, 5)

def mtfo_182_ultimate_osc_proxy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_182_ultimate_osc_proxy_zscore_5d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _zscore_rolling(base, 5)

def mtfo_183_ultimate_osc_proxy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_183_ultimate_osc_proxy_rank_5d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rank_pct(base, 5)

def mtfo_184_ultimate_osc_proxy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_184_ultimate_osc_proxy_lvl_21d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rolling_mean(base, 21)

def mtfo_185_ultimate_osc_proxy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_185_ultimate_osc_proxy_zscore_21d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _zscore_rolling(base, 21)

def mtfo_186_ultimate_osc_proxy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_186_ultimate_osc_proxy_rank_21d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rank_pct(base, 21)

def mtfo_187_ultimate_osc_proxy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_187_ultimate_osc_proxy_lvl_63d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rolling_mean(base, 63)

def mtfo_188_ultimate_osc_proxy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_188_ultimate_osc_proxy_zscore_63d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _zscore_rolling(base, 63)

def mtfo_189_ultimate_osc_proxy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_189_ultimate_osc_proxy_rank_63d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rank_pct(base, 63)

def mtfo_190_ultimate_osc_proxy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_190_ultimate_osc_proxy_lvl_126d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rolling_mean(base, 126)

def mtfo_191_ultimate_osc_proxy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_191_ultimate_osc_proxy_zscore_126d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _zscore_rolling(base, 126)

def mtfo_192_ultimate_osc_proxy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_192_ultimate_osc_proxy_rank_126d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rank_pct(base, 126)

def mtfo_193_ultimate_osc_proxy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_193_ultimate_osc_proxy_lvl_252d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rolling_mean(base, 252)

def mtfo_194_ultimate_osc_proxy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_194_ultimate_osc_proxy_zscore_252d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _zscore_rolling(base, 252)

def mtfo_195_ultimate_osc_proxy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_195_ultimate_osc_proxy_rank_252d
    ECONOMIC RATIONALE: Simplified Ultimate Oscillator.
    """
    base = ((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3
    return _rank_pct(base, 252)

def mtfo_196_mfi_oversold_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_196_mfi_oversold_lvl_5d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 5)

def mtfo_197_mfi_oversold_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_197_mfi_oversold_zscore_5d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 5)

def mtfo_198_mfi_oversold_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_198_mfi_oversold_rank_5d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 5)

def mtfo_199_mfi_oversold_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_199_mfi_oversold_lvl_21d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 21)

def mtfo_200_mfi_oversold_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_200_mfi_oversold_zscore_21d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 21)

def mtfo_201_mfi_oversold_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_201_mfi_oversold_rank_21d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 21)

def mtfo_202_mfi_oversold_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_202_mfi_oversold_lvl_63d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 63)

def mtfo_203_mfi_oversold_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_203_mfi_oversold_zscore_63d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 63)

def mtfo_204_mfi_oversold_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_204_mfi_oversold_rank_63d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 63)

def mtfo_205_mfi_oversold_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_205_mfi_oversold_lvl_126d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 126)

def mtfo_206_mfi_oversold_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_206_mfi_oversold_zscore_126d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 126)

def mtfo_207_mfi_oversold_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_207_mfi_oversold_rank_126d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 126)

def mtfo_208_mfi_oversold_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_208_mfi_oversold_lvl_252d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 252)

def mtfo_209_mfi_oversold_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_209_mfi_oversold_zscore_252d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 252)

def mtfo_210_mfi_oversold_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_210_mfi_oversold_rank_252d
    ECONOMIC RATIONALE: Money Flow Index.
    """
    base = 100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 252)

def mtfo_211_tf_regime_spread_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_211_tf_regime_spread_lvl_5d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rolling_mean(base, 5)

def mtfo_212_tf_regime_spread_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_212_tf_regime_spread_zscore_5d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _zscore_rolling(base, 5)

def mtfo_213_tf_regime_spread_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_213_tf_regime_spread_rank_5d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rank_pct(base, 5)

def mtfo_214_tf_regime_spread_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_214_tf_regime_spread_lvl_21d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rolling_mean(base, 21)

def mtfo_215_tf_regime_spread_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_215_tf_regime_spread_zscore_21d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _zscore_rolling(base, 21)

def mtfo_216_tf_regime_spread_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_216_tf_regime_spread_rank_21d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rank_pct(base, 21)

def mtfo_217_tf_regime_spread_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_217_tf_regime_spread_lvl_63d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rolling_mean(base, 63)

def mtfo_218_tf_regime_spread_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_218_tf_regime_spread_zscore_63d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _zscore_rolling(base, 63)

def mtfo_219_tf_regime_spread_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_219_tf_regime_spread_rank_63d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rank_pct(base, 63)

def mtfo_220_tf_regime_spread_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_220_tf_regime_spread_lvl_126d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rolling_mean(base, 126)

def mtfo_221_tf_regime_spread_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_221_tf_regime_spread_zscore_126d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _zscore_rolling(base, 126)

def mtfo_222_tf_regime_spread_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_222_tf_regime_spread_rank_126d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rank_pct(base, 126)

def mtfo_223_tf_regime_spread_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_223_tf_regime_spread_lvl_252d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rolling_mean(base, 252)

def mtfo_224_tf_regime_spread_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_224_tf_regime_spread_zscore_252d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _zscore_rolling(base, 252)

def mtfo_225_tf_regime_spread_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_225_tf_regime_spread_rank_252d
    ECONOMIC RATIONALE: Spread between short and medium term averages.
    """
    base = close.rolling(5).mean() / close.rolling(63).mean()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V103_REGISTRY_2 = {
    "mtfo_121_stoch_rsi_hybrid_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_121_stoch_rsi_hybrid_lvl_5d},
    "mtfo_122_stoch_rsi_hybrid_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_122_stoch_rsi_hybrid_zscore_5d},
    "mtfo_123_stoch_rsi_hybrid_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_123_stoch_rsi_hybrid_rank_5d},
    "mtfo_124_stoch_rsi_hybrid_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_124_stoch_rsi_hybrid_lvl_21d},
    "mtfo_125_stoch_rsi_hybrid_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_125_stoch_rsi_hybrid_zscore_21d},
    "mtfo_126_stoch_rsi_hybrid_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_126_stoch_rsi_hybrid_rank_21d},
    "mtfo_127_stoch_rsi_hybrid_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_127_stoch_rsi_hybrid_lvl_63d},
    "mtfo_128_stoch_rsi_hybrid_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_128_stoch_rsi_hybrid_zscore_63d},
    "mtfo_129_stoch_rsi_hybrid_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_129_stoch_rsi_hybrid_rank_63d},
    "mtfo_130_stoch_rsi_hybrid_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_130_stoch_rsi_hybrid_lvl_126d},
    "mtfo_131_stoch_rsi_hybrid_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_131_stoch_rsi_hybrid_zscore_126d},
    "mtfo_132_stoch_rsi_hybrid_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_132_stoch_rsi_hybrid_rank_126d},
    "mtfo_133_stoch_rsi_hybrid_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_133_stoch_rsi_hybrid_lvl_252d},
    "mtfo_134_stoch_rsi_hybrid_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_134_stoch_rsi_hybrid_zscore_252d},
    "mtfo_135_stoch_rsi_hybrid_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_135_stoch_rsi_hybrid_rank_252d},
    "mtfo_136_williams_r_multi_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_136_williams_r_multi_lvl_5d},
    "mtfo_137_williams_r_multi_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_137_williams_r_multi_zscore_5d},
    "mtfo_138_williams_r_multi_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_138_williams_r_multi_rank_5d},
    "mtfo_139_williams_r_multi_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_139_williams_r_multi_lvl_21d},
    "mtfo_140_williams_r_multi_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_140_williams_r_multi_zscore_21d},
    "mtfo_141_williams_r_multi_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_141_williams_r_multi_rank_21d},
    "mtfo_142_williams_r_multi_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_142_williams_r_multi_lvl_63d},
    "mtfo_143_williams_r_multi_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_143_williams_r_multi_zscore_63d},
    "mtfo_144_williams_r_multi_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_144_williams_r_multi_rank_63d},
    "mtfo_145_williams_r_multi_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_145_williams_r_multi_lvl_126d},
    "mtfo_146_williams_r_multi_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_146_williams_r_multi_zscore_126d},
    "mtfo_147_williams_r_multi_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_147_williams_r_multi_rank_126d},
    "mtfo_148_williams_r_multi_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_148_williams_r_multi_lvl_252d},
    "mtfo_149_williams_r_multi_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_149_williams_r_multi_zscore_252d},
    "mtfo_150_williams_r_multi_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_150_williams_r_multi_rank_252d},
    "mtfo_151_rsi_acceleration_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_151_rsi_acceleration_lvl_5d},
    "mtfo_152_rsi_acceleration_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_152_rsi_acceleration_zscore_5d},
    "mtfo_153_rsi_acceleration_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_153_rsi_acceleration_rank_5d},
    "mtfo_154_rsi_acceleration_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_154_rsi_acceleration_lvl_21d},
    "mtfo_155_rsi_acceleration_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_155_rsi_acceleration_zscore_21d},
    "mtfo_156_rsi_acceleration_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_156_rsi_acceleration_rank_21d},
    "mtfo_157_rsi_acceleration_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_157_rsi_acceleration_lvl_63d},
    "mtfo_158_rsi_acceleration_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_158_rsi_acceleration_zscore_63d},
    "mtfo_159_rsi_acceleration_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_159_rsi_acceleration_rank_63d},
    "mtfo_160_rsi_acceleration_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_160_rsi_acceleration_lvl_126d},
    "mtfo_161_rsi_acceleration_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_161_rsi_acceleration_zscore_126d},
    "mtfo_162_rsi_acceleration_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_162_rsi_acceleration_rank_126d},
    "mtfo_163_rsi_acceleration_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_163_rsi_acceleration_lvl_252d},
    "mtfo_164_rsi_acceleration_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_164_rsi_acceleration_zscore_252d},
    "mtfo_165_rsi_acceleration_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_165_rsi_acceleration_rank_252d},
    "mtfo_166_cci_oversold_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_166_cci_oversold_lvl_5d},
    "mtfo_167_cci_oversold_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_167_cci_oversold_zscore_5d},
    "mtfo_168_cci_oversold_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_168_cci_oversold_rank_5d},
    "mtfo_169_cci_oversold_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_169_cci_oversold_lvl_21d},
    "mtfo_170_cci_oversold_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_170_cci_oversold_zscore_21d},
    "mtfo_171_cci_oversold_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_171_cci_oversold_rank_21d},
    "mtfo_172_cci_oversold_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_172_cci_oversold_lvl_63d},
    "mtfo_173_cci_oversold_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_173_cci_oversold_zscore_63d},
    "mtfo_174_cci_oversold_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_174_cci_oversold_rank_63d},
    "mtfo_175_cci_oversold_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_175_cci_oversold_lvl_126d},
    "mtfo_176_cci_oversold_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_176_cci_oversold_zscore_126d},
    "mtfo_177_cci_oversold_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_177_cci_oversold_rank_126d},
    "mtfo_178_cci_oversold_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_178_cci_oversold_lvl_252d},
    "mtfo_179_cci_oversold_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_179_cci_oversold_zscore_252d},
    "mtfo_180_cci_oversold_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_180_cci_oversold_rank_252d},
    "mtfo_181_ultimate_osc_proxy_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_181_ultimate_osc_proxy_lvl_5d},
    "mtfo_182_ultimate_osc_proxy_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_182_ultimate_osc_proxy_zscore_5d},
    "mtfo_183_ultimate_osc_proxy_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_183_ultimate_osc_proxy_rank_5d},
    "mtfo_184_ultimate_osc_proxy_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_184_ultimate_osc_proxy_lvl_21d},
    "mtfo_185_ultimate_osc_proxy_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_185_ultimate_osc_proxy_zscore_21d},
    "mtfo_186_ultimate_osc_proxy_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_186_ultimate_osc_proxy_rank_21d},
    "mtfo_187_ultimate_osc_proxy_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_187_ultimate_osc_proxy_lvl_63d},
    "mtfo_188_ultimate_osc_proxy_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_188_ultimate_osc_proxy_zscore_63d},
    "mtfo_189_ultimate_osc_proxy_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_189_ultimate_osc_proxy_rank_63d},
    "mtfo_190_ultimate_osc_proxy_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_190_ultimate_osc_proxy_lvl_126d},
    "mtfo_191_ultimate_osc_proxy_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_191_ultimate_osc_proxy_zscore_126d},
    "mtfo_192_ultimate_osc_proxy_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_192_ultimate_osc_proxy_rank_126d},
    "mtfo_193_ultimate_osc_proxy_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_193_ultimate_osc_proxy_lvl_252d},
    "mtfo_194_ultimate_osc_proxy_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_194_ultimate_osc_proxy_zscore_252d},
    "mtfo_195_ultimate_osc_proxy_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_195_ultimate_osc_proxy_rank_252d},
    "mtfo_196_mfi_oversold_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_196_mfi_oversold_lvl_5d},
    "mtfo_197_mfi_oversold_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_197_mfi_oversold_zscore_5d},
    "mtfo_198_mfi_oversold_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_198_mfi_oversold_rank_5d},
    "mtfo_199_mfi_oversold_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_199_mfi_oversold_lvl_21d},
    "mtfo_200_mfi_oversold_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_200_mfi_oversold_zscore_21d},
    "mtfo_201_mfi_oversold_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_201_mfi_oversold_rank_21d},
    "mtfo_202_mfi_oversold_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_202_mfi_oversold_lvl_63d},
    "mtfo_203_mfi_oversold_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_203_mfi_oversold_zscore_63d},
    "mtfo_204_mfi_oversold_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_204_mfi_oversold_rank_63d},
    "mtfo_205_mfi_oversold_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_205_mfi_oversold_lvl_126d},
    "mtfo_206_mfi_oversold_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_206_mfi_oversold_zscore_126d},
    "mtfo_207_mfi_oversold_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_207_mfi_oversold_rank_126d},
    "mtfo_208_mfi_oversold_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_208_mfi_oversold_lvl_252d},
    "mtfo_209_mfi_oversold_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_209_mfi_oversold_zscore_252d},
    "mtfo_210_mfi_oversold_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_210_mfi_oversold_rank_252d},
    "mtfo_211_tf_regime_spread_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_211_tf_regime_spread_lvl_5d},
    "mtfo_212_tf_regime_spread_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_212_tf_regime_spread_zscore_5d},
    "mtfo_213_tf_regime_spread_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_213_tf_regime_spread_rank_5d},
    "mtfo_214_tf_regime_spread_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_214_tf_regime_spread_lvl_21d},
    "mtfo_215_tf_regime_spread_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_215_tf_regime_spread_zscore_21d},
    "mtfo_216_tf_regime_spread_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_216_tf_regime_spread_rank_21d},
    "mtfo_217_tf_regime_spread_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_217_tf_regime_spread_lvl_63d},
    "mtfo_218_tf_regime_spread_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_218_tf_regime_spread_zscore_63d},
    "mtfo_219_tf_regime_spread_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_219_tf_regime_spread_rank_63d},
    "mtfo_220_tf_regime_spread_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_220_tf_regime_spread_lvl_126d},
    "mtfo_221_tf_regime_spread_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_221_tf_regime_spread_zscore_126d},
    "mtfo_222_tf_regime_spread_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_222_tf_regime_spread_rank_126d},
    "mtfo_223_tf_regime_spread_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_223_tf_regime_spread_lvl_252d},
    "mtfo_224_tf_regime_spread_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_224_tf_regime_spread_zscore_252d},
    "mtfo_225_tf_regime_spread_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_225_tf_regime_spread_rank_252d},
}
