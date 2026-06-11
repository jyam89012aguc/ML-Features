"""
110_tail_risk_evt — Velocity (2nd Derivatives)
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

def trev_226_var_95_proxy_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_226_var_95_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(5)

def trev_227_var_95_proxy_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_227_var_95_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(21)

def trev_228_var_95_proxy_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_228_var_95_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(63)

def trev_229_var_95_proxy_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_229_var_95_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(126)

def trev_230_var_95_proxy_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_230_var_95_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of var_95_proxy. 5% Value-at-Risk proxy.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05)).diff(252)

def trev_231_expected_shortfall_proxy_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_231_expected_shortfall_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(5)

def trev_232_expected_shortfall_proxy_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_232_expected_shortfall_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(21)

def trev_233_expected_shortfall_proxy_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_233_expected_shortfall_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(63)

def trev_234_expected_shortfall_proxy_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_234_expected_shortfall_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(126)

def trev_235_expected_shortfall_proxy_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_235_expected_shortfall_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of expected_shortfall_proxy. Average loss in the bottom 5th percentile.
    """
    return (close.pct_change(1).apply(lambda x: x[x < x.quantile(0.05)].mean() if len(x[x < x.quantile(0.05)]) > 0 else 0)).diff(252)

def trev_236_tail_event_density_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_236_tail_event_density_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(5)

def trev_237_tail_event_density_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_237_tail_event_density_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(21)

def trev_238_tail_event_density_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_238_tail_event_density_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(63)

def trev_239_tail_event_density_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_239_tail_event_density_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(126)

def trev_240_tail_event_density_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_240_tail_event_density_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_event_density. Frequency of 5% tail events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(63).sum()).diff(252)

def trev_241_skewness_252d_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_241_skewness_252d_vel_5d
    ECONOMIC RATIONALE: Velocity of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(5)

def trev_242_skewness_252d_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_242_skewness_252d_vel_21d
    ECONOMIC RATIONALE: Velocity of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(21)

def trev_243_skewness_252d_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_243_skewness_252d_vel_63d
    ECONOMIC RATIONALE: Velocity of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(63)

def trev_244_skewness_252d_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_244_skewness_252d_vel_126d
    ECONOMIC RATIONALE: Velocity of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(126)

def trev_245_skewness_252d_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_245_skewness_252d_vel_252d
    ECONOMIC RATIONALE: Velocity of skewness_252d. Asymmetry of return distribution (negative = tail risk).
    """
    return (close.pct_change(1).rolling(252).skew()).diff(252)

def trev_246_kurtosis_252d_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_246_kurtosis_252d_vel_5d
    ECONOMIC RATIONALE: Velocity of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(5)

def trev_247_kurtosis_252d_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_247_kurtosis_252d_vel_21d
    ECONOMIC RATIONALE: Velocity of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(21)

def trev_248_kurtosis_252d_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_248_kurtosis_252d_vel_63d
    ECONOMIC RATIONALE: Velocity of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(63)

def trev_249_kurtosis_252d_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_249_kurtosis_252d_vel_126d
    ECONOMIC RATIONALE: Velocity of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(126)

def trev_250_kurtosis_252d_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_250_kurtosis_252d_vel_252d
    ECONOMIC RATIONALE: Velocity of kurtosis_252d. Fatness of tails in the return distribution.
    """
    return (close.pct_change(1).rolling(252).kurt()).diff(252)

def trev_251_tail_ratio_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_251_tail_ratio_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(5)

def trev_252_tail_ratio_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_252_tail_ratio_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(21)

def trev_253_tail_ratio_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_253_tail_ratio_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(63)

def trev_254_tail_ratio_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_254_tail_ratio_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(126)

def trev_255_tail_ratio_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_255_tail_ratio_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_ratio. Ratio of upside to downside tail risk.
    """
    return (abs(close.pct_change(1).rolling(252).quantile(0.95) / close.pct_change(1).rolling(252).quantile(0.05).replace(0, 1e-9))).diff(252)

def trev_256_extreme_low_z_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_256_extreme_low_z_vel_5d
    ECONOMIC RATIONALE: Velocity of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(5)

def trev_257_extreme_low_z_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_257_extreme_low_z_vel_21d
    ECONOMIC RATIONALE: Velocity of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(21)

def trev_258_extreme_low_z_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_258_extreme_low_z_vel_63d
    ECONOMIC RATIONALE: Velocity of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(63)

def trev_259_extreme_low_z_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_259_extreme_low_z_vel_126d
    ECONOMIC RATIONALE: Velocity of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(126)

def trev_260_extreme_low_z_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_260_extreme_low_z_vel_252d
    ECONOMIC RATIONALE: Velocity of extreme_low_z. Low price deviation from annual mean.
    """
    return (_zscore_rolling(low, 252)).diff(252)

