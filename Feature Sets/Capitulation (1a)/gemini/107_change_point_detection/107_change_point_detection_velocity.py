"""
107_change_point_detection — Velocity (2nd Derivatives)
Domain: change_point_detection
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

def cpdt_226_mean_shift_detection_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_226_mean_shift_detection_vel_5d
    ECONOMIC RATIONALE: Velocity of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(5)

def cpdt_227_mean_shift_detection_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_227_mean_shift_detection_vel_21d
    ECONOMIC RATIONALE: Velocity of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(21)

def cpdt_228_mean_shift_detection_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_228_mean_shift_detection_vel_63d
    ECONOMIC RATIONALE: Velocity of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(63)

def cpdt_229_mean_shift_detection_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_229_mean_shift_detection_vel_126d
    ECONOMIC RATIONALE: Velocity of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(126)

def cpdt_230_mean_shift_detection_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_230_mean_shift_detection_vel_252d
    ECONOMIC RATIONALE: Velocity of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(252)

def cpdt_231_vol_regime_shift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_231_vol_regime_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(5)

def cpdt_232_vol_regime_shift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_232_vol_regime_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(21)

def cpdt_233_vol_regime_shift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_233_vol_regime_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(63)

def cpdt_234_vol_regime_shift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_234_vol_regime_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(126)

def cpdt_235_vol_regime_shift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_235_vol_regime_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(252)

def cpdt_236_cusum_proxy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_236_cusum_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(5)

def cpdt_237_cusum_proxy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_237_cusum_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(21)

def cpdt_238_cusum_proxy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_238_cusum_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(63)

def cpdt_239_cusum_proxy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_239_cusum_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(126)

def cpdt_240_cusum_proxy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_240_cusum_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(252)

def cpdt_241_change_point_z_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_241_change_point_z_vel_5d
    ECONOMIC RATIONALE: Velocity of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(5)

def cpdt_242_change_point_z_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_242_change_point_z_vel_21d
    ECONOMIC RATIONALE: Velocity of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(21)

def cpdt_243_change_point_z_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_243_change_point_z_vel_63d
    ECONOMIC RATIONALE: Velocity of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(63)

def cpdt_244_change_point_z_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_244_change_point_z_vel_126d
    ECONOMIC RATIONALE: Velocity of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(126)

def cpdt_245_change_point_z_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_245_change_point_z_vel_252d
    ECONOMIC RATIONALE: Velocity of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(252)

def cpdt_246_trend_regime_change_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_246_trend_regime_change_vel_5d
    ECONOMIC RATIONALE: Velocity of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(5)

def cpdt_247_trend_regime_change_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_247_trend_regime_change_vel_21d
    ECONOMIC RATIONALE: Velocity of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(21)

def cpdt_248_trend_regime_change_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_248_trend_regime_change_vel_63d
    ECONOMIC RATIONALE: Velocity of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(63)

def cpdt_249_trend_regime_change_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_249_trend_regime_change_vel_126d
    ECONOMIC RATIONALE: Velocity of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(126)

def cpdt_250_trend_regime_change_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_250_trend_regime_change_vel_252d
    ECONOMIC RATIONALE: Velocity of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(252)

def cpdt_251_volatility_structural_break_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_251_volatility_structural_break_vel_5d
    ECONOMIC RATIONALE: Velocity of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(5)

def cpdt_252_volatility_structural_break_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_252_volatility_structural_break_vel_21d
    ECONOMIC RATIONALE: Velocity of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(21)

def cpdt_253_volatility_structural_break_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_253_volatility_structural_break_vel_63d
    ECONOMIC RATIONALE: Velocity of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(63)

def cpdt_254_volatility_structural_break_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_254_volatility_structural_break_vel_126d
    ECONOMIC RATIONALE: Velocity of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(126)

def cpdt_255_volatility_structural_break_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_255_volatility_structural_break_vel_252d
    ECONOMIC RATIONALE: Velocity of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(252)

def cpdt_256_distribution_entropy_shift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_256_distribution_entropy_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(5)

def cpdt_257_distribution_entropy_shift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_257_distribution_entropy_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(21)

def cpdt_258_distribution_entropy_shift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_258_distribution_entropy_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(63)

def cpdt_259_distribution_entropy_shift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_259_distribution_entropy_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(126)

def cpdt_260_distribution_entropy_shift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_260_distribution_entropy_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(252)

def cpdt_261_change_point_momentum_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_261_change_point_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(5)

def cpdt_262_change_point_momentum_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_262_change_point_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(21)

def cpdt_263_change_point_momentum_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_263_change_point_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(63)

def cpdt_264_change_point_momentum_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_264_change_point_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(126)

def cpdt_265_change_point_momentum_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_265_change_point_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(252)

def cpdt_266_volume_regime_break_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_266_volume_regime_break_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(5)

def cpdt_267_volume_regime_break_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_267_volume_regime_break_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(21)

def cpdt_268_volume_regime_break_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_268_volume_regime_break_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(63)

def cpdt_269_volume_regime_break_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_269_volume_regime_break_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(126)

def cpdt_270_volume_regime_break_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_270_volume_regime_break_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(252)

def cpdt_271_price_level_stability_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_271_price_level_stability_vel_5d
    ECONOMIC RATIONALE: Velocity of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(5)

def cpdt_272_price_level_stability_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_272_price_level_stability_vel_21d
    ECONOMIC RATIONALE: Velocity of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(21)

def cpdt_273_price_level_stability_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_273_price_level_stability_vel_63d
    ECONOMIC RATIONALE: Velocity of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(63)

def cpdt_274_price_level_stability_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_274_price_level_stability_vel_126d
    ECONOMIC RATIONALE: Velocity of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(126)

def cpdt_275_price_level_stability_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_275_price_level_stability_vel_252d
    ECONOMIC RATIONALE: Velocity of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(252)

def cpdt_276_structural_break_score_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_276_structural_break_score_vel_5d
    ECONOMIC RATIONALE: Velocity of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(5)

def cpdt_277_structural_break_score_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_277_structural_break_score_vel_21d
    ECONOMIC RATIONALE: Velocity of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(21)

def cpdt_278_structural_break_score_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_278_structural_break_score_vel_63d
    ECONOMIC RATIONALE: Velocity of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(63)

def cpdt_279_structural_break_score_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_279_structural_break_score_vel_126d
    ECONOMIC RATIONALE: Velocity of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(126)

def cpdt_280_structural_break_score_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_280_structural_break_score_vel_252d
    ECONOMIC RATIONALE: Velocity of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(252)

def cpdt_281_regime_switching_proxy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_281_regime_switching_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(5)

def cpdt_282_regime_switching_proxy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_282_regime_switching_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(21)

def cpdt_283_regime_switching_proxy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_283_regime_switching_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(63)

def cpdt_284_regime_switching_proxy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_284_regime_switching_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(126)

def cpdt_285_regime_switching_proxy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_285_regime_switching_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(252)

def cpdt_286_autocorr_regime_shift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_286_autocorr_regime_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5)

def cpdt_287_autocorr_regime_shift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_287_autocorr_regime_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21)

def cpdt_288_autocorr_regime_shift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_288_autocorr_regime_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63)

def cpdt_289_autocorr_regime_shift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_289_autocorr_regime_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126)

def cpdt_290_autocorr_regime_shift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_290_autocorr_regime_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252)

def cpdt_291_tail_event_density_change_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_291_tail_event_density_change_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(5)

def cpdt_292_tail_event_density_change_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_292_tail_event_density_change_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(21)

def cpdt_293_tail_event_density_change_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_293_tail_event_density_change_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(63)

def cpdt_294_tail_event_density_change_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_294_tail_event_density_change_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(126)

def cpdt_295_tail_event_density_change_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_295_tail_event_density_change_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(252)

def cpdt_296_price_volume_regime_corr_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_296_price_volume_regime_corr_vel_5d
    ECONOMIC RATIONALE: Velocity of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(5)

def cpdt_297_price_volume_regime_corr_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_297_price_volume_regime_corr_vel_21d
    ECONOMIC RATIONALE: Velocity of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(21)

def cpdt_298_price_volume_regime_corr_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_298_price_volume_regime_corr_vel_63d
    ECONOMIC RATIONALE: Velocity of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(63)

def cpdt_299_price_volume_regime_corr_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_299_price_volume_regime_corr_vel_126d
    ECONOMIC RATIONALE: Velocity of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(126)

def cpdt_300_price_volume_regime_corr_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_300_price_volume_regime_corr_vel_252d
    ECONOMIC RATIONALE: Velocity of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V107_REGISTRY_VEL = {
    "cpdt_226_mean_shift_detection_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_226_mean_shift_detection_vel_5d},
    "cpdt_227_mean_shift_detection_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_227_mean_shift_detection_vel_21d},
    "cpdt_228_mean_shift_detection_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_228_mean_shift_detection_vel_63d},
    "cpdt_229_mean_shift_detection_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_229_mean_shift_detection_vel_126d},
    "cpdt_230_mean_shift_detection_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_230_mean_shift_detection_vel_252d},
    "cpdt_231_vol_regime_shift_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_231_vol_regime_shift_vel_5d},
    "cpdt_232_vol_regime_shift_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_232_vol_regime_shift_vel_21d},
    "cpdt_233_vol_regime_shift_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_233_vol_regime_shift_vel_63d},
    "cpdt_234_vol_regime_shift_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_234_vol_regime_shift_vel_126d},
    "cpdt_235_vol_regime_shift_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_235_vol_regime_shift_vel_252d},
    "cpdt_236_cusum_proxy_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_236_cusum_proxy_vel_5d},
    "cpdt_237_cusum_proxy_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_237_cusum_proxy_vel_21d},
    "cpdt_238_cusum_proxy_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_238_cusum_proxy_vel_63d},
    "cpdt_239_cusum_proxy_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_239_cusum_proxy_vel_126d},
    "cpdt_240_cusum_proxy_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_240_cusum_proxy_vel_252d},
    "cpdt_241_change_point_z_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_241_change_point_z_vel_5d},
    "cpdt_242_change_point_z_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_242_change_point_z_vel_21d},
    "cpdt_243_change_point_z_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_243_change_point_z_vel_63d},
    "cpdt_244_change_point_z_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_244_change_point_z_vel_126d},
    "cpdt_245_change_point_z_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_245_change_point_z_vel_252d},
    "cpdt_246_trend_regime_change_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_246_trend_regime_change_vel_5d},
    "cpdt_247_trend_regime_change_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_247_trend_regime_change_vel_21d},
    "cpdt_248_trend_regime_change_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_248_trend_regime_change_vel_63d},
    "cpdt_249_trend_regime_change_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_249_trend_regime_change_vel_126d},
    "cpdt_250_trend_regime_change_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_250_trend_regime_change_vel_252d},
    "cpdt_251_volatility_structural_break_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_251_volatility_structural_break_vel_5d},
    "cpdt_252_volatility_structural_break_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_252_volatility_structural_break_vel_21d},
    "cpdt_253_volatility_structural_break_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_253_volatility_structural_break_vel_63d},
    "cpdt_254_volatility_structural_break_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_254_volatility_structural_break_vel_126d},
    "cpdt_255_volatility_structural_break_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_255_volatility_structural_break_vel_252d},
    "cpdt_256_distribution_entropy_shift_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_256_distribution_entropy_shift_vel_5d},
    "cpdt_257_distribution_entropy_shift_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_257_distribution_entropy_shift_vel_21d},
    "cpdt_258_distribution_entropy_shift_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_258_distribution_entropy_shift_vel_63d},
    "cpdt_259_distribution_entropy_shift_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_259_distribution_entropy_shift_vel_126d},
    "cpdt_260_distribution_entropy_shift_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_260_distribution_entropy_shift_vel_252d},
    "cpdt_261_change_point_momentum_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_261_change_point_momentum_vel_5d},
    "cpdt_262_change_point_momentum_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_262_change_point_momentum_vel_21d},
    "cpdt_263_change_point_momentum_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_263_change_point_momentum_vel_63d},
    "cpdt_264_change_point_momentum_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_264_change_point_momentum_vel_126d},
    "cpdt_265_change_point_momentum_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_265_change_point_momentum_vel_252d},
    "cpdt_266_volume_regime_break_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_266_volume_regime_break_vel_5d},
    "cpdt_267_volume_regime_break_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_267_volume_regime_break_vel_21d},
    "cpdt_268_volume_regime_break_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_268_volume_regime_break_vel_63d},
    "cpdt_269_volume_regime_break_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_269_volume_regime_break_vel_126d},
    "cpdt_270_volume_regime_break_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_270_volume_regime_break_vel_252d},
    "cpdt_271_price_level_stability_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_271_price_level_stability_vel_5d},
    "cpdt_272_price_level_stability_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_272_price_level_stability_vel_21d},
    "cpdt_273_price_level_stability_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_273_price_level_stability_vel_63d},
    "cpdt_274_price_level_stability_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_274_price_level_stability_vel_126d},
    "cpdt_275_price_level_stability_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_275_price_level_stability_vel_252d},
    "cpdt_276_structural_break_score_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_276_structural_break_score_vel_5d},
    "cpdt_277_structural_break_score_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_277_structural_break_score_vel_21d},
    "cpdt_278_structural_break_score_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_278_structural_break_score_vel_63d},
    "cpdt_279_structural_break_score_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_279_structural_break_score_vel_126d},
    "cpdt_280_structural_break_score_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_280_structural_break_score_vel_252d},
    "cpdt_281_regime_switching_proxy_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_281_regime_switching_proxy_vel_5d},
    "cpdt_282_regime_switching_proxy_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_282_regime_switching_proxy_vel_21d},
    "cpdt_283_regime_switching_proxy_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_283_regime_switching_proxy_vel_63d},
    "cpdt_284_regime_switching_proxy_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_284_regime_switching_proxy_vel_126d},
    "cpdt_285_regime_switching_proxy_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_285_regime_switching_proxy_vel_252d},
    "cpdt_286_autocorr_regime_shift_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_286_autocorr_regime_shift_vel_5d},
    "cpdt_287_autocorr_regime_shift_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_287_autocorr_regime_shift_vel_21d},
    "cpdt_288_autocorr_regime_shift_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_288_autocorr_regime_shift_vel_63d},
    "cpdt_289_autocorr_regime_shift_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_289_autocorr_regime_shift_vel_126d},
    "cpdt_290_autocorr_regime_shift_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_290_autocorr_regime_shift_vel_252d},
    "cpdt_291_tail_event_density_change_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_291_tail_event_density_change_vel_5d},
    "cpdt_292_tail_event_density_change_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_292_tail_event_density_change_vel_21d},
    "cpdt_293_tail_event_density_change_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_293_tail_event_density_change_vel_63d},
    "cpdt_294_tail_event_density_change_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_294_tail_event_density_change_vel_126d},
    "cpdt_295_tail_event_density_change_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_295_tail_event_density_change_vel_252d},
    "cpdt_296_price_volume_regime_corr_vel_5d": {"inputs": ["close", "volume"], "func": cpdt_296_price_volume_regime_corr_vel_5d},
    "cpdt_297_price_volume_regime_corr_vel_21d": {"inputs": ["close", "volume"], "func": cpdt_297_price_volume_regime_corr_vel_21d},
    "cpdt_298_price_volume_regime_corr_vel_63d": {"inputs": ["close", "volume"], "func": cpdt_298_price_volume_regime_corr_vel_63d},
    "cpdt_299_price_volume_regime_corr_vel_126d": {"inputs": ["close", "volume"], "func": cpdt_299_price_volume_regime_corr_vel_126d},
    "cpdt_300_price_volume_regime_corr_vel_252d": {"inputs": ["close", "volume"], "func": cpdt_300_price_volume_regime_corr_vel_252d},
}
