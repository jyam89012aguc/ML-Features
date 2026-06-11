"""
101_wyckoff_capitulation_structure — Statistical Moments
Domain: wyckoff_capitulation_structure
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

def wyck_376_selling_climax_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_376_selling_climax_skew_5d
    ECONOMIC RATIONALE: Skewness of selling_climax over 5d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(5).skew()

def wyck_377_selling_climax_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_377_selling_climax_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of selling_climax over 5d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(5).kurt()

def wyck_378_selling_climax_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_378_selling_climax_skew_21d
    ECONOMIC RATIONALE: Skewness of selling_climax over 21d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(21).skew()

def wyck_379_selling_climax_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_379_selling_climax_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of selling_climax over 21d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(21).kurt()

def wyck_380_selling_climax_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_380_selling_climax_skew_63d
    ECONOMIC RATIONALE: Skewness of selling_climax over 63d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(63).skew()

def wyck_381_selling_climax_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_381_selling_climax_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of selling_climax over 63d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(63).kurt()

def wyck_382_selling_climax_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_382_selling_climax_skew_126d
    ECONOMIC RATIONALE: Skewness of selling_climax over 126d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(126).skew()

def wyck_383_selling_climax_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_383_selling_climax_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of selling_climax over 126d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(126).kurt()

def wyck_384_selling_climax_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_384_selling_climax_skew_252d
    ECONOMIC RATIONALE: Skewness of selling_climax over 252d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(252).skew()

def wyck_385_selling_climax_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_385_selling_climax_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of selling_climax over 252d. High volume price collapse indicating a selling climax.
    """
    return ((volume > volume.rolling(63).mean()*2) * (close < low.shift(1))).rolling(252).kurt()

def wyck_386_automatic_rally_failure_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_386_automatic_rally_failure_skew_5d
    ECONOMIC RATIONALE: Skewness of automatic_rally_failure over 5d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(5).skew()

def wyck_387_automatic_rally_failure_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_387_automatic_rally_failure_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of automatic_rally_failure over 5d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(5).kurt()

def wyck_388_automatic_rally_failure_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_388_automatic_rally_failure_skew_21d
    ECONOMIC RATIONALE: Skewness of automatic_rally_failure over 21d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(21).skew()

def wyck_389_automatic_rally_failure_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_389_automatic_rally_failure_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of automatic_rally_failure over 21d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(21).kurt()

def wyck_390_automatic_rally_failure_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_390_automatic_rally_failure_skew_63d
    ECONOMIC RATIONALE: Skewness of automatic_rally_failure over 63d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(63).skew()

def wyck_391_automatic_rally_failure_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_391_automatic_rally_failure_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of automatic_rally_failure over 63d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(63).kurt()

def wyck_392_automatic_rally_failure_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_392_automatic_rally_failure_skew_126d
    ECONOMIC RATIONALE: Skewness of automatic_rally_failure over 126d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(126).skew()

def wyck_393_automatic_rally_failure_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_393_automatic_rally_failure_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of automatic_rally_failure over 126d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(126).kurt()

def wyck_394_automatic_rally_failure_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_394_automatic_rally_failure_skew_252d
    ECONOMIC RATIONALE: Skewness of automatic_rally_failure over 252d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(252).skew()

def wyck_395_automatic_rally_failure_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_395_automatic_rally_failure_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of automatic_rally_failure over 252d. Weakness of the initial bounce from lows.
    """
    return ((close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())).rolling(252).kurt()

def wyck_396_secondary_test_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_396_secondary_test_skew_5d
    ECONOMIC RATIONALE: Skewness of secondary_test over 5d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(5).skew()

def wyck_397_secondary_test_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_397_secondary_test_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of secondary_test over 5d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(5).kurt()

def wyck_398_secondary_test_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_398_secondary_test_skew_21d
    ECONOMIC RATIONALE: Skewness of secondary_test over 21d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(21).skew()

def wyck_399_secondary_test_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_399_secondary_test_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of secondary_test over 21d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(21).kurt()

def wyck_400_secondary_test_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_400_secondary_test_skew_63d
    ECONOMIC RATIONALE: Skewness of secondary_test over 63d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(63).skew()

def wyck_401_secondary_test_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_401_secondary_test_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of secondary_test over 63d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(63).kurt()

def wyck_402_secondary_test_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_402_secondary_test_skew_126d
    ECONOMIC RATIONALE: Skewness of secondary_test over 126d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(126).skew()

def wyck_403_secondary_test_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_403_secondary_test_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of secondary_test over 126d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(126).kurt()

def wyck_404_secondary_test_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_404_secondary_test_skew_252d
    ECONOMIC RATIONALE: Skewness of secondary_test over 252d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(252).skew()

def wyck_405_secondary_test_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_405_secondary_test_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of secondary_test over 252d. Testing of previous lows on lower volume.
    """
    return (low / low.rolling(21).min().shift(5)).rolling(252).kurt()

