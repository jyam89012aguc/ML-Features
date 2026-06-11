"""island_reversal_gap_dynamics base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the gap / island-reversal theme: largest-gap
statistics, gap rank in distribution, gap acceleration/regime, gap location in
range context, overnight-vs-intraday return decomposition, reversal-after-gap
rate, gap streaks, gap volume signatures, filled/unfilled gap mix, net unfilled
gap stack, close-strength on gap days, multi-bar post-gap effects, gap size
scaling with vol, and composite gap signature scores.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---- family-specific helpers (PIT-clean) ----

def _up_gap_bool(high, low):
    return low > high.shift(1)


def _down_gap_bool(high, low):
    return high < low.shift(1)


def _up_gap_size(high, low):
    return (low - high.shift(1)).where(_up_gap_bool(high, low), np.nan)


def _down_gap_size(high, low):
    return (low.shift(1) - high).where(_down_gap_bool(high, low), np.nan)


def _bars_since_event(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last_idx = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last_idx


def _streak(condition):
    grp = (~condition).cumsum()
    return condition.astype(int).groupby(grp).cumsum().astype(float)


# ============================================================
# Bucket L — Largest gap statistics in windows (076-084)
# ============================================================

def f09_irgd_076_largest_up_gap_atr_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest ATR-normalized up-gap size in trailing 21 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr)
    return sz.rolling(MDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_077_largest_up_gap_atr_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest ATR-normalized up-gap size in trailing 63 bars — quarterly extreme."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr)
    return sz.rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_078_largest_up_gap_atr_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest ATR-normalized up-gap size in trailing 252 bars — annual extreme."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr)
    return sz.rolling(YDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_079_largest_down_gap_atr_in_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest ATR-normalized down-gap size in trailing 63 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_down_gap_size(high, low), atr)
    return sz.rolling(QDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_080_largest_down_gap_atr_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest ATR-normalized down-gap size in trailing 252 bars."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_down_gap_size(high, low), atr)
    return sz.rolling(YDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_081_largest_gap_either_log_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest |log gap size| (either direction) in trailing 252 bars."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0)
    abs_log = up_log.abs() + dn_log.abs()  # at most one is non-zero on a given bar
    return abs_log.rolling(YDAYS, min_periods=1).max().fillna(0.0)


def f09_irgd_082_bars_since_largest_up_gap_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the bar with largest ATR-normalized up-gap in trailing 252d."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr).fillna(0.0)
    def _argmax_offset(w):
        if np.isnan(w).all(): return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return sz.rolling(YDAYS, min_periods=QDAYS).apply(_argmax_offset, raw=True)


def f09_irgd_083_largest_gap_zscore_in_252d_window(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of largest up-gap log size in 252d vs trailing-252d distribution of (non-zero) gap log sizes."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    largest = log_sz.rolling(YDAYS, min_periods=QDAYS).max()
    mean = log_sz.rolling(YDAYS, min_periods=QDAYS).mean()
    std = log_sz.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(largest - mean, std)


def f09_irgd_084_largest_gap_pct_in_252d_window(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest raw-% up-gap size in 252d window."""
    pct_sz = _safe_div(_up_gap_size(high, low), high.shift(1))
    return pct_sz.rolling(YDAYS, min_periods=1).max().fillna(0.0)


# ============================================================
# Bucket M — Gap rank / distribution position (085-089)
# ============================================================

def f09_irgd_085_most_recent_up_gap_size_rank_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of most-recent up-gap log size against trailing 252d distribution of up-gap log sizes."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    last_sz = log_sz.ffill()
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return last_sz.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f09_irgd_086_most_recent_up_gap_size_rank_in_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of most-recent up-gap log size in trailing 5y of gap log sizes."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    last_sz = log_sz.ffill()
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return last_sz.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)


def f09_irgd_087_most_recent_down_gap_size_rank_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of most-recent down-gap log size."""
    log_sz = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), np.nan)
    last_sz = log_sz.ffill()
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return last_sz.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f09_irgd_088_most_recent_gap_zscore_vs_252d_history(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of most-recent up-gap log size against trailing 252d distribution of up-gap log sizes."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    last_sz = log_sz.ffill()
    mean = log_sz.rolling(YDAYS, min_periods=QDAYS).mean()
    std = log_sz.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(last_sz - mean, std)


def f09_irgd_089_gap_size_distribution_skew_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of (signed) gap log sizes (up positive, down negative, no-gap = 0) in trailing 252 bars."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0)
    signed = up_log - dn_log
    return signed.rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket N — Gap acceleration / regime (090-094)
# ============================================================

def f09_irgd_090_gap_size_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Linear-regression slope of up-gap log sizes over trailing 252 bars (NaN gaps treated as 0)."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    return _rolling_slope(log_sz, YDAYS, min_periods=QDAYS)


def f09_irgd_091_gap_size_velocity_recent_minus_prior(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean(last 21 up-gap log sizes) - mean(prior 21 up-gap log sizes from 42d back)."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    recent = log_sz.rolling(MDAYS, min_periods=WDAYS).mean()
    prior = log_sz.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).mean()
    return recent - prior


def f09_irgd_092_gap_count_acceleration_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Up-gap count in last 63d minus prior 63d (lagged by 63d)."""
    up = _up_gap_bool(high, low).astype(float)
    last = up.rolling(QDAYS, min_periods=MDAYS).sum()
    prior = last.shift(QDAYS)
    return last - prior


