"""
124_cross_sectional_distress_rank — Acceleration (3rd Derivatives)
Domain: cross_sectional_distress_rank
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

def csdr_301_price_rank_xs_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_301_price_rank_xs_accel_5d
    ECONOMIC RATIONALE: Acceleration of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(5).diff(_TD_MON)

def csdr_302_price_rank_xs_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_302_price_rank_xs_accel_21d
    ECONOMIC RATIONALE: Acceleration of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(21).diff(_TD_MON)

def csdr_303_price_rank_xs_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_303_price_rank_xs_accel_63d
    ECONOMIC RATIONALE: Acceleration of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(63).diff(_TD_MON)

def csdr_304_price_rank_xs_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_304_price_rank_xs_accel_126d
    ECONOMIC RATIONALE: Acceleration of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(126).diff(_TD_MON)

def csdr_305_price_rank_xs_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_305_price_rank_xs_accel_252d
    ECONOMIC RATIONALE: Acceleration of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(252).diff(_TD_MON)

def csdr_306_volume_rank_xs_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_306_volume_rank_xs_accel_5d
    ECONOMIC RATIONALE: Acceleration of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(5).diff(_TD_MON)

def csdr_307_volume_rank_xs_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_307_volume_rank_xs_accel_21d
    ECONOMIC RATIONALE: Acceleration of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(21).diff(_TD_MON)

def csdr_308_volume_rank_xs_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_308_volume_rank_xs_accel_63d
    ECONOMIC RATIONALE: Acceleration of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(63).diff(_TD_MON)

def csdr_309_volume_rank_xs_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_309_volume_rank_xs_accel_126d
    ECONOMIC RATIONALE: Acceleration of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(126).diff(_TD_MON)

def csdr_310_volume_rank_xs_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_310_volume_rank_xs_accel_252d
    ECONOMIC RATIONALE: Acceleration of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(252).diff(_TD_MON)

def csdr_311_relative_distress_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_311_relative_distress_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(5).diff(_TD_MON)

def csdr_312_relative_distress_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_312_relative_distress_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(21).diff(_TD_MON)

def csdr_313_relative_distress_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_313_relative_distress_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(63).diff(_TD_MON)

def csdr_314_relative_distress_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_314_relative_distress_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(126).diff(_TD_MON)

def csdr_315_relative_distress_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_315_relative_distress_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(252).diff(_TD_MON)

def csdr_316_xs_volatility_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_316_xs_volatility_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(5).diff(_TD_MON)

def csdr_317_xs_volatility_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_317_xs_volatility_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(21).diff(_TD_MON)

def csdr_318_xs_volatility_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_318_xs_volatility_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(63).diff(_TD_MON)

def csdr_319_xs_volatility_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_319_xs_volatility_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(126).diff(_TD_MON)

def csdr_320_xs_volatility_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_320_xs_volatility_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(252).diff(_TD_MON)

def csdr_321_xs_drawdown_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_321_xs_drawdown_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(5).diff(_TD_MON)

def csdr_322_xs_drawdown_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_322_xs_drawdown_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(21).diff(_TD_MON)

def csdr_323_xs_drawdown_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_323_xs_drawdown_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(63).diff(_TD_MON)

def csdr_324_xs_drawdown_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_324_xs_drawdown_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(126).diff(_TD_MON)

def csdr_325_xs_drawdown_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_325_xs_drawdown_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(252).diff(_TD_MON)

def csdr_326_relative_volume_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_326_relative_volume_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(5).diff(_TD_MON)

def csdr_327_relative_volume_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_327_relative_volume_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(21).diff(_TD_MON)

def csdr_328_relative_volume_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_328_relative_volume_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(63).diff(_TD_MON)

def csdr_329_relative_volume_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_329_relative_volume_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(126).diff(_TD_MON)

def csdr_330_relative_volume_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_330_relative_volume_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(252).diff(_TD_MON)

def csdr_331_xs_momentum_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_331_xs_momentum_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(5).diff(_TD_MON)

def csdr_332_xs_momentum_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_332_xs_momentum_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(21).diff(_TD_MON)

def csdr_333_xs_momentum_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_333_xs_momentum_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(63).diff(_TD_MON)

def csdr_334_xs_momentum_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_334_xs_momentum_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(126).diff(_TD_MON)

def csdr_335_xs_momentum_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_335_xs_momentum_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(252).diff(_TD_MON)

def csdr_336_distress_rank_z_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_336_distress_rank_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(5).diff(_TD_MON)

def csdr_337_distress_rank_z_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_337_distress_rank_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(21).diff(_TD_MON)

def csdr_338_distress_rank_z_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_338_distress_rank_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(63).diff(_TD_MON)

def csdr_339_distress_rank_z_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_339_distress_rank_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(126).diff(_TD_MON)

def csdr_340_distress_rank_z_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_340_distress_rank_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(252).diff(_TD_MON)

def csdr_341_xs_recovery_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_341_xs_recovery_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(5).diff(_TD_MON)

def csdr_342_xs_recovery_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_342_xs_recovery_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(21).diff(_TD_MON)

def csdr_343_xs_recovery_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_343_xs_recovery_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(63).diff(_TD_MON)

def csdr_344_xs_recovery_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_344_xs_recovery_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(126).diff(_TD_MON)

def csdr_345_xs_recovery_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_345_xs_recovery_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(252).diff(_TD_MON)

def csdr_346_xs_liquidity_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_346_xs_liquidity_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(5).diff(_TD_MON)

def csdr_347_xs_liquidity_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_347_xs_liquidity_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(21).diff(_TD_MON)

def csdr_348_xs_liquidity_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_348_xs_liquidity_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(63).diff(_TD_MON)

def csdr_349_xs_liquidity_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_349_xs_liquidity_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(126).diff(_TD_MON)

def csdr_350_xs_liquidity_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_350_xs_liquidity_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(252).diff(_TD_MON)

def csdr_351_xs_tail_risk_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_351_xs_tail_risk_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(5).diff(_TD_MON)

def csdr_352_xs_tail_risk_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_352_xs_tail_risk_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(21).diff(_TD_MON)

def csdr_353_xs_tail_risk_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_353_xs_tail_risk_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(63).diff(_TD_MON)

def csdr_354_xs_tail_risk_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_354_xs_tail_risk_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(126).diff(_TD_MON)

def csdr_355_xs_tail_risk_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_355_xs_tail_risk_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(252).diff(_TD_MON)

def csdr_356_xs_asymmetry_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_356_xs_asymmetry_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(5).diff(_TD_MON)

def csdr_357_xs_asymmetry_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_357_xs_asymmetry_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(21).diff(_TD_MON)

def csdr_358_xs_asymmetry_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_358_xs_asymmetry_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(63).diff(_TD_MON)

def csdr_359_xs_asymmetry_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_359_xs_asymmetry_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(126).diff(_TD_MON)

def csdr_360_xs_asymmetry_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_360_xs_asymmetry_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(252).diff(_TD_MON)

def csdr_361_xs_persistence_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_361_xs_persistence_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5).diff(_TD_MON)

def csdr_362_xs_persistence_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_362_xs_persistence_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21).diff(_TD_MON)

def csdr_363_xs_persistence_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_363_xs_persistence_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63).diff(_TD_MON)

def csdr_364_xs_persistence_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_364_xs_persistence_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126).diff(_TD_MON)

def csdr_365_xs_persistence_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_365_xs_persistence_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252).diff(_TD_MON)

def csdr_366_xs_gap_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_366_xs_gap_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(5).diff(_TD_MON)

def csdr_367_xs_gap_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_367_xs_gap_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(21).diff(_TD_MON)

def csdr_368_xs_gap_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_368_xs_gap_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(63).diff(_TD_MON)

def csdr_369_xs_gap_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_369_xs_gap_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(126).diff(_TD_MON)

def csdr_370_xs_gap_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_370_xs_gap_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(252).diff(_TD_MON)

def csdr_371_xs_composite_rank_accel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_371_xs_composite_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(5).diff(_TD_MON)

def csdr_372_xs_composite_rank_accel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_372_xs_composite_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(21).diff(_TD_MON)

def csdr_373_xs_composite_rank_accel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_373_xs_composite_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(63).diff(_TD_MON)

def csdr_374_xs_composite_rank_accel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_374_xs_composite_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(126).diff(_TD_MON)

def csdr_375_xs_composite_rank_accel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_375_xs_composite_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V124_REGISTRY_ACCEL = {
    "csdr_301_price_rank_xs_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_301_price_rank_xs_accel_5d},
    "csdr_302_price_rank_xs_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_302_price_rank_xs_accel_21d},
    "csdr_303_price_rank_xs_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_303_price_rank_xs_accel_63d},
    "csdr_304_price_rank_xs_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_304_price_rank_xs_accel_126d},
    "csdr_305_price_rank_xs_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_305_price_rank_xs_accel_252d},
    "csdr_306_volume_rank_xs_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_306_volume_rank_xs_accel_5d},
    "csdr_307_volume_rank_xs_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_307_volume_rank_xs_accel_21d},
    "csdr_308_volume_rank_xs_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_308_volume_rank_xs_accel_63d},
    "csdr_309_volume_rank_xs_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_309_volume_rank_xs_accel_126d},
    "csdr_310_volume_rank_xs_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_310_volume_rank_xs_accel_252d},
    "csdr_311_relative_distress_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_311_relative_distress_rank_accel_5d},
    "csdr_312_relative_distress_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_312_relative_distress_rank_accel_21d},
    "csdr_313_relative_distress_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_313_relative_distress_rank_accel_63d},
    "csdr_314_relative_distress_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_314_relative_distress_rank_accel_126d},
    "csdr_315_relative_distress_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_315_relative_distress_rank_accel_252d},
    "csdr_316_xs_volatility_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_316_xs_volatility_rank_accel_5d},
    "csdr_317_xs_volatility_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_317_xs_volatility_rank_accel_21d},
    "csdr_318_xs_volatility_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_318_xs_volatility_rank_accel_63d},
    "csdr_319_xs_volatility_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_319_xs_volatility_rank_accel_126d},
    "csdr_320_xs_volatility_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_320_xs_volatility_rank_accel_252d},
    "csdr_321_xs_drawdown_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_321_xs_drawdown_rank_accel_5d},
    "csdr_322_xs_drawdown_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_322_xs_drawdown_rank_accel_21d},
    "csdr_323_xs_drawdown_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_323_xs_drawdown_rank_accel_63d},
    "csdr_324_xs_drawdown_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_324_xs_drawdown_rank_accel_126d},
    "csdr_325_xs_drawdown_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_325_xs_drawdown_rank_accel_252d},
    "csdr_326_relative_volume_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_326_relative_volume_rank_accel_5d},
    "csdr_327_relative_volume_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_327_relative_volume_rank_accel_21d},
    "csdr_328_relative_volume_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_328_relative_volume_rank_accel_63d},
    "csdr_329_relative_volume_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_329_relative_volume_rank_accel_126d},
    "csdr_330_relative_volume_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_330_relative_volume_rank_accel_252d},
    "csdr_331_xs_momentum_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_331_xs_momentum_rank_accel_5d},
    "csdr_332_xs_momentum_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_332_xs_momentum_rank_accel_21d},
    "csdr_333_xs_momentum_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_333_xs_momentum_rank_accel_63d},
    "csdr_334_xs_momentum_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_334_xs_momentum_rank_accel_126d},
    "csdr_335_xs_momentum_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_335_xs_momentum_rank_accel_252d},
    "csdr_336_distress_rank_z_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_336_distress_rank_z_accel_5d},
    "csdr_337_distress_rank_z_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_337_distress_rank_z_accel_21d},
    "csdr_338_distress_rank_z_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_338_distress_rank_z_accel_63d},
    "csdr_339_distress_rank_z_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_339_distress_rank_z_accel_126d},
    "csdr_340_distress_rank_z_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_340_distress_rank_z_accel_252d},
    "csdr_341_xs_recovery_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_341_xs_recovery_rank_accel_5d},
    "csdr_342_xs_recovery_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_342_xs_recovery_rank_accel_21d},
    "csdr_343_xs_recovery_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_343_xs_recovery_rank_accel_63d},
    "csdr_344_xs_recovery_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_344_xs_recovery_rank_accel_126d},
    "csdr_345_xs_recovery_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_345_xs_recovery_rank_accel_252d},
    "csdr_346_xs_liquidity_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_346_xs_liquidity_rank_accel_5d},
    "csdr_347_xs_liquidity_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_347_xs_liquidity_rank_accel_21d},
    "csdr_348_xs_liquidity_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_348_xs_liquidity_rank_accel_63d},
    "csdr_349_xs_liquidity_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_349_xs_liquidity_rank_accel_126d},
    "csdr_350_xs_liquidity_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_350_xs_liquidity_rank_accel_252d},
    "csdr_351_xs_tail_risk_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_351_xs_tail_risk_rank_accel_5d},
    "csdr_352_xs_tail_risk_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_352_xs_tail_risk_rank_accel_21d},
    "csdr_353_xs_tail_risk_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_353_xs_tail_risk_rank_accel_63d},
    "csdr_354_xs_tail_risk_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_354_xs_tail_risk_rank_accel_126d},
    "csdr_355_xs_tail_risk_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_355_xs_tail_risk_rank_accel_252d},
    "csdr_356_xs_asymmetry_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_356_xs_asymmetry_rank_accel_5d},
    "csdr_357_xs_asymmetry_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_357_xs_asymmetry_rank_accel_21d},
    "csdr_358_xs_asymmetry_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_358_xs_asymmetry_rank_accel_63d},
    "csdr_359_xs_asymmetry_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_359_xs_asymmetry_rank_accel_126d},
    "csdr_360_xs_asymmetry_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_360_xs_asymmetry_rank_accel_252d},
    "csdr_361_xs_persistence_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_361_xs_persistence_rank_accel_5d},
    "csdr_362_xs_persistence_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_362_xs_persistence_rank_accel_21d},
    "csdr_363_xs_persistence_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_363_xs_persistence_rank_accel_63d},
    "csdr_364_xs_persistence_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_364_xs_persistence_rank_accel_126d},
    "csdr_365_xs_persistence_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_365_xs_persistence_rank_accel_252d},
    "csdr_366_xs_gap_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_366_xs_gap_rank_accel_5d},
    "csdr_367_xs_gap_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_367_xs_gap_rank_accel_21d},
    "csdr_368_xs_gap_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_368_xs_gap_rank_accel_63d},
    "csdr_369_xs_gap_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_369_xs_gap_rank_accel_126d},
    "csdr_370_xs_gap_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_370_xs_gap_rank_accel_252d},
    "csdr_371_xs_composite_rank_accel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_371_xs_composite_rank_accel_5d},
    "csdr_372_xs_composite_rank_accel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_372_xs_composite_rank_accel_21d},
    "csdr_373_xs_composite_rank_accel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_373_xs_composite_rank_accel_63d},
    "csdr_374_xs_composite_rank_accel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_374_xs_composite_rank_accel_126d},
    "csdr_375_xs_composite_rank_accel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_375_xs_composite_rank_accel_252d},
}
