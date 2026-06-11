"""
Decline Streaks — 3rd Derivatives
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

def dstk_drv3_001_consecutive_down_days_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_001_consecutive_down_days_jerk feature"""
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    vel = dur.diff(5)
    return vel.diff(5)

def dstk_drv3_002_cumulative_streak_loss_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_002_cumulative_streak_loss_jerk feature"""
    ret = close.pct_change()
    is_down = (ret < 0)
    streak_id = (is_down != is_down.shift()).cumsum()
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby(streak_id).cumsum()) - 1).abs()
    vel = loss.diff(5)
    return vel.diff(5)

def dstk_drv3_003_down_day_frequency_21d_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_003_down_day_frequency_21d_jerk feature"""
    f = (close < close.shift(1)).rolling(21).mean()
    vel = f.diff(5)
    return vel.diff(5)

def dstk_drv3_004_streak_loss_zscore_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_004_streak_loss_zscore_jerk feature"""
    ret = close.pct_change()
    is_down = (ret < 0)
    loss = (np.exp(np.log(1 + ret).where(is_down, 0).groupby((is_down != is_down.shift()).cumsum()).cumsum()) - 1).abs()
    z = (loss - loss.rolling(252).mean()) / loss.rolling(252).std()
    vel = z.diff(5)
    return vel.diff(5)

def dstk_drv3_005_streak_acceleration_index_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_005_streak_acceleration_index_jerk feature"""
    f5 = (close < close.shift(1)).rolling(5).mean()
    f21 = (close < close.shift(1)).rolling(21).mean()
    idx = _safe_div(f5, f21)
    vel = idx.diff(5)
    return vel.diff(5)

def dstk_drv3_006_days_since_last_up_day_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_006_days_since_last_up_day_jerk feature"""
    is_up = (close > close.shift(1))
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_up).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - indices
    vel = dsl.diff(5)
    return vel.diff(5)

def dstk_drv3_007_down_streak_intensity_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_007_down_streak_intensity_jerk feature"""
    dur = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    vel = (dur * loss).diff(5)
    return vel.diff(5)

def dstk_drv3_008_streak_exhaustion_prob_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_008_streak_exhaustion_prob_jerk feature"""
    is_down = (close < close.shift(1))
    dur = _consecutive_count(is_down)
    def _prob(y):
        if len(y) == 0: return 0.0
        curr_dur = y[-1]
        if curr_dur == 0: return 0.0
        relevant = y[y >= curr_dur]
        ends = (relevant.shift(-1) == 0).sum()
        return ends / (len(relevant) + _EPS)
    p = dur.rolling(252).apply(_prob, raw=True)
    vel = p.diff(5)
    return vel.diff(5)

def dstk_drv3_009_consecutive_red_candles_jerk(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_drv3_009_consecutive_red_candles_jerk feature"""
    vel = _consecutive_count(close < open).diff(5)
    return vel.diff(5)

def dstk_drv3_010_consecutive_gap_downs_jerk(close: pd.Series, open: pd.Series) -> pd.Series:
    """dstk_drv3_010_consecutive_gap_downs_jerk feature"""
    vel = _consecutive_count(open < close.shift(1)).diff(5)
    return vel.diff(5)

def dstk_drv3_011_streak_climax_velocity_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_011_streak_climax_velocity_jerk feature"""
    d = _consecutive_count(close < close.shift(1))
    mx = d.rolling(252).max()
    v = np.log(close).diff(5).abs()
    score = _safe_div(d, mx) * v
    vel = score.diff(5)
    return vel.diff(5)

def dstk_drv3_012_down_streak_power_index_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_012_down_streak_power_index_jerk feature"""
    d = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    freq = (ret < 0).rolling(63).mean()
    vel = (d * loss * freq).diff(5)
    return vel.diff(5)

