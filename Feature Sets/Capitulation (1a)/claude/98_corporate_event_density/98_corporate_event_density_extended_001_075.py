"""
98_corporate_event_density — Extended Features 001-075
Domain: 8-K / event-filing frequency — additional angles: burst recency and decay,
        gap-distribution statistics, half-life ratios, quantile-threshold exceedances,
        multi-window acceleration, drawdown-conditioned event clustering composites
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs to feature functions in this file are daily-frequency pandas Series
aligned to one shared daily trading-day index.

  event_count : daily count of corporate-event / SEC filing occurrences attributed
                to that date (8-K and similar event filings). Daily Series,
                non-negative integer-valued, mostly 0; spikes when distress-related
                corporate events cluster.
  close       : split/dividend-adjusted daily close price, USD.

Functions look strictly backward using .shift(positive), .rolling(), or
.expanding(). Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_TD_3Q    = 189
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _active_days(s: pd.Series, w: int) -> pd.Series:
    """Count of days with s > 0 in rolling window w."""
    return _rolling_sum((s > 0).astype(float), w)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum().astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional rolling-window event sums and means ---

def ced_ext_001_event_sum_3d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 3 trading days (very-short burst window)."""
    return _rolling_sum(event_count, 3)


def ced_ext_002_event_sum_7d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 7 trading days."""
    return _rolling_sum(event_count, 7)


def ced_ext_003_event_sum_45d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 45 trading days."""
    return _rolling_sum(event_count, 45)


def ced_ext_004_event_sum_189d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 189 trading days (3 quarters)."""
    return _rolling_sum(event_count, _TD_3Q)


def ced_ext_005_event_sum_1260d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 1260 trading days (5 years)."""
    return _rolling_sum(event_count, 1260)


def ced_ext_006_event_mean_3d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 3 trading days."""
    return _rolling_mean(event_count, 3)


def ced_ext_007_event_mean_45d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 45 trading days."""
    return _rolling_mean(event_count, 45)


def ced_ext_008_event_mean_189d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 189 trading days (3 quarters)."""
    return _rolling_mean(event_count, _TD_3Q)


def ced_ext_009_event_ewm_mean_5d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=5 (weekly half-life)."""
    return _ewm_mean(event_count, _TD_WK)


def ced_ext_010_event_ewm_mean_10d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=10 (2-week half-life)."""
    return _ewm_mean(event_count, 10)


def ced_ext_011_event_ewm_mean_126d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=126 (semi-annual half-life)."""
    return _ewm_mean(event_count, _TD_2Q)


