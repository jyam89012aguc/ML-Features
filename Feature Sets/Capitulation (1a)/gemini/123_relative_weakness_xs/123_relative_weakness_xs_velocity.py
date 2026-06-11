"""
123_relative_weakness_xs — Velocity (2nd Derivatives)
Domain: relative_weakness_xs
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

def rwxs_226_relative_return_21d_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_226_relative_return_21d_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(5)

def rwxs_227_relative_return_21d_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_227_relative_return_21d_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(21)

def rwxs_228_relative_return_21d_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_228_relative_return_21d_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(63)

def rwxs_229_relative_return_21d_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_229_relative_return_21d_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(126)

def rwxs_230_relative_return_21d_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_230_relative_return_21d_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(252)

def rwxs_231_relative_drawdown_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_231_relative_drawdown_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(5)

def rwxs_232_relative_drawdown_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_232_relative_drawdown_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(21)

def rwxs_233_relative_drawdown_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_233_relative_drawdown_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(63)

def rwxs_234_relative_drawdown_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_234_relative_drawdown_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(126)

def rwxs_235_relative_drawdown_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_235_relative_drawdown_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(252)

def rwxs_236_beta_adjusted_alpha_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_236_beta_adjusted_alpha_vel_5d
    ECONOMIC RATIONALE: Velocity of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(5)

def rwxs_237_beta_adjusted_alpha_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_237_beta_adjusted_alpha_vel_21d
    ECONOMIC RATIONALE: Velocity of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(21)

def rwxs_238_beta_adjusted_alpha_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_238_beta_adjusted_alpha_vel_63d
    ECONOMIC RATIONALE: Velocity of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(63)

def rwxs_239_beta_adjusted_alpha_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_239_beta_adjusted_alpha_vel_126d
    ECONOMIC RATIONALE: Velocity of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(126)

def rwxs_240_beta_adjusted_alpha_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_240_beta_adjusted_alpha_vel_252d
    ECONOMIC RATIONALE: Velocity of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(252)

def rwxs_241_relative_weakness_z_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_241_relative_weakness_z_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(5)

def rwxs_242_relative_weakness_z_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_242_relative_weakness_z_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(21)

def rwxs_243_relative_weakness_z_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_243_relative_weakness_z_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(63)

def rwxs_244_relative_weakness_z_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_244_relative_weakness_z_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(126)

def rwxs_245_relative_weakness_z_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_245_relative_weakness_z_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(252)

def rwxs_246_underperformance_persistence_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_246_underperformance_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(5)

def rwxs_247_underperformance_persistence_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_247_underperformance_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(21)

def rwxs_248_underperformance_persistence_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_248_underperformance_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(63)

def rwxs_249_underperformance_persistence_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_249_underperformance_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(126)

def rwxs_250_underperformance_persistence_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_250_underperformance_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(252)

def rwxs_251_relative_momentum_div_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_251_relative_momentum_div_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(5)

def rwxs_252_relative_momentum_div_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_252_relative_momentum_div_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(21)

def rwxs_253_relative_momentum_div_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_253_relative_momentum_div_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(63)

def rwxs_254_relative_momentum_div_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_254_relative_momentum_div_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(126)

def rwxs_255_relative_momentum_div_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_255_relative_momentum_div_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(252)

def rwxs_256_xs_weakness_acceleration_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_256_xs_weakness_acceleration_vel_5d
    ECONOMIC RATIONALE: Velocity of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(5)

def rwxs_257_xs_weakness_acceleration_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_257_xs_weakness_acceleration_vel_21d
    ECONOMIC RATIONALE: Velocity of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(21)

def rwxs_258_xs_weakness_acceleration_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_258_xs_weakness_acceleration_vel_63d
    ECONOMIC RATIONALE: Velocity of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(63)

def rwxs_259_xs_weakness_acceleration_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_259_xs_weakness_acceleration_vel_126d
    ECONOMIC RATIONALE: Velocity of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(126)

def rwxs_260_xs_weakness_acceleration_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_260_xs_weakness_acceleration_vel_252d
    ECONOMIC RATIONALE: Velocity of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(252)

def rwxs_261_relative_volatility_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_261_relative_volatility_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(5)

def rwxs_262_relative_volatility_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_262_relative_volatility_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(21)

def rwxs_263_relative_volatility_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_263_relative_volatility_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(63)

def rwxs_264_relative_volatility_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_264_relative_volatility_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(126)

def rwxs_265_relative_volatility_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_265_relative_volatility_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(252)

def rwxs_266_relative_strength_rank_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_266_relative_strength_rank_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(5)

def rwxs_267_relative_strength_rank_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_267_relative_strength_rank_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(21)

def rwxs_268_relative_strength_rank_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_268_relative_strength_rank_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(63)

def rwxs_269_relative_strength_rank_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_269_relative_strength_rank_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(126)

def rwxs_270_relative_strength_rank_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_270_relative_strength_rank_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(252)

def rwxs_271_market_decoupling_flag_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_271_market_decoupling_flag_vel_5d
    ECONOMIC RATIONALE: Velocity of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(5)

def rwxs_272_market_decoupling_flag_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_272_market_decoupling_flag_vel_21d
    ECONOMIC RATIONALE: Velocity of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(21)

def rwxs_273_market_decoupling_flag_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_273_market_decoupling_flag_vel_63d
    ECONOMIC RATIONALE: Velocity of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(63)

def rwxs_274_market_decoupling_flag_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_274_market_decoupling_flag_vel_126d
    ECONOMIC RATIONALE: Velocity of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(126)

def rwxs_275_market_decoupling_flag_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_275_market_decoupling_flag_vel_252d
    ECONOMIC RATIONALE: Velocity of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(252)

def rwxs_276_relative_low_test_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_276_relative_low_test_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(5)

def rwxs_277_relative_low_test_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_277_relative_low_test_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(21)

def rwxs_278_relative_low_test_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_278_relative_low_test_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(63)

def rwxs_279_relative_low_test_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_279_relative_low_test_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(126)

def rwxs_280_relative_low_test_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_280_relative_low_test_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(252)

def rwxs_281_relative_weakness_score_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_281_relative_weakness_score_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(5)

def rwxs_282_relative_weakness_score_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_282_relative_weakness_score_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(21)

def rwxs_283_relative_weakness_score_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_283_relative_weakness_score_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(63)

def rwxs_284_relative_weakness_score_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_284_relative_weakness_score_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(126)

def rwxs_285_relative_weakness_score_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_285_relative_weakness_score_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(252)

def rwxs_286_excess_volatility_z_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_286_excess_volatility_z_vel_5d
    ECONOMIC RATIONALE: Velocity of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(5)

def rwxs_287_excess_volatility_z_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_287_excess_volatility_z_vel_21d
    ECONOMIC RATIONALE: Velocity of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(21)

def rwxs_288_excess_volatility_z_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_288_excess_volatility_z_vel_63d
    ECONOMIC RATIONALE: Velocity of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(63)

def rwxs_289_excess_volatility_z_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_289_excess_volatility_z_vel_126d
    ECONOMIC RATIONALE: Velocity of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(126)

def rwxs_290_excess_volatility_z_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_290_excess_volatility_z_vel_252d
    ECONOMIC RATIONALE: Velocity of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(252)

def rwxs_291_relative_strength_roc_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_291_relative_strength_roc_vel_5d
    ECONOMIC RATIONALE: Velocity of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(5)

def rwxs_292_relative_strength_roc_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_292_relative_strength_roc_vel_21d
    ECONOMIC RATIONALE: Velocity of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(21)

def rwxs_293_relative_strength_roc_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_293_relative_strength_roc_vel_63d
    ECONOMIC RATIONALE: Velocity of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(63)

def rwxs_294_relative_strength_roc_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_294_relative_strength_roc_vel_126d
    ECONOMIC RATIONALE: Velocity of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(126)

def rwxs_295_relative_strength_roc_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_295_relative_strength_roc_vel_252d
    ECONOMIC RATIONALE: Velocity of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(252)

def rwxs_296_market_beta_zscore_vel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_296_market_beta_zscore_vel_5d
    ECONOMIC RATIONALE: Velocity of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(5)

def rwxs_297_market_beta_zscore_vel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_297_market_beta_zscore_vel_21d
    ECONOMIC RATIONALE: Velocity of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(21)

def rwxs_298_market_beta_zscore_vel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_298_market_beta_zscore_vel_63d
    ECONOMIC RATIONALE: Velocity of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(63)

def rwxs_299_market_beta_zscore_vel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_299_market_beta_zscore_vel_126d
    ECONOMIC RATIONALE: Velocity of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(126)

def rwxs_300_market_beta_zscore_vel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_300_market_beta_zscore_vel_252d
    ECONOMIC RATIONALE: Velocity of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V123_REGISTRY_VEL = {
    "rwxs_226_relative_return_21d_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_226_relative_return_21d_vel_5d},
    "rwxs_227_relative_return_21d_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_227_relative_return_21d_vel_21d},
    "rwxs_228_relative_return_21d_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_228_relative_return_21d_vel_63d},
    "rwxs_229_relative_return_21d_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_229_relative_return_21d_vel_126d},
    "rwxs_230_relative_return_21d_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_230_relative_return_21d_vel_252d},
    "rwxs_231_relative_drawdown_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_231_relative_drawdown_vel_5d},
    "rwxs_232_relative_drawdown_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_232_relative_drawdown_vel_21d},
    "rwxs_233_relative_drawdown_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_233_relative_drawdown_vel_63d},
    "rwxs_234_relative_drawdown_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_234_relative_drawdown_vel_126d},
    "rwxs_235_relative_drawdown_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_235_relative_drawdown_vel_252d},
    "rwxs_236_beta_adjusted_alpha_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_236_beta_adjusted_alpha_vel_5d},
    "rwxs_237_beta_adjusted_alpha_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_237_beta_adjusted_alpha_vel_21d},
    "rwxs_238_beta_adjusted_alpha_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_238_beta_adjusted_alpha_vel_63d},
    "rwxs_239_beta_adjusted_alpha_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_239_beta_adjusted_alpha_vel_126d},
    "rwxs_240_beta_adjusted_alpha_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_240_beta_adjusted_alpha_vel_252d},
    "rwxs_241_relative_weakness_z_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_241_relative_weakness_z_vel_5d},
    "rwxs_242_relative_weakness_z_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_242_relative_weakness_z_vel_21d},
    "rwxs_243_relative_weakness_z_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_243_relative_weakness_z_vel_63d},
    "rwxs_244_relative_weakness_z_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_244_relative_weakness_z_vel_126d},
    "rwxs_245_relative_weakness_z_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_245_relative_weakness_z_vel_252d},
    "rwxs_246_underperformance_persistence_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_246_underperformance_persistence_vel_5d},
    "rwxs_247_underperformance_persistence_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_247_underperformance_persistence_vel_21d},
    "rwxs_248_underperformance_persistence_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_248_underperformance_persistence_vel_63d},
    "rwxs_249_underperformance_persistence_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_249_underperformance_persistence_vel_126d},
    "rwxs_250_underperformance_persistence_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_250_underperformance_persistence_vel_252d},
    "rwxs_251_relative_momentum_div_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_251_relative_momentum_div_vel_5d},
    "rwxs_252_relative_momentum_div_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_252_relative_momentum_div_vel_21d},
    "rwxs_253_relative_momentum_div_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_253_relative_momentum_div_vel_63d},
    "rwxs_254_relative_momentum_div_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_254_relative_momentum_div_vel_126d},
    "rwxs_255_relative_momentum_div_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_255_relative_momentum_div_vel_252d},
    "rwxs_256_xs_weakness_acceleration_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_256_xs_weakness_acceleration_vel_5d},
    "rwxs_257_xs_weakness_acceleration_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_257_xs_weakness_acceleration_vel_21d},
    "rwxs_258_xs_weakness_acceleration_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_258_xs_weakness_acceleration_vel_63d},
    "rwxs_259_xs_weakness_acceleration_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_259_xs_weakness_acceleration_vel_126d},
    "rwxs_260_xs_weakness_acceleration_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_260_xs_weakness_acceleration_vel_252d},
    "rwxs_261_relative_volatility_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_261_relative_volatility_vel_5d},
    "rwxs_262_relative_volatility_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_262_relative_volatility_vel_21d},
    "rwxs_263_relative_volatility_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_263_relative_volatility_vel_63d},
    "rwxs_264_relative_volatility_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_264_relative_volatility_vel_126d},
    "rwxs_265_relative_volatility_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_265_relative_volatility_vel_252d},
    "rwxs_266_relative_strength_rank_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_266_relative_strength_rank_vel_5d},
    "rwxs_267_relative_strength_rank_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_267_relative_strength_rank_vel_21d},
    "rwxs_268_relative_strength_rank_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_268_relative_strength_rank_vel_63d},
    "rwxs_269_relative_strength_rank_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_269_relative_strength_rank_vel_126d},
    "rwxs_270_relative_strength_rank_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_270_relative_strength_rank_vel_252d},
    "rwxs_271_market_decoupling_flag_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_271_market_decoupling_flag_vel_5d},
    "rwxs_272_market_decoupling_flag_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_272_market_decoupling_flag_vel_21d},
    "rwxs_273_market_decoupling_flag_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_273_market_decoupling_flag_vel_63d},
    "rwxs_274_market_decoupling_flag_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_274_market_decoupling_flag_vel_126d},
    "rwxs_275_market_decoupling_flag_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_275_market_decoupling_flag_vel_252d},
    "rwxs_276_relative_low_test_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_276_relative_low_test_vel_5d},
    "rwxs_277_relative_low_test_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_277_relative_low_test_vel_21d},
    "rwxs_278_relative_low_test_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_278_relative_low_test_vel_63d},
    "rwxs_279_relative_low_test_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_279_relative_low_test_vel_126d},
    "rwxs_280_relative_low_test_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_280_relative_low_test_vel_252d},
    "rwxs_281_relative_weakness_score_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_281_relative_weakness_score_vel_5d},
    "rwxs_282_relative_weakness_score_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_282_relative_weakness_score_vel_21d},
    "rwxs_283_relative_weakness_score_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_283_relative_weakness_score_vel_63d},
    "rwxs_284_relative_weakness_score_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_284_relative_weakness_score_vel_126d},
    "rwxs_285_relative_weakness_score_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_285_relative_weakness_score_vel_252d},
    "rwxs_286_excess_volatility_z_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_286_excess_volatility_z_vel_5d},
    "rwxs_287_excess_volatility_z_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_287_excess_volatility_z_vel_21d},
    "rwxs_288_excess_volatility_z_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_288_excess_volatility_z_vel_63d},
    "rwxs_289_excess_volatility_z_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_289_excess_volatility_z_vel_126d},
    "rwxs_290_excess_volatility_z_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_290_excess_volatility_z_vel_252d},
    "rwxs_291_relative_strength_roc_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_291_relative_strength_roc_vel_5d},
    "rwxs_292_relative_strength_roc_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_292_relative_strength_roc_vel_21d},
    "rwxs_293_relative_strength_roc_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_293_relative_strength_roc_vel_63d},
    "rwxs_294_relative_strength_roc_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_294_relative_strength_roc_vel_126d},
    "rwxs_295_relative_strength_roc_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_295_relative_strength_roc_vel_252d},
    "rwxs_296_market_beta_zscore_vel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_296_market_beta_zscore_vel_5d},
    "rwxs_297_market_beta_zscore_vel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_297_market_beta_zscore_vel_21d},
    "rwxs_298_market_beta_zscore_vel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_298_market_beta_zscore_vel_63d},
    "rwxs_299_market_beta_zscore_vel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_299_market_beta_zscore_vel_126d},
    "rwxs_300_market_beta_zscore_vel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_300_market_beta_zscore_vel_252d},
}
