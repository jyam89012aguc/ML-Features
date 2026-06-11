"""
123_relative_weakness_xs — Statistical Moments
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

def rwxs_376_relative_return_21d_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_376_relative_return_21d_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_return_21d over 5d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(5).skew()

def rwxs_377_relative_return_21d_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_377_relative_return_21d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_return_21d over 5d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(5).kurt()

def rwxs_378_relative_return_21d_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_378_relative_return_21d_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_return_21d over 21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(21).skew()

def rwxs_379_relative_return_21d_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_379_relative_return_21d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_return_21d over 21d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(21).kurt()

def rwxs_380_relative_return_21d_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_380_relative_return_21d_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_return_21d over 63d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(63).skew()

def rwxs_381_relative_return_21d_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_381_relative_return_21d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_return_21d over 63d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(63).kurt()

def rwxs_382_relative_return_21d_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_382_relative_return_21d_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_return_21d over 126d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(126).skew()

def rwxs_383_relative_return_21d_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_383_relative_return_21d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_return_21d over 126d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(126).kurt()

def rwxs_384_relative_return_21d_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_384_relative_return_21d_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_return_21d over 252d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(252).skew()

def rwxs_385_relative_return_21d_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_385_relative_return_21d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_return_21d over 252d. Excess return over the market index.
    """
    return (close.pct_change(21) - mkt_close.pct_change(21)).rolling(252).kurt()

def rwxs_386_relative_drawdown_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_386_relative_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_drawdown over 5d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(5).skew()

def rwxs_387_relative_drawdown_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_387_relative_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_drawdown over 5d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(5).kurt()

def rwxs_388_relative_drawdown_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_388_relative_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_drawdown over 21d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(21).skew()

def rwxs_389_relative_drawdown_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_389_relative_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_drawdown over 21d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(21).kurt()

def rwxs_390_relative_drawdown_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_390_relative_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_drawdown over 63d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(63).skew()

def rwxs_391_relative_drawdown_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_391_relative_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_drawdown over 63d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(63).kurt()

def rwxs_392_relative_drawdown_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_392_relative_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_drawdown over 126d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(126).skew()

def rwxs_393_relative_drawdown_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_393_relative_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_drawdown over 126d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(126).kurt()

def rwxs_394_relative_drawdown_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_394_relative_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_drawdown over 252d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(252).skew()

def rwxs_395_relative_drawdown_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_395_relative_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_drawdown over 252d. Drawdown depth relative to market drawdown.
    """
    return ((close/close.rolling(252).max()) - (mkt_close/mkt_close.rolling(252).max())).rolling(252).kurt()

def rwxs_396_beta_adjusted_alpha_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_396_beta_adjusted_alpha_skew_5d
    ECONOMIC RATIONALE: Skewness of beta_adjusted_alpha over 5d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(5).skew()

def rwxs_397_beta_adjusted_alpha_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_397_beta_adjusted_alpha_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of beta_adjusted_alpha over 5d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(5).kurt()

def rwxs_398_beta_adjusted_alpha_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_398_beta_adjusted_alpha_skew_21d
    ECONOMIC RATIONALE: Skewness of beta_adjusted_alpha over 21d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(21).skew()

def rwxs_399_beta_adjusted_alpha_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_399_beta_adjusted_alpha_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of beta_adjusted_alpha over 21d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(21).kurt()

def rwxs_400_beta_adjusted_alpha_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_400_beta_adjusted_alpha_skew_63d
    ECONOMIC RATIONALE: Skewness of beta_adjusted_alpha over 63d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(63).skew()

def rwxs_401_beta_adjusted_alpha_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_401_beta_adjusted_alpha_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of beta_adjusted_alpha over 63d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(63).kurt()

def rwxs_402_beta_adjusted_alpha_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_402_beta_adjusted_alpha_skew_126d
    ECONOMIC RATIONALE: Skewness of beta_adjusted_alpha over 126d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(126).skew()

def rwxs_403_beta_adjusted_alpha_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_403_beta_adjusted_alpha_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of beta_adjusted_alpha over 126d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(126).kurt()

def rwxs_404_beta_adjusted_alpha_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_404_beta_adjusted_alpha_skew_252d
    ECONOMIC RATIONALE: Skewness of beta_adjusted_alpha over 252d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(252).skew()

def rwxs_405_beta_adjusted_alpha_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_405_beta_adjusted_alpha_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of beta_adjusted_alpha over 252d. 21-day alpha adjusted for rolling beta.
    """
    return (close.pct_change(21) - (close.pct_change(1).rolling(252).corr(mkt_close.pct_change(1)) * (close.rolling(252).std()/mkt_close.rolling(252).std()) * mkt_close.pct_change(21))).rolling(252).kurt()