def wyck_406_spring_detection_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_406_spring_detection_skew_5d
    ECONOMIC RATIONALE: Skewness of spring_detection over 5d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(5).skew()

def wyck_407_spring_detection_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_407_spring_detection_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of spring_detection over 5d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(5).kurt()

def wyck_408_spring_detection_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_408_spring_detection_skew_21d
    ECONOMIC RATIONALE: Skewness of spring_detection over 21d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(21).skew()

def wyck_409_spring_detection_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_409_spring_detection_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of spring_detection over 21d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(21).kurt()

def wyck_410_spring_detection_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_410_spring_detection_skew_63d
    ECONOMIC RATIONALE: Skewness of spring_detection over 63d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(63).skew()

def wyck_411_spring_detection_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_411_spring_detection_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of spring_detection over 63d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(63).kurt()

def wyck_412_spring_detection_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_412_spring_detection_skew_126d
    ECONOMIC RATIONALE: Skewness of spring_detection over 126d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(126).skew()

def wyck_413_spring_detection_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_413_spring_detection_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of spring_detection over 126d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(126).kurt()

def wyck_414_spring_detection_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_414_spring_detection_skew_252d
    ECONOMIC RATIONALE: Skewness of spring_detection over 252d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(252).skew()

def wyck_415_spring_detection_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_415_spring_detection_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of spring_detection over 252d. False breakdown below support (spring).
    """
    return ((low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))).rolling(252).kurt()

def wyck_416_sign_of_weakness_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_416_sign_of_weakness_skew_5d
    ECONOMIC RATIONALE: Skewness of sign_of_weakness over 5d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(5).skew()

def wyck_417_sign_of_weakness_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_417_sign_of_weakness_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of sign_of_weakness over 5d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(5).kurt()

def wyck_418_sign_of_weakness_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_418_sign_of_weakness_skew_21d
    ECONOMIC RATIONALE: Skewness of sign_of_weakness over 21d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(21).skew()

def wyck_419_sign_of_weakness_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_419_sign_of_weakness_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of sign_of_weakness over 21d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(21).kurt()

def wyck_420_sign_of_weakness_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_420_sign_of_weakness_skew_63d
    ECONOMIC RATIONALE: Skewness of sign_of_weakness over 63d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(63).skew()

def wyck_421_sign_of_weakness_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_421_sign_of_weakness_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of sign_of_weakness over 63d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(63).kurt()

def wyck_422_sign_of_weakness_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_422_sign_of_weakness_skew_126d
    ECONOMIC RATIONALE: Skewness of sign_of_weakness over 126d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(126).skew()

def wyck_423_sign_of_weakness_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_423_sign_of_weakness_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of sign_of_weakness over 126d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(126).kurt()

def wyck_424_sign_of_weakness_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_424_sign_of_weakness_skew_252d
    ECONOMIC RATIONALE: Skewness of sign_of_weakness over 252d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(252).skew()

def wyck_425_sign_of_weakness_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_425_sign_of_weakness_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of sign_of_weakness over 252d. Sharp drop after a period of consolidation.
    """
    return (close.pct_change(5) < -0.1).rolling(252).kurt()

def wyck_426_supply_overcoming_demand_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_426_supply_overcoming_demand_skew_5d
    ECONOMIC RATIONALE: Skewness of supply_overcoming_demand over 5d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(5).skew()

def wyck_427_supply_overcoming_demand_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_427_supply_overcoming_demand_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of supply_overcoming_demand over 5d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(5).kurt()

def wyck_428_supply_overcoming_demand_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_428_supply_overcoming_demand_skew_21d
    ECONOMIC RATIONALE: Skewness of supply_overcoming_demand over 21d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(21).skew()

def wyck_429_supply_overcoming_demand_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_429_supply_overcoming_demand_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of supply_overcoming_demand over 21d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(21).kurt()

def wyck_430_supply_overcoming_demand_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_430_supply_overcoming_demand_skew_63d
    ECONOMIC RATIONALE: Skewness of supply_overcoming_demand over 63d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(63).skew()

def wyck_431_supply_overcoming_demand_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_431_supply_overcoming_demand_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of supply_overcoming_demand over 63d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(63).kurt()

def wyck_432_supply_overcoming_demand_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_432_supply_overcoming_demand_skew_126d
    ECONOMIC RATIONALE: Skewness of supply_overcoming_demand over 126d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(126).skew()