def trev_261_tail_risk_momentum_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_261_tail_risk_momentum_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(5)

def trev_262_tail_risk_momentum_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_262_tail_risk_momentum_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(21)

def trev_263_tail_risk_momentum_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_263_tail_risk_momentum_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(63)

def trev_264_tail_risk_momentum_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_264_tail_risk_momentum_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(126)

def trev_265_tail_risk_momentum_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_265_tail_risk_momentum_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_risk_momentum. Trend in the severity of tail risk.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).diff(21)).diff(252)

def trev_266_gap_down_risk_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_266_gap_down_risk_vel_5d
    ECONOMIC RATIONALE: Velocity of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(5)

def trev_267_gap_down_risk_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_267_gap_down_risk_vel_21d
    ECONOMIC RATIONALE: Velocity of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(21)

def trev_268_gap_down_risk_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_268_gap_down_risk_vel_63d
    ECONOMIC RATIONALE: Velocity of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(63)

def trev_269_gap_down_risk_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_269_gap_down_risk_vel_126d
    ECONOMIC RATIONALE: Velocity of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(126)

def trev_270_gap_down_risk_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_270_gap_down_risk_vel_252d
    ECONOMIC RATIONALE: Velocity of gap_down_risk. 1st percentile of overnight gaps.
    """
    return ((open / close.shift(1) - 1).rolling(252).quantile(0.01)).diff(252)

def trev_271_tail_persistence_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_271_tail_persistence_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(5)

def trev_272_tail_persistence_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_272_tail_persistence_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(21)

def trev_273_tail_persistence_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_273_tail_persistence_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(63)

def trev_274_tail_persistence_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_274_tail_persistence_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(126)

def trev_275_tail_persistence_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_275_tail_persistence_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_persistence. Sequential tail events.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(10).sum() > 1).astype(float)).diff(252)

def trev_276_tail_volatility_spread_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_276_tail_volatility_spread_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(5)

def trev_277_tail_volatility_spread_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_277_tail_volatility_spread_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(21)

def trev_278_tail_volatility_spread_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_278_tail_volatility_spread_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(63)

def trev_279_tail_volatility_spread_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_279_tail_volatility_spread_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(126)

def trev_280_tail_volatility_spread_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_280_tail_volatility_spread_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_volatility_spread. Short-term vs long-term volatility expansion.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std()).diff(252)

def trev_281_downside_deviation_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_281_downside_deviation_vel_5d
    ECONOMIC RATIONALE: Velocity of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(5)

def trev_282_downside_deviation_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_282_downside_deviation_vel_21d
    ECONOMIC RATIONALE: Velocity of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(21)

def trev_283_downside_deviation_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_283_downside_deviation_vel_63d
    ECONOMIC RATIONALE: Velocity of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(63)

def trev_284_downside_deviation_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_284_downside_deviation_vel_126d
    ECONOMIC RATIONALE: Velocity of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(126)

def trev_285_downside_deviation_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_285_downside_deviation_vel_252d
    ECONOMIC RATIONALE: Velocity of downside_deviation. Standard deviation of negative returns only.
    """
    return (close.pct_change(1).clip(upper=0).rolling(252).std()).diff(252)

def trev_286_tail_event_cluster_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_286_tail_event_cluster_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(5)

def trev_287_tail_event_cluster_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_287_tail_event_cluster_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(21)

def trev_288_tail_event_cluster_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_288_tail_event_cluster_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(63)

def trev_289_tail_event_cluster_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_289_tail_event_cluster_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(126)

