"""
115_volatility_term_structure — Velocity (2nd Derivatives)
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

def vts_226_vol_5d_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_226_vol_5d_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(5)

def vts_227_vol_5d_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_227_vol_5d_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(21)

def vts_228_vol_5d_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_228_vol_5d_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(63)

def vts_229_vol_5d_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_229_vol_5d_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(126)

def vts_230_vol_5d_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_230_vol_5d_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).diff(252)

def vts_231_vol_21d_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_231_vol_21d_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(5)

def vts_232_vol_21d_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_232_vol_21d_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(21)

def vts_233_vol_21d_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_233_vol_21d_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(63)

def vts_234_vol_21d_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_234_vol_21d_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(126)

def vts_235_vol_21d_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_235_vol_21d_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).diff(252)

def vts_236_vol_63d_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_236_vol_63d_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(5)

def vts_237_vol_63d_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_237_vol_63d_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(21)

def vts_238_vol_63d_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_238_vol_63d_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(63)

def vts_239_vol_63d_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_239_vol_63d_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(126)

def vts_240_vol_63d_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_240_vol_63d_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).diff(252)

def vts_241_vol_spread_short_long_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_241_vol_spread_short_long_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(5)

def vts_242_vol_spread_short_long_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_242_vol_spread_short_long_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(21)

def vts_243_vol_spread_short_long_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_243_vol_spread_short_long_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(63)

def vts_244_vol_spread_short_long_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_244_vol_spread_short_long_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(126)

def vts_245_vol_spread_short_long_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_245_vol_spread_short_long_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_spread_short_long. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).diff(252)

def vts_246_vol_term_slope_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_246_vol_term_slope_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(5)

def vts_247_vol_term_slope_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_247_vol_term_slope_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(21)

def vts_248_vol_term_slope_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_248_vol_term_slope_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(63)

def vts_249_vol_term_slope_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_249_vol_term_slope_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(126)

def vts_250_vol_term_slope_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_250_vol_term_slope_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_term_slope. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).diff(252)

def vts_251_vol_convexity_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_251_vol_convexity_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(5)

def vts_252_vol_convexity_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_252_vol_convexity_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(21)

def vts_253_vol_convexity_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_253_vol_convexity_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(63)

def vts_254_vol_convexity_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_254_vol_convexity_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(126)

def vts_255_vol_convexity_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_255_vol_convexity_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_convexity. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).diff(252)

def vts_256_vol_mean_reversion_speed_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_256_vol_mean_reversion_speed_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(5)

def vts_257_vol_mean_reversion_speed_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_257_vol_mean_reversion_speed_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(21)

def vts_258_vol_mean_reversion_speed_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_258_vol_mean_reversion_speed_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(63)

def vts_259_vol_mean_reversion_speed_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_259_vol_mean_reversion_speed_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(126)

def vts_260_vol_mean_reversion_speed_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_260_vol_mean_reversion_speed_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_mean_reversion_speed. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).diff(252)

def vts_261_vol_regime_z_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_261_vol_regime_z_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(5)

def vts_262_vol_regime_z_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_262_vol_regime_z_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(21)

def vts_263_vol_regime_z_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_263_vol_regime_z_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(63)

def vts_264_vol_regime_z_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_264_vol_regime_z_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(126)

def vts_265_vol_regime_z_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_265_vol_regime_z_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_regime_z. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).diff(252)

def vts_266_vol_acceleration_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_266_vol_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(5)

def vts_267_vol_acceleration_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_267_vol_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(21)

def vts_268_vol_acceleration_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_268_vol_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(63)

def vts_269_vol_acceleration_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_269_vol_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(126)

def vts_270_vol_acceleration_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_270_vol_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_acceleration. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).diff(252)

def vts_271_vol_of_vol_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_271_vol_of_vol_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(5)

def vts_272_vol_of_vol_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_272_vol_of_vol_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(21)

def vts_273_vol_of_vol_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_273_vol_of_vol_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(63)

def vts_274_vol_of_vol_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_274_vol_of_vol_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(126)

def vts_275_vol_of_vol_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_275_vol_of_vol_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_of_vol. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).diff(252)

def vts_276_vol_decay_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_276_vol_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(5)

def vts_277_vol_decay_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_277_vol_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(21)

def vts_278_vol_decay_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_278_vol_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(63)

def vts_279_vol_decay_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_279_vol_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(126)

def vts_280_vol_decay_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_280_vol_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_decay. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).diff(252)

def vts_281_vol_term_inversion_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_281_vol_term_inversion_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(5)

def vts_282_vol_term_inversion_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_282_vol_term_inversion_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(21)

def vts_283_vol_term_inversion_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_283_vol_term_inversion_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(63)

def vts_284_vol_term_inversion_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_284_vol_term_inversion_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(126)

def vts_285_vol_term_inversion_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_285_vol_term_inversion_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_term_inversion. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).diff(252)

def vts_286_vol_peak_dist_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_286_vol_peak_dist_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(5)

def vts_287_vol_peak_dist_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_287_vol_peak_dist_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(21)

def vts_288_vol_peak_dist_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_288_vol_peak_dist_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(63)

def vts_289_vol_peak_dist_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_289_vol_peak_dist_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(126)

def vts_290_vol_peak_dist_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_290_vol_peak_dist_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_peak_dist. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).diff(252)

def vts_291_vol_tail_spread_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_291_vol_tail_spread_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(5)

def vts_292_vol_tail_spread_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_292_vol_tail_spread_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(21)

def vts_293_vol_tail_spread_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_293_vol_tail_spread_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(63)

def vts_294_vol_tail_spread_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_294_vol_tail_spread_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(126)

def vts_295_vol_tail_spread_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_295_vol_tail_spread_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_tail_spread. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).diff(252)

def vts_296_vol_structural_stability_vel_5d(close: pd.Series) -> pd.Series:
    """
    vts_296_vol_structural_stability_vel_5d
    ECONOMIC RATIONALE: Velocity of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(5)

