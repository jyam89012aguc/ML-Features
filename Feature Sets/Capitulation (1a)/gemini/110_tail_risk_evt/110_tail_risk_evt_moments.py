"""
110_tail_risk_evt — Statistical Moments
Domain: tail_risk_evt
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

def trev_376_var_95_proxy_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_376_var_95_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of var_95_proxy over 5d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(5).skew()

def trev_377_var_95_proxy_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_377_var_95_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of var_95_proxy over 5d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(5).kurt()

def trev_378_var_95_proxy_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_378_var_95_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of var_95_proxy over 21d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).skew()

def trev_379_var_95_proxy_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_379_var_95_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of var_95_proxy over 21d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).kurt()

def trev_380_var_95_proxy_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_380_var_95_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of var_95_proxy over 63d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).skew()

def trev_381_var_95_proxy_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_381_var_95_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of var_95_proxy over 63d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).kurt()

def trev_382_var_95_proxy_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_382_var_95_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of var_95_proxy over 126d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(126).skew()

def trev_383_var_95_proxy_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_383_var_95_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of var_95_proxy over 126d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(126).kurt()

def trev_384_var_95_proxy_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_384_var_95_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of var_95_proxy over 252d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(252).skew()

def trev_385_var_95_proxy_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_385_var_95_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of var_95_proxy over 252d. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).rolling(252).kurt()

def trev_386_expected_shortfall_proxy_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_386_expected_shortfall_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of expected_shortfall_proxy over 5d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(5).skew()

def trev_387_expected_shortfall_proxy_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_387_expected_shortfall_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of expected_shortfall_proxy over 5d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(5).kurt()

def trev_388_expected_shortfall_proxy_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_388_expected_shortfall_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of expected_shortfall_proxy over 21d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(21).skew()

def trev_389_expected_shortfall_proxy_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_389_expected_shortfall_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of expected_shortfall_proxy over 21d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(21).kurt()

def trev_390_expected_shortfall_proxy_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_390_expected_shortfall_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of expected_shortfall_proxy over 63d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(63).skew()

def trev_391_expected_shortfall_proxy_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_391_expected_shortfall_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of expected_shortfall_proxy over 63d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(63).kurt()

def trev_392_expected_shortfall_proxy_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_392_expected_shortfall_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of expected_shortfall_proxy over 126d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(126).skew()

def trev_393_expected_shortfall_proxy_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_393_expected_shortfall_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of expected_shortfall_proxy over 126d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(126).kurt()

def trev_394_expected_shortfall_proxy_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_394_expected_shortfall_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of expected_shortfall_proxy over 252d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(252).skew()

def trev_395_expected_shortfall_proxy_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_395_expected_shortfall_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of expected_shortfall_proxy over 252d. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).rolling(252).kurt()

def trev_396_tail_event_density_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_396_tail_event_density_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_event_density over 5d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(5).skew()

def trev_397_tail_event_density_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_397_tail_event_density_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density over 5d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(5).kurt()

def trev_398_tail_event_density_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_398_tail_event_density_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_event_density over 21d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(21).skew()

def trev_399_tail_event_density_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_399_tail_event_density_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density over 21d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(21).kurt()

def trev_400_tail_event_density_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_400_tail_event_density_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_event_density over 63d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(63).skew()

def trev_401_tail_event_density_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_401_tail_event_density_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density over 63d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(63).kurt()

def trev_402_tail_event_density_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_402_tail_event_density_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_event_density over 126d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(126).skew()

def trev_403_tail_event_density_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_403_tail_event_density_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density over 126d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(126).kurt()

def trev_404_tail_event_density_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_404_tail_event_density_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_event_density over 252d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(252).skew()

def trev_405_tail_event_density_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_405_tail_event_density_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density over 252d. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).rolling(252).kurt()

def trev_406_skewness_252d_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_406_skewness_252d_skew_5d
    ECONOMIC RATIONALE: Skewness of skewness_252d over 5d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(5).skew()

def trev_407_skewness_252d_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_407_skewness_252d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of skewness_252d over 5d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(5).kurt()

def trev_408_skewness_252d_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_408_skewness_252d_skew_21d
    ECONOMIC RATIONALE: Skewness of skewness_252d over 21d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(21).skew()

def trev_409_skewness_252d_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_409_skewness_252d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of skewness_252d over 21d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(21).kurt()

def trev_410_skewness_252d_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_410_skewness_252d_skew_63d
    ECONOMIC RATIONALE: Skewness of skewness_252d over 63d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(63).skew()

def trev_411_skewness_252d_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_411_skewness_252d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of skewness_252d over 63d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(63).kurt()

def trev_412_skewness_252d_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_412_skewness_252d_skew_126d
    ECONOMIC RATIONALE: Skewness of skewness_252d over 126d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(126).skew()

def trev_413_skewness_252d_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_413_skewness_252d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of skewness_252d over 126d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(126).kurt()

def trev_414_skewness_252d_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_414_skewness_252d_skew_252d
    ECONOMIC RATIONALE: Skewness of skewness_252d over 252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(252).skew()

def trev_415_skewness_252d_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_415_skewness_252d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of skewness_252d over 252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).rolling(252).kurt()

def trev_416_kurtosis_252d_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_416_kurtosis_252d_skew_5d
    ECONOMIC RATIONALE: Skewness of kurtosis_252d over 5d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(5).skew()

def trev_417_kurtosis_252d_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_417_kurtosis_252d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of kurtosis_252d over 5d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(5).kurt()

def trev_418_kurtosis_252d_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_418_kurtosis_252d_skew_21d
    ECONOMIC RATIONALE: Skewness of kurtosis_252d over 21d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(21).skew()

def trev_419_kurtosis_252d_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_419_kurtosis_252d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of kurtosis_252d over 21d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(21).kurt()

def trev_420_kurtosis_252d_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_420_kurtosis_252d_skew_63d
    ECONOMIC RATIONALE: Skewness of kurtosis_252d over 63d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(63).skew()

def trev_421_kurtosis_252d_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_421_kurtosis_252d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of kurtosis_252d over 63d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(63).kurt()

def trev_422_kurtosis_252d_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_422_kurtosis_252d_skew_126d
    ECONOMIC RATIONALE: Skewness of kurtosis_252d over 126d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(126).skew()

def trev_423_kurtosis_252d_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_423_kurtosis_252d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of kurtosis_252d over 126d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(126).kurt()

def trev_424_kurtosis_252d_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_424_kurtosis_252d_skew_252d
    ECONOMIC RATIONALE: Skewness of kurtosis_252d over 252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(252).skew()

def trev_425_kurtosis_252d_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_425_kurtosis_252d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of kurtosis_252d over 252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).rolling(252).kurt()

def trev_426_tail_ratio_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_426_tail_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_ratio over 5d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(5).skew()

def trev_427_tail_ratio_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_427_tail_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_ratio over 5d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(5).kurt()

def trev_428_tail_ratio_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_428_tail_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_ratio over 21d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(21).skew()

def trev_429_tail_ratio_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_429_tail_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_ratio over 21d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(21).kurt()

def trev_430_tail_ratio_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_430_tail_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_ratio over 63d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(63).skew()

def trev_431_tail_ratio_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_431_tail_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_ratio over 63d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(63).kurt()

def trev_432_tail_ratio_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_432_tail_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_ratio over 126d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(126).skew()

def trev_433_tail_ratio_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_433_tail_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_ratio over 126d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(126).kurt()

def trev_434_tail_ratio_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_434_tail_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_ratio over 252d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(252).skew()

def trev_435_tail_ratio_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_435_tail_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_ratio over 252d. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).rolling(252).kurt()

def trev_436_extreme_low_z_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_436_extreme_low_z_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_low_z over 5d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(5).skew()

def trev_437_extreme_low_z_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_437_extreme_low_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_low_z over 5d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(5).kurt()

def trev_438_extreme_low_z_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_438_extreme_low_z_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_low_z over 21d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(21).skew()

def trev_439_extreme_low_z_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_439_extreme_low_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_low_z over 21d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(21).kurt()

def trev_440_extreme_low_z_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_440_extreme_low_z_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_low_z over 63d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(63).skew()

def trev_441_extreme_low_z_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_441_extreme_low_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_low_z over 63d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(63).kurt()

def trev_442_extreme_low_z_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_442_extreme_low_z_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_low_z over 126d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(126).skew()

def trev_443_extreme_low_z_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_443_extreme_low_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_low_z over 126d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(126).kurt()

def trev_444_extreme_low_z_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_444_extreme_low_z_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_low_z over 252d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(252).skew()

def trev_445_extreme_low_z_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_445_extreme_low_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_low_z over 252d. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).rolling(252).kurt()

def trev_446_tail_risk_momentum_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_446_tail_risk_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_risk_momentum over 5d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(5).skew()

def trev_447_tail_risk_momentum_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_447_tail_risk_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_risk_momentum over 5d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(5).kurt()

def trev_448_tail_risk_momentum_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_448_tail_risk_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_risk_momentum over 21d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(21).skew()

def trev_449_tail_risk_momentum_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_449_tail_risk_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_risk_momentum over 21d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(21).kurt()

def trev_450_tail_risk_momentum_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_450_tail_risk_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_risk_momentum over 63d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(63).skew()

def trev_451_tail_risk_momentum_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_451_tail_risk_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_risk_momentum over 63d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(63).kurt()

def trev_452_tail_risk_momentum_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_452_tail_risk_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_risk_momentum over 126d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(126).skew()

def trev_453_tail_risk_momentum_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_453_tail_risk_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_risk_momentum over 126d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(126).kurt()

def trev_454_tail_risk_momentum_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_454_tail_risk_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_risk_momentum over 252d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(252).skew()

def trev_455_tail_risk_momentum_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_455_tail_risk_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_risk_momentum over 252d. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).rolling(252).kurt()

def trev_456_gap_down_risk_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_456_gap_down_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of gap_down_risk over 5d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(5).skew()

def trev_457_gap_down_risk_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_457_gap_down_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of gap_down_risk over 5d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(5).kurt()

def trev_458_gap_down_risk_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_458_gap_down_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of gap_down_risk over 21d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(21).skew()

def trev_459_gap_down_risk_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_459_gap_down_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of gap_down_risk over 21d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(21).kurt()

def trev_460_gap_down_risk_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_460_gap_down_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of gap_down_risk over 63d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(63).skew()

def trev_461_gap_down_risk_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_461_gap_down_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of gap_down_risk over 63d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(63).kurt()

def trev_462_gap_down_risk_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_462_gap_down_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of gap_down_risk over 126d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(126).skew()

def trev_463_gap_down_risk_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_463_gap_down_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of gap_down_risk over 126d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(126).kurt()

def trev_464_gap_down_risk_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_464_gap_down_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of gap_down_risk over 252d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(252).skew()

def trev_465_gap_down_risk_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_465_gap_down_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of gap_down_risk over 252d. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).rolling(252).kurt()

def trev_466_tail_persistence_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_466_tail_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_persistence over 5d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(5).skew()

def trev_467_tail_persistence_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_467_tail_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_persistence over 5d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(5).kurt()

def trev_468_tail_persistence_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_468_tail_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_persistence over 21d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(21).skew()

def trev_469_tail_persistence_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_469_tail_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_persistence over 21d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(21).kurt()

def trev_470_tail_persistence_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_470_tail_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_persistence over 63d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(63).skew()

def trev_471_tail_persistence_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_471_tail_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_persistence over 63d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(63).kurt()

def trev_472_tail_persistence_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_472_tail_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_persistence over 126d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(126).skew()

def trev_473_tail_persistence_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_473_tail_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_persistence over 126d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(126).kurt()

def trev_474_tail_persistence_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_474_tail_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_persistence over 252d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(252).skew()

def trev_475_tail_persistence_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_475_tail_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_persistence over 252d. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).rolling(252).kurt()

def trev_476_tail_volatility_spread_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_476_tail_volatility_spread_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_volatility_spread over 5d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(5).skew()

def trev_477_tail_volatility_spread_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_477_tail_volatility_spread_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_volatility_spread over 5d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(5).kurt()

def trev_478_tail_volatility_spread_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_478_tail_volatility_spread_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_volatility_spread over 21d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(21).skew()

def trev_479_tail_volatility_spread_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_479_tail_volatility_spread_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_volatility_spread over 21d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(21).kurt()

def trev_480_tail_volatility_spread_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_480_tail_volatility_spread_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_volatility_spread over 63d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(63).skew()

def trev_481_tail_volatility_spread_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_481_tail_volatility_spread_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_volatility_spread over 63d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(63).kurt()

def trev_482_tail_volatility_spread_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_482_tail_volatility_spread_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_volatility_spread over 126d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(126).skew()

def trev_483_tail_volatility_spread_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_483_tail_volatility_spread_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_volatility_spread over 126d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(126).kurt()

def trev_484_tail_volatility_spread_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_484_tail_volatility_spread_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_volatility_spread over 252d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(252).skew()

def trev_485_tail_volatility_spread_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_485_tail_volatility_spread_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_volatility_spread over 252d. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).rolling(252).kurt()

def trev_486_downside_deviation_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_486_downside_deviation_skew_5d
    ECONOMIC RATIONALE: Skewness of downside_deviation over 5d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(5).skew()

def trev_487_downside_deviation_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_487_downside_deviation_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of downside_deviation over 5d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(5).kurt()

def trev_488_downside_deviation_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_488_downside_deviation_skew_21d
    ECONOMIC RATIONALE: Skewness of downside_deviation over 21d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(21).skew()

def trev_489_downside_deviation_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_489_downside_deviation_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of downside_deviation over 21d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(21).kurt()

def trev_490_downside_deviation_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_490_downside_deviation_skew_63d
    ECONOMIC RATIONALE: Skewness of downside_deviation over 63d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(63).skew()

def trev_491_downside_deviation_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_491_downside_deviation_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of downside_deviation over 63d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(63).kurt()

def trev_492_downside_deviation_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_492_downside_deviation_skew_126d
    ECONOMIC RATIONALE: Skewness of downside_deviation over 126d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(126).skew()

def trev_493_downside_deviation_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_493_downside_deviation_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of downside_deviation over 126d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(126).kurt()

def trev_494_downside_deviation_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_494_downside_deviation_skew_252d
    ECONOMIC RATIONALE: Skewness of downside_deviation over 252d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(252).skew()

def trev_495_downside_deviation_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_495_downside_deviation_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of downside_deviation over 252d. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).rolling(252).kurt()

def trev_496_tail_event_cluster_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_496_tail_event_cluster_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_event_cluster over 5d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(5).skew()

def trev_497_tail_event_cluster_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_497_tail_event_cluster_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_event_cluster over 5d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(5).kurt()

def trev_498_tail_event_cluster_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_498_tail_event_cluster_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_event_cluster over 21d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(21).skew()

def trev_499_tail_event_cluster_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_499_tail_event_cluster_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_event_cluster over 21d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(21).kurt()

def trev_500_tail_event_cluster_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_500_tail_event_cluster_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_event_cluster over 63d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(63).skew()

def trev_501_tail_event_cluster_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_501_tail_event_cluster_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_event_cluster over 63d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(63).kurt()

def trev_502_tail_event_cluster_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_502_tail_event_cluster_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_event_cluster over 126d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(126).skew()

def trev_503_tail_event_cluster_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_503_tail_event_cluster_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_event_cluster over 126d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(126).kurt()

def trev_504_tail_event_cluster_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_504_tail_event_cluster_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_event_cluster over 252d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(252).skew()

def trev_505_tail_event_cluster_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_505_tail_event_cluster_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_event_cluster over 252d. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).rolling(252).kurt()

def trev_506_tail_drawdown_corr_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_506_tail_drawdown_corr_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_drawdown_corr over 5d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(5).skew()

def trev_507_tail_drawdown_corr_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_507_tail_drawdown_corr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_drawdown_corr over 5d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(5).kurt()

def trev_508_tail_drawdown_corr_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_508_tail_drawdown_corr_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_drawdown_corr over 21d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(21).skew()

def trev_509_tail_drawdown_corr_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_509_tail_drawdown_corr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_drawdown_corr over 21d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(21).kurt()

def trev_510_tail_drawdown_corr_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_510_tail_drawdown_corr_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_drawdown_corr over 63d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(63).skew()

def trev_511_tail_drawdown_corr_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_511_tail_drawdown_corr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_drawdown_corr over 63d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(63).kurt()

def trev_512_tail_drawdown_corr_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_512_tail_drawdown_corr_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_drawdown_corr over 126d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(126).skew()

def trev_513_tail_drawdown_corr_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_513_tail_drawdown_corr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_drawdown_corr over 126d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(126).kurt()

def trev_514_tail_drawdown_corr_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_514_tail_drawdown_corr_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_drawdown_corr over 252d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(252).skew()

def trev_515_tail_drawdown_corr_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_515_tail_drawdown_corr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_drawdown_corr over 252d. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).rolling(252).kurt()

def trev_516_black_swan_proxy_skew_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_516_black_swan_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of black_swan_proxy over 5d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(5).skew()

def trev_517_black_swan_proxy_kurt_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_517_black_swan_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of black_swan_proxy over 5d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(5).kurt()

def trev_518_black_swan_proxy_skew_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_518_black_swan_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of black_swan_proxy over 21d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(21).skew()

def trev_519_black_swan_proxy_kurt_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_519_black_swan_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of black_swan_proxy over 21d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(21).kurt()

def trev_520_black_swan_proxy_skew_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_520_black_swan_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of black_swan_proxy over 63d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(63).skew()

def trev_521_black_swan_proxy_kurt_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_521_black_swan_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of black_swan_proxy over 63d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(63).kurt()

def trev_522_black_swan_proxy_skew_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_522_black_swan_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of black_swan_proxy over 126d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(126).skew()

def trev_523_black_swan_proxy_kurt_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_523_black_swan_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of black_swan_proxy over 126d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(126).kurt()

def trev_524_black_swan_proxy_skew_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_524_black_swan_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of black_swan_proxy over 252d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(252).skew()

def trev_525_black_swan_proxy_kurt_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_525_black_swan_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of black_swan_proxy over 252d. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V110_REGISTRY_MOMENTS = {
    "trev_376_var_95_proxy_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_376_var_95_proxy_skew_5d},
    "trev_377_var_95_proxy_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_377_var_95_proxy_kurt_5d},
    "trev_378_var_95_proxy_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_378_var_95_proxy_skew_21d},
    "trev_379_var_95_proxy_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_379_var_95_proxy_kurt_21d},
    "trev_380_var_95_proxy_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_380_var_95_proxy_skew_63d},
    "trev_381_var_95_proxy_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_381_var_95_proxy_kurt_63d},
    "trev_382_var_95_proxy_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_382_var_95_proxy_skew_126d},
    "trev_383_var_95_proxy_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_383_var_95_proxy_kurt_126d},
    "trev_384_var_95_proxy_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_384_var_95_proxy_skew_252d},
    "trev_385_var_95_proxy_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_385_var_95_proxy_kurt_252d},
    "trev_386_expected_shortfall_proxy_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_386_expected_shortfall_proxy_skew_5d},
    "trev_387_expected_shortfall_proxy_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_387_expected_shortfall_proxy_kurt_5d},
    "trev_388_expected_shortfall_proxy_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_388_expected_shortfall_proxy_skew_21d},
    "trev_389_expected_shortfall_proxy_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_389_expected_shortfall_proxy_kurt_21d},
    "trev_390_expected_shortfall_proxy_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_390_expected_shortfall_proxy_skew_63d},
    "trev_391_expected_shortfall_proxy_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_391_expected_shortfall_proxy_kurt_63d},
    "trev_392_expected_shortfall_proxy_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_392_expected_shortfall_proxy_skew_126d},
    "trev_393_expected_shortfall_proxy_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_393_expected_shortfall_proxy_kurt_126d},
    "trev_394_expected_shortfall_proxy_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_394_expected_shortfall_proxy_skew_252d},
    "trev_395_expected_shortfall_proxy_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_395_expected_shortfall_proxy_kurt_252d},
    "trev_396_tail_event_density_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_396_tail_event_density_skew_5d},
    "trev_397_tail_event_density_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_397_tail_event_density_kurt_5d},
    "trev_398_tail_event_density_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_398_tail_event_density_skew_21d},
    "trev_399_tail_event_density_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_399_tail_event_density_kurt_21d},
    "trev_400_tail_event_density_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_400_tail_event_density_skew_63d},
    "trev_401_tail_event_density_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_401_tail_event_density_kurt_63d},
    "trev_402_tail_event_density_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_402_tail_event_density_skew_126d},
    "trev_403_tail_event_density_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_403_tail_event_density_kurt_126d},
    "trev_404_tail_event_density_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_404_tail_event_density_skew_252d},
    "trev_405_tail_event_density_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_405_tail_event_density_kurt_252d},
    "trev_406_skewness_252d_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_406_skewness_252d_skew_5d},
    "trev_407_skewness_252d_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_407_skewness_252d_kurt_5d},
    "trev_408_skewness_252d_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_408_skewness_252d_skew_21d},
    "trev_409_skewness_252d_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_409_skewness_252d_kurt_21d},
    "trev_410_skewness_252d_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_410_skewness_252d_skew_63d},
    "trev_411_skewness_252d_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_411_skewness_252d_kurt_63d},
    "trev_412_skewness_252d_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_412_skewness_252d_skew_126d},
    "trev_413_skewness_252d_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_413_skewness_252d_kurt_126d},
    "trev_414_skewness_252d_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_414_skewness_252d_skew_252d},
    "trev_415_skewness_252d_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_415_skewness_252d_kurt_252d},
    "trev_416_kurtosis_252d_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_416_kurtosis_252d_skew_5d},
    "trev_417_kurtosis_252d_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_417_kurtosis_252d_kurt_5d},
    "trev_418_kurtosis_252d_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_418_kurtosis_252d_skew_21d},
    "trev_419_kurtosis_252d_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_419_kurtosis_252d_kurt_21d},
    "trev_420_kurtosis_252d_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_420_kurtosis_252d_skew_63d},
    "trev_421_kurtosis_252d_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_421_kurtosis_252d_kurt_63d},
    "trev_422_kurtosis_252d_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_422_kurtosis_252d_skew_126d},
    "trev_423_kurtosis_252d_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_423_kurtosis_252d_kurt_126d},
    "trev_424_kurtosis_252d_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_424_kurtosis_252d_skew_252d},
    "trev_425_kurtosis_252d_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_425_kurtosis_252d_kurt_252d},
    "trev_426_tail_ratio_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_426_tail_ratio_skew_5d},
    "trev_427_tail_ratio_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_427_tail_ratio_kurt_5d},
    "trev_428_tail_ratio_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_428_tail_ratio_skew_21d},
    "trev_429_tail_ratio_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_429_tail_ratio_kurt_21d},
    "trev_430_tail_ratio_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_430_tail_ratio_skew_63d},
    "trev_431_tail_ratio_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_431_tail_ratio_kurt_63d},
    "trev_432_tail_ratio_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_432_tail_ratio_skew_126d},
    "trev_433_tail_ratio_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_433_tail_ratio_kurt_126d},
    "trev_434_tail_ratio_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_434_tail_ratio_skew_252d},
    "trev_435_tail_ratio_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_435_tail_ratio_kurt_252d},
    "trev_436_extreme_low_z_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_436_extreme_low_z_skew_5d},
    "trev_437_extreme_low_z_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_437_extreme_low_z_kurt_5d},
    "trev_438_extreme_low_z_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_438_extreme_low_z_skew_21d},
    "trev_439_extreme_low_z_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_439_extreme_low_z_kurt_21d},
    "trev_440_extreme_low_z_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_440_extreme_low_z_skew_63d},
    "trev_441_extreme_low_z_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_441_extreme_low_z_kurt_63d},
    "trev_442_extreme_low_z_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_442_extreme_low_z_skew_126d},
    "trev_443_extreme_low_z_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_443_extreme_low_z_kurt_126d},
    "trev_444_extreme_low_z_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_444_extreme_low_z_skew_252d},
    "trev_445_extreme_low_z_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_445_extreme_low_z_kurt_252d},
    "trev_446_tail_risk_momentum_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_446_tail_risk_momentum_skew_5d},
    "trev_447_tail_risk_momentum_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_447_tail_risk_momentum_kurt_5d},
    "trev_448_tail_risk_momentum_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_448_tail_risk_momentum_skew_21d},
    "trev_449_tail_risk_momentum_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_449_tail_risk_momentum_kurt_21d},
    "trev_450_tail_risk_momentum_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_450_tail_risk_momentum_skew_63d},
    "trev_451_tail_risk_momentum_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_451_tail_risk_momentum_kurt_63d},
    "trev_452_tail_risk_momentum_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_452_tail_risk_momentum_skew_126d},
    "trev_453_tail_risk_momentum_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_453_tail_risk_momentum_kurt_126d},
    "trev_454_tail_risk_momentum_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_454_tail_risk_momentum_skew_252d},
    "trev_455_tail_risk_momentum_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_455_tail_risk_momentum_kurt_252d},
    "trev_456_gap_down_risk_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_456_gap_down_risk_skew_5d},
    "trev_457_gap_down_risk_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_457_gap_down_risk_kurt_5d},
    "trev_458_gap_down_risk_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_458_gap_down_risk_skew_21d},
    "trev_459_gap_down_risk_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_459_gap_down_risk_kurt_21d},
    "trev_460_gap_down_risk_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_460_gap_down_risk_skew_63d},
    "trev_461_gap_down_risk_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_461_gap_down_risk_kurt_63d},
    "trev_462_gap_down_risk_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_462_gap_down_risk_skew_126d},
    "trev_463_gap_down_risk_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_463_gap_down_risk_kurt_126d},
    "trev_464_gap_down_risk_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_464_gap_down_risk_skew_252d},
    "trev_465_gap_down_risk_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_465_gap_down_risk_kurt_252d},
    "trev_466_tail_persistence_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_466_tail_persistence_skew_5d},
    "trev_467_tail_persistence_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_467_tail_persistence_kurt_5d},
    "trev_468_tail_persistence_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_468_tail_persistence_skew_21d},
    "trev_469_tail_persistence_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_469_tail_persistence_kurt_21d},
    "trev_470_tail_persistence_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_470_tail_persistence_skew_63d},
    "trev_471_tail_persistence_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_471_tail_persistence_kurt_63d},
    "trev_472_tail_persistence_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_472_tail_persistence_skew_126d},
    "trev_473_tail_persistence_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_473_tail_persistence_kurt_126d},
    "trev_474_tail_persistence_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_474_tail_persistence_skew_252d},
    "trev_475_tail_persistence_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_475_tail_persistence_kurt_252d},
    "trev_476_tail_volatility_spread_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_476_tail_volatility_spread_skew_5d},
    "trev_477_tail_volatility_spread_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_477_tail_volatility_spread_kurt_5d},
    "trev_478_tail_volatility_spread_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_478_tail_volatility_spread_skew_21d},
    "trev_479_tail_volatility_spread_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_479_tail_volatility_spread_kurt_21d},
    "trev_480_tail_volatility_spread_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_480_tail_volatility_spread_skew_63d},
    "trev_481_tail_volatility_spread_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_481_tail_volatility_spread_kurt_63d},
    "trev_482_tail_volatility_spread_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_482_tail_volatility_spread_skew_126d},
    "trev_483_tail_volatility_spread_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_483_tail_volatility_spread_kurt_126d},
    "trev_484_tail_volatility_spread_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_484_tail_volatility_spread_skew_252d},
    "trev_485_tail_volatility_spread_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_485_tail_volatility_spread_kurt_252d},
    "trev_486_downside_deviation_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_486_downside_deviation_skew_5d},
    "trev_487_downside_deviation_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_487_downside_deviation_kurt_5d},
    "trev_488_downside_deviation_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_488_downside_deviation_skew_21d},
    "trev_489_downside_deviation_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_489_downside_deviation_kurt_21d},
    "trev_490_downside_deviation_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_490_downside_deviation_skew_63d},
    "trev_491_downside_deviation_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_491_downside_deviation_kurt_63d},
    "trev_492_downside_deviation_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_492_downside_deviation_skew_126d},
    "trev_493_downside_deviation_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_493_downside_deviation_kurt_126d},
    "trev_494_downside_deviation_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_494_downside_deviation_skew_252d},
    "trev_495_downside_deviation_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_495_downside_deviation_kurt_252d},
    "trev_496_tail_event_cluster_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_496_tail_event_cluster_skew_5d},
    "trev_497_tail_event_cluster_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_497_tail_event_cluster_kurt_5d},
    "trev_498_tail_event_cluster_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_498_tail_event_cluster_skew_21d},
    "trev_499_tail_event_cluster_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_499_tail_event_cluster_kurt_21d},
    "trev_500_tail_event_cluster_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_500_tail_event_cluster_skew_63d},
    "trev_501_tail_event_cluster_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_501_tail_event_cluster_kurt_63d},
    "trev_502_tail_event_cluster_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_502_tail_event_cluster_skew_126d},
    "trev_503_tail_event_cluster_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_503_tail_event_cluster_kurt_126d},
    "trev_504_tail_event_cluster_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_504_tail_event_cluster_skew_252d},
    "trev_505_tail_event_cluster_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_505_tail_event_cluster_kurt_252d},
    "trev_506_tail_drawdown_corr_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_506_tail_drawdown_corr_skew_5d},
    "trev_507_tail_drawdown_corr_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_507_tail_drawdown_corr_kurt_5d},
    "trev_508_tail_drawdown_corr_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_508_tail_drawdown_corr_skew_21d},
    "trev_509_tail_drawdown_corr_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_509_tail_drawdown_corr_kurt_21d},
    "trev_510_tail_drawdown_corr_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_510_tail_drawdown_corr_skew_63d},
    "trev_511_tail_drawdown_corr_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_511_tail_drawdown_corr_kurt_63d},
    "trev_512_tail_drawdown_corr_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_512_tail_drawdown_corr_skew_126d},
    "trev_513_tail_drawdown_corr_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_513_tail_drawdown_corr_kurt_126d},
    "trev_514_tail_drawdown_corr_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_514_tail_drawdown_corr_skew_252d},
    "trev_515_tail_drawdown_corr_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_515_tail_drawdown_corr_kurt_252d},
    "trev_516_black_swan_proxy_skew_5d": {"inputs": ["close", "low", "open"], "func": trev_516_black_swan_proxy_skew_5d},
    "trev_517_black_swan_proxy_kurt_5d": {"inputs": ["close", "low", "open"], "func": trev_517_black_swan_proxy_kurt_5d},
    "trev_518_black_swan_proxy_skew_21d": {"inputs": ["close", "low", "open"], "func": trev_518_black_swan_proxy_skew_21d},
    "trev_519_black_swan_proxy_kurt_21d": {"inputs": ["close", "low", "open"], "func": trev_519_black_swan_proxy_kurt_21d},
    "trev_520_black_swan_proxy_skew_63d": {"inputs": ["close", "low", "open"], "func": trev_520_black_swan_proxy_skew_63d},
    "trev_521_black_swan_proxy_kurt_63d": {"inputs": ["close", "low", "open"], "func": trev_521_black_swan_proxy_kurt_63d},
    "trev_522_black_swan_proxy_skew_126d": {"inputs": ["close", "low", "open"], "func": trev_522_black_swan_proxy_skew_126d},
    "trev_523_black_swan_proxy_kurt_126d": {"inputs": ["close", "low", "open"], "func": trev_523_black_swan_proxy_kurt_126d},
    "trev_524_black_swan_proxy_skew_252d": {"inputs": ["close", "low", "open"], "func": trev_524_black_swan_proxy_skew_252d},
    "trev_525_black_swan_proxy_kurt_252d": {"inputs": ["close", "low", "open"], "func": trev_525_black_swan_proxy_kurt_252d},
}
