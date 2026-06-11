"""
114_overnight_intraday_split — Acceleration (3rd Derivatives)
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

def onid_301_overnight_return_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_301_overnight_return_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(5).diff(_TD_MON)

def onid_302_overnight_return_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_302_overnight_return_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(21).diff(_TD_MON)

def onid_303_overnight_return_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_303_overnight_return_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(63).diff(_TD_MON)

def onid_304_overnight_return_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_304_overnight_return_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(126).diff(_TD_MON)

def onid_305_overnight_return_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_305_overnight_return_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_return. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).diff(252).diff(_TD_MON)

def onid_306_intraday_return_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_306_intraday_return_accel_5d
    ECONOMIC RATIONALE: Acceleration of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(5).diff(_TD_MON)

def onid_307_intraday_return_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_307_intraday_return_accel_21d
    ECONOMIC RATIONALE: Acceleration of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(21).diff(_TD_MON)

def onid_308_intraday_return_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_308_intraday_return_accel_63d
    ECONOMIC RATIONALE: Acceleration of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(63).diff(_TD_MON)

def onid_309_intraday_return_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_309_intraday_return_accel_126d
    ECONOMIC RATIONALE: Acceleration of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(126).diff(_TD_MON)

def onid_310_intraday_return_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_310_intraday_return_accel_252d
    ECONOMIC RATIONALE: Acceleration of intraday_return. Returns from current open to current close.
    """
    return (close / open - 1).diff(252).diff(_TD_MON)

def onid_311_on_id_divergence_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_311_on_id_divergence_accel_5d
    ECONOMIC RATIONALE: Acceleration of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(5).diff(_TD_MON)

def onid_312_on_id_divergence_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_312_on_id_divergence_accel_21d
    ECONOMIC RATIONALE: Acceleration of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(21).diff(_TD_MON)

def onid_313_on_id_divergence_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_313_on_id_divergence_accel_63d
    ECONOMIC RATIONALE: Acceleration of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(63).diff(_TD_MON)

def onid_314_on_id_divergence_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_314_on_id_divergence_accel_126d
    ECONOMIC RATIONALE: Acceleration of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(126).diff(_TD_MON)

def onid_315_on_id_divergence_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_315_on_id_divergence_accel_252d
    ECONOMIC RATIONALE: Acceleration of on_id_divergence. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).diff(252).diff(_TD_MON)

def onid_316_overnight_vol_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_316_overnight_vol_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(5).diff(_TD_MON)

def onid_317_overnight_vol_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_317_overnight_vol_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(21).diff(_TD_MON)

def onid_318_overnight_vol_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_318_overnight_vol_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(63).diff(_TD_MON)

def onid_319_overnight_vol_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_319_overnight_vol_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(126).diff(_TD_MON)

def onid_320_overnight_vol_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_320_overnight_vol_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_vol. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).diff(252).diff(_TD_MON)

def onid_321_intraday_vol_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_321_intraday_vol_accel_5d
    ECONOMIC RATIONALE: Acceleration of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(5).diff(_TD_MON)

def onid_322_intraday_vol_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_322_intraday_vol_accel_21d
    ECONOMIC RATIONALE: Acceleration of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(21).diff(_TD_MON)

def onid_323_intraday_vol_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_323_intraday_vol_accel_63d
    ECONOMIC RATIONALE: Acceleration of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(63).diff(_TD_MON)

def onid_324_intraday_vol_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_324_intraday_vol_accel_126d
    ECONOMIC RATIONALE: Acceleration of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(126).diff(_TD_MON)

def onid_325_intraday_vol_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_325_intraday_vol_accel_252d
    ECONOMIC RATIONALE: Acceleration of intraday_vol. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).diff(252).diff(_TD_MON)

def onid_326_on_id_vol_ratio_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_326_on_id_vol_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def onid_327_on_id_vol_ratio_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_327_on_id_vol_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def onid_328_on_id_vol_ratio_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_328_on_id_vol_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def onid_329_on_id_vol_ratio_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_329_on_id_vol_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def onid_330_on_id_vol_ratio_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_330_on_id_vol_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of on_id_vol_ratio. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def onid_331_overnight_bias_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_331_overnight_bias_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(5).diff(_TD_MON)

