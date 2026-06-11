"""
117_price_clustering_psychology — Acceleration (3rd Derivatives)
Domain: price_clustering_psychology
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

def ppsy_301_round_number_proximity_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_301_round_number_proximity_accel_5d
    ECONOMIC RATIONALE: Acceleration of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(5).diff(_TD_MON)

def ppsy_302_round_number_proximity_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_302_round_number_proximity_accel_21d
    ECONOMIC RATIONALE: Acceleration of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(21).diff(_TD_MON)

def ppsy_303_round_number_proximity_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_303_round_number_proximity_accel_63d
    ECONOMIC RATIONALE: Acceleration of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(63).diff(_TD_MON)

def ppsy_304_round_number_proximity_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_304_round_number_proximity_accel_126d
    ECONOMIC RATIONALE: Acceleration of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(126).diff(_TD_MON)

def ppsy_305_round_number_proximity_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_305_round_number_proximity_accel_252d
    ECONOMIC RATIONALE: Acceleration of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(252).diff(_TD_MON)

def ppsy_306_decade_number_proximity_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_306_decade_number_proximity_accel_5d
    ECONOMIC RATIONALE: Acceleration of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(5).diff(_TD_MON)

def ppsy_307_decade_number_proximity_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_307_decade_number_proximity_accel_21d
    ECONOMIC RATIONALE: Acceleration of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(21).diff(_TD_MON)

def ppsy_308_decade_number_proximity_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_308_decade_number_proximity_accel_63d
    ECONOMIC RATIONALE: Acceleration of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(63).diff(_TD_MON)

def ppsy_309_decade_number_proximity_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_309_decade_number_proximity_accel_126d
    ECONOMIC RATIONALE: Acceleration of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(126).diff(_TD_MON)

def ppsy_310_decade_number_proximity_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_310_decade_number_proximity_accel_252d
    ECONOMIC RATIONALE: Acceleration of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(252).diff(_TD_MON)

def ppsy_311_century_number_proximity_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_311_century_number_proximity_accel_5d
    ECONOMIC RATIONALE: Acceleration of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(5).diff(_TD_MON)

def ppsy_312_century_number_proximity_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_312_century_number_proximity_accel_21d
    ECONOMIC RATIONALE: Acceleration of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(21).diff(_TD_MON)

def ppsy_313_century_number_proximity_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_313_century_number_proximity_accel_63d
    ECONOMIC RATIONALE: Acceleration of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(63).diff(_TD_MON)

def ppsy_314_century_number_proximity_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_314_century_number_proximity_accel_126d
    ECONOMIC RATIONALE: Acceleration of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(126).diff(_TD_MON)

def ppsy_315_century_number_proximity_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_315_century_number_proximity_accel_252d
    ECONOMIC RATIONALE: Acceleration of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(252).diff(_TD_MON)

def ppsy_316_price_level_clustering_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_316_price_level_clustering_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(5).diff(_TD_MON)

def ppsy_317_price_level_clustering_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_317_price_level_clustering_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(21).diff(_TD_MON)

def ppsy_318_price_level_clustering_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_318_price_level_clustering_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(63).diff(_TD_MON)

def ppsy_319_price_level_clustering_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_319_price_level_clustering_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(126).diff(_TD_MON)

def ppsy_320_price_level_clustering_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_320_price_level_clustering_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(252).diff(_TD_MON)

def ppsy_321_clustering_entropy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_321_clustering_entropy_accel_5d
    ECONOMIC RATIONALE: Acceleration of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(5).diff(_TD_MON)

def ppsy_322_clustering_entropy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_322_clustering_entropy_accel_21d
    ECONOMIC RATIONALE: Acceleration of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(21).diff(_TD_MON)

def ppsy_323_clustering_entropy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_323_clustering_entropy_accel_63d
    ECONOMIC RATIONALE: Acceleration of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(63).diff(_TD_MON)

def ppsy_324_clustering_entropy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_324_clustering_entropy_accel_126d
    ECONOMIC RATIONALE: Acceleration of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(126).diff(_TD_MON)

def ppsy_325_clustering_entropy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_325_clustering_entropy_accel_252d
    ECONOMIC RATIONALE: Acceleration of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(252).diff(_TD_MON)

def ppsy_326_price_support_psych_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_326_price_support_psych_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(5).diff(_TD_MON)

def ppsy_327_price_support_psych_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_327_price_support_psych_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(21).diff(_TD_MON)

def ppsy_328_price_support_psych_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_328_price_support_psych_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(63).diff(_TD_MON)

def ppsy_329_price_support_psych_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_329_price_support_psych_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(126).diff(_TD_MON)

def ppsy_330_price_support_psych_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_330_price_support_psych_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(252).diff(_TD_MON)

def ppsy_331_price_resistance_psych_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_331_price_resistance_psych_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(5).diff(_TD_MON)

def ppsy_332_price_resistance_psych_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_332_price_resistance_psych_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(21).diff(_TD_MON)

def ppsy_333_price_resistance_psych_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_333_price_resistance_psych_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(63).diff(_TD_MON)

def ppsy_334_price_resistance_psych_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_334_price_resistance_psych_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(126).diff(_TD_MON)

def ppsy_335_price_resistance_psych_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_335_price_resistance_psych_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(252).diff(_TD_MON)

def ppsy_336_clustering_zscore_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_336_clustering_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(5).diff(_TD_MON)

def ppsy_337_clustering_zscore_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_337_clustering_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(21).diff(_TD_MON)

def ppsy_338_clustering_zscore_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_338_clustering_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(63).diff(_TD_MON)

def ppsy_339_clustering_zscore_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_339_clustering_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(126).diff(_TD_MON)

def ppsy_340_clustering_zscore_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_340_clustering_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(252).diff(_TD_MON)

def ppsy_341_digit_bias_last_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_341_digit_bias_last_accel_5d
    ECONOMIC RATIONALE: Acceleration of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(5).diff(_TD_MON)

def ppsy_342_digit_bias_last_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_342_digit_bias_last_accel_21d
    ECONOMIC RATIONALE: Acceleration of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(21).diff(_TD_MON)

def ppsy_343_digit_bias_last_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_343_digit_bias_last_accel_63d
    ECONOMIC RATIONALE: Acceleration of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(63).diff(_TD_MON)

def ppsy_344_digit_bias_last_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_344_digit_bias_last_accel_126d
    ECONOMIC RATIONALE: Acceleration of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(126).diff(_TD_MON)

def ppsy_345_digit_bias_last_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_345_digit_bias_last_accel_252d
    ECONOMIC RATIONALE: Acceleration of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(252).diff(_TD_MON)

def ppsy_346_price_magnet_effect_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_346_price_magnet_effect_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(5).diff(_TD_MON)

def ppsy_347_price_magnet_effect_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_347_price_magnet_effect_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(21).diff(_TD_MON)

def ppsy_348_price_magnet_effect_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_348_price_magnet_effect_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(63).diff(_TD_MON)

def ppsy_349_price_magnet_effect_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_349_price_magnet_effect_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(126).diff(_TD_MON)

def ppsy_350_price_magnet_effect_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_350_price_magnet_effect_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(252).diff(_TD_MON)

def ppsy_351_clustering_regime_shift_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_351_clustering_regime_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(5).diff(_TD_MON)

def ppsy_352_clustering_regime_shift_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_352_clustering_regime_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(21).diff(_TD_MON)

def ppsy_353_clustering_regime_shift_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_353_clustering_regime_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(63).diff(_TD_MON)

def ppsy_354_clustering_regime_shift_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_354_clustering_regime_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(126).diff(_TD_MON)

def ppsy_355_clustering_regime_shift_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_355_clustering_regime_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(252).diff(_TD_MON)

def ppsy_356_psychological_breakthrough_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_356_psychological_breakthrough_accel_5d
    ECONOMIC RATIONALE: Acceleration of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(5).diff(_TD_MON)

def ppsy_357_psychological_breakthrough_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_357_psychological_breakthrough_accel_21d
    ECONOMIC RATIONALE: Acceleration of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(21).diff(_TD_MON)

def ppsy_358_psychological_breakthrough_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_358_psychological_breakthrough_accel_63d
    ECONOMIC RATIONALE: Acceleration of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(63).diff(_TD_MON)

def ppsy_359_psychological_breakthrough_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_359_psychological_breakthrough_accel_126d
    ECONOMIC RATIONALE: Acceleration of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(126).diff(_TD_MON)

def ppsy_360_psychological_breakthrough_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_360_psychological_breakthrough_accel_252d
    ECONOMIC RATIONALE: Acceleration of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(252).diff(_TD_MON)

def ppsy_361_price_stickiness_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_361_price_stickiness_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(5).diff(_TD_MON)

def ppsy_362_price_stickiness_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_362_price_stickiness_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(21).diff(_TD_MON)

def ppsy_363_price_stickiness_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_363_price_stickiness_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(63).diff(_TD_MON)

def ppsy_364_price_stickiness_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_364_price_stickiness_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(126).diff(_TD_MON)

def ppsy_365_price_stickiness_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_365_price_stickiness_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(252).diff(_TD_MON)

def ppsy_366_clustering_vol_corr_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_366_clustering_vol_corr_accel_5d
    ECONOMIC RATIONALE: Acceleration of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(5).diff(_TD_MON)

def ppsy_367_clustering_vol_corr_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_367_clustering_vol_corr_accel_21d
    ECONOMIC RATIONALE: Acceleration of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(21).diff(_TD_MON)

def ppsy_368_clustering_vol_corr_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_368_clustering_vol_corr_accel_63d
    ECONOMIC RATIONALE: Acceleration of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(63).diff(_TD_MON)

def ppsy_369_clustering_vol_corr_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_369_clustering_vol_corr_accel_126d
    ECONOMIC RATIONALE: Acceleration of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(126).diff(_TD_MON)

def ppsy_370_clustering_vol_corr_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_370_clustering_vol_corr_accel_252d
    ECONOMIC RATIONALE: Acceleration of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(252).diff(_TD_MON)

def ppsy_371_psych_exhaustion_proxy_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_371_psych_exhaustion_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(5).diff(_TD_MON)

def ppsy_372_psych_exhaustion_proxy_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_372_psych_exhaustion_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(21).diff(_TD_MON)

def ppsy_373_psych_exhaustion_proxy_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_373_psych_exhaustion_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(63).diff(_TD_MON)

def ppsy_374_psych_exhaustion_proxy_accel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_374_psych_exhaustion_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(126).diff(_TD_MON)

def ppsy_375_psych_exhaustion_proxy_accel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_375_psych_exhaustion_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V117_REGISTRY_ACCEL = {
    "ppsy_301_round_number_proximity_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_301_round_number_proximity_accel_5d},
    "ppsy_302_round_number_proximity_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_302_round_number_proximity_accel_21d},
    "ppsy_303_round_number_proximity_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_303_round_number_proximity_accel_63d},
    "ppsy_304_round_number_proximity_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_304_round_number_proximity_accel_126d},
    "ppsy_305_round_number_proximity_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_305_round_number_proximity_accel_252d},
    "ppsy_306_decade_number_proximity_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_306_decade_number_proximity_accel_5d},
    "ppsy_307_decade_number_proximity_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_307_decade_number_proximity_accel_21d},
    "ppsy_308_decade_number_proximity_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_308_decade_number_proximity_accel_63d},
    "ppsy_309_decade_number_proximity_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_309_decade_number_proximity_accel_126d},
    "ppsy_310_decade_number_proximity_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_310_decade_number_proximity_accel_252d},
    "ppsy_311_century_number_proximity_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_311_century_number_proximity_accel_5d},
    "ppsy_312_century_number_proximity_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_312_century_number_proximity_accel_21d},
    "ppsy_313_century_number_proximity_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_313_century_number_proximity_accel_63d},
    "ppsy_314_century_number_proximity_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_314_century_number_proximity_accel_126d},
    "ppsy_315_century_number_proximity_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_315_century_number_proximity_accel_252d},
    "ppsy_316_price_level_clustering_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_316_price_level_clustering_accel_5d},
    "ppsy_317_price_level_clustering_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_317_price_level_clustering_accel_21d},
    "ppsy_318_price_level_clustering_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_318_price_level_clustering_accel_63d},
    "ppsy_319_price_level_clustering_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_319_price_level_clustering_accel_126d},
    "ppsy_320_price_level_clustering_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_320_price_level_clustering_accel_252d},
    "ppsy_321_clustering_entropy_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_321_clustering_entropy_accel_5d},
    "ppsy_322_clustering_entropy_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_322_clustering_entropy_accel_21d},
    "ppsy_323_clustering_entropy_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_323_clustering_entropy_accel_63d},
    "ppsy_324_clustering_entropy_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_324_clustering_entropy_accel_126d},
    "ppsy_325_clustering_entropy_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_325_clustering_entropy_accel_252d},
    "ppsy_326_price_support_psych_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_326_price_support_psych_accel_5d},
    "ppsy_327_price_support_psych_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_327_price_support_psych_accel_21d},
    "ppsy_328_price_support_psych_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_328_price_support_psych_accel_63d},
    "ppsy_329_price_support_psych_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_329_price_support_psych_accel_126d},
    "ppsy_330_price_support_psych_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_330_price_support_psych_accel_252d},
    "ppsy_331_price_resistance_psych_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_331_price_resistance_psych_accel_5d},
    "ppsy_332_price_resistance_psych_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_332_price_resistance_psych_accel_21d},
    "ppsy_333_price_resistance_psych_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_333_price_resistance_psych_accel_63d},
    "ppsy_334_price_resistance_psych_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_334_price_resistance_psych_accel_126d},
    "ppsy_335_price_resistance_psych_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_335_price_resistance_psych_accel_252d},
    "ppsy_336_clustering_zscore_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_336_clustering_zscore_accel_5d},
    "ppsy_337_clustering_zscore_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_337_clustering_zscore_accel_21d},
    "ppsy_338_clustering_zscore_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_338_clustering_zscore_accel_63d},
    "ppsy_339_clustering_zscore_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_339_clustering_zscore_accel_126d},
    "ppsy_340_clustering_zscore_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_340_clustering_zscore_accel_252d},
    "ppsy_341_digit_bias_last_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_341_digit_bias_last_accel_5d},
    "ppsy_342_digit_bias_last_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_342_digit_bias_last_accel_21d},
    "ppsy_343_digit_bias_last_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_343_digit_bias_last_accel_63d},
    "ppsy_344_digit_bias_last_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_344_digit_bias_last_accel_126d},
    "ppsy_345_digit_bias_last_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_345_digit_bias_last_accel_252d},
    "ppsy_346_price_magnet_effect_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_346_price_magnet_effect_accel_5d},
    "ppsy_347_price_magnet_effect_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_347_price_magnet_effect_accel_21d},
    "ppsy_348_price_magnet_effect_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_348_price_magnet_effect_accel_63d},
    "ppsy_349_price_magnet_effect_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_349_price_magnet_effect_accel_126d},
    "ppsy_350_price_magnet_effect_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_350_price_magnet_effect_accel_252d},
    "ppsy_351_clustering_regime_shift_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_351_clustering_regime_shift_accel_5d},
    "ppsy_352_clustering_regime_shift_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_352_clustering_regime_shift_accel_21d},
    "ppsy_353_clustering_regime_shift_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_353_clustering_regime_shift_accel_63d},
    "ppsy_354_clustering_regime_shift_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_354_clustering_regime_shift_accel_126d},
    "ppsy_355_clustering_regime_shift_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_355_clustering_regime_shift_accel_252d},
    "ppsy_356_psychological_breakthrough_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_356_psychological_breakthrough_accel_5d},
    "ppsy_357_psychological_breakthrough_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_357_psychological_breakthrough_accel_21d},
    "ppsy_358_psychological_breakthrough_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_358_psychological_breakthrough_accel_63d},
    "ppsy_359_psychological_breakthrough_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_359_psychological_breakthrough_accel_126d},
    "ppsy_360_psychological_breakthrough_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_360_psychological_breakthrough_accel_252d},
    "ppsy_361_price_stickiness_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_361_price_stickiness_accel_5d},
    "ppsy_362_price_stickiness_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_362_price_stickiness_accel_21d},
    "ppsy_363_price_stickiness_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_363_price_stickiness_accel_63d},
    "ppsy_364_price_stickiness_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_364_price_stickiness_accel_126d},
    "ppsy_365_price_stickiness_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_365_price_stickiness_accel_252d},
    "ppsy_366_clustering_vol_corr_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_366_clustering_vol_corr_accel_5d},
    "ppsy_367_clustering_vol_corr_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_367_clustering_vol_corr_accel_21d},
    "ppsy_368_clustering_vol_corr_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_368_clustering_vol_corr_accel_63d},
    "ppsy_369_clustering_vol_corr_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_369_clustering_vol_corr_accel_126d},
    "ppsy_370_clustering_vol_corr_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_370_clustering_vol_corr_accel_252d},
    "ppsy_371_psych_exhaustion_proxy_accel_5d": {"inputs": ["close", "volume"], "func": ppsy_371_psych_exhaustion_proxy_accel_5d},
    "ppsy_372_psych_exhaustion_proxy_accel_21d": {"inputs": ["close", "volume"], "func": ppsy_372_psych_exhaustion_proxy_accel_21d},
    "ppsy_373_psych_exhaustion_proxy_accel_63d": {"inputs": ["close", "volume"], "func": ppsy_373_psych_exhaustion_proxy_accel_63d},
    "ppsy_374_psych_exhaustion_proxy_accel_126d": {"inputs": ["close", "volume"], "func": ppsy_374_psych_exhaustion_proxy_accel_126d},
    "ppsy_375_psych_exhaustion_proxy_accel_252d": {"inputs": ["close", "volume"], "func": ppsy_375_psych_exhaustion_proxy_accel_252d},
}
