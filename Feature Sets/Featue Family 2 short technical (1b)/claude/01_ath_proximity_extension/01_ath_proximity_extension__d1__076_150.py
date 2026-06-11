"""ath_proximity_extension d1 features 076-150 — Pipeline 1b-technical.

Continues from __base__001_075.py: 75 more distinct hypotheses covering
Bucket G (statistical position) tail, Bucket H (Fibonacci/proportional),
Bucket I (prior-cycle / historical high), Bucket J (ATR-/sigma-/dollar-
normalized extension dynamics), Bucket K (stretched-state booleans), and
Bucket L (narrow ATH-proximity composites).

PIT-clean. Self-contained helpers. No cross-family imports.
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


def _swing_low_then_high(low: pd.Series, high: pd.Series, n: int = YDAYS, mp: int = QDAYS):
    """Helper: return (swing_low, swing_high) where the low is the n-bar min, the high
    is the n-bar max, anchored by the rolling window (PIT-safe right-anchored)."""
    rmin = low.rolling(n, min_periods=mp).min()
    rmax = high.rolling(n, min_periods=mp).max()
    return rmin, rmax


def f01_athx_076_tukey_fence_upper_breach_count_252d_d1(close: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where close > Q3 + 1.5*IQR (Tukey upper fence)
    computed on a 63d window — count of statistical 'outlier highs'."""
    q1 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    q3 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    iqr = q3 - q1
    fence = q3 + 1.5 * iqr
    breach = (close > fence).astype(float)
    return (breach.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f01_athx_077_cornish_fisher_adjusted_zscore_close_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher-adjusted z-score of close in 252d window (skew/kurt correction)."""
    m = close.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = close.rolling(YDAYS, min_periods=QDAYS).std()
    sk = close.rolling(YDAYS, min_periods=QDAYS).skew()
    ku = close.rolling(YDAYS, min_periods=QDAYS).kurt()  # excess
    z = _safe_div(close - m, sd)
    cf = z + (z * z - 1.0) * sk / 6.0 + (z ** 3 - 3.0 * z) * ku / 24.0 \
         - (2.0 * z ** 3 - 5.0 * z) * (sk * sk) / 36.0
    return (cf).diff()


def f01_athx_078_mahalanobis_dist_ohlc_at_high_252d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mahalanobis distance of today's OHLC vector vs 252d OHLC centroid.
    Uses diagonal covariance (variance-normalized) for tractability."""
    df = pd.concat([open_.rename("o"), high.rename("h"), low.rename("l"), close.rename("c")], axis=1)
    m = df.rolling(YDAYS, min_periods=QDAYS).mean()
    v = df.rolling(YDAYS, min_periods=QDAYS).var()
    diff = df - m
    sq = (diff ** 2) / v.replace(0, np.nan)
    return (np.sqrt(sq.sum(axis=1, min_count=4))).diff()


def f01_athx_079_dist_from_252d_mean_in_iqr_units_d1(close: pd.Series) -> pd.Series:
    """(close - 252d mean) / 252d IQR — robust extension in IQR units."""
    m = close.rolling(YDAYS, min_periods=QDAYS).mean()
    q1 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q3 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    iqr = q3 - q1
    return (_safe_div(close - m, iqr)).diff()


def f01_athx_080_dist_from_252d_trimmed_mean_5pct_d1(close: pd.Series) -> pd.Series:
    """Distance of close from 5%-trimmed mean of 252d window, normalized by trimmed std."""
    def _tstats(w):
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            return np.nan
        v = np.sort(v)
        k = max(1, int(0.05 * v.size))
        vt = v[k:-k] if k > 0 and v.size > 2 * k else v
        if vt.size == 0:
            return np.nan
        return float(vt.mean())
    def _tstd(w):
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            return np.nan
        v = np.sort(v)
        k = max(1, int(0.05 * v.size))
        vt = v[k:-k] if k > 0 and v.size > 2 * k else v
        if vt.size < 2:
            return np.nan
        return float(vt.std(ddof=1))
    tm = close.rolling(YDAYS, min_periods=QDAYS).apply(_tstats, raw=True)
    ts = close.rolling(YDAYS, min_periods=QDAYS).apply(_tstd, raw=True)
    return (_safe_div(close - tm, ts)).diff()


def f01_athx_081_dist_from_252d_trimmed_mean_10pct_d1(close: pd.Series) -> pd.Series:
    """Distance of close from 10%-trimmed mean of 252d window, normalized by trimmed std."""
    def _tstats(w):
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            return np.nan
        v = np.sort(v)
        k = max(1, int(0.10 * v.size))
        vt = v[k:-k] if k > 0 and v.size > 2 * k else v
        if vt.size == 0:
            return np.nan
        return float(vt.mean())
    def _tstd(w):
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            return np.nan
        v = np.sort(v)
        k = max(1, int(0.10 * v.size))
        vt = v[k:-k] if k > 0 and v.size > 2 * k else v
        if vt.size < 2:
            return np.nan
        return float(vt.std(ddof=1))
    tm = close.rolling(YDAYS, min_periods=QDAYS).apply(_tstats, raw=True)
    ts = close.rolling(YDAYS, min_periods=QDAYS).apply(_tstd, raw=True)
    return (_safe_div(close - tm, ts)).diff()


def f01_athx_082_studentized_residual_close_vs_252d_linear_fit_d1(close: pd.Series) -> pd.Series:
    """Studentized residual: (close - 252d linear-fit prediction) / 252d residual std.
    Distance from the local trend at the current peak."""
    n = YDAYS
    def _stu(w):
        v = w[~np.isnan(w)]
        if v.size < QDAYS:
            return np.nan
        x = np.arange(v.size, dtype=float)
        xm = x.mean(); ym = v.mean()
        sx = ((x - xm) ** 2).sum()
        if sx == 0:
            return np.nan
        b = ((x - xm) * (v - ym)).sum() / sx
        a = ym - b * xm
        resid = v - (a + b * x)
        s = resid[:-1].std(ddof=1) if resid.size > 1 else np.nan
        if not np.isfinite(s) or s == 0:
            return np.nan
        return float(resid[-1] / s)
    return (close.rolling(n, min_periods=QDAYS).apply(_stu, raw=True)).diff()


def f01_athx_083_percentile_rank_close_in_2520d_d1(close: pd.Series) -> pd.Series:
    """Empirical percentile rank of close in trailing ~10y (2520d) distribution
    — very-long-horizon stretch indicator."""
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return (close.rolling(2520, min_periods=YDAYS).apply(_rk, raw=True)).diff()


def f01_athx_084_fib_extension_0618_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - swing_low) / (swing_high - swing_low) - 1.0 minus 0.618 fib level
    — distance from the 0.618 retracement *above* the swing-high baseline.
    Positive = beyond the 61.8% extension above the prior swing."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 0.618 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_085_fib_extension_1000_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 1.000 extension (= swing_low + 2*amp) of prior 252d swing."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 1.000 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_086_fib_extension_1382_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 1.382 extension."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 1.382 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_087_fib_extension_1618_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 1.618 'golden' extension."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 1.618 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_088_fib_extension_2000_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 2.000 extension."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 2.000 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_089_fib_extension_2618_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 2.618 extension (extreme blowoff target)."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 2.618 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_090_fib_extension_4236_of_prior_252d_swing_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position relative to the 4.236 'parabolic blowoff' extension."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 4.236 * amp
    return (_safe_div(close - ext_lvl, amp)).diff()