def ced_ext_012_event_ewm_mean_504d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=504 (2-year half-life)."""
    return _ewm_mean(event_count, _TD_2Y)


# --- Group B (013-024): Burst recency, decay and inter-arrival timing ---

def ced_ext_013_days_since_event_log1p(event_count: pd.Series) -> pd.Series:
    """Log(1 + trading days since the most recent event)."""
    has_event = (event_count > 0).astype(float)
    gap = np.zeros(len(has_event), dtype=float)
    arr = has_event.values
    for i in range(1, len(arr)):
        gap[i] = 0.0 if arr[i] > 0 else gap[i - 1] + 1.0
    return np.log1p(pd.Series(gap, index=event_count.index))


def ced_ext_014_event_recency_inverse(event_count: pd.Series) -> pd.Series:
    """Inverse-recency score 1/(1+days since last event); high right after an event."""
    has_event = (event_count > 0).astype(float)
    gap = np.zeros(len(has_event), dtype=float)
    arr = has_event.values
    for i in range(1, len(arr)):
        gap[i] = 0.0 if arr[i] > 0 else gap[i - 1] + 1.0
    return 1.0 / (1.0 + pd.Series(gap, index=event_count.index))


def ced_ext_015_event_flag_decay_fast(event_count: pd.Series) -> pd.Series:
    """EWM-decayed event-occurrence flag with fast decay (span=10)."""
    return _ewm_mean((event_count > 0).astype(float), 10)


def ced_ext_016_event_flag_decay_slow(event_count: pd.Series) -> pd.Series:
    """EWM-decayed event-occurrence flag with slow decay (span=126)."""
    return _ewm_mean((event_count > 0).astype(float), _TD_2Q)


def ced_ext_017_event_inter_arrival_last_gap(event_count: pd.Series) -> pd.Series:
    """Trading-day gap between the two most recent event days (carried forward)."""
    arr = (event_count > 0).values
    idxs = [i for i in range(len(arr)) if arr[i]]
    out = np.full(len(arr), np.nan)
    for k in range(1, len(idxs)):
        gap = float(idxs[k] - idxs[k - 1])
        start = idxs[k]
        end = idxs[k + 1] if k + 1 < len(idxs) else len(arr)
        out[start:end] = gap
    return pd.Series(out, index=event_count.index)


def ced_ext_018_event_inter_arrival_mean_252d(event_count: pd.Series) -> pd.Series:
    """Mean trading-day gap between events over trailing 252 days (active days / window)."""
    active = _active_days(event_count, _TD_YEAR)
    return _safe_div(pd.Series(float(_TD_YEAR), index=event_count.index), active)


def ced_ext_019_event_burst_recency_252d(event_count: pd.Series) -> pd.Series:
    """Days since the most recent event, normalized by 252 then inverted (1=just happened)."""
    has_event = (event_count > 0).astype(float)
    gap = np.zeros(len(has_event), dtype=float)
    arr = has_event.values
    for i in range(1, len(arr)):
        gap[i] = 0.0 if arr[i] > 0 else gap[i - 1] + 1.0
    g = pd.Series(gap, index=event_count.index).clip(upper=float(_TD_YEAR))
    return 1.0 - g / float(_TD_YEAR)


def ced_ext_020_event_consecutive_active_streak(event_count: pd.Series) -> pd.Series:
    """Consecutive trading days with at least one event (active streak)."""
    return _consec_streak(event_count > 0)


def ced_ext_021_event_consecutive_quiet_streak(event_count: pd.Series) -> pd.Series:
    """Consecutive trading days with zero events (quiet streak)."""
    return _consec_streak(event_count == 0)


def ced_ext_022_event_active_streak_max_252d(event_count: pd.Series) -> pd.Series:
    """Longest run of consecutive active days within the trailing 252-day window."""
    streak = _consec_streak(event_count > 0)
    return _rolling_max(streak, _TD_YEAR)


def ced_ext_023_event_days_since_spike_2sigma(event_count: pd.Series) -> pd.Series:
    """Trading days since event_count last exceeded its 252-day mean by 2 std."""
    m = _rolling_mean(event_count, _TD_YEAR)
    sd = _rolling_std(event_count, _TD_YEAR)
    spike = (event_count > m + 2.0 * sd).astype(float)
    gap = np.zeros(len(spike), dtype=float)
    arr = spike.values
    for i in range(1, len(arr)):
        gap[i] = 0.0 if arr[i] > 0 else gap[i - 1] + 1.0
    return pd.Series(gap, index=event_count.index)


def ced_ext_024_event_recent_burst_decay_weighted_21d(event_count: pd.Series) -> pd.Series:
    """Sum of event_count over 21 days with linearly decaying weights toward today."""
    w = np.arange(1, _TD_MO + 1, dtype=float)

    def _wsum(arr):
        n = len(arr)
        return float(np.dot(arr, w[-n:]))

    return event_count.rolling(_TD_MO, min_periods=1).apply(_wsum, raw=True)


# --- Group C (025-038): Quantile-threshold exceedances and dispersion ---

def ced_ext_025_event_above_p75_63d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds its trailing 63-day 75th percentile."""
    q = event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).quantile(0.75)
    return (event_count > q).astype(float)


def ced_ext_026_event_above_p90_252d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds its trailing 252-day 90th percentile."""
    q = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)
    return (event_count > q).astype(float)


def ced_ext_027_event_above_p95_252d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds its trailing 252-day 95th percentile."""
    q = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.95)
    return (event_count > q).astype(float)


def ced_ext_028_event_above_p90_252d_count_63d(event_count: pd.Series) -> pd.Series:
    """Count over trailing 63 days of days exceeding the 252-day 90th percentile."""
    q = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)
    return _rolling_sum((event_count > q).astype(float), _TD_QTR)


def ced_ext_029_event_q90_63d(event_count: pd.Series) -> pd.Series:
    """Trailing 63-day 90th percentile of event_count (upper-tail event rate)."""
    return event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).quantile(0.90)


