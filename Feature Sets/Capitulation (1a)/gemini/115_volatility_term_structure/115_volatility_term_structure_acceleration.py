"""
115_volatility_term_structure — Acceleration (3rd Derivatives)
Domain: volatility_term_structure
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

def vts_301_vol_5d_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_301_vol_5d_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(5).diff(_TD_MON)

def vts_302_vol_5d_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_302_vol_5d_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(21).diff(_TD_MON)

def vts_303_vol_5d_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_303_vol_5d_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(63).diff(_TD_MON)

def vts_304_vol_5d_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_304_vol_5d_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(126).diff(_TD_MON)

def vts_305_vol_5d_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_305_vol_5d_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(252).diff(_TD_MON)

def vts_306_vol_21d_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_306_vol_21d_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(5).diff(_TD_MON)

def vts_307_vol_21d_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_307_vol_21d_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(21).diff(_TD_MON)

def vts_308_vol_21d_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_308_vol_21d_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(63).diff(_TD_MON)

def vts_309_vol_21d_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_309_vol_21d_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(126).diff(_TD_MON)

def vts_310_vol_21d_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_310_vol_21d_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(252).diff(_TD_MON)

def vts_311_vol_63d_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_311_vol_63d_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(5).diff(_TD_MON)

def vts_312_vol_63d_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_312_vol_63d_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(21).diff(_TD_MON)

def vts_313_vol_63d_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_313_vol_63d_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(63).diff(_TD_MON)

def vts_314_vol_63d_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_314_vol_63d_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(126).diff(_TD_MON)

def vts_315_vol_63d_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_315_vol_63d_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(252).diff(_TD_MON)

def vts_316_vol_spread_short_long_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_316_vol_spread_short_long_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(5).diff(_TD_MON)

def vts_317_vol_spread_short_long_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_317_vol_spread_short_long_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(21).diff(_TD_MON)

def vts_318_vol_spread_short_long_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_318_vol_spread_short_long_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(63).diff(_TD_MON)

def vts_319_vol_spread_short_long_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_319_vol_spread_short_long_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(126).diff(_TD_MON)

def vts_320_vol_spread_short_long_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_320_vol_spread_short_long_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(252).diff(_TD_MON)

def vts_321_vol_term_slope_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_321_vol_term_slope_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(5).diff(_TD_MON)

def vts_322_vol_term_slope_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_322_vol_term_slope_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(21).diff(_TD_MON)

def vts_323_vol_term_slope_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_323_vol_term_slope_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(63).diff(_TD_MON)

def vts_324_vol_term_slope_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_324_vol_term_slope_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(126).diff(_TD_MON)

def vts_325_vol_term_slope_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_325_vol_term_slope_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(252).diff(_TD_MON)

def vts_326_vol_convexity_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_326_vol_convexity_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(5).diff(_TD_MON)

def vts_327_vol_convexity_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_327_vol_convexity_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(21).diff(_TD_MON)

def vts_328_vol_convexity_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_328_vol_convexity_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(63).diff(_TD_MON)

def vts_329_vol_convexity_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_329_vol_convexity_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(126).diff(_TD_MON)

def vts_330_vol_convexity_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_330_vol_convexity_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(252).diff(_TD_MON)

def vts_331_vol_mean_reversion_speed_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_331_vol_mean_reversion_speed_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(5).diff(_TD_MON)

def vts_332_vol_mean_reversion_speed_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_332_vol_mean_reversion_speed_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(21).diff(_TD_MON)

def vts_333_vol_mean_reversion_speed_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_333_vol_mean_reversion_speed_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(63).diff(_TD_MON)

def vts_334_vol_mean_reversion_speed_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_334_vol_mean_reversion_speed_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(126).diff(_TD_MON)

def vts_335_vol_mean_reversion_speed_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_335_vol_mean_reversion_speed_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(252).diff(_TD_MON)

def vts_336_vol_regime_z_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_336_vol_regime_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(5).diff(_TD_MON)

def vts_337_vol_regime_z_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_337_vol_regime_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(21).diff(_TD_MON)

def vts_338_vol_regime_z_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_338_vol_regime_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(63).diff(_TD_MON)

def vts_339_vol_regime_z_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_339_vol_regime_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(126).diff(_TD_MON)

def vts_340_vol_regime_z_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_340_vol_regime_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(252).diff(_TD_MON)

def vts_341_vol_acceleration_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_341_vol_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(5).diff(_TD_MON)

def vts_342_vol_acceleration_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_342_vol_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(21).diff(_TD_MON)

def vts_343_vol_acceleration_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_343_vol_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(63).diff(_TD_MON)

def vts_344_vol_acceleration_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_344_vol_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(126).diff(_TD_MON)

def vts_345_vol_acceleration_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_345_vol_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(252).diff(_TD_MON)

def vts_346_vol_of_vol_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_346_vol_of_vol_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(5).diff(_TD_MON)

def vts_347_vol_of_vol_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_347_vol_of_vol_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(21).diff(_TD_MON)

def vts_348_vol_of_vol_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_348_vol_of_vol_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(63).diff(_TD_MON)

def vts_349_vol_of_vol_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_349_vol_of_vol_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(126).diff(_TD_MON)

def vts_350_vol_of_vol_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_350_vol_of_vol_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(252).diff(_TD_MON)

def vts_351_vol_decay_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_351_vol_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(5).diff(_TD_MON)

def vts_352_vol_decay_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_352_vol_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(21).diff(_TD_MON)

def vts_353_vol_decay_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_353_vol_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(63).diff(_TD_MON)

def vts_354_vol_decay_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_354_vol_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(126).diff(_TD_MON)

def vts_355_vol_decay_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_355_vol_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(252).diff(_TD_MON)

def vts_356_vol_term_inversion_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_356_vol_term_inversion_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(5).diff(_TD_MON)

def vts_357_vol_term_inversion_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_357_vol_term_inversion_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(21).diff(_TD_MON)

def vts_358_vol_term_inversion_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_358_vol_term_inversion_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(63).diff(_TD_MON)

def vts_359_vol_term_inversion_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_359_vol_term_inversion_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(126).diff(_TD_MON)

def vts_360_vol_term_inversion_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_360_vol_term_inversion_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(252).diff(_TD_MON)

def vts_361_vol_peak_dist_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_361_vol_peak_dist_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(5).diff(_TD_MON)

def vts_362_vol_peak_dist_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_362_vol_peak_dist_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(21).diff(_TD_MON)

def vts_363_vol_peak_dist_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_363_vol_peak_dist_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(63).diff(_TD_MON)

def vts_364_vol_peak_dist_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_364_vol_peak_dist_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(126).diff(_TD_MON)

def vts_365_vol_peak_dist_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_365_vol_peak_dist_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(252).diff(_TD_MON)

def vts_366_vol_tail_spread_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_366_vol_tail_spread_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(5).diff(_TD_MON)

def vts_367_vol_tail_spread_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_367_vol_tail_spread_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(21).diff(_TD_MON)

def vts_368_vol_tail_spread_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_368_vol_tail_spread_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(63).diff(_TD_MON)

def vts_369_vol_tail_spread_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_369_vol_tail_spread_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(126).diff(_TD_MON)

def vts_370_vol_tail_spread_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_370_vol_tail_spread_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(252).diff(_TD_MON)

def vts_371_vol_structural_stability_accel_5d(close: pd.Series) -> pd.Series:
    """
    vts_371_vol_structural_stability_accel_5d
    ECONOMIC RATIONALE: Acceleration of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(5).diff(_TD_MON)

