"""
112_volume_at_price — Acceleration (3rd Derivatives)
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

def vapr_301_volume_poc_dist_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_301_volume_poc_dist_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(5).diff(_TD_MON)

def vapr_302_volume_poc_dist_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_302_volume_poc_dist_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(21).diff(_TD_MON)

def vapr_303_volume_poc_dist_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_303_volume_poc_dist_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(63).diff(_TD_MON)

def vapr_304_volume_poc_dist_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_304_volume_poc_dist_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(126).diff(_TD_MON)

def vapr_305_volume_poc_dist_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_305_volume_poc_dist_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_poc_dist. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(252).diff(_TD_MON)

def vapr_306_value_area_high_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_306_value_area_high_accel_5d
    ECONOMIC RATIONALE: Acceleration of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(5).diff(_TD_MON)

def vapr_307_value_area_high_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_307_value_area_high_accel_21d
    ECONOMIC RATIONALE: Acceleration of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(21).diff(_TD_MON)

def vapr_308_value_area_high_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_308_value_area_high_accel_63d
    ECONOMIC RATIONALE: Acceleration of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(63).diff(_TD_MON)

def vapr_309_value_area_high_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_309_value_area_high_accel_126d
    ECONOMIC RATIONALE: Acceleration of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(126).diff(_TD_MON)

def vapr_310_value_area_high_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_310_value_area_high_accel_252d
    ECONOMIC RATIONALE: Acceleration of value_area_high. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).diff(252).diff(_TD_MON)

def vapr_311_value_area_low_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_311_value_area_low_accel_5d
    ECONOMIC RATIONALE: Acceleration of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(5).diff(_TD_MON)

def vapr_312_value_area_low_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_312_value_area_low_accel_21d
    ECONOMIC RATIONALE: Acceleration of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(21).diff(_TD_MON)

def vapr_313_value_area_low_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_313_value_area_low_accel_63d
    ECONOMIC RATIONALE: Acceleration of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(63).diff(_TD_MON)

def vapr_314_value_area_low_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_314_value_area_low_accel_126d
    ECONOMIC RATIONALE: Acceleration of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(126).diff(_TD_MON)

def vapr_315_value_area_low_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_315_value_area_low_accel_252d
    ECONOMIC RATIONALE: Acceleration of value_area_low. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).diff(252).diff(_TD_MON)

def vapr_316_high_volume_node_dist_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_316_high_volume_node_dist_accel_5d
    ECONOMIC RATIONALE: Acceleration of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(5).diff(_TD_MON)

def vapr_317_high_volume_node_dist_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_317_high_volume_node_dist_accel_21d
    ECONOMIC RATIONALE: Acceleration of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(21).diff(_TD_MON)

def vapr_318_high_volume_node_dist_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_318_high_volume_node_dist_accel_63d
    ECONOMIC RATIONALE: Acceleration of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(63).diff(_TD_MON)

def vapr_319_high_volume_node_dist_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_319_high_volume_node_dist_accel_126d
    ECONOMIC RATIONALE: Acceleration of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(126).diff(_TD_MON)

def vapr_320_high_volume_node_dist_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_320_high_volume_node_dist_accel_252d
    ECONOMIC RATIONALE: Acceleration of high_volume_node_dist. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).diff(252).diff(_TD_MON)

def vapr_321_low_volume_node_flag_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_321_low_volume_node_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(5).diff(_TD_MON)

def vapr_322_low_volume_node_flag_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_322_low_volume_node_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(21).diff(_TD_MON)

def vapr_323_low_volume_node_flag_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_323_low_volume_node_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(63).diff(_TD_MON)

def vapr_324_low_volume_node_flag_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_324_low_volume_node_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(126).diff(_TD_MON)

def vapr_325_low_volume_node_flag_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_325_low_volume_node_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of low_volume_node_flag. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).diff(252).diff(_TD_MON)

def vapr_326_volume_skew_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_326_volume_skew_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(5).diff(_TD_MON)

def vapr_327_volume_skew_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_327_volume_skew_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(21).diff(_TD_MON)

def vapr_328_volume_skew_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_328_volume_skew_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(63).diff(_TD_MON)

def vapr_329_volume_skew_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_329_volume_skew_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(126).diff(_TD_MON)

def vapr_330_volume_skew_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_330_volume_skew_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_skew. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).diff(252).diff(_TD_MON)

def vapr_331_vapr_zscore_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_331_vapr_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def vapr_332_vapr_zscore_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_332_vapr_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def vapr_333_vapr_zscore_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_333_vapr_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def vapr_334_vapr_zscore_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_334_vapr_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def vapr_335_vapr_zscore_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_335_vapr_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of vapr_zscore. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def vapr_336_volume_concentration_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_336_volume_concentration_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(5).diff(_TD_MON)

def vapr_337_volume_concentration_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_337_volume_concentration_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(21).diff(_TD_MON)

def vapr_338_volume_concentration_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_338_volume_concentration_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(63).diff(_TD_MON)

def vapr_339_volume_concentration_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_339_volume_concentration_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(126).diff(_TD_MON)

def vapr_340_volume_concentration_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_340_volume_concentration_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_concentration. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).diff(252).diff(_TD_MON)

def vapr_341_price_volume_overlap_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_341_price_volume_overlap_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(5).diff(_TD_MON)

def vapr_342_price_volume_overlap_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_342_price_volume_overlap_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(21).diff(_TD_MON)

def vapr_343_price_volume_overlap_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_343_price_volume_overlap_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(63).diff(_TD_MON)

def vapr_344_price_volume_overlap_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_344_price_volume_overlap_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(126).diff(_TD_MON)

def vapr_345_price_volume_overlap_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_345_price_volume_overlap_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_volume_overlap. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).diff(252).diff(_TD_MON)

def vapr_346_vapr_momentum_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_346_vapr_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(5).diff(_TD_MON)

def vapr_347_vapr_momentum_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_347_vapr_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(21).diff(_TD_MON)

def vapr_348_vapr_momentum_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_348_vapr_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(63).diff(_TD_MON)

def vapr_349_vapr_momentum_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_349_vapr_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(126).diff(_TD_MON)

def vapr_350_vapr_momentum_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_350_vapr_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of vapr_momentum. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).diff(252).diff(_TD_MON)

def vapr_351_vapr_exhaustion_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_351_vapr_exhaustion_accel_5d
    ECONOMIC RATIONALE: Acceleration of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(5).diff(_TD_MON)

def vapr_352_vapr_exhaustion_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_352_vapr_exhaustion_accel_21d
    ECONOMIC RATIONALE: Acceleration of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(21).diff(_TD_MON)

def vapr_353_vapr_exhaustion_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_353_vapr_exhaustion_accel_63d
    ECONOMIC RATIONALE: Acceleration of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(63).diff(_TD_MON)

def vapr_354_vapr_exhaustion_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_354_vapr_exhaustion_accel_126d
    ECONOMIC RATIONALE: Acceleration of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(126).diff(_TD_MON)

def vapr_355_vapr_exhaustion_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_355_vapr_exhaustion_accel_252d
    ECONOMIC RATIONALE: Acceleration of vapr_exhaustion. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).diff(252).diff(_TD_MON)

def vapr_356_support_volume_strength_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_356_support_volume_strength_accel_5d
    ECONOMIC RATIONALE: Acceleration of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(5).diff(_TD_MON)

def vapr_357_support_volume_strength_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_357_support_volume_strength_accel_21d
    ECONOMIC RATIONALE: Acceleration of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(21).diff(_TD_MON)

def vapr_358_support_volume_strength_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_358_support_volume_strength_accel_63d
    ECONOMIC RATIONALE: Acceleration of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(63).diff(_TD_MON)

def vapr_359_support_volume_strength_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_359_support_volume_strength_accel_126d
    ECONOMIC RATIONALE: Acceleration of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(126).diff(_TD_MON)

def vapr_360_support_volume_strength_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_360_support_volume_strength_accel_252d
    ECONOMIC RATIONALE: Acceleration of support_volume_strength. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).diff(252).diff(_TD_MON)

def vapr_361_resistance_volume_strength_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_361_resistance_volume_strength_accel_5d
    ECONOMIC RATIONALE: Acceleration of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(5).diff(_TD_MON)

def vapr_362_resistance_volume_strength_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_362_resistance_volume_strength_accel_21d
    ECONOMIC RATIONALE: Acceleration of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(21).diff(_TD_MON)

def vapr_363_resistance_volume_strength_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_363_resistance_volume_strength_accel_63d
    ECONOMIC RATIONALE: Acceleration of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(63).diff(_TD_MON)

def vapr_364_resistance_volume_strength_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_364_resistance_volume_strength_accel_126d
    ECONOMIC RATIONALE: Acceleration of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(126).diff(_TD_MON)

def vapr_365_resistance_volume_strength_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_365_resistance_volume_strength_accel_252d
    ECONOMIC RATIONALE: Acceleration of resistance_volume_strength. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).diff(252).diff(_TD_MON)

def vapr_366_vapr_regime_shift_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_366_vapr_regime_shift_accel_5d
    ECONOMIC RATIONALE: Acceleration of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(5).diff(_TD_MON)

def vapr_367_vapr_regime_shift_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_367_vapr_regime_shift_accel_21d
    ECONOMIC RATIONALE: Acceleration of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(21).diff(_TD_MON)

def vapr_368_vapr_regime_shift_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_368_vapr_regime_shift_accel_63d
    ECONOMIC RATIONALE: Acceleration of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(63).diff(_TD_MON)

def vapr_369_vapr_regime_shift_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_369_vapr_regime_shift_accel_126d
    ECONOMIC RATIONALE: Acceleration of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(126).diff(_TD_MON)

def vapr_370_vapr_regime_shift_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_370_vapr_regime_shift_accel_252d
    ECONOMIC RATIONALE: Acceleration of vapr_regime_shift. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).diff(252).diff(_TD_MON)

def vapr_371_vapr_tail_volume_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_371_vapr_tail_volume_accel_5d
    ECONOMIC RATIONALE: Acceleration of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(5).diff(_TD_MON)

def vapr_372_vapr_tail_volume_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_372_vapr_tail_volume_accel_21d
    ECONOMIC RATIONALE: Acceleration of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(21).diff(_TD_MON)

def vapr_373_vapr_tail_volume_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_373_vapr_tail_volume_accel_63d
    ECONOMIC RATIONALE: Acceleration of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(63).diff(_TD_MON)

def vapr_374_vapr_tail_volume_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_374_vapr_tail_volume_accel_126d
    ECONOMIC RATIONALE: Acceleration of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(126).diff(_TD_MON)

def vapr_375_vapr_tail_volume_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_375_vapr_tail_volume_accel_252d
    ECONOMIC RATIONALE: Acceleration of vapr_tail_volume. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V112_REGISTRY_ACCEL = {
    "vapr_301_volume_poc_dist_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_301_volume_poc_dist_accel_5d},
    "vapr_302_volume_poc_dist_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_302_volume_poc_dist_accel_21d},
    "vapr_303_volume_poc_dist_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_303_volume_poc_dist_accel_63d},
    "vapr_304_volume_poc_dist_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_304_volume_poc_dist_accel_126d},
    "vapr_305_volume_poc_dist_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_305_volume_poc_dist_accel_252d},
    "vapr_306_value_area_high_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_306_value_area_high_accel_5d},
    "vapr_307_value_area_high_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_307_value_area_high_accel_21d},
    "vapr_308_value_area_high_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_308_value_area_high_accel_63d},
    "vapr_309_value_area_high_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_309_value_area_high_accel_126d},
    "vapr_310_value_area_high_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_310_value_area_high_accel_252d},
    "vapr_311_value_area_low_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_311_value_area_low_accel_5d},
    "vapr_312_value_area_low_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_312_value_area_low_accel_21d},
    "vapr_313_value_area_low_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_313_value_area_low_accel_63d},
    "vapr_314_value_area_low_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_314_value_area_low_accel_126d},
    "vapr_315_value_area_low_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_315_value_area_low_accel_252d},
    "vapr_316_high_volume_node_dist_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_316_high_volume_node_dist_accel_5d},
    "vapr_317_high_volume_node_dist_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_317_high_volume_node_dist_accel_21d},
    "vapr_318_high_volume_node_dist_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_318_high_volume_node_dist_accel_63d},
    "vapr_319_high_volume_node_dist_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_319_high_volume_node_dist_accel_126d},
    "vapr_320_high_volume_node_dist_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_320_high_volume_node_dist_accel_252d},
    "vapr_321_low_volume_node_flag_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_321_low_volume_node_flag_accel_5d},
    "vapr_322_low_volume_node_flag_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_322_low_volume_node_flag_accel_21d},
    "vapr_323_low_volume_node_flag_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_323_low_volume_node_flag_accel_63d},
    "vapr_324_low_volume_node_flag_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_324_low_volume_node_flag_accel_126d},
    "vapr_325_low_volume_node_flag_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_325_low_volume_node_flag_accel_252d},
    "vapr_326_volume_skew_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_326_volume_skew_accel_5d},
    "vapr_327_volume_skew_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_327_volume_skew_accel_21d},
    "vapr_328_volume_skew_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_328_volume_skew_accel_63d},
    "vapr_329_volume_skew_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_329_volume_skew_accel_126d},
    "vapr_330_volume_skew_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_330_volume_skew_accel_252d},
    "vapr_331_vapr_zscore_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_331_vapr_zscore_accel_5d},
    "vapr_332_vapr_zscore_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_332_vapr_zscore_accel_21d},
    "vapr_333_vapr_zscore_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_333_vapr_zscore_accel_63d},
    "vapr_334_vapr_zscore_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_334_vapr_zscore_accel_126d},
    "vapr_335_vapr_zscore_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_335_vapr_zscore_accel_252d},
    "vapr_336_volume_concentration_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_336_volume_concentration_accel_5d},
    "vapr_337_volume_concentration_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_337_volume_concentration_accel_21d},
    "vapr_338_volume_concentration_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_338_volume_concentration_accel_63d},
    "vapr_339_volume_concentration_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_339_volume_concentration_accel_126d},
    "vapr_340_volume_concentration_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_340_volume_concentration_accel_252d},
    "vapr_341_price_volume_overlap_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_341_price_volume_overlap_accel_5d},
    "vapr_342_price_volume_overlap_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_342_price_volume_overlap_accel_21d},
    "vapr_343_price_volume_overlap_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_343_price_volume_overlap_accel_63d},
    "vapr_344_price_volume_overlap_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_344_price_volume_overlap_accel_126d},
    "vapr_345_price_volume_overlap_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_345_price_volume_overlap_accel_252d},
    "vapr_346_vapr_momentum_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_346_vapr_momentum_accel_5d},
    "vapr_347_vapr_momentum_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_347_vapr_momentum_accel_21d},
    "vapr_348_vapr_momentum_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_348_vapr_momentum_accel_63d},
    "vapr_349_vapr_momentum_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_349_vapr_momentum_accel_126d},
    "vapr_350_vapr_momentum_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_350_vapr_momentum_accel_252d},
    "vapr_351_vapr_exhaustion_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_351_vapr_exhaustion_accel_5d},
    "vapr_352_vapr_exhaustion_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_352_vapr_exhaustion_accel_21d},
    "vapr_353_vapr_exhaustion_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_353_vapr_exhaustion_accel_63d},
    "vapr_354_vapr_exhaustion_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_354_vapr_exhaustion_accel_126d},
    "vapr_355_vapr_exhaustion_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_355_vapr_exhaustion_accel_252d},
    "vapr_356_support_volume_strength_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_356_support_volume_strength_accel_5d},
    "vapr_357_support_volume_strength_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_357_support_volume_strength_accel_21d},
    "vapr_358_support_volume_strength_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_358_support_volume_strength_accel_63d},
    "vapr_359_support_volume_strength_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_359_support_volume_strength_accel_126d},
    "vapr_360_support_volume_strength_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_360_support_volume_strength_accel_252d},
    "vapr_361_resistance_volume_strength_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_361_resistance_volume_strength_accel_5d},
    "vapr_362_resistance_volume_strength_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_362_resistance_volume_strength_accel_21d},
    "vapr_363_resistance_volume_strength_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_363_resistance_volume_strength_accel_63d},
    "vapr_364_resistance_volume_strength_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_364_resistance_volume_strength_accel_126d},
    "vapr_365_resistance_volume_strength_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_365_resistance_volume_strength_accel_252d},
    "vapr_366_vapr_regime_shift_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_366_vapr_regime_shift_accel_5d},
    "vapr_367_vapr_regime_shift_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_367_vapr_regime_shift_accel_21d},
    "vapr_368_vapr_regime_shift_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_368_vapr_regime_shift_accel_63d},
    "vapr_369_vapr_regime_shift_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_369_vapr_regime_shift_accel_126d},
    "vapr_370_vapr_regime_shift_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_370_vapr_regime_shift_accel_252d},
    "vapr_371_vapr_tail_volume_accel_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_371_vapr_tail_volume_accel_5d},
    "vapr_372_vapr_tail_volume_accel_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_372_vapr_tail_volume_accel_21d},
    "vapr_373_vapr_tail_volume_accel_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_373_vapr_tail_volume_accel_63d},
    "vapr_374_vapr_tail_volume_accel_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_374_vapr_tail_volume_accel_126d},
    "vapr_375_vapr_tail_volume_accel_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_375_vapr_tail_volume_accel_252d},
}