def dstk_drv3_013_consecutive_oversold_rsi_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_013_consecutive_oversold_rsi_jerk feature"""
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = delta.where(delta < 0, 0).abs().rolling(14).mean()
    rsi = 100 - (100 / (1 + _safe_div(gain, loss)))
    vel = _consecutive_count(rsi < 30).diff(5)
    return vel.diff(5)

def dstk_drv3_014_streak_recovery_failure_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_014_streak_recovery_failure_jerk feature"""
    ret = close.pct_change()
    is_up = (ret > 0)
    up_streak_id = (is_up != is_up.shift()).cumsum()
    up_loss = np.exp(np.log(1 + ret).where(is_up, 0).groupby(up_streak_id).cumsum()) - 1
    failed_bounce = (is_up == False) & (is_up.shift(1) == True) & (up_loss.shift(1) < 0.01)
    vel = failed_bounce.rolling(63).sum().diff(5)
    return vel.diff(5)

def dstk_drv3_015_streak_stability_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_015_streak_stability_jerk feature"""
    dur = _consecutive_count(close < close.shift(1))
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = dur.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)

def dstk_drv3_016_consecutive_mktcap_down_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dstk_drv3_016_consecutive_mktcap_down_jerk feature"""
    mc = close * sharesbas
    vel = _consecutive_count(mc < mc.shift(1)).diff(5)
    return vel.diff(5)

def dstk_drv3_017_consecutive_negative_surprise_jerk(surprise: pd.Series) -> pd.Series:
    """dstk_drv3_017_consecutive_negative_surprise_jerk feature"""
    vel = _consecutive_count(surprise < 0).diff(5)
    return vel.diff(5)

def dstk_drv3_018_avg_loss_per_streak_day_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_018_avg_loss_per_streak_day_jerk feature"""
    dur = _consecutive_count(close < close.shift(1))
    ret = close.pct_change()
    loss = (np.exp(np.log(1 + ret).where(ret < 0, 0).groupby((ret < 0).diff().ne(0).cumsum()).cumsum()) - 1).abs()
    vel = _safe_div(loss, dur).diff(5)
    return vel.diff(5)

def dstk_drv3_019_consecutive_days_under_vwap_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dstk_drv3_019_consecutive_days_under_vwap_jerk feature"""
    vwap = (close * volume).rolling(21).sum() / volume.rolling(21).sum()
    vel = _consecutive_count(close < vwap).diff(5)
    return vel.diff(5)

def dstk_drv3_020_streak_duration_rank_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_020_streak_duration_rank_jerk feature"""
    dur = _consecutive_count(close < close.shift(1))
    rank = dur.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)

def dstk_drv3_021_consecutive_days_under_ma20_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_021_consecutive_days_under_ma20_jerk feature"""
    ma = close.rolling(20).mean()
    vel = _consecutive_count(close < ma).diff(5)
    return vel.diff(5)

def dstk_drv3_022_consecutive_days_outside_bollinger_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_022_consecutive_days_outside_bollinger_jerk feature"""
    ma = close.rolling(20).mean()
    std = close.rolling(20).std()
    vel = _consecutive_count(close < ma - 2 * std).diff(5)
    return vel.diff(5)

def dstk_drv3_023_consecutive_days_decreasing_range_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    """dstk_drv3_023_consecutive_days_decreasing_range_jerk feature"""
    r = high - low
    vel = _consecutive_count(r < r.shift(1)).diff(5)
    return vel.diff(5)

def dstk_drv3_024_down_streak_entropy_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_024_down_streak_entropy_jerk feature"""
    counts = _consecutive_count(close < close.shift(1))
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y, bins=5, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = counts.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)

