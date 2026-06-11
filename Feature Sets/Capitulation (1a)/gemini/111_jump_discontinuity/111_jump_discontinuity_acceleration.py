"""
111_jump_discontinuity — Acceleration (3rd Derivatives)
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

def jump_301_price_jump_magnitude_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_301_price_jump_magnitude_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(5).diff(_TD_MON)

def jump_302_price_jump_magnitude_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_302_price_jump_magnitude_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(21).diff(_TD_MON)

def jump_303_price_jump_magnitude_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_303_price_jump_magnitude_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(63).diff(_TD_MON)

def jump_304_price_jump_magnitude_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_304_price_jump_magnitude_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(126).diff(_TD_MON)

def jump_305_price_jump_magnitude_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_305_price_jump_magnitude_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_jump_magnitude. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).diff(252).diff(_TD_MON)

def jump_306_overnight_gap_jump_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_306_overnight_gap_jump_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(5).diff(_TD_MON)

def jump_307_overnight_gap_jump_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_307_overnight_gap_jump_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(21).diff(_TD_MON)

def jump_308_overnight_gap_jump_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_308_overnight_gap_jump_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(63).diff(_TD_MON)

def jump_309_overnight_gap_jump_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_309_overnight_gap_jump_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(126).diff(_TD_MON)

def jump_310_overnight_gap_jump_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_310_overnight_gap_jump_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_jump. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).diff(252).diff(_TD_MON)

def jump_311_jump_volume_intensity_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_311_jump_volume_intensity_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(5).diff(_TD_MON)

def jump_312_jump_volume_intensity_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_312_jump_volume_intensity_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(21).diff(_TD_MON)

def jump_313_jump_volume_intensity_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_313_jump_volume_intensity_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(63).diff(_TD_MON)

def jump_314_jump_volume_intensity_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_314_jump_volume_intensity_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(126).diff(_TD_MON)

def jump_315_jump_volume_intensity_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_315_jump_volume_intensity_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_volume_intensity. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).diff(252).diff(_TD_MON)

def jump_316_jump_frequency_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_316_jump_frequency_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(5).diff(_TD_MON)

def jump_317_jump_frequency_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_317_jump_frequency_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(21).diff(_TD_MON)

def jump_318_jump_frequency_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_318_jump_frequency_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(63).diff(_TD_MON)

def jump_319_jump_frequency_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_319_jump_frequency_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(126).diff(_TD_MON)

def jump_320_jump_frequency_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_320_jump_frequency_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_frequency. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).diff(252).diff(_TD_MON)

def jump_321_jump_direction_bias_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_321_jump_direction_bias_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def jump_322_jump_direction_bias_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_322_jump_direction_bias_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def jump_323_jump_direction_bias_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_323_jump_direction_bias_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def jump_324_jump_direction_bias_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_324_jump_direction_bias_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def jump_325_jump_direction_bias_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_325_jump_direction_bias_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_direction_bias. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def jump_326_jump_zscore_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_326_jump_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(5).diff(_TD_MON)

def jump_327_jump_zscore_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_327_jump_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(21).diff(_TD_MON)

def jump_328_jump_zscore_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_328_jump_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(63).diff(_TD_MON)

def jump_329_jump_zscore_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_329_jump_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(126).diff(_TD_MON)

def jump_330_jump_zscore_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_330_jump_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_zscore. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).diff(252).diff(_TD_MON)

def jump_331_jump_reversal_rate_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_331_jump_reversal_rate_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(5).diff(_TD_MON)

def jump_332_jump_reversal_rate_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_332_jump_reversal_rate_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(21).diff(_TD_MON)

def jump_333_jump_reversal_rate_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_333_jump_reversal_rate_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(63).diff(_TD_MON)

def jump_334_jump_reversal_rate_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_334_jump_reversal_rate_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(126).diff(_TD_MON)

def jump_335_jump_reversal_rate_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_335_jump_reversal_rate_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_reversal_rate. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).diff(252).diff(_TD_MON)

def jump_336_vol_adjusted_jump_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_336_vol_adjusted_jump_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def jump_337_vol_adjusted_jump_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_337_vol_adjusted_jump_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def jump_338_vol_adjusted_jump_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_338_vol_adjusted_jump_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def jump_339_vol_adjusted_jump_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_339_vol_adjusted_jump_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def jump_340_vol_adjusted_jump_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_340_vol_adjusted_jump_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_adjusted_jump. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def jump_341_jump_decay_rate_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_341_jump_decay_rate_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(5).diff(_TD_MON)

def jump_342_jump_decay_rate_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_342_jump_decay_rate_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(21).diff(_TD_MON)

def jump_343_jump_decay_rate_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_343_jump_decay_rate_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(63).diff(_TD_MON)

def jump_344_jump_decay_rate_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_344_jump_decay_rate_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(126).diff(_TD_MON)

def jump_345_jump_decay_rate_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_345_jump_decay_rate_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_decay_rate. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).diff(252).diff(_TD_MON)

def jump_346_jump_clustering_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_346_jump_clustering_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(5).diff(_TD_MON)

def jump_347_jump_clustering_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_347_jump_clustering_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(21).diff(_TD_MON)

def jump_348_jump_clustering_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_348_jump_clustering_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(63).diff(_TD_MON)

def jump_349_jump_clustering_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_349_jump_clustering_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(126).diff(_TD_MON)

def jump_350_jump_clustering_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_350_jump_clustering_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_clustering. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).diff(252).diff(_TD_MON)

def jump_351_intraday_jump_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_351_intraday_jump_accel_5d
    ECONOMIC RATIONALE: Acceleration of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(5).diff(_TD_MON)

def jump_352_intraday_jump_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_352_intraday_jump_accel_21d
    ECONOMIC RATIONALE: Acceleration of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(21).diff(_TD_MON)

def jump_353_intraday_jump_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_353_intraday_jump_accel_63d
    ECONOMIC RATIONALE: Acceleration of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(63).diff(_TD_MON)

def jump_354_intraday_jump_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_354_intraday_jump_accel_126d
    ECONOMIC RATIONALE: Acceleration of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(126).diff(_TD_MON)

def jump_355_intraday_jump_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_355_intraday_jump_accel_252d
    ECONOMIC RATIONALE: Acceleration of intraday_jump. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).diff(252).diff(_TD_MON)

def jump_356_jump_regime_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_356_jump_regime_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(5).diff(_TD_MON)

def jump_357_jump_regime_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_357_jump_regime_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(21).diff(_TD_MON)

def jump_358_jump_regime_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_358_jump_regime_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(63).diff(_TD_MON)

def jump_359_jump_regime_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_359_jump_regime_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(126).diff(_TD_MON)

def jump_360_jump_regime_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_360_jump_regime_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_regime. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).diff(252).diff(_TD_MON)

def jump_361_jump_impact_on_drawdown_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_361_jump_impact_on_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(5).diff(_TD_MON)

def jump_362_jump_impact_on_drawdown_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_362_jump_impact_on_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(21).diff(_TD_MON)

def jump_363_jump_impact_on_drawdown_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_363_jump_impact_on_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(63).diff(_TD_MON)

def jump_364_jump_impact_on_drawdown_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_364_jump_impact_on_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(126).diff(_TD_MON)

def jump_365_jump_impact_on_drawdown_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_365_jump_impact_on_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_impact_on_drawdown. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).diff(252).diff(_TD_MON)

def jump_366_jump_entropy_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_366_jump_entropy_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(5).diff(_TD_MON)

def jump_367_jump_entropy_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_367_jump_entropy_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(21).diff(_TD_MON)

def jump_368_jump_entropy_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_368_jump_entropy_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(63).diff(_TD_MON)

def jump_369_jump_entropy_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_369_jump_entropy_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(126).diff(_TD_MON)

def jump_370_jump_entropy_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_370_jump_entropy_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_entropy. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).diff(252).diff(_TD_MON)

def jump_371_jump_tail_risk_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_371_jump_tail_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(5).diff(_TD_MON)

def jump_372_jump_tail_risk_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_372_jump_tail_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(21).diff(_TD_MON)

def jump_373_jump_tail_risk_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_373_jump_tail_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(63).diff(_TD_MON)

def jump_374_jump_tail_risk_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_374_jump_tail_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(126).diff(_TD_MON)

def jump_375_jump_tail_risk_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_375_jump_tail_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_tail_risk. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V111_REGISTRY_ACCEL = {
    "jump_301_price_jump_magnitude_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_301_price_jump_magnitude_accel_5d},
    "jump_302_price_jump_magnitude_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_302_price_jump_magnitude_accel_21d},
    "jump_303_price_jump_magnitude_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_303_price_jump_magnitude_accel_63d},
    "jump_304_price_jump_magnitude_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_304_price_jump_magnitude_accel_126d},
    "jump_305_price_jump_magnitude_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_305_price_jump_magnitude_accel_252d},
    "jump_306_overnight_gap_jump_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_306_overnight_gap_jump_accel_5d},
    "jump_307_overnight_gap_jump_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_307_overnight_gap_jump_accel_21d},
    "jump_308_overnight_gap_jump_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_308_overnight_gap_jump_accel_63d},
    "jump_309_overnight_gap_jump_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_309_overnight_gap_jump_accel_126d},
    "jump_310_overnight_gap_jump_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_310_overnight_gap_jump_accel_252d},
    "jump_311_jump_volume_intensity_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_311_jump_volume_intensity_accel_5d},
    "jump_312_jump_volume_intensity_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_312_jump_volume_intensity_accel_21d},
    "jump_313_jump_volume_intensity_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_313_jump_volume_intensity_accel_63d},
    "jump_314_jump_volume_intensity_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_314_jump_volume_intensity_accel_126d},
    "jump_315_jump_volume_intensity_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_315_jump_volume_intensity_accel_252d},
    "jump_316_jump_frequency_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_316_jump_frequency_accel_5d},
    "jump_317_jump_frequency_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_317_jump_frequency_accel_21d},
    "jump_318_jump_frequency_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_318_jump_frequency_accel_63d},
    "jump_319_jump_frequency_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_319_jump_frequency_accel_126d},
    "jump_320_jump_frequency_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_320_jump_frequency_accel_252d},
    "jump_321_jump_direction_bias_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_321_jump_direction_bias_accel_5d},
    "jump_322_jump_direction_bias_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_322_jump_direction_bias_accel_21d},
    "jump_323_jump_direction_bias_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_323_jump_direction_bias_accel_63d},
    "jump_324_jump_direction_bias_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_324_jump_direction_bias_accel_126d},
    "jump_325_jump_direction_bias_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_325_jump_direction_bias_accel_252d},
    "jump_326_jump_zscore_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_326_jump_zscore_accel_5d},
    "jump_327_jump_zscore_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_327_jump_zscore_accel_21d},
    "jump_328_jump_zscore_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_328_jump_zscore_accel_63d},
    "jump_329_jump_zscore_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_329_jump_zscore_accel_126d},
    "jump_330_jump_zscore_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_330_jump_zscore_accel_252d},
    "jump_331_jump_reversal_rate_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_331_jump_reversal_rate_accel_5d},
    "jump_332_jump_reversal_rate_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_332_jump_reversal_rate_accel_21d},
    "jump_333_jump_reversal_rate_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_333_jump_reversal_rate_accel_63d},
    "jump_334_jump_reversal_rate_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_334_jump_reversal_rate_accel_126d},
    "jump_335_jump_reversal_rate_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_335_jump_reversal_rate_accel_252d},
    "jump_336_vol_adjusted_jump_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_336_vol_adjusted_jump_accel_5d},
    "jump_337_vol_adjusted_jump_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_337_vol_adjusted_jump_accel_21d},
    "jump_338_vol_adjusted_jump_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_338_vol_adjusted_jump_accel_63d},
    "jump_339_vol_adjusted_jump_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_339_vol_adjusted_jump_accel_126d},
    "jump_340_vol_adjusted_jump_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_340_vol_adjusted_jump_accel_252d},
    "jump_341_jump_decay_rate_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_341_jump_decay_rate_accel_5d},
    "jump_342_jump_decay_rate_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_342_jump_decay_rate_accel_21d},
    "jump_343_jump_decay_rate_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_343_jump_decay_rate_accel_63d},
    "jump_344_jump_decay_rate_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_344_jump_decay_rate_accel_126d},
    "jump_345_jump_decay_rate_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_345_jump_decay_rate_accel_252d},
    "jump_346_jump_clustering_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_346_jump_clustering_accel_5d},
    "jump_347_jump_clustering_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_347_jump_clustering_accel_21d},
    "jump_348_jump_clustering_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_348_jump_clustering_accel_63d},
    "jump_349_jump_clustering_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_349_jump_clustering_accel_126d},
    "jump_350_jump_clustering_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_350_jump_clustering_accel_252d},
    "jump_351_intraday_jump_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_351_intraday_jump_accel_5d},
    "jump_352_intraday_jump_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_352_intraday_jump_accel_21d},
    "jump_353_intraday_jump_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_353_intraday_jump_accel_63d},
    "jump_354_intraday_jump_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_354_intraday_jump_accel_126d},
    "jump_355_intraday_jump_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_355_intraday_jump_accel_252d},
    "jump_356_jump_regime_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_356_jump_regime_accel_5d},
    "jump_357_jump_regime_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_357_jump_regime_accel_21d},
    "jump_358_jump_regime_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_358_jump_regime_accel_63d},
    "jump_359_jump_regime_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_359_jump_regime_accel_126d},
    "jump_360_jump_regime_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_360_jump_regime_accel_252d},
    "jump_361_jump_impact_on_drawdown_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_361_jump_impact_on_drawdown_accel_5d},
    "jump_362_jump_impact_on_drawdown_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_362_jump_impact_on_drawdown_accel_21d},
    "jump_363_jump_impact_on_drawdown_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_363_jump_impact_on_drawdown_accel_63d},
    "jump_364_jump_impact_on_drawdown_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_364_jump_impact_on_drawdown_accel_126d},
    "jump_365_jump_impact_on_drawdown_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_365_jump_impact_on_drawdown_accel_252d},
    "jump_366_jump_entropy_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_366_jump_entropy_accel_5d},
    "jump_367_jump_entropy_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_367_jump_entropy_accel_21d},
    "jump_368_jump_entropy_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_368_jump_entropy_accel_63d},
    "jump_369_jump_entropy_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_369_jump_entropy_accel_126d},
    "jump_370_jump_entropy_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_370_jump_entropy_accel_252d},
    "jump_371_jump_tail_risk_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_371_jump_tail_risk_accel_5d},
    "jump_372_jump_tail_risk_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_372_jump_tail_risk_accel_21d},
    "jump_373_jump_tail_risk_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_373_jump_tail_risk_accel_63d},
    "jump_374_jump_tail_risk_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_374_jump_tail_risk_accel_126d},
    "jump_375_jump_tail_risk_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_375_jump_tail_risk_accel_252d},
}
