"""
117_price_clustering_psychology — Velocity (2nd Derivatives)
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

def ppsy_226_round_number_proximity_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_226_round_number_proximity_vel_5d
    ECONOMIC RATIONALE: Velocity of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(5)

def ppsy_227_round_number_proximity_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_227_round_number_proximity_vel_21d
    ECONOMIC RATIONALE: Velocity of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(21)

def ppsy_228_round_number_proximity_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_228_round_number_proximity_vel_63d
    ECONOMIC RATIONALE: Velocity of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(63)

def ppsy_229_round_number_proximity_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_229_round_number_proximity_vel_126d
    ECONOMIC RATIONALE: Velocity of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(126)

def ppsy_230_round_number_proximity_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_230_round_number_proximity_vel_252d
    ECONOMIC RATIONALE: Velocity of round_number_proximity. Proximity to whole dollar amounts.
    """
    return (close % 1.0).diff(252)

def ppsy_231_decade_number_proximity_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_231_decade_number_proximity_vel_5d
    ECONOMIC RATIONALE: Velocity of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(5)

def ppsy_232_decade_number_proximity_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_232_decade_number_proximity_vel_21d
    ECONOMIC RATIONALE: Velocity of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(21)

def ppsy_233_decade_number_proximity_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_233_decade_number_proximity_vel_63d
    ECONOMIC RATIONALE: Velocity of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(63)

def ppsy_234_decade_number_proximity_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_234_decade_number_proximity_vel_126d
    ECONOMIC RATIONALE: Velocity of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(126)