def wyck_433_supply_overcoming_demand_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_433_supply_overcoming_demand_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of supply_overcoming_demand over 126d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(126).kurt()

def wyck_434_supply_overcoming_demand_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_434_supply_overcoming_demand_skew_252d
    ECONOMIC RATIONALE: Skewness of supply_overcoming_demand over 252d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(252).skew()

def wyck_435_supply_overcoming_demand_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_435_supply_overcoming_demand_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of supply_overcoming_demand over 252d. Volume-weighted negative price action.
    """
    return (volume * (close - open) < 0).rolling(252).kurt()

def wyck_436_trading_range_position_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_436_trading_range_position_skew_5d
    ECONOMIC RATIONALE: Skewness of trading_range_position over 5d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(5).skew()

def wyck_437_trading_range_position_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_437_trading_range_position_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of trading_range_position over 5d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(5).kurt()

def wyck_438_trading_range_position_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_438_trading_range_position_skew_21d
    ECONOMIC RATIONALE: Skewness of trading_range_position over 21d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(21).skew()

def wyck_439_trading_range_position_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_439_trading_range_position_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of trading_range_position over 21d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(21).kurt()

def wyck_440_trading_range_position_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_440_trading_range_position_skew_63d
    ECONOMIC RATIONALE: Skewness of trading_range_position over 63d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(63).skew()

def wyck_441_trading_range_position_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_441_trading_range_position_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of trading_range_position over 63d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(63).kurt()

def wyck_442_trading_range_position_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_442_trading_range_position_skew_126d
    ECONOMIC RATIONALE: Skewness of trading_range_position over 126d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(126).skew()

def wyck_443_trading_range_position_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_443_trading_range_position_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of trading_range_position over 126d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(126).kurt()

def wyck_444_trading_range_position_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_444_trading_range_position_skew_252d
    ECONOMIC RATIONALE: Skewness of trading_range_position over 252d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(252).skew()

def wyck_445_trading_range_position_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_445_trading_range_position_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of trading_range_position over 252d. Position within the Wyckoff trading range.
    """
    return ((close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())).rolling(252).kurt()

def wyck_446_volume_dry_up_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_446_volume_dry_up_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_dry_up over 5d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(5).skew()

def wyck_447_volume_dry_up_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_447_volume_dry_up_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_dry_up over 5d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(5).kurt()

def wyck_448_volume_dry_up_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_448_volume_dry_up_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_dry_up over 21d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(21).skew()

def wyck_449_volume_dry_up_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_449_volume_dry_up_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_dry_up over 21d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(21).kurt()

def wyck_450_volume_dry_up_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_450_volume_dry_up_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_dry_up over 63d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(63).skew()

def wyck_451_volume_dry_up_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_451_volume_dry_up_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_dry_up over 63d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(63).kurt()

def wyck_452_volume_dry_up_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_452_volume_dry_up_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_dry_up over 126d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(126).skew()

def wyck_453_volume_dry_up_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_453_volume_dry_up_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_dry_up over 126d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(126).kurt()

def wyck_454_volume_dry_up_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_454_volume_dry_up_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_dry_up over 252d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(252).skew()

def wyck_455_volume_dry_up_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_455_volume_dry_up_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_dry_up over 252d. Reduction in volume suggesting supply exhaustion.
    """
    return (volume / volume.rolling(63).max()).rolling(252).kurt()

def wyck_456_upthrust_detection_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_456_upthrust_detection_skew_5d
    ECONOMIC RATIONALE: Skewness of upthrust_detection over 5d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(5).skew()

def wyck_457_upthrust_detection_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_457_upthrust_detection_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of upthrust_detection over 5d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(5).kurt()

def wyck_458_upthrust_detection_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_458_upthrust_detection_skew_21d
    ECONOMIC RATIONALE: Skewness of upthrust_detection over 21d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(21).skew()

def wyck_459_upthrust_detection_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_459_upthrust_detection_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of upthrust_detection over 21d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(21).kurt()

def wyck_460_upthrust_detection_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_460_upthrust_detection_skew_63d
    ECONOMIC RATIONALE: Skewness of upthrust_detection over 63d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(63).skew()

def wyck_461_upthrust_detection_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_461_upthrust_detection_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of upthrust_detection over 63d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(63).kurt()

def wyck_462_upthrust_detection_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_462_upthrust_detection_skew_126d
    ECONOMIC RATIONALE: Skewness of upthrust_detection over 126d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(126).skew()

def wyck_463_upthrust_detection_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_463_upthrust_detection_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of upthrust_detection over 126d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(126).kurt()

def wyck_464_upthrust_detection_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_464_upthrust_detection_skew_252d
    ECONOMIC RATIONALE: Skewness of upthrust_detection over 252d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(252).skew()

def wyck_465_upthrust_detection_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_465_upthrust_detection_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of upthrust_detection over 252d. False breakout above resistance.
    """
    return ((high > high.rolling(63).max().shift(1)) * (close < high.rolling(63).max().shift(1))).rolling(252).kurt()