def rwxs_406_relative_weakness_z_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_406_relative_weakness_z_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_weakness_z over 5d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(5).skew()

def rwxs_407_relative_weakness_z_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_407_relative_weakness_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_z over 5d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(5).kurt()

def rwxs_408_relative_weakness_z_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_408_relative_weakness_z_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_weakness_z over 21d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(21).skew()

def rwxs_409_relative_weakness_z_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_409_relative_weakness_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_z over 21d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(21).kurt()

def rwxs_410_relative_weakness_z_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_410_relative_weakness_z_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_weakness_z over 63d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(63).skew()

def rwxs_411_relative_weakness_z_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_411_relative_weakness_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_z over 63d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(63).kurt()

def rwxs_412_relative_weakness_z_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_412_relative_weakness_z_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_weakness_z over 126d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(126).skew()

def rwxs_413_relative_weakness_z_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_413_relative_weakness_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_z over 126d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(126).kurt()

def rwxs_414_relative_weakness_z_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_414_relative_weakness_z_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_weakness_z over 252d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(252).skew()

def rwxs_415_relative_weakness_z_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_415_relative_weakness_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_z over 252d. Z-score of relative performance.
    """
    return (_zscore_rolling(close.pct_change(21) - mkt_close.pct_change(21), 252)).rolling(252).kurt()

def rwxs_416_underperformance_persistence_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_416_underperformance_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of underperformance_persistence over 5d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(5).skew()

def rwxs_417_underperformance_persistence_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_417_underperformance_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of underperformance_persistence over 5d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(5).kurt()

def rwxs_418_underperformance_persistence_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_418_underperformance_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of underperformance_persistence over 21d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(21).skew()

def rwxs_419_underperformance_persistence_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_419_underperformance_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of underperformance_persistence over 21d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(21).kurt()

def rwxs_420_underperformance_persistence_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_420_underperformance_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of underperformance_persistence over 63d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(63).skew()

def rwxs_421_underperformance_persistence_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_421_underperformance_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of underperformance_persistence over 63d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(63).kurt()

def rwxs_422_underperformance_persistence_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_422_underperformance_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of underperformance_persistence over 126d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(126).skew()

def rwxs_423_underperformance_persistence_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_423_underperformance_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of underperformance_persistence over 126d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(126).kurt()

def rwxs_424_underperformance_persistence_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_424_underperformance_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of underperformance_persistence over 252d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(252).skew()

def rwxs_425_underperformance_persistence_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_425_underperformance_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of underperformance_persistence over 252d. Frequency of days underperforming the market.
    """
    return (((close.pct_change(1) < mkt_close.pct_change(1)).rolling(21).sum())).rolling(252).kurt()

def rwxs_426_relative_momentum_div_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_426_relative_momentum_div_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_momentum_div over 5d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(5).skew()

def rwxs_427_relative_momentum_div_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_427_relative_momentum_div_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_momentum_div over 5d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(5).kurt()

def rwxs_428_relative_momentum_div_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_428_relative_momentum_div_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_momentum_div over 21d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(21).skew()

def rwxs_429_relative_momentum_div_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_429_relative_momentum_div_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_momentum_div over 21d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(21).kurt()

def rwxs_430_relative_momentum_div_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_430_relative_momentum_div_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_momentum_div over 63d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(63).skew()

def rwxs_431_relative_momentum_div_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_431_relative_momentum_div_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_momentum_div over 63d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(63).kurt()

def rwxs_432_relative_momentum_div_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_432_relative_momentum_div_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_momentum_div over 126d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(126).skew()

def rwxs_433_relative_momentum_div_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_433_relative_momentum_div_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_momentum_div over 126d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(126).kurt()

def rwxs_434_relative_momentum_div_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_434_relative_momentum_div_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_momentum_div over 252d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(252).skew()

