"""
113_volume_autocorrelation — Velocity (2nd Derivatives)
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

def vaut_226_vol_lag1_autocorr_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_226_vol_lag1_autocorr_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5)

def vaut_227_vol_lag1_autocorr_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_227_vol_lag1_autocorr_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21)

def vaut_228_vol_lag1_autocorr_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_228_vol_lag1_autocorr_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63)

def vaut_229_vol_lag1_autocorr_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_229_vol_lag1_autocorr_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126)

def vaut_230_vol_lag1_autocorr_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_230_vol_lag1_autocorr_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_lag1_autocorr. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252)

def vaut_231_vol_autocorr_zscore_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_231_vol_autocorr_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5)

def vaut_232_vol_autocorr_zscore_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_232_vol_autocorr_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21)

def vaut_233_vol_autocorr_zscore_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_233_vol_autocorr_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63)

def vaut_234_vol_autocorr_zscore_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_234_vol_autocorr_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126)

def vaut_235_vol_autocorr_zscore_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_235_vol_autocorr_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_zscore. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252)

def vaut_236_vol_persistence_trend_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_236_vol_persistence_trend_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5)

def vaut_237_vol_persistence_trend_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_237_vol_persistence_trend_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21)

def vaut_238_vol_persistence_trend_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_238_vol_persistence_trend_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63)

def vaut_239_vol_persistence_trend_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_239_vol_persistence_trend_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126)

def vaut_240_vol_persistence_trend_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_240_vol_persistence_trend_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_persistence_trend. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252)

def vaut_241_vol_clustering_index_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_241_vol_clustering_index_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(5)

def vaut_242_vol_clustering_index_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_242_vol_clustering_index_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(21)

def vaut_243_vol_clustering_index_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_243_vol_clustering_index_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(63)

def vaut_244_vol_clustering_index_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_244_vol_clustering_index_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(126)

def vaut_245_vol_clustering_index_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_245_vol_clustering_index_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_clustering_index. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).diff(252)

def vaut_246_vol_autocorr_rank_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_246_vol_autocorr_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5)

def vaut_247_vol_autocorr_rank_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_247_vol_autocorr_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21)

def vaut_248_vol_autocorr_rank_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_248_vol_autocorr_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63)

def vaut_249_vol_autocorr_rank_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_249_vol_autocorr_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126)

def vaut_250_vol_autocorr_rank_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_250_vol_autocorr_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_rank. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252)

def vaut_251_vol_autocorr_stability_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_251_vol_autocorr_stability_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(5)

def vaut_252_vol_autocorr_stability_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_252_vol_autocorr_stability_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(21)

def vaut_253_vol_autocorr_stability_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_253_vol_autocorr_stability_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(63)

def vaut_254_vol_autocorr_stability_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_254_vol_autocorr_stability_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(126)

def vaut_255_vol_autocorr_stability_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_255_vol_autocorr_stability_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_stability. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(252)

def vaut_256_vol_autocorr_acceleration_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_256_vol_autocorr_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(5)

def vaut_257_vol_autocorr_acceleration_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_257_vol_autocorr_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(21)

def vaut_258_vol_autocorr_acceleration_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_258_vol_autocorr_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(63)

def vaut_259_vol_autocorr_acceleration_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_259_vol_autocorr_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(126)

def vaut_260_vol_autocorr_acceleration_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_260_vol_autocorr_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_acceleration. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(252)

def vaut_261_vol_mean_reversion_flag_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_261_vol_mean_reversion_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(5)

def vaut_262_vol_mean_reversion_flag_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_262_vol_mean_reversion_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(21)

def vaut_263_vol_mean_reversion_flag_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_263_vol_mean_reversion_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(63)

def vaut_264_vol_mean_reversion_flag_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_264_vol_mean_reversion_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(126)

def vaut_265_vol_mean_reversion_flag_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_265_vol_mean_reversion_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_flag. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).diff(252)

def vaut_266_vol_trend_persistence_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_266_vol_trend_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(5)

def vaut_267_vol_trend_persistence_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_267_vol_trend_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(21)

def vaut_268_vol_trend_persistence_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_268_vol_trend_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(63)

def vaut_269_vol_trend_persistence_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_269_vol_trend_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(126)

def vaut_270_vol_trend_persistence_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_270_vol_trend_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_trend_persistence. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).diff(252)

def vaut_271_vol_autocorr_vs_price_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_271_vol_autocorr_vs_price_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(5)

def vaut_272_vol_autocorr_vs_price_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_272_vol_autocorr_vs_price_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(21)

def vaut_273_vol_autocorr_vs_price_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_273_vol_autocorr_vs_price_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(63)

def vaut_274_vol_autocorr_vs_price_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_274_vol_autocorr_vs_price_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(126)

def vaut_275_vol_autocorr_vs_price_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_275_vol_autocorr_vs_price_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_vs_price. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).diff(252)

def vaut_276_vol_autocorr_peak_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_276_vol_autocorr_peak_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(5)

def vaut_277_vol_autocorr_peak_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_277_vol_autocorr_peak_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(21)

def vaut_278_vol_autocorr_peak_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_278_vol_autocorr_peak_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(63)

def vaut_279_vol_autocorr_peak_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_279_vol_autocorr_peak_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(126)

def vaut_280_vol_autocorr_peak_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_280_vol_autocorr_peak_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_peak. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).diff(252)

def vaut_281_vol_autocorr_entropy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_281_vol_autocorr_entropy_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(5)

def vaut_282_vol_autocorr_entropy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_282_vol_autocorr_entropy_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(21)

def vaut_283_vol_autocorr_entropy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_283_vol_autocorr_entropy_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(63)

def vaut_284_vol_autocorr_entropy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_284_vol_autocorr_entropy_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(126)

def vaut_285_vol_autocorr_entropy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_285_vol_autocorr_entropy_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_entropy. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).diff(252)

def vaut_286_vol_autocorr_regime_switch_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_286_vol_autocorr_regime_switch_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(5)

def vaut_287_vol_autocorr_regime_switch_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_287_vol_autocorr_regime_switch_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(21)

def vaut_288_vol_autocorr_regime_switch_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_288_vol_autocorr_regime_switch_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(63)

def vaut_289_vol_autocorr_regime_switch_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_289_vol_autocorr_regime_switch_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(126)

def vaut_290_vol_autocorr_regime_switch_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_290_vol_autocorr_regime_switch_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_regime_switch. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).diff(252)

def vaut_291_vol_autocorr_ma_spread_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_291_vol_autocorr_ma_spread_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(5)

def vaut_292_vol_autocorr_ma_spread_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_292_vol_autocorr_ma_spread_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(21)

def vaut_293_vol_autocorr_ma_spread_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_293_vol_autocorr_ma_spread_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(63)

def vaut_294_vol_autocorr_ma_spread_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_294_vol_autocorr_ma_spread_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(126)

def vaut_295_vol_autocorr_ma_spread_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_295_vol_autocorr_ma_spread_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_ma_spread. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).diff(252)

def vaut_296_vol_autocorr_low_liquidity_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_296_vol_autocorr_low_liquidity_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(5)

def vaut_297_vol_autocorr_low_liquidity_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_297_vol_autocorr_low_liquidity_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(21)

def vaut_298_vol_autocorr_low_liquidity_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_298_vol_autocorr_low_liquidity_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(63)

def vaut_299_vol_autocorr_low_liquidity_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_299_vol_autocorr_low_liquidity_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(126)

def vaut_300_vol_autocorr_low_liquidity_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_300_vol_autocorr_low_liquidity_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_autocorr_low_liquidity. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V113_REGISTRY_VEL = {
    "vaut_226_vol_lag1_autocorr_vel_5d": {"inputs": ["close", "volume"], "func": vaut_226_vol_lag1_autocorr_vel_5d},
    "vaut_227_vol_lag1_autocorr_vel_21d": {"inputs": ["close", "volume"], "func": vaut_227_vol_lag1_autocorr_vel_21d},
    "vaut_228_vol_lag1_autocorr_vel_63d": {"inputs": ["close", "volume"], "func": vaut_228_vol_lag1_autocorr_vel_63d},
    "vaut_229_vol_lag1_autocorr_vel_126d": {"inputs": ["close", "volume"], "func": vaut_229_vol_lag1_autocorr_vel_126d},
    "vaut_230_vol_lag1_autocorr_vel_252d": {"inputs": ["close", "volume"], "func": vaut_230_vol_lag1_autocorr_vel_252d},
    "vaut_231_vol_autocorr_zscore_vel_5d": {"inputs": ["close", "volume"], "func": vaut_231_vol_autocorr_zscore_vel_5d},
    "vaut_232_vol_autocorr_zscore_vel_21d": {"inputs": ["close", "volume"], "func": vaut_232_vol_autocorr_zscore_vel_21d},
    "vaut_233_vol_autocorr_zscore_vel_63d": {"inputs": ["close", "volume"], "func": vaut_233_vol_autocorr_zscore_vel_63d},
    "vaut_234_vol_autocorr_zscore_vel_126d": {"inputs": ["close", "volume"], "func": vaut_234_vol_autocorr_zscore_vel_126d},
    "vaut_235_vol_autocorr_zscore_vel_252d": {"inputs": ["close", "volume"], "func": vaut_235_vol_autocorr_zscore_vel_252d},
    "vaut_236_vol_persistence_trend_vel_5d": {"inputs": ["close", "volume"], "func": vaut_236_vol_persistence_trend_vel_5d},
    "vaut_237_vol_persistence_trend_vel_21d": {"inputs": ["close", "volume"], "func": vaut_237_vol_persistence_trend_vel_21d},
    "vaut_238_vol_persistence_trend_vel_63d": {"inputs": ["close", "volume"], "func": vaut_238_vol_persistence_trend_vel_63d},
    "vaut_239_vol_persistence_trend_vel_126d": {"inputs": ["close", "volume"], "func": vaut_239_vol_persistence_trend_vel_126d},
    "vaut_240_vol_persistence_trend_vel_252d": {"inputs": ["close", "volume"], "func": vaut_240_vol_persistence_trend_vel_252d},
    "vaut_241_vol_clustering_index_vel_5d": {"inputs": ["close", "volume"], "func": vaut_241_vol_clustering_index_vel_5d},
    "vaut_242_vol_clustering_index_vel_21d": {"inputs": ["close", "volume"], "func": vaut_242_vol_clustering_index_vel_21d},
    "vaut_243_vol_clustering_index_vel_63d": {"inputs": ["close", "volume"], "func": vaut_243_vol_clustering_index_vel_63d},
    "vaut_244_vol_clustering_index_vel_126d": {"inputs": ["close", "volume"], "func": vaut_244_vol_clustering_index_vel_126d},
    "vaut_245_vol_clustering_index_vel_252d": {"inputs": ["close", "volume"], "func": vaut_245_vol_clustering_index_vel_252d},
    "vaut_246_vol_autocorr_rank_vel_5d": {"inputs": ["close", "volume"], "func": vaut_246_vol_autocorr_rank_vel_5d},
    "vaut_247_vol_autocorr_rank_vel_21d": {"inputs": ["close", "volume"], "func": vaut_247_vol_autocorr_rank_vel_21d},
    "vaut_248_vol_autocorr_rank_vel_63d": {"inputs": ["close", "volume"], "func": vaut_248_vol_autocorr_rank_vel_63d},
    "vaut_249_vol_autocorr_rank_vel_126d": {"inputs": ["close", "volume"], "func": vaut_249_vol_autocorr_rank_vel_126d},
    "vaut_250_vol_autocorr_rank_vel_252d": {"inputs": ["close", "volume"], "func": vaut_250_vol_autocorr_rank_vel_252d},
    "vaut_251_vol_autocorr_stability_vel_5d": {"inputs": ["close", "volume"], "func": vaut_251_vol_autocorr_stability_vel_5d},
    "vaut_252_vol_autocorr_stability_vel_21d": {"inputs": ["close", "volume"], "func": vaut_252_vol_autocorr_stability_vel_21d},
    "vaut_253_vol_autocorr_stability_vel_63d": {"inputs": ["close", "volume"], "func": vaut_253_vol_autocorr_stability_vel_63d},
    "vaut_254_vol_autocorr_stability_vel_126d": {"inputs": ["close", "volume"], "func": vaut_254_vol_autocorr_stability_vel_126d},
    "vaut_255_vol_autocorr_stability_vel_252d": {"inputs": ["close", "volume"], "func": vaut_255_vol_autocorr_stability_vel_252d},
    "vaut_256_vol_autocorr_acceleration_vel_5d": {"inputs": ["close", "volume"], "func": vaut_256_vol_autocorr_acceleration_vel_5d},
    "vaut_257_vol_autocorr_acceleration_vel_21d": {"inputs": ["close", "volume"], "func": vaut_257_vol_autocorr_acceleration_vel_21d},
    "vaut_258_vol_autocorr_acceleration_vel_63d": {"inputs": ["close", "volume"], "func": vaut_258_vol_autocorr_acceleration_vel_63d},
    "vaut_259_vol_autocorr_acceleration_vel_126d": {"inputs": ["close", "volume"], "func": vaut_259_vol_autocorr_acceleration_vel_126d},
    "vaut_260_vol_autocorr_acceleration_vel_252d": {"inputs": ["close", "volume"], "func": vaut_260_vol_autocorr_acceleration_vel_252d},
    "vaut_261_vol_mean_reversion_flag_vel_5d": {"inputs": ["close", "volume"], "func": vaut_261_vol_mean_reversion_flag_vel_5d},
    "vaut_262_vol_mean_reversion_flag_vel_21d": {"inputs": ["close", "volume"], "func": vaut_262_vol_mean_reversion_flag_vel_21d},
    "vaut_263_vol_mean_reversion_flag_vel_63d": {"inputs": ["close", "volume"], "func": vaut_263_vol_mean_reversion_flag_vel_63d},
    "vaut_264_vol_mean_reversion_flag_vel_126d": {"inputs": ["close", "volume"], "func": vaut_264_vol_mean_reversion_flag_vel_126d},
    "vaut_265_vol_mean_reversion_flag_vel_252d": {"inputs": ["close", "volume"], "func": vaut_265_vol_mean_reversion_flag_vel_252d},
    "vaut_266_vol_trend_persistence_vel_5d": {"inputs": ["close", "volume"], "func": vaut_266_vol_trend_persistence_vel_5d},
    "vaut_267_vol_trend_persistence_vel_21d": {"inputs": ["close", "volume"], "func": vaut_267_vol_trend_persistence_vel_21d},
    "vaut_268_vol_trend_persistence_vel_63d": {"inputs": ["close", "volume"], "func": vaut_268_vol_trend_persistence_vel_63d},
    "vaut_269_vol_trend_persistence_vel_126d": {"inputs": ["close", "volume"], "func": vaut_269_vol_trend_persistence_vel_126d},
    "vaut_270_vol_trend_persistence_vel_252d": {"inputs": ["close", "volume"], "func": vaut_270_vol_trend_persistence_vel_252d},
    "vaut_271_vol_autocorr_vs_price_vel_5d": {"inputs": ["close", "volume"], "func": vaut_271_vol_autocorr_vs_price_vel_5d},
    "vaut_272_vol_autocorr_vs_price_vel_21d": {"inputs": ["close", "volume"], "func": vaut_272_vol_autocorr_vs_price_vel_21d},
    "vaut_273_vol_autocorr_vs_price_vel_63d": {"inputs": ["close", "volume"], "func": vaut_273_vol_autocorr_vs_price_vel_63d},
    "vaut_274_vol_autocorr_vs_price_vel_126d": {"inputs": ["close", "volume"], "func": vaut_274_vol_autocorr_vs_price_vel_126d},
    "vaut_275_vol_autocorr_vs_price_vel_252d": {"inputs": ["close", "volume"], "func": vaut_275_vol_autocorr_vs_price_vel_252d},
    "vaut_276_vol_autocorr_peak_vel_5d": {"inputs": ["close", "volume"], "func": vaut_276_vol_autocorr_peak_vel_5d},
    "vaut_277_vol_autocorr_peak_vel_21d": {"inputs": ["close", "volume"], "func": vaut_277_vol_autocorr_peak_vel_21d},
    "vaut_278_vol_autocorr_peak_vel_63d": {"inputs": ["close", "volume"], "func": vaut_278_vol_autocorr_peak_vel_63d},
    "vaut_279_vol_autocorr_peak_vel_126d": {"inputs": ["close", "volume"], "func": vaut_279_vol_autocorr_peak_vel_126d},
    "vaut_280_vol_autocorr_peak_vel_252d": {"inputs": ["close", "volume"], "func": vaut_280_vol_autocorr_peak_vel_252d},
    "vaut_281_vol_autocorr_entropy_vel_5d": {"inputs": ["close", "volume"], "func": vaut_281_vol_autocorr_entropy_vel_5d},
    "vaut_282_vol_autocorr_entropy_vel_21d": {"inputs": ["close", "volume"], "func": vaut_282_vol_autocorr_entropy_vel_21d},
    "vaut_283_vol_autocorr_entropy_vel_63d": {"inputs": ["close", "volume"], "func": vaut_283_vol_autocorr_entropy_vel_63d},
    "vaut_284_vol_autocorr_entropy_vel_126d": {"inputs": ["close", "volume"], "func": vaut_284_vol_autocorr_entropy_vel_126d},
    "vaut_285_vol_autocorr_entropy_vel_252d": {"inputs": ["close", "volume"], "func": vaut_285_vol_autocorr_entropy_vel_252d},
    "vaut_286_vol_autocorr_regime_switch_vel_5d": {"inputs": ["close", "volume"], "func": vaut_286_vol_autocorr_regime_switch_vel_5d},
    "vaut_287_vol_autocorr_regime_switch_vel_21d": {"inputs": ["close", "volume"], "func": vaut_287_vol_autocorr_regime_switch_vel_21d},
    "vaut_288_vol_autocorr_regime_switch_vel_63d": {"inputs": ["close", "volume"], "func": vaut_288_vol_autocorr_regime_switch_vel_63d},
    "vaut_289_vol_autocorr_regime_switch_vel_126d": {"inputs": ["close", "volume"], "func": vaut_289_vol_autocorr_regime_switch_vel_126d},
    "vaut_290_vol_autocorr_regime_switch_vel_252d": {"inputs": ["close", "volume"], "func": vaut_290_vol_autocorr_regime_switch_vel_252d},
    "vaut_291_vol_autocorr_ma_spread_vel_5d": {"inputs": ["close", "volume"], "func": vaut_291_vol_autocorr_ma_spread_vel_5d},
    "vaut_292_vol_autocorr_ma_spread_vel_21d": {"inputs": ["close", "volume"], "func": vaut_292_vol_autocorr_ma_spread_vel_21d},
    "vaut_293_vol_autocorr_ma_spread_vel_63d": {"inputs": ["close", "volume"], "func": vaut_293_vol_autocorr_ma_spread_vel_63d},
    "vaut_294_vol_autocorr_ma_spread_vel_126d": {"inputs": ["close", "volume"], "func": vaut_294_vol_autocorr_ma_spread_vel_126d},
    "vaut_295_vol_autocorr_ma_spread_vel_252d": {"inputs": ["close", "volume"], "func": vaut_295_vol_autocorr_ma_spread_vel_252d},
    "vaut_296_vol_autocorr_low_liquidity_vel_5d": {"inputs": ["close", "volume"], "func": vaut_296_vol_autocorr_low_liquidity_vel_5d},
    "vaut_297_vol_autocorr_low_liquidity_vel_21d": {"inputs": ["close", "volume"], "func": vaut_297_vol_autocorr_low_liquidity_vel_21d},
    "vaut_298_vol_autocorr_low_liquidity_vel_63d": {"inputs": ["close", "volume"], "func": vaut_298_vol_autocorr_low_liquidity_vel_63d},
    "vaut_299_vol_autocorr_low_liquidity_vel_126d": {"inputs": ["close", "volume"], "func": vaut_299_vol_autocorr_low_liquidity_vel_126d},
    "vaut_300_vol_autocorr_low_liquidity_vel_252d": {"inputs": ["close", "volume"], "func": vaut_300_vol_autocorr_low_liquidity_vel_252d},
}
