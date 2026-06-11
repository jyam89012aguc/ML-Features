"""
109_return_autocorrelation — Velocity (2nd Derivatives)
Domain: return_autocorrelation
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

def raut_226_lag1_autocorr_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_226_lag1_autocorr_vel_5d
    ECONOMIC RATIONALE: Velocity of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5)

def raut_227_lag1_autocorr_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_227_lag1_autocorr_vel_21d
    ECONOMIC RATIONALE: Velocity of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21)

def raut_228_lag1_autocorr_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_228_lag1_autocorr_vel_63d
    ECONOMIC RATIONALE: Velocity of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63)

def raut_229_lag1_autocorr_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_229_lag1_autocorr_vel_126d
    ECONOMIC RATIONALE: Velocity of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126)

def raut_230_lag1_autocorr_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_230_lag1_autocorr_vel_252d
    ECONOMIC RATIONALE: Velocity of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252)

def raut_231_lag5_autocorr_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_231_lag5_autocorr_vel_5d
    ECONOMIC RATIONALE: Velocity of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(5)

def raut_232_lag5_autocorr_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_232_lag5_autocorr_vel_21d
    ECONOMIC RATIONALE: Velocity of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(21)

def raut_233_lag5_autocorr_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_233_lag5_autocorr_vel_63d
    ECONOMIC RATIONALE: Velocity of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(63)

def raut_234_lag5_autocorr_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_234_lag5_autocorr_vel_126d
    ECONOMIC RATIONALE: Velocity of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(126)

def raut_235_lag5_autocorr_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_235_lag5_autocorr_vel_252d
    ECONOMIC RATIONALE: Velocity of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(252)

def raut_236_autocorr_zscore_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_236_autocorr_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5)

def raut_237_autocorr_zscore_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_237_autocorr_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21)

def raut_238_autocorr_zscore_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_238_autocorr_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63)

def raut_239_autocorr_zscore_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_239_autocorr_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126)

def raut_240_autocorr_zscore_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_240_autocorr_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252)

def raut_241_autocorr_trend_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_241_autocorr_trend_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5)

def raut_242_autocorr_trend_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_242_autocorr_trend_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21)

def raut_243_autocorr_trend_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_243_autocorr_trend_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63)

def raut_244_autocorr_trend_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_244_autocorr_trend_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126)

def raut_245_autocorr_trend_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_245_autocorr_trend_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252)

def raut_246_negative_autocorr_flag_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_246_negative_autocorr_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(5)

def raut_247_negative_autocorr_flag_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_247_negative_autocorr_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(21)

def raut_248_negative_autocorr_flag_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_248_negative_autocorr_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(63)

def raut_249_negative_autocorr_flag_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_249_negative_autocorr_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(126)

def raut_250_negative_autocorr_flag_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_250_negative_autocorr_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(252)

def raut_251_positive_autocorr_flag_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_251_positive_autocorr_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(5)

def raut_252_positive_autocorr_flag_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_252_positive_autocorr_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(21)

def raut_253_positive_autocorr_flag_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_253_positive_autocorr_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(63)

def raut_254_positive_autocorr_flag_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_254_positive_autocorr_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(126)

def raut_255_positive_autocorr_flag_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_255_positive_autocorr_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(252)

def raut_256_autocorr_vol_corr_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_256_autocorr_vol_corr_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(5)

def raut_257_autocorr_vol_corr_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_257_autocorr_vol_corr_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(21)

def raut_258_autocorr_vol_corr_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_258_autocorr_vol_corr_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(63)

def raut_259_autocorr_vol_corr_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_259_autocorr_vol_corr_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(126)

def raut_260_autocorr_vol_corr_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_260_autocorr_vol_corr_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(252)

def raut_261_multi_lag_autocorr_sum_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_261_multi_lag_autocorr_sum_vel_5d
    ECONOMIC RATIONALE: Velocity of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(5)

def raut_262_multi_lag_autocorr_sum_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_262_multi_lag_autocorr_sum_vel_21d
    ECONOMIC RATIONALE: Velocity of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(21)

def raut_263_multi_lag_autocorr_sum_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_263_multi_lag_autocorr_sum_vel_63d
    ECONOMIC RATIONALE: Velocity of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(63)

def raut_264_multi_lag_autocorr_sum_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_264_multi_lag_autocorr_sum_vel_126d
    ECONOMIC RATIONALE: Velocity of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(126)

def raut_265_multi_lag_autocorr_sum_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_265_multi_lag_autocorr_sum_vel_252d
    ECONOMIC RATIONALE: Velocity of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(252)

def raut_266_autocorr_breakdown_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_266_autocorr_breakdown_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(5)

def raut_267_autocorr_breakdown_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_267_autocorr_breakdown_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(21)

def raut_268_autocorr_breakdown_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_268_autocorr_breakdown_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(63)

def raut_269_autocorr_breakdown_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_269_autocorr_breakdown_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(126)

def raut_270_autocorr_breakdown_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_270_autocorr_breakdown_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(252)

def raut_271_return_clustering_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_271_return_clustering_vel_5d
    ECONOMIC RATIONALE: Velocity of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(5)

def raut_272_return_clustering_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_272_return_clustering_vel_21d
    ECONOMIC RATIONALE: Velocity of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(21)

def raut_273_return_clustering_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_273_return_clustering_vel_63d
    ECONOMIC RATIONALE: Velocity of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(63)

def raut_274_return_clustering_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_274_return_clustering_vel_126d
    ECONOMIC RATIONALE: Velocity of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(126)

def raut_275_return_clustering_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_275_return_clustering_vel_252d
    ECONOMIC RATIONALE: Velocity of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(252)

def raut_276_autocorr_regime_rank_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_276_autocorr_regime_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5)

def raut_277_autocorr_regime_rank_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_277_autocorr_regime_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21)

def raut_278_autocorr_regime_rank_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_278_autocorr_regime_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63)

def raut_279_autocorr_regime_rank_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_279_autocorr_regime_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126)

def raut_280_autocorr_regime_rank_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_280_autocorr_regime_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252)

def raut_281_autocorr_momentum_div_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_281_autocorr_momentum_div_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5)

def raut_282_autocorr_momentum_div_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_282_autocorr_momentum_div_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21)

def raut_283_autocorr_momentum_div_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_283_autocorr_momentum_div_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63)

def raut_284_autocorr_momentum_div_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_284_autocorr_momentum_div_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126)

def raut_285_autocorr_momentum_div_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_285_autocorr_momentum_div_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252)

def raut_286_mean_reversion_edge_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_286_mean_reversion_edge_vel_5d
    ECONOMIC RATIONALE: Velocity of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(5)

def raut_287_mean_reversion_edge_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_287_mean_reversion_edge_vel_21d
    ECONOMIC RATIONALE: Velocity of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(21)

def raut_288_mean_reversion_edge_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_288_mean_reversion_edge_vel_63d
    ECONOMIC RATIONALE: Velocity of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(63)

def raut_289_mean_reversion_edge_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_289_mean_reversion_edge_vel_126d
    ECONOMIC RATIONALE: Velocity of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(126)

def raut_290_mean_reversion_edge_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_290_mean_reversion_edge_vel_252d
    ECONOMIC RATIONALE: Velocity of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(252)

def raut_291_autocorr_stability_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_291_autocorr_stability_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(5)

def raut_292_autocorr_stability_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_292_autocorr_stability_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(21)

def raut_293_autocorr_stability_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_293_autocorr_stability_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(63)

def raut_294_autocorr_stability_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_294_autocorr_stability_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(126)

def raut_295_autocorr_stability_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_295_autocorr_stability_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(252)

def raut_296_autocorr_acceleration_vel_5d(close: pd.Series) -> pd.Series:
    """
    raut_296_autocorr_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(5)

