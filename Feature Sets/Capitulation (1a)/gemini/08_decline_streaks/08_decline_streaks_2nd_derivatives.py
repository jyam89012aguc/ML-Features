"""
Decline Streaks — 2nd Derivatives
Domain: consecutive down days and negative persistence
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

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def dstk_drv2_001_consecutive_down_days_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_001_consecutive_down_days_velocity feature"""
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    return dur.diff(5)

def dstk_drv2_002_cumulative_streak_loss_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_002_cumulative_streak_loss_velocity feature"""
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby(streak_id).cumsum()) - 1).abs()
    return loss.diff(5)

def dstk_drv2_003_down_day_frequency_21d_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_003_down_day_frequency_21d_velocity feature"""
    f = (close < close.shift(1)).rolling(21).mean()
    return f.diff(5)

def dstk_drv2_004_streak_loss_zscore_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_004_streak_loss_zscore_velocity feature"""
    ret = close.pct_change()
    is_down = (ret < 0)
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby((is_down != is_down.shift()).cumsum()).cumsum()) - 1).abs()
    z = (loss - loss.rolling(252).mean()) / loss.rolling(252).std()
    return z.diff(5)

def dstk_drv2_005_streak_acceleration_index_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_005_streak_acceleration_index_velocity feature"""
    f5 = (close < close.shift(1)).rolling(5).mean()
    f21 = (close < close.shift(1)).rolling(21).mean()
    idx = _safe_div(f5, f21)
    return idx.diff(5)

def dstk_drv2_006_days_since_last_up_day_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_006_days_since_last_up_day_velocity feature"""
    is_up = (close > close.shift(1))
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_up).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - indices
    return dsl.diff(5)

def dstk_drv2_007_down_streak_intensity_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_007_down_streak_intensity_velocity feature"""
    dur = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    return (dur * loss).diff(5)

def dstk_drv2_008_streak_exhaustion_prob_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_008_streak_exhaustion_prob_velocity feature"""
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    def _prob(y):
        if len(y) == 0: return 0.0
        curr_dur = y[-1]
        if curr_dur == 0: return 0.0
        relevant = y[y >= curr_dur]
        ends = (relevant.shift(-1) == 0).sum()
        return ends / len(relevant)
    p = dur.rolling(252).apply(_prob, raw=True)
    return p.diff(5)

def dstk_drv2_009_consecutive_red_candles_velocity(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_drv2_009_consecutive_red_candles_velocity feature"""
    return _consecutive_count(close < open).diff(5)

def dstk_drv2_010_consecutive_gap_downs_velocity(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_drv2_010_consecutive_gap_downs_velocity feature"""
    return _consecutive_count(open < close.shift(1)).diff(5)

def dstk_drv2_011_streak_climax_velocity_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_011_streak_climax_velocity_velocity feature"""
    d = _consecutive_count(close < close.shift(1))
    mx = d.rolling(252).max()
    v = np.log(close).diff(5).abs()
    score = _safe_div(d, mx) * v
    return score.diff(5)

def dstk_drv2_012_down_streak_power_index_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_012_down_streak_power_index_velocity feature"""
    d = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    freq = (ret < 0).rolling(63).mean()
    return (d * loss * freq).diff(5)

def dstk_drv2_013_consecutive_oversold_rsi_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_013_consecutive_oversold_rsi_velocity feature"""
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = delta.where(delta < 0, 0).abs().rolling(14).mean()
    rsi = 100 - (100 / (1 + _safe_div(gain, loss)))
    return _consecutive_count(rsi < 30).diff(5)

def dstk_drv2_014_streak_recovery_failure_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_014_streak_recovery_failure_velocity feature"""
    ret = close.pct_change()
    is_up = (ret > 0)
    up_streak_id = (is_up != is_up.shift()).cumsum()
    up_loss = np.exp(np.log(1 + ret).where(is_up, 0).groupby(up_streak_id).cumsum()) - 1
    failed_bounce = (is_up == False) & (is_up.shift(1) == True) & (up_loss.shift(1) < 0.01)
    return failed_bounce.rolling(63).sum().diff(5)

def dstk_drv2_015_streak_stability_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_015_streak_stability_velocity feature"""
    dur = _consecutive_count(close < close.shift(1))
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = dur.rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)

def dstk_drv2_016_consecutive_mktcap_down_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dstk_drv2_016_consecutive_mktcap_down_velocity feature"""
    mc = close * sharesbas
    return _consecutive_count(mc < mc.shift(1)).diff(5)

def dstk_drv2_017_consecutive_negative_surprise_velocity(surprise: pd.Series) -> pd.Series:
    """dstk_drv2_017_consecutive_negative_surprise_velocity feature"""
    return _consecutive_count(surprise < 0).diff(5)

def dstk_drv2_018_avg_loss_per_streak_day_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_018_avg_loss_per_streak_day_velocity feature"""
    dur = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    return _safe_div(loss, dur).diff(5)

def dstk_drv2_019_consecutive_days_under_vwap_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dstk_drv2_019_consecutive_days_under_vwap_velocity feature"""
    vwap = (close * volume).rolling(21).sum() / volume.rolling(21).sum()
    return _consecutive_count(close < vwap).diff(5)

def dstk_drv2_020_streak_duration_rank_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_020_streak_duration_rank_velocity feature"""
    dur = _consecutive_count(close < close.shift(1))
    rank = dur.expanding().rank(pct=True)
    return rank.diff(5)