def f01_athx_091_cumulative_swing_amplitude_overshoot_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many times the prior 252d swing-amplitude does close overshoot above
    the swing high: (close - swing_high) / amp."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    return (_safe_div(close - rmax, amp)).diff()


def f01_athx_092_dist_from_1382_fib_extension_atr_units_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance from the 1.382 fib extension anchor."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    amp = rmax - rmin
    ext_lvl = rmax + 1.382 * amp
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ext_lvl, atr)).diff()


def f01_athx_093_proportional_extension_ratio_vs_prior_cycle_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current cycle's extension (close above its 252d swing-high) divided by the
    median extension realized in the prior 1260d. Higher = stretching beyond
    historical comparable runs."""
    rmin, rmax = _swing_low_then_high(low, high, YDAYS, QDAYS)
    cur_ext = (close - rmax).clip(lower=0)
    cur_ext_rel = _safe_div(cur_ext, rmax)
    median_ext = cur_ext_rel.rolling(DDAYS_5Y, min_periods=YDAYS).median()
    return (_safe_div(cur_ext_rel, median_ext)).diff()


def f01_athx_094_ratio_current_to_prior_252d_high_d1(high: pd.Series) -> pd.Series:
    """Current 252d high / prior-distinct 252d high (looking back 252d further)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prior = rmax.shift(YDAYS)
    return (_safe_div(rmax, prior)).diff()


def f01_athx_095_ratio_current_to_prior_63d_high_d1(high: pd.Series) -> pd.Series:
    """Current 63d high / prior 63d high (shifted by 63 bars)."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    prior = rmax.shift(QDAYS)
    return (_safe_div(rmax, prior)).diff()


def f01_athx_096_ratio_current_to_prior_1260d_high_d1(high: pd.Series) -> pd.Series:
    """Current 1260d (5y) high / prior 1260d high (shifted by 1260 bars)."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    prior = rmax.shift(DDAYS_5Y)
    return (_safe_div(rmax, prior)).diff()


def f01_athx_097_distinct_252d_max_resets_in_1260d_d1(high: pd.Series) -> pd.Series:
    """Number of distinct strict 252d-max upward resets in trailing 1260d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    resets = (rmax.diff() > 0).astype(float)
    return (resets.rolling(DDAYS_5Y, min_periods=YDAYS).sum()).diff()


def f01_athx_098_mean_bars_between_252d_max_resets_1260d_d1(high: pd.Series) -> pd.Series:
    """Mean bars between 252d-max upward resets in trailing 1260d window."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    resets = (rmax.diff() > 0).astype(float)
    def _mg(w):
        idx = np.where(w > 0)[0]
        if idx.size < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return (resets.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_mg, raw=True)).diff()


def f01_athx_099_prior_cycle_amp_over_current_cycle_amp_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """(prior 252d swing amplitude) / (current 252d swing amplitude)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    amp = rmax - rmin
    prior_amp = amp.shift(YDAYS)
    return (_safe_div(prior_amp, amp)).diff()


def f01_athx_100_cycle_relative_position_current_advance_vs_median_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current advance amplitude (close - 252d low) divided by the median
    historical 252d swing amplitude over the past 1260d."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    amp = rmax - rmin
    med_amp = amp.rolling(DDAYS_5Y, min_periods=YDAYS).median()
    current_adv = (close - rmin).clip(lower=0)
    return (_safe_div(current_adv, med_amp)).diff()


def f01_athx_101_bars_since_prior_1260d_max_d1(high: pd.Series) -> pd.Series:
    """Bars since the 1260d (5y) rolling max — recency of the prior multi-year peak."""
    def _bsm(w):
        if np.isnan(w).all():
            return np.nan
        return float((len(w) - 1) - int(np.nanargmax(w)))
    return (high.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_bsm, raw=True)).diff()


def f01_athx_102_sequence_rank_of_current_alltime_peak_d1(high: pd.Series) -> pd.Series:
    """How many distinct prior all-time-high resets have occurred so far
    (i.e. 1 if today's price equals first lifetime high, 2 if it's the second new ATH,
    etc.). Bars where price is not at a new ATH carry forward the prior rank."""
    arr = high.to_numpy(copy=True)
    n = len(arr)
    out = np.full(n, np.nan, dtype=float)
    cur_max = -np.inf
    rank = 0
    for i in range(n):
        v = arr[i]
        if not np.isnan(v):
            if v > cur_max:
                rank += 1
                cur_max = v
            out[i] = float(rank) if rank > 0 else np.nan
    return (pd.Series(out, index=high.index)).diff()


def f01_athx_103_inter_peak_interval_zscore_1260d_d1(high: pd.Series) -> pd.Series:
    """Z-score of the latest inter-252d-max-reset interval vs the distribution of
    intervals over the trailing 1260d window."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    resets = (rmax.diff() > 0).astype(float)
    def _z_last_gap(w):
        idx = np.where(w > 0)[0]
        if idx.size < 4:
            return np.nan
        gaps = np.diff(idx).astype(float)
        last = gaps[-1]
        m = gaps[:-1].mean()
        s = gaps[:-1].std(ddof=1)
        if not np.isfinite(s) or s == 0:
            return np.nan
        return float((last - m) / s)
    return (resets.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_z_last_gap, raw=True)).diff()