def wyck_466_preliminary_support_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_466_preliminary_support_skew_5d
    ECONOMIC RATIONALE: Skewness of preliminary_support over 5d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(5).skew()

def wyck_467_preliminary_support_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_467_preliminary_support_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of preliminary_support over 5d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(5).kurt()

def wyck_468_preliminary_support_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_468_preliminary_support_skew_21d
    ECONOMIC RATIONALE: Skewness of preliminary_support over 21d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(21).skew()

def wyck_469_preliminary_support_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_469_preliminary_support_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of preliminary_support over 21d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(21).kurt()

def wyck_470_preliminary_support_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_470_preliminary_support_skew_63d
    ECONOMIC RATIONALE: Skewness of preliminary_support over 63d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(63).skew()

def wyck_471_preliminary_support_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_471_preliminary_support_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of preliminary_support over 63d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(63).kurt()

def wyck_472_preliminary_support_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_472_preliminary_support_skew_126d
    ECONOMIC RATIONALE: Skewness of preliminary_support over 126d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(126).skew()

def wyck_473_preliminary_support_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_473_preliminary_support_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of preliminary_support over 126d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(126).kurt()

def wyck_474_preliminary_support_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_474_preliminary_support_skew_252d
    ECONOMIC RATIONALE: Skewness of preliminary_support over 252d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(252).skew()

def wyck_475_preliminary_support_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_475_preliminary_support_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of preliminary_support over 252d. Identification of early support levels.
    """
    return (low.rolling(10).min() < low.rolling(63).min()).rolling(252).kurt()

def wyck_476_jump_across_creek_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_476_jump_across_creek_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_across_creek over 5d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(5).skew()

def wyck_477_jump_across_creek_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_477_jump_across_creek_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_across_creek over 5d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(5).kurt()

def wyck_478_jump_across_creek_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_478_jump_across_creek_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_across_creek over 21d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(21).skew()

def wyck_479_jump_across_creek_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_479_jump_across_creek_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_across_creek over 21d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(21).kurt()

def wyck_480_jump_across_creek_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_480_jump_across_creek_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_across_creek over 63d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(63).skew()

def wyck_481_jump_across_creek_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_481_jump_across_creek_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_across_creek over 63d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(63).kurt()

def wyck_482_jump_across_creek_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_482_jump_across_creek_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_across_creek over 126d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(126).skew()

def wyck_483_jump_across_creek_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_483_jump_across_creek_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_across_creek over 126d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(126).kurt()

def wyck_484_jump_across_creek_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_484_jump_across_creek_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_across_creek over 252d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(252).skew()

def wyck_485_jump_across_creek_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_485_jump_across_creek_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_across_creek over 252d. Strong breakout indicating change of trend.
    """
    return (close > high.rolling(63).max()).rolling(252).kurt()

def wyck_486_last_point_of_supply_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_486_last_point_of_supply_skew_5d
    ECONOMIC RATIONALE: Skewness of last_point_of_supply over 5d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(5).skew()

def wyck_487_last_point_of_supply_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_487_last_point_of_supply_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of last_point_of_supply over 5d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(5).kurt()

def wyck_488_last_point_of_supply_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_488_last_point_of_supply_skew_21d
    ECONOMIC RATIONALE: Skewness of last_point_of_supply over 21d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(21).skew()

def wyck_489_last_point_of_supply_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_489_last_point_of_supply_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of last_point_of_supply over 21d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(21).kurt()

def wyck_490_last_point_of_supply_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_490_last_point_of_supply_skew_63d
    ECONOMIC RATIONALE: Skewness of last_point_of_supply over 63d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(63).skew()

def wyck_491_last_point_of_supply_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_491_last_point_of_supply_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of last_point_of_supply over 63d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(63).kurt()

def wyck_492_last_point_of_supply_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_492_last_point_of_supply_skew_126d
    ECONOMIC RATIONALE: Skewness of last_point_of_supply over 126d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(126).skew()

def wyck_493_last_point_of_supply_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_493_last_point_of_supply_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of last_point_of_supply over 126d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(126).kurt()