def rwxs_435_relative_momentum_div_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_435_relative_momentum_div_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_momentum_div over 252d. Ratio of stock momentum to market momentum.
    """
    return (close.pct_change(63) / mkt_close.pct_change(63).replace(0, 1e-9)).rolling(252).kurt()

def rwxs_436_xs_weakness_acceleration_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_436_xs_weakness_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_weakness_acceleration over 5d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(5).skew()

def rwxs_437_xs_weakness_acceleration_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_437_xs_weakness_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_weakness_acceleration over 5d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(5).kurt()

def rwxs_438_xs_weakness_acceleration_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_438_xs_weakness_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_weakness_acceleration over 21d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(21).skew()

def rwxs_439_xs_weakness_acceleration_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_439_xs_weakness_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_weakness_acceleration over 21d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(21).kurt()

def rwxs_440_xs_weakness_acceleration_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_440_xs_weakness_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_weakness_acceleration over 63d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(63).skew()

def rwxs_441_xs_weakness_acceleration_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_441_xs_weakness_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_weakness_acceleration over 63d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(63).kurt()

def rwxs_442_xs_weakness_acceleration_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_442_xs_weakness_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_weakness_acceleration over 126d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(126).skew()

def rwxs_443_xs_weakness_acceleration_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_443_xs_weakness_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_weakness_acceleration over 126d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(126).kurt()

def rwxs_444_xs_weakness_acceleration_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_444_xs_weakness_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_weakness_acceleration over 252d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(252).skew()

def rwxs_445_xs_weakness_acceleration_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_445_xs_weakness_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_weakness_acceleration over 252d. Acceleration of underperformance.
    """
    return ((close.pct_change(21) - mkt_close.pct_change(21)).diff(21)).rolling(252).kurt()

def rwxs_446_relative_volatility_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_446_relative_volatility_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_volatility over 5d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(5).skew()

def rwxs_447_relative_volatility_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_447_relative_volatility_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_volatility over 5d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(5).kurt()

def rwxs_448_relative_volatility_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_448_relative_volatility_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_volatility over 21d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(21).skew()

def rwxs_449_relative_volatility_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_449_relative_volatility_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_volatility over 21d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(21).kurt()

def rwxs_450_relative_volatility_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_450_relative_volatility_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_volatility over 63d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(63).skew()

def rwxs_451_relative_volatility_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_451_relative_volatility_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_volatility over 63d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(63).kurt()

def rwxs_452_relative_volatility_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_452_relative_volatility_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_volatility over 126d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(126).skew()

def rwxs_453_relative_volatility_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_453_relative_volatility_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_volatility over 126d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(126).kurt()

def rwxs_454_relative_volatility_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_454_relative_volatility_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_volatility over 252d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(252).skew()

def rwxs_455_relative_volatility_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_455_relative_volatility_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_volatility over 252d. Stock volatility relative to market volatility.
    """
    return (close.rolling(21).std() / mkt_close.rolling(21).std()).rolling(252).kurt()

def rwxs_456_relative_strength_rank_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_456_relative_strength_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_strength_rank over 5d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(5).skew()

def rwxs_457_relative_strength_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_457_relative_strength_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_rank over 5d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(5).kurt()

def rwxs_458_relative_strength_rank_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_458_relative_strength_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_strength_rank over 21d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(21).skew()

def rwxs_459_relative_strength_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_459_relative_strength_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_rank over 21d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(21).kurt()

def rwxs_460_relative_strength_rank_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_460_relative_strength_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_strength_rank over 63d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(63).skew()

def rwxs_461_relative_strength_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_461_relative_strength_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_rank over 63d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(63).kurt()

def rwxs_462_relative_strength_rank_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_462_relative_strength_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_strength_rank over 126d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(126).skew()

def rwxs_463_relative_strength_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_463_relative_strength_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_rank over 126d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(126).kurt()

def rwxs_464_relative_strength_rank_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_464_relative_strength_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_strength_rank over 252d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(252).skew()

def rwxs_465_relative_strength_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_465_relative_strength_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_rank over 252d. Historical rank of relative price level.
    """
    return (_rank_pct(close/mkt_close, 252)).rolling(252).kurt()

def rwxs_466_market_decoupling_flag_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_466_market_decoupling_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of market_decoupling_flag over 5d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(5).skew()

def rwxs_467_market_decoupling_flag_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_467_market_decoupling_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of market_decoupling_flag over 5d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(5).kurt()

def rwxs_468_market_decoupling_flag_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_468_market_decoupling_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of market_decoupling_flag over 21d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(21).skew()

def rwxs_469_market_decoupling_flag_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_469_market_decoupling_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of market_decoupling_flag over 21d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(21).kurt()

def rwxs_470_market_decoupling_flag_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_470_market_decoupling_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of market_decoupling_flag over 63d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(63).skew()

def rwxs_471_market_decoupling_flag_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_471_market_decoupling_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of market_decoupling_flag over 63d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(63).kurt()

def rwxs_472_market_decoupling_flag_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_472_market_decoupling_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of market_decoupling_flag over 126d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(126).skew()