def ced_ext_030_event_q90_252d(event_count: pd.Series) -> pd.Series:
    """Trailing 252-day 90th percentile of event_count."""
    return event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)


def ced_ext_031_event_excess_over_p90_252d(event_count: pd.Series) -> pd.Series:
    """event_count minus its trailing 252-day 90th percentile (upper-tail excess)."""
    q = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)
    return event_count - q


def ced_ext_032_event_range_63d(event_count: pd.Series) -> pd.Series:
    """Trailing 63-day event_count range (max minus min)."""
    return _rolling_max(event_count, _TD_QTR) - _rolling_min(event_count, _TD_QTR)


def ced_ext_033_event_range_252d(event_count: pd.Series) -> pd.Series:
    """Trailing 252-day event_count range (max minus min)."""
    return _rolling_max(event_count, _TD_YEAR) - _rolling_min(event_count, _TD_YEAR)


def ced_ext_034_event_mad_63d(event_count: pd.Series) -> pd.Series:
    """Mean absolute deviation of event_count from its 63-day mean."""
    m = _rolling_mean(event_count, _TD_QTR)
    return _rolling_mean((event_count - m).abs(), _TD_QTR)


def ced_ext_035_event_cv_126d(event_count: pd.Series) -> pd.Series:
    """Coefficient of variation of event_count over trailing 126 days (std / |mean|)."""
    m  = _rolling_mean(event_count, _TD_2Q)
    sd = _rolling_std(event_count, _TD_2Q)
    return _safe_div_abs(sd, m)


def ced_ext_036_event_std_126d(event_count: pd.Series) -> pd.Series:
    """Rolling std of event_count over trailing 126 days."""
    return _rolling_std(event_count, _TD_2Q)


def ced_ext_037_event_skew_proxy_252d(event_count: pd.Series) -> pd.Series:
    """Skewness proxy: (mean - median) / std of event_count over trailing 252 days."""
    m   = _rolling_mean(event_count, _TD_YEAR)
    med = _rolling_median(event_count, _TD_YEAR)
    sd  = _rolling_std(event_count, _TD_YEAR)
    return _safe_div(m - med, sd)


def ced_ext_038_event_max_over_std_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of trailing 252-day max event_count to its 252-day std (tail-spike sharpness)."""
    return _safe_div(_rolling_max(event_count, _TD_YEAR), _rolling_std(event_count, _TD_YEAR))


# --- Group D (039-052): Multi-window acceleration and ratio variants ---

def ced_ext_039_event_sum_5d_qoq_change(event_count: pd.Series) -> pd.Series:
    """Change in trailing 5-day event sum vs one quarter ago."""
    s = _rolling_sum(event_count, _TD_WK)
    return s - s.shift(_TD_QTR)


def ced_ext_040_event_sum_21d_qoq_change(event_count: pd.Series) -> pd.Series:
    """Change in trailing 21-day event sum vs one quarter ago."""
    s = _rolling_sum(event_count, _TD_MO)
    return s - s.shift(_TD_QTR)


def ced_ext_041_event_sum_63d_2q_change(event_count: pd.Series) -> pd.Series:
    """Change in trailing 63-day event sum vs two quarters ago."""
    s = _rolling_sum(event_count, _TD_QTR)
    return s - s.shift(_TD_2Q)


def ced_ext_042_event_mean_63d_acceleration(event_count: pd.Series) -> pd.Series:
    """Second difference of 63-day mean event rate over 63-day steps (event acceleration)."""
    m = _rolling_mean(event_count, _TD_QTR)
    d1 = m - m.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ced_ext_043_event_burst_ratio_3d_vs_63d(event_count: pd.Series) -> pd.Series:
    """Ratio of 3-day mean to 63-day mean event rate (sharp recent burst)."""
    return _safe_div(_rolling_mean(event_count, 3), _rolling_mean(event_count, _TD_QTR))


def ced_ext_044_event_burst_ratio_10d_vs_63d(event_count: pd.Series) -> pd.Series:
    """Ratio of 10-day mean to 63-day mean event rate."""
    return _safe_div(_rolling_mean(event_count, 10), _rolling_mean(event_count, _TD_QTR))


def ced_ext_045_event_burst_ratio_42d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 42-day mean to 252-day mean event rate (2-month burst vs annual base)."""
    return _safe_div(_rolling_mean(event_count, 42), _rolling_mean(event_count, _TD_YEAR))


