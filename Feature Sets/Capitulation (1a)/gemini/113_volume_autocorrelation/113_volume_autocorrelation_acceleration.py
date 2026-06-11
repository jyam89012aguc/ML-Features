"""
113_volume_autocorrelation — Acceleration (3rd Derivatives)
Domain: volume_autocorrelation
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

def vaut_301_vol_lag1_autocorr_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_301_vol_lag1_autocorr_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5).diff(_TD_MON)

def vaut_302_vol_lag1_autocorr_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_302_vol_lag1_autocorr_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21).diff(_TD_MON)

def vaut_303_vol_lag1_autocorr_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_303_vol_lag1_autocorr_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63).diff(_TD_MON)

def vaut_304_vol_lag1_autocorr_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_304_vol_lag1_autocorr_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126).diff(_TD_MON)

def vaut_305_vol_lag1_autocorr_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_305_vol_lag1_autocorr_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252).diff(_TD_MON)

def vaut_306_vol_autocorr_zscore_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_306_vol_autocorr_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5).diff(_TD_MON)

def vaut_307_vol_autocorr_zscore_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_307_vol_autocorr_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21).diff(_TD_MON)

def vaut_308_vol_autocorr_zscore_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_308_vol_autocorr_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63).diff(_TD_MON)

def vaut_309_vol_autocorr_zscore_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_309_vol_autocorr_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126).diff(_TD_MON)

def vaut_310_vol_autocorr_zscore_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_310_vol_autocorr_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252).diff(_TD_MON)

def vaut_311_vol_persistence_trend_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_311_vol_persistence_trend_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5).diff(_TD_MON)

def vaut_312_vol_persistence_trend_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_312_vol_persistence_trend_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21).diff(_TD_MON)

def vaut_313_vol_persistence_trend_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_313_vol_persistence_trend_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63).diff(_TD_MON)

def vaut_314_vol_persistence_trend_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_314_vol_persistence_trend_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126).diff(_TD_MON)

def vaut_315_vol_persistence_trend_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_315_vol_persistence_trend_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252).diff(_TD_MON)

def vaut_316_vol_clustering_index_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_316_vol_clustering_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(5).diff(_TD_MON)

def vaut_317_vol_clustering_index_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_317_vol_clustering_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(21).diff(_TD_MON)

def vaut_318_vol_clustering_index_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_318_vol_clustering_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(63).diff(_TD_MON)

def vaut_319_vol_clustering_index_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_319_vol_clustering_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(126).diff(_TD_MON)

def vaut_320_vol_clustering_index_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_320_vol_clustering_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(252).diff(_TD_MON)

def vaut_321_vol_autocorr_rank_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_321_vol_autocorr_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5).diff(_TD_MON)

def vaut_322_vol_autocorr_rank_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_322_vol_autocorr_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21).diff(_TD_MON)

def vaut_323_vol_autocorr_rank_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_323_vol_autocorr_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63).diff(_TD_MON)

def vaut_324_vol_autocorr_rank_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_324_vol_autocorr_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126).diff(_TD_MON)

def vaut_325_vol_autocorr_rank_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_325_vol_autocorr_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252).diff(_TD_MON)

def vaut_326_vol_autocorr_stability_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_326_vol_autocorr_stability_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(5).diff(_TD_MON)

def vaut_327_vol_autocorr_stability_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_327_vol_autocorr_stability_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(21).diff(_TD_MON)

def vaut_328_vol_autocorr_stability_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_328_vol_autocorr_stability_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(63).diff(_TD_MON)

def vaut_329_vol_autocorr_stability_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_329_vol_autocorr_stability_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(126).diff(_TD_MON)

def vaut_330_vol_autocorr_stability_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_330_vol_autocorr_stability_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(252).diff(_TD_MON)

def vaut_331_vol_autocorr_acceleration_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_331_vol_autocorr_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(5).diff(_TD_MON)

def vaut_332_vol_autocorr_acceleration_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_332_vol_autocorr_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(21).diff(_TD_MON)

def vaut_333_vol_autocorr_acceleration_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_333_vol_autocorr_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(63).diff(_TD_MON)

def vaut_334_vol_autocorr_acceleration_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_334_vol_autocorr_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(126).diff(_TD_MON)

def vaut_335_vol_autocorr_acceleration_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_335_vol_autocorr_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(252).diff(_TD_MON)

def vaut_336_vol_mean_reversion_flag_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_336_vol_mean_reversion_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(5).diff(_TD_MON)

def vaut_337_vol_mean_reversion_flag_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_337_vol_mean_reversion_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(21).diff(_TD_MON)

def vaut_338_vol_mean_reversion_flag_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_338_vol_mean_reversion_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(63).diff(_TD_MON)

def vaut_339_vol_mean_reversion_flag_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_339_vol_mean_reversion_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(126).diff(_TD_MON)

def vaut_340_vol_mean_reversion_flag_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_340_vol_mean_reversion_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(252).diff(_TD_MON)

def vaut_341_vol_trend_persistence_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_341_vol_trend_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(5).diff(_TD_MON)

def vaut_342_vol_trend_persistence_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_342_vol_trend_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(21).diff(_TD_MON)

def vaut_343_vol_trend_persistence_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_343_vol_trend_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(63).diff(_TD_MON)

def vaut_344_vol_trend_persistence_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_344_vol_trend_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(126).diff(_TD_MON)

def vaut_345_vol_trend_persistence_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_345_vol_trend_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(252).diff(_TD_MON)

def vaut_346_vol_autocorr_vs_price_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_346_vol_autocorr_vs_price_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(5).diff(_TD_MON)

def vaut_347_vol_autocorr_vs_price_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_347_vol_autocorr_vs_price_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(21).diff(_TD_MON)

def vaut_348_vol_autocorr_vs_price_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_348_vol_autocorr_vs_price_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(63).diff(_TD_MON)

def vaut_349_vol_autocorr_vs_price_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_349_vol_autocorr_vs_price_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(126).diff(_TD_MON)

def vaut_350_vol_autocorr_vs_price_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_350_vol_autocorr_vs_price_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(252).diff(_TD_MON)

def vaut_351_vol_autocorr_peak_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_351_vol_autocorr_peak_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(5).diff(_TD_MON)

def vaut_352_vol_autocorr_peak_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_352_vol_autocorr_peak_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(21).diff(_TD_MON)

def vaut_353_vol_autocorr_peak_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_353_vol_autocorr_peak_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(63).diff(_TD_MON)

def vaut_354_vol_autocorr_peak_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_354_vol_autocorr_peak_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(126).diff(_TD_MON)

def vaut_355_vol_autocorr_peak_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_355_vol_autocorr_peak_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(252).diff(_TD_MON)

def vaut_356_vol_autocorr_entropy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_356_vol_autocorr_entropy_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(5).diff(_TD_MON)

def vaut_357_vol_autocorr_entropy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_357_vol_autocorr_entropy_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(21).diff(_TD_MON)

def vaut_358_vol_autocorr_entropy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_358_vol_autocorr_entropy_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(63).diff(_TD_MON)

def vaut_359_vol_autocorr_entropy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_359_vol_autocorr_entropy_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(126).diff(_TD_MON)

def vaut_360_vol_autocorr_entropy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_360_vol_autocorr_entropy_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(252).diff(_TD_MON)

def vaut_361_vol_autocorr_regime_switch_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_361_vol_autocorr_regime_switch_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(5).diff(_TD_MON)

def vaut_362_vol_autocorr_regime_switch_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_362_vol_autocorr_regime_switch_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(21).diff(_TD_MON)

def vaut_363_vol_autocorr_regime_switch_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_363_vol_autocorr_regime_switch_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(63).diff(_TD_MON)

def vaut_364_vol_autocorr_regime_switch_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_364_vol_autocorr_regime_switch_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(126).diff(_TD_MON)

def vaut_365_vol_autocorr_regime_switch_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_365_vol_autocorr_regime_switch_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(252).diff(_TD_MON)

def vaut_366_vol_autocorr_ma_spread_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_366_vol_autocorr_ma_spread_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(5).diff(_TD_MON)

def vaut_367_vol_autocorr_ma_spread_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_367_vol_autocorr_ma_spread_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(21).diff(_TD_MON)

def vaut_368_vol_autocorr_ma_spread_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_368_vol_autocorr_ma_spread_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(63).diff(_TD_MON)

def vaut_369_vol_autocorr_ma_spread_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_369_vol_autocorr_ma_spread_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(126).diff(_TD_MON)

def vaut_370_vol_autocorr_ma_spread_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_370_vol_autocorr_ma_spread_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(252).diff(_TD_MON)

def vaut_371_vol_autocorr_low_liquidity_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_371_vol_autocorr_low_liquidity_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(5).diff(_TD_MON)

def vaut_372_vol_autocorr_low_liquidity_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_372_vol_autocorr_low_liquidity_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(21).diff(_TD_MON)

def vaut_373_vol_autocorr_low_liquidity_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_373_vol_autocorr_low_liquidity_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(63).diff(_TD_MON)

def vaut_374_vol_autocorr_low_liquidity_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_374_vol_autocorr_low_liquidity_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(126).diff(_TD_MON)

def vaut_375_vol_autocorr_low_liquidity_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_375_vol_autocorr_low_liquidity_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V113_REGISTRY_ACCEL = {
    "vaut_301_vol_lag1_autocorr_accel_5d": {"inputs": ["close", "volume"], "func": vaut_301_vol_lag1_autocorr_accel_5d},
    "vaut_302_vol_lag1_autocorr_accel_21d": {"inputs": ["close", "volume"], "func": vaut_302_vol_lag1_autocorr_accel_21d},
    "vaut_303_vol_lag1_autocorr_accel_63d": {"inputs": ["close", "volume"], "func": vaut_303_vol_lag1_autocorr_accel_63d},
    "vaut_304_vol_lag1_autocorr_accel_126d": {"inputs": ["close", "volume"], "func": vaut_304_vol_lag1_autocorr_accel_126d},
    "vaut_305_vol_lag1_autocorr_accel_252d": {"inputs": ["close", "volume"], "func": vaut_305_vol_lag1_autocorr_accel_252d},
    "vaut_306_vol_autocorr_zscore_accel_5d": {"inputs": ["close", "volume"], "func": vaut_306_vol_autocorr_zscore_accel_5d},
    "vaut_307_vol_autocorr_zscore_accel_21d": {"inputs": ["close", "volume"], "func": vaut_307_vol_autocorr_zscore_accel_21d},
    "vaut_308_vol_autocorr_zscore_accel_63d": {"inputs": ["close", "volume"], "func": vaut_308_vol_autocorr_zscore_accel_63d},
    "vaut_309_vol_autocorr_zscore_accel_126d": {"inputs": ["close", "volume"], "func": vaut_309_vol_autocorr_zscore_accel_126d},
    "vaut_310_vol_autocorr_zscore_accel_252d": {"inputs": ["close", "volume"], "func": vaut_310_vol_autocorr_zscore_accel_252d},
    "vaut_311_vol_persistence_trend_accel_5d": {"inputs": ["close", "volume"], "func": vaut_311_vol_persistence_trend_accel_5d},
    "vaut_312_vol_persistence_trend_accel_21d": {"inputs": ["close", "volume"], "func": vaut_312_vol_persistence_trend_accel_21d},
    "vaut_313_vol_persistence_trend_accel_63d": {"inputs": ["close", "volume"], "func": vaut_313_vol_persistence_trend_accel_63d},
    "vaut_314_vol_persistence_trend_accel_126d": {"inputs": ["close", "volume"], "func": vaut_314_vol_persistence_trend_accel_126d},
    "vaut_315_vol_persistence_trend_accel_252d": {"inputs": ["close", "volume"], "func": vaut_315_vol_persistence_trend_accel_252d},
    "vaut_316_vol_clustering_index_accel_5d": {"inputs": ["close", "volume"], "func": vaut_316_vol_clustering_index_accel_5d},
    "vaut_317_vol_clustering_index_accel_21d": {"inputs": ["close", "volume"], "func": vaut_317_vol_clustering_index_accel_21d},
    "vaut_318_vol_clustering_index_accel_63d": {"inputs": ["close", "volume"], "func": vaut_318_vol_clustering_index_accel_63d},
    "vaut_319_vol_clustering_index_accel_126d": {"inputs": ["close", "volume"], "func": vaut_319_vol_clustering_index_accel_126d},
    "vaut_320_vol_clustering_index_accel_252d": {"inputs": ["close", "volume"], "func": vaut_320_vol_clustering_index_accel_252d},
    "vaut_321_vol_autocorr_rank_accel_5d": {"inputs": ["close", "volume"], "func": vaut_321_vol_autocorr_rank_accel_5d},
    "vaut_322_vol_autocorr_rank_accel_21d": {"inputs": ["close", "volume"], "func": vaut_322_vol_autocorr_rank_accel_21d},
    "vaut_323_vol_autocorr_rank_accel_63d": {"inputs": ["close", "volume"], "func": vaut_323_vol_autocorr_rank_accel_63d},
    "vaut_324_vol_autocorr_rank_accel_126d": {"inputs": ["close", "volume"], "func": vaut_324_vol_autocorr_rank_accel_126d},
    "vaut_325_vol_autocorr_rank_accel_252d": {"inputs": ["close", "volume"], "func": vaut_325_vol_autocorr_rank_accel_252d},
    "vaut_326_vol_autocorr_stability_accel_5d": {"inputs": ["close", "volume"], "func": vaut_326_vol_autocorr_stability_accel_5d},
    "vaut_327_vol_autocorr_stability_accel_21d": {"inputs": ["close", "volume"], "func": vaut_327_vol_autocorr_stability_accel_21d},
    "vaut_328_vol_autocorr_stability_accel_63d": {"inputs": ["close", "volume"], "func": vaut_328_vol_autocorr_stability_accel_63d},
    "vaut_329_vol_autocorr_stability_accel_126d": {"inputs": ["close", "volume"], "func": vaut_329_vol_autocorr_stability_accel_126d},
    "vaut_330_vol_autocorr_stability_accel_252d": {"inputs": ["close", "volume"], "func": vaut_330_vol_autocorr_stability_accel_252d},
    "vaut_331_vol_autocorr_acceleration_accel_5d": {"inputs": ["close", "volume"], "func": vaut_331_vol_autocorr_acceleration_accel_5d},
    "vaut_332_vol_autocorr_acceleration_accel_21d": {"inputs": ["close", "volume"], "func": vaut_332_vol_autocorr_acceleration_accel_21d},
    "vaut_333_vol_autocorr_acceleration_accel_63d": {"inputs": ["close", "volume"], "func": vaut_333_vol_autocorr_acceleration_accel_63d},
    "vaut_334_vol_autocorr_acceleration_accel_126d": {"inputs": ["close", "volume"], "func": vaut_334_vol_autocorr_acceleration_accel_126d},
    "vaut_335_vol_autocorr_acceleration_accel_252d": {"inputs": ["close", "volume"], "func": vaut_335_vol_autocorr_acceleration_accel_252d},
    "vaut_336_vol_mean_reversion_flag_accel_5d": {"inputs": ["close", "volume"], "func": vaut_336_vol_mean_reversion_flag_accel_5d},
    "vaut_337_vol_mean_reversion_flag_accel_21d": {"inputs": ["close", "volume"], "func": vaut_337_vol_mean_reversion_flag_accel_21d},
    "vaut_338_vol_mean_reversion_flag_accel_63d": {"inputs": ["close", "volume"], "func": vaut_338_vol_mean_reversion_flag_accel_63d},
    "vaut_339_vol_mean_reversion_flag_accel_126d": {"inputs": ["close", "volume"], "func": vaut_339_vol_mean_reversion_flag_accel_126d},
    "vaut_340_vol_mean_reversion_flag_accel_252d": {"inputs": ["close", "volume"], "func": vaut_340_vol_mean_reversion_flag_accel_252d},
    "vaut_341_vol_trend_persistence_accel_5d": {"inputs": ["close", "volume"], "func": vaut_341_vol_trend_persistence_accel_5d},
    "vaut_342_vol_trend_persistence_accel_21d": {"inputs": ["close", "volume"], "func": vaut_342_vol_trend_persistence_accel_21d},
    "vaut_343_vol_trend_persistence_accel_63d": {"inputs": ["close", "volume"], "func": vaut_343_vol_trend_persistence_accel_63d},
    "vaut_344_vol_trend_persistence_accel_126d": {"inputs": ["close", "volume"], "func": vaut_344_vol_trend_persistence_accel_126d},
    "vaut_345_vol_trend_persistence_accel_252d": {"inputs": ["close", "volume"], "func": vaut_345_vol_trend_persistence_accel_252d},
    "vaut_346_vol_autocorr_vs_price_accel_5d": {"inputs": ["close", "volume"], "func": vaut_346_vol_autocorr_vs_price_accel_5d},
    "vaut_347_vol_autocorr_vs_price_accel_21d": {"inputs": ["close", "volume"], "func": vaut_347_vol_autocorr_vs_price_accel_21d},
    "vaut_348_vol_autocorr_vs_price_accel_63d": {"inputs": ["close", "volume"], "func": vaut_348_vol_autocorr_vs_price_accel_63d},
    "vaut_349_vol_autocorr_vs_price_accel_126d": {"inputs": ["close", "volume"], "func": vaut_349_vol_autocorr_vs_price_accel_126d},
    "vaut_350_vol_autocorr_vs_price_accel_252d": {"inputs": ["close", "volume"], "func": vaut_350_vol_autocorr_vs_price_accel_252d},
    "vaut_351_vol_autocorr_peak_accel_5d": {"inputs": ["close", "volume"], "func": vaut_351_vol_autocorr_peak_accel_5d},
    "vaut_352_vol_autocorr_peak_accel_21d": {"inputs": ["close", "volume"], "func": vaut_352_vol_autocorr_peak_accel_21d},
    "vaut_353_vol_autocorr_peak_accel_63d": {"inputs": ["close", "volume"], "func": vaut_353_vol_autocorr_peak_accel_63d},
    "vaut_354_vol_autocorr_peak_accel_126d": {"inputs": ["close", "volume"], "func": vaut_354_vol_autocorr_peak_accel_126d},
    "vaut_355_vol_autocorr_peak_accel_252d": {"inputs": ["close", "volume"], "func": vaut_355_vol_autocorr_peak_accel_252d},
    "vaut_356_vol_autocorr_entropy_accel_5d": {"inputs": ["close", "volume"], "func": vaut_356_vol_autocorr_entropy_accel_5d},
    "vaut_357_vol_autocorr_entropy_accel_21d": {"inputs": ["close", "volume"], "func": vaut_357_vol_autocorr_entropy_accel_21d},
    "vaut_358_vol_autocorr_entropy_accel_63d": {"inputs": ["close", "volume"], "func": vaut_358_vol_autocorr_entropy_accel_63d},
    "vaut_359_vol_autocorr_entropy_accel_126d": {"inputs": ["close", "volume"], "func": vaut_359_vol_autocorr_entropy_accel_126d},
    "vaut_360_vol_autocorr_entropy_accel_252d": {"inputs": ["close", "volume"], "func": vaut_360_vol_autocorr_entropy_accel_252d},
    "vaut_361_vol_autocorr_regime_switch_accel_5d": {"inputs": ["close", "volume"], "func": vaut_361_vol_autocorr_regime_switch_accel_5d},
    "vaut_362_vol_autocorr_regime_switch_accel_21d": {"inputs": ["close", "volume"], "func": vaut_362_vol_autocorr_regime_switch_accel_21d},
    "vaut_363_vol_autocorr_regime_switch_accel_63d": {"inputs": ["close", "volume"], "func": vaut_363_vol_autocorr_regime_switch_accel_63d},
    "vaut_364_vol_autocorr_regime_switch_accel_126d": {"inputs": ["close", "volume"], "func": vaut_364_vol_autocorr_regime_switch_accel_126d},
    "vaut_365_vol_autocorr_regime_switch_accel_252d": {"inputs": ["close", "volume"], "func": vaut_365_vol_autocorr_regime_switch_accel_252d},
    "vaut_366_vol_autocorr_ma_spread_accel_5d": {"inputs": ["close", "volume"], "func": vaut_366_vol_autocorr_ma_spread_accel_5d},
    "vaut_367_vol_autocorr_ma_spread_accel_21d": {"inputs": ["close", "volume"], "func": vaut_367_vol_autocorr_ma_spread_accel_21d},
    "vaut_368_vol_autocorr_ma_spread_accel_63d": {"inputs": ["close", "volume"], "func": vaut_368_vol_autocorr_ma_spread_accel_63d},
    "vaut_369_vol_autocorr_ma_spread_accel_126d": {"inputs": ["close", "volume"], "func": vaut_369_vol_autocorr_ma_spread_accel_126d},
    "vaut_370_vol_autocorr_ma_spread_accel_252d": {"inputs": ["close", "volume"], "func": vaut_370_vol_autocorr_ma_spread_accel_252d},
    "vaut_371_vol_autocorr_low_liquidity_accel_5d": {"inputs": ["close", "volume"], "func": vaut_371_vol_autocorr_low_liquidity_accel_5d},
    "vaut_372_vol_autocorr_low_liquidity_accel_21d": {"inputs": ["close", "volume"], "func": vaut_372_vol_autocorr_low_liquidity_accel_21d},
    "vaut_373_vol_autocorr_low_liquidity_accel_63d": {"inputs": ["close", "volume"], "func": vaut_373_vol_autocorr_low_liquidity_accel_63d},
    "vaut_374_vol_autocorr_low_liquidity_accel_126d": {"inputs": ["close", "volume"], "func": vaut_374_vol_autocorr_low_liquidity_accel_126d},
    "vaut_375_vol_autocorr_low_liquidity_accel_252d": {"inputs": ["close", "volume"], "func": vaut_375_vol_autocorr_low_liquidity_accel_252d},
}
