"""
104_mean_reversion_potential — Acceleration (3rd Derivatives)
Domain: mean_reversion_potential
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

def mrpt_301_bollinger_pct_b_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_301_bollinger_pct_b_accel_5d
    ECONOMIC RATIONALE: Acceleration of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def mrpt_302_bollinger_pct_b_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_302_bollinger_pct_b_accel_21d
    ECONOMIC RATIONALE: Acceleration of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def mrpt_303_bollinger_pct_b_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_303_bollinger_pct_b_accel_63d
    ECONOMIC RATIONALE: Acceleration of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def mrpt_304_bollinger_pct_b_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_304_bollinger_pct_b_accel_126d
    ECONOMIC RATIONALE: Acceleration of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def mrpt_305_bollinger_pct_b_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_305_bollinger_pct_b_accel_252d
    ECONOMIC RATIONALE: Acceleration of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def mrpt_306_distance_from_ma200_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_306_distance_from_ma200_accel_5d
    ECONOMIC RATIONALE: Acceleration of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(5).diff(_TD_MON)

def mrpt_307_distance_from_ma200_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_307_distance_from_ma200_accel_21d
    ECONOMIC RATIONALE: Acceleration of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(21).diff(_TD_MON)

def mrpt_308_distance_from_ma200_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_308_distance_from_ma200_accel_63d
    ECONOMIC RATIONALE: Acceleration of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(63).diff(_TD_MON)

def mrpt_309_distance_from_ma200_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_309_distance_from_ma200_accel_126d
    ECONOMIC RATIONALE: Acceleration of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(126).diff(_TD_MON)

def mrpt_310_distance_from_ma200_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_310_distance_from_ma200_accel_252d
    ECONOMIC RATIONALE: Acceleration of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(252).diff(_TD_MON)

def mrpt_311_keltner_channel_lower_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_311_keltner_channel_lower_accel_5d
    ECONOMIC RATIONALE: Acceleration of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(5).diff(_TD_MON)

def mrpt_312_keltner_channel_lower_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_312_keltner_channel_lower_accel_21d
    ECONOMIC RATIONALE: Acceleration of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(21).diff(_TD_MON)

def mrpt_313_keltner_channel_lower_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_313_keltner_channel_lower_accel_63d
    ECONOMIC RATIONALE: Acceleration of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(63).diff(_TD_MON)

def mrpt_314_keltner_channel_lower_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_314_keltner_channel_lower_accel_126d
    ECONOMIC RATIONALE: Acceleration of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(126).diff(_TD_MON)

def mrpt_315_keltner_channel_lower_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_315_keltner_channel_lower_accel_252d
    ECONOMIC RATIONALE: Acceleration of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(252).diff(_TD_MON)

def mrpt_316_mean_reversion_z_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_316_mean_reversion_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(5).diff(_TD_MON)

def mrpt_317_mean_reversion_z_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_317_mean_reversion_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(21).diff(_TD_MON)

def mrpt_318_mean_reversion_z_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_318_mean_reversion_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(63).diff(_TD_MON)

def mrpt_319_mean_reversion_z_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_319_mean_reversion_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(126).diff(_TD_MON)

def mrpt_320_mean_reversion_z_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_320_mean_reversion_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(252).diff(_TD_MON)

def mrpt_321_extreme_stretch_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_321_extreme_stretch_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(5).diff(_TD_MON)

def mrpt_322_extreme_stretch_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_322_extreme_stretch_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(21).diff(_TD_MON)

def mrpt_323_extreme_stretch_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_323_extreme_stretch_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(63).diff(_TD_MON)

def mrpt_324_extreme_stretch_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_324_extreme_stretch_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(126).diff(_TD_MON)

def mrpt_325_extreme_stretch_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_325_extreme_stretch_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(252).diff(_TD_MON)

def mrpt_326_reversion_velocity_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_326_reversion_velocity_accel_5d
    ECONOMIC RATIONALE: Acceleration of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(5).diff(_TD_MON)

def mrpt_327_reversion_velocity_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_327_reversion_velocity_accel_21d
    ECONOMIC RATIONALE: Acceleration of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(21).diff(_TD_MON)

def mrpt_328_reversion_velocity_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_328_reversion_velocity_accel_63d
    ECONOMIC RATIONALE: Acceleration of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(63).diff(_TD_MON)

def mrpt_329_reversion_velocity_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_329_reversion_velocity_accel_126d
    ECONOMIC RATIONALE: Acceleration of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(126).diff(_TD_MON)

def mrpt_330_reversion_velocity_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_330_reversion_velocity_accel_252d
    ECONOMIC RATIONALE: Acceleration of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(252).diff(_TD_MON)

def mrpt_331_ma_cross_intensity_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_331_ma_cross_intensity_accel_5d
    ECONOMIC RATIONALE: Acceleration of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(5).diff(_TD_MON)

def mrpt_332_ma_cross_intensity_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_332_ma_cross_intensity_accel_21d
    ECONOMIC RATIONALE: Acceleration of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(21).diff(_TD_MON)

def mrpt_333_ma_cross_intensity_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_333_ma_cross_intensity_accel_63d
    ECONOMIC RATIONALE: Acceleration of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(63).diff(_TD_MON)

def mrpt_334_ma_cross_intensity_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_334_ma_cross_intensity_accel_126d
    ECONOMIC RATIONALE: Acceleration of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(126).diff(_TD_MON)

def mrpt_335_ma_cross_intensity_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_335_ma_cross_intensity_accel_252d
    ECONOMIC RATIONALE: Acceleration of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(252).diff(_TD_MON)

def mrpt_336_overshot_magnitude_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_336_overshot_magnitude_accel_5d
    ECONOMIC RATIONALE: Acceleration of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(5).diff(_TD_MON)

def mrpt_337_overshot_magnitude_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_337_overshot_magnitude_accel_21d
    ECONOMIC RATIONALE: Acceleration of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(21).diff(_TD_MON)

def mrpt_338_overshot_magnitude_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_338_overshot_magnitude_accel_63d
    ECONOMIC RATIONALE: Acceleration of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(63).diff(_TD_MON)

def mrpt_339_overshot_magnitude_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_339_overshot_magnitude_accel_126d
    ECONOMIC RATIONALE: Acceleration of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(126).diff(_TD_MON)

def mrpt_340_overshot_magnitude_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_340_overshot_magnitude_accel_252d
    ECONOMIC RATIONALE: Acceleration of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(252).diff(_TD_MON)

def mrpt_341_mean_reversion_rank_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_341_mean_reversion_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(5).diff(_TD_MON)

def mrpt_342_mean_reversion_rank_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_342_mean_reversion_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(21).diff(_TD_MON)

def mrpt_343_mean_reversion_rank_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_343_mean_reversion_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(63).diff(_TD_MON)

def mrpt_344_mean_reversion_rank_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_344_mean_reversion_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(126).diff(_TD_MON)

def mrpt_345_mean_reversion_rank_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_345_mean_reversion_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(252).diff(_TD_MON)

def mrpt_346_volatility_adjusted_stretch_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_346_volatility_adjusted_stretch_accel_5d
    ECONOMIC RATIONALE: Acceleration of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(5).diff(_TD_MON)

def mrpt_347_volatility_adjusted_stretch_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_347_volatility_adjusted_stretch_accel_21d
    ECONOMIC RATIONALE: Acceleration of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(21).diff(_TD_MON)

def mrpt_348_volatility_adjusted_stretch_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_348_volatility_adjusted_stretch_accel_63d
    ECONOMIC RATIONALE: Acceleration of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(63).diff(_TD_MON)

def mrpt_349_volatility_adjusted_stretch_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_349_volatility_adjusted_stretch_accel_126d
    ECONOMIC RATIONALE: Acceleration of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(126).diff(_TD_MON)

def mrpt_350_volatility_adjusted_stretch_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_350_volatility_adjusted_stretch_accel_252d
    ECONOMIC RATIONALE: Acceleration of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(252).diff(_TD_MON)

def mrpt_351_mean_reversion_score_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_351_mean_reversion_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(5).diff(_TD_MON)

def mrpt_352_mean_reversion_score_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_352_mean_reversion_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(21).diff(_TD_MON)

def mrpt_353_mean_reversion_score_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_353_mean_reversion_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(63).diff(_TD_MON)

def mrpt_354_mean_reversion_score_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_354_mean_reversion_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(126).diff(_TD_MON)

def mrpt_355_mean_reversion_score_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_355_mean_reversion_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(252).diff(_TD_MON)

def mrpt_356_price_to_median_ratio_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_356_price_to_median_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(5).diff(_TD_MON)

def mrpt_357_price_to_median_ratio_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_357_price_to_median_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(21).diff(_TD_MON)

def mrpt_358_price_to_median_ratio_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_358_price_to_median_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(63).diff(_TD_MON)

def mrpt_359_price_to_median_ratio_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_359_price_to_median_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(126).diff(_TD_MON)

def mrpt_360_price_to_median_ratio_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_360_price_to_median_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(252).diff(_TD_MON)

def mrpt_361_reversion_potential_index_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_361_reversion_potential_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(5).diff(_TD_MON)

def mrpt_362_reversion_potential_index_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_362_reversion_potential_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(21).diff(_TD_MON)

def mrpt_363_reversion_potential_index_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_363_reversion_potential_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(63).diff(_TD_MON)

def mrpt_364_reversion_potential_index_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_364_reversion_potential_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(126).diff(_TD_MON)

def mrpt_365_reversion_potential_index_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_365_reversion_potential_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(252).diff(_TD_MON)

def mrpt_366_linear_regression_slope_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_366_linear_regression_slope_accel_5d
    ECONOMIC RATIONALE: Acceleration of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(5).diff(_TD_MON)

def mrpt_367_linear_regression_slope_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_367_linear_regression_slope_accel_21d
    ECONOMIC RATIONALE: Acceleration of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(21).diff(_TD_MON)

def mrpt_368_linear_regression_slope_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_368_linear_regression_slope_accel_63d
    ECONOMIC RATIONALE: Acceleration of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(63).diff(_TD_MON)

def mrpt_369_linear_regression_slope_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_369_linear_regression_slope_accel_126d
    ECONOMIC RATIONALE: Acceleration of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(126).diff(_TD_MON)

def mrpt_370_linear_regression_slope_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_370_linear_regression_slope_accel_252d
    ECONOMIC RATIONALE: Acceleration of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(252).diff(_TD_MON)

def mrpt_371_standard_error_channel_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_371_standard_error_channel_accel_5d
    ECONOMIC RATIONALE: Acceleration of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(5).diff(_TD_MON)

def mrpt_372_standard_error_channel_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_372_standard_error_channel_accel_21d
    ECONOMIC RATIONALE: Acceleration of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(21).diff(_TD_MON)

def mrpt_373_standard_error_channel_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_373_standard_error_channel_accel_63d
    ECONOMIC RATIONALE: Acceleration of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(63).diff(_TD_MON)

def mrpt_374_standard_error_channel_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_374_standard_error_channel_accel_126d
    ECONOMIC RATIONALE: Acceleration of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(126).diff(_TD_MON)

def mrpt_375_standard_error_channel_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_375_standard_error_channel_accel_252d
    ECONOMIC RATIONALE: Acceleration of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V104_REGISTRY_ACCEL = {
    "mrpt_301_bollinger_pct_b_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_301_bollinger_pct_b_accel_5d},
    "mrpt_302_bollinger_pct_b_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_302_bollinger_pct_b_accel_21d},
    "mrpt_303_bollinger_pct_b_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_303_bollinger_pct_b_accel_63d},
    "mrpt_304_bollinger_pct_b_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_304_bollinger_pct_b_accel_126d},
    "mrpt_305_bollinger_pct_b_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_305_bollinger_pct_b_accel_252d},
    "mrpt_306_distance_from_ma200_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_306_distance_from_ma200_accel_5d},
    "mrpt_307_distance_from_ma200_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_307_distance_from_ma200_accel_21d},
    "mrpt_308_distance_from_ma200_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_308_distance_from_ma200_accel_63d},
    "mrpt_309_distance_from_ma200_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_309_distance_from_ma200_accel_126d},
    "mrpt_310_distance_from_ma200_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_310_distance_from_ma200_accel_252d},
    "mrpt_311_keltner_channel_lower_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_311_keltner_channel_lower_accel_5d},
    "mrpt_312_keltner_channel_lower_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_312_keltner_channel_lower_accel_21d},
    "mrpt_313_keltner_channel_lower_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_313_keltner_channel_lower_accel_63d},
    "mrpt_314_keltner_channel_lower_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_314_keltner_channel_lower_accel_126d},
    "mrpt_315_keltner_channel_lower_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_315_keltner_channel_lower_accel_252d},
    "mrpt_316_mean_reversion_z_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_316_mean_reversion_z_accel_5d},
    "mrpt_317_mean_reversion_z_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_317_mean_reversion_z_accel_21d},
    "mrpt_318_mean_reversion_z_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_318_mean_reversion_z_accel_63d},
    "mrpt_319_mean_reversion_z_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_319_mean_reversion_z_accel_126d},
    "mrpt_320_mean_reversion_z_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_320_mean_reversion_z_accel_252d},
    "mrpt_321_extreme_stretch_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_321_extreme_stretch_accel_5d},
    "mrpt_322_extreme_stretch_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_322_extreme_stretch_accel_21d},
    "mrpt_323_extreme_stretch_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_323_extreme_stretch_accel_63d},
    "mrpt_324_extreme_stretch_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_324_extreme_stretch_accel_126d},
    "mrpt_325_extreme_stretch_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_325_extreme_stretch_accel_252d},
    "mrpt_326_reversion_velocity_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_326_reversion_velocity_accel_5d},
    "mrpt_327_reversion_velocity_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_327_reversion_velocity_accel_21d},
    "mrpt_328_reversion_velocity_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_328_reversion_velocity_accel_63d},
    "mrpt_329_reversion_velocity_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_329_reversion_velocity_accel_126d},
    "mrpt_330_reversion_velocity_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_330_reversion_velocity_accel_252d},
    "mrpt_331_ma_cross_intensity_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_331_ma_cross_intensity_accel_5d},
    "mrpt_332_ma_cross_intensity_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_332_ma_cross_intensity_accel_21d},
    "mrpt_333_ma_cross_intensity_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_333_ma_cross_intensity_accel_63d},
    "mrpt_334_ma_cross_intensity_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_334_ma_cross_intensity_accel_126d},
    "mrpt_335_ma_cross_intensity_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_335_ma_cross_intensity_accel_252d},
    "mrpt_336_overshot_magnitude_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_336_overshot_magnitude_accel_5d},
    "mrpt_337_overshot_magnitude_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_337_overshot_magnitude_accel_21d},
    "mrpt_338_overshot_magnitude_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_338_overshot_magnitude_accel_63d},
    "mrpt_339_overshot_magnitude_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_339_overshot_magnitude_accel_126d},
    "mrpt_340_overshot_magnitude_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_340_overshot_magnitude_accel_252d},
    "mrpt_341_mean_reversion_rank_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_341_mean_reversion_rank_accel_5d},
    "mrpt_342_mean_reversion_rank_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_342_mean_reversion_rank_accel_21d},
    "mrpt_343_mean_reversion_rank_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_343_mean_reversion_rank_accel_63d},
    "mrpt_344_mean_reversion_rank_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_344_mean_reversion_rank_accel_126d},
    "mrpt_345_mean_reversion_rank_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_345_mean_reversion_rank_accel_252d},
    "mrpt_346_volatility_adjusted_stretch_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_346_volatility_adjusted_stretch_accel_5d},
    "mrpt_347_volatility_adjusted_stretch_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_347_volatility_adjusted_stretch_accel_21d},
    "mrpt_348_volatility_adjusted_stretch_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_348_volatility_adjusted_stretch_accel_63d},
    "mrpt_349_volatility_adjusted_stretch_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_349_volatility_adjusted_stretch_accel_126d},
    "mrpt_350_volatility_adjusted_stretch_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_350_volatility_adjusted_stretch_accel_252d},
    "mrpt_351_mean_reversion_score_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_351_mean_reversion_score_accel_5d},
    "mrpt_352_mean_reversion_score_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_352_mean_reversion_score_accel_21d},
    "mrpt_353_mean_reversion_score_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_353_mean_reversion_score_accel_63d},
    "mrpt_354_mean_reversion_score_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_354_mean_reversion_score_accel_126d},
    "mrpt_355_mean_reversion_score_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_355_mean_reversion_score_accel_252d},
    "mrpt_356_price_to_median_ratio_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_356_price_to_median_ratio_accel_5d},
    "mrpt_357_price_to_median_ratio_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_357_price_to_median_ratio_accel_21d},
    "mrpt_358_price_to_median_ratio_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_358_price_to_median_ratio_accel_63d},
    "mrpt_359_price_to_median_ratio_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_359_price_to_median_ratio_accel_126d},
    "mrpt_360_price_to_median_ratio_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_360_price_to_median_ratio_accel_252d},
    "mrpt_361_reversion_potential_index_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_361_reversion_potential_index_accel_5d},
    "mrpt_362_reversion_potential_index_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_362_reversion_potential_index_accel_21d},
    "mrpt_363_reversion_potential_index_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_363_reversion_potential_index_accel_63d},
    "mrpt_364_reversion_potential_index_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_364_reversion_potential_index_accel_126d},
    "mrpt_365_reversion_potential_index_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_365_reversion_potential_index_accel_252d},
    "mrpt_366_linear_regression_slope_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_366_linear_regression_slope_accel_5d},
    "mrpt_367_linear_regression_slope_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_367_linear_regression_slope_accel_21d},
    "mrpt_368_linear_regression_slope_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_368_linear_regression_slope_accel_63d},
    "mrpt_369_linear_regression_slope_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_369_linear_regression_slope_accel_126d},
    "mrpt_370_linear_regression_slope_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_370_linear_regression_slope_accel_252d},
    "mrpt_371_standard_error_channel_accel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_371_standard_error_channel_accel_5d},
    "mrpt_372_standard_error_channel_accel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_372_standard_error_channel_accel_21d},
    "mrpt_373_standard_error_channel_accel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_373_standard_error_channel_accel_63d},
    "mrpt_374_standard_error_channel_accel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_374_standard_error_channel_accel_126d},
    "mrpt_375_standard_error_channel_accel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_375_standard_error_channel_accel_252d},
}
