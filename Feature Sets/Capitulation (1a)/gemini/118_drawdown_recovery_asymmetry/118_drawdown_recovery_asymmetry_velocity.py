"""
118_drawdown_recovery_asymmetry — Velocity (2nd Derivatives)
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

def dras_226_downside_speed_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_226_downside_speed_vel_5d
    ECONOMIC RATIONALE: Velocity of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(5)

def dras_227_downside_speed_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_227_downside_speed_vel_21d
    ECONOMIC RATIONALE: Velocity of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(21)

def dras_228_downside_speed_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_228_downside_speed_vel_63d
    ECONOMIC RATIONALE: Velocity of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(63)

def dras_229_downside_speed_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_229_downside_speed_vel_126d
    ECONOMIC RATIONALE: Velocity of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(126)

def dras_230_downside_speed_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_230_downside_speed_vel_252d
    ECONOMIC RATIONALE: Velocity of downside_speed. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).diff(252)

def dras_231_upside_speed_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_231_upside_speed_vel_5d
    ECONOMIC RATIONALE: Velocity of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(5)

def dras_232_upside_speed_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_232_upside_speed_vel_21d
    ECONOMIC RATIONALE: Velocity of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(21)

def dras_233_upside_speed_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_233_upside_speed_vel_63d
    ECONOMIC RATIONALE: Velocity of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(63)

def dras_234_upside_speed_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_234_upside_speed_vel_126d
    ECONOMIC RATIONALE: Velocity of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(126)

def dras_235_upside_speed_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_235_upside_speed_vel_252d
    ECONOMIC RATIONALE: Velocity of upside_speed. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).diff(252)

def dras_236_recovery_asymmetry_ratio_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_236_recovery_asymmetry_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(5)

def dras_237_recovery_asymmetry_ratio_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_237_recovery_asymmetry_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(21)

def dras_238_recovery_asymmetry_ratio_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_238_recovery_asymmetry_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(63)

def dras_239_recovery_asymmetry_ratio_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_239_recovery_asymmetry_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(126)

def dras_240_recovery_asymmetry_ratio_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_240_recovery_asymmetry_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of recovery_asymmetry_ratio. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).diff(252)

def dras_241_drawdown_recovery_lag_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_241_drawdown_recovery_lag_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(5)

def dras_242_drawdown_recovery_lag_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_242_drawdown_recovery_lag_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(21)

def dras_243_drawdown_recovery_lag_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_243_drawdown_recovery_lag_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(63)

def dras_244_drawdown_recovery_lag_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_244_drawdown_recovery_lag_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(126)

def dras_245_drawdown_recovery_lag_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_245_drawdown_recovery_lag_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_lag. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).diff(252)

def dras_246_asymmetry_zscore_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_246_asymmetry_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(5)

def dras_247_asymmetry_zscore_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_247_asymmetry_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(21)

def dras_248_asymmetry_zscore_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_248_asymmetry_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(63)

def dras_249_asymmetry_zscore_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_249_asymmetry_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(126)

def dras_250_asymmetry_zscore_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_250_asymmetry_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of asymmetry_zscore. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).diff(252)

def dras_251_drawdown_severity_skew_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_251_drawdown_severity_skew_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(5)

def dras_252_drawdown_severity_skew_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_252_drawdown_severity_skew_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(21)

def dras_253_drawdown_severity_skew_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_253_drawdown_severity_skew_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(63)

def dras_254_drawdown_severity_skew_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_254_drawdown_severity_skew_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(126)

def dras_255_drawdown_severity_skew_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_255_drawdown_severity_skew_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_severity_skew. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).diff(252)

def dras_256_recovery_strength_index_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_256_recovery_strength_index_vel_5d
    ECONOMIC RATIONALE: Velocity of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(5)

def dras_257_recovery_strength_index_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_257_recovery_strength_index_vel_21d
    ECONOMIC RATIONALE: Velocity of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(21)

def dras_258_recovery_strength_index_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_258_recovery_strength_index_vel_63d
    ECONOMIC RATIONALE: Velocity of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(63)

def dras_259_recovery_strength_index_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_259_recovery_strength_index_vel_126d
    ECONOMIC RATIONALE: Velocity of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(126)

def dras_260_recovery_strength_index_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_260_recovery_strength_index_vel_252d
    ECONOMIC RATIONALE: Velocity of recovery_strength_index. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).diff(252)

def dras_261_asymmetry_momentum_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_261_asymmetry_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(5)

def dras_262_asymmetry_momentum_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_262_asymmetry_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(21)

def dras_263_asymmetry_momentum_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_263_asymmetry_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(63)

def dras_264_asymmetry_momentum_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_264_asymmetry_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(126)

def dras_265_asymmetry_momentum_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_265_asymmetry_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of asymmetry_momentum. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).diff(252)

def dras_266_drawdown_velocity_z_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_266_drawdown_velocity_z_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(5)

def dras_267_drawdown_velocity_z_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_267_drawdown_velocity_z_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(21)

def dras_268_drawdown_velocity_z_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_268_drawdown_velocity_z_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(63)

def dras_269_drawdown_velocity_z_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_269_drawdown_velocity_z_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(126)

def dras_270_drawdown_velocity_z_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_270_drawdown_velocity_z_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_velocity_z. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).diff(252)

def dras_271_recovery_efficiency_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_271_recovery_efficiency_vel_5d
    ECONOMIC RATIONALE: Velocity of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(5)

def dras_272_recovery_efficiency_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_272_recovery_efficiency_vel_21d
    ECONOMIC RATIONALE: Velocity of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(21)

def dras_273_recovery_efficiency_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_273_recovery_efficiency_vel_63d
    ECONOMIC RATIONALE: Velocity of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(63)

def dras_274_recovery_efficiency_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_274_recovery_efficiency_vel_126d
    ECONOMIC RATIONALE: Velocity of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(126)

def dras_275_recovery_efficiency_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_275_recovery_efficiency_vel_252d
    ECONOMIC RATIONALE: Velocity of recovery_efficiency. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).diff(252)

def dras_276_drawdown_efficiency_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_276_drawdown_efficiency_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(5)

def dras_277_drawdown_efficiency_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_277_drawdown_efficiency_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(21)

def dras_278_drawdown_efficiency_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_278_drawdown_efficiency_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(63)

def dras_279_drawdown_efficiency_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_279_drawdown_efficiency_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(126)

def dras_280_drawdown_efficiency_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_280_drawdown_efficiency_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_efficiency. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).diff(252)

def dras_281_asymmetry_regime_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_281_asymmetry_regime_vel_5d
    ECONOMIC RATIONALE: Velocity of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(5)

def dras_282_asymmetry_regime_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_282_asymmetry_regime_vel_21d
    ECONOMIC RATIONALE: Velocity of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(21)

def dras_283_asymmetry_regime_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_283_asymmetry_regime_vel_63d
    ECONOMIC RATIONALE: Velocity of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(63)

def dras_284_asymmetry_regime_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_284_asymmetry_regime_vel_126d
    ECONOMIC RATIONALE: Velocity of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(126)

def dras_285_asymmetry_regime_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_285_asymmetry_regime_vel_252d
    ECONOMIC RATIONALE: Velocity of asymmetry_regime. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).diff(252)

def dras_286_sequential_drop_count_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_286_sequential_drop_count_vel_5d
    ECONOMIC RATIONALE: Velocity of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(5)

def dras_287_sequential_drop_count_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_287_sequential_drop_count_vel_21d
    ECONOMIC RATIONALE: Velocity of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(21)

def dras_288_sequential_drop_count_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_288_sequential_drop_count_vel_63d
    ECONOMIC RATIONALE: Velocity of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(63)

def dras_289_sequential_drop_count_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_289_sequential_drop_count_vel_126d
    ECONOMIC RATIONALE: Velocity of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(126)

def dras_290_sequential_drop_count_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_290_sequential_drop_count_vel_252d
    ECONOMIC RATIONALE: Velocity of sequential_drop_count. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).diff(252)

def dras_291_sequential_rally_count_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_291_sequential_rally_count_vel_5d
    ECONOMIC RATIONALE: Velocity of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(5)

def dras_292_sequential_rally_count_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_292_sequential_rally_count_vel_21d
    ECONOMIC RATIONALE: Velocity of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(21)

def dras_293_sequential_rally_count_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_293_sequential_rally_count_vel_63d
    ECONOMIC RATIONALE: Velocity of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(63)

def dras_294_sequential_rally_count_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_294_sequential_rally_count_vel_126d
    ECONOMIC RATIONALE: Velocity of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(126)

def dras_295_sequential_rally_count_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_295_sequential_rally_count_vel_252d
    ECONOMIC RATIONALE: Velocity of sequential_rally_count. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).diff(252)

def dras_296_drawdown_recovery_gap_vel_5d(close: pd.Series) -> pd.Series:
    """
    dras_296_drawdown_recovery_gap_vel_5d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(5)

