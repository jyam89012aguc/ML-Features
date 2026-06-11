"""
111_jump_discontinuity — Velocity (2nd Derivatives)
Domain: jump_discontinuity
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

def jump_226_price_jump_magnitude_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_226_price_jump_magnitude_vel_5d
    ECONOMIC RATIONALE: Velocity of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(5)

def jump_227_price_jump_magnitude_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_227_price_jump_magnitude_vel_21d
    ECONOMIC RATIONALE: Velocity of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(21)

def jump_228_price_jump_magnitude_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_228_price_jump_magnitude_vel_63d
    ECONOMIC RATIONALE: Velocity of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(63)

def jump_229_price_jump_magnitude_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_229_price_jump_magnitude_vel_126d
    ECONOMIC RATIONALE: Velocity of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(126)

def jump_230_price_jump_magnitude_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_230_price_jump_magnitude_vel_252d
    ECONOMIC RATIONALE: Velocity of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(252)

def jump_231_overnight_gap_jump_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_231_overnight_gap_jump_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(5)

def jump_232_overnight_gap_jump_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_232_overnight_gap_jump_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(21)

def jump_233_overnight_gap_jump_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_233_overnight_gap_jump_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(63)

def jump_234_overnight_gap_jump_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_234_overnight_gap_jump_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(126)

def jump_235_overnight_gap_jump_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_235_overnight_gap_jump_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(252)

def jump_236_jump_volume_intensity_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_236_jump_volume_intensity_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(5)

def jump_237_jump_volume_intensity_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_237_jump_volume_intensity_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(21)

def jump_238_jump_volume_intensity_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_238_jump_volume_intensity_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(63)

def jump_239_jump_volume_intensity_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_239_jump_volume_intensity_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(126)

def jump_240_jump_volume_intensity_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_240_jump_volume_intensity_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(252)

def jump_241_jump_frequency_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_241_jump_frequency_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(5)

def jump_242_jump_frequency_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_242_jump_frequency_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(21)

def jump_243_jump_frequency_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_243_jump_frequency_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(63)

def jump_244_jump_frequency_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_244_jump_frequency_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(126)

def jump_245_jump_frequency_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_245_jump_frequency_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(252)

def jump_246_jump_direction_bias_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_246_jump_direction_bias_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(5)

def jump_247_jump_direction_bias_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_247_jump_direction_bias_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(21)

def jump_248_jump_direction_bias_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_248_jump_direction_bias_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(63)

def jump_249_jump_direction_bias_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_249_jump_direction_bias_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(126)

def jump_250_jump_direction_bias_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_250_jump_direction_bias_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(252)

def jump_251_jump_zscore_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_251_jump_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(5)

def jump_252_jump_zscore_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_252_jump_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(21)

def jump_253_jump_zscore_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_253_jump_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(63)

def jump_254_jump_zscore_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_254_jump_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(126)

def jump_255_jump_zscore_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_255_jump_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(252)

def jump_256_jump_reversal_rate_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_256_jump_reversal_rate_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(5)

def jump_257_jump_reversal_rate_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_257_jump_reversal_rate_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(21)

def jump_258_jump_reversal_rate_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_258_jump_reversal_rate_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(63)

def jump_259_jump_reversal_rate_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_259_jump_reversal_rate_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(126)

def jump_260_jump_reversal_rate_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_260_jump_reversal_rate_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(252)

def jump_261_vol_adjusted_jump_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_261_vol_adjusted_jump_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(5)

def jump_262_vol_adjusted_jump_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_262_vol_adjusted_jump_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(21)

def jump_263_vol_adjusted_jump_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_263_vol_adjusted_jump_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(63)

def jump_264_vol_adjusted_jump_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_264_vol_adjusted_jump_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(126)

def jump_265_vol_adjusted_jump_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_265_vol_adjusted_jump_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(252)

def jump_266_jump_decay_rate_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_266_jump_decay_rate_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(5)

def jump_267_jump_decay_rate_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_267_jump_decay_rate_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(21)

def jump_268_jump_decay_rate_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_268_jump_decay_rate_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(63)

def jump_269_jump_decay_rate_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_269_jump_decay_rate_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(126)

def jump_270_jump_decay_rate_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_270_jump_decay_rate_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(252)

def jump_271_jump_clustering_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_271_jump_clustering_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(5)

def jump_272_jump_clustering_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_272_jump_clustering_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(21)

def jump_273_jump_clustering_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_273_jump_clustering_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(63)

def jump_274_jump_clustering_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_274_jump_clustering_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(126)

def jump_275_jump_clustering_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_275_jump_clustering_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(252)

def jump_276_intraday_jump_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_276_intraday_jump_vel_5d
    ECONOMIC RATIONALE: Velocity of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(5)

def jump_277_intraday_jump_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_277_intraday_jump_vel_21d
    ECONOMIC RATIONALE: Velocity of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(21)

def jump_278_intraday_jump_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_278_intraday_jump_vel_63d
    ECONOMIC RATIONALE: Velocity of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(63)

def jump_279_intraday_jump_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_279_intraday_jump_vel_126d
    ECONOMIC RATIONALE: Velocity of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(126)

def jump_280_intraday_jump_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_280_intraday_jump_vel_252d
    ECONOMIC RATIONALE: Velocity of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(252)

def jump_281_jump_regime_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_281_jump_regime_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(5)

def jump_282_jump_regime_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_282_jump_regime_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(21)

def jump_283_jump_regime_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_283_jump_regime_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(63)

def jump_284_jump_regime_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_284_jump_regime_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(126)

def jump_285_jump_regime_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_285_jump_regime_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(252)

def jump_286_jump_impact_on_drawdown_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_286_jump_impact_on_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(5)

def jump_287_jump_impact_on_drawdown_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_287_jump_impact_on_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(21)

def jump_288_jump_impact_on_drawdown_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_288_jump_impact_on_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(63)

def jump_289_jump_impact_on_drawdown_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_289_jump_impact_on_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(126)

def jump_290_jump_impact_on_drawdown_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_290_jump_impact_on_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(252)

def jump_291_jump_entropy_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_291_jump_entropy_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(5)

def jump_292_jump_entropy_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_292_jump_entropy_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(21)

def jump_293_jump_entropy_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_293_jump_entropy_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(63)

def jump_294_jump_entropy_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_294_jump_entropy_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(126)

def jump_295_jump_entropy_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_295_jump_entropy_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(252)

def jump_296_jump_tail_risk_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_296_jump_tail_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(5)

def jump_297_jump_tail_risk_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_297_jump_tail_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(21)

def jump_298_jump_tail_risk_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_298_jump_tail_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(63)

def jump_299_jump_tail_risk_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_299_jump_tail_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(126)

def jump_300_jump_tail_risk_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_300_jump_tail_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V111_REGISTRY_VEL = {
    "jump_226_price_jump_magnitude_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_226_price_jump_magnitude_vel_5d},
    "jump_227_price_jump_magnitude_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_227_price_jump_magnitude_vel_21d},
    "jump_228_price_jump_magnitude_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_228_price_jump_magnitude_vel_63d},
    "jump_229_price_jump_magnitude_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_229_price_jump_magnitude_vel_126d},
    "jump_230_price_jump_magnitude_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_230_price_jump_magnitude_vel_252d},
    "jump_231_overnight_gap_jump_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_231_overnight_gap_jump_vel_5d},
    "jump_232_overnight_gap_jump_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_232_overnight_gap_jump_vel_21d},
    "jump_233_overnight_gap_jump_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_233_overnight_gap_jump_vel_63d},
    "jump_234_overnight_gap_jump_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_234_overnight_gap_jump_vel_126d},
    "jump_235_overnight_gap_jump_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_235_overnight_gap_jump_vel_252d},
    "jump_236_jump_volume_intensity_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_236_jump_volume_intensity_vel_5d},
    "jump_237_jump_volume_intensity_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_237_jump_volume_intensity_vel_21d},
    "jump_238_jump_volume_intensity_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_238_jump_volume_intensity_vel_63d},
    "jump_239_jump_volume_intensity_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_239_jump_volume_intensity_vel_126d},
    "jump_240_jump_volume_intensity_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_240_jump_volume_intensity_vel_252d},
    "jump_241_jump_frequency_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_241_jump_frequency_vel_5d},
    "jump_242_jump_frequency_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_242_jump_frequency_vel_21d},
    "jump_243_jump_frequency_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_243_jump_frequency_vel_63d},
    "jump_244_jump_frequency_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_244_jump_frequency_vel_126d},
    "jump_245_jump_frequency_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_245_jump_frequency_vel_252d},
    "jump_246_jump_direction_bias_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_246_jump_direction_bias_vel_5d},
    "jump_247_jump_direction_bias_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_247_jump_direction_bias_vel_21d},
    "jump_248_jump_direction_bias_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_248_jump_direction_bias_vel_63d},
    "jump_249_jump_direction_bias_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_249_jump_direction_bias_vel_126d},
    "jump_250_jump_direction_bias_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_250_jump_direction_bias_vel_252d},
    "jump_251_jump_zscore_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_251_jump_zscore_vel_5d},
    "jump_252_jump_zscore_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_252_jump_zscore_vel_21d},
    "jump_253_jump_zscore_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_253_jump_zscore_vel_63d},
    "jump_254_jump_zscore_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_254_jump_zscore_vel_126d},
    "jump_255_jump_zscore_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_255_jump_zscore_vel_252d},
    "jump_256_jump_reversal_rate_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_256_jump_reversal_rate_vel_5d},
    "jump_257_jump_reversal_rate_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_257_jump_reversal_rate_vel_21d},
    "jump_258_jump_reversal_rate_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_258_jump_reversal_rate_vel_63d},
    "jump_259_jump_reversal_rate_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_259_jump_reversal_rate_vel_126d},
    "jump_260_jump_reversal_rate_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_260_jump_reversal_rate_vel_252d},
    "jump_261_vol_adjusted_jump_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_261_vol_adjusted_jump_vel_5d},
    "jump_262_vol_adjusted_jump_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_262_vol_adjusted_jump_vel_21d},
    "jump_263_vol_adjusted_jump_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_263_vol_adjusted_jump_vel_63d},
    "jump_264_vol_adjusted_jump_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_264_vol_adjusted_jump_vel_126d},
    "jump_265_vol_adjusted_jump_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_265_vol_adjusted_jump_vel_252d},
    "jump_266_jump_decay_rate_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_266_jump_decay_rate_vel_5d},
    "jump_267_jump_decay_rate_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_267_jump_decay_rate_vel_21d},
    "jump_268_jump_decay_rate_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_268_jump_decay_rate_vel_63d},
    "jump_269_jump_decay_rate_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_269_jump_decay_rate_vel_126d},
    "jump_270_jump_decay_rate_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_270_jump_decay_rate_vel_252d},
    "jump_271_jump_clustering_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_271_jump_clustering_vel_5d},
    "jump_272_jump_clustering_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_272_jump_clustering_vel_21d},
    "jump_273_jump_clustering_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_273_jump_clustering_vel_63d},
    "jump_274_jump_clustering_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_274_jump_clustering_vel_126d},
    "jump_275_jump_clustering_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_275_jump_clustering_vel_252d},
    "jump_276_intraday_jump_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_276_intraday_jump_vel_5d},
    "jump_277_intraday_jump_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_277_intraday_jump_vel_21d},
    "jump_278_intraday_jump_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_278_intraday_jump_vel_63d},
    "jump_279_intraday_jump_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_279_intraday_jump_vel_126d},
    "jump_280_intraday_jump_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_280_intraday_jump_vel_252d},
    "jump_281_jump_regime_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_281_jump_regime_vel_5d},
    "jump_282_jump_regime_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_282_jump_regime_vel_21d},
    "jump_283_jump_regime_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_283_jump_regime_vel_63d},
    "jump_284_jump_regime_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_284_jump_regime_vel_126d},
    "jump_285_jump_regime_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_285_jump_regime_vel_252d},
    "jump_286_jump_impact_on_drawdown_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_286_jump_impact_on_drawdown_vel_5d},
    "jump_287_jump_impact_on_drawdown_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_287_jump_impact_on_drawdown_vel_21d},
    "jump_288_jump_impact_on_drawdown_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_288_jump_impact_on_drawdown_vel_63d},
    "jump_289_jump_impact_on_drawdown_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_289_jump_impact_on_drawdown_vel_126d},
    "jump_290_jump_impact_on_drawdown_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_290_jump_impact_on_drawdown_vel_252d},
    "jump_291_jump_entropy_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_291_jump_entropy_vel_5d},
    "jump_292_jump_entropy_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_292_jump_entropy_vel_21d},
    "jump_293_jump_entropy_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_293_jump_entropy_vel_63d},
    "jump_294_jump_entropy_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_294_jump_entropy_vel_126d},
    "jump_295_jump_entropy_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_295_jump_entropy_vel_252d},
    "jump_296_jump_tail_risk_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_296_jump_tail_risk_vel_5d},
    "jump_297_jump_tail_risk_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_297_jump_tail_risk_vel_21d},
    "jump_298_jump_tail_risk_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_298_jump_tail_risk_vel_63d},
    "jump_299_jump_tail_risk_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_299_jump_tail_risk_vel_126d},
    "jump_300_jump_tail_risk_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_300_jump_tail_risk_vel_252d},
}
