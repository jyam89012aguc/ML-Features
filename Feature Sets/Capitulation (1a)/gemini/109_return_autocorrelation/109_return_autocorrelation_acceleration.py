"""
109_return_autocorrelation — Acceleration (3rd Derivatives)
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

def raut_301_lag1_autocorr_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_301_lag1_autocorr_accel_5d
    ECONOMIC RATIONALE: Acceleration of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5).diff(_TD_MON)

def raut_302_lag1_autocorr_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_302_lag1_autocorr_accel_21d
    ECONOMIC RATIONALE: Acceleration of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21).diff(_TD_MON)

def raut_303_lag1_autocorr_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_303_lag1_autocorr_accel_63d
    ECONOMIC RATIONALE: Acceleration of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63).diff(_TD_MON)

def raut_304_lag1_autocorr_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_304_lag1_autocorr_accel_126d
    ECONOMIC RATIONALE: Acceleration of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126).diff(_TD_MON)

def raut_305_lag1_autocorr_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_305_lag1_autocorr_accel_252d
    ECONOMIC RATIONALE: Acceleration of lag1_autocorr. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252).diff(_TD_MON)

def raut_306_lag5_autocorr_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_306_lag5_autocorr_accel_5d
    ECONOMIC RATIONALE: Acceleration of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(5).diff(_TD_MON)

def raut_307_lag5_autocorr_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_307_lag5_autocorr_accel_21d
    ECONOMIC RATIONALE: Acceleration of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(21).diff(_TD_MON)

def raut_308_lag5_autocorr_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_308_lag5_autocorr_accel_63d
    ECONOMIC RATIONALE: Acceleration of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(63).diff(_TD_MON)

def raut_309_lag5_autocorr_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_309_lag5_autocorr_accel_126d
    ECONOMIC RATIONALE: Acceleration of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(126).diff(_TD_MON)

def raut_310_lag5_autocorr_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_310_lag5_autocorr_accel_252d
    ECONOMIC RATIONALE: Acceleration of lag5_autocorr. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).diff(252).diff(_TD_MON)

def raut_311_autocorr_zscore_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_311_autocorr_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5).diff(_TD_MON)

def raut_312_autocorr_zscore_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_312_autocorr_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21).diff(_TD_MON)

def raut_313_autocorr_zscore_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_313_autocorr_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63).diff(_TD_MON)

def raut_314_autocorr_zscore_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_314_autocorr_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126).diff(_TD_MON)

def raut_315_autocorr_zscore_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_315_autocorr_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_zscore. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252).diff(_TD_MON)

def raut_316_autocorr_trend_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_316_autocorr_trend_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(5).diff(_TD_MON)

def raut_317_autocorr_trend_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_317_autocorr_trend_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(21).diff(_TD_MON)

def raut_318_autocorr_trend_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_318_autocorr_trend_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(63).diff(_TD_MON)

def raut_319_autocorr_trend_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_319_autocorr_trend_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(126).diff(_TD_MON)

def raut_320_autocorr_trend_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_320_autocorr_trend_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_trend. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).diff(252).diff(_TD_MON)

def raut_321_negative_autocorr_flag_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_321_negative_autocorr_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(5).diff(_TD_MON)

def raut_322_negative_autocorr_flag_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_322_negative_autocorr_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(21).diff(_TD_MON)

def raut_323_negative_autocorr_flag_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_323_negative_autocorr_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(63).diff(_TD_MON)

def raut_324_negative_autocorr_flag_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_324_negative_autocorr_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(126).diff(_TD_MON)

def raut_325_negative_autocorr_flag_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_325_negative_autocorr_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of negative_autocorr_flag. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).diff(252).diff(_TD_MON)

def raut_326_positive_autocorr_flag_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_326_positive_autocorr_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(5).diff(_TD_MON)

def raut_327_positive_autocorr_flag_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_327_positive_autocorr_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(21).diff(_TD_MON)

def raut_328_positive_autocorr_flag_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_328_positive_autocorr_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(63).diff(_TD_MON)

def raut_329_positive_autocorr_flag_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_329_positive_autocorr_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(126).diff(_TD_MON)

def raut_330_positive_autocorr_flag_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_330_positive_autocorr_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of positive_autocorr_flag. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).diff(252).diff(_TD_MON)

def raut_331_autocorr_vol_corr_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_331_autocorr_vol_corr_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(5).diff(_TD_MON)

def raut_332_autocorr_vol_corr_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_332_autocorr_vol_corr_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(21).diff(_TD_MON)

def raut_333_autocorr_vol_corr_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_333_autocorr_vol_corr_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(63).diff(_TD_MON)

def raut_334_autocorr_vol_corr_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_334_autocorr_vol_corr_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(126).diff(_TD_MON)

def raut_335_autocorr_vol_corr_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_335_autocorr_vol_corr_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_vol_corr. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).diff(252).diff(_TD_MON)

def raut_336_multi_lag_autocorr_sum_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_336_multi_lag_autocorr_sum_accel_5d
    ECONOMIC RATIONALE: Acceleration of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(5).diff(_TD_MON)

def raut_337_multi_lag_autocorr_sum_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_337_multi_lag_autocorr_sum_accel_21d
    ECONOMIC RATIONALE: Acceleration of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(21).diff(_TD_MON)

def raut_338_multi_lag_autocorr_sum_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_338_multi_lag_autocorr_sum_accel_63d
    ECONOMIC RATIONALE: Acceleration of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(63).diff(_TD_MON)

def raut_339_multi_lag_autocorr_sum_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_339_multi_lag_autocorr_sum_accel_126d
    ECONOMIC RATIONALE: Acceleration of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(126).diff(_TD_MON)

def raut_340_multi_lag_autocorr_sum_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_340_multi_lag_autocorr_sum_accel_252d
    ECONOMIC RATIONALE: Acceleration of multi_lag_autocorr_sum. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).diff(252).diff(_TD_MON)

def raut_341_autocorr_breakdown_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_341_autocorr_breakdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(5).diff(_TD_MON)

def raut_342_autocorr_breakdown_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_342_autocorr_breakdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(21).diff(_TD_MON)

def raut_343_autocorr_breakdown_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_343_autocorr_breakdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(63).diff(_TD_MON)

def raut_344_autocorr_breakdown_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_344_autocorr_breakdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(126).diff(_TD_MON)

def raut_345_autocorr_breakdown_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_345_autocorr_breakdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_breakdown. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).diff(252).diff(_TD_MON)

def raut_346_return_clustering_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_346_return_clustering_accel_5d
    ECONOMIC RATIONALE: Acceleration of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(5).diff(_TD_MON)

def raut_347_return_clustering_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_347_return_clustering_accel_21d
    ECONOMIC RATIONALE: Acceleration of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(21).diff(_TD_MON)

def raut_348_return_clustering_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_348_return_clustering_accel_63d
    ECONOMIC RATIONALE: Acceleration of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(63).diff(_TD_MON)

def raut_349_return_clustering_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_349_return_clustering_accel_126d
    ECONOMIC RATIONALE: Acceleration of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(126).diff(_TD_MON)

def raut_350_return_clustering_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_350_return_clustering_accel_252d
    ECONOMIC RATIONALE: Acceleration of return_clustering. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).diff(252).diff(_TD_MON)

def raut_351_autocorr_regime_rank_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_351_autocorr_regime_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5).diff(_TD_MON)

def raut_352_autocorr_regime_rank_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_352_autocorr_regime_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21).diff(_TD_MON)

def raut_353_autocorr_regime_rank_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_353_autocorr_regime_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63).diff(_TD_MON)

def raut_354_autocorr_regime_rank_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_354_autocorr_regime_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126).diff(_TD_MON)

def raut_355_autocorr_regime_rank_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_355_autocorr_regime_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_regime_rank. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252).diff(_TD_MON)

def raut_356_autocorr_momentum_div_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_356_autocorr_momentum_div_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(5).diff(_TD_MON)

def raut_357_autocorr_momentum_div_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_357_autocorr_momentum_div_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(21).diff(_TD_MON)

def raut_358_autocorr_momentum_div_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_358_autocorr_momentum_div_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(63).diff(_TD_MON)

def raut_359_autocorr_momentum_div_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_359_autocorr_momentum_div_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(126).diff(_TD_MON)

def raut_360_autocorr_momentum_div_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_360_autocorr_momentum_div_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_momentum_div. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).diff(252).diff(_TD_MON)

def raut_361_mean_reversion_edge_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_361_mean_reversion_edge_accel_5d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(5).diff(_TD_MON)

def raut_362_mean_reversion_edge_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_362_mean_reversion_edge_accel_21d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(21).diff(_TD_MON)

def raut_363_mean_reversion_edge_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_363_mean_reversion_edge_accel_63d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(63).diff(_TD_MON)

def raut_364_mean_reversion_edge_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_364_mean_reversion_edge_accel_126d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(126).diff(_TD_MON)

def raut_365_mean_reversion_edge_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_365_mean_reversion_edge_accel_252d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_edge. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).diff(252).diff(_TD_MON)

def raut_366_autocorr_stability_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_366_autocorr_stability_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(5).diff(_TD_MON)

def raut_367_autocorr_stability_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_367_autocorr_stability_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(21).diff(_TD_MON)

def raut_368_autocorr_stability_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_368_autocorr_stability_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(63).diff(_TD_MON)

def raut_369_autocorr_stability_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_369_autocorr_stability_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(126).diff(_TD_MON)

def raut_370_autocorr_stability_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_370_autocorr_stability_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_stability. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).diff(252).diff(_TD_MON)

def raut_371_autocorr_acceleration_accel_5d(close: pd.Series) -> pd.Series:
    """
    raut_371_autocorr_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(5).diff(_TD_MON)