def f09_irgd_093_gap_intensity_regime_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: count of up-gaps in last 21d > 2x trailing-252d mean rate per 21d window."""
    up = _up_gap_bool(high, low).astype(float)
    cnt21 = up.rolling(MDAYS, min_periods=WDAYS).sum()
    mean_rate = up.rolling(YDAYS, min_periods=QDAYS).mean() * MDAYS
    return (cnt21 > 2.0 * mean_rate).astype(float)


def f09_irgd_094_gap_clustering_indicator_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: >= 2 up-gap events within last 5 bars — clustered gap activity."""
    up = _up_gap_bool(high, low).astype(float)
    return (up.rolling(WDAYS, min_periods=1).sum() >= 2.0).astype(float)


# ============================================================
# Bucket O — Gap location in range / context (095-100)
# ============================================================

def f09_irgd_095_most_recent_up_gap_close_position_in_252d_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position in 252d range on most-recent up-gap day (0=at 252d low, 1=at 252d high)."""
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    return pos.where(_up_gap_bool(high, low), np.nan).ffill()


def f09_irgd_096_most_recent_up_gap_distance_above_63d_ma_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance of close above 63d SMA on most-recent up-gap day."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    d = _safe_div(close - sma, atr)
    return d.where(_up_gap_bool(high, low), np.nan).ffill()


def f09_irgd_097_most_recent_up_gap_distance_above_252d_ma_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance of close above 252d SMA on most-recent up-gap day."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    d = _safe_div(close - sma, atr)
    return d.where(_up_gap_bool(high, low), np.nan).ffill()


def f09_irgd_098_pct_of_gaps_252d_near_52w_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of up-gaps in last 252d that occurred within 5% of the trailing 252d high at the time of gap."""
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * hi252
    gap_and_near = (_up_gap_bool(high, low) & near).astype(float)
    gap_total = _up_gap_bool(high, low).astype(float)
    return _safe_div(gap_and_near.rolling(YDAYS, min_periods=QDAYS).sum(), gap_total.rolling(YDAYS, min_periods=QDAYS).sum())


def f09_irgd_099_pct_of_gaps_252d_in_top_decile_of_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of up-gaps in 252d occurring while close in top decile of 252d range."""
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    g_in = (_up_gap_bool(high, low) & in_top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    g_tot = _up_gap_bool(high, low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(g_in, g_tot)


def f09_irgd_100_most_recent_up_gap_zone_above_or_below_63d_ma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 1 if most-recent up-gap day had close > 63d SMA, 0 if below. Sticky between gap events."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    z = (close > sma).astype(float)
    return z.where(_up_gap_bool(high, low), np.nan).ffill()


# ============================================================
# Bucket P — Overnight vs intraday return decomposition (101-107)
# ============================================================

def f09_irgd_101_cum_overnight_log_return_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight log returns (log(open[i]) - log(close[i-1])) in last 21 bars."""
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    return overnight.rolling(MDAYS, min_periods=WDAYS).sum()


def f09_irgd_102_cum_overnight_log_return_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight log returns in last 63 bars."""
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    return overnight.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_103_cum_overnight_log_return_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight log returns in last 252 bars."""
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    return overnight.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_104_cum_intraday_log_return_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of intraday log returns (log(close) - log(open)) in last 63 bars."""
    intraday = _safe_log(close) - _safe_log(open_)
    return intraday.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_irgd_105_overnight_minus_intraday_balance_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d overnight return sum minus intraday return sum — where returns are happening."""
    overnight = (_safe_log(open_) - _safe_log(close.shift(1))).rolling(QDAYS, min_periods=MDAYS).sum()
    intraday = (_safe_log(close) - _safe_log(open_)).rolling(QDAYS, min_periods=MDAYS).sum()
    return overnight - intraday


def f09_irgd_106_overnight_log_return_zscore_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's overnight log return against trailing 252d distribution."""
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    return _rolling_zscore(overnight, YDAYS, min_periods=QDAYS)


def f09_irgd_107_gap_to_overnight_ratio_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: count of full gap days / count of |overnight return| > 1% in trailing 252d."""
    full_gap = (_up_gap_bool(high, low) | _down_gap_bool(high, low)).astype(float)
    overnight_abs = (_safe_log(open_) - _safe_log(close.shift(1))).abs()
    large_overnight = (overnight_abs > 0.01).astype(float)
    return _safe_div(full_gap.rolling(YDAYS, min_periods=QDAYS).sum(), large_overnight.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
# Bucket Q — Reversal-after-gap-up rate (108-112)
# ============================================================

def f09_irgd_108_reversal_after_gap_up_rate_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of gap-up days in last 63d that closed below open — bearish followthrough rate."""
    rev = (_up_gap_bool(high, low) & (close < open_)).astype(float)
    tot = _up_gap_bool(high, low).astype(float)
    return _safe_div(rev.rolling(QDAYS, min_periods=MDAYS).sum(), tot.rolling(QDAYS, min_periods=MDAYS).sum())


