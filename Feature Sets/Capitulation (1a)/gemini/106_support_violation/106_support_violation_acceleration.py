"""
106_support_violation — Acceleration (3rd Derivatives)
Domain: support_violation
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

def supv_301_support_252d_break_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_301_support_252d_break_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def supv_302_support_252d_break_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_302_support_252d_break_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def supv_303_support_252d_break_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_303_support_252d_break_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def supv_304_support_252d_break_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_304_support_252d_break_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def supv_305_support_252d_break_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_305_support_252d_break_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def supv_306_support_63d_break_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_306_support_63d_break_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def supv_307_support_63d_break_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_307_support_63d_break_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def supv_308_support_63d_break_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_308_support_63d_break_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def supv_309_support_63d_break_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_309_support_63d_break_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def supv_310_support_63d_break_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_310_support_63d_break_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def supv_311_volume_on_breakout_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_311_volume_on_breakout_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def supv_312_volume_on_breakout_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_312_volume_on_breakout_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def supv_313_volume_on_breakout_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_313_volume_on_breakout_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def supv_314_volume_on_breakout_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_314_volume_on_breakout_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def supv_315_volume_on_breakout_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_315_volume_on_breakout_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def supv_316_support_proximity_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_316_support_proximity_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(5).diff(_TD_MON)

def supv_317_support_proximity_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_317_support_proximity_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(21).diff(_TD_MON)

def supv_318_support_proximity_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_318_support_proximity_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(63).diff(_TD_MON)

def supv_319_support_proximity_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_319_support_proximity_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(126).diff(_TD_MON)

def supv_320_support_proximity_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_320_support_proximity_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(252).diff(_TD_MON)

def supv_321_support_bounce_failure_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_321_support_bounce_failure_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(5).diff(_TD_MON)

def supv_322_support_bounce_failure_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_322_support_bounce_failure_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(21).diff(_TD_MON)

def supv_323_support_bounce_failure_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_323_support_bounce_failure_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(63).diff(_TD_MON)

def supv_324_support_bounce_failure_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_324_support_bounce_failure_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(126).diff(_TD_MON)

def supv_325_support_bounce_failure_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_325_support_bounce_failure_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(252).diff(_TD_MON)

def supv_326_multiple_support_test_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_326_multiple_support_test_accel_5d
    ECONOMIC RATIONALE: Acceleration of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(5).diff(_TD_MON)

def supv_327_multiple_support_test_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_327_multiple_support_test_accel_21d
    ECONOMIC RATIONALE: Acceleration of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(21).diff(_TD_MON)

def supv_328_multiple_support_test_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_328_multiple_support_test_accel_63d
    ECONOMIC RATIONALE: Acceleration of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(63).diff(_TD_MON)

def supv_329_multiple_support_test_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_329_multiple_support_test_accel_126d
    ECONOMIC RATIONALE: Acceleration of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(126).diff(_TD_MON)

def supv_330_multiple_support_test_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_330_multiple_support_test_accel_252d
    ECONOMIC RATIONALE: Acceleration of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(252).diff(_TD_MON)

def supv_331_support_zone_density_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_331_support_zone_density_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(5).diff(_TD_MON)

def supv_332_support_zone_density_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_332_support_zone_density_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(21).diff(_TD_MON)

def supv_333_support_zone_density_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_333_support_zone_density_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(63).diff(_TD_MON)

def supv_334_support_zone_density_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_334_support_zone_density_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(126).diff(_TD_MON)

def supv_335_support_zone_density_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_335_support_zone_density_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(252).diff(_TD_MON)

def supv_336_breakdown_momentum_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_336_breakdown_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(5).diff(_TD_MON)

def supv_337_breakdown_momentum_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_337_breakdown_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(21).diff(_TD_MON)

def supv_338_breakdown_momentum_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_338_breakdown_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(63).diff(_TD_MON)

def supv_339_breakdown_momentum_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_339_breakdown_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(126).diff(_TD_MON)

def supv_340_breakdown_momentum_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_340_breakdown_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(252).diff(_TD_MON)

def supv_341_support_reversal_trap_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_341_support_reversal_trap_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(5).diff(_TD_MON)

def supv_342_support_reversal_trap_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_342_support_reversal_trap_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(21).diff(_TD_MON)

def supv_343_support_reversal_trap_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_343_support_reversal_trap_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(63).diff(_TD_MON)

def supv_344_support_reversal_trap_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_344_support_reversal_trap_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(126).diff(_TD_MON)

def supv_345_support_reversal_trap_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_345_support_reversal_trap_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(252).diff(_TD_MON)

def supv_346_support_gap_down_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_346_support_gap_down_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(5).diff(_TD_MON)

def supv_347_support_gap_down_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_347_support_gap_down_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(21).diff(_TD_MON)

def supv_348_support_gap_down_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_348_support_gap_down_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(63).diff(_TD_MON)

def supv_349_support_gap_down_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_349_support_gap_down_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(126).diff(_TD_MON)

def supv_350_support_gap_down_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_350_support_gap_down_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(252).diff(_TD_MON)

def supv_351_psychological_support_100_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_351_psychological_support_100_accel_5d
    ECONOMIC RATIONALE: Acceleration of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(5).diff(_TD_MON)

def supv_352_psychological_support_100_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_352_psychological_support_100_accel_21d
    ECONOMIC RATIONALE: Acceleration of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(21).diff(_TD_MON)

def supv_353_psychological_support_100_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_353_psychological_support_100_accel_63d
    ECONOMIC RATIONALE: Acceleration of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(63).diff(_TD_MON)

def supv_354_psychological_support_100_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_354_psychological_support_100_accel_126d
    ECONOMIC RATIONALE: Acceleration of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(126).diff(_TD_MON)

def supv_355_psychological_support_100_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_355_psychological_support_100_accel_252d
    ECONOMIC RATIONALE: Acceleration of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(252).diff(_TD_MON)

def supv_356_support_vol_z_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_356_support_vol_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(5).diff(_TD_MON)

def supv_357_support_vol_z_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_357_support_vol_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(21).diff(_TD_MON)

def supv_358_support_vol_z_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_358_support_vol_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(63).diff(_TD_MON)

def supv_359_support_vol_z_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_359_support_vol_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(126).diff(_TD_MON)

def supv_360_support_vol_z_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_360_support_vol_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(252).diff(_TD_MON)

def supv_361_structural_breakdown_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_361_structural_breakdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(5).diff(_TD_MON)

def supv_362_structural_breakdown_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_362_structural_breakdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(21).diff(_TD_MON)

def supv_363_structural_breakdown_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_363_structural_breakdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(63).diff(_TD_MON)

def supv_364_structural_breakdown_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_364_structural_breakdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(126).diff(_TD_MON)

def supv_365_structural_breakdown_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_365_structural_breakdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(252).diff(_TD_MON)

def supv_366_support_recovery_rate_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_366_support_recovery_rate_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(5).diff(_TD_MON)

def supv_367_support_recovery_rate_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_367_support_recovery_rate_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(21).diff(_TD_MON)

def supv_368_support_recovery_rate_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_368_support_recovery_rate_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(63).diff(_TD_MON)

def supv_369_support_recovery_rate_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_369_support_recovery_rate_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(126).diff(_TD_MON)

def supv_370_support_recovery_rate_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_370_support_recovery_rate_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(252).diff(_TD_MON)

def supv_371_support_cascade_risk_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_371_support_cascade_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(5).diff(_TD_MON)

def supv_372_support_cascade_risk_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_372_support_cascade_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(21).diff(_TD_MON)

def supv_373_support_cascade_risk_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_373_support_cascade_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(63).diff(_TD_MON)

def supv_374_support_cascade_risk_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_374_support_cascade_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(126).diff(_TD_MON)

def supv_375_support_cascade_risk_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_375_support_cascade_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V106_REGISTRY_ACCEL = {
    "supv_301_support_252d_break_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_301_support_252d_break_accel_5d},
    "supv_302_support_252d_break_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_302_support_252d_break_accel_21d},
    "supv_303_support_252d_break_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_303_support_252d_break_accel_63d},
    "supv_304_support_252d_break_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_304_support_252d_break_accel_126d},
    "supv_305_support_252d_break_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_305_support_252d_break_accel_252d},
    "supv_306_support_63d_break_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_306_support_63d_break_accel_5d},
    "supv_307_support_63d_break_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_307_support_63d_break_accel_21d},
    "supv_308_support_63d_break_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_308_support_63d_break_accel_63d},
    "supv_309_support_63d_break_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_309_support_63d_break_accel_126d},
    "supv_310_support_63d_break_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_310_support_63d_break_accel_252d},
    "supv_311_volume_on_breakout_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_311_volume_on_breakout_accel_5d},
    "supv_312_volume_on_breakout_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_312_volume_on_breakout_accel_21d},
    "supv_313_volume_on_breakout_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_313_volume_on_breakout_accel_63d},
    "supv_314_volume_on_breakout_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_314_volume_on_breakout_accel_126d},
    "supv_315_volume_on_breakout_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_315_volume_on_breakout_accel_252d},
    "supv_316_support_proximity_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_316_support_proximity_accel_5d},
    "supv_317_support_proximity_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_317_support_proximity_accel_21d},
    "supv_318_support_proximity_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_318_support_proximity_accel_63d},
    "supv_319_support_proximity_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_319_support_proximity_accel_126d},
    "supv_320_support_proximity_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_320_support_proximity_accel_252d},
    "supv_321_support_bounce_failure_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_321_support_bounce_failure_accel_5d},
    "supv_322_support_bounce_failure_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_322_support_bounce_failure_accel_21d},
    "supv_323_support_bounce_failure_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_323_support_bounce_failure_accel_63d},
    "supv_324_support_bounce_failure_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_324_support_bounce_failure_accel_126d},
    "supv_325_support_bounce_failure_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_325_support_bounce_failure_accel_252d},
    "supv_326_multiple_support_test_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_326_multiple_support_test_accel_5d},
    "supv_327_multiple_support_test_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_327_multiple_support_test_accel_21d},
    "supv_328_multiple_support_test_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_328_multiple_support_test_accel_63d},
    "supv_329_multiple_support_test_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_329_multiple_support_test_accel_126d},
    "supv_330_multiple_support_test_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_330_multiple_support_test_accel_252d},
    "supv_331_support_zone_density_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_331_support_zone_density_accel_5d},
    "supv_332_support_zone_density_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_332_support_zone_density_accel_21d},
    "supv_333_support_zone_density_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_333_support_zone_density_accel_63d},
    "supv_334_support_zone_density_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_334_support_zone_density_accel_126d},
    "supv_335_support_zone_density_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_335_support_zone_density_accel_252d},
    "supv_336_breakdown_momentum_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_336_breakdown_momentum_accel_5d},
    "supv_337_breakdown_momentum_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_337_breakdown_momentum_accel_21d},
    "supv_338_breakdown_momentum_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_338_breakdown_momentum_accel_63d},
    "supv_339_breakdown_momentum_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_339_breakdown_momentum_accel_126d},
    "supv_340_breakdown_momentum_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_340_breakdown_momentum_accel_252d},
    "supv_341_support_reversal_trap_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_341_support_reversal_trap_accel_5d},
    "supv_342_support_reversal_trap_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_342_support_reversal_trap_accel_21d},
    "supv_343_support_reversal_trap_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_343_support_reversal_trap_accel_63d},
    "supv_344_support_reversal_trap_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_344_support_reversal_trap_accel_126d},
    "supv_345_support_reversal_trap_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_345_support_reversal_trap_accel_252d},
    "supv_346_support_gap_down_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_346_support_gap_down_accel_5d},
    "supv_347_support_gap_down_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_347_support_gap_down_accel_21d},
    "supv_348_support_gap_down_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_348_support_gap_down_accel_63d},
    "supv_349_support_gap_down_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_349_support_gap_down_accel_126d},
    "supv_350_support_gap_down_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_350_support_gap_down_accel_252d},
    "supv_351_psychological_support_100_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_351_psychological_support_100_accel_5d},
    "supv_352_psychological_support_100_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_352_psychological_support_100_accel_21d},
    "supv_353_psychological_support_100_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_353_psychological_support_100_accel_63d},
    "supv_354_psychological_support_100_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_354_psychological_support_100_accel_126d},
    "supv_355_psychological_support_100_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_355_psychological_support_100_accel_252d},
    "supv_356_support_vol_z_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_356_support_vol_z_accel_5d},
    "supv_357_support_vol_z_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_357_support_vol_z_accel_21d},
    "supv_358_support_vol_z_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_358_support_vol_z_accel_63d},
    "supv_359_support_vol_z_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_359_support_vol_z_accel_126d},
    "supv_360_support_vol_z_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_360_support_vol_z_accel_252d},
    "supv_361_structural_breakdown_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_361_structural_breakdown_accel_5d},
    "supv_362_structural_breakdown_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_362_structural_breakdown_accel_21d},
    "supv_363_structural_breakdown_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_363_structural_breakdown_accel_63d},
    "supv_364_structural_breakdown_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_364_structural_breakdown_accel_126d},
    "supv_365_structural_breakdown_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_365_structural_breakdown_accel_252d},
    "supv_366_support_recovery_rate_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_366_support_recovery_rate_accel_5d},
    "supv_367_support_recovery_rate_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_367_support_recovery_rate_accel_21d},
    "supv_368_support_recovery_rate_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_368_support_recovery_rate_accel_63d},
    "supv_369_support_recovery_rate_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_369_support_recovery_rate_accel_126d},
    "supv_370_support_recovery_rate_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_370_support_recovery_rate_accel_252d},
    "supv_371_support_cascade_risk_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_371_support_cascade_risk_accel_5d},
    "supv_372_support_cascade_risk_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_372_support_cascade_risk_accel_21d},
    "supv_373_support_cascade_risk_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_373_support_cascade_risk_accel_63d},
    "supv_374_support_cascade_risk_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_374_support_cascade_risk_accel_126d},
    "supv_375_support_cascade_risk_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_375_support_cascade_risk_accel_252d},
}
