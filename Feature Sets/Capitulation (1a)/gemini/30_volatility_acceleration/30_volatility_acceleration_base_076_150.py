"""
30_volatility_acceleration — Base Features 076–150
Domain: second derivative of volatility, fear breakaway
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Vol Acceleration (Ranks)
def vtac_076_vol_accel_pct_rank_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 5)
    return a.expanding().rank(pct=True)


def vtac_077_vol_accel_volatility_63d(close: pd.Series) -> pd.Series:
    # Std dev of daily volatility acceleration values
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 1)
    return a.rolling(63).std() / (v.rolling(252).mean() + _EPS)


# 091-105: Climax Acceleration Threshold Counts
def vtac_091_count_extreme_vol_accel_days_252d(close: pd.Series) -> pd.Series:
    # Days with vol acceleration > 2.5 standard deviations
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    threshold = a.rolling(252).mean() + 2.5 * a.rolling(252).std()
    return (a > threshold).rolling(252).sum()


def vtac_092_days_since_peak_vol_accel_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 5).abs()
    idx = a.expanding().apply(np.argmax, raw=True)
    return pd.Series(np.arange(len(close)), index=close.index) - idx


# 106-125: specialized Vol-Flow Accelerators
def vtac_106_vol_accel_to_vol_drift_ratio(close: pd.Series) -> pd.Series:
    # Accel / Abs(Slope)
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 5).abs()
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    s = v.rolling(21).apply(_slope, raw=True).abs()
    return _safe_div(a, s)


def vtac_107_vol_accel_at_climax_volume_spike(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Vol acceleration on the day of highest 63-day volume
    v_rat = _safe_div(volume, volume.rolling(252).median())
    idx = v_rat.rolling(63).apply(np.argmax, raw=True)
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    return a.iloc[idx.astype(int)]


# 126-140: Multi-Horizon Risk Breakaway
def vtac_126_vol_accel_spread_short_long(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1))
    a_s = _calculate_accel(v.rolling(5).std(), 5)
    a_l = _calculate_accel(v.rolling(21).std(), 21)
    return a_s - a_l


# 141-150: Final Vol Acceleration composites
def vtac_141_fear_acceleration_exhaustion_index(close: pd.Series) -> pd.Series:
    # (Vol Accel) / (Price Range Stability)
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    r = (close.rolling(21).max() - close.rolling(21).min()) / close.rolling(21).mean()
    def _rsq(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = r.rolling(21).apply(_rsq, raw=True)
    return _safe_div(va, rs + _EPS)


def vtac_142_energy_density_vol_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Change in (Volatility^2 * Volume)
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    ed = (v**2) * v_rat
    return _calculate_accel(ed, 21)


def vtac_143_consecutive_days_high_vol_accel(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    is_high = (a > a.rolling(252).median())
    return is_high.astype(int).groupby((is_high == 0).cumsum()).cumsum()


def vtac_144_vol_accel_reversal_climax_score(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5)
    vva = va.diff(5)
    c_low = _safe_div(close, low)
    return vva * c_low


def vtac_145_mktcap_vol_accel_persistence(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    mv = np.log(mc / mc.shift(1)).rolling(21).std()
    ma = _calculate_accel(mv, 21)
    return (ma > 0).rolling(63).mean()


def vtac_146_years_since_max_vol_accel_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5).abs()
    idx = a.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vtac_147_vol_accel_regime_break_63d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    return _calculate_accel(v, 5) - _calculate_accel(v, 63)


def vtac_148_consecutive_days_vol_accel_gt_median(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    med = a.rolling(252).median()
    is_high = (a > med).astype(int)
    return is_high.groupby((is_high == 0).cumsum()).cumsum()


def vtac_149_cumulative_vol_accel_energy_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    return a.cumsum() / (a.abs().cumsum() + _EPS)


def vtac_150_vol_accel_final_climax_index(close: pd.Series) -> pd.Series:
    # Composite: (Vol Accel) * (1 - Recovery Fraction) * (Drawdown Depth)
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    dd = (h - close) / h
    return va * (1.0 - rf) * dd


# ── Registry ──────────────────────────────────────────────────────────────────

V30_REGISTRY = {
    "vtac_076_vol_accel_pct_rank_ath": {"inputs": ["close"], "func": vtac_076_vol_accel_pct_rank_ath},
    "vtac_077_vol_accel_volatility_63d": {"inputs": ["close"], "func": vtac_077_vol_accel_volatility_63d},
    "vtac_091_count_extreme_vol_accel_days_252d": {"inputs": ["close"], "func": vtac_091_count_extreme_vol_accel_days_252d},
    "vtac_092_days_since_peak_vol_accel_ath": {"inputs": ["close"], "func": vtac_092_days_since_peak_vol_accel_ath},
    "vtac_106_vol_accel_drift_ratio": {"inputs": ["close"], "func": vtac_106_vol_accel_to_vol_drift_ratio},
    "vtac_107_vol_accel_at_volume_climax": {"inputs": ["close", "volume"], "func": vtac_107_vol_accel_at_climax_volume_spike},
    "vtac_126_vol_accel_spread_short_long": {"inputs": ["close"], "func": vtac_126_vol_accel_spread_short_long},
    "vtac_141_fear_accel_exhaustion_index": {"inputs": ["close"], "func": vtac_141_fear_acceleration_exhaustion_index},
    "vtac_142_energy_density_vol_accel_63d": {"inputs": ["close", "volume"], "func": vtac_142_energy_density_vol_accel_63d},
    "vtac_143_consecutive_high_vol_accel_days": {"inputs": ["close"], "func": vtac_143_consecutive_days_high_vol_accel},
    "vtac_144_vol_accel_reversal_climax": {"inputs": ["close", "low"], "func": vtac_144_vol_accel_reversal_climax_score},
    "vtac_145_mktcap_vol_accel_persistence": {"inputs": ["close", "sharesbas"], "func": vtac_145_mktcap_vol_accel_persistence},
    "vtac_146_years_since_max_vol_accel_ath": {"inputs": ["close"], "func": vtac_146_years_since_max_vol_accel_ath},
    "vtac_147_vol_accel_regime_break_63d": {"inputs": ["close"], "func": vtac_147_vol_accel_regime_break_63d},
    "vtac_148_consecutive_vol_accel_gt_median": {"inputs": ["close"], "func": vtac_148_consecutive_days_vol_accel_gt_median},
    "vtac_149_cumulative_vol_accel_energy_ath": {"inputs": ["close"], "func": vtac_149_cumulative_vol_accel_energy_ath},
    "vtac_150_vol_accel_final_climax_index": {"inputs": ["close"], "func": vtac_150_vol_accel_final_climax_index},
}
