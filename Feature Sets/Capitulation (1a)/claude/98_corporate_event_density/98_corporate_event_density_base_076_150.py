"""
98_corporate_event_density — Base Features 076-200
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
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
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


def _log_ret(close: pd.Series) -> pd.Series:
    """Daily log return of close price."""
    return np.log(close / close.shift(1).replace(0, np.nan))


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Event count QoQ / YoY changes and acceleration ---

def ced_076_event_sum_qoq_change(event_count: pd.Series) -> pd.Series:
    """QoQ change in 63-day rolling event sum (absolute acceleration)."""
    base = _rolling_sum(event_count, _TD_QTR)
    return base - base.shift(_TD_QTR)


def ced_077_event_sum_yoy_change(event_count: pd.Series) -> pd.Series:
    """YoY change in 252-day rolling event sum."""
    base = _rolling_sum(event_count, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def ced_078_event_mean_qoq_change(event_count: pd.Series) -> pd.Series:
    """QoQ change in 63-day rolling mean event rate."""
    base = _rolling_mean(event_count, _TD_QTR)
    return base - base.shift(_TD_QTR)


def ced_079_event_mean_yoy_change(event_count: pd.Series) -> pd.Series:
    """YoY change in 252-day rolling mean event rate."""
    base = _rolling_mean(event_count, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def ced_080_event_active_frac_qoq_change(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day active-day fraction."""
    base = _safe_div(_active_days(event_count, _TD_QTR),
                     pd.Series(_TD_QTR, index=event_count.index, dtype=float))
    return base - base.shift(_TD_QTR)


