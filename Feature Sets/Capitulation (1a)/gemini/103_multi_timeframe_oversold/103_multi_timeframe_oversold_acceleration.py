"""
103_multi_timeframe_oversold — Acceleration (3rd Derivatives)
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

def mtfo_301_daily_rsi_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_301_daily_rsi_accel_5d
    ECONOMIC RATIONALE: Acceleration of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5).diff(_TD_MON)

def mtfo_302_daily_rsi_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_302_daily_rsi_accel_21d
    ECONOMIC RATIONALE: Acceleration of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21).diff(_TD_MON)

def mtfo_303_daily_rsi_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_303_daily_rsi_accel_63d
    ECONOMIC RATIONALE: Acceleration of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63).diff(_TD_MON)

def mtfo_304_daily_rsi_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_304_daily_rsi_accel_126d
    ECONOMIC RATIONALE: Acceleration of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126).diff(_TD_MON)

def mtfo_305_daily_rsi_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_305_daily_rsi_accel_252d
    ECONOMIC RATIONALE: Acceleration of daily_rsi. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252).diff(_TD_MON)

def mtfo_306_weekly_rsi_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_306_weekly_rsi_accel_5d
    ECONOMIC RATIONALE: Acceleration of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5).diff(_TD_MON)

def mtfo_307_weekly_rsi_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_307_weekly_rsi_accel_21d
    ECONOMIC RATIONALE: Acceleration of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21).diff(_TD_MON)

def mtfo_308_weekly_rsi_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_308_weekly_rsi_accel_63d
    ECONOMIC RATIONALE: Acceleration of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63).diff(_TD_MON)

def mtfo_309_weekly_rsi_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_309_weekly_rsi_accel_126d
    ECONOMIC RATIONALE: Acceleration of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126).diff(_TD_MON)

def mtfo_310_weekly_rsi_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_310_weekly_rsi_accel_252d
    ECONOMIC RATIONALE: Acceleration of weekly_rsi. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252).diff(_TD_MON)

def mtfo_311_monthly_rsi_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_311_monthly_rsi_accel_5d
    ECONOMIC RATIONALE: Acceleration of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5).diff(_TD_MON)

def mtfo_312_monthly_rsi_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_312_monthly_rsi_accel_21d
    ECONOMIC RATIONALE: Acceleration of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21).diff(_TD_MON)

def mtfo_313_monthly_rsi_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_313_monthly_rsi_accel_63d
    ECONOMIC RATIONALE: Acceleration of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63).diff(_TD_MON)

def mtfo_314_monthly_rsi_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_314_monthly_rsi_accel_126d
    ECONOMIC RATIONALE: Acceleration of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126).diff(_TD_MON)

def mtfo_315_monthly_rsi_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_315_monthly_rsi_accel_252d
    ECONOMIC RATIONALE: Acceleration of monthly_rsi. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252).diff(_TD_MON)

def mtfo_316_stoch_k_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_316_stoch_k_accel_5d
    ECONOMIC RATIONALE: Acceleration of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def mtfo_317_stoch_k_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_317_stoch_k_accel_21d
    ECONOMIC RATIONALE: Acceleration of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def mtfo_318_stoch_k_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_318_stoch_k_accel_63d
    ECONOMIC RATIONALE: Acceleration of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def mtfo_319_stoch_k_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_319_stoch_k_accel_126d
    ECONOMIC RATIONALE: Acceleration of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def mtfo_320_stoch_k_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_320_stoch_k_accel_252d
    ECONOMIC RATIONALE: Acceleration of stoch_k. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def mtfo_321_stoch_d_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_321_stoch_d_accel_5d
    ECONOMIC RATIONALE: Acceleration of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def mtfo_322_stoch_d_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_322_stoch_d_accel_21d
    ECONOMIC RATIONALE: Acceleration of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def mtfo_323_stoch_d_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_323_stoch_d_accel_63d
    ECONOMIC RATIONALE: Acceleration of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def mtfo_324_stoch_d_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_324_stoch_d_accel_126d
    ECONOMIC RATIONALE: Acceleration of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def mtfo_325_stoch_d_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_325_stoch_d_accel_252d
    ECONOMIC RATIONALE: Acceleration of stoch_d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def mtfo_326_multi_tf_oversold_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_326_multi_tf_oversold_accel_5d
    ECONOMIC RATIONALE: Acceleration of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(5).diff(_TD_MON)

def mtfo_327_multi_tf_oversold_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_327_multi_tf_oversold_accel_21d
    ECONOMIC RATIONALE: Acceleration of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(21).diff(_TD_MON)

def mtfo_328_multi_tf_oversold_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_328_multi_tf_oversold_accel_63d
    ECONOMIC RATIONALE: Acceleration of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(63).diff(_TD_MON)

def mtfo_329_multi_tf_oversold_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_329_multi_tf_oversold_accel_126d
    ECONOMIC RATIONALE: Acceleration of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(126).diff(_TD_MON)

def mtfo_330_multi_tf_oversold_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_330_multi_tf_oversold_accel_252d
    ECONOMIC RATIONALE: Acceleration of multi_tf_oversold. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).diff(252).diff(_TD_MON)

def mtfo_331_rsi_divergence_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_331_rsi_divergence_accel_5d
    ECONOMIC RATIONALE: Acceleration of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(5).diff(_TD_MON)

def mtfo_332_rsi_divergence_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_332_rsi_divergence_accel_21d
    ECONOMIC RATIONALE: Acceleration of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(21).diff(_TD_MON)

def mtfo_333_rsi_divergence_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_333_rsi_divergence_accel_63d
    ECONOMIC RATIONALE: Acceleration of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(63).diff(_TD_MON)

def mtfo_334_rsi_divergence_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_334_rsi_divergence_accel_126d
    ECONOMIC RATIONALE: Acceleration of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(126).diff(_TD_MON)

def mtfo_335_rsi_divergence_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_335_rsi_divergence_accel_252d
    ECONOMIC RATIONALE: Acceleration of rsi_divergence. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).diff(252).diff(_TD_MON)

def mtfo_336_oversold_persistence_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_336_oversold_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(5).diff(_TD_MON)

def mtfo_337_oversold_persistence_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_337_oversold_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(21).diff(_TD_MON)

def mtfo_338_oversold_persistence_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_338_oversold_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(63).diff(_TD_MON)

def mtfo_339_oversold_persistence_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_339_oversold_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(126).diff(_TD_MON)

def mtfo_340_oversold_persistence_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_340_oversold_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of oversold_persistence. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).diff(252).diff(_TD_MON)

def mtfo_341_stoch_rsi_hybrid_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_341_stoch_rsi_hybrid_accel_5d
    ECONOMIC RATIONALE: Acceleration of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(5).diff(_TD_MON)

def mtfo_342_stoch_rsi_hybrid_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_342_stoch_rsi_hybrid_accel_21d
    ECONOMIC RATIONALE: Acceleration of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(21).diff(_TD_MON)

def mtfo_343_stoch_rsi_hybrid_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_343_stoch_rsi_hybrid_accel_63d
    ECONOMIC RATIONALE: Acceleration of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(63).diff(_TD_MON)

def mtfo_344_stoch_rsi_hybrid_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_344_stoch_rsi_hybrid_accel_126d
    ECONOMIC RATIONALE: Acceleration of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(126).diff(_TD_MON)

def mtfo_345_stoch_rsi_hybrid_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_345_stoch_rsi_hybrid_accel_252d
    ECONOMIC RATIONALE: Acceleration of stoch_rsi_hybrid. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).diff(252).diff(_TD_MON)

def mtfo_346_williams_r_multi_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_346_williams_r_multi_accel_5d
    ECONOMIC RATIONALE: Acceleration of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def mtfo_347_williams_r_multi_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_347_williams_r_multi_accel_21d
    ECONOMIC RATIONALE: Acceleration of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def mtfo_348_williams_r_multi_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_348_williams_r_multi_accel_63d
    ECONOMIC RATIONALE: Acceleration of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def mtfo_349_williams_r_multi_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_349_williams_r_multi_accel_126d
    ECONOMIC RATIONALE: Acceleration of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def mtfo_350_williams_r_multi_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_350_williams_r_multi_accel_252d
    ECONOMIC RATIONALE: Acceleration of williams_r_multi. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def mtfo_351_rsi_acceleration_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_351_rsi_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(5).diff(_TD_MON)

def mtfo_352_rsi_acceleration_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_352_rsi_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(21).diff(_TD_MON)

def mtfo_353_rsi_acceleration_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_353_rsi_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(63).diff(_TD_MON)

def mtfo_354_rsi_acceleration_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_354_rsi_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(126).diff(_TD_MON)

def mtfo_355_rsi_acceleration_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_355_rsi_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of rsi_acceleration. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).diff(252).diff(_TD_MON)

def mtfo_356_cci_oversold_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_356_cci_oversold_accel_5d
    ECONOMIC RATIONALE: Acceleration of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(5).diff(_TD_MON)

def mtfo_357_cci_oversold_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_357_cci_oversold_accel_21d
    ECONOMIC RATIONALE: Acceleration of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(21).diff(_TD_MON)

def mtfo_358_cci_oversold_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_358_cci_oversold_accel_63d
    ECONOMIC RATIONALE: Acceleration of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(63).diff(_TD_MON)

def mtfo_359_cci_oversold_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_359_cci_oversold_accel_126d
    ECONOMIC RATIONALE: Acceleration of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(126).diff(_TD_MON)

def mtfo_360_cci_oversold_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_360_cci_oversold_accel_252d
    ECONOMIC RATIONALE: Acceleration of cci_oversold. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).diff(252).diff(_TD_MON)

def mtfo_361_ultimate_osc_proxy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_361_ultimate_osc_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(5).diff(_TD_MON)

def mtfo_362_ultimate_osc_proxy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_362_ultimate_osc_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(21).diff(_TD_MON)

def mtfo_363_ultimate_osc_proxy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_363_ultimate_osc_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(63).diff(_TD_MON)

def mtfo_364_ultimate_osc_proxy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_364_ultimate_osc_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(126).diff(_TD_MON)

def mtfo_365_ultimate_osc_proxy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_365_ultimate_osc_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of ultimate_osc_proxy. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).diff(252).diff(_TD_MON)

def mtfo_366_mfi_oversold_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_366_mfi_oversold_accel_5d
    ECONOMIC RATIONALE: Acceleration of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(5).diff(_TD_MON)

def mtfo_367_mfi_oversold_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_367_mfi_oversold_accel_21d
    ECONOMIC RATIONALE: Acceleration of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(21).diff(_TD_MON)

def mtfo_368_mfi_oversold_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_368_mfi_oversold_accel_63d
    ECONOMIC RATIONALE: Acceleration of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(63).diff(_TD_MON)

def mtfo_369_mfi_oversold_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_369_mfi_oversold_accel_126d
    ECONOMIC RATIONALE: Acceleration of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(126).diff(_TD_MON)

def mtfo_370_mfi_oversold_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_370_mfi_oversold_accel_252d
    ECONOMIC RATIONALE: Acceleration of mfi_oversold. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).diff(252).diff(_TD_MON)

def mtfo_371_tf_regime_spread_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_371_tf_regime_spread_accel_5d
    ECONOMIC RATIONALE: Acceleration of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(5).diff(_TD_MON)

def mtfo_372_tf_regime_spread_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_372_tf_regime_spread_accel_21d
    ECONOMIC RATIONALE: Acceleration of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(21).diff(_TD_MON)

def mtfo_373_tf_regime_spread_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_373_tf_regime_spread_accel_63d
    ECONOMIC RATIONALE: Acceleration of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(63).diff(_TD_MON)

def mtfo_374_tf_regime_spread_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_374_tf_regime_spread_accel_126d
    ECONOMIC RATIONALE: Acceleration of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(126).diff(_TD_MON)

def mtfo_375_tf_regime_spread_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_375_tf_regime_spread_accel_252d
    ECONOMIC RATIONALE: Acceleration of tf_regime_spread. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V103_REGISTRY_ACCEL = {
    "mtfo_301_daily_rsi_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_301_daily_rsi_accel_5d},
    "mtfo_302_daily_rsi_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_302_daily_rsi_accel_21d},
    "mtfo_303_daily_rsi_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_303_daily_rsi_accel_63d},
    "mtfo_304_daily_rsi_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_304_daily_rsi_accel_126d},
    "mtfo_305_daily_rsi_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_305_daily_rsi_accel_252d},
    "mtfo_306_weekly_rsi_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_306_weekly_rsi_accel_5d},
    "mtfo_307_weekly_rsi_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_307_weekly_rsi_accel_21d},
    "mtfo_308_weekly_rsi_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_308_weekly_rsi_accel_63d},
    "mtfo_309_weekly_rsi_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_309_weekly_rsi_accel_126d},
    "mtfo_310_weekly_rsi_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_310_weekly_rsi_accel_252d},
    "mtfo_311_monthly_rsi_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_311_monthly_rsi_accel_5d},
    "mtfo_312_monthly_rsi_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_312_monthly_rsi_accel_21d},
    "mtfo_313_monthly_rsi_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_313_monthly_rsi_accel_63d},
    "mtfo_314_monthly_rsi_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_314_monthly_rsi_accel_126d},
    "mtfo_315_monthly_rsi_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_315_monthly_rsi_accel_252d},
    "mtfo_316_stoch_k_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_316_stoch_k_accel_5d},
    "mtfo_317_stoch_k_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_317_stoch_k_accel_21d},
    "mtfo_318_stoch_k_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_318_stoch_k_accel_63d},
    "mtfo_319_stoch_k_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_319_stoch_k_accel_126d},
    "mtfo_320_stoch_k_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_320_stoch_k_accel_252d},
    "mtfo_321_stoch_d_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_321_stoch_d_accel_5d},
    "mtfo_322_stoch_d_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_322_stoch_d_accel_21d},
    "mtfo_323_stoch_d_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_323_stoch_d_accel_63d},
    "mtfo_324_stoch_d_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_324_stoch_d_accel_126d},
    "mtfo_325_stoch_d_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_325_stoch_d_accel_252d},
    "mtfo_326_multi_tf_oversold_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_326_multi_tf_oversold_accel_5d},
    "mtfo_327_multi_tf_oversold_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_327_multi_tf_oversold_accel_21d},
    "mtfo_328_multi_tf_oversold_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_328_multi_tf_oversold_accel_63d},
    "mtfo_329_multi_tf_oversold_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_329_multi_tf_oversold_accel_126d},
    "mtfo_330_multi_tf_oversold_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_330_multi_tf_oversold_accel_252d},
    "mtfo_331_rsi_divergence_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_331_rsi_divergence_accel_5d},
    "mtfo_332_rsi_divergence_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_332_rsi_divergence_accel_21d},
    "mtfo_333_rsi_divergence_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_333_rsi_divergence_accel_63d},
    "mtfo_334_rsi_divergence_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_334_rsi_divergence_accel_126d},
    "mtfo_335_rsi_divergence_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_335_rsi_divergence_accel_252d},
    "mtfo_336_oversold_persistence_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_336_oversold_persistence_accel_5d},
    "mtfo_337_oversold_persistence_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_337_oversold_persistence_accel_21d},
    "mtfo_338_oversold_persistence_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_338_oversold_persistence_accel_63d},
    "mtfo_339_oversold_persistence_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_339_oversold_persistence_accel_126d},
    "mtfo_340_oversold_persistence_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_340_oversold_persistence_accel_252d},
    "mtfo_341_stoch_rsi_hybrid_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_341_stoch_rsi_hybrid_accel_5d},
    "mtfo_342_stoch_rsi_hybrid_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_342_stoch_rsi_hybrid_accel_21d},
    "mtfo_343_stoch_rsi_hybrid_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_343_stoch_rsi_hybrid_accel_63d},
    "mtfo_344_stoch_rsi_hybrid_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_344_stoch_rsi_hybrid_accel_126d},
    "mtfo_345_stoch_rsi_hybrid_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_345_stoch_rsi_hybrid_accel_252d},
    "mtfo_346_williams_r_multi_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_346_williams_r_multi_accel_5d},
    "mtfo_347_williams_r_multi_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_347_williams_r_multi_accel_21d},
    "mtfo_348_williams_r_multi_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_348_williams_r_multi_accel_63d},
    "mtfo_349_williams_r_multi_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_349_williams_r_multi_accel_126d},
    "mtfo_350_williams_r_multi_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_350_williams_r_multi_accel_252d},
    "mtfo_351_rsi_acceleration_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_351_rsi_acceleration_accel_5d},
    "mtfo_352_rsi_acceleration_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_352_rsi_acceleration_accel_21d},
    "mtfo_353_rsi_acceleration_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_353_rsi_acceleration_accel_63d},
    "mtfo_354_rsi_acceleration_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_354_rsi_acceleration_accel_126d},
    "mtfo_355_rsi_acceleration_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_355_rsi_acceleration_accel_252d},
    "mtfo_356_cci_oversold_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_356_cci_oversold_accel_5d},
    "mtfo_357_cci_oversold_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_357_cci_oversold_accel_21d},
    "mtfo_358_cci_oversold_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_358_cci_oversold_accel_63d},
    "mtfo_359_cci_oversold_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_359_cci_oversold_accel_126d},
    "mtfo_360_cci_oversold_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_360_cci_oversold_accel_252d},
    "mtfo_361_ultimate_osc_proxy_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_361_ultimate_osc_proxy_accel_5d},
    "mtfo_362_ultimate_osc_proxy_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_362_ultimate_osc_proxy_accel_21d},
    "mtfo_363_ultimate_osc_proxy_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_363_ultimate_osc_proxy_accel_63d},
    "mtfo_364_ultimate_osc_proxy_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_364_ultimate_osc_proxy_accel_126d},
    "mtfo_365_ultimate_osc_proxy_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_365_ultimate_osc_proxy_accel_252d},
    "mtfo_366_mfi_oversold_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_366_mfi_oversold_accel_5d},
    "mtfo_367_mfi_oversold_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_367_mfi_oversold_accel_21d},
    "mtfo_368_mfi_oversold_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_368_mfi_oversold_accel_63d},
    "mtfo_369_mfi_oversold_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_369_mfi_oversold_accel_126d},
    "mtfo_370_mfi_oversold_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_370_mfi_oversold_accel_252d},
    "mtfo_371_tf_regime_spread_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_371_tf_regime_spread_accel_5d},
    "mtfo_372_tf_regime_spread_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_372_tf_regime_spread_accel_21d},
    "mtfo_373_tf_regime_spread_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_373_tf_regime_spread_accel_63d},
    "mtfo_374_tf_regime_spread_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_374_tf_regime_spread_accel_126d},
    "mtfo_375_tf_regime_spread_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_375_tf_regime_spread_accel_252d},
}
