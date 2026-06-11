"""
98_corporate_event_density — Base Features 001-100
Domain: 8-K / event-filing frequency spikes — bursts of corporate events around distress
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_TD_MO    = 21    # 1 month in trading days
_TD_WK    = 5     # 1 week in trading days
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Rolling event sums over multiple windows ---

def ced_001_event_sum_5d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 5 trading days (1 week)."""
    return _rolling_sum(event_count, _TD_WK)


def ced_002_event_sum_21d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 21 trading days (1 month)."""
    return _rolling_sum(event_count, _TD_MO)


def ced_003_event_sum_63d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 63 trading days (1 quarter)."""
    return _rolling_sum(event_count, _TD_QTR)


def ced_004_event_sum_126d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 126 trading days (2 quarters)."""
    return _rolling_sum(event_count, _TD_2Q)


def ced_005_event_sum_252d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 252 trading days (1 year)."""
    return _rolling_sum(event_count, _TD_YEAR)


def ced_006_event_sum_504d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 504 trading days (2 years)."""
    return _rolling_sum(event_count, _TD_2Y)


def ced_007_event_sum_756d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 756 trading days (3 years)."""
    return _rolling_sum(event_count, _TD_3Y)


def ced_008_event_sum_10d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 10 trading days (2 weeks)."""
    return _rolling_sum(event_count, 10)


def ced_009_event_sum_42d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 42 trading days (~2 months)."""
    return _rolling_sum(event_count, 42)


def ced_010_event_sum_189d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 189 trading days (~3 quarters)."""
    return _rolling_sum(event_count, 189)


def ced_011_event_expanding_sum(event_count: pd.Series) -> pd.Series:
    """Expanding cumulative sum of event_count (all-history total events)."""
    return event_count.expanding(min_periods=1).sum()


def ced_012_event_sum_15d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 15 trading days."""
    return _rolling_sum(event_count, 15)


def ced_013_event_sum_30d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 30 trading days."""
    return _rolling_sum(event_count, 30)


def ced_014_event_sum_90d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 90 trading days."""
    return _rolling_sum(event_count, 90)


def ced_015_event_sum_378d(event_count: pd.Series) -> pd.Series:
    """Rolling sum of event_count over 378 trading days (~1.5 years)."""
    return _rolling_sum(event_count, 378)


# --- Group B (016-030): Mean event rate over multiple windows ---

def ced_016_event_mean_5d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 5 trading days."""
    return _rolling_mean(event_count, _TD_WK)


def ced_017_event_mean_21d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 21 trading days."""
    return _rolling_mean(event_count, _TD_MO)


def ced_018_event_mean_63d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 63 trading days."""
    return _rolling_mean(event_count, _TD_QTR)


def ced_019_event_mean_126d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 126 trading days."""
    return _rolling_mean(event_count, _TD_2Q)


def ced_020_event_mean_252d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 252 trading days."""
    return _rolling_mean(event_count, _TD_YEAR)


def ced_021_event_mean_504d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 504 trading days."""
    return _rolling_mean(event_count, _TD_2Y)


def ced_022_event_mean_756d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 756 trading days."""
    return _rolling_mean(event_count, _TD_3Y)


def ced_023_event_ewm_mean_21d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=21 (1-month half-life)."""
    return _ewm_mean(event_count, _TD_MO)


def ced_024_event_ewm_mean_63d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=63 (quarterly half-life)."""
    return _ewm_mean(event_count, _TD_QTR)


def ced_025_event_ewm_mean_252d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=252 (annual half-life)."""
    return _ewm_mean(event_count, _TD_YEAR)


def ced_026_event_expanding_mean(event_count: pd.Series) -> pd.Series:
    """Expanding mean of event_count (long-run average event rate)."""
    return event_count.expanding(min_periods=1).mean()


def ced_027_event_mean_10d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 10 trading days."""
    return _rolling_mean(event_count, 10)


def ced_028_event_mean_42d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 42 trading days."""
    return _rolling_mean(event_count, 42)


