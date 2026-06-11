"""
112_volume_at_price — Velocity (2nd Derivatives)
Domain: volume_at_price
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

def vapr_226_volume_poc_dist_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_226_volume_poc_dist_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(5)

def vapr_227_volume_poc_dist_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_227_volume_poc_dist_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(21)

def vapr_228_volume_poc_dist_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_228_volume_poc_dist_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(63)

def vapr_229_volume_poc_dist_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_229_volume_poc_dist_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(126)

def vapr_230_volume_poc_dist_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_230_volume_poc_dist_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(252)

def vapr_231_value_area_high_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_231_value_area_high_vel_5d
    ECONOMIC RATIONALE: Velocity of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(5)

def vapr_232_value_area_high_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_232_value_area_high_vel_21d
    ECONOMIC RATIONALE: Velocity of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(21)

def vapr_233_value_area_high_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_233_value_area_high_vel_63d
    ECONOMIC RATIONALE: Velocity of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(63)

def vapr_234_value_area_high_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_234_value_area_high_vel_126d
    ECONOMIC RATIONALE: Velocity of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(126)

def vapr_235_value_area_high_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_235_value_area_high_vel_252d
    ECONOMIC RATIONALE: Velocity of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(252)

def vapr_236_value_area_low_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_236_value_area_low_vel_5d
    ECONOMIC RATIONALE: Velocity of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(5)

def vapr_237_value_area_low_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_237_value_area_low_vel_21d
    ECONOMIC RATIONALE: Velocity of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(21)

def vapr_238_value_area_low_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_238_value_area_low_vel_63d
    ECONOMIC RATIONALE: Velocity of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(63)

def vapr_239_value_area_low_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_239_value_area_low_vel_126d
    ECONOMIC RATIONALE: Velocity of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(126)

def vapr_240_value_area_low_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_240_value_area_low_vel_252d
    ECONOMIC RATIONALE: Velocity of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(252)

def vapr_241_high_volume_node_dist_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_241_high_volume_node_dist_vel_5d
    ECONOMIC RATIONALE: Velocity of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(5)

def vapr_242_high_volume_node_dist_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_242_high_volume_node_dist_vel_21d
    ECONOMIC RATIONALE: Velocity of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(21)

def vapr_243_high_volume_node_dist_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_243_high_volume_node_dist_vel_63d
    ECONOMIC RATIONALE: Velocity of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(63)

def vapr_244_high_volume_node_dist_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_244_high_volume_node_dist_vel_126d
    ECONOMIC RATIONALE: Velocity of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(126)

def vapr_245_high_volume_node_dist_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_245_high_volume_node_dist_vel_252d
    ECONOMIC RATIONALE: Velocity of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(252)

def vapr_246_low_volume_node_flag_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_246_low_volume_node_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(5)

def vapr_247_low_volume_node_flag_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_247_low_volume_node_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(21)

def vapr_248_low_volume_node_flag_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_248_low_volume_node_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(63)

def vapr_249_low_volume_node_flag_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_249_low_volume_node_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(126)

def vapr_250_low_volume_node_flag_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_250_low_volume_node_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(252)

def vapr_251_volume_skew_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_251_volume_skew_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(5)

def vapr_252_volume_skew_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_252_volume_skew_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(21)

def vapr_253_volume_skew_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_253_volume_skew_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(63)

def vapr_254_volume_skew_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_254_volume_skew_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(126)

def vapr_255_volume_skew_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_255_volume_skew_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(252)

def vapr_256_vapr_zscore_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_256_vapr_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(5)

def vapr_257_vapr_zscore_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_257_vapr_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(21)

def vapr_258_vapr_zscore_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_258_vapr_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(63)

def vapr_259_vapr_zscore_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_259_vapr_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(126)

def vapr_260_vapr_zscore_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_260_vapr_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(252)

def vapr_261_volume_concentration_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_261_volume_concentration_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(5)

def vapr_262_volume_concentration_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_262_volume_concentration_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(21)

def vapr_263_volume_concentration_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_263_volume_concentration_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(63)

def vapr_264_volume_concentration_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_264_volume_concentration_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(126)

def vapr_265_volume_concentration_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_265_volume_concentration_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(252)

def vapr_266_price_volume_overlap_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_266_price_volume_overlap_vel_5d
    ECONOMIC RATIONALE: Velocity of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(5)

def vapr_267_price_volume_overlap_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_267_price_volume_overlap_vel_21d
    ECONOMIC RATIONALE: Velocity of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(21)

def vapr_268_price_volume_overlap_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_268_price_volume_overlap_vel_63d
    ECONOMIC RATIONALE: Velocity of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(63)

def vapr_269_price_volume_overlap_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_269_price_volume_overlap_vel_126d
    ECONOMIC RATIONALE: Velocity of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(126)

def vapr_270_price_volume_overlap_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_270_price_volume_overlap_vel_252d
    ECONOMIC RATIONALE: Velocity of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(252)

def vapr_271_vapr_momentum_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_271_vapr_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(5)

def vapr_272_vapr_momentum_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_272_vapr_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(21)

def vapr_273_vapr_momentum_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_273_vapr_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(63)

def vapr_274_vapr_momentum_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_274_vapr_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(126)

def vapr_275_vapr_momentum_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_275_vapr_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(252)

def vapr_276_vapr_exhaustion_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_276_vapr_exhaustion_vel_5d
    ECONOMIC RATIONALE: Velocity of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(5)

def vapr_277_vapr_exhaustion_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_277_vapr_exhaustion_vel_21d
    ECONOMIC RATIONALE: Velocity of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(21)

def vapr_278_vapr_exhaustion_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_278_vapr_exhaustion_vel_63d
    ECONOMIC RATIONALE: Velocity of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(63)

def vapr_279_vapr_exhaustion_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_279_vapr_exhaustion_vel_126d
    ECONOMIC RATIONALE: Velocity of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(126)

def vapr_280_vapr_exhaustion_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_280_vapr_exhaustion_vel_252d
    ECONOMIC RATIONALE: Velocity of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(252)

def vapr_281_support_volume_strength_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_281_support_volume_strength_vel_5d
    ECONOMIC RATIONALE: Velocity of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(5)

def vapr_282_support_volume_strength_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_282_support_volume_strength_vel_21d
    ECONOMIC RATIONALE: Velocity of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(21)

def vapr_283_support_volume_strength_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_283_support_volume_strength_vel_63d
    ECONOMIC RATIONALE: Velocity of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(63)

def vapr_284_support_volume_strength_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_284_support_volume_strength_vel_126d
    ECONOMIC RATIONALE: Velocity of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(126)

def vapr_285_support_volume_strength_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_285_support_volume_strength_vel_252d
    ECONOMIC RATIONALE: Velocity of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(252)

def vapr_286_resistance_volume_strength_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_286_resistance_volume_strength_vel_5d
    ECONOMIC RATIONALE: Velocity of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(5)

def vapr_287_resistance_volume_strength_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_287_resistance_volume_strength_vel_21d
    ECONOMIC RATIONALE: Velocity of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(21)

def vapr_288_resistance_volume_strength_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_288_resistance_volume_strength_vel_63d
    ECONOMIC RATIONALE: Velocity of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(63)

def vapr_289_resistance_volume_strength_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_289_resistance_volume_strength_vel_126d
    ECONOMIC RATIONALE: Velocity of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(126)

def vapr_290_resistance_volume_strength_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_290_resistance_volume_strength_vel_252d
    ECONOMIC RATIONALE: Velocity of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(252)

def vapr_291_vapr_regime_shift_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_291_vapr_regime_shift_vel_5d
    ECONOMIC RATIONALE: Velocity of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(5)

def vapr_292_vapr_regime_shift_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_292_vapr_regime_shift_vel_21d
    ECONOMIC RATIONALE: Velocity of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(21)

def vapr_293_vapr_regime_shift_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_293_vapr_regime_shift_vel_63d
    ECONOMIC RATIONALE: Velocity of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(63)

def vapr_294_vapr_regime_shift_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_294_vapr_regime_shift_vel_126d
    ECONOMIC RATIONALE: Velocity of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(126)

def vapr_295_vapr_regime_shift_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_295_vapr_regime_shift_vel_252d
    ECONOMIC RATIONALE: Velocity of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(252)

def vapr_296_vapr_tail_volume_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_296_vapr_tail_volume_vel_5d
    ECONOMIC RATIONALE: Velocity of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(5)

def vapr_297_vapr_tail_volume_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_297_vapr_tail_volume_vel_21d
    ECONOMIC RATIONALE: Velocity of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(21)

def vapr_298_vapr_tail_volume_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_298_vapr_tail_volume_vel_63d
    ECONOMIC RATIONALE: Velocity of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(63)

def vapr_299_vapr_tail_volume_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_299_vapr_tail_volume_vel_126d
    ECONOMIC RATIONALE: Velocity of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(126)

def vapr_300_vapr_tail_volume_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_300_vapr_tail_volume_vel_252d
    ECONOMIC RATIONALE: Velocity of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V112_REGISTRY_VEL = {
    "vapr_226_volume_poc_dist_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_226_volume_poc_dist_vel_5d},
    "vapr_227_volume_poc_dist_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_227_volume_poc_dist_vel_21d},
    "vapr_228_volume_poc_dist_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_228_volume_poc_dist_vel_63d},
    "vapr_229_volume_poc_dist_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_229_volume_poc_dist_vel_126d},
    "vapr_230_volume_poc_dist_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_230_volume_poc_dist_vel_252d},
    "vapr_231_value_area_high_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_231_value_area_high_vel_5d},
    "vapr_232_value_area_high_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_232_value_area_high_vel_21d},
    "vapr_233_value_area_high_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_233_value_area_high_vel_63d},
    "vapr_234_value_area_high_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_234_value_area_high_vel_126d},
    "vapr_235_value_area_high_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_235_value_area_high_vel_252d},
    "vapr_236_value_area_low_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_236_value_area_low_vel_5d},
    "vapr_237_value_area_low_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_237_value_area_low_vel_21d},
    "vapr_238_value_area_low_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_238_value_area_low_vel_63d},
    "vapr_239_value_area_low_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_239_value_area_low_vel_126d},
    "vapr_240_value_area_low_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_240_value_area_low_vel_252d},
    "vapr_241_high_volume_node_dist_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_241_high_volume_node_dist_vel_5d},
    "vapr_242_high_volume_node_dist_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_242_high_volume_node_dist_vel_21d},
    "vapr_243_high_volume_node_dist_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_243_high_volume_node_dist_vel_63d},
    "vapr_244_high_volume_node_dist_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_244_high_volume_node_dist_vel_126d},
    "vapr_245_high_volume_node_dist_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_245_high_volume_node_dist_vel_252d},
    "vapr_246_low_volume_node_flag_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_246_low_volume_node_flag_vel_5d},
    "vapr_247_low_volume_node_flag_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_247_low_volume_node_flag_vel_21d},
    "vapr_248_low_volume_node_flag_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_248_low_volume_node_flag_vel_63d},
    "vapr_249_low_volume_node_flag_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_249_low_volume_node_flag_vel_126d},
    "vapr_250_low_volume_node_flag_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_250_low_volume_node_flag_vel_252d},
    "vapr_251_volume_skew_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_251_volume_skew_vel_5d},
    "vapr_252_volume_skew_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_252_volume_skew_vel_21d},
    "vapr_253_volume_skew_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_253_volume_skew_vel_63d},
    "vapr_254_volume_skew_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_254_volume_skew_vel_126d},
    "vapr_255_volume_skew_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_255_volume_skew_vel_252d},
    "vapr_256_vapr_zscore_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_256_vapr_zscore_vel_5d},
    "vapr_257_vapr_zscore_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_257_vapr_zscore_vel_21d},
    "vapr_258_vapr_zscore_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_258_vapr_zscore_vel_63d},
    "vapr_259_vapr_zscore_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_259_vapr_zscore_vel_126d},
    "vapr_260_vapr_zscore_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_260_vapr_zscore_vel_252d},
    "vapr_261_volume_concentration_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_261_volume_concentration_vel_5d},
    "vapr_262_volume_concentration_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_262_volume_concentration_vel_21d},
    "vapr_263_volume_concentration_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_263_volume_concentration_vel_63d},
    "vapr_264_volume_concentration_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_264_volume_concentration_vel_126d},
    "vapr_265_volume_concentration_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_265_volume_concentration_vel_252d},
    "vapr_266_price_volume_overlap_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_266_price_volume_overlap_vel_5d},
    "vapr_267_price_volume_overlap_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_267_price_volume_overlap_vel_21d},
    "vapr_268_price_volume_overlap_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_268_price_volume_overlap_vel_63d},
    "vapr_269_price_volume_overlap_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_269_price_volume_overlap_vel_126d},
    "vapr_270_price_volume_overlap_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_270_price_volume_overlap_vel_252d},
    "vapr_271_vapr_momentum_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_271_vapr_momentum_vel_5d},
    "vapr_272_vapr_momentum_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_272_vapr_momentum_vel_21d},
    "vapr_273_vapr_momentum_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_273_vapr_momentum_vel_63d},
    "vapr_274_vapr_momentum_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_274_vapr_momentum_vel_126d},
    "vapr_275_vapr_momentum_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_275_vapr_momentum_vel_252d},
    "vapr_276_vapr_exhaustion_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_276_vapr_exhaustion_vel_5d},
    "vapr_277_vapr_exhaustion_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_277_vapr_exhaustion_vel_21d},
    "vapr_278_vapr_exhaustion_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_278_vapr_exhaustion_vel_63d},
    "vapr_279_vapr_exhaustion_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_279_vapr_exhaustion_vel_126d},
    "vapr_280_vapr_exhaustion_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_280_vapr_exhaustion_vel_252d},
    "vapr_281_support_volume_strength_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_281_support_volume_strength_vel_5d},
    "vapr_282_support_volume_strength_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_282_support_volume_strength_vel_21d},
    "vapr_283_support_volume_strength_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_283_support_volume_strength_vel_63d},
    "vapr_284_support_volume_strength_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_284_support_volume_strength_vel_126d},
    "vapr_285_support_volume_strength_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_285_support_volume_strength_vel_252d},
    "vapr_286_resistance_volume_strength_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_286_resistance_volume_strength_vel_5d},
    "vapr_287_resistance_volume_strength_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_287_resistance_volume_strength_vel_21d},
    "vapr_288_resistance_volume_strength_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_288_resistance_volume_strength_vel_63d},
    "vapr_289_resistance_volume_strength_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_289_resistance_volume_strength_vel_126d},
    "vapr_290_resistance_volume_strength_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_290_resistance_volume_strength_vel_252d},
    "vapr_291_vapr_regime_shift_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_291_vapr_regime_shift_vel_5d},
    "vapr_292_vapr_regime_shift_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_292_vapr_regime_shift_vel_21d},
    "vapr_293_vapr_regime_shift_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_293_vapr_regime_shift_vel_63d},
    "vapr_294_vapr_regime_shift_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_294_vapr_regime_shift_vel_126d},
    "vapr_295_vapr_regime_shift_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_295_vapr_regime_shift_vel_252d},
    "vapr_296_vapr_tail_volume_vel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_296_vapr_tail_volume_vel_5d},
    "vapr_297_vapr_tail_volume_vel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_297_vapr_tail_volume_vel_21d},
    "vapr_298_vapr_tail_volume_vel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_298_vapr_tail_volume_vel_63d},
    "vapr_299_vapr_tail_volume_vel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_299_vapr_tail_volume_vel_126d},
    "vapr_300_vapr_tail_volume_vel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_300_vapr_tail_volume_vel_252d},
}