def f01_athx_104_atr21_units_close_above_252d_max_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many 21d-ATR units close is above the 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff()


def f01_athx_105_atr63_units_close_above_alltime_max_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many 63d-ATR units close is above the expanding all-time max."""
    rmax = high.expanding(min_periods=QDAYS).max()
    atr = _atr(high, low, close, n=QDAYS)
    return (_safe_div(close - rmax, atr)).diff()


def f01_athx_106_realized_sigma_units_close_above_252d_max_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """How many 252d realized-sigma units close is above the 252d max (return-sigma scale)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ret = _safe_log(close).diff()
    sig = ret.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(_safe_log(close) - _safe_log(rmax), sig)).diff()


def f01_athx_107_dollar_ext_above_252d_max_over_recent_intraday_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d max) / median 21d intraday range — extension in units of
    typical recent daily range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).rolling(MDAYS, min_periods=WDAYS).median()
    return (_safe_div(close - rmax, rng)).diff()


def f01_athx_108_std_of_extension_over_21d_when_at_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d std of (log close - log 252d max) — volatility of the extension state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ext = _safe_log(close) - _safe_log(rmax)
    return (ext.rolling(MDAYS, min_periods=WDAYS).std()).diff()


def f01_athx_109_extension_percentile_rank_in_504d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's log-extension above 252d max vs the trailing
    504d distribution of that extension."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ext = _safe_log(close) - _safe_log(rmax)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return (ext.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)).diff()