def onid_332_overnight_bias_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_332_overnight_bias_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(21).diff(_TD_MON)

def onid_333_overnight_bias_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_333_overnight_bias_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(63).diff(_TD_MON)

def onid_334_overnight_bias_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_334_overnight_bias_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(126).diff(_TD_MON)

def onid_335_overnight_bias_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_335_overnight_bias_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_bias. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).diff(252).diff(_TD_MON)

def onid_336_intraday_bias_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_336_intraday_bias_accel_5d
    ECONOMIC RATIONALE: Acceleration of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(5).diff(_TD_MON)

def onid_337_intraday_bias_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_337_intraday_bias_accel_21d
    ECONOMIC RATIONALE: Acceleration of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(21).diff(_TD_MON)

def onid_338_intraday_bias_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_338_intraday_bias_accel_63d
    ECONOMIC RATIONALE: Acceleration of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(63).diff(_TD_MON)

def onid_339_intraday_bias_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_339_intraday_bias_accel_126d
    ECONOMIC RATIONALE: Acceleration of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(126).diff(_TD_MON)

def onid_340_intraday_bias_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_340_intraday_bias_accel_252d
    ECONOMIC RATIONALE: Acceleration of intraday_bias. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).diff(252).diff(_TD_MON)

def onid_341_gap_fade_potential_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_341_gap_fade_potential_accel_5d
    ECONOMIC RATIONALE: Acceleration of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(5).diff(_TD_MON)

def onid_342_gap_fade_potential_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_342_gap_fade_potential_accel_21d
    ECONOMIC RATIONALE: Acceleration of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(21).diff(_TD_MON)

def onid_343_gap_fade_potential_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_343_gap_fade_potential_accel_63d
    ECONOMIC RATIONALE: Acceleration of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(63).diff(_TD_MON)

def onid_344_gap_fade_potential_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_344_gap_fade_potential_accel_126d
    ECONOMIC RATIONALE: Acceleration of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(126).diff(_TD_MON)

def onid_345_gap_fade_potential_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_345_gap_fade_potential_accel_252d
    ECONOMIC RATIONALE: Acceleration of gap_fade_potential. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).diff(252).diff(_TD_MON)

def onid_346_overnight_gap_z_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_346_overnight_gap_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(5).diff(_TD_MON)

def onid_347_overnight_gap_z_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_347_overnight_gap_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(21).diff(_TD_MON)

def onid_348_overnight_gap_z_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_348_overnight_gap_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(63).diff(_TD_MON)

def onid_349_overnight_gap_z_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_349_overnight_gap_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(126).diff(_TD_MON)

def onid_350_overnight_gap_z_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_350_overnight_gap_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_gap_z. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).diff(252).diff(_TD_MON)

def onid_351_intraday_range_pos_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_351_intraday_range_pos_accel_5d
    ECONOMIC RATIONALE: Acceleration of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def onid_352_intraday_range_pos_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_352_intraday_range_pos_accel_21d
    ECONOMIC RATIONALE: Acceleration of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def onid_353_intraday_range_pos_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_353_intraday_range_pos_accel_63d
    ECONOMIC RATIONALE: Acceleration of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def onid_354_intraday_range_pos_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_354_intraday_range_pos_accel_126d
    ECONOMIC RATIONALE: Acceleration of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def onid_355_intraday_range_pos_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_355_intraday_range_pos_accel_252d
    ECONOMIC RATIONALE: Acceleration of intraday_range_pos. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def onid_356_overnight_momentum_lead_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_356_overnight_momentum_lead_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def onid_357_overnight_momentum_lead_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_357_overnight_momentum_lead_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def onid_358_overnight_momentum_lead_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_358_overnight_momentum_lead_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def onid_359_overnight_momentum_lead_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_359_overnight_momentum_lead_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def onid_360_overnight_momentum_lead_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_360_overnight_momentum_lead_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_momentum_lead. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def onid_361_id_reversal_strength_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_361_id_reversal_strength_accel_5d
    ECONOMIC RATIONALE: Acceleration of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(5).diff(_TD_MON)

def onid_362_id_reversal_strength_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_362_id_reversal_strength_accel_21d
    ECONOMIC RATIONALE: Acceleration of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(21).diff(_TD_MON)