def wyck_494_last_point_of_supply_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_494_last_point_of_supply_skew_252d
    ECONOMIC RATIONALE: Skewness of last_point_of_supply over 252d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(252).skew()

def wyck_495_last_point_of_supply_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_495_last_point_of_supply_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of last_point_of_supply over 252d. Lower highs during a distributive phase.
    """
    return (high < high.rolling(21).max()).rolling(252).kurt()

def wyck_496_volume_price_divergence_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_496_volume_price_divergence_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_price_divergence over 5d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(5).skew()

def wyck_497_volume_price_divergence_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_497_volume_price_divergence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_price_divergence over 5d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(5).kurt()

def wyck_498_volume_price_divergence_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_498_volume_price_divergence_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_price_divergence over 21d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(21).skew()

def wyck_499_volume_price_divergence_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_499_volume_price_divergence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_price_divergence over 21d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(21).kurt()

def wyck_500_volume_price_divergence_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_500_volume_price_divergence_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_price_divergence over 63d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(63).skew()

def wyck_501_volume_price_divergence_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_501_volume_price_divergence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_price_divergence over 63d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(63).kurt()

def wyck_502_volume_price_divergence_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_502_volume_price_divergence_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_price_divergence over 126d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(126).skew()

def wyck_503_volume_price_divergence_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_503_volume_price_divergence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_price_divergence over 126d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(126).kurt()

def wyck_504_volume_price_divergence_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_504_volume_price_divergence_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_price_divergence over 252d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(252).skew()

def wyck_505_volume_price_divergence_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_505_volume_price_divergence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_price_divergence over 252d. Efficiency of volume in moving price.
    """
    return (close.pct_change(21).abs() / volume.pct_change(21).abs()).rolling(252).kurt()

def wyck_506_effort_vs_result_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_506_effort_vs_result_skew_5d
    ECONOMIC RATIONALE: Skewness of effort_vs_result over 5d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(5).skew()

def wyck_507_effort_vs_result_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_507_effort_vs_result_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of effort_vs_result over 5d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(5).kurt()

def wyck_508_effort_vs_result_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_508_effort_vs_result_skew_21d
    ECONOMIC RATIONALE: Skewness of effort_vs_result over 21d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(21).skew()

def wyck_509_effort_vs_result_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_509_effort_vs_result_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of effort_vs_result over 21d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(21).kurt()

def wyck_510_effort_vs_result_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_510_effort_vs_result_skew_63d
    ECONOMIC RATIONALE: Skewness of effort_vs_result over 63d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(63).skew()

def wyck_511_effort_vs_result_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_511_effort_vs_result_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of effort_vs_result over 63d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(63).kurt()

def wyck_512_effort_vs_result_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_512_effort_vs_result_skew_126d
    ECONOMIC RATIONALE: Skewness of effort_vs_result over 126d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(126).skew()

def wyck_513_effort_vs_result_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_513_effort_vs_result_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of effort_vs_result over 126d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(126).kurt()

def wyck_514_effort_vs_result_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_514_effort_vs_result_skew_252d
    ECONOMIC RATIONALE: Skewness of effort_vs_result over 252d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(252).skew()

