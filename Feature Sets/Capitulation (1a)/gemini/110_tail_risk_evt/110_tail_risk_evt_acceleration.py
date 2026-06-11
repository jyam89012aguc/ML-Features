"""
110_tail_risk_evt — Acceleration (3rd Derivatives)
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

def trev_301_var_95_proxy_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_301_var_95_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(5).diff(_TD_MON)

def trev_302_var_95_proxy_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_302_var_95_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(21).diff(_TD_MON)

def trev_303_var_95_proxy_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_303_var_95_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(63).diff(_TD_MON)

def trev_304_var_95_proxy_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_304_var_95_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(126).diff(_TD_MON)

def trev_305_var_95_proxy_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_305_var_95_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(252).diff(_TD_MON)

def trev_306_expected_shortfall_proxy_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_306_expected_shortfall_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(5).diff(_TD_MON)

def trev_307_expected_shortfall_proxy_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_307_expected_shortfall_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(21).diff(_TD_MON)

def trev_308_expected_shortfall_proxy_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_308_expected_shortfall_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(63).diff(_TD_MON)

def trev_309_expected_shortfall_proxy_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_309_expected_shortfall_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(126).diff(_TD_MON)

def trev_310_expected_shortfall_proxy_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_310_expected_shortfall_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(252).diff(_TD_MON)

def trev_311_tail_event_density_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_311_tail_event_density_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(5).diff(_TD_MON)

def trev_312_tail_event_density_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_312_tail_event_density_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(21).diff(_TD_MON)

def trev_313_tail_event_density_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_313_tail_event_density_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(63).diff(_TD_MON)

def trev_314_tail_event_density_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_314_tail_event_density_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(126).diff(_TD_MON)

def trev_315_tail_event_density_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_315_tail_event_density_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(252).diff(_TD_MON)

def trev_316_skewness_252d_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_316_skewness_252d_accel_5d
    ECONOMIC RATIONALE: Acceleration of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(5).diff(_TD_MON)

def trev_317_skewness_252d_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_317_skewness_252d_accel_21d
    ECONOMIC RATIONALE: Acceleration of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(21).diff(_TD_MON)

def trev_318_skewness_252d_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_318_skewness_252d_accel_63d
    ECONOMIC RATIONALE: Acceleration of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(63).diff(_TD_MON)

def trev_319_skewness_252d_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_319_skewness_252d_accel_126d
    ECONOMIC RATIONALE: Acceleration of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(126).diff(_TD_MON)

def trev_320_skewness_252d_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_320_skewness_252d_accel_252d
    ECONOMIC RATIONALE: Acceleration of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(252).diff(_TD_MON)

def trev_321_kurtosis_252d_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_321_kurtosis_252d_accel_5d
    ECONOMIC RATIONALE: Acceleration of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(5).diff(_TD_MON)

def trev_322_kurtosis_252d_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_322_kurtosis_252d_accel_21d
    ECONOMIC RATIONALE: Acceleration of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(21).diff(_TD_MON)

def trev_323_kurtosis_252d_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_323_kurtosis_252d_accel_63d
    ECONOMIC RATIONALE: Acceleration of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(63).diff(_TD_MON)

def trev_324_kurtosis_252d_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_324_kurtosis_252d_accel_126d
    ECONOMIC RATIONALE: Acceleration of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(126).diff(_TD_MON)

def trev_325_kurtosis_252d_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_325_kurtosis_252d_accel_252d
    ECONOMIC RATIONALE: Acceleration of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(252).diff(_TD_MON)

def trev_326_tail_ratio_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_326_tail_ratio_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(5).diff(_TD_MON)

def trev_327_tail_ratio_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_327_tail_ratio_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(21).diff(_TD_MON)

def trev_328_tail_ratio_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_328_tail_ratio_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(63).diff(_TD_MON)

def trev_329_tail_ratio_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_329_tail_ratio_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(126).diff(_TD_MON)

def trev_330_tail_ratio_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_330_tail_ratio_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(252).diff(_TD_MON)

def trev_331_extreme_low_z_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_331_extreme_low_z_accel_5d
    ECONOMIC RATIONALE: Acceleration of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(5).diff(_TD_MON)

def trev_332_extreme_low_z_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_332_extreme_low_z_accel_21d
    ECONOMIC RATIONALE: Acceleration of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(21).diff(_TD_MON)

def trev_333_extreme_low_z_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_333_extreme_low_z_accel_63d
    ECONOMIC RATIONALE: Acceleration of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(63).diff(_TD_MON)

def trev_334_extreme_low_z_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_334_extreme_low_z_accel_126d
    ECONOMIC RATIONALE: Acceleration of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(126).diff(_TD_MON)

def trev_335_extreme_low_z_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_335_extreme_low_z_accel_252d
    ECONOMIC RATIONALE: Acceleration of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(252).diff(_TD_MON)

def trev_336_tail_risk_momentum_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_336_tail_risk_momentum_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(5).diff(_TD_MON)

def trev_337_tail_risk_momentum_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_337_tail_risk_momentum_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(21).diff(_TD_MON)

def trev_338_tail_risk_momentum_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_338_tail_risk_momentum_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(63).diff(_TD_MON)

def trev_339_tail_risk_momentum_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_339_tail_risk_momentum_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(126).diff(_TD_MON)

def trev_340_tail_risk_momentum_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_340_tail_risk_momentum_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(252).diff(_TD_MON)

def trev_341_gap_down_risk_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_341_gap_down_risk_accel_5d
    ECONOMIC RATIONALE: Acceleration of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(5).diff(_TD_MON)

def trev_342_gap_down_risk_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_342_gap_down_risk_accel_21d
    ECONOMIC RATIONALE: Acceleration of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(21).diff(_TD_MON)

def trev_343_gap_down_risk_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_343_gap_down_risk_accel_63d
    ECONOMIC RATIONALE: Acceleration of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(63).diff(_TD_MON)

def trev_344_gap_down_risk_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_344_gap_down_risk_accel_126d
    ECONOMIC RATIONALE: Acceleration of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(126).diff(_TD_MON)

def trev_345_gap_down_risk_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_345_gap_down_risk_accel_252d
    ECONOMIC RATIONALE: Acceleration of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(252).diff(_TD_MON)

def trev_346_tail_persistence_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_346_tail_persistence_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(5).diff(_TD_MON)

def trev_347_tail_persistence_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_347_tail_persistence_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(21).diff(_TD_MON)

def trev_348_tail_persistence_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_348_tail_persistence_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(63).diff(_TD_MON)

def trev_349_tail_persistence_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_349_tail_persistence_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(126).diff(_TD_MON)

def trev_350_tail_persistence_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_350_tail_persistence_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(252).diff(_TD_MON)

def trev_351_tail_volatility_spread_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_351_tail_volatility_spread_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(5).diff(_TD_MON)

def trev_352_tail_volatility_spread_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_352_tail_volatility_spread_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(21).diff(_TD_MON)

def trev_353_tail_volatility_spread_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_353_tail_volatility_spread_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(63).diff(_TD_MON)

def trev_354_tail_volatility_spread_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_354_tail_volatility_spread_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(126).diff(_TD_MON)

def trev_355_tail_volatility_spread_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_355_tail_volatility_spread_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(252).diff(_TD_MON)

def trev_356_downside_deviation_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_356_downside_deviation_accel_5d
    ECONOMIC RATIONALE: Acceleration of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(5).diff(_TD_MON)

def trev_357_downside_deviation_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_357_downside_deviation_accel_21d
    ECONOMIC RATIONALE: Acceleration of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(21).diff(_TD_MON)

def trev_358_downside_deviation_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_358_downside_deviation_accel_63d
    ECONOMIC RATIONALE: Acceleration of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(63).diff(_TD_MON)

def trev_359_downside_deviation_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_359_downside_deviation_accel_126d
    ECONOMIC RATIONALE: Acceleration of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(126).diff(_TD_MON)

def trev_360_downside_deviation_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_360_downside_deviation_accel_252d
    ECONOMIC RATIONALE: Acceleration of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(252).diff(_TD_MON)

def trev_361_tail_event_cluster_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_361_tail_event_cluster_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(5).diff(_TD_MON)

def trev_362_tail_event_cluster_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_362_tail_event_cluster_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(21).diff(_TD_MON)

def trev_363_tail_event_cluster_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_363_tail_event_cluster_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(63).diff(_TD_MON)

def trev_364_tail_event_cluster_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_364_tail_event_cluster_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(126).diff(_TD_MON)

def trev_365_tail_event_cluster_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_365_tail_event_cluster_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(252).diff(_TD_MON)

def trev_366_tail_drawdown_corr_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_366_tail_drawdown_corr_accel_5d
    ECONOMIC RATIONALE: Acceleration of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(5).diff(_TD_MON)

def trev_367_tail_drawdown_corr_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_367_tail_drawdown_corr_accel_21d
    ECONOMIC RATIONALE: Acceleration of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(21).diff(_TD_MON)

def trev_368_tail_drawdown_corr_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_368_tail_drawdown_corr_accel_63d
    ECONOMIC RATIONALE: Acceleration of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(63).diff(_TD_MON)

def trev_369_tail_drawdown_corr_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_369_tail_drawdown_corr_accel_126d
    ECONOMIC RATIONALE: Acceleration of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(126).diff(_TD_MON)

def trev_370_tail_drawdown_corr_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_370_tail_drawdown_corr_accel_252d
    ECONOMIC RATIONALE: Acceleration of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(252).diff(_TD_MON)

def trev_371_black_swan_proxy_accel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_371_black_swan_proxy_accel_5d
    ECONOMIC RATIONALE: Acceleration of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(5).diff(_TD_MON)

def trev_372_black_swan_proxy_accel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_372_black_swan_proxy_accel_21d
    ECONOMIC RATIONALE: Acceleration of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(21).diff(_TD_MON)

def trev_373_black_swan_proxy_accel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_373_black_swan_proxy_accel_63d
    ECONOMIC RATIONALE: Acceleration of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(63).diff(_TD_MON)

def trev_374_black_swan_proxy_accel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_374_black_swan_proxy_accel_126d
    ECONOMIC RATIONALE: Acceleration of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(126).diff(_TD_MON)

def trev_375_black_swan_proxy_accel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_375_black_swan_proxy_accel_252d
    ECONOMIC RATIONALE: Acceleration of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(252).diff(_TD_MON)

# ── Registry ──────────────────────────────────────────────────────────────────
V110_REGISTRY_ACCEL = {
    "trev_301_var_95_proxy_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_301_var_95_proxy_accel_5d},
    "trev_302_var_95_proxy_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_302_var_95_proxy_accel_21d},
    "trev_303_var_95_proxy_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_303_var_95_proxy_accel_63d},
    "trev_304_var_95_proxy_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_304_var_95_proxy_accel_126d},
    "trev_305_var_95_proxy_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_305_var_95_proxy_accel_252d},
    "trev_306_expected_shortfall_proxy_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_306_expected_shortfall_proxy_accel_5d},
    "trev_307_expected_shortfall_proxy_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_307_expected_shortfall_proxy_accel_21d},
    "trev_308_expected_shortfall_proxy_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_308_expected_shortfall_proxy_accel_63d},
    "trev_309_expected_shortfall_proxy_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_309_expected_shortfall_proxy_accel_126d},
    "trev_310_expected_shortfall_proxy_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_310_expected_shortfall_proxy_accel_252d},
    "trev_311_tail_event_density_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_311_tail_event_density_accel_5d},
    "trev_312_tail_event_density_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_312_tail_event_density_accel_21d},
    "trev_313_tail_event_density_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_313_tail_event_density_accel_63d},
    "trev_314_tail_event_density_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_314_tail_event_density_accel_126d},
    "trev_315_tail_event_density_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_315_tail_event_density_accel_252d},
    "trev_316_skewness_252d_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_316_skewness_252d_accel_5d},
    "trev_317_skewness_252d_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_317_skewness_252d_accel_21d},
    "trev_318_skewness_252d_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_318_skewness_252d_accel_63d},
    "trev_319_skewness_252d_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_319_skewness_252d_accel_126d},
    "trev_320_skewness_252d_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_320_skewness_252d_accel_252d},
    "trev_321_kurtosis_252d_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_321_kurtosis_252d_accel_5d},
    "trev_322_kurtosis_252d_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_322_kurtosis_252d_accel_21d},
    "trev_323_kurtosis_252d_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_323_kurtosis_252d_accel_63d},
    "trev_324_kurtosis_252d_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_324_kurtosis_252d_accel_126d},
    "trev_325_kurtosis_252d_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_325_kurtosis_252d_accel_252d},
    "trev_326_tail_ratio_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_326_tail_ratio_accel_5d},
    "trev_327_tail_ratio_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_327_tail_ratio_accel_21d},
    "trev_328_tail_ratio_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_328_tail_ratio_accel_63d},
    "trev_329_tail_ratio_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_329_tail_ratio_accel_126d},
    "trev_330_tail_ratio_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_330_tail_ratio_accel_252d},
    "trev_331_extreme_low_z_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_331_extreme_low_z_accel_5d},
    "trev_332_extreme_low_z_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_332_extreme_low_z_accel_21d},
    "trev_333_extreme_low_z_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_333_extreme_low_z_accel_63d},
    "trev_334_extreme_low_z_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_334_extreme_low_z_accel_126d},
    "trev_335_extreme_low_z_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_335_extreme_low_z_accel_252d},
    "trev_336_tail_risk_momentum_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_336_tail_risk_momentum_accel_5d},
    "trev_337_tail_risk_momentum_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_337_tail_risk_momentum_accel_21d},
    "trev_338_tail_risk_momentum_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_338_tail_risk_momentum_accel_63d},
    "trev_339_tail_risk_momentum_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_339_tail_risk_momentum_accel_126d},
    "trev_340_tail_risk_momentum_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_340_tail_risk_momentum_accel_252d},
    "trev_341_gap_down_risk_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_341_gap_down_risk_accel_5d},
    "trev_342_gap_down_risk_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_342_gap_down_risk_accel_21d},
    "trev_343_gap_down_risk_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_343_gap_down_risk_accel_63d},
    "trev_344_gap_down_risk_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_344_gap_down_risk_accel_126d},
    "trev_345_gap_down_risk_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_345_gap_down_risk_accel_252d},
    "trev_346_tail_persistence_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_346_tail_persistence_accel_5d},
    "trev_347_tail_persistence_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_347_tail_persistence_accel_21d},
    "trev_348_tail_persistence_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_348_tail_persistence_accel_63d},
    "trev_349_tail_persistence_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_349_tail_persistence_accel_126d},
    "trev_350_tail_persistence_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_350_tail_persistence_accel_252d},
    "trev_351_tail_volatility_spread_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_351_tail_volatility_spread_accel_5d},
    "trev_352_tail_volatility_spread_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_352_tail_volatility_spread_accel_21d},
    "trev_353_tail_volatility_spread_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_353_tail_volatility_spread_accel_63d},
    "trev_354_tail_volatility_spread_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_354_tail_volatility_spread_accel_126d},
    "trev_355_tail_volatility_spread_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_355_tail_volatility_spread_accel_252d},
    "trev_356_downside_deviation_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_356_downside_deviation_accel_5d},
    "trev_357_downside_deviation_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_357_downside_deviation_accel_21d},
    "trev_358_downside_deviation_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_358_downside_deviation_accel_63d},
    "trev_359_downside_deviation_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_359_downside_deviation_accel_126d},
    "trev_360_downside_deviation_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_360_downside_deviation_accel_252d},
    "trev_361_tail_event_cluster_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_361_tail_event_cluster_accel_5d},
    "trev_362_tail_event_cluster_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_362_tail_event_cluster_accel_21d},
    "trev_363_tail_event_cluster_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_363_tail_event_cluster_accel_63d},
    "trev_364_tail_event_cluster_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_364_tail_event_cluster_accel_126d},
    "trev_365_tail_event_cluster_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_365_tail_event_cluster_accel_252d},
    "trev_366_tail_drawdown_corr_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_366_tail_drawdown_corr_accel_5d},
    "trev_367_tail_drawdown_corr_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_367_tail_drawdown_corr_accel_21d},
    "trev_368_tail_drawdown_corr_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_368_tail_drawdown_corr_accel_63d},
    "trev_369_tail_drawdown_corr_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_369_tail_drawdown_corr_accel_126d},
    "trev_370_tail_drawdown_corr_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_370_tail_drawdown_corr_accel_252d},
    "trev_371_black_swan_proxy_accel_5d": {"inputs": ["close", "low", "open"], "func": trev_371_black_swan_proxy_accel_5d},
    "trev_372_black_swan_proxy_accel_21d": {"inputs": ["close", "low", "open"], "func": trev_372_black_swan_proxy_accel_21d},
    "trev_373_black_swan_proxy_accel_63d": {"inputs": ["close", "low", "open"], "func": trev_373_black_swan_proxy_accel_63d},
    "trev_374_black_swan_proxy_accel_126d": {"inputs": ["close", "low", "open"], "func": trev_374_black_swan_proxy_accel_126d},
    "trev_375_black_swan_proxy_accel_252d": {"inputs": ["close", "low", "open"], "func": trev_375_black_swan_proxy_accel_252d},
}
