"""
124_cross_sectional_distress_rank — Statistical Moments
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

def csdr_376_price_rank_xs_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_376_price_rank_xs_skew_5d
    ECONOMIC RATIONALE: Skewness of price_rank_xs over 5d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(5).skew()

def csdr_377_price_rank_xs_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_377_price_rank_xs_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_rank_xs over 5d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(5).kurt()

def csdr_378_price_rank_xs_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_378_price_rank_xs_skew_21d
    ECONOMIC RATIONALE: Skewness of price_rank_xs over 21d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(21).skew()

def csdr_379_price_rank_xs_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_379_price_rank_xs_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_rank_xs over 21d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(21).kurt()

def csdr_380_price_rank_xs_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_380_price_rank_xs_skew_63d
    ECONOMIC RATIONALE: Skewness of price_rank_xs over 63d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(63).skew()

def csdr_381_price_rank_xs_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_381_price_rank_xs_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_rank_xs over 63d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(63).kurt()

def csdr_382_price_rank_xs_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_382_price_rank_xs_skew_126d
    ECONOMIC RATIONALE: Skewness of price_rank_xs over 126d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(126).skew()

def csdr_383_price_rank_xs_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_383_price_rank_xs_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_rank_xs over 126d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(126).kurt()

def csdr_384_price_rank_xs_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_384_price_rank_xs_skew_252d
    ECONOMIC RATIONALE: Skewness of price_rank_xs over 252d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(252).skew()

def csdr_385_price_rank_xs_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_385_price_rank_xs_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_rank_xs over 252d. Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    return (_rank_pct(close / close.rolling(252).max(), 252)).rolling(252).kurt()

def csdr_386_volume_rank_xs_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_386_volume_rank_xs_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_rank_xs over 5d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(5).skew()

def csdr_387_volume_rank_xs_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_387_volume_rank_xs_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_rank_xs over 5d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(5).kurt()

def csdr_388_volume_rank_xs_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_388_volume_rank_xs_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_rank_xs over 21d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(21).skew()

def csdr_389_volume_rank_xs_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_389_volume_rank_xs_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_rank_xs over 21d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(21).kurt()

def csdr_390_volume_rank_xs_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_390_volume_rank_xs_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_rank_xs over 63d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(63).skew()

def csdr_391_volume_rank_xs_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_391_volume_rank_xs_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_rank_xs over 63d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(63).kurt()

def csdr_392_volume_rank_xs_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_392_volume_rank_xs_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_rank_xs over 126d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(126).skew()

def csdr_393_volume_rank_xs_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_393_volume_rank_xs_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_rank_xs over 126d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(126).kurt()

def csdr_394_volume_rank_xs_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_394_volume_rank_xs_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_rank_xs over 252d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(252).skew()

def csdr_395_volume_rank_xs_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_395_volume_rank_xs_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_rank_xs over 252d. Rank of volume intensity vs history.
    """
    return (_rank_pct(volume / volume.rolling(252).mean(), 252)).rolling(252).kurt()

def csdr_396_relative_distress_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_396_relative_distress_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_distress_rank over 5d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(5).skew()

def csdr_397_relative_distress_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_397_relative_distress_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_distress_rank over 5d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(5).kurt()

def csdr_398_relative_distress_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_398_relative_distress_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_distress_rank over 21d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(21).skew()

def csdr_399_relative_distress_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_399_relative_distress_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_distress_rank over 21d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(21).kurt()

def csdr_400_relative_distress_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_400_relative_distress_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_distress_rank over 63d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(63).skew()

def csdr_401_relative_distress_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_401_relative_distress_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_distress_rank over 63d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(63).kurt()

def csdr_402_relative_distress_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_402_relative_distress_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_distress_rank over 126d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(126).skew()

def csdr_403_relative_distress_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_403_relative_distress_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_distress_rank over 126d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(126).kurt()

def csdr_404_relative_distress_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_404_relative_distress_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_distress_rank over 252d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(252).skew()

