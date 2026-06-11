"""
118_drawdown_recovery_asymmetry — Acceleration (3rd Derivatives)
Domain: drawdown_recovery_asymmetry
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

def dras_301_downside_speed_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_301_downside_speed_accel_5d
    ECONOMIC RATIONALE: Acceleration of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(5).diff(_TD_MON)

def dras_302_downside_speed_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_302_downside_speed_accel_21d
    ECONOMIC RATIONALE: Acceleration of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(21).diff(_TD_MON)

def dras_303_downside_speed_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_303_downside_speed_accel_63d
    ECONOMIC RATIONALE: Acceleration of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(63).diff(_TD_MON)

def dras_304_downside_speed_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_304_downside_speed_accel_126d
    ECONOMIC RATIONALE: Acceleration of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(126).diff(_TD_MON)

def dras_305_downside_speed_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_305_downside_speed_accel_252d
    ECONOMIC RATIONALE: Acceleration of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(252).diff(_TD_MON)

def dras_306_upside_speed_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_306_upside_speed_accel_5d
    ECONOMIC RATIONALE: Acceleration of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(5).diff(_TD_MON)

def dras_307_upside_speed_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_307_upside_speed_accel_21d
    ECONOMIC RATIONALE: Acceleration of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(21).diff(_TD_MON)

def dras_308_upside_speed_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_308_upside_speed_accel_63d
    ECONOMIC RATIONALE: Acceleration of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(63).diff(_TD_MON)

def dras_309_upside_speed_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_309_upside_speed_accel_126d
    ECONOMIC RATIONALE: Acceleration of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(126).diff(_TD_MON)

def dras_310_upside_speed_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_310_upside_speed_accel_252d
    ECONOMIC RATIONALE: Acceleration of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(252).diff(_TD_MON)

def dras_311_recovery_asymmetry_ratio_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_311_recovery_asymmetry_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dras_312_recovery_asymmetry_ratio_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_312_recovery_asymmetry_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dras_313_recovery_asymmetry_ratio_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_313_recovery_asymmetry_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dras_314_recovery_asymmetry_ratio_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_314_recovery_asymmetry_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dras_315_recovery_asymmetry_ratio_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_315_recovery_asymmetry_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dras_316_drawdown_recovery_lag_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_316_drawdown_recovery_lag_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(5).diff(_TD_MON)

def dras_317_drawdown_recovery_lag_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_317_drawdown_recovery_lag_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(21).diff(_TD_MON)

def dras_318_drawdown_recovery_lag_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_318_drawdown_recovery_lag_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(63).diff(_TD_MON)

def dras_319_drawdown_recovery_lag_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_319_drawdown_recovery_lag_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(126).diff(_TD_MON)

def dras_320_drawdown_recovery_lag_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_320_drawdown_recovery_lag_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(252).diff(_TD_MON)

def dras_321_asymmetry_zscore_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_321_asymmetry_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(5).diff(_TD_MON)

def dras_322_asymmetry_zscore_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_322_asymmetry_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(21).diff(_TD_MON)

def dras_323_asymmetry_zscore_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_323_asymmetry_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(63).diff(_TD_MON)

def dras_324_asymmetry_zscore_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_324_asymmetry_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(126).diff(_TD_MON)

def dras_325_asymmetry_zscore_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_325_asymmetry_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(252).diff(_TD_MON)

def dras_326_drawdown_severity_skew_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_326_drawdown_severity_skew_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(5).diff(_TD_MON)

def dras_327_drawdown_severity_skew_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_327_drawdown_severity_skew_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(21).diff(_TD_MON)

def dras_328_drawdown_severity_skew_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_328_drawdown_severity_skew_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(63).diff(_TD_MON)

def dras_329_drawdown_severity_skew_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_329_drawdown_severity_skew_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(126).diff(_TD_MON)

def dras_330_drawdown_severity_skew_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_330_drawdown_severity_skew_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(252).diff(_TD_MON)

def dras_331_recovery_strength_index_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_331_recovery_strength_index_accel_5d
    ECONOMIC RATIONALE: Acceleration of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dras_332_recovery_strength_index_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_332_recovery_strength_index_accel_21d
    ECONOMIC RATIONALE: Acceleration of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dras_333_recovery_strength_index_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_333_recovery_strength_index_accel_63d
    ECONOMIC RATIONALE: Acceleration of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dras_334_recovery_strength_index_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_334_recovery_strength_index_accel_126d
    ECONOMIC RATIONALE: Acceleration of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dras_335_recovery_strength_index_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_335_recovery_strength_index_accel_252d
    ECONOMIC RATIONALE: Acceleration of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dras_336_asymmetry_momentum_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_336_asymmetry_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(5).diff(_TD_MON)

def dras_337_asymmetry_momentum_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_337_asymmetry_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(21).diff(_TD_MON)

def dras_338_asymmetry_momentum_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_338_asymmetry_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(63).diff(_TD_MON)

def dras_339_asymmetry_momentum_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_339_asymmetry_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(126).diff(_TD_MON)

def dras_340_asymmetry_momentum_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_340_asymmetry_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(252).diff(_TD_MON)

def dras_341_drawdown_velocity_z_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_341_drawdown_velocity_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(5).diff(_TD_MON)

def dras_342_drawdown_velocity_z_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_342_drawdown_velocity_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(21).diff(_TD_MON)

def dras_343_drawdown_velocity_z_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_343_drawdown_velocity_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(63).diff(_TD_MON)

def dras_344_drawdown_velocity_z_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_344_drawdown_velocity_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(126).diff(_TD_MON)

def dras_345_drawdown_velocity_z_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_345_drawdown_velocity_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(252).diff(_TD_MON)

def dras_346_recovery_efficiency_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_346_recovery_efficiency_accel_5d
    ECONOMIC RATIONALE: Acceleration of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dras_347_recovery_efficiency_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_347_recovery_efficiency_accel_21d
    ECONOMIC RATIONALE: Acceleration of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dras_348_recovery_efficiency_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_348_recovery_efficiency_accel_63d
    ECONOMIC RATIONALE: Acceleration of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dras_349_recovery_efficiency_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_349_recovery_efficiency_accel_126d
    ECONOMIC RATIONALE: Acceleration of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dras_350_recovery_efficiency_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_350_recovery_efficiency_accel_252d
    ECONOMIC RATIONALE: Acceleration of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dras_351_drawdown_efficiency_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_351_drawdown_efficiency_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(5).diff(_TD_MON)

def dras_352_drawdown_efficiency_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_352_drawdown_efficiency_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(21).diff(_TD_MON)

def dras_353_drawdown_efficiency_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_353_drawdown_efficiency_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(63).diff(_TD_MON)

def dras_354_drawdown_efficiency_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_354_drawdown_efficiency_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(126).diff(_TD_MON)

def dras_355_drawdown_efficiency_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_355_drawdown_efficiency_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(252).diff(_TD_MON)

def dras_356_asymmetry_regime_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_356_asymmetry_regime_accel_5d
    ECONOMIC RATIONALE: Acceleration of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(5).diff(_TD_MON)

def dras_357_asymmetry_regime_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_357_asymmetry_regime_accel_21d
    ECONOMIC RATIONALE: Acceleration of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(21).diff(_TD_MON)

def dras_358_asymmetry_regime_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_358_asymmetry_regime_accel_63d
    ECONOMIC RATIONALE: Acceleration of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(63).diff(_TD_MON)

def dras_359_asymmetry_regime_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_359_asymmetry_regime_accel_126d
    ECONOMIC RATIONALE: Acceleration of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(126).diff(_TD_MON)

def dras_360_asymmetry_regime_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_360_asymmetry_regime_accel_252d
    ECONOMIC RATIONALE: Acceleration of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(252).diff(_TD_MON)

def dras_361_sequential_drop_count_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_361_sequential_drop_count_accel_5d
    ECONOMIC RATIONALE: Acceleration of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(5).diff(_TD_MON)

def dras_362_sequential_drop_count_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_362_sequential_drop_count_accel_21d
    ECONOMIC RATIONALE: Acceleration of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(21).diff(_TD_MON)

def dras_363_sequential_drop_count_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_363_sequential_drop_count_accel_63d
    ECONOMIC RATIONALE: Acceleration of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(63).diff(_TD_MON)

def dras_364_sequential_drop_count_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_364_sequential_drop_count_accel_126d
    ECONOMIC RATIONALE: Acceleration of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(126).diff(_TD_MON)

def dras_365_sequential_drop_count_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_365_sequential_drop_count_accel_252d
    ECONOMIC RATIONALE: Acceleration of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(252).diff(_TD_MON)

def dras_366_sequential_rally_count_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_366_sequential_rally_count_accel_5d
    ECONOMIC RATIONALE: Acceleration of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(5).diff(_TD_MON)

def dras_367_sequential_rally_count_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_367_sequential_rally_count_accel_21d
    ECONOMIC RATIONALE: Acceleration of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(21).diff(_TD_MON)

def dras_368_sequential_rally_count_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_368_sequential_rally_count_accel_63d
    ECONOMIC RATIONALE: Acceleration of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(63).diff(_TD_MON)

def dras_369_sequential_rally_count_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_369_sequential_rally_count_accel_126d
    ECONOMIC RATIONALE: Acceleration of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(126).diff(_TD_MON)

def dras_370_sequential_rally_count_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_370_sequential_rally_count_accel_252d
    ECONOMIC RATIONALE: Acceleration of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(252).diff(_TD_MON)

def dras_371_drawdown_recovery_gap_accel_5d(close: pd.Series) -> pd.Series:
    """
    dras_371_drawdown_recovery_gap_accel_5d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(5).diff(_TD_MON)