def ced_ext_046_event_burst_ratio_63d_vs_756d(event_count: pd.Series) -> pd.Series:
    """Ratio of 63-day mean to 756-day mean event rate (quarterly vs 3-year base)."""
    return _safe_div(_rolling_mean(event_count, _TD_QTR), _rolling_mean(event_count, _TD_3Y))


def ced_ext_047_event_ewm_ratio_10d_vs_126d(event_count: pd.Series) -> pd.Series:
    """Ratio of fast (span=10) to slow (span=126) EWM event rate."""
    return _safe_div(_ewm_mean(event_count, 10), _ewm_mean(event_count, _TD_2Q))


def ced_ext_048_event_ewm_ratio_21d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day EWM event rate (monthly vs annual EWM base)."""
    return _safe_div(_ewm_mean(event_count, _TD_MO), _ewm_mean(event_count, _TD_YEAR))


def ced_ext_049_event_excess_over_p50_63d(event_count: pd.Series) -> pd.Series:
    """event_count minus its trailing 63-day median (excess over typical level)."""
    return event_count - _rolling_median(event_count, _TD_QTR)


def ced_ext_050_event_sum_21d_vs_504d_excess(event_count: pd.Series) -> pd.Series:
    """Trailing 21-day event sum minus 21d-equivalent share of the 504-day sum."""
    s21 = _rolling_sum(event_count, _TD_MO)
    base = _rolling_sum(event_count, _TD_2Y) * (float(_TD_MO) / float(_TD_2Y))
    return s21 - base


def ced_ext_051_event_zscore_diff_21d_minus_252d(event_count: pd.Series) -> pd.Series:
    """Difference between 21-day and 252-day z-scores of event_count (horizon spread)."""
    return _zscore_rolling(event_count, _TD_MO) - _zscore_rolling(event_count, _TD_YEAR)


def ced_ext_052_event_pct_rank_diff_63d_minus_252d(event_count: pd.Series) -> pd.Series:
    """Difference between 63-day and 252-day percentile ranks of event_count."""
    return _rolling_rank_pct(event_count, _TD_QTR) - _rolling_rank_pct(event_count, _TD_YEAR)


# --- Group E (053-064): Active-day, gap and clustering measures ---

def ced_ext_053_active_day_frac_10d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 10 days with at least one event."""
    return _active_days(event_count, 10) / 10.0


def ced_ext_054_active_day_frac_42d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 42 days with at least one event."""
    return _active_days(event_count, 42) / 42.0


def ced_ext_055_active_day_frac_189d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 189 days with at least one event."""
    return _active_days(event_count, _TD_3Q) / float(_TD_3Q)


def ced_ext_056_active_day_count_63d(event_count: pd.Series) -> pd.Series:
    """Count of days with at least one event in the trailing 63 days."""
    return _active_days(event_count, _TD_QTR)


def ced_ext_057_active_day_frac_change_63d(event_count: pd.Series) -> pd.Series:
    """Change in 63-day active-day fraction vs one quarter ago."""
    f = _active_days(event_count, _TD_QTR) / float(_TD_QTR)
    return f - f.shift(_TD_QTR)


def ced_ext_058_event_quiet_gap_max_63d(event_count: pd.Series) -> pd.Series:
    """Longest consecutive event-free streak within the trailing 63-day window."""
    quiet = (event_count == 0).astype(float)

    def _max_gap(arr):
        best = 0
        cur = 0
        for v in arr:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return quiet.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 4)).apply(_max_gap, raw=True)