def csdr_405_relative_distress_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_405_relative_distress_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_distress_rank over 252d. Historical rank of relative underperformance.
    """
    return (_rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)).rolling(252).kurt()

def csdr_406_xs_volatility_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_406_xs_volatility_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_volatility_rank over 5d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(5).skew()

def csdr_407_xs_volatility_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_407_xs_volatility_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_volatility_rank over 5d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(5).kurt()

def csdr_408_xs_volatility_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_408_xs_volatility_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_volatility_rank over 21d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(21).skew()

def csdr_409_xs_volatility_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_409_xs_volatility_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_volatility_rank over 21d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(21).kurt()

def csdr_410_xs_volatility_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_410_xs_volatility_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_volatility_rank over 63d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(63).skew()

def csdr_411_xs_volatility_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_411_xs_volatility_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_volatility_rank over 63d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(63).kurt()

def csdr_412_xs_volatility_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_412_xs_volatility_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_volatility_rank over 126d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(126).skew()

def csdr_413_xs_volatility_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_413_xs_volatility_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_volatility_rank over 126d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(126).kurt()

def csdr_414_xs_volatility_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_414_xs_volatility_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_volatility_rank over 252d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(252).skew()

def csdr_415_xs_volatility_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_415_xs_volatility_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_volatility_rank over 252d. Historical rank of realized volatility.
    """
    return (_rank_pct(close.rolling(21).std(), 252)).rolling(252).kurt()

def csdr_416_xs_drawdown_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_416_xs_drawdown_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_drawdown_rank over 5d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(5).skew()

def csdr_417_xs_drawdown_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_417_xs_drawdown_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_drawdown_rank over 5d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(5).kurt()

def csdr_418_xs_drawdown_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_418_xs_drawdown_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_drawdown_rank over 21d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(21).skew()

def csdr_419_xs_drawdown_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_419_xs_drawdown_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_drawdown_rank over 21d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(21).kurt()

def csdr_420_xs_drawdown_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_420_xs_drawdown_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_drawdown_rank over 63d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(63).skew()

def csdr_421_xs_drawdown_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_421_xs_drawdown_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_drawdown_rank over 63d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(63).kurt()

def csdr_422_xs_drawdown_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_422_xs_drawdown_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_drawdown_rank over 126d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(126).skew()

def csdr_423_xs_drawdown_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_423_xs_drawdown_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_drawdown_rank over 126d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(126).kurt()

def csdr_424_xs_drawdown_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_424_xs_drawdown_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_drawdown_rank over 252d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(252).skew()

def csdr_425_xs_drawdown_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_425_xs_drawdown_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_drawdown_rank over 252d. Historical rank of drawdown severity.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(252).kurt()

def csdr_426_relative_volume_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_426_relative_volume_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of relative_volume_rank over 5d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(5).skew()

def csdr_427_relative_volume_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_427_relative_volume_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of relative_volume_rank over 5d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(5).kurt()

def csdr_428_relative_volume_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_428_relative_volume_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of relative_volume_rank over 21d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(21).skew()

def csdr_429_relative_volume_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_429_relative_volume_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of relative_volume_rank over 21d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(21).kurt()

def csdr_430_relative_volume_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_430_relative_volume_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of relative_volume_rank over 63d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(63).skew()

def csdr_431_relative_volume_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_431_relative_volume_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of relative_volume_rank over 63d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(63).kurt()

def csdr_432_relative_volume_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_432_relative_volume_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of relative_volume_rank over 126d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(126).skew()

def csdr_433_relative_volume_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_433_relative_volume_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of relative_volume_rank over 126d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(126).kurt()

def csdr_434_relative_volume_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_434_relative_volume_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of relative_volume_rank over 252d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(252).skew()

def csdr_435_relative_volume_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_435_relative_volume_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of relative_volume_rank over 252d. Rank of volume relative to market volume.
    """
    return (_rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)).rolling(252).kurt()

def csdr_436_xs_momentum_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_436_xs_momentum_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_momentum_rank over 5d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(5).skew()

def csdr_437_xs_momentum_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_437_xs_momentum_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_momentum_rank over 5d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(5).kurt()

def csdr_438_xs_momentum_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_438_xs_momentum_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_momentum_rank over 21d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(21).skew()

def csdr_439_xs_momentum_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_439_xs_momentum_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_momentum_rank over 21d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(21).kurt()

def csdr_440_xs_momentum_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_440_xs_momentum_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_momentum_rank over 63d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(63).skew()

def csdr_441_xs_momentum_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_441_xs_momentum_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_momentum_rank over 63d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(63).kurt()

def csdr_442_xs_momentum_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_442_xs_momentum_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_momentum_rank over 126d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(126).skew()

def csdr_443_xs_momentum_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_443_xs_momentum_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_momentum_rank over 126d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(126).kurt()

def csdr_444_xs_momentum_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_444_xs_momentum_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_momentum_rank over 252d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(252).skew()

def csdr_445_xs_momentum_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_445_xs_momentum_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_momentum_rank over 252d. Rank of long-term annual momentum.
    """
    return (_rank_pct(close.pct_change(252), 252)).rolling(252).kurt()