def dras_297_drawdown_recovery_gap_vel_21d(close: pd.Series) -> pd.Series:
    """
    dras_297_drawdown_recovery_gap_vel_21d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(21)

def dras_298_drawdown_recovery_gap_vel_63d(close: pd.Series) -> pd.Series:
    """
    dras_298_drawdown_recovery_gap_vel_63d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(63)

def dras_299_drawdown_recovery_gap_vel_126d(close: pd.Series) -> pd.Series:
    """
    dras_299_drawdown_recovery_gap_vel_126d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(126)

def dras_300_drawdown_recovery_gap_vel_252d(close: pd.Series) -> pd.Series:
    """
    dras_300_drawdown_recovery_gap_vel_252d
    ECONOMIC RATIONALE: Velocity of drawdown_recovery_gap. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V118_REGISTRY_VEL = {
    "dras_226_downside_speed_vel_5d": {"inputs": ["close"], "func": dras_226_downside_speed_vel_5d},
    "dras_227_downside_speed_vel_21d": {"inputs": ["close"], "func": dras_227_downside_speed_vel_21d},
    "dras_228_downside_speed_vel_63d": {"inputs": ["close"], "func": dras_228_downside_speed_vel_63d},
    "dras_229_downside_speed_vel_126d": {"inputs": ["close"], "func": dras_229_downside_speed_vel_126d},
    "dras_230_downside_speed_vel_252d": {"inputs": ["close"], "func": dras_230_downside_speed_vel_252d},
    "dras_231_upside_speed_vel_5d": {"inputs": ["close"], "func": dras_231_upside_speed_vel_5d},
    "dras_232_upside_speed_vel_21d": {"inputs": ["close"], "func": dras_232_upside_speed_vel_21d},
    "dras_233_upside_speed_vel_63d": {"inputs": ["close"], "func": dras_233_upside_speed_vel_63d},
    "dras_234_upside_speed_vel_126d": {"inputs": ["close"], "func": dras_234_upside_speed_vel_126d},
    "dras_235_upside_speed_vel_252d": {"inputs": ["close"], "func": dras_235_upside_speed_vel_252d},
    "dras_236_recovery_asymmetry_ratio_vel_5d": {"inputs": ["close"], "func": dras_236_recovery_asymmetry_ratio_vel_5d},
    "dras_237_recovery_asymmetry_ratio_vel_21d": {"inputs": ["close"], "func": dras_237_recovery_asymmetry_ratio_vel_21d},
    "dras_238_recovery_asymmetry_ratio_vel_63d": {"inputs": ["close"], "func": dras_238_recovery_asymmetry_ratio_vel_63d},
    "dras_239_recovery_asymmetry_ratio_vel_126d": {"inputs": ["close"], "func": dras_239_recovery_asymmetry_ratio_vel_126d},
    "dras_240_recovery_asymmetry_ratio_vel_252d": {"inputs": ["close"], "func": dras_240_recovery_asymmetry_ratio_vel_252d},
    "dras_241_drawdown_recovery_lag_vel_5d": {"inputs": ["close"], "func": dras_241_drawdown_recovery_lag_vel_5d},
    "dras_242_drawdown_recovery_lag_vel_21d": {"inputs": ["close"], "func": dras_242_drawdown_recovery_lag_vel_21d},
    "dras_243_drawdown_recovery_lag_vel_63d": {"inputs": ["close"], "func": dras_243_drawdown_recovery_lag_vel_63d},
    "dras_244_drawdown_recovery_lag_vel_126d": {"inputs": ["close"], "func": dras_244_drawdown_recovery_lag_vel_126d},
    "dras_245_drawdown_recovery_lag_vel_252d": {"inputs": ["close"], "func": dras_245_drawdown_recovery_lag_vel_252d},
    "dras_246_asymmetry_zscore_vel_5d": {"inputs": ["close"], "func": dras_246_asymmetry_zscore_vel_5d},
    "dras_247_asymmetry_zscore_vel_21d": {"inputs": ["close"], "func": dras_247_asymmetry_zscore_vel_21d},
    "dras_248_asymmetry_zscore_vel_63d": {"inputs": ["close"], "func": dras_248_asymmetry_zscore_vel_63d},
    "dras_249_asymmetry_zscore_vel_126d": {"inputs": ["close"], "func": dras_249_asymmetry_zscore_vel_126d},
    "dras_250_asymmetry_zscore_vel_252d": {"inputs": ["close"], "func": dras_250_asymmetry_zscore_vel_252d},
    "dras_251_drawdown_severity_skew_vel_5d": {"inputs": ["close"], "func": dras_251_drawdown_severity_skew_vel_5d},
    "dras_252_drawdown_severity_skew_vel_21d": {"inputs": ["close"], "func": dras_252_drawdown_severity_skew_vel_21d},
    "dras_253_drawdown_severity_skew_vel_63d": {"inputs": ["close"], "func": dras_253_drawdown_severity_skew_vel_63d},
    "dras_254_drawdown_severity_skew_vel_126d": {"inputs": ["close"], "func": dras_254_drawdown_severity_skew_vel_126d},
    "dras_255_drawdown_severity_skew_vel_252d": {"inputs": ["close"], "func": dras_255_drawdown_severity_skew_vel_252d},
    "dras_256_recovery_strength_index_vel_5d": {"inputs": ["close"], "func": dras_256_recovery_strength_index_vel_5d},
    "dras_257_recovery_strength_index_vel_21d": {"inputs": ["close"], "func": dras_257_recovery_strength_index_vel_21d},
    "dras_258_recovery_strength_index_vel_63d": {"inputs": ["close"], "func": dras_258_recovery_strength_index_vel_63d},
    "dras_259_recovery_strength_index_vel_126d": {"inputs": ["close"], "func": dras_259_recovery_strength_index_vel_126d},
    "dras_260_recovery_strength_index_vel_252d": {"inputs": ["close"], "func": dras_260_recovery_strength_index_vel_252d},
    "dras_261_asymmetry_momentum_vel_5d": {"inputs": ["close"], "func": dras_261_asymmetry_momentum_vel_5d},
    "dras_262_asymmetry_momentum_vel_21d": {"inputs": ["close"], "func": dras_262_asymmetry_momentum_vel_21d},
    "dras_263_asymmetry_momentum_vel_63d": {"inputs": ["close"], "func": dras_263_asymmetry_momentum_vel_63d},
    "dras_264_asymmetry_momentum_vel_126d": {"inputs": ["close"], "func": dras_264_asymmetry_momentum_vel_126d},
    "dras_265_asymmetry_momentum_vel_252d": {"inputs": ["close"], "func": dras_265_asymmetry_momentum_vel_252d},
    "dras_266_drawdown_velocity_z_vel_5d": {"inputs": ["close"], "func": dras_266_drawdown_velocity_z_vel_5d},
    "dras_267_drawdown_velocity_z_vel_21d": {"inputs": ["close"], "func": dras_267_drawdown_velocity_z_vel_21d},
    "dras_268_drawdown_velocity_z_vel_63d": {"inputs": ["close"], "func": dras_268_drawdown_velocity_z_vel_63d},
    "dras_269_drawdown_velocity_z_vel_126d": {"inputs": ["close"], "func": dras_269_drawdown_velocity_z_vel_126d},
    "dras_270_drawdown_velocity_z_vel_252d": {"inputs": ["close"], "func": dras_270_drawdown_velocity_z_vel_252d},
    "dras_271_recovery_efficiency_vel_5d": {"inputs": ["close"], "func": dras_271_recovery_efficiency_vel_5d},
    "dras_272_recovery_efficiency_vel_21d": {"inputs": ["close"], "func": dras_272_recovery_efficiency_vel_21d},
    "dras_273_recovery_efficiency_vel_63d": {"inputs": ["close"], "func": dras_273_recovery_efficiency_vel_63d},
    "dras_274_recovery_efficiency_vel_126d": {"inputs": ["close"], "func": dras_274_recovery_efficiency_vel_126d},
    "dras_275_recovery_efficiency_vel_252d": {"inputs": ["close"], "func": dras_275_recovery_efficiency_vel_252d},
    "dras_276_drawdown_efficiency_vel_5d": {"inputs": ["close"], "func": dras_276_drawdown_efficiency_vel_5d},
    "dras_277_drawdown_efficiency_vel_21d": {"inputs": ["close"], "func": dras_277_drawdown_efficiency_vel_21d},
    "dras_278_drawdown_efficiency_vel_63d": {"inputs": ["close"], "func": dras_278_drawdown_efficiency_vel_63d},
    "dras_279_drawdown_efficiency_vel_126d": {"inputs": ["close"], "func": dras_279_drawdown_efficiency_vel_126d},
    "dras_280_drawdown_efficiency_vel_252d": {"inputs": ["close"], "func": dras_280_drawdown_efficiency_vel_252d},
    "dras_281_asymmetry_regime_vel_5d": {"inputs": ["close"], "func": dras_281_asymmetry_regime_vel_5d},
    "dras_282_asymmetry_regime_vel_21d": {"inputs": ["close"], "func": dras_282_asymmetry_regime_vel_21d},
    "dras_283_asymmetry_regime_vel_63d": {"inputs": ["close"], "func": dras_283_asymmetry_regime_vel_63d},
    "dras_284_asymmetry_regime_vel_126d": {"inputs": ["close"], "func": dras_284_asymmetry_regime_vel_126d},
    "dras_285_asymmetry_regime_vel_252d": {"inputs": ["close"], "func": dras_285_asymmetry_regime_vel_252d},
    "dras_286_sequential_drop_count_vel_5d": {"inputs": ["close"], "func": dras_286_sequential_drop_count_vel_5d},
    "dras_287_sequential_drop_count_vel_21d": {"inputs": ["close"], "func": dras_287_sequential_drop_count_vel_21d},
    "dras_288_sequential_drop_count_vel_63d": {"inputs": ["close"], "func": dras_288_sequential_drop_count_vel_63d},
    "dras_289_sequential_drop_count_vel_126d": {"inputs": ["close"], "func": dras_289_sequential_drop_count_vel_126d},
    "dras_290_sequential_drop_count_vel_252d": {"inputs": ["close"], "func": dras_290_sequential_drop_count_vel_252d},
    "dras_291_sequential_rally_count_vel_5d": {"inputs": ["close"], "func": dras_291_sequential_rally_count_vel_5d},
    "dras_292_sequential_rally_count_vel_21d": {"inputs": ["close"], "func": dras_292_sequential_rally_count_vel_21d},
    "dras_293_sequential_rally_count_vel_63d": {"inputs": ["close"], "func": dras_293_sequential_rally_count_vel_63d},
    "dras_294_sequential_rally_count_vel_126d": {"inputs": ["close"], "func": dras_294_sequential_rally_count_vel_126d},
    "dras_295_sequential_rally_count_vel_252d": {"inputs": ["close"], "func": dras_295_sequential_rally_count_vel_252d},
    "dras_296_drawdown_recovery_gap_vel_5d": {"inputs": ["close"], "func": dras_296_drawdown_recovery_gap_vel_5d},
    "dras_297_drawdown_recovery_gap_vel_21d": {"inputs": ["close"], "func": dras_297_drawdown_recovery_gap_vel_21d},
    "dras_298_drawdown_recovery_gap_vel_63d": {"inputs": ["close"], "func": dras_298_drawdown_recovery_gap_vel_63d},
    "dras_299_drawdown_recovery_gap_vel_126d": {"inputs": ["close"], "func": dras_299_drawdown_recovery_gap_vel_126d},
    "dras_300_drawdown_recovery_gap_vel_252d": {"inputs": ["close"], "func": dras_300_drawdown_recovery_gap_vel_252d},
}
