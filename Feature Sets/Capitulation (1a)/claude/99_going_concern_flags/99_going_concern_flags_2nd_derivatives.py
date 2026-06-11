"""
99_going_concern_flags — 2nd-Derivative Features 001-075
Domain: rate of change of base going-concern / audit-warning features (acceleration)
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Flag series are forward-filled between filings; flat
stretches are correct and expected.  2nd-derivative series are sparse /
stepwise on a daily index because the underlying flag data is binary and
changes infrequently — this is correct and expected.

    going_concern : daily binary (1.0 / 0.0) — 1 when the most recent annual
                    audit on record contains going-concern doubt language, else 0.
    audit_warning : daily binary (1.0 / 0.0) — 1 when the most recent filing
                    carries an audit qualification, material-weakness, or
                    restatement warning, else 0.
    close         : split/dividend-adjusted daily close price, USD.

Functions look strictly backward using .shift(positive), .rolling(),
.expanding(), or .ewm().  Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
This file is SELF-CONTAINED: it does not import from the base files.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _gc_fraction_63d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_QTR)


def _gc_fraction_252d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_YEAR)


def _aw_fraction_63d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_QTR)


def _aw_fraction_252d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_YEAR)


def _gc_streak_length(going_concern: pd.Series) -> pd.Series:
    arr = going_concern.values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=going_concern.index)


def _aw_streak_length(audit_warning: pd.Series) -> pd.Series:
    arr = audit_warning.values.astype(int)
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=audit_warning.index)


def _flag_sum(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    return going_concern.astype(float) + audit_warning.astype(float)


def _gc_ewm_63(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_QTR)


def _aw_ewm_63(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_QTR)


def _close_pct_dd_expanding(close: pd.Series) -> pd.Series:
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _gc_fraction_504d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_2Y)


def _aw_fraction_504d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_2Y)


def _either_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_mean(either, _TD_YEAR)


def _gc_flag_times_price_dd_252d(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_YEAR)
    dd_pct = _safe_div(close - peak, peak)
    return going_concern.astype(float) * dd_pct


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def gcf_drv2_001_gc_fraction_63d_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in the 63-day GC fraction — acceleration of short-run flag intensity."""
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_002_gc_fraction_252d_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in the 252-day GC fraction — acceleration of annual flag intensity."""
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_003_aw_fraction_63d_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the 63-day AW fraction — acceleration of short-run AW intensity."""
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_004_aw_fraction_252d_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the 252-day AW fraction — acceleration of annual AW intensity."""
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_005_gc_fraction_63d_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in the 63-day GC fraction — year-on-year shift in flag intensity."""
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_006_aw_fraction_63d_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in the 63-day AW fraction."""
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_007_gc_streak_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in GC streak length — acceleration of flagged-run duration."""
    base = _gc_streak_length(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_008_aw_streak_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in AW streak length."""
    base = _aw_streak_length(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_009_flag_sum_rolling_mean_63d_qoq_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the 63-day rolling mean of daily flag sum (combined acceleration)."""
    s = _flag_sum(going_concern, audit_warning)
    base = _rolling_mean(s, _TD_QTR)
    return base - base.shift(_TD_QTR)


def gcf_drv2_010_gc_ewm_63_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in the EWM (span=63) smoothed GC flag — smooth acceleration."""
    base = _gc_ewm_63(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_011_aw_ewm_63_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the EWM (span=63) smoothed AW flag."""
    base = _aw_ewm_63(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_012_gc_ewm_63_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in the EWM (span=63) smoothed GC flag."""
    base = _gc_ewm_63(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_013_aw_ewm_63_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in the EWM (span=63) smoothed AW flag."""
    base = _aw_ewm_63(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_014_close_pct_dd_expanding_qoq_diff(close: pd.Series) -> pd.Series:
    """QoQ change in percent drawdown from expanding price peak — price deterioration rate."""
    base = _close_pct_dd_expanding(close)
    return base - base.shift(_TD_QTR)


def gcf_drv2_015_close_pct_dd_expanding_yoy_diff(close: pd.Series) -> pd.Series:
    """YoY change in percent drawdown from expanding price peak."""
    base = _close_pct_dd_expanding(close)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_016_gc_fraction_504d_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in the 504-day GC fraction — acceleration at 2-year horizon."""
    base = _gc_fraction_504d(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_017_aw_fraction_504d_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the 504-day AW fraction."""
    base = _aw_fraction_504d(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_018_either_fraction_252d_qoq_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """QoQ change in 252-day 'either flag' fraction — combined acceleration signal."""
    base = _either_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_019_gc_flag_times_price_dd_252d_qoq_diff(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in the GC-flag-times-252d-price-drawdown interaction term."""
    base = _gc_flag_times_price_dd_252d(going_concern, close)
    return base - base.shift(_TD_QTR)


def gcf_drv2_020_gc_fraction_252d_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in 252-day GC fraction — second-order annual acceleration."""
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_021_aw_fraction_252d_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in 252-day AW fraction."""
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_022_gc_fraction_63d_slope_252d(going_concern: pd.Series) -> pd.Series:
    """
    Rolling 252-day OLS slope of the 63-day GC fraction series.
    Captures trend in GC intensity momentum.
    """
    base = _gc_fraction_63d(going_concern)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gcf_drv2_023_aw_fraction_63d_slope_252d(audit_warning: pd.Series) -> pd.Series:
    """
    Rolling 252-day OLS slope of the 63-day AW fraction series.
    Captures trend in AW intensity momentum.
    """
    base = _aw_fraction_63d(audit_warning)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return base.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gcf_drv2_024_gc_ewm_63_ewm_deviation(going_concern: pd.Series) -> pd.Series:
    """
    GC EWM (span=63) minus its own EWM (span=252) — short vs long EWM deviation.
    Measures whether current GC intensity is accelerating relative to its slow trend.
    """
    short = _ewm_mean(going_concern.astype(float), _TD_QTR)
    long_ = _ewm_mean(going_concern.astype(float), _TD_YEAR)
    base = short - long_
    return base - base.shift(_TD_QTR)


def gcf_drv2_025_combined_flag_intensity_accel(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """
    QoQ change in combined EWM intensity: (GC_ewm63 * 2 + AW_ewm63) / 3.
    Captures acceleration in weighted flag severity.
    """
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    base = (gc_ewm * 2.0 + aw_ewm) / 3.0
    return base - base.shift(_TD_QTR)


# ── Additional base helpers for 026-075 ──────────────────────────────────────

def _gc_fraction_126d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_2Q)


def _aw_fraction_126d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_2Q)


def _gc_fraction_1260d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), 1260)


def _aw_fraction_1260d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), 1260)


def _gc_ewm_21(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_MO)


def _aw_ewm_21(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_MO)


def _gc_ewm_252(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_YEAR)


def _aw_ewm_252(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_YEAR)


def _gc_ewm_126(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_2Q)


def _aw_ewm_126(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_2Q)


def _aw_flag_times_price_dd_252d(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    peak = _rolling_max(close, _TD_YEAR)
    dd_pct = _safe_div(close - peak, peak)
    return audit_warning.astype(float) * dd_pct


def _both_flag_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    return _rolling_mean(both, _TD_YEAR)


def _flag_sum_mean_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_mean(s, _TD_QTR)


def _gc_to_aw_intensity_ratio(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    gc_ewm = _gc_ewm_63(going_concern)
    aw_ewm = _aw_ewm_63(audit_warning)
    return _safe_div(gc_ewm, aw_ewm)


def _ols_slope(s: pd.Series, w: int) -> pd.Series:
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean(); ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def gcf_drv2_026_gc_fraction_504d_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in the 504-day GC fraction — 2-year horizon annual acceleration."""
    base = _gc_fraction_504d(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_027_aw_fraction_504d_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in the 504-day AW fraction."""
    base = _aw_fraction_504d(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_028_gc_streak_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in GC streak length — annual shift in flagged-run duration."""
    base = _gc_streak_length(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_029_aw_streak_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in AW streak length."""
    base = _aw_streak_length(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_030_gc_ewm_21_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=21) smoothed GC flag — short-run acceleration."""
    base = _gc_ewm_21(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_031_aw_ewm_21_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=21) smoothed AW flag."""
    base = _aw_ewm_21(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_032_gc_ewm_252_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=252) smoothed GC flag — slow-trend acceleration."""
    base = _gc_ewm_252(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_033_aw_ewm_252_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=252) smoothed AW flag."""
    base = _aw_ewm_252(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_034_gc_fraction_63d_5d_diff(going_concern: pd.Series) -> pd.Series:
    """5-day change in 63-day GC fraction — very short-run flag acceleration."""
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_WK)


def gcf_drv2_035_aw_fraction_63d_5d_diff(audit_warning: pd.Series) -> pd.Series:
    """5-day change in 63-day AW fraction."""
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_WK)


def gcf_drv2_036_gc_fraction_63d_21d_diff(going_concern: pd.Series) -> pd.Series:
    """21-day change in 63-day GC fraction — monthly acceleration."""
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_MO)


def gcf_drv2_037_aw_fraction_63d_21d_diff(audit_warning: pd.Series) -> pd.Series:
    """21-day change in 63-day AW fraction."""
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_MO)


def gcf_drv2_038_either_fraction_252d_yoy_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """YoY change in 252-day either-flag fraction — combined annual acceleration."""
    base = _either_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_039_flag_sum_mean_63d_yoy_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """YoY change in the 63-day rolling mean of daily flag sum."""
    base = _flag_sum_mean_63d(going_concern, audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_040_gc_fraction_252d_21d_diff(going_concern: pd.Series) -> pd.Series:
    """21-day change in 252-day GC fraction — monthly acceleration of annual level."""
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_MO)


def gcf_drv2_041_aw_fraction_252d_21d_diff(audit_warning: pd.Series) -> pd.Series:
    """21-day change in 252-day AW fraction."""
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_MO)


def gcf_drv2_042_close_pct_dd_expanding_21d_diff(close: pd.Series) -> pd.Series:
    """21-day change in percent drawdown from expanding peak — monthly price deterioration."""
    base = _close_pct_dd_expanding(close)
    return base - base.shift(_TD_MO)


def gcf_drv2_043_gc_ewm_63_5d_diff(going_concern: pd.Series) -> pd.Series:
    """5-day change in EWM (span=63) GC flag — weekly smooth acceleration."""
    base = _gc_ewm_63(going_concern)
    return base - base.shift(_TD_WK)


def gcf_drv2_044_aw_ewm_63_5d_diff(audit_warning: pd.Series) -> pd.Series:
    """5-day change in EWM (span=63) AW flag."""
    base = _aw_ewm_63(audit_warning)
    return base - base.shift(_TD_WK)


def gcf_drv2_045_gc_fraction_504d_slope_504d(going_concern: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 504-day GC fraction — curvature at 2-year horizon."""
    base = _gc_fraction_504d(going_concern)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_046_aw_fraction_504d_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 504-day AW fraction."""
    base = _aw_fraction_504d(audit_warning)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_047_gc_streak_slope_252d(going_concern: pd.Series) -> pd.Series:
    """Rolling 252-day OLS slope of GC streak length — trend in flagged-run duration."""
    base = _gc_streak_length(going_concern)
    return _ols_slope(base, _TD_YEAR)


def gcf_drv2_048_aw_streak_slope_252d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 252-day OLS slope of AW streak length."""
    base = _aw_streak_length(audit_warning)
    return _ols_slope(base, _TD_YEAR)


def gcf_drv2_049_gc_flag_times_dd_252d_qoq_diff(going_concern: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in GC-flag × 252d drawdown interaction term."""
    base = _gc_flag_times_price_dd_252d(going_concern, close)
    return base - base.shift(_TD_QTR)


def gcf_drv2_050_aw_flag_times_dd_252d_qoq_diff(audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in AW-flag × 252d drawdown interaction term."""
    base = _aw_flag_times_price_dd_252d(audit_warning, close)
    return base - base.shift(_TD_QTR)


def gcf_drv2_051_gc_fraction_252d_slope_504d(going_concern: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 252-day GC fraction — long-horizon trend."""
    base = _gc_fraction_252d(going_concern)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_052_aw_fraction_252d_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 252-day AW fraction."""
    base = _aw_fraction_252d(audit_warning)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_053_either_fraction_252d_21d_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """21-day change in 252-day either-flag fraction — monthly combined acceleration."""
    base = _either_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_MO)


def gcf_drv2_054_gc_ewm_126_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=126) GC flag — 2-quarter smooth acceleration."""
    base = _gc_ewm_126(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_055_aw_ewm_126_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in EWM (span=126) AW flag."""
    base = _aw_ewm_126(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_056_gc_fraction_126d_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in 126-day GC fraction — 2-quarter horizon acceleration."""
    base = _gc_fraction_126d(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_057_aw_fraction_126d_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in 126-day AW fraction."""
    base = _aw_fraction_126d(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_058_gc_fraction_126d_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in 126-day GC fraction."""
    base = _gc_fraction_126d(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_059_aw_fraction_126d_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in 126-day AW fraction."""
    base = _aw_fraction_126d(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_060_both_flag_fraction_252d_qoq_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """QoQ change in 252-day both-flag fraction — co-occurrence acceleration."""
    base = _both_flag_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_061_gc_fraction_1260d_qoq_diff(going_concern: pd.Series) -> pd.Series:
    """QoQ change in 5-year GC fraction — ultra-long-horizon acceleration."""
    base = _gc_fraction_1260d(going_concern)
    return base - base.shift(_TD_QTR)


def gcf_drv2_062_aw_fraction_1260d_qoq_diff(audit_warning: pd.Series) -> pd.Series:
    """QoQ change in 5-year AW fraction."""
    base = _aw_fraction_1260d(audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_063_gc_ewm_21_yoy_diff(going_concern: pd.Series) -> pd.Series:
    """YoY change in EWM (span=21) GC flag — annual short-smooth acceleration."""
    base = _gc_ewm_21(going_concern)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_064_aw_ewm_21_yoy_diff(audit_warning: pd.Series) -> pd.Series:
    """YoY change in EWM (span=21) AW flag."""
    base = _aw_ewm_21(audit_warning)
    return base - base.shift(_TD_YEAR)


def gcf_drv2_065_combined_flag_intensity_yoy_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """YoY change in combined EWM intensity (GC_ewm63*2 + AW_ewm63) / 3."""
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    base = (gc_ewm * 2.0 + aw_ewm) / 3.0
    return base - base.shift(_TD_YEAR)


def gcf_drv2_066_gc_fraction_63d_slope_504d(going_concern: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 63-day GC fraction — long-horizon intensity trend."""
    base = _gc_fraction_63d(going_concern)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_067_aw_fraction_63d_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of 63-day AW fraction."""
    base = _aw_fraction_63d(audit_warning)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_068_close_pct_dd_expanding_slope_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day OLS slope of percent drawdown from expanding peak."""
    base = _close_pct_dd_expanding(close)
    return _ols_slope(base, _TD_YEAR)


def gcf_drv2_069_gc_ewm_63_slope_504d(going_concern: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of GC EWM (span=63) — long smooth trend."""
    base = _gc_ewm_63(going_concern)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_070_aw_ewm_63_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """Rolling 504-day OLS slope of AW EWM (span=63)."""
    base = _aw_ewm_63(audit_warning)
    return _ols_slope(base, _TD_2Y)


def gcf_drv2_071_gc_fraction_252d_5d_diff(going_concern: pd.Series) -> pd.Series:
    """5-day change in 252-day GC fraction — immediate pulse in annual level."""
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_WK)


def gcf_drv2_072_aw_fraction_252d_5d_diff(audit_warning: pd.Series) -> pd.Series:
    """5-day change in 252-day AW fraction."""
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_WK)


def gcf_drv2_073_flag_sum_mean_63d_21d_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """21-day change in the 63-day rolling mean of daily flag sum."""
    base = _flag_sum_mean_63d(going_concern, audit_warning)
    return base - base.shift(_TD_MO)


def gcf_drv2_074_gc_aw_intensity_ratio_qoq_diff(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """QoQ change in the ratio of GC EWM-63 to AW EWM-63 (relative severity shift)."""
    base = _gc_to_aw_intensity_ratio(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


def gcf_drv2_075_combined_distress_accel_504d(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    QoQ change in the 504-day combined distress composite:
    (gc_frac_504d + aw_frac_504d + abs_dd_pct_504d) / 3.
    Captures acceleration in medium-term distress severity.
    """
    gc_frac = _rolling_mean(going_concern.astype(float), _TD_2Y)
    aw_frac = _rolling_mean(audit_warning.astype(float), _TD_2Y)
    peak = _rolling_max(close, _TD_2Y)
    dd_pct = _safe_div(close - peak, peak).clip(lower=-1.0, upper=0.0).abs()
    base = (gc_frac + aw_frac + dd_pct) / 3.0
    return base - base.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

GOING_CONCERN_FLAGS_REGISTRY_2ND_DERIVATIVES = {
    "gcf_drv2_001_gc_fraction_63d_qoq_diff":              {"inputs": ["going_concern"],                  "func": gcf_drv2_001_gc_fraction_63d_qoq_diff},
    "gcf_drv2_002_gc_fraction_252d_qoq_diff":             {"inputs": ["going_concern"],                  "func": gcf_drv2_002_gc_fraction_252d_qoq_diff},
    "gcf_drv2_003_aw_fraction_63d_qoq_diff":              {"inputs": ["audit_warning"],                  "func": gcf_drv2_003_aw_fraction_63d_qoq_diff},
    "gcf_drv2_004_aw_fraction_252d_qoq_diff":             {"inputs": ["audit_warning"],                  "func": gcf_drv2_004_aw_fraction_252d_qoq_diff},
    "gcf_drv2_005_gc_fraction_63d_yoy_diff":              {"inputs": ["going_concern"],                  "func": gcf_drv2_005_gc_fraction_63d_yoy_diff},
    "gcf_drv2_006_aw_fraction_63d_yoy_diff":              {"inputs": ["audit_warning"],                  "func": gcf_drv2_006_aw_fraction_63d_yoy_diff},
    "gcf_drv2_007_gc_streak_qoq_diff":                    {"inputs": ["going_concern"],                  "func": gcf_drv2_007_gc_streak_qoq_diff},
    "gcf_drv2_008_aw_streak_qoq_diff":                    {"inputs": ["audit_warning"],                  "func": gcf_drv2_008_aw_streak_qoq_diff},
    "gcf_drv2_009_flag_sum_rolling_mean_63d_qoq_diff":    {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_009_flag_sum_rolling_mean_63d_qoq_diff},
    "gcf_drv2_010_gc_ewm_63_qoq_diff":                    {"inputs": ["going_concern"],                  "func": gcf_drv2_010_gc_ewm_63_qoq_diff},
    "gcf_drv2_011_aw_ewm_63_qoq_diff":                    {"inputs": ["audit_warning"],                  "func": gcf_drv2_011_aw_ewm_63_qoq_diff},
    "gcf_drv2_012_gc_ewm_63_yoy_diff":                    {"inputs": ["going_concern"],                  "func": gcf_drv2_012_gc_ewm_63_yoy_diff},
    "gcf_drv2_013_aw_ewm_63_yoy_diff":                    {"inputs": ["audit_warning"],                  "func": gcf_drv2_013_aw_ewm_63_yoy_diff},
    "gcf_drv2_014_close_pct_dd_expanding_qoq_diff":       {"inputs": ["close"],                          "func": gcf_drv2_014_close_pct_dd_expanding_qoq_diff},
    "gcf_drv2_015_close_pct_dd_expanding_yoy_diff":       {"inputs": ["close"],                          "func": gcf_drv2_015_close_pct_dd_expanding_yoy_diff},
    "gcf_drv2_016_gc_fraction_504d_qoq_diff":             {"inputs": ["going_concern"],                  "func": gcf_drv2_016_gc_fraction_504d_qoq_diff},
    "gcf_drv2_017_aw_fraction_504d_qoq_diff":             {"inputs": ["audit_warning"],                  "func": gcf_drv2_017_aw_fraction_504d_qoq_diff},
    "gcf_drv2_018_either_fraction_252d_qoq_diff":         {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_018_either_fraction_252d_qoq_diff},
    "gcf_drv2_019_gc_flag_times_price_dd_252d_qoq_diff":  {"inputs": ["going_concern", "close"],         "func": gcf_drv2_019_gc_flag_times_price_dd_252d_qoq_diff},
    "gcf_drv2_020_gc_fraction_252d_yoy_diff":             {"inputs": ["going_concern"],                  "func": gcf_drv2_020_gc_fraction_252d_yoy_diff},
    "gcf_drv2_021_aw_fraction_252d_yoy_diff":             {"inputs": ["audit_warning"],                  "func": gcf_drv2_021_aw_fraction_252d_yoy_diff},
    "gcf_drv2_022_gc_fraction_63d_slope_252d":            {"inputs": ["going_concern"],                  "func": gcf_drv2_022_gc_fraction_63d_slope_252d},
    "gcf_drv2_023_aw_fraction_63d_slope_252d":            {"inputs": ["audit_warning"],                  "func": gcf_drv2_023_aw_fraction_63d_slope_252d},
    "gcf_drv2_024_gc_ewm_63_ewm_deviation":               {"inputs": ["going_concern"],                  "func": gcf_drv2_024_gc_ewm_63_ewm_deviation},
    "gcf_drv2_025_combined_flag_intensity_accel":         {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_025_combined_flag_intensity_accel},
    "gcf_drv2_026_gc_fraction_504d_yoy_diff":            {"inputs": ["going_concern"],                  "func": gcf_drv2_026_gc_fraction_504d_yoy_diff},
    "gcf_drv2_027_aw_fraction_504d_yoy_diff":            {"inputs": ["audit_warning"],                  "func": gcf_drv2_027_aw_fraction_504d_yoy_diff},
    "gcf_drv2_028_gc_streak_yoy_diff":                   {"inputs": ["going_concern"],                  "func": gcf_drv2_028_gc_streak_yoy_diff},
    "gcf_drv2_029_aw_streak_yoy_diff":                   {"inputs": ["audit_warning"],                  "func": gcf_drv2_029_aw_streak_yoy_diff},
    "gcf_drv2_030_gc_ewm_21_qoq_diff":                   {"inputs": ["going_concern"],                  "func": gcf_drv2_030_gc_ewm_21_qoq_diff},
    "gcf_drv2_031_aw_ewm_21_qoq_diff":                   {"inputs": ["audit_warning"],                  "func": gcf_drv2_031_aw_ewm_21_qoq_diff},
    "gcf_drv2_032_gc_ewm_252_qoq_diff":                  {"inputs": ["going_concern"],                  "func": gcf_drv2_032_gc_ewm_252_qoq_diff},
    "gcf_drv2_033_aw_ewm_252_qoq_diff":                  {"inputs": ["audit_warning"],                  "func": gcf_drv2_033_aw_ewm_252_qoq_diff},
    "gcf_drv2_034_gc_fraction_63d_5d_diff":              {"inputs": ["going_concern"],                  "func": gcf_drv2_034_gc_fraction_63d_5d_diff},
    "gcf_drv2_035_aw_fraction_63d_5d_diff":              {"inputs": ["audit_warning"],                  "func": gcf_drv2_035_aw_fraction_63d_5d_diff},
    "gcf_drv2_036_gc_fraction_63d_21d_diff":             {"inputs": ["going_concern"],                  "func": gcf_drv2_036_gc_fraction_63d_21d_diff},
    "gcf_drv2_037_aw_fraction_63d_21d_diff":             {"inputs": ["audit_warning"],                  "func": gcf_drv2_037_aw_fraction_63d_21d_diff},
    "gcf_drv2_038_either_fraction_252d_yoy_diff":        {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_038_either_fraction_252d_yoy_diff},
    "gcf_drv2_039_flag_sum_mean_63d_yoy_diff":           {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_039_flag_sum_mean_63d_yoy_diff},
    "gcf_drv2_040_gc_fraction_252d_21d_diff":            {"inputs": ["going_concern"],                  "func": gcf_drv2_040_gc_fraction_252d_21d_diff},
    "gcf_drv2_041_aw_fraction_252d_21d_diff":            {"inputs": ["audit_warning"],                  "func": gcf_drv2_041_aw_fraction_252d_21d_diff},
    "gcf_drv2_042_close_pct_dd_expanding_21d_diff":      {"inputs": ["close"],                          "func": gcf_drv2_042_close_pct_dd_expanding_21d_diff},
    "gcf_drv2_043_gc_ewm_63_5d_diff":                   {"inputs": ["going_concern"],                  "func": gcf_drv2_043_gc_ewm_63_5d_diff},
    "gcf_drv2_044_aw_ewm_63_5d_diff":                   {"inputs": ["audit_warning"],                  "func": gcf_drv2_044_aw_ewm_63_5d_diff},
    "gcf_drv2_045_gc_fraction_504d_slope_504d":          {"inputs": ["going_concern"],                  "func": gcf_drv2_045_gc_fraction_504d_slope_504d},
    "gcf_drv2_046_aw_fraction_504d_slope_504d":          {"inputs": ["audit_warning"],                  "func": gcf_drv2_046_aw_fraction_504d_slope_504d},
    "gcf_drv2_047_gc_streak_slope_252d":                 {"inputs": ["going_concern"],                  "func": gcf_drv2_047_gc_streak_slope_252d},
    "gcf_drv2_048_aw_streak_slope_252d":                 {"inputs": ["audit_warning"],                  "func": gcf_drv2_048_aw_streak_slope_252d},
    "gcf_drv2_049_gc_flag_times_dd_252d_qoq_diff":      {"inputs": ["going_concern", "close"],         "func": gcf_drv2_049_gc_flag_times_dd_252d_qoq_diff},
    "gcf_drv2_050_aw_flag_times_dd_252d_qoq_diff":      {"inputs": ["audit_warning", "close"],         "func": gcf_drv2_050_aw_flag_times_dd_252d_qoq_diff},
    "gcf_drv2_051_gc_fraction_252d_slope_504d":          {"inputs": ["going_concern"],                  "func": gcf_drv2_051_gc_fraction_252d_slope_504d},
    "gcf_drv2_052_aw_fraction_252d_slope_504d":          {"inputs": ["audit_warning"],                  "func": gcf_drv2_052_aw_fraction_252d_slope_504d},
    "gcf_drv2_053_either_fraction_252d_21d_diff":        {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_053_either_fraction_252d_21d_diff},
    "gcf_drv2_054_gc_ewm_126_qoq_diff":                  {"inputs": ["going_concern"],                  "func": gcf_drv2_054_gc_ewm_126_qoq_diff},
    "gcf_drv2_055_aw_ewm_126_qoq_diff":                  {"inputs": ["audit_warning"],                  "func": gcf_drv2_055_aw_ewm_126_qoq_diff},
    "gcf_drv2_056_gc_fraction_126d_qoq_diff":            {"inputs": ["going_concern"],                  "func": gcf_drv2_056_gc_fraction_126d_qoq_diff},
    "gcf_drv2_057_aw_fraction_126d_qoq_diff":            {"inputs": ["audit_warning"],                  "func": gcf_drv2_057_aw_fraction_126d_qoq_diff},
    "gcf_drv2_058_gc_fraction_126d_yoy_diff":            {"inputs": ["going_concern"],                  "func": gcf_drv2_058_gc_fraction_126d_yoy_diff},
    "gcf_drv2_059_aw_fraction_126d_yoy_diff":            {"inputs": ["audit_warning"],                  "func": gcf_drv2_059_aw_fraction_126d_yoy_diff},
    "gcf_drv2_060_both_flag_fraction_252d_qoq_diff":     {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_060_both_flag_fraction_252d_qoq_diff},
    "gcf_drv2_061_gc_fraction_1260d_qoq_diff":           {"inputs": ["going_concern"],                  "func": gcf_drv2_061_gc_fraction_1260d_qoq_diff},
    "gcf_drv2_062_aw_fraction_1260d_qoq_diff":           {"inputs": ["audit_warning"],                  "func": gcf_drv2_062_aw_fraction_1260d_qoq_diff},
    "gcf_drv2_063_gc_ewm_21_yoy_diff":                   {"inputs": ["going_concern"],                  "func": gcf_drv2_063_gc_ewm_21_yoy_diff},
    "gcf_drv2_064_aw_ewm_21_yoy_diff":                   {"inputs": ["audit_warning"],                  "func": gcf_drv2_064_aw_ewm_21_yoy_diff},
    "gcf_drv2_065_combined_flag_intensity_yoy_diff":     {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_065_combined_flag_intensity_yoy_diff},
    "gcf_drv2_066_gc_fraction_63d_slope_504d":           {"inputs": ["going_concern"],                  "func": gcf_drv2_066_gc_fraction_63d_slope_504d},
    "gcf_drv2_067_aw_fraction_63d_slope_504d":           {"inputs": ["audit_warning"],                  "func": gcf_drv2_067_aw_fraction_63d_slope_504d},
    "gcf_drv2_068_close_pct_dd_expanding_slope_252d":    {"inputs": ["close"],                          "func": gcf_drv2_068_close_pct_dd_expanding_slope_252d},
    "gcf_drv2_069_gc_ewm_63_slope_504d":                 {"inputs": ["going_concern"],                  "func": gcf_drv2_069_gc_ewm_63_slope_504d},
    "gcf_drv2_070_aw_ewm_63_slope_504d":                 {"inputs": ["audit_warning"],                  "func": gcf_drv2_070_aw_ewm_63_slope_504d},
    "gcf_drv2_071_gc_fraction_252d_5d_diff":             {"inputs": ["going_concern"],                  "func": gcf_drv2_071_gc_fraction_252d_5d_diff},
    "gcf_drv2_072_aw_fraction_252d_5d_diff":             {"inputs": ["audit_warning"],                  "func": gcf_drv2_072_aw_fraction_252d_5d_diff},
    "gcf_drv2_073_flag_sum_mean_63d_21d_diff":           {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_073_flag_sum_mean_63d_21d_diff},
    "gcf_drv2_074_gc_aw_intensity_ratio_qoq_diff":       {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv2_074_gc_aw_intensity_ratio_qoq_diff},
    "gcf_drv2_075_combined_distress_accel_504d":         {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_drv2_075_combined_distress_accel_504d},
}