def dras_372_drawdown_recovery_gap_accel_21d(close: pd.Series) -> pd.Series:
    """
    dras_372_drawdown_recovery_gap_accel_21d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(21).diff(_TD_MON)

def dras_373_drawdown_recovery_gap_accel_63d(close: pd.Series) -> pd.Series:
    """
    dras_373_drawdown_recovery_gap_accel_63d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(63).diff(_TD_MON)

def dras_374_drawdown_recovery_gap_accel_126d(close: pd.Series) -> pd.Series:
    """
    dras_374_drawdown_recovery_gap_accel_126d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(126).diff(_TD_MON)

def dras_375_drawdown_recovery_gap_accel_252d(close: pd.Series) -> pd.Series:
    """
    dras_375_drawdown_recovery_gap_accel_252d
    ECONOMIC RATIONALE: Acceleration of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V118_REGISTRY_ACCEL = {
    "dras_301_downside_speed_accel_5d": {"inputs": ["close"], "func": dras_301_downside_speed_accel_5d},
    "dras_302_downside_speed_accel_21d": {"inputs": ["close"], "func": dras_302_downside_speed_accel_21d},
    "dras_303_downside_speed_accel_63d": {"inputs": ["close"], "func": dras_303_downside_speed_accel_63d},
    "dras_304_downside_speed_accel_126d": {"inputs": ["close"], "func": dras_304_downside_speed_accel_126d},
    "dras_305_downside_speed_accel_252d": {"inputs": ["close"], "func": dras_305_downside_speed_accel_252d},
    "dras_306_upside_speed_accel_5d": {"inputs": ["close"], "func": dras_306_upside_speed_accel_5d},
    "dras_307_upside_speed_accel_21d": {"inputs": ["close"], "func": dras_307_upside_speed_accel_21d},
    "dras_308_upside_speed_accel_63d": {"inputs": ["close"], "func": dras_308_upside_speed_accel_63d},
    "dras_309_upside_speed_accel_126d": {"inputs": ["close"], "func": dras_309_upside_speed_accel_126d},
    "dras_310_upside_speed_accel_252d": {"inputs": ["close"], "func": dras_310_upside_speed_accel_252d},
    "dras_311_recovery_asymmetry_ratio_accel_5d": {"inputs": ["close"], "func": dras_311_recovery_asymmetry_ratio_accel_5d},
    "dras_312_recovery_asymmetry_ratio_accel_21d": {"inputs": ["close"], "func": dras_312_recovery_asymmetry_ratio_accel_21d},
    "dras_313_recovery_asymmetry_ratio_accel_63d": {"inputs": ["close"], "func": dras_313_recovery_asymmetry_ratio_accel_63d},
    "dras_314_recovery_asymmetry_ratio_accel_126d": {"inputs": ["close"], "func": dras_314_recovery_asymmetry_ratio_accel_126d},
    "dras_315_recovery_asymmetry_ratio_accel_252d": {"inputs": ["close"], "func": dras_315_recovery_asymmetry_ratio_accel_252d},
    "dras_316_drawdown_recovery_lag_accel_5d": {"inputs": ["close"], "func": dras_316_drawdown_recovery_lag_accel_5d},
    "dras_317_drawdown_recovery_lag_accel_21d": {"inputs": ["close"], "func": dras_317_drawdown_recovery_lag_accel_21d},
    "dras_318_drawdown_recovery_lag_accel_63d": {"inputs": ["close"], "func": dras_318_drawdown_recovery_lag_accel_63d},
    "dras_319_drawdown_recovery_lag_accel_126d": {"inputs": ["close"], "func": dras_319_drawdown_recovery_lag_accel_126d},
    "dras_320_drawdown_recovery_lag_accel_252d": {"inputs": ["close"], "func": dras_320_drawdown_recovery_lag_accel_252d},
    "dras_321_asymmetry_zscore_accel_5d": {"inputs": ["close"], "func": dras_321_asymmetry_zscore_accel_5d},
    "dras_322_asymmetry_zscore_accel_21d": {"inputs": ["close"], "func": dras_322_asymmetry_zscore_accel_21d},
    "dras_323_asymmetry_zscore_accel_63d": {"inputs": ["close"], "func": dras_323_asymmetry_zscore_accel_63d},
    "dras_324_asymmetry_zscore_accel_126d": {"inputs": ["close"], "func": dras_324_asymmetry_zscore_accel_126d},
    "dras_325_asymmetry_zscore_accel_252d": {"inputs": ["close"], "func": dras_325_asymmetry_zscore_accel_252d},
    "dras_326_drawdown_severity_skew_accel_5d": {"inputs": ["close"], "func": dras_326_drawdown_severity_skew_accel_5d},
    "dras_327_drawdown_severity_skew_accel_21d": {"inputs": ["close"], "func": dras_327_drawdown_severity_skew_accel_21d},
    "dras_328_drawdown_severity_skew_accel_63d": {"inputs": ["close"], "func": dras_328_drawdown_severity_skew_accel_63d},
    "dras_329_drawdown_severity_skew_accel_126d": {"inputs": ["close"], "func": dras_329_drawdown_severity_skew_accel_126d},
    "dras_330_drawdown_severity_skew_accel_252d": {"inputs": ["close"], "func": dras_330_drawdown_severity_skew_accel_252d},
    "dras_331_recovery_strength_index_accel_5d": {"inputs": ["close"], "func": dras_331_recovery_strength_index_accel_5d},
    "dras_332_recovery_strength_index_accel_21d": {"inputs": ["close"], "func": dras_332_recovery_strength_index_accel_21d},
    "dras_333_recovery_strength_index_accel_63d": {"inputs": ["close"], "func": dras_333_recovery_strength_index_accel_63d},
    "dras_334_recovery_strength_index_accel_126d": {"inputs": ["close"], "func": dras_334_recovery_strength_index_accel_126d},
    "dras_335_recovery_strength_index_accel_252d": {"inputs": ["close"], "func": dras_335_recovery_strength_index_accel_252d},
    "dras_336_asymmetry_momentum_accel_5d": {"inputs": ["close"], "func": dras_336_asymmetry_momentum_accel_5d},
    "dras_337_asymmetry_momentum_accel_21d": {"inputs": ["close"], "func": dras_337_asymmetry_momentum_accel_21d},
    "dras_338_asymmetry_momentum_accel_63d": {"inputs": ["close"], "func": dras_338_asymmetry_momentum_accel_63d},
    "dras_339_asymmetry_momentum_accel_126d": {"inputs": ["close"], "func": dras_339_asymmetry_momentum_accel_126d},
    "dras_340_asymmetry_momentum_accel_252d": {"inputs": ["close"], "func": dras_340_asymmetry_momentum_accel_252d},
    "dras_341_drawdown_velocity_z_accel_5d": {"inputs": ["close"], "func": dras_341_drawdown_velocity_z_accel_5d},
    "dras_342_drawdown_velocity_z_accel_21d": {"inputs": ["close"], "func": dras_342_drawdown_velocity_z_accel_21d},
    "dras_343_drawdown_velocity_z_accel_63d": {"inputs": ["close"], "func": dras_343_drawdown_velocity_z_accel_63d},
    "dras_344_drawdown_velocity_z_accel_126d": {"inputs": ["close"], "func": dras_344_drawdown_velocity_z_accel_126d},
    "dras_345_drawdown_velocity_z_accel_252d": {"inputs": ["close"], "func": dras_345_drawdown_velocity_z_accel_252d},
    "dras_346_recovery_efficiency_accel_5d": {"inputs": ["close"], "func": dras_346_recovery_efficiency_accel_5d},
    "dras_347_recovery_efficiency_accel_21d": {"inputs": ["close"], "func": dras_347_recovery_efficiency_accel_21d},
    "dras_348_recovery_efficiency_accel_63d": {"inputs": ["close"], "func": dras_348_recovery_efficiency_accel_63d},
    "dras_349_recovery_efficiency_accel_126d": {"inputs": ["close"], "func": dras_349_recovery_efficiency_accel_126d},
    "dras_350_recovery_efficiency_accel_252d": {"inputs": ["close"], "func": dras_350_recovery_efficiency_accel_252d},
    "dras_351_drawdown_efficiency_accel_5d": {"inputs": ["close"], "func": dras_351_drawdown_efficiency_accel_5d},
    "dras_352_drawdown_efficiency_accel_21d": {"inputs": ["close"], "func": dras_352_drawdown_efficiency_accel_21d},
    "dras_353_drawdown_efficiency_accel_63d": {"inputs": ["close"], "func": dras_353_drawdown_efficiency_accel_63d},
    "dras_354_drawdown_efficiency_accel_126d": {"inputs": ["close"], "func": dras_354_drawdown_efficiency_accel_126d},
    "dras_355_drawdown_efficiency_accel_252d": {"inputs": ["close"], "func": dras_355_drawdown_efficiency_accel_252d},
    "dras_356_asymmetry_regime_accel_5d": {"inputs": ["close"], "func": dras_356_asymmetry_regime_accel_5d},
    "dras_357_asymmetry_regime_accel_21d": {"inputs": ["close"], "func": dras_357_asymmetry_regime_accel_21d},
    "dras_358_asymmetry_regime_accel_63d": {"inputs": ["close"], "func": dras_358_asymmetry_regime_accel_63d},
    "dras_359_asymmetry_regime_accel_126d": {"inputs": ["close"], "func": dras_359_asymmetry_regime_accel_126d},
    "dras_360_asymmetry_regime_accel_252d": {"inputs": ["close"], "func": dras_360_asymmetry_regime_accel_252d},
    "dras_361_sequential_drop_count_accel_5d": {"inputs": ["close"], "func": dras_361_sequential_drop_count_accel_5d},
    "dras_362_sequential_drop_count_accel_21d": {"inputs": ["close"], "func": dras_362_sequential_drop_count_accel_21d},
    "dras_363_sequential_drop_count_accel_63d": {"inputs": ["close"], "func": dras_363_sequential_drop_count_accel_63d},
    "dras_364_sequential_drop_count_accel_126d": {"inputs": ["close"], "func": dras_364_sequential_drop_count_accel_126d},
    "dras_365_sequential_drop_count_accel_252d": {"inputs": ["close"], "func": dras_365_sequential_drop_count_accel_252d},
    "dras_366_sequential_rally_count_accel_5d": {"inputs": ["close"], "func": dras_366_sequential_rally_count_accel_5d},
    "dras_367_sequential_rally_count_accel_21d": {"inputs": ["close"], "func": dras_367_sequential_rally_count_accel_21d},
    "dras_368_sequential_rally_count_accel_63d": {"inputs": ["close"], "func": dras_368_sequential_rally_count_accel_63d},
    "dras_369_sequential_rally_count_accel_126d": {"inputs": ["close"], "func": dras_369_sequential_rally_count_accel_126d},
    "dras_370_sequential_rally_count_accel_252d": {"inputs": ["close"], "func": dras_370_sequential_rally_count_accel_252d},
    "dras_371_drawdown_recovery_gap_accel_5d": {"inputs": ["close"], "func": dras_371_drawdown_recovery_gap_accel_5d},
    "dras_372_drawdown_recovery_gap_accel_21d": {"inputs": ["close"], "func": dras_372_drawdown_recovery_gap_accel_21d},
    "dras_373_drawdown_recovery_gap_accel_63d": {"inputs": ["close"], "func": dras_373_drawdown_recovery_gap_accel_63d},
    "dras_374_drawdown_recovery_gap_accel_126d": {"inputs": ["close"], "func": dras_374_drawdown_recovery_gap_accel_126d},
    "dras_375_drawdown_recovery_gap_accel_252d": {"inputs": ["close"], "func": dras_375_drawdown_recovery_gap_accel_252d},
}
