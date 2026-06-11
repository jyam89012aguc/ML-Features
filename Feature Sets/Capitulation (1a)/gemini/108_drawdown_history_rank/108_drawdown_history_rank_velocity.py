"""
108_drawdown_history_rank — Velocity (2nd Derivatives)
Domain: drawdown_history_rank
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

def dhrk_226_current_drawdown_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_226_current_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(5)

def dhrk_227_current_drawdown_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_227_current_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(21)

def dhrk_228_current_drawdown_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_228_current_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(63)

def dhrk_229_current_drawdown_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_229_current_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(126)

def dhrk_230_current_drawdown_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_230_current_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(252)

def dhrk_231_drawdown_rank_252d_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_231_drawdown_rank_252d_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(5)

def dhrk_232_drawdown_rank_252d_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_232_drawdown_rank_252d_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(21)

def dhrk_233_drawdown_rank_252d_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_233_drawdown_rank_252d_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(63)

def dhrk_234_drawdown_rank_252d_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_234_drawdown_rank_252d_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(126)

def dhrk_235_drawdown_rank_252d_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_235_drawdown_rank_252d_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(252)

def dhrk_236_drawdown_severity_z_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_236_drawdown_severity_z_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(5)

def dhrk_237_drawdown_severity_z_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_237_drawdown_severity_z_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(21)

def dhrk_238_drawdown_severity_z_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_238_drawdown_severity_z_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(63)

def dhrk_239_drawdown_severity_z_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_239_drawdown_severity_z_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(126)

def dhrk_240_drawdown_severity_z_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_240_drawdown_severity_z_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(252)

def dhrk_241_drawdown_duration_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_241_drawdown_duration_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(5)

def dhrk_242_drawdown_duration_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_242_drawdown_duration_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(21)

def dhrk_243_drawdown_duration_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_243_drawdown_duration_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(63)

def dhrk_244_drawdown_duration_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_244_drawdown_duration_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(126)

def dhrk_245_drawdown_duration_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_245_drawdown_duration_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(252)

def dhrk_246_peak_to_trough_momentum_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_246_peak_to_trough_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(5)

def dhrk_247_peak_to_trough_momentum_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_247_peak_to_trough_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(21)

def dhrk_248_peak_to_trough_momentum_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_248_peak_to_trough_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(63)

def dhrk_249_peak_to_trough_momentum_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_249_peak_to_trough_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(126)

def dhrk_250_peak_to_trough_momentum_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_250_peak_to_trough_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(252)

def dhrk_251_drawdown_acceleration_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_251_drawdown_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(5)

def dhrk_252_drawdown_acceleration_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_252_drawdown_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(21)

def dhrk_253_drawdown_acceleration_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_253_drawdown_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(63)

def dhrk_254_drawdown_acceleration_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_254_drawdown_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(126)

def dhrk_255_drawdown_acceleration_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_255_drawdown_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(252)

def dhrk_256_drawdown_vol_ratio_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_256_drawdown_vol_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(5)

def dhrk_257_drawdown_vol_ratio_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_257_drawdown_vol_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(21)

def dhrk_258_drawdown_vol_ratio_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_258_drawdown_vol_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(63)

def dhrk_259_drawdown_vol_ratio_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_259_drawdown_vol_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(126)

def dhrk_260_drawdown_vol_ratio_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_260_drawdown_vol_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(252)

def dhrk_261_recovery_from_lows_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_261_recovery_from_lows_vel_5d
    ECONOMIC RATIONALE: Velocity of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(5)

def dhrk_262_recovery_from_lows_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_262_recovery_from_lows_vel_21d
    ECONOMIC RATIONALE: Velocity of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(21)

def dhrk_263_recovery_from_lows_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_263_recovery_from_lows_vel_63d
    ECONOMIC RATIONALE: Velocity of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(63)

def dhrk_264_recovery_from_lows_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_264_recovery_from_lows_vel_126d
    ECONOMIC RATIONALE: Velocity of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(126)

def dhrk_265_recovery_from_lows_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_265_recovery_from_lows_vel_252d
    ECONOMIC RATIONALE: Velocity of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(252)

def dhrk_266_drawdown_persistence_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_266_drawdown_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(5)

def dhrk_267_drawdown_persistence_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_267_drawdown_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(21)

def dhrk_268_drawdown_persistence_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_268_drawdown_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(63)

def dhrk_269_drawdown_persistence_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_269_drawdown_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(126)

def dhrk_270_drawdown_persistence_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_270_drawdown_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(252)

def dhrk_271_drawdown_regime_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_271_drawdown_regime_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(5)

def dhrk_272_drawdown_regime_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_272_drawdown_regime_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(21)

def dhrk_273_drawdown_regime_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_273_drawdown_regime_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(63)

def dhrk_274_drawdown_regime_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_274_drawdown_regime_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(126)

def dhrk_275_drawdown_regime_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_275_drawdown_regime_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(252)

def dhrk_276_drawdown_impact_score_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_276_drawdown_impact_score_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(5)

def dhrk_277_drawdown_impact_score_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_277_drawdown_impact_score_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(21)

def dhrk_278_drawdown_impact_score_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_278_drawdown_impact_score_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(63)

def dhrk_279_drawdown_impact_score_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_279_drawdown_impact_score_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(126)

def dhrk_280_drawdown_impact_score_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_280_drawdown_impact_score_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(252)

def dhrk_281_historical_max_drawdown_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_281_historical_max_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(5)

def dhrk_282_historical_max_drawdown_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_282_historical_max_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(21)

def dhrk_283_historical_max_drawdown_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_283_historical_max_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(63)

def dhrk_284_historical_max_drawdown_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_284_historical_max_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(126)

def dhrk_285_historical_max_drawdown_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_285_historical_max_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(252)

def dhrk_286_drawdown_exhaustion_proxy_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_286_drawdown_exhaustion_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(5)

def dhrk_287_drawdown_exhaustion_proxy_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_287_drawdown_exhaustion_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(21)

def dhrk_288_drawdown_exhaustion_proxy_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_288_drawdown_exhaustion_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(63)

def dhrk_289_drawdown_exhaustion_proxy_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_289_drawdown_exhaustion_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(126)

def dhrk_290_drawdown_exhaustion_proxy_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_290_drawdown_exhaustion_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(252)

def dhrk_291_drawdown_oscillator_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_291_drawdown_oscillator_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(5)

def dhrk_292_drawdown_oscillator_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_292_drawdown_oscillator_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(21)

def dhrk_293_drawdown_oscillator_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_293_drawdown_oscillator_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(63)

def dhrk_294_drawdown_oscillator_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_294_drawdown_oscillator_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(126)

def dhrk_295_drawdown_oscillator_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_295_drawdown_oscillator_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(252)

def dhrk_296_drawdown_tail_risk_vel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_296_drawdown_tail_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(5)

def dhrk_297_drawdown_tail_risk_vel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_297_drawdown_tail_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(21)

def dhrk_298_drawdown_tail_risk_vel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_298_drawdown_tail_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(63)

def dhrk_299_drawdown_tail_risk_vel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_299_drawdown_tail_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(126)

def dhrk_300_drawdown_tail_risk_vel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_300_drawdown_tail_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V108_REGISTRY_VEL = {
    "dhrk_226_current_drawdown_vel_5d": {"inputs": ["close"], "func": dhrk_226_current_drawdown_vel_5d},
    "dhrk_227_current_drawdown_vel_21d": {"inputs": ["close"], "func": dhrk_227_current_drawdown_vel_21d},
    "dhrk_228_current_drawdown_vel_63d": {"inputs": ["close"], "func": dhrk_228_current_drawdown_vel_63d},
    "dhrk_229_current_drawdown_vel_126d": {"inputs": ["close"], "func": dhrk_229_current_drawdown_vel_126d},
    "dhrk_230_current_drawdown_vel_252d": {"inputs": ["close"], "func": dhrk_230_current_drawdown_vel_252d},
    "dhrk_231_drawdown_rank_252d_vel_5d": {"inputs": ["close"], "func": dhrk_231_drawdown_rank_252d_vel_5d},
    "dhrk_232_drawdown_rank_252d_vel_21d": {"inputs": ["close"], "func": dhrk_232_drawdown_rank_252d_vel_21d},
    "dhrk_233_drawdown_rank_252d_vel_63d": {"inputs": ["close"], "func": dhrk_233_drawdown_rank_252d_vel_63d},
    "dhrk_234_drawdown_rank_252d_vel_126d": {"inputs": ["close"], "func": dhrk_234_drawdown_rank_252d_vel_126d},
    "dhrk_235_drawdown_rank_252d_vel_252d": {"inputs": ["close"], "func": dhrk_235_drawdown_rank_252d_vel_252d},
    "dhrk_236_drawdown_severity_z_vel_5d": {"inputs": ["close"], "func": dhrk_236_drawdown_severity_z_vel_5d},
    "dhrk_237_drawdown_severity_z_vel_21d": {"inputs": ["close"], "func": dhrk_237_drawdown_severity_z_vel_21d},
    "dhrk_238_drawdown_severity_z_vel_63d": {"inputs": ["close"], "func": dhrk_238_drawdown_severity_z_vel_63d},
    "dhrk_239_drawdown_severity_z_vel_126d": {"inputs": ["close"], "func": dhrk_239_drawdown_severity_z_vel_126d},
    "dhrk_240_drawdown_severity_z_vel_252d": {"inputs": ["close"], "func": dhrk_240_drawdown_severity_z_vel_252d},
    "dhrk_241_drawdown_duration_vel_5d": {"inputs": ["close"], "func": dhrk_241_drawdown_duration_vel_5d},
    "dhrk_242_drawdown_duration_vel_21d": {"inputs": ["close"], "func": dhrk_242_drawdown_duration_vel_21d},
    "dhrk_243_drawdown_duration_vel_63d": {"inputs": ["close"], "func": dhrk_243_drawdown_duration_vel_63d},
    "dhrk_244_drawdown_duration_vel_126d": {"inputs": ["close"], "func": dhrk_244_drawdown_duration_vel_126d},
    "dhrk_245_drawdown_duration_vel_252d": {"inputs": ["close"], "func": dhrk_245_drawdown_duration_vel_252d},
    "dhrk_246_peak_to_trough_momentum_vel_5d": {"inputs": ["close"], "func": dhrk_246_peak_to_trough_momentum_vel_5d},
    "dhrk_247_peak_to_trough_momentum_vel_21d": {"inputs": ["close"], "func": dhrk_247_peak_to_trough_momentum_vel_21d},
    "dhrk_248_peak_to_trough_momentum_vel_63d": {"inputs": ["close"], "func": dhrk_248_peak_to_trough_momentum_vel_63d},
    "dhrk_249_peak_to_trough_momentum_vel_126d": {"inputs": ["close"], "func": dhrk_249_peak_to_trough_momentum_vel_126d},
    "dhrk_250_peak_to_trough_momentum_vel_252d": {"inputs": ["close"], "func": dhrk_250_peak_to_trough_momentum_vel_252d},
    "dhrk_251_drawdown_acceleration_vel_5d": {"inputs": ["close"], "func": dhrk_251_drawdown_acceleration_vel_5d},
    "dhrk_252_drawdown_acceleration_vel_21d": {"inputs": ["close"], "func": dhrk_252_drawdown_acceleration_vel_21d},
    "dhrk_253_drawdown_acceleration_vel_63d": {"inputs": ["close"], "func": dhrk_253_drawdown_acceleration_vel_63d},
    "dhrk_254_drawdown_acceleration_vel_126d": {"inputs": ["close"], "func": dhrk_254_drawdown_acceleration_vel_126d},
    "dhrk_255_drawdown_acceleration_vel_252d": {"inputs": ["close"], "func": dhrk_255_drawdown_acceleration_vel_252d},
    "dhrk_256_drawdown_vol_ratio_vel_5d": {"inputs": ["close"], "func": dhrk_256_drawdown_vol_ratio_vel_5d},
    "dhrk_257_drawdown_vol_ratio_vel_21d": {"inputs": ["close"], "func": dhrk_257_drawdown_vol_ratio_vel_21d},
    "dhrk_258_drawdown_vol_ratio_vel_63d": {"inputs": ["close"], "func": dhrk_258_drawdown_vol_ratio_vel_63d},
    "dhrk_259_drawdown_vol_ratio_vel_126d": {"inputs": ["close"], "func": dhrk_259_drawdown_vol_ratio_vel_126d},
    "dhrk_260_drawdown_vol_ratio_vel_252d": {"inputs": ["close"], "func": dhrk_260_drawdown_vol_ratio_vel_252d},
    "dhrk_261_recovery_from_lows_vel_5d": {"inputs": ["close"], "func": dhrk_261_recovery_from_lows_vel_5d},
    "dhrk_262_recovery_from_lows_vel_21d": {"inputs": ["close"], "func": dhrk_262_recovery_from_lows_vel_21d},
    "dhrk_263_recovery_from_lows_vel_63d": {"inputs": ["close"], "func": dhrk_263_recovery_from_lows_vel_63d},
    "dhrk_264_recovery_from_lows_vel_126d": {"inputs": ["close"], "func": dhrk_264_recovery_from_lows_vel_126d},
    "dhrk_265_recovery_from_lows_vel_252d": {"inputs": ["close"], "func": dhrk_265_recovery_from_lows_vel_252d},
    "dhrk_266_drawdown_persistence_vel_5d": {"inputs": ["close"], "func": dhrk_266_drawdown_persistence_vel_5d},
    "dhrk_267_drawdown_persistence_vel_21d": {"inputs": ["close"], "func": dhrk_267_drawdown_persistence_vel_21d},
    "dhrk_268_drawdown_persistence_vel_63d": {"inputs": ["close"], "func": dhrk_268_drawdown_persistence_vel_63d},
    "dhrk_269_drawdown_persistence_vel_126d": {"inputs": ["close"], "func": dhrk_269_drawdown_persistence_vel_126d},
    "dhrk_270_drawdown_persistence_vel_252d": {"inputs": ["close"], "func": dhrk_270_drawdown_persistence_vel_252d},
    "dhrk_271_drawdown_regime_vel_5d": {"inputs": ["close"], "func": dhrk_271_drawdown_regime_vel_5d},
    "dhrk_272_drawdown_regime_vel_21d": {"inputs": ["close"], "func": dhrk_272_drawdown_regime_vel_21d},
    "dhrk_273_drawdown_regime_vel_63d": {"inputs": ["close"], "func": dhrk_273_drawdown_regime_vel_63d},
    "dhrk_274_drawdown_regime_vel_126d": {"inputs": ["close"], "func": dhrk_274_drawdown_regime_vel_126d},
    "dhrk_275_drawdown_regime_vel_252d": {"inputs": ["close"], "func": dhrk_275_drawdown_regime_vel_252d},
    "dhrk_276_drawdown_impact_score_vel_5d": {"inputs": ["close"], "func": dhrk_276_drawdown_impact_score_vel_5d},
    "dhrk_277_drawdown_impact_score_vel_21d": {"inputs": ["close"], "func": dhrk_277_drawdown_impact_score_vel_21d},
    "dhrk_278_drawdown_impact_score_vel_63d": {"inputs": ["close"], "func": dhrk_278_drawdown_impact_score_vel_63d},
    "dhrk_279_drawdown_impact_score_vel_126d": {"inputs": ["close"], "func": dhrk_279_drawdown_impact_score_vel_126d},
    "dhrk_280_drawdown_impact_score_vel_252d": {"inputs": ["close"], "func": dhrk_280_drawdown_impact_score_vel_252d},
    "dhrk_281_historical_max_drawdown_vel_5d": {"inputs": ["close"], "func": dhrk_281_historical_max_drawdown_vel_5d},
    "dhrk_282_historical_max_drawdown_vel_21d": {"inputs": ["close"], "func": dhrk_282_historical_max_drawdown_vel_21d},
    "dhrk_283_historical_max_drawdown_vel_63d": {"inputs": ["close"], "func": dhrk_283_historical_max_drawdown_vel_63d},
    "dhrk_284_historical_max_drawdown_vel_126d": {"inputs": ["close"], "func": dhrk_284_historical_max_drawdown_vel_126d},
    "dhrk_285_historical_max_drawdown_vel_252d": {"inputs": ["close"], "func": dhrk_285_historical_max_drawdown_vel_252d},
    "dhrk_286_drawdown_exhaustion_proxy_vel_5d": {"inputs": ["close"], "func": dhrk_286_drawdown_exhaustion_proxy_vel_5d},
    "dhrk_287_drawdown_exhaustion_proxy_vel_21d": {"inputs": ["close"], "func": dhrk_287_drawdown_exhaustion_proxy_vel_21d},
    "dhrk_288_drawdown_exhaustion_proxy_vel_63d": {"inputs": ["close"], "func": dhrk_288_drawdown_exhaustion_proxy_vel_63d},
    "dhrk_289_drawdown_exhaustion_proxy_vel_126d": {"inputs": ["close"], "func": dhrk_289_drawdown_exhaustion_proxy_vel_126d},
    "dhrk_290_drawdown_exhaustion_proxy_vel_252d": {"inputs": ["close"], "func": dhrk_290_drawdown_exhaustion_proxy_vel_252d},
    "dhrk_291_drawdown_oscillator_vel_5d": {"inputs": ["close"], "func": dhrk_291_drawdown_oscillator_vel_5d},
    "dhrk_292_drawdown_oscillator_vel_21d": {"inputs": ["close"], "func": dhrk_292_drawdown_oscillator_vel_21d},
    "dhrk_293_drawdown_oscillator_vel_63d": {"inputs": ["close"], "func": dhrk_293_drawdown_oscillator_vel_63d},
    "dhrk_294_drawdown_oscillator_vel_126d": {"inputs": ["close"], "func": dhrk_294_drawdown_oscillator_vel_126d},
    "dhrk_295_drawdown_oscillator_vel_252d": {"inputs": ["close"], "func": dhrk_295_drawdown_oscillator_vel_252d},
    "dhrk_296_drawdown_tail_risk_vel_5d": {"inputs": ["close"], "func": dhrk_296_drawdown_tail_risk_vel_5d},
    "dhrk_297_drawdown_tail_risk_vel_21d": {"inputs": ["close"], "func": dhrk_297_drawdown_tail_risk_vel_21d},
    "dhrk_298_drawdown_tail_risk_vel_63d": {"inputs": ["close"], "func": dhrk_298_drawdown_tail_risk_vel_63d},
    "dhrk_299_drawdown_tail_risk_vel_126d": {"inputs": ["close"], "func": dhrk_299_drawdown_tail_risk_vel_126d},
    "dhrk_300_drawdown_tail_risk_vel_252d": {"inputs": ["close"], "func": dhrk_300_drawdown_tail_risk_vel_252d},
}
