"""
107_change_point_detection — Acceleration (3rd Derivatives)
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

def cpdt_301_mean_shift_detection_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_301_mean_shift_detection_accel_5d
    ECONOMIC RATIONALE: Acceleration of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(5).diff(_TD_MON)

def cpdt_302_mean_shift_detection_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_302_mean_shift_detection_accel_21d
    ECONOMIC RATIONALE: Acceleration of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(21).diff(_TD_MON)

def cpdt_303_mean_shift_detection_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_303_mean_shift_detection_accel_63d
    ECONOMIC RATIONALE: Acceleration of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(63).diff(_TD_MON)

def cpdt_304_mean_shift_detection_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_304_mean_shift_detection_accel_126d
    ECONOMIC RATIONALE: Acceleration of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(126).diff(_TD_MON)

def cpdt_305_mean_shift_detection_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_305_mean_shift_detection_accel_252d
    ECONOMIC RATIONALE: Acceleration of mean_shift_detection. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).diff(252).diff(_TD_MON)

def cpdt_306_vol_regime_shift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_306_vol_regime_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(5).diff(_TD_MON)

def cpdt_307_vol_regime_shift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_307_vol_regime_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(21).diff(_TD_MON)

def cpdt_308_vol_regime_shift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_308_vol_regime_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(63).diff(_TD_MON)

def cpdt_309_vol_regime_shift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_309_vol_regime_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(126).diff(_TD_MON)

def cpdt_310_vol_regime_shift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_310_vol_regime_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_regime_shift. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).diff(252).diff(_TD_MON)

def cpdt_311_cusum_proxy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_311_cusum_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(5).diff(_TD_MON)

def cpdt_312_cusum_proxy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_312_cusum_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(21).diff(_TD_MON)

def cpdt_313_cusum_proxy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_313_cusum_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(63).diff(_TD_MON)

def cpdt_314_cusum_proxy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_314_cusum_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(126).diff(_TD_MON)

def cpdt_315_cusum_proxy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_315_cusum_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of cusum_proxy. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).diff(252).diff(_TD_MON)

def cpdt_316_change_point_z_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_316_change_point_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(5).diff(_TD_MON)

def cpdt_317_change_point_z_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_317_change_point_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(21).diff(_TD_MON)

def cpdt_318_change_point_z_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_318_change_point_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(63).diff(_TD_MON)

def cpdt_319_change_point_z_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_319_change_point_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(126).diff(_TD_MON)

def cpdt_320_change_point_z_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_320_change_point_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of change_point_z. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(252).diff(_TD_MON)

def cpdt_321_trend_regime_change_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_321_trend_regime_change_accel_5d
    ECONOMIC RATIONALE: Acceleration of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(5).diff(_TD_MON)

def cpdt_322_trend_regime_change_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_322_trend_regime_change_accel_21d
    ECONOMIC RATIONALE: Acceleration of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(21).diff(_TD_MON)

def cpdt_323_trend_regime_change_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_323_trend_regime_change_accel_63d
    ECONOMIC RATIONALE: Acceleration of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(63).diff(_TD_MON)

def cpdt_324_trend_regime_change_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_324_trend_regime_change_accel_126d
    ECONOMIC RATIONALE: Acceleration of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(126).diff(_TD_MON)

def cpdt_325_trend_regime_change_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_325_trend_regime_change_accel_252d
    ECONOMIC RATIONALE: Acceleration of trend_regime_change. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).diff(252).diff(_TD_MON)

def cpdt_326_volatility_structural_break_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_326_volatility_structural_break_accel_5d
    ECONOMIC RATIONALE: Acceleration of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(5).diff(_TD_MON)

def cpdt_327_volatility_structural_break_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_327_volatility_structural_break_accel_21d
    ECONOMIC RATIONALE: Acceleration of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(21).diff(_TD_MON)

def cpdt_328_volatility_structural_break_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_328_volatility_structural_break_accel_63d
    ECONOMIC RATIONALE: Acceleration of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(63).diff(_TD_MON)

def cpdt_329_volatility_structural_break_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_329_volatility_structural_break_accel_126d
    ECONOMIC RATIONALE: Acceleration of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(126).diff(_TD_MON)

def cpdt_330_volatility_structural_break_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_330_volatility_structural_break_accel_252d
    ECONOMIC RATIONALE: Acceleration of volatility_structural_break. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).diff(252).diff(_TD_MON)

def cpdt_331_distribution_entropy_shift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_331_distribution_entropy_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(5).diff(_TD_MON)

def cpdt_332_distribution_entropy_shift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_332_distribution_entropy_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(21).diff(_TD_MON)

def cpdt_333_distribution_entropy_shift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_333_distribution_entropy_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(63).diff(_TD_MON)

def cpdt_334_distribution_entropy_shift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_334_distribution_entropy_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(126).diff(_TD_MON)

def cpdt_335_distribution_entropy_shift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_335_distribution_entropy_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of distribution_entropy_shift. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).diff(252).diff(_TD_MON)

def cpdt_336_change_point_momentum_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_336_change_point_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(5).diff(_TD_MON)

def cpdt_337_change_point_momentum_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_337_change_point_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(21).diff(_TD_MON)

def cpdt_338_change_point_momentum_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_338_change_point_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(63).diff(_TD_MON)

def cpdt_339_change_point_momentum_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_339_change_point_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(126).diff(_TD_MON)

def cpdt_340_change_point_momentum_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_340_change_point_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of change_point_momentum. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).diff(252).diff(_TD_MON)

def cpdt_341_volume_regime_break_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_341_volume_regime_break_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(5).diff(_TD_MON)

def cpdt_342_volume_regime_break_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_342_volume_regime_break_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(21).diff(_TD_MON)

def cpdt_343_volume_regime_break_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_343_volume_regime_break_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(63).diff(_TD_MON)

def cpdt_344_volume_regime_break_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_344_volume_regime_break_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(126).diff(_TD_MON)

def cpdt_345_volume_regime_break_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_345_volume_regime_break_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_regime_break. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).diff(252).diff(_TD_MON)

def cpdt_346_price_level_stability_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_346_price_level_stability_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(5).diff(_TD_MON)

def cpdt_347_price_level_stability_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_347_price_level_stability_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(21).diff(_TD_MON)

def cpdt_348_price_level_stability_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_348_price_level_stability_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(63).diff(_TD_MON)

def cpdt_349_price_level_stability_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_349_price_level_stability_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(126).diff(_TD_MON)

def cpdt_350_price_level_stability_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_350_price_level_stability_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_level_stability. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).diff(252).diff(_TD_MON)

def cpdt_351_structural_break_score_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_351_structural_break_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(5).diff(_TD_MON)

def cpdt_352_structural_break_score_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_352_structural_break_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(21).diff(_TD_MON)

def cpdt_353_structural_break_score_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_353_structural_break_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(63).diff(_TD_MON)

def cpdt_354_structural_break_score_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_354_structural_break_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(126).diff(_TD_MON)

def cpdt_355_structural_break_score_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_355_structural_break_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of structural_break_score. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).diff(252).diff(_TD_MON)

def cpdt_356_regime_switching_proxy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_356_regime_switching_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(5).diff(_TD_MON)

def cpdt_357_regime_switching_proxy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_357_regime_switching_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(21).diff(_TD_MON)

def cpdt_358_regime_switching_proxy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_358_regime_switching_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(63).diff(_TD_MON)

def cpdt_359_regime_switching_proxy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_359_regime_switching_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(126).diff(_TD_MON)

def cpdt_360_regime_switching_proxy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_360_regime_switching_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of regime_switching_proxy. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).diff(252).diff(_TD_MON)

def cpdt_361_autocorr_regime_shift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_361_autocorr_regime_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5).diff(_TD_MON)

def cpdt_362_autocorr_regime_shift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_362_autocorr_regime_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21).diff(_TD_MON)

def cpdt_363_autocorr_regime_shift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_363_autocorr_regime_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63).diff(_TD_MON)

def cpdt_364_autocorr_regime_shift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_364_autocorr_regime_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126).diff(_TD_MON)

def cpdt_365_autocorr_regime_shift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_365_autocorr_regime_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_shift. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252).diff(_TD_MON)

def cpdt_366_tail_event_density_change_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_366_tail_event_density_change_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(5).diff(_TD_MON)

def cpdt_367_tail_event_density_change_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_367_tail_event_density_change_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(21).diff(_TD_MON)

def cpdt_368_tail_event_density_change_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_368_tail_event_density_change_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(63).diff(_TD_MON)

def cpdt_369_tail_event_density_change_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_369_tail_event_density_change_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(126).diff(_TD_MON)

def cpdt_370_tail_event_density_change_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_370_tail_event_density_change_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_event_density_change. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).diff(252).diff(_TD_MON)

def cpdt_371_price_volume_regime_corr_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_371_price_volume_regime_corr_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(5).diff(_TD_MON)

def cpdt_372_price_volume_regime_corr_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_372_price_volume_regime_corr_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(21).diff(_TD_MON)

def cpdt_373_price_volume_regime_corr_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_373_price_volume_regime_corr_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(63).diff(_TD_MON)

def cpdt_374_price_volume_regime_corr_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_374_price_volume_regime_corr_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(126).diff(_TD_MON)

def cpdt_375_price_volume_regime_corr_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_375_price_volume_regime_corr_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_volume_regime_corr. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V107_REGISTRY_ACCEL = {
    "cpdt_301_mean_shift_detection_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_301_mean_shift_detection_accel_5d},
    "cpdt_302_mean_shift_detection_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_302_mean_shift_detection_accel_21d},
    "cpdt_303_mean_shift_detection_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_303_mean_shift_detection_accel_63d},
    "cpdt_304_mean_shift_detection_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_304_mean_shift_detection_accel_126d},
    "cpdt_305_mean_shift_detection_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_305_mean_shift_detection_accel_252d},
    "cpdt_306_vol_regime_shift_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_306_vol_regime_shift_accel_5d},
    "cpdt_307_vol_regime_shift_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_307_vol_regime_shift_accel_21d},
    "cpdt_308_vol_regime_shift_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_308_vol_regime_shift_accel_63d},
    "cpdt_309_vol_regime_shift_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_309_vol_regime_shift_accel_126d},
    "cpdt_310_vol_regime_shift_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_310_vol_regime_shift_accel_252d},
    "cpdt_311_cusum_proxy_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_311_cusum_proxy_accel_5d},
    "cpdt_312_cusum_proxy_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_312_cusum_proxy_accel_21d},
    "cpdt_313_cusum_proxy_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_313_cusum_proxy_accel_63d},
    "cpdt_314_cusum_proxy_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_314_cusum_proxy_accel_126d},
    "cpdt_315_cusum_proxy_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_315_cusum_proxy_accel_252d},
    "cpdt_316_change_point_z_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_316_change_point_z_accel_5d},
    "cpdt_317_change_point_z_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_317_change_point_z_accel_21d},
    "cpdt_318_change_point_z_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_318_change_point_z_accel_63d},
    "cpdt_319_change_point_z_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_319_change_point_z_accel_126d},
    "cpdt_320_change_point_z_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_320_change_point_z_accel_252d},
    "cpdt_321_trend_regime_change_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_321_trend_regime_change_accel_5d},
    "cpdt_322_trend_regime_change_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_322_trend_regime_change_accel_21d},
    "cpdt_323_trend_regime_change_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_323_trend_regime_change_accel_63d},
    "cpdt_324_trend_regime_change_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_324_trend_regime_change_accel_126d},
    "cpdt_325_trend_regime_change_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_325_trend_regime_change_accel_252d},
    "cpdt_326_volatility_structural_break_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_326_volatility_structural_break_accel_5d},
    "cpdt_327_volatility_structural_break_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_327_volatility_structural_break_accel_21d},
    "cpdt_328_volatility_structural_break_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_328_volatility_structural_break_accel_63d},
    "cpdt_329_volatility_structural_break_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_329_volatility_structural_break_accel_126d},
    "cpdt_330_volatility_structural_break_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_330_volatility_structural_break_accel_252d},
    "cpdt_331_distribution_entropy_shift_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_331_distribution_entropy_shift_accel_5d},
    "cpdt_332_distribution_entropy_shift_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_332_distribution_entropy_shift_accel_21d},
    "cpdt_333_distribution_entropy_shift_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_333_distribution_entropy_shift_accel_63d},
    "cpdt_334_distribution_entropy_shift_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_334_distribution_entropy_shift_accel_126d},
    "cpdt_335_distribution_entropy_shift_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_335_distribution_entropy_shift_accel_252d},
    "cpdt_336_change_point_momentum_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_336_change_point_momentum_accel_5d},
    "cpdt_337_change_point_momentum_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_337_change_point_momentum_accel_21d},
    "cpdt_338_change_point_momentum_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_338_change_point_momentum_accel_63d},
    "cpdt_339_change_point_momentum_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_339_change_point_momentum_accel_126d},
    "cpdt_340_change_point_momentum_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_340_change_point_momentum_accel_252d},
    "cpdt_341_volume_regime_break_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_341_volume_regime_break_accel_5d},
    "cpdt_342_volume_regime_break_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_342_volume_regime_break_accel_21d},
    "cpdt_343_volume_regime_break_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_343_volume_regime_break_accel_63d},
    "cpdt_344_volume_regime_break_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_344_volume_regime_break_accel_126d},
    "cpdt_345_volume_regime_break_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_345_volume_regime_break_accel_252d},
    "cpdt_346_price_level_stability_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_346_price_level_stability_accel_5d},
    "cpdt_347_price_level_stability_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_347_price_level_stability_accel_21d},
    "cpdt_348_price_level_stability_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_348_price_level_stability_accel_63d},
    "cpdt_349_price_level_stability_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_349_price_level_stability_accel_126d},
    "cpdt_350_price_level_stability_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_350_price_level_stability_accel_252d},
    "cpdt_351_structural_break_score_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_351_structural_break_score_accel_5d},
    "cpdt_352_structural_break_score_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_352_structural_break_score_accel_21d},
    "cpdt_353_structural_break_score_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_353_structural_break_score_accel_63d},
    "cpdt_354_structural_break_score_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_354_structural_break_score_accel_126d},
    "cpdt_355_structural_break_score_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_355_structural_break_score_accel_252d},
    "cpdt_356_regime_switching_proxy_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_356_regime_switching_proxy_accel_5d},
    "cpdt_357_regime_switching_proxy_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_357_regime_switching_proxy_accel_21d},
    "cpdt_358_regime_switching_proxy_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_358_regime_switching_proxy_accel_63d},
    "cpdt_359_regime_switching_proxy_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_359_regime_switching_proxy_accel_126d},
    "cpdt_360_regime_switching_proxy_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_360_regime_switching_proxy_accel_252d},
    "cpdt_361_autocorr_regime_shift_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_361_autocorr_regime_shift_accel_5d},
    "cpdt_362_autocorr_regime_shift_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_362_autocorr_regime_shift_accel_21d},
    "cpdt_363_autocorr_regime_shift_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_363_autocorr_regime_shift_accel_63d},
    "cpdt_364_autocorr_regime_shift_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_364_autocorr_regime_shift_accel_126d},
    "cpdt_365_autocorr_regime_shift_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_365_autocorr_regime_shift_accel_252d},
    "cpdt_366_tail_event_density_change_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_366_tail_event_density_change_accel_5d},
    "cpdt_367_tail_event_density_change_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_367_tail_event_density_change_accel_21d},
    "cpdt_368_tail_event_density_change_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_368_tail_event_density_change_accel_63d},
    "cpdt_369_tail_event_density_change_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_369_tail_event_density_change_accel_126d},
    "cpdt_370_tail_event_density_change_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_370_tail_event_density_change_accel_252d},
    "cpdt_371_price_volume_regime_corr_accel_5d": {"inputs": ["close", "volume"], "func": cpdt_371_price_volume_regime_corr_accel_5d},
    "cpdt_372_price_volume_regime_corr_accel_21d": {"inputs": ["close", "volume"], "func": cpdt_372_price_volume_regime_corr_accel_21d},
    "cpdt_373_price_volume_regime_corr_accel_63d": {"inputs": ["close", "volume"], "func": cpdt_373_price_volume_regime_corr_accel_63d},
    "cpdt_374_price_volume_regime_corr_accel_126d": {"inputs": ["close", "volume"], "func": cpdt_374_price_volume_regime_corr_accel_126d},
    "cpdt_375_price_volume_regime_corr_accel_252d": {"inputs": ["close", "volume"], "func": cpdt_375_price_volume_regime_corr_accel_252d},
}
