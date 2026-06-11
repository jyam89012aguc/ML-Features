"""
106_support_violation — Velocity (2nd Derivatives)
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

def supv_226_support_252d_break_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_226_support_252d_break_vel_5d
    ECONOMIC RATIONALE: Velocity of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(5)

def supv_227_support_252d_break_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_227_support_252d_break_vel_21d
    ECONOMIC RATIONALE: Velocity of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(21)

def supv_228_support_252d_break_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_228_support_252d_break_vel_63d
    ECONOMIC RATIONALE: Velocity of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(63)

def supv_229_support_252d_break_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_229_support_252d_break_vel_126d
    ECONOMIC RATIONALE: Velocity of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(126)

def supv_230_support_252d_break_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_230_support_252d_break_vel_252d
    ECONOMIC RATIONALE: Velocity of support_252d_break. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).diff(252)

def supv_231_support_63d_break_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_231_support_63d_break_vel_5d
    ECONOMIC RATIONALE: Velocity of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(5)

def supv_232_support_63d_break_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_232_support_63d_break_vel_21d
    ECONOMIC RATIONALE: Velocity of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(21)

def supv_233_support_63d_break_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_233_support_63d_break_vel_63d
    ECONOMIC RATIONALE: Velocity of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(63)

def supv_234_support_63d_break_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_234_support_63d_break_vel_126d
    ECONOMIC RATIONALE: Velocity of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(126)

def supv_235_support_63d_break_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_235_support_63d_break_vel_252d
    ECONOMIC RATIONALE: Velocity of support_63d_break. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).diff(252)

def supv_236_volume_on_breakout_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_236_volume_on_breakout_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(5)

def supv_237_volume_on_breakout_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_237_volume_on_breakout_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(21)

def supv_238_volume_on_breakout_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_238_volume_on_breakout_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(63)

def supv_239_volume_on_breakout_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_239_volume_on_breakout_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(126)

def supv_240_volume_on_breakout_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_240_volume_on_breakout_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_on_breakout. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).diff(252)

def supv_241_support_proximity_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_241_support_proximity_vel_5d
    ECONOMIC RATIONALE: Velocity of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(5)

def supv_242_support_proximity_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_242_support_proximity_vel_21d
    ECONOMIC RATIONALE: Velocity of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(21)

def supv_243_support_proximity_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_243_support_proximity_vel_63d
    ECONOMIC RATIONALE: Velocity of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(63)

def supv_244_support_proximity_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_244_support_proximity_vel_126d
    ECONOMIC RATIONALE: Velocity of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(126)

def supv_245_support_proximity_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_245_support_proximity_vel_252d
    ECONOMIC RATIONALE: Velocity of support_proximity. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).diff(252)

def supv_246_support_bounce_failure_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_246_support_bounce_failure_vel_5d
    ECONOMIC RATIONALE: Velocity of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(5)

def supv_247_support_bounce_failure_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_247_support_bounce_failure_vel_21d
    ECONOMIC RATIONALE: Velocity of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(21)

def supv_248_support_bounce_failure_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_248_support_bounce_failure_vel_63d
    ECONOMIC RATIONALE: Velocity of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(63)

def supv_249_support_bounce_failure_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_249_support_bounce_failure_vel_126d
    ECONOMIC RATIONALE: Velocity of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(126)

def supv_250_support_bounce_failure_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_250_support_bounce_failure_vel_252d
    ECONOMIC RATIONALE: Velocity of support_bounce_failure. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).diff(252)

def supv_251_multiple_support_test_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_251_multiple_support_test_vel_5d
    ECONOMIC RATIONALE: Velocity of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(5)

def supv_252_multiple_support_test_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_252_multiple_support_test_vel_21d
    ECONOMIC RATIONALE: Velocity of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(21)

def supv_253_multiple_support_test_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_253_multiple_support_test_vel_63d
    ECONOMIC RATIONALE: Velocity of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(63)

def supv_254_multiple_support_test_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_254_multiple_support_test_vel_126d
    ECONOMIC RATIONALE: Velocity of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(126)

def supv_255_multiple_support_test_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_255_multiple_support_test_vel_252d
    ECONOMIC RATIONALE: Velocity of multiple_support_test. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).diff(252)

def supv_256_support_zone_density_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_256_support_zone_density_vel_5d
    ECONOMIC RATIONALE: Velocity of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(5)

def supv_257_support_zone_density_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_257_support_zone_density_vel_21d
    ECONOMIC RATIONALE: Velocity of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(21)

def supv_258_support_zone_density_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_258_support_zone_density_vel_63d
    ECONOMIC RATIONALE: Velocity of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(63)

def supv_259_support_zone_density_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_259_support_zone_density_vel_126d
    ECONOMIC RATIONALE: Velocity of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(126)

def supv_260_support_zone_density_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_260_support_zone_density_vel_252d
    ECONOMIC RATIONALE: Velocity of support_zone_density. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).diff(252)

def supv_261_breakdown_momentum_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_261_breakdown_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(5)

def supv_262_breakdown_momentum_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_262_breakdown_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(21)

def supv_263_breakdown_momentum_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_263_breakdown_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(63)

def supv_264_breakdown_momentum_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_264_breakdown_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(126)

def supv_265_breakdown_momentum_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_265_breakdown_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of breakdown_momentum. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).diff(252)

def supv_266_support_reversal_trap_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_266_support_reversal_trap_vel_5d
    ECONOMIC RATIONALE: Velocity of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(5)

def supv_267_support_reversal_trap_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_267_support_reversal_trap_vel_21d
    ECONOMIC RATIONALE: Velocity of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(21)

def supv_268_support_reversal_trap_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_268_support_reversal_trap_vel_63d
    ECONOMIC RATIONALE: Velocity of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(63)

def supv_269_support_reversal_trap_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_269_support_reversal_trap_vel_126d
    ECONOMIC RATIONALE: Velocity of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(126)

def supv_270_support_reversal_trap_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_270_support_reversal_trap_vel_252d
    ECONOMIC RATIONALE: Velocity of support_reversal_trap. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).diff(252)

def supv_271_support_gap_down_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_271_support_gap_down_vel_5d
    ECONOMIC RATIONALE: Velocity of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(5)

def supv_272_support_gap_down_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_272_support_gap_down_vel_21d
    ECONOMIC RATIONALE: Velocity of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(21)

def supv_273_support_gap_down_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_273_support_gap_down_vel_63d
    ECONOMIC RATIONALE: Velocity of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(63)

def supv_274_support_gap_down_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_274_support_gap_down_vel_126d
    ECONOMIC RATIONALE: Velocity of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(126)

def supv_275_support_gap_down_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_275_support_gap_down_vel_252d
    ECONOMIC RATIONALE: Velocity of support_gap_down. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).diff(252)

def supv_276_psychological_support_100_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_276_psychological_support_100_vel_5d
    ECONOMIC RATIONALE: Velocity of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(5)

def supv_277_psychological_support_100_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_277_psychological_support_100_vel_21d
    ECONOMIC RATIONALE: Velocity of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(21)

def supv_278_psychological_support_100_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_278_psychological_support_100_vel_63d
    ECONOMIC RATIONALE: Velocity of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(63)

def supv_279_psychological_support_100_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_279_psychological_support_100_vel_126d
    ECONOMIC RATIONALE: Velocity of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(126)

def supv_280_psychological_support_100_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_280_psychological_support_100_vel_252d
    ECONOMIC RATIONALE: Velocity of psychological_support_100. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).diff(252)

def supv_281_support_vol_z_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_281_support_vol_z_vel_5d
    ECONOMIC RATIONALE: Velocity of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(5)

def supv_282_support_vol_z_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_282_support_vol_z_vel_21d
    ECONOMIC RATIONALE: Velocity of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(21)

def supv_283_support_vol_z_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_283_support_vol_z_vel_63d
    ECONOMIC RATIONALE: Velocity of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(63)

def supv_284_support_vol_z_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_284_support_vol_z_vel_126d
    ECONOMIC RATIONALE: Velocity of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(126)

def supv_285_support_vol_z_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_285_support_vol_z_vel_252d
    ECONOMIC RATIONALE: Velocity of support_vol_z. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).diff(252)

def supv_286_structural_breakdown_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_286_structural_breakdown_vel_5d
    ECONOMIC RATIONALE: Velocity of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(5)

def supv_287_structural_breakdown_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_287_structural_breakdown_vel_21d
    ECONOMIC RATIONALE: Velocity of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(21)

def supv_288_structural_breakdown_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_288_structural_breakdown_vel_63d
    ECONOMIC RATIONALE: Velocity of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(63)

def supv_289_structural_breakdown_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_289_structural_breakdown_vel_126d
    ECONOMIC RATIONALE: Velocity of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(126)

def supv_290_structural_breakdown_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_290_structural_breakdown_vel_252d
    ECONOMIC RATIONALE: Velocity of structural_breakdown. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).diff(252)

def supv_291_support_recovery_rate_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_291_support_recovery_rate_vel_5d
    ECONOMIC RATIONALE: Velocity of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(5)

def supv_292_support_recovery_rate_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_292_support_recovery_rate_vel_21d
    ECONOMIC RATIONALE: Velocity of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(21)

def supv_293_support_recovery_rate_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_293_support_recovery_rate_vel_63d
    ECONOMIC RATIONALE: Velocity of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(63)

def supv_294_support_recovery_rate_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_294_support_recovery_rate_vel_126d
    ECONOMIC RATIONALE: Velocity of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(126)

def supv_295_support_recovery_rate_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_295_support_recovery_rate_vel_252d
    ECONOMIC RATIONALE: Velocity of support_recovery_rate. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).diff(252)

def supv_296_support_cascade_risk_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_296_support_cascade_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(5)

def supv_297_support_cascade_risk_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_297_support_cascade_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(21)

def supv_298_support_cascade_risk_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_298_support_cascade_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(63)

def supv_299_support_cascade_risk_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_299_support_cascade_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(126)

def supv_300_support_cascade_risk_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_300_support_cascade_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of support_cascade_risk. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V106_REGISTRY_VEL = {
    "supv_226_support_252d_break_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_226_support_252d_break_vel_5d},
    "supv_227_support_252d_break_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_227_support_252d_break_vel_21d},
    "supv_228_support_252d_break_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_228_support_252d_break_vel_63d},
    "supv_229_support_252d_break_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_229_support_252d_break_vel_126d},
    "supv_230_support_252d_break_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_230_support_252d_break_vel_252d},
    "supv_231_support_63d_break_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_231_support_63d_break_vel_5d},
    "supv_232_support_63d_break_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_232_support_63d_break_vel_21d},
    "supv_233_support_63d_break_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_233_support_63d_break_vel_63d},
    "supv_234_support_63d_break_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_234_support_63d_break_vel_126d},
    "supv_235_support_63d_break_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_235_support_63d_break_vel_252d},
    "supv_236_volume_on_breakout_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_236_volume_on_breakout_vel_5d},
    "supv_237_volume_on_breakout_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_237_volume_on_breakout_vel_21d},
    "supv_238_volume_on_breakout_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_238_volume_on_breakout_vel_63d},
    "supv_239_volume_on_breakout_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_239_volume_on_breakout_vel_126d},
    "supv_240_volume_on_breakout_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_240_volume_on_breakout_vel_252d},
    "supv_241_support_proximity_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_241_support_proximity_vel_5d},
    "supv_242_support_proximity_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_242_support_proximity_vel_21d},
    "supv_243_support_proximity_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_243_support_proximity_vel_63d},
    "supv_244_support_proximity_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_244_support_proximity_vel_126d},
    "supv_245_support_proximity_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_245_support_proximity_vel_252d},
    "supv_246_support_bounce_failure_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_246_support_bounce_failure_vel_5d},
    "supv_247_support_bounce_failure_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_247_support_bounce_failure_vel_21d},
    "supv_248_support_bounce_failure_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_248_support_bounce_failure_vel_63d},
    "supv_249_support_bounce_failure_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_249_support_bounce_failure_vel_126d},
    "supv_250_support_bounce_failure_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_250_support_bounce_failure_vel_252d},
    "supv_251_multiple_support_test_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_251_multiple_support_test_vel_5d},
    "supv_252_multiple_support_test_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_252_multiple_support_test_vel_21d},
    "supv_253_multiple_support_test_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_253_multiple_support_test_vel_63d},
    "supv_254_multiple_support_test_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_254_multiple_support_test_vel_126d},
    "supv_255_multiple_support_test_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_255_multiple_support_test_vel_252d},
    "supv_256_support_zone_density_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_256_support_zone_density_vel_5d},
    "supv_257_support_zone_density_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_257_support_zone_density_vel_21d},
    "supv_258_support_zone_density_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_258_support_zone_density_vel_63d},
    "supv_259_support_zone_density_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_259_support_zone_density_vel_126d},
    "supv_260_support_zone_density_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_260_support_zone_density_vel_252d},
    "supv_261_breakdown_momentum_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_261_breakdown_momentum_vel_5d},
    "supv_262_breakdown_momentum_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_262_breakdown_momentum_vel_21d},
    "supv_263_breakdown_momentum_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_263_breakdown_momentum_vel_63d},
    "supv_264_breakdown_momentum_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_264_breakdown_momentum_vel_126d},
    "supv_265_breakdown_momentum_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_265_breakdown_momentum_vel_252d},
    "supv_266_support_reversal_trap_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_266_support_reversal_trap_vel_5d},
    "supv_267_support_reversal_trap_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_267_support_reversal_trap_vel_21d},
    "supv_268_support_reversal_trap_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_268_support_reversal_trap_vel_63d},
    "supv_269_support_reversal_trap_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_269_support_reversal_trap_vel_126d},
    "supv_270_support_reversal_trap_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_270_support_reversal_trap_vel_252d},
    "supv_271_support_gap_down_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_271_support_gap_down_vel_5d},
    "supv_272_support_gap_down_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_272_support_gap_down_vel_21d},
    "supv_273_support_gap_down_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_273_support_gap_down_vel_63d},
    "supv_274_support_gap_down_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_274_support_gap_down_vel_126d},
    "supv_275_support_gap_down_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_275_support_gap_down_vel_252d},
    "supv_276_psychological_support_100_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_276_psychological_support_100_vel_5d},
    "supv_277_psychological_support_100_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_277_psychological_support_100_vel_21d},
    "supv_278_psychological_support_100_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_278_psychological_support_100_vel_63d},
    "supv_279_psychological_support_100_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_279_psychological_support_100_vel_126d},
    "supv_280_psychological_support_100_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_280_psychological_support_100_vel_252d},
    "supv_281_support_vol_z_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_281_support_vol_z_vel_5d},
    "supv_282_support_vol_z_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_282_support_vol_z_vel_21d},
    "supv_283_support_vol_z_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_283_support_vol_z_vel_63d},
    "supv_284_support_vol_z_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_284_support_vol_z_vel_126d},
    "supv_285_support_vol_z_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_285_support_vol_z_vel_252d},
    "supv_286_structural_breakdown_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_286_structural_breakdown_vel_5d},
    "supv_287_structural_breakdown_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_287_structural_breakdown_vel_21d},
    "supv_288_structural_breakdown_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_288_structural_breakdown_vel_63d},
    "supv_289_structural_breakdown_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_289_structural_breakdown_vel_126d},
    "supv_290_structural_breakdown_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_290_structural_breakdown_vel_252d},
    "supv_291_support_recovery_rate_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_291_support_recovery_rate_vel_5d},
    "supv_292_support_recovery_rate_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_292_support_recovery_rate_vel_21d},
    "supv_293_support_recovery_rate_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_293_support_recovery_rate_vel_63d},
    "supv_294_support_recovery_rate_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_294_support_recovery_rate_vel_126d},
    "supv_295_support_recovery_rate_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_295_support_recovery_rate_vel_252d},
    "supv_296_support_cascade_risk_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_296_support_cascade_risk_vel_5d},
    "supv_297_support_cascade_risk_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_297_support_cascade_risk_vel_21d},
    "supv_298_support_cascade_risk_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_298_support_cascade_risk_vel_63d},
    "supv_299_support_cascade_risk_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_299_support_cascade_risk_vel_126d},
    "supv_300_support_cascade_risk_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_300_support_cascade_risk_vel_252d},
}
