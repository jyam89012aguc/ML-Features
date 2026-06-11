"""
99_going_concern_flags — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative features (exhaustion / inflection signals)
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Flag series are forward-filled between filings; flat
stretches are correct and expected.  3rd-derivative series are sparse /
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


# ── Base + 2nd-derivative helpers (self-contained recomputes) ─────────────────
# These inline both the base and 2nd-derivative computations so this file
# needs no cross-import.

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


def _gc_ewm_63(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_QTR)


def _aw_ewm_63(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_QTR)


def _close_pct_dd_expanding(close: pd.Series) -> pd.Series:
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _flag_sum_mean_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    s = going_concern.astype(float) + audit_warning.astype(float)
    return _rolling_mean(s, _TD_QTR)


def _gc_fraction_504d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_2Y)


def _aw_fraction_504d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_2Y)


def _either_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    either = ((going_concern == 1) | (audit_warning == 1)).astype(float)
    return _rolling_mean(either, _TD_YEAR)


def _combined_flag_intensity(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    return (gc_ewm * 2.0 + aw_ewm) / 3.0


# ── 2nd-derivative helpers (used as input to 3rd derivatives) ────────────────

def _drv2_gc_fraction_63d_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_fraction_63d_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_fraction_252d_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_fraction_252d_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_streak_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_streak_length(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_streak_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_streak_length(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_ewm_63_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_ewm_63(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_ewm_63_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_ewm_63(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_close_pct_dd_expanding_qoq(close: pd.Series) -> pd.Series:
    base = _close_pct_dd_expanding(close)
    return base - base.shift(_TD_QTR)


def _drv2_combined_intensity_qoq(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    base = _combined_flag_intensity(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_either_fraction_252d_qoq(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    base = _either_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def gcf_drv3_001_gc_fraction_63d_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 63-day GC fraction) — inflection of GC acceleration."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_002_aw_fraction_63d_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_003_gc_fraction_252d_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 252-day GC fraction)."""
    drv2 = _drv2_gc_fraction_252d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_004_aw_fraction_252d_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 252-day AW fraction)."""
    drv2 = _drv2_aw_fraction_252d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_005_gc_streak_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of GC streak 2nd derivative — exhaustion of streak acceleration."""
    drv2 = _drv2_gc_streak_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_006_aw_streak_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of AW streak 2nd derivative."""
    drv2 = _drv2_aw_streak_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_007_gc_ewm_63_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of GC EWM-63) — smooth flag inflection."""
    drv2 = _drv2_gc_ewm_63_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_008_aw_ewm_63_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of AW EWM-63)."""
    drv2 = _drv2_aw_ewm_63_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_009_close_pct_dd_expanding_qoq_3rd(close: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of price-drawdown 2nd derivative — price deterioration inflection."""
    drv2 = _drv2_close_pct_dd_expanding_qoq(close)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_010_combined_intensity_qoq_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of combined flag intensity 2nd derivative."""
    drv2 = _drv2_combined_intensity_qoq(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_011_gc_fraction_63d_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of 63-day GC fraction) — cross-horizon inflection."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_012_aw_fraction_63d_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_013_gc_ewm_63_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of GC EWM-63) — annual inflection of GC momentum."""
    drv2 = _drv2_gc_ewm_63_qoq(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_014_aw_ewm_63_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of AW EWM-63)."""
    drv2 = _drv2_aw_ewm_63_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_015_either_fraction_252d_qoq_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of either-flag 252-day fraction 2nd derivative."""
    drv2 = _drv2_either_fraction_252d_qoq(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_016_gc_fraction_63d_21d_diff_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of 63-day GC fraction) — short exhaustion."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_017_aw_fraction_63d_21d_diff_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_018_gc_streak_21d_diff_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of GC streak 2nd derivative — intra-month exhaustion."""
    drv2 = _drv2_gc_streak_qoq(going_concern)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_019_aw_streak_21d_diff_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of AW streak 2nd derivative."""
    drv2 = _drv2_aw_streak_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_020_gc_ewm_63_21d_diff_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of GC EWM-63 2nd derivative."""
    drv2 = _drv2_gc_ewm_63_qoq(going_concern)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_021_close_pct_dd_21d_diff_3rd(close: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of price-drawdown 2nd derivative — short-term inflection."""
    drv2 = _drv2_close_pct_dd_expanding_qoq(close)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_022_combined_intensity_21d_diff_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of combined flag intensity 2nd derivative."""
    drv2 = _drv2_combined_intensity_qoq(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_023_gc_fraction_252d_qoq_slope_252d(going_concern: pd.Series) -> pd.Series:
    """
    Rolling 252-day OLS slope of the 2nd-derivative (QoQ diff of 252-day GC fraction).
    Captures the trend in GC acceleration — a curvature measure.
    """
    drv2 = _drv2_gc_fraction_252d_qoq(going_concern)

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

    return drv2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gcf_drv3_024_aw_fraction_252d_qoq_slope_252d(audit_warning: pd.Series) -> pd.Series:
    """
    Rolling 252-day OLS slope of the 2nd-derivative (QoQ diff of 252-day AW fraction).
    Captures the trend in AW acceleration — a curvature measure.
    """
    drv2 = _drv2_aw_fraction_252d_qoq(audit_warning)

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

    return drv2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gcf_drv3_025_flag_exhaustion_composite(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite exhaustion/inflection score: equally-weighted sum of three 3rd-derivative
    z-scores within a 252-day window:
      (1) GC fraction 63d qoq 3rd derivative
      (2) AW fraction 63d qoq 3rd derivative
      (3) price drawdown expanding 3rd derivative
    Higher absolute value signals a critical inflection in distress intensity.
    """
    drv3_gc = _drv2_gc_fraction_63d_qoq(going_concern)
    drv3_gc = drv3_gc - drv3_gc.shift(_TD_QTR)
    drv3_aw = _drv2_aw_fraction_63d_qoq(audit_warning)
    drv3_aw = drv3_aw - drv3_aw.shift(_TD_QTR)
    drv3_dd = _drv2_close_pct_dd_expanding_qoq(close)
    drv3_dd = drv3_dd - drv3_dd.shift(_TD_QTR)

    def _zscore(s):
        m  = _rolling_mean(s, _TD_YEAR)
        sd = s.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
        return _safe_div(s - m, sd)

    return (_zscore(drv3_gc) + _zscore(drv3_aw) + _zscore(drv3_dd)) / 3.0


# ── Additional helpers for 3rd-derivative features 026-075 ───────────────────

def _gc_fraction_504d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_2Y)


def _aw_fraction_504d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_2Y)


def _gc_fraction_126d(going_concern: pd.Series) -> pd.Series:
    return _rolling_mean(going_concern.astype(float), _TD_2Q)


def _aw_fraction_126d(audit_warning: pd.Series) -> pd.Series:
    return _rolling_mean(audit_warning.astype(float), _TD_2Q)


def _gc_ewm_21(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_MO)


def _aw_ewm_21(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_MO)


def _gc_ewm_252(going_concern: pd.Series) -> pd.Series:
    return _ewm_mean(going_concern.astype(float), _TD_YEAR)


def _aw_ewm_252(audit_warning: pd.Series) -> pd.Series:
    return _ewm_mean(audit_warning.astype(float), _TD_YEAR)


def _both_flag_fraction_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    both = ((going_concern == 1) & (audit_warning == 1)).astype(float)
    return _rolling_mean(both, _TD_YEAR)


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


# 2nd-derivative helpers added for new 3rd-derivative features

def _drv2_gc_fraction_504d_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_504d(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_fraction_504d_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_504d(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_streak_yoy(going_concern: pd.Series) -> pd.Series:
    base = _gc_streak_length(going_concern)
    return base - base.shift(_TD_YEAR)


def _drv2_aw_streak_yoy(audit_warning: pd.Series) -> pd.Series:
    base = _aw_streak_length(audit_warning)
    return base - base.shift(_TD_YEAR)


def _drv2_gc_ewm_21_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_ewm_21(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_ewm_21_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_ewm_21(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_fraction_63d_5d(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_WK)


def _drv2_aw_fraction_63d_5d(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_WK)


def _drv2_gc_fraction_63d_21d(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_63d(going_concern)
    return base - base.shift(_TD_MO)


def _drv2_aw_fraction_63d_21d(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_63d(audit_warning)
    return base - base.shift(_TD_MO)


def _drv2_gc_ewm_63_5d(going_concern: pd.Series) -> pd.Series:
    base = _gc_ewm_63(going_concern)
    return base - base.shift(_TD_WK)


def _drv2_aw_ewm_63_5d(audit_warning: pd.Series) -> pd.Series:
    base = _aw_ewm_63(audit_warning)
    return base - base.shift(_TD_WK)


def _drv2_either_fraction_252d_21d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    base = _either_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_MO)


def _drv2_close_pct_dd_expanding_5d(close: pd.Series) -> pd.Series:
    base = _close_pct_dd_expanding(close)
    return base - base.shift(_TD_WK)


def _drv2_gc_fraction_504d_yoy(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_504d(going_concern)
    return base - base.shift(_TD_YEAR)


def _drv2_aw_fraction_504d_yoy(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_504d(audit_warning)
    return base - base.shift(_TD_YEAR)


def _drv2_combined_intensity_yoy(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    gc_ewm = _ewm_mean(going_concern.astype(float), _TD_QTR)
    aw_ewm = _ewm_mean(audit_warning.astype(float), _TD_QTR)
    base = (gc_ewm * 2.0 + aw_ewm) / 3.0
    return base - base.shift(_TD_YEAR)


def _drv2_gc_fraction_252d_yoy(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_252d(going_concern)
    return base - base.shift(_TD_YEAR)


def _drv2_aw_fraction_252d_yoy(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_252d(audit_warning)
    return base - base.shift(_TD_YEAR)


def _drv2_gc_ewm_21_yoy(going_concern: pd.Series) -> pd.Series:
    base = _gc_ewm_21(going_concern)
    return base - base.shift(_TD_YEAR)


def _drv2_aw_ewm_21_yoy(audit_warning: pd.Series) -> pd.Series:
    base = _aw_ewm_21(audit_warning)
    return base - base.shift(_TD_YEAR)


def _drv2_gc_fraction_504d_qoq_21d(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_504d(going_concern)
    return base - base.shift(_TD_MO)


def _drv2_aw_fraction_504d_qoq_21d(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_504d(audit_warning)
    return base - base.shift(_TD_MO)


def _drv2_gc_ewm_252_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_ewm_252(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_ewm_252_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_ewm_252(audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_flag_sum_mean_63d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    s = going_concern.astype(float) + audit_warning.astype(float)
    base = _rolling_mean(s, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _drv2_both_flag_fraction_252d_qoq(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    base = _both_flag_fraction_252d(going_concern, audit_warning)
    return base - base.shift(_TD_QTR)


def _drv2_gc_fraction_126d_qoq(going_concern: pd.Series) -> pd.Series:
    base = _gc_fraction_126d(going_concern)
    return base - base.shift(_TD_QTR)


def _drv2_aw_fraction_126d_qoq(audit_warning: pd.Series) -> pd.Series:
    base = _aw_fraction_126d(audit_warning)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def gcf_drv3_026_gc_fraction_504d_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 504-day GC fraction) — 2-year inflection."""
    drv2 = _drv2_gc_fraction_504d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_027_aw_fraction_504d_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 504-day AW fraction)."""
    drv2 = _drv2_aw_fraction_504d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_028_gc_streak_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of GC streak YoY 2nd derivative — annual streak inflection."""
    drv2 = _drv2_gc_streak_yoy(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_029_aw_streak_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of AW streak YoY 2nd derivative."""
    drv2 = _drv2_aw_streak_yoy(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_030_gc_ewm_21_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of GC EWM-21) — weekly-smooth inflection."""
    drv2 = _drv2_gc_ewm_21_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_031_aw_ewm_21_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of AW EWM-21)."""
    drv2 = _drv2_aw_ewm_21_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_032_gc_fraction_63d_5d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (5-day diff of 63-day GC fraction) — very short inflection."""
    drv2 = _drv2_gc_fraction_63d_5d(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_033_aw_fraction_63d_5d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (5-day diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_5d(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_034_gc_fraction_252d_qoq_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of 252-day GC fraction)."""
    drv2 = _drv2_gc_fraction_252d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_035_aw_fraction_252d_qoq_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of 252-day AW fraction)."""
    drv2 = _drv2_aw_fraction_252d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_036_gc_fraction_63d_21d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (21-day diff of 63-day GC fraction)."""
    drv2 = _drv2_gc_fraction_63d_21d(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_037_aw_fraction_63d_21d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (21-day diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_21d(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_038_gc_ewm_63_5d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (5-day diff of GC EWM-63) — weekly smooth inflection."""
    drv2 = _drv2_gc_ewm_63_5d(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_039_aw_ewm_63_5d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (5-day diff of AW EWM-63)."""
    drv2 = _drv2_aw_ewm_63_5d(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_040_either_fraction_252d_21d_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (21-day diff of either-flag 252-day fraction)."""
    drv2 = _drv2_either_fraction_252d_21d(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_041_close_pct_dd_5d_3rd(close: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (5-day diff of price drawdown) — immediate inflection."""
    drv2 = _drv2_close_pct_dd_expanding_5d(close)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_042_gc_fraction_504d_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (YoY diff of 504-day GC fraction) — 2-year curvature."""
    drv2 = _drv2_gc_fraction_504d_yoy(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_043_aw_fraction_504d_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (YoY diff of 504-day AW fraction)."""
    drv2 = _drv2_aw_fraction_504d_yoy(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_044_combined_intensity_yoy_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of combined flag intensity YoY 2nd derivative."""
    drv2 = _drv2_combined_intensity_yoy(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_045_gc_streak_qoq_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of GC streak) — cross-horizon streak inflection."""
    drv2 = _drv2_gc_streak_qoq(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_046_aw_streak_qoq_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of AW streak)."""
    drv2 = _drv2_aw_streak_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_047_gc_fraction_63d_qoq_5d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of (QoQ diff of 63-day GC fraction) — fastest inflection."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_WK)


def gcf_drv3_048_aw_fraction_63d_qoq_5d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of (QoQ diff of 63-day AW fraction)."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_WK)


def gcf_drv3_049_gc_ewm_63_qoq_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of GC EWM-63) — annual smooth inflection."""
    drv2 = _drv2_gc_ewm_63_qoq(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_050_aw_ewm_63_qoq_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (QoQ diff of AW EWM-63)."""
    drv2 = _drv2_aw_ewm_63_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_051_gc_fraction_252d_yoy_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (YoY diff of 252-day GC fraction) — annual curvature."""
    drv2 = _drv2_gc_fraction_252d_yoy(going_concern)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_052_aw_fraction_252d_yoy_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of (YoY diff of 252-day AW fraction)."""
    drv2 = _drv2_aw_fraction_252d_yoy(audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_053_close_pct_dd_qoq_slope_252d(close: pd.Series) -> pd.Series:
    """3rd derivative: rolling 252-day OLS slope of price-drawdown QoQ 2nd derivative."""
    drv2 = _drv2_close_pct_dd_expanding_qoq(close)
    return _ols_slope(drv2, _TD_YEAR)


def gcf_drv3_054_gc_fraction_63d_qoq_slope_504d(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: rolling 504-day OLS slope of GC fraction 63d QoQ 2nd derivative."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return _ols_slope(drv2, _TD_2Y)


def gcf_drv3_055_aw_fraction_63d_qoq_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: rolling 504-day OLS slope of AW fraction 63d QoQ 2nd derivative."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return _ols_slope(drv2, _TD_2Y)


def gcf_drv3_056_either_fraction_252d_qoq_yoy_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of either-flag 252-day fraction QoQ 2nd derivative."""
    drv2 = _drv2_either_fraction_252d_qoq(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_057_gc_ewm_21_qoq_21d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of GC EWM-21) — monthly-slow inflection."""
    drv2 = _drv2_gc_ewm_21_qoq(going_concern)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_058_aw_ewm_21_qoq_21d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of AW EWM-21)."""
    drv2 = _drv2_aw_ewm_21_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_059_gc_fraction_504d_qoq_21d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of 504-day GC fraction)."""
    drv2 = _drv2_gc_fraction_504d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_060_aw_fraction_504d_qoq_21d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 21-day diff of (QoQ diff of 504-day AW fraction)."""
    drv2 = _drv2_aw_fraction_504d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_MO)


def gcf_drv3_061_gc_streak_qoq_5d_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of GC streak QoQ 2nd derivative."""
    drv2 = _drv2_gc_streak_qoq(going_concern)
    return drv2 - drv2.shift(_TD_WK)


def gcf_drv3_062_aw_streak_qoq_5d_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: 5-day diff of AW streak QoQ 2nd derivative."""
    drv2 = _drv2_aw_streak_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_WK)


def gcf_drv3_063_close_pct_dd_qoq_yoy_3rd(close: pd.Series) -> pd.Series:
    """3rd derivative: YoY diff of price-drawdown QoQ 2nd derivative."""
    drv2 = _drv2_close_pct_dd_expanding_qoq(close)
    return drv2 - drv2.shift(_TD_YEAR)


def gcf_drv3_064_both_flag_fraction_qoq_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of both-flag 252-day fraction QoQ 2nd derivative."""
    drv2 = _drv2_both_flag_fraction_252d_qoq(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_065_gc_fraction_126d_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 126-day GC fraction)."""
    drv2 = _drv2_gc_fraction_126d_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_066_aw_fraction_126d_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of 126-day AW fraction)."""
    drv2 = _drv2_aw_fraction_126d_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_067_gc_ewm_252_qoq_3rd(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of GC EWM-252) — slow-trend inflection."""
    drv2 = _drv2_gc_ewm_252_qoq(going_concern)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_068_aw_ewm_252_qoq_3rd(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of (QoQ diff of AW EWM-252)."""
    drv2 = _drv2_aw_ewm_252_qoq(audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_069_flag_sum_mean_63d_qoq_3rd(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: QoQ diff of combined flag-sum mean 63d QoQ 2nd derivative."""
    drv2 = _drv2_flag_sum_mean_63d(going_concern, audit_warning)
    return drv2 - drv2.shift(_TD_QTR)


def gcf_drv3_070_gc_fraction_63d_qoq_slope_252d(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: rolling 252-day OLS slope of GC fraction 63d QoQ 2nd derivative."""
    drv2 = _drv2_gc_fraction_63d_qoq(going_concern)
    return _ols_slope(drv2, _TD_YEAR)


def gcf_drv3_071_aw_fraction_63d_qoq_slope_252d(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: rolling 252-day OLS slope of AW fraction 63d QoQ 2nd derivative."""
    drv2 = _drv2_aw_fraction_63d_qoq(audit_warning)
    return _ols_slope(drv2, _TD_YEAR)


def gcf_drv3_072_gc_fraction_252d_qoq_slope_504d(going_concern: pd.Series) -> pd.Series:
    """3rd derivative: rolling 504-day OLS slope of GC fraction 252d QoQ 2nd derivative."""
    drv2 = _drv2_gc_fraction_252d_qoq(going_concern)
    return _ols_slope(drv2, _TD_2Y)


def gcf_drv3_073_aw_fraction_252d_qoq_slope_504d(audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: rolling 504-day OLS slope of AW fraction 252d QoQ 2nd derivative."""
    drv2 = _drv2_aw_fraction_252d_qoq(audit_warning)
    return _ols_slope(drv2, _TD_2Y)


def gcf_drv3_074_combined_intensity_qoq_slope_252d(going_concern: pd.Series, audit_warning: pd.Series) -> pd.Series:
    """3rd derivative: rolling 252-day OLS slope of combined flag intensity QoQ 2nd derivative."""
    drv2 = _drv2_combined_intensity_qoq(going_concern, audit_warning)
    return _ols_slope(drv2, _TD_YEAR)


def gcf_drv3_075_grand_exhaustion_composite(going_concern: pd.Series, audit_warning: pd.Series, close: pd.Series) -> pd.Series:
    """
    Grand exhaustion composite: z-score-weighted sum of five 3rd-derivative signals
    in a 252-day window: GC frac 63d qoq, AW frac 63d qoq, GC ewm63 qoq,
    AW ewm63 qoq, and price drawdown qoq.  Extends gcf_drv3_025 with two more components.
    """
    def _z3(drv2, lag):
        d3 = drv2 - drv2.shift(lag)
        m  = _rolling_mean(d3, _TD_YEAR)
        sd = d3.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).std()
        return _safe_div(d3 - m, sd)

    z1 = _z3(_drv2_gc_fraction_63d_qoq(going_concern), _TD_QTR)
    z2 = _z3(_drv2_aw_fraction_63d_qoq(audit_warning), _TD_QTR)
    z3 = _z3(_drv2_gc_ewm_63_qoq(going_concern), _TD_QTR)
    z4 = _z3(_drv2_aw_ewm_63_qoq(audit_warning), _TD_QTR)
    z5 = _z3(_drv2_close_pct_dd_expanding_qoq(close), _TD_QTR)
    return (z1 + z2 + z3 + z4 + z5) / 5.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

GOING_CONCERN_FLAGS_REGISTRY_3RD_DERIVATIVES = {
    "gcf_drv3_001_gc_fraction_63d_qoq_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_001_gc_fraction_63d_qoq_3rd},
    "gcf_drv3_002_aw_fraction_63d_qoq_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_002_aw_fraction_63d_qoq_3rd},
    "gcf_drv3_003_gc_fraction_252d_qoq_3rd":         {"inputs": ["going_concern"],                  "func": gcf_drv3_003_gc_fraction_252d_qoq_3rd},
    "gcf_drv3_004_aw_fraction_252d_qoq_3rd":         {"inputs": ["audit_warning"],                  "func": gcf_drv3_004_aw_fraction_252d_qoq_3rd},
    "gcf_drv3_005_gc_streak_qoq_3rd":                {"inputs": ["going_concern"],                  "func": gcf_drv3_005_gc_streak_qoq_3rd},
    "gcf_drv3_006_aw_streak_qoq_3rd":                {"inputs": ["audit_warning"],                  "func": gcf_drv3_006_aw_streak_qoq_3rd},
    "gcf_drv3_007_gc_ewm_63_qoq_3rd":                {"inputs": ["going_concern"],                  "func": gcf_drv3_007_gc_ewm_63_qoq_3rd},
    "gcf_drv3_008_aw_ewm_63_qoq_3rd":                {"inputs": ["audit_warning"],                  "func": gcf_drv3_008_aw_ewm_63_qoq_3rd},
    "gcf_drv3_009_close_pct_dd_expanding_qoq_3rd":   {"inputs": ["close"],                          "func": gcf_drv3_009_close_pct_dd_expanding_qoq_3rd},
    "gcf_drv3_010_combined_intensity_qoq_3rd":       {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_010_combined_intensity_qoq_3rd},
    "gcf_drv3_011_gc_fraction_63d_yoy_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_011_gc_fraction_63d_yoy_3rd},
    "gcf_drv3_012_aw_fraction_63d_yoy_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_012_aw_fraction_63d_yoy_3rd},
    "gcf_drv3_013_gc_ewm_63_yoy_3rd":                {"inputs": ["going_concern"],                  "func": gcf_drv3_013_gc_ewm_63_yoy_3rd},
    "gcf_drv3_014_aw_ewm_63_yoy_3rd":                {"inputs": ["audit_warning"],                  "func": gcf_drv3_014_aw_ewm_63_yoy_3rd},
    "gcf_drv3_015_either_fraction_252d_qoq_3rd":     {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_015_either_fraction_252d_qoq_3rd},
    "gcf_drv3_016_gc_fraction_63d_21d_diff_3rd":     {"inputs": ["going_concern"],                  "func": gcf_drv3_016_gc_fraction_63d_21d_diff_3rd},
    "gcf_drv3_017_aw_fraction_63d_21d_diff_3rd":     {"inputs": ["audit_warning"],                  "func": gcf_drv3_017_aw_fraction_63d_21d_diff_3rd},
    "gcf_drv3_018_gc_streak_21d_diff_3rd":           {"inputs": ["going_concern"],                  "func": gcf_drv3_018_gc_streak_21d_diff_3rd},
    "gcf_drv3_019_aw_streak_21d_diff_3rd":           {"inputs": ["audit_warning"],                  "func": gcf_drv3_019_aw_streak_21d_diff_3rd},
    "gcf_drv3_020_gc_ewm_63_21d_diff_3rd":           {"inputs": ["going_concern"],                  "func": gcf_drv3_020_gc_ewm_63_21d_diff_3rd},
    "gcf_drv3_021_close_pct_dd_21d_diff_3rd":        {"inputs": ["close"],                          "func": gcf_drv3_021_close_pct_dd_21d_diff_3rd},
    "gcf_drv3_022_combined_intensity_21d_diff_3rd":  {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_022_combined_intensity_21d_diff_3rd},
    "gcf_drv3_023_gc_fraction_252d_qoq_slope_252d":  {"inputs": ["going_concern"],                  "func": gcf_drv3_023_gc_fraction_252d_qoq_slope_252d},
    "gcf_drv3_024_aw_fraction_252d_qoq_slope_252d":  {"inputs": ["audit_warning"],                  "func": gcf_drv3_024_aw_fraction_252d_qoq_slope_252d},
    "gcf_drv3_025_flag_exhaustion_composite":        {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_drv3_025_flag_exhaustion_composite},
    "gcf_drv3_026_gc_fraction_504d_qoq_3rd":        {"inputs": ["going_concern"],                  "func": gcf_drv3_026_gc_fraction_504d_qoq_3rd},
    "gcf_drv3_027_aw_fraction_504d_qoq_3rd":        {"inputs": ["audit_warning"],                  "func": gcf_drv3_027_aw_fraction_504d_qoq_3rd},
    "gcf_drv3_028_gc_streak_yoy_3rd":               {"inputs": ["going_concern"],                  "func": gcf_drv3_028_gc_streak_yoy_3rd},
    "gcf_drv3_029_aw_streak_yoy_3rd":               {"inputs": ["audit_warning"],                  "func": gcf_drv3_029_aw_streak_yoy_3rd},
    "gcf_drv3_030_gc_ewm_21_qoq_3rd":               {"inputs": ["going_concern"],                  "func": gcf_drv3_030_gc_ewm_21_qoq_3rd},
    "gcf_drv3_031_aw_ewm_21_qoq_3rd":               {"inputs": ["audit_warning"],                  "func": gcf_drv3_031_aw_ewm_21_qoq_3rd},
    "gcf_drv3_032_gc_fraction_63d_5d_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_032_gc_fraction_63d_5d_3rd},
    "gcf_drv3_033_aw_fraction_63d_5d_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_033_aw_fraction_63d_5d_3rd},
    "gcf_drv3_034_gc_fraction_252d_qoq_yoy_3rd":    {"inputs": ["going_concern"],                  "func": gcf_drv3_034_gc_fraction_252d_qoq_yoy_3rd},
    "gcf_drv3_035_aw_fraction_252d_qoq_yoy_3rd":    {"inputs": ["audit_warning"],                  "func": gcf_drv3_035_aw_fraction_252d_qoq_yoy_3rd},
    "gcf_drv3_036_gc_fraction_63d_21d_3rd":         {"inputs": ["going_concern"],                  "func": gcf_drv3_036_gc_fraction_63d_21d_3rd},
    "gcf_drv3_037_aw_fraction_63d_21d_3rd":         {"inputs": ["audit_warning"],                  "func": gcf_drv3_037_aw_fraction_63d_21d_3rd},
    "gcf_drv3_038_gc_ewm_63_5d_3rd":               {"inputs": ["going_concern"],                  "func": gcf_drv3_038_gc_ewm_63_5d_3rd},
    "gcf_drv3_039_aw_ewm_63_5d_3rd":               {"inputs": ["audit_warning"],                  "func": gcf_drv3_039_aw_ewm_63_5d_3rd},
    "gcf_drv3_040_either_fraction_252d_21d_3rd":    {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_040_either_fraction_252d_21d_3rd},
    "gcf_drv3_041_close_pct_dd_5d_3rd":            {"inputs": ["close"],                          "func": gcf_drv3_041_close_pct_dd_5d_3rd},
    "gcf_drv3_042_gc_fraction_504d_yoy_3rd":        {"inputs": ["going_concern"],                  "func": gcf_drv3_042_gc_fraction_504d_yoy_3rd},
    "gcf_drv3_043_aw_fraction_504d_yoy_3rd":        {"inputs": ["audit_warning"],                  "func": gcf_drv3_043_aw_fraction_504d_yoy_3rd},
    "gcf_drv3_044_combined_intensity_yoy_3rd":      {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_044_combined_intensity_yoy_3rd},
    "gcf_drv3_045_gc_streak_qoq_yoy_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_045_gc_streak_qoq_yoy_3rd},
    "gcf_drv3_046_aw_streak_qoq_yoy_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_046_aw_streak_qoq_yoy_3rd},
    "gcf_drv3_047_gc_fraction_63d_qoq_5d_3rd":     {"inputs": ["going_concern"],                  "func": gcf_drv3_047_gc_fraction_63d_qoq_5d_3rd},
    "gcf_drv3_048_aw_fraction_63d_qoq_5d_3rd":     {"inputs": ["audit_warning"],                  "func": gcf_drv3_048_aw_fraction_63d_qoq_5d_3rd},
    "gcf_drv3_049_gc_ewm_63_qoq_yoy_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_049_gc_ewm_63_qoq_yoy_3rd},
    "gcf_drv3_050_aw_ewm_63_qoq_yoy_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_050_aw_ewm_63_qoq_yoy_3rd},
    "gcf_drv3_051_gc_fraction_252d_yoy_3rd":        {"inputs": ["going_concern"],                  "func": gcf_drv3_051_gc_fraction_252d_yoy_3rd},
    "gcf_drv3_052_aw_fraction_252d_yoy_3rd":        {"inputs": ["audit_warning"],                  "func": gcf_drv3_052_aw_fraction_252d_yoy_3rd},
    "gcf_drv3_053_close_pct_dd_qoq_slope_252d":    {"inputs": ["close"],                          "func": gcf_drv3_053_close_pct_dd_qoq_slope_252d},
    "gcf_drv3_054_gc_fraction_63d_qoq_slope_504d": {"inputs": ["going_concern"],                  "func": gcf_drv3_054_gc_fraction_63d_qoq_slope_504d},
    "gcf_drv3_055_aw_fraction_63d_qoq_slope_504d": {"inputs": ["audit_warning"],                  "func": gcf_drv3_055_aw_fraction_63d_qoq_slope_504d},
    "gcf_drv3_056_either_fraction_252d_qoq_yoy_3rd": {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_056_either_fraction_252d_qoq_yoy_3rd},
    "gcf_drv3_057_gc_ewm_21_qoq_21d_3rd":          {"inputs": ["going_concern"],                  "func": gcf_drv3_057_gc_ewm_21_qoq_21d_3rd},
    "gcf_drv3_058_aw_ewm_21_qoq_21d_3rd":          {"inputs": ["audit_warning"],                  "func": gcf_drv3_058_aw_ewm_21_qoq_21d_3rd},
    "gcf_drv3_059_gc_fraction_504d_qoq_21d_3rd":   {"inputs": ["going_concern"],                  "func": gcf_drv3_059_gc_fraction_504d_qoq_21d_3rd},
    "gcf_drv3_060_aw_fraction_504d_qoq_21d_3rd":   {"inputs": ["audit_warning"],                  "func": gcf_drv3_060_aw_fraction_504d_qoq_21d_3rd},
    "gcf_drv3_061_gc_streak_qoq_5d_3rd":           {"inputs": ["going_concern"],                  "func": gcf_drv3_061_gc_streak_qoq_5d_3rd},
    "gcf_drv3_062_aw_streak_qoq_5d_3rd":           {"inputs": ["audit_warning"],                  "func": gcf_drv3_062_aw_streak_qoq_5d_3rd},
    "gcf_drv3_063_close_pct_dd_qoq_yoy_3rd":       {"inputs": ["close"],                          "func": gcf_drv3_063_close_pct_dd_qoq_yoy_3rd},
    "gcf_drv3_064_both_flag_fraction_qoq_3rd":     {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_064_both_flag_fraction_qoq_3rd},
    "gcf_drv3_065_gc_fraction_126d_qoq_3rd":       {"inputs": ["going_concern"],                  "func": gcf_drv3_065_gc_fraction_126d_qoq_3rd},
    "gcf_drv3_066_aw_fraction_126d_qoq_3rd":       {"inputs": ["audit_warning"],                  "func": gcf_drv3_066_aw_fraction_126d_qoq_3rd},
    "gcf_drv3_067_gc_ewm_252_qoq_3rd":             {"inputs": ["going_concern"],                  "func": gcf_drv3_067_gc_ewm_252_qoq_3rd},
    "gcf_drv3_068_aw_ewm_252_qoq_3rd":             {"inputs": ["audit_warning"],                  "func": gcf_drv3_068_aw_ewm_252_qoq_3rd},
    "gcf_drv3_069_flag_sum_mean_63d_qoq_3rd":      {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_069_flag_sum_mean_63d_qoq_3rd},
    "gcf_drv3_070_gc_fraction_63d_qoq_slope_252d": {"inputs": ["going_concern"],                  "func": gcf_drv3_070_gc_fraction_63d_qoq_slope_252d},
    "gcf_drv3_071_aw_fraction_63d_qoq_slope_252d": {"inputs": ["audit_warning"],                  "func": gcf_drv3_071_aw_fraction_63d_qoq_slope_252d},
    "gcf_drv3_072_gc_fraction_252d_qoq_slope_504d": {"inputs": ["going_concern"],                 "func": gcf_drv3_072_gc_fraction_252d_qoq_slope_504d},
    "gcf_drv3_073_aw_fraction_252d_qoq_slope_504d": {"inputs": ["audit_warning"],                 "func": gcf_drv3_073_aw_fraction_252d_qoq_slope_504d},
    "gcf_drv3_074_combined_intensity_qoq_slope_252d": {"inputs": ["going_concern", "audit_warning"], "func": gcf_drv3_074_combined_intensity_qoq_slope_252d},
    "gcf_drv3_075_grand_exhaustion_composite":      {"inputs": ["going_concern", "audit_warning", "close"], "func": gcf_drv3_075_grand_exhaustion_composite},
}
