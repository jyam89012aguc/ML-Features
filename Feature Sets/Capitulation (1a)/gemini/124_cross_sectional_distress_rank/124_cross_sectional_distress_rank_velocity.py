"""
124_cross_sectional_distress_rank — Velocity (2nd Derivatives)
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

def csdr_226_price_rank_xs_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_226_price_rank_xs_vel_5d
    ECONOMIC RATIONALE: Velocity of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(5)

def csdr_227_price_rank_xs_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_227_price_rank_xs_vel_21d
    ECONOMIC RATIONALE: Velocity of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(21)

def csdr_228_price_rank_xs_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_228_price_rank_xs_vel_63d
    ECONOMIC RATIONALE: Velocity of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(63)

def csdr_229_price_rank_xs_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_229_price_rank_xs_vel_126d
    ECONOMIC RATIONALE: Velocity of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(126)

def csdr_230_price_rank_xs_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_230_price_rank_xs_vel_252d
    ECONOMIC RATIONALE: Velocity of price_rank_xs. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).diff(252)

def csdr_231_volume_rank_xs_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_231_volume_rank_xs_vel_5d
    ECONOMIC RATIONALE: Velocity of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(5)

def csdr_232_volume_rank_xs_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_232_volume_rank_xs_vel_21d
    ECONOMIC RATIONALE: Velocity of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(21)

def csdr_233_volume_rank_xs_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_233_volume_rank_xs_vel_63d
    ECONOMIC RATIONALE: Velocity of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(63)

def csdr_234_volume_rank_xs_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_234_volume_rank_xs_vel_126d
    ECONOMIC RATIONALE: Velocity of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(126)

def csdr_235_volume_rank_xs_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_235_volume_rank_xs_vel_252d
    ECONOMIC RATIONALE: Velocity of volume_rank_xs. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).diff(252)

def csdr_236_relative_distress_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_236_relative_distress_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(5)

def csdr_237_relative_distress_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_237_relative_distress_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(21)

def csdr_238_relative_distress_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_238_relative_distress_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(63)

def csdr_239_relative_distress_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_239_relative_distress_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(126)

def csdr_240_relative_distress_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_240_relative_distress_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_distress_rank. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).diff(252)

def csdr_241_xs_volatility_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_241_xs_volatility_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(5)

def csdr_242_xs_volatility_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_242_xs_volatility_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(21)

def csdr_243_xs_volatility_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_243_xs_volatility_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(63)

def csdr_244_xs_volatility_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_244_xs_volatility_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(126)

def csdr_245_xs_volatility_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_245_xs_volatility_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_volatility_rank. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).diff(252)

def csdr_246_xs_drawdown_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_246_xs_drawdown_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(5)

def csdr_247_xs_drawdown_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_247_xs_drawdown_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(21)

def csdr_248_xs_drawdown_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_248_xs_drawdown_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(63)

def csdr_249_xs_drawdown_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_249_xs_drawdown_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(126)

def csdr_250_xs_drawdown_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_250_xs_drawdown_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_drawdown_rank. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).diff(252)

def csdr_251_relative_volume_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_251_relative_volume_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(5)

def csdr_252_relative_volume_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_252_relative_volume_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(21)

def csdr_253_relative_volume_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_253_relative_volume_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(63)

def csdr_254_relative_volume_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_254_relative_volume_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(126)

def csdr_255_relative_volume_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_255_relative_volume_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_volume_rank. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).diff(252)

def csdr_256_xs_momentum_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_256_xs_momentum_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(5)

def csdr_257_xs_momentum_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_257_xs_momentum_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(21)

def csdr_258_xs_momentum_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_258_xs_momentum_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(63)

def csdr_259_xs_momentum_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_259_xs_momentum_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(126)

def csdr_260_xs_momentum_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_260_xs_momentum_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_momentum_rank. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).diff(252)

def csdr_261_distress_rank_z_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_261_distress_rank_z_vel_5d
    ECONOMIC RATIONALE: Velocity of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(5)

def csdr_262_distress_rank_z_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_262_distress_rank_z_vel_21d
    ECONOMIC RATIONALE: Velocity of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(21)

def csdr_263_distress_rank_z_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_263_distress_rank_z_vel_63d
    ECONOMIC RATIONALE: Velocity of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(63)

def csdr_264_distress_rank_z_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_264_distress_rank_z_vel_126d
    ECONOMIC RATIONALE: Velocity of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(126)

def csdr_265_distress_rank_z_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_265_distress_rank_z_vel_252d
    ECONOMIC RATIONALE: Velocity of distress_rank_z. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).diff(252)

def csdr_266_xs_recovery_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_266_xs_recovery_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(5)

def csdr_267_xs_recovery_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_267_xs_recovery_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(21)

def csdr_268_xs_recovery_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_268_xs_recovery_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(63)

def csdr_269_xs_recovery_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_269_xs_recovery_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(126)

def csdr_270_xs_recovery_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_270_xs_recovery_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_recovery_rank. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).diff(252)

def csdr_271_xs_liquidity_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_271_xs_liquidity_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(5)

def csdr_272_xs_liquidity_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_272_xs_liquidity_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(21)

def csdr_273_xs_liquidity_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_273_xs_liquidity_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(63)

def csdr_274_xs_liquidity_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_274_xs_liquidity_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(126)

def csdr_275_xs_liquidity_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_275_xs_liquidity_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_liquidity_rank. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).diff(252)

def csdr_276_xs_tail_risk_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_276_xs_tail_risk_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(5)

def csdr_277_xs_tail_risk_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_277_xs_tail_risk_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(21)

def csdr_278_xs_tail_risk_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_278_xs_tail_risk_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(63)

def csdr_279_xs_tail_risk_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_279_xs_tail_risk_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(126)

def csdr_280_xs_tail_risk_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_280_xs_tail_risk_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_tail_risk_rank. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).diff(252)

def csdr_281_xs_asymmetry_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_281_xs_asymmetry_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(5)

def csdr_282_xs_asymmetry_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_282_xs_asymmetry_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(21)

def csdr_283_xs_asymmetry_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_283_xs_asymmetry_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(63)

def csdr_284_xs_asymmetry_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_284_xs_asymmetry_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(126)

def csdr_285_xs_asymmetry_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_285_xs_asymmetry_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_asymmetry_rank. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).diff(252)

def csdr_286_xs_persistence_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_286_xs_persistence_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(5)

def csdr_287_xs_persistence_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_287_xs_persistence_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(21)

def csdr_288_xs_persistence_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_288_xs_persistence_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(63)

def csdr_289_xs_persistence_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_289_xs_persistence_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(126)

def csdr_290_xs_persistence_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_290_xs_persistence_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_persistence_rank. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).diff(252)

def csdr_291_xs_gap_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_291_xs_gap_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(5)

def csdr_292_xs_gap_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_292_xs_gap_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(21)

def csdr_293_xs_gap_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_293_xs_gap_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(63)

def csdr_294_xs_gap_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_294_xs_gap_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(126)

def csdr_295_xs_gap_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_295_xs_gap_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_gap_rank. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).diff(252)

def csdr_296_xs_composite_rank_vel_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_296_xs_composite_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(5)

def csdr_297_xs_composite_rank_vel_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_297_xs_composite_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(21)

def csdr_298_xs_composite_rank_vel_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_298_xs_composite_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(63)

def csdr_299_xs_composite_rank_vel_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_299_xs_composite_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(126)

def csdr_300_xs_composite_rank_vel_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_300_xs_composite_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_composite_rank. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V124_REGISTRY_VEL = {
    "csdr_226_price_rank_xs_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_226_price_rank_xs_vel_5d},
    "csdr_227_price_rank_xs_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_227_price_rank_xs_vel_21d},
    "csdr_228_price_rank_xs_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_228_price_rank_xs_vel_63d},
    "csdr_229_price_rank_xs_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_229_price_rank_xs_vel_126d},
    "csdr_230_price_rank_xs_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_230_price_rank_xs_vel_252d},
    "csdr_231_volume_rank_xs_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_231_volume_rank_xs_vel_5d},
    "csdr_232_volume_rank_xs_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_232_volume_rank_xs_vel_21d},
    "csdr_233_volume_rank_xs_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_233_volume_rank_xs_vel_63d},
    "csdr_234_volume_rank_xs_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_234_volume_rank_xs_vel_126d},
    "csdr_235_volume_rank_xs_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_235_volume_rank_xs_vel_252d},
    "csdr_236_relative_distress_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_236_relative_distress_rank_vel_5d},
    "csdr_237_relative_distress_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_237_relative_distress_rank_vel_21d},
    "csdr_238_relative_distress_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_238_relative_distress_rank_vel_63d},
    "csdr_239_relative_distress_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_239_relative_distress_rank_vel_126d},
    "csdr_240_relative_distress_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_240_relative_distress_rank_vel_252d},
    "csdr_241_xs_volatility_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_241_xs_volatility_rank_vel_5d},
    "csdr_242_xs_volatility_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_242_xs_volatility_rank_vel_21d},
    "csdr_243_xs_volatility_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_243_xs_volatility_rank_vel_63d},
    "csdr_244_xs_volatility_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_244_xs_volatility_rank_vel_126d},
    "csdr_245_xs_volatility_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_245_xs_volatility_rank_vel_252d},
    "csdr_246_xs_drawdown_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_246_xs_drawdown_rank_vel_5d},
    "csdr_247_xs_drawdown_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_247_xs_drawdown_rank_vel_21d},
    "csdr_248_xs_drawdown_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_248_xs_drawdown_rank_vel_63d},
    "csdr_249_xs_drawdown_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_249_xs_drawdown_rank_vel_126d},
    "csdr_250_xs_drawdown_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_250_xs_drawdown_rank_vel_252d},
    "csdr_251_relative_volume_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_251_relative_volume_rank_vel_5d},
    "csdr_252_relative_volume_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_252_relative_volume_rank_vel_21d},
    "csdr_253_relative_volume_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_253_relative_volume_rank_vel_63d},
    "csdr_254_relative_volume_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_254_relative_volume_rank_vel_126d},
    "csdr_255_relative_volume_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_255_relative_volume_rank_vel_252d},
    "csdr_256_xs_momentum_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_256_xs_momentum_rank_vel_5d},
    "csdr_257_xs_momentum_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_257_xs_momentum_rank_vel_21d},
    "csdr_258_xs_momentum_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_258_xs_momentum_rank_vel_63d},
    "csdr_259_xs_momentum_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_259_xs_momentum_rank_vel_126d},
    "csdr_260_xs_momentum_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_260_xs_momentum_rank_vel_252d},
    "csdr_261_distress_rank_z_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_261_distress_rank_z_vel_5d},
    "csdr_262_distress_rank_z_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_262_distress_rank_z_vel_21d},
    "csdr_263_distress_rank_z_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_263_distress_rank_z_vel_63d},
    "csdr_264_distress_rank_z_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_264_distress_rank_z_vel_126d},
    "csdr_265_distress_rank_z_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_265_distress_rank_z_vel_252d},
    "csdr_266_xs_recovery_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_266_xs_recovery_rank_vel_5d},
    "csdr_267_xs_recovery_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_267_xs_recovery_rank_vel_21d},
    "csdr_268_xs_recovery_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_268_xs_recovery_rank_vel_63d},
    "csdr_269_xs_recovery_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_269_xs_recovery_rank_vel_126d},
    "csdr_270_xs_recovery_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_270_xs_recovery_rank_vel_252d},
    "csdr_271_xs_liquidity_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_271_xs_liquidity_rank_vel_5d},
    "csdr_272_xs_liquidity_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_272_xs_liquidity_rank_vel_21d},
    "csdr_273_xs_liquidity_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_273_xs_liquidity_rank_vel_63d},
    "csdr_274_xs_liquidity_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_274_xs_liquidity_rank_vel_126d},
    "csdr_275_xs_liquidity_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_275_xs_liquidity_rank_vel_252d},
    "csdr_276_xs_tail_risk_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_276_xs_tail_risk_rank_vel_5d},
    "csdr_277_xs_tail_risk_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_277_xs_tail_risk_rank_vel_21d},
    "csdr_278_xs_tail_risk_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_278_xs_tail_risk_rank_vel_63d},
    "csdr_279_xs_tail_risk_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_279_xs_tail_risk_rank_vel_126d},
    "csdr_280_xs_tail_risk_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_280_xs_tail_risk_rank_vel_252d},
    "csdr_281_xs_asymmetry_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_281_xs_asymmetry_rank_vel_5d},
    "csdr_282_xs_asymmetry_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_282_xs_asymmetry_rank_vel_21d},
    "csdr_283_xs_asymmetry_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_283_xs_asymmetry_rank_vel_63d},
    "csdr_284_xs_asymmetry_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_284_xs_asymmetry_rank_vel_126d},
    "csdr_285_xs_asymmetry_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_285_xs_asymmetry_rank_vel_252d},
    "csdr_286_xs_persistence_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_286_xs_persistence_rank_vel_5d},
    "csdr_287_xs_persistence_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_287_xs_persistence_rank_vel_21d},
    "csdr_288_xs_persistence_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_288_xs_persistence_rank_vel_63d},
    "csdr_289_xs_persistence_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_289_xs_persistence_rank_vel_126d},
    "csdr_290_xs_persistence_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_290_xs_persistence_rank_vel_252d},
    "csdr_291_xs_gap_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_291_xs_gap_rank_vel_5d},
    "csdr_292_xs_gap_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_292_xs_gap_rank_vel_21d},
    "csdr_293_xs_gap_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_293_xs_gap_rank_vel_63d},
    "csdr_294_xs_gap_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_294_xs_gap_rank_vel_126d},
    "csdr_295_xs_gap_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_295_xs_gap_rank_vel_252d},
    "csdr_296_xs_composite_rank_vel_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_296_xs_composite_rank_vel_5d},
    "csdr_297_xs_composite_rank_vel_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_297_xs_composite_rank_vel_21d},
    "csdr_298_xs_composite_rank_vel_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_298_xs_composite_rank_vel_63d},
    "csdr_299_xs_composite_rank_vel_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_299_xs_composite_rank_vel_126d},
    "csdr_300_xs_composite_rank_vel_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_300_xs_composite_rank_vel_252d},
}
