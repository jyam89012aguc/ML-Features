"""volume_dryup_at_high base features 376-450 — Pipeline 1b-technical (extension #3 cont.).

Continuation of the ML-focused individual signal extension. Buckets:
- Specific test-bar / spring / secondary-test patterns
- Volume cluster timing
- Practical multi-condition compound signals
- Dryup at multi-year horizons
- Distribution-day refinements (DD after up days)
- Failure-to-resume patterns
- Cumulative vol-decay metrics

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


# ============================================================
# Bucket BH — Test / spring / secondary-test patterns (376-385)
# ============================================================

def f20_vdah_376_spring_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spring failure: today's low pierces 63d-trailing-low intraday but close back above, with HIGH vol z(252d)>1."""
    rmin63 = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    pierced = low < rmin63
    closed_back = close > rmin63
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (pierced & closed_back & (z > 1.0)).astype(float)


def f20_vdah_377_secondary_test_lower_vol_indicator(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second test of recent 21d low within 5d of first; today vol < volume on first test."""
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    first_test = (low <= 1.005 * rmin21)
    recent_first = first_test.shift(1).rolling(WDAYS - 1, min_periods=1).max().fillna(0.0)
    return (first_test & (recent_first > 0) & (volume < volume.rolling(WDAYS, min_periods=1).mean().shift(1))).astype(float)


def f20_vdah_378_probe_above_252d_high_close_below_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 when intraday high pierces above prior 252d max but close finishes below it."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    pierced = high > rmax
    closed_below = close < rmax
    return (pierced & closed_below).astype(float)


def f20_vdah_379_rejection_wick_depth_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score(252d) of (upper_wick / atr21) on bars where high at 252d max."""
    upper_wick = high - pd.concat([close, close.shift(1)], axis=1).max(axis=1)
    atr = _atr(high, low, close, n=MDAYS)
    depth = _safe_div(upper_wick, atr)
    z = _rolling_zscore(depth, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return z.where(high >= rmax, np.nan)


def f20_vdah_380_tag_count_at_252d_high_252d(high: pd.Series) -> pd.Series:
    """Trailing 252d count of distinct bars where high touched 252d trailing max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (high >= rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_381_cluster_of_rejections_5d_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when >=3 rejection bars (close in bottom third, at 252d high) in trailing 5d."""
    pos = _safe_div(close - low, high - low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((pos <= 0.33) & (high >= rmax)).astype(float)
    return (flag.rolling(WDAYS, min_periods=2).sum() >= 3).astype(float)


def f20_vdah_382_low_pierce_with_low_vol_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when low < prior bar's low but close > prior bar's low AND vol below 252d median."""
    pierced = low < low.shift(1)
    closed_back = close > low.shift(1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (pierced & closed_back & (volume < med)).astype(float)


def f20_vdah_383_failed_retake_of_resistance_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 when close > 252d high in past 3 bars BUT today close < 252d high (lost the level)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recently_above = (close > rmax).shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool)
    return (recently_above & (close < rmax)).astype(float)


def f20_vdah_384_cluster_inside_days_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 21d count of inside-day bars."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return inside.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f20_vdah_385_rejection_at_round_number_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when high is within 1% of nearest $5 multiple AND close in bottom third (round-number rejection)."""
    near_round = pd.Series((high / 5.0 - (high / 5.0).round()).abs() <= 0.20, index=high.index)
    pos = _safe_div(close - low, high - low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (near_round & (pos <= 0.33) & (high >= rmax)).astype(float)


# ============================================================
# Bucket BI — Volume cluster timing (386-395)
# ============================================================

def f20_vdah_386_time_since_first_3sigma_vol_in_252d(volume: pd.Series) -> pd.Series:
    """Bars since the FIRST 3-sigma vol burst in the trailing 252d window."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size == 0:
            return float(v.size)
        return float(v.size - 1 - pos[0])
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f20_vdah_387_time_between_first_and_last_3sigma_vol_252d(volume: pd.Series) -> pd.Series:
    """Bars between FIRST and LAST 3-sigma vol burst in trailing 252d window."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return 0.0
        return float(pos[-1] - pos[0])
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f20_vdah_388_bars_since_vol_above_252d_avg_indicator(volume: pd.Series) -> pd.Series:
    """Bars since last day vol exceeded 252d trailing mean, capped at 252."""
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > avg).astype(int)
    grp = flag.cumsum()
    return ((~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)).clip(upper=float(YDAYS))


def f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (3-sigma burst occurred 3 bars ago AND all 3 since have vol < 252d median)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med)
    silent3 = silent & silent.shift(1) & silent.shift(2)
    return (burst.shift(3) & silent3).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of burst-then-5-silent-days patterns."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med).astype(float)
    silent5 = silent.rolling(WDAYS, min_periods=1).sum() >= 5
    return (burst.shift(5) & silent5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of burst-then-21-silent-days patterns."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = (volume < med).astype(float)
    silent21 = silent.rolling(MDAYS, min_periods=WDAYS).sum() >= 18
    return (burst.shift(MDAYS) & silent21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_392_avg_bars_to_normalize_after_burst_252d(volume: pd.Series) -> pd.Series:
    """Avg bars from each 3-sigma burst to first subsequent bar with vol back at/above 252d median, over trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    def _f(w_z, w_v, w_m):
        vz = w_z; vv = w_v; vm = w_m
        if vz.size < 30:
            return np.nan
        bursts = np.where(vz > 3.0)[0]
        if bursts.size == 0:
            return np.nan
        normalization_lags = []
        for b in bursts:
            for j in range(b + 1, vv.size):
                if vv[j] >= vm[j]:
                    normalization_lags.append(j - b)
                    break
        return float(np.mean(normalization_lags)) if normalization_lags else np.nan
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    z_vals = z.values; v_vals = volume.values; m_vals = med.values
    n = volume.size
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(z_vals[i - YDAYS + 1: i + 1], v_vals[i - YDAYS + 1: i + 1], m_vals[i - YDAYS + 1: i + 1])
    return out


def f20_vdah_393_median_silence_length_after_burst_252d(volume: pd.Series) -> pd.Series:
    """Median length of silence (consec bars below 252d median vol) immediately following each 3-sigma burst, over 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    def _f(w_z, w_v, w_m):
        if w_z.size < 30:
            return np.nan
        bursts = np.where(w_z > 3.0)[0]
        if bursts.size == 0:
            return np.nan
        silences = []
        for b in bursts:
            cnt = 0
            for j in range(b + 1, w_v.size):
                if w_v[j] < w_m[j]:
                    cnt += 1
                else:
                    break
            silences.append(cnt)
        return float(np.median(silences)) if silences else np.nan
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    z_vals = z.values; v_vals = volume.values; m_vals = med.values
    n = volume.size
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(z_vals[i - YDAYS + 1: i + 1], v_vals[i - YDAYS + 1: i + 1], m_vals[i - YDAYS + 1: i + 1])
    return out


def f20_vdah_394_long_silence_period_count_252d(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of distinct silence-period starts where the silence lasted >=10 consec bars."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    silent = volume < med
    streak = _consecutive_true_streak(silent).astype(float)
    # mark bars where streak reaches exactly 10 (= start of qualifying long-silence period)
    starts_10 = (streak == 10).astype(float)
    return starts_10.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_395_median_burst_to_burst_interval_252d(volume: pd.Series) -> pd.Series:
    """Median inter-arrival between consecutive 3-sigma vol bursts in trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _f(w):
        if w.size < 30:
            return np.nan
        pos = np.where(w > 3.0)[0]
        if pos.size < 2:
            return np.nan
        return float(np.median(np.diff(pos)))
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


# ============================================================
# Bucket BJ — Practical "actionable" compound signals (396-405)
# ============================================================

def f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when high at 252d max AND 3d avg vol < 30% of 21d avg vol — actionable dryup at top."""
    m3 = volume.rolling(3, min_periods=2).mean()
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (m3 < 0.30 * m21)).astype(float)


def f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when high at 252d max AND 5d avg vol < 50% of 21d avg vol."""
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (m5 < 0.50 * m21)).astype(float)


def f20_vdah_398_dryup_at_5atr_extension_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close >= 21EMA + 5*ATR21 (extended) AND vol < 252d median."""
    ema21 = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    atr = _atr(high, low, close, n=MDAYS)
    extended = close >= (ema21 + 5.0 * atr)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (extended & (volume < med)).astype(float)


def f20_vdah_399_parabolic_acceleration_no_vol_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 5d return > 10% AND 21d return > 25% AND today's vol < 21d median (parabolic with no vol)."""
    r5 = close / close.shift(WDAYS) - 1.0
    r21 = close / close.shift(MDAYS) - 1.0
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((r5 > 0.10) & (r21 > 0.25) & (volume < med21)).astype(float)


def f20_vdah_400_vol_per_atr_pct_rank_252d_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank(252d) of (volume / ATR21) on bars where high at 252d max."""
    atr = _atr(high, low, close, n=MDAYS)
    r = _safe_div(volume, atr)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = r.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return pr.where(high >= rmax, np.nan)


def f20_vdah_401_low_vol_post_2x_atr_breakout_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when in last 3 bars there was a true_range > 2x ATR21 up-bar AND today's vol < 252d median."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    up_wide = (tr > 2.0 * atr) & (close > close.shift(1))
    had = up_wide.shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (had & (volume < med)).astype(float)


def f20_vdah_402_low_vol_close_above_3sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close z(252d) > 3 AND vol < 252d median."""
    cz = _rolling_zscore(close, YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((cz > 3.0) & (volume < med)).astype(float)


def f20_vdah_403_low_vol_close_above_2sigma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close z(252d) > 2 AND vol < 252d median."""
    cz = _rolling_zscore(close, YDAYS)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((cz > 2.0) & (volume < med)).astype(float)


def f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close > 95%-quantile(close, 5y) AND vol < 252d median."""
    q95 = close.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close > q95) & (volume < med)).astype(float)


def f20_vdah_405_low_vol_after_5_consec_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when prior 5 bars all up-close AND today's vol < 252d median."""
    up = close > close.shift(1)
    five_up = up & up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (five_up & (volume < med)).astype(float)


# ============================================================
# Bucket BK — Dryup at multi-year horizons (406-415)
# ============================================================

def f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol / 5y-mean-vol on bars where close >= expanding max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    avg5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg5y)
    return r.where(close >= rmax, np.nan)


def f20_vdah_407_vol_at_alltime_high_dwell_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (close at expanding max AND vol < 252d median)."""
    rmax = close.expanding(min_periods=YDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close >= rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol / 5y-mean-vol on bars where close = 5y trailing max."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    avg5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg5y)
    return r.where(close >= rmax5y, np.nan)


def f20_vdah_409_cluster_of_5y_high_low_vol_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (close at 5y max AND vol < 252d median)."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((close >= rmax5y) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_410_bars_since_last_5y_high_vol_burst(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last 3-sigma log-vol burst occurring at a 5y close-max, capped 252."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    cond = (z > 3.0) & (close >= rmax5y)
    flag = cond.astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_411_vol_at_3y_high_normalized(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol / 3y-mean-vol on bars where close = 3y trailing max."""
    rmax3y = close.rolling(DDAYS_3Y, min_periods=YDAYS).max()
    avg3y = volume.rolling(DDAYS_3Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg3y)
    return r.where(close >= rmax3y, np.nan)


def f20_vdah_412_vol_at_2y_high_normalized(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol / 2y-mean-vol on bars where close = 2y trailing max."""
    rmax2y = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    avg2y = volume.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    r = _safe_div(volume, avg2y)
    return r.where(close >= rmax2y, np.nan)


def f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (close in top decile of 5y range AND vol < 252d median)."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin5y, rmax5y - rmin5y)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((pos >= 0.90) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol pct-rank(252d) on bars where close at 5y max, over trailing 252d."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = volume.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return pr.where(close >= rmax5y, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_415_extreme_dryup_at_5y_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close at 5y max AND log-vol z(252d) < -2 (extreme dryup at extreme high)."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return ((close >= rmax5y) & (z < -2.0)).astype(float)


# ============================================================
# Bucket BL — Distribution-day refinements (416-425)
# ============================================================

def f20_vdah_416_dd_after_3_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a distribution day (close pct<-0.2%, vol>prev) AND prior 3 bars were all up-close."""
    pc = close.pct_change()
    up = close > close.shift(1)
    three_up = up.shift(1) & up.shift(2) & up.shift(3)
    dd = (pc < -0.002) & (volume > volume.shift(1))
    return (dd & three_up).astype(float)


def f20_vdah_417_dd_after_5_up_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a DD AND prior 5 bars were all up-close."""
    pc = close.pct_change()
    up = close > close.shift(1)
    five_up = up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4) & up.shift(5)
    dd = (pc < -0.002) & (volume > volume.shift(1))
    return (dd & five_up).astype(float)


def f20_vdah_418_dd_immediately_after_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a DD AND a 252d high event happened in the last 5 bars."""
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).shift(1).rolling(WDAYS, min_periods=1).max().fillna(False).astype(bool)
    return (dd & recent_high).astype(float)


def f20_vdah_419_dd_immediately_after_252d_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (DD within 5 bars of a 252d-high event)."""
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).shift(1).rolling(WDAYS, min_periods=1).max().fillna(False).astype(bool)
    return (dd & recent_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_420_count_dds_in_first_5d_after_252d_high(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of DDs in the 5 bars immediately following the most recent 252d high (lookback)."""
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (high >= rmax).astype(int)
    grp = is_peak.cumsum()
    bars_since_peak = (~is_peak.astype(bool)).astype(int).groupby(grp).cumsum()
    in_post_peak_window = bars_since_peak <= 5
    return dd.where(in_post_peak_window, 0.0).groupby(grp).cumsum().clip(upper=5.0)


def f20_vdah_421_dd_with_no_recovery_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a DD AND next 3 bars (using shifts on a prior frame: PIT — look BACK 3 days from a DD)."""
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    # 'No recovery' means: from 3 days after a DD looking back, the bar that was a DD had 3 subsequent NO-up days
    # PIT-safe: detect at t whether the DD-bar 3 days ago had no up-close in any of the 3 days since
    dd_3ago = dd.shift(3)
    no_up_since = (close.shift(2) <= close.shift(3)) & (close.shift(1) <= close.shift(2)) & (close <= close.shift(1))
    return (dd_3ago & no_up_since).astype(float)


def f20_vdah_422_dd_count_last_21d_after_252d_high_signal(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when trailing 21d contains >= 4 DDs AND a 252d high also occurred in trailing 21d."""
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    dd_count_21 = dd.rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_high = (high >= rmax).astype(float).rolling(MDAYS, min_periods=WDAYS).max() > 0
    return ((dd_count_21 >= 4) & recent_high).astype(float)


def f20_vdah_423_heavy_dd_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close pct_change < -2% AND vol > 1.5 × 21d median (heavy distribution day)."""
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.02) & (volume > 1.5 * med21)).astype(float)


def f20_vdah_424_heavy_dd_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of heavy DDs."""
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.02) & (volume > 1.5 * med21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_425_dd_with_widest_range_in_21d_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a DD AND today's true_range is the largest of the trailing 21 bars."""
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1))
    tr = _true_range(high, low, close)
    is_widest = tr >= tr.rolling(MDAYS, min_periods=WDAYS).max()
    return (dd & is_widest).astype(float)


