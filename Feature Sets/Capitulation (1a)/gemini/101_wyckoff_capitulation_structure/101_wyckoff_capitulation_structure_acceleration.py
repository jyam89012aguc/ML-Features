"""
101_wyckoff_capitulation_structure — Acceleration (3rd Derivatives)
Domain: wyckoff_capitulation_structure
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

def wyck_301_selling_climax_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_301_selling_climax_accel_5d
    ECONOMIC RATIONALE: Acceleration of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(5).diff(_TD_MON)

def wyck_302_selling_climax_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_302_selling_climax_accel_21d
    ECONOMIC RATIONALE: Acceleration of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(21).diff(_TD_MON)

def wyck_303_selling_climax_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_303_selling_climax_accel_63d
    ECONOMIC RATIONALE: Acceleration of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(63).diff(_TD_MON)

def wyck_304_selling_climax_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_304_selling_climax_accel_126d
    ECONOMIC RATIONALE: Acceleration of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(126).diff(_TD_MON)

def wyck_305_selling_climax_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_305_selling_climax_accel_252d
    ECONOMIC RATIONALE: Acceleration of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(252).diff(_TD_MON)

def wyck_306_automatic_rally_failure_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_306_automatic_rally_failure_accel_5d
    ECONOMIC RATIONALE: Acceleration of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(5).diff(_TD_MON)

def wyck_307_automatic_rally_failure_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_307_automatic_rally_failure_accel_21d
    ECONOMIC RATIONALE: Acceleration of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(21).diff(_TD_MON)

def wyck_308_automatic_rally_failure_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_308_automatic_rally_failure_accel_63d
    ECONOMIC RATIONALE: Acceleration of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(63).diff(_TD_MON)

def wyck_309_automatic_rally_failure_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_309_automatic_rally_failure_accel_126d
    ECONOMIC RATIONALE: Acceleration of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(126).diff(_TD_MON)

def wyck_310_automatic_rally_failure_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_310_automatic_rally_failure_accel_252d
    ECONOMIC RATIONALE: Acceleration of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(252).diff(_TD_MON)

def wyck_311_secondary_test_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_311_secondary_test_accel_5d
    ECONOMIC RATIONALE: Acceleration of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(5).diff(_TD_MON)

def wyck_312_secondary_test_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_312_secondary_test_accel_21d
    ECONOMIC RATIONALE: Acceleration of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(21).diff(_TD_MON)

def wyck_313_secondary_test_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_313_secondary_test_accel_63d
    ECONOMIC RATIONALE: Acceleration of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(63).diff(_TD_MON)

def wyck_314_secondary_test_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_314_secondary_test_accel_126d
    ECONOMIC RATIONALE: Acceleration of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(126).diff(_TD_MON)

def wyck_315_secondary_test_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_315_secondary_test_accel_252d
    ECONOMIC RATIONALE: Acceleration of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(252).diff(_TD_MON)

def wyck_316_spring_detection_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_316_spring_detection_accel_5d
    ECONOMIC RATIONALE: Acceleration of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(5).diff(_TD_MON)

def wyck_317_spring_detection_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_317_spring_detection_accel_21d
    ECONOMIC RATIONALE: Acceleration of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(21).diff(_TD_MON)

def wyck_318_spring_detection_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_318_spring_detection_accel_63d
    ECONOMIC RATIONALE: Acceleration of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(63).diff(_TD_MON)

def wyck_319_spring_detection_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_319_spring_detection_accel_126d
    ECONOMIC RATIONALE: Acceleration of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(126).diff(_TD_MON)

def wyck_320_spring_detection_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_320_spring_detection_accel_252d
    ECONOMIC RATIONALE: Acceleration of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(252).diff(_TD_MON)

def wyck_321_sign_of_weakness_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_321_sign_of_weakness_accel_5d
    ECONOMIC RATIONALE: Acceleration of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(5).diff(_TD_MON)

def wyck_322_sign_of_weakness_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_322_sign_of_weakness_accel_21d
    ECONOMIC RATIONALE: Acceleration of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(21).diff(_TD_MON)

def wyck_323_sign_of_weakness_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_323_sign_of_weakness_accel_63d
    ECONOMIC RATIONALE: Acceleration of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(63).diff(_TD_MON)

def wyck_324_sign_of_weakness_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_324_sign_of_weakness_accel_126d
    ECONOMIC RATIONALE: Acceleration of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(126).diff(_TD_MON)

def wyck_325_sign_of_weakness_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_325_sign_of_weakness_accel_252d
    ECONOMIC RATIONALE: Acceleration of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(252).diff(_TD_MON)

def wyck_326_supply_overcoming_demand_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_326_supply_overcoming_demand_accel_5d
    ECONOMIC RATIONALE: Acceleration of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(5).diff(_TD_MON)

def wyck_327_supply_overcoming_demand_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_327_supply_overcoming_demand_accel_21d
    ECONOMIC RATIONALE: Acceleration of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(21).diff(_TD_MON)

def wyck_328_supply_overcoming_demand_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_328_supply_overcoming_demand_accel_63d
    ECONOMIC RATIONALE: Acceleration of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(63).diff(_TD_MON)

def wyck_329_supply_overcoming_demand_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_329_supply_overcoming_demand_accel_126d
    ECONOMIC RATIONALE: Acceleration of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(126).diff(_TD_MON)

def wyck_330_supply_overcoming_demand_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_330_supply_overcoming_demand_accel_252d
    ECONOMIC RATIONALE: Acceleration of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(252).diff(_TD_MON)

def wyck_331_trading_range_position_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_331_trading_range_position_accel_5d
    ECONOMIC RATIONALE: Acceleration of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(5).diff(_TD_MON)

def wyck_332_trading_range_position_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_332_trading_range_position_accel_21d
    ECONOMIC RATIONALE: Acceleration of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(21).diff(_TD_MON)

def wyck_333_trading_range_position_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_333_trading_range_position_accel_63d
    ECONOMIC RATIONALE: Acceleration of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(63).diff(_TD_MON)

def wyck_334_trading_range_position_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_334_trading_range_position_accel_126d
    ECONOMIC RATIONALE: Acceleration of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(126).diff(_TD_MON)

def wyck_335_trading_range_position_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_335_trading_range_position_accel_252d
    ECONOMIC RATIONALE: Acceleration of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(252).diff(_TD_MON)

def wyck_336_volume_dry_up_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_336_volume_dry_up_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(5).diff(_TD_MON)

def wyck_337_volume_dry_up_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_337_volume_dry_up_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(21).diff(_TD_MON)

def wyck_338_volume_dry_up_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_338_volume_dry_up_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(63).diff(_TD_MON)

def wyck_339_volume_dry_up_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_339_volume_dry_up_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(126).diff(_TD_MON)

def wyck_340_volume_dry_up_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_340_volume_dry_up_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(252).diff(_TD_MON)

def wyck_341_upthrust_detection_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_341_upthrust_detection_accel_5d
    ECONOMIC RATIONALE: Acceleration of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(5).diff(_TD_MON)

def wyck_342_upthrust_detection_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_342_upthrust_detection_accel_21d
    ECONOMIC RATIONALE: Acceleration of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(21).diff(_TD_MON)

def wyck_343_upthrust_detection_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_343_upthrust_detection_accel_63d
    ECONOMIC RATIONALE: Acceleration of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(63).diff(_TD_MON)

def wyck_344_upthrust_detection_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_344_upthrust_detection_accel_126d
    ECONOMIC RATIONALE: Acceleration of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(126).diff(_TD_MON)

def wyck_345_upthrust_detection_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_345_upthrust_detection_accel_252d
    ECONOMIC RATIONALE: Acceleration of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(252).diff(_TD_MON)

def wyck_346_preliminary_support_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_346_preliminary_support_accel_5d
    ECONOMIC RATIONALE: Acceleration of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(5).diff(_TD_MON)

def wyck_347_preliminary_support_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_347_preliminary_support_accel_21d
    ECONOMIC RATIONALE: Acceleration of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(21).diff(_TD_MON)

def wyck_348_preliminary_support_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_348_preliminary_support_accel_63d
    ECONOMIC RATIONALE: Acceleration of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(63).diff(_TD_MON)

def wyck_349_preliminary_support_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_349_preliminary_support_accel_126d
    ECONOMIC RATIONALE: Acceleration of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(126).diff(_TD_MON)

def wyck_350_preliminary_support_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_350_preliminary_support_accel_252d
    ECONOMIC RATIONALE: Acceleration of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(252).diff(_TD_MON)

def wyck_351_jump_across_creek_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_351_jump_across_creek_accel_5d
    ECONOMIC RATIONALE: Acceleration of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(5).diff(_TD_MON)

def wyck_352_jump_across_creek_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_352_jump_across_creek_accel_21d
    ECONOMIC RATIONALE: Acceleration of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(21).diff(_TD_MON)

def wyck_353_jump_across_creek_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_353_jump_across_creek_accel_63d
    ECONOMIC RATIONALE: Acceleration of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(63).diff(_TD_MON)

def wyck_354_jump_across_creek_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_354_jump_across_creek_accel_126d
    ECONOMIC RATIONALE: Acceleration of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(126).diff(_TD_MON)

def wyck_355_jump_across_creek_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_355_jump_across_creek_accel_252d
    ECONOMIC RATIONALE: Acceleration of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(252).diff(_TD_MON)

def wyck_356_last_point_of_supply_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_356_last_point_of_supply_accel_5d
    ECONOMIC RATIONALE: Acceleration of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(5).diff(_TD_MON)

def wyck_357_last_point_of_supply_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_357_last_point_of_supply_accel_21d
    ECONOMIC RATIONALE: Acceleration of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(21).diff(_TD_MON)

def wyck_358_last_point_of_supply_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_358_last_point_of_supply_accel_63d
    ECONOMIC RATIONALE: Acceleration of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(63).diff(_TD_MON)

def wyck_359_last_point_of_supply_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_359_last_point_of_supply_accel_126d
    ECONOMIC RATIONALE: Acceleration of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(126).diff(_TD_MON)

def wyck_360_last_point_of_supply_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_360_last_point_of_supply_accel_252d
    ECONOMIC RATIONALE: Acceleration of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(252).diff(_TD_MON)

def wyck_361_volume_price_divergence_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_361_volume_price_divergence_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(5).diff(_TD_MON)

def wyck_362_volume_price_divergence_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_362_volume_price_divergence_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(21).diff(_TD_MON)

def wyck_363_volume_price_divergence_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_363_volume_price_divergence_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(63).diff(_TD_MON)

def wyck_364_volume_price_divergence_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_364_volume_price_divergence_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(126).diff(_TD_MON)

def wyck_365_volume_price_divergence_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_365_volume_price_divergence_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(252).diff(_TD_MON)

def wyck_366_effort_vs_result_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_366_effort_vs_result_accel_5d
    ECONOMIC RATIONALE: Acceleration of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def wyck_367_effort_vs_result_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_367_effort_vs_result_accel_21d
    ECONOMIC RATIONALE: Acceleration of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def wyck_368_effort_vs_result_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_368_effort_vs_result_accel_63d
    ECONOMIC RATIONALE: Acceleration of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def wyck_369_effort_vs_result_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_369_effort_vs_result_accel_126d
    ECONOMIC RATIONALE: Acceleration of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def wyck_370_effort_vs_result_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_370_effort_vs_result_accel_252d
    ECONOMIC RATIONALE: Acceleration of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def wyck_371_trend_channel_violation_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_371_trend_channel_violation_accel_5d
    ECONOMIC RATIONALE: Acceleration of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(5).diff(_TD_MON)

def wyck_372_trend_channel_violation_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_372_trend_channel_violation_accel_21d
    ECONOMIC RATIONALE: Acceleration of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(21).diff(_TD_MON)

def wyck_373_trend_channel_violation_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_373_trend_channel_violation_accel_63d
    ECONOMIC RATIONALE: Acceleration of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(63).diff(_TD_MON)

def wyck_374_trend_channel_violation_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_374_trend_channel_violation_accel_126d
    ECONOMIC RATIONALE: Acceleration of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(126).diff(_TD_MON)

def wyck_375_trend_channel_violation_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_375_trend_channel_violation_accel_252d
    ECONOMIC RATIONALE: Acceleration of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V101_REGISTRY_ACCEL = {
    "wyck_301_selling_climax_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_301_selling_climax_accel_5d},
    "wyck_302_selling_climax_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_302_selling_climax_accel_21d},
    "wyck_303_selling_climax_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_303_selling_climax_accel_63d},
    "wyck_304_selling_climax_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_304_selling_climax_accel_126d},
    "wyck_305_selling_climax_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_305_selling_climax_accel_252d},
    "wyck_306_automatic_rally_failure_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_306_automatic_rally_failure_accel_5d},
    "wyck_307_automatic_rally_failure_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_307_automatic_rally_failure_accel_21d},
    "wyck_308_automatic_rally_failure_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_308_automatic_rally_failure_accel_63d},
    "wyck_309_automatic_rally_failure_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_309_automatic_rally_failure_accel_126d},
    "wyck_310_automatic_rally_failure_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_310_automatic_rally_failure_accel_252d},
    "wyck_311_secondary_test_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_311_secondary_test_accel_5d},
    "wyck_312_secondary_test_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_312_secondary_test_accel_21d},
    "wyck_313_secondary_test_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_313_secondary_test_accel_63d},
    "wyck_314_secondary_test_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_314_secondary_test_accel_126d},
    "wyck_315_secondary_test_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_315_secondary_test_accel_252d},
    "wyck_316_spring_detection_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_316_spring_detection_accel_5d},
    "wyck_317_spring_detection_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_317_spring_detection_accel_21d},
    "wyck_318_spring_detection_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_318_spring_detection_accel_63d},
    "wyck_319_spring_detection_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_319_spring_detection_accel_126d},
    "wyck_320_spring_detection_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_320_spring_detection_accel_252d},
    "wyck_321_sign_of_weakness_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_321_sign_of_weakness_accel_5d},
    "wyck_322_sign_of_weakness_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_322_sign_of_weakness_accel_21d},
    "wyck_323_sign_of_weakness_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_323_sign_of_weakness_accel_63d},
    "wyck_324_sign_of_weakness_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_324_sign_of_weakness_accel_126d},
    "wyck_325_sign_of_weakness_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_325_sign_of_weakness_accel_252d},
    "wyck_326_supply_overcoming_demand_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_326_supply_overcoming_demand_accel_5d},
    "wyck_327_supply_overcoming_demand_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_327_supply_overcoming_demand_accel_21d},
    "wyck_328_supply_overcoming_demand_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_328_supply_overcoming_demand_accel_63d},
    "wyck_329_supply_overcoming_demand_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_329_supply_overcoming_demand_accel_126d},
    "wyck_330_supply_overcoming_demand_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_330_supply_overcoming_demand_accel_252d},
    "wyck_331_trading_range_position_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_331_trading_range_position_accel_5d},
    "wyck_332_trading_range_position_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_332_trading_range_position_accel_21d},
    "wyck_333_trading_range_position_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_333_trading_range_position_accel_63d},
    "wyck_334_trading_range_position_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_334_trading_range_position_accel_126d},
    "wyck_335_trading_range_position_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_335_trading_range_position_accel_252d},
    "wyck_336_volume_dry_up_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_336_volume_dry_up_accel_5d},
    "wyck_337_volume_dry_up_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_337_volume_dry_up_accel_21d},
    "wyck_338_volume_dry_up_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_338_volume_dry_up_accel_63d},
    "wyck_339_volume_dry_up_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_339_volume_dry_up_accel_126d},
    "wyck_340_volume_dry_up_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_340_volume_dry_up_accel_252d},
    "wyck_341_upthrust_detection_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_341_upthrust_detection_accel_5d},
    "wyck_342_upthrust_detection_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_342_upthrust_detection_accel_21d},
    "wyck_343_upthrust_detection_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_343_upthrust_detection_accel_63d},
    "wyck_344_upthrust_detection_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_344_upthrust_detection_accel_126d},
    "wyck_345_upthrust_detection_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_345_upthrust_detection_accel_252d},
    "wyck_346_preliminary_support_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_346_preliminary_support_accel_5d},
    "wyck_347_preliminary_support_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_347_preliminary_support_accel_21d},
    "wyck_348_preliminary_support_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_348_preliminary_support_accel_63d},
    "wyck_349_preliminary_support_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_349_preliminary_support_accel_126d},
    "wyck_350_preliminary_support_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_350_preliminary_support_accel_252d},
    "wyck_351_jump_across_creek_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_351_jump_across_creek_accel_5d},
    "wyck_352_jump_across_creek_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_352_jump_across_creek_accel_21d},
    "wyck_353_jump_across_creek_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_353_jump_across_creek_accel_63d},
    "wyck_354_jump_across_creek_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_354_jump_across_creek_accel_126d},
    "wyck_355_jump_across_creek_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_355_jump_across_creek_accel_252d},
    "wyck_356_last_point_of_supply_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_356_last_point_of_supply_accel_5d},
    "wyck_357_last_point_of_supply_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_357_last_point_of_supply_accel_21d},
    "wyck_358_last_point_of_supply_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_358_last_point_of_supply_accel_63d},
    "wyck_359_last_point_of_supply_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_359_last_point_of_supply_accel_126d},
    "wyck_360_last_point_of_supply_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_360_last_point_of_supply_accel_252d},
    "wyck_361_volume_price_divergence_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_361_volume_price_divergence_accel_5d},
    "wyck_362_volume_price_divergence_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_362_volume_price_divergence_accel_21d},
    "wyck_363_volume_price_divergence_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_363_volume_price_divergence_accel_63d},
    "wyck_364_volume_price_divergence_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_364_volume_price_divergence_accel_126d},
    "wyck_365_volume_price_divergence_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_365_volume_price_divergence_accel_252d},
    "wyck_366_effort_vs_result_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_366_effort_vs_result_accel_5d},
    "wyck_367_effort_vs_result_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_367_effort_vs_result_accel_21d},
    "wyck_368_effort_vs_result_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_368_effort_vs_result_accel_63d},
    "wyck_369_effort_vs_result_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_369_effort_vs_result_accel_126d},
    "wyck_370_effort_vs_result_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_370_effort_vs_result_accel_252d},
    "wyck_371_trend_channel_violation_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_371_trend_channel_violation_accel_5d},
    "wyck_372_trend_channel_violation_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_372_trend_channel_violation_accel_21d},
    "wyck_373_trend_channel_violation_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_373_trend_channel_violation_accel_63d},
    "wyck_374_trend_channel_violation_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_374_trend_channel_violation_accel_126d},
    "wyck_375_trend_channel_violation_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_375_trend_channel_violation_accel_252d},
}