def f09_irgd_109_reversal_after_gap_up_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reversal rate over 252d window."""
    rev = (_up_gap_bool(high, low) & (close < open_)).astype(float)
    tot = _up_gap_bool(high, low).astype(float)
    return _safe_div(rev.rolling(YDAYS, min_periods=QDAYS).sum(), tot.rolling(YDAYS, min_periods=QDAYS).sum())


def f09_irgd_110_mean_close_minus_open_atr_after_gap_up_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR-normalized (close - open) on gap-up days in last 63d. Negative = bearish reversal regime."""
    atr = _atr(high, low, close, n=MDAYS)
    intra = _safe_div(close - open_, atr).where(_up_gap_bool(high, low), np.nan)
    return intra.rolling(QDAYS, min_periods=MDAYS).mean()


def f09_irgd_111_median_close_minus_open_atr_after_gap_up_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median ATR-normalized (close - open) on gap-up days in last 252d."""
    atr = _atr(high, low, close, n=MDAYS)
    intra = _safe_div(close - open_, atr).where(_up_gap_bool(high, low), np.nan)
    return intra.rolling(YDAYS, min_periods=QDAYS).median()


def f09_irgd_112_followthrough_after_gap_up_rate_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of gap-up days that closed > open (bullish followthrough)."""
    ft = (_up_gap_bool(high, low) & (close > open_)).astype(float)
    tot = _up_gap_bool(high, low).astype(float)
    return _safe_div(ft.rolling(YDAYS, min_periods=QDAYS).sum(), tot.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
# Bucket R — Gap streaks (113-115)
# ============================================================

def f09_irgd_113_consecutive_up_gap_days_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current run of consecutive up-gap days."""
    cond = _up_gap_bool(high, low).fillna(False)
    return _streak(cond)


def f09_irgd_114_consecutive_down_gap_days_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current run of consecutive down-gap days."""
    cond = _down_gap_bool(high, low).fillna(False)
    return _streak(cond)


def f09_irgd_115_max_consecutive_up_gap_days_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest consecutive up-gap-day streak length seen in trailing 252 bars."""
    cond = _up_gap_bool(high, low).fillna(False)
    streak = _streak(cond)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket S — Volume signature on gap day (116-121)
# ============================================================

def f09_irgd_116_most_recent_up_gap_volume_zscore_in_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on most-recent up-gap day vs trailing 63d volume."""
    vz = _rolling_zscore(volume, QDAYS, min_periods=MDAYS)
    return vz.where(_up_gap_bool(high, low), np.nan).ffill()


def f09_irgd_117_most_recent_up_gap_volume_zscore_in_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on most-recent up-gap day vs trailing 252d volume."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return vz.where(_up_gap_bool(high, low), np.nan).ffill()


def f09_irgd_118_mean_volume_zscore_gap_up_days_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume z-score across all gap-up days in trailing 252d."""
    vz = _rolling_zscore(volume, QDAYS, min_periods=MDAYS)
    return vz.where(_up_gap_bool(high, low), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f09_irgd_119_largest_up_gap_volume_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of the volume on the largest-up-gap-day in trailing 252d, vs full 252d volume distribution."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr).fillna(-np.inf)
    # For each bar i: find the bar j in last 252d with max sz, take volume[j], compute its percentile rank in last 252d volume.
    n = len(high)
    sz_arr = sz.to_numpy()
    vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_sz = sz_arr[start:i + 1]
        win_vol = vol_arr[start:i + 1]
        if win_sz.size == 0: continue
        valid_mask = ~np.isinf(win_sz)
        if not valid_mask.any(): continue
        idx_max = int(np.argmax(win_sz))
        if np.isinf(win_sz[idx_max]): continue
        v = win_vol[idx_max]
        if np.isnan(v): continue
        valid_vol = win_vol[~np.isnan(win_vol)]
        if valid_vol.size == 0: continue
        out[i] = float((valid_vol <= v).sum()) / float(valid_vol.size)
    return pd.Series(out, index=high.index)


def f09_irgd_120_volume_decline_after_gap_up_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """For most-recent up-gap day (in last 63d): ratio of mean volume in next 5 bars / volume on gap day."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy()
    vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j >= n: continue
        gap_vol = vol_arr[j]
        if np.isnan(gap_vol) or gap_vol == 0: continue
        post = vol_arr[j + 1:min(n, j + 1 + WDAYS)]
        if post.size == 0: continue
        out[i] = float(np.nanmean(post) / gap_vol)
    return pd.Series(out, index=high.index)


def f09_irgd_121_gap_up_with_low_volume_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: up-gap on a day where volume is below 21d trailing average — failed-conviction gap."""
    vavg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_up_gap_bool(high, low) & (volume < vavg)).astype(float)


# ============================================================
# Bucket T — Filled vs unfilled gap mix (122-125)
# ============================================================

def _pct_gaps_filled_within(high, low, fill_horizon, count_horizon, direction='up'):
    """Fraction of up-gaps (or down-gaps) that occurred AT LEAST `fill_horizon` bars ago and were
    filled within `fill_horizon` bars, against total gaps occurring more than `fill_horizon` ago in trailing `count_horizon`."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - count_horizon)
        end_for_gap = i - fill_horizon
        total = 0; filled = 0
        for k in range(start + 1, end_for_gap + 1):
            if direction == 'up':
                if not (low_arr[k] > high_arr[k - 1]): continue
                gap_floor = high_arr[k - 1]
                window = low_arr[k + 1:k + 1 + fill_horizon]
                total += 1
                if np.any(window <= gap_floor): filled += 1
            else:
                if not (high_arr[k] < low_arr[k - 1]): continue
                gap_ceil = low_arr[k - 1]
                window = high_arr[k + 1:k + 1 + fill_horizon]
                total += 1
                if np.any(window >= gap_ceil): filled += 1
        if total > 0:
            out[i] = float(filled) / float(total)
    return pd.Series(out, index=high.index)


def f09_irgd_122_pct_up_gaps_filled_within_5d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d up-gaps that were filled within 5 bars."""
    return _pct_gaps_filled_within(high, low, fill_horizon=WDAYS, count_horizon=YDAYS, direction='up')


def f09_irgd_123_pct_up_gaps_filled_within_21d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d up-gaps filled within 21 bars."""
    return _pct_gaps_filled_within(high, low, fill_horizon=MDAYS, count_horizon=YDAYS, direction='up')


def f09_irgd_124_pct_up_gaps_filled_within_63d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d up-gaps filled within 63 bars."""
    return _pct_gaps_filled_within(high, low, fill_horizon=QDAYS, count_horizon=YDAYS, direction='up')


def f09_irgd_125_pct_down_gaps_filled_within_21d_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d down-gaps filled within 21 bars."""
    return _pct_gaps_filled_within(high, low, fill_horizon=MDAYS, count_horizon=YDAYS, direction='down')


# ============================================================
# Bucket U — Net unfilled gap stack (126-130)
# ============================================================

def _unfilled_gap_log_size_total(high, low, direction, horizon):
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - horizon)
        total = 0.0
        for k in range(start + 1, i + 1):
            if direction == 'up':
                if not (low_arr[k] > high_arr[k - 1]): continue
                gap_floor = high_arr[k - 1]
                if i >= k + 1:
                    if np.any(low_arr[k + 1:i + 1] <= gap_floor): continue
                if gap_floor > 0 and low_arr[k] > 0:
                    total += np.log(low_arr[k] / gap_floor)
            else:
                if not (high_arr[k] < low_arr[k - 1]): continue
                gap_ceil = low_arr[k - 1]
                if i >= k + 1:
                    if np.any(high_arr[k + 1:i + 1] >= gap_ceil): continue
                if gap_ceil > 0 and high_arr[k] > 0:
                    total += np.log(gap_ceil / high_arr[k])
        out[i] = total
    return pd.Series(out, index=high.index)


