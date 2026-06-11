"""
103_multi_timeframe_oversold — Velocity (2nd Derivatives)
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

def mtfo_226_daily_rsi_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_226_daily_rsi_vel_5d
    ECONOMIC RATIONALE: Velocity of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5)

def mtfo_227_daily_rsi_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_227_daily_rsi_vel_21d
    ECONOMIC RATIONALE: Velocity of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21)

def mtfo_228_daily_rsi_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_228_daily_rsi_vel_63d
    ECONOMIC RATIONALE: Velocity of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63)

def mtfo_229_daily_rsi_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_229_daily_rsi_vel_126d
    ECONOMIC RATIONALE: Velocity of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126)

def mtfo_230_daily_rsi_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_230_daily_rsi_vel_252d
    ECONOMIC RATIONALE: Velocity of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252)

def mtfo_231_weekly_rsi_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_231_weekly_rsi_vel_5d
    ECONOMIC RATIONALE: Velocity of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5)

def mtfo_232_weekly_rsi_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_232_weekly_rsi_vel_21d
    ECONOMIC RATIONALE: Velocity of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21)

def mtfo_233_weekly_rsi_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_233_weekly_rsi_vel_63d
    ECONOMIC RATIONALE: Velocity of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63)

def mtfo_234_weekly_rsi_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_234_weekly_rsi_vel_126d
    ECONOMIC RATIONALE: Velocity of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126)

def mtfo_235_weekly_rsi_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_235_weekly_rsi_vel_252d
    ECONOMIC RATIONALE: Velocity of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252)

def mtfo_236_monthly_rsi_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_236_monthly_rsi_vel_5d
    ECONOMIC RATIONALE: Velocity of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5)

def mtfo_237_monthly_rsi_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_237_monthly_rsi_vel_21d
    ECONOMIC RATIONALE: Velocity of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21)

def mtfo_238_monthly_rsi_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_238_monthly_rsi_vel_63d
    ECONOMIC RATIONALE: Velocity of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63)

def mtfo_239_monthly_rsi_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_239_monthly_rsi_vel_126d
    ECONOMIC RATIONALE: Velocity of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126)

def mtfo_240_monthly_rsi_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_240_monthly_rsi_vel_252d
    ECONOMIC RATIONALE: Velocity of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252)

def mtfo_241_stoch_k_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_241_stoch_k_vel_5d
    ECONOMIC RATIONALE: Velocity of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(5)

def mtfo_242_stoch_k_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_242_stoch_k_vel_21d
    ECONOMIC RATIONALE: Velocity of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(21)

def mtfo_243_stoch_k_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_243_stoch_k_vel_63d
    ECONOMIC RATIONALE: Velocity of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(63)

def mtfo_244_stoch_k_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_244_stoch_k_vel_126d
    ECONOMIC RATIONALE: Velocity of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(126)

def mtfo_245_stoch_k_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_245_stoch_k_vel_252d
    ECONOMIC RATIONALE: Velocity of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(252)

def mtfo_246_stoch_d_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_246_stoch_d_vel_5d
    ECONOMIC RATIONALE: Velocity of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(5)

def mtfo_247_stoch_d_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_247_stoch_d_vel_21d
    ECONOMIC RATIONALE: Velocity of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(21)

def mtfo_248_stoch_d_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_248_stoch_d_vel_63d
    ECONOMIC RATIONALE: Velocity of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(63)

def mtfo_249_stoch_d_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_249_stoch_d_vel_126d
    ECONOMIC RATIONALE: Velocity of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(126)

def mtfo_250_stoch_d_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_250_stoch_d_vel_252d
    ECONOMIC RATIONALE: Velocity of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(252)

def mtfo_251_multi_tf_oversold_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_251_multi_tf_oversold_vel_5d
    ECONOMIC RATIONALE: Velocity of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(5)

def mtfo_252_multi_tf_oversold_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_252_multi_tf_oversold_vel_21d
    ECONOMIC RATIONALE: Velocity of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(21)

def mtfo_253_multi_tf_oversold_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_253_multi_tf_oversold_vel_63d
    ECONOMIC RATIONALE: Velocity of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(63)

def mtfo_254_multi_tf_oversold_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_254_multi_tf_oversold_vel_126d
    ECONOMIC RATIONALE: Velocity of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(126)

def mtfo_255_multi_tf_oversold_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_255_multi_tf_oversold_vel_252d
    ECONOMIC RATIONALE: Velocity of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(252)

def mtfo_256_rsi_divergence_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_256_rsi_divergence_vel_5d
    ECONOMIC RATIONALE: Velocity of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(5)

def mtfo_257_rsi_divergence_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_257_rsi_divergence_vel_21d
    ECONOMIC RATIONALE: Velocity of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(21)

def mtfo_258_rsi_divergence_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_258_rsi_divergence_vel_63d
    ECONOMIC RATIONALE: Velocity of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(63)

def mtfo_259_rsi_divergence_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_259_rsi_divergence_vel_126d
    ECONOMIC RATIONALE: Velocity of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(126)

def mtfo_260_rsi_divergence_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_260_rsi_divergence_vel_252d
    ECONOMIC RATIONALE: Velocity of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(252)

def mtfo_261_oversold_persistence_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_261_oversold_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(5)

def mtfo_262_oversold_persistence_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_262_oversold_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(21)

def mtfo_263_oversold_persistence_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_263_oversold_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(63)

def mtfo_264_oversold_persistence_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_264_oversold_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(126)

def mtfo_265_oversold_persistence_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_265_oversold_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(252)

def mtfo_266_stoch_rsi_hybrid_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_266_stoch_rsi_hybrid_vel_5d
    ECONOMIC RATIONALE: Velocity of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(5)

def mtfo_267_stoch_rsi_hybrid_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_267_stoch_rsi_hybrid_vel_21d
    ECONOMIC RATIONALE: Velocity of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(21)

def mtfo_268_stoch_rsi_hybrid_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_268_stoch_rsi_hybrid_vel_63d
    ECONOMIC RATIONALE: Velocity of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(63)

def mtfo_269_stoch_rsi_hybrid_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_269_stoch_rsi_hybrid_vel_126d
    ECONOMIC RATIONALE: Velocity of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(126)

def mtfo_270_stoch_rsi_hybrid_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_270_stoch_rsi_hybrid_vel_252d
    ECONOMIC RATIONALE: Velocity of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(252)

def mtfo_271_williams_r_multi_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_271_williams_r_multi_vel_5d
    ECONOMIC RATIONALE: Velocity of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(5)

def mtfo_272_williams_r_multi_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_272_williams_r_multi_vel_21d
    ECONOMIC RATIONALE: Velocity of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(21)

def mtfo_273_williams_r_multi_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_273_williams_r_multi_vel_63d
    ECONOMIC RATIONALE: Velocity of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(63)

def mtfo_274_williams_r_multi_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_274_williams_r_multi_vel_126d
    ECONOMIC RATIONALE: Velocity of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(126)

def mtfo_275_williams_r_multi_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_275_williams_r_multi_vel_252d
    ECONOMIC RATIONALE: Velocity of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(252)

def mtfo_276_rsi_acceleration_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_276_rsi_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(5)

def mtfo_277_rsi_acceleration_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_277_rsi_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(21)

def mtfo_278_rsi_acceleration_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_278_rsi_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(63)

def mtfo_279_rsi_acceleration_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_279_rsi_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(126)

def mtfo_280_rsi_acceleration_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_280_rsi_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(252)

def mtfo_281_cci_oversold_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_281_cci_oversold_vel_5d
    ECONOMIC RATIONALE: Velocity of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(5)

def mtfo_282_cci_oversold_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_282_cci_oversold_vel_21d
    ECONOMIC RATIONALE: Velocity of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(21)

def mtfo_283_cci_oversold_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_283_cci_oversold_vel_63d
    ECONOMIC RATIONALE: Velocity of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(63)

def mtfo_284_cci_oversold_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_284_cci_oversold_vel_126d
    ECONOMIC RATIONALE: Velocity of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(126)

def mtfo_285_cci_oversold_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_285_cci_oversold_vel_252d
    ECONOMIC RATIONALE: Velocity of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(252)

def mtfo_286_ultimate_osc_proxy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_286_ultimate_osc_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(5)

def mtfo_287_ultimate_osc_proxy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_287_ultimate_osc_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(21)

def mtfo_288_ultimate_osc_proxy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_288_ultimate_osc_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(63)

def mtfo_289_ultimate_osc_proxy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_289_ultimate_osc_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(126)

def mtfo_290_ultimate_osc_proxy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_290_ultimate_osc_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(252)

def mtfo_291_mfi_oversold_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_291_mfi_oversold_vel_5d
    ECONOMIC RATIONALE: Velocity of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5)

def mtfo_292_mfi_oversold_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_292_mfi_oversold_vel_21d
    ECONOMIC RATIONALE: Velocity of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21)

def mtfo_293_mfi_oversold_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_293_mfi_oversold_vel_63d
    ECONOMIC RATIONALE: Velocity of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63)

def mtfo_294_mfi_oversold_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_294_mfi_oversold_vel_126d
    ECONOMIC RATIONALE: Velocity of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126)

def mtfo_295_mfi_oversold_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_295_mfi_oversold_vel_252d
    ECONOMIC RATIONALE: Velocity of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252)

def mtfo_296_tf_regime_spread_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_296_tf_regime_spread_vel_5d
    ECONOMIC RATIONALE: Velocity of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(5)

def mtfo_297_tf_regime_spread_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_297_tf_regime_spread_vel_21d
    ECONOMIC RATIONALE: Velocity of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(21)

def mtfo_298_tf_regime_spread_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_298_tf_regime_spread_vel_63d
    ECONOMIC RATIONALE: Velocity of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(63)

def mtfo_299_tf_regime_spread_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_299_tf_regime_spread_vel_126d
    ECONOMIC RATIONALE: Velocity of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(126)

def mtfo_300_tf_regime_spread_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_300_tf_regime_spread_vel_252d
    ECONOMIC RATIONALE: Velocity of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V103_REGISTRY_VEL = {
    "mtfo_226_daily_rsi_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_226_daily_rsi_vel_5d},
    "mtfo_227_daily_rsi_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_227_daily_rsi_vel_21d},
    "mtfo_228_daily_rsi_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_228_daily_rsi_vel_63d},
    "mtfo_229_daily_rsi_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_229_daily_rsi_vel_126d},
    "mtfo_230_daily_rsi_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_230_daily_rsi_vel_252d},
    "mtfo_231_weekly_rsi_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_231_weekly_rsi_vel_5d},
    "mtfo_232_weekly_rsi_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_232_weekly_rsi_vel_21d},
    "mtfo_233_weekly_rsi_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_233_weekly_rsi_vel_63d},
    "mtfo_234_weekly_rsi_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_234_weekly_rsi_vel_126d},
    "mtfo_235_weekly_rsi_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_235_weekly_rsi_vel_252d},
    "mtfo_236_monthly_rsi_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_236_monthly_rsi_vel_5d},
    "mtfo_237_monthly_rsi_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_237_monthly_rsi_vel_21d},
    "mtfo_238_monthly_rsi_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_238_monthly_rsi_vel_63d},
    "mtfo_239_monthly_rsi_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_239_monthly_rsi_vel_126d},
    "mtfo_240_monthly_rsi_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_240_monthly_rsi_vel_252d},
    "mtfo_241_stoch_k_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_241_stoch_k_vel_5d},
    "mtfo_242_stoch_k_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_242_stoch_k_vel_21d},
    "mtfo_243_stoch_k_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_243_stoch_k_vel_63d},
    "mtfo_244_stoch_k_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_244_stoch_k_vel_126d},
    "mtfo_245_stoch_k_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_245_stoch_k_vel_252d},
    "mtfo_246_stoch_d_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_246_stoch_d_vel_5d},
    "mtfo_247_stoch_d_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_247_stoch_d_vel_21d},
    "mtfo_248_stoch_d_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_248_stoch_d_vel_63d},
    "mtfo_249_stoch_d_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_249_stoch_d_vel_126d},
    "mtfo_250_stoch_d_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_250_stoch_d_vel_252d},
    "mtfo_251_multi_tf_oversold_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_251_multi_tf_oversold_vel_5d},
    "mtfo_252_multi_tf_oversold_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_252_multi_tf_oversold_vel_21d},
    "mtfo_253_multi_tf_oversold_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_253_multi_tf_oversold_vel_63d},
    "mtfo_254_multi_tf_oversold_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_254_multi_tf_oversold_vel_126d},
    "mtfo_255_multi_tf_oversold_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_255_multi_tf_oversold_vel_252d},
    "mtfo_256_rsi_divergence_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_256_rsi_divergence_vel_5d},
    "mtfo_257_rsi_divergence_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_257_rsi_divergence_vel_21d},
    "mtfo_258_rsi_divergence_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_258_rsi_divergence_vel_63d},
    "mtfo_259_rsi_divergence_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_259_rsi_divergence_vel_126d},
    "mtfo_260_rsi_divergence_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_260_rsi_divergence_vel_252d},
    "mtfo_261_oversold_persistence_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_261_oversold_persistence_vel_5d},
    "mtfo_262_oversold_persistence_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_262_oversold_persistence_vel_21d},
    "mtfo_263_oversold_persistence_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_263_oversold_persistence_vel_63d},
    "mtfo_264_oversold_persistence_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_264_oversold_persistence_vel_126d},
    "mtfo_265_oversold_persistence_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_265_oversold_persistence_vel_252d},
    "mtfo_266_stoch_rsi_hybrid_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_266_stoch_rsi_hybrid_vel_5d},
    "mtfo_267_stoch_rsi_hybrid_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_267_stoch_rsi_hybrid_vel_21d},
    "mtfo_268_stoch_rsi_hybrid_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_268_stoch_rsi_hybrid_vel_63d},
    "mtfo_269_stoch_rsi_hybrid_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_269_stoch_rsi_hybrid_vel_126d},
    "mtfo_270_stoch_rsi_hybrid_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_270_stoch_rsi_hybrid_vel_252d},
    "mtfo_271_williams_r_multi_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_271_williams_r_multi_vel_5d},
    "mtfo_272_williams_r_multi_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_272_williams_r_multi_vel_21d},
    "mtfo_273_williams_r_multi_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_273_williams_r_multi_vel_63d},
    "mtfo_274_williams_r_multi_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_274_williams_r_multi_vel_126d},
    "mtfo_275_williams_r_multi_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_275_williams_r_multi_vel_252d},
    "mtfo_276_rsi_acceleration_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_276_rsi_acceleration_vel_5d},
    "mtfo_277_rsi_acceleration_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_277_rsi_acceleration_vel_21d},
    "mtfo_278_rsi_acceleration_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_278_rsi_acceleration_vel_63d},
    "mtfo_279_rsi_acceleration_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_279_rsi_acceleration_vel_126d},
    "mtfo_280_rsi_acceleration_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_280_rsi_acceleration_vel_252d},
    "mtfo_281_cci_oversold_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_281_cci_oversold_vel_5d},
    "mtfo_282_cci_oversold_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_282_cci_oversold_vel_21d},
    "mtfo_283_cci_oversold_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_283_cci_oversold_vel_63d},
    "mtfo_284_cci_oversold_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_284_cci_oversold_vel_126d},
    "mtfo_285_cci_oversold_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_285_cci_oversold_vel_252d},
    "mtfo_286_ultimate_osc_proxy_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_286_ultimate_osc_proxy_vel_5d},
    "mtfo_287_ultimate_osc_proxy_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_287_ultimate_osc_proxy_vel_21d},
    "mtfo_288_ultimate_osc_proxy_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_288_ultimate_osc_proxy_vel_63d},
    "mtfo_289_ultimate_osc_proxy_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_289_ultimate_osc_proxy_vel_126d},
    "mtfo_290_ultimate_osc_proxy_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_290_ultimate_osc_proxy_vel_252d},
    "mtfo_291_mfi_oversold_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_291_mfi_oversold_vel_5d},
    "mtfo_292_mfi_oversold_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_292_mfi_oversold_vel_21d},
    "mtfo_293_mfi_oversold_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_293_mfi_oversold_vel_63d},
    "mtfo_294_mfi_oversold_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_294_mfi_oversold_vel_126d},
    "mtfo_295_mfi_oversold_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_295_mfi_oversold_vel_252d},
    "mtfo_296_tf_regime_spread_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_296_tf_regime_spread_vel_5d},
    "mtfo_297_tf_regime_spread_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_297_tf_regime_spread_vel_21d},
    "mtfo_298_tf_regime_spread_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_298_tf_regime_spread_vel_63d},
    "mtfo_299_tf_regime_spread_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_299_tf_regime_spread_vel_126d},
    "mtfo_300_tf_regime_spread_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_300_tf_regime_spread_vel_252d},
}
