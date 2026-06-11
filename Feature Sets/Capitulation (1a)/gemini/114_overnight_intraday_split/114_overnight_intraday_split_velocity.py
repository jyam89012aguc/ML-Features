"""
114_overnight_intraday_split — Velocity (2nd Derivatives)
Domain: overnight_intraday_split
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

def onid_226_overnight_return_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_226_overnight_return_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(5)

def onid_227_overnight_return_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_227_overnight_return_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(21)

def onid_228_overnight_return_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_228_overnight_return_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(63)

def onid_229_overnight_return_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_229_overnight_return_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(126)

def onid_230_overnight_return_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_230_overnight_return_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(252)

def onid_231_intraday_return_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_231_intraday_return_vel_5d
    ECONOMIC RATIONALE: Velocity of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(5)

def onid_232_intraday_return_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_232_intraday_return_vel_21d
    ECONOMIC RATIONALE: Velocity of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(21)

def onid_233_intraday_return_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_233_intraday_return_vel_63d
    ECONOMIC RATIONALE: Velocity of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(63)

def onid_234_intraday_return_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_234_intraday_return_vel_126d
    ECONOMIC RATIONALE: Velocity of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(126)

def onid_235_intraday_return_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_235_intraday_return_vel_252d
    ECONOMIC RATIONALE: Velocity of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(252)

def onid_236_on_id_divergence_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_236_on_id_divergence_vel_5d
    ECONOMIC RATIONALE: Velocity of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(5)

def onid_237_on_id_divergence_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_237_on_id_divergence_vel_21d
    ECONOMIC RATIONALE: Velocity of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(21)

def onid_238_on_id_divergence_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_238_on_id_divergence_vel_63d
    ECONOMIC RATIONALE: Velocity of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(63)

def onid_239_on_id_divergence_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_239_on_id_divergence_vel_126d
    ECONOMIC RATIONALE: Velocity of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(126)

def onid_240_on_id_divergence_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_240_on_id_divergence_vel_252d
    ECONOMIC RATIONALE: Velocity of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(252)

def onid_241_overnight_vol_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_241_overnight_vol_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(5)

def onid_242_overnight_vol_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_242_overnight_vol_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(21)

def onid_243_overnight_vol_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_243_overnight_vol_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(63)

def onid_244_overnight_vol_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_244_overnight_vol_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(126)

def onid_245_overnight_vol_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_245_overnight_vol_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(252)

def onid_246_intraday_vol_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_246_intraday_vol_vel_5d
    ECONOMIC RATIONALE: Velocity of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(5)

def onid_247_intraday_vol_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_247_intraday_vol_vel_21d
    ECONOMIC RATIONALE: Velocity of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(21)

def onid_248_intraday_vol_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_248_intraday_vol_vel_63d
    ECONOMIC RATIONALE: Velocity of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(63)

def onid_249_intraday_vol_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_249_intraday_vol_vel_126d
    ECONOMIC RATIONALE: Velocity of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(126)

def onid_250_intraday_vol_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_250_intraday_vol_vel_252d
    ECONOMIC RATIONALE: Velocity of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(252)

def onid_251_on_id_vol_ratio_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_251_on_id_vol_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(5)

def onid_252_on_id_vol_ratio_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_252_on_id_vol_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(21)

def onid_253_on_id_vol_ratio_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_253_on_id_vol_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(63)

def onid_254_on_id_vol_ratio_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_254_on_id_vol_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(126)

def onid_255_on_id_vol_ratio_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_255_on_id_vol_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(252)

def onid_256_overnight_bias_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_256_overnight_bias_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(5)

def onid_257_overnight_bias_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_257_overnight_bias_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(21)

def onid_258_overnight_bias_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_258_overnight_bias_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(63)

def onid_259_overnight_bias_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_259_overnight_bias_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(126)

def onid_260_overnight_bias_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_260_overnight_bias_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(252)

def onid_261_intraday_bias_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_261_intraday_bias_vel_5d
    ECONOMIC RATIONALE: Velocity of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(5)

def onid_262_intraday_bias_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_262_intraday_bias_vel_21d
    ECONOMIC RATIONALE: Velocity of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(21)

def onid_263_intraday_bias_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_263_intraday_bias_vel_63d
    ECONOMIC RATIONALE: Velocity of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(63)

def onid_264_intraday_bias_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_264_intraday_bias_vel_126d
    ECONOMIC RATIONALE: Velocity of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(126)

def onid_265_intraday_bias_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_265_intraday_bias_vel_252d
    ECONOMIC RATIONALE: Velocity of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(252)

def onid_266_gap_fade_potential_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_266_gap_fade_potential_vel_5d
    ECONOMIC RATIONALE: Velocity of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(5)

def onid_267_gap_fade_potential_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_267_gap_fade_potential_vel_21d
    ECONOMIC RATIONALE: Velocity of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(21)

def onid_268_gap_fade_potential_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_268_gap_fade_potential_vel_63d
    ECONOMIC RATIONALE: Velocity of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(63)

def onid_269_gap_fade_potential_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_269_gap_fade_potential_vel_126d
    ECONOMIC RATIONALE: Velocity of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(126)

def onid_270_gap_fade_potential_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_270_gap_fade_potential_vel_252d
    ECONOMIC RATIONALE: Velocity of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(252)

def onid_271_overnight_gap_z_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_271_overnight_gap_z_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(5)

def onid_272_overnight_gap_z_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_272_overnight_gap_z_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(21)

def onid_273_overnight_gap_z_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_273_overnight_gap_z_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(63)

def onid_274_overnight_gap_z_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_274_overnight_gap_z_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(126)

def onid_275_overnight_gap_z_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_275_overnight_gap_z_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(252)

def onid_276_intraday_range_pos_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_276_intraday_range_pos_vel_5d
    ECONOMIC RATIONALE: Velocity of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(5)

def onid_277_intraday_range_pos_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_277_intraday_range_pos_vel_21d
    ECONOMIC RATIONALE: Velocity of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(21)

def onid_278_intraday_range_pos_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_278_intraday_range_pos_vel_63d
    ECONOMIC RATIONALE: Velocity of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(63)

def onid_279_intraday_range_pos_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_279_intraday_range_pos_vel_126d
    ECONOMIC RATIONALE: Velocity of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(126)

def onid_280_intraday_range_pos_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_280_intraday_range_pos_vel_252d
    ECONOMIC RATIONALE: Velocity of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(252)

def onid_281_overnight_momentum_lead_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_281_overnight_momentum_lead_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(5)

def onid_282_overnight_momentum_lead_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_282_overnight_momentum_lead_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(21)

def onid_283_overnight_momentum_lead_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_283_overnight_momentum_lead_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(63)

def onid_284_overnight_momentum_lead_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_284_overnight_momentum_lead_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(126)

def onid_285_overnight_momentum_lead_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_285_overnight_momentum_lead_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(252)

def onid_286_id_reversal_strength_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_286_id_reversal_strength_vel_5d
    ECONOMIC RATIONALE: Velocity of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(5)

def onid_287_id_reversal_strength_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_287_id_reversal_strength_vel_21d
    ECONOMIC RATIONALE: Velocity of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(21)

def onid_288_id_reversal_strength_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_288_id_reversal_strength_vel_63d
    ECONOMIC RATIONALE: Velocity of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(63)

def onid_289_id_reversal_strength_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_289_id_reversal_strength_vel_126d
    ECONOMIC RATIONALE: Velocity of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(126)

def onid_290_id_reversal_strength_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_290_id_reversal_strength_vel_252d
    ECONOMIC RATIONALE: Velocity of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(252)

def onid_291_on_id_correlation_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_291_on_id_correlation_vel_5d
    ECONOMIC RATIONALE: Velocity of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(5)

def onid_292_on_id_correlation_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_292_on_id_correlation_vel_21d
    ECONOMIC RATIONALE: Velocity of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(21)

def onid_293_on_id_correlation_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_293_on_id_correlation_vel_63d
    ECONOMIC RATIONALE: Velocity of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(63)

def onid_294_on_id_correlation_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_294_on_id_correlation_vel_126d
    ECONOMIC RATIONALE: Velocity of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(126)

def onid_295_on_id_correlation_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_295_on_id_correlation_vel_252d
    ECONOMIC RATIONALE: Velocity of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(252)

def onid_296_overnight_shock_flag_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_296_overnight_shock_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(5)

def onid_297_overnight_shock_flag_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_297_overnight_shock_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(21)

def onid_298_overnight_shock_flag_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_298_overnight_shock_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(63)

def onid_299_overnight_shock_flag_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_299_overnight_shock_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(126)

def onid_300_overnight_shock_flag_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_300_overnight_shock_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V114_REGISTRY_VEL = {
    "onid_226_overnight_return_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_226_overnight_return_vel_5d},
    "onid_227_overnight_return_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_227_overnight_return_vel_21d},
    "onid_228_overnight_return_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_228_overnight_return_vel_63d},
    "onid_229_overnight_return_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_229_overnight_return_vel_126d},
    "onid_230_overnight_return_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_230_overnight_return_vel_252d},
    "onid_231_intraday_return_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_231_intraday_return_vel_5d},
    "onid_232_intraday_return_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_232_intraday_return_vel_21d},
    "onid_233_intraday_return_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_233_intraday_return_vel_63d},
    "onid_234_intraday_return_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_234_intraday_return_vel_126d},
    "onid_235_intraday_return_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_235_intraday_return_vel_252d},
    "onid_236_on_id_divergence_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_236_on_id_divergence_vel_5d},
    "onid_237_on_id_divergence_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_237_on_id_divergence_vel_21d},
    "onid_238_on_id_divergence_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_238_on_id_divergence_vel_63d},
    "onid_239_on_id_divergence_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_239_on_id_divergence_vel_126d},
    "onid_240_on_id_divergence_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_240_on_id_divergence_vel_252d},
    "onid_241_overnight_vol_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_241_overnight_vol_vel_5d},
    "onid_242_overnight_vol_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_242_overnight_vol_vel_21d},
    "onid_243_overnight_vol_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_243_overnight_vol_vel_63d},
    "onid_244_overnight_vol_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_244_overnight_vol_vel_126d},
    "onid_245_overnight_vol_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_245_overnight_vol_vel_252d},
    "onid_246_intraday_vol_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_246_intraday_vol_vel_5d},
    "onid_247_intraday_vol_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_247_intraday_vol_vel_21d},
    "onid_248_intraday_vol_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_248_intraday_vol_vel_63d},
    "onid_249_intraday_vol_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_249_intraday_vol_vel_126d},
    "onid_250_intraday_vol_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_250_intraday_vol_vel_252d},
    "onid_251_on_id_vol_ratio_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_251_on_id_vol_ratio_vel_5d},
    "onid_252_on_id_vol_ratio_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_252_on_id_vol_ratio_vel_21d},
    "onid_253_on_id_vol_ratio_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_253_on_id_vol_ratio_vel_63d},
    "onid_254_on_id_vol_ratio_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_254_on_id_vol_ratio_vel_126d},
    "onid_255_on_id_vol_ratio_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_255_on_id_vol_ratio_vel_252d},
    "onid_256_overnight_bias_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_256_overnight_bias_vel_5d},
    "onid_257_overnight_bias_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_257_overnight_bias_vel_21d},
    "onid_258_overnight_bias_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_258_overnight_bias_vel_63d},
    "onid_259_overnight_bias_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_259_overnight_bias_vel_126d},
    "onid_260_overnight_bias_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_260_overnight_bias_vel_252d},
    "onid_261_intraday_bias_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_261_intraday_bias_vel_5d},
    "onid_262_intraday_bias_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_262_intraday_bias_vel_21d},
    "onid_263_intraday_bias_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_263_intraday_bias_vel_63d},
    "onid_264_intraday_bias_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_264_intraday_bias_vel_126d},
    "onid_265_intraday_bias_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_265_intraday_bias_vel_252d},
    "onid_266_gap_fade_potential_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_266_gap_fade_potential_vel_5d},
    "onid_267_gap_fade_potential_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_267_gap_fade_potential_vel_21d},
    "onid_268_gap_fade_potential_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_268_gap_fade_potential_vel_63d},
    "onid_269_gap_fade_potential_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_269_gap_fade_potential_vel_126d},
    "onid_270_gap_fade_potential_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_270_gap_fade_potential_vel_252d},
    "onid_271_overnight_gap_z_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_271_overnight_gap_z_vel_5d},
    "onid_272_overnight_gap_z_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_272_overnight_gap_z_vel_21d},
    "onid_273_overnight_gap_z_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_273_overnight_gap_z_vel_63d},
    "onid_274_overnight_gap_z_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_274_overnight_gap_z_vel_126d},
    "onid_275_overnight_gap_z_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_275_overnight_gap_z_vel_252d},
    "onid_276_intraday_range_pos_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_276_intraday_range_pos_vel_5d},
    "onid_277_intraday_range_pos_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_277_intraday_range_pos_vel_21d},
    "onid_278_intraday_range_pos_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_278_intraday_range_pos_vel_63d},
    "onid_279_intraday_range_pos_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_279_intraday_range_pos_vel_126d},
    "onid_280_intraday_range_pos_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_280_intraday_range_pos_vel_252d},
    "onid_281_overnight_momentum_lead_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_281_overnight_momentum_lead_vel_5d},
    "onid_282_overnight_momentum_lead_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_282_overnight_momentum_lead_vel_21d},
    "onid_283_overnight_momentum_lead_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_283_overnight_momentum_lead_vel_63d},
    "onid_284_overnight_momentum_lead_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_284_overnight_momentum_lead_vel_126d},
    "onid_285_overnight_momentum_lead_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_285_overnight_momentum_lead_vel_252d},
    "onid_286_id_reversal_strength_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_286_id_reversal_strength_vel_5d},
    "onid_287_id_reversal_strength_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_287_id_reversal_strength_vel_21d},
    "onid_288_id_reversal_strength_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_288_id_reversal_strength_vel_63d},
    "onid_289_id_reversal_strength_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_289_id_reversal_strength_vel_126d},
    "onid_290_id_reversal_strength_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_290_id_reversal_strength_vel_252d},
    "onid_291_on_id_correlation_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_291_on_id_correlation_vel_5d},
    "onid_292_on_id_correlation_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_292_on_id_correlation_vel_21d},
    "onid_293_on_id_correlation_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_293_on_id_correlation_vel_63d},
    "onid_294_on_id_correlation_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_294_on_id_correlation_vel_126d},
    "onid_295_on_id_correlation_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_295_on_id_correlation_vel_252d},
    "onid_296_overnight_shock_flag_vel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_296_overnight_shock_flag_vel_5d},
    "onid_297_overnight_shock_flag_vel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_297_overnight_shock_flag_vel_21d},
    "onid_298_overnight_shock_flag_vel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_298_overnight_shock_flag_vel_63d},
    "onid_299_overnight_shock_flag_vel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_299_overnight_shock_flag_vel_126d},
    "onid_300_overnight_shock_flag_vel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_300_overnight_shock_flag_vel_252d},
}