def ced_ext_059_event_quiet_gap_max_756d(event_count: pd.Series) -> pd.Series:
    """Longest consecutive event-free streak within the trailing 756-day window."""
    quiet = (event_count == 0).astype(float)

    def _max_gap(arr):
        best = 0
        cur = 0
        for v in arr:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return quiet.rolling(_TD_3Y, min_periods=max(1, _TD_3Y // 4)).apply(_max_gap, raw=True)


def ced_ext_060_event_clustering_index_252d(event_count: pd.Series) -> pd.Series:
    """Variance-to-mean ratio of event_count over trailing 252 days (Fano factor; >1 = clustered)."""
    m  = _rolling_mean(event_count, _TD_YEAR)
    v  = _rolling_std(event_count, _TD_YEAR) ** 2
    return _safe_div(v, m)


def ced_ext_061_event_clustering_index_63d(event_count: pd.Series) -> pd.Series:
    """Variance-to-mean ratio of event_count over trailing 63 days (Fano factor)."""
    m  = _rolling_mean(event_count, _TD_QTR)
    v  = _rolling_std(event_count, _TD_QTR) ** 2
    return _safe_div(v, m)


def ced_ext_062_event_active_to_total_ratio_63d(event_count: pd.Series) -> pd.Series:
    """Total events divided by active-day count over trailing 63 days (events per active day)."""
    return _safe_div(_rolling_sum(event_count, _TD_QTR), _active_days(event_count, _TD_QTR))


def ced_ext_063_event_multi_day_active_flag(event_count: pd.Series) -> pd.Series:
    """1 when at least 3 of the last 5 days had events (sustained recent activity)."""
    return (_active_days(event_count, _TD_WK) >= 3).astype(float)


def ced_ext_064_event_active_frac_above_1y_base_flag(event_count: pd.Series) -> pd.Series:
    """1 when 21-day active-day fraction exceeds the 252-day active-day fraction."""
    f21  = _active_days(event_count, _TD_MO) / float(_TD_MO)
    f252 = _active_days(event_count, _TD_YEAR) / float(_TD_YEAR)
    return (f21 > f252).astype(float)


# --- Group F (065-075): Price-conditioned event density and composites ---

def ced_ext_065_event_sum_21d_during_drawdown(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21-day event sum counted only on days where close is below its 252-day mean."""
    in_dd = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_sum(event_count * in_dd, _TD_MO)


def ced_ext_066_event_sum_63d_during_deep_drawdown(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63-day event sum on days where close is >50% below its 252-day peak."""
    peak = _rolling_max(close, _TD_YEAR)
    deep = (_safe_div_abs(close - peak, peak) < -0.5).astype(float)
    return _rolling_sum(event_count * deep, _TD_QTR)


def ced_ext_067_event_density_near_3y_low(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """21-day event sum multiplied by proximity of close to its 756-day low (1=at low)."""
    mn = _rolling_min(close, _TD_3Y)
    mx = _rolling_max(close, _TD_3Y)
    proximity = 1.0 - _safe_div(close - mn, mx - mn)
    return _rolling_sum(event_count, _TD_MO) * proximity


def ced_ext_068_event_sum_x_neg_ret_21d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 21-day sum of event_count weighted by that day's negative log return magnitude."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    neg = (-lr).clip(lower=0.0)
    return _rolling_sum(event_count * neg, _TD_MO)


def ced_ext_069_event_corr_with_drawdown_126d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 126-day correlation between event_count and close drawdown from 252d peak."""
    peak = _rolling_max(close, _TD_YEAR)
    dd = _safe_div_abs(close - peak, peak)
    return event_count.rolling(_TD_2Q, min_periods=max(2, _TD_2Q // 4)).corr(dd)


def ced_ext_070_event_burst_x_drawdown_flag(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """1 when event_count exceeds its 252-day 90th percentile AND close is below its 252-day mean."""
    q = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)
    in_dd = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return (event_count > q).astype(float) * in_dd


def ced_ext_071_event_sum_63d_x_pct_from_3y_high(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63-day event sum multiplied by close's percent shortfall from its 756-day high."""
    peak = _rolling_max(close, _TD_3Y)
    shortfall = _safe_div_abs(peak - close, peak).clip(lower=0.0)
    return _rolling_sum(event_count, _TD_QTR) * shortfall


def ced_ext_072_event_active_frac_x_below_2y_low_flag(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """63-day active-day fraction multiplied by a flag for close at its 504-day minimum."""
    f63 = _active_days(event_count, _TD_QTR) / float(_TD_QTR)
    at_low = (close <= _rolling_min(close, _TD_2Y) + _EPS).astype(float)
    return f63 * at_low


def ced_ext_073_event_intensity_scaled_by_volatility(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """21-day event sum divided by 21-day return volatility (events per unit of price risk)."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    vol = _rolling_std(lr, _TD_MO)
    return _safe_div(_rolling_sum(event_count, _TD_MO), vol)


def ced_ext_074_event_drawdown_burst_composite(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: event 63-day z-score times close percent drawdown from its 252-day peak."""
    z = _zscore_rolling(event_count, _TD_QTR)
    peak = _rolling_max(close, _TD_YEAR)
    dd = _safe_div_abs(peak - close, peak).clip(lower=0.0)
    return z * dd


def ced_ext_075_event_density_capitulation_composite(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Composite capitulation score: mean of 5d/21d/63d event z-scores plus close's
    percent drawdown from its 756-day peak (higher = event burst amid deep drawdown)."""
    z5  = _zscore_rolling(event_count, _TD_WK)
    z21 = _zscore_rolling(event_count, _TD_MO)
    z63 = _zscore_rolling(event_count, _TD_QTR)
    peak = _rolling_max(close, _TD_3Y)
    dd = _safe_div_abs(peak - close, peak).clip(lower=0.0)
    return (z5 + z21 + z63) / 3.0 + dd


# ── Registry ──────────────────────────────────────────────────────────────────

CORPORATE_EVENT_DENSITY_EXTENDED_REGISTRY_001_075 = {
    "ced_ext_001_event_sum_3d":                  {"inputs": ["event_count"],          "func": ced_ext_001_event_sum_3d},
    "ced_ext_002_event_sum_7d":                  {"inputs": ["event_count"],          "func": ced_ext_002_event_sum_7d},
    "ced_ext_003_event_sum_45d":                 {"inputs": ["event_count"],          "func": ced_ext_003_event_sum_45d},
    "ced_ext_004_event_sum_189d":                {"inputs": ["event_count"],          "func": ced_ext_004_event_sum_189d},
    "ced_ext_005_event_sum_1260d":               {"inputs": ["event_count"],          "func": ced_ext_005_event_sum_1260d},
    "ced_ext_006_event_mean_3d":                 {"inputs": ["event_count"],          "func": ced_ext_006_event_mean_3d},
    "ced_ext_007_event_mean_45d":                {"inputs": ["event_count"],          "func": ced_ext_007_event_mean_45d},
    "ced_ext_008_event_mean_189d":               {"inputs": ["event_count"],          "func": ced_ext_008_event_mean_189d},
    "ced_ext_009_event_ewm_mean_5d":             {"inputs": ["event_count"],          "func": ced_ext_009_event_ewm_mean_5d},
    "ced_ext_010_event_ewm_mean_10d":            {"inputs": ["event_count"],          "func": ced_ext_010_event_ewm_mean_10d},
    "ced_ext_011_event_ewm_mean_126d":           {"inputs": ["event_count"],          "func": ced_ext_011_event_ewm_mean_126d},
    "ced_ext_012_event_ewm_mean_504d":           {"inputs": ["event_count"],          "func": ced_ext_012_event_ewm_mean_504d},
    "ced_ext_013_days_since_event_log1p":        {"inputs": ["event_count"],          "func": ced_ext_013_days_since_event_log1p},
    "ced_ext_014_event_recency_inverse":         {"inputs": ["event_count"],          "func": ced_ext_014_event_recency_inverse},
    "ced_ext_015_event_flag_decay_fast":         {"inputs": ["event_count"],          "func": ced_ext_015_event_flag_decay_fast},
    "ced_ext_016_event_flag_decay_slow":         {"inputs": ["event_count"],          "func": ced_ext_016_event_flag_decay_slow},
    "ced_ext_017_event_inter_arrival_last_gap":  {"inputs": ["event_count"],          "func": ced_ext_017_event_inter_arrival_last_gap},
    "ced_ext_018_event_inter_arrival_mean_252d": {"inputs": ["event_count"],          "func": ced_ext_018_event_inter_arrival_mean_252d},
    "ced_ext_019_event_burst_recency_252d":      {"inputs": ["event_count"],          "func": ced_ext_019_event_burst_recency_252d},
    "ced_ext_020_event_consecutive_active_streak":{"inputs": ["event_count"],         "func": ced_ext_020_event_consecutive_active_streak},
    "ced_ext_021_event_consecutive_quiet_streak":{"inputs": ["event_count"],          "func": ced_ext_021_event_consecutive_quiet_streak},
    "ced_ext_022_event_active_streak_max_252d":  {"inputs": ["event_count"],          "func": ced_ext_022_event_active_streak_max_252d},
    "ced_ext_023_event_days_since_spike_2sigma": {"inputs": ["event_count"],          "func": ced_ext_023_event_days_since_spike_2sigma},
    "ced_ext_024_event_recent_burst_decay_weighted_21d":{"inputs": ["event_count"],   "func": ced_ext_024_event_recent_burst_decay_weighted_21d},
    "ced_ext_025_event_above_p75_63d_flag":      {"inputs": ["event_count"],          "func": ced_ext_025_event_above_p75_63d_flag},
    "ced_ext_026_event_above_p90_252d_flag":     {"inputs": ["event_count"],          "func": ced_ext_026_event_above_p90_252d_flag},
    "ced_ext_027_event_above_p95_252d_flag":     {"inputs": ["event_count"],          "func": ced_ext_027_event_above_p95_252d_flag},
    "ced_ext_028_event_above_p90_252d_count_63d":{"inputs": ["event_count"],          "func": ced_ext_028_event_above_p90_252d_count_63d},
    "ced_ext_029_event_q90_63d":                 {"inputs": ["event_count"],          "func": ced_ext_029_event_q90_63d},
    "ced_ext_030_event_q90_252d":                {"inputs": ["event_count"],          "func": ced_ext_030_event_q90_252d},
    "ced_ext_031_event_excess_over_p90_252d":    {"inputs": ["event_count"],          "func": ced_ext_031_event_excess_over_p90_252d},
    "ced_ext_032_event_range_63d":               {"inputs": ["event_count"],          "func": ced_ext_032_event_range_63d},
    "ced_ext_033_event_range_252d":              {"inputs": ["event_count"],          "func": ced_ext_033_event_range_252d},
    "ced_ext_034_event_mad_63d":                 {"inputs": ["event_count"],          "func": ced_ext_034_event_mad_63d},
    "ced_ext_035_event_cv_126d":                 {"inputs": ["event_count"],          "func": ced_ext_035_event_cv_126d},
    "ced_ext_036_event_std_126d":                {"inputs": ["event_count"],          "func": ced_ext_036_event_std_126d},
    "ced_ext_037_event_skew_proxy_252d":         {"inputs": ["event_count"],          "func": ced_ext_037_event_skew_proxy_252d},
    "ced_ext_038_event_max_over_std_252d":       {"inputs": ["event_count"],          "func": ced_ext_038_event_max_over_std_252d},
    "ced_ext_039_event_sum_5d_qoq_change":       {"inputs": ["event_count"],          "func": ced_ext_039_event_sum_5d_qoq_change},
    "ced_ext_040_event_sum_21d_qoq_change":      {"inputs": ["event_count"],          "func": ced_ext_040_event_sum_21d_qoq_change},
    "ced_ext_041_event_sum_63d_2q_change":       {"inputs": ["event_count"],          "func": ced_ext_041_event_sum_63d_2q_change},
    "ced_ext_042_event_mean_63d_acceleration":   {"inputs": ["event_count"],          "func": ced_ext_042_event_mean_63d_acceleration},
    "ced_ext_043_event_burst_ratio_3d_vs_63d":   {"inputs": ["event_count"],          "func": ced_ext_043_event_burst_ratio_3d_vs_63d},
    "ced_ext_044_event_burst_ratio_10d_vs_63d":  {"inputs": ["event_count"],          "func": ced_ext_044_event_burst_ratio_10d_vs_63d},
    "ced_ext_045_event_burst_ratio_42d_vs_252d": {"inputs": ["event_count"],          "func": ced_ext_045_event_burst_ratio_42d_vs_252d},
    "ced_ext_046_event_burst_ratio_63d_vs_756d": {"inputs": ["event_count"],          "func": ced_ext_046_event_burst_ratio_63d_vs_756d},
    "ced_ext_047_event_ewm_ratio_10d_vs_126d":   {"inputs": ["event_count"],          "func": ced_ext_047_event_ewm_ratio_10d_vs_126d},
    "ced_ext_048_event_ewm_ratio_21d_vs_252d":   {"inputs": ["event_count"],          "func": ced_ext_048_event_ewm_ratio_21d_vs_252d},
    "ced_ext_049_event_excess_over_p50_63d":     {"inputs": ["event_count"],          "func": ced_ext_049_event_excess_over_p50_63d},
    "ced_ext_050_event_sum_21d_vs_504d_excess":  {"inputs": ["event_count"],          "func": ced_ext_050_event_sum_21d_vs_504d_excess},
    "ced_ext_051_event_zscore_diff_21d_minus_252d":{"inputs": ["event_count"],        "func": ced_ext_051_event_zscore_diff_21d_minus_252d},
    "ced_ext_052_event_pct_rank_diff_63d_minus_252d":{"inputs": ["event_count"],      "func": ced_ext_052_event_pct_rank_diff_63d_minus_252d},
    "ced_ext_053_active_day_frac_10d":           {"inputs": ["event_count"],          "func": ced_ext_053_active_day_frac_10d},
    "ced_ext_054_active_day_frac_42d":           {"inputs": ["event_count"],          "func": ced_ext_054_active_day_frac_42d},
    "ced_ext_055_active_day_frac_189d":          {"inputs": ["event_count"],          "func": ced_ext_055_active_day_frac_189d},
    "ced_ext_056_active_day_count_63d":          {"inputs": ["event_count"],          "func": ced_ext_056_active_day_count_63d},
    "ced_ext_057_active_day_frac_change_63d":    {"inputs": ["event_count"],          "func": ced_ext_057_active_day_frac_change_63d},
    "ced_ext_058_event_quiet_gap_max_63d":       {"inputs": ["event_count"],          "func": ced_ext_058_event_quiet_gap_max_63d},
    "ced_ext_059_event_quiet_gap_max_756d":      {"inputs": ["event_count"],          "func": ced_ext_059_event_quiet_gap_max_756d},
    "ced_ext_060_event_clustering_index_252d":   {"inputs": ["event_count"],          "func": ced_ext_060_event_clustering_index_252d},
    "ced_ext_061_event_clustering_index_63d":    {"inputs": ["event_count"],          "func": ced_ext_061_event_clustering_index_63d},
    "ced_ext_062_event_active_to_total_ratio_63d":{"inputs": ["event_count"],         "func": ced_ext_062_event_active_to_total_ratio_63d},
    "ced_ext_063_event_multi_day_active_flag":   {"inputs": ["event_count"],          "func": ced_ext_063_event_multi_day_active_flag},
    "ced_ext_064_event_active_frac_above_1y_base_flag":{"inputs": ["event_count"],    "func": ced_ext_064_event_active_frac_above_1y_base_flag},
    "ced_ext_065_event_sum_21d_during_drawdown": {"inputs": ["event_count", "close"], "func": ced_ext_065_event_sum_21d_during_drawdown},
    "ced_ext_066_event_sum_63d_during_deep_drawdown":{"inputs": ["event_count", "close"],"func": ced_ext_066_event_sum_63d_during_deep_drawdown},
    "ced_ext_067_event_density_near_3y_low":     {"inputs": ["event_count", "close"], "func": ced_ext_067_event_density_near_3y_low},
    "ced_ext_068_event_sum_x_neg_ret_21d":       {"inputs": ["event_count", "close"], "func": ced_ext_068_event_sum_x_neg_ret_21d},
    "ced_ext_069_event_corr_with_drawdown_126d": {"inputs": ["event_count", "close"], "func": ced_ext_069_event_corr_with_drawdown_126d},
    "ced_ext_070_event_burst_x_drawdown_flag":   {"inputs": ["event_count", "close"], "func": ced_ext_070_event_burst_x_drawdown_flag},
    "ced_ext_071_event_sum_63d_x_pct_from_3y_high":{"inputs": ["event_count", "close"],"func": ced_ext_071_event_sum_63d_x_pct_from_3y_high},
    "ced_ext_072_event_active_frac_x_below_2y_low_flag":{"inputs": ["event_count", "close"],"func": ced_ext_072_event_active_frac_x_below_2y_low_flag},
    "ced_ext_073_event_intensity_scaled_by_volatility":{"inputs": ["event_count", "close"],"func": ced_ext_073_event_intensity_scaled_by_volatility},
    "ced_ext_074_event_drawdown_burst_composite":{"inputs": ["event_count", "close"], "func": ced_ext_074_event_drawdown_burst_composite},
    "ced_ext_075_event_density_capitulation_composite":{"inputs": ["event_count", "close"],"func": ced_ext_075_event_density_capitulation_composite},
}
