"""
123_relative_weakness_xs — Acceleration (3rd Derivatives)
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

def rwxs_301_relative_return_21d_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_301_relative_return_21d_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(5).diff(_TD_MON)

def rwxs_302_relative_return_21d_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_302_relative_return_21d_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(21).diff(_TD_MON)

def rwxs_303_relative_return_21d_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_303_relative_return_21d_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(63).diff(_TD_MON)

def rwxs_304_relative_return_21d_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_304_relative_return_21d_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(126).diff(_TD_MON)

def rwxs_305_relative_return_21d_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_305_relative_return_21d_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_return_21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).diff(252).diff(_TD_MON)

def rwxs_306_relative_drawdown_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_306_relative_drawdown_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(5).diff(_TD_MON)

def rwxs_307_relative_drawdown_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_307_relative_drawdown_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(21).diff(_TD_MON)

def rwxs_308_relative_drawdown_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_308_relative_drawdown_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(63).diff(_TD_MON)

def rwxs_309_relative_drawdown_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_309_relative_drawdown_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(126).diff(_TD_MON)

def rwxs_310_relative_drawdown_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_310_relative_drawdown_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_drawdown. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).diff(252).diff(_TD_MON)

def rwxs_311_beta_adjusted_alpha_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_311_beta_adjusted_alpha_accel_5d
    ECONOMIC RATIONALE: Acceleration of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(5).diff(_TD_MON)

def rwxs_312_beta_adjusted_alpha_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_312_beta_adjusted_alpha_accel_21d
    ECONOMIC RATIONALE: Acceleration of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(21).diff(_TD_MON)

def rwxs_313_beta_adjusted_alpha_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_313_beta_adjusted_alpha_accel_63d
    ECONOMIC RATIONALE: Acceleration of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(63).diff(_TD_MON)

def rwxs_314_beta_adjusted_alpha_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_314_beta_adjusted_alpha_accel_126d
    ECONOMIC RATIONALE: Acceleration of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(126).diff(_TD_MON)

def rwxs_315_beta_adjusted_alpha_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_315_beta_adjusted_alpha_accel_252d
    ECONOMIC RATIONALE: Acceleration of beta_adjusted_alpha. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).diff(252).diff(_TD_MON)

def rwxs_316_relative_weakness_z_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_316_relative_weakness_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(5).diff(_TD_MON)

def rwxs_317_relative_weakness_z_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_317_relative_weakness_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(21).diff(_TD_MON)

def rwxs_318_relative_weakness_z_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_318_relative_weakness_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(63).diff(_TD_MON)

def rwxs_319_relative_weakness_z_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_319_relative_weakness_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(126).diff(_TD_MON)

def rwxs_320_relative_weakness_z_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_320_relative_weakness_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_z. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).diff(252).diff(_TD_MON)

def rwxs_321_underperformance_persistence_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_321_underperformance_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(5).diff(_TD_MON)

def rwxs_322_underperformance_persistence_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_322_underperformance_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(21).diff(_TD_MON)

def rwxs_323_underperformance_persistence_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_323_underperformance_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(63).diff(_TD_MON)

def rwxs_324_underperformance_persistence_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_324_underperformance_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(126).diff(_TD_MON)

def rwxs_325_underperformance_persistence_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_325_underperformance_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of underperformance_persistence. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).diff(252).diff(_TD_MON)

def rwxs_326_relative_momentum_div_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_326_relative_momentum_div_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def rwxs_327_relative_momentum_div_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_327_relative_momentum_div_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def rwxs_328_relative_momentum_div_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_328_relative_momentum_div_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def rwxs_329_relative_momentum_div_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_329_relative_momentum_div_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def rwxs_330_relative_momentum_div_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_330_relative_momentum_div_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_momentum_div. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def rwxs_331_xs_weakness_acceleration_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_331_xs_weakness_acceleration_accel_5d
    ECONOMIC RATIONALE: Acceleration of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(5).diff(_TD_MON)

def rwxs_332_xs_weakness_acceleration_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_332_xs_weakness_acceleration_accel_21d
    ECONOMIC RATIONALE: Acceleration of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(21).diff(_TD_MON)

def rwxs_333_xs_weakness_acceleration_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_333_xs_weakness_acceleration_accel_63d
    ECONOMIC RATIONALE: Acceleration of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(63).diff(_TD_MON)

def rwxs_334_xs_weakness_acceleration_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_334_xs_weakness_acceleration_accel_126d
    ECONOMIC RATIONALE: Acceleration of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(126).diff(_TD_MON)

def rwxs_335_xs_weakness_acceleration_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_335_xs_weakness_acceleration_accel_252d
    ECONOMIC RATIONALE: Acceleration of xs_weakness_acceleration. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).diff(252).diff(_TD_MON)

def rwxs_336_relative_volatility_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_336_relative_volatility_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(5).diff(_TD_MON)

def rwxs_337_relative_volatility_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_337_relative_volatility_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(21).diff(_TD_MON)

def rwxs_338_relative_volatility_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_338_relative_volatility_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(63).diff(_TD_MON)

def rwxs_339_relative_volatility_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_339_relative_volatility_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(126).diff(_TD_MON)

def rwxs_340_relative_volatility_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_340_relative_volatility_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_volatility. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).diff(252).diff(_TD_MON)

def rwxs_341_relative_strength_rank_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_341_relative_strength_rank_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(5).diff(_TD_MON)

def rwxs_342_relative_strength_rank_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_342_relative_strength_rank_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(21).diff(_TD_MON)

def rwxs_343_relative_strength_rank_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_343_relative_strength_rank_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(63).diff(_TD_MON)

def rwxs_344_relative_strength_rank_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_344_relative_strength_rank_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(126).diff(_TD_MON)

def rwxs_345_relative_strength_rank_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_345_relative_strength_rank_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_strength_rank. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).diff(252).diff(_TD_MON)

def rwxs_346_market_decoupling_flag_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_346_market_decoupling_flag_accel_5d
    ECONOMIC RATIONALE: Acceleration of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(5).diff(_TD_MON)

def rwxs_347_market_decoupling_flag_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_347_market_decoupling_flag_accel_21d
    ECONOMIC RATIONALE: Acceleration of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(21).diff(_TD_MON)

def rwxs_348_market_decoupling_flag_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_348_market_decoupling_flag_accel_63d
    ECONOMIC RATIONALE: Acceleration of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(63).diff(_TD_MON)

def rwxs_349_market_decoupling_flag_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_349_market_decoupling_flag_accel_126d
    ECONOMIC RATIONALE: Acceleration of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(126).diff(_TD_MON)

def rwxs_350_market_decoupling_flag_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_350_market_decoupling_flag_accel_252d
    ECONOMIC RATIONALE: Acceleration of market_decoupling_flag. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).diff(252).diff(_TD_MON)

def rwxs_351_relative_low_test_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_351_relative_low_test_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(5).diff(_TD_MON)

def rwxs_352_relative_low_test_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_352_relative_low_test_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(21).diff(_TD_MON)

def rwxs_353_relative_low_test_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_353_relative_low_test_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(63).diff(_TD_MON)

def rwxs_354_relative_low_test_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_354_relative_low_test_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(126).diff(_TD_MON)

def rwxs_355_relative_low_test_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_355_relative_low_test_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_low_test. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).diff(252).diff(_TD_MON)

def rwxs_356_relative_weakness_score_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_356_relative_weakness_score_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(5).diff(_TD_MON)

def rwxs_357_relative_weakness_score_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_357_relative_weakness_score_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(21).diff(_TD_MON)

def rwxs_358_relative_weakness_score_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_358_relative_weakness_score_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(63).diff(_TD_MON)

def rwxs_359_relative_weakness_score_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_359_relative_weakness_score_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(126).diff(_TD_MON)

def rwxs_360_relative_weakness_score_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_360_relative_weakness_score_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_weakness_score. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).diff(252).diff(_TD_MON)

def rwxs_361_excess_volatility_z_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_361_excess_volatility_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(5).diff(_TD_MON)

def rwxs_362_excess_volatility_z_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_362_excess_volatility_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(21).diff(_TD_MON)

def rwxs_363_excess_volatility_z_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_363_excess_volatility_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(63).diff(_TD_MON)

def rwxs_364_excess_volatility_z_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_364_excess_volatility_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(126).diff(_TD_MON)

def rwxs_365_excess_volatility_z_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_365_excess_volatility_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of excess_volatility_z. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).diff(252).diff(_TD_MON)

def rwxs_366_relative_strength_roc_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_366_relative_strength_roc_accel_5d
    ECONOMIC RATIONALE: Acceleration of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(5).diff(_TD_MON)

def rwxs_367_relative_strength_roc_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_367_relative_strength_roc_accel_21d
    ECONOMIC RATIONALE: Acceleration of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(21).diff(_TD_MON)

def rwxs_368_relative_strength_roc_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_368_relative_strength_roc_accel_63d
    ECONOMIC RATIONALE: Acceleration of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(63).diff(_TD_MON)

def rwxs_369_relative_strength_roc_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_369_relative_strength_roc_accel_126d
    ECONOMIC RATIONALE: Acceleration of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(126).diff(_TD_MON)

def rwxs_370_relative_strength_roc_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_370_relative_strength_roc_accel_252d
    ECONOMIC RATIONALE: Acceleration of relative_strength_roc. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).diff(252).diff(_TD_MON)

def rwxs_371_market_beta_zscore_accel_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_371_market_beta_zscore_accel_5d
    ECONOMIC RATIONALE: Acceleration of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(5).diff(_TD_MON)

def rwxs_372_market_beta_zscore_accel_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_372_market_beta_zscore_accel_21d
    ECONOMIC RATIONALE: Acceleration of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(21).diff(_TD_MON)

def rwxs_373_market_beta_zscore_accel_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_373_market_beta_zscore_accel_63d
    ECONOMIC RATIONALE: Acceleration of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(63).diff(_TD_MON)

def rwxs_374_market_beta_zscore_accel_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_374_market_beta_zscore_accel_126d
    ECONOMIC RATIONALE: Acceleration of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(126).diff(_TD_MON)

def rwxs_375_market_beta_zscore_accel_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_375_market_beta_zscore_accel_252d
    ECONOMIC RATIONALE: Acceleration of market_beta_zscore. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V123_REGISTRY_ACCEL = {
    "rwxs_301_relative_return_21d_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_301_relative_return_21d_accel_5d},
    "rwxs_302_relative_return_21d_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_302_relative_return_21d_accel_21d},
    "rwxs_303_relative_return_21d_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_303_relative_return_21d_accel_63d},
    "rwxs_304_relative_return_21d_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_304_relative_return_21d_accel_126d},
    "rwxs_305_relative_return_21d_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_305_relative_return_21d_accel_252d},
    "rwxs_306_relative_drawdown_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_306_relative_drawdown_accel_5d},
    "rwxs_307_relative_drawdown_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_307_relative_drawdown_accel_21d},
    "rwxs_308_relative_drawdown_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_308_relative_drawdown_accel_63d},
    "rwxs_309_relative_drawdown_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_309_relative_drawdown_accel_126d},
    "rwxs_310_relative_drawdown_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_310_relative_drawdown_accel_252d},
    "rwxs_311_beta_adjusted_alpha_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_311_beta_adjusted_alpha_accel_5d},
    "rwxs_312_beta_adjusted_alpha_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_312_beta_adjusted_alpha_accel_21d},
    "rwxs_313_beta_adjusted_alpha_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_313_beta_adjusted_alpha_accel_63d},
    "rwxs_314_beta_adjusted_alpha_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_314_beta_adjusted_alpha_accel_126d},
    "rwxs_315_beta_adjusted_alpha_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_315_beta_adjusted_alpha_accel_252d},
    "rwxs_316_relative_weakness_z_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_316_relative_weakness_z_accel_5d},
    "rwxs_317_relative_weakness_z_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_317_relative_weakness_z_accel_21d},
    "rwxs_318_relative_weakness_z_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_318_relative_weakness_z_accel_63d},
    "rwxs_319_relative_weakness_z_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_319_relative_weakness_z_accel_126d},
    "rwxs_320_relative_weakness_z_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_320_relative_weakness_z_accel_252d},
    "rwxs_321_underperformance_persistence_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_321_underperformance_persistence_accel_5d},
    "rwxs_322_underperformance_persistence_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_322_underperformance_persistence_accel_21d},
    "rwxs_323_underperformance_persistence_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_323_underperformance_persistence_accel_63d},
    "rwxs_324_underperformance_persistence_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_324_underperformance_persistence_accel_126d},
    "rwxs_325_underperformance_persistence_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_325_underperformance_persistence_accel_252d},
    "rwxs_326_relative_momentum_div_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_326_relative_momentum_div_accel_5d},
    "rwxs_327_relative_momentum_div_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_327_relative_momentum_div_accel_21d},
    "rwxs_328_relative_momentum_div_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_328_relative_momentum_div_accel_63d},
    "rwxs_329_relative_momentum_div_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_329_relative_momentum_div_accel_126d},
    "rwxs_330_relative_momentum_div_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_330_relative_momentum_div_accel_252d},
    "rwxs_331_xs_weakness_acceleration_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_331_xs_weakness_acceleration_accel_5d},
    "rwxs_332_xs_weakness_acceleration_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_332_xs_weakness_acceleration_accel_21d},
    "rwxs_333_xs_weakness_acceleration_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_333_xs_weakness_acceleration_accel_63d},
    "rwxs_334_xs_weakness_acceleration_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_334_xs_weakness_acceleration_accel_126d},
    "rwxs_335_xs_weakness_acceleration_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_335_xs_weakness_acceleration_accel_252d},
    "rwxs_336_relative_volatility_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_336_relative_volatility_accel_5d},
    "rwxs_337_relative_volatility_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_337_relative_volatility_accel_21d},
    "rwxs_338_relative_volatility_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_338_relative_volatility_accel_63d},
    "rwxs_339_relative_volatility_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_339_relative_volatility_accel_126d},
    "rwxs_340_relative_volatility_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_340_relative_volatility_accel_252d},
    "rwxs_341_relative_strength_rank_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_341_relative_strength_rank_accel_5d},
    "rwxs_342_relative_strength_rank_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_342_relative_strength_rank_accel_21d},
    "rwxs_343_relative_strength_rank_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_343_relative_strength_rank_accel_63d},
    "rwxs_344_relative_strength_rank_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_344_relative_strength_rank_accel_126d},
    "rwxs_345_relative_strength_rank_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_345_relative_strength_rank_accel_252d},
    "rwxs_346_market_decoupling_flag_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_346_market_decoupling_flag_accel_5d},
    "rwxs_347_market_decoupling_flag_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_347_market_decoupling_flag_accel_21d},
    "rwxs_348_market_decoupling_flag_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_348_market_decoupling_flag_accel_63d},
    "rwxs_349_market_decoupling_flag_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_349_market_decoupling_flag_accel_126d},
    "rwxs_350_market_decoupling_flag_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_350_market_decoupling_flag_accel_252d},
    "rwxs_351_relative_low_test_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_351_relative_low_test_accel_5d},
    "rwxs_352_relative_low_test_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_352_relative_low_test_accel_21d},
    "rwxs_353_relative_low_test_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_353_relative_low_test_accel_63d},
    "rwxs_354_relative_low_test_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_354_relative_low_test_accel_126d},
    "rwxs_355_relative_low_test_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_355_relative_low_test_accel_252d},
    "rwxs_356_relative_weakness_score_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_356_relative_weakness_score_accel_5d},
    "rwxs_357_relative_weakness_score_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_357_relative_weakness_score_accel_21d},
    "rwxs_358_relative_weakness_score_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_358_relative_weakness_score_accel_63d},
    "rwxs_359_relative_weakness_score_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_359_relative_weakness_score_accel_126d},
    "rwxs_360_relative_weakness_score_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_360_relative_weakness_score_accel_252d},
    "rwxs_361_excess_volatility_z_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_361_excess_volatility_z_accel_5d},
    "rwxs_362_excess_volatility_z_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_362_excess_volatility_z_accel_21d},
    "rwxs_363_excess_volatility_z_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_363_excess_volatility_z_accel_63d},
    "rwxs_364_excess_volatility_z_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_364_excess_volatility_z_accel_126d},
    "rwxs_365_excess_volatility_z_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_365_excess_volatility_z_accel_252d},
    "rwxs_366_relative_strength_roc_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_366_relative_strength_roc_accel_5d},
    "rwxs_367_relative_strength_roc_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_367_relative_strength_roc_accel_21d},
    "rwxs_368_relative_strength_roc_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_368_relative_strength_roc_accel_63d},
    "rwxs_369_relative_strength_roc_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_369_relative_strength_roc_accel_126d},
    "rwxs_370_relative_strength_roc_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_370_relative_strength_roc_accel_252d},
    "rwxs_371_market_beta_zscore_accel_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_371_market_beta_zscore_accel_5d},
    "rwxs_372_market_beta_zscore_accel_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_372_market_beta_zscore_accel_21d},
    "rwxs_373_market_beta_zscore_accel_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_373_market_beta_zscore_accel_63d},
    "rwxs_374_market_beta_zscore_accel_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_374_market_beta_zscore_accel_126d},
    "rwxs_375_market_beta_zscore_accel_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_375_market_beta_zscore_accel_252d},
}