def rwxs_473_market_decoupling_flag_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_473_market_decoupling_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of market_decoupling_flag over 126d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(126).kurt()

def rwxs_474_market_decoupling_flag_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_474_market_decoupling_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of market_decoupling_flag over 252d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(252).skew()

def rwxs_475_market_decoupling_flag_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_475_market_decoupling_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of market_decoupling_flag over 252d. Loss of correlation with market indices during distress.
    """
    return ((close.pct_change(21).rolling(63).corr(mkt_close.pct_change(21)) < 0.3).astype(float)).rolling(252).kurt()

def rwxs_476_relative_low_test_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_476_relative_low_test_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_low_test over 5d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(5).skew()

def rwxs_477_relative_low_test_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_477_relative_low_test_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_low_test over 5d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(5).kurt()

def rwxs_478_relative_low_test_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_478_relative_low_test_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_low_test over 21d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(21).skew()

def rwxs_479_relative_low_test_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_479_relative_low_test_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_low_test over 21d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(21).kurt()

def rwxs_480_relative_low_test_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_480_relative_low_test_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_low_test over 63d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(63).skew()

def rwxs_481_relative_low_test_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_481_relative_low_test_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_low_test over 63d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(63).kurt()

def rwxs_482_relative_low_test_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_482_relative_low_test_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_low_test over 126d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(126).skew()

def rwxs_483_relative_low_test_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_483_relative_low_test_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_low_test over 126d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(126).kurt()

def rwxs_484_relative_low_test_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_484_relative_low_test_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_low_test over 252d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(252).skew()

def rwxs_485_relative_low_test_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_485_relative_low_test_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_low_test over 252d. Proximity to lows relative to the market.
    """
    return ((close / close.rolling(252).min()) / (mkt_close / mkt_close.rolling(252).min()).replace(0, 1e-9)).rolling(252).kurt()

def rwxs_486_relative_weakness_score_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_486_relative_weakness_score_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_weakness_score over 5d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(5).skew()

def rwxs_487_relative_weakness_score_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_487_relative_weakness_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_score over 5d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(5).kurt()

def rwxs_488_relative_weakness_score_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_488_relative_weakness_score_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_weakness_score over 21d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(21).skew()

def rwxs_489_relative_weakness_score_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_489_relative_weakness_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_score over 21d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(21).kurt()

def rwxs_490_relative_weakness_score_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_490_relative_weakness_score_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_weakness_score over 63d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(63).skew()

def rwxs_491_relative_weakness_score_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_491_relative_weakness_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_score over 63d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(63).kurt()

def rwxs_492_relative_weakness_score_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_492_relative_weakness_score_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_weakness_score over 126d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(126).skew()

def rwxs_493_relative_weakness_score_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_493_relative_weakness_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_score over 126d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(126).kurt()

def rwxs_494_relative_weakness_score_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_494_relative_weakness_score_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_weakness_score over 252d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(252).skew()

def rwxs_495_relative_weakness_score_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_495_relative_weakness_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_weakness_score over 252d. Binary flag for absolute and relative weakness.
    """
    return (((close.pct_change(21) < -0.1) & (close.pct_change(21) < mkt_close.pct_change(21))).astype(float)).rolling(252).kurt()

def rwxs_496_excess_volatility_z_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_496_excess_volatility_z_skew_5d
    ECONOMIC RATIONALE: Skewness of excess_volatility_z over 5d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(5).skew()

def rwxs_497_excess_volatility_z_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_497_excess_volatility_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of excess_volatility_z over 5d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(5).kurt()

def rwxs_498_excess_volatility_z_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_498_excess_volatility_z_skew_21d
    ECONOMIC RATIONALE: Skewness of excess_volatility_z over 21d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(21).skew()

def rwxs_499_excess_volatility_z_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_499_excess_volatility_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of excess_volatility_z over 21d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(21).kurt()

def rwxs_500_excess_volatility_z_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_500_excess_volatility_z_skew_63d
    ECONOMIC RATIONALE: Skewness of excess_volatility_z over 63d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(63).skew()

def rwxs_501_excess_volatility_z_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_501_excess_volatility_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of excess_volatility_z over 63d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(63).kurt()

def rwxs_502_excess_volatility_z_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_502_excess_volatility_z_skew_126d
    ECONOMIC RATIONALE: Skewness of excess_volatility_z over 126d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(126).skew()

def rwxs_503_excess_volatility_z_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_503_excess_volatility_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of excess_volatility_z over 126d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(126).kurt()

def rwxs_504_excess_volatility_z_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_504_excess_volatility_z_skew_252d
    ECONOMIC RATIONALE: Skewness of excess_volatility_z over 252d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(252).skew()

def rwxs_505_excess_volatility_z_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_505_excess_volatility_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of excess_volatility_z over 252d. Abnormal excess volatility over the market.
    """
    return (_zscore_rolling(close.rolling(21).std() - mkt_close.rolling(21).std(), 252)).rolling(252).kurt()

