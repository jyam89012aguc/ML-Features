"""
104_mean_reversion_potential — Velocity (2nd Derivatives)
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

def mrpt_226_bollinger_pct_b_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_226_bollinger_pct_b_vel_5d
    ECONOMIC RATIONALE: Velocity of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(5)

def mrpt_227_bollinger_pct_b_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_227_bollinger_pct_b_vel_21d
    ECONOMIC RATIONALE: Velocity of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(21)

def mrpt_228_bollinger_pct_b_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_228_bollinger_pct_b_vel_63d
    ECONOMIC RATIONALE: Velocity of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(63)

def mrpt_229_bollinger_pct_b_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_229_bollinger_pct_b_vel_126d
    ECONOMIC RATIONALE: Velocity of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(126)

def mrpt_230_bollinger_pct_b_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_230_bollinger_pct_b_vel_252d
    ECONOMIC RATIONALE: Velocity of bollinger_pct_b. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).diff(252)

def mrpt_231_distance_from_ma200_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_231_distance_from_ma200_vel_5d
    ECONOMIC RATIONALE: Velocity of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(5)

def mrpt_232_distance_from_ma200_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_232_distance_from_ma200_vel_21d
    ECONOMIC RATIONALE: Velocity of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(21)

def mrpt_233_distance_from_ma200_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_233_distance_from_ma200_vel_63d
    ECONOMIC RATIONALE: Velocity of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(63)

def mrpt_234_distance_from_ma200_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_234_distance_from_ma200_vel_126d
    ECONOMIC RATIONALE: Velocity of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(126)

def mrpt_235_distance_from_ma200_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_235_distance_from_ma200_vel_252d
    ECONOMIC RATIONALE: Velocity of distance_from_ma200. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).diff(252)

def mrpt_236_keltner_channel_lower_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_236_keltner_channel_lower_vel_5d
    ECONOMIC RATIONALE: Velocity of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(5)

def mrpt_237_keltner_channel_lower_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_237_keltner_channel_lower_vel_21d
    ECONOMIC RATIONALE: Velocity of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(21)

def mrpt_238_keltner_channel_lower_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_238_keltner_channel_lower_vel_63d
    ECONOMIC RATIONALE: Velocity of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(63)

def mrpt_239_keltner_channel_lower_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_239_keltner_channel_lower_vel_126d
    ECONOMIC RATIONALE: Velocity of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(126)

def mrpt_240_keltner_channel_lower_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_240_keltner_channel_lower_vel_252d
    ECONOMIC RATIONALE: Velocity of keltner_channel_lower. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).diff(252)

def mrpt_241_mean_reversion_z_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_241_mean_reversion_z_vel_5d
    ECONOMIC RATIONALE: Velocity of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(5)

def mrpt_242_mean_reversion_z_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_242_mean_reversion_z_vel_21d
    ECONOMIC RATIONALE: Velocity of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(21)

def mrpt_243_mean_reversion_z_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_243_mean_reversion_z_vel_63d
    ECONOMIC RATIONALE: Velocity of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(63)

def mrpt_244_mean_reversion_z_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_244_mean_reversion_z_vel_126d
    ECONOMIC RATIONALE: Velocity of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(126)

def mrpt_245_mean_reversion_z_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_245_mean_reversion_z_vel_252d
    ECONOMIC RATIONALE: Velocity of mean_reversion_z. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).diff(252)

def mrpt_246_extreme_stretch_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_246_extreme_stretch_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(5)

def mrpt_247_extreme_stretch_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_247_extreme_stretch_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(21)

def mrpt_248_extreme_stretch_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_248_extreme_stretch_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(63)

def mrpt_249_extreme_stretch_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_249_extreme_stretch_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(126)

def mrpt_250_extreme_stretch_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_250_extreme_stretch_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_stretch. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).diff(252)

def mrpt_251_reversion_velocity_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_251_reversion_velocity_vel_5d
    ECONOMIC RATIONALE: Velocity of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(5)

def mrpt_252_reversion_velocity_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_252_reversion_velocity_vel_21d
    ECONOMIC RATIONALE: Velocity of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(21)

def mrpt_253_reversion_velocity_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_253_reversion_velocity_vel_63d
    ECONOMIC RATIONALE: Velocity of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(63)

def mrpt_254_reversion_velocity_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_254_reversion_velocity_vel_126d
    ECONOMIC RATIONALE: Velocity of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(126)

def mrpt_255_reversion_velocity_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_255_reversion_velocity_vel_252d
    ECONOMIC RATIONALE: Velocity of reversion_velocity. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).diff(252)

def mrpt_256_ma_cross_intensity_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_256_ma_cross_intensity_vel_5d
    ECONOMIC RATIONALE: Velocity of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(5)

def mrpt_257_ma_cross_intensity_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_257_ma_cross_intensity_vel_21d
    ECONOMIC RATIONALE: Velocity of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(21)

def mrpt_258_ma_cross_intensity_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_258_ma_cross_intensity_vel_63d
    ECONOMIC RATIONALE: Velocity of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(63)

def mrpt_259_ma_cross_intensity_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_259_ma_cross_intensity_vel_126d
    ECONOMIC RATIONALE: Velocity of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(126)

def mrpt_260_ma_cross_intensity_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_260_ma_cross_intensity_vel_252d
    ECONOMIC RATIONALE: Velocity of ma_cross_intensity. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).diff(252)

def mrpt_261_overshot_magnitude_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_261_overshot_magnitude_vel_5d
    ECONOMIC RATIONALE: Velocity of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(5)

def mrpt_262_overshot_magnitude_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_262_overshot_magnitude_vel_21d
    ECONOMIC RATIONALE: Velocity of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(21)

def mrpt_263_overshot_magnitude_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_263_overshot_magnitude_vel_63d
    ECONOMIC RATIONALE: Velocity of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(63)

def mrpt_264_overshot_magnitude_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_264_overshot_magnitude_vel_126d
    ECONOMIC RATIONALE: Velocity of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(126)

def mrpt_265_overshot_magnitude_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_265_overshot_magnitude_vel_252d
    ECONOMIC RATIONALE: Velocity of overshot_magnitude. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).diff(252)

def mrpt_266_mean_reversion_rank_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_266_mean_reversion_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(5)

def mrpt_267_mean_reversion_rank_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_267_mean_reversion_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(21)

def mrpt_268_mean_reversion_rank_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_268_mean_reversion_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(63)

def mrpt_269_mean_reversion_rank_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_269_mean_reversion_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(126)

def mrpt_270_mean_reversion_rank_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_270_mean_reversion_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of mean_reversion_rank. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).diff(252)

def mrpt_271_volatility_adjusted_stretch_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_271_volatility_adjusted_stretch_vel_5d
    ECONOMIC RATIONALE: Velocity of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(5)

def mrpt_272_volatility_adjusted_stretch_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_272_volatility_adjusted_stretch_vel_21d
    ECONOMIC RATIONALE: Velocity of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(21)

def mrpt_273_volatility_adjusted_stretch_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_273_volatility_adjusted_stretch_vel_63d
    ECONOMIC RATIONALE: Velocity of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(63)

def mrpt_274_volatility_adjusted_stretch_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_274_volatility_adjusted_stretch_vel_126d
    ECONOMIC RATIONALE: Velocity of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(126)

def mrpt_275_volatility_adjusted_stretch_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_275_volatility_adjusted_stretch_vel_252d
    ECONOMIC RATIONALE: Velocity of volatility_adjusted_stretch. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).diff(252)

def mrpt_276_mean_reversion_score_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_276_mean_reversion_score_vel_5d
    ECONOMIC RATIONALE: Velocity of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(5)

def mrpt_277_mean_reversion_score_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_277_mean_reversion_score_vel_21d
    ECONOMIC RATIONALE: Velocity of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(21)

def mrpt_278_mean_reversion_score_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_278_mean_reversion_score_vel_63d
    ECONOMIC RATIONALE: Velocity of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(63)

def mrpt_279_mean_reversion_score_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_279_mean_reversion_score_vel_126d
    ECONOMIC RATIONALE: Velocity of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(126)

def mrpt_280_mean_reversion_score_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_280_mean_reversion_score_vel_252d
    ECONOMIC RATIONALE: Velocity of mean_reversion_score. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).diff(252)

def mrpt_281_price_to_median_ratio_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_281_price_to_median_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(5)

def mrpt_282_price_to_median_ratio_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_282_price_to_median_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(21)

def mrpt_283_price_to_median_ratio_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_283_price_to_median_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(63)

def mrpt_284_price_to_median_ratio_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_284_price_to_median_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(126)

def mrpt_285_price_to_median_ratio_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_285_price_to_median_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of price_to_median_ratio. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).diff(252)

def mrpt_286_reversion_potential_index_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_286_reversion_potential_index_vel_5d
    ECONOMIC RATIONALE: Velocity of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(5)

def mrpt_287_reversion_potential_index_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_287_reversion_potential_index_vel_21d
    ECONOMIC RATIONALE: Velocity of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(21)

def mrpt_288_reversion_potential_index_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_288_reversion_potential_index_vel_63d
    ECONOMIC RATIONALE: Velocity of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(63)

def mrpt_289_reversion_potential_index_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_289_reversion_potential_index_vel_126d
    ECONOMIC RATIONALE: Velocity of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(126)

def mrpt_290_reversion_potential_index_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_290_reversion_potential_index_vel_252d
    ECONOMIC RATIONALE: Velocity of reversion_potential_index. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).diff(252)

def mrpt_291_linear_regression_slope_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_291_linear_regression_slope_vel_5d
    ECONOMIC RATIONALE: Velocity of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(5)

def mrpt_292_linear_regression_slope_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_292_linear_regression_slope_vel_21d
    ECONOMIC RATIONALE: Velocity of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(21)

def mrpt_293_linear_regression_slope_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_293_linear_regression_slope_vel_63d
    ECONOMIC RATIONALE: Velocity of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(63)

def mrpt_294_linear_regression_slope_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_294_linear_regression_slope_vel_126d
    ECONOMIC RATIONALE: Velocity of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(126)

def mrpt_295_linear_regression_slope_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_295_linear_regression_slope_vel_252d
    ECONOMIC RATIONALE: Velocity of linear_regression_slope. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).diff(252)

def mrpt_296_standard_error_channel_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_296_standard_error_channel_vel_5d
    ECONOMIC RATIONALE: Velocity of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(5)

def mrpt_297_standard_error_channel_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_297_standard_error_channel_vel_21d
    ECONOMIC RATIONALE: Velocity of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(21)

def mrpt_298_standard_error_channel_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_298_standard_error_channel_vel_63d
    ECONOMIC RATIONALE: Velocity of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(63)

def mrpt_299_standard_error_channel_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_299_standard_error_channel_vel_126d
    ECONOMIC RATIONALE: Velocity of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(126)

def mrpt_300_standard_error_channel_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_300_standard_error_channel_vel_252d
    ECONOMIC RATIONALE: Velocity of standard_error_channel. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V104_REGISTRY_VEL = {
    "mrpt_226_bollinger_pct_b_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_226_bollinger_pct_b_vel_5d},
    "mrpt_227_bollinger_pct_b_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_227_bollinger_pct_b_vel_21d},
    "mrpt_228_bollinger_pct_b_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_228_bollinger_pct_b_vel_63d},
    "mrpt_229_bollinger_pct_b_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_229_bollinger_pct_b_vel_126d},
    "mrpt_230_bollinger_pct_b_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_230_bollinger_pct_b_vel_252d},
    "mrpt_231_distance_from_ma200_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_231_distance_from_ma200_vel_5d},
    "mrpt_232_distance_from_ma200_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_232_distance_from_ma200_vel_21d},
    "mrpt_233_distance_from_ma200_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_233_distance_from_ma200_vel_63d},
    "mrpt_234_distance_from_ma200_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_234_distance_from_ma200_vel_126d},
    "mrpt_235_distance_from_ma200_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_235_distance_from_ma200_vel_252d},
    "mrpt_236_keltner_channel_lower_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_236_keltner_channel_lower_vel_5d},
    "mrpt_237_keltner_channel_lower_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_237_keltner_channel_lower_vel_21d},
    "mrpt_238_keltner_channel_lower_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_238_keltner_channel_lower_vel_63d},
    "mrpt_239_keltner_channel_lower_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_239_keltner_channel_lower_vel_126d},
    "mrpt_240_keltner_channel_lower_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_240_keltner_channel_lower_vel_252d},
    "mrpt_241_mean_reversion_z_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_241_mean_reversion_z_vel_5d},
    "mrpt_242_mean_reversion_z_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_242_mean_reversion_z_vel_21d},
    "mrpt_243_mean_reversion_z_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_243_mean_reversion_z_vel_63d},
    "mrpt_244_mean_reversion_z_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_244_mean_reversion_z_vel_126d},
    "mrpt_245_mean_reversion_z_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_245_mean_reversion_z_vel_252d},
    "mrpt_246_extreme_stretch_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_246_extreme_stretch_vel_5d},
    "mrpt_247_extreme_stretch_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_247_extreme_stretch_vel_21d},
    "mrpt_248_extreme_stretch_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_248_extreme_stretch_vel_63d},
    "mrpt_249_extreme_stretch_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_249_extreme_stretch_vel_126d},
    "mrpt_250_extreme_stretch_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_250_extreme_stretch_vel_252d},
    "mrpt_251_reversion_velocity_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_251_reversion_velocity_vel_5d},
    "mrpt_252_reversion_velocity_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_252_reversion_velocity_vel_21d},
    "mrpt_253_reversion_velocity_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_253_reversion_velocity_vel_63d},
    "mrpt_254_reversion_velocity_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_254_reversion_velocity_vel_126d},
    "mrpt_255_reversion_velocity_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_255_reversion_velocity_vel_252d},
    "mrpt_256_ma_cross_intensity_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_256_ma_cross_intensity_vel_5d},
    "mrpt_257_ma_cross_intensity_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_257_ma_cross_intensity_vel_21d},
    "mrpt_258_ma_cross_intensity_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_258_ma_cross_intensity_vel_63d},
    "mrpt_259_ma_cross_intensity_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_259_ma_cross_intensity_vel_126d},
    "mrpt_260_ma_cross_intensity_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_260_ma_cross_intensity_vel_252d},
    "mrpt_261_overshot_magnitude_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_261_overshot_magnitude_vel_5d},
    "mrpt_262_overshot_magnitude_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_262_overshot_magnitude_vel_21d},
    "mrpt_263_overshot_magnitude_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_263_overshot_magnitude_vel_63d},
    "mrpt_264_overshot_magnitude_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_264_overshot_magnitude_vel_126d},
    "mrpt_265_overshot_magnitude_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_265_overshot_magnitude_vel_252d},
    "mrpt_266_mean_reversion_rank_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_266_mean_reversion_rank_vel_5d},
    "mrpt_267_mean_reversion_rank_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_267_mean_reversion_rank_vel_21d},
    "mrpt_268_mean_reversion_rank_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_268_mean_reversion_rank_vel_63d},
    "mrpt_269_mean_reversion_rank_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_269_mean_reversion_rank_vel_126d},
    "mrpt_270_mean_reversion_rank_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_270_mean_reversion_rank_vel_252d},
    "mrpt_271_volatility_adjusted_stretch_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_271_volatility_adjusted_stretch_vel_5d},
    "mrpt_272_volatility_adjusted_stretch_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_272_volatility_adjusted_stretch_vel_21d},
    "mrpt_273_volatility_adjusted_stretch_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_273_volatility_adjusted_stretch_vel_63d},
    "mrpt_274_volatility_adjusted_stretch_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_274_volatility_adjusted_stretch_vel_126d},
    "mrpt_275_volatility_adjusted_stretch_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_275_volatility_adjusted_stretch_vel_252d},
    "mrpt_276_mean_reversion_score_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_276_mean_reversion_score_vel_5d},
    "mrpt_277_mean_reversion_score_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_277_mean_reversion_score_vel_21d},
    "mrpt_278_mean_reversion_score_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_278_mean_reversion_score_vel_63d},
    "mrpt_279_mean_reversion_score_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_279_mean_reversion_score_vel_126d},
    "mrpt_280_mean_reversion_score_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_280_mean_reversion_score_vel_252d},
    "mrpt_281_price_to_median_ratio_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_281_price_to_median_ratio_vel_5d},
    "mrpt_282_price_to_median_ratio_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_282_price_to_median_ratio_vel_21d},
    "mrpt_283_price_to_median_ratio_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_283_price_to_median_ratio_vel_63d},
    "mrpt_284_price_to_median_ratio_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_284_price_to_median_ratio_vel_126d},
    "mrpt_285_price_to_median_ratio_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_285_price_to_median_ratio_vel_252d},
    "mrpt_286_reversion_potential_index_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_286_reversion_potential_index_vel_5d},
    "mrpt_287_reversion_potential_index_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_287_reversion_potential_index_vel_21d},
    "mrpt_288_reversion_potential_index_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_288_reversion_potential_index_vel_63d},
    "mrpt_289_reversion_potential_index_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_289_reversion_potential_index_vel_126d},
    "mrpt_290_reversion_potential_index_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_290_reversion_potential_index_vel_252d},
    "mrpt_291_linear_regression_slope_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_291_linear_regression_slope_vel_5d},
    "mrpt_292_linear_regression_slope_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_292_linear_regression_slope_vel_21d},
    "mrpt_293_linear_regression_slope_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_293_linear_regression_slope_vel_63d},
    "mrpt_294_linear_regression_slope_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_294_linear_regression_slope_vel_126d},
    "mrpt_295_linear_regression_slope_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_295_linear_regression_slope_vel_252d},
    "mrpt_296_standard_error_channel_vel_5d": {"inputs": ["close", "high", "low"], "func": mrpt_296_standard_error_channel_vel_5d},
    "mrpt_297_standard_error_channel_vel_21d": {"inputs": ["close", "high", "low"], "func": mrpt_297_standard_error_channel_vel_21d},
    "mrpt_298_standard_error_channel_vel_63d": {"inputs": ["close", "high", "low"], "func": mrpt_298_standard_error_channel_vel_63d},
    "mrpt_299_standard_error_channel_vel_126d": {"inputs": ["close", "high", "low"], "func": mrpt_299_standard_error_channel_vel_126d},
    "mrpt_300_standard_error_channel_vel_252d": {"inputs": ["close", "high", "low"], "func": mrpt_300_standard_error_channel_vel_252d},
}