def ced_029_event_mean_189d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 189 trading days."""
    return _rolling_mean(event_count, 189)


def ced_030_event_mean_378d(event_count: pd.Series) -> pd.Series:
    """Rolling mean of event_count over 378 trading days."""
    return _rolling_mean(event_count, 378)


# --- Group C (031-045): Z-score and percentile rank of event rate ---

def ced_031_event_zscore_21d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 21-day rolling window."""
    return _zscore_rolling(event_count, _TD_MO)


def ced_032_event_zscore_63d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 63-day rolling window."""
    return _zscore_rolling(event_count, _TD_QTR)


def ced_033_event_zscore_126d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 126-day rolling window."""
    return _zscore_rolling(event_count, _TD_2Q)


def ced_034_event_zscore_252d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 252-day rolling window."""
    return _zscore_rolling(event_count, _TD_YEAR)


def ced_035_event_zscore_504d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 504-day rolling window."""
    return _zscore_rolling(event_count, _TD_2Y)


def ced_036_event_zscore_756d(event_count: pd.Series) -> pd.Series:
    """Z-score of event_count within a 756-day rolling window."""
    return _zscore_rolling(event_count, _TD_3Y)


def ced_037_event_expanding_zscore(event_count: pd.Series) -> pd.Series:
    """Expanding z-score of event_count (how extreme vs entire history)."""
    m  = event_count.expanding(min_periods=2).mean()
    sd = event_count.expanding(min_periods=2).std()
    return _safe_div(event_count - m, sd)


def ced_038_event_pct_rank_63d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 63-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_QTR)


def ced_039_event_pct_rank_252d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 252-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_YEAR)


def ced_040_event_pct_rank_504d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 504-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_2Y)


def ced_041_event_pct_rank_756d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 756-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_3Y)


def ced_042_event_expanding_pct_rank(event_count: pd.Series) -> pd.Series:
    """Expanding percentile rank of event_count (all-history rank)."""
    return event_count.expanding(min_periods=2).rank(pct=True)


