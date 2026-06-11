"""
14_recovery_failure — Base Features 076–150
Domain: failed bounces, lower-highs within drawdown
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Failures
def rfl_076_max_bounce_pct_rank_ath(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    l_idx = argrelextrema(close.values, np.less, order=5)[0]
    h_idx = argrelextrema(close.values, np.greater, order=5)[0]
    # Simple proxy: current return from 63d low vs historical returns from local lows
    l = _rolling_min(close, 63)
    b = (close - l) / l
    return b.expanding().rank(pct=True)


def rfl_077_bounce_volatility_zscore_252d(close: pd.Series) -> pd.Series:
    # How volatile are the bounces in the last year?
    ret = close.pct_change()
    b_ret = ret.where(ret > 0.02)
    b_vol = b_ret.rolling(252).std()
    return (b_vol - b_vol.rolling(252).mean()) / b_vol.rolling(252).std()


def rfl_078_recovery_fraction_pct_rank_252d(close: pd.Series) -> pd.Series:
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    rf = _safe_div(close - l, h - l)
    return rf.rolling(252).rank(pct=True)


# 091-105: Threshold-Based Failure counts
def rfl_091_count_fading_bounces_63d(close: pd.Series) -> pd.Series:
    # Count of rallies > 3% that reversed and made a new low within 10 days
    ret = close.pct_change()
    is_bounce = (ret.rolling(3).sum() > 0.03).astype(int)
    new_low = (close == _rolling_min(close, 63)).astype(int)
    faded = is_bounce.shift(10) & new_low
    return faded.rolling(63).sum()


def rfl_092_count_lower_high_breaches_252d(close: pd.Series) -> pd.Series:
    # Number of times price failed to break above the previous local peak
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    peaks = close.iloc[peaks_idx].reindex(close.index).ffill()
    failed = (close > peaks.shift(1) * 0.98) & (close < peaks.shift(1))
    return failed.rolling(252).sum()


# 106-125: Event and Metric Specific Failures
def rfl_106_equity_ps_recovery_failure_spread(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    p_rec = close / close.cummax()
    bv_rec = (equity / sharesbas) / (equity / sharesbas).cummax()
    return p_rec - bv_rec


def rfl_107_insider_sell_at_bounce_peak_63d(close: pd.Series, insider_sells: pd.Series) -> pd.Series:
    # Sells occurring within 2% of the 63-day high
    h = _rolling_max(close, 63)
    at_high = (close >= h * 0.98)
    return (at_high & (insider_sells > 0)).rolling(63).sum()


# 126-140: Multi- Horizon Resistance Dynamics
def rfl_126_resistance_zone_density_63d(close: pd.Series) -> pd.Series:
    # Number of days spent within 2% of any local peak in last 63 days
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    peaks = close.iloc[peaks_idx]
    # Check current close against the set of peaks (vectorized proxy)
    avg_peak = peaks.rolling(10).mean().reindex(close.index).ffill()
    return ((close / avg_peak - 1).abs() < 0.02).rolling(63).sum()


def rfl_127_bounce_rejection_velocity_21d(close: pd.Series) -> pd.Series:
    # Speed of decline after hitting a 21-day high
    h = _rolling_max(close, 21)
    is_high = (close == h)
    high_val = close.where(is_high).ffill()
    return (close - high_val).diff(5)


# 141-150: Final Failure composites
def rfl_141_recovery_exhaustion_score_63d(close: pd.Series) -> pd.Series:
    # (Bounce Magnitude) / (Days Since Low) -> decreasing = exhaustion
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    is_low = (close == l)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_low).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - idx
    return _safe_div(b, dsl + 1)


def rfl_142_mktcap_lower_high_count_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(mc.values, np.greater, order=5)[0]
    peaks = mc.iloc[peaks_idx]
    is_lower = (peaks < peaks.shift(1)).astype(int)
    return is_lower.rolling(252, min_periods=1).sum().reindex(close.index).ffill()


def rfl_143_consecutive_days_with_fading_bounces(close: pd.Series) -> pd.Series:
    # Days since last 1% up-day that didn't result in a new high
    ret = close.pct_change()
    h = _rolling_max(close, 21)
    failing = (ret > 0.01) & (close < h.shift(1))
    return failing.astype(int).groupby((failing == 0).cumsum()).cumsum()


def rfl_144_bounce_amplitude_decay_index_63d(close: pd.Series) -> pd.Series:
    # Ratio of current bounce to avg of last 3 bounces
    from scipy.signal import argrelextrema
    l_idx = argrelextrema(close.values, np.less, order=5)[0]
    h_idx = argrelextrema(close.values, np.greater, order=5)[0]
    # Simple proxy: current recovery / avg recovery
    rec = _safe_div(close - _rolling_min(close, 21), _rolling_min(close, 21))
    return _safe_div(rec, rec.rolling(63).mean())


def rfl_145_ath_drawdown_stalling_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    return dd.diff(5).where(dd > 0.20)


def rfl_146_failed_rally_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume on failed rallies (price up but < 1% gain) vs Volume on strong rallies
    ret = close.pct_change()
    v_weak = volume.where((ret > 0) & (ret < 0.01)).rolling(63).mean()
    v_strong = volume.where(ret >= 0.02).rolling(63).mean()
    return _safe_div(v_weak, v_strong)


def rfl_147_recovery_trap_persistence_21d(close: pd.Series) -> pd.Series:
    # Days where price was above its 5-day average but below its 21-day average
    ma5 = close.rolling(5).mean()
    ma21 = close.rolling(21).mean()
    return ((close > ma5) & (close < ma21)).astype(int).rolling(21).sum()


def rfl_148_ratio_of_bounces_to_new_lows_252d(close: pd.Series) -> pd.Series:
    # (Count of rallies > 5%) / (Count of new 252d lows)
    ret = close.pct_change()
    b = (ret > 0.05).rolling(252).sum()
    l = (close == _rolling_min(close, 252)).astype(int).rolling(252).sum()
    return _safe_div(b, l)


def rfl_149_bounce_duration_zscore_ath(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    is_up = (ret > 0).astype(int)
    streak = is_up.groupby((is_up == 0).cumsum()).cumsum()
    return (streak - streak.expanding().mean()) / (streak.expanding().std() + _EPS)


def rfl_150_terminal_resistance_climax_score(close: pd.Series) -> pd.Series:
    # (Lower High Count) / (Standard Deviation of Bounces)
    lh = rfl_016_count_lower_highs_63d(close)
    b_vol = close.pct_change().where(close.pct_change() > 0).rolling(63).std()
    return _safe_div(lh, b_vol + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

V14_REGISTRY = {
    "rfl_076_max_bounce_pct_rank_ath": {"inputs": ["close"], "func": rfl_076_max_bounce_pct_rank_ath},
    "rfl_077_bounce_volatility_zscore_252d": {"inputs": ["close"], "func": rfl_077_bounce_volatility_zscore_252d},
    "rfl_078_recovery_fraction_pct_rank_252d": {"inputs": ["close"], "func": rfl_078_recovery_fraction_pct_rank_252d},
    "rfl_091_count_fading_bounces_63d": {"inputs": ["close"], "func": rfl_091_count_fading_bounces_63d},
    "rfl_092_count_lower_high_breaches_252d": {"inputs": ["close"], "func": rfl_092_count_lower_high_breaches_252d},
    "rfl_106_equity_ps_recovery_failure_spread": {"inputs": ["close", "equity", "sharesbas"], "func": rfl_106_equity_ps_recovery_failure_spread},
    "rfl_107_insider_sell_at_bounce_peak_63d": {"inputs": ["close", "insider_sells"], "func": rfl_107_insider_sell_at_bounce_peak_63d},
    "rfl_126_resistance_zone_density_63d": {"inputs": ["close"], "func": rfl_126_resistance_zone_density_63d},
    "rfl_127_bounce_rejection_velocity_21d": {"inputs": ["close"], "func": rfl_127_bounce_rejection_velocity_21d},
    "rfl_141_recovery_exhaustion_score_63d": {"inputs": ["close"], "func": rfl_141_recovery_exhaustion_score_63d},
    "rfl_142_mktcap_lower_high_count_252d": {"inputs": ["close", "sharesbas"], "func": rfl_142_mktcap_lower_high_count_252d},
    "rfl_143_consecutive_days_with_fading_bounces": {"inputs": ["close"], "func": rfl_143_consecutive_days_with_fading_bounces},
    "rfl_144_bounce_amplitude_decay_index_63d": {"inputs": ["close"], "func": rfl_144_bounce_amplitude_decay_index_63d},
    "rfl_145_ath_drawdown_stalling_velocity": {"inputs": ["close"], "func": rfl_145_ath_drawdown_stalling_velocity},
    "rfl_146_failed_rally_volume_ratio_63d": {"inputs": ["close", "volume"], "func": rfl_146_failed_rally_volume_ratio_63d},
    "rfl_147_recovery_trap_persistence_21d": {"inputs": ["close"], "func": rfl_147_recovery_trap_persistence_21d},
    "rfl_148_ratio_of_bounces_to_new_lows_252d": {"inputs": ["close"], "func": rfl_148_ratio_of_bounces_to_new_lows_252d},
    "rfl_149_bounce_duration_zscore_ath": {"inputs": ["close"], "func": rfl_149_bounce_duration_zscore_ath},
    "rfl_150_terminal_resistance_climax_score": {"inputs": ["close"], "func": rfl_150_terminal_resistance_climax_score},
}
