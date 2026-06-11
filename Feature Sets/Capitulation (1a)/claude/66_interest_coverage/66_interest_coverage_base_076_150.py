"""
66_interest_coverage — Base Features 076-150
Domain: interest-coverage / debt-servicing deterioration
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  All feature functions in this file look strictly backward.
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """
    Element-wise division; replaces zero (and NaN-producing) denominators with NaN.
    Interest expense can be zero (company has no debt -> coverage is undefined);
    returning NaN deliberately signals undefined, not infinite.
    """
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Coverage consecutive-decline streaks and counts ---

def icv_076_ebit_coverage_declining_streak(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Consecutive-day streak of EBIT coverage declining QoQ.
    Each step checks whether coverage is lower than one quarter ago.
    Resets to 0 when coverage stops declining.
    """
    cov     = _safe_div(ebit, intexp)
    decline = (cov < cov.shift(_TD_QTR)).fillna(False).astype(int)
    arr     = decline.values
    streak  = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ebit.index)


def icv_077_ebitda_coverage_declining_streak(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of EBITDA coverage declining QoQ."""
    cov     = _safe_div(ebitda, intexp)
    decline = (cov < cov.shift(_TD_QTR)).fillna(False).astype(int)
    arr     = decline.values
    streak  = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ebitda.index)


def icv_078_ebit_coverage_below_1_count_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days with EBIT coverage < 1.0 in the trailing 252-day window."""
    flag = (_safe_div(ebit, intexp) < 1.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icv_079_ebit_coverage_below_1_count_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days with EBIT coverage < 1.0 in the trailing 504-day window."""
    flag = (_safe_div(ebit, intexp) < 1.0).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def icv_080_ebitda_coverage_below_2_count_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days with EBITDA coverage < 2.0 in the trailing 252-day window."""
    flag = (_safe_div(ebitda, intexp) < 2.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icv_081_ebit_coverage_fraction_below_2_3y(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year (756-day) window where EBIT coverage < 2.0."""
    flag = (_safe_div(ebit, intexp) < 2.0).astype(float)
    return _rolling_mean(flag, _TD_3Y)


def icv_082_ncfo_coverage_below_1_count_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days with ncfo coverage < 1.0 in the trailing 252-day window."""
    flag = (_safe_div(ncfo, intexp) < 1.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icv_083_ncfo_coverage_below_1_fraction_3y(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fraction of trailing 756-day window where ncfo coverage < 1.0."""
    flag = (_safe_div(ncfo, intexp) < 1.0).astype(float)
    return _rolling_mean(flag, _TD_3Y)


def icv_084_ebit_coverage_declining_4q_count(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where EBIT coverage < prior-quarter coverage."""
    cov  = _safe_div(ebit, intexp)
    flag = (cov < cov.shift(_TD_QTR)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def icv_085_all_three_below_2_flag(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 when EBIT, EBITDA, AND ncfo coverages are ALL simultaneously < 2.0."""
    c_ebit   = _safe_div(ebit,   intexp)
    c_ebitda = _safe_div(ebitda, intexp)
    c_ncfo   = _safe_div(ncfo,   intexp)
    return ((c_ebit < 2.0) & (c_ebitda < 2.0) & (c_ncfo < 2.0)).astype(float)


def icv_086_ebit_coverage_turned_below_1_flag(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """1 when EBIT coverage crosses below 1.0 (was >= 1.0 a quarter ago, now < 1.0)."""
    cov      = _safe_div(ebit, intexp)
    now_low  = (cov < 1.0).astype(float)
    was_ok   = (cov.shift(_TD_QTR) >= 1.0).astype(float)
    return now_low * was_ok


def icv_087_ebitda_coverage_turned_below_1_flag(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """1 when EBITDA coverage crosses below 1.0 for the first time in a quarter."""
    cov      = _safe_div(ebitda, intexp)
    now_low  = (cov < 1.0).astype(float)
    was_ok   = (cov.shift(_TD_QTR) >= 1.0).astype(float)
    return now_low * was_ok


def icv_088_ncfo_coverage_turned_below_1_flag(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """1 when ncfo coverage crosses below 1.0 (was >= 1.0 a quarter ago)."""
    cov      = _safe_div(ncfo, intexp)
    now_low  = (cov < 1.0).astype(float)
    was_ok   = (cov.shift(_TD_QTR) >= 1.0).astype(float)
    return now_low * was_ok


def icv_089_ebit_coverage_worst_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Worst (minimum) EBIT coverage in the trailing 252-day window."""
    cov = _safe_div(ebit, intexp)
    return _rolling_min(cov, _TD_YEAR)


def icv_090_ebitda_coverage_worst_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Worst (minimum) EBITDA coverage in the trailing 504-day window."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_min(cov, _TD_2Y)


# --- Group G (091-105): Rolling average coverage levels and medians ---

def icv_091_ebit_coverage_4q_avg(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean EBIT coverage ratio."""
    cov = _safe_div(ebit, intexp)
    return _rolling_mean(cov, _TD_YEAR)


def icv_092_ebitda_coverage_4q_avg(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_mean(cov, _TD_YEAR)


def icv_093_ncfo_coverage_4q_avg(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean ncfo coverage ratio."""
    cov = _safe_div(ncfo, intexp)
    return _rolling_mean(cov, _TD_YEAR)


def icv_094_ebit_coverage_8q_avg(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean EBIT coverage ratio."""
    cov = _safe_div(ebit, intexp)
    return _rolling_mean(cov, _TD_2Y)


def icv_095_ebitda_coverage_8q_avg(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_mean(cov, _TD_2Y)


def icv_096_ebit_coverage_4q_median(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter median EBIT coverage ratio."""
    cov = _safe_div(ebit, intexp)
    return _rolling_median(cov, _TD_YEAR)


def icv_097_ebitda_coverage_4q_median(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter median EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_median(cov, _TD_YEAR)


def icv_098_ncfo_coverage_4q_median(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 4-quarter median ncfo coverage ratio."""
    cov = _safe_div(ncfo, intexp)
    return _rolling_median(cov, _TD_YEAR)


def icv_099_ebit_coverage_expanding_mean(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding mean of EBIT coverage."""
    cov = _safe_div(ebit, intexp)
    return cov.expanding(min_periods=1).mean()


def icv_100_ebitda_coverage_expanding_mean(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding mean of EBITDA coverage."""
    cov = _safe_div(ebitda, intexp)
    return cov.expanding(min_periods=1).mean()


def icv_101_ncfo_coverage_expanding_mean(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding mean of ncfo coverage."""
    cov = _safe_div(ncfo, intexp)
    return cov.expanding(min_periods=1).mean()


def icv_102_ebit_coverage_vs_expanding_mean(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage minus its all-history expanding mean."""
    cov  = _safe_div(ebit, intexp)
    mean = cov.expanding(min_periods=1).mean()
    return cov - mean


def icv_103_ebitda_coverage_vs_expanding_mean(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage minus its all-history expanding mean."""
    cov  = _safe_div(ebitda, intexp)
    mean = cov.expanding(min_periods=1).mean()
    return cov - mean


def icv_104_ebit_coverage_ewm_deviation(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage minus its 4-quarter EWM (span=252) — momentum signal."""
    cov = _safe_div(ebit, intexp)
    ewm = _ewm_mean(cov, _TD_YEAR)
    return cov - ewm


def icv_105_ebitda_coverage_ewm_deviation(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage minus its 4-quarter EWM (span=252)."""
    cov = _safe_div(ebitda, intexp)
    ewm = _ewm_mean(cov, _TD_YEAR)
    return cov - ewm


# --- Group H (106-120): intexp growth rate, effective rate, share of income ---

def icv_106_intexp_2y_pct_change(intexp: pd.Series) -> pd.Series:
    """2-year percent change in interest expense."""
    prior = intexp.shift(_TD_2Y)
    return _safe_div_abs(intexp - prior, prior)


def icv_107_intexp_3y_pct_change(intexp: pd.Series) -> pd.Series:
    """3-year percent change in interest expense."""
    prior = intexp.shift(_TD_3Y)
    return _safe_div_abs(intexp - prior, prior)


def icv_108_intexp_zscore_4q(intexp: pd.Series) -> pd.Series:
    """Z-score of interest expense within trailing 4-quarter window."""
    return _zscore_rolling(intexp, _TD_YEAR)


def icv_109_intexp_vs_4q_avg(intexp: pd.Series) -> pd.Series:
    """Interest expense minus its trailing 4-quarter mean."""
    return intexp - _rolling_mean(intexp, _TD_YEAR)


def icv_110_intexp_drawdown_from_expanding_min(intexp: pd.Series) -> pd.Series:
    """
    Interest expense minus its all-history expanding minimum.
    Rising above expanding minimum = interest burden increasing from lowest-ever level.
    """
    mn = intexp.expanding(min_periods=1).min()
    return intexp - mn


def icv_111_effective_rate_qoq_change(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in effective interest rate (intexp/debt)."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return rate - rate.shift(_TD_QTR)


def icv_112_effective_rate_2y_change(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """2-year change in effective interest rate."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return rate - rate.shift(_TD_2Y)


def icv_113_effective_rate_pct_rank_4q(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Percentile rank of effective interest rate within trailing 4-quarter window."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return _rolling_rank_pct(rate, _TD_YEAR)


def icv_114_intexp_as_pct_ebit_qoq_change(intexp: pd.Series, ebit: pd.Series) -> pd.Series:
    """QoQ change in (intexp / |ebit|) ratio."""
    ratio = _safe_div(intexp, ebit.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def icv_115_intexp_as_pct_ebit_zscore_4q(intexp: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of (intexp / |ebit|) within trailing 4-quarter window."""
    ratio = _safe_div(intexp, ebit.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


def icv_116_intexp_as_pct_ebitda_qoq_change(intexp: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in (intexp / |ebitda|) ratio."""
    ratio = _safe_div(intexp, ebitda.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def icv_117_intexp_as_pct_revenue_zscore_4q(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of (intexp / revenue) within trailing 4-quarter window."""
    ratio = _safe_div(intexp, revenue.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


def icv_118_intexp_as_pct_ncfo(intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Interest expense as a fraction of operating cash flow (>1 means ncfo cannot cover)."""
    return _safe_div(intexp, ncfo.abs().replace(0, np.nan))


def icv_119_intexp_as_pct_ncfo_qoq_change(intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ change in (intexp / |ncfo|) ratio."""
    ratio = _safe_div(intexp, ncfo.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def icv_120_intexp_as_pct_ncfo_zscore_4q(intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Z-score of (intexp / |ncfo|) within trailing 4-quarter window."""
    ratio = _safe_div(intexp, ncfo.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


# --- Group I (121-135): Coverage percentile ranks and z-scores ---

def icv_121_ebit_coverage_pct_rank_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of EBIT coverage within trailing 4-quarter window."""
    cov = _safe_div(ebit, intexp)
    return _rolling_rank_pct(cov, _TD_YEAR)


def icv_122_ebit_coverage_pct_rank_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of EBIT coverage within trailing 8-quarter window."""
    cov = _safe_div(ebit, intexp)
    return _rolling_rank_pct(cov, _TD_2Y)


def icv_123_ebit_coverage_pct_rank_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of EBIT coverage within trailing 12-quarter window."""
    cov = _safe_div(ebit, intexp)
    return _rolling_rank_pct(cov, _TD_3Y)


def icv_124_ebit_coverage_expanding_pct_rank(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of EBIT coverage."""
    cov = _safe_div(ebit, intexp)
    return cov.expanding(min_periods=2).rank(pct=True)


def icv_125_ebitda_coverage_zscore_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBITDA coverage within a trailing 8-quarter window."""
    cov = _safe_div(ebitda, intexp)
    return _zscore_rolling(cov, _TD_2Y)


def icv_126_ebitda_coverage_zscore_12q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBITDA coverage within a trailing 12-quarter window."""
    cov = _safe_div(ebitda, intexp)
    return _zscore_rolling(cov, _TD_3Y)


def icv_127_ebitda_coverage_expanding_zscore(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Expanding z-score of EBITDA coverage (how extreme vs entire history)."""
    cov = _safe_div(ebitda, intexp)
    m   = cov.expanding(min_periods=2).mean()
    sd  = cov.expanding(min_periods=2).std()
    return _safe_div(cov - m, sd)


def icv_128_ncfo_coverage_zscore_8q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of ncfo coverage within a trailing 8-quarter window."""
    cov = _safe_div(ncfo, intexp)
    return _zscore_rolling(cov, _TD_2Y)


def icv_129_opinc_coverage_zscore_8q(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of opinc coverage within a trailing 8-quarter window."""
    cov = _safe_div(opinc, intexp)
    return _zscore_rolling(cov, _TD_2Y)


def icv_130_ebit_coverage_zscore_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBIT coverage within a trailing 8-quarter window."""
    cov = _safe_div(ebit, intexp)
    return _zscore_rolling(cov, _TD_2Y)


def icv_131_ebit_coverage_zscore_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBIT coverage within a trailing 12-quarter window."""
    cov = _safe_div(ebit, intexp)
    return _zscore_rolling(cov, _TD_3Y)


def icv_132_ebit_coverage_expanding_zscore(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Expanding z-score of EBIT coverage (how extreme vs entire history)."""
    cov = _safe_div(ebit, intexp)
    m   = cov.expanding(min_periods=2).mean()
    sd  = cov.expanding(min_periods=2).std()
    return _safe_div(cov - m, sd)


def icv_133_ncfo_coverage_pct_rank_8q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of ncfo coverage within trailing 8-quarter window."""
    cov = _safe_div(ncfo, intexp)
    return _rolling_rank_pct(cov, _TD_2Y)


def icv_134_ncfo_coverage_expanding_pct_rank(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of ncfo coverage."""
    cov = _safe_div(ncfo, intexp)
    return cov.expanding(min_periods=2).rank(pct=True)


def icv_135_coverage_composite_8q(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Composite coverage severity: equally weighted 8-quarter z-scores of
    EBIT, EBITDA, and ncfo coverage ratios.
    """
    z_ebit   = _zscore_rolling(_safe_div(ebit,   intexp), _TD_2Y)
    z_ebitda = _zscore_rolling(_safe_div(ebitda, intexp), _TD_2Y)
    z_ncfo   = _zscore_rolling(_safe_div(ncfo,   intexp), _TD_2Y)
    return (z_ebit + z_ebitda + z_ncfo) / 3.0


# --- Group J (136-150): Multi-metric slopes, TTM coverage, debt-mix signals ---

def icv_136_ebit_coverage_4q_slope(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    OLS slope of EBIT coverage over trailing 4-quarter (252-day) window.
    Negative slope = coverage is trending down.
    """
    cov = _safe_div(ebit, intexp)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return cov.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def icv_137_ebitda_coverage_4q_slope(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """OLS slope of EBITDA coverage over trailing 4-quarter window."""
    cov = _safe_div(ebitda, intexp)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return cov.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def icv_138_ebit_ttm_coverage(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """TTM (trailing-12-month sum) EBIT divided by TTM intexp coverage ratio."""
    ttm_ebit   = _rolling_sum(ebit,   _TD_YEAR)
    ttm_intexp = _rolling_sum(intexp, _TD_YEAR)
    return _safe_div(ttm_ebit, ttm_intexp)


def icv_139_ebitda_ttm_coverage(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """TTM EBITDA divided by TTM intexp."""
    ttm_ebitda = _rolling_sum(ebitda, _TD_YEAR)
    ttm_intexp = _rolling_sum(intexp, _TD_YEAR)
    return _safe_div(ttm_ebitda, ttm_intexp)


def icv_140_ncfo_ttm_coverage(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """TTM ncfo divided by TTM intexp."""
    ttm_ncfo   = _rolling_sum(ncfo,   _TD_YEAR)
    ttm_intexp = _rolling_sum(intexp, _TD_YEAR)
    return _safe_div(ttm_ncfo, ttm_intexp)


def icv_141_ebit_ttm_coverage_pct_rank_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Percentile rank of TTM EBIT coverage within the trailing 8-quarter (504-day) window.
    Low rank = TTM coverage near its worst level over 2 years.
    """
    cov = _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return _rolling_rank_pct(cov, _TD_2Y)


def icv_142_ebitda_ttm_coverage_qoq_change(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in TTM EBITDA coverage."""
    cov = _safe_div(_rolling_sum(ebitda, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return cov - cov.shift(_TD_QTR)


def icv_143_ebit_ttm_coverage_below_1(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if TTM EBIT coverage < 1.0."""
    cov = _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return (cov < 1.0).astype(float)


def icv_144_short_debt_share_of_total(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Short-term debt as a fraction of total debt.
    Higher short-term share = refinancing risk near-term (debt-servicing pressure).
    """
    return _safe_div(debtc.abs(), debt.abs().replace(0, np.nan))


def icv_145_short_debt_share_yoy_change(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """YoY change in short-term-debt / total-debt share."""
    ratio = _safe_div(debtc.abs(), debt.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def icv_146_intexp_per_debt_unit_qoq_pct(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ percent change in effective interest rate (intexp/debt) -- rate acceleration."""
    rate  = _safe_div(intexp, debt.abs().replace(0, np.nan))
    prior = rate.shift(_TD_QTR)
    return _safe_div_abs(rate - prior, prior)


def icv_147_ncfo_minus_intexp_level(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    ncfo minus intexp in absolute dollar terms.
    Negative = operating cash flow is insufficient to cover interest expense.
    """
    return ncfo - intexp


def icv_148_ebit_minus_intexp_level(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT minus intexp — absolute gap between earnings power and interest burden."""
    return ebit - intexp


def icv_149_ebitda_minus_intexp_level(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA minus intexp — absolute dollar interest coverage surplus/deficit."""
    return ebitda - intexp


def icv_150_coverage_deterioration_composite_yoy(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Composite YoY deterioration: equally weighted average of YoY changes in
    EBIT, EBITDA, and ncfo coverage ratios.  More negative = broader deterioration.
    """
    c_ebit   = _safe_div(ebit,   intexp)
    c_ebitda = _safe_div(ebitda, intexp)
    c_ncfo   = _safe_div(ncfo,   intexp)
    d_ebit   = c_ebit   - c_ebit.shift(_TD_YEAR)
    d_ebitda = c_ebitda - c_ebitda.shift(_TD_YEAR)
    d_ncfo   = c_ncfo   - c_ncfo.shift(_TD_YEAR)
    return (d_ebit + d_ebitda + d_ncfo) / 3.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INTEREST_COVERAGE_REGISTRY_076_150 = {
    "icv_076_ebit_coverage_declining_streak":          {"inputs": ["ebit", "intexp"],                      "func": icv_076_ebit_coverage_declining_streak},
    "icv_077_ebitda_coverage_declining_streak":        {"inputs": ["ebitda", "intexp"],                    "func": icv_077_ebitda_coverage_declining_streak},
    "icv_078_ebit_coverage_below_1_count_4q":          {"inputs": ["ebit", "intexp"],                      "func": icv_078_ebit_coverage_below_1_count_4q},
    "icv_079_ebit_coverage_below_1_count_8q":          {"inputs": ["ebit", "intexp"],                      "func": icv_079_ebit_coverage_below_1_count_8q},
    "icv_080_ebitda_coverage_below_2_count_4q":        {"inputs": ["ebitda", "intexp"],                    "func": icv_080_ebitda_coverage_below_2_count_4q},
    "icv_081_ebit_coverage_fraction_below_2_3y":       {"inputs": ["ebit", "intexp"],                      "func": icv_081_ebit_coverage_fraction_below_2_3y},
    "icv_082_ncfo_coverage_below_1_count_4q":          {"inputs": ["ncfo", "intexp"],                      "func": icv_082_ncfo_coverage_below_1_count_4q},
    "icv_083_ncfo_coverage_below_1_fraction_3y":       {"inputs": ["ncfo", "intexp"],                      "func": icv_083_ncfo_coverage_below_1_fraction_3y},
    "icv_084_ebit_coverage_declining_4q_count":        {"inputs": ["ebit", "intexp"],                      "func": icv_084_ebit_coverage_declining_4q_count},
    "icv_085_all_three_below_2_flag":                  {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],    "func": icv_085_all_three_below_2_flag},
    "icv_086_ebit_coverage_turned_below_1_flag":       {"inputs": ["ebit", "intexp"],                      "func": icv_086_ebit_coverage_turned_below_1_flag},
    "icv_087_ebitda_coverage_turned_below_1_flag":     {"inputs": ["ebitda", "intexp"],                    "func": icv_087_ebitda_coverage_turned_below_1_flag},
    "icv_088_ncfo_coverage_turned_below_1_flag":       {"inputs": ["ncfo", "intexp"],                      "func": icv_088_ncfo_coverage_turned_below_1_flag},
    "icv_089_ebit_coverage_worst_4q":                  {"inputs": ["ebit", "intexp"],                      "func": icv_089_ebit_coverage_worst_4q},
    "icv_090_ebitda_coverage_worst_8q":                {"inputs": ["ebitda", "intexp"],                    "func": icv_090_ebitda_coverage_worst_8q},
    "icv_091_ebit_coverage_4q_avg":                    {"inputs": ["ebit", "intexp"],                      "func": icv_091_ebit_coverage_4q_avg},
    "icv_092_ebitda_coverage_4q_avg":                  {"inputs": ["ebitda", "intexp"],                    "func": icv_092_ebitda_coverage_4q_avg},
    "icv_093_ncfo_coverage_4q_avg":                    {"inputs": ["ncfo", "intexp"],                      "func": icv_093_ncfo_coverage_4q_avg},
    "icv_094_ebit_coverage_8q_avg":                    {"inputs": ["ebit", "intexp"],                      "func": icv_094_ebit_coverage_8q_avg},
    "icv_095_ebitda_coverage_8q_avg":                  {"inputs": ["ebitda", "intexp"],                    "func": icv_095_ebitda_coverage_8q_avg},
    "icv_096_ebit_coverage_4q_median":                 {"inputs": ["ebit", "intexp"],                      "func": icv_096_ebit_coverage_4q_median},
    "icv_097_ebitda_coverage_4q_median":               {"inputs": ["ebitda", "intexp"],                    "func": icv_097_ebitda_coverage_4q_median},
    "icv_098_ncfo_coverage_4q_median":                 {"inputs": ["ncfo", "intexp"],                      "func": icv_098_ncfo_coverage_4q_median},
    "icv_099_ebit_coverage_expanding_mean":            {"inputs": ["ebit", "intexp"],                      "func": icv_099_ebit_coverage_expanding_mean},
    "icv_100_ebitda_coverage_expanding_mean":          {"inputs": ["ebitda", "intexp"],                    "func": icv_100_ebitda_coverage_expanding_mean},
    "icv_101_ncfo_coverage_expanding_mean":            {"inputs": ["ncfo", "intexp"],                      "func": icv_101_ncfo_coverage_expanding_mean},
    "icv_102_ebit_coverage_vs_expanding_mean":         {"inputs": ["ebit", "intexp"],                      "func": icv_102_ebit_coverage_vs_expanding_mean},
    "icv_103_ebitda_coverage_vs_expanding_mean":       {"inputs": ["ebitda", "intexp"],                    "func": icv_103_ebitda_coverage_vs_expanding_mean},
    "icv_104_ebit_coverage_ewm_deviation":             {"inputs": ["ebit", "intexp"],                      "func": icv_104_ebit_coverage_ewm_deviation},
    "icv_105_ebitda_coverage_ewm_deviation":           {"inputs": ["ebitda", "intexp"],                    "func": icv_105_ebitda_coverage_ewm_deviation},
    "icv_106_intexp_2y_pct_change":                    {"inputs": ["intexp"],                              "func": icv_106_intexp_2y_pct_change},
    "icv_107_intexp_3y_pct_change":                    {"inputs": ["intexp"],                              "func": icv_107_intexp_3y_pct_change},
    "icv_108_intexp_zscore_4q":                        {"inputs": ["intexp"],                              "func": icv_108_intexp_zscore_4q},
    "icv_109_intexp_vs_4q_avg":                        {"inputs": ["intexp"],                              "func": icv_109_intexp_vs_4q_avg},
    "icv_110_intexp_drawdown_from_expanding_min":      {"inputs": ["intexp"],                              "func": icv_110_intexp_drawdown_from_expanding_min},
    "icv_111_effective_rate_qoq_change":               {"inputs": ["intexp", "debt"],                      "func": icv_111_effective_rate_qoq_change},
    "icv_112_effective_rate_2y_change":                {"inputs": ["intexp", "debt"],                      "func": icv_112_effective_rate_2y_change},
    "icv_113_effective_rate_pct_rank_4q":              {"inputs": ["intexp", "debt"],                      "func": icv_113_effective_rate_pct_rank_4q},
    "icv_114_intexp_as_pct_ebit_qoq_change":           {"inputs": ["intexp", "ebit"],                      "func": icv_114_intexp_as_pct_ebit_qoq_change},
    "icv_115_intexp_as_pct_ebit_zscore_4q":            {"inputs": ["intexp", "ebit"],                      "func": icv_115_intexp_as_pct_ebit_zscore_4q},
    "icv_116_intexp_as_pct_ebitda_qoq_change":         {"inputs": ["intexp", "ebitda"],                    "func": icv_116_intexp_as_pct_ebitda_qoq_change},
    "icv_117_intexp_as_pct_revenue_zscore_4q":         {"inputs": ["intexp", "revenue"],                   "func": icv_117_intexp_as_pct_revenue_zscore_4q},
    "icv_118_intexp_as_pct_ncfo":                      {"inputs": ["intexp", "ncfo"],                      "func": icv_118_intexp_as_pct_ncfo},
    "icv_119_intexp_as_pct_ncfo_qoq_change":           {"inputs": ["intexp", "ncfo"],                      "func": icv_119_intexp_as_pct_ncfo_qoq_change},
    "icv_120_intexp_as_pct_ncfo_zscore_4q":            {"inputs": ["intexp", "ncfo"],                      "func": icv_120_intexp_as_pct_ncfo_zscore_4q},
    "icv_121_ebit_coverage_pct_rank_4q":               {"inputs": ["ebit", "intexp"],                      "func": icv_121_ebit_coverage_pct_rank_4q},
    "icv_122_ebit_coverage_pct_rank_8q":               {"inputs": ["ebit", "intexp"],                      "func": icv_122_ebit_coverage_pct_rank_8q},
    "icv_123_ebit_coverage_pct_rank_12q":              {"inputs": ["ebit", "intexp"],                      "func": icv_123_ebit_coverage_pct_rank_12q},
    "icv_124_ebit_coverage_expanding_pct_rank":        {"inputs": ["ebit", "intexp"],                      "func": icv_124_ebit_coverage_expanding_pct_rank},
    "icv_125_ebitda_coverage_zscore_8q":               {"inputs": ["ebitda", "intexp"],                    "func": icv_125_ebitda_coverage_zscore_8q},
    "icv_126_ebitda_coverage_zscore_12q":              {"inputs": ["ebitda", "intexp"],                    "func": icv_126_ebitda_coverage_zscore_12q},
    "icv_127_ebitda_coverage_expanding_zscore":        {"inputs": ["ebitda", "intexp"],                    "func": icv_127_ebitda_coverage_expanding_zscore},
    "icv_128_ncfo_coverage_zscore_8q":                 {"inputs": ["ncfo", "intexp"],                      "func": icv_128_ncfo_coverage_zscore_8q},
    "icv_129_opinc_coverage_zscore_8q":                {"inputs": ["opinc", "intexp"],                     "func": icv_129_opinc_coverage_zscore_8q},
    "icv_130_ebit_coverage_zscore_8q":                 {"inputs": ["ebit", "intexp"],                      "func": icv_130_ebit_coverage_zscore_8q},
    "icv_131_ebit_coverage_zscore_12q":                {"inputs": ["ebit", "intexp"],                      "func": icv_131_ebit_coverage_zscore_12q},
    "icv_132_ebit_coverage_expanding_zscore":          {"inputs": ["ebit", "intexp"],                      "func": icv_132_ebit_coverage_expanding_zscore},
    "icv_133_ncfo_coverage_pct_rank_8q":               {"inputs": ["ncfo", "intexp"],                      "func": icv_133_ncfo_coverage_pct_rank_8q},
    "icv_134_ncfo_coverage_expanding_pct_rank":        {"inputs": ["ncfo", "intexp"],                      "func": icv_134_ncfo_coverage_expanding_pct_rank},
    "icv_135_coverage_composite_8q":                   {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],    "func": icv_135_coverage_composite_8q},
    "icv_136_ebit_coverage_4q_slope":                  {"inputs": ["ebit", "intexp"],                      "func": icv_136_ebit_coverage_4q_slope},
    "icv_137_ebitda_coverage_4q_slope":                {"inputs": ["ebitda", "intexp"],                    "func": icv_137_ebitda_coverage_4q_slope},
    "icv_138_ebit_ttm_coverage":                       {"inputs": ["ebit", "intexp"],                      "func": icv_138_ebit_ttm_coverage},
    "icv_139_ebitda_ttm_coverage":                     {"inputs": ["ebitda", "intexp"],                    "func": icv_139_ebitda_ttm_coverage},
    "icv_140_ncfo_ttm_coverage":                       {"inputs": ["ncfo", "intexp"],                      "func": icv_140_ncfo_ttm_coverage},
    "icv_141_ebit_ttm_coverage_pct_rank_8q":           {"inputs": ["ebit", "intexp"],                      "func": icv_141_ebit_ttm_coverage_pct_rank_8q},
    "icv_142_ebitda_ttm_coverage_qoq_change":          {"inputs": ["ebitda", "intexp"],                    "func": icv_142_ebitda_ttm_coverage_qoq_change},
    "icv_143_ebit_ttm_coverage_below_1":               {"inputs": ["ebit", "intexp"],                      "func": icv_143_ebit_ttm_coverage_below_1},
    "icv_144_short_debt_share_of_total":               {"inputs": ["debtc", "debt"],                       "func": icv_144_short_debt_share_of_total},
    "icv_145_short_debt_share_yoy_change":             {"inputs": ["debtc", "debt"],                       "func": icv_145_short_debt_share_yoy_change},
    "icv_146_intexp_per_debt_unit_qoq_pct":            {"inputs": ["intexp", "debt"],                      "func": icv_146_intexp_per_debt_unit_qoq_pct},
    "icv_147_ncfo_minus_intexp_level":                 {"inputs": ["ncfo", "intexp"],                      "func": icv_147_ncfo_minus_intexp_level},
    "icv_148_ebit_minus_intexp_level":                 {"inputs": ["ebit", "intexp"],                      "func": icv_148_ebit_minus_intexp_level},
    "icv_149_ebitda_minus_intexp_level":               {"inputs": ["ebitda", "intexp"],                    "func": icv_149_ebitda_minus_intexp_level},
    "icv_150_coverage_deterioration_composite_yoy":    {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],    "func": icv_150_coverage_deterioration_composite_yoy},
}