def ced_043_event_ewm_zscore_21d(event_count: pd.Series) -> pd.Series:
    """EWM-based z-score: (event_count - ewm_mean_21d) / ewm_std_21d."""
    mu  = _ewm_mean(event_count, _TD_MO)
    dev = (event_count - mu) ** 2
    sd  = dev.ewm(span=_TD_MO, min_periods=max(2, _TD_MO // 4)).mean() ** 0.5
    return _safe_div(event_count - mu, sd)


def ced_044_event_ewm_zscore_63d(event_count: pd.Series) -> pd.Series:
    """EWM-based z-score: (event_count - ewm_mean_63d) / ewm_std_63d."""
    mu  = _ewm_mean(event_count, _TD_QTR)
    dev = (event_count - mu) ** 2
    sd  = dev.ewm(span=_TD_QTR, min_periods=max(2, _TD_QTR // 4)).mean() ** 0.5
    return _safe_div(event_count - mu, sd)


def ced_045_event_pct_rank_21d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 21-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_MO)


# --- Group D (046-060): Spike flags and burst detection ---

def ced_046_spike_above_1mo_mean(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count > trailing 21-day mean, else 0."""
    return (event_count > _rolling_mean(event_count, _TD_MO)).astype(float)


def ced_047_spike_above_1q_mean(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count > trailing 63-day mean, else 0."""
    return (event_count > _rolling_mean(event_count, _TD_QTR)).astype(float)


def ced_048_spike_above_1y_mean(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count > trailing 252-day mean, else 0."""
    return (event_count > _rolling_mean(event_count, _TD_YEAR)).astype(float)


def ced_049_spike_above_1q_median(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count > trailing 63-day median, else 0."""
    return (event_count > _rolling_median(event_count, _TD_QTR)).astype(float)


def ced_050_spike_above_1y_median(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count > trailing 252-day median, else 0."""
    return (event_count > _rolling_median(event_count, _TD_YEAR)).astype(float)


def ced_051_burst_ratio_5d_vs_63d(event_count: pd.Series) -> pd.Series:
    """Ratio of 5-day mean to 63-day mean: recent burst vs quarterly baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_WK), _rolling_mean(event_count, _TD_QTR))


def ced_052_burst_ratio_21d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 21-day mean to 252-day mean: monthly burst vs annual baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_MO), _rolling_mean(event_count, _TD_YEAR))


def ced_053_burst_ratio_21d_vs_126d(event_count: pd.Series) -> pd.Series:
    """Ratio of 21-day mean to 126-day mean: monthly vs 2-quarter baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_MO), _rolling_mean(event_count, _TD_2Q))


def ced_054_burst_ratio_63d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 63-day mean to 252-day mean: quarterly vs annual baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_QTR), _rolling_mean(event_count, _TD_YEAR))


def ced_055_burst_ratio_5d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 5-day mean to 252-day mean: weekly burst vs annual baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_WK), _rolling_mean(event_count, _TD_YEAR))


def ced_056_burst_ratio_10d_vs_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 10-day mean to 252-day mean: 2-week burst vs annual baseline."""
    return _safe_div(_rolling_mean(event_count, 10), _rolling_mean(event_count, _TD_YEAR))


def ced_057_event_excess_over_1y_mean(event_count: pd.Series) -> pd.Series:
    """event_count minus its trailing 252-day mean (raw excess)."""
    return event_count - _rolling_mean(event_count, _TD_YEAR)


def ced_058_event_excess_over_1q_mean(event_count: pd.Series) -> pd.Series:
    """event_count minus its trailing 63-day mean (raw excess)."""
    return event_count - _rolling_mean(event_count, _TD_QTR)


def ced_059_event_excess_over_ewm_63d(event_count: pd.Series) -> pd.Series:
    """event_count minus its 63-day EWM mean (deviation from EWM baseline)."""
    return event_count - _ewm_mean(event_count, _TD_QTR)


def ced_060_event_excess_over_ewm_252d(event_count: pd.Series) -> pd.Series:
    """event_count minus its 252-day EWM mean (deviation from annual EWM baseline)."""
    return event_count - _ewm_mean(event_count, _TD_YEAR)


# --- Group E (061-075): Active day fractions, gaps, and density measures ---

def ced_061_active_day_frac_5d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 5 days with at least one event (event_count > 0)."""
    return _safe_div(_active_days(event_count, _TD_WK), pd.Series(_TD_WK, index=event_count.index, dtype=float))


def ced_062_active_day_frac_21d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 21 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_MO), pd.Series(_TD_MO, index=event_count.index, dtype=float))


def ced_063_active_day_frac_63d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_QTR), pd.Series(_TD_QTR, index=event_count.index, dtype=float))


def ced_064_active_day_frac_126d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 126 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_2Q), pd.Series(_TD_2Q, index=event_count.index, dtype=float))


def ced_065_active_day_frac_252d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_YEAR), pd.Series(_TD_YEAR, index=event_count.index, dtype=float))


def ced_066_active_day_frac_504d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 504 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_2Y), pd.Series(_TD_2Y, index=event_count.index, dtype=float))


def ced_067_active_day_frac_756d(event_count: pd.Series) -> pd.Series:
    """Fraction of last 756 days with at least one event."""
    return _safe_div(_active_days(event_count, _TD_3Y), pd.Series(_TD_3Y, index=event_count.index, dtype=float))


def ced_068_days_since_last_event(event_count: pd.Series) -> pd.Series:
    """Number of trading days since the most recent event_count > 0 occurrence."""
    has_event = (event_count > 0).astype(float)
    gap = np.zeros(len(has_event), dtype=float)
    arr = has_event.values
    for i in range(1, len(arr)):
        if arr[i] > 0:
            gap[i] = 0.0
        else:
            gap[i] = gap[i - 1] + 1.0
    return pd.Series(gap, index=event_count.index)


def ced_069_max_event_free_gap_63d(event_count: pd.Series) -> pd.Series:
    """Longest consecutive event-free streak within the trailing 63-day window."""
    no_event = (event_count == 0).astype(float)

    def _max_gap(arr):
        best = 0
        cur  = 0
        for v in arr:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return no_event.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 4)).apply(_max_gap, raw=True)


def ced_070_max_event_free_gap_252d(event_count: pd.Series) -> pd.Series:
    """Longest consecutive event-free streak within the trailing 252-day window."""
    no_event = (event_count == 0).astype(float)

    def _max_gap(arr):
        best = 0
        cur  = 0
        for v in arr:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return no_event.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).apply(_max_gap, raw=True)


def ced_071_event_rolling_std_63d(event_count: pd.Series) -> pd.Series:
    """Rolling std of event_count over 63 days — event-rate dispersion."""
    return _rolling_std(event_count, _TD_QTR)


def ced_072_event_rolling_std_252d(event_count: pd.Series) -> pd.Series:
    """Rolling std of event_count over 252 days — annual event-rate dispersion."""
    return _rolling_std(event_count, _TD_YEAR)


def ced_073_event_rolling_max_63d(event_count: pd.Series) -> pd.Series:
    """Rolling maximum of event_count over 63 days (single-day spike magnitude)."""
    return _rolling_max(event_count, _TD_QTR)


def ced_074_event_rolling_max_252d(event_count: pd.Series) -> pd.Series:
    """Rolling maximum of event_count over 252 days."""
    return _rolling_max(event_count, _TD_YEAR)


def ced_075_event_density_composite(event_count: pd.Series) -> pd.Series:
    """
    Composite event density score: equally weighted sum of three z-scores
    (5d, 63d, 252d rolling windows) — multi-horizon burst signal.
    """
    z5   = _zscore_rolling(event_count, _TD_WK)
    z63  = _zscore_rolling(event_count, _TD_QTR)
    z252 = _zscore_rolling(event_count, _TD_YEAR)
    return (z5 + z63 + z252) / 3.0


# --- Group F extra (151-175): New density transforms and multi-window signals ---

def ced_151_event_rolling_min_63d(event_count: pd.Series) -> pd.Series:
    """Rolling minimum of event_count over 63 trading days."""
    return _rolling_min(event_count, _TD_QTR)


def ced_152_event_rolling_min_252d(event_count: pd.Series) -> pd.Series:
    """Rolling minimum of event_count over 252 trading days."""
    return _rolling_min(event_count, _TD_YEAR)


def ced_153_event_range_63d(event_count: pd.Series) -> pd.Series:
    """Rolling range (max - min) of event_count over 63 days."""
    return _rolling_max(event_count, _TD_QTR) - _rolling_min(event_count, _TD_QTR)


def ced_154_event_range_252d(event_count: pd.Series) -> pd.Series:
    """Rolling range (max - min) of event_count over 252 days."""
    return _rolling_max(event_count, _TD_YEAR) - _rolling_min(event_count, _TD_YEAR)


def ced_155_event_sum_21d_zscore_252d(event_count: pd.Series) -> pd.Series:
    """Z-score of the 21-day rolling event sum within a 252-day window."""
    s21 = _rolling_sum(event_count, _TD_MO)
    return _zscore_rolling(s21, _TD_YEAR)


def ced_156_event_sum_63d_zscore_252d(event_count: pd.Series) -> pd.Series:
    """Z-score of the 63-day rolling event sum within a 252-day window."""
    s63 = _rolling_sum(event_count, _TD_QTR)
    return _zscore_rolling(s63, _TD_YEAR)


def ced_157_event_active_days_21d(event_count: pd.Series) -> pd.Series:
    """Count of event-active days in the trailing 21-day window."""
    return _active_days(event_count, _TD_MO)


def ced_158_event_active_days_63d(event_count: pd.Series) -> pd.Series:
    """Count of event-active days in the trailing 63-day window."""
    return _active_days(event_count, _TD_QTR)


def ced_159_event_active_days_252d(event_count: pd.Series) -> pd.Series:
    """Count of event-active days in the trailing 252-day window."""
    return _active_days(event_count, _TD_YEAR)


def ced_160_event_ewm_mean_5d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=5 (very short-run momentum)."""
    return _ewm_mean(event_count, _TD_WK)


def ced_161_event_ewm_mean_126d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=126 (2-quarter half-life)."""
    return _ewm_mean(event_count, _TD_2Q)


def ced_162_event_ewm_mean_504d(event_count: pd.Series) -> pd.Series:
    """EWM mean of event_count with span=504 (2-year half-life)."""
    return _ewm_mean(event_count, _TD_2Y)


def ced_163_event_sum_5d_zscore_63d(event_count: pd.Series) -> pd.Series:
    """Z-score of the 5-day rolling event sum within a 63-day window."""
    s5 = _rolling_sum(event_count, _TD_WK)
    return _zscore_rolling(s5, _TD_QTR)


def ced_164_event_pct_rank_126d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 126-day rolling window."""
    return _rolling_rank_pct(event_count, _TD_2Q)


def ced_165_event_expanding_max(event_count: pd.Series) -> pd.Series:
    """Expanding maximum of event_count (all-time single-day event spike)."""
    return event_count.expanding(min_periods=1).max()


def ced_166_event_ratio_to_expanding_max(event_count: pd.Series) -> pd.Series:
    """event_count divided by the expanding historical maximum."""
    return _safe_div(event_count, event_count.expanding(min_periods=1).max())


def ced_167_event_sum_10d_zscore_252d(event_count: pd.Series) -> pd.Series:
    """Z-score of the 10-day rolling event sum within a 252-day window."""
    s10 = _rolling_sum(event_count, 10)
    return _zscore_rolling(s10, _TD_YEAR)


def ced_168_event_burst_ratio_5d_vs_504d(event_count: pd.Series) -> pd.Series:
    """Ratio of 5-day mean to 504-day mean: weekly burst vs 2-year baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_WK), _rolling_mean(event_count, _TD_2Y))


def ced_169_event_burst_ratio_21d_vs_504d(event_count: pd.Series) -> pd.Series:
    """Ratio of 21-day mean to 504-day mean: monthly burst vs 2-year baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_MO), _rolling_mean(event_count, _TD_2Y))