def trev_290_tail_event_cluster_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_290_tail_event_cluster_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_event_cluster. Clustering of extreme negative returns.
    """
    return (((close.pct_change(1) < close.pct_change(1).rolling(252).quantile(0.05)).rolling(21).sum())).diff(252)

def trev_291_tail_drawdown_corr_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_291_tail_drawdown_corr_vel_5d
    ECONOMIC RATIONALE: Velocity of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(5)

def trev_292_tail_drawdown_corr_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_292_tail_drawdown_corr_vel_21d
    ECONOMIC RATIONALE: Velocity of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(21)

def trev_293_tail_drawdown_corr_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_293_tail_drawdown_corr_vel_63d
    ECONOMIC RATIONALE: Velocity of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(63)

def trev_294_tail_drawdown_corr_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_294_tail_drawdown_corr_vel_126d
    ECONOMIC RATIONALE: Velocity of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(126)

def trev_295_tail_drawdown_corr_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_295_tail_drawdown_corr_vel_252d
    ECONOMIC RATIONALE: Velocity of tail_drawdown_corr. Correlation between tail risk and drawdown depth.
    """
    return (close.pct_change(1).rolling(252).quantile(0.05).rolling(63).corr(close / close.rolling(252).max() - 1)).diff(252)

def trev_296_black_swan_proxy_vel_5d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_296_black_swan_proxy_vel_5d
    ECONOMIC RATIONALE: Velocity of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(5)

def trev_297_black_swan_proxy_vel_21d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_297_black_swan_proxy_vel_21d
    ECONOMIC RATIONALE: Velocity of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(21)

def trev_298_black_swan_proxy_vel_63d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_298_black_swan_proxy_vel_63d
    ECONOMIC RATIONALE: Velocity of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(63)

def trev_299_black_swan_proxy_vel_126d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_299_black_swan_proxy_vel_126d
    ECONOMIC RATIONALE: Velocity of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(126)