def wyck_515_effort_vs_result_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_515_effort_vs_result_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of effort_vs_result over 252d. Volume expended relative to the price range achieved.
    """
    return (volume / (high - low).replace(0, 1e-9)).rolling(252).kurt()

def wyck_516_trend_channel_violation_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_516_trend_channel_violation_skew_5d
    ECONOMIC RATIONALE: Skewness of trend_channel_violation over 5d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(5).skew()

def wyck_517_trend_channel_violation_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_517_trend_channel_violation_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of trend_channel_violation over 5d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(5).kurt()

def wyck_518_trend_channel_violation_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_518_trend_channel_violation_skew_21d
    ECONOMIC RATIONALE: Skewness of trend_channel_violation over 21d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(21).skew()

def wyck_519_trend_channel_violation_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_519_trend_channel_violation_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of trend_channel_violation over 21d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(21).kurt()

def wyck_520_trend_channel_violation_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_520_trend_channel_violation_skew_63d
    ECONOMIC RATIONALE: Skewness of trend_channel_violation over 63d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(63).skew()

def wyck_521_trend_channel_violation_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_521_trend_channel_violation_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of trend_channel_violation over 63d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(63).kurt()

def wyck_522_trend_channel_violation_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_522_trend_channel_violation_skew_126d
    ECONOMIC RATIONALE: Skewness of trend_channel_violation over 126d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(126).skew()

def wyck_523_trend_channel_violation_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_523_trend_channel_violation_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of trend_channel_violation over 126d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(126).kurt()

def wyck_524_trend_channel_violation_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_524_trend_channel_violation_skew_252d
    ECONOMIC RATIONALE: Skewness of trend_channel_violation over 252d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(252).skew()

def wyck_525_trend_channel_violation_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_525_trend_channel_violation_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of trend_channel_violation over 252d. Breakdown below trend channels.
    """
    return (low < low.rolling(63).mean() - 2*low.rolling(63).std()).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V101_REGISTRY_MOMENTS = {
    "wyck_376_selling_climax_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_376_selling_climax_skew_5d},
    "wyck_377_selling_climax_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_377_selling_climax_kurt_5d},
    "wyck_378_selling_climax_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_378_selling_climax_skew_21d},
    "wyck_379_selling_climax_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_379_selling_climax_kurt_21d},
    "wyck_380_selling_climax_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_380_selling_climax_skew_63d},
    "wyck_381_selling_climax_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_381_selling_climax_kurt_63d},
    "wyck_382_selling_climax_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_382_selling_climax_skew_126d},
    "wyck_383_selling_climax_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_383_selling_climax_kurt_126d},
    "wyck_384_selling_climax_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_384_selling_climax_skew_252d},
    "wyck_385_selling_climax_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_385_selling_climax_kurt_252d},
    "wyck_386_automatic_rally_failure_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_386_automatic_rally_failure_skew_5d},
    "wyck_387_automatic_rally_failure_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_387_automatic_rally_failure_kurt_5d},
    "wyck_388_automatic_rally_failure_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_388_automatic_rally_failure_skew_21d},
    "wyck_389_automatic_rally_failure_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_389_automatic_rally_failure_kurt_21d},
    "wyck_390_automatic_rally_failure_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_390_automatic_rally_failure_skew_63d},
    "wyck_391_automatic_rally_failure_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_391_automatic_rally_failure_kurt_63d},
    "wyck_392_automatic_rally_failure_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_392_automatic_rally_failure_skew_126d},
    "wyck_393_automatic_rally_failure_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_393_automatic_rally_failure_kurt_126d},
    "wyck_394_automatic_rally_failure_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_394_automatic_rally_failure_skew_252d},
    "wyck_395_automatic_rally_failure_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_395_automatic_rally_failure_kurt_252d},
    "wyck_396_secondary_test_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_396_secondary_test_skew_5d},
    "wyck_397_secondary_test_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_397_secondary_test_kurt_5d},
    "wyck_398_secondary_test_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_398_secondary_test_skew_21d},
    "wyck_399_secondary_test_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_399_secondary_test_kurt_21d},
    "wyck_400_secondary_test_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_400_secondary_test_skew_63d},
    "wyck_401_secondary_test_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_401_secondary_test_kurt_63d},
    "wyck_402_secondary_test_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_402_secondary_test_skew_126d},
    "wyck_403_secondary_test_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_403_secondary_test_kurt_126d},
    "wyck_404_secondary_test_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_404_secondary_test_skew_252d},
    "wyck_405_secondary_test_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_405_secondary_test_kurt_252d},
    "wyck_406_spring_detection_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_406_spring_detection_skew_5d},
    "wyck_407_spring_detection_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_407_spring_detection_kurt_5d},
    "wyck_408_spring_detection_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_408_spring_detection_skew_21d},
    "wyck_409_spring_detection_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_409_spring_detection_kurt_21d},
    "wyck_410_spring_detection_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_410_spring_detection_skew_63d},
    "wyck_411_spring_detection_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_411_spring_detection_kurt_63d},
    "wyck_412_spring_detection_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_412_spring_detection_skew_126d},
    "wyck_413_spring_detection_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_413_spring_detection_kurt_126d},
    "wyck_414_spring_detection_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_414_spring_detection_skew_252d},
    "wyck_415_spring_detection_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_415_spring_detection_kurt_252d},
    "wyck_416_sign_of_weakness_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_416_sign_of_weakness_skew_5d},
    "wyck_417_sign_of_weakness_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_417_sign_of_weakness_kurt_5d},
    "wyck_418_sign_of_weakness_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_418_sign_of_weakness_skew_21d},
    "wyck_419_sign_of_weakness_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_419_sign_of_weakness_kurt_21d},
    "wyck_420_sign_of_weakness_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_420_sign_of_weakness_skew_63d},
    "wyck_421_sign_of_weakness_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_421_sign_of_weakness_kurt_63d},
    "wyck_422_sign_of_weakness_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_422_sign_of_weakness_skew_126d},
    "wyck_423_sign_of_weakness_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_423_sign_of_weakness_kurt_126d},
    "wyck_424_sign_of_weakness_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_424_sign_of_weakness_skew_252d},
    "wyck_425_sign_of_weakness_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_425_sign_of_weakness_kurt_252d},
    "wyck_426_supply_overcoming_demand_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_426_supply_overcoming_demand_skew_5d},
    "wyck_427_supply_overcoming_demand_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_427_supply_overcoming_demand_kurt_5d},
    "wyck_428_supply_overcoming_demand_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_428_supply_overcoming_demand_skew_21d},
    "wyck_429_supply_overcoming_demand_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_429_supply_overcoming_demand_kurt_21d},
    "wyck_430_supply_overcoming_demand_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_430_supply_overcoming_demand_skew_63d},
    "wyck_431_supply_overcoming_demand_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_431_supply_overcoming_demand_kurt_63d},
    "wyck_432_supply_overcoming_demand_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_432_supply_overcoming_demand_skew_126d},
    "wyck_433_supply_overcoming_demand_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_433_supply_overcoming_demand_kurt_126d},
    "wyck_434_supply_overcoming_demand_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_434_supply_overcoming_demand_skew_252d},
    "wyck_435_supply_overcoming_demand_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_435_supply_overcoming_demand_kurt_252d},
    "wyck_436_trading_range_position_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_436_trading_range_position_skew_5d},
    "wyck_437_trading_range_position_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_437_trading_range_position_kurt_5d},
    "wyck_438_trading_range_position_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_438_trading_range_position_skew_21d},
    "wyck_439_trading_range_position_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_439_trading_range_position_kurt_21d},
    "wyck_440_trading_range_position_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_440_trading_range_position_skew_63d},
    "wyck_441_trading_range_position_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_441_trading_range_position_kurt_63d},
    "wyck_442_trading_range_position_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_442_trading_range_position_skew_126d},
    "wyck_443_trading_range_position_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_443_trading_range_position_kurt_126d},
    "wyck_444_trading_range_position_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_444_trading_range_position_skew_252d},
    "wyck_445_trading_range_position_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_445_trading_range_position_kurt_252d},
    "wyck_446_volume_dry_up_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_446_volume_dry_up_skew_5d},
    "wyck_447_volume_dry_up_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_447_volume_dry_up_kurt_5d},
    "wyck_448_volume_dry_up_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_448_volume_dry_up_skew_21d},
    "wyck_449_volume_dry_up_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_449_volume_dry_up_kurt_21d},
    "wyck_450_volume_dry_up_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_450_volume_dry_up_skew_63d},
    "wyck_451_volume_dry_up_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_451_volume_dry_up_kurt_63d},
    "wyck_452_volume_dry_up_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_452_volume_dry_up_skew_126d},
    "wyck_453_volume_dry_up_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_453_volume_dry_up_kurt_126d},
    "wyck_454_volume_dry_up_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_454_volume_dry_up_skew_252d},
    "wyck_455_volume_dry_up_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_455_volume_dry_up_kurt_252d},
    "wyck_456_upthrust_detection_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_456_upthrust_detection_skew_5d},
    "wyck_457_upthrust_detection_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_457_upthrust_detection_kurt_5d},
    "wyck_458_upthrust_detection_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_458_upthrust_detection_skew_21d},
    "wyck_459_upthrust_detection_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_459_upthrust_detection_kurt_21d},
    "wyck_460_upthrust_detection_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_460_upthrust_detection_skew_63d},
    "wyck_461_upthrust_detection_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_461_upthrust_detection_kurt_63d},
    "wyck_462_upthrust_detection_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_462_upthrust_detection_skew_126d},
    "wyck_463_upthrust_detection_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_463_upthrust_detection_kurt_126d},
    "wyck_464_upthrust_detection_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_464_upthrust_detection_skew_252d},
    "wyck_465_upthrust_detection_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_465_upthrust_detection_kurt_252d},
    "wyck_466_preliminary_support_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_466_preliminary_support_skew_5d},
    "wyck_467_preliminary_support_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_467_preliminary_support_kurt_5d},
    "wyck_468_preliminary_support_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_468_preliminary_support_skew_21d},
    "wyck_469_preliminary_support_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_469_preliminary_support_kurt_21d},
    "wyck_470_preliminary_support_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_470_preliminary_support_skew_63d},
    "wyck_471_preliminary_support_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_471_preliminary_support_kurt_63d},
    "wyck_472_preliminary_support_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_472_preliminary_support_skew_126d},
    "wyck_473_preliminary_support_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_473_preliminary_support_kurt_126d},
    "wyck_474_preliminary_support_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_474_preliminary_support_skew_252d},
    "wyck_475_preliminary_support_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_475_preliminary_support_kurt_252d},
    "wyck_476_jump_across_creek_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_476_jump_across_creek_skew_5d},
    "wyck_477_jump_across_creek_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_477_jump_across_creek_kurt_5d},
    "wyck_478_jump_across_creek_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_478_jump_across_creek_skew_21d},
    "wyck_479_jump_across_creek_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_479_jump_across_creek_kurt_21d},
    "wyck_480_jump_across_creek_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_480_jump_across_creek_skew_63d},
    "wyck_481_jump_across_creek_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_481_jump_across_creek_kurt_63d},
    "wyck_482_jump_across_creek_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_482_jump_across_creek_skew_126d},
    "wyck_483_jump_across_creek_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_483_jump_across_creek_kurt_126d},
    "wyck_484_jump_across_creek_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_484_jump_across_creek_skew_252d},
    "wyck_485_jump_across_creek_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_485_jump_across_creek_kurt_252d},
    "wyck_486_last_point_of_supply_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_486_last_point_of_supply_skew_5d},
    "wyck_487_last_point_of_supply_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_487_last_point_of_supply_kurt_5d},
    "wyck_488_last_point_of_supply_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_488_last_point_of_supply_skew_21d},
    "wyck_489_last_point_of_supply_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_489_last_point_of_supply_kurt_21d},
    "wyck_490_last_point_of_supply_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_490_last_point_of_supply_skew_63d},
    "wyck_491_last_point_of_supply_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_491_last_point_of_supply_kurt_63d},
    "wyck_492_last_point_of_supply_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_492_last_point_of_supply_skew_126d},
    "wyck_493_last_point_of_supply_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_493_last_point_of_supply_kurt_126d},
    "wyck_494_last_point_of_supply_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_494_last_point_of_supply_skew_252d},
    "wyck_495_last_point_of_supply_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_495_last_point_of_supply_kurt_252d},
    "wyck_496_volume_price_divergence_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_496_volume_price_divergence_skew_5d},
    "wyck_497_volume_price_divergence_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_497_volume_price_divergence_kurt_5d},
    "wyck_498_volume_price_divergence_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_498_volume_price_divergence_skew_21d},
    "wyck_499_volume_price_divergence_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_499_volume_price_divergence_kurt_21d},
    "wyck_500_volume_price_divergence_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_500_volume_price_divergence_skew_63d},
    "wyck_501_volume_price_divergence_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_501_volume_price_divergence_kurt_63d},
    "wyck_502_volume_price_divergence_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_502_volume_price_divergence_skew_126d},
    "wyck_503_volume_price_divergence_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_503_volume_price_divergence_kurt_126d},
    "wyck_504_volume_price_divergence_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_504_volume_price_divergence_skew_252d},
    "wyck_505_volume_price_divergence_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_505_volume_price_divergence_kurt_252d},
    "wyck_506_effort_vs_result_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_506_effort_vs_result_skew_5d},
    "wyck_507_effort_vs_result_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_507_effort_vs_result_kurt_5d},
    "wyck_508_effort_vs_result_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_508_effort_vs_result_skew_21d},
    "wyck_509_effort_vs_result_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_509_effort_vs_result_kurt_21d},
    "wyck_510_effort_vs_result_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_510_effort_vs_result_skew_63d},
    "wyck_511_effort_vs_result_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_511_effort_vs_result_kurt_63d},
    "wyck_512_effort_vs_result_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_512_effort_vs_result_skew_126d},
    "wyck_513_effort_vs_result_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_513_effort_vs_result_kurt_126d},
    "wyck_514_effort_vs_result_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_514_effort_vs_result_skew_252d},
    "wyck_515_effort_vs_result_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_515_effort_vs_result_kurt_252d},
    "wyck_516_trend_channel_violation_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_516_trend_channel_violation_skew_5d},
    "wyck_517_trend_channel_violation_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_517_trend_channel_violation_kurt_5d},
    "wyck_518_trend_channel_violation_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_518_trend_channel_violation_skew_21d},
    "wyck_519_trend_channel_violation_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_519_trend_channel_violation_kurt_21d},
    "wyck_520_trend_channel_violation_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_520_trend_channel_violation_skew_63d},
    "wyck_521_trend_channel_violation_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_521_trend_channel_violation_kurt_63d},
    "wyck_522_trend_channel_violation_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_522_trend_channel_violation_skew_126d},
    "wyck_523_trend_channel_violation_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_523_trend_channel_violation_kurt_126d},
    "wyck_524_trend_channel_violation_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_524_trend_channel_violation_skew_252d},
    "wyck_525_trend_channel_violation_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_525_trend_channel_violation_kurt_252d},
}
