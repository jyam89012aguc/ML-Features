"""
116_extreme_day_density — Velocity (2nd Derivatives)
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

def exdd_226_extreme_down_day_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_226_extreme_down_day_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(5)

def exdd_227_extreme_down_day_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_227_extreme_down_day_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(21)

def exdd_228_extreme_down_day_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_228_extreme_down_day_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(63)

def exdd_229_extreme_down_day_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_229_extreme_down_day_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(126)

def exdd_230_extreme_down_day_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_230_extreme_down_day_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_down_day. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).diff(252)

def exdd_231_extreme_up_day_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_231_extreme_up_day_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(5)

def exdd_232_extreme_up_day_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_232_extreme_up_day_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(21)

def exdd_233_extreme_up_day_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_233_extreme_up_day_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(63)

def exdd_234_extreme_up_day_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_234_extreme_up_day_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(126)

def exdd_235_extreme_up_day_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_235_extreme_up_day_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_up_day. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).diff(252)

def exdd_236_extreme_vol_day_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_236_extreme_vol_day_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(5)

def exdd_237_extreme_vol_day_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_237_extreme_vol_day_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(21)

def exdd_238_extreme_vol_day_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_238_extreme_vol_day_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(63)

def exdd_239_extreme_vol_day_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_239_extreme_vol_day_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(126)

def exdd_240_extreme_vol_day_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_240_extreme_vol_day_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_vol_day. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).diff(252)

def exdd_241_extreme_day_cluster_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_241_extreme_day_cluster_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(5)

def exdd_242_extreme_day_cluster_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_242_extreme_day_cluster_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(21)

def exdd_243_extreme_day_cluster_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_243_extreme_day_cluster_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(63)

def exdd_244_extreme_day_cluster_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_244_extreme_day_cluster_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(126)

def exdd_245_extreme_day_cluster_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_245_extreme_day_cluster_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_cluster. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).diff(252)

def exdd_246_extreme_day_bias_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_246_extreme_day_bias_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(5)

def exdd_247_extreme_day_bias_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_247_extreme_day_bias_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(21)

def exdd_248_extreme_day_bias_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_248_extreme_day_bias_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(63)

def exdd_249_extreme_day_bias_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_249_extreme_day_bias_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(126)

def exdd_250_extreme_day_bias_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_250_extreme_day_bias_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_bias. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).diff(252)

def exdd_251_extreme_vol_price_sync_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_251_extreme_vol_price_sync_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(5)

def exdd_252_extreme_vol_price_sync_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_252_extreme_vol_price_sync_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(21)

def exdd_253_extreme_vol_price_sync_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_253_extreme_vol_price_sync_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(63)

def exdd_254_extreme_vol_price_sync_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_254_extreme_vol_price_sync_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(126)

def exdd_255_extreme_vol_price_sync_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_255_extreme_vol_price_sync_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_vol_price_sync. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).diff(252)

def exdd_256_extreme_day_z_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_256_extreme_day_z_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(5)

def exdd_257_extreme_day_z_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_257_extreme_day_z_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(21)

def exdd_258_extreme_day_z_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_258_extreme_day_z_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(63)

def exdd_259_extreme_day_z_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_259_extreme_day_z_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(126)

def exdd_260_extreme_day_z_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_260_extreme_day_z_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_z. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).diff(252)

def exdd_261_extreme_day_momentum_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_261_extreme_day_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(5)

def exdd_262_extreme_day_momentum_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_262_extreme_day_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(21)

def exdd_263_extreme_day_momentum_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_263_extreme_day_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(63)

def exdd_264_extreme_day_momentum_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_264_extreme_day_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(126)

def exdd_265_extreme_day_momentum_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_265_extreme_day_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_momentum. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).diff(252)

def exdd_266_extreme_range_day_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_266_extreme_range_day_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(5)

def exdd_267_extreme_range_day_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_267_extreme_range_day_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(21)

def exdd_268_extreme_range_day_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_268_extreme_range_day_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(63)

def exdd_269_extreme_range_day_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_269_extreme_range_day_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(126)

def exdd_270_extreme_range_day_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_270_extreme_range_day_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_range_day. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).diff(252)

def exdd_271_extreme_gap_day_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_271_extreme_gap_day_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(5)

def exdd_272_extreme_gap_day_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_272_extreme_gap_day_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(21)

def exdd_273_extreme_gap_day_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_273_extreme_gap_day_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(63)

def exdd_274_extreme_gap_day_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_274_extreme_gap_day_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(126)

def exdd_275_extreme_gap_day_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_275_extreme_gap_day_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_gap_day. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).diff(252)

def exdd_276_extreme_day_persistence_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_276_extreme_day_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(5)

def exdd_277_extreme_day_persistence_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_277_extreme_day_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(21)

def exdd_278_extreme_day_persistence_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_278_extreme_day_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(63)

def exdd_279_extreme_day_persistence_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_279_extreme_day_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(126)

def exdd_280_extreme_day_persistence_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_280_extreme_day_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_persistence. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).diff(252)

def exdd_281_extreme_day_decay_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_281_extreme_day_decay_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(5)

def exdd_282_extreme_day_decay_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_282_extreme_day_decay_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(21)

def exdd_283_extreme_day_decay_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_283_extreme_day_decay_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(63)

def exdd_284_extreme_day_decay_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_284_extreme_day_decay_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(126)

def exdd_285_extreme_day_decay_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_285_extreme_day_decay_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_decay. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).diff(252)

def exdd_286_extreme_day_vol_ratio_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_286_extreme_day_vol_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(5)

def exdd_287_extreme_day_vol_ratio_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_287_extreme_day_vol_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(21)

def exdd_288_extreme_day_vol_ratio_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_288_extreme_day_vol_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(63)

def exdd_289_extreme_day_vol_ratio_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_289_extreme_day_vol_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(126)

def exdd_290_extreme_day_vol_ratio_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_290_extreme_day_vol_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_vol_ratio. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).diff(252)

def exdd_291_extreme_day_regime_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_291_extreme_day_regime_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(5)

def exdd_292_extreme_day_regime_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_292_extreme_day_regime_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(21)

def exdd_293_extreme_day_regime_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_293_extreme_day_regime_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(63)

def exdd_294_extreme_day_regime_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_294_extreme_day_regime_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(126)

def exdd_295_extreme_day_regime_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_295_extreme_day_regime_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_regime. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).diff(252)

def exdd_296_extreme_day_exhaustion_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_296_extreme_day_exhaustion_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(5)

def exdd_297_extreme_day_exhaustion_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_297_extreme_day_exhaustion_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(21)

def exdd_298_extreme_day_exhaustion_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_298_extreme_day_exhaustion_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(63)

def exdd_299_extreme_day_exhaustion_vel_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_299_extreme_day_exhaustion_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(126)

def exdd_300_extreme_day_exhaustion_vel_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_300_extreme_day_exhaustion_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_day_exhaustion. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V116_REGISTRY_VEL = {
    "exdd_226_extreme_down_day_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_226_extreme_down_day_vel_5d},
    "exdd_227_extreme_down_day_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_227_extreme_down_day_vel_21d},
    "exdd_228_extreme_down_day_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_228_extreme_down_day_vel_63d},
    "exdd_229_extreme_down_day_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_229_extreme_down_day_vel_126d},
    "exdd_230_extreme_down_day_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_230_extreme_down_day_vel_252d},
    "exdd_231_extreme_up_day_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_231_extreme_up_day_vel_5d},
    "exdd_232_extreme_up_day_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_232_extreme_up_day_vel_21d},
    "exdd_233_extreme_up_day_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_233_extreme_up_day_vel_63d},
    "exdd_234_extreme_up_day_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_234_extreme_up_day_vel_126d},
    "exdd_235_extreme_up_day_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_235_extreme_up_day_vel_252d},
    "exdd_236_extreme_vol_day_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_236_extreme_vol_day_vel_5d},
    "exdd_237_extreme_vol_day_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_237_extreme_vol_day_vel_21d},
    "exdd_238_extreme_vol_day_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_238_extreme_vol_day_vel_63d},
    "exdd_239_extreme_vol_day_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_239_extreme_vol_day_vel_126d},
    "exdd_240_extreme_vol_day_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_240_extreme_vol_day_vel_252d},
    "exdd_241_extreme_day_cluster_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_241_extreme_day_cluster_vel_5d},
    "exdd_242_extreme_day_cluster_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_242_extreme_day_cluster_vel_21d},
    "exdd_243_extreme_day_cluster_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_243_extreme_day_cluster_vel_63d},
    "exdd_244_extreme_day_cluster_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_244_extreme_day_cluster_vel_126d},
    "exdd_245_extreme_day_cluster_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_245_extreme_day_cluster_vel_252d},
    "exdd_246_extreme_day_bias_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_246_extreme_day_bias_vel_5d},
    "exdd_247_extreme_day_bias_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_247_extreme_day_bias_vel_21d},
    "exdd_248_extreme_day_bias_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_248_extreme_day_bias_vel_63d},
    "exdd_249_extreme_day_bias_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_249_extreme_day_bias_vel_126d},
    "exdd_250_extreme_day_bias_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_250_extreme_day_bias_vel_252d},
    "exdd_251_extreme_vol_price_sync_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_251_extreme_vol_price_sync_vel_5d},
    "exdd_252_extreme_vol_price_sync_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_252_extreme_vol_price_sync_vel_21d},
    "exdd_253_extreme_vol_price_sync_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_253_extreme_vol_price_sync_vel_63d},
    "exdd_254_extreme_vol_price_sync_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_254_extreme_vol_price_sync_vel_126d},
    "exdd_255_extreme_vol_price_sync_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_255_extreme_vol_price_sync_vel_252d},
    "exdd_256_extreme_day_z_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_256_extreme_day_z_vel_5d},
    "exdd_257_extreme_day_z_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_257_extreme_day_z_vel_21d},
    "exdd_258_extreme_day_z_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_258_extreme_day_z_vel_63d},
    "exdd_259_extreme_day_z_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_259_extreme_day_z_vel_126d},
    "exdd_260_extreme_day_z_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_260_extreme_day_z_vel_252d},
    "exdd_261_extreme_day_momentum_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_261_extreme_day_momentum_vel_5d},
    "exdd_262_extreme_day_momentum_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_262_extreme_day_momentum_vel_21d},
    "exdd_263_extreme_day_momentum_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_263_extreme_day_momentum_vel_63d},
    "exdd_264_extreme_day_momentum_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_264_extreme_day_momentum_vel_126d},
    "exdd_265_extreme_day_momentum_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_265_extreme_day_momentum_vel_252d},
    "exdd_266_extreme_range_day_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_266_extreme_range_day_vel_5d},
    "exdd_267_extreme_range_day_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_267_extreme_range_day_vel_21d},
    "exdd_268_extreme_range_day_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_268_extreme_range_day_vel_63d},
    "exdd_269_extreme_range_day_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_269_extreme_range_day_vel_126d},
    "exdd_270_extreme_range_day_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_270_extreme_range_day_vel_252d},
    "exdd_271_extreme_gap_day_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_271_extreme_gap_day_vel_5d},
    "exdd_272_extreme_gap_day_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_272_extreme_gap_day_vel_21d},
    "exdd_273_extreme_gap_day_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_273_extreme_gap_day_vel_63d},
    "exdd_274_extreme_gap_day_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_274_extreme_gap_day_vel_126d},
    "exdd_275_extreme_gap_day_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_275_extreme_gap_day_vel_252d},
    "exdd_276_extreme_day_persistence_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_276_extreme_day_persistence_vel_5d},
    "exdd_277_extreme_day_persistence_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_277_extreme_day_persistence_vel_21d},
    "exdd_278_extreme_day_persistence_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_278_extreme_day_persistence_vel_63d},
    "exdd_279_extreme_day_persistence_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_279_extreme_day_persistence_vel_126d},
    "exdd_280_extreme_day_persistence_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_280_extreme_day_persistence_vel_252d},
    "exdd_281_extreme_day_decay_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_281_extreme_day_decay_vel_5d},
    "exdd_282_extreme_day_decay_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_282_extreme_day_decay_vel_21d},
    "exdd_283_extreme_day_decay_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_283_extreme_day_decay_vel_63d},
    "exdd_284_extreme_day_decay_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_284_extreme_day_decay_vel_126d},
    "exdd_285_extreme_day_decay_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_285_extreme_day_decay_vel_252d},
    "exdd_286_extreme_day_vol_ratio_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_286_extreme_day_vol_ratio_vel_5d},
    "exdd_287_extreme_day_vol_ratio_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_287_extreme_day_vol_ratio_vel_21d},
    "exdd_288_extreme_day_vol_ratio_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_288_extreme_day_vol_ratio_vel_63d},
    "exdd_289_extreme_day_vol_ratio_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_289_extreme_day_vol_ratio_vel_126d},
    "exdd_290_extreme_day_vol_ratio_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_290_extreme_day_vol_ratio_vel_252d},
    "exdd_291_extreme_day_regime_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_291_extreme_day_regime_vel_5d},
    "exdd_292_extreme_day_regime_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_292_extreme_day_regime_vel_21d},
    "exdd_293_extreme_day_regime_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_293_extreme_day_regime_vel_63d},
    "exdd_294_extreme_day_regime_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_294_extreme_day_regime_vel_126d},
    "exdd_295_extreme_day_regime_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_295_extreme_day_regime_vel_252d},
    "exdd_296_extreme_day_exhaustion_vel_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_296_extreme_day_exhaustion_vel_5d},
    "exdd_297_extreme_day_exhaustion_vel_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_297_extreme_day_exhaustion_vel_21d},
    "exdd_298_extreme_day_exhaustion_vel_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_298_extreme_day_exhaustion_vel_63d},
    "exdd_299_extreme_day_exhaustion_vel_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_299_extreme_day_exhaustion_vel_126d},
    "exdd_300_extreme_day_exhaustion_vel_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_300_extreme_day_exhaustion_vel_252d},
}