def ced_081_event_active_frac_yoy_change(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day active-day fraction."""
    base = _safe_div(_active_days(event_count, _TD_YEAR),
                     pd.Series(_TD_YEAR, index=event_count.index, dtype=float))
    return base - base.shift(_TD_YEAR)


def ced_082_event_sum_2q_change(event_count: pd.Series) -> pd.Series:
    """Half-year change in 63-day rolling event sum."""
    base = _rolling_sum(event_count, _TD_QTR)
    return base - base.shift(_TD_2Q)


def ced_083_event_mean_mo_change(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in 21-day rolling mean event rate."""
    base = _rolling_mean(event_count, _TD_MO)
    return base - base.shift(_TD_MO)


def ced_084_event_mean_wk_change(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in 5-day rolling mean event rate."""
    base = _rolling_mean(event_count, _TD_WK)
    return base - base.shift(_TD_WK)


def ced_085_event_pct_rank_qoq_change(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day percentile rank of event_count."""
    base = _rolling_rank_pct(event_count, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def ced_086_event_zscore_qoq_change(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day z-score of event_count."""
    base = _zscore_rolling(event_count, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def ced_087_event_zscore_yoy_change(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day z-score of event_count."""
    base = _zscore_rolling(event_count, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def ced_088_event_sum_5d_qoq_ratio(event_count: pd.Series) -> pd.Series:
    """Ratio of current 5-day event sum to lagged-1Q 5-day event sum."""
    base = _rolling_sum(event_count, _TD_WK)
    return _safe_div(base, base.shift(_TD_QTR))


def ced_089_event_sum_21d_yoy_ratio(event_count: pd.Series) -> pd.Series:
    """Ratio of current 21-day event sum to lagged-1Y 21-day event sum."""
    base = _rolling_sum(event_count, _TD_MO)
    return _safe_div(base, base.shift(_TD_YEAR))


def ced_090_event_sum_63d_yoy_ratio(event_count: pd.Series) -> pd.Series:
    """Ratio of current 63-day event sum to lagged-1Y 63-day event sum."""
    base = _rolling_sum(event_count, _TD_QTR)
    return _safe_div(base, base.shift(_TD_YEAR))


# --- Group G (091-105): Poisson / intensity proxies ---

def ced_091_event_log_intensity_21d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 21-day mean event rate): Poisson-style intensity proxy."""
    return np.log1p(_rolling_mean(event_count, _TD_MO))


def ced_092_event_log_intensity_63d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 63-day mean event rate): quarterly Poisson intensity."""
    return np.log1p(_rolling_mean(event_count, _TD_QTR))


def ced_093_event_log_intensity_252d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 252-day mean event rate): annual Poisson intensity."""
    return np.log1p(_rolling_mean(event_count, _TD_YEAR))


def ced_094_event_log_count_today(event_count: pd.Series) -> pd.Series:
    """Log of (1 + event_count) on the current day."""
    return np.log1p(event_count)


def ced_095_event_log_sum_63d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 63-day rolling event sum)."""
    return np.log1p(_rolling_sum(event_count, _TD_QTR))


def ced_096_event_log_sum_252d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 252-day rolling event sum)."""
    return np.log1p(_rolling_sum(event_count, _TD_YEAR))


def ced_097_event_intensity_vs_ewm_21d(event_count: pd.Series) -> pd.Series:
    """Ratio of event_count to its 21-day EWM: current vs short-run intensity."""
    return _safe_div(event_count, _ewm_mean(event_count, _TD_MO))


def ced_098_event_intensity_vs_ewm_63d(event_count: pd.Series) -> pd.Series:
    """Ratio of event_count to its 63-day EWM: current vs quarterly intensity."""
    return _safe_div(event_count, _ewm_mean(event_count, _TD_QTR))


def ced_099_event_intensity_vs_ewm_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of event_count to its 252-day EWM: current vs annual intensity."""
    return _safe_div(event_count, _ewm_mean(event_count, _TD_YEAR))


def ced_100_event_above_2sigma_63d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds mean + 2*std over trailing 63 days."""
    mu  = _rolling_mean(event_count, _TD_QTR)
    sig = _rolling_std(event_count, _TD_QTR)
    return (event_count > (mu + 2.0 * sig)).astype(float)


def ced_101_event_above_2sigma_252d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds mean + 2*std over trailing 252 days."""
    mu  = _rolling_mean(event_count, _TD_YEAR)
    sig = _rolling_std(event_count, _TD_YEAR)
    return (event_count > (mu + 2.0 * sig)).astype(float)


def ced_102_event_above_3sigma_252d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds mean + 3*std over trailing 252 days (extreme spike)."""
    mu  = _rolling_mean(event_count, _TD_YEAR)
    sig = _rolling_std(event_count, _TD_YEAR)
    return (event_count > (mu + 3.0 * sig)).astype(float)


def ced_103_event_sum_spike_count_63d(event_count: pd.Series) -> pd.Series:
    """Count of days in trailing 63 days where event_count > 1-year mean."""
    mu     = _rolling_mean(event_count, _TD_YEAR)
    spikes = (event_count > mu).astype(float)
    return _rolling_sum(spikes, _TD_QTR)


def ced_104_event_sum_spike_count_252d(event_count: pd.Series) -> pd.Series:
    """Count of days in trailing 252 days where event_count > 1-year mean."""
    mu     = _rolling_mean(event_count, _TD_YEAR)
    spikes = (event_count > mu).astype(float)
    return _rolling_sum(spikes, _TD_YEAR)


def ced_105_event_inter_arrival_mean_63d(event_count: pd.Series) -> pd.Series:
    """
    Mean inter-arrival time (days between events) over trailing 63 days.
    Approximated as window / (1 + active_day_count).
    """
    active = _active_days(event_count, _TD_QTR)
    return _safe_div(pd.Series(_TD_QTR, index=event_count.index, dtype=float),
                     (active + 1.0))


# --- Group H (106-120): Event density during price drawdown ---

def ced_106_event_sum_during_price_decline_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of event_count on days when close < its 63-day rolling mean (price-decline filter)."""
    below_avg = (close < _rolling_mean(close, _TD_QTR)).astype(float)
    return _rolling_sum(event_count * below_avg, _TD_QTR)


def ced_107_event_sum_during_price_decline_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of event_count on days when close < its 252-day rolling mean."""
    below_avg = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_sum(event_count * below_avg, _TD_YEAR)


def ced_108_event_sum_price_down_days_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of event_count on negative-return days in trailing 63 days."""
    ret_neg = (close < close.shift(1)).astype(float)
    return _rolling_sum(event_count * ret_neg, _TD_QTR)


def ced_109_event_sum_price_down_days_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of event_count on negative-return days in trailing 252 days."""
    ret_neg = (close < close.shift(1)).astype(float)
    return _rolling_sum(event_count * ret_neg, _TD_YEAR)


def ced_110_event_density_near_52w_low(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Mean event_count rate on days when close is within 10% of its 252-day low."""
    low252 = _rolling_min(close, _TD_YEAR)
    near_low = (close <= low252 * 1.10).astype(float)
    return _rolling_mean(event_count * near_low, _TD_YEAR)


def ced_111_event_frac_during_drawdown_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of 63-day active event days that fall on price-below-63d-mean days."""
    below_avg = (close < _rolling_mean(close, _TD_QTR)).astype(float)
    active    = (event_count > 0).astype(float)
    co_occur  = _rolling_sum(active * below_avg, _TD_QTR)
    total_act = _active_days(event_count, _TD_QTR)
    return _safe_div(co_occur, total_act)


def ced_112_event_price_corr_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between event_count and daily log return."""
    lr = _log_ret(close)
    return event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).corr(lr)


def ced_113_event_price_corr_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day correlation between event_count and daily log return."""
    lr = _log_ret(close)
    return event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).corr(lr)


def ced_114_event_sum_x_neg_ret_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of event_count * abs(negative log return): event-weighted loss."""
    lr     = _log_ret(close)
    neg_lr = lr.clip(upper=0).abs()
    return _rolling_sum(event_count * neg_lr, _TD_QTR)


def ced_115_event_sum_x_neg_ret_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day sum of event_count * abs(negative log return)."""
    lr     = _log_ret(close)
    neg_lr = lr.clip(upper=0).abs()
    return _rolling_sum(event_count * neg_lr, _TD_YEAR)


def ced_116_event_density_vs_price_pct_from_high_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean event rate weighted by distance of close from 63-day high (distress proximity)."""
    high63 = _rolling_max(close, _TD_QTR)
    dist   = _safe_div_abs(high63 - close, high63).fillna(0.0)
    return _rolling_mean(event_count * dist, _TD_QTR)


def ced_117_event_density_vs_price_pct_from_high_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """252-day mean event rate weighted by distance of close from 252-day high."""
    high252 = _rolling_max(close, _TD_YEAR)
    dist    = _safe_div_abs(high252 - close, high252).fillna(0.0)
    return _rolling_mean(event_count * dist, _TD_YEAR)


def ced_118_event_sum_below_52w_low_flag(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative event sum over days when close makes a new 252-day low."""
    prev_low = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()
    new_low  = (close < prev_low).astype(float)
    return _rolling_sum(event_count * new_low, _TD_YEAR)


def ced_119_event_active_frac_below_1y_mean(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of event-active days (trailing 252d) when close was below its 252-day mean."""
    below  = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    active = (event_count > 0).astype(float)
    return _safe_div(_rolling_sum(active * below, _TD_YEAR),
                     _active_days(event_count, _TD_YEAR))


def ced_120_event_count_pct_from_high_product(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """event_count * (1 - close/rolling_max_252d): spike-at-trough combined signal."""
    high252 = _rolling_max(close, _TD_YEAR)
    pct_off = (1.0 - _safe_div(close, high252)).fillna(0.0).clip(lower=0.0)
    return event_count * pct_off


# --- Group I (121-135): Rolling OLS slope, clustering, and dispersion ---

def ced_121_event_slope_63d(event_count: pd.Series) -> pd.Series:
    """OLS slope of event_count over trailing 63 days (trend in event rate)."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        if d == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / d

    return event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def ced_122_event_slope_252d(event_count: pd.Series) -> pd.Series:
    """OLS slope of event_count over trailing 252 days."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        if d == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / d

    return event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def ced_123_event_cv_63d(event_count: pd.Series) -> pd.Series:
    """Coefficient of variation of event_count over 63 days (std/mean)."""
    return _safe_div(_rolling_std(event_count, _TD_QTR),
                     _rolling_mean(event_count, _TD_QTR))


def ced_124_event_cv_252d(event_count: pd.Series) -> pd.Series:
    """Coefficient of variation of event_count over 252 days."""
    return _safe_div(_rolling_std(event_count, _TD_YEAR),
                     _rolling_mean(event_count, _TD_YEAR))


def ced_125_event_rolling_median_63d(event_count: pd.Series) -> pd.Series:
    """Rolling median of event_count over 63 days."""
    return _rolling_median(event_count, _TD_QTR)


def ced_126_event_rolling_median_252d(event_count: pd.Series) -> pd.Series:
    """Rolling median of event_count over 252 days."""
    return _rolling_median(event_count, _TD_YEAR)


def ced_127_event_above_median_frac_252d(event_count: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252d where event_count > rolling 252-day median."""
    med = _rolling_median(event_count, _TD_YEAR)
    return _rolling_mean((event_count > med).astype(float), _TD_YEAR)


def ced_128_event_max_minus_median_63d(event_count: pd.Series) -> pd.Series:
    """Rolling max minus median over 63 days (spike height above typical)."""
    return _rolling_max(event_count, _TD_QTR) - _rolling_median(event_count, _TD_QTR)


def ced_129_event_max_minus_median_252d(event_count: pd.Series) -> pd.Series:
    """Rolling max minus median over 252 days."""
    return _rolling_max(event_count, _TD_YEAR) - _rolling_median(event_count, _TD_YEAR)


def ced_130_event_sum_top_decile_days_252d(event_count: pd.Series) -> pd.Series:
    """Sum of event_count on days in top decile of event_count over trailing 252 days."""
    threshold = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.90)
    top_mask  = (event_count >= threshold).astype(float)
    return _rolling_sum(event_count * top_mask, _TD_YEAR)


def ced_131_event_sum_top_quintile_days_252d(event_count: pd.Series) -> pd.Series:
    """Sum of event_count on days in top quintile of event_count over trailing 252 days."""
    threshold = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.80)
    top_mask  = (event_count >= threshold).astype(float)
    return _rolling_sum(event_count * top_mask, _TD_YEAR)


def ced_132_event_iqr_252d(event_count: pd.Series) -> pd.Series:
    """Interquartile range of event_count over trailing 252 days."""
    q75 = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.75)
    q25 = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.25)
    return q75 - q25


def ced_133_event_iqr_63d(event_count: pd.Series) -> pd.Series:
    """Interquartile range of event_count over trailing 63 days."""
    q75 = event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).quantile(0.75)
    q25 = event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).quantile(0.25)
    return q75 - q25


def ced_134_event_consecutive_active_streak(event_count: pd.Series) -> pd.Series:
    """Current consecutive-active-day streak (days since last event-free day)."""
    active = (event_count > 0).astype(int)
    streak = np.zeros(len(active), dtype=float)
    arr    = active.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=event_count.index)


def ced_135_event_consecutive_inactive_streak(event_count: pd.Series) -> pd.Series:
    """Current consecutive-inactive-day streak (days since last event occurrence)."""
    inactive = (event_count == 0).astype(int)
    streak   = np.zeros(len(inactive), dtype=float)
    arr      = inactive.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=event_count.index)


# --- Group J (136-150): Combined/ratio features using both series ---

def ced_136_event_sum_21d_vs_252d_excess(event_count: pd.Series) -> pd.Series:
    """21-day event sum minus (21/252) * 252-day event sum: burst vs scaled annual."""
    s21  = _rolling_sum(event_count, _TD_MO)
    s252 = _rolling_sum(event_count, _TD_YEAR)
    return s21 - (_TD_MO / _TD_YEAR) * s252


def ced_137_event_sum_63d_vs_252d_excess(event_count: pd.Series) -> pd.Series:
    """63-day event sum minus (63/252) * 252-day event sum: quarterly burst vs annual pace."""
    s63  = _rolling_sum(event_count, _TD_QTR)
    s252 = _rolling_sum(event_count, _TD_YEAR)
    return s63 - (_TD_QTR / _TD_YEAR) * s252


def ced_138_event_ewm_vs_rolling_mean_63d(event_count: pd.Series) -> pd.Series:
    """63-day EWM mean minus 63-day rolling mean: short-memory vs uniform-memory difference."""
    return _ewm_mean(event_count, _TD_QTR) - _rolling_mean(event_count, _TD_QTR)


def ced_139_event_ewm_vs_rolling_mean_252d(event_count: pd.Series) -> pd.Series:
    """252-day EWM mean minus 252-day rolling mean."""
    return _ewm_mean(event_count, _TD_YEAR) - _rolling_mean(event_count, _TD_YEAR)


def ced_140_event_rolling_max_over_mean_63d(event_count: pd.Series) -> pd.Series:
    """Ratio of 63-day rolling max to 63-day mean: spike magnitude relative to baseline."""
    return _safe_div(_rolling_max(event_count, _TD_QTR),
                     _rolling_mean(event_count, _TD_QTR))


def ced_141_event_rolling_max_over_mean_252d(event_count: pd.Series) -> pd.Series:
    """Ratio of 252-day rolling max to 252-day mean."""
    return _safe_div(_rolling_max(event_count, _TD_YEAR),
                     _rolling_mean(event_count, _TD_YEAR))


def ced_142_event_sum_21d_pct_of_252d(event_count: pd.Series) -> pd.Series:
    """21-day event sum as fraction of 252-day event sum."""
    return _safe_div(_rolling_sum(event_count, _TD_MO),
                     _rolling_sum(event_count, _TD_YEAR))


def ced_143_event_sum_63d_pct_of_252d(event_count: pd.Series) -> pd.Series:
    """63-day event sum as fraction of 252-day event sum."""
    return _safe_div(_rolling_sum(event_count, _TD_QTR),
                     _rolling_sum(event_count, _TD_YEAR))


def ced_144_event_sum_5d_pct_of_63d(event_count: pd.Series) -> pd.Series:
    """5-day event sum as fraction of 63-day event sum."""
    return _safe_div(_rolling_sum(event_count, _TD_WK),
                     _rolling_sum(event_count, _TD_QTR))


def ced_145_event_close_drawdown_interaction(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """event_count * (1 - close / expanding_max(close)): events at all-time-low trough."""
    exp_max = close.expanding(min_periods=1).max()
    pct_off = (1.0 - _safe_div(close, exp_max)).fillna(0.0).clip(lower=0.0)
    return event_count * pct_off


def ced_146_event_close_below_2y_low_flag(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of event_count on days where close is at a 2-year low (trailing 504 days)."""
    prev_low = close.shift(1).rolling(_TD_2Y, min_periods=max(1, _TD_2Y // 4)).min()
    at_low   = (close <= prev_low).astype(float)
    return _rolling_sum(event_count * at_low, _TD_2Y)


def ced_147_event_sum_scaled_by_price_volatility(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """63-day event sum scaled by 63-day close price volatility (std of log returns)."""
    lr     = _log_ret(close)
    vol63  = _rolling_std(lr, _TD_QTR)
    s63    = _rolling_sum(event_count, _TD_QTR)
    return s63 * vol63


def ced_148_event_rate_above_1sigma_frac_252d(event_count: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where event_count > mean + 1*std (1-sigma spike frequency)."""
    mu  = _rolling_mean(event_count, _TD_YEAR)
    sig = _rolling_std(event_count, _TD_YEAR)
    above = (event_count > (mu + sig)).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def ced_149_event_ewm_acceleration_63d(event_count: pd.Series) -> pd.Series:
    """EWM(span=5) of event_count minus EWM(span=63): short vs medium EWM momentum."""
    return _ewm_mean(event_count, _TD_WK) - _ewm_mean(event_count, _TD_QTR)


def ced_150_event_density_full_composite(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """
    Full composite event density score combining z-score, active-frac, and price-proximity.
    Equally weighted average of: 252-day z-score, 252-day active-day fraction,
    and event_count * pct-off-252d-high.
    """
    z252     = _zscore_rolling(event_count, _TD_YEAR)
    af252    = _safe_div(_active_days(event_count, _TD_YEAR),
                         pd.Series(_TD_YEAR, index=event_count.index, dtype=float))
    high252  = _rolling_max(close, _TD_YEAR)
    pct_off  = (1.0 - _safe_div(close, high252)).fillna(0.0).clip(lower=0.0)
    prox_sig = _zscore_rolling(event_count * pct_off, _TD_YEAR)
    return (z252 + af252 + prox_sig) / 3.0


# --- Group K (176-200): Extended interaction, quantile, and momentum features ---

def ced_176_event_sum_x_pos_ret_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day sum of event_count * positive log return: events on up-days."""
    lr     = _log_ret(close)
    pos_lr = lr.clip(lower=0.0)
    return _rolling_sum(event_count * pos_lr, _TD_QTR)


def ced_177_event_sum_x_pos_ret_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day sum of event_count * positive log return."""
    lr     = _log_ret(close)
    pos_lr = lr.clip(lower=0.0)
    return _rolling_sum(event_count * pos_lr, _TD_YEAR)


def ced_178_event_price_corr_126d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 126-day correlation between event_count and daily log return."""
    lr = _log_ret(close)
    return event_count.rolling(_TD_2Q, min_periods=max(2, _TD_2Q // 4)).corr(lr)


def ced_179_event_sum_q90_thresh_63d(event_count: pd.Series) -> pd.Series:
    """Rolling 63-day 90th-percentile threshold of event_count."""
    return event_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).quantile(0.90)


def ced_180_event_sum_q75_thresh_252d(event_count: pd.Series) -> pd.Series:
    """Rolling 252-day 75th-percentile threshold of event_count."""
    return event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.75)


def ced_181_event_sum_q10_thresh_252d(event_count: pd.Series) -> pd.Series:
    """Rolling 252-day 10th-percentile threshold of event_count."""
    return event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.10)


def ced_182_event_below_q25_frac_252d(event_count: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where event_count is below its 25th percentile."""
    q25 = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.25)
    return _rolling_mean((event_count < q25).astype(float), _TD_YEAR)


def ced_183_event_inter_arrival_mean_252d(event_count: pd.Series) -> pd.Series:
    """Mean inter-arrival time over trailing 252 days (window / (1 + active_count))."""
    active = _active_days(event_count, _TD_YEAR)
    return _safe_div(pd.Series(_TD_YEAR, index=event_count.index, dtype=float), active + 1.0)


def ced_184_event_slope_21d(event_count: pd.Series) -> pd.Series:
    """OLS slope of event_count over trailing 21 days (short-term trend in event rate)."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    return event_count.rolling(_TD_MO, min_periods=max(2, _TD_MO // 4)).apply(_slope, raw=True)


def ced_185_event_slope_126d(event_count: pd.Series) -> pd.Series:
    """OLS slope of event_count over trailing 126 days (2-quarter trend)."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        d  = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    return event_count.rolling(_TD_2Q, min_periods=max(2, _TD_2Q // 4)).apply(_slope, raw=True)


def ced_186_event_cv_21d(event_count: pd.Series) -> pd.Series:
    """Coefficient of variation of event_count over 21 days."""
    return _safe_div(_rolling_std(event_count, _TD_MO),
                     _rolling_mean(event_count, _TD_MO))


def ced_187_event_cv_126d(event_count: pd.Series) -> pd.Series:
    """Coefficient of variation of event_count over 126 days."""
    return _safe_div(_rolling_std(event_count, _TD_2Q),
                     _rolling_mean(event_count, _TD_2Q))


def ced_188_event_log_sum_21d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 21-day rolling event sum)."""
    return np.log1p(_rolling_sum(event_count, _TD_MO))


def ced_189_event_log_sum_126d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 126-day rolling event sum)."""
    return np.log1p(_rolling_sum(event_count, _TD_2Q))


def ced_190_event_log_intensity_126d(event_count: pd.Series) -> pd.Series:
    """Log of (1 + 126-day mean event rate): semi-annual Poisson intensity."""
    return np.log1p(_rolling_mean(event_count, _TD_2Q))


def ced_191_event_rolling_std_21d(event_count: pd.Series) -> pd.Series:
    """Rolling std of event_count over 21 days — short-run event-rate dispersion."""
    return _rolling_std(event_count, _TD_MO)


def ced_192_event_rolling_std_126d(event_count: pd.Series) -> pd.Series:
    """Rolling std of event_count over 126 days."""
    return _rolling_std(event_count, _TD_2Q)


def ced_193_event_sum_bottom_decile_frac_252d(event_count: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days in the bottom decile of event_count."""
    q10 = event_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.10)
    return _rolling_mean((event_count <= q10).astype(float), _TD_YEAR)


def ced_194_event_above_1sigma_63d_flag(event_count: pd.Series) -> pd.Series:
    """Binary: 1 if event_count exceeds mean + 1*std over trailing 63 days."""
    mu  = _rolling_mean(event_count, _TD_QTR)
    sig = _rolling_std(event_count, _TD_QTR)
    return (event_count > (mu + sig)).astype(float)


def ced_195_event_sum_at_new_high_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling sum of event_count on days when close sets a 252-day high."""
    prev_high = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()
    new_high  = (close >= prev_high).astype(float)
    return _rolling_sum(event_count * new_high, _TD_YEAR)


def ced_196_event_frac_active_near_52w_low(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of event-active days (trailing 252d) when close <= 110% of 252-day low."""
    low252   = _rolling_min(close, _TD_YEAR)
    near_low = (close <= low252 * 1.10).astype(float)
    active   = (event_count > 0).astype(float)
    return _safe_div(_rolling_sum(active * near_low, _TD_YEAR),
                     _active_days(event_count, _TD_YEAR))


def ced_197_event_ewm_vs_rolling_mean_21d(event_count: pd.Series) -> pd.Series:
    """21-day EWM mean minus 21-day rolling mean: short-memory vs uniform difference."""
    return _ewm_mean(event_count, _TD_MO) - _rolling_mean(event_count, _TD_MO)


def ced_198_event_sum_21d_pct_of_504d(event_count: pd.Series) -> pd.Series:
    """21-day event sum as fraction of 504-day event sum."""
    return _safe_div(_rolling_sum(event_count, _TD_MO),
                     _rolling_sum(event_count, _TD_2Y))


def ced_199_event_intensity_vs_ewm_126d(event_count: pd.Series) -> pd.Series:
    """Ratio of event_count to its 126-day EWM: current vs semi-annual intensity."""
    return _safe_div(event_count, _ewm_mean(event_count, _TD_2Q))


def ced_200_event_density_composite_v3(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite v3: average of 252d z-score of event_count, 63d active-day fraction
    z-scored over 252d, and 252d event sum / close-drawdown interaction z-score.
    """
    z_ec   = _zscore_rolling(event_count, _TD_YEAR)
    af63   = _safe_div(_active_days(event_count, _TD_QTR),
                       pd.Series(_TD_QTR, index=event_count.index, dtype=float))
    z_af   = _zscore_rolling(af63, _TD_YEAR)
    high252= _rolling_max(close, _TD_YEAR)
    pct_off= (1.0 - _safe_div(close, high252)).fillna(0.0).clip(lower=0.0)
    combo  = _rolling_sum(event_count, _TD_YEAR) * pct_off
    z_combo= _zscore_rolling(combo, _TD_YEAR)
    return (z_ec + z_af + z_combo) / 3.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

CORPORATE_EVENT_DENSITY_REGISTRY_076_150 = {
    "ced_076_event_sum_qoq_change":                    {"inputs": ["event_count"],               "func": ced_076_event_sum_qoq_change},
    "ced_077_event_sum_yoy_change":                    {"inputs": ["event_count"],               "func": ced_077_event_sum_yoy_change},
    "ced_078_event_mean_qoq_change":                   {"inputs": ["event_count"],               "func": ced_078_event_mean_qoq_change},
    "ced_079_event_mean_yoy_change":                   {"inputs": ["event_count"],               "func": ced_079_event_mean_yoy_change},
    "ced_080_event_active_frac_qoq_change":            {"inputs": ["event_count"],               "func": ced_080_event_active_frac_qoq_change},
    "ced_081_event_active_frac_yoy_change":            {"inputs": ["event_count"],               "func": ced_081_event_active_frac_yoy_change},
    "ced_082_event_sum_2q_change":                     {"inputs": ["event_count"],               "func": ced_082_event_sum_2q_change},
    "ced_083_event_mean_mo_change":                    {"inputs": ["event_count"],               "func": ced_083_event_mean_mo_change},
    "ced_084_event_mean_wk_change":                    {"inputs": ["event_count"],               "func": ced_084_event_mean_wk_change},
    "ced_085_event_pct_rank_qoq_change":               {"inputs": ["event_count"],               "func": ced_085_event_pct_rank_qoq_change},
    "ced_086_event_zscore_qoq_change":                 {"inputs": ["event_count"],               "func": ced_086_event_zscore_qoq_change},
    "ced_087_event_zscore_yoy_change":                 {"inputs": ["event_count"],               "func": ced_087_event_zscore_yoy_change},
    "ced_088_event_sum_5d_qoq_ratio":                  {"inputs": ["event_count"],               "func": ced_088_event_sum_5d_qoq_ratio},
    "ced_089_event_sum_21d_yoy_ratio":                 {"inputs": ["event_count"],               "func": ced_089_event_sum_21d_yoy_ratio},
    "ced_090_event_sum_63d_yoy_ratio":                 {"inputs": ["event_count"],               "func": ced_090_event_sum_63d_yoy_ratio},
    "ced_091_event_log_intensity_21d":                 {"inputs": ["event_count"],               "func": ced_091_event_log_intensity_21d},
    "ced_092_event_log_intensity_63d":                 {"inputs": ["event_count"],               "func": ced_092_event_log_intensity_63d},
    "ced_093_event_log_intensity_252d":                {"inputs": ["event_count"],               "func": ced_093_event_log_intensity_252d},
    "ced_094_event_log_count_today":                   {"inputs": ["event_count"],               "func": ced_094_event_log_count_today},
    "ced_095_event_log_sum_63d":                       {"inputs": ["event_count"],               "func": ced_095_event_log_sum_63d},
    "ced_096_event_log_sum_252d":                      {"inputs": ["event_count"],               "func": ced_096_event_log_sum_252d},
    "ced_097_event_intensity_vs_ewm_21d":              {"inputs": ["event_count"],               "func": ced_097_event_intensity_vs_ewm_21d},
    "ced_098_event_intensity_vs_ewm_63d":              {"inputs": ["event_count"],               "func": ced_098_event_intensity_vs_ewm_63d},
    "ced_099_event_intensity_vs_ewm_252d":             {"inputs": ["event_count"],               "func": ced_099_event_intensity_vs_ewm_252d},
    "ced_100_event_above_2sigma_63d_flag":             {"inputs": ["event_count"],               "func": ced_100_event_above_2sigma_63d_flag},
    "ced_101_event_above_2sigma_252d_flag":            {"inputs": ["event_count"],               "func": ced_101_event_above_2sigma_252d_flag},
    "ced_102_event_above_3sigma_252d_flag":            {"inputs": ["event_count"],               "func": ced_102_event_above_3sigma_252d_flag},
    "ced_103_event_sum_spike_count_63d":               {"inputs": ["event_count"],               "func": ced_103_event_sum_spike_count_63d},
    "ced_104_event_sum_spike_count_252d":              {"inputs": ["event_count"],               "func": ced_104_event_sum_spike_count_252d},
    "ced_105_event_inter_arrival_mean_63d":            {"inputs": ["event_count"],               "func": ced_105_event_inter_arrival_mean_63d},
    "ced_106_event_sum_during_price_decline_63d":      {"inputs": ["event_count", "close"],      "func": ced_106_event_sum_during_price_decline_63d},
    "ced_107_event_sum_during_price_decline_252d":     {"inputs": ["event_count", "close"],      "func": ced_107_event_sum_during_price_decline_252d},
    "ced_108_event_sum_price_down_days_63d":           {"inputs": ["event_count", "close"],      "func": ced_108_event_sum_price_down_days_63d},
    "ced_109_event_sum_price_down_days_252d":          {"inputs": ["event_count", "close"],      "func": ced_109_event_sum_price_down_days_252d},
    "ced_110_event_density_near_52w_low":              {"inputs": ["event_count", "close"],      "func": ced_110_event_density_near_52w_low},
    "ced_111_event_frac_during_drawdown_63d":          {"inputs": ["event_count", "close"],      "func": ced_111_event_frac_during_drawdown_63d},
    "ced_112_event_price_corr_63d":                    {"inputs": ["event_count", "close"],      "func": ced_112_event_price_corr_63d},
    "ced_113_event_price_corr_252d":                   {"inputs": ["event_count", "close"],      "func": ced_113_event_price_corr_252d},
    "ced_114_event_sum_x_neg_ret_63d":                 {"inputs": ["event_count", "close"],      "func": ced_114_event_sum_x_neg_ret_63d},
    "ced_115_event_sum_x_neg_ret_252d":                {"inputs": ["event_count", "close"],      "func": ced_115_event_sum_x_neg_ret_252d},
    "ced_116_event_density_vs_price_pct_from_high_63d":  {"inputs": ["event_count", "close"],   "func": ced_116_event_density_vs_price_pct_from_high_63d},
    "ced_117_event_density_vs_price_pct_from_high_252d": {"inputs": ["event_count", "close"],   "func": ced_117_event_density_vs_price_pct_from_high_252d},
    "ced_118_event_sum_below_52w_low_flag":            {"inputs": ["event_count", "close"],      "func": ced_118_event_sum_below_52w_low_flag},
    "ced_119_event_active_frac_below_1y_mean":         {"inputs": ["event_count", "close"],      "func": ced_119_event_active_frac_below_1y_mean},
    "ced_120_event_count_pct_from_high_product":       {"inputs": ["event_count", "close"],      "func": ced_120_event_count_pct_from_high_product},
    "ced_121_event_slope_63d":                         {"inputs": ["event_count"],               "func": ced_121_event_slope_63d},
    "ced_122_event_slope_252d":                        {"inputs": ["event_count"],               "func": ced_122_event_slope_252d},
    "ced_123_event_cv_63d":                            {"inputs": ["event_count"],               "func": ced_123_event_cv_63d},
    "ced_124_event_cv_252d":                           {"inputs": ["event_count"],               "func": ced_124_event_cv_252d},
    "ced_125_event_rolling_median_63d":                {"inputs": ["event_count"],               "func": ced_125_event_rolling_median_63d},
    "ced_126_event_rolling_median_252d":               {"inputs": ["event_count"],               "func": ced_126_event_rolling_median_252d},
    "ced_127_event_above_median_frac_252d":            {"inputs": ["event_count"],               "func": ced_127_event_above_median_frac_252d},
    "ced_128_event_max_minus_median_63d":              {"inputs": ["event_count"],               "func": ced_128_event_max_minus_median_63d},
    "ced_129_event_max_minus_median_252d":             {"inputs": ["event_count"],               "func": ced_129_event_max_minus_median_252d},
    "ced_130_event_sum_top_decile_days_252d":          {"inputs": ["event_count"],               "func": ced_130_event_sum_top_decile_days_252d},
    "ced_131_event_sum_top_quintile_days_252d":        {"inputs": ["event_count"],               "func": ced_131_event_sum_top_quintile_days_252d},
    "ced_132_event_iqr_252d":                          {"inputs": ["event_count"],               "func": ced_132_event_iqr_252d},
    "ced_133_event_iqr_63d":                           {"inputs": ["event_count"],               "func": ced_133_event_iqr_63d},
    "ced_134_event_consecutive_active_streak":         {"inputs": ["event_count"],               "func": ced_134_event_consecutive_active_streak},
    "ced_135_event_consecutive_inactive_streak":       {"inputs": ["event_count"],               "func": ced_135_event_consecutive_inactive_streak},
    "ced_136_event_sum_21d_vs_252d_excess":            {"inputs": ["event_count"],               "func": ced_136_event_sum_21d_vs_252d_excess},
    "ced_137_event_sum_63d_vs_252d_excess":            {"inputs": ["event_count"],               "func": ced_137_event_sum_63d_vs_252d_excess},
    "ced_138_event_ewm_vs_rolling_mean_63d":           {"inputs": ["event_count"],               "func": ced_138_event_ewm_vs_rolling_mean_63d},
    "ced_139_event_ewm_vs_rolling_mean_252d":          {"inputs": ["event_count"],               "func": ced_139_event_ewm_vs_rolling_mean_252d},
    "ced_140_event_rolling_max_over_mean_63d":         {"inputs": ["event_count"],               "func": ced_140_event_rolling_max_over_mean_63d},
    "ced_141_event_rolling_max_over_mean_252d":        {"inputs": ["event_count"],               "func": ced_141_event_rolling_max_over_mean_252d},
    "ced_142_event_sum_21d_pct_of_252d":               {"inputs": ["event_count"],               "func": ced_142_event_sum_21d_pct_of_252d},
    "ced_143_event_sum_63d_pct_of_252d":               {"inputs": ["event_count"],               "func": ced_143_event_sum_63d_pct_of_252d},
    "ced_144_event_sum_5d_pct_of_63d":                 {"inputs": ["event_count"],               "func": ced_144_event_sum_5d_pct_of_63d},
    "ced_145_event_close_drawdown_interaction":        {"inputs": ["event_count", "close"],      "func": ced_145_event_close_drawdown_interaction},
    "ced_146_event_close_below_2y_low_flag":           {"inputs": ["event_count", "close"],      "func": ced_146_event_close_below_2y_low_flag},
    "ced_147_event_sum_scaled_by_price_volatility":    {"inputs": ["event_count", "close"],      "func": ced_147_event_sum_scaled_by_price_volatility},
    "ced_148_event_rate_above_1sigma_frac_252d":       {"inputs": ["event_count"],               "func": ced_148_event_rate_above_1sigma_frac_252d},
    "ced_149_event_ewm_acceleration_63d":              {"inputs": ["event_count"],               "func": ced_149_event_ewm_acceleration_63d},
    "ced_150_event_density_full_composite":            {"inputs": ["event_count", "close"],      "func": ced_150_event_density_full_composite},
    "ced_176_event_sum_x_pos_ret_63d":                 {"inputs": ["event_count", "close"],      "func": ced_176_event_sum_x_pos_ret_63d},
    "ced_177_event_sum_x_pos_ret_252d":                {"inputs": ["event_count", "close"],      "func": ced_177_event_sum_x_pos_ret_252d},
    "ced_178_event_price_corr_126d":                   {"inputs": ["event_count", "close"],      "func": ced_178_event_price_corr_126d},
    "ced_179_event_sum_q90_thresh_63d":                {"inputs": ["event_count"],               "func": ced_179_event_sum_q90_thresh_63d},
    "ced_180_event_sum_q75_thresh_252d":               {"inputs": ["event_count"],               "func": ced_180_event_sum_q75_thresh_252d},
    "ced_181_event_sum_q10_thresh_252d":               {"inputs": ["event_count"],               "func": ced_181_event_sum_q10_thresh_252d},
    "ced_182_event_below_q25_frac_252d":               {"inputs": ["event_count"],               "func": ced_182_event_below_q25_frac_252d},
    "ced_183_event_inter_arrival_mean_252d":           {"inputs": ["event_count"],               "func": ced_183_event_inter_arrival_mean_252d},
    "ced_184_event_slope_21d":                         {"inputs": ["event_count"],               "func": ced_184_event_slope_21d},
    "ced_185_event_slope_126d":                        {"inputs": ["event_count"],               "func": ced_185_event_slope_126d},
    "ced_186_event_cv_21d":                            {"inputs": ["event_count"],               "func": ced_186_event_cv_21d},
    "ced_187_event_cv_126d":                           {"inputs": ["event_count"],               "func": ced_187_event_cv_126d},
    "ced_188_event_log_sum_21d":                       {"inputs": ["event_count"],               "func": ced_188_event_log_sum_21d},
    "ced_189_event_log_sum_126d":                      {"inputs": ["event_count"],               "func": ced_189_event_log_sum_126d},
    "ced_190_event_log_intensity_126d":                {"inputs": ["event_count"],               "func": ced_190_event_log_intensity_126d},
    "ced_191_event_rolling_std_21d":                   {"inputs": ["event_count"],               "func": ced_191_event_rolling_std_21d},
    "ced_192_event_rolling_std_126d":                  {"inputs": ["event_count"],               "func": ced_192_event_rolling_std_126d},
    "ced_193_event_sum_bottom_decile_frac_252d":       {"inputs": ["event_count"],               "func": ced_193_event_sum_bottom_decile_frac_252d},
    "ced_194_event_above_1sigma_63d_flag":             {"inputs": ["event_count"],               "func": ced_194_event_above_1sigma_63d_flag},
    "ced_195_event_sum_at_new_high_252d":              {"inputs": ["event_count", "close"],      "func": ced_195_event_sum_at_new_high_252d},
    "ced_196_event_frac_active_near_52w_low":          {"inputs": ["event_count", "close"],      "func": ced_196_event_frac_active_near_52w_low},
    "ced_197_event_ewm_vs_rolling_mean_21d":           {"inputs": ["event_count"],               "func": ced_197_event_ewm_vs_rolling_mean_21d},
    "ced_198_event_sum_21d_pct_of_504d":               {"inputs": ["event_count"],               "func": ced_198_event_sum_21d_pct_of_504d},
    "ced_199_event_intensity_vs_ewm_126d":             {"inputs": ["event_count"],               "func": ced_199_event_intensity_vs_ewm_126d},
    "ced_200_event_density_composite_v3":              {"inputs": ["event_count", "close"],      "func": ced_200_event_density_composite_v3},
}