def f09_irgd_126_total_unfilled_up_gap_log_size_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of log-sizes of all unfilled up-gaps in trailing 252d — accumulated supply void above price."""
    return _unfilled_gap_log_size_total(high, low, direction='up', horizon=YDAYS)


def f09_irgd_127_total_unfilled_down_gap_log_size_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of log-sizes of all unfilled down-gaps in trailing 252d."""
    return _unfilled_gap_log_size_total(high, low, direction='down', horizon=YDAYS)


def f09_irgd_128_net_unfilled_gap_balance_log_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum unfilled-up minus unfilled-down log sizes — net structural imbalance."""
    up = _unfilled_gap_log_size_total(high, low, direction='up', horizon=YDAYS)
    dn = _unfilled_gap_log_size_total(high, low, direction='down', horizon=YDAYS)
    return up - dn


def f09_irgd_129_bars_since_oldest_unfilled_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the oldest still-unfilled up-gap in trailing 252d."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        oldest = np.nan
        for k in range(start + 1, i + 1):
            if not (low_arr[k] > high_arr[k - 1]): continue
            gap_floor = high_arr[k - 1]
            if i >= k + 1:
                if np.any(low_arr[k + 1:i + 1] <= gap_floor): continue
            age = float(i - k)
            if np.isnan(oldest) or age > oldest: oldest = age
        out[i] = oldest
    return pd.Series(out, index=high.index)


def f09_irgd_130_unfilled_gap_stack_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of distinct unfilled up-gaps + unfilled down-gaps in trailing 252d (total stack depth)."""
    n = len(high)
    high_arr = high.to_numpy()
    low_arr = low.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS)
        cnt = 0
        for k in range(start + 1, i + 1):
            up = low_arr[k] > high_arr[k - 1]
            dn = high_arr[k] < low_arr[k - 1]
            if up:
                gap_floor = high_arr[k - 1]
                if i < k + 1 or not np.any(low_arr[k + 1:i + 1] <= gap_floor):
                    cnt += 1
            if dn:
                gap_ceil = low_arr[k - 1]
                if i < k + 1 or not np.any(high_arr[k + 1:i + 1] >= gap_ceil):
                    cnt += 1
        out[i] = float(cnt)
    return pd.Series(out, index=high.index)


# ============================================================
# Bucket V — Gap close-strength indicators (131-135)
# ============================================================

