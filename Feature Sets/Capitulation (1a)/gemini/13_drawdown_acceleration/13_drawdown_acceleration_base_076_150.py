"""
13_drawdown_acceleration — Base Features 076–150
Domain: whether the decline is speeding up
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Acceleration
def dacc_076_accel_pct_rank_ath(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return a.expanding().rank(pct=True)


def dacc_077_accel_volatility_63d(close: pd.Series) -> pd.Series:
    # Std dev of daily acceleration values
    a = _calculate_accel(np.log(close), 1)
    return a.rolling(63).std()


def dacc_078_accel_skewness_63d(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return a.rolling(63).skew()


# 091-105: Threshold and Peak Acceleration counts
def dacc_091_count_extreme_accel_days_252d(close: pd.Series) -> pd.Series:
    # Days with acceleration < -2 standard deviations
    a = _calculate_accel(np.log(close), 5)
    threshold = a.rolling(252).mean() - 2 * a.rolling(252).std()
    return (a < threshold).rolling(252).sum()


def dacc_092_days_since_ath_acceleration_peak(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    a = _calculate_accel(dist, 5)
    idx = a.expanding().apply(np.argmax, raw=True)
    return pd.Series(np.arange(len(close)), index=close.index) - idx


# 106-125: Curvature and Cubic (3rd derivative) components
def dacc_106_log_price_curvature_63d(close: pd.Series) -> pd.Series:
    # Coeff of x^2 in rolling log price regression (direct acceleration proxy)
    def _poly2(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    return np.log(close).rolling(63).apply(_poly2, raw=True)


def dacc_107_acceleration_of_underwater_integral_63d(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    integral = uw.cumsum()
    return _calculate_accel(integral, 21)


# 126-140: Multi-Asset and Event Acceleration
def dacc_126_mktcap_to_revenue_accel_ratio(close: pd.Series, sharesbas: pd.Series, revenue: pd.Series) -> pd.Series:
    mc = close * sharesbas
    a_mc = _calculate_accel(np.log(mc), 21)
    a_rev = _calculate_accel(np.log(revenue + _EPS), 1) # Assumes quarterly
    return _safe_div(a_mc, a_rev)


def dacc_127_accel_at_earnings_surprise(close: pd.Series, surprise: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return a.where(surprise.abs() > 0).ffill()


# 141-150: Final Acceleration composites
def dacc_141_terminal_drawdown_accel_score(close: pd.Series) -> pd.Series:
    # Sum of negative accelerations over short horizons
    a1 = _calculate_accel(np.log(close), 1)
    a3 = _calculate_accel(np.log(close), 3)
    a5 = _calculate_accel(np.log(close), 5)
    return (a1.clip(upper=0) + a3.clip(upper=0) + a5.clip(upper=0))


def dacc_142_acceleration_energy_density_63d(close: pd.Series) -> pd.Series:
    # Mean squared acceleration / volatility
    a = _calculate_accel(np.log(close), 5)
    v = close.pct_change().rolling(63).std()
    return _safe_div((a**2).rolling(63).mean(), v)


def dacc_143_consecutive_down_accel_streak(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    is_neg = (a < a.shift(1))
    return is_neg.astype(int).groupby((is_neg == 0).cumsum()).cumsum()


def dacc_144_acceleration_reversal_intensity_63d(close: pd.Series) -> pd.Series:
    # Number of times acceleration sign flips
    a = _calculate_accel(np.log(close), 5)
    flip = (np.sign(a) != np.sign(a.shift(1))).astype(int)
    return flip.rolling(63).sum()


def dacc_145_mktcap_accel_zscore_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    a = _calculate_accel(np.log(mc), 21)
    return (a - a.rolling(252).mean()) / a.rolling(252).std()


def dacc_146_accel_normalized_by_drawdown_depth(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return _safe_div(a, dd + _EPS)


def dacc_147_days_spent_in_negative_accel_last_63d(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return (a < 0).rolling(63).sum()


def dacc_148_accel_at_vol_peak_63d(close: pd.Series) -> pd.Series:
    v = close.pct_change().rolling(21).std()
    max_v_idx = v.rolling(63).apply(np.argmax, raw=True)
    a = _calculate_accel(np.log(close), 5)
    return a.iloc[max_v_idx.astype(int)]


def dacc_149_accel_autocorrelation_lag_1_63d(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return a.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)


def dacc_150_final_accel_capitulation_index(close: pd.Series) -> pd.Series:
    # (Accel * Velocity) / (1 - Proximity to Low)
    a = _calculate_accel(np.log(close), 5).abs()
    v = np.log(close).diff(5).abs()
    l = close.rolling(252).min()
    prox = _safe_div(close, l)
    return (a * v) / (prox - 1.0 + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

V13_REGISTRY = {
    "dacc_076_accel_pct_rank_ath": {"inputs": ["close"], "func": dacc_076_accel_pct_rank_ath},
    "dacc_077_accel_volatility_63d": {"inputs": ["close"], "func": dacc_077_accel_volatility_63d},
    "dacc_078_accel_skewness_63d": {"inputs": ["close"], "func": dacc_078_accel_skewness_63d},
    "dacc_091_count_extreme_accel_days_252d": {"inputs": ["close"], "func": dacc_091_count_extreme_accel_days_252d},
    "dacc_092_days_since_ath_acceleration_peak": {"inputs": ["close"], "func": dacc_092_days_since_ath_acceleration_peak},
    "dacc_106_log_price_curvature_63d": {"inputs": ["close"], "func": dacc_106_log_price_curvature_63d},
    "dacc_107_acceleration_of_underwater_integral_63d": {"inputs": ["close"], "func": dacc_107_acceleration_of_underwater_integral_63d},
    "dacc_126_mktcap_to_revenue_accel_ratio": {"inputs": ["close", "sharesbas", "revenue"], "func": dacc_126_mktcap_to_revenue_accel_ratio},
    "dacc_127_accel_at_earnings_surprise": {"inputs": ["close", "surprise"], "func": dacc_127_accel_at_earnings_surprise},
    "dacc_141_terminal_drawdown_accel_score": {"inputs": ["close"], "func": dacc_141_terminal_drawdown_accel_score},
    "dacc_142_acceleration_energy_density_63d": {"inputs": ["close"], "func": dacc_142_acceleration_energy_density_63d},
    "dacc_143_consecutive_down_accel_streak": {"inputs": ["close"], "func": dacc_143_consecutive_down_accel_streak},
    "dacc_144_acceleration_reversal_intensity_63d": {"inputs": ["close"], "func": dacc_144_acceleration_reversal_intensity_63d},
    "dacc_145_mktcap_accel_zscore_252d": {"inputs": ["close", "sharesbas"], "func": dacc_145_mktcap_accel_zscore_252d},
    "dacc_146_accel_normalized_by_drawdown_depth": {"inputs": ["close"], "func": dacc_146_accel_normalized_by_drawdown_depth},
    "dacc_147_days_spent_in_negative_accel_last_63d": {"inputs": ["close"], "func": dacc_147_days_spent_in_negative_accel_last_63d},
    "dacc_148_accel_at_vol_peak_63d": {"inputs": ["close"], "func": dacc_148_accel_at_vol_peak_63d},
    "dacc_149_accel_autocorrelation_lag_1_63d": {"inputs": ["close"], "func": dacc_149_accel_autocorrelation_lag_1_63d},
    "dacc_150_final_accel_capitulation_index": {"inputs": ["close"], "func": dacc_150_final_accel_capitulation_index},
}