def ced_170_event_burst_ratio_63d_vs_504d(event_count: pd.Series) -> pd.Series:
    """Ratio of 63-day mean to 504-day mean: quarterly burst vs 2-year baseline."""
    return _safe_div(_rolling_mean(event_count, _TD_QTR), _rolling_mean(event_count, _TD_2Y))


def ced_171_event_excess_over_ewm_21d(event_count: pd.Series) -> pd.Series:
    """event_count minus its 21-day EWM mean (deviation from short EWM baseline)."""
    return event_count - _ewm_mean(event_count, _TD_MO)


def ced_172_event_excess_over_ewm_126d(event_count: pd.Series) -> pd.Series:
    """event_count minus its 126-day EWM mean."""
    return event_count - _ewm_mean(event_count, _TD_2Q)


def ced_173_event_pct_rank_10d(event_count: pd.Series) -> pd.Series:
    """Percentile rank of event_count within a 10-day rolling window."""
    return _rolling_rank_pct(event_count, 10)


def ced_174_event_ewm_zscore_252d(event_count: pd.Series) -> pd.Series:
    """EWM-based z-score: (event_count - ewm_mean_252d) / ewm_std_252d."""
    mu  = _ewm_mean(event_count, _TD_YEAR)
    dev = (event_count - mu) ** 2
    sd  = dev.ewm(span=_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).mean() ** 0.5
    return _safe_div(event_count - mu, sd)