def csdr_446_distress_rank_z_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_446_distress_rank_z_skew_5d
    ECONOMIC RATIONALE: Skewness of distress_rank_z over 5d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(5).skew()

def csdr_447_distress_rank_z_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_447_distress_rank_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distress_rank_z over 5d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(5).kurt()

def csdr_448_distress_rank_z_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_448_distress_rank_z_skew_21d
    ECONOMIC RATIONALE: Skewness of distress_rank_z over 21d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(21).skew()

def csdr_449_distress_rank_z_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_449_distress_rank_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distress_rank_z over 21d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(21).kurt()

def csdr_450_distress_rank_z_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_450_distress_rank_z_skew_63d
    ECONOMIC RATIONALE: Skewness of distress_rank_z over 63d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(63).skew()

def csdr_451_distress_rank_z_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_451_distress_rank_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distress_rank_z over 63d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(63).kurt()

def csdr_452_distress_rank_z_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_452_distress_rank_z_skew_126d
    ECONOMIC RATIONALE: Skewness of distress_rank_z over 126d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(126).skew()

def csdr_453_distress_rank_z_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_453_distress_rank_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distress_rank_z over 126d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(126).kurt()

def csdr_454_distress_rank_z_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_454_distress_rank_z_skew_252d
    ECONOMIC RATIONALE: Skewness of distress_rank_z over 252d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(252).skew()

def csdr_455_distress_rank_z_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_455_distress_rank_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distress_rank_z over 252d. Z-score of the current momentum rank.
    """
    return (_zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)).rolling(252).kurt()

def csdr_456_xs_recovery_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_456_xs_recovery_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_recovery_rank over 5d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(5).skew()

def csdr_457_xs_recovery_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_457_xs_recovery_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_recovery_rank over 5d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(5).kurt()

def csdr_458_xs_recovery_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_458_xs_recovery_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_recovery_rank over 21d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(21).skew()

def csdr_459_xs_recovery_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_459_xs_recovery_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_recovery_rank over 21d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(21).kurt()

def csdr_460_xs_recovery_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_460_xs_recovery_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_recovery_rank over 63d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(63).skew()

def csdr_461_xs_recovery_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_461_xs_recovery_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_recovery_rank over 63d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(63).kurt()

def csdr_462_xs_recovery_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_462_xs_recovery_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_recovery_rank over 126d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(126).skew()

def csdr_463_xs_recovery_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_463_xs_recovery_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_recovery_rank over 126d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(126).kurt()

def csdr_464_xs_recovery_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_464_xs_recovery_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_recovery_rank over 252d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(252).skew()

def csdr_465_xs_recovery_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_465_xs_recovery_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_recovery_rank over 252d. Rank of recovery from annual lows.
    """
    return (_rank_pct(close / close.rolling(252).min() - 1, 252)).rolling(252).kurt()

def csdr_466_xs_liquidity_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_466_xs_liquidity_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_liquidity_rank over 5d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(5).skew()

def csdr_467_xs_liquidity_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_467_xs_liquidity_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_liquidity_rank over 5d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(5).kurt()

def csdr_468_xs_liquidity_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_468_xs_liquidity_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_liquidity_rank over 21d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(21).skew()

def csdr_469_xs_liquidity_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_469_xs_liquidity_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_liquidity_rank over 21d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(21).kurt()

def csdr_470_xs_liquidity_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_470_xs_liquidity_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_liquidity_rank over 63d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(63).skew()

def csdr_471_xs_liquidity_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_471_xs_liquidity_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_liquidity_rank over 63d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(63).kurt()

