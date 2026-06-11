"""
66_interest_coverage — 2nd-Derivative Features 001-025
Domain: rate of change of base interest-coverage features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 2nd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
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
_TD_QTR   = 63
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
    """Divide by absolute value of den."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


# ── Base feature helpers (self-contained recomputes) ─────────────────────────
# These inline the relevant base computations so this file needs no cross-import.

def _ebit_cov(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebit, intexp)


def _ebitda_cov(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebitda, intexp)


def _ncfo_cov(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ncfo, intexp)


def _opinc_cov(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(opinc, intexp)


def _ebit_cov_qoq(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebit_cov(ebit, intexp)
    return cov - cov.shift(_TD_QTR)


def _ebitda_cov_qoq(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebitda_cov(ebitda, intexp)
    return cov - cov.shift(_TD_QTR)


def _ebit_cov_yoy(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebit_cov(ebit, intexp)
    return cov - cov.shift(_TD_YEAR)


def _ebitda_cov_yoy(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebitda_cov(ebitda, intexp)
    return cov - cov.shift(_TD_YEAR)


def _effective_rate(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    return _safe_div(intexp, debt.abs().replace(0, np.nan))


def _ebit_cov_drawdown_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov  = _ebit_cov(ebit, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def _ebitda_cov_drawdown_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov  = _ebitda_cov(ebitda, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def _ncfo_cov_drawdown_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    cov  = _ncfo_cov(ncfo, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def _ebit_zscore_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebit_cov(ebit, intexp)
    m   = _rolling_mean(cov, _TD_YEAR)
    sd  = _rolling_std(cov, _TD_YEAR)
    return _safe_div(cov - m, sd)


def _ebitda_zscore_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebitda_cov(ebitda, intexp)
    m   = _rolling_mean(cov, _TD_YEAR)
    sd  = _rolling_std(cov, _TD_YEAR)
    return _safe_div(cov - m, sd)


def _ncfo_zscore_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ncfo_cov(ncfo, intexp)
    m   = _rolling_mean(cov, _TD_YEAR)
    sd  = _rolling_std(cov, _TD_YEAR)
    return _safe_div(cov - m, sd)


def _intexp_as_pct_revenue(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(intexp, revenue.abs().replace(0, np.nan))


def _ebit_ttm_cov(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def icv_drv2_001_ebit_cov_qoq_diff_of_qoq(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ EBIT coverage change (acceleration of coverage decline)."""
    base = _ebit_cov_qoq(ebit, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_002_ebit_cov_yoy_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the YoY EBIT coverage change (how fast the annual trend shifts)."""
    base = _ebit_cov_yoy(ebit, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_003_ebitda_cov_qoq_diff_of_qoq(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ EBITDA coverage change."""
    base = _ebitda_cov_qoq(ebitda, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_004_ebitda_cov_yoy_qoq_diff(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the YoY EBITDA coverage change."""
    base = _ebitda_cov_yoy(ebitda, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_005_ebit_zscore_4q_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of EBIT coverage."""
    base = _ebit_zscore_4q(ebit, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_006_ebitda_zscore_4q_qoq_diff(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of EBITDA coverage."""
    base = _ebitda_zscore_4q(ebitda, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_007_ncfo_zscore_4q_qoq_diff(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter z-score of ncfo coverage."""
    base = _ncfo_zscore_4q(ncfo, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_008_ebit_cov_drawdown_4q_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter-peak drawdown of EBIT coverage."""
    base = _ebit_cov_drawdown_4q(ebit, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_009_ebitda_cov_drawdown_4q_qoq_diff(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter-peak drawdown of EBITDA coverage."""
    base = _ebitda_cov_drawdown_4q(ebitda, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_010_ncfo_cov_drawdown_4q_qoq_diff(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter-peak drawdown of ncfo coverage."""
    base = _ncfo_cov_drawdown_4q(ncfo, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_011_ebit_cov_drawdown_4q_yoy_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter-peak drawdown of EBIT coverage."""
    base = _ebit_cov_drawdown_4q(ebit, intexp)
    return base - base.shift(_TD_YEAR)


def icv_drv2_012_effective_rate_qoq_diff_of_qoq(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in the QoQ effective interest rate change (rate acceleration)."""
    rate = _effective_rate(intexp, debt)
    qoq  = rate - rate.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def icv_drv2_013_intexp_pct_revenue_qoq_diff(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in (intexp / revenue) ratio."""
    base = _intexp_as_pct_revenue(intexp, revenue)
    return base - base.shift(_TD_QTR)


def icv_drv2_014_intexp_pct_revenue_yoy_diff(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in (intexp / revenue) ratio."""
    base = _intexp_as_pct_revenue(intexp, revenue)
    return base - base.shift(_TD_YEAR)


def icv_drv2_015_ebit_ttm_cov_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the TTM EBIT coverage ratio."""
    base = _ebit_ttm_cov(ebit, intexp)
    return base - base.shift(_TD_QTR)


def icv_drv2_016_ebit_ttm_cov_yoy_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in the TTM EBIT coverage ratio."""
    base = _ebit_ttm_cov(ebit, intexp)
    return base - base.shift(_TD_YEAR)


def icv_drv2_017_ebit_cov_qoq_ewm_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Current QoQ EBIT coverage change minus its 4-quarter EWM.
    Measures whether this quarter's decline is worse than its recent trend.
    """
    base = _ebit_cov_qoq(ebit, intexp)
    ewm  = base.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    return base - ewm


def icv_drv2_018_ebit_cov_yoy_pct_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent change of EBIT coverage."""
    cov   = _ebit_cov(ebit, intexp)
    prior = cov.shift(_TD_YEAR)
    base  = _safe_div_abs(cov - prior, prior)
    return base - base.shift(_TD_QTR)


def icv_drv2_019_ebitda_cov_yoy_pct_qoq_diff(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the YoY percent change of EBITDA coverage."""
    cov   = _ebitda_cov(ebitda, intexp)
    prior = cov.shift(_TD_YEAR)
    base  = _safe_div_abs(cov - prior, prior)
    return base - base.shift(_TD_QTR)


def icv_drv2_020_ebit_zscore_4q_yoy_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter z-score of EBIT coverage."""
    base = _ebit_zscore_4q(ebit, intexp)
    return base - base.shift(_TD_YEAR)


def icv_drv2_021_ncfo_cov_qoq_diff_of_qoq(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ ncfo coverage change (ncfo coverage acceleration)."""
    cov  = _ncfo_cov(ncfo, intexp)
    qoq  = cov - cov.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def icv_drv2_022_ebit_cov_4q_slope_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the rolling 4-quarter OLS slope of EBIT coverage.
    Captures whether the downtrend in coverage is steepening.
    """
    cov = _ebit_cov(ebit, intexp)

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

    slope = cov.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def icv_drv2_023_ebit_minus_intexp_qoq_diff(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in (EBIT - intexp) absolute gap."""
    base = ebit - intexp
    return base - base.shift(_TD_QTR)


def icv_drv2_024_ebitda_minus_intexp_qoq_diff(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in (EBITDA - intexp) absolute gap."""
    base = ebitda - intexp
    return base - base.shift(_TD_QTR)


def icv_drv2_025_composite_cov_zscore_qoq_diff(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in composite coverage z-score (average of EBIT, EBITDA, ncfo 4Q z-scores).
    Measures whether overall coverage distress is worsening quarter-over-quarter.
    """
    composite = (
        _ebit_zscore_4q(ebit, intexp)
        + _ebitda_zscore_4q(ebitda, intexp)
        + _ncfo_zscore_4q(ncfo, intexp)
    ) / 3.0
    return composite - composite.shift(_TD_QTR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INTEREST_COVERAGE_REGISTRY_2ND_DERIVATIVES = {
    "icv_drv2_001_ebit_cov_qoq_diff_of_qoq":      {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_001_ebit_cov_qoq_diff_of_qoq},
    "icv_drv2_002_ebit_cov_yoy_qoq_diff":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_002_ebit_cov_yoy_qoq_diff},
    "icv_drv2_003_ebitda_cov_qoq_diff_of_qoq":    {"inputs": ["ebitda", "intexp"],                 "func": icv_drv2_003_ebitda_cov_qoq_diff_of_qoq},
    "icv_drv2_004_ebitda_cov_yoy_qoq_diff":        {"inputs": ["ebitda", "intexp"],                 "func": icv_drv2_004_ebitda_cov_yoy_qoq_diff},
    "icv_drv2_005_ebit_zscore_4q_qoq_diff":        {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_005_ebit_zscore_4q_qoq_diff},
    "icv_drv2_006_ebitda_zscore_4q_qoq_diff":      {"inputs": ["ebitda", "intexp"],                 "func": icv_drv2_006_ebitda_zscore_4q_qoq_diff},
    "icv_drv2_007_ncfo_zscore_4q_qoq_diff":        {"inputs": ["ncfo", "intexp"],                   "func": icv_drv2_007_ncfo_zscore_4q_qoq_diff},
    "icv_drv2_008_ebit_cov_drawdown_4q_qoq_diff":  {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_008_ebit_cov_drawdown_4q_qoq_diff},
    "icv_drv2_009_ebitda_cov_drawdown_4q_qoq_diff": {"inputs": ["ebitda", "intexp"],                "func": icv_drv2_009_ebitda_cov_drawdown_4q_qoq_diff},
    "icv_drv2_010_ncfo_cov_drawdown_4q_qoq_diff":  {"inputs": ["ncfo", "intexp"],                   "func": icv_drv2_010_ncfo_cov_drawdown_4q_qoq_diff},
    "icv_drv2_011_ebit_cov_drawdown_4q_yoy_diff":  {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_011_ebit_cov_drawdown_4q_yoy_diff},
    "icv_drv2_012_effective_rate_qoq_diff_of_qoq": {"inputs": ["intexp", "debt"],                   "func": icv_drv2_012_effective_rate_qoq_diff_of_qoq},
    "icv_drv2_013_intexp_pct_revenue_qoq_diff":    {"inputs": ["intexp", "revenue"],                "func": icv_drv2_013_intexp_pct_revenue_qoq_diff},
    "icv_drv2_014_intexp_pct_revenue_yoy_diff":    {"inputs": ["intexp", "revenue"],                "func": icv_drv2_014_intexp_pct_revenue_yoy_diff},
    "icv_drv2_015_ebit_ttm_cov_qoq_diff":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_015_ebit_ttm_cov_qoq_diff},
    "icv_drv2_016_ebit_ttm_cov_yoy_diff":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_016_ebit_ttm_cov_yoy_diff},
    "icv_drv2_017_ebit_cov_qoq_ewm_diff":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_017_ebit_cov_qoq_ewm_diff},
    "icv_drv2_018_ebit_cov_yoy_pct_qoq_diff":      {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_018_ebit_cov_yoy_pct_qoq_diff},
    "icv_drv2_019_ebitda_cov_yoy_pct_qoq_diff":    {"inputs": ["ebitda", "intexp"],                 "func": icv_drv2_019_ebitda_cov_yoy_pct_qoq_diff},
    "icv_drv2_020_ebit_zscore_4q_yoy_diff":        {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_020_ebit_zscore_4q_yoy_diff},
    "icv_drv2_021_ncfo_cov_qoq_diff_of_qoq":       {"inputs": ["ncfo", "intexp"],                   "func": icv_drv2_021_ncfo_cov_qoq_diff_of_qoq},
    "icv_drv2_022_ebit_cov_4q_slope_qoq_diff":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_022_ebit_cov_4q_slope_qoq_diff},
    "icv_drv2_023_ebit_minus_intexp_qoq_diff":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv2_023_ebit_minus_intexp_qoq_diff},
    "icv_drv2_024_ebitda_minus_intexp_qoq_diff":   {"inputs": ["ebitda", "intexp"],                 "func": icv_drv2_024_ebitda_minus_intexp_qoq_diff},
    "icv_drv2_025_composite_cov_zscore_qoq_diff":  {"inputs": ["ebit", "ebitda", "ncfo", "intexp"], "func": icv_drv2_025_composite_cov_zscore_qoq_diff},
}