def raut_372_autocorr_acceleration_accel_21d(close: pd.Series) -> pd.Series:
    """
    raut_372_autocorr_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(21).diff(_TD_MON)

def raut_373_autocorr_acceleration_accel_63d(close: pd.Series) -> pd.Series:
    """
    raut_373_autocorr_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(63).diff(_TD_MON)

def raut_374_autocorr_acceleration_accel_126d(close: pd.Series) -> pd.Series:
    """
    raut_374_autocorr_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(126).diff(_TD_MON)

def raut_375_autocorr_acceleration_accel_252d(close: pd.Series) -> pd.Series:
    """
    raut_375_autocorr_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of autocorr_acceleration. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V109_REGISTRY_ACCEL = {
    "raut_301_lag1_autocorr_accel_5d": {"inputs": ["close"], "func": raut_301_lag1_autocorr_accel_5d},
    "raut_302_lag1_autocorr_accel_21d": {"inputs": ["close"], "func": raut_302_lag1_autocorr_accel_21d},
    "raut_303_lag1_autocorr_accel_63d": {"inputs": ["close"], "func": raut_303_lag1_autocorr_accel_63d},
    "raut_304_lag1_autocorr_accel_126d": {"inputs": ["close"], "func": raut_304_lag1_autocorr_accel_126d},
    "raut_305_lag1_autocorr_accel_252d": {"inputs": ["close"], "func": raut_305_lag1_autocorr_accel_252d},
    "raut_306_lag5_autocorr_accel_5d": {"inputs": ["close"], "func": raut_306_lag5_autocorr_accel_5d},
    "raut_307_lag5_autocorr_accel_21d": {"inputs": ["close"], "func": raut_307_lag5_autocorr_accel_21d},
    "raut_308_lag5_autocorr_accel_63d": {"inputs": ["close"], "func": raut_308_lag5_autocorr_accel_63d},
    "raut_309_lag5_autocorr_accel_126d": {"inputs": ["close"], "func": raut_309_lag5_autocorr_accel_126d},
    "raut_310_lag5_autocorr_accel_252d": {"inputs": ["close"], "func": raut_310_lag5_autocorr_accel_252d},
    "raut_311_autocorr_zscore_accel_5d": {"inputs": ["close"], "func": raut_311_autocorr_zscore_accel_5d},
    "raut_312_autocorr_zscore_accel_21d": {"inputs": ["close"], "func": raut_312_autocorr_zscore_accel_21d},
    "raut_313_autocorr_zscore_accel_63d": {"inputs": ["close"], "func": raut_313_autocorr_zscore_accel_63d},
    "raut_314_autocorr_zscore_accel_126d": {"inputs": ["close"], "func": raut_314_autocorr_zscore_accel_126d},
    "raut_315_autocorr_zscore_accel_252d": {"inputs": ["close"], "func": raut_315_autocorr_zscore_accel_252d},
    "raut_316_autocorr_trend_accel_5d": {"inputs": ["close"], "func": raut_316_autocorr_trend_accel_5d},
    "raut_317_autocorr_trend_accel_21d": {"inputs": ["close"], "func": raut_317_autocorr_trend_accel_21d},
    "raut_318_autocorr_trend_accel_63d": {"inputs": ["close"], "func": raut_318_autocorr_trend_accel_63d},
    "raut_319_autocorr_trend_accel_126d": {"inputs": ["close"], "func": raut_319_autocorr_trend_accel_126d},
    "raut_320_autocorr_trend_accel_252d": {"inputs": ["close"], "func": raut_320_autocorr_trend_accel_252d},
    "raut_321_negative_autocorr_flag_accel_5d": {"inputs": ["close"], "func": raut_321_negative_autocorr_flag_accel_5d},
    "raut_322_negative_autocorr_flag_accel_21d": {"inputs": ["close"], "func": raut_322_negative_autocorr_flag_accel_21d},
    "raut_323_negative_autocorr_flag_accel_63d": {"inputs": ["close"], "func": raut_323_negative_autocorr_flag_accel_63d},
    "raut_324_negative_autocorr_flag_accel_126d": {"inputs": ["close"], "func": raut_324_negative_autocorr_flag_accel_126d},
    "raut_325_negative_autocorr_flag_accel_252d": {"inputs": ["close"], "func": raut_325_negative_autocorr_flag_accel_252d},
    "raut_326_positive_autocorr_flag_accel_5d": {"inputs": ["close"], "func": raut_326_positive_autocorr_flag_accel_5d},
    "raut_327_positive_autocorr_flag_accel_21d": {"inputs": ["close"], "func": raut_327_positive_autocorr_flag_accel_21d},
    "raut_328_positive_autocorr_flag_accel_63d": {"inputs": ["close"], "func": raut_328_positive_autocorr_flag_accel_63d},
    "raut_329_positive_autocorr_flag_accel_126d": {"inputs": ["close"], "func": raut_329_positive_autocorr_flag_accel_126d},
    "raut_330_positive_autocorr_flag_accel_252d": {"inputs": ["close"], "func": raut_330_positive_autocorr_flag_accel_252d},
    "raut_331_autocorr_vol_corr_accel_5d": {"inputs": ["close"], "func": raut_331_autocorr_vol_corr_accel_5d},
    "raut_332_autocorr_vol_corr_accel_21d": {"inputs": ["close"], "func": raut_332_autocorr_vol_corr_accel_21d},
    "raut_333_autocorr_vol_corr_accel_63d": {"inputs": ["close"], "func": raut_333_autocorr_vol_corr_accel_63d},
    "raut_334_autocorr_vol_corr_accel_126d": {"inputs": ["close"], "func": raut_334_autocorr_vol_corr_accel_126d},
    "raut_335_autocorr_vol_corr_accel_252d": {"inputs": ["close"], "func": raut_335_autocorr_vol_corr_accel_252d},
    "raut_336_multi_lag_autocorr_sum_accel_5d": {"inputs": ["close"], "func": raut_336_multi_lag_autocorr_sum_accel_5d},
    "raut_337_multi_lag_autocorr_sum_accel_21d": {"inputs": ["close"], "func": raut_337_multi_lag_autocorr_sum_accel_21d},
    "raut_338_multi_lag_autocorr_sum_accel_63d": {"inputs": ["close"], "func": raut_338_multi_lag_autocorr_sum_accel_63d},
    "raut_339_multi_lag_autocorr_sum_accel_126d": {"inputs": ["close"], "func": raut_339_multi_lag_autocorr_sum_accel_126d},
    "raut_340_multi_lag_autocorr_sum_accel_252d": {"inputs": ["close"], "func": raut_340_multi_lag_autocorr_sum_accel_252d},
    "raut_341_autocorr_breakdown_accel_5d": {"inputs": ["close"], "func": raut_341_autocorr_breakdown_accel_5d},
    "raut_342_autocorr_breakdown_accel_21d": {"inputs": ["close"], "func": raut_342_autocorr_breakdown_accel_21d},
    "raut_343_autocorr_breakdown_accel_63d": {"inputs": ["close"], "func": raut_343_autocorr_breakdown_accel_63d},
    "raut_344_autocorr_breakdown_accel_126d": {"inputs": ["close"], "func": raut_344_autocorr_breakdown_accel_126d},
    "raut_345_autocorr_breakdown_accel_252d": {"inputs": ["close"], "func": raut_345_autocorr_breakdown_accel_252d},
    "raut_346_return_clustering_accel_5d": {"inputs": ["close"], "func": raut_346_return_clustering_accel_5d},
    "raut_347_return_clustering_accel_21d": {"inputs": ["close"], "func": raut_347_return_clustering_accel_21d},
    "raut_348_return_clustering_accel_63d": {"inputs": ["close"], "func": raut_348_return_clustering_accel_63d},
    "raut_349_return_clustering_accel_126d": {"inputs": ["close"], "func": raut_349_return_clustering_accel_126d},
    "raut_350_return_clustering_accel_252d": {"inputs": ["close"], "func": raut_350_return_clustering_accel_252d},
    "raut_351_autocorr_regime_rank_accel_5d": {"inputs": ["close"], "func": raut_351_autocorr_regime_rank_accel_5d},
    "raut_352_autocorr_regime_rank_accel_21d": {"inputs": ["close"], "func": raut_352_autocorr_regime_rank_accel_21d},
    "raut_353_autocorr_regime_rank_accel_63d": {"inputs": ["close"], "func": raut_353_autocorr_regime_rank_accel_63d},
    "raut_354_autocorr_regime_rank_accel_126d": {"inputs": ["close"], "func": raut_354_autocorr_regime_rank_accel_126d},
    "raut_355_autocorr_regime_rank_accel_252d": {"inputs": ["close"], "func": raut_355_autocorr_regime_rank_accel_252d},
    "raut_356_autocorr_momentum_div_accel_5d": {"inputs": ["close"], "func": raut_356_autocorr_momentum_div_accel_5d},
    "raut_357_autocorr_momentum_div_accel_21d": {"inputs": ["close"], "func": raut_357_autocorr_momentum_div_accel_21d},
    "raut_358_autocorr_momentum_div_accel_63d": {"inputs": ["close"], "func": raut_358_autocorr_momentum_div_accel_63d},
    "raut_359_autocorr_momentum_div_accel_126d": {"inputs": ["close"], "func": raut_359_autocorr_momentum_div_accel_126d},
    "raut_360_autocorr_momentum_div_accel_252d": {"inputs": ["close"], "func": raut_360_autocorr_momentum_div_accel_252d},
    "raut_361_mean_reversion_edge_accel_5d": {"inputs": ["close"], "func": raut_361_mean_reversion_edge_accel_5d},
    "raut_362_mean_reversion_edge_accel_21d": {"inputs": ["close"], "func": raut_362_mean_reversion_edge_accel_21d},
    "raut_363_mean_reversion_edge_accel_63d": {"inputs": ["close"], "func": raut_363_mean_reversion_edge_accel_63d},
    "raut_364_mean_reversion_edge_accel_126d": {"inputs": ["close"], "func": raut_364_mean_reversion_edge_accel_126d},
    "raut_365_mean_reversion_edge_accel_252d": {"inputs": ["close"], "func": raut_365_mean_reversion_edge_accel_252d},
    "raut_366_autocorr_stability_accel_5d": {"inputs": ["close"], "func": raut_366_autocorr_stability_accel_5d},
    "raut_367_autocorr_stability_accel_21d": {"inputs": ["close"], "func": raut_367_autocorr_stability_accel_21d},
    "raut_368_autocorr_stability_accel_63d": {"inputs": ["close"], "func": raut_368_autocorr_stability_accel_63d},
    "raut_369_autocorr_stability_accel_126d": {"inputs": ["close"], "func": raut_369_autocorr_stability_accel_126d},
    "raut_370_autocorr_stability_accel_252d": {"inputs": ["close"], "func": raut_370_autocorr_stability_accel_252d},
    "raut_371_autocorr_acceleration_accel_5d": {"inputs": ["close"], "func": raut_371_autocorr_acceleration_accel_5d},
    "raut_372_autocorr_acceleration_accel_21d": {"inputs": ["close"], "func": raut_372_autocorr_acceleration_accel_21d},
    "raut_373_autocorr_acceleration_accel_63d": {"inputs": ["close"], "func": raut_373_autocorr_acceleration_accel_63d},
    "raut_374_autocorr_acceleration_accel_126d": {"inputs": ["close"], "func": raut_374_autocorr_acceleration_accel_126d},
    "raut_375_autocorr_acceleration_accel_252d": {"inputs": ["close"], "func": raut_375_autocorr_acceleration_accel_252d},
}