def ppsy_235_decade_number_proximity_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_235_decade_number_proximity_vel_252d
    ECONOMIC RATIONALE: Velocity of decade_number_proximity. Proximity to ten-dollar increments.
    """
    return (close % 10.0).diff(252)

def ppsy_236_century_number_proximity_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_236_century_number_proximity_vel_5d
    ECONOMIC RATIONALE: Velocity of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(5)

def ppsy_237_century_number_proximity_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_237_century_number_proximity_vel_21d
    ECONOMIC RATIONALE: Velocity of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(21)

def ppsy_238_century_number_proximity_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_238_century_number_proximity_vel_63d
    ECONOMIC RATIONALE: Velocity of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(63)

def ppsy_239_century_number_proximity_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_239_century_number_proximity_vel_126d
    ECONOMIC RATIONALE: Velocity of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(126)

def ppsy_240_century_number_proximity_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_240_century_number_proximity_vel_252d
    ECONOMIC RATIONALE: Velocity of century_number_proximity. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).diff(252)

def ppsy_241_price_level_clustering_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_241_price_level_clustering_vel_5d
    ECONOMIC RATIONALE: Velocity of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(5)

def ppsy_242_price_level_clustering_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_242_price_level_clustering_vel_21d
    ECONOMIC RATIONALE: Velocity of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(21)

def ppsy_243_price_level_clustering_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_243_price_level_clustering_vel_63d
    ECONOMIC RATIONALE: Velocity of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(63)

def ppsy_244_price_level_clustering_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_244_price_level_clustering_vel_126d
    ECONOMIC RATIONALE: Velocity of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(126)

def ppsy_245_price_level_clustering_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_245_price_level_clustering_vel_252d
    ECONOMIC RATIONALE: Velocity of price_level_clustering. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).diff(252)

def ppsy_246_clustering_entropy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_246_clustering_entropy_vel_5d
    ECONOMIC RATIONALE: Velocity of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(5)

def ppsy_247_clustering_entropy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_247_clustering_entropy_vel_21d
    ECONOMIC RATIONALE: Velocity of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(21)

def ppsy_248_clustering_entropy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_248_clustering_entropy_vel_63d
    ECONOMIC RATIONALE: Velocity of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(63)

def ppsy_249_clustering_entropy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_249_clustering_entropy_vel_126d
    ECONOMIC RATIONALE: Velocity of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(126)

def ppsy_250_clustering_entropy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_250_clustering_entropy_vel_252d
    ECONOMIC RATIONALE: Velocity of clustering_entropy. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).diff(252)

def ppsy_251_price_support_psych_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_251_price_support_psych_vel_5d
    ECONOMIC RATIONALE: Velocity of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(5)

def ppsy_252_price_support_psych_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_252_price_support_psych_vel_21d
    ECONOMIC RATIONALE: Velocity of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(21)

def ppsy_253_price_support_psych_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_253_price_support_psych_vel_63d
    ECONOMIC RATIONALE: Velocity of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(63)

def ppsy_254_price_support_psych_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_254_price_support_psych_vel_126d
    ECONOMIC RATIONALE: Velocity of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(126)

def ppsy_255_price_support_psych_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_255_price_support_psych_vel_252d
    ECONOMIC RATIONALE: Velocity of price_support_psych. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).diff(252)

def ppsy_256_price_resistance_psych_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_256_price_resistance_psych_vel_5d
    ECONOMIC RATIONALE: Velocity of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(5)

def ppsy_257_price_resistance_psych_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_257_price_resistance_psych_vel_21d
    ECONOMIC RATIONALE: Velocity of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(21)

def ppsy_258_price_resistance_psych_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_258_price_resistance_psych_vel_63d
    ECONOMIC RATIONALE: Velocity of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(63)

def ppsy_259_price_resistance_psych_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_259_price_resistance_psych_vel_126d
    ECONOMIC RATIONALE: Velocity of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(126)

def ppsy_260_price_resistance_psych_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_260_price_resistance_psych_vel_252d
    ECONOMIC RATIONALE: Velocity of price_resistance_psych. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).diff(252)

def ppsy_261_clustering_zscore_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_261_clustering_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(5)

def ppsy_262_clustering_zscore_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_262_clustering_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(21)

def ppsy_263_clustering_zscore_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_263_clustering_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(63)

def ppsy_264_clustering_zscore_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_264_clustering_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(126)

def ppsy_265_clustering_zscore_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_265_clustering_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of clustering_zscore. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).diff(252)

def ppsy_266_digit_bias_last_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_266_digit_bias_last_vel_5d
    ECONOMIC RATIONALE: Velocity of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(5)

def ppsy_267_digit_bias_last_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_267_digit_bias_last_vel_21d
    ECONOMIC RATIONALE: Velocity of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(21)

def ppsy_268_digit_bias_last_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_268_digit_bias_last_vel_63d
    ECONOMIC RATIONALE: Velocity of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(63)

def ppsy_269_digit_bias_last_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_269_digit_bias_last_vel_126d
    ECONOMIC RATIONALE: Velocity of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(126)

def ppsy_270_digit_bias_last_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_270_digit_bias_last_vel_252d
    ECONOMIC RATIONALE: Velocity of digit_bias_last. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).diff(252)

def ppsy_271_price_magnet_effect_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_271_price_magnet_effect_vel_5d
    ECONOMIC RATIONALE: Velocity of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(5)

def ppsy_272_price_magnet_effect_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_272_price_magnet_effect_vel_21d
    ECONOMIC RATIONALE: Velocity of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(21)

def ppsy_273_price_magnet_effect_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_273_price_magnet_effect_vel_63d
    ECONOMIC RATIONALE: Velocity of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(63)

def ppsy_274_price_magnet_effect_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_274_price_magnet_effect_vel_126d
    ECONOMIC RATIONALE: Velocity of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(126)

def ppsy_275_price_magnet_effect_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_275_price_magnet_effect_vel_252d
    ECONOMIC RATIONALE: Velocity of price_magnet_effect. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).diff(252)

def ppsy_276_clustering_regime_shift_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_276_clustering_regime_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(5)

def ppsy_277_clustering_regime_shift_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_277_clustering_regime_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(21)

def ppsy_278_clustering_regime_shift_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_278_clustering_regime_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(63)

def ppsy_279_clustering_regime_shift_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_279_clustering_regime_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(126)

def ppsy_280_clustering_regime_shift_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_280_clustering_regime_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of clustering_regime_shift. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).diff(252)

def ppsy_281_psychological_breakthrough_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_281_psychological_breakthrough_vel_5d
    ECONOMIC RATIONALE: Velocity of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(5)

def ppsy_282_psychological_breakthrough_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_282_psychological_breakthrough_vel_21d
    ECONOMIC RATIONALE: Velocity of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(21)

def ppsy_283_psychological_breakthrough_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_283_psychological_breakthrough_vel_63d
    ECONOMIC RATIONALE: Velocity of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(63)

def ppsy_284_psychological_breakthrough_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_284_psychological_breakthrough_vel_126d
    ECONOMIC RATIONALE: Velocity of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(126)

def ppsy_285_psychological_breakthrough_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_285_psychological_breakthrough_vel_252d
    ECONOMIC RATIONALE: Velocity of psychological_breakthrough. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).diff(252)

def ppsy_286_price_stickiness_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_286_price_stickiness_vel_5d
    ECONOMIC RATIONALE: Velocity of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(5)

def ppsy_287_price_stickiness_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_287_price_stickiness_vel_21d
    ECONOMIC RATIONALE: Velocity of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(21)

def ppsy_288_price_stickiness_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_288_price_stickiness_vel_63d
    ECONOMIC RATIONALE: Velocity of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(63)

def ppsy_289_price_stickiness_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_289_price_stickiness_vel_126d
    ECONOMIC RATIONALE: Velocity of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(126)

def ppsy_290_price_stickiness_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_290_price_stickiness_vel_252d
    ECONOMIC RATIONALE: Velocity of price_stickiness. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).diff(252)

def ppsy_291_clustering_vol_corr_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_291_clustering_vol_corr_vel_5d
    ECONOMIC RATIONALE: Velocity of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(5)

def ppsy_292_clustering_vol_corr_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_292_clustering_vol_corr_vel_21d
    ECONOMIC RATIONALE: Velocity of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(21)

def ppsy_293_clustering_vol_corr_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_293_clustering_vol_corr_vel_63d
    ECONOMIC RATIONALE: Velocity of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(63)

def ppsy_294_clustering_vol_corr_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_294_clustering_vol_corr_vel_126d
    ECONOMIC RATIONALE: Velocity of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(126)

def ppsy_295_clustering_vol_corr_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_295_clustering_vol_corr_vel_252d
    ECONOMIC RATIONALE: Velocity of clustering_vol_corr. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).diff(252)

def ppsy_296_psych_exhaustion_proxy_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_296_psych_exhaustion_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(5)

def ppsy_297_psych_exhaustion_proxy_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_297_psych_exhaustion_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(21)

def ppsy_298_psych_exhaustion_proxy_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_298_psych_exhaustion_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(63)

def ppsy_299_psych_exhaustion_proxy_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_299_psych_exhaustion_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(126)

def ppsy_300_psych_exhaustion_proxy_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_300_psych_exhaustion_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of psych_exhaustion_proxy. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V117_REGISTRY_VEL = {
    "ppsy_226_round_number_proximity_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_226_round_number_proximity_vel_5d},
    "ppsy_227_round_number_proximity_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_227_round_number_proximity_vel_21d},
    "ppsy_228_round_number_proximity_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_228_round_number_proximity_vel_63d},
    "ppsy_229_round_number_proximity_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_229_round_number_proximity_vel_126d},
    "ppsy_230_round_number_proximity_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_230_round_number_proximity_vel_252d},
    "ppsy_231_decade_number_proximity_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_231_decade_number_proximity_vel_5d},
    "ppsy_232_decade_number_proximity_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_232_decade_number_proximity_vel_21d},
    "ppsy_233_decade_number_proximity_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_233_decade_number_proximity_vel_63d},
    "ppsy_234_decade_number_proximity_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_234_decade_number_proximity_vel_126d},
    "ppsy_235_decade_number_proximity_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_235_decade_number_proximity_vel_252d},
    "ppsy_236_century_number_proximity_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_236_century_number_proximity_vel_5d},
    "ppsy_237_century_number_proximity_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_237_century_number_proximity_vel_21d},
    "ppsy_238_century_number_proximity_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_238_century_number_proximity_vel_63d},
    "ppsy_239_century_number_proximity_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_239_century_number_proximity_vel_126d},
    "ppsy_240_century_number_proximity_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_240_century_number_proximity_vel_252d},
    "ppsy_241_price_level_clustering_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_241_price_level_clustering_vel_5d},
    "ppsy_242_price_level_clustering_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_242_price_level_clustering_vel_21d},
    "ppsy_243_price_level_clustering_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_243_price_level_clustering_vel_63d},
    "ppsy_244_price_level_clustering_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_244_price_level_clustering_vel_126d},
    "ppsy_245_price_level_clustering_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_245_price_level_clustering_vel_252d},
    "ppsy_246_clustering_entropy_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_246_clustering_entropy_vel_5d},
    "ppsy_247_clustering_entropy_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_247_clustering_entropy_vel_21d},
    "ppsy_248_clustering_entropy_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_248_clustering_entropy_vel_63d},
    "ppsy_249_clustering_entropy_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_249_clustering_entropy_vel_126d},
    "ppsy_250_clustering_entropy_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_250_clustering_entropy_vel_252d},
    "ppsy_251_price_support_psych_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_251_price_support_psych_vel_5d},
    "ppsy_252_price_support_psych_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_252_price_support_psych_vel_21d},
    "ppsy_253_price_support_psych_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_253_price_support_psych_vel_63d},
    "ppsy_254_price_support_psych_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_254_price_support_psych_vel_126d},
    "ppsy_255_price_support_psych_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_255_price_support_psych_vel_252d},
    "ppsy_256_price_resistance_psych_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_256_price_resistance_psych_vel_5d},
    "ppsy_257_price_resistance_psych_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_257_price_resistance_psych_vel_21d},
    "ppsy_258_price_resistance_psych_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_258_price_resistance_psych_vel_63d},
    "ppsy_259_price_resistance_psych_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_259_price_resistance_psych_vel_126d},
    "ppsy_260_price_resistance_psych_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_260_price_resistance_psych_vel_252d},
    "ppsy_261_clustering_zscore_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_261_clustering_zscore_vel_5d},
    "ppsy_262_clustering_zscore_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_262_clustering_zscore_vel_21d},
    "ppsy_263_clustering_zscore_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_263_clustering_zscore_vel_63d},
    "ppsy_264_clustering_zscore_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_264_clustering_zscore_vel_126d},
    "ppsy_265_clustering_zscore_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_265_clustering_zscore_vel_252d},
    "ppsy_266_digit_bias_last_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_266_digit_bias_last_vel_5d},
    "ppsy_267_digit_bias_last_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_267_digit_bias_last_vel_21d},
    "ppsy_268_digit_bias_last_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_268_digit_bias_last_vel_63d},
    "ppsy_269_digit_bias_last_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_269_digit_bias_last_vel_126d},
    "ppsy_270_digit_bias_last_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_270_digit_bias_last_vel_252d},
    "ppsy_271_price_magnet_effect_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_271_price_magnet_effect_vel_5d},
    "ppsy_272_price_magnet_effect_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_272_price_magnet_effect_vel_21d},
    "ppsy_273_price_magnet_effect_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_273_price_magnet_effect_vel_63d},
    "ppsy_274_price_magnet_effect_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_274_price_magnet_effect_vel_126d},
    "ppsy_275_price_magnet_effect_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_275_price_magnet_effect_vel_252d},
    "ppsy_276_clustering_regime_shift_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_276_clustering_regime_shift_vel_5d},
    "ppsy_277_clustering_regime_shift_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_277_clustering_regime_shift_vel_21d},
    "ppsy_278_clustering_regime_shift_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_278_clustering_regime_shift_vel_63d},
    "ppsy_279_clustering_regime_shift_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_279_clustering_regime_shift_vel_126d},
    "ppsy_280_clustering_regime_shift_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_280_clustering_regime_shift_vel_252d},
    "ppsy_281_psychological_breakthrough_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_281_psychological_breakthrough_vel_5d},
    "ppsy_282_psychological_breakthrough_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_282_psychological_breakthrough_vel_21d},
    "ppsy_283_psychological_breakthrough_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_283_psychological_breakthrough_vel_63d},
    "ppsy_284_psychological_breakthrough_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_284_psychological_breakthrough_vel_126d},
    "ppsy_285_psychological_breakthrough_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_285_psychological_breakthrough_vel_252d},
    "ppsy_286_price_stickiness_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_286_price_stickiness_vel_5d},
    "ppsy_287_price_stickiness_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_287_price_stickiness_vel_21d},
    "ppsy_288_price_stickiness_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_288_price_stickiness_vel_63d},
    "ppsy_289_price_stickiness_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_289_price_stickiness_vel_126d},
    "ppsy_290_price_stickiness_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_290_price_stickiness_vel_252d},
    "ppsy_291_clustering_vol_corr_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_291_clustering_vol_corr_vel_5d},
    "ppsy_292_clustering_vol_corr_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_292_clustering_vol_corr_vel_21d},
    "ppsy_293_clustering_vol_corr_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_293_clustering_vol_corr_vel_63d},
    "ppsy_294_clustering_vol_corr_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_294_clustering_vol_corr_vel_126d},
    "ppsy_295_clustering_vol_corr_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_295_clustering_vol_corr_vel_252d},
    "ppsy_296_psych_exhaustion_proxy_vel_5d": {"inputs": ["close", "volume"], "func": ppsy_296_psych_exhaustion_proxy_vel_5d},
    "ppsy_297_psych_exhaustion_proxy_vel_21d": {"inputs": ["close", "volume"], "func": ppsy_297_psych_exhaustion_proxy_vel_21d},
    "ppsy_298_psych_exhaustion_proxy_vel_63d": {"inputs": ["close", "volume"], "func": ppsy_298_psych_exhaustion_proxy_vel_63d},
    "ppsy_299_psych_exhaustion_proxy_vel_126d": {"inputs": ["close", "volume"], "func": ppsy_299_psych_exhaustion_proxy_vel_126d},
    "ppsy_300_psych_exhaustion_proxy_vel_252d": {"inputs": ["close", "volume"], "func": ppsy_300_psych_exhaustion_proxy_vel_252d},
}