def csdr_472_xs_liquidity_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_472_xs_liquidity_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_liquidity_rank over 126d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(126).skew()

def csdr_473_xs_liquidity_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_473_xs_liquidity_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_liquidity_rank over 126d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(126).kurt()

def csdr_474_xs_liquidity_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_474_xs_liquidity_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_liquidity_rank over 252d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(252).skew()

def csdr_475_xs_liquidity_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_475_xs_liquidity_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_liquidity_rank over 252d. Rank of dollar turnover.
    """
    return (_rank_pct(volume * close, 252)).rolling(252).kurt()

def csdr_476_xs_tail_risk_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_476_xs_tail_risk_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_tail_risk_rank over 5d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(5).skew()

def csdr_477_xs_tail_risk_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_477_xs_tail_risk_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_tail_risk_rank over 5d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(5).kurt()

def csdr_478_xs_tail_risk_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_478_xs_tail_risk_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_tail_risk_rank over 21d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(21).skew()

def csdr_479_xs_tail_risk_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_479_xs_tail_risk_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_tail_risk_rank over 21d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(21).kurt()

def csdr_480_xs_tail_risk_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_480_xs_tail_risk_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_tail_risk_rank over 63d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(63).skew()

def csdr_481_xs_tail_risk_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_481_xs_tail_risk_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_tail_risk_rank over 63d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(63).kurt()

def csdr_482_xs_tail_risk_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_482_xs_tail_risk_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_tail_risk_rank over 126d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(126).skew()

def csdr_483_xs_tail_risk_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_483_xs_tail_risk_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_tail_risk_rank over 126d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(126).kurt()

def csdr_484_xs_tail_risk_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_484_xs_tail_risk_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_tail_risk_rank over 252d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(252).skew()

def csdr_485_xs_tail_risk_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_485_xs_tail_risk_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_tail_risk_rank over 252d. Rank of tail risk severity.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).quantile(0.05), 252)).rolling(252).kurt()

def csdr_486_xs_asymmetry_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_486_xs_asymmetry_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_asymmetry_rank over 5d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(5).skew()

def csdr_487_xs_asymmetry_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_487_xs_asymmetry_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_asymmetry_rank over 5d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(5).kurt()

def csdr_488_xs_asymmetry_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_488_xs_asymmetry_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_asymmetry_rank over 21d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(21).skew()

def csdr_489_xs_asymmetry_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_489_xs_asymmetry_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_asymmetry_rank over 21d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(21).kurt()

def csdr_490_xs_asymmetry_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_490_xs_asymmetry_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_asymmetry_rank over 63d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(63).skew()

def csdr_491_xs_asymmetry_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_491_xs_asymmetry_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_asymmetry_rank over 63d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(63).kurt()

def csdr_492_xs_asymmetry_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_492_xs_asymmetry_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_asymmetry_rank over 126d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(126).skew()

def csdr_493_xs_asymmetry_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_493_xs_asymmetry_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_asymmetry_rank over 126d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(126).kurt()

def csdr_494_xs_asymmetry_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_494_xs_asymmetry_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_asymmetry_rank over 252d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(252).skew()

def csdr_495_xs_asymmetry_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_495_xs_asymmetry_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_asymmetry_rank over 252d. Rank of return skewness.
    """
    return (_rank_pct(close.pct_change(1).rolling(252).skew(), 252)).rolling(252).kurt()

def csdr_496_xs_persistence_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_496_xs_persistence_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_persistence_rank over 5d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).skew()

def csdr_497_xs_persistence_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_497_xs_persistence_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_persistence_rank over 5d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).kurt()

def csdr_498_xs_persistence_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_498_xs_persistence_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_persistence_rank over 21d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).skew()

def csdr_499_xs_persistence_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_499_xs_persistence_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_persistence_rank over 21d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).kurt()

def csdr_500_xs_persistence_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_500_xs_persistence_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_persistence_rank over 63d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).skew()

def csdr_501_xs_persistence_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_501_xs_persistence_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_persistence_rank over 63d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).kurt()

def csdr_502_xs_persistence_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_502_xs_persistence_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_persistence_rank over 126d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).skew()

def csdr_503_xs_persistence_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_503_xs_persistence_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_persistence_rank over 126d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).kurt()

