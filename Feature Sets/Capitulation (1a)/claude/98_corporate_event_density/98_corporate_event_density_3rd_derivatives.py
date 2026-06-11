"""
98_corporate_event_density — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative corporate-event-density features (exhaustion/inflection)
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

The 3rd-derivative series capture the rate-of-change of the 2nd-derivative
features — i.e., inflection / exhaustion signals within the event-burst cycle.
Sparse or stepwise output is expected and fine.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding(). Trading-day constants: 1 year = 252 td, 1 quarter = 63 td,
1 month = 21 td, 1 week = 5 td.
This file is self-contained: all base and 2nd-derivative computations are
inlined as private helpers.
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


# ── Base helpers (level-1) ────────────────────────────────────────────────────

def _event_sum_63d(ec: pd.Series) -> pd.Series:
    return _rolling_sum(ec, _TD_QTR)


def _event_sum_252d(ec: pd.Series) -> pd.Series:
    return _rolling_sum(ec, _TD_YEAR)


def _event_mean_63d(ec: pd.Series) -> pd.Series:
    return _rolling_mean(ec, _TD_QTR)


def _event_mean_252d(ec: pd.Series) -> pd.Series:
    return _rolling_mean(ec, _TD_YEAR)


def _event_mean_21d(ec: pd.Series) -> pd.Series:
    return _rolling_mean(ec, _TD_MO)


def _event_zscore_252d(ec: pd.Series) -> pd.Series:
    m  = _rolling_mean(ec, _TD_YEAR)
    sd = _rolling_std(ec, _TD_YEAR)
    return _safe_div(ec - m, sd)


def _event_zscore_63d(ec: pd.Series) -> pd.Series:
    m  = _rolling_mean(ec, _TD_QTR)
    sd = _rolling_std(ec, _TD_QTR)
    return _safe_div(ec - m, sd)


def _event_pct_rank_252d(ec: pd.Series) -> pd.Series:
    return _rolling_rank_pct(ec, _TD_YEAR)


def _active_day_frac_63d(ec: pd.Series) -> pd.Series:
    return _safe_div(_active_days(ec, _TD_QTR),
                     pd.Series(_TD_QTR, index=ec.index, dtype=float))


def _active_day_frac_252d(ec: pd.Series) -> pd.Series:
    return _safe_div(_active_days(ec, _TD_YEAR),
                     pd.Series(_TD_YEAR, index=ec.index, dtype=float))


def _burst_ratio_21d_vs_252d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(ec, _TD_MO),
                     _rolling_mean(ec, _TD_YEAR))


def _burst_ratio_5d_vs_63d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(ec, _TD_WK),
                     _rolling_mean(ec, _TD_QTR))


def _event_ewm_mean_63d(ec: pd.Series) -> pd.Series:
    return _ewm_mean(ec, _TD_QTR)


def _event_log_intensity_63d(ec: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(ec, _TD_QTR))


def _event_cv_252d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_std(ec, _TD_YEAR),
                     _rolling_mean(ec, _TD_YEAR))


def _event_sum_during_price_decline_63d(ec: pd.Series, close: pd.Series) -> pd.Series:
    below_avg = (close < _rolling_mean(close, _TD_QTR)).astype(float)
    return _rolling_sum(ec * below_avg, _TD_QTR)


def _event_sum_21d(ec: pd.Series) -> pd.Series:
    return _rolling_sum(ec, _TD_MO)


def _event_sum_5d(ec: pd.Series) -> pd.Series:
    return _rolling_sum(ec, _TD_WK)


def _event_mean_5d(ec: pd.Series) -> pd.Series:
    return _rolling_mean(ec, _TD_WK)


def _event_mean_126d(ec: pd.Series) -> pd.Series:
    return _rolling_mean(ec, _TD_2Q)


def _event_zscore_21d(ec: pd.Series) -> pd.Series:
    m  = _rolling_mean(ec, _TD_MO)
    sd = _rolling_std(ec, _TD_MO)
    return _safe_div(ec - m, sd)


def _event_pct_rank_63d(ec: pd.Series) -> pd.Series:
    return _rolling_rank_pct(ec, _TD_QTR)


def _active_day_frac_21d(ec: pd.Series) -> pd.Series:
    return _safe_div(_active_days(ec, _TD_MO),
                     pd.Series(_TD_MO, index=ec.index, dtype=float))


def _burst_ratio_5d_vs_252d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(ec, _TD_WK),
                     _rolling_mean(ec, _TD_YEAR))


def _burst_ratio_21d_vs_126d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_mean(ec, _TD_MO),
                     _rolling_mean(ec, _TD_2Q))


def _event_log_intensity_21d(ec: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(ec, _TD_MO))


def _event_log_intensity_252d(ec: pd.Series) -> pd.Series:
    return np.log1p(_rolling_mean(ec, _TD_YEAR))


def _event_ewm_mean_21d(ec: pd.Series) -> pd.Series:
    return _ewm_mean(ec, _TD_MO)


def _event_ewm_mean_252d(ec: pd.Series) -> pd.Series:
    return _ewm_mean(ec, _TD_YEAR)


def _event_rolling_std_63d(ec: pd.Series) -> pd.Series:
    return _rolling_std(ec, _TD_QTR)


def _event_rolling_std_252d(ec: pd.Series) -> pd.Series:
    return _rolling_std(ec, _TD_YEAR)


def _event_cv_63d(ec: pd.Series) -> pd.Series:
    return _safe_div(_rolling_std(ec, _TD_QTR),
                     _rolling_mean(ec, _TD_QTR))


# ── 2nd-derivative helpers (level-2; inlined for self-containment) ────────────

def _drv2_event_sum_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_sum_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_event_sum_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_sum_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_event_mean_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_mean_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_event_mean_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_mean_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_event_mean_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_mean_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_zscore_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_zscore_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_zscore_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_zscore_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_zscore_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_zscore_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_pct_rank_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_pct_rank_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_active_frac_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_active_frac_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_burst_21d_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_21d_vs_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_burst_5d_63d_wk(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_5d_vs_63d(ec)
    return b - b.shift(_TD_WK)


def _drv2_ewm_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_ewm_mean_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_log_intensity_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_cv_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_cv_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_sum_decline_63d_qoq(ec: pd.Series, close: pd.Series) -> pd.Series:
    b = _event_sum_during_price_decline_63d(ec, close)
    return b - b.shift(_TD_QTR)


def _drv2_event_sum_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_sum_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_event_sum_5d_wk(ec: pd.Series) -> pd.Series:
    b = _event_sum_5d(ec)
    return b - b.shift(_TD_WK)


def _drv2_event_mean_5d_wk(ec: pd.Series) -> pd.Series:
    b = _event_mean_5d(ec)
    return b - b.shift(_TD_WK)


def _drv2_event_mean_126d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_mean_126d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_event_mean_126d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_mean_126d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_zscore_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_zscore_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_zscore_21d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_zscore_21d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_pct_rank_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_pct_rank_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_pct_rank_63d_mo(ec: pd.Series) -> pd.Series:
    b = _event_pct_rank_63d(ec)
    return b - b.shift(_TD_MO)


def _drv2_active_frac_21d_mo(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_active_frac_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_burst_5d_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_5d_vs_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_burst_5d_252d_wk(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_5d_vs_252d(ec)
    return b - b.shift(_TD_WK)


def _drv2_burst_21d_126d_qoq(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_21d_vs_126d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_burst_21d_252d_mo(ec: pd.Series) -> pd.Series:
    b = _burst_ratio_21d_vs_252d(ec)
    return b - b.shift(_TD_MO)


def _drv2_log_intensity_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_log_intensity_21d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_21d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_log_intensity_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_log_intensity_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_cv_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_cv_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_cv_63d_mo(ec: pd.Series) -> pd.Series:
    b = _event_cv_63d(ec)
    return b - b.shift(_TD_MO)


def _drv2_ewm_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_ewm_mean_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_ewm_252d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_ewm_mean_252d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_ewm_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_ewm_mean_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_rolling_std_63d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_rolling_std_63d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_rolling_std_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_rolling_std_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_event_mean_21d_mo(ec: pd.Series) -> pd.Series:
    b = _event_mean_21d(ec)
    return b - b.shift(_TD_MO)


def _drv2_event_mean_21d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_mean_21d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_event_sum_21d_qoq(ec: pd.Series) -> pd.Series:
    b = _event_sum_21d(ec)
    return b - b.shift(_TD_QTR)


def _drv2_pct_rank_252d_wk(ec: pd.Series) -> pd.Series:
    b = _event_pct_rank_252d(ec)
    return b - b.shift(_TD_WK)


def _drv2_active_frac_63d_wk(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_63d(ec)
    return b - b.shift(_TD_WK)


def _drv2_zscore_63d_mo(ec: pd.Series) -> pd.Series:
    b = _event_zscore_63d(ec)
    return b - b.shift(_TD_MO)


def _drv2_zscore_252d_wk(ec: pd.Series) -> pd.Series:
    b = _event_zscore_252d(ec)
    return b - b.shift(_TD_WK)


def _drv2_active_frac_63d_2q(ec: pd.Series) -> pd.Series:
    b = _active_day_frac_63d(ec)
    return b - b.shift(_TD_2Q)


def _drv2_log_intensity_63d_mo(ec: pd.Series) -> pd.Series:
    b = _event_log_intensity_63d(ec)
    return b - b.shift(_TD_MO)


def _drv2_cv_252d_yoy(ec: pd.Series) -> pd.Series:
    b = _event_cv_252d(ec)
    return b - b.shift(_TD_YEAR)


def _drv2_cv_252d_mo(ec: pd.Series) -> pd.Series:
    b = _event_cv_252d(ec)
    return b - b.shift(_TD_MO)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def ced_drv3_001_event_sum_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the 2nd-derivative (QoQ of 63-day event sum): 3rd-order inflection."""
    base = _drv2_event_sum_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_002_event_sum_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day event sum: quarterly inflection of annual trend."""
    base = _drv2_event_sum_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_003_event_mean_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day mean event rate."""
    base = _drv2_event_mean_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_004_event_mean_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day mean event rate."""
    base = _drv2_event_mean_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_005_event_mean_21d_mo_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the MoM-diff of 21-day mean event rate."""
    base = _drv2_event_mean_21d_mo(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_006_event_zscore_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 252-day z-score: z-score inflection."""
    base = _drv2_zscore_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_007_event_zscore_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day z-score."""
    base = _drv2_zscore_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_008_event_zscore_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day z-score."""
    base = _drv2_zscore_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_009_event_pct_rank_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 252-day percentile rank."""
    base = _drv2_pct_rank_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_010_event_active_frac_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day active-day fraction."""
    base = _drv2_active_frac_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_011_event_active_frac_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day active-day fraction."""
    base = _drv2_active_frac_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_012_burst_ratio_21d_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 21d-vs-252d burst ratio."""
    base = _drv2_burst_21d_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_013_burst_ratio_5d_63d_wk_wk_diff(event_count: pd.Series) -> pd.Series:
    """Week-over-week change in the WoW-diff of 5d-vs-63d burst ratio."""
    base = _drv2_burst_5d_63d_wk(event_count)
    return base - base.shift(_TD_WK)


def ced_drv3_014_event_ewm_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day EWM mean event rate."""
    base = _drv2_ewm_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_015_event_log_intensity_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of log(1+mean_63d) Poisson intensity."""
    base = _drv2_log_intensity_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_016_event_cv_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 252-day coefficient of variation."""
    base = _drv2_cv_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_017_event_sum_decline_63d_qoq_qoq_diff(event_count: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of event sum on price-decline days."""
    base = _drv2_sum_decline_63d_qoq(event_count, close)
    return base - base.shift(_TD_QTR)


def ced_drv3_018_event_sum_63d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 63-day event sum (cross-horizon inflection)."""
    base = _drv2_event_sum_63d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_019_event_zscore_252d_qoq_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the QoQ-diff of 252-day z-score."""
    base = _drv2_zscore_252d_qoq(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_020_event_mean_63d_qoq_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the QoQ-diff of 63-day mean event rate."""
    base = _drv2_event_mean_63d_qoq(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_021_event_active_frac_63d_qoq_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the QoQ-diff of 63-day active-day fraction."""
    base = _drv2_active_frac_63d_qoq(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_022_event_sum_252d_yoy_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the YoY-diff of 252-day event sum (3rd-order annual exhaustion)."""
    base = _drv2_event_sum_252d_yoy(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_023_event_zscore_252d_yoy_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the YoY-diff of 252-day z-score (annual z-score exhaustion)."""
    base = _drv2_zscore_252d_yoy(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_024_event_pct_rank_252d_qoq_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the QoQ-diff of 252-day percentile rank."""
    base = _drv2_pct_rank_252d_qoq(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_025_event_density_exhaustion_composite(event_count: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative exhaustion score: equally weighted sum of QoQ-diff
    of three 2nd-derivative series (z-score_252d QoQ, active_frac_63d QoQ,
    log_intensity_63d QoQ).
    """
    dz2  = _drv2_zscore_252d_qoq(event_count)
    daf2 = _drv2_active_frac_63d_qoq(event_count)
    dli2 = _drv2_log_intensity_63d_qoq(event_count)
    return ((dz2  - dz2.shift(_TD_QTR)) +
            (daf2 - daf2.shift(_TD_QTR)) +
            (dli2 - dli2.shift(_TD_QTR))) / 3.0


# --- 3rd-derivative features 026-075 ---

def ced_drv3_026_event_sum_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21-day event sum."""
    base = _drv2_event_sum_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_027_event_sum_5d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 5-day event sum."""
    base = _drv2_event_sum_5d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_028_event_mean_5d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 5-day mean event rate."""
    base = _drv2_event_mean_5d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_029_event_mean_126d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 126-day mean event rate."""
    base = _drv2_event_mean_126d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_030_event_mean_126d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 126-day mean event rate."""
    base = _drv2_event_mean_126d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_031_event_zscore_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21-day z-score."""
    base = _drv2_zscore_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_032_event_zscore_21d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 21-day z-score."""
    base = _drv2_zscore_21d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_033_event_pct_rank_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day percentile rank."""
    base = _drv2_pct_rank_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_034_event_pct_rank_63d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 63-day percentile rank."""
    base = _drv2_pct_rank_63d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_035_event_active_frac_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21-day active-day fraction."""
    base = _drv2_active_frac_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_036_event_active_frac_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 252-day active-day fraction."""
    base = _drv2_active_frac_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_037_burst_ratio_5d_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 5d-vs-252d burst ratio."""
    base = _drv2_burst_5d_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_038_burst_ratio_5d_252d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 5d-vs-252d burst ratio."""
    base = _drv2_burst_5d_252d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_039_burst_ratio_21d_126d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 21d-vs-126d burst ratio."""
    base = _drv2_burst_21d_126d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_040_burst_ratio_21d_252d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21d-vs-252d burst ratio."""
    base = _drv2_burst_21d_252d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_041_log_intensity_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of log(1+mean_21d) intensity."""
    base = _drv2_log_intensity_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_042_log_intensity_21d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of log(1+mean_21d) intensity."""
    base = _drv2_log_intensity_21d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_043_log_intensity_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of log(1+mean_252d) intensity."""
    base = _drv2_log_intensity_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_044_log_intensity_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of log(1+mean_252d) intensity."""
    base = _drv2_log_intensity_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_045_event_cv_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day coefficient of variation."""
    base = _drv2_cv_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_046_event_cv_63d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 63-day coefficient of variation."""
    base = _drv2_cv_63d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_047_event_ewm_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21-day EWM mean event rate."""
    base = _drv2_ewm_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_048_event_ewm_252d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 252-day EWM mean event rate."""
    base = _drv2_ewm_252d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_049_event_ewm_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day EWM mean event rate."""
    base = _drv2_ewm_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_050_event_rolling_std_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day rolling std of event_count."""
    base = _drv2_rolling_std_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_051_event_rolling_std_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day rolling std of event_count."""
    base = _drv2_rolling_std_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_052_event_mean_21d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 21-day mean event rate."""
    base = _drv2_event_mean_21d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_053_event_mean_21d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 21-day mean event rate."""
    base = _drv2_event_mean_21d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_054_event_sum_21d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 21-day rolling event sum."""
    base = _drv2_event_sum_21d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_055_event_pct_rank_252d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 252-day percentile rank."""
    base = _drv2_pct_rank_252d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_056_event_active_frac_63d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 63-day active-day fraction."""
    base = _drv2_active_frac_63d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_057_event_zscore_63d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 63-day z-score."""
    base = _drv2_zscore_63d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_058_event_zscore_252d_wk_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the WoW-diff of 252-day z-score."""
    base = _drv2_zscore_252d_wk(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_059_event_active_frac_63d_2q_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the half-year diff of 63-day active-day fraction."""
    base = _drv2_active_frac_63d_2q(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_060_event_log_intensity_63d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of log(1+mean_63d) intensity."""
    base = _drv2_log_intensity_63d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_061_event_cv_252d_yoy_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of 252-day coefficient of variation."""
    base = _drv2_cv_252d_yoy(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_062_event_cv_252d_mo_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the MoM-diff of 252-day coefficient of variation."""
    base = _drv2_cv_252d_mo(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_063_event_sum_63d_qoq_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the QoQ-diff of 63-day event sum."""
    base = _drv2_event_sum_63d_qoq(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_064_event_sum_252d_yoy_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the YoY-diff of 252-day event sum."""
    base = _drv2_event_sum_252d_yoy(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_065_event_mean_63d_qoq_qoq_diff(event_count: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-diff of 63-day mean event rate (mirror-extend)."""
    base = _drv2_event_mean_63d_qoq(event_count)
    return base - base.shift(_TD_QTR)


def ced_drv3_066_event_zscore_252d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 252-day z-score."""
    base = _drv2_zscore_252d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_067_event_active_frac_63d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 63-day active-day fraction."""
    base = _drv2_active_frac_63d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_068_event_burst_21d_252d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 21d-vs-252d burst ratio."""
    base = _drv2_burst_21d_252d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_069_event_log_intensity_63d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of log(1+mean_63d) intensity."""
    base = _drv2_log_intensity_63d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_070_event_cv_252d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 252-day coefficient of variation."""
    base = _drv2_cv_252d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_071_event_sum_21d_mo_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the MoM-diff of 21-day event sum."""
    base = _drv2_event_sum_21d_mo(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_072_event_zscore_21d_mo_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the MoM-diff of 21-day z-score."""
    base = _drv2_zscore_21d_mo(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_073_burst_ratio_5d_63d_wk_mo_diff(event_count: pd.Series) -> pd.Series:
    """Month-over-month change in the WoW-diff of 5d-vs-63d burst ratio."""
    base = _drv2_burst_5d_63d_wk(event_count)
    return base - base.shift(_TD_MO)


def ced_drv3_074_event_pct_rank_252d_qoq_yoy_diff(event_count: pd.Series) -> pd.Series:
    """YoY change in the QoQ-diff of 252-day percentile rank."""
    base = _drv2_pct_rank_252d_qoq(event_count)
    return base - base.shift(_TD_YEAR)


def ced_drv3_075_event_density_exhaustion_composite_v2(event_count: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative exhaustion v2: equally weighted QoQ change in five
    2nd-derivative series (z21d MoM, z63d QoQ, active_frac_21d MoM,
    log_intensity_21d MoM, burst_5d_63d WoW).
    """
    d21  = _drv2_zscore_21d_mo(event_count)
    d63  = _drv2_zscore_63d_qoq(event_count)
    daf  = _drv2_active_frac_21d_mo(event_count)
    dli  = _drv2_log_intensity_21d_mo(event_count)
    dbr  = _drv2_burst_5d_63d_wk(event_count)
    return ((d21  - d21.shift(_TD_QTR)) +
            (d63  - d63.shift(_TD_QTR)) +
            (daf  - daf.shift(_TD_QTR)) +
            (dli  - dli.shift(_TD_QTR)) +
            (dbr  - dbr.shift(_TD_QTR))) / 5.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

CORPORATE_EVENT_DENSITY_REGISTRY_3RD_DERIVATIVES = {
    "ced_drv3_001_event_sum_63d_qoq_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_001_event_sum_63d_qoq_qoq_diff},
    "ced_drv3_002_event_sum_252d_yoy_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_002_event_sum_252d_yoy_qoq_diff},
    "ced_drv3_003_event_mean_63d_qoq_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_003_event_mean_63d_qoq_qoq_diff},
    "ced_drv3_004_event_mean_252d_yoy_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv3_004_event_mean_252d_yoy_qoq_diff},
    "ced_drv3_005_event_mean_21d_mo_mo_diff":            {"inputs": ["event_count"],          "func": ced_drv3_005_event_mean_21d_mo_mo_diff},
    "ced_drv3_006_event_zscore_252d_qoq_qoq_diff":       {"inputs": ["event_count"],          "func": ced_drv3_006_event_zscore_252d_qoq_qoq_diff},
    "ced_drv3_007_event_zscore_252d_yoy_qoq_diff":       {"inputs": ["event_count"],          "func": ced_drv3_007_event_zscore_252d_yoy_qoq_diff},
    "ced_drv3_008_event_zscore_63d_qoq_qoq_diff":        {"inputs": ["event_count"],          "func": ced_drv3_008_event_zscore_63d_qoq_qoq_diff},
    "ced_drv3_009_event_pct_rank_252d_qoq_qoq_diff":     {"inputs": ["event_count"],          "func": ced_drv3_009_event_pct_rank_252d_qoq_qoq_diff},
    "ced_drv3_010_event_active_frac_63d_qoq_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv3_010_event_active_frac_63d_qoq_qoq_diff},
    "ced_drv3_011_event_active_frac_252d_yoy_qoq_diff":  {"inputs": ["event_count"],          "func": ced_drv3_011_event_active_frac_252d_yoy_qoq_diff},
    "ced_drv3_012_burst_ratio_21d_252d_qoq_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv3_012_burst_ratio_21d_252d_qoq_qoq_diff},
    "ced_drv3_013_burst_ratio_5d_63d_wk_wk_diff":        {"inputs": ["event_count"],          "func": ced_drv3_013_burst_ratio_5d_63d_wk_wk_diff},
    "ced_drv3_014_event_ewm_63d_qoq_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_014_event_ewm_63d_qoq_qoq_diff},
    "ced_drv3_015_event_log_intensity_63d_qoq_qoq_diff": {"inputs": ["event_count"],          "func": ced_drv3_015_event_log_intensity_63d_qoq_qoq_diff},
    "ced_drv3_016_event_cv_252d_qoq_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_016_event_cv_252d_qoq_qoq_diff},
    "ced_drv3_017_event_sum_decline_63d_qoq_qoq_diff":   {"inputs": ["event_count", "close"], "func": ced_drv3_017_event_sum_decline_63d_qoq_qoq_diff},
    "ced_drv3_018_event_sum_63d_qoq_yoy_diff":           {"inputs": ["event_count"],          "func": ced_drv3_018_event_sum_63d_qoq_yoy_diff},
    "ced_drv3_019_event_zscore_252d_qoq_mo_diff":        {"inputs": ["event_count"],          "func": ced_drv3_019_event_zscore_252d_qoq_mo_diff},
    "ced_drv3_020_event_mean_63d_qoq_mo_diff":           {"inputs": ["event_count"],          "func": ced_drv3_020_event_mean_63d_qoq_mo_diff},
    "ced_drv3_021_event_active_frac_63d_qoq_mo_diff":    {"inputs": ["event_count"],          "func": ced_drv3_021_event_active_frac_63d_qoq_mo_diff},
    "ced_drv3_022_event_sum_252d_yoy_yoy_diff":          {"inputs": ["event_count"],          "func": ced_drv3_022_event_sum_252d_yoy_yoy_diff},
    "ced_drv3_023_event_zscore_252d_yoy_yoy_diff":       {"inputs": ["event_count"],          "func": ced_drv3_023_event_zscore_252d_yoy_yoy_diff},
    "ced_drv3_024_event_pct_rank_252d_qoq_mo_diff":      {"inputs": ["event_count"],          "func": ced_drv3_024_event_pct_rank_252d_qoq_mo_diff},
    "ced_drv3_025_event_density_exhaustion_composite":   {"inputs": ["event_count"],          "func": ced_drv3_025_event_density_exhaustion_composite},
    "ced_drv3_026_event_sum_21d_mo_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv3_026_event_sum_21d_mo_qoq_diff},
    "ced_drv3_027_event_sum_5d_wk_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv3_027_event_sum_5d_wk_qoq_diff},
    "ced_drv3_028_event_mean_5d_wk_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv3_028_event_mean_5d_wk_qoq_diff},
    "ced_drv3_029_event_mean_126d_qoq_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv3_029_event_mean_126d_qoq_qoq_diff},
    "ced_drv3_030_event_mean_126d_yoy_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv3_030_event_mean_126d_yoy_qoq_diff},
    "ced_drv3_031_event_zscore_21d_mo_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv3_031_event_zscore_21d_mo_qoq_diff},
    "ced_drv3_032_event_zscore_21d_qoq_qoq_diff":        {"inputs": ["event_count"],          "func": ced_drv3_032_event_zscore_21d_qoq_qoq_diff},
    "ced_drv3_033_event_pct_rank_63d_qoq_qoq_diff":      {"inputs": ["event_count"],          "func": ced_drv3_033_event_pct_rank_63d_qoq_qoq_diff},
    "ced_drv3_034_event_pct_rank_63d_mo_qoq_diff":       {"inputs": ["event_count"],          "func": ced_drv3_034_event_pct_rank_63d_mo_qoq_diff},
    "ced_drv3_035_event_active_frac_21d_mo_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv3_035_event_active_frac_21d_mo_qoq_diff},
    "ced_drv3_036_event_active_frac_252d_qoq_qoq_diff":  {"inputs": ["event_count"],          "func": ced_drv3_036_event_active_frac_252d_qoq_qoq_diff},
    "ced_drv3_037_burst_ratio_5d_252d_qoq_qoq_diff":     {"inputs": ["event_count"],          "func": ced_drv3_037_burst_ratio_5d_252d_qoq_qoq_diff},
    "ced_drv3_038_burst_ratio_5d_252d_wk_qoq_diff":      {"inputs": ["event_count"],          "func": ced_drv3_038_burst_ratio_5d_252d_wk_qoq_diff},
    "ced_drv3_039_burst_ratio_21d_126d_qoq_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv3_039_burst_ratio_21d_126d_qoq_qoq_diff},
    "ced_drv3_040_burst_ratio_21d_252d_mo_qoq_diff":     {"inputs": ["event_count"],          "func": ced_drv3_040_burst_ratio_21d_252d_mo_qoq_diff},
    "ced_drv3_041_log_intensity_21d_mo_qoq_diff":        {"inputs": ["event_count"],          "func": ced_drv3_041_log_intensity_21d_mo_qoq_diff},
    "ced_drv3_042_log_intensity_21d_qoq_qoq_diff":       {"inputs": ["event_count"],          "func": ced_drv3_042_log_intensity_21d_qoq_qoq_diff},
    "ced_drv3_043_log_intensity_252d_qoq_qoq_diff":      {"inputs": ["event_count"],          "func": ced_drv3_043_log_intensity_252d_qoq_qoq_diff},
    "ced_drv3_044_log_intensity_252d_yoy_qoq_diff":      {"inputs": ["event_count"],          "func": ced_drv3_044_log_intensity_252d_yoy_qoq_diff},
    "ced_drv3_045_event_cv_63d_qoq_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv3_045_event_cv_63d_qoq_qoq_diff},
    "ced_drv3_046_event_cv_63d_mo_qoq_diff":             {"inputs": ["event_count"],          "func": ced_drv3_046_event_cv_63d_mo_qoq_diff},
    "ced_drv3_047_event_ewm_21d_mo_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv3_047_event_ewm_21d_mo_qoq_diff},
    "ced_drv3_048_event_ewm_252d_qoq_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_048_event_ewm_252d_qoq_qoq_diff},
    "ced_drv3_049_event_ewm_252d_yoy_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_049_event_ewm_252d_yoy_qoq_diff},
    "ced_drv3_050_event_rolling_std_63d_qoq_qoq_diff":   {"inputs": ["event_count"],          "func": ced_drv3_050_event_rolling_std_63d_qoq_qoq_diff},
    "ced_drv3_051_event_rolling_std_252d_yoy_qoq_diff":  {"inputs": ["event_count"],          "func": ced_drv3_051_event_rolling_std_252d_yoy_qoq_diff},
    "ced_drv3_052_event_mean_21d_mo_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_052_event_mean_21d_mo_qoq_diff},
    "ced_drv3_053_event_mean_21d_qoq_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_053_event_mean_21d_qoq_qoq_diff},
    "ced_drv3_054_event_sum_21d_qoq_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_054_event_sum_21d_qoq_qoq_diff},
    "ced_drv3_055_event_pct_rank_252d_wk_qoq_diff":      {"inputs": ["event_count"],          "func": ced_drv3_055_event_pct_rank_252d_wk_qoq_diff},
    "ced_drv3_056_event_active_frac_63d_wk_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv3_056_event_active_frac_63d_wk_qoq_diff},
    "ced_drv3_057_event_zscore_63d_mo_qoq_diff":         {"inputs": ["event_count"],          "func": ced_drv3_057_event_zscore_63d_mo_qoq_diff},
    "ced_drv3_058_event_zscore_252d_wk_qoq_diff":        {"inputs": ["event_count"],          "func": ced_drv3_058_event_zscore_252d_wk_qoq_diff},
    "ced_drv3_059_event_active_frac_63d_2q_qoq_diff":    {"inputs": ["event_count"],          "func": ced_drv3_059_event_active_frac_63d_2q_qoq_diff},
    "ced_drv3_060_event_log_intensity_63d_mo_qoq_diff":  {"inputs": ["event_count"],          "func": ced_drv3_060_event_log_intensity_63d_mo_qoq_diff},
    "ced_drv3_061_event_cv_252d_yoy_qoq_diff":           {"inputs": ["event_count"],          "func": ced_drv3_061_event_cv_252d_yoy_qoq_diff},
    "ced_drv3_062_event_cv_252d_mo_qoq_diff":            {"inputs": ["event_count"],          "func": ced_drv3_062_event_cv_252d_mo_qoq_diff},
    "ced_drv3_063_event_sum_63d_qoq_mo_diff":            {"inputs": ["event_count"],          "func": ced_drv3_063_event_sum_63d_qoq_mo_diff},
    "ced_drv3_064_event_sum_252d_yoy_mo_diff":           {"inputs": ["event_count"],          "func": ced_drv3_064_event_sum_252d_yoy_mo_diff},
    "ced_drv3_065_event_mean_63d_qoq_qoq_diff":          {"inputs": ["event_count"],          "func": ced_drv3_065_event_mean_63d_qoq_qoq_diff},
    "ced_drv3_066_event_zscore_252d_qoq_yoy_diff":       {"inputs": ["event_count"],          "func": ced_drv3_066_event_zscore_252d_qoq_yoy_diff},
    "ced_drv3_067_event_active_frac_63d_qoq_yoy_diff":   {"inputs": ["event_count"],          "func": ced_drv3_067_event_active_frac_63d_qoq_yoy_diff},
    "ced_drv3_068_event_burst_21d_252d_qoq_yoy_diff":    {"inputs": ["event_count"],          "func": ced_drv3_068_event_burst_21d_252d_qoq_yoy_diff},
    "ced_drv3_069_event_log_intensity_63d_qoq_yoy_diff": {"inputs": ["event_count"],          "func": ced_drv3_069_event_log_intensity_63d_qoq_yoy_diff},
    "ced_drv3_070_event_cv_252d_qoq_yoy_diff":           {"inputs": ["event_count"],          "func": ced_drv3_070_event_cv_252d_qoq_yoy_diff},
    "ced_drv3_071_event_sum_21d_mo_mo_diff":             {"inputs": ["event_count"],          "func": ced_drv3_071_event_sum_21d_mo_mo_diff},
    "ced_drv3_072_event_zscore_21d_mo_mo_diff":          {"inputs": ["event_count"],          "func": ced_drv3_072_event_zscore_21d_mo_mo_diff},
    "ced_drv3_073_burst_ratio_5d_63d_wk_mo_diff":        {"inputs": ["event_count"],          "func": ced_drv3_073_burst_ratio_5d_63d_wk_mo_diff},
    "ced_drv3_074_event_pct_rank_252d_qoq_yoy_diff":     {"inputs": ["event_count"],          "func": ced_drv3_074_event_pct_rank_252d_qoq_yoy_diff},
    "ced_drv3_075_event_density_exhaustion_composite_v2":{"inputs": ["event_count"],          "func": ced_drv3_075_event_density_exhaustion_composite_v2},
}