def onid_363_id_reversal_strength_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_363_id_reversal_strength_accel_63d
    ECONOMIC RATIONALE: Acceleration of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(63).diff(_TD_MON)

def onid_364_id_reversal_strength_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_364_id_reversal_strength_accel_126d
    ECONOMIC RATIONALE: Acceleration of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(126).diff(_TD_MON)

def onid_365_id_reversal_strength_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_365_id_reversal_strength_accel_252d
    ECONOMIC RATIONALE: Acceleration of id_reversal_strength. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).diff(252).diff(_TD_MON)

def onid_366_on_id_correlation_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_366_on_id_correlation_accel_5d
    ECONOMIC RATIONALE: Acceleration of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(5).diff(_TD_MON)

def onid_367_on_id_correlation_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_367_on_id_correlation_accel_21d
    ECONOMIC RATIONALE: Acceleration of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(21).diff(_TD_MON)

def onid_368_on_id_correlation_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_368_on_id_correlation_accel_63d
    ECONOMIC RATIONALE: Acceleration of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(63).diff(_TD_MON)

def onid_369_on_id_correlation_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_369_on_id_correlation_accel_126d
    ECONOMIC RATIONALE: Acceleration of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(126).diff(_TD_MON)

def onid_370_on_id_correlation_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_370_on_id_correlation_accel_252d
    ECONOMIC RATIONALE: Acceleration of on_id_correlation. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).diff(252).diff(_TD_MON)

def onid_371_overnight_shock_flag_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_371_overnight_shock_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(5).diff(_TD_MON)

def onid_372_overnight_shock_flag_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_372_overnight_shock_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(21).diff(_TD_MON)

def onid_373_overnight_shock_flag_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_373_overnight_shock_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(63).diff(_TD_MON)

def onid_374_overnight_shock_flag_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_374_overnight_shock_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(126).diff(_TD_MON)