def raut_297_autocorr_acceleration_vel_21d(close: pd.Series) -> pd.Series:
    """
    raut_297_autocorr_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(21)

def raut_298_autocorr_acceleration_vel_63d(close: pd.Series) -> pd.Series:
    """
    raut_298_autocorr_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(63)

def raut_299_autocorr_acceleration_vel_126d(close: pd.Series) -> pd.Series:
    """
    raut_299_autocorr_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(126)

def raut_300_autocorr_acceleration_vel_252d(close: pd.Series) -> pd.Series:
    """
    raut_300_autocorr_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V109_REGISTRY_VEL = {
    "raut_226_lag1_autocorr_vel_5d": {"inputs": ["close"], "func": raut_226_lag1_autocorr_vel_5d},
    "raut_227_lag1_autocorr_vel_21d": {"inputs": ["close"], "func": raut_227_lag1_autocorr_vel_21d},
    "raut_228_lag1_autocorr_vel_63d": {"inputs": ["close"], "func": raut_228_lag1_autocorr_vel_63d},
    "raut_229_lag1_autocorr_vel_126d": {"inputs": ["close"], "func": raut_229_lag1_autocorr_vel_126d},
    "raut_230_lag1_autocorr_vel_252d": {"inputs": ["close"], "func": raut_230_lag1_autocorr_vel_252d},
    "raut_231_lag5_autocorr_vel_5d": {"inputs": ["close"], "func": raut_231_lag5_autocorr_vel_5d},
    "raut_232_lag5_autocorr_vel_21d": {"inputs": ["close"], "func": raut_232_lag5_autocorr_vel_21d},
    "raut_233_lag5_autocorr_vel_63d": {"inputs": ["close"], "func": raut_233_lag5_autocorr_vel_63d},
    "raut_234_lag5_autocorr_vel_126d": {"inputs": ["close"], "func": raut_234_lag5_autocorr_vel_126d},
    "raut_235_lag5_autocorr_vel_252d": {"inputs": ["close"], "func": raut_235_lag5_autocorr_vel_252d},
    "raut_236_autocorr_zscore_vel_5d": {"inputs": ["close"], "func": raut_236_autocorr_zscore_vel_5d},
    "raut_237_autocorr_zscore_vel_21d": {"inputs": ["close"], "func": raut_237_autocorr_zscore_vel_21d},
    "raut_238_autocorr_zscore_vel_63d": {"inputs": ["close"], "func": raut_238_autocorr_zscore_vel_63d},
    "raut_239_autocorr_zscore_vel_126d": {"inputs": ["close"], "func": raut_239_autocorr_zscore_vel_126d},
    "raut_240_autocorr_zscore_vel_252d": {"inputs": ["close"], "func": raut_240_autocorr_zscore_vel_252d},
    "raut_241_autocorr_trend_vel_5d": {"inputs": ["close"], "func": raut_241_autocorr_trend_vel_5d},
    "raut_242_autocorr_trend_vel_21d": {"inputs": ["close"], "func": raut_242_autocorr_trend_vel_21d},
    "raut_243_autocorr_trend_vel_63d": {"inputs": ["close"], "func": raut_243_autocorr_trend_vel_63d},
    "raut_244_autocorr_trend_vel_126d": {"inputs": ["close"], "func": raut_244_autocorr_trend_vel_126d},
    "raut_245_autocorr_trend_vel_252d": {"inputs": ["close"], "func": raut_245_autocorr_trend_vel_252d},
    "raut_246_negative_autocorr_flag_vel_5d": {"inputs": ["close"], "func": raut_246_negative_autocorr_flag_vel_5d},
    "raut_247_negative_autocorr_flag_vel_21d": {"inputs": ["close"], "func": raut_247_negative_autocorr_flag_vel_21d},
    "raut_248_negative_autocorr_flag_vel_63d": {"inputs": ["close"], "func": raut_248_negative_autocorr_flag_vel_63d},
    "raut_249_negative_autocorr_flag_vel_126d": {"inputs": ["close"], "func": raut_249_negative_autocorr_flag_vel_126d},
    "raut_250_negative_autocorr_flag_vel_252d": {"inputs": ["close"], "func": raut_250_negative_autocorr_flag_vel_252d},
    "raut_251_positive_autocorr_flag_vel_5d": {"inputs": ["close"], "func": raut_251_positive_autocorr_flag_vel_5d},
    "raut_252_positive_autocorr_flag_vel_21d": {"inputs": ["close"], "func": raut_252_positive_autocorr_flag_vel_21d},
    "raut_253_positive_autocorr_flag_vel_63d": {"inputs": ["close"], "func": raut_253_positive_autocorr_flag_vel_63d},
    "raut_254_positive_autocorr_flag_vel_126d": {"inputs": ["close"], "func": raut_254_positive_autocorr_flag_vel_126d},
    "raut_255_positive_autocorr_flag_vel_252d": {"inputs": ["close"], "func": raut_255_positive_autocorr_flag_vel_252d},
    "raut_256_autocorr_vol_corr_vel_5d": {"inputs": ["close"], "func": raut_256_autocorr_vol_corr_vel_5d},
    "raut_257_autocorr_vol_corr_vel_21d": {"inputs": ["close"], "func": raut_257_autocorr_vol_corr_vel_21d},
    "raut_258_autocorr_vol_corr_vel_63d": {"inputs": ["close"], "func": raut_258_autocorr_vol_corr_vel_63d},
    "raut_259_autocorr_vol_corr_vel_126d": {"inputs": ["close"], "func": raut_259_autocorr_vol_corr_vel_126d},
    "raut_260_autocorr_vol_corr_vel_252d": {"inputs": ["close"], "func": raut_260_autocorr_vol_corr_vel_252d},
    "raut_261_multi_lag_autocorr_sum_vel_5d": {"inputs": ["close"], "func": raut_261_multi_lag_autocorr_sum_vel_5d},
    "raut_262_multi_lag_autocorr_sum_vel_21d": {"inputs": ["close"], "func": raut_262_multi_lag_autocorr_sum_vel_21d},
    "raut_263_multi_lag_autocorr_sum_vel_63d": {"inputs": ["close"], "func": raut_263_multi_lag_autocorr_sum_vel_63d},
    "raut_264_multi_lag_autocorr_sum_vel_126d": {"inputs": ["close"], "func": raut_264_multi_lag_autocorr_sum_vel_126d},
    "raut_265_multi_lag_autocorr_sum_vel_252d": {"inputs": ["close"], "func": raut_265_multi_lag_autocorr_sum_vel_252d},
    "raut_266_autocorr_breakdown_vel_5d": {"inputs": ["close"], "func": raut_266_autocorr_breakdown_vel_5d},
    "raut_267_autocorr_breakdown_vel_21d": {"inputs": ["close"], "func": raut_267_autocorr_breakdown_vel_21d},
    "raut_268_autocorr_breakdown_vel_63d": {"inputs": ["close"], "func": raut_268_autocorr_breakdown_vel_63d},
    "raut_269_autocorr_breakdown_vel_126d": {"inputs": ["close"], "func": raut_269_autocorr_breakdown_vel_126d},
    "raut_270_autocorr_breakdown_vel_252d": {"inputs": ["close"], "func": raut_270_autocorr_breakdown_vel_252d},
    "raut_271_return_clustering_vel_5d": {"inputs": ["close"], "func": raut_271_return_clustering_vel_5d},
    "raut_272_return_clustering_vel_21d": {"inputs": ["close"], "func": raut_272_return_clustering_vel_21d},
    "raut_273_return_clustering_vel_63d": {"inputs": ["close"], "func": raut_273_return_clustering_vel_63d},
    "raut_274_return_clustering_vel_126d": {"inputs": ["close"], "func": raut_274_return_clustering_vel_126d},
    "raut_275_return_clustering_vel_252d": {"inputs": ["close"], "func": raut_275_return_clustering_vel_252d},
    "raut_276_autocorr_regime_rank_vel_5d": {"inputs": ["close"], "func": raut_276_autocorr_regime_rank_vel_5d},
    "raut_277_autocorr_regime_rank_vel_21d": {"inputs": ["close"], "func": raut_277_autocorr_regime_rank_vel_21d},
    "raut_278_autocorr_regime_rank_vel_63d": {"inputs": ["close"], "func": raut_278_autocorr_regime_rank_vel_63d},
    "raut_279_autocorr_regime_rank_vel_126d": {"inputs": ["close"], "func": raut_279_autocorr_regime_rank_vel_126d},
    "raut_280_autocorr_regime_rank_vel_252d": {"inputs": ["close"], "func": raut_280_autocorr_regime_rank_vel_252d},
    "raut_281_autocorr_momentum_div_vel_5d": {"inputs": ["close"], "func": raut_281_autocorr_momentum_div_vel_5d},
    "raut_282_autocorr_momentum_div_vel_21d": {"inputs": ["close"], "func": raut_282_autocorr_momentum_div_vel_21d},
    "raut_283_autocorr_momentum_div_vel_63d": {"inputs": ["close"], "func": raut_283_autocorr_momentum_div_vel_63d},
    "raut_284_autocorr_momentum_div_vel_126d": {"inputs": ["close"], "func": raut_284_autocorr_momentum_div_vel_126d},
    "raut_285_autocorr_momentum_div_vel_252d": {"inputs": ["close"], "func": raut_285_autocorr_momentum_div_vel_252d},
    "raut_286_mean_reversion_edge_vel_5d": {"inputs": ["close"], "func": raut_286_mean_reversion_edge_vel_5d},
    "raut_287_mean_reversion_edge_vel_21d": {"inputs": ["close"], "func": raut_287_mean_reversion_edge_vel_21d},
    "raut_288_mean_reversion_edge_vel_63d": {"inputs": ["close"], "func": raut_288_mean_reversion_edge_vel_63d},
    "raut_289_mean_reversion_edge_vel_126d": {"inputs": ["close"], "func": raut_289_mean_reversion_edge_vel_126d},
    "raut_290_mean_reversion_edge_vel_252d": {"inputs": ["close"], "func": raut_290_mean_reversion_edge_vel_252d},
    "raut_291_autocorr_stability_vel_5d": {"inputs": ["close"], "func": raut_291_autocorr_stability_vel_5d},
    "raut_292_autocorr_stability_vel_21d": {"inputs": ["close"], "func": raut_292_autocorr_stability_vel_21d},
    "raut_293_autocorr_stability_vel_63d": {"inputs": ["close"], "func": raut_293_autocorr_stability_vel_63d},
    "raut_294_autocorr_stability_vel_126d": {"inputs": ["close"], "func": raut_294_autocorr_stability_vel_126d},
    "raut_295_autocorr_stability_vel_252d": {"inputs": ["close"], "func": raut_295_autocorr_stability_vel_252d},
    "raut_296_autocorr_acceleration_vel_5d": {"inputs": ["close"], "func": raut_296_autocorr_acceleration_vel_5d},
    "raut_297_autocorr_acceleration_vel_21d": {"inputs": ["close"], "func": raut_297_autocorr_acceleration_vel_21d},
    "raut_298_autocorr_acceleration_vel_63d": {"inputs": ["close"], "func": raut_298_autocorr_acceleration_vel_63d},
    "raut_299_autocorr_acceleration_vel_126d": {"inputs": ["close"], "func": raut_299_autocorr_acceleration_vel_126d},
    "raut_300_autocorr_acceleration_vel_252d": {"inputs": ["close"], "func": raut_300_autocorr_acceleration_vel_252d},
}
