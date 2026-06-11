"""
108_drawdown_history_rank — Acceleration (3rd Derivatives)
Domain: drawdown_history_rank
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

def dhrk_301_current_drawdown_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_301_current_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(5).diff(_TD_MON)

def dhrk_302_current_drawdown_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_302_current_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(21).diff(_TD_MON)

def dhrk_303_current_drawdown_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_303_current_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(63).diff(_TD_MON)

def dhrk_304_current_drawdown_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_304_current_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(126).diff(_TD_MON)

def dhrk_305_current_drawdown_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_305_current_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of current_drawdown. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).diff(252).diff(_TD_MON)

def dhrk_306_drawdown_rank_252d_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_306_drawdown_rank_252d_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(5).diff(_TD_MON)

def dhrk_307_drawdown_rank_252d_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_307_drawdown_rank_252d_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(21).diff(_TD_MON)

def dhrk_308_drawdown_rank_252d_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_308_drawdown_rank_252d_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(63).diff(_TD_MON)

def dhrk_309_drawdown_rank_252d_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_309_drawdown_rank_252d_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(126).diff(_TD_MON)

def dhrk_310_drawdown_rank_252d_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_310_drawdown_rank_252d_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_rank_252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(252).diff(_TD_MON)

def dhrk_311_drawdown_severity_z_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_311_drawdown_severity_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(5).diff(_TD_MON)

def dhrk_312_drawdown_severity_z_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_312_drawdown_severity_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(21).diff(_TD_MON)

def dhrk_313_drawdown_severity_z_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_313_drawdown_severity_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(63).diff(_TD_MON)

def dhrk_314_drawdown_severity_z_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_314_drawdown_severity_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(126).diff(_TD_MON)

def dhrk_315_drawdown_severity_z_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_315_drawdown_severity_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_z. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).diff(252).diff(_TD_MON)

def dhrk_316_drawdown_duration_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_316_drawdown_duration_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(5).diff(_TD_MON)

def dhrk_317_drawdown_duration_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_317_drawdown_duration_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(21).diff(_TD_MON)

def dhrk_318_drawdown_duration_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_318_drawdown_duration_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(63).diff(_TD_MON)

def dhrk_319_drawdown_duration_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_319_drawdown_duration_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(126).diff(_TD_MON)

def dhrk_320_drawdown_duration_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_320_drawdown_duration_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_duration. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).diff(252).diff(_TD_MON)

def dhrk_321_peak_to_trough_momentum_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_321_peak_to_trough_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(5).diff(_TD_MON)

def dhrk_322_peak_to_trough_momentum_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_322_peak_to_trough_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(21).diff(_TD_MON)

def dhrk_323_peak_to_trough_momentum_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_323_peak_to_trough_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(63).diff(_TD_MON)

def dhrk_324_peak_to_trough_momentum_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_324_peak_to_trough_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(126).diff(_TD_MON)

def dhrk_325_peak_to_trough_momentum_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_325_peak_to_trough_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of peak_to_trough_momentum. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).diff(252).diff(_TD_MON)

def dhrk_326_drawdown_acceleration_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_326_drawdown_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(5).diff(_TD_MON)

def dhrk_327_drawdown_acceleration_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_327_drawdown_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(21).diff(_TD_MON)

def dhrk_328_drawdown_acceleration_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_328_drawdown_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(63).diff(_TD_MON)

def dhrk_329_drawdown_acceleration_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_329_drawdown_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(126).diff(_TD_MON)

def dhrk_330_drawdown_acceleration_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_330_drawdown_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_acceleration. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).diff(252).diff(_TD_MON)

def dhrk_331_drawdown_vol_ratio_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_331_drawdown_vol_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(5).diff(_TD_MON)

def dhrk_332_drawdown_vol_ratio_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_332_drawdown_vol_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(21).diff(_TD_MON)

def dhrk_333_drawdown_vol_ratio_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_333_drawdown_vol_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(63).diff(_TD_MON)

def dhrk_334_drawdown_vol_ratio_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_334_drawdown_vol_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(126).diff(_TD_MON)

def dhrk_335_drawdown_vol_ratio_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_335_drawdown_vol_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_vol_ratio. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).diff(252).diff(_TD_MON)

def dhrk_336_recovery_from_lows_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_336_recovery_from_lows_accel_5d
    ECONOMIC RATIONALE: Acceleration of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(5).diff(_TD_MON)

def dhrk_337_recovery_from_lows_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_337_recovery_from_lows_accel_21d
    ECONOMIC RATIONALE: Acceleration of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(21).diff(_TD_MON)

def dhrk_338_recovery_from_lows_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_338_recovery_from_lows_accel_63d
    ECONOMIC RATIONALE: Acceleration of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(63).diff(_TD_MON)

def dhrk_339_recovery_from_lows_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_339_recovery_from_lows_accel_126d
    ECONOMIC RATIONALE: Acceleration of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(126).diff(_TD_MON)

def dhrk_340_recovery_from_lows_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_340_recovery_from_lows_accel_252d
    ECONOMIC RATIONALE: Acceleration of recovery_from_lows. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).diff(252).diff(_TD_MON)

def dhrk_341_drawdown_persistence_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_341_drawdown_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(5).diff(_TD_MON)

def dhrk_342_drawdown_persistence_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_342_drawdown_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(21).diff(_TD_MON)

def dhrk_343_drawdown_persistence_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_343_drawdown_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(63).diff(_TD_MON)

def dhrk_344_drawdown_persistence_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_344_drawdown_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(126).diff(_TD_MON)

def dhrk_345_drawdown_persistence_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_345_drawdown_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_persistence. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).diff(252).diff(_TD_MON)

def dhrk_346_drawdown_regime_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_346_drawdown_regime_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(5).diff(_TD_MON)

def dhrk_347_drawdown_regime_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_347_drawdown_regime_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(21).diff(_TD_MON)

def dhrk_348_drawdown_regime_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_348_drawdown_regime_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(63).diff(_TD_MON)

def dhrk_349_drawdown_regime_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_349_drawdown_regime_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(126).diff(_TD_MON)

def dhrk_350_drawdown_regime_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_350_drawdown_regime_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_regime. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).diff(252).diff(_TD_MON)

def dhrk_351_drawdown_impact_score_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_351_drawdown_impact_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(5).diff(_TD_MON)

def dhrk_352_drawdown_impact_score_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_352_drawdown_impact_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(21).diff(_TD_MON)

def dhrk_353_drawdown_impact_score_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_353_drawdown_impact_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(63).diff(_TD_MON)

def dhrk_354_drawdown_impact_score_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_354_drawdown_impact_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(126).diff(_TD_MON)

def dhrk_355_drawdown_impact_score_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_355_drawdown_impact_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_impact_score. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).diff(252).diff(_TD_MON)

def dhrk_356_historical_max_drawdown_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_356_historical_max_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(5).diff(_TD_MON)

def dhrk_357_historical_max_drawdown_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_357_historical_max_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(21).diff(_TD_MON)

def dhrk_358_historical_max_drawdown_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_358_historical_max_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(63).diff(_TD_MON)

def dhrk_359_historical_max_drawdown_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_359_historical_max_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(126).diff(_TD_MON)

def dhrk_360_historical_max_drawdown_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_360_historical_max_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of historical_max_drawdown. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).diff(252).diff(_TD_MON)

def dhrk_361_drawdown_exhaustion_proxy_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_361_drawdown_exhaustion_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dhrk_362_drawdown_exhaustion_proxy_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_362_drawdown_exhaustion_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dhrk_363_drawdown_exhaustion_proxy_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_363_drawdown_exhaustion_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dhrk_364_drawdown_exhaustion_proxy_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_364_drawdown_exhaustion_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dhrk_365_drawdown_exhaustion_proxy_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_365_drawdown_exhaustion_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_exhaustion_proxy. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dhrk_366_drawdown_oscillator_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_366_drawdown_oscillator_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dhrk_367_drawdown_oscillator_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_367_drawdown_oscillator_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dhrk_368_drawdown_oscillator_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_368_drawdown_oscillator_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dhrk_369_drawdown_oscillator_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_369_drawdown_oscillator_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dhrk_370_drawdown_oscillator_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_370_drawdown_oscillator_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_oscillator. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dhrk_371_drawdown_tail_risk_accel_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_371_drawdown_tail_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(5).diff(_TD_MON)

def dhrk_372_drawdown_tail_risk_accel_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_372_drawdown_tail_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(21).diff(_TD_MON)

def dhrk_373_drawdown_tail_risk_accel_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_373_drawdown_tail_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(63).diff(_TD_MON)

def dhrk_374_drawdown_tail_risk_accel_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_374_drawdown_tail_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(126).diff(_TD_MON)

def dhrk_375_drawdown_tail_risk_accel_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_375_drawdown_tail_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_tail_risk. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V108_REGISTRY_ACCEL = {
    "dhrk_301_current_drawdown_accel_5d": {"inputs": ["close"], "func": dhrk_301_current_drawdown_accel_5d},
    "dhrk_302_current_drawdown_accel_21d": {"inputs": ["close"], "func": dhrk_302_current_drawdown_accel_21d},
    "dhrk_303_current_drawdown_accel_63d": {"inputs": ["close"], "func": dhrk_303_current_drawdown_accel_63d},
    "dhrk_304_current_drawdown_accel_126d": {"inputs": ["close"], "func": dhrk_304_current_drawdown_accel_126d},
    "dhrk_305_current_drawdown_accel_252d": {"inputs": ["close"], "func": dhrk_305_current_drawdown_accel_252d},
    "dhrk_306_drawdown_rank_252d_accel_5d": {"inputs": ["close"], "func": dhrk_306_drawdown_rank_252d_accel_5d},
    "dhrk_307_drawdown_rank_252d_accel_21d": {"inputs": ["close"], "func": dhrk_307_drawdown_rank_252d_accel_21d},
    "dhrk_308_drawdown_rank_252d_accel_63d": {"inputs": ["close"], "func": dhrk_308_drawdown_rank_252d_accel_63d},
    "dhrk_309_drawdown_rank_252d_accel_126d": {"inputs": ["close"], "func": dhrk_309_drawdown_rank_252d_accel_126d},
    "dhrk_310_drawdown_rank_252d_accel_252d": {"inputs": ["close"], "func": dhrk_310_drawdown_rank_252d_accel_252d},
    "dhrk_311_drawdown_severity_z_accel_5d": {"inputs": ["close"], "func": dhrk_311_drawdown_severity_z_accel_5d},
    "dhrk_312_drawdown_severity_z_accel_21d": {"inputs": ["close"], "func": dhrk_312_drawdown_severity_z_accel_21d},
    "dhrk_313_drawdown_severity_z_accel_63d": {"inputs": ["close"], "func": dhrk_313_drawdown_severity_z_accel_63d},
    "dhrk_314_drawdown_severity_z_accel_126d": {"inputs": ["close"], "func": dhrk_314_drawdown_severity_z_accel_126d},
    "dhrk_315_drawdown_severity_z_accel_252d": {"inputs": ["close"], "func": dhrk_315_drawdown_severity_z_accel_252d},
    "dhrk_316_drawdown_duration_accel_5d": {"inputs": ["close"], "func": dhrk_316_drawdown_duration_accel_5d},
    "dhrk_317_drawdown_duration_accel_21d": {"inputs": ["close"], "func": dhrk_317_drawdown_duration_accel_21d},
    "dhrk_318_drawdown_duration_accel_63d": {"inputs": ["close"], "func": dhrk_318_drawdown_duration_accel_63d},
    "dhrk_319_drawdown_duration_accel_126d": {"inputs": ["close"], "func": dhrk_319_drawdown_duration_accel_126d},
    "dhrk_320_drawdown_duration_accel_252d": {"inputs": ["close"], "func": dhrk_320_drawdown_duration_accel_252d},
    "dhrk_321_peak_to_trough_momentum_accel_5d": {"inputs": ["close"], "func": dhrk_321_peak_to_trough_momentum_accel_5d},
    "dhrk_322_peak_to_trough_momentum_accel_21d": {"inputs": ["close"], "func": dhrk_322_peak_to_trough_momentum_accel_21d},
    "dhrk_323_peak_to_trough_momentum_accel_63d": {"inputs": ["close"], "func": dhrk_323_peak_to_trough_momentum_accel_63d},
    "dhrk_324_peak_to_trough_momentum_accel_126d": {"inputs": ["close"], "func": dhrk_324_peak_to_trough_momentum_accel_126d},
    "dhrk_325_peak_to_trough_momentum_accel_252d": {"inputs": ["close"], "func": dhrk_325_peak_to_trough_momentum_accel_252d},
    "dhrk_326_drawdown_acceleration_accel_5d": {"inputs": ["close"], "func": dhrk_326_drawdown_acceleration_accel_5d},
    "dhrk_327_drawdown_acceleration_accel_21d": {"inputs": ["close"], "func": dhrk_327_drawdown_acceleration_accel_21d},
    "dhrk_328_drawdown_acceleration_accel_63d": {"inputs": ["close"], "func": dhrk_328_drawdown_acceleration_accel_63d},
    "dhrk_329_drawdown_acceleration_accel_126d": {"inputs": ["close"], "func": dhrk_329_drawdown_acceleration_accel_126d},
    "dhrk_330_drawdown_acceleration_accel_252d": {"inputs": ["close"], "func": dhrk_330_drawdown_acceleration_accel_252d},
    "dhrk_331_drawdown_vol_ratio_accel_5d": {"inputs": ["close"], "func": dhrk_331_drawdown_vol_ratio_accel_5d},
    "dhrk_332_drawdown_vol_ratio_accel_21d": {"inputs": ["close"], "func": dhrk_332_drawdown_vol_ratio_accel_21d},
    "dhrk_333_drawdown_vol_ratio_accel_63d": {"inputs": ["close"], "func": dhrk_333_drawdown_vol_ratio_accel_63d},
    "dhrk_334_drawdown_vol_ratio_accel_126d": {"inputs": ["close"], "func": dhrk_334_drawdown_vol_ratio_accel_126d},
    "dhrk_335_drawdown_vol_ratio_accel_252d": {"inputs": ["close"], "func": dhrk_335_drawdown_vol_ratio_accel_252d},
    "dhrk_336_recovery_from_lows_accel_5d": {"inputs": ["close"], "func": dhrk_336_recovery_from_lows_accel_5d},
    "dhrk_337_recovery_from_lows_accel_21d": {"inputs": ["close"], "func": dhrk_337_recovery_from_lows_accel_21d},
    "dhrk_338_recovery_from_lows_accel_63d": {"inputs": ["close"], "func": dhrk_338_recovery_from_lows_accel_63d},
    "dhrk_339_recovery_from_lows_accel_126d": {"inputs": ["close"], "func": dhrk_339_recovery_from_lows_accel_126d},
    "dhrk_340_recovery_from_lows_accel_252d": {"inputs": ["close"], "func": dhrk_340_recovery_from_lows_accel_252d},
    "dhrk_341_drawdown_persistence_accel_5d": {"inputs": ["close"], "func": dhrk_341_drawdown_persistence_accel_5d},
    "dhrk_342_drawdown_persistence_accel_21d": {"inputs": ["close"], "func": dhrk_342_drawdown_persistence_accel_21d},
    "dhrk_343_drawdown_persistence_accel_63d": {"inputs": ["close"], "func": dhrk_343_drawdown_persistence_accel_63d},
    "dhrk_344_drawdown_persistence_accel_126d": {"inputs": ["close"], "func": dhrk_344_drawdown_persistence_accel_126d},
    "dhrk_345_drawdown_persistence_accel_252d": {"inputs": ["close"], "func": dhrk_345_drawdown_persistence_accel_252d},
    "dhrk_346_drawdown_regime_accel_5d": {"inputs": ["close"], "func": dhrk_346_drawdown_regime_accel_5d},
    "dhrk_347_drawdown_regime_accel_21d": {"inputs": ["close"], "func": dhrk_347_drawdown_regime_accel_21d},
    "dhrk_348_drawdown_regime_accel_63d": {"inputs": ["close"], "func": dhrk_348_drawdown_regime_accel_63d},
    "dhrk_349_drawdown_regime_accel_126d": {"inputs": ["close"], "func": dhrk_349_drawdown_regime_accel_126d},
    "dhrk_350_drawdown_regime_accel_252d": {"inputs": ["close"], "func": dhrk_350_drawdown_regime_accel_252d},
    "dhrk_351_drawdown_impact_score_accel_5d": {"inputs": ["close"], "func": dhrk_351_drawdown_impact_score_accel_5d},
    "dhrk_352_drawdown_impact_score_accel_21d": {"inputs": ["close"], "func": dhrk_352_drawdown_impact_score_accel_21d},
    "dhrk_353_drawdown_impact_score_accel_63d": {"inputs": ["close"], "func": dhrk_353_drawdown_impact_score_accel_63d},
    "dhrk_354_drawdown_impact_score_accel_126d": {"inputs": ["close"], "func": dhrk_354_drawdown_impact_score_accel_126d},
    "dhrk_355_drawdown_impact_score_accel_252d": {"inputs": ["close"], "func": dhrk_355_drawdown_impact_score_accel_252d},
    "dhrk_356_historical_max_drawdown_accel_5d": {"inputs": ["close"], "func": dhrk_356_historical_max_drawdown_accel_5d},
    "dhrk_357_historical_max_drawdown_accel_21d": {"inputs": ["close"], "func": dhrk_357_historical_max_drawdown_accel_21d},
    "dhrk_358_historical_max_drawdown_accel_63d": {"inputs": ["close"], "func": dhrk_358_historical_max_drawdown_accel_63d},
    "dhrk_359_historical_max_drawdown_accel_126d": {"inputs": ["close"], "func": dhrk_359_historical_max_drawdown_accel_126d},
    "dhrk_360_historical_max_drawdown_accel_252d": {"inputs": ["close"], "func": dhrk_360_historical_max_drawdown_accel_252d},
    "dhrk_361_drawdown_exhaustion_proxy_accel_5d": {"inputs": ["close"], "func": dhrk_361_drawdown_exhaustion_proxy_accel_5d},
    "dhrk_362_drawdown_exhaustion_proxy_accel_21d": {"inputs": ["close"], "func": dhrk_362_drawdown_exhaustion_proxy_accel_21d},
    "dhrk_363_drawdown_exhaustion_proxy_accel_63d": {"inputs": ["close"], "func": dhrk_363_drawdown_exhaustion_proxy_accel_63d},
    "dhrk_364_drawdown_exhaustion_proxy_accel_126d": {"inputs": ["close"], "func": dhrk_364_drawdown_exhaustion_proxy_accel_126d},
    "dhrk_365_drawdown_exhaustion_proxy_accel_252d": {"inputs": ["close"], "func": dhrk_365_drawdown_exhaustion_proxy_accel_252d},
    "dhrk_366_drawdown_oscillator_accel_5d": {"inputs": ["close"], "func": dhrk_366_drawdown_oscillator_accel_5d},
    "dhrk_367_drawdown_oscillator_accel_21d": {"inputs": ["close"], "func": dhrk_367_drawdown_oscillator_accel_21d},
    "dhrk_368_drawdown_oscillator_accel_63d": {"inputs": ["close"], "func": dhrk_368_drawdown_oscillator_accel_63d},
    "dhrk_369_drawdown_oscillator_accel_126d": {"inputs": ["close"], "func": dhrk_369_drawdown_oscillator_accel_126d},
    "dhrk_370_drawdown_oscillator_accel_252d": {"inputs": ["close"], "func": dhrk_370_drawdown_oscillator_accel_252d},
    "dhrk_371_drawdown_tail_risk_accel_5d": {"inputs": ["close"], "func": dhrk_371_drawdown_tail_risk_accel_5d},
    "dhrk_372_drawdown_tail_risk_accel_21d": {"inputs": ["close"], "func": dhrk_372_drawdown_tail_risk_accel_21d},
    "dhrk_373_drawdown_tail_risk_accel_63d": {"inputs": ["close"], "func": dhrk_373_drawdown_tail_risk_accel_63d},
    "dhrk_374_drawdown_tail_risk_accel_126d": {"inputs": ["close"], "func": dhrk_374_drawdown_tail_risk_accel_126d},
    "dhrk_375_drawdown_tail_risk_accel_252d": {"inputs": ["close"], "func": dhrk_375_drawdown_tail_risk_accel_252d},
}