def onid_375_overnight_shock_flag_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_375_overnight_shock_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of overnight_shock_flag. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V114_REGISTRY_ACCEL = {
    "onid_301_overnight_return_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_301_overnight_return_accel_5d},
    "onid_302_overnight_return_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_302_overnight_return_accel_21d},
    "onid_303_overnight_return_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_303_overnight_return_accel_63d},
    "onid_304_overnight_return_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_304_overnight_return_accel_126d},
    "onid_305_overnight_return_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_305_overnight_return_accel_252d},
    "onid_306_intraday_return_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_306_intraday_return_accel_5d},
    "onid_307_intraday_return_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_307_intraday_return_accel_21d},
    "onid_308_intraday_return_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_308_intraday_return_accel_63d},
    "onid_309_intraday_return_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_309_intraday_return_accel_126d},
    "onid_310_intraday_return_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_310_intraday_return_accel_252d},
    "onid_311_on_id_divergence_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_311_on_id_divergence_accel_5d},
    "onid_312_on_id_divergence_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_312_on_id_divergence_accel_21d},
    "onid_313_on_id_divergence_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_313_on_id_divergence_accel_63d},
    "onid_314_on_id_divergence_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_314_on_id_divergence_accel_126d},
    "onid_315_on_id_divergence_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_315_on_id_divergence_accel_252d},
    "onid_316_overnight_vol_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_316_overnight_vol_accel_5d},
    "onid_317_overnight_vol_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_317_overnight_vol_accel_21d},
    "onid_318_overnight_vol_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_318_overnight_vol_accel_63d},
    "onid_319_overnight_vol_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_319_overnight_vol_accel_126d},
    "onid_320_overnight_vol_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_320_overnight_vol_accel_252d},
    "onid_321_intraday_vol_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_321_intraday_vol_accel_5d},
    "onid_322_intraday_vol_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_322_intraday_vol_accel_21d},
    "onid_323_intraday_vol_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_323_intraday_vol_accel_63d},
    "onid_324_intraday_vol_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_324_intraday_vol_accel_126d},
    "onid_325_intraday_vol_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_325_intraday_vol_accel_252d},
    "onid_326_on_id_vol_ratio_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_326_on_id_vol_ratio_accel_5d},
    "onid_327_on_id_vol_ratio_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_327_on_id_vol_ratio_accel_21d},
    "onid_328_on_id_vol_ratio_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_328_on_id_vol_ratio_accel_63d},
    "onid_329_on_id_vol_ratio_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_329_on_id_vol_ratio_accel_126d},
    "onid_330_on_id_vol_ratio_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_330_on_id_vol_ratio_accel_252d},
    "onid_331_overnight_bias_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_331_overnight_bias_accel_5d},
    "onid_332_overnight_bias_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_332_overnight_bias_accel_21d},
    "onid_333_overnight_bias_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_333_overnight_bias_accel_63d},
    "onid_334_overnight_bias_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_334_overnight_bias_accel_126d},
    "onid_335_overnight_bias_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_335_overnight_bias_accel_252d},
    "onid_336_intraday_bias_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_336_intraday_bias_accel_5d},
    "onid_337_intraday_bias_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_337_intraday_bias_accel_21d},
    "onid_338_intraday_bias_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_338_intraday_bias_accel_63d},
    "onid_339_intraday_bias_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_339_intraday_bias_accel_126d},
    "onid_340_intraday_bias_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_340_intraday_bias_accel_252d},
    "onid_341_gap_fade_potential_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_341_gap_fade_potential_accel_5d},
    "onid_342_gap_fade_potential_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_342_gap_fade_potential_accel_21d},
    "onid_343_gap_fade_potential_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_343_gap_fade_potential_accel_63d},
    "onid_344_gap_fade_potential_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_344_gap_fade_potential_accel_126d},
    "onid_345_gap_fade_potential_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_345_gap_fade_potential_accel_252d},
    "onid_346_overnight_gap_z_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_346_overnight_gap_z_accel_5d},
    "onid_347_overnight_gap_z_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_347_overnight_gap_z_accel_21d},
    "onid_348_overnight_gap_z_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_348_overnight_gap_z_accel_63d},
    "onid_349_overnight_gap_z_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_349_overnight_gap_z_accel_126d},
    "onid_350_overnight_gap_z_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_350_overnight_gap_z_accel_252d},
    "onid_351_intraday_range_pos_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_351_intraday_range_pos_accel_5d},
    "onid_352_intraday_range_pos_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_352_intraday_range_pos_accel_21d},
    "onid_353_intraday_range_pos_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_353_intraday_range_pos_accel_63d},
    "onid_354_intraday_range_pos_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_354_intraday_range_pos_accel_126d},
    "onid_355_intraday_range_pos_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_355_intraday_range_pos_accel_252d},
    "onid_356_overnight_momentum_lead_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_356_overnight_momentum_lead_accel_5d},
    "onid_357_overnight_momentum_lead_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_357_overnight_momentum_lead_accel_21d},
    "onid_358_overnight_momentum_lead_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_358_overnight_momentum_lead_accel_63d},
    "onid_359_overnight_momentum_lead_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_359_overnight_momentum_lead_accel_126d},
    "onid_360_overnight_momentum_lead_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_360_overnight_momentum_lead_accel_252d},
    "onid_361_id_reversal_strength_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_361_id_reversal_strength_accel_5d},
    "onid_362_id_reversal_strength_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_362_id_reversal_strength_accel_21d},
    "onid_363_id_reversal_strength_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_363_id_reversal_strength_accel_63d},
    "onid_364_id_reversal_strength_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_364_id_reversal_strength_accel_126d},
    "onid_365_id_reversal_strength_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_365_id_reversal_strength_accel_252d},
    "onid_366_on_id_correlation_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_366_on_id_correlation_accel_5d},
    "onid_367_on_id_correlation_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_367_on_id_correlation_accel_21d},
    "onid_368_on_id_correlation_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_368_on_id_correlation_accel_63d},
    "onid_369_on_id_correlation_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_369_on_id_correlation_accel_126d},
    "onid_370_on_id_correlation_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_370_on_id_correlation_accel_252d},
    "onid_371_overnight_shock_flag_accel_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_371_overnight_shock_flag_accel_5d},
    "onid_372_overnight_shock_flag_accel_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_372_overnight_shock_flag_accel_21d},
    "onid_373_overnight_shock_flag_accel_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_373_overnight_shock_flag_accel_63d},
    "onid_374_overnight_shock_flag_accel_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_374_overnight_shock_flag_accel_126d},
    "onid_375_overnight_shock_flag_accel_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_375_overnight_shock_flag_accel_252d},
}
