"""stochastic_williams_family base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: basic stoch K/D at multi-horizons (short/quarter/annual = distinct concepts).
Bucket B: K-D differential and cross dynamics.
Bucket C: OB state at multiple thresholds & horizons.
Bucket D: OB exits (the bearish signal).
Bucket E: dwell / persistence in OB.
Bucket F: failed retest / lower OB peaks.
Bucket G: bearish divergence (price up, stoch down).
Bucket H: Williams %R variants.
Bucket I: Stoch RSI variants.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers.
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


def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k


def _stoch_d(k, n_d):
    return k.rolling(n_d, min_periods=max(n_d // 2, 1)).mean()


def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _stoch_rsi_kd(close, n_rsi=14, n_k=14, smooth_k=3, smooth_d=3):
    r = _rsi(close, n_rsi)
    ll = r.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = r.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    k = raw_k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    d = k.rolling(smooth_d, min_periods=max(smooth_d // 2, 1)).mean()
    return k, d


def _ultimate_osc(high, low, close, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    s1 = bp.rolling(n1, min_periods=max(n1 // 3, 2)).sum() / tr.rolling(n1, min_periods=max(n1 // 3, 2)).sum()
    s2 = bp.rolling(n2, min_periods=max(n2 // 3, 2)).sum() / tr.rolling(n2, min_periods=max(n2 // 3, 2)).sum()
    s3 = bp.rolling(n3, min_periods=max(n3 // 3, 2)).sum() / tr.rolling(n3, min_periods=max(n3 // 3, 2)).sum()
    return 100.0 * (4.0 * s1 + 2.0 * s2 + s3) / 7.0


def _bars_since_true(mask: pd.Series) -> pd.Series:
    """Bars since `mask` was last True. NaN until first True occurs."""
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    """Current consecutive run of True. Resets to 0 at False."""
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket A — basic stoch K / D at multi-horizons (001-008)
# ============================================================

def f26_stwf_001_fast_k_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical fast %K(14) — level."""
    return _stoch_k(high, low, close, 14)


def f26_stwf_002_fast_k_5_weekly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast %K(5) — weekly momentum extreme detector (distinct concept from 14)."""
    return _stoch_k(high, low, close, WDAYS)


def f26_stwf_003_fast_k_63_quarterly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast %K(63) — quarterly momentum extreme (distinct concept)."""
    return _stoch_k(high, low, close, QDAYS)


def f26_stwf_004_fast_k_252_annual(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast %K(252) — annual momentum extreme (distinct concept)."""
    return _stoch_k(high, low, close, YDAYS)


def f26_stwf_005_slow_d_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical slow %D(14) = SMA3 of %K — smoothed level."""
    return _stoch_d(_stoch_k(high, low, close, 14), 3)


def f26_stwf_006_slow_d_63_quarterly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow %D over quarterly horizon — smoothed quarterly momentum."""
    return _stoch_d(_stoch_k(high, low, close, QDAYS), 5)


def f26_stwf_007_slow_d_252_annual(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow %D over annual horizon — smoothed long-run momentum."""
    return _stoch_d(_stoch_k(high, low, close, YDAYS), 21)


def f26_stwf_008_full_stoch_d_14_5_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Full stochastic %D (period=14, smooth_k=5, smooth_d=5) — double-smoothed top detector."""
    return _stoch_d(_stoch_k(high, low, close, 14, smooth_k=5), 5)


# ============================================================
# Bucket B — K-D differential / cross dynamics (009-015)
# ============================================================

def f26_stwf_009_k_minus_d_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K - D differential at n=14 — cross magnitude (negative => bearish bias)."""
    k = _stoch_k(high, low, close, 14)
    return k - _stoch_d(k, 3)


def f26_stwf_010_k_minus_d_63_quarterly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K - D differential at quarterly horizon — slower cross dynamic."""
    k = _stoch_k(high, low, close, QDAYS)
    return k - _stoch_d(k, 5)


def f26_stwf_011_bearish_cross_indicator_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 when %K crosses below %D this bar (classical bearish stoch cross)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)


def f26_stwf_012_bearish_cross_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bearish K/D crosses in trailing 63 bars — cross density."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    ev = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)


def f26_stwf_013_bars_since_last_bearish_cross_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent bearish K/D cross — recency of bearish signal."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    ev = (diff.shift(1) > 0) & (diff <= 0)
    return _bars_since_true(ev)


def f26_stwf_014_bullish_cross_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bullish K/D crosses in 63 bars — context for cross-density net."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    ev = ((diff.shift(1) <= 0) & (diff > 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)


def f26_stwf_015_cross_density_net_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish crosses minus bullish crosses in 63 — net cross-pressure index."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    diff = k - d
    be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    bu = ((diff.shift(1) <= 0) & (diff > 0)).astype(float)
    return (be - bu).rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)


# ============================================================
# Bucket C — OB state at multiple thresholds / horizons (016-023)
# ============================================================

def f26_stwf_016_stoch_in_ob80_14_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K(14) > 80 — classical OB state."""
    k = _stoch_k(high, low, close, 14)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_017_stoch_in_extreme_ob90_14_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K(14) > 90 — extreme OB (distinct hypothesis from OB80: severity)."""
    k = _stoch_k(high, low, close, 14)
    return (k > 90.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_018_stoch_in_ob80_63_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K(63) > 80 — quarterly OB state (distinct horizon concept)."""
    k = _stoch_k(high, low, close, QDAYS)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_019_stoch_in_ob80_252_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K(252) > 80 — annual OB state."""
    k = _stoch_k(high, low, close, YDAYS)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_020_williams_r_in_ob_state_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R(14) > -20 — alternative OB indicator (different scale, different smoothing)."""
    wr = _williams_r(high, low, close, 14)
    return (wr > -20.0).astype(float).where(wr.notna(), np.nan)


def f26_stwf_021_stoch_above_q95_distribution_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if current %K above its trailing 252d 95th percentile — distribution-based OB."""
    k = _stoch_k(high, low, close, 14)
    q = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return (k > q).astype(float).where(k.notna() & q.notna(), np.nan)


def f26_stwf_022_stoch_above_q99_distribution_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if current %K above trailing 252d 99th percentile — extreme distribution OB."""
    k = _stoch_k(high, low, close, 14)
    q = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return (k > q).astype(float).where(k.notna() & q.notna(), np.nan)


def f26_stwf_023_kd_both_above_80_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) > 80 AND D(14) > 80 — confirmed-OB (both fast and smoothed agree)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    return ((k > 80.0) & (d > 80.0)).astype(float).where(k.notna() & d.notna(), np.nan)