def dstk_drv2_021_consecutive_days_under_ma20_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_021_consecutive_days_under_ma20_velocity feature"""
    ma = close.rolling(20).mean()
    return _consecutive_count(close < ma).diff(5)

def dstk_drv2_022_consecutive_days_outside_bollinger_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_022_consecutive_days_outside_bollinger_velocity feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    return _consecutive_count(close < ma - 2 * std).diff(5)

def dstk_drv2_023_consecutive_days_decreasing_range_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    """dstk_drv2_023_consecutive_days_decreasing_range_velocity feature"""
    r = high - low
    return _consecutive_count(r < r.shift(1)).diff(5)

def dstk_drv2_024_down_streak_entropy_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_024_down_streak_entropy_velocity feature"""
    counts = _consecutive_count(close < close.shift(1))
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y, bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = counts.rolling(63).apply(_ent, raw=True)
    return e.diff(5)

def dstk_drv2_025_decline_streak_final_composite_velocity(close: pd.Series) -> pd.Series:
    """dstk_drv2_025_decline_streak_final_composite_velocity feature"""
    d = _consecutive_count(close < close.shift(1))
    w_close = close.iloc[::5]
    w = _consecutive_count(w_close < w_close.shift(1)).reindex(close.index).ffill()
    m_close = close.iloc[::21]
    m = _consecutive_count(m_close < m_close.shift(1)).reindex(close.index).ffill()
    comp = (0.6 * d + 0.3 * w + 0.1 * m)
    return comp.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V08_V_REGISTRY = {
    "dstk_drv2_001_consecutive_down_days_velocity": {"inputs": ["close"], "func": dstk_drv2_001_consecutive_down_days_velocity},
    "dstk_drv2_002_cumulative_streak_loss_velocity": {"inputs": ["close"], "func": dstk_drv2_002_cumulative_streak_loss_velocity},
    "dstk_drv2_003_down_day_frequency_21d_velocity": {"inputs": ["close"], "func": dstk_drv2_003_down_day_frequency_21d_velocity},
    "dstk_drv2_004_streak_loss_zscore_velocity": {"inputs": ["close"], "func": dstk_drv2_004_streak_loss_zscore_velocity},
    "dstk_drv2_005_streak_acceleration_index_velocity": {"inputs": ["close"], "func": dstk_drv2_005_streak_acceleration_index_velocity},
    "dstk_drv2_006_days_since_last_up_day_velocity": {"inputs": ["close"], "func": dstk_drv2_006_days_since_last_up_day_velocity},
    "dstk_drv2_007_down_streak_intensity_velocity": {"inputs": ["close"], "func": dstk_drv2_007_down_streak_intensity_velocity},
    "dstk_drv2_008_streak_exhaustion_prob_velocity": {"inputs": ["close"], "func": dstk_drv2_008_streak_exhaustion_prob_velocity},
    "dstk_drv2_009_consecutive_red_candles_velocity": {"inputs": ["close", "open"], "func": dstk_drv2_009_consecutive_red_candles_velocity},
    "dstk_drv2_010_consecutive_gap_downs_velocity": {"inputs": ["close", "open"], "func": dstk_drv2_010_consecutive_gap_downs_velocity},
    "dstk_drv2_011_streak_climax_velocity_velocity": {"inputs": ["close"], "func": dstk_drv2_011_streak_climax_velocity_velocity},
    "dstk_drv2_012_down_streak_power_index_velocity": {"inputs": ["close"], "func": dstk_drv2_012_down_streak_power_index_velocity},
    "dstk_drv2_013_consecutive_oversold_rsi_velocity": {"inputs": ["close"], "func": dstk_drv2_013_consecutive_oversold_rsi_velocity},
    "dstk_drv2_014_streak_recovery_failure_velocity": {"inputs": ["close"], "func": dstk_drv2_014_streak_recovery_failure_velocity},
    "dstk_drv2_015_streak_stability_velocity": {"inputs": ["close"], "func": dstk_drv2_015_streak_stability_velocity},
    "dstk_drv2_016_consecutive_mktcap_down_velocity": {"inputs": ["close", "sharesbas"], "func": dstk_drv2_016_consecutive_mktcap_down_velocity},
    "dstk_drv2_017_consecutive_negative_surprise_velocity": {"inputs": ["surprise"], "func": dstk_drv2_017_consecutive_negative_surprise_velocity},
    "dstk_drv2_018_avg_loss_per_streak_day_velocity": {"inputs": ["close"], "func": dstk_drv2_018_avg_loss_per_streak_day_velocity},
    "dstk_drv2_019_consecutive_days_under_vwap_velocity": {"inputs": ["close", "volume"], "func": dstk_drv2_019_consecutive_days_under_vwap_velocity},
    "dstk_drv2_020_streak_duration_rank_velocity": {"inputs": ["close"], "func": dstk_drv2_020_streak_duration_rank_velocity},
    "dstk_drv2_021_consecutive_days_under_ma20_velocity": {"inputs": ["close"], "func": dstk_drv2_021_consecutive_days_under_ma20_velocity},
    "dstk_drv2_022_consecutive_days_outside_bollinger_velocity": {"inputs": ["close"], "func": dstk_drv2_022_consecutive_days_outside_bollinger_velocity},
    "dstk_drv2_023_consecutive_days_decreasing_range_velocity": {"inputs": ["high", "low"], "func": dstk_drv2_023_consecutive_days_decreasing_range_velocity},
    "dstk_drv2_024_down_streak_entropy_velocity": {"inputs": ["close"], "func": dstk_drv2_024_down_streak_entropy_velocity},
    "dstk_drv2_025_decline_streak_final_composite_velocity": {"inputs": ["close"], "func": dstk_drv2_025_decline_streak_final_composite_velocity},
}
