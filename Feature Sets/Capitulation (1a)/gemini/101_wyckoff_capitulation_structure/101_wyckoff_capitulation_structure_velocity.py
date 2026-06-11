"""
101_wyckoff_capitulation_structure — Velocity (2nd Derivatives)
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

def wyck_226_selling_climax_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_226_selling_climax_vel_5d
    ECONOMIC RATIONALE: Velocity of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(5)

def wyck_227_selling_climax_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_227_selling_climax_vel_21d
    ECONOMIC RATIONALE: Velocity of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(21)

def wyck_228_selling_climax_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_228_selling_climax_vel_63d
    ECONOMIC RATIONALE: Velocity of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(63)

def wyck_229_selling_climax_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_229_selling_climax_vel_126d
    ECONOMIC RATIONALE: Velocity of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(126)

def wyck_230_selling_climax_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_230_selling_climax_vel_252d
    ECONOMIC RATIONALE: Velocity of selling_climax. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).diff(252)

def wyck_231_automatic_rally_failure_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_231_automatic_rally_failure_vel_5d
    ECONOMIC RATIONALE: Velocity of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(5)

def wyck_232_automatic_rally_failure_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_232_automatic_rally_failure_vel_21d
    ECONOMIC RATIONALE: Velocity of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(21)

def wyck_233_automatic_rally_failure_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_233_automatic_rally_failure_vel_63d
    ECONOMIC RATIONALE: Velocity of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(63)

def wyck_234_automatic_rally_failure_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_234_automatic_rally_failure_vel_126d
    ECONOMIC RATIONALE: Velocity of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(126)

def wyck_235_automatic_rally_failure_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_235_automatic_rally_failure_vel_252d
    ECONOMIC RATIONALE: Velocity of automatic_rally_failure. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).diff(252)

def wyck_236_secondary_test_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_236_secondary_test_vel_5d
    ECONOMIC RATIONALE: Velocity of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(5)

def wyck_237_secondary_test_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_237_secondary_test_vel_21d
    ECONOMIC RATIONALE: Velocity of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(21)

def wyck_238_secondary_test_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_238_secondary_test_vel_63d
    ECONOMIC RATIONALE: Velocity of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(63)

def wyck_239_secondary_test_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_239_secondary_test_vel_126d
    ECONOMIC RATIONALE: Velocity of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(126)

def wyck_240_secondary_test_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_240_secondary_test_vel_252d
    ECONOMIC RATIONALE: Velocity of secondary_test. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).diff(252)

def wyck_241_spring_detection_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_241_spring_detection_vel_5d
    ECONOMIC RATIONALE: Velocity of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(5)

def wyck_242_spring_detection_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_242_spring_detection_vel_21d
    ECONOMIC RATIONALE: Velocity of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(21)

def wyck_243_spring_detection_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_243_spring_detection_vel_63d
    ECONOMIC RATIONALE: Velocity of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(63)

def wyck_244_spring_detection_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_244_spring_detection_vel_126d
    ECONOMIC RATIONALE: Velocity of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(126)

def wyck_245_spring_detection_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_245_spring_detection_vel_252d
    ECONOMIC RATIONALE: Velocity of spring_detection. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).diff(252)

def wyck_246_sign_of_weakness_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_246_sign_of_weakness_vel_5d
    ECONOMIC RATIONALE: Velocity of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(5)

def wyck_247_sign_of_weakness_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_247_sign_of_weakness_vel_21d
    ECONOMIC RATIONALE: Velocity of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(21)

def wyck_248_sign_of_weakness_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_248_sign_of_weakness_vel_63d
    ECONOMIC RATIONALE: Velocity of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(63)

def wyck_249_sign_of_weakness_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_249_sign_of_weakness_vel_126d
    ECONOMIC RATIONALE: Velocity of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(126)

def wyck_250_sign_of_weakness_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_250_sign_of_weakness_vel_252d
    ECONOMIC RATIONALE: Velocity of sign_of_weakness. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).diff(252)

def wyck_251_supply_overcoming_demand_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_251_supply_overcoming_demand_vel_5d
    ECONOMIC RATIONALE: Velocity of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(5)

def wyck_252_supply_overcoming_demand_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_252_supply_overcoming_demand_vel_21d
    ECONOMIC RATIONALE: Velocity of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(21)

def wyck_253_supply_overcoming_demand_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_253_supply_overcoming_demand_vel_63d
    ECONOMIC RATIONALE: Velocity of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(63)

def wyck_254_supply_overcoming_demand_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_254_supply_overcoming_demand_vel_126d
    ECONOMIC RATIONALE: Velocity of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(126)

def wyck_255_supply_overcoming_demand_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_255_supply_overcoming_demand_vel_252d
    ECONOMIC RATIONALE: Velocity of supply_overcoming_demand. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).diff(252)

def wyck_256_trading_range_position_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_256_trading_range_position_vel_5d
    ECONOMIC RATIONALE: Velocity of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(5)

def wyck_257_trading_range_position_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_257_trading_range_position_vel_21d
    ECONOMIC RATIONALE: Velocity of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(21)

def wyck_258_trading_range_position_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_258_trading_range_position_vel_63d
    ECONOMIC RATIONALE: Velocity of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(63)

def wyck_259_trading_range_position_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_259_trading_range_position_vel_126d
    ECONOMIC RATIONALE: Velocity of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(126)

def wyck_260_trading_range_position_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_260_trading_range_position_vel_252d
    ECONOMIC RATIONALE: Velocity of trading_range_position. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).diff(252)

def wyck_261_volume_dry_up_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_261_volume_dry_up_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(5)

def wyck_262_volume_dry_up_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_262_volume_dry_up_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(21)

def wyck_263_volume_dry_up_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_263_volume_dry_up_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(63)

def wyck_264_volume_dry_up_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_264_volume_dry_up_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(126)

def wyck_265_volume_dry_up_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_265_volume_dry_up_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_dry_up. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).diff(252)

def wyck_266_upthrust_detection_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_266_upthrust_detection_vel_5d
    ECONOMIC RATIONALE: Velocity of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(5)

def wyck_267_upthrust_detection_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_267_upthrust_detection_vel_21d
    ECONOMIC RATIONALE: Velocity of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(21)

def wyck_268_upthrust_detection_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_268_upthrust_detection_vel_63d
    ECONOMIC RATIONALE: Velocity of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(63)

def wyck_269_upthrust_detection_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_269_upthrust_detection_vel_126d
    ECONOMIC RATIONALE: Velocity of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(126)

def wyck_270_upthrust_detection_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_270_upthrust_detection_vel_252d
    ECONOMIC RATIONALE: Velocity of upthrust_detection. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).diff(252)

def wyck_271_preliminary_support_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_271_preliminary_support_vel_5d
    ECONOMIC RATIONALE: Velocity of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(5)

def wyck_272_preliminary_support_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_272_preliminary_support_vel_21d
    ECONOMIC RATIONALE: Velocity of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(21)

def wyck_273_preliminary_support_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_273_preliminary_support_vel_63d
    ECONOMIC RATIONALE: Velocity of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(63)

def wyck_274_preliminary_support_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_274_preliminary_support_vel_126d
    ECONOMIC RATIONALE: Velocity of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(126)

def wyck_275_preliminary_support_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_275_preliminary_support_vel_252d
    ECONOMIC RATIONALE: Velocity of preliminary_support. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).diff(252)

def wyck_276_jump_across_creek_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_276_jump_across_creek_vel_5d
    ECONOMIC RATIONALE: Velocity of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(5)

def wyck_277_jump_across_creek_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_277_jump_across_creek_vel_21d
    ECONOMIC RATIONALE: Velocity of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(21)

def wyck_278_jump_across_creek_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_278_jump_across_creek_vel_63d
    ECONOMIC RATIONALE: Velocity of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(63)

def wyck_279_jump_across_creek_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_279_jump_across_creek_vel_126d
    ECONOMIC RATIONALE: Velocity of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(126)

def wyck_280_jump_across_creek_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_280_jump_across_creek_vel_252d
    ECONOMIC RATIONALE: Velocity of jump_across_creek. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).diff(252)

def wyck_281_last_point_of_supply_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_281_last_point_of_supply_vel_5d
    ECONOMIC RATIONALE: Velocity of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(5)

def wyck_282_last_point_of_supply_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_282_last_point_of_supply_vel_21d
    ECONOMIC RATIONALE: Velocity of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(21)

def wyck_283_last_point_of_supply_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_283_last_point_of_supply_vel_63d
    ECONOMIC RATIONALE: Velocity of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(63)

def wyck_284_last_point_of_supply_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_284_last_point_of_supply_vel_126d
    ECONOMIC RATIONALE: Velocity of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(126)

def wyck_285_last_point_of_supply_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_285_last_point_of_supply_vel_252d
    ECONOMIC RATIONALE: Velocity of last_point_of_supply. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).diff(252)

def wyck_286_volume_price_divergence_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_286_volume_price_divergence_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(5)

def wyck_287_volume_price_divergence_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_287_volume_price_divergence_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(21)

def wyck_288_volume_price_divergence_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_288_volume_price_divergence_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(63)

def wyck_289_volume_price_divergence_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_289_volume_price_divergence_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(126)

def wyck_290_volume_price_divergence_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_290_volume_price_divergence_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_price_divergence. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).diff(252)

def wyck_291_effort_vs_result_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_291_effort_vs_result_vel_5d
    ECONOMIC RATIONALE: Velocity of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(5)

def wyck_292_effort_vs_result_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_292_effort_vs_result_vel_21d
    ECONOMIC RATIONALE: Velocity of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(21)

def wyck_293_effort_vs_result_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_293_effort_vs_result_vel_63d
    ECONOMIC RATIONALE: Velocity of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(63)

def wyck_294_effort_vs_result_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_294_effort_vs_result_vel_126d
    ECONOMIC RATIONALE: Velocity of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(126)

def wyck_295_effort_vs_result_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_295_effort_vs_result_vel_252d
    ECONOMIC RATIONALE: Velocity of effort_vs_result. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).diff(252)

def wyck_296_trend_channel_violation_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_296_trend_channel_violation_vel_5d
    ECONOMIC RATIONALE: Velocity of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(5)

def wyck_297_trend_channel_violation_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_297_trend_channel_violation_vel_21d
    ECONOMIC RATIONALE: Velocity of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(21)

def wyck_298_trend_channel_violation_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_298_trend_channel_violation_vel_63d
    ECONOMIC RATIONALE: Velocity of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(63)

def wyck_299_trend_channel_violation_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_299_trend_channel_violation_vel_126d
    ECONOMIC RATIONALE: Velocity of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(126)

def wyck_300_trend_channel_violation_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_300_trend_channel_violation_vel_252d
    ECONOMIC RATIONALE: Velocity of trend_channel_violation. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V101_REGISTRY_VEL = {
    "wyck_226_selling_climax_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_226_selling_climax_vel_5d},
    "wyck_227_selling_climax_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_227_selling_climax_vel_21d},
    "wyck_228_selling_climax_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_228_selling_climax_vel_63d},
    "wyck_229_selling_climax_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_229_selling_climax_vel_126d},
    "wyck_230_selling_climax_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_230_selling_climax_vel_252d},
    "wyck_231_automatic_rally_failure_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_231_automatic_rally_failure_vel_5d},
    "wyck_232_automatic_rally_failure_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_232_automatic_rally_failure_vel_21d},
    "wyck_233_automatic_rally_failure_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_233_automatic_rally_failure_vel_63d},
    "wyck_234_automatic_rally_failure_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_234_automatic_rally_failure_vel_126d},
    "wyck_235_automatic_rally_failure_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_235_automatic_rally_failure_vel_252d},
    "wyck_236_secondary_test_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_236_secondary_test_vel_5d},
    "wyck_237_secondary_test_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_237_secondary_test_vel_21d},
    "wyck_238_secondary_test_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_238_secondary_test_vel_63d},
    "wyck_239_secondary_test_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_239_secondary_test_vel_126d},
    "wyck_240_secondary_test_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_240_secondary_test_vel_252d},
    "wyck_241_spring_detection_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_241_spring_detection_vel_5d},
    "wyck_242_spring_detection_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_242_spring_detection_vel_21d},
    "wyck_243_spring_detection_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_243_spring_detection_vel_63d},
    "wyck_244_spring_detection_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_244_spring_detection_vel_126d},
    "wyck_245_spring_detection_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_245_spring_detection_vel_252d},
    "wyck_246_sign_of_weakness_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_246_sign_of_weakness_vel_5d},
    "wyck_247_sign_of_weakness_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_247_sign_of_weakness_vel_21d},
    "wyck_248_sign_of_weakness_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_248_sign_of_weakness_vel_63d},
    "wyck_249_sign_of_weakness_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_249_sign_of_weakness_vel_126d},
    "wyck_250_sign_of_weakness_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_250_sign_of_weakness_vel_252d},
    "wyck_251_supply_overcoming_demand_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_251_supply_overcoming_demand_vel_5d},
    "wyck_252_supply_overcoming_demand_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_252_supply_overcoming_demand_vel_21d},
    "wyck_253_supply_overcoming_demand_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_253_supply_overcoming_demand_vel_63d},
    "wyck_254_supply_overcoming_demand_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_254_supply_overcoming_demand_vel_126d},
    "wyck_255_supply_overcoming_demand_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_255_supply_overcoming_demand_vel_252d},
    "wyck_256_trading_range_position_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_256_trading_range_position_vel_5d},
    "wyck_257_trading_range_position_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_257_trading_range_position_vel_21d},
    "wyck_258_trading_range_position_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_258_trading_range_position_vel_63d},
    "wyck_259_trading_range_position_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_259_trading_range_position_vel_126d},
    "wyck_260_trading_range_position_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_260_trading_range_position_vel_252d},
    "wyck_261_volume_dry_up_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_261_volume_dry_up_vel_5d},
    "wyck_262_volume_dry_up_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_262_volume_dry_up_vel_21d},
    "wyck_263_volume_dry_up_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_263_volume_dry_up_vel_63d},
    "wyck_264_volume_dry_up_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_264_volume_dry_up_vel_126d},
    "wyck_265_volume_dry_up_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_265_volume_dry_up_vel_252d},
    "wyck_266_upthrust_detection_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_266_upthrust_detection_vel_5d},
    "wyck_267_upthrust_detection_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_267_upthrust_detection_vel_21d},
    "wyck_268_upthrust_detection_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_268_upthrust_detection_vel_63d},
    "wyck_269_upthrust_detection_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_269_upthrust_detection_vel_126d},
    "wyck_270_upthrust_detection_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_270_upthrust_detection_vel_252d},
    "wyck_271_preliminary_support_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_271_preliminary_support_vel_5d},
    "wyck_272_preliminary_support_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_272_preliminary_support_vel_21d},
    "wyck_273_preliminary_support_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_273_preliminary_support_vel_63d},
    "wyck_274_preliminary_support_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_274_preliminary_support_vel_126d},
    "wyck_275_preliminary_support_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_275_preliminary_support_vel_252d},
    "wyck_276_jump_across_creek_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_276_jump_across_creek_vel_5d},
    "wyck_277_jump_across_creek_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_277_jump_across_creek_vel_21d},
    "wyck_278_jump_across_creek_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_278_jump_across_creek_vel_63d},
    "wyck_279_jump_across_creek_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_279_jump_across_creek_vel_126d},
    "wyck_280_jump_across_creek_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_280_jump_across_creek_vel_252d},
    "wyck_281_last_point_of_supply_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_281_last_point_of_supply_vel_5d},
    "wyck_282_last_point_of_supply_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_282_last_point_of_supply_vel_21d},
    "wyck_283_last_point_of_supply_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_283_last_point_of_supply_vel_63d},
    "wyck_284_last_point_of_supply_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_284_last_point_of_supply_vel_126d},
    "wyck_285_last_point_of_supply_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_285_last_point_of_supply_vel_252d},
    "wyck_286_volume_price_divergence_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_286_volume_price_divergence_vel_5d},
    "wyck_287_volume_price_divergence_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_287_volume_price_divergence_vel_21d},
    "wyck_288_volume_price_divergence_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_288_volume_price_divergence_vel_63d},
    "wyck_289_volume_price_divergence_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_289_volume_price_divergence_vel_126d},
    "wyck_290_volume_price_divergence_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_290_volume_price_divergence_vel_252d},
    "wyck_291_effort_vs_result_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_291_effort_vs_result_vel_5d},
    "wyck_292_effort_vs_result_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_292_effort_vs_result_vel_21d},
    "wyck_293_effort_vs_result_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_293_effort_vs_result_vel_63d},
    "wyck_294_effort_vs_result_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_294_effort_vs_result_vel_126d},
    "wyck_295_effort_vs_result_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_295_effort_vs_result_vel_252d},
    "wyck_296_trend_channel_violation_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_296_trend_channel_violation_vel_5d},
    "wyck_297_trend_channel_violation_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_297_trend_channel_violation_vel_21d},
    "wyck_298_trend_channel_violation_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_298_trend_channel_violation_vel_63d},
    "wyck_299_trend_channel_violation_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_299_trend_channel_violation_vel_126d},
    "wyck_300_trend_channel_violation_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_300_trend_channel_violation_vel_252d},
}