# ============================================================
# Bucket D — OB exits (024-031)
# ============================================================

def f26_stwf_024_just_exited_ob80_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K(14) was > 80 on prior bar and is <= 80 this bar — classical OB-exit trigger."""
    k = _stoch_k(high, low, close, 14)
    return ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_025_bars_since_last_ob80_exit_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent OB80 exit — recency of the bearish trigger."""
    k = _stoch_k(high, low, close, 14)
    ev = (k.shift(1) > 80.0) & (k <= 80.0)
    return _bars_since_true(ev)


def f26_stwf_026_count_ob80_exits_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of OB80 exits in trailing 63 bars — frequency / churn in OB zone."""
    k = _stoch_k(high, low, close, 14)
    ev = ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_027_count_ob80_exits_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of OB80 exits in 252 bars — annual frequency of OB exits."""
    k = _stoch_k(high, low, close, 14)
    ev = ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_028_bars_since_last_extreme_ob90_exit(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent extreme-OB(>90) exit — extreme-momentum recency."""
    k = _stoch_k(high, low, close, 14)
    ev = (k.shift(1) > 90.0) & (k <= 90.0)
    return _bars_since_true(ev)


def f26_stwf_029_just_exited_ob80_63_quarterly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if quarterly-stoch %K(63) just exited OB80 — slow-horizon exit."""
    k = _stoch_k(high, low, close, QDAYS)
    return ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_030_ob_exit_velocity_drop_from_peak_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At OB exit, magnitude = (rolling 21d max of K) - K — speed of post-peak collapse.
    Only defined when an OB exit fires; else NaN."""
    k = _stoch_k(high, low, close, 14)
    ev = (k.shift(1) > 80.0) & (k <= 80.0)
    peak = k.rolling(MDAYS, min_periods=WDAYS).max()
    out = (peak - k).where(ev, np.nan)
    return out


def f26_stwf_031_failed_retest_lower_ob_peak_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if current OB-zone local peak of %K is lower than the prior OB-zone peak in 63 bars
    — failed retest (lower momentum at higher price)."""
    k = _stoch_k(high, low, close, 14)
    in_ob = (k > 80.0)
    # find local peak in OB: K[t-1] = max in 63d AND in_ob[t-1]; compare to prior OB peak max
    rmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    prev_rmax = rmax.shift(MDAYS)
    just_exited = (k.shift(1) > 80.0) & (k <= 80.0)
    failed = (rmax < prev_rmax).astype(float)
    return failed.where(just_exited & rmax.notna() & prev_rmax.notna(), np.nan)


# ============================================================
# Bucket E — dwell / persistence in OB (032-039)
# ============================================================

def f26_stwf_032_fraction_time_in_ob80_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 21 bars in OB80 — monthly OB dwell."""
    k = _stoch_k(high, low, close, 14)
    return (k > 80.0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(k.notna(), np.nan)


def f26_stwf_033_fraction_time_in_ob80_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars in OB80 — quarterly OB dwell."""
    k = _stoch_k(high, low, close, 14)
    return (k > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(k.notna(), np.nan)


def f26_stwf_034_fraction_time_in_ob80_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars in OB80 — annual OB dwell (saturation index)."""
    k = _stoch_k(high, low, close, 14)
    return (k > 80.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna(), np.nan)


def f26_stwf_035_longest_ob80_run_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest consecutive run of OB80 days in trailing 252 bars."""
    k = _stoch_k(high, low, close, 14)
    streak = _streak_true(k > 80.0)
    return streak.rolling(YDAYS, min_periods=QDAYS).max().where(k.notna(), np.nan)


def f26_stwf_036_current_ob80_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive run of OB80 (resets at exit) — live streak length."""
    k = _stoch_k(high, low, close, 14)
    return _streak_true(k > 80.0).where(k.notna(), np.nan)


def f26_stwf_037_distinct_ob80_sessions_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of distinct OB80 sessions (entries) in 252d — # of separate OB episodes."""
    k = _stoch_k(high, low, close, 14)
    entered = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    return entered.rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_038_avg_ob80_session_duration_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average OB80 session duration in 252 bars = (time-in-OB) / (#sessions)."""
    k = _stoch_k(high, low, close, 14)
    in_ob = (k > 80.0).astype(float)
    entered = ((k.shift(1) <= 80.0) & (k > 80.0)).astype(float)
    num = in_ob.rolling(YDAYS, min_periods=QDAYS).sum()
    den = entered.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den).where(k.notna(), np.nan)


def f26_stwf_039_cumulative_ob_area_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of (K - 80) over bars where K > 80, past 252 — cumulative OB area / saturation intensity."""
    k = _stoch_k(high, low, close, 14)
    area_bar = (k - 80.0).clip(lower=0).where(k.notna(), np.nan)
    return area_bar.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — failed retest / lower OB peaks (040-047)
# ============================================================

def f26_stwf_040_peak_decay_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference: rolling 21d max of K minus its value 21 bars ago — short-term peak decay."""
    k = _stoch_k(high, low, close, 14)
    pmax = k.rolling(MDAYS, min_periods=WDAYS).max()
    return pmax - pmax.shift(MDAYS)


def f26_stwf_041_peak_decay_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d max of K minus its value 63 bars ago — quarterly peak decay."""
    k = _stoch_k(high, low, close, 14)
    pmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f26_stwf_042_count_lower_high_peaks_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of OB-zone exits where the K-peak was below the prior 63d K-peak — quarterly cooling."""
    k = _stoch_k(high, low, close, 14)
    rmax_prev = k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    just_exited = (k.shift(1) > 80.0) & (k <= 80.0)
    lh = (k.shift(1) < rmax_prev) & just_exited
    return lh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_043_count_lower_high_peaks_ob_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of OB-exits where K-peak was below the prior 252d K-peak."""
    k = _stoch_k(high, low, close, 14)
    rmax_prev = k.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    just_exited = (k.shift(1) > 80.0) & (k <= 80.0)
    lh = (k.shift(1) < rmax_prev) & just_exited
    return lh.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_044_compression_high_minus_low_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K(14) 63d range high minus 63d range low — compression of oscillator range (narrow => squeeze)."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(QDAYS, min_periods=MDAYS).max() - k.rolling(QDAYS, min_periods=MDAYS).min()


def f26_stwf_045_failed_to_reach_prior_max_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d rolling max of K is < 21d rolling max of K from 21 bars ago, while price made a new 21d high."""
    k = _stoch_k(high, low, close, 14)
    p_now = k.rolling(MDAYS, min_periods=WDAYS).max()
    p_prev = p_now.shift(MDAYS)
    price_new_high = high == high.rolling(MDAYS, min_periods=WDAYS).max()
    return ((p_now < p_prev) & price_new_high).astype(float).where(k.notna() & p_prev.notna(), np.nan)


def f26_stwf_046_peak_amplitude_decay_ratio_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(63d K-peak) / (63d K-peak from 63 bars ago) — ratio < 1 = decaying momentum amplitude."""
    k = _stoch_k(high, low, close, 14)
    pmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(pmax, pmax.shift(QDAYS))


def f26_stwf_047_recent_ob_peak_height_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of the most-recent 21d K-peak vs its trailing 252d distribution of 21d K-peaks."""
    k = _stoch_k(high, low, close, 14)
    pmax = k.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(pmax, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket G — bearish divergence (price up, stoch down) (048-058)
# ============================================================

def f26_stwf_048_price_vs_stochk_div_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price > prior 63d high AND %K below prior 63d K-high — bearish divergence indicator."""
    k = _stoch_k(high, low, close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    k_below = k < k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & k_below).astype(float).where(k.notna(), np.nan)


def f26_stwf_049_price_vs_stochk_div_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Long-horizon bearish divergence: new 252d price-high but K below prior 252d K-high."""
    k = _stoch_k(high, low, close, 14)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    k_below = k < k.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & k_below).astype(float).where(k.notna(), np.nan)


def f26_stwf_050_price_vs_stochd_div_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish div using slow %D (smoother divergence signal)."""
    k = _stoch_k(high, low, close, 14)
    d = _stoch_d(k, 3)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    d_below = d < d.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & d_below).astype(float).where(d.notna(), np.nan)


def f26_stwf_051_rolling_corr_price_stochk_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d correlation(close, %K) — when it drops sharply, price and momentum decouple."""
    k = _stoch_k(high, low, close, 14)
    return close.rolling(QDAYS, min_periods=MDAYS).corr(k)


def f26_stwf_052_count_price_new_21h_with_k_not_ob_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where price made a new 21d high but %K(14) was NOT in OB — quiet new highs."""
    k = _stoch_k(high, low, close, 14)
    pnew = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    quiet = (pnew == 1.0) & (k <= 80.0)
    return quiet.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)


def f26_stwf_053_amplitude_last_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bearish-div bars, amplitude = (prior 63d K-max) - K — magnitude of divergence."""
    k = _stoch_k(high, low, close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_kmax = k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_kmax - k).where(p_new & (k < prior_kmax), np.nan)
    return amp.ffill(limit=QDAYS)


def f26_stwf_054_bars_since_last_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent bearish K-divergence event — recency of bearish setup."""
    k = _stoch_k(high, low, close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_kmax = k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = p_new & (k < prior_kmax)
    return _bars_since_true(ev)


def f26_stwf_055_williams_r_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using Williams %R instead of stoch %K."""
    wr = _williams_r(high, low, close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    wr_below = wr < wr.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & wr_below).astype(float).where(wr.notna(), np.nan)


def f26_stwf_056_stoch_rsi_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using Stoch-RSI K — momentum-of-RSI divergence."""
    sr_k, _ = _stoch_rsi_kd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    sr_below = sr_k < sr_k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & sr_below).astype(float).where(sr_k.notna(), np.nan)


def f26_stwf_057_ultimate_osc_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using Williams' Ultimate Oscillator (multi-timeframe momentum)."""
    uo = _ultimate_osc(high, low, close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    uo_below = uo < uo.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & uo_below).astype(float).where(uo.notna(), np.nan)


def f26_stwf_058_multi_oscillator_div_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of {stoch K, Williams %R, stoch-RSI K, ultimate-osc} indicators showing
    bearish div on the current bar — multi-oscillator divergence breadth."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sr_k, _ = _stoch_rsi_kd(close)
    uo = _ultimate_osc(high, low, close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    d1 = (k < k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    d2 = (wr < wr.shift(1).rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    d3 = (sr_k < sr_k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    d4 = (uo < uo.shift(1).rolling(QDAYS, min_periods=MDAYS).max()).astype(float)
    cnt = (d1.fillna(0) + d2.fillna(0) + d3.fillna(0) + d4.fillna(0)).where(p_new, np.nan)
    return cnt


# ============================================================
# Bucket H — Williams %R variants (059-066)
# ============================================================

def f26_stwf_059_williams_r_14(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical Williams %R(14) — inverted stoch on [-100, 0]."""
    return _williams_r(high, low, close, 14)


def f26_stwf_060_williams_r_21_monthly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R(21) — monthly horizon (distinct concept from 14)."""
    return _williams_r(high, low, close, MDAYS)


def f26_stwf_061_williams_r_63_quarterly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R(63) — quarterly horizon."""
    return _williams_r(high, low, close, QDAYS)


def f26_stwf_062_williams_r_252_annual(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R(252) — annual horizon."""
    return _williams_r(high, low, close, YDAYS)


def f26_stwf_063_williams_r_above_minus20_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R(14) > -20 — Williams-OB state indicator."""
    wr = _williams_r(high, low, close, 14)
    return (wr > -20.0).astype(float).where(wr.notna(), np.nan)


def f26_stwf_064_williams_r_just_exited_above_minus20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R crossed back below -20 this bar — Williams OB-exit trigger."""
    wr = _williams_r(high, low, close, 14)
    return ((wr.shift(1) > -20.0) & (wr <= -20.0)).astype(float).where(wr.notna(), np.nan)


def f26_stwf_065_williams_r_dwell_above_minus20_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with Williams %R > -20 — Williams OB dwell."""
    wr = _williams_r(high, low, close, 14)
    return (wr > -20.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(wr.notna(), np.nan)


def f26_stwf_066_williams_r_bars_since_topped(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Williams %R reached its 252d max — recency of Williams peak."""
    wr = _williams_r(high, low, close, 14)
    at_max = wr == wr.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


# ============================================================
# Bucket I — Stoch RSI variants (067-075)
# ============================================================

def f26_stwf_067_stoch_rsi_k_14(close: pd.Series) -> pd.Series:
    """Classical Stoch-RSI %K(14,14,3,3) — momentum-of-RSI level."""
    k, _ = _stoch_rsi_kd(close)
    return k


def f26_stwf_068_stoch_rsi_d_14(close: pd.Series) -> pd.Series:
    """Stoch-RSI %D smoothed line."""
    _, d = _stoch_rsi_kd(close)
    return d


def f26_stwf_069_stoch_rsi_k_minus_d(close: pd.Series) -> pd.Series:
    """Stoch-RSI K - D differential — momentum-of-RSI cross magnitude."""
    k, d = _stoch_rsi_kd(close)
    return k - d


def f26_stwf_070_stoch_rsi_in_ob80_state(close: pd.Series) -> pd.Series:
    """1 if Stoch-RSI K > 80 — momentum-of-RSI OB."""
    k, _ = _stoch_rsi_kd(close)
    return (k > 80.0).astype(float).where(k.notna(), np.nan)


def f26_stwf_071_stoch_rsi_just_exited_ob80(close: pd.Series) -> pd.Series:
    """Stoch-RSI K just crossed back below 80 — momentum-of-RSI OB-exit trigger."""
    k, _ = _stoch_rsi_kd(close)
    return ((k.shift(1) > 80.0) & (k <= 80.0)).astype(float).where(k.notna(), np.nan)


def f26_stwf_072_stoch_rsi_dwell_ob80_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with Stoch-RSI K > 80 — momentum-of-RSI OB dwell."""
    k, _ = _stoch_rsi_kd(close)
    return (k > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(k.notna(), np.nan)


def f26_stwf_073_stoch_rsi_bars_since_topped(close: pd.Series) -> pd.Series:
    """Bars since Stoch-RSI K reached 252d max — recency of momentum-of-RSI peak."""
    k, _ = _stoch_rsi_kd(close)
    at_max = k == k.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f26_stwf_074_stoch_rsi_peak_decay_63(close: pd.Series) -> pd.Series:
    """Stoch-RSI K 63d-max minus its value 63 bars ago — quarterly momentum-of-RSI peak decay."""
    k, _ = _stoch_rsi_kd(close)
    pmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f26_stwf_075_stoch_rsi_cumulative_ob_area_252(close: pd.Series) -> pd.Series:
    """Sum of (K - 80) over OB bars past 252 — momentum-of-RSI saturation intensity."""
    k, _ = _stoch_rsi_kd(close)
    area = (k - 80.0).clip(lower=0).where(k.notna(), np.nan)
    return area.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 001-075
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_BASE_REGISTRY_001_075 = {
    "f26_stwf_001_fast_k_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_001_fast_k_14},
    "f26_stwf_002_fast_k_5_weekly": {"inputs": ["high", "low", "close"], "func": f26_stwf_002_fast_k_5_weekly},
    "f26_stwf_003_fast_k_63_quarterly": {"inputs": ["high", "low", "close"], "func": f26_stwf_003_fast_k_63_quarterly},
    "f26_stwf_004_fast_k_252_annual": {"inputs": ["high", "low", "close"], "func": f26_stwf_004_fast_k_252_annual},
    "f26_stwf_005_slow_d_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_005_slow_d_14},
    "f26_stwf_006_slow_d_63_quarterly": {"inputs": ["high", "low", "close"], "func": f26_stwf_006_slow_d_63_quarterly},
    "f26_stwf_007_slow_d_252_annual": {"inputs": ["high", "low", "close"], "func": f26_stwf_007_slow_d_252_annual},
    "f26_stwf_008_full_stoch_d_14_5_5": {"inputs": ["high", "low", "close"], "func": f26_stwf_008_full_stoch_d_14_5_5},
    "f26_stwf_009_k_minus_d_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_009_k_minus_d_14},
    "f26_stwf_010_k_minus_d_63_quarterly": {"inputs": ["high", "low", "close"], "func": f26_stwf_010_k_minus_d_63_quarterly},
    "f26_stwf_011_bearish_cross_indicator_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_011_bearish_cross_indicator_14},
    "f26_stwf_012_bearish_cross_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_012_bearish_cross_count_63},
    "f26_stwf_013_bars_since_last_bearish_cross_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_013_bars_since_last_bearish_cross_14},
    "f26_stwf_014_bullish_cross_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_014_bullish_cross_count_63},
    "f26_stwf_015_cross_density_net_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_015_cross_density_net_63},
    "f26_stwf_016_stoch_in_ob80_14_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_016_stoch_in_ob80_14_state},
    "f26_stwf_017_stoch_in_extreme_ob90_14_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_017_stoch_in_extreme_ob90_14_state},
    "f26_stwf_018_stoch_in_ob80_63_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_018_stoch_in_ob80_63_state},
    "f26_stwf_019_stoch_in_ob80_252_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_019_stoch_in_ob80_252_state},
    "f26_stwf_020_williams_r_in_ob_state_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_020_williams_r_in_ob_state_14},
    "f26_stwf_021_stoch_above_q95_distribution_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_021_stoch_above_q95_distribution_252},
    "f26_stwf_022_stoch_above_q99_distribution_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_022_stoch_above_q99_distribution_252},
    "f26_stwf_023_kd_both_above_80_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_023_kd_both_above_80_state},
    "f26_stwf_024_just_exited_ob80_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_024_just_exited_ob80_14},
    "f26_stwf_025_bars_since_last_ob80_exit_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_025_bars_since_last_ob80_exit_14},
    "f26_stwf_026_count_ob80_exits_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_026_count_ob80_exits_63},
    "f26_stwf_027_count_ob80_exits_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_027_count_ob80_exits_252},
    "f26_stwf_028_bars_since_last_extreme_ob90_exit": {"inputs": ["high", "low", "close"], "func": f26_stwf_028_bars_since_last_extreme_ob90_exit},
    "f26_stwf_029_just_exited_ob80_63_quarterly": {"inputs": ["high", "low", "close"], "func": f26_stwf_029_just_exited_ob80_63_quarterly},
    "f26_stwf_030_ob_exit_velocity_drop_from_peak_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_030_ob_exit_velocity_drop_from_peak_21},
    "f26_stwf_031_failed_retest_lower_ob_peak_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_031_failed_retest_lower_ob_peak_63},
    "f26_stwf_032_fraction_time_in_ob80_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_032_fraction_time_in_ob80_21},
    "f26_stwf_033_fraction_time_in_ob80_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_033_fraction_time_in_ob80_63},
    "f26_stwf_034_fraction_time_in_ob80_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_034_fraction_time_in_ob80_252},
    "f26_stwf_035_longest_ob80_run_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_035_longest_ob80_run_252},
    "f26_stwf_036_current_ob80_streak": {"inputs": ["high", "low", "close"], "func": f26_stwf_036_current_ob80_streak},
    "f26_stwf_037_distinct_ob80_sessions_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_037_distinct_ob80_sessions_252},
    "f26_stwf_038_avg_ob80_session_duration_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_038_avg_ob80_session_duration_252},
    "f26_stwf_039_cumulative_ob_area_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_039_cumulative_ob_area_252},
    "f26_stwf_040_peak_decay_21": {"inputs": ["high", "low", "close"], "func": f26_stwf_040_peak_decay_21},
    "f26_stwf_041_peak_decay_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_041_peak_decay_63},
    "f26_stwf_042_count_lower_high_peaks_ob_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_042_count_lower_high_peaks_ob_63},
    "f26_stwf_043_count_lower_high_peaks_ob_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_043_count_lower_high_peaks_ob_252},
    "f26_stwf_044_compression_high_minus_low_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_044_compression_high_minus_low_63},
    "f26_stwf_045_failed_to_reach_prior_max_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_045_failed_to_reach_prior_max_63},
    "f26_stwf_046_peak_amplitude_decay_ratio_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_046_peak_amplitude_decay_ratio_63},
    "f26_stwf_047_recent_ob_peak_height_zscore_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_047_recent_ob_peak_height_zscore_252},
    "f26_stwf_048_price_vs_stochk_div_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_048_price_vs_stochk_div_63},
    "f26_stwf_049_price_vs_stochk_div_252": {"inputs": ["high", "low", "close"], "func": f26_stwf_049_price_vs_stochk_div_252},
    "f26_stwf_050_price_vs_stochd_div_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_050_price_vs_stochd_div_63},
    "f26_stwf_051_rolling_corr_price_stochk_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_051_rolling_corr_price_stochk_63},
    "f26_stwf_052_count_price_new_21h_with_k_not_ob_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_052_count_price_new_21h_with_k_not_ob_63},
    "f26_stwf_053_amplitude_last_bearish_div_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_053_amplitude_last_bearish_div_63},
    "f26_stwf_054_bars_since_last_bearish_div_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_054_bars_since_last_bearish_div_63},
    "f26_stwf_055_williams_r_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_055_williams_r_div_vs_price_63},
    "f26_stwf_056_stoch_rsi_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_056_stoch_rsi_div_vs_price_63},
    "f26_stwf_057_ultimate_osc_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_057_ultimate_osc_div_vs_price_63},
    "f26_stwf_058_multi_oscillator_div_count_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_058_multi_oscillator_div_count_63},
    "f26_stwf_059_williams_r_14": {"inputs": ["high", "low", "close"], "func": f26_stwf_059_williams_r_14},
    "f26_stwf_060_williams_r_21_monthly": {"inputs": ["high", "low", "close"], "func": f26_stwf_060_williams_r_21_monthly},
    "f26_stwf_061_williams_r_63_quarterly": {"inputs": ["high", "low", "close"], "func": f26_stwf_061_williams_r_63_quarterly},
    "f26_stwf_062_williams_r_252_annual": {"inputs": ["high", "low", "close"], "func": f26_stwf_062_williams_r_252_annual},
    "f26_stwf_063_williams_r_above_minus20_state": {"inputs": ["high", "low", "close"], "func": f26_stwf_063_williams_r_above_minus20_state},
    "f26_stwf_064_williams_r_just_exited_above_minus20": {"inputs": ["high", "low", "close"], "func": f26_stwf_064_williams_r_just_exited_above_minus20},
    "f26_stwf_065_williams_r_dwell_above_minus20_63": {"inputs": ["high", "low", "close"], "func": f26_stwf_065_williams_r_dwell_above_minus20_63},
    "f26_stwf_066_williams_r_bars_since_topped": {"inputs": ["high", "low", "close"], "func": f26_stwf_066_williams_r_bars_since_topped},
    "f26_stwf_067_stoch_rsi_k_14": {"inputs": ["close"], "func": f26_stwf_067_stoch_rsi_k_14},
    "f26_stwf_068_stoch_rsi_d_14": {"inputs": ["close"], "func": f26_stwf_068_stoch_rsi_d_14},
    "f26_stwf_069_stoch_rsi_k_minus_d": {"inputs": ["close"], "func": f26_stwf_069_stoch_rsi_k_minus_d},
    "f26_stwf_070_stoch_rsi_in_ob80_state": {"inputs": ["close"], "func": f26_stwf_070_stoch_rsi_in_ob80_state},
    "f26_stwf_071_stoch_rsi_just_exited_ob80": {"inputs": ["close"], "func": f26_stwf_071_stoch_rsi_just_exited_ob80},
    "f26_stwf_072_stoch_rsi_dwell_ob80_63": {"inputs": ["close"], "func": f26_stwf_072_stoch_rsi_dwell_ob80_63},
    "f26_stwf_073_stoch_rsi_bars_since_topped": {"inputs": ["close"], "func": f26_stwf_073_stoch_rsi_bars_since_topped},
    "f26_stwf_074_stoch_rsi_peak_decay_63": {"inputs": ["close"], "func": f26_stwf_074_stoch_rsi_peak_decay_63},
    "f26_stwf_075_stoch_rsi_cumulative_ob_area_252": {"inputs": ["close"], "func": f26_stwf_075_stoch_rsi_cumulative_ob_area_252},
}


# === D2 wrappers + registry (001_075) ===
def f26_stwf_001_fast_k_14_d2(high, low, close): return f26_stwf_001_fast_k_14(high, low, close).diff().diff()
def f26_stwf_002_fast_k_5_weekly_d2(high, low, close): return f26_stwf_002_fast_k_5_weekly(high, low, close).diff().diff()
def f26_stwf_003_fast_k_63_quarterly_d2(high, low, close): return f26_stwf_003_fast_k_63_quarterly(high, low, close).diff().diff()
def f26_stwf_004_fast_k_252_annual_d2(high, low, close): return f26_stwf_004_fast_k_252_annual(high, low, close).diff().diff()
def f26_stwf_005_slow_d_14_d2(high, low, close): return f26_stwf_005_slow_d_14(high, low, close).diff().diff()
def f26_stwf_006_slow_d_63_quarterly_d2(high, low, close): return f26_stwf_006_slow_d_63_quarterly(high, low, close).diff().diff()
def f26_stwf_007_slow_d_252_annual_d2(high, low, close): return f26_stwf_007_slow_d_252_annual(high, low, close).diff().diff()
def f26_stwf_008_full_stoch_d_14_5_5_d2(high, low, close): return f26_stwf_008_full_stoch_d_14_5_5(high, low, close).diff().diff()
def f26_stwf_009_k_minus_d_14_d2(high, low, close): return f26_stwf_009_k_minus_d_14(high, low, close).diff().diff()
def f26_stwf_010_k_minus_d_63_quarterly_d2(high, low, close): return f26_stwf_010_k_minus_d_63_quarterly(high, low, close).diff().diff()
def f26_stwf_011_bearish_cross_indicator_14_d2(high, low, close): return f26_stwf_011_bearish_cross_indicator_14(high, low, close).diff().diff()
def f26_stwf_012_bearish_cross_count_63_d2(high, low, close): return f26_stwf_012_bearish_cross_count_63(high, low, close).diff().diff()
def f26_stwf_013_bars_since_last_bearish_cross_14_d2(high, low, close): return f26_stwf_013_bars_since_last_bearish_cross_14(high, low, close).diff().diff()
def f26_stwf_014_bullish_cross_count_63_d2(high, low, close): return f26_stwf_014_bullish_cross_count_63(high, low, close).diff().diff()
def f26_stwf_015_cross_density_net_63_d2(high, low, close): return f26_stwf_015_cross_density_net_63(high, low, close).diff().diff()
def f26_stwf_016_stoch_in_ob80_14_state_d2(high, low, close): return f26_stwf_016_stoch_in_ob80_14_state(high, low, close).diff().diff()
def f26_stwf_017_stoch_in_extreme_ob90_14_state_d2(high, low, close): return f26_stwf_017_stoch_in_extreme_ob90_14_state(high, low, close).diff().diff()
def f26_stwf_018_stoch_in_ob80_63_state_d2(high, low, close): return f26_stwf_018_stoch_in_ob80_63_state(high, low, close).diff().diff()
def f26_stwf_019_stoch_in_ob80_252_state_d2(high, low, close): return f26_stwf_019_stoch_in_ob80_252_state(high, low, close).diff().diff()
def f26_stwf_020_williams_r_in_ob_state_14_d2(high, low, close): return f26_stwf_020_williams_r_in_ob_state_14(high, low, close).diff().diff()
def f26_stwf_021_stoch_above_q95_distribution_252_d2(high, low, close): return f26_stwf_021_stoch_above_q95_distribution_252(high, low, close).diff().diff()
def f26_stwf_022_stoch_above_q99_distribution_252_d2(high, low, close): return f26_stwf_022_stoch_above_q99_distribution_252(high, low, close).diff().diff()
def f26_stwf_023_kd_both_above_80_state_d2(high, low, close): return f26_stwf_023_kd_both_above_80_state(high, low, close).diff().diff()
def f26_stwf_024_just_exited_ob80_14_d2(high, low, close): return f26_stwf_024_just_exited_ob80_14(high, low, close).diff().diff()
def f26_stwf_025_bars_since_last_ob80_exit_14_d2(high, low, close): return f26_stwf_025_bars_since_last_ob80_exit_14(high, low, close).diff().diff()
def f26_stwf_026_count_ob80_exits_63_d2(high, low, close): return f26_stwf_026_count_ob80_exits_63(high, low, close).diff().diff()
def f26_stwf_027_count_ob80_exits_252_d2(high, low, close): return f26_stwf_027_count_ob80_exits_252(high, low, close).diff().diff()
def f26_stwf_028_bars_since_last_extreme_ob90_exit_d2(high, low, close): return f26_stwf_028_bars_since_last_extreme_ob90_exit(high, low, close).diff().diff()
def f26_stwf_029_just_exited_ob80_63_quarterly_d2(high, low, close): return f26_stwf_029_just_exited_ob80_63_quarterly(high, low, close).diff().diff()
def f26_stwf_030_ob_exit_velocity_drop_from_peak_21_d2(high, low, close): return f26_stwf_030_ob_exit_velocity_drop_from_peak_21(high, low, close).diff().diff()
def f26_stwf_031_failed_retest_lower_ob_peak_63_d2(high, low, close): return f26_stwf_031_failed_retest_lower_ob_peak_63(high, low, close).diff().diff()
def f26_stwf_032_fraction_time_in_ob80_21_d2(high, low, close): return f26_stwf_032_fraction_time_in_ob80_21(high, low, close).diff().diff()
def f26_stwf_033_fraction_time_in_ob80_63_d2(high, low, close): return f26_stwf_033_fraction_time_in_ob80_63(high, low, close).diff().diff()
def f26_stwf_034_fraction_time_in_ob80_252_d2(high, low, close): return f26_stwf_034_fraction_time_in_ob80_252(high, low, close).diff().diff()
def f26_stwf_035_longest_ob80_run_252_d2(high, low, close): return f26_stwf_035_longest_ob80_run_252(high, low, close).diff().diff()
def f26_stwf_036_current_ob80_streak_d2(high, low, close): return f26_stwf_036_current_ob80_streak(high, low, close).diff().diff()
def f26_stwf_037_distinct_ob80_sessions_252_d2(high, low, close): return f26_stwf_037_distinct_ob80_sessions_252(high, low, close).diff().diff()
def f26_stwf_038_avg_ob80_session_duration_252_d2(high, low, close): return f26_stwf_038_avg_ob80_session_duration_252(high, low, close).diff().diff()
def f26_stwf_039_cumulative_ob_area_252_d2(high, low, close): return f26_stwf_039_cumulative_ob_area_252(high, low, close).diff().diff()
def f26_stwf_040_peak_decay_21_d2(high, low, close): return f26_stwf_040_peak_decay_21(high, low, close).diff().diff()
def f26_stwf_041_peak_decay_63_d2(high, low, close): return f26_stwf_041_peak_decay_63(high, low, close).diff().diff()
def f26_stwf_042_count_lower_high_peaks_ob_63_d2(high, low, close): return f26_stwf_042_count_lower_high_peaks_ob_63(high, low, close).diff().diff()
def f26_stwf_043_count_lower_high_peaks_ob_252_d2(high, low, close): return f26_stwf_043_count_lower_high_peaks_ob_252(high, low, close).diff().diff()
def f26_stwf_044_compression_high_minus_low_63_d2(high, low, close): return f26_stwf_044_compression_high_minus_low_63(high, low, close).diff().diff()
def f26_stwf_045_failed_to_reach_prior_max_63_d2(high, low, close): return f26_stwf_045_failed_to_reach_prior_max_63(high, low, close).diff().diff()
def f26_stwf_046_peak_amplitude_decay_ratio_63_d2(high, low, close): return f26_stwf_046_peak_amplitude_decay_ratio_63(high, low, close).diff().diff()
def f26_stwf_047_recent_ob_peak_height_zscore_252_d2(high, low, close): return f26_stwf_047_recent_ob_peak_height_zscore_252(high, low, close).diff().diff()
def f26_stwf_048_price_vs_stochk_div_63_d2(high, low, close): return f26_stwf_048_price_vs_stochk_div_63(high, low, close).diff().diff()
def f26_stwf_049_price_vs_stochk_div_252_d2(high, low, close): return f26_stwf_049_price_vs_stochk_div_252(high, low, close).diff().diff()
def f26_stwf_050_price_vs_stochd_div_63_d2(high, low, close): return f26_stwf_050_price_vs_stochd_div_63(high, low, close).diff().diff()
def f26_stwf_051_rolling_corr_price_stochk_63_d2(high, low, close): return f26_stwf_051_rolling_corr_price_stochk_63(high, low, close).diff().diff()
def f26_stwf_052_count_price_new_21h_with_k_not_ob_63_d2(high, low, close): return f26_stwf_052_count_price_new_21h_with_k_not_ob_63(high, low, close).diff().diff()
def f26_stwf_053_amplitude_last_bearish_div_63_d2(high, low, close): return f26_stwf_053_amplitude_last_bearish_div_63(high, low, close).diff().diff()
def f26_stwf_054_bars_since_last_bearish_div_63_d2(high, low, close): return f26_stwf_054_bars_since_last_bearish_div_63(high, low, close).diff().diff()
def f26_stwf_055_williams_r_div_vs_price_63_d2(high, low, close): return f26_stwf_055_williams_r_div_vs_price_63(high, low, close).diff().diff()
def f26_stwf_056_stoch_rsi_div_vs_price_63_d2(high, low, close): return f26_stwf_056_stoch_rsi_div_vs_price_63(high, low, close).diff().diff()
def f26_stwf_057_ultimate_osc_div_vs_price_63_d2(high, low, close): return f26_stwf_057_ultimate_osc_div_vs_price_63(high, low, close).diff().diff()
def f26_stwf_058_multi_oscillator_div_count_63_d2(high, low, close): return f26_stwf_058_multi_oscillator_div_count_63(high, low, close).diff().diff()
def f26_stwf_059_williams_r_14_d2(high, low, close): return f26_stwf_059_williams_r_14(high, low, close).diff().diff()
def f26_stwf_060_williams_r_21_monthly_d2(high, low, close): return f26_stwf_060_williams_r_21_monthly(high, low, close).diff().diff()
def f26_stwf_061_williams_r_63_quarterly_d2(high, low, close): return f26_stwf_061_williams_r_63_quarterly(high, low, close).diff().diff()
def f26_stwf_062_williams_r_252_annual_d2(high, low, close): return f26_stwf_062_williams_r_252_annual(high, low, close).diff().diff()
def f26_stwf_063_williams_r_above_minus20_state_d2(high, low, close): return f26_stwf_063_williams_r_above_minus20_state(high, low, close).diff().diff()
def f26_stwf_064_williams_r_just_exited_above_minus20_d2(high, low, close): return f26_stwf_064_williams_r_just_exited_above_minus20(high, low, close).diff().diff()
def f26_stwf_065_williams_r_dwell_above_minus20_63_d2(high, low, close): return f26_stwf_065_williams_r_dwell_above_minus20_63(high, low, close).diff().diff()
def f26_stwf_066_williams_r_bars_since_topped_d2(high, low, close): return f26_stwf_066_williams_r_bars_since_topped(high, low, close).diff().diff()
def f26_stwf_067_stoch_rsi_k_14_d2(close): return f26_stwf_067_stoch_rsi_k_14(close).diff().diff()
def f26_stwf_068_stoch_rsi_d_14_d2(close): return f26_stwf_068_stoch_rsi_d_14(close).diff().diff()
def f26_stwf_069_stoch_rsi_k_minus_d_d2(close): return f26_stwf_069_stoch_rsi_k_minus_d(close).diff().diff()
def f26_stwf_070_stoch_rsi_in_ob80_state_d2(close): return f26_stwf_070_stoch_rsi_in_ob80_state(close).diff().diff()
def f26_stwf_071_stoch_rsi_just_exited_ob80_d2(close): return f26_stwf_071_stoch_rsi_just_exited_ob80(close).diff().diff()
def f26_stwf_072_stoch_rsi_dwell_ob80_63_d2(close): return f26_stwf_072_stoch_rsi_dwell_ob80_63(close).diff().diff()
def f26_stwf_073_stoch_rsi_bars_since_topped_d2(close): return f26_stwf_073_stoch_rsi_bars_since_topped(close).diff().diff()
def f26_stwf_074_stoch_rsi_peak_decay_63_d2(close): return f26_stwf_074_stoch_rsi_peak_decay_63(close).diff().diff()
def f26_stwf_075_stoch_rsi_cumulative_ob_area_252_d2(close): return f26_stwf_075_stoch_rsi_cumulative_ob_area_252(close).diff().diff()

STOCHASTIC_WILLIAMS_FAMILY_D2_REGISTRY_001_075 = {
    "f26_stwf_001_fast_k_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_001_fast_k_14_d2},
    "f26_stwf_002_fast_k_5_weekly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_002_fast_k_5_weekly_d2},
    "f26_stwf_003_fast_k_63_quarterly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_003_fast_k_63_quarterly_d2},
    "f26_stwf_004_fast_k_252_annual_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_004_fast_k_252_annual_d2},
    "f26_stwf_005_slow_d_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_005_slow_d_14_d2},
    "f26_stwf_006_slow_d_63_quarterly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_006_slow_d_63_quarterly_d2},
    "f26_stwf_007_slow_d_252_annual_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_007_slow_d_252_annual_d2},
    "f26_stwf_008_full_stoch_d_14_5_5_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_008_full_stoch_d_14_5_5_d2},
    "f26_stwf_009_k_minus_d_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_009_k_minus_d_14_d2},
    "f26_stwf_010_k_minus_d_63_quarterly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_010_k_minus_d_63_quarterly_d2},
    "f26_stwf_011_bearish_cross_indicator_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_011_bearish_cross_indicator_14_d2},
    "f26_stwf_012_bearish_cross_count_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_012_bearish_cross_count_63_d2},
    "f26_stwf_013_bars_since_last_bearish_cross_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_013_bars_since_last_bearish_cross_14_d2},
    "f26_stwf_014_bullish_cross_count_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_014_bullish_cross_count_63_d2},
    "f26_stwf_015_cross_density_net_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_015_cross_density_net_63_d2},
    "f26_stwf_016_stoch_in_ob80_14_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_016_stoch_in_ob80_14_state_d2},
    "f26_stwf_017_stoch_in_extreme_ob90_14_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_017_stoch_in_extreme_ob90_14_state_d2},
    "f26_stwf_018_stoch_in_ob80_63_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_018_stoch_in_ob80_63_state_d2},
    "f26_stwf_019_stoch_in_ob80_252_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_019_stoch_in_ob80_252_state_d2},
    "f26_stwf_020_williams_r_in_ob_state_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_020_williams_r_in_ob_state_14_d2},
    "f26_stwf_021_stoch_above_q95_distribution_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_021_stoch_above_q95_distribution_252_d2},
    "f26_stwf_022_stoch_above_q99_distribution_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_022_stoch_above_q99_distribution_252_d2},
    "f26_stwf_023_kd_both_above_80_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_023_kd_both_above_80_state_d2},
    "f26_stwf_024_just_exited_ob80_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_024_just_exited_ob80_14_d2},
    "f26_stwf_025_bars_since_last_ob80_exit_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_025_bars_since_last_ob80_exit_14_d2},
    "f26_stwf_026_count_ob80_exits_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_026_count_ob80_exits_63_d2},
    "f26_stwf_027_count_ob80_exits_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_027_count_ob80_exits_252_d2},
    "f26_stwf_028_bars_since_last_extreme_ob90_exit_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_028_bars_since_last_extreme_ob90_exit_d2},
    "f26_stwf_029_just_exited_ob80_63_quarterly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_029_just_exited_ob80_63_quarterly_d2},
    "f26_stwf_030_ob_exit_velocity_drop_from_peak_21_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_030_ob_exit_velocity_drop_from_peak_21_d2},
    "f26_stwf_031_failed_retest_lower_ob_peak_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_031_failed_retest_lower_ob_peak_63_d2},
    "f26_stwf_032_fraction_time_in_ob80_21_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_032_fraction_time_in_ob80_21_d2},
    "f26_stwf_033_fraction_time_in_ob80_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_033_fraction_time_in_ob80_63_d2},
    "f26_stwf_034_fraction_time_in_ob80_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_034_fraction_time_in_ob80_252_d2},
    "f26_stwf_035_longest_ob80_run_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_035_longest_ob80_run_252_d2},
    "f26_stwf_036_current_ob80_streak_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_036_current_ob80_streak_d2},
    "f26_stwf_037_distinct_ob80_sessions_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_037_distinct_ob80_sessions_252_d2},
    "f26_stwf_038_avg_ob80_session_duration_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_038_avg_ob80_session_duration_252_d2},
    "f26_stwf_039_cumulative_ob_area_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_039_cumulative_ob_area_252_d2},
    "f26_stwf_040_peak_decay_21_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_040_peak_decay_21_d2},
    "f26_stwf_041_peak_decay_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_041_peak_decay_63_d2},
    "f26_stwf_042_count_lower_high_peaks_ob_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_042_count_lower_high_peaks_ob_63_d2},
    "f26_stwf_043_count_lower_high_peaks_ob_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_043_count_lower_high_peaks_ob_252_d2},
    "f26_stwf_044_compression_high_minus_low_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_044_compression_high_minus_low_63_d2},
    "f26_stwf_045_failed_to_reach_prior_max_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_045_failed_to_reach_prior_max_63_d2},
    "f26_stwf_046_peak_amplitude_decay_ratio_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_046_peak_amplitude_decay_ratio_63_d2},
    "f26_stwf_047_recent_ob_peak_height_zscore_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_047_recent_ob_peak_height_zscore_252_d2},
    "f26_stwf_048_price_vs_stochk_div_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_048_price_vs_stochk_div_63_d2},
    "f26_stwf_049_price_vs_stochk_div_252_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_049_price_vs_stochk_div_252_d2},
    "f26_stwf_050_price_vs_stochd_div_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_050_price_vs_stochd_div_63_d2},
    "f26_stwf_051_rolling_corr_price_stochk_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_051_rolling_corr_price_stochk_63_d2},
    "f26_stwf_052_count_price_new_21h_with_k_not_ob_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_052_count_price_new_21h_with_k_not_ob_63_d2},
    "f26_stwf_053_amplitude_last_bearish_div_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_053_amplitude_last_bearish_div_63_d2},
    "f26_stwf_054_bars_since_last_bearish_div_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_054_bars_since_last_bearish_div_63_d2},
    "f26_stwf_055_williams_r_div_vs_price_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_055_williams_r_div_vs_price_63_d2},
    "f26_stwf_056_stoch_rsi_div_vs_price_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_056_stoch_rsi_div_vs_price_63_d2},
    "f26_stwf_057_ultimate_osc_div_vs_price_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_057_ultimate_osc_div_vs_price_63_d2},
    "f26_stwf_058_multi_oscillator_div_count_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_058_multi_oscillator_div_count_63_d2},
    "f26_stwf_059_williams_r_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_059_williams_r_14_d2},
    "f26_stwf_060_williams_r_21_monthly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_060_williams_r_21_monthly_d2},
    "f26_stwf_061_williams_r_63_quarterly_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_061_williams_r_63_quarterly_d2},
    "f26_stwf_062_williams_r_252_annual_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_062_williams_r_252_annual_d2},
    "f26_stwf_063_williams_r_above_minus20_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_063_williams_r_above_minus20_state_d2},
    "f26_stwf_064_williams_r_just_exited_above_minus20_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_064_williams_r_just_exited_above_minus20_d2},
    "f26_stwf_065_williams_r_dwell_above_minus20_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_065_williams_r_dwell_above_minus20_63_d2},
    "f26_stwf_066_williams_r_bars_since_topped_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_066_williams_r_bars_since_topped_d2},
    "f26_stwf_067_stoch_rsi_k_14_d2": {"inputs": ["close"], "func": f26_stwf_067_stoch_rsi_k_14_d2},
    "f26_stwf_068_stoch_rsi_d_14_d2": {"inputs": ["close"], "func": f26_stwf_068_stoch_rsi_d_14_d2},
    "f26_stwf_069_stoch_rsi_k_minus_d_d2": {"inputs": ["close"], "func": f26_stwf_069_stoch_rsi_k_minus_d_d2},
    "f26_stwf_070_stoch_rsi_in_ob80_state_d2": {"inputs": ["close"], "func": f26_stwf_070_stoch_rsi_in_ob80_state_d2},
    "f26_stwf_071_stoch_rsi_just_exited_ob80_d2": {"inputs": ["close"], "func": f26_stwf_071_stoch_rsi_just_exited_ob80_d2},
    "f26_stwf_072_stoch_rsi_dwell_ob80_63_d2": {"inputs": ["close"], "func": f26_stwf_072_stoch_rsi_dwell_ob80_63_d2},
    "f26_stwf_073_stoch_rsi_bars_since_topped_d2": {"inputs": ["close"], "func": f26_stwf_073_stoch_rsi_bars_since_topped_d2},
    "f26_stwf_074_stoch_rsi_peak_decay_63_d2": {"inputs": ["close"], "func": f26_stwf_074_stoch_rsi_peak_decay_63_d2},
    "f26_stwf_075_stoch_rsi_cumulative_ob_area_252_d2": {"inputs": ["close"], "func": f26_stwf_075_stoch_rsi_cumulative_ob_area_252_d2},
}
