"""
116_extreme_day_density — Acceleration (3rd Derivatives)
Domain: extreme_day_density
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

def exdd_301_extreme_down_day_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_301_extreme_down_day_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(5).diff(_TD_MON)

def exdd_302_extreme_down_day_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_302_extreme_down_day_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(21).diff(_TD_MON)

def exdd_303_extreme_down_day_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_303_extreme_down_day_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(63).diff(_TD_MON)

def exdd_304_extreme_down_day_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_304_extreme_down_day_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(126).diff(_TD_MON)

def exdd_305_extreme_down_day_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_305_extreme_down_day_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(252).diff(_TD_MON)

def exdd_306_extreme_up_day_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_306_extreme_up_day_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(5).diff(_TD_MON)

def exdd_307_extreme_up_day_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_307_extreme_up_day_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(21).diff(_TD_MON)

def exdd_308_extreme_up_day_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_308_extreme_up_day_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(63).diff(_TD_MON)

def exdd_309_extreme_up_day_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_309_extreme_up_day_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(126).diff(_TD_MON)

def exdd_310_extreme_up_day_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_310_extreme_up_day_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(252).diff(_TD_MON)

def exdd_311_extreme_vol_day_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_311_extreme_vol_day_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(5).diff(_TD_MON)

def exdd_312_extreme_vol_day_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_312_extreme_vol_day_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(21).diff(_TD_MON)

def exdd_313_extreme_vol_day_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_313_extreme_vol_day_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(63).diff(_TD_MON)

def exdd_314_extreme_vol_day_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_314_extreme_vol_day_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(126).diff(_TD_MON)

def exdd_315_extreme_vol_day_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_315_extreme_vol_day_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(252).diff(_TD_MON)

def exdd_316_extreme_day_cluster_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_316_extreme_day_cluster_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(5).diff(_TD_MON)

def exdd_317_extreme_day_cluster_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_317_extreme_day_cluster_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(21).diff(_TD_MON)

def exdd_318_extreme_day_cluster_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_318_extreme_day_cluster_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(63).diff(_TD_MON)

def exdd_319_extreme_day_cluster_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_319_extreme_day_cluster_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(126).diff(_TD_MON)

def exdd_320_extreme_day_cluster_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_320_extreme_day_cluster_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(252).diff(_TD_MON)

def exdd_321_extreme_day_bias_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_321_extreme_day_bias_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(5).diff(_TD_MON)

def exdd_322_extreme_day_bias_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_322_extreme_day_bias_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(21).diff(_TD_MON)

def exdd_323_extreme_day_bias_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_323_extreme_day_bias_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(63).diff(_TD_MON)

def exdd_324_extreme_day_bias_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_324_extreme_day_bias_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(126).diff(_TD_MON)

def exdd_325_extreme_day_bias_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_325_extreme_day_bias_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(252).diff(_TD_MON)

def exdd_326_extreme_vol_price_sync_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_326_extreme_vol_price_sync_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(5).diff(_TD_MON)

def exdd_327_extreme_vol_price_sync_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_327_extreme_vol_price_sync_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(21).diff(_TD_MON)

def exdd_328_extreme_vol_price_sync_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_328_extreme_vol_price_sync_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(63).diff(_TD_MON)

def exdd_329_extreme_vol_price_sync_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_329_extreme_vol_price_sync_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(126).diff(_TD_MON)

def exdd_330_extreme_vol_price_sync_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_330_extreme_vol_price_sync_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(252).diff(_TD_MON)

def exdd_331_extreme_day_z_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_331_extreme_day_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(5).diff(_TD_MON)

def exdd_332_extreme_day_z_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_332_extreme_day_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(21).diff(_TD_MON)

def exdd_333_extreme_day_z_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_333_extreme_day_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(63).diff(_TD_MON)

def exdd_334_extreme_day_z_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_334_extreme_day_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(126).diff(_TD_MON)

def exdd_335_extreme_day_z_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_335_extreme_day_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(252).diff(_TD_MON)

def exdd_336_extreme_day_momentum_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_336_extreme_day_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(5).diff(_TD_MON)

def exdd_337_extreme_day_momentum_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_337_extreme_day_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(21).diff(_TD_MON)

def exdd_338_extreme_day_momentum_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_338_extreme_day_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(63).diff(_TD_MON)

def exdd_339_extreme_day_momentum_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_339_extreme_day_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(126).diff(_TD_MON)

def exdd_340_extreme_day_momentum_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_340_extreme_day_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(252).diff(_TD_MON)

def exdd_341_extreme_range_day_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_341_extreme_range_day_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(5).diff(_TD_MON)

def exdd_342_extreme_range_day_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_342_extreme_range_day_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(21).diff(_TD_MON)

def exdd_343_extreme_range_day_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_343_extreme_range_day_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(63).diff(_TD_MON)

def exdd_344_extreme_range_day_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_344_extreme_range_day_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(126).diff(_TD_MON)

def exdd_345_extreme_range_day_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_345_extreme_range_day_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(252).diff(_TD_MON)

def exdd_346_extreme_gap_day_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_346_extreme_gap_day_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(5).diff(_TD_MON)

def exdd_347_extreme_gap_day_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_347_extreme_gap_day_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(21).diff(_TD_MON)

def exdd_348_extreme_gap_day_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_348_extreme_gap_day_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(63).diff(_TD_MON)

def exdd_349_extreme_gap_day_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_349_extreme_gap_day_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(126).diff(_TD_MON)

def exdd_350_extreme_gap_day_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_350_extreme_gap_day_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(252).diff(_TD_MON)

def exdd_351_extreme_day_persistence_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_351_extreme_day_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(5).diff(_TD_MON)

def exdd_352_extreme_day_persistence_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_352_extreme_day_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(21).diff(_TD_MON)

def exdd_353_extreme_day_persistence_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_353_extreme_day_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(63).diff(_TD_MON)

def exdd_354_extreme_day_persistence_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_354_extreme_day_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(126).diff(_TD_MON)

def exdd_355_extreme_day_persistence_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_355_extreme_day_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(252).diff(_TD_MON)

def exdd_356_extreme_day_decay_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_356_extreme_day_decay_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(5).diff(_TD_MON)

def exdd_357_extreme_day_decay_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_357_extreme_day_decay_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(21).diff(_TD_MON)

def exdd_358_extreme_day_decay_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_358_extreme_day_decay_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(63).diff(_TD_MON)

def exdd_359_extreme_day_decay_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_359_extreme_day_decay_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(126).diff(_TD_MON)

def exdd_360_extreme_day_decay_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_360_extreme_day_decay_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(252).diff(_TD_MON)

def exdd_361_extreme_day_vol_ratio_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_361_extreme_day_vol_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(5).diff(_TD_MON)

def exdd_362_extreme_day_vol_ratio_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_362_extreme_day_vol_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(21).diff(_TD_MON)

def exdd_363_extreme_day_vol_ratio_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_363_extreme_day_vol_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(63).diff(_TD_MON)

def exdd_364_extreme_day_vol_ratio_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_364_extreme_day_vol_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(126).diff(_TD_MON)

def exdd_365_extreme_day_vol_ratio_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_365_extreme_day_vol_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(252).diff(_TD_MON)

def exdd_366_extreme_day_regime_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_366_extreme_day_regime_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(5).diff(_TD_MON)

def exdd_367_extreme_day_regime_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_367_extreme_day_regime_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(21).diff(_TD_MON)

def exdd_368_extreme_day_regime_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_368_extreme_day_regime_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(63).diff(_TD_MON)

def exdd_369_extreme_day_regime_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_369_extreme_day_regime_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(126).diff(_TD_MON)

def exdd_370_extreme_day_regime_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_370_extreme_day_regime_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(252).diff(_TD_MON)

def exdd_371_extreme_day_exhaustion_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_371_extreme_day_exhaustion_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(5).diff(_TD_MON)

def exdd_372_extreme_day_exhaustion_accel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_372_extreme_day_exhaustion_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(21).diff(_TD_MON)

def exdd_373_extreme_day_exhaustion_accel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_373_extreme_day_exhaustion_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(63).diff(_TD_MON)

def exdd_374_extreme_day_exhaustion_accel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_374_extreme_day_exhaustion_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(126).diff(_TD_MON)

def exdd_375_extreme_day_exhaustion_accel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_375_extreme_day_exhaustion_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V116_REGISTRY_ACCEL = {
    "exdd_301_extreme_down_day_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_301_extreme_down_day_accel_5d},
    "exdd_302_extreme_down_day_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_302_extreme_down_day_accel_21d},
    "exdd_303_extreme_down_day_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_303_extreme_down_day_accel_63d},
    "exdd_304_extreme_down_day_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_304_extreme_down_day_accel_126d},
    "exdd_305_extreme_down_day_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_305_extreme_down_day_accel_252d},
    "exdd_306_extreme_up_day_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_306_extreme_up_day_accel_5d},
    "exdd_307_extreme_up_day_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_307_extreme_up_day_accel_21d},
    "exdd_308_extreme_up_day_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_308_extreme_up_day_accel_63d},
    "exdd_309_extreme_up_day_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_309_extreme_up_day_accel_126d},
    "exdd_310_extreme_up_day_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_310_extreme_up_day_accel_252d},
    "exdd_311_extreme_vol_day_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_311_extreme_vol_day_accel_5d},
    "exdd_312_extreme_vol_day_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_312_extreme_vol_day_accel_21d},
    "exdd_313_extreme_vol_day_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_313_extreme_vol_day_accel_63d},
    "exdd_314_extreme_vol_day_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_314_extreme_vol_day_accel_126d},
    "exdd_315_extreme_vol_day_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_315_extreme_vol_day_accel_252d},
    "exdd_316_extreme_day_cluster_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_316_extreme_day_cluster_accel_5d},
    "exdd_317_extreme_day_cluster_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_317_extreme_day_cluster_accel_21d},
    "exdd_318_extreme_day_cluster_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_318_extreme_day_cluster_accel_63d},
    "exdd_319_extreme_day_cluster_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_319_extreme_day_cluster_accel_126d},
    "exdd_320_extreme_day_cluster_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_320_extreme_day_cluster_accel_252d},
    "exdd_321_extreme_day_bias_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_321_extreme_day_bias_accel_5d},
    "exdd_322_extreme_day_bias_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_322_extreme_day_bias_accel_21d},
    "exdd_323_extreme_day_bias_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_323_extreme_day_bias_accel_63d},
    "exdd_324_extreme_day_bias_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_324_extreme_day_bias_accel_126d},
    "exdd_325_extreme_day_bias_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_325_extreme_day_bias_accel_252d},
    "exdd_326_extreme_vol_price_sync_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_326_extreme_vol_price_sync_accel_5d},
    "exdd_327_extreme_vol_price_sync_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_327_extreme_vol_price_sync_accel_21d},
    "exdd_328_extreme_vol_price_sync_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_328_extreme_vol_price_sync_accel_63d},
    "exdd_329_extreme_vol_price_sync_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_329_extreme_vol_price_sync_accel_126d},
    "exdd_330_extreme_vol_price_sync_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_330_extreme_vol_price_sync_accel_252d},
    "exdd_331_extreme_day_z_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_331_extreme_day_z_accel_5d},
    "exdd_332_extreme_day_z_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_332_extreme_day_z_accel_21d},
    "exdd_333_extreme_day_z_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_333_extreme_day_z_accel_63d},
    "exdd_334_extreme_day_z_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_334_extreme_day_z_accel_126d},
    "exdd_335_extreme_day_z_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_335_extreme_day_z_accel_252d},
    "exdd_336_extreme_day_momentum_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_336_extreme_day_momentum_accel_5d},
    "exdd_337_extreme_day_momentum_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_337_extreme_day_momentum_accel_21d},
    "exdd_338_extreme_day_momentum_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_338_extreme_day_momentum_accel_63d},
    "exdd_339_extreme_day_momentum_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_339_extreme_day_momentum_accel_126d},
    "exdd_340_extreme_day_momentum_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_340_extreme_day_momentum_accel_252d},
    "exdd_341_extreme_range_day_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_341_extreme_range_day_accel_5d},
    "exdd_342_extreme_range_day_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_342_extreme_range_day_accel_21d},
    "exdd_343_extreme_range_day_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_343_extreme_range_day_accel_63d},
    "exdd_344_extreme_range_day_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_344_extreme_range_day_accel_126d},
    "exdd_345_extreme_range_day_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_345_extreme_range_day_accel_252d},
    "exdd_346_extreme_gap_day_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_346_extreme_gap_day_accel_5d},
    "exdd_347_extreme_gap_day_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_347_extreme_gap_day_accel_21d},
    "exdd_348_extreme_gap_day_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_348_extreme_gap_day_accel_63d},
    "exdd_349_extreme_gap_day_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_349_extreme_gap_day_accel_126d},
    "exdd_350_extreme_gap_day_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_350_extreme_gap_day_accel_252d},
    "exdd_351_extreme_day_persistence_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_351_extreme_day_persistence_accel_5d},
    "exdd_352_extreme_day_persistence_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_352_extreme_day_persistence_accel_21d},
    "exdd_353_extreme_day_persistence_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_353_extreme_day_persistence_accel_63d},
    "exdd_354_extreme_day_persistence_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_354_extreme_day_persistence_accel_126d},
    "exdd_355_extreme_day_persistence_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_355_extreme_day_persistence_accel_252d},
    "exdd_356_extreme_day_decay_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_356_extreme_day_decay_accel_5d},
    "exdd_357_extreme_day_decay_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_357_extreme_day_decay_accel_21d},
    "exdd_358_extreme_day_decay_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_358_extreme_day_decay_accel_63d},
    "exdd_359_extreme_day_decay_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_359_extreme_day_decay_accel_126d},
    "exdd_360_extreme_day_decay_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_360_extreme_day_decay_accel_252d},
    "exdd_361_extreme_day_vol_ratio_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_361_extreme_day_vol_ratio_accel_5d},
    "exdd_362_extreme_day_vol_ratio_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_362_extreme_day_vol_ratio_accel_21d},
    "exdd_363_extreme_day_vol_ratio_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_363_extreme_day_vol_ratio_accel_63d},
    "exdd_364_extreme_day_vol_ratio_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_364_extreme_day_vol_ratio_accel_126d},
    "exdd_365_extreme_day_vol_ratio_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_365_extreme_day_vol_ratio_accel_252d},
    "exdd_366_extreme_day_regime_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_366_extreme_day_regime_accel_5d},
    "exdd_367_extreme_day_regime_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_367_extreme_day_regime_accel_21d},
    "exdd_368_extreme_day_regime_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_368_extreme_day_regime_accel_63d},
    "exdd_369_extreme_day_regime_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_369_extreme_day_regime_accel_126d},
    "exdd_370_extreme_day_regime_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_370_extreme_day_regime_accel_252d},
    "exdd_371_extreme_day_exhaustion_accel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_371_extreme_day_exhaustion_accel_5d},
    "exdd_372_extreme_day_exhaustion_accel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_372_extreme_day_exhaustion_accel_21d},
    "exdd_373_extreme_day_exhaustion_accel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_373_extreme_day_exhaustion_accel_63d},
    "exdd_374_extreme_day_exhaustion_accel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_374_extreme_day_exhaustion_accel_126d},
    "exdd_375_extreme_day_exhaustion_accel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_375_extreme_day_exhaustion_accel_252d},
}