def rwxs_506_relative_strength_roc_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_506_relative_strength_roc_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_strength_roc over 5d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(5).skew()

def rwxs_507_relative_strength_roc_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_507_relative_strength_roc_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_roc over 5d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(5).kurt()

def rwxs_508_relative_strength_roc_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_508_relative_strength_roc_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_strength_roc over 21d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(21).skew()

def rwxs_509_relative_strength_roc_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_509_relative_strength_roc_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_roc over 21d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(21).kurt()

def rwxs_510_relative_strength_roc_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_510_relative_strength_roc_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_strength_roc over 63d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(63).skew()

def rwxs_511_relative_strength_roc_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_511_relative_strength_roc_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_roc over 63d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(63).kurt()

def rwxs_512_relative_strength_roc_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_512_relative_strength_roc_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_strength_roc over 126d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(126).skew()

def rwxs_513_relative_strength_roc_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_513_relative_strength_roc_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_roc over 126d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(126).kurt()

def rwxs_514_relative_strength_roc_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_514_relative_strength_roc_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_strength_roc over 252d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(252).skew()

def rwxs_515_relative_strength_roc_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_515_relative_strength_roc_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_strength_roc over 252d. Rate of change in the relative strength line.
    """
    return ((close/mkt_close).pct_change(21)).rolling(252).kurt()

def rwxs_516_market_beta_zscore_skew_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_516_market_beta_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of market_beta_zscore over 5d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(5).skew()

def rwxs_517_market_beta_zscore_kurt_5d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_517_market_beta_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of market_beta_zscore over 5d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(5).kurt()

def rwxs_518_market_beta_zscore_skew_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_518_market_beta_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of market_beta_zscore over 21d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(21).skew()

def rwxs_519_market_beta_zscore_kurt_21d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_519_market_beta_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of market_beta_zscore over 21d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(21).kurt()

def rwxs_520_market_beta_zscore_skew_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_520_market_beta_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of market_beta_zscore over 63d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(63).skew()

def rwxs_521_market_beta_zscore_kurt_63d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_521_market_beta_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of market_beta_zscore over 63d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(63).kurt()

def rwxs_522_market_beta_zscore_skew_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_522_market_beta_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of market_beta_zscore over 126d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(126).skew()

def rwxs_523_market_beta_zscore_kurt_126d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_523_market_beta_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of market_beta_zscore over 126d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(126).kurt()

def rwxs_524_market_beta_zscore_skew_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_524_market_beta_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of market_beta_zscore over 252d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(252).skew()

def rwxs_525_market_beta_zscore_kurt_252d(close: pd.Series, mkt_close: pd.Series) -> pd.Series:
    """
    rwxs_525_market_beta_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of market_beta_zscore over 252d. Anomaly in market sensitivity.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(63).corr(mkt_close.pct_change(1)), 252)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V123_REGISTRY_MOMENTS = {
    "rwxs_376_relative_return_21d_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_376_relative_return_21d_skew_5d},
    "rwxs_377_relative_return_21d_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_377_relative_return_21d_kurt_5d},
    "rwxs_378_relative_return_21d_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_378_relative_return_21d_skew_21d},
    "rwxs_379_relative_return_21d_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_379_relative_return_21d_kurt_21d},
    "rwxs_380_relative_return_21d_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_380_relative_return_21d_skew_63d},
    "rwxs_381_relative_return_21d_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_381_relative_return_21d_kurt_63d},
    "rwxs_382_relative_return_21d_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_382_relative_return_21d_skew_126d},
    "rwxs_383_relative_return_21d_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_383_relative_return_21d_kurt_126d},
    "rwxs_384_relative_return_21d_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_384_relative_return_21d_skew_252d},
    "rwxs_385_relative_return_21d_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_385_relative_return_21d_kurt_252d},
    "rwxs_386_relative_drawdown_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_386_relative_drawdown_skew_5d},
    "rwxs_387_relative_drawdown_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_387_relative_drawdown_kurt_5d},
    "rwxs_388_relative_drawdown_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_388_relative_drawdown_skew_21d},
    "rwxs_389_relative_drawdown_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_389_relative_drawdown_kurt_21d},
    "rwxs_390_relative_drawdown_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_390_relative_drawdown_skew_63d},
    "rwxs_391_relative_drawdown_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_391_relative_drawdown_kurt_63d},
    "rwxs_392_relative_drawdown_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_392_relative_drawdown_skew_126d},
    "rwxs_393_relative_drawdown_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_393_relative_drawdown_kurt_126d},
    "rwxs_394_relative_drawdown_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_394_relative_drawdown_skew_252d},
    "rwxs_395_relative_drawdown_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_395_relative_drawdown_kurt_252d},
    "rwxs_396_beta_adjusted_alpha_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_396_beta_adjusted_alpha_skew_5d},
    "rwxs_397_beta_adjusted_alpha_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_397_beta_adjusted_alpha_kurt_5d},
    "rwxs_398_beta_adjusted_alpha_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_398_beta_adjusted_alpha_skew_21d},
    "rwxs_399_beta_adjusted_alpha_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_399_beta_adjusted_alpha_kurt_21d},
    "rwxs_400_beta_adjusted_alpha_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_400_beta_adjusted_alpha_skew_63d},
    "rwxs_401_beta_adjusted_alpha_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_401_beta_adjusted_alpha_kurt_63d},
    "rwxs_402_beta_adjusted_alpha_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_402_beta_adjusted_alpha_skew_126d},
    "rwxs_403_beta_adjusted_alpha_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_403_beta_adjusted_alpha_kurt_126d},
    "rwxs_404_beta_adjusted_alpha_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_404_beta_adjusted_alpha_skew_252d},
    "rwxs_405_beta_adjusted_alpha_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_405_beta_adjusted_alpha_kurt_252d},
    "rwxs_406_relative_weakness_z_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_406_relative_weakness_z_skew_5d},
    "rwxs_407_relative_weakness_z_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_407_relative_weakness_z_kurt_5d},
    "rwxs_408_relative_weakness_z_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_408_relative_weakness_z_skew_21d},
    "rwxs_409_relative_weakness_z_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_409_relative_weakness_z_kurt_21d},
    "rwxs_410_relative_weakness_z_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_410_relative_weakness_z_skew_63d},
    "rwxs_411_relative_weakness_z_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_411_relative_weakness_z_kurt_63d},
    "rwxs_412_relative_weakness_z_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_412_relative_weakness_z_skew_126d},
    "rwxs_413_relative_weakness_z_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_413_relative_weakness_z_kurt_126d},
    "rwxs_414_relative_weakness_z_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_414_relative_weakness_z_skew_252d},
    "rwxs_415_relative_weakness_z_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_415_relative_weakness_z_kurt_252d},
    "rwxs_416_underperformance_persistence_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_416_underperformance_persistence_skew_5d},
    "rwxs_417_underperformance_persistence_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_417_underperformance_persistence_kurt_5d},
    "rwxs_418_underperformance_persistence_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_418_underperformance_persistence_skew_21d},
    "rwxs_419_underperformance_persistence_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_419_underperformance_persistence_kurt_21d},
    "rwxs_420_underperformance_persistence_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_420_underperformance_persistence_skew_63d},
    "rwxs_421_underperformance_persistence_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_421_underperformance_persistence_kurt_63d},
    "rwxs_422_underperformance_persistence_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_422_underperformance_persistence_skew_126d},
    "rwxs_423_underperformance_persistence_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_423_underperformance_persistence_kurt_126d},
    "rwxs_424_underperformance_persistence_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_424_underperformance_persistence_skew_252d},
    "rwxs_425_underperformance_persistence_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_425_underperformance_persistence_kurt_252d},
    "rwxs_426_relative_momentum_div_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_426_relative_momentum_div_skew_5d},
    "rwxs_427_relative_momentum_div_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_427_relative_momentum_div_kurt_5d},
    "rwxs_428_relative_momentum_div_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_428_relative_momentum_div_skew_21d},
    "rwxs_429_relative_momentum_div_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_429_relative_momentum_div_kurt_21d},
    "rwxs_430_relative_momentum_div_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_430_relative_momentum_div_skew_63d},
    "rwxs_431_relative_momentum_div_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_431_relative_momentum_div_kurt_63d},
    "rwxs_432_relative_momentum_div_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_432_relative_momentum_div_skew_126d},
    "rwxs_433_relative_momentum_div_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_433_relative_momentum_div_kurt_126d},
    "rwxs_434_relative_momentum_div_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_434_relative_momentum_div_skew_252d},
    "rwxs_435_relative_momentum_div_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_435_relative_momentum_div_kurt_252d},
    "rwxs_436_xs_weakness_acceleration_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_436_xs_weakness_acceleration_skew_5d},
    "rwxs_437_xs_weakness_acceleration_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_437_xs_weakness_acceleration_kurt_5d},
    "rwxs_438_xs_weakness_acceleration_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_438_xs_weakness_acceleration_skew_21d},
    "rwxs_439_xs_weakness_acceleration_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_439_xs_weakness_acceleration_kurt_21d},
    "rwxs_440_xs_weakness_acceleration_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_440_xs_weakness_acceleration_skew_63d},
    "rwxs_441_xs_weakness_acceleration_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_441_xs_weakness_acceleration_kurt_63d},
    "rwxs_442_xs_weakness_acceleration_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_442_xs_weakness_acceleration_skew_126d},
    "rwxs_443_xs_weakness_acceleration_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_443_xs_weakness_acceleration_kurt_126d},
    "rwxs_444_xs_weakness_acceleration_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_444_xs_weakness_acceleration_skew_252d},
    "rwxs_445_xs_weakness_acceleration_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_445_xs_weakness_acceleration_kurt_252d},
    "rwxs_446_relative_volatility_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_446_relative_volatility_skew_5d},
    "rwxs_447_relative_volatility_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_447_relative_volatility_kurt_5d},
    "rwxs_448_relative_volatility_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_448_relative_volatility_skew_21d},
    "rwxs_449_relative_volatility_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_449_relative_volatility_kurt_21d},
    "rwxs_450_relative_volatility_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_450_relative_volatility_skew_63d},
    "rwxs_451_relative_volatility_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_451_relative_volatility_kurt_63d},
    "rwxs_452_relative_volatility_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_452_relative_volatility_skew_126d},
    "rwxs_453_relative_volatility_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_453_relative_volatility_kurt_126d},
    "rwxs_454_relative_volatility_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_454_relative_volatility_skew_252d},
    "rwxs_455_relative_volatility_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_455_relative_volatility_kurt_252d},
    "rwxs_456_relative_strength_rank_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_456_relative_strength_rank_skew_5d},
    "rwxs_457_relative_strength_rank_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_457_relative_strength_rank_kurt_5d},
    "rwxs_458_relative_strength_rank_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_458_relative_strength_rank_skew_21d},
    "rwxs_459_relative_strength_rank_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_459_relative_strength_rank_kurt_21d},
    "rwxs_460_relative_strength_rank_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_460_relative_strength_rank_skew_63d},
    "rwxs_461_relative_strength_rank_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_461_relative_strength_rank_kurt_63d},
    "rwxs_462_relative_strength_rank_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_462_relative_strength_rank_skew_126d},
    "rwxs_463_relative_strength_rank_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_463_relative_strength_rank_kurt_126d},
    "rwxs_464_relative_strength_rank_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_464_relative_strength_rank_skew_252d},
    "rwxs_465_relative_strength_rank_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_465_relative_strength_rank_kurt_252d},
    "rwxs_466_market_decoupling_flag_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_466_market_decoupling_flag_skew_5d},
    "rwxs_467_market_decoupling_flag_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_467_market_decoupling_flag_kurt_5d},
    "rwxs_468_market_decoupling_flag_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_468_market_decoupling_flag_skew_21d},
    "rwxs_469_market_decoupling_flag_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_469_market_decoupling_flag_kurt_21d},
    "rwxs_470_market_decoupling_flag_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_470_market_decoupling_flag_skew_63d},
    "rwxs_471_market_decoupling_flag_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_471_market_decoupling_flag_kurt_63d},
    "rwxs_472_market_decoupling_flag_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_472_market_decoupling_flag_skew_126d},
    "rwxs_473_market_decoupling_flag_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_473_market_decoupling_flag_kurt_126d},
    "rwxs_474_market_decoupling_flag_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_474_market_decoupling_flag_skew_252d},
    "rwxs_475_market_decoupling_flag_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_475_market_decoupling_flag_kurt_252d},
    "rwxs_476_relative_low_test_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_476_relative_low_test_skew_5d},
    "rwxs_477_relative_low_test_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_477_relative_low_test_kurt_5d},
    "rwxs_478_relative_low_test_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_478_relative_low_test_skew_21d},
    "rwxs_479_relative_low_test_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_479_relative_low_test_kurt_21d},
    "rwxs_480_relative_low_test_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_480_relative_low_test_skew_63d},
    "rwxs_481_relative_low_test_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_481_relative_low_test_kurt_63d},
    "rwxs_482_relative_low_test_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_482_relative_low_test_skew_126d},
    "rwxs_483_relative_low_test_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_483_relative_low_test_kurt_126d},
    "rwxs_484_relative_low_test_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_484_relative_low_test_skew_252d},
    "rwxs_485_relative_low_test_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_485_relative_low_test_kurt_252d},
    "rwxs_486_relative_weakness_score_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_486_relative_weakness_score_skew_5d},
    "rwxs_487_relative_weakness_score_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_487_relative_weakness_score_kurt_5d},
    "rwxs_488_relative_weakness_score_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_488_relative_weakness_score_skew_21d},
    "rwxs_489_relative_weakness_score_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_489_relative_weakness_score_kurt_21d},
    "rwxs_490_relative_weakness_score_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_490_relative_weakness_score_skew_63d},
    "rwxs_491_relative_weakness_score_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_491_relative_weakness_score_kurt_63d},
    "rwxs_492_relative_weakness_score_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_492_relative_weakness_score_skew_126d},
    "rwxs_493_relative_weakness_score_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_493_relative_weakness_score_kurt_126d},
    "rwxs_494_relative_weakness_score_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_494_relative_weakness_score_skew_252d},
    "rwxs_495_relative_weakness_score_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_495_relative_weakness_score_kurt_252d},
    "rwxs_496_excess_volatility_z_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_496_excess_volatility_z_skew_5d},
    "rwxs_497_excess_volatility_z_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_497_excess_volatility_z_kurt_5d},
    "rwxs_498_excess_volatility_z_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_498_excess_volatility_z_skew_21d},
    "rwxs_499_excess_volatility_z_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_499_excess_volatility_z_kurt_21d},
    "rwxs_500_excess_volatility_z_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_500_excess_volatility_z_skew_63d},
    "rwxs_501_excess_volatility_z_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_501_excess_volatility_z_kurt_63d},
    "rwxs_502_excess_volatility_z_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_502_excess_volatility_z_skew_126d},
    "rwxs_503_excess_volatility_z_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_503_excess_volatility_z_kurt_126d},
    "rwxs_504_excess_volatility_z_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_504_excess_volatility_z_skew_252d},
    "rwxs_505_excess_volatility_z_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_505_excess_volatility_z_kurt_252d},
    "rwxs_506_relative_strength_roc_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_506_relative_strength_roc_skew_5d},
    "rwxs_507_relative_strength_roc_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_507_relative_strength_roc_kurt_5d},
    "rwxs_508_relative_strength_roc_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_508_relative_strength_roc_skew_21d},
    "rwxs_509_relative_strength_roc_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_509_relative_strength_roc_kurt_21d},
    "rwxs_510_relative_strength_roc_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_510_relative_strength_roc_skew_63d},
    "rwxs_511_relative_strength_roc_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_511_relative_strength_roc_kurt_63d},
    "rwxs_512_relative_strength_roc_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_512_relative_strength_roc_skew_126d},
    "rwxs_513_relative_strength_roc_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_513_relative_strength_roc_kurt_126d},
    "rwxs_514_relative_strength_roc_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_514_relative_strength_roc_skew_252d},
    "rwxs_515_relative_strength_roc_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_515_relative_strength_roc_kurt_252d},
    "rwxs_516_market_beta_zscore_skew_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_516_market_beta_zscore_skew_5d},
    "rwxs_517_market_beta_zscore_kurt_5d": {"inputs": ["close", "mkt_close"], "func": rwxs_517_market_beta_zscore_kurt_5d},
    "rwxs_518_market_beta_zscore_skew_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_518_market_beta_zscore_skew_21d},
    "rwxs_519_market_beta_zscore_kurt_21d": {"inputs": ["close", "mkt_close"], "func": rwxs_519_market_beta_zscore_kurt_21d},
    "rwxs_520_market_beta_zscore_skew_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_520_market_beta_zscore_skew_63d},
    "rwxs_521_market_beta_zscore_kurt_63d": {"inputs": ["close", "mkt_close"], "func": rwxs_521_market_beta_zscore_kurt_63d},
    "rwxs_522_market_beta_zscore_skew_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_522_market_beta_zscore_skew_126d},
    "rwxs_523_market_beta_zscore_kurt_126d": {"inputs": ["close", "mkt_close"], "func": rwxs_523_market_beta_zscore_kurt_126d},
    "rwxs_524_market_beta_zscore_skew_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_524_market_beta_zscore_skew_252d},
    "rwxs_525_market_beta_zscore_kurt_252d": {"inputs": ["close", "mkt_close"], "func": rwxs_525_market_beta_zscore_kurt_252d},
}