def vts_297_vol_structural_stability_vel_21d(close: pd.Series) -> pd.Series:
    """
    vts_297_vol_structural_stability_vel_21d
    ECONOMIC RATIONALE: Velocity of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(21)

def vts_298_vol_structural_stability_vel_63d(close: pd.Series) -> pd.Series:
    """
    vts_298_vol_structural_stability_vel_63d
    ECONOMIC RATIONALE: Velocity of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(63)

def vts_299_vol_structural_stability_vel_126d(close: pd.Series) -> pd.Series:
    """
    vts_299_vol_structural_stability_vel_126d
    ECONOMIC RATIONALE: Velocity of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(126)

def vts_300_vol_structural_stability_vel_252d(close: pd.Series) -> pd.Series:
    """
    vts_300_vol_structural_stability_vel_252d
    ECONOMIC RATIONALE: Velocity of vol_structural_stability. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V115_REGISTRY_VEL = {
    "vts_226_vol_5d_vel_5d": {"inputs": ["close"], "func": vts_226_vol_5d_vel_5d},
    "vts_227_vol_5d_vel_21d": {"inputs": ["close"], "func": vts_227_vol_5d_vel_21d},
    "vts_228_vol_5d_vel_63d": {"inputs": ["close"], "func": vts_228_vol_5d_vel_63d},
    "vts_229_vol_5d_vel_126d": {"inputs": ["close"], "func": vts_229_vol_5d_vel_126d},
    "vts_230_vol_5d_vel_252d": {"inputs": ["close"], "func": vts_230_vol_5d_vel_252d},
    "vts_231_vol_21d_vel_5d": {"inputs": ["close"], "func": vts_231_vol_21d_vel_5d},
    "vts_232_vol_21d_vel_21d": {"inputs": ["close"], "func": vts_232_vol_21d_vel_21d},
    "vts_233_vol_21d_vel_63d": {"inputs": ["close"], "func": vts_233_vol_21d_vel_63d},
    "vts_234_vol_21d_vel_126d": {"inputs": ["close"], "func": vts_234_vol_21d_vel_126d},
    "vts_235_vol_21d_vel_252d": {"inputs": ["close"], "func": vts_235_vol_21d_vel_252d},
    "vts_236_vol_63d_vel_5d": {"inputs": ["close"], "func": vts_236_vol_63d_vel_5d},
    "vts_237_vol_63d_vel_21d": {"inputs": ["close"], "func": vts_237_vol_63d_vel_21d},
    "vts_238_vol_63d_vel_63d": {"inputs": ["close"], "func": vts_238_vol_63d_vel_63d},
    "vts_239_vol_63d_vel_126d": {"inputs": ["close"], "func": vts_239_vol_63d_vel_126d},
    "vts_240_vol_63d_vel_252d": {"inputs": ["close"], "func": vts_240_vol_63d_vel_252d},
    "vts_241_vol_spread_short_long_vel_5d": {"inputs": ["close"], "func": vts_241_vol_spread_short_long_vel_5d},
    "vts_242_vol_spread_short_long_vel_21d": {"inputs": ["close"], "func": vts_242_vol_spread_short_long_vel_21d},
    "vts_243_vol_spread_short_long_vel_63d": {"inputs": ["close"], "func": vts_243_vol_spread_short_long_vel_63d},
    "vts_244_vol_spread_short_long_vel_126d": {"inputs": ["close"], "func": vts_244_vol_spread_short_long_vel_126d},
    "vts_245_vol_spread_short_long_vel_252d": {"inputs": ["close"], "func": vts_245_vol_spread_short_long_vel_252d},
    "vts_246_vol_term_slope_vel_5d": {"inputs": ["close"], "func": vts_246_vol_term_slope_vel_5d},
    "vts_247_vol_term_slope_vel_21d": {"inputs": ["close"], "func": vts_247_vol_term_slope_vel_21d},
    "vts_248_vol_term_slope_vel_63d": {"inputs": ["close"], "func": vts_248_vol_term_slope_vel_63d},
    "vts_249_vol_term_slope_vel_126d": {"inputs": ["close"], "func": vts_249_vol_term_slope_vel_126d},
    "vts_250_vol_term_slope_vel_252d": {"inputs": ["close"], "func": vts_250_vol_term_slope_vel_252d},
    "vts_251_vol_convexity_vel_5d": {"inputs": ["close"], "func": vts_251_vol_convexity_vel_5d},
    "vts_252_vol_convexity_vel_21d": {"inputs": ["close"], "func": vts_252_vol_convexity_vel_21d},
    "vts_253_vol_convexity_vel_63d": {"inputs": ["close"], "func": vts_253_vol_convexity_vel_63d},
    "vts_254_vol_convexity_vel_126d": {"inputs": ["close"], "func": vts_254_vol_convexity_vel_126d},
    "vts_255_vol_convexity_vel_252d": {"inputs": ["close"], "func": vts_255_vol_convexity_vel_252d},
    "vts_256_vol_mean_reversion_speed_vel_5d": {"inputs": ["close"], "func": vts_256_vol_mean_reversion_speed_vel_5d},
    "vts_257_vol_mean_reversion_speed_vel_21d": {"inputs": ["close"], "func": vts_257_vol_mean_reversion_speed_vel_21d},
    "vts_258_vol_mean_reversion_speed_vel_63d": {"inputs": ["close"], "func": vts_258_vol_mean_reversion_speed_vel_63d},
    "vts_259_vol_mean_reversion_speed_vel_126d": {"inputs": ["close"], "func": vts_259_vol_mean_reversion_speed_vel_126d},
    "vts_260_vol_mean_reversion_speed_vel_252d": {"inputs": ["close"], "func": vts_260_vol_mean_reversion_speed_vel_252d},
    "vts_261_vol_regime_z_vel_5d": {"inputs": ["close"], "func": vts_261_vol_regime_z_vel_5d},
    "vts_262_vol_regime_z_vel_21d": {"inputs": ["close"], "func": vts_262_vol_regime_z_vel_21d},
    "vts_263_vol_regime_z_vel_63d": {"inputs": ["close"], "func": vts_263_vol_regime_z_vel_63d},
    "vts_264_vol_regime_z_vel_126d": {"inputs": ["close"], "func": vts_264_vol_regime_z_vel_126d},
    "vts_265_vol_regime_z_vel_252d": {"inputs": ["close"], "func": vts_265_vol_regime_z_vel_252d},
    "vts_266_vol_acceleration_vel_5d": {"inputs": ["close"], "func": vts_266_vol_acceleration_vel_5d},
    "vts_267_vol_acceleration_vel_21d": {"inputs": ["close"], "func": vts_267_vol_acceleration_vel_21d},
    "vts_268_vol_acceleration_vel_63d": {"inputs": ["close"], "func": vts_268_vol_acceleration_vel_63d},
    "vts_269_vol_acceleration_vel_126d": {"inputs": ["close"], "func": vts_269_vol_acceleration_vel_126d},
    "vts_270_vol_acceleration_vel_252d": {"inputs": ["close"], "func": vts_270_vol_acceleration_vel_252d},
    "vts_271_vol_of_vol_vel_5d": {"inputs": ["close"], "func": vts_271_vol_of_vol_vel_5d},
    "vts_272_vol_of_vol_vel_21d": {"inputs": ["close"], "func": vts_272_vol_of_vol_vel_21d},
    "vts_273_vol_of_vol_vel_63d": {"inputs": ["close"], "func": vts_273_vol_of_vol_vel_63d},
    "vts_274_vol_of_vol_vel_126d": {"inputs": ["close"], "func": vts_274_vol_of_vol_vel_126d},
    "vts_275_vol_of_vol_vel_252d": {"inputs": ["close"], "func": vts_275_vol_of_vol_vel_252d},
    "vts_276_vol_decay_vel_5d": {"inputs": ["close"], "func": vts_276_vol_decay_vel_5d},
    "vts_277_vol_decay_vel_21d": {"inputs": ["close"], "func": vts_277_vol_decay_vel_21d},
    "vts_278_vol_decay_vel_63d": {"inputs": ["close"], "func": vts_278_vol_decay_vel_63d},
    "vts_279_vol_decay_vel_126d": {"inputs": ["close"], "func": vts_279_vol_decay_vel_126d},
    "vts_280_vol_decay_vel_252d": {"inputs": ["close"], "func": vts_280_vol_decay_vel_252d},
    "vts_281_vol_term_inversion_vel_5d": {"inputs": ["close"], "func": vts_281_vol_term_inversion_vel_5d},
    "vts_282_vol_term_inversion_vel_21d": {"inputs": ["close"], "func": vts_282_vol_term_inversion_vel_21d},
    "vts_283_vol_term_inversion_vel_63d": {"inputs": ["close"], "func": vts_283_vol_term_inversion_vel_63d},
    "vts_284_vol_term_inversion_vel_126d": {"inputs": ["close"], "func": vts_284_vol_term_inversion_vel_126d},
    "vts_285_vol_term_inversion_vel_252d": {"inputs": ["close"], "func": vts_285_vol_term_inversion_vel_252d},
    "vts_286_vol_peak_dist_vel_5d": {"inputs": ["close"], "func": vts_286_vol_peak_dist_vel_5d},
    "vts_287_vol_peak_dist_vel_21d": {"inputs": ["close"], "func": vts_287_vol_peak_dist_vel_21d},
    "vts_288_vol_peak_dist_vel_63d": {"inputs": ["close"], "func": vts_288_vol_peak_dist_vel_63d},
    "vts_289_vol_peak_dist_vel_126d": {"inputs": ["close"], "func": vts_289_vol_peak_dist_vel_126d},
    "vts_290_vol_peak_dist_vel_252d": {"inputs": ["close"], "func": vts_290_vol_peak_dist_vel_252d},
    "vts_291_vol_tail_spread_vel_5d": {"inputs": ["close"], "func": vts_291_vol_tail_spread_vel_5d},
    "vts_292_vol_tail_spread_vel_21d": {"inputs": ["close"], "func": vts_292_vol_tail_spread_vel_21d},
    "vts_293_vol_tail_spread_vel_63d": {"inputs": ["close"], "func": vts_293_vol_tail_spread_vel_63d},
    "vts_294_vol_tail_spread_vel_126d": {"inputs": ["close"], "func": vts_294_vol_tail_spread_vel_126d},
    "vts_295_vol_tail_spread_vel_252d": {"inputs": ["close"], "func": vts_295_vol_tail_spread_vel_252d},
    "vts_296_vol_structural_stability_vel_5d": {"inputs": ["close"], "func": vts_296_vol_structural_stability_vel_5d},
    "vts_297_vol_structural_stability_vel_21d": {"inputs": ["close"], "func": vts_297_vol_structural_stability_vel_21d},
    "vts_298_vol_structural_stability_vel_63d": {"inputs": ["close"], "func": vts_298_vol_structural_stability_vel_63d},
    "vts_299_vol_structural_stability_vel_126d": {"inputs": ["close"], "func": vts_299_vol_structural_stability_vel_126d},
    "vts_300_vol_structural_stability_vel_252d": {"inputs": ["close"], "func": vts_300_vol_structural_stability_vel_252d},
}