def dstk_drv3_025_decline_streak_final_composite_jerk(close: pd.Series) -> pd.Series:
    """dstk_drv3_025_decline_streak_final_composite_jerk feature"""
    d = _consecutive_count(close < close.shift(1))
    w_close = close.iloc[::5]
    w = _consecutive_count(w_close < w_close.shift(1)).reindex(close.index).ffill()
    m_close = close.iloc[::21]
    m = _consecutive_count(m_close < m_close.shift(1)).reindex(close.index).ffill()
    comp = (0.6 * d + 0.3 * w + 0.1 * m)
    vel = comp.diff(5)
    return vel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V08_A_REGISTRY = {
    "dstk_drv3_001_consecutive_down_days_jerk": {"inputs": ["close"], "func": dstk_drv3_001_consecutive_down_days_jerk},
    "dstk_drv3_002_cumulative_streak_loss_jerk": {"inputs": ["close"], "func": dstk_drv3_002_cumulative_streak_loss_jerk},
    "dstk_drv3_003_down_day_frequency_21d_jerk": {"inputs": ["close"], "func": dstk_drv3_003_down_day_frequency_21d_jerk},
    "dstk_drv3_004_streak_loss_zscore_jerk": {"inputs": ["close"], "func": dstk_drv3_004_streak_loss_zscore_jerk},
    "dstk_drv3_005_streak_acceleration_index_jerk": {"inputs": ["close"], "func": dstk_drv3_005_streak_acceleration_index_jerk},
    "dstk_drv3_006_days_since_last_up_day_jerk": {"inputs": ["close"], "func": dstk_drv3_006_days_since_last_up_day_jerk},
    "dstk_drv3_007_down_streak_intensity_jerk": {"inputs": ["close"], "func": dstk_drv3_007_down_streak_intensity_jerk},
    "dstk_drv3_008_streak_exhaustion_prob_jerk": {"inputs": ["close"], "func": dstk_drv3_008_streak_exhaustion_prob_jerk},
    "dstk_drv3_009_consecutive_red_candles_jerk": {"inputs": ["close", "open"], "func": dstk_drv3_009_consecutive_red_candles_jerk},
    "dstk_drv3_010_consecutive_gap_downs_jerk": {"inputs": ["close", "open"], "func": dstk_drv3_010_consecutive_gap_downs_jerk},
    "dstk_drv3_011_streak_climax_velocity_jerk": {"inputs": ["close"], "func": dstk_drv3_011_streak_climax_velocity_jerk},
    "dstk_drv3_012_down_streak_power_index_jerk": {"inputs": ["close"], "func": dstk_drv3_012_down_streak_power_index_jerk},
    "dstk_drv3_013_consecutive_oversold_rsi_jerk": {"inputs": ["close"], "func": dstk_drv3_013_consecutive_oversold_rsi_jerk},
    "dstk_drv3_014_streak_recovery_failure_jerk": {"inputs": ["close"], "func": dstk_drv3_014_streak_recovery_failure_jerk},
    "dstk_drv3_015_streak_stability_jerk": {"inputs": ["close"], "func": dstk_drv3_015_streak_stability_jerk},
    "dstk_drv3_016_consecutive_mktcap_down_jerk": {"inputs": ["close", "sharesbas"], "func": dstk_drv3_016_consecutive_mktcap_down_jerk},
    "dstk_drv3_017_consecutive_negative_surprise_jerk": {"inputs": ["surprise"], "func": dstk_drv3_017_consecutive_negative_surprise_jerk},
    "dstk_drv3_018_avg_loss_per_streak_day_jerk": {"inputs": ["close"], "func": dstk_drv3_018_avg_loss_per_streak_day_jerk},
    "dstk_drv3_019_consecutive_days_under_vwap_jerk": {"inputs": ["close", "volume"], "func": dstk_drv3_019_consecutive_days_under_vwap_jerk},
    "dstk_drv3_020_streak_duration_rank_jerk": {"inputs": ["close"], "func": dstk_drv3_020_streak_duration_rank_jerk},
    "dstk_drv3_021_consecutive_days_under_ma20_jerk": {"inputs": ["close"], "func": dstk_drv3_021_consecutive_days_under_ma20_jerk},
    "dstk_drv3_022_consecutive_days_outside_bollinger_jerk": {"inputs": ["close"], "func": dstk_drv3_022_consecutive_days_outside_bollinger_jerk},
    "dstk_drv3_023_consecutive_days_decreasing_range_jerk": {"inputs": ["high", "low"], "func": dstk_drv3_023_consecutive_days_decreasing_range_jerk},
    "dstk_drv3_024_down_streak_entropy_jerk": {"inputs": ["close"], "func": dstk_drv3_024_down_streak_entropy_jerk},
    "dstk_drv3_025_decline_streak_final_composite_jerk": {"inputs": ["close"], "func": dstk_drv3_025_decline_streak_final_composite_jerk},
}
