"""
17_volume_climax — Base Features 076–150
Domain: single-day extreme volume events
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Distributional Climax Ranks
def vcx_076_climax_pct_rank_252d(volume: pd.Series) -> pd.Series:
    return volume.rolling(252).rank(pct=True)


def vcx_077_climax_zscore_63d(volume: pd.Series) -> pd.Series:
    return (volume - _rolling_mean(volume, 63)) / volume.rolling(63).std()


def vcx_078_climax_concentration_ratio_63d(volume: pd.Series) -> pd.Series:
    # Volume today / avg volume in 63 days
    return _safe_div(volume, _rolling_mean(volume, 63))


# 091-105: Climax Event Signatures (Pattern Matching)
def vcx_091_climax_at_range_peak_63d(volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    # Volume ratio on the day of the widest daily range in 63 days
    r = high - low
    is_max_r = (r == r.rolling(63).max())
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    return v_rat.where(is_max_r).ffill()


def vcx_092_climax_at_gap_peak_63d(volume: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    is_max_g = (gap == gap.rolling(63).max())
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    return v_rat.where(is_max_g).ffill()


# 106-125: Specialized Climax Accelerators
def vcx_106_climax_impulse_score_21d(volume: pd.Series) -> pd.Series:
    # (Volume / Prev Day Volume) - 1
    return _safe_div(volume, volume.shift(1)) - 1.0


def vcx_107_climax_magnitude_drift_63d(volume: pd.Series) -> pd.Series:
    # Slope of climax ratios
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    return v_rat.rolling(63).apply(_slope, raw=True)


# 126-140: Multi-Metric Alignment Composites
def vcx_126_climax_to_fundamental_ratio_spread(volume: pd.Series, netinc: pd.Series, sharesbas: pd.Series) -> pd.Series:
    # (Turnover Climax) - (Earnings Climax proxy)
    to = _safe_div(volume, sharesbas)
    to_rat = _safe_div(to, to.rolling(252).median())
    # Sparse earnings proxy
    e_rat = _safe_div(netinc.abs(), netinc.abs().expanding().median())
    return to_rat - e_rat.ffill()


def vcx_127_climax_at_dividend_indicator(volume: pd.Series, dividend: pd.Series) -> pd.Series:
    # Volume spike ratio on dividend ex-dates
    ratio = _safe_div(volume, _rolling_median(volume, 252))
    return ratio.where(dividend > 0).ffill()


# 141-150: Final Climax composites
def vcx_141_terminal_volume_spike_acceleration(volume: pd.Series) -> pd.Series:
    # Rate of change of the 5-day volume spike ratio
    vs = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 63))
    return vs.diff(5)


def vcx_142_climax_to_volatility_adjusted_depth(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Volume Spike) * (Drawdown / Volatility)
    vs = _safe_div(volume, _rolling_median(volume, 63))
    h = close.rolling(252).max()
    dd = (h - close) / h
    vol = close.pct_change().rolling(21).std()
    return vs * _safe_div(dd, vol)


def vcx_143_consecutive_days_with_climax_volume(volume: pd.Series) -> pd.Series:
    # Days in a row volume > 2x median
    med = _rolling_median(volume, 252)
    is_climax = (volume > 2 * med).astype(int)
    return is_climax.groupby((is_climax == 0).cumsum()).cumsum()


def vcx_144_climax_reversal_trap_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    # (Volume Climax) * (Close in Lower Half of Range)
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    r = high - low
    pos = (close - low) / (r + _EPS)
    return v_rat * (1.0 - pos)


def vcx_145_mktcap_turnover_climax_zscore(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    to = _safe_div(volume, sharesbas)
    idx = mc * to
    return (idx - idx.rolling(252).mean()) / idx.rolling(252).std()


def vcx_146_years_since_max_climax_ath(volume: pd.Series) -> pd.Series:
    idx = volume.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vcx_147_climax_at_new_ath_low_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    val = v_rat.where(is_low).ffill()
    return val.diff(5)


def vcx_148_volume_climax_skew_intensity_63d(volume: pd.Series) -> pd.Series:
    # (Max Volume / Median Volume) / Volume Skewness
    mx = _rolling_max(volume, 63)
    med = _rolling_median(volume, 63)
    skew = volume.rolling(63).skew()
    return _safe_div(_safe_div(mx, med), skew.abs())


def vcx_149_climax_integral_ratio_21d(volume: pd.Series) -> pd.Series:
    # Total volume in last 5 days / volume in last 21 days
    return _safe_div(volume.rolling(5).sum(), volume.rolling(21).sum())


def vcx_150_final_volume_capitulation_climax(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    # Composite of Spike, Reversal, and Depth
    vs = _safe_div(volume, _rolling_median(volume, 63))
    rev = _safe_div(close - low, high - low)
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    return vs * rev * dd


# ── Registry ──────────────────────────────────────────────────────────────────

V17_REGISTRY = {
    "vcx_076_climax_pct_rank_252d": {"inputs": ["volume"], "func": vcx_076_climax_pct_rank_252d},
    "vcx_077_climax_zscore_63d": {"inputs": ["volume"], "func": vcx_077_climax_zscore_63d},
    "vcx_078_climax_concentration_ratio_63d": {"inputs": ["volume"], "func": vcx_078_climax_concentration_ratio_63d},
    "vcx_091_climax_at_range_peak_63d": {"inputs": ["volume", "high", "low"], "func": vcx_091_climax_at_range_peak_63d},
    "vcx_092_climax_at_gap_peak_63d": {"inputs": ["volume", "close", "open"], "func": vcx_092_climax_at_gap_peak_63d},
    "vcx_106_climax_impulse_score_21d": {"inputs": ["volume"], "func": vcx_106_climax_impulse_score_21d},
    "vcx_107_climax_magnitude_drift_63d": {"inputs": ["volume"], "func": vcx_107_climax_magnitude_drift_63d},
    "vcx_126_climax_fundamental_spread": {"inputs": ["volume", "netinc", "sharesbas"], "func": vcx_126_climax_to_fundamental_ratio_spread},
    "vcx_127_climax_at_dividend_indicator": {"inputs": ["volume", "dividend"], "func": vcx_127_climax_at_dividend_indicator},
    "vcx_141_terminal_volume_spike_acceleration": {"inputs": ["volume"], "func": vcx_141_terminal_volume_spike_acceleration},
    "vcx_142_climax_to_vol_adjusted_depth": {"inputs": ["close", "volume"], "func": vcx_142_climax_to_volatility_adjusted_depth},
    "vcx_143_consecutive_climax_days": {"inputs": ["volume"], "func": vcx_143_consecutive_days_with_climax_volume},
    "vcx_144_climax_reversal_trap_score": {"inputs": ["close", "high", "low", "volume"], "func": vcx_144_climax_reversal_trap_score},
    "vcx_145_mktcap_turnover_climax_zscore": {"inputs": ["close", "volume", "sharesbas"], "func": vcx_145_mktcap_turnover_climax_zscore},
    "vcx_146_years_since_max_climax_ath": {"inputs": ["volume"], "func": vcx_146_years_since_max_climax_ath},
    "vcx_147_climax_at_ath_low_velocity": {"inputs": ["close", "volume"], "func": vcx_147_climax_at_new_ath_low_velocity},
    "vcx_148_volume_climax_skew_intensity_63d": {"inputs": ["volume"], "func": vcx_148_volume_climax_skew_intensity_63d},
    "vcx_149_climax_integral_ratio_21d": {"inputs": ["volume"], "func": vcx_149_climax_integral_ratio_21d},
    "vcx_150_final_volume_capitulation_climax": {"inputs": ["close", "volume", "high", "low"], "func": vcx_150_final_volume_capitulation_climax},
}