def f01_athx_110_extension_acceleration_21d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d change in the log-extension above 252d max — extension accelerating?"""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ext = _safe_log(close) - _safe_log(rmax)
    return (ext - ext.shift(MDAYS)).diff()


def f01_athx_111_consecutive_bars_extension_positive_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Current streak length: consecutive bars with close > 252d max (strict extension)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_ext = (close > rmax).astype(float).to_numpy(copy=True)
    has_rmax = rmax.notna().to_numpy(copy=True)
    n = len(is_ext)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if not has_rmax[i]:
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if is_ext[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=high.index)).diff()


def f01_athx_112_extension_to_range_ratio_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d max) / (252d max - 252d min) — extension as fraction of cycle range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - rmax, rmax - rmin)).diff()


def f01_athx_113_multi_horizon_extended_count_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {21,63,126,252,504} where close > that horizon's high
    (close in strict extension territory)."""
    pieces = []
    for hz, mp in [(MDAYS, WDAYS), (QDAYS, MDAYS), (126, QDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS)]:
        rmax = high.rolling(hz, min_periods=mp).max()
        pieces.append(((close > rmax).astype(float)).rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return (df.sum(axis=1)).diff()


def f01_athx_114_extension_decay_rate_after_peak_21d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of log-extension above 252d max — negative slope = decaying off peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ext = _safe_log(close) - _safe_log(rmax)
    return (_rolling_slope(ext, MDAYS)).diff()


def f01_athx_115_atr21_units_close_above_5y_max_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many 21d-ATR units close is above the 1260d (5y) max — secular extension in vol units."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - rmax, atr)).diff()


def f01_athx_116_within_1pct_of_252d_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 1% of 252d max — 'fully stretched' state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= 0.99 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_117_within_2pct_of_252d_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 2% of 252d max — 'near-stretched' state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= 0.98 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_118_within_5pct_of_252d_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 5% of 252d max — 'approaching peak' state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= 0.95 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_119_within_10pct_of_252d_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 10% of 252d max — broad 'in-the-zone' state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= 0.90 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_120_within_1pct_of_alltime_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 1% of expanding all-time max."""
    rmax = high.expanding(min_periods=QDAYS).max()
    return ((high >= 0.99 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_121_within_2pct_of_alltime_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 2% of expanding all-time max."""
    rmax = high.expanding(min_periods=QDAYS).max()
    return ((high >= 0.98 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_122_within_5pct_of_alltime_max_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if high within 5% of expanding all-time max."""
    rmax = high.expanding(min_periods=QDAYS).max()
    return ((high >= 0.95 * rmax).astype(float).where(rmax.notna(), np.nan)).diff()


def f01_athx_123_first_touch_5pct_of_ath_after_180d_absence_d1(high: pd.Series) -> pd.Series:
    """1 if today is the first bar in 180+ days that touched within 5% of expanding ATH."""
    rmax = high.expanding(min_periods=QDAYS).max()
    in_zone = (high >= 0.95 * rmax).astype(float)
    prior_180_count = in_zone.shift(1).rolling(180, min_periods=60).sum()
    return (((in_zone > 0) & (prior_180_count == 0)).astype(float).where(in_zone.notna() & prior_180_count.notna(), np.nan)).diff()


def f01_athx_124_stretched_and_aged_indicator_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (within 1% of 252d max) AND (the current advance from 252d low is >180 bars old).
    Captures 'stretched + extended-time-in-trend'."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    # Advance age = bars since the 252d-min was hit (low recency proxy)
    def _bsm_min(w):
        if np.isnan(w).all():
            return np.nan
        return float((len(w) - 1) - int(np.nanargmin(w)))
    bsm = close.rolling(YDAYS, min_periods=QDAYS).apply(_bsm_min, raw=True)
    aged = (bsm > 180).astype(float)
    return (((stretched > 0) & (aged > 0)).astype(float).where(stretched.notna() & aged.notna(), np.nan)).diff()


def f01_athx_125_stretched_and_lone_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if (within 1% of 252d max) AND (no new 252d max in the last 21 days) — lonely peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    is_nh = (high >= rmax).astype(float)
    recent_nh = is_nh.rolling(MDAYS, min_periods=WDAYS).sum()
    lone = (recent_nh == 0).astype(float)
    return (((stretched > 0) & (lone > 0)).astype(float).where(stretched.notna() & recent_nh.notna(), np.nan)).diff()


def f01_athx_126_stretched_cluster_21d_indicator_d1(high: pd.Series) -> pd.Series:
    """1 if trailing 21d had >=5 bars within 1% of 252d max — clustered top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    cnt = stretched.rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 5).astype(float).where(cnt.notna(), np.nan)).diff()


def f01_athx_127_newly_stretched_indicator_63d_d1(high: pd.Series) -> pd.Series:
    """1 if today is the first bar within 1% of 252d max in the last 63 days."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    prior_cnt = stretched.shift(1).rolling(QDAYS - 1, min_periods=MDAYS).sum()
    return (((stretched > 0) & (prior_cnt == 0)).astype(float).where(stretched.notna() & prior_cnt.notna(), np.nan)).diff()


def f01_athx_128_restretched_after_pullback_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if (within 1% of 252d max NOW) AND prior 21d contained at least one bar
    with low <= 0.95 * its-then-252d-max (i.e. a >=5% pullback occurred recently)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    drew_down_5pct = (low <= 0.95 * rmax).astype(float)
    pullback_recently = drew_down_5pct.shift(1).rolling(MDAYS, min_periods=WDAYS).sum()
    return (((stretched > 0) & (pullback_recently > 0)).astype(float).where(stretched.notna() & pullback_recently.notna(), np.nan)).diff()


def f01_athx_129_stretched_on_volume_confirmation_indicator_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (within 1% of 252d max) AND (volume > 252d median * 1.5) — stretched with volume."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    med_vol = volume.rolling(YDAYS, min_periods=QDAYS).median()
    high_vol = (volume > 1.5 * med_vol).astype(float)
    return (((stretched > 0) & (high_vol > 0)).astype(float).where(stretched.notna() & med_vol.notna(), np.nan)).diff()


def f01_athx_130_stretched_on_volume_dryup_indicator_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (within 1% of 252d max) AND (volume < 252d median) — stretched but volume dry."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    med_vol = volume.rolling(YDAYS, min_periods=QDAYS).median()
    dry = (volume < med_vol).astype(float)
    return (((stretched > 0) & (dry > 0)).astype(float).where(stretched.notna() & med_vol.notna(), np.nan)).diff()


def f01_athx_131_multi_horizon_top_decile_breadth_sum_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of in-top-decile-of-N-day-range indicators across {21,63,126,252,504,1260}."""
    pieces = []
    for hz, mp in [(MDAYS, WDAYS), (QDAYS, MDAYS), (126, QDAYS), (YDAYS, QDAYS),
                    (DDAYS_2Y, YDAYS), (DDAYS_5Y, YDAYS)]:
        rmax = high.rolling(hz, min_periods=mp).max()
        rmin = low.rolling(hz, min_periods=mp).min()
        pos = _safe_div(close - rmin, rmax - rmin)
        pieces.append(((pos >= 0.9).astype(float)).rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return (df.sum(axis=1)).diff()


def f01_athx_132_multi_threshold_stretched_state_composite_d1(high: pd.Series) -> pd.Series:
    """Count of stretched thresholds satisfied: within {1%,2%,5%,10%} of 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    s1 = (high >= 0.99 * rmax).astype(float)
    s2 = (high >= 0.98 * rmax).astype(float)
    s5 = (high >= 0.95 * rmax).astype(float)
    s10 = (high >= 0.90 * rmax).astype(float)
    return ((s1 + s2 + s5 + s10).where(rmax.notna(), np.nan)).diff()


def f01_athx_133_stretched_aged_vol_confirmed_composite_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stretched (within 1% of 252d max) + aged (bars-since-252d-low >180) + vol-confirmed (vol>1.5*median).
    Returns count 0-3."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    def _bsm_min(w):
        if np.isnan(w).all():
            return np.nan
        return float((len(w) - 1) - int(np.nanargmin(w)))
    bsm = close.rolling(YDAYS, min_periods=QDAYS).apply(_bsm_min, raw=True)
    aged = (bsm > 180).astype(float)
    med_vol = volume.rolling(YDAYS, min_periods=QDAYS).median()
    high_vol = (volume > 1.5 * med_vol).astype(float)
    return ((stretched + aged + high_vol).where(rmax.notna() & med_vol.notna(), np.nan)).diff()


def f01_athx_134_stretched_volume_dryup_composite_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Stretched (within 1% of 252d max) AND dryup (vol < 0.7 * 63d-median).
    Composite returns sum: 2 = both, 1 = stretched only, 0 = neither stretched nor dry."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    med_vol = volume.rolling(QDAYS, min_periods=MDAYS).median()
    dry = (volume < 0.7 * med_vol).astype(float)
    return ((stretched + dry * stretched).where(rmax.notna() & med_vol.notna(), np.nan)).diff()


def f01_athx_135_distance_percentile_aggregate_across_horizons_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean across horizons {21,63,126,252,504} of percentile-rank of (close - high_max_h)
    in the trailing 504d distribution of that signed-extension."""
    pieces = []
    for hz, mp in [(MDAYS, WDAYS), (QDAYS, MDAYS), (126, QDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS)]:
        rmax = high.rolling(hz, min_periods=mp).max()
        ext = _safe_log(close) - _safe_log(rmax)
        def _rk(w):
            if np.isnan(w).all():
                return np.nan
            last = w[-1]
            if np.isnan(last):
                return np.nan
            v = w[~np.isnan(w)]
            if v.size == 0:
                return np.nan
            return float((v <= last).sum()) / float(v.size)
        pieces.append(ext.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True).rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return (df.mean(axis=1)).diff()


def f01_athx_136_time_at_high_aggregate_d1(high: pd.Series) -> pd.Series:
    """Aggregate of trailing 21d dwell counts within {0.5%,1%,2%,5%} of 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pieces = []
    for thr, name in [(0.995, "p5"), (0.99, "p1"), (0.98, "p2"), (0.95, "p5b")]:
        st = (high >= thr * rmax).astype(float)
        pieces.append(st.rolling(MDAYS, min_periods=WDAYS).sum().rename(name))
    df = pd.concat(pieces, axis=1)
    return (df.sum(axis=1)).diff()


def f01_athx_137_dist_from_prior_cycle_high_zscore_aggregate_d1(high: pd.Series) -> pd.Series:
    """Z-score in 504d window of the ratio (current 252d high / prior 252d high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prior = rmax.shift(YDAYS)
    ratio = _safe_div(rmax, prior)
    return (_rolling_zscore(ratio, DDAYS_2Y, min_periods=YDAYS)).diff()


def f01_athx_138_newly_stretched_then_failed_count_63d_d1(high: pd.Series) -> pd.Series:
    """Count in trailing 63d of bars where a 'newly stretched within 1% of 252d max' event
    was immediately followed (within 5d) by a >2% drop from that high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    prior_zero = stretched.shift(1).rolling(QDAYS - 1, min_periods=MDAYS).sum()
    new_str = ((stretched > 0) & (prior_zero == 0)).astype(float)
    fwd_drop = (high.rolling(WDAYS, min_periods=2).max().shift(WDAYS) -
                high).fillna(np.nan)
    # Avoid forward-leak: instead measure that the *prior* bars confirmed a fail.
    # Use lookback: at time t, did a 'new_str' event happen at t-5..t-1 AND high now
    # has dropped >=2% from that event's high?
    arr_ns = new_str.to_numpy(copy=True)
    arr_h = high.to_numpy(copy=True)
    n = len(arr_h)
    out = np.full(n, 0.0)
    for i in range(n):
        if np.isnan(arr_h[i]):
            out[i] = np.nan
            continue
        cnt = 0
        for k in range(1, WDAYS + 1):
            j = i - k
            if j < 0:
                break
            if arr_ns[j] > 0 and not np.isnan(arr_h[j]):
                if (arr_h[j] - arr_h[i]) / arr_h[j] >= 0.02:
                    cnt += 1
        out[i] = float(cnt)
    res = pd.Series(out, index=high.index)
    return (res.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f01_athx_139_newly_stretched_then_extended_count_63d_d1(high: pd.Series) -> pd.Series:
    """Count in trailing 63d of 'new-stretched within 1% of 252d max' events that
    successfully *extended* (close > 252d max within next 5 days)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    prior_zero = stretched.shift(1).rolling(QDAYS - 1, min_periods=MDAYS).sum()
    new_str = ((stretched > 0) & (prior_zero == 0)).astype(float)
    arr_ns = new_str.to_numpy(copy=True)
    arr_h = high.to_numpy(copy=True)
    arr_rm = rmax.to_numpy(copy=True)
    n = len(arr_h)
    out = np.full(n, 0.0)
    for i in range(n):
        if np.isnan(arr_h[i]):
            out[i] = np.nan
            continue
        cnt = 0
        for k in range(1, WDAYS + 1):
            j = i - k
            if j < 0:
                break
            if arr_ns[j] > 0 and not np.isnan(arr_rm[j]):
                # At j, the bar was at 99% of its-then-252d-max; did some bar between
                # j+1..i strictly exceed that level?
                seg = arr_h[j + 1:i + 1]
                seg = seg[~np.isnan(seg)]
                if seg.size > 0 and seg.max() > arr_rm[j]:
                    cnt += 1
        out[i] = float(cnt)
    res = pd.Series(out, index=high.index)
    return (res.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f01_athx_140_stretched_state_persistence_length_d1(high: pd.Series) -> pd.Series:
    """Current run length of consecutive bars within 1% of 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_state = (high >= 0.99 * rmax).astype(float).to_numpy(copy=True)
    has = rmax.notna().to_numpy(copy=True)
    n = len(in_state)
    out = np.full(n, np.nan, dtype=float)
    streak = 0
    for i in range(n):
        if not has[i]:
            streak = 0
            out[i] = np.nan
        else:
            streak = streak + 1 if in_state[i] > 0 else 0
            out[i] = float(streak)
    return (pd.Series(out, index=high.index)).diff()


def f01_athx_141_stretched_after_long_absence_ratio_d1(high: pd.Series) -> pd.Series:
    """(current consecutive stretched-state length) / (length of the gap before this state).
    High when we abruptly re-enter the zone after a long absence."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_state = (high >= 0.99 * rmax).astype(float).to_numpy(copy=True)
    has = rmax.notna().to_numpy(copy=True)
    n = len(in_state)
    cur_streak = np.full(n, 0.0)
    cur_gap = np.full(n, 0.0)
    s = 0
    g = 0
    last_gap_at_entry = np.full(n, np.nan)
    for i in range(n):
        if not has[i]:
            s = 0; g = 0
            cur_streak[i] = np.nan
            cur_gap[i] = np.nan
            continue
        if in_state[i] > 0:
            if s == 0:
                last_gap_at_entry[i] = float(g)
            else:
                last_gap_at_entry[i] = last_gap_at_entry[i - 1] if i > 0 else np.nan
            s += 1
            g = 0
        else:
            s = 0
            g += 1
            last_gap_at_entry[i] = np.nan
        cur_streak[i] = float(s) if s > 0 else np.nan
        cur_gap[i] = float(g)
    out = cur_streak / np.where(last_gap_at_entry > 0, last_gap_at_entry, np.nan)
    return (pd.Series(out, index=high.index)).diff()


def f01_athx_142_multi_anchor_extension_consensus_d1(high: pd.Series) -> pd.Series:
    """Count {YTD, 252d, 1260d, alltime} anchors where high is within 1% of that anchor's max.
    Range 0-4. Requires DatetimeIndex for YTD; falls back to NaN otherwise."""
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmax_5y = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmax_alltime = high.expanding(min_periods=QDAYS).max()
    s252 = (high >= 0.99 * rmax_252).astype(float)
    s5y = (high >= 0.99 * rmax_5y).astype(float)
    salltime = (high >= 0.99 * rmax_alltime).astype(float)
    if isinstance(high.index, pd.DatetimeIndex):
        year_id = pd.Series(high.index.year, index=high.index)
        ytd_max = high.groupby(year_id).cummax()
        sytd = (high >= 0.99 * ytd_max).astype(float)
    else:
        sytd = pd.Series(np.nan, index=high.index)
    return ((s252 + s5y + salltime + sytd).where(rmax_252.notna(), np.nan)).diff()


def f01_athx_143_cross_horizon_extension_dispersion_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Std across horizons {21,63,252,504,1260} of the log-extension above each horizon's max
    — disagreement between short and long anchors."""
    pieces = []
    for hz, mp in [(MDAYS, WDAYS), (QDAYS, MDAYS), (YDAYS, QDAYS), (DDAYS_2Y, YDAYS), (DDAYS_5Y, YDAYS)]:
        rmax = high.rolling(hz, min_periods=mp).max()
        ext = _safe_log(close) - _safe_log(rmax)
        pieces.append(ext.rename(f"h{hz}"))
    df = pd.concat(pieces, axis=1)
    return (df.std(axis=1)).diff()


def f01_athx_144_ath_proximity_fatigue_composite_d1(high: pd.Series) -> pd.Series:
    """Fatigue: stretched (within 1% of 252d max) + slowing new-high rate
    (recent 21d new-21d-high count BELOW the 63d-prior 21d new-21d-high count).
    Returns 2 if both conditions hold, 1 if only stretched, 0 otherwise."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    nh21 = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    recent_cnt = nh21.rolling(MDAYS, min_periods=WDAYS).sum()
    prior_cnt = nh21.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).sum()
    slowing = (recent_cnt < prior_cnt).astype(float)
    return ((stretched + slowing * stretched).where(stretched.notna() & slowing.notna(), np.nan)).diff()


def f01_athx_145_ath_proximity_acceleration_composite_d1(high: pd.Series) -> pd.Series:
    """Acceleration: stretched + accelerating new-high rate
    (recent 21d new-21d-high count ABOVE the prior 21d count)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched = (high >= 0.99 * rmax).astype(float)
    nh21 = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    recent_cnt = nh21.rolling(MDAYS, min_periods=WDAYS).sum()
    prior_cnt = nh21.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).sum()
    accel = (recent_cnt > prior_cnt).astype(float)
    return ((stretched + accel * stretched).where(stretched.notna() & accel.notna(), np.nan)).diff()


def f01_athx_146_ath_proximity_exhaustion_composite_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Exhaustion: stretched (within 1% of 252d max) + failed-retest
    (prior 5 bars: a bar got within 1% of 252d max AND today's low < 0.98 * 252d max).
    Returns 2 if both, 1 if stretched only, 0 otherwise."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    stretched_now = (high >= 0.99 * rmax).astype(float)
    near_recently = (high.shift(1).rolling(WDAYS, min_periods=2).max() >= 0.99 * rmax).astype(float)
    failed = ((near_recently > 0) & (low < 0.98 * rmax)).astype(float)
    return ((stretched_now + failed).where(rmax.notna(), np.nan)).diff()


def f01_athx_147_ath_proximity_terminal_state_composite_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal: 1 if ALL four sub-scores are above 90th percentile of 504d distribution:
    (distance-above-252d-max, age-of-advance, new-high-rate-63d, range-position-252d)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()

    dist = _safe_log(close) - _safe_log(rmax)
    def _bsm_min(w):
        if np.isnan(w).all():
            return np.nan
        return float((len(w) - 1) - int(np.nanargmin(w)))
    age = close.rolling(YDAYS, min_periods=QDAYS).apply(_bsm_min, raw=True)
    nh21 = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    nh_rate = nh21.rolling(QDAYS, min_periods=MDAYS).sum()
    rng_pos = _safe_div(close - rmin, rmax - rmin)

    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    r_dist = dist.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    r_age = age.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    r_nh = nh_rate.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    r_rng = rng_pos.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True)
    cond = ((r_dist > 0.9) & (r_age > 0.9) & (r_nh > 0.9) & (r_rng > 0.9)).astype(float)
    valid = r_dist.notna() & r_age.notna() & r_nh.notna() & r_rng.notna()
    return (cond.where(valid, np.nan)).diff()


def f01_athx_148_stretched_runlength_to_total_in_252d_ratio_d1(high: pd.Series) -> pd.Series:
    """Length of current consecutive stretched run / total bars stretched in 252d.
    Higher = today's stretch is unusually concentrated in time."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    st = (high >= 0.99 * rmax).astype(float).to_numpy(copy=True)
    has = rmax.notna().to_numpy(copy=True)
    n = len(st)
    cur = np.full(n, np.nan)
    s = 0
    for i in range(n):
        if not has[i]:
            s = 0
            cur[i] = np.nan
        else:
            s = s + 1 if st[i] > 0 else 0
            cur[i] = float(s)
    cur_s = pd.Series(cur, index=high.index)
    total = pd.Series(st, index=high.index).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(cur_s, total)).diff()


def f01_athx_149_consensus_extension_across_units_count_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of units in which today is 'extended' above the 252d max:
    {log>0, ATR>1, sigma>1, percent>2%}. Range 0-4."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    log_ext = _safe_log(close) - _safe_log(rmax)
    atr = _atr(high, low, close, n=MDAYS)
    atr_units = _safe_div(close - rmax, atr)
    ret = _safe_log(close).diff()
    sig = ret.rolling(QDAYS, min_periods=MDAYS).std()
    sig_units = _safe_div(log_ext, sig)
    pct = _safe_div(high - rmax, rmax)
    c1 = (log_ext > 0).astype(float)
    c2 = (atr_units > 1.0).astype(float)
    c3 = (sig_units > 1.0).astype(float)
    c4 = (pct > 0.02).astype(float)
    valid = rmax.notna() & atr.notna() & sig.notna()
    return ((c1 + c2 + c3 + c4).where(valid, np.nan)).diff()


def f01_athx_150_ath_proximity_aggregate_score_504d_zscore_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final ATH-proximity composite: equal-weighted sum of z-scores in 504d window of
    (log-dist-above-252d-max, range-position-252d, count-new-252d-highs-126d), then
    re-zscored across 504d. Captures stretch + leadership + cadence in one number."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    log_ext = _safe_log(close) - _safe_log(rmax)
    pos = _safe_div(close - rmin, rmax - rmin)
    is_nh = (high >= rmax).astype(float)
    rate = is_nh.rolling(126, min_periods=QDAYS).sum()

    z_e = _rolling_zscore(log_ext, DDAYS_2Y, min_periods=YDAYS)
    z_p = _rolling_zscore(pos, DDAYS_2Y, min_periods=YDAYS)
    z_r = _rolling_zscore(rate, DDAYS_2Y, min_periods=YDAYS)
    agg = z_e + z_p + z_r
    return (_rolling_zscore(agg, DDAYS_2Y, min_periods=YDAYS)).diff()

# ============================================================
#                         REGISTRY 076_150 (d1)
# ============================================================

ATH_PROXIMITY_EXTENSION_D1_REGISTRY_076_150 = {
    "f01_athx_076_tukey_fence_upper_breach_count_252d_d1": {"inputs": ["close"], "func": f01_athx_076_tukey_fence_upper_breach_count_252d_d1},
    "f01_athx_077_cornish_fisher_adjusted_zscore_close_252d_d1": {"inputs": ["close"], "func": f01_athx_077_cornish_fisher_adjusted_zscore_close_252d_d1},
    "f01_athx_078_mahalanobis_dist_ohlc_at_high_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f01_athx_078_mahalanobis_dist_ohlc_at_high_252d_d1},
    "f01_athx_079_dist_from_252d_mean_in_iqr_units_d1": {"inputs": ["close"], "func": f01_athx_079_dist_from_252d_mean_in_iqr_units_d1},
    "f01_athx_080_dist_from_252d_trimmed_mean_5pct_d1": {"inputs": ["close"], "func": f01_athx_080_dist_from_252d_trimmed_mean_5pct_d1},
    "f01_athx_081_dist_from_252d_trimmed_mean_10pct_d1": {"inputs": ["close"], "func": f01_athx_081_dist_from_252d_trimmed_mean_10pct_d1},
    "f01_athx_082_studentized_residual_close_vs_252d_linear_fit_d1": {"inputs": ["close"], "func": f01_athx_082_studentized_residual_close_vs_252d_linear_fit_d1},
    "f01_athx_083_percentile_rank_close_in_2520d_d1": {"inputs": ["close"], "func": f01_athx_083_percentile_rank_close_in_2520d_d1},
    "f01_athx_084_fib_extension_0618_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_084_fib_extension_0618_of_prior_252d_swing_d1},
    "f01_athx_085_fib_extension_1000_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_085_fib_extension_1000_of_prior_252d_swing_d1},
    "f01_athx_086_fib_extension_1382_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_086_fib_extension_1382_of_prior_252d_swing_d1},
    "f01_athx_087_fib_extension_1618_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_087_fib_extension_1618_of_prior_252d_swing_d1},
    "f01_athx_088_fib_extension_2000_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_088_fib_extension_2000_of_prior_252d_swing_d1},
    "f01_athx_089_fib_extension_2618_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_089_fib_extension_2618_of_prior_252d_swing_d1},
    "f01_athx_090_fib_extension_4236_of_prior_252d_swing_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_090_fib_extension_4236_of_prior_252d_swing_d1},
    "f01_athx_091_cumulative_swing_amplitude_overshoot_252d_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_091_cumulative_swing_amplitude_overshoot_252d_d1},
    "f01_athx_092_dist_from_1382_fib_extension_atr_units_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_092_dist_from_1382_fib_extension_atr_units_d1},
    "f01_athx_093_proportional_extension_ratio_vs_prior_cycle_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_093_proportional_extension_ratio_vs_prior_cycle_d1},
    "f01_athx_094_ratio_current_to_prior_252d_high_d1": {"inputs": ["high"], "func": f01_athx_094_ratio_current_to_prior_252d_high_d1},
    "f01_athx_095_ratio_current_to_prior_63d_high_d1": {"inputs": ["high"], "func": f01_athx_095_ratio_current_to_prior_63d_high_d1},
    "f01_athx_096_ratio_current_to_prior_1260d_high_d1": {"inputs": ["high"], "func": f01_athx_096_ratio_current_to_prior_1260d_high_d1},
    "f01_athx_097_distinct_252d_max_resets_in_1260d_d1": {"inputs": ["high"], "func": f01_athx_097_distinct_252d_max_resets_in_1260d_d1},
    "f01_athx_098_mean_bars_between_252d_max_resets_1260d_d1": {"inputs": ["high"], "func": f01_athx_098_mean_bars_between_252d_max_resets_1260d_d1},
    "f01_athx_099_prior_cycle_amp_over_current_cycle_amp_d1": {"inputs": ["high", "low"], "func": f01_athx_099_prior_cycle_amp_over_current_cycle_amp_d1},
    "f01_athx_100_cycle_relative_position_current_advance_vs_median_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_100_cycle_relative_position_current_advance_vs_median_d1},
    "f01_athx_101_bars_since_prior_1260d_max_d1": {"inputs": ["high"], "func": f01_athx_101_bars_since_prior_1260d_max_d1},
    "f01_athx_102_sequence_rank_of_current_alltime_peak_d1": {"inputs": ["high"], "func": f01_athx_102_sequence_rank_of_current_alltime_peak_d1},
    "f01_athx_103_inter_peak_interval_zscore_1260d_d1": {"inputs": ["high"], "func": f01_athx_103_inter_peak_interval_zscore_1260d_d1},
    "f01_athx_104_atr21_units_close_above_252d_max_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_104_atr21_units_close_above_252d_max_d1},
    "f01_athx_105_atr63_units_close_above_alltime_max_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_105_atr63_units_close_above_alltime_max_d1},
    "f01_athx_106_realized_sigma_units_close_above_252d_max_d1": {"inputs": ["high", "close"], "func": f01_athx_106_realized_sigma_units_close_above_252d_max_d1},
    "f01_athx_107_dollar_ext_above_252d_max_over_recent_intraday_range_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_107_dollar_ext_above_252d_max_over_recent_intraday_range_d1},
    "f01_athx_108_std_of_extension_over_21d_when_at_high_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_108_std_of_extension_over_21d_when_at_high_d1},
    "f01_athx_109_extension_percentile_rank_in_504d_d1": {"inputs": ["high", "close"], "func": f01_athx_109_extension_percentile_rank_in_504d_d1},
    "f01_athx_110_extension_acceleration_21d_d1": {"inputs": ["high", "close"], "func": f01_athx_110_extension_acceleration_21d_d1},
    "f01_athx_111_consecutive_bars_extension_positive_252d_d1": {"inputs": ["high", "close"], "func": f01_athx_111_consecutive_bars_extension_positive_252d_d1},
    "f01_athx_112_extension_to_range_ratio_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_112_extension_to_range_ratio_d1},
    "f01_athx_113_multi_horizon_extended_count_d1": {"inputs": ["high", "close"], "func": f01_athx_113_multi_horizon_extended_count_d1},
    "f01_athx_114_extension_decay_rate_after_peak_21d_d1": {"inputs": ["high", "close"], "func": f01_athx_114_extension_decay_rate_after_peak_21d_d1},
    "f01_athx_115_atr21_units_close_above_5y_max_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_115_atr21_units_close_above_5y_max_d1},
    "f01_athx_116_within_1pct_of_252d_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_116_within_1pct_of_252d_max_indicator_d1},
    "f01_athx_117_within_2pct_of_252d_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_117_within_2pct_of_252d_max_indicator_d1},
    "f01_athx_118_within_5pct_of_252d_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_118_within_5pct_of_252d_max_indicator_d1},
    "f01_athx_119_within_10pct_of_252d_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_119_within_10pct_of_252d_max_indicator_d1},
    "f01_athx_120_within_1pct_of_alltime_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_120_within_1pct_of_alltime_max_indicator_d1},
    "f01_athx_121_within_2pct_of_alltime_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_121_within_2pct_of_alltime_max_indicator_d1},
    "f01_athx_122_within_5pct_of_alltime_max_indicator_d1": {"inputs": ["high"], "func": f01_athx_122_within_5pct_of_alltime_max_indicator_d1},
    "f01_athx_123_first_touch_5pct_of_ath_after_180d_absence_d1": {"inputs": ["high"], "func": f01_athx_123_first_touch_5pct_of_ath_after_180d_absence_d1},
    "f01_athx_124_stretched_and_aged_indicator_d1": {"inputs": ["high", "close"], "func": f01_athx_124_stretched_and_aged_indicator_d1},
    "f01_athx_125_stretched_and_lone_indicator_d1": {"inputs": ["high"], "func": f01_athx_125_stretched_and_lone_indicator_d1},
    "f01_athx_126_stretched_cluster_21d_indicator_d1": {"inputs": ["high"], "func": f01_athx_126_stretched_cluster_21d_indicator_d1},
    "f01_athx_127_newly_stretched_indicator_63d_d1": {"inputs": ["high"], "func": f01_athx_127_newly_stretched_indicator_63d_d1},
    "f01_athx_128_restretched_after_pullback_indicator_d1": {"inputs": ["high", "low"], "func": f01_athx_128_restretched_after_pullback_indicator_d1},
    "f01_athx_129_stretched_on_volume_confirmation_indicator_d1": {"inputs": ["high", "close", "volume"], "func": f01_athx_129_stretched_on_volume_confirmation_indicator_d1},
    "f01_athx_130_stretched_on_volume_dryup_indicator_d1": {"inputs": ["high", "volume"], "func": f01_athx_130_stretched_on_volume_dryup_indicator_d1},
    "f01_athx_131_multi_horizon_top_decile_breadth_sum_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_131_multi_horizon_top_decile_breadth_sum_d1},
    "f01_athx_132_multi_threshold_stretched_state_composite_d1": {"inputs": ["high"], "func": f01_athx_132_multi_threshold_stretched_state_composite_d1},
    "f01_athx_133_stretched_aged_vol_confirmed_composite_d1": {"inputs": ["high", "close", "volume"], "func": f01_athx_133_stretched_aged_vol_confirmed_composite_d1},
    "f01_athx_134_stretched_volume_dryup_composite_d1": {"inputs": ["high", "volume"], "func": f01_athx_134_stretched_volume_dryup_composite_d1},
    "f01_athx_135_distance_percentile_aggregate_across_horizons_d1": {"inputs": ["high", "close"], "func": f01_athx_135_distance_percentile_aggregate_across_horizons_d1},
    "f01_athx_136_time_at_high_aggregate_d1": {"inputs": ["high"], "func": f01_athx_136_time_at_high_aggregate_d1},
    "f01_athx_137_dist_from_prior_cycle_high_zscore_aggregate_d1": {"inputs": ["high"], "func": f01_athx_137_dist_from_prior_cycle_high_zscore_aggregate_d1},
    "f01_athx_138_newly_stretched_then_failed_count_63d_d1": {"inputs": ["high"], "func": f01_athx_138_newly_stretched_then_failed_count_63d_d1},
    "f01_athx_139_newly_stretched_then_extended_count_63d_d1": {"inputs": ["high"], "func": f01_athx_139_newly_stretched_then_extended_count_63d_d1},
    "f01_athx_140_stretched_state_persistence_length_d1": {"inputs": ["high"], "func": f01_athx_140_stretched_state_persistence_length_d1},
    "f01_athx_141_stretched_after_long_absence_ratio_d1": {"inputs": ["high"], "func": f01_athx_141_stretched_after_long_absence_ratio_d1},
    "f01_athx_142_multi_anchor_extension_consensus_d1": {"inputs": ["high"], "func": f01_athx_142_multi_anchor_extension_consensus_d1},
    "f01_athx_143_cross_horizon_extension_dispersion_d1": {"inputs": ["high", "close"], "func": f01_athx_143_cross_horizon_extension_dispersion_d1},
    "f01_athx_144_ath_proximity_fatigue_composite_d1": {"inputs": ["high"], "func": f01_athx_144_ath_proximity_fatigue_composite_d1},
    "f01_athx_145_ath_proximity_acceleration_composite_d1": {"inputs": ["high"], "func": f01_athx_145_ath_proximity_acceleration_composite_d1},
    "f01_athx_146_ath_proximity_exhaustion_composite_d1": {"inputs": ["high", "low"], "func": f01_athx_146_ath_proximity_exhaustion_composite_d1},
    "f01_athx_147_ath_proximity_terminal_state_composite_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_147_ath_proximity_terminal_state_composite_d1},
    "f01_athx_148_stretched_runlength_to_total_in_252d_ratio_d1": {"inputs": ["high"], "func": f01_athx_148_stretched_runlength_to_total_in_252d_ratio_d1},
    "f01_athx_149_consensus_extension_across_units_count_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_149_consensus_extension_across_units_count_d1},
    "f01_athx_150_ath_proximity_aggregate_score_504d_zscore_d1": {"inputs": ["high", "low", "close"], "func": f01_athx_150_ath_proximity_aggregate_score_504d_zscore_d1},
}