def trev_300_black_swan_proxy_vel_252d(close: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    trev_300_black_swan_proxy_vel_252d
    ECONOMIC RATIONALE: Velocity of black_swan_proxy. Occurrence of 4-sigma negative events.
    """
    return ((close.pct_change(1) < close.pct_change(1).rolling(252).mean() - 4*close.pct_change(1).rolling(252).std()).astype(float)).diff(252)

# ── Registry ──────────────────────────────────────────────────────────────────
V110_REGISTRY_VEL = {
    "trev_226_var_95_proxy_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_226_var_95_proxy_vel_5d},
    "trev_227_var_95_proxy_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_227_var_95_proxy_vel_21d},
    "trev_228_var_95_proxy_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_228_var_95_proxy_vel_63d},
    "trev_229_var_95_proxy_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_229_var_95_proxy_vel_126d},
    "trev_230_var_95_proxy_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_230_var_95_proxy_vel_252d},
    "trev_231_expected_shortfall_proxy_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_231_expected_shortfall_proxy_vel_5d},
    "trev_232_expected_shortfall_proxy_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_232_expected_shortfall_proxy_vel_21d},
    "trev_233_expected_shortfall_proxy_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_233_expected_shortfall_proxy_vel_63d},
    "trev_234_expected_shortfall_proxy_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_234_expected_shortfall_proxy_vel_126d},
    "trev_235_expected_shortfall_proxy_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_235_expected_shortfall_proxy_vel_252d},
    "trev_236_tail_event_density_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_236_tail_event_density_vel_5d},
    "trev_237_tail_event_density_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_237_tail_event_density_vel_21d},
    "trev_238_tail_event_density_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_238_tail_event_density_vel_63d},
    "trev_239_tail_event_density_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_239_tail_event_density_vel_126d},
    "trev_240_tail_event_density_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_240_tail_event_density_vel_252d},
    "trev_241_skewness_252d_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_241_skewness_252d_vel_5d},
    "trev_242_skewness_252d_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_242_skewness_252d_vel_21d},
    "trev_243_skewness_252d_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_243_skewness_252d_vel_63d},
    "trev_244_skewness_252d_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_244_skewness_252d_vel_126d},
    "trev_245_skewness_252d_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_245_skewness_252d_vel_252d},
    "trev_246_kurtosis_252d_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_246_kurtosis_252d_vel_5d},
    "trev_247_kurtosis_252d_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_247_kurtosis_252d_vel_21d},
    "trev_248_kurtosis_252d_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_248_kurtosis_252d_vel_63d},
    "trev_249_kurtosis_252d_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_249_kurtosis_252d_vel_126d},
    "trev_250_kurtosis_252d_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_250_kurtosis_252d_vel_252d},
    "trev_251_tail_ratio_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_251_tail_ratio_vel_5d},
    "trev_252_tail_ratio_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_252_tail_ratio_vel_21d},
    "trev_253_tail_ratio_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_253_tail_ratio_vel_63d},
    "trev_254_tail_ratio_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_254_tail_ratio_vel_126d},
    "trev_255_tail_ratio_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_255_tail_ratio_vel_252d},
    "trev_256_extreme_low_z_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_256_extreme_low_z_vel_5d},
    "trev_257_extreme_low_z_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_257_extreme_low_z_vel_21d},
    "trev_258_extreme_low_z_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_258_extreme_low_z_vel_63d},
    "trev_259_extreme_low_z_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_259_extreme_low_z_vel_126d},
    "trev_260_extreme_low_z_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_260_extreme_low_z_vel_252d},
    "trev_261_tail_risk_momentum_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_261_tail_risk_momentum_vel_5d},
    "trev_262_tail_risk_momentum_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_262_tail_risk_momentum_vel_21d},
    "trev_263_tail_risk_momentum_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_263_tail_risk_momentum_vel_63d},
    "trev_264_tail_risk_momentum_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_264_tail_risk_momentum_vel_126d},
    "trev_265_tail_risk_momentum_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_265_tail_risk_momentum_vel_252d},
    "trev_266_gap_down_risk_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_266_gap_down_risk_vel_5d},
    "trev_267_gap_down_risk_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_267_gap_down_risk_vel_21d},
    "trev_268_gap_down_risk_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_268_gap_down_risk_vel_63d},
    "trev_269_gap_down_risk_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_269_gap_down_risk_vel_126d},
    "trev_270_gap_down_risk_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_270_gap_down_risk_vel_252d},
    "trev_271_tail_persistence_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_271_tail_persistence_vel_5d},
    "trev_272_tail_persistence_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_272_tail_persistence_vel_21d},
    "trev_273_tail_persistence_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_273_tail_persistence_vel_63d},
    "trev_274_tail_persistence_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_274_tail_persistence_vel_126d},
    "trev_275_tail_persistence_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_275_tail_persistence_vel_252d},
    "trev_276_tail_volatility_spread_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_276_tail_volatility_spread_vel_5d},
    "trev_277_tail_volatility_spread_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_277_tail_volatility_spread_vel_21d},
    "trev_278_tail_volatility_spread_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_278_tail_volatility_spread_vel_63d},
    "trev_279_tail_volatility_spread_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_279_tail_volatility_spread_vel_126d},
    "trev_280_tail_volatility_spread_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_280_tail_volatility_spread_vel_252d},
    "trev_281_downside_deviation_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_281_downside_deviation_vel_5d},
    "trev_282_downside_deviation_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_282_downside_deviation_vel_21d},
    "trev_283_downside_deviation_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_283_downside_deviation_vel_63d},
    "trev_284_downside_deviation_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_284_downside_deviation_vel_126d},
    "trev_285_downside_deviation_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_285_downside_deviation_vel_252d},
    "trev_286_tail_event_cluster_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_286_tail_event_cluster_vel_5d},
    "trev_287_tail_event_cluster_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_287_tail_event_cluster_vel_21d},
    "trev_288_tail_event_cluster_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_288_tail_event_cluster_vel_63d},
    "trev_289_tail_event_cluster_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_289_tail_event_cluster_vel_126d},
    "trev_290_tail_event_cluster_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_290_tail_event_cluster_vel_252d},
    "trev_291_tail_drawdown_corr_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_291_tail_drawdown_corr_vel_5d},
    "trev_292_tail_drawdown_corr_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_292_tail_drawdown_corr_vel_21d},
    "trev_293_tail_drawdown_corr_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_293_tail_drawdown_corr_vel_63d},
    "trev_294_tail_drawdown_corr_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_294_tail_drawdown_corr_vel_126d},
    "trev_295_tail_drawdown_corr_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_295_tail_drawdown_corr_vel_252d},
    "trev_296_black_swan_proxy_vel_5d": {"inputs": ["close", "low", "open"], "func": trev_296_black_swan_proxy_vel_5d},
    "trev_297_black_swan_proxy_vel_21d": {"inputs": ["close", "low", "open"], "func": trev_297_black_swan_proxy_vel_21d},
    "trev_298_black_swan_proxy_vel_63d": {"inputs": ["close", "low", "open"], "func": trev_298_black_swan_proxy_vel_63d},
    "trev_299_black_swan_proxy_vel_126d": {"inputs": ["close", "low", "open"], "func": trev_299_black_swan_proxy_vel_126d},
    "trev_300_black_swan_proxy_vel_252d": {"inputs": ["close", "low", "open"], "func": trev_300_black_swan_proxy_vel_252d},
}
