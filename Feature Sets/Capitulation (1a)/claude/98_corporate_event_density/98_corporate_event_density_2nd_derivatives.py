"""
98_corporate_event_density — 2nd-Derivative Features 001-075
Domain: rate of change of base corporate-event-density features (acceleration)
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

The 2nd-derivative series capture the acceleration / rate-of-change of base
event-density features over QoQ / YoY / short-window horizons.  Sparse or
stepwise output on event-driven data is expected and fine.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding(). Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.
This file is self-contained: base computations are inlined as private helpers.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _active_days(s: pd.Series, w: int) -> pd.Series:
    return _rolling_sum((s > 0).astype(float), w)


def _log_ret(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1).replace(0, np.nan))


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# Inline the relevant base computations so this file needs no cross-import.

def _event_sum_63d(event_count: pd.Series) -> pd.Series:
    return _rolling_sum(event_count, _TD_QTR)


def _event_sum_252d(event_count: pd.Series) -> pd.Series:
    return _rolling_sum(event_count, _TD_YEAR)


def _event_mean_63d(event_count: pd.Series) -> pd.Series:
    return _rolling_mean(event_count, _TD_QTR)


def _event_mean_252d(event_count: pd.Series) -> pd.Series:
    return _rolling_mean(event_count, _TD_YEAR)


def _event_mean_21d(event_count: pd.Series) -> pd.Series:
    return _rolling_mean(event_count, _TD_MO)


def _event_zscore_252d(event_count: pd.Series) -> pd.Series:
    m  = _rolling_mean(event_count, _TD_YEAR)
    sd = _rolling_std(event_count, _TD_YEAR)
    return _safe_div(event_count - m, sd)


def _event_zscore_63d(event_count: pd.Series) -> pd.Series:
    m  = _rolling_mean(event_count, _TD_QTR)
    sd = _rolling_std(event_count, _TD_QTR)
    return _safe_div(event_count - m, sd)


def _event_pct_rank_252d(event_count: pd.Series) -> pd.Series:
    return _rolling_rank_pct(event_count, _TD_YEAR)


def _active_day_frac_63d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(event_count, _TD_QTR),
                     pd.Series(_TD_QTR, index=event_count.index, dtype=float))


def _active_day_frac_252d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(event_count, _TD_YEAR),
                     pd.Series(_TD_YEAR, index=event_count.index, dtype=float))


def _burst_ratio_21d_vs_252d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(event_count, _TD_MO),
                     _rolling_mean(event_count, _TD_YEAR))


def _burst_ratio_5d_vs_63d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(event_count, _TD_WK),
                     _rolling_mean(event_count, _TD_QTR))


def _event_ewm_mean_63d(event_count: pd.Series) -> pd.Series:
    return _ewm_mean(event_count, _TD_QTR)


def _event_log_intensity_63d(event_count: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(event_count, _TD_QTR))


def _event_sum_during_price_decline_63d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    below_avg = (close < _rolling_mean(close, _TD_QTR)).astype(float)
    return _rolling_sum(event_count * below_avg, _TD_QTR)


def _event_cv_252d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_std(event_count, _TD_YEAR),
                     _rolling_mean(event_count, _TD_YEAR))


def _event_sum_21d(event_count: pd.Series) -> pd.Series:
    return _rolling_sum(event_count, _TD_MO)


def _event_sum_5d(event_count: pd.Series) -> pd.Series:
    return _rolling_sum(event_count, _TD_WK)


def _event_mean_5d(event_count: pd.Series) -> pd.Series:
    return _rolling_mean(event_count, _TD_WK)


def _event_mean_126d(event_count: pd.Series) -> pd.Series:
    return _rolling_mean(event_count, _TD_2Q)


def _event_zscore_21d(event_count: pd.Series) -> pd.Series:
    m  = _rolling_mean(event_count, _TD_MO)
    sd = _rolling_std(event_count, _TD_MO)
    return _safe_div(event_count - m, sd)


def _event_pct_rank_63d(event_count: pd.Series) -> pd.Series:
    return _rolling_rank_pct(event_count, _TD_QTR)


def _active_day_frac_21d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_active_days(event_count, _TD_MO),
                     pd.Series(_TD_MO, index=event_count.index, dtype=float))


def _burst_ratio_5d_vs_252d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(event_count, _TD_WK),
                     _rolling_mean(event_count, _TD_YEAR))


def _burst_ratio_21d_vs_126d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(event_count, _TD_MO),
                     _rolling_mean(event_count, _TD_2Q))


def _event_log_intensity_21d(event_count: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(event_count, _TD_MO))


def _event_log_intensity_252d(event_count: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(event_count, _TD_YEAR))


def _event_cv_63d(event_count: pd.Series) -> pd.Series:
    return _safe_div(_rolling_std(event_count, _TD_QTR),
                     _rolling_mean(event_count, _TD_QTR))


def _event_ewm_mean_21d(event_count: pd.Series) -> pd.Series:
    return _ewm_mean(event_count, _TD_MO)


def _event_ewm_mean_252d(event_count: pd.Series) -> pd.Series:
    return _ewm_mean(event_count, _TD_YEAR)


def _event_max_63d(event_count: pd.Series) -> pd.Series:
    return _rolling_max(event_count, _TD_QTR)


def _event_max_252d(event_count: pd.Series) -> pd.Series:
    return _rolling_max(event_count, _TD_YEAR)


def _event_rolling_std_63d(event_count: pd.Series) -> pd.Series:
    return _rolling_std(event_count, _TD_QTR)


def _event_rolling_std_252d(event_count: pd.Series) -> pd.Series:
    return _rolling_std(event_count, _TD_YEAR)


def _event_sum_during_price_decline_252d(event_count: pd.Series, close: pd.Series) -> pd.Series:
    below_avg = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_sum(event_count * below_avg, _TD_YEAR)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def ced_drv2_001_event_sum_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day rolling event sum (acceleration of quarterly count)."""
    base = _event_sum_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_002_event_sum_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day rolling event sum."""
    base = _event_sum_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_003_event_mean_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day mean event rate."""
    base = _event_mean_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_004_event_mean_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day mean event rate."""
    base = _event_mean_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_005_event_mean_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21-day mean event rate."""
    base = _event_mean_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_006_event_zscore_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day z-score of event_count."""
    base = _event_zscore_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_007_event_zscore_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day z-score of event_count."""
    base = _event_zscore_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_008_event_zscore_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day z-score of event_count."""
    base = _event_zscore_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_009_event_pct_rank_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day percentile rank of event_count."""
    base = _event_pct_rank_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_010_event_active_frac_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day active-day fraction."""
    base = _active_day_frac_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_011_event_active_frac_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day active-day fraction."""
    base = _active_day_frac_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_012_burst_ratio_21d_vs_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 21d-vs-252d burst ratio."""
    base = _burst_ratio_21d_vs_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_013_burst_ratio_5d_vs_63d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 5d-vs-63d burst ratio."""
    base = _burst_ratio_5d_vs_63d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_014_event_ewm_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day EWM mean event rate."""
    base = _event_ewm_mean_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_015_event_log_intensity_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the log(1+mean_63d) Poisson intensity."""
    base = _event_log_intensity_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_016_event_sum_decline_63d_qoq_diff(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the 63-day event sum during price-decline days."""
    base = _event_sum_during_price_decline_63d(event_count, close)
    return base - base.shift(_TD_QTR)


def ced_drv2_017_event_cv_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day coefficient of variation of event_count."""
    base = _event_cv_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_018_event_sum_63d_ewm_diff(event_count: pd.Series) -> pd.Series:
    """63-day event sum minus its 4-quarter EWM (span=252): burst vs its own trend."""
    base = _event_sum_63d(event_count)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def ced_drv2_019_event_zscore_slope_of_zscore(event_count: pd.Series) -> pd.Series:
    """
    Rolling 63-day OLS slope of the 252-day z-score series.
    Captures the trend in z-score momentum (second-order acceleration).
    """
    base = _event_zscore_252d(event_count)

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

    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def ced_drv2_020_event_mean_63d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 63-day mean event rate (longer-horizon acceleration)."""
    base = _event_mean_63d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_021_event_pct_rank_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day percentile rank of event_count."""
    base = _event_pct_rank_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_022_event_active_frac_63d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 63-day active-day fraction."""
    base = _active_day_frac_63d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_023_event_sum_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day rolling event sum."""
    base = _event_sum_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_024_event_zscore_252d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 252-day z-score of event_count."""
    base = _event_zscore_252d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_025_event_density_accel_composite(event_count: pd.Series) -> pd.Series:
    """
    Composite 2nd-derivative acceleration score: equally weighted sum of three
    QoQ-diff series (z-score_252d, active_frac_63d, log_intensity_63d).
    """
    dz   = _event_zscore_252d(event_count)
    daf  = _active_day_frac_63d(event_count)
    dli  = _event_log_intensity_63d(event_count)
    return ((dz  - dz.shift(_TD_QTR)) +
            (daf - daf.shift(_TD_QTR)) +
            (dli - dli.shift(_TD_QTR))) / 3.0


# --- 2nd-derivative features 026-075 ---

def ced_drv2_026_event_sum_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21-day rolling event sum."""
    base = _event_sum_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_027_event_sum_5d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 5-day rolling event sum."""
    base = _event_sum_5d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_028_event_mean_5d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 5-day rolling mean event rate."""
    base = _event_mean_5d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_029_event_mean_126d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 126-day rolling mean event rate."""
    base = _event_mean_126d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_030_event_mean_126d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 126-day rolling mean event rate."""
    base = _event_mean_126d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_031_event_zscore_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21-day z-score of event_count."""
    base = _event_zscore_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_032_event_zscore_21d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 21-day z-score of event_count."""
    base = _event_zscore_21d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_033_event_pct_rank_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day percentile rank of event_count."""
    base = _event_pct_rank_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_034_event_pct_rank_63d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 63-day percentile rank of event_count."""
    base = _event_pct_rank_63d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_035_event_active_frac_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21-day active-day fraction."""
    base = _active_day_frac_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_036_event_active_frac_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day active-day fraction."""
    base = _active_day_frac_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_037_burst_ratio_5d_vs_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 5d-vs-252d burst ratio."""
    base = _burst_ratio_5d_vs_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_038_burst_ratio_5d_vs_252d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 5d-vs-252d burst ratio."""
    base = _burst_ratio_5d_vs_252d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_039_burst_ratio_21d_vs_126d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 21d-vs-126d burst ratio."""
    base = _burst_ratio_21d_vs_126d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_040_burst_ratio_21d_vs_252d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21d-vs-252d burst ratio."""
    base = _burst_ratio_21d_vs_252d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_041_event_log_intensity_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the log(1+mean_21d) Poisson intensity."""
    base = _event_log_intensity_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_042_event_log_intensity_21d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the log(1+mean_21d) Poisson intensity."""
    base = _event_log_intensity_21d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_043_event_log_intensity_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the log(1+mean_252d) annual Poisson intensity."""
    base = _event_log_intensity_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_044_event_log_intensity_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the log(1+mean_252d) annual Poisson intensity."""
    base = _event_log_intensity_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_045_event_cv_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day coefficient of variation of event_count."""
    base = _event_cv_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_046_event_cv_63d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 63-day coefficient of variation."""
    base = _event_cv_63d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_047_event_ewm_21d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 21-day EWM mean event rate."""
    base = _event_ewm_mean_21d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_048_event_ewm_252d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 252-day EWM mean event rate."""
    base = _event_ewm_mean_252d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_049_event_ewm_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day EWM mean event rate."""
    base = _event_ewm_mean_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_050_event_max_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day rolling maximum of event_count."""
    base = _event_max_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_051_event_max_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day rolling maximum of event_count."""
    base = _event_max_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_052_event_rolling_std_63d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 63-day rolling std of event_count."""
    base = _event_rolling_std_63d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_053_event_rolling_std_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day rolling std of event_count."""
    base = _event_rolling_std_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_054_event_sum_decline_252d_yoy_diff(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in the 252-day event sum during price-decline days."""
    base = _event_sum_during_price_decline_252d(event_count, close)
    return base - base.shift(_TD_YEAR)


def ced_drv2_055_event_sum_decline_63d_mo_diff(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """Month-over-month change in the 63-day event sum during price-decline days."""
    base = _event_sum_during_price_decline_63d(event_count, close)
    return base - base.shift(_TD_MO)


def ced_drv2_056_event_sum_63d_ewm_diff_qoq(event_count: pd.Series) -> pd.Series:
    """QoQ change in the (63d sum - 252d EWM of 63d sum) excess."""
    s63 = _event_sum_63d(event_count)
    ewm = s63.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base = s63 - ewm
    return base - base.shift(_TD_QTR)


def ced_drv2_057_event_zscore_slope_of_zscore_63d(event_count: pd.Series) -> pd.Series:
    """21-day OLS slope of the 63-day z-score series (short-run z-score trend)."""
    base = _event_zscore_63d(event_count)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    return base.rolling(_TD_MO, min_periods=max(2, _TD_MO // 4)).apply(_slope, raw=True)


def ced_drv2_058_event_pct_rank_252d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 252-day percentile rank of event_count."""
    base = _event_pct_rank_252d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_059_event_active_frac_63d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 63-day active-day fraction."""
    base = _active_day_frac_63d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_060_event_sum_21d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 21-day rolling event sum."""
    base = _event_sum_21d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_061_event_sum_5d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 5-day rolling event sum."""
    base = _event_sum_5d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_062_event_zscore_63d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 63-day z-score of event_count."""
    base = _event_zscore_63d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_063_event_zscore_252d_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the 252-day z-score of event_count."""
    base = _event_zscore_252d(event_count)
    return base - base.shift(_TD_WK)


def ced_drv2_064_event_mean_21d_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 21-day mean event rate."""
    base = _event_mean_21d(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv2_065_event_mean_21d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 21-day mean event rate."""
    base = _event_mean_21d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_066_event_cv_252d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 252-day coefficient of variation of event_count."""
    base = _event_cv_252d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_067_event_cv_252d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the 252-day coefficient of variation."""
    base = _event_cv_252d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_068_event_sum_63d_qoq_ratio(event_count: pd.Series) -> pd.Series:
    """Ratio of 63-day event sum to its lagged-1Q value (relative acceleration)."""
    base = _event_sum_63d(event_count)
    return _safe_div(base, base.shift(_TD_QTR))


def ced_drv2_069_event_sum_252d_yoy_ratio(event_count: pd.Series) -> pd.Series:
    """Ratio of 252-day event sum to its lagged-1Y value."""
    base = _event_sum_252d(event_count)
    return _safe_div(base, base.shift(_TD_YEAR))


def ced_drv2_070_event_mean_63d_ewm_diff(event_count: pd.Series) -> pd.Series:
    """63-day mean minus its 252d EWM: mean vs its own long-run smoothed trend."""
    base = _event_mean_63d(event_count)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def ced_drv2_071_event_active_frac_63d_2q_diff(event_count: pd.Series) -> pd.Series:
    """Half-year change in the 63-day active-day fraction."""
    base = _active_day_frac_63d(event_count)
    return base - base.shift(_TD_2Q)


def ced_drv2_072_event_log_intensity_63d_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the log(1+mean_63d) Poisson intensity."""
    base = _event_log_intensity_63d(event_count)
    return base - base.shift(_TD_MO)


def ced_drv2_073_event_zscore_slope_of_active_frac(event_count: pd.Series) -> pd.Series:
    """63-day OLS slope of the 252-day active-day fraction series."""
    base = _active_day_frac_252d(event_count)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float); xm = x.mean(); ym = arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d
    return base.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_slope, raw=True)


def ced_drv2_074_event_sum_21d_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the 21-day rolling event sum."""
    base = _event_sum_21d(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv2_075_event_density_accel_composite_v2(event_count: pd.Series) -> pd.Series:
    """
    Composite 2nd-derivative acceleration v2: equally weighted sum of five
    1-month diffs (z21d MoM, z63d MoM, active_frac_21d MoM,
    log_intensity_21d MoM, burst_21d_252d MoM).
    """
    dz21  = _event_zscore_21d(event_count)
    dz63  = _event_zscore_63d(event_count)
    daf21 = _active_day_frac_21d(event_count)
    dli21 = _event_log_intensity_21d(event_count)
    dbr   = _burst_ratio_21d_vs_252d(event_count)
    return ((dz21  - dz21.shift(_TD_MO)) +
            (dz63  - dz63.shift(_TD_MO)) +
            (daf21 - daf21.shift(_TD_MO)) +
            (dli21 - dli21.shift(_TD_MO)) +
            (dbr   - dbr.shift(_TD_MO))) / 5.0


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

CORPORATE_EVENT_DENSITY_REGISTRY_2ND_DERIVATIVES = {
    "ced_drv2_001_event_sum_63d_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv2_001_event_sum_63d_qoq_diff},
    "ced_drv2_002_event_sum_252d_yoy_diff":            {"inputs": ["event_count"],          "func": ced_drv2_002_event_sum_252d_yoy_diff},
    "ced_drv2_003_event_mean_63d_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv2_003_event_mean_63d_qoq_diff},
    "ced_drv2_004_event_mean_252d_yoy_diff":           {"inputs": ["event_count"],          "func": ced_drv2_004_event_mean_252d_yoy_diff},
    "ced_drv2_005_event_mean_21d_mo_diff":             {"inputs": ["event_count"],          "func": ced_drv2_005_event_mean_21d_mo_diff},
    "ced_drv2_006_event_zscore_252d_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv2_006_event_zscore_252d_qoq_diff},
    "ced_drv2_007_event_zscore_252d_yoy_diff":         {"inputs": ["event_count"],          "func": ced_drv2_007_event_zscore_252d_yoy_diff},
    "ced_drv2_008_event_zscore_63d_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv2_008_event_zscore_63d_qoq_diff},
    "ced_drv2_009_event_pct_rank_252d_qoq_diff":       {"inputs": ["event_count"],          "func": ced_drv2_009_event_pct_rank_252d_qoq_diff},
    "ced_drv2_010_event_active_frac_63d_qoq_diff":     {"inputs": ["event_count"],          "func": ced_drv2_010_event_active_frac_63d_qoq_diff},
    "ced_drv2_011_event_active_frac_252d_yoy_diff":    {"inputs": ["event_count"],          "func": ced_drv2_011_event_active_frac_252d_yoy_diff},
    "ced_drv2_012_burst_ratio_21d_vs_252d_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv2_012_burst_ratio_21d_vs_252d_qoq_diff},
    "ced_drv2_013_burst_ratio_5d_vs_63d_wk_diff":      {"inputs": ["event_count"],          "func": ced_drv2_013_burst_ratio_5d_vs_63d_wk_diff},
    "ced_drv2_014_event_ewm_63d_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv2_014_event_ewm_63d_qoq_diff},
    "ced_drv2_015_event_log_intensity_63d_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv2_015_event_log_intensity_63d_qoq_diff},
    "ced_drv2_016_event_sum_decline_63d_qoq_diff":     {"inputs": ["event_count", "close"], "func": ced_drv2_016_event_sum_decline_63d_qoq_diff},
    "ced_drv2_017_event_cv_252d_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv2_017_event_cv_252d_qoq_diff},
    "ced_drv2_018_event_sum_63d_ewm_diff":             {"inputs": ["event_count"],          "func": ced_drv2_018_event_sum_63d_ewm_diff},
    "ced_drv2_019_event_zscore_slope_of_zscore":       {"inputs": ["event_count"],          "func": ced_drv2_019_event_zscore_slope_of_zscore},
    "ced_drv2_020_event_mean_63d_yoy_diff":            {"inputs": ["event_count"],          "func": ced_drv2_020_event_mean_63d_yoy_diff},
    "ced_drv2_021_event_pct_rank_252d_yoy_diff":       {"inputs": ["event_count"],          "func": ced_drv2_021_event_pct_rank_252d_yoy_diff},
    "ced_drv2_022_event_active_frac_63d_yoy_diff":     {"inputs": ["event_count"],          "func": ced_drv2_022_event_active_frac_63d_yoy_diff},
    "ced_drv2_023_event_sum_252d_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv2_023_event_sum_252d_qoq_diff},
    "ced_drv2_024_event_zscore_252d_mo_diff":          {"inputs": ["event_count"],          "func": ced_drv2_024_event_zscore_252d_mo_diff},
    "ced_drv2_025_event_density_accel_composite":      {"inputs": ["event_count"],          "func": ced_drv2_025_event_density_accel_composite},
    "ced_drv2_026_event_sum_21d_mo_diff":              {"inputs": ["event_count"],          "func": ced_drv2_026_event_sum_21d_mo_diff},
    "ced_drv2_027_event_sum_5d_wk_diff":               {"inputs": ["event_count"],          "func": ced_drv2_027_event_sum_5d_wk_diff},
    "ced_drv2_028_event_mean_5d_wk_diff":              {"inputs": ["event_count"],          "func": ced_drv2_028_event_mean_5d_wk_diff},
    "ced_drv2_029_event_mean_126d_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv2_029_event_mean_126d_qoq_diff},
    "ced_drv2_030_event_mean_126d_yoy_diff":           {"inputs": ["event_count"],          "func": ced_drv2_030_event_mean_126d_yoy_diff},
    "ced_drv2_031_event_zscore_21d_mo_diff":           {"inputs": ["event_count"],          "func": ced_drv2_031_event_zscore_21d_mo_diff},
    "ced_drv2_032_event_zscore_21d_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv2_032_event_zscore_21d_qoq_diff},
    "ced_drv2_033_event_pct_rank_63d_qoq_diff":        {"inputs": ["event_count"],          "func": ced_drv2_033_event_pct_rank_63d_qoq_diff},
    "ced_drv2_034_event_pct_rank_63d_mo_diff":         {"inputs": ["event_count"],          "func": ced_drv2_034_event_pct_rank_63d_mo_diff},
    "ced_drv2_035_event_active_frac_21d_mo_diff":      {"inputs": ["event_count"],          "func": ced_drv2_035_event_active_frac_21d_mo_diff},
    "ced_drv2_036_event_active_frac_252d_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv2_036_event_active_frac_252d_qoq_diff},
    "ced_drv2_037_burst_ratio_5d_vs_252d_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv2_037_burst_ratio_5d_vs_252d_qoq_diff},
    "ced_drv2_038_burst_ratio_5d_vs_252d_wk_diff":     {"inputs": ["event_count"],          "func": ced_drv2_038_burst_ratio_5d_vs_252d_wk_diff},
    "ced_drv2_039_burst_ratio_21d_vs_126d_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv2_039_burst_ratio_21d_vs_126d_qoq_diff},
    "ced_drv2_040_burst_ratio_21d_vs_252d_mo_diff":    {"inputs": ["event_count"],          "func": ced_drv2_040_burst_ratio_21d_vs_252d_mo_diff},
    "ced_drv2_041_event_log_intensity_21d_mo_diff":    {"inputs": ["event_count"],          "func": ced_drv2_041_event_log_intensity_21d_mo_diff},
    "ced_drv2_042_event_log_intensity_21d_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv2_042_event_log_intensity_21d_qoq_diff},
    "ced_drv2_043_event_log_intensity_252d_qoq_diff":  {"inputs": ["event_count"],          "func": ced_drv2_043_event_log_intensity_252d_qoq_diff},
    "ced_drv2_044_event_log_intensity_252d_yoy_diff":  {"inputs": ["event_count"],          "func": ced_drv2_044_event_log_intensity_252d_yoy_diff},
    "ced_drv2_045_event_cv_63d_qoq_diff":              {"inputs": ["event_count"],          "func": ced_drv2_045_event_cv_63d_qoq_diff},
    "ced_drv2_046_event_cv_63d_mo_diff":               {"inputs": ["event_count"],          "func": ced_drv2_046_event_cv_63d_mo_diff},
    "ced_drv2_047_event_ewm_21d_mo_diff":              {"inputs": ["event_count"],          "func": ced_drv2_047_event_ewm_21d_mo_diff},
    "ced_drv2_048_event_ewm_252d_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv2_048_event_ewm_252d_qoq_diff},
    "ced_drv2_049_event_ewm_252d_yoy_diff":            {"inputs": ["event_count"],          "func": ced_drv2_049_event_ewm_252d_yoy_diff},
    "ced_drv2_050_event_max_63d_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv2_050_event_max_63d_qoq_diff},
    "ced_drv2_051_event_max_252d_yoy_diff":            {"inputs": ["event_count"],          "func": ced_drv2_051_event_max_252d_yoy_diff},
    "ced_drv2_052_event_rolling_std_63d_qoq_diff":     {"inputs": ["event_count"],          "func": ced_drv2_052_event_rolling_std_63d_qoq_diff},
    "ced_drv2_053_event_rolling_std_252d_yoy_diff":    {"inputs": ["event_count"],          "func": ced_drv2_053_event_rolling_std_252d_yoy_diff},
    "ced_drv2_054_event_sum_decline_252d_yoy_diff":    {"inputs": ["event_count", "close"], "func": ced_drv2_054_event_sum_decline_252d_yoy_diff},
    "ced_drv2_055_event_sum_decline_63d_mo_diff":      {"inputs": ["event_count", "close"], "func": ced_drv2_055_event_sum_decline_63d_mo_diff},
    "ced_drv2_056_event_sum_63d_ewm_diff_qoq":         {"inputs": ["event_count"],          "func": ced_drv2_056_event_sum_63d_ewm_diff_qoq},
    "ced_drv2_057_event_zscore_slope_of_zscore_63d":   {"inputs": ["event_count"],          "func": ced_drv2_057_event_zscore_slope_of_zscore_63d},
    "ced_drv2_058_event_pct_rank_252d_wk_diff":        {"inputs": ["event_count"],          "func": ced_drv2_058_event_pct_rank_252d_wk_diff},
    "ced_drv2_059_event_active_frac_63d_wk_diff":      {"inputs": ["event_count"],          "func": ced_drv2_059_event_active_frac_63d_wk_diff},
    "ced_drv2_060_event_sum_21d_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv2_060_event_sum_21d_qoq_diff},
    "ced_drv2_061_event_sum_5d_qoq_diff":              {"inputs": ["event_count"],          "func": ced_drv2_061_event_sum_5d_qoq_diff},
    "ced_drv2_062_event_zscore_63d_mo_diff":           {"inputs": ["event_count"],          "func": ced_drv2_062_event_zscore_63d_mo_diff},
    "ced_drv2_063_event_zscore_252d_wk_diff":          {"inputs": ["event_count"],          "func": ced_drv2_063_event_zscore_252d_wk_diff},
    "ced_drv2_064_event_mean_21d_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv2_064_event_mean_21d_qoq_diff},
    "ced_drv2_065_event_mean_21d_yoy_diff":            {"inputs": ["event_count"],          "func": ced_drv2_065_event_mean_21d_yoy_diff},
    "ced_drv2_066_event_cv_252d_yoy_diff":             {"inputs": ["event_count"],          "func": ced_drv2_066_event_cv_252d_yoy_diff},
    "ced_drv2_067_event_cv_252d_mo_diff":              {"inputs": ["event_count"],          "func": ced_drv2_067_event_cv_252d_mo_diff},
    "ced_drv2_068_event_sum_63d_qoq_ratio":            {"inputs": ["event_count"],          "func": ced_drv2_068_event_sum_63d_qoq_ratio},
    "ced_drv2_069_event_sum_252d_yoy_ratio":           {"inputs": ["event_count"],          "func": ced_drv2_069_event_sum_252d_yoy_ratio},
    "ced_drv2_070_event_mean_63d_ewm_diff":            {"inputs": ["event_count"],          "func": ced_drv2_070_event_mean_63d_ewm_diff},
    "ced_drv2_071_event_active_frac_63d_2q_diff":      {"inputs": ["event_count"],          "func": ced_drv2_071_event_active_frac_63d_2q_diff},
    "ced_drv2_072_event_log_intensity_63d_mo_diff":    {"inputs": ["event_count"],          "func": ced_drv2_072_event_log_intensity_63d_mo_diff},
    "ced_drv2_073_event_zscore_slope_of_active_frac":  {"inputs": ["event_count"],          "func": ced_drv2_073_event_zscore_slope_of_active_frac},
    "ced_drv2_074_event_sum_21d_yoy_diff":             {"inputs": ["event_count"],          "func": ced_drv2_074_event_sum_21d_yoy_diff},
    "ced_drv2_075_event_density_accel_composite_v2":   {"inputs": ["event_count"],          "func": ced_drv2_075_event_density_accel_composite_v2},
}