def f09_irgd_131_gap_up_with_strong_close_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up AND close position in intraday range >= 0.8 — strong-close gap-up."""
    pos = _safe_div(close - low, high - low)
    return (_up_gap_bool(high, low) & (pos >= 0.8)).astype(float)


def f09_irgd_132_gap_up_with_weak_close_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up AND close position in intraday range <= 0.2 — weak-close gap-up (bearish)."""
    pos = _safe_div(close - low, high - low)
    return (_up_gap_bool(high, low) & (pos <= 0.2)).astype(float)


def f09_irgd_133_count_strong_close_gap_ups_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of strong-close gap-up events in last 252 bars."""
    pos = _safe_div(close - low, high - low)
    ev = (_up_gap_bool(high, low) & (pos >= 0.8)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_134_count_weak_close_gap_ups_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of weak-close gap-up events in last 252 bars."""
    pos = _safe_div(close - low, high - low)
    ev = (_up_gap_bool(high, low) & (pos <= 0.2)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f09_irgd_135_strong_minus_weak_close_gap_balance_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Strong-close count minus weak-close count of gap-ups in last 252d — close-strength regime."""
    pos = _safe_div(close - low, high - low)
    strong = (_up_gap_bool(high, low) & (pos >= 0.8)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    weak = (_up_gap_bool(high, low) & (pos <= 0.2)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return strong - weak


# ============================================================
# Bucket W — Multi-bar post-gap effects (136-140)
# ============================================================

def f09_irgd_136_5d_log_return_after_most_recent_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap (≥5 bars ago, within 63d): log return over 5 bars after gap day."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy()
    close_arr = close.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        c0 = close_arr[j]; c5 = close_arr[j + WDAYS]
        if np.isnan(c0) or np.isnan(c5) or c0 <= 0 or c5 <= 0: continue
        out[i] = float(np.log(c5 / c0))
    return pd.Series(out, index=close.index)


def f09_irgd_137_21d_log_return_after_most_recent_up_gap(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap (≥21 bars ago, within 252d): log return over 21 bars after gap day."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy()
    close_arr = close.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < MDAYS or b > YDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + MDAYS >= n: continue
        c0 = close_arr[j]; cM = close_arr[j + MDAYS]
        if np.isnan(c0) or np.isnan(cM) or c0 <= 0 or cM <= 0: continue
        out[i] = float(np.log(cM / c0))
    return pd.Series(out, index=close.index)


def f09_irgd_138_5d_high_excess_after_most_recent_up_gap_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap (≥5 bars ago, within 63d): (max high in next 5 bars - close on gap day) / ATR."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    atr_s = _atr(high, low, close, n=MDAYS)
    n = len(high)
    bsu_arr = bsu.to_numpy()
    high_arr = high.to_numpy()
    close_arr = close.to_numpy()
    atr_arr = atr_s.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        max_hi = np.nanmax(high_arr[j + 1:j + 1 + WDAYS])
        c0 = close_arr[j]; a = atr_arr[j]
        if np.isnan(max_hi) or np.isnan(c0) or np.isnan(a) or a == 0: continue
        out[i] = float((max_hi - c0) / a)
    return pd.Series(out, index=close.index)


def f09_irgd_139_5d_low_breakdown_after_most_recent_up_gap_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap day: (low on gap day - min low in next 5 bars) / ATR (positive = breakdown below)."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    atr_s = _atr(high, low, close, n=MDAYS)
    n = len(high)
    bsu_arr = bsu.to_numpy()
    low_arr = low.to_numpy()
    atr_arr = atr_s.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        min_lo = np.nanmin(low_arr[j + 1:j + 1 + WDAYS])
        l0 = low_arr[j]; a = atr_arr[j]
        if np.isnan(min_lo) or np.isnan(l0) or np.isnan(a) or a == 0: continue
        out[i] = float((l0 - min_lo) / a)
    return pd.Series(out, index=close.index)


def f09_irgd_140_post_gap_up_5d_max_drawdown_pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """For most-recent up-gap day: max % drawdown of close in next 5 bars from gap-day close."""
    bsu = _bars_since_event(_up_gap_bool(high, low).fillna(False))
    n = len(high)
    bsu_arr = bsu.to_numpy()
    close_arr = close.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        b = bsu_arr[i]
        if np.isnan(b) or b < WDAYS or b > QDAYS: continue
        j = int(i - int(b))
        if j < 0 or j + WDAYS >= n: continue
        c0 = close_arr[j]
        post = close_arr[j + 1:j + 1 + WDAYS]
        if c0 <= 0 or np.isnan(c0) or post.size == 0 or np.all(np.isnan(post)): continue
        dd = float(np.nanmin(post / c0) - 1.0)
        out[i] = dd
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket X — Gap size scaling with volatility (141-146)
# ============================================================

def f09_irgd_141_gap_size_atr_normalized_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ATR-normalized up-gap size (today) against trailing-252d distribution of same metric."""
    atr = _atr(high, low, close, n=MDAYS)
    sz = _safe_div(_up_gap_size(high, low), atr)
    return _rolling_zscore(sz.ffill(), YDAYS, min_periods=QDAYS)


def f09_irgd_142_gap_size_log_normalized_by_realized_vol_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent up-gap log size / 252d realized log-vol."""
    log_sz = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan).ffill()
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(log_sz, sigma)


def f09_irgd_143_gap_signal_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |gap log size| / sum of |daily log return| in last 252d — fraction of total motion that is gap-driven."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0).abs()
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0).abs()
    total_gap = (up_log + dn_log).rolling(YDAYS, min_periods=QDAYS).sum()
    total_ret = _safe_log(close).diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(total_gap, total_ret)


def f09_irgd_144_gap_intensity_index_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |gap log size| in last 63d normalized by 63d realized vol (annualized)."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0).abs()
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0).abs()
    total_gap = (up_log + dn_log).rolling(QDAYS, min_periods=MDAYS).sum()
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=MDAYS).std() * np.sqrt(252.0)
    return _safe_div(total_gap, sigma)


def f09_irgd_145_gap_to_range_ratio_most_recent(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Most-recent up-gap log size / log true-range of that bar — fraction of the bar's motion that was the gap."""
    log_gap = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), np.nan)
    tr = _true_range(high, low, close)
    log_tr = _safe_log(close + tr) - _safe_log(close.where(close > 0, np.nan))
    last_gap = log_gap.ffill()
    last_log_tr = log_tr.where(_up_gap_bool(high, low), np.nan).ffill()
    return _safe_div(last_gap, last_log_tr)