# ============================================================
# Bucket BM — Failure-to-resume patterns (426-435)
# ============================================================

def f20_vdah_426_lower_high_after_252d_max_count_63d(high: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where today's 21d-high is lower than the prior 21d-high (lower-high sequence)."""
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    past_peak = (high >= rmax).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
    flag = (h21 < h21.shift(MDAYS)) & past_peak
    return flag.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_427_lower_high_with_low_vol_count_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where 21d-high < prior 21d-high AND vol < 252d median (silent lower-highs)."""
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (h21 < h21.shift(MDAYS)) & (volume < med)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_428_rolling_top_pattern_indicator(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3 distinct 21d-highs within 1% of each other in last 63d AND vol decreasing across them."""
    h = high.rolling(MDAYS, min_periods=WDAYS).max()
    h_lag1 = h.shift(MDAYS); h_lag2 = h.shift(2 * MDAYS)
    same = ((h - h_lag1).abs() / h_lag1 < 0.01) & ((h_lag1 - h_lag2).abs() / h_lag2 < 0.01)
    v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v_lag1 = v.shift(MDAYS); v_lag2 = v.shift(2 * MDAYS)
    vol_dec = (v < v_lag1) & (v_lag1 < v_lag2)
    return (same & vol_dec).astype(float)


def f20_vdah_429_triple_top_failure_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 when 3 highs within 1% in last 63d AND close < the lowest of those 3 highs (failed triple top)."""
    h = high.rolling(MDAYS, min_periods=WDAYS).max()
    h_lag1 = h.shift(MDAYS); h_lag2 = h.shift(2 * MDAYS)
    same = ((h - h_lag1).abs() / h_lag1 < 0.01) & ((h_lag1 - h_lag2).abs() / h_lag2 < 0.01)
    lowest = pd.concat([h, h_lag1, h_lag2], axis=1).min(axis=1)
    return (same & (close < lowest * 0.98)).astype(float)


def f20_vdah_430_neckline_break_with_high_vol_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxy for H&S neck break: close below 63d low AND vol z(252d) > 1, after recent 252d high in 63d."""
    rmin63 = low.rolling(QDAYS, min_periods=MDAYS).min().shift(1)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
    return ((close < rmin63) & (z > 1.0) & recent_peak).astype(float)


def f20_vdah_431_rising_wedge_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rising wedge breakdown proxy: highs rising AND lows rising but at slower rate AND close < 21d-low."""
    h_slope = (high.rolling(MDAYS, min_periods=WDAYS).max() - high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS))
    l_slope = (low.rolling(MDAYS, min_periods=WDAYS).min() - low.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS))
    wedge = (h_slope > 0) & (l_slope > 0) & (h_slope < l_slope)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (wedge & (close < rmin21)).astype(float)


def f20_vdah_432_rising_wedge_breakdown_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d count of rising wedge breakdown events."""
    h_slope = (high.rolling(MDAYS, min_periods=WDAYS).max() - high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS))
    l_slope = (low.rolling(MDAYS, min_periods=WDAYS).min() - low.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS))
    wedge = (h_slope > 0) & (l_slope > 0) & (h_slope < l_slope)
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    return (wedge & (close < rmin21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_433_descending_triangle_apex_close_above_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when 21d-high < prior 21d-high AND 21d-low ≈ prior 21d-low AND close > 21d-low (sitting on support — risky)."""
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    l21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    desc = (h21 < h21.shift(MDAYS)) & ((l21 - l21.shift(MDAYS)).abs() / l21.shift(MDAYS) < 0.01)
    sitting = close > l21
    return (desc & sitting).astype(float)


def f20_vdah_434_failed_attempt_to_break_resistance_count_252d(high: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where high > 252d max but immediately next bar high < that level (failed break)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    cross = high > rmax
    next_below = high.shift(1) < rmax  # peek — flip frame: use PIT-safe shift
    # PIT-safe: at t, check if t-1 was a cross AND today's high < t-1's max-of-prior level
    cross_yest = cross.shift(1)
    return (cross_yest & (high < rmax)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_435_gap_below_uptrend_line_low_vol_indicator(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when open < min(close-21d, close-63d) AND vol < 252d median — gap-below-trend with low vol."""
    c21 = close.rolling(MDAYS, min_periods=WDAYS).min()
    c63 = close.rolling(QDAYS, min_periods=MDAYS).min()
    trend_low = pd.concat([c21, c63], axis=1).min(axis=1)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((open < trend_low) & (volume < med)).astype(float)


# ============================================================
# Bucket BN — Cumulative vol-decay metrics (436-450)
# ============================================================

def f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where (high at 252d max AND vol < 252d median)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (high >= rmax) & (volume < med)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_437_cumulative_vol_deficit_below_median_252d(volume: pd.Series) -> pd.Series:
    """Sum over 252d of max(median - vol, 0) — cumulative vol deficit."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    deficit = (med - volume).clip(lower=0.0)
    return deficit.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 252d of (close in top decile of 252d range AND vol < q20 of 252d) — strict compound count."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    q20 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.20)
    return ((pos >= 0.90) & (volume <= q20)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_439_avg_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on bars where high at 252d max, over trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_440_median_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Median vol on bars where high at 252d max, over trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).median()


def f20_vdah_441_max_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Max vol on bars where high at 252d max, over trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_442_min_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Min vol on bars where high at 252d max, over trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).min()


def f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Max minus min vol on at-252d-high bars over trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v = volume.where(high >= rmax, np.nan)
    return v.rolling(YDAYS, min_periods=QDAYS).max() - v.rolling(YDAYS, min_periods=QDAYS).min()


def f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol-quintile (0-4) on at-252d-high bars over trailing 252d."""
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr = volume.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    q = (pr * 5.0).clip(upper=4.999)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return q.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """(Avg vol on at-252d-high bars 252d) / (overall 252d avg vol). <1 = silent at high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high_avg = volume.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall_avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(at_high_avg, overall_avg)


def f20_vdah_446_low_vol_close_top_decile_max_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec streak of (close in top decile of 252d range AND vol < 252d median) in trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    cond = (pos >= 0.90) & (volume < med)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_447_min_vol_age_at_252d_high(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the most recent (at-252d-high AND trailing-252d-min-vol) bar, capped 252."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    vmin = volume.rolling(YDAYS, min_periods=QDAYS).min()
    cond = (high >= rmax) & (volume <= vmin)
    flag = cond.astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_448_low_vol_within_5pct_of_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (high ≥ 95% × 252d-max AND vol < 252d median)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= 0.95 * rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_449_low_vol_within_2pct_of_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (high ≥ 98% × 252d-max AND vol < 252d median)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= 0.98 * rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_450_low_vol_at_exact_252d_high_count(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (high = 252d-max AND vol < 252d median)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((high >= rmax) & (volume < med)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 376-450
# ============================================================

VOLUME_DRYUP_AT_HIGH_BASE_REGISTRY_376_450 = {
    "f20_vdah_376_spring_failure_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_376_spring_failure_indicator},
    "f20_vdah_377_secondary_test_lower_vol_indicator": {"inputs": ["low", "volume"], "func": f20_vdah_377_secondary_test_lower_vol_indicator},
    "f20_vdah_378_probe_above_252d_high_close_below_indicator": {"inputs": ["high", "close"], "func": f20_vdah_378_probe_above_252d_high_close_below_indicator},
    "f20_vdah_379_rejection_wick_depth_zscore_252d": {"inputs": ["high", "low", "close"], "func": f20_vdah_379_rejection_wick_depth_zscore_252d},
    "f20_vdah_380_tag_count_at_252d_high_252d": {"inputs": ["high"], "func": f20_vdah_380_tag_count_at_252d_high_252d},
    "f20_vdah_381_cluster_of_rejections_5d_indicator": {"inputs": ["high", "low", "close"], "func": f20_vdah_381_cluster_of_rejections_5d_indicator},
    "f20_vdah_382_low_pierce_with_low_vol_indicator": {"inputs": ["low", "close", "volume"], "func": f20_vdah_382_low_pierce_with_low_vol_indicator},
    "f20_vdah_383_failed_retake_of_resistance_indicator": {"inputs": ["high", "close"], "func": f20_vdah_383_failed_retake_of_resistance_indicator},
    "f20_vdah_384_cluster_inside_days_count_21d": {"inputs": ["high", "low"], "func": f20_vdah_384_cluster_inside_days_count_21d},
    "f20_vdah_385_rejection_at_round_number_indicator": {"inputs": ["high", "low", "close"], "func": f20_vdah_385_rejection_at_round_number_indicator},
    "f20_vdah_386_time_since_first_3sigma_vol_in_252d": {"inputs": ["volume"], "func": f20_vdah_386_time_since_first_3sigma_vol_in_252d},
    "f20_vdah_387_time_between_first_and_last_3sigma_vol_252d": {"inputs": ["volume"], "func": f20_vdah_387_time_between_first_and_last_3sigma_vol_252d},
    "f20_vdah_388_bars_since_vol_above_252d_avg_indicator": {"inputs": ["volume"], "func": f20_vdah_388_bars_since_vol_above_252d_avg_indicator},
    "f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d": {"inputs": ["volume"], "func": f20_vdah_389_vol_burst_followed_by_3_silent_days_count_252d},
    "f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d": {"inputs": ["volume"], "func": f20_vdah_390_vol_burst_followed_by_5_silent_days_count_252d},
    "f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d": {"inputs": ["volume"], "func": f20_vdah_391_vol_burst_followed_by_21_silent_days_count_252d},
    "f20_vdah_392_avg_bars_to_normalize_after_burst_252d": {"inputs": ["volume"], "func": f20_vdah_392_avg_bars_to_normalize_after_burst_252d},
    "f20_vdah_393_median_silence_length_after_burst_252d": {"inputs": ["volume"], "func": f20_vdah_393_median_silence_length_after_burst_252d},
    "f20_vdah_394_long_silence_period_count_252d": {"inputs": ["volume"], "func": f20_vdah_394_long_silence_period_count_252d},
    "f20_vdah_395_median_burst_to_burst_interval_252d": {"inputs": ["volume"], "func": f20_vdah_395_median_burst_to_burst_interval_252d},
    "f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg": {"inputs": ["high", "volume"], "func": f20_vdah_396_at_252d_high_with_vol_3d_below_30pct_21d_avg},
    "f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg": {"inputs": ["high", "volume"], "func": f20_vdah_397_at_252d_high_with_vol_5d_below_50pct_21d_avg},
    "f20_vdah_398_dryup_at_5atr_extension_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_398_dryup_at_5atr_extension_indicator},
    "f20_vdah_399_parabolic_acceleration_no_vol_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_399_parabolic_acceleration_no_vol_indicator},
    "f20_vdah_400_vol_per_atr_pct_rank_252d_at_high": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_400_vol_per_atr_pct_rank_252d_at_high},
    "f20_vdah_401_low_vol_post_2x_atr_breakout_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_401_low_vol_post_2x_atr_breakout_indicator},
    "f20_vdah_402_low_vol_close_above_3sigma_252d": {"inputs": ["close", "volume"], "func": f20_vdah_402_low_vol_close_above_3sigma_252d},
    "f20_vdah_403_low_vol_close_above_2sigma_252d": {"inputs": ["close", "volume"], "func": f20_vdah_403_low_vol_close_above_2sigma_252d},
    "f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_404_low_vol_close_in_top_5pct_5y_indicator},
    "f20_vdah_405_low_vol_after_5_consec_up_days_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_405_low_vol_after_5_consec_up_days_indicator},
    "f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg": {"inputs": ["close", "volume"], "func": f20_vdah_406_vol_at_alltime_high_normalized_by_5y_avg},
    "f20_vdah_407_vol_at_alltime_high_dwell_count_252d": {"inputs": ["close", "volume"], "func": f20_vdah_407_vol_at_alltime_high_dwell_count_252d},
    "f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg": {"inputs": ["close", "volume"], "func": f20_vdah_408_vol_at_5y_high_normalized_by_5y_avg},
    "f20_vdah_409_cluster_of_5y_high_low_vol_count_252d": {"inputs": ["close", "volume"], "func": f20_vdah_409_cluster_of_5y_high_low_vol_count_252d},
    "f20_vdah_410_bars_since_last_5y_high_vol_burst": {"inputs": ["close", "volume"], "func": f20_vdah_410_bars_since_last_5y_high_vol_burst},
    "f20_vdah_411_vol_at_3y_high_normalized": {"inputs": ["close", "volume"], "func": f20_vdah_411_vol_at_3y_high_normalized},
    "f20_vdah_412_vol_at_2y_high_normalized": {"inputs": ["close", "volume"], "func": f20_vdah_412_vol_at_2y_high_normalized},
    "f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d": {"inputs": ["close", "volume"], "func": f20_vdah_413_low_vol_density_at_top_decile_5y_range_252d},
    "f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d": {"inputs": ["close", "volume"], "func": f20_vdah_414_vol_pct_rank_at_5y_high_bars_mean_252d},
    "f20_vdah_415_extreme_dryup_at_5y_high_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_415_extreme_dryup_at_5y_high_indicator},
    "f20_vdah_416_dd_after_3_up_days_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_416_dd_after_3_up_days_indicator},
    "f20_vdah_417_dd_after_5_up_days_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_417_dd_after_5_up_days_indicator},
    "f20_vdah_418_dd_immediately_after_252d_high_indicator": {"inputs": ["high", "close", "volume"], "func": f20_vdah_418_dd_immediately_after_252d_high_indicator},
    "f20_vdah_419_dd_immediately_after_252d_high_count_252d": {"inputs": ["high", "close", "volume"], "func": f20_vdah_419_dd_immediately_after_252d_high_count_252d},
    "f20_vdah_420_count_dds_in_first_5d_after_252d_high": {"inputs": ["high", "close", "volume"], "func": f20_vdah_420_count_dds_in_first_5d_after_252d_high},
    "f20_vdah_421_dd_with_no_recovery_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_421_dd_with_no_recovery_indicator},
    "f20_vdah_422_dd_count_last_21d_after_252d_high_signal": {"inputs": ["high", "close", "volume"], "func": f20_vdah_422_dd_count_last_21d_after_252d_high_signal},
    "f20_vdah_423_heavy_dd_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_423_heavy_dd_indicator},
    "f20_vdah_424_heavy_dd_count_252d": {"inputs": ["close", "volume"], "func": f20_vdah_424_heavy_dd_count_252d},
    "f20_vdah_425_dd_with_widest_range_in_21d_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_425_dd_with_widest_range_in_21d_indicator},
    "f20_vdah_426_lower_high_after_252d_max_count_63d": {"inputs": ["high"], "func": f20_vdah_426_lower_high_after_252d_max_count_63d},
    "f20_vdah_427_lower_high_with_low_vol_count_252d": {"inputs": ["high", "volume"], "func": f20_vdah_427_lower_high_with_low_vol_count_252d},
    "f20_vdah_428_rolling_top_pattern_indicator": {"inputs": ["high", "volume"], "func": f20_vdah_428_rolling_top_pattern_indicator},
    "f20_vdah_429_triple_top_failure_indicator": {"inputs": ["high", "close"], "func": f20_vdah_429_triple_top_failure_indicator},
    "f20_vdah_430_neckline_break_with_high_vol_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_430_neckline_break_with_high_vol_indicator},
    "f20_vdah_431_rising_wedge_breakdown_indicator": {"inputs": ["high", "low", "close"], "func": f20_vdah_431_rising_wedge_breakdown_indicator},
    "f20_vdah_432_rising_wedge_breakdown_count_252d": {"inputs": ["high", "low", "close"], "func": f20_vdah_432_rising_wedge_breakdown_count_252d},
    "f20_vdah_433_descending_triangle_apex_close_above_indicator": {"inputs": ["high", "low", "close"], "func": f20_vdah_433_descending_triangle_apex_close_above_indicator},
    "f20_vdah_434_failed_attempt_to_break_resistance_count_252d": {"inputs": ["high"], "func": f20_vdah_434_failed_attempt_to_break_resistance_count_252d},
    "f20_vdah_435_gap_below_uptrend_line_low_vol_indicator": {"inputs": ["open", "close", "volume"], "func": f20_vdah_435_gap_below_uptrend_line_low_vol_indicator},
    "f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high": {"inputs": ["high", "volume"], "func": f20_vdah_436_cumulative_low_vol_days_pct_of_252d_at_high},
    "f20_vdah_437_cumulative_vol_deficit_below_median_252d": {"inputs": ["volume"], "func": f20_vdah_437_cumulative_vol_deficit_below_median_252d},
    "f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_438_cum_low_vol_dwell_score_top_decile_252d},
    "f20_vdah_439_avg_vol_on_at_252d_high_bars_252d": {"inputs": ["high", "volume"], "func": f20_vdah_439_avg_vol_on_at_252d_high_bars_252d},
    "f20_vdah_440_median_vol_on_at_252d_high_bars_252d": {"inputs": ["high", "volume"], "func": f20_vdah_440_median_vol_on_at_252d_high_bars_252d},
    "f20_vdah_441_max_vol_on_at_252d_high_bars_252d": {"inputs": ["high", "volume"], "func": f20_vdah_441_max_vol_on_at_252d_high_bars_252d},
    "f20_vdah_442_min_vol_on_at_252d_high_bars_252d": {"inputs": ["high", "volume"], "func": f20_vdah_442_min_vol_on_at_252d_high_bars_252d},
    "f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d": {"inputs": ["high", "volume"], "func": f20_vdah_443_range_of_vol_on_at_252d_high_bars_252d},
    "f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d": {"inputs": ["high", "volume"], "func": f20_vdah_444_vol_quintile_on_at_252d_high_bars_mean_252d},
    "f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d": {"inputs": ["high", "volume"], "func": f20_vdah_445_ratio_avg_vol_at_high_to_avg_vol_overall_252d},
    "f20_vdah_446_low_vol_close_top_decile_max_streak_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_446_low_vol_close_top_decile_max_streak_252d},
    "f20_vdah_447_min_vol_age_at_252d_high": {"inputs": ["high", "volume"], "func": f20_vdah_447_min_vol_age_at_252d_high},
    "f20_vdah_448_low_vol_within_5pct_of_252d_high_count": {"inputs": ["high", "volume"], "func": f20_vdah_448_low_vol_within_5pct_of_252d_high_count},
    "f20_vdah_449_low_vol_within_2pct_of_252d_high_count": {"inputs": ["high", "volume"], "func": f20_vdah_449_low_vol_within_2pct_of_252d_high_count},
    "f20_vdah_450_low_vol_at_exact_252d_high_count": {"inputs": ["high", "volume"], "func": f20_vdah_450_low_vol_at_exact_252d_high_count},
}