def ced_175_event_spike_density_composite_v2(event_count: pd.Series) -> pd.Series:
    """
    Composite burst signal v2: average of 5d/21d/63d z-scores of 21d event sum,
    weighting short-run spikes more heavily than ced_075.
    """
    s21 = _rolling_sum(event_count, _TD_MO)
    z5  = _zscore_rolling(s21, _TD_WK)
    z21 = _zscore_rolling(s21, _TD_MO)
    z63 = _zscore_rolling(s21, _TD_QTR)
    return (z5 + z21 + z63) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

CORPORATE_EVENT_DENSITY_REGISTRY_001_075 = {
    "ced_001_event_sum_5d":               {"inputs": ["event_count"], "func": ced_001_event_sum_5d},
    "ced_002_event_sum_21d":              {"inputs": ["event_count"], "func": ced_002_event_sum_21d},
    "ced_003_event_sum_63d":              {"inputs": ["event_count"], "func": ced_003_event_sum_63d},
    "ced_004_event_sum_126d":             {"inputs": ["event_count"], "func": ced_004_event_sum_126d},
    "ced_005_event_sum_252d":             {"inputs": ["event_count"], "func": ced_005_event_sum_252d},
    "ced_006_event_sum_504d":             {"inputs": ["event_count"], "func": ced_006_event_sum_504d},
    "ced_007_event_sum_756d":             {"inputs": ["event_count"], "func": ced_007_event_sum_756d},
    "ced_008_event_sum_10d":              {"inputs": ["event_count"], "func": ced_008_event_sum_10d},
    "ced_009_event_sum_42d":              {"inputs": ["event_count"], "func": ced_009_event_sum_42d},
    "ced_010_event_sum_189d":             {"inputs": ["event_count"], "func": ced_010_event_sum_189d},
    "ced_011_event_expanding_sum":        {"inputs": ["event_count"], "func": ced_011_event_expanding_sum},
    "ced_012_event_sum_15d":              {"inputs": ["event_count"], "func": ced_012_event_sum_15d},
    "ced_013_event_sum_30d":              {"inputs": ["event_count"], "func": ced_013_event_sum_30d},
    "ced_014_event_sum_90d":              {"inputs": ["event_count"], "func": ced_014_event_sum_90d},
    "ced_015_event_sum_378d":             {"inputs": ["event_count"], "func": ced_015_event_sum_378d},
    "ced_016_event_mean_5d":              {"inputs": ["event_count"], "func": ced_016_event_mean_5d},
    "ced_017_event_mean_21d":             {"inputs": ["event_count"], "func": ced_017_event_mean_21d},
    "ced_018_event_mean_63d":             {"inputs": ["event_count"], "func": ced_018_event_mean_63d},
    "ced_019_event_mean_126d":            {"inputs": ["event_count"], "func": ced_019_event_mean_126d},
    "ced_020_event_mean_252d":            {"inputs": ["event_count"], "func": ced_020_event_mean_252d},
    "ced_021_event_mean_504d":            {"inputs": ["event_count"], "func": ced_021_event_mean_504d},
    "ced_022_event_mean_756d":            {"inputs": ["event_count"], "func": ced_022_event_mean_756d},
    "ced_023_event_ewm_mean_21d":         {"inputs": ["event_count"], "func": ced_023_event_ewm_mean_21d},
    "ced_024_event_ewm_mean_63d":         {"inputs": ["event_count"], "func": ced_024_event_ewm_mean_63d},
    "ced_025_event_ewm_mean_252d":        {"inputs": ["event_count"], "func": ced_025_event_ewm_mean_252d},
    "ced_026_event_expanding_mean":       {"inputs": ["event_count"], "func": ced_026_event_expanding_mean},
    "ced_027_event_mean_10d":             {"inputs": ["event_count"], "func": ced_027_event_mean_10d},
    "ced_028_event_mean_42d":             {"inputs": ["event_count"], "func": ced_028_event_mean_42d},
    "ced_029_event_mean_189d":            {"inputs": ["event_count"], "func": ced_029_event_mean_189d},
    "ced_030_event_mean_378d":            {"inputs": ["event_count"], "func": ced_030_event_mean_378d},
    "ced_031_event_zscore_21d":           {"inputs": ["event_count"], "func": ced_031_event_zscore_21d},
    "ced_032_event_zscore_63d":           {"inputs": ["event_count"], "func": ced_032_event_zscore_63d},
    "ced_033_event_zscore_126d":          {"inputs": ["event_count"], "func": ced_033_event_zscore_126d},
    "ced_034_event_zscore_252d":          {"inputs": ["event_count"], "func": ced_034_event_zscore_252d},
    "ced_035_event_zscore_504d":          {"inputs": ["event_count"], "func": ced_035_event_zscore_504d},
    "ced_036_event_zscore_756d":          {"inputs": ["event_count"], "func": ced_036_event_zscore_756d},
    "ced_037_event_expanding_zscore":     {"inputs": ["event_count"], "func": ced_037_event_expanding_zscore},
    "ced_038_event_pct_rank_63d":         {"inputs": ["event_count"], "func": ced_038_event_pct_rank_63d},
    "ced_039_event_pct_rank_252d":        {"inputs": ["event_count"], "func": ced_039_event_pct_rank_252d},
    "ced_040_event_pct_rank_504d":        {"inputs": ["event_count"], "func": ced_040_event_pct_rank_504d},
    "ced_041_event_pct_rank_756d":        {"inputs": ["event_count"], "func": ced_041_event_pct_rank_756d},
    "ced_042_event_expanding_pct_rank":   {"inputs": ["event_count"], "func": ced_042_event_expanding_pct_rank},
    "ced_043_event_ewm_zscore_21d":       {"inputs": ["event_count"], "func": ced_043_event_ewm_zscore_21d},
    "ced_044_event_ewm_zscore_63d":       {"inputs": ["event_count"], "func": ced_044_event_ewm_zscore_63d},
    "ced_045_event_pct_rank_21d":         {"inputs": ["event_count"], "func": ced_045_event_pct_rank_21d},
    "ced_046_spike_above_1mo_mean":       {"inputs": ["event_count"], "func": ced_046_spike_above_1mo_mean},
    "ced_047_spike_above_1q_mean":        {"inputs": ["event_count"], "func": ced_047_spike_above_1q_mean},
    "ced_048_spike_above_1y_mean":        {"inputs": ["event_count"], "func": ced_048_spike_above_1y_mean},
    "ced_049_spike_above_1q_median":      {"inputs": ["event_count"], "func": ced_049_spike_above_1q_median},
    "ced_050_spike_above_1y_median":      {"inputs": ["event_count"], "func": ced_050_spike_above_1y_median},
    "ced_051_burst_ratio_5d_vs_63d":      {"inputs": ["event_count"], "func": ced_051_burst_ratio_5d_vs_63d},
    "ced_052_burst_ratio_21d_vs_252d":    {"inputs": ["event_count"], "func": ced_052_burst_ratio_21d_vs_252d},
    "ced_053_burst_ratio_21d_vs_126d":    {"inputs": ["event_count"], "func": ced_053_burst_ratio_21d_vs_126d},
    "ced_054_burst_ratio_63d_vs_252d":    {"inputs": ["event_count"], "func": ced_054_burst_ratio_63d_vs_252d},
    "ced_055_burst_ratio_5d_vs_252d":     {"inputs": ["event_count"], "func": ced_055_burst_ratio_5d_vs_252d},
    "ced_056_burst_ratio_10d_vs_252d":    {"inputs": ["event_count"], "func": ced_056_burst_ratio_10d_vs_252d},
    "ced_057_event_excess_over_1y_mean":  {"inputs": ["event_count"], "func": ced_057_event_excess_over_1y_mean},
    "ced_058_event_excess_over_1q_mean":  {"inputs": ["event_count"], "func": ced_058_event_excess_over_1q_mean},
    "ced_059_event_excess_over_ewm_63d":  {"inputs": ["event_count"], "func": ced_059_event_excess_over_ewm_63d},
    "ced_060_event_excess_over_ewm_252d": {"inputs": ["event_count"], "func": ced_060_event_excess_over_ewm_252d},
    "ced_061_active_day_frac_5d":         {"inputs": ["event_count"], "func": ced_061_active_day_frac_5d},
    "ced_062_active_day_frac_21d":        {"inputs": ["event_count"], "func": ced_062_active_day_frac_21d},
    "ced_063_active_day_frac_63d":        {"inputs": ["event_count"], "func": ced_063_active_day_frac_63d},
    "ced_064_active_day_frac_126d":       {"inputs": ["event_count"], "func": ced_064_active_day_frac_126d},
    "ced_065_active_day_frac_252d":       {"inputs": ["event_count"], "func": ced_065_active_day_frac_252d},
    "ced_066_active_day_frac_504d":       {"inputs": ["event_count"], "func": ced_066_active_day_frac_504d},
    "ced_067_active_day_frac_756d":       {"inputs": ["event_count"], "func": ced_067_active_day_frac_756d},
    "ced_068_days_since_last_event":      {"inputs": ["event_count"], "func": ced_068_days_since_last_event},
    "ced_069_max_event_free_gap_63d":     {"inputs": ["event_count"], "func": ced_069_max_event_free_gap_63d},
    "ced_070_max_event_free_gap_252d":    {"inputs": ["event_count"], "func": ced_070_max_event_free_gap_252d},
    "ced_071_event_rolling_std_63d":      {"inputs": ["event_count"], "func": ced_071_event_rolling_std_63d},
    "ced_072_event_rolling_std_252d":     {"inputs": ["event_count"], "func": ced_072_event_rolling_std_252d},
    "ced_073_event_rolling_max_63d":      {"inputs": ["event_count"], "func": ced_073_event_rolling_max_63d},
    "ced_074_event_rolling_max_252d":     {"inputs": ["event_count"], "func": ced_074_event_rolling_max_252d},
    "ced_075_event_density_composite":    {"inputs": ["event_count"], "func": ced_075_event_density_composite},
    "ced_151_event_rolling_min_63d":              {"inputs": ["event_count"], "func": ced_151_event_rolling_min_63d},
    "ced_152_event_rolling_min_252d":             {"inputs": ["event_count"], "func": ced_152_event_rolling_min_252d},
    "ced_153_event_range_63d":                    {"inputs": ["event_count"], "func": ced_153_event_range_63d},
    "ced_154_event_range_252d":                   {"inputs": ["event_count"], "func": ced_154_event_range_252d},
    "ced_155_event_sum_21d_zscore_252d":          {"inputs": ["event_count"], "func": ced_155_event_sum_21d_zscore_252d},
    "ced_156_event_sum_63d_zscore_252d":          {"inputs": ["event_count"], "func": ced_156_event_sum_63d_zscore_252d},
    "ced_157_event_active_days_21d":              {"inputs": ["event_count"], "func": ced_157_event_active_days_21d},
    "ced_158_event_active_days_63d":              {"inputs": ["event_count"], "func": ced_158_event_active_days_63d},
    "ced_159_event_active_days_252d":             {"inputs": ["event_count"], "func": ced_159_event_active_days_252d},
    "ced_160_event_ewm_mean_5d":                  {"inputs": ["event_count"], "func": ced_160_event_ewm_mean_5d},
    "ced_161_event_ewm_mean_126d":                {"inputs": ["event_count"], "func": ced_161_event_ewm_mean_126d},
    "ced_162_event_ewm_mean_504d":                {"inputs": ["event_count"], "func": ced_162_event_ewm_mean_504d},
    "ced_163_event_sum_5d_zscore_63d":            {"inputs": ["event_count"], "func": ced_163_event_sum_5d_zscore_63d},
    "ced_164_event_pct_rank_126d":                {"inputs": ["event_count"], "func": ced_164_event_pct_rank_126d},
    "ced_165_event_expanding_max":                {"inputs": ["event_count"], "func": ced_165_event_expanding_max},
    "ced_166_event_ratio_to_expanding_max":       {"inputs": ["event_count"], "func": ced_166_event_ratio_to_expanding_max},
    "ced_167_event_sum_10d_zscore_252d":          {"inputs": ["event_count"], "func": ced_167_event_sum_10d_zscore_252d},
    "ced_168_event_burst_ratio_5d_vs_504d":       {"inputs": ["event_count"], "func": ced_168_event_burst_ratio_5d_vs_504d},
    "ced_169_event_burst_ratio_21d_vs_504d":      {"inputs": ["event_count"], "func": ced_169_event_burst_ratio_21d_vs_504d},
    "ced_170_event_burst_ratio_63d_vs_504d":      {"inputs": ["event_count"], "func": ced_170_event_burst_ratio_63d_vs_504d},
    "ced_171_event_excess_over_ewm_21d":          {"inputs": ["event_count"], "func": ced_171_event_excess_over_ewm_21d},
    "ced_172_event_excess_over_ewm_126d":         {"inputs": ["event_count"], "func": ced_172_event_excess_over_ewm_126d},
    "ced_173_event_pct_rank_10d":                 {"inputs": ["event_count"], "func": ced_173_event_pct_rank_10d},
    "ced_174_event_ewm_zscore_252d":              {"inputs": ["event_count"], "func": ced_174_event_ewm_zscore_252d},
    "ced_175_event_spike_density_composite_v2":   {"inputs": ["event_count"], "func": ced_175_event_spike_density_composite_v2},
}