def csdr_504_xs_persistence_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_504_xs_persistence_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_persistence_rank over 252d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).skew()

def csdr_505_xs_persistence_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_505_xs_persistence_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_persistence_rank over 252d. Rank of return autocorrelation.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).kurt()

def csdr_506_xs_gap_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_506_xs_gap_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_gap_rank over 5d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(5).skew()

def csdr_507_xs_gap_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_507_xs_gap_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_gap_rank over 5d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(5).kurt()

def csdr_508_xs_gap_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_508_xs_gap_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_gap_rank over 21d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(21).skew()

def csdr_509_xs_gap_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_509_xs_gap_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_gap_rank over 21d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(21).kurt()

def csdr_510_xs_gap_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_510_xs_gap_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_gap_rank over 63d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(63).skew()

def csdr_511_xs_gap_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_511_xs_gap_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_gap_rank over 63d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(63).kurt()

def csdr_512_xs_gap_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_512_xs_gap_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_gap_rank over 126d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(126).skew()

def csdr_513_xs_gap_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_513_xs_gap_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_gap_rank over 126d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(126).kurt()

def csdr_514_xs_gap_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_514_xs_gap_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_gap_rank over 252d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(252).skew()

def csdr_515_xs_gap_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_515_xs_gap_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_gap_rank over 252d. Rank of overnight gap magnitude.
    """
    return (_rank_pct(abs(open/close.shift(1)-1), 252)).rolling(252).kurt()

def csdr_516_xs_composite_rank_skew_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_516_xs_composite_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of xs_composite_rank over 5d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(5).skew()

def csdr_517_xs_composite_rank_kurt_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_517_xs_composite_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of xs_composite_rank over 5d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(5).kurt()

def csdr_518_xs_composite_rank_skew_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_518_xs_composite_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of xs_composite_rank over 21d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(21).skew()

def csdr_519_xs_composite_rank_kurt_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_519_xs_composite_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of xs_composite_rank over 21d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(21).kurt()

def csdr_520_xs_composite_rank_skew_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_520_xs_composite_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of xs_composite_rank over 63d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(63).skew()

def csdr_521_xs_composite_rank_kurt_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_521_xs_composite_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of xs_composite_rank over 63d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(63).kurt()

def csdr_522_xs_composite_rank_skew_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_522_xs_composite_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of xs_composite_rank over 126d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(126).skew()

def csdr_523_xs_composite_rank_kurt_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_523_xs_composite_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of xs_composite_rank over 126d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(126).kurt()

def csdr_524_xs_composite_rank_skew_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_524_xs_composite_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of xs_composite_rank over 252d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(252).skew()

def csdr_525_xs_composite_rank_kurt_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_525_xs_composite_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of xs_composite_rank over 252d. Average of momentum and drawdown ranks.
    """
    return ((_rank_pct(close.pct_change(63), 252) + _rank_pct(close/close.rolling(252).max(), 252)) / 2).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V124_REGISTRY_MOMENTS = {
    "csdr_376_price_rank_xs_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_376_price_rank_xs_skew_5d},
    "csdr_377_price_rank_xs_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_377_price_rank_xs_kurt_5d},
    "csdr_378_price_rank_xs_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_378_price_rank_xs_skew_21d},
    "csdr_379_price_rank_xs_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_379_price_rank_xs_kurt_21d},
    "csdr_380_price_rank_xs_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_380_price_rank_xs_skew_63d},
    "csdr_381_price_rank_xs_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_381_price_rank_xs_kurt_63d},
    "csdr_382_price_rank_xs_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_382_price_rank_xs_skew_126d},
    "csdr_383_price_rank_xs_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_383_price_rank_xs_kurt_126d},
    "csdr_384_price_rank_xs_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_384_price_rank_xs_skew_252d},
    "csdr_385_price_rank_xs_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_385_price_rank_xs_kurt_252d},
    "csdr_386_volume_rank_xs_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_386_volume_rank_xs_skew_5d},
    "csdr_387_volume_rank_xs_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_387_volume_rank_xs_kurt_5d},
    "csdr_388_volume_rank_xs_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_388_volume_rank_xs_skew_21d},
    "csdr_389_volume_rank_xs_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_389_volume_rank_xs_kurt_21d},
    "csdr_390_volume_rank_xs_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_390_volume_rank_xs_skew_63d},
    "csdr_391_volume_rank_xs_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_391_volume_rank_xs_kurt_63d},
    "csdr_392_volume_rank_xs_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_392_volume_rank_xs_skew_126d},
    "csdr_393_volume_rank_xs_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_393_volume_rank_xs_kurt_126d},
    "csdr_394_volume_rank_xs_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_394_volume_rank_xs_skew_252d},
    "csdr_395_volume_rank_xs_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_395_volume_rank_xs_kurt_252d},
    "csdr_396_relative_distress_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_396_relative_distress_rank_skew_5d},
    "csdr_397_relative_distress_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_397_relative_distress_rank_kurt_5d},
    "csdr_398_relative_distress_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_398_relative_distress_rank_skew_21d},
    "csdr_399_relative_distress_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_399_relative_distress_rank_kurt_21d},
    "csdr_400_relative_distress_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_400_relative_distress_rank_skew_63d},
    "csdr_401_relative_distress_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_401_relative_distress_rank_kurt_63d},
    "csdr_402_relative_distress_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_402_relative_distress_rank_skew_126d},
    "csdr_403_relative_distress_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_403_relative_distress_rank_kurt_126d},
    "csdr_404_relative_distress_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_404_relative_distress_rank_skew_252d},
    "csdr_405_relative_distress_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_405_relative_distress_rank_kurt_252d},
    "csdr_406_xs_volatility_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_406_xs_volatility_rank_skew_5d},
    "csdr_407_xs_volatility_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_407_xs_volatility_rank_kurt_5d},
    "csdr_408_xs_volatility_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_408_xs_volatility_rank_skew_21d},
    "csdr_409_xs_volatility_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_409_xs_volatility_rank_kurt_21d},
    "csdr_410_xs_volatility_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_410_xs_volatility_rank_skew_63d},
    "csdr_411_xs_volatility_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_411_xs_volatility_rank_kurt_63d},
    "csdr_412_xs_volatility_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_412_xs_volatility_rank_skew_126d},
    "csdr_413_xs_volatility_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_413_xs_volatility_rank_kurt_126d},
    "csdr_414_xs_volatility_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_414_xs_volatility_rank_skew_252d},
    "csdr_415_xs_volatility_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_415_xs_volatility_rank_kurt_252d},
    "csdr_416_xs_drawdown_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_416_xs_drawdown_rank_skew_5d},
    "csdr_417_xs_drawdown_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_417_xs_drawdown_rank_kurt_5d},
    "csdr_418_xs_drawdown_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_418_xs_drawdown_rank_skew_21d},
    "csdr_419_xs_drawdown_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_419_xs_drawdown_rank_kurt_21d},
    "csdr_420_xs_drawdown_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_420_xs_drawdown_rank_skew_63d},
    "csdr_421_xs_drawdown_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_421_xs_drawdown_rank_kurt_63d},
    "csdr_422_xs_drawdown_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_422_xs_drawdown_rank_skew_126d},
    "csdr_423_xs_drawdown_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_423_xs_drawdown_rank_kurt_126d},
    "csdr_424_xs_drawdown_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_424_xs_drawdown_rank_skew_252d},
    "csdr_425_xs_drawdown_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_425_xs_drawdown_rank_kurt_252d},
    "csdr_426_relative_volume_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_426_relative_volume_rank_skew_5d},
    "csdr_427_relative_volume_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_427_relative_volume_rank_kurt_5d},
    "csdr_428_relative_volume_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_428_relative_volume_rank_skew_21d},
    "csdr_429_relative_volume_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_429_relative_volume_rank_kurt_21d},
    "csdr_430_relative_volume_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_430_relative_volume_rank_skew_63d},
    "csdr_431_relative_volume_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_431_relative_volume_rank_kurt_63d},
    "csdr_432_relative_volume_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_432_relative_volume_rank_skew_126d},
    "csdr_433_relative_volume_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_433_relative_volume_rank_kurt_126d},
    "csdr_434_relative_volume_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_434_relative_volume_rank_skew_252d},
    "csdr_435_relative_volume_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_435_relative_volume_rank_kurt_252d},
    "csdr_436_xs_momentum_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_436_xs_momentum_rank_skew_5d},
    "csdr_437_xs_momentum_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_437_xs_momentum_rank_kurt_5d},
    "csdr_438_xs_momentum_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_438_xs_momentum_rank_skew_21d},
    "csdr_439_xs_momentum_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_439_xs_momentum_rank_kurt_21d},
    "csdr_440_xs_momentum_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_440_xs_momentum_rank_skew_63d},
    "csdr_441_xs_momentum_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_441_xs_momentum_rank_kurt_63d},
    "csdr_442_xs_momentum_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_442_xs_momentum_rank_skew_126d},
    "csdr_443_xs_momentum_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_443_xs_momentum_rank_kurt_126d},
    "csdr_444_xs_momentum_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_444_xs_momentum_rank_skew_252d},
    "csdr_445_xs_momentum_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_445_xs_momentum_rank_kurt_252d},
    "csdr_446_distress_rank_z_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_446_distress_rank_z_skew_5d},
    "csdr_447_distress_rank_z_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_447_distress_rank_z_kurt_5d},
    "csdr_448_distress_rank_z_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_448_distress_rank_z_skew_21d},
    "csdr_449_distress_rank_z_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_449_distress_rank_z_kurt_21d},
    "csdr_450_distress_rank_z_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_450_distress_rank_z_skew_63d},
    "csdr_451_distress_rank_z_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_451_distress_rank_z_kurt_63d},
    "csdr_452_distress_rank_z_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_452_distress_rank_z_skew_126d},
    "csdr_453_distress_rank_z_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_453_distress_rank_z_kurt_126d},
    "csdr_454_distress_rank_z_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_454_distress_rank_z_skew_252d},
    "csdr_455_distress_rank_z_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_455_distress_rank_z_kurt_252d},
    "csdr_456_xs_recovery_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_456_xs_recovery_rank_skew_5d},
    "csdr_457_xs_recovery_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_457_xs_recovery_rank_kurt_5d},
    "csdr_458_xs_recovery_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_458_xs_recovery_rank_skew_21d},
    "csdr_459_xs_recovery_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_459_xs_recovery_rank_kurt_21d},
    "csdr_460_xs_recovery_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_460_xs_recovery_rank_skew_63d},
    "csdr_461_xs_recovery_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_461_xs_recovery_rank_kurt_63d},
    "csdr_462_xs_recovery_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_462_xs_recovery_rank_skew_126d},
    "csdr_463_xs_recovery_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_463_xs_recovery_rank_kurt_126d},
    "csdr_464_xs_recovery_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_464_xs_recovery_rank_skew_252d},
    "csdr_465_xs_recovery_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_465_xs_recovery_rank_kurt_252d},
    "csdr_466_xs_liquidity_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_466_xs_liquidity_rank_skew_5d},
    "csdr_467_xs_liquidity_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_467_xs_liquidity_rank_kurt_5d},
    "csdr_468_xs_liquidity_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_468_xs_liquidity_rank_skew_21d},
    "csdr_469_xs_liquidity_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_469_xs_liquidity_rank_kurt_21d},
    "csdr_470_xs_liquidity_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_470_xs_liquidity_rank_skew_63d},
    "csdr_471_xs_liquidity_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_471_xs_liquidity_rank_kurt_63d},
    "csdr_472_xs_liquidity_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_472_xs_liquidity_rank_skew_126d},
    "csdr_473_xs_liquidity_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_473_xs_liquidity_rank_kurt_126d},
    "csdr_474_xs_liquidity_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_474_xs_liquidity_rank_skew_252d},
    "csdr_475_xs_liquidity_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_475_xs_liquidity_rank_kurt_252d},
    "csdr_476_xs_tail_risk_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_476_xs_tail_risk_rank_skew_5d},
    "csdr_477_xs_tail_risk_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_477_xs_tail_risk_rank_kurt_5d},
    "csdr_478_xs_tail_risk_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_478_xs_tail_risk_rank_skew_21d},
    "csdr_479_xs_tail_risk_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_479_xs_tail_risk_rank_kurt_21d},
    "csdr_480_xs_tail_risk_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_480_xs_tail_risk_rank_skew_63d},
    "csdr_481_xs_tail_risk_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_481_xs_tail_risk_rank_kurt_63d},
    "csdr_482_xs_tail_risk_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_482_xs_tail_risk_rank_skew_126d},
    "csdr_483_xs_tail_risk_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_483_xs_tail_risk_rank_kurt_126d},
    "csdr_484_xs_tail_risk_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_484_xs_tail_risk_rank_skew_252d},
    "csdr_485_xs_tail_risk_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_485_xs_tail_risk_rank_kurt_252d},
    "csdr_486_xs_asymmetry_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_486_xs_asymmetry_rank_skew_5d},
    "csdr_487_xs_asymmetry_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_487_xs_asymmetry_rank_kurt_5d},
    "csdr_488_xs_asymmetry_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_488_xs_asymmetry_rank_skew_21d},
    "csdr_489_xs_asymmetry_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_489_xs_asymmetry_rank_kurt_21d},
    "csdr_490_xs_asymmetry_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_490_xs_asymmetry_rank_skew_63d},
    "csdr_491_xs_asymmetry_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_491_xs_asymmetry_rank_kurt_63d},
    "csdr_492_xs_asymmetry_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_492_xs_asymmetry_rank_skew_126d},
    "csdr_493_xs_asymmetry_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_493_xs_asymmetry_rank_kurt_126d},
    "csdr_494_xs_asymmetry_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_494_xs_asymmetry_rank_skew_252d},
    "csdr_495_xs_asymmetry_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_495_xs_asymmetry_rank_kurt_252d},
    "csdr_496_xs_persistence_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_496_xs_persistence_rank_skew_5d},
    "csdr_497_xs_persistence_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_497_xs_persistence_rank_kurt_5d},
    "csdr_498_xs_persistence_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_498_xs_persistence_rank_skew_21d},
    "csdr_499_xs_persistence_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_499_xs_persistence_rank_kurt_21d},
    "csdr_500_xs_persistence_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_500_xs_persistence_rank_skew_63d},
    "csdr_501_xs_persistence_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_501_xs_persistence_rank_kurt_63d},
    "csdr_502_xs_persistence_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_502_xs_persistence_rank_skew_126d},
    "csdr_503_xs_persistence_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_503_xs_persistence_rank_kurt_126d},
    "csdr_504_xs_persistence_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_504_xs_persistence_rank_skew_252d},
    "csdr_505_xs_persistence_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_505_xs_persistence_rank_kurt_252d},
    "csdr_506_xs_gap_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_506_xs_gap_rank_skew_5d},
    "csdr_507_xs_gap_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_507_xs_gap_rank_kurt_5d},
    "csdr_508_xs_gap_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_508_xs_gap_rank_skew_21d},
    "csdr_509_xs_gap_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_509_xs_gap_rank_kurt_21d},
    "csdr_510_xs_gap_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_510_xs_gap_rank_skew_63d},
    "csdr_511_xs_gap_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_511_xs_gap_rank_kurt_63d},
    "csdr_512_xs_gap_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_512_xs_gap_rank_skew_126d},
    "csdr_513_xs_gap_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_513_xs_gap_rank_kurt_126d},
    "csdr_514_xs_gap_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_514_xs_gap_rank_skew_252d},
    "csdr_515_xs_gap_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_515_xs_gap_rank_kurt_252d},
    "csdr_516_xs_composite_rank_skew_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_516_xs_composite_rank_skew_5d},
    "csdr_517_xs_composite_rank_kurt_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_517_xs_composite_rank_kurt_5d},
    "csdr_518_xs_composite_rank_skew_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_518_xs_composite_rank_skew_21d},
    "csdr_519_xs_composite_rank_kurt_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_519_xs_composite_rank_kurt_21d},
    "csdr_520_xs_composite_rank_skew_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_520_xs_composite_rank_skew_63d},
    "csdr_521_xs_composite_rank_kurt_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_521_xs_composite_rank_kurt_63d},
    "csdr_522_xs_composite_rank_skew_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_522_xs_composite_rank_skew_126d},
    "csdr_523_xs_composite_rank_kurt_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_523_xs_composite_rank_kurt_126d},
    "csdr_524_xs_composite_rank_skew_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_524_xs_composite_rank_skew_252d},
    "csdr_525_xs_composite_rank_kurt_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_525_xs_composite_rank_kurt_252d},
}