def f09_irgd_146_gap_distribution_kurtosis_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Excess kurtosis of signed gap log size distribution in last 252d."""
    up_log = (_safe_log(low) - _safe_log(high.shift(1))).where(_up_gap_bool(high, low), 0.0)
    dn_log = (_safe_log(low.shift(1)) - _safe_log(high)).where(_down_gap_bool(high, low), 0.0)
    signed = up_log - dn_log
    return signed.rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket Y — Composite gap signature (147-150)
# ============================================================

def f09_irgd_147_terminal_gap_signature_score_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite score in last 252d: (exhaustion-gap count) + 2*(close-reversal gap count) + 3*(unfilled stack count proxy via cnt up-gap not in last 21d).
    Weighted top-of-trend signature."""
    sma252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above60 = (close > sma252).rolling(60, min_periods=20).sum() >= 60
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    exh = (_up_gap_bool(high, low) & above60 & in_top).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rev = (_up_gap_bool(high, low) & (close < open_)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    old_gap_proxy = _up_gap_bool(high, low).astype(float).shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return exh + 2.0 * rev + 3.0 * old_gap_proxy


def f09_irgd_148_gap_failure_score_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite score: (reversal-after-gap-up rate) * (count of up-gaps in 252d) — weighted failure tally."""
    rev = (_up_gap_bool(high, low) & (close < open_)).astype(float)
    tot = _up_gap_bool(high, low).astype(float)
    rate = _safe_div(rev.rolling(YDAYS, min_periods=QDAYS).sum(), tot.rolling(YDAYS, min_periods=QDAYS).sum())
    cnt = tot.rolling(YDAYS, min_periods=QDAYS).sum()
    return rate * cnt


def f09_irgd_149_gap_top_signature_composite_indicator(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: at least 1 large up-gap (>1 ATR) in last 5d AND price in top decile of 252d range AND weak close (pos<=0.4 in intraday range) on the gap day."""
    atr = _atr(high, low, close, n=MDAYS)
    big = (_up_gap_size(high, low) > atr).fillna(False)
    big_recent = big.rolling(WDAYS, min_periods=1).sum() >= 1
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = pos >= 0.9
    pos_intraday = _safe_div(close - low, high - low)
    weak = (pos_intraday <= 0.4).where(big, False)
    weak_recent = weak.fillna(False).rolling(WDAYS, min_periods=1).sum() >= 1
    return (big_recent & in_top & weak_recent).astype(float)


def f09_irgd_150_gap_pattern_diversity_index_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy over {up_gap, down_gap, no_gap} states in last 252d."""
    upg = _up_gap_bool(high, low).astype(float)
    dng = _down_gap_bool(high, low).astype(float)
    p_up = upg.rolling(YDAYS, min_periods=QDAYS).mean()
    p_dn = dng.rolling(YDAYS, min_periods=QDAYS).mean()
    p_no = (1.0 - p_up - p_dn).clip(lower=1e-9)
    p_up_c = p_up.clip(lower=1e-9); p_dn_c = p_dn.clip(lower=1e-9)
    h = -(p_up_c * np.log(p_up_c) + p_dn_c * np.log(p_dn_c) + p_no * np.log(p_no))
    return h


# ============================================================
#                         REGISTRY 076-150
# ============================================================

ISLAND_REVERSAL_GAP_DYNAMICS_BASE_REGISTRY_076_150 = {
    "f09_irgd_076_largest_up_gap_atr_in_21d": {"inputs": ["high", "low", "close"], "func": f09_irgd_076_largest_up_gap_atr_in_21d},
    "f09_irgd_077_largest_up_gap_atr_in_63d": {"inputs": ["high", "low", "close"], "func": f09_irgd_077_largest_up_gap_atr_in_63d},
    "f09_irgd_078_largest_up_gap_atr_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_078_largest_up_gap_atr_in_252d},
    "f09_irgd_079_largest_down_gap_atr_in_63d": {"inputs": ["high", "low", "close"], "func": f09_irgd_079_largest_down_gap_atr_in_63d},
    "f09_irgd_080_largest_down_gap_atr_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_080_largest_down_gap_atr_in_252d},
    "f09_irgd_081_largest_gap_either_log_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_081_largest_gap_either_log_in_252d},
    "f09_irgd_082_bars_since_largest_up_gap_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_082_bars_since_largest_up_gap_in_252d},
    "f09_irgd_083_largest_gap_zscore_in_252d_window": {"inputs": ["high", "low", "close"], "func": f09_irgd_083_largest_gap_zscore_in_252d_window},
    "f09_irgd_084_largest_gap_pct_in_252d_window": {"inputs": ["high", "low", "close"], "func": f09_irgd_084_largest_gap_pct_in_252d_window},
    "f09_irgd_085_most_recent_up_gap_size_rank_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_085_most_recent_up_gap_size_rank_in_252d},
    "f09_irgd_086_most_recent_up_gap_size_rank_in_1260d": {"inputs": ["high", "low", "close"], "func": f09_irgd_086_most_recent_up_gap_size_rank_in_1260d},
    "f09_irgd_087_most_recent_down_gap_size_rank_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_087_most_recent_down_gap_size_rank_in_252d},
    "f09_irgd_088_most_recent_gap_zscore_vs_252d_history": {"inputs": ["high", "low", "close"], "func": f09_irgd_088_most_recent_gap_zscore_vs_252d_history},
    "f09_irgd_089_gap_size_distribution_skew_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_089_gap_size_distribution_skew_252d},
    "f09_irgd_090_gap_size_slope_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_090_gap_size_slope_252d},
    "f09_irgd_091_gap_size_velocity_recent_minus_prior": {"inputs": ["high", "low", "close"], "func": f09_irgd_091_gap_size_velocity_recent_minus_prior},
    "f09_irgd_092_gap_count_acceleration_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_092_gap_count_acceleration_252d},
    "f09_irgd_093_gap_intensity_regime_indicator": {"inputs": ["high", "low", "close"], "func": f09_irgd_093_gap_intensity_regime_indicator},
    "f09_irgd_094_gap_clustering_indicator_5d": {"inputs": ["high", "low", "close"], "func": f09_irgd_094_gap_clustering_indicator_5d},
    "f09_irgd_095_most_recent_up_gap_close_position_in_252d_range": {"inputs": ["high", "low", "close"], "func": f09_irgd_095_most_recent_up_gap_close_position_in_252d_range},
    "f09_irgd_096_most_recent_up_gap_distance_above_63d_ma_atr": {"inputs": ["high", "low", "close"], "func": f09_irgd_096_most_recent_up_gap_distance_above_63d_ma_atr},
    "f09_irgd_097_most_recent_up_gap_distance_above_252d_ma_atr": {"inputs": ["high", "low", "close"], "func": f09_irgd_097_most_recent_up_gap_distance_above_252d_ma_atr},
    "f09_irgd_098_pct_of_gaps_252d_near_52w_high": {"inputs": ["high", "low", "close"], "func": f09_irgd_098_pct_of_gaps_252d_near_52w_high},
    "f09_irgd_099_pct_of_gaps_252d_in_top_decile_of_range": {"inputs": ["high", "low", "close"], "func": f09_irgd_099_pct_of_gaps_252d_in_top_decile_of_range},
    "f09_irgd_100_most_recent_up_gap_zone_above_or_below_63d_ma": {"inputs": ["high", "low", "close"], "func": f09_irgd_100_most_recent_up_gap_zone_above_or_below_63d_ma},
    "f09_irgd_101_cum_overnight_log_return_21d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_101_cum_overnight_log_return_21d},
    "f09_irgd_102_cum_overnight_log_return_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_102_cum_overnight_log_return_63d},
    "f09_irgd_103_cum_overnight_log_return_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_103_cum_overnight_log_return_252d},
    "f09_irgd_104_cum_intraday_log_return_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_104_cum_intraday_log_return_63d},
    "f09_irgd_105_overnight_minus_intraday_balance_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_105_overnight_minus_intraday_balance_63d},
    "f09_irgd_106_overnight_log_return_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_106_overnight_log_return_zscore_252d},
    "f09_irgd_107_gap_to_overnight_ratio_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_107_gap_to_overnight_ratio_252d},
    "f09_irgd_108_reversal_after_gap_up_rate_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_108_reversal_after_gap_up_rate_63d},
    "f09_irgd_109_reversal_after_gap_up_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_109_reversal_after_gap_up_rate_252d},
    "f09_irgd_110_mean_close_minus_open_atr_after_gap_up_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_110_mean_close_minus_open_atr_after_gap_up_63d},
    "f09_irgd_111_median_close_minus_open_atr_after_gap_up_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_111_median_close_minus_open_atr_after_gap_up_252d},
    "f09_irgd_112_followthrough_after_gap_up_rate_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_112_followthrough_after_gap_up_rate_252d},
    "f09_irgd_113_consecutive_up_gap_days_streak": {"inputs": ["high", "low", "close"], "func": f09_irgd_113_consecutive_up_gap_days_streak},
    "f09_irgd_114_consecutive_down_gap_days_streak": {"inputs": ["high", "low", "close"], "func": f09_irgd_114_consecutive_down_gap_days_streak},
    "f09_irgd_115_max_consecutive_up_gap_days_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_115_max_consecutive_up_gap_days_in_252d},
    "f09_irgd_116_most_recent_up_gap_volume_zscore_in_63d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_116_most_recent_up_gap_volume_zscore_in_63d},
    "f09_irgd_117_most_recent_up_gap_volume_zscore_in_252d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_117_most_recent_up_gap_volume_zscore_in_252d},
    "f09_irgd_118_mean_volume_zscore_gap_up_days_252d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_118_mean_volume_zscore_gap_up_days_252d},
    "f09_irgd_119_largest_up_gap_volume_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_119_largest_up_gap_volume_rank_252d},
    "f09_irgd_120_volume_decline_after_gap_up_5d": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_120_volume_decline_after_gap_up_5d},
    "f09_irgd_121_gap_up_with_low_volume_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f09_irgd_121_gap_up_with_low_volume_indicator},
    "f09_irgd_122_pct_up_gaps_filled_within_5d_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_122_pct_up_gaps_filled_within_5d_in_252d},
    "f09_irgd_123_pct_up_gaps_filled_within_21d_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_123_pct_up_gaps_filled_within_21d_in_252d},
    "f09_irgd_124_pct_up_gaps_filled_within_63d_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_124_pct_up_gaps_filled_within_63d_in_252d},
    "f09_irgd_125_pct_down_gaps_filled_within_21d_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_125_pct_down_gaps_filled_within_21d_in_252d},
    "f09_irgd_126_total_unfilled_up_gap_log_size_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_126_total_unfilled_up_gap_log_size_in_252d},
    "f09_irgd_127_total_unfilled_down_gap_log_size_in_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_127_total_unfilled_down_gap_log_size_in_252d},
    "f09_irgd_128_net_unfilled_gap_balance_log_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_128_net_unfilled_gap_balance_log_252d},
    "f09_irgd_129_bars_since_oldest_unfilled_up_gap": {"inputs": ["high", "low", "close"], "func": f09_irgd_129_bars_since_oldest_unfilled_up_gap},
    "f09_irgd_130_unfilled_gap_stack_count_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_130_unfilled_gap_stack_count_252d},
    "f09_irgd_131_gap_up_with_strong_close_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_131_gap_up_with_strong_close_indicator},
    "f09_irgd_132_gap_up_with_weak_close_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_132_gap_up_with_weak_close_indicator},
    "f09_irgd_133_count_strong_close_gap_ups_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_133_count_strong_close_gap_ups_252d},
    "f09_irgd_134_count_weak_close_gap_ups_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_134_count_weak_close_gap_ups_252d},
    "f09_irgd_135_strong_minus_weak_close_gap_balance_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_135_strong_minus_weak_close_gap_balance_252d},
    "f09_irgd_136_5d_log_return_after_most_recent_up_gap": {"inputs": ["high", "low", "close"], "func": f09_irgd_136_5d_log_return_after_most_recent_up_gap},
    "f09_irgd_137_21d_log_return_after_most_recent_up_gap": {"inputs": ["high", "low", "close"], "func": f09_irgd_137_21d_log_return_after_most_recent_up_gap},
    "f09_irgd_138_5d_high_excess_after_most_recent_up_gap_atr": {"inputs": ["high", "low", "close"], "func": f09_irgd_138_5d_high_excess_after_most_recent_up_gap_atr},
    "f09_irgd_139_5d_low_breakdown_after_most_recent_up_gap_atr": {"inputs": ["high", "low", "close"], "func": f09_irgd_139_5d_low_breakdown_after_most_recent_up_gap_atr},
    "f09_irgd_140_post_gap_up_5d_max_drawdown_pct": {"inputs": ["high", "low", "close"], "func": f09_irgd_140_post_gap_up_5d_max_drawdown_pct},
    "f09_irgd_141_gap_size_atr_normalized_zscore_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_141_gap_size_atr_normalized_zscore_252d},
    "f09_irgd_142_gap_size_log_normalized_by_realized_vol_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_142_gap_size_log_normalized_by_realized_vol_252d},
    "f09_irgd_143_gap_signal_ratio_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_143_gap_signal_ratio_252d},
    "f09_irgd_144_gap_intensity_index_63d": {"inputs": ["high", "low", "close"], "func": f09_irgd_144_gap_intensity_index_63d},
    "f09_irgd_145_gap_to_range_ratio_most_recent": {"inputs": ["high", "low", "close"], "func": f09_irgd_145_gap_to_range_ratio_most_recent},
    "f09_irgd_146_gap_distribution_kurtosis_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_146_gap_distribution_kurtosis_252d},
    "f09_irgd_147_terminal_gap_signature_score_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_147_terminal_gap_signature_score_252d},
    "f09_irgd_148_gap_failure_score_252d": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_148_gap_failure_score_252d},
    "f09_irgd_149_gap_top_signature_composite_indicator": {"inputs": ["open", "high", "low", "close"], "func": f09_irgd_149_gap_top_signature_composite_indicator},
    "f09_irgd_150_gap_pattern_diversity_index_252d": {"inputs": ["high", "low", "close"], "func": f09_irgd_150_gap_pattern_diversity_index_252d},
}