def vts_372_vol_structural_stability_accel_21d(close: pd.Series) -> pd.Series:
    """
    vts_372_vol_structural_stability_accel_21d
    ECONOMIC RATIONALE: Acceleration of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(21).diff(_TD_MON)

def vts_373_vol_structural_stability_accel_63d(close: pd.Series) -> pd.Series:
    """
    vts_373_vol_structural_stability_accel_63d
    ECONOMIC RATIONALE: Acceleration of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(63).diff(_TD_MON)

def vts_374_vol_structural_stability_accel_126d(close: pd.Series) -> pd.Series:
    """
    vts_374_vol_structural_stability_accel_126d
    ECONOMIC RATIONALE: Acceleration of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(126).diff(_TD_MON)

def vts_375_vol_structural_stability_accel_252d(close: pd.Series) -> pd.Series:
    """
    vts_375_vol_structural_stability_accel_252d
    ECONOMIC RATIONALE: Acceleration of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V115_REGISTRY_ACCEL = {
    "vts_301_vol_5d_accel_5d": {"inputs": ["close"], "func": vts_301_vol_5d_accel_5d},
    "vts_302_vol_5d_accel_21d": {"inputs": ["close"], "func": vts_302_vol_5d_accel_21d},
    "vts_303_vol_5d_accel_63d": {"inputs": ["close"], "func": vts_303_vol_5d_accel_63d},
    "vts_304_vol_5d_accel_126d": {"inputs": ["close"], "func": vts_304_vol_5d_accel_126d},
    "vts_305_vol_5d_accel_252d": {"inputs": ["close"], "func": vts_305_vol_5d_accel_252d},
    "vts_306_vol_21d_accel_5d": {"inputs": ["close"], "func": vts_306_vol_21d_accel_5d},
    "vts_307_vol_21d_accel_21d": {"inputs": ["close"], "func": vts_307_vol_21d_accel_21d},
    "vts_308_vol_21d_accel_63d": {"inputs": ["close"], "func": vts_308_vol_21d_accel_63d},
    "vts_309_vol_21d_accel_126d": {"inputs": ["close"], "func": vts_309_vol_21d_accel_126d},
    "vts_310_vol_21d_accel_252d": {"inputs": ["close"], "func": vts_310_vol_21d_accel_252d},
    "vts_311_vol_63d_accel_5d": {"inputs": ["close"], "func": vts_311_vol_63d_accel_5d},
    "vts_312_vol_63d_accel_21d": {"inputs": ["close"], "func": vts_312_vol_63d_accel_21d},
    "vts_313_vol_63d_accel_63d": {"inputs": ["close"], "func": vts_313_vol_63d_accel_63d},
    "vts_314_vol_63d_accel_126d": {"inputs": ["close"], "func": vts_314_vol_63d_accel_126d},
    "vts_315_vol_63d_accel_252d": {"inputs": ["close"], "func": vts_315_vol_63d_accel_252d},
    "vts_316_vol_spread_short_long_accel_5d": {"inputs": ["close"], "func": vts_316_vol_spread_short_long_accel_5d},
    "vts_317_vol_spread_short_long_accel_21d": {"inputs": ["close"], "func": vts_317_vol_spread_short_long_accel_21d},
    "vts_318_vol_spread_short_long_accel_63d": {"inputs": ["close"], "func": vts_318_vol_spread_short_long_accel_63d},
    "vts_319_vol_spread_short_long_accel_126d": {"inputs": ["close"], "func": vts_319_vol_spread_short_long_accel_126d},
    "vts_320_vol_spread_short_long_accel_252d": {"inputs": ["close"], "func": vts_320_vol_spread_short_long_accel_252d},
    "vts_321_vol_term_slope_accel_5d": {"inputs": ["close"], "func": vts_321_vol_term_slope_accel_5d},
    "vts_322_vol_term_slope_accel_21d": {"inputs": ["close"], "func": vts_322_vol_term_slope_accel_21d},
    "vts_323_vol_term_slope_accel_63d": {"inputs": ["close"], "func": vts_323_vol_term_slope_accel_63d},
    "vts_324_vol_term_slope_accel_126d": {"inputs": ["close"], "func": vts_324_vol_term_slope_accel_126d},
    "vts_325_vol_term_slope_accel_252d": {"inputs": ["close"], "func": vts_325_vol_term_slope_accel_252d},
    "vts_326_vol_convexity_accel_5d": {"inputs": ["close"], "func": vts_326_vol_convexity_accel_5d},
    "vts_327_vol_convexity_accel_21d": {"inputs": ["close"], "func": vts_327_vol_convexity_accel_21d},
    "vts_328_vol_convexity_accel_63d": {"inputs": ["close"], "func": vts_328_vol_convexity_accel_63d},
    "vts_329_vol_convexity_accel_126d": {"inputs": ["close"], "func": vts_329_vol_convexity_accel_126d},
    "vts_330_vol_convexity_accel_252d": {"inputs": ["close"], "func": vts_330_vol_convexity_accel_252d},
    "vts_331_vol_mean_reversion_speed_accel_5d": {"inputs": ["close"], "func": vts_331_vol_mean_reversion_speed_accel_5d},
    "vts_332_vol_mean_reversion_speed_accel_21d": {"inputs": ["close"], "func": vts_332_vol_mean_reversion_speed_accel_21d},
    "vts_333_vol_mean_reversion_speed_accel_63d": {"inputs": ["close"], "func": vts_333_vol_mean_reversion_speed_accel_63d},
    "vts_334_vol_mean_reversion_speed_accel_126d": {"inputs": ["close"], "func": vts_334_vol_mean_reversion_speed_accel_126d},
    "vts_335_vol_mean_reversion_speed_accel_252d": {"inputs": ["close"], "func": vts_335_vol_mean_reversion_speed_accel_252d},
    "vts_336_vol_regime_z_accel_5d": {"inputs": ["close"], "func": vts_336_vol_regime_z_accel_5d},
    "vts_337_vol_regime_z_accel_21d": {"inputs": ["close"], "func": vts_337_vol_regime_z_accel_21d},
    "vts_338_vol_regime_z_accel_63d": {"inputs": ["close"], "func": vts_338_vol_regime_z_accel_63d},
    "vts_339_vol_regime_z_accel_126d": {"inputs": ["close"], "func": vts_339_vol_regime_z_accel_126d},
    "vts_340_vol_regime_z_accel_252d": {"inputs": ["close"], "func": vts_340_vol_regime_z_accel_252d},
    "vts_341_vol_acceleration_accel_5d": {"inputs": ["close"], "func": vts_341_vol_acceleration_accel_5d},
    "vts_342_vol_acceleration_accel_21d": {"inputs": ["close"], "func": vts_342_vol_acceleration_accel_21d},
    "vts_343_vol_acceleration_accel_63d": {"inputs": ["close"], "func": vts_343_vol_acceleration_accel_63d},
    "vts_344_vol_acceleration_accel_126d": {"inputs": ["close"], "func": vts_344_vol_acceleration_accel_126d},
    "vts_345_vol_acceleration_accel_252d": {"inputs": ["close"], "func": vts_345_vol_acceleration_accel_252d},
    "vts_346_vol_of_vol_accel_5d": {"inputs": ["close"], "func": vts_346_vol_of_vol_accel_5d},
    "vts_347_vol_of_vol_accel_21d": {"inputs": ["close"], "func": vts_347_vol_of_vol_accel_21d},
    "vts_348_vol_of_vol_accel_63d": {"inputs": ["close"], "func": vts_348_vol_of_vol_accel_63d},
    "vts_349_vol_of_vol_accel_126d": {"inputs": ["close"], "func": vts_349_vol_of_vol_accel_126d},
    "vts_350_vol_of_vol_accel_252d": {"inputs": ["close"], "func": vts_350_vol_of_vol_accel_252d},
    "vts_351_vol_decay_accel_5d": {"inputs": ["close"], "func": vts_351_vol_decay_accel_5d},
    "vts_352_vol_decay_accel_21d": {"inputs": ["close"], "func": vts_352_vol_decay_accel_21d},
    "vts_353_vol_decay_accel_63d": {"inputs": ["close"], "func": vts_353_vol_decay_accel_63d},
    "vts_354_vol_decay_accel_126d": {"inputs": ["close"], "func": vts_354_vol_decay_accel_126d},
    "vts_355_vol_decay_accel_252d": {"inputs": ["close"], "func": vts_355_vol_decay_accel_252d},
    "vts_356_vol_term_inversion_accel_5d": {"inputs": ["close"], "func": vts_356_vol_term_inversion_accel_5d},
    "vts_357_vol_term_inversion_accel_21d": {"inputs": ["close"], "func": vts_357_vol_term_inversion_accel_21d},
    "vts_358_vol_term_inversion_accel_63d": {"inputs": ["close"], "func": vts_358_vol_term_inversion_accel_63d},
    "vts_359_vol_term_inversion_accel_126d": {"inputs": ["close"], "func": vts_359_vol_term_inversion_accel_126d},
    "vts_360_vol_term_inversion_accel_252d": {"inputs": ["close"], "func": vts_360_vol_term_inversion_accel_252d},
    "vts_361_vol_peak_dist_accel_5d": {"inputs": ["close"], "func": vts_361_vol_peak_dist_accel_5d},
    "vts_362_vol_peak_dist_accel_21d": {"inputs": ["close"], "func": vts_362_vol_peak_dist_accel_21d},
    "vts_363_vol_peak_dist_accel_63d": {"inputs": ["close"], "func": vts_363_vol_peak_dist_accel_63d},
    "vts_364_vol_peak_dist_accel_126d": {"inputs": ["close"], "func": vts_364_vol_peak_dist_accel_126d},
    "vts_365_vol_peak_dist_accel_252d": {"inputs": ["close"], "func": vts_365_vol_peak_dist_accel_252d},
    "vts_366_vol_tail_spread_accel_5d": {"inputs": ["close"], "func": vts_366_vol_tail_spread_accel_5d},
    "vts_367_vol_tail_spread_accel_21d": {"inputs": ["close"], "func": vts_367_vol_tail_spread_accel_21d},
    "vts_368_vol_tail_spread_accel_63d": {"inputs": ["close"], "func": vts_368_vol_tail_spread_accel_63d},
    "vts_369_vol_tail_spread_accel_126d": {"inputs": ["close"], "func": vts_369_vol_tail_spread_accel_126d},
    "vts_370_vol_tail_spread_accel_252d": {"inputs": ["close"], "func": vts_370_vol_tail_spread_accel_252d},
    "vts_371_vol_structural_stability_accel_5d": {"inputs": ["close"], "func": vts_371_vol_structural_stability_accel_5d},
    "vts_372_vol_structural_stability_accel_21d": {"inputs": ["close"], "func": vts_372_vol_structural_stability_accel_21d},
    "vts_373_vol_structural_stability_accel_63d": {"inputs": ["close"], "func": vts_373_vol_structural_stability_accel_63d},
    "vts_374_vol_structural_stability_accel_126d": {"inputs": ["close"], "func": vts_374_vol_structural_stability_accel_126d},
    "vts_375_vol_structural_stability_accel_252d": {"inputs": ["close"], "func": vts_375_vol_structural_stability_accel_252d},
}
