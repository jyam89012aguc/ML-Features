"""
66_interest_coverage — 3rd-Derivative Features 001-025
Domain: second-order rate of change of interest-coverage features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index because the
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


# ── 2nd-level base helpers (self-contained recomputes) ───────────────────────
# Each 3rd-derivative function builds on a 2nd-derivative concept,
# then takes another diff.  All inline; no cross-file imports.

def _ebit_cov(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebit, intexp)


def _ebitda_cov(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebitda, intexp)


def _ncfo_cov(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ncfo, intexp)


def _opinc_cov(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(opinc, intexp)


def _effective_rate(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    return _safe_div(intexp, debt.abs().replace(0, np.nan))


def _ebit_cov_qoq(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebit_cov(ebit, intexp)
    return cov - cov.shift(_TD_QTR)


def _ebitda_cov_qoq(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ebitda_cov(ebitda, intexp)
    return cov - cov.shift(_TD_QTR)


def _ncfo_cov_qoq(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    cov = _ncfo_cov(ncfo, intexp)
    return cov - cov.shift(_TD_QTR)


def _ebit_cov_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of QoQ EBIT coverage change (2nd derivative)."""
    d1 = _ebit_cov_qoq(ebit, intexp)
    return d1 - d1.shift(_TD_QTR)


def _ebitda_cov_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of QoQ EBITDA coverage change (2nd derivative)."""
    d1 = _ebitda_cov_qoq(ebitda, intexp)
    return d1 - d1.shift(_TD_QTR)


def _ncfo_cov_d2(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of QoQ ncfo coverage change (2nd derivative)."""
    d1 = _ncfo_cov_qoq(ncfo, intexp)
    return d1 - d1.shift(_TD_QTR)


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


def _ebit_ttm_cov(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))


def _intexp_as_pct_revenue(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(intexp, revenue.abs().replace(0, np.nan))


def _ebit_cov_drawdown_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    cov  = _ebit_cov(ebit, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def _ebitda_cov_drawdown_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    cov  = _ebitda_cov(ebitda, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def icv_drv3_001_ebit_cov_d3_qoq(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd-order QoQ diff of EBIT coverage (jerk in coverage trajectory)."""
    d2 = _ebit_cov_d2(ebit, intexp)
    return d2 - d2.shift(_TD_QTR)


def icv_drv3_002_ebitda_cov_d3_qoq(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd-order QoQ diff of EBITDA coverage."""
    d2 = _ebitda_cov_d2(ebitda, intexp)
    return d2 - d2.shift(_TD_QTR)


def icv_drv3_003_ncfo_cov_d3_qoq(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd-order QoQ diff of ncfo coverage."""
    d2 = _ncfo_cov_d2(ncfo, intexp)
    return d2 - d2.shift(_TD_QTR)


def icv_drv3_004_ebit_zscore_qoq_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ diff of the QoQ change in EBIT coverage z-score
    (2nd derivative of z-score = acceleration of distress signal).
    """
    z   = _ebit_zscore_4q(ebit, intexp)
    dz  = z - z.shift(_TD_QTR)
    return dz - dz.shift(_TD_QTR)


def icv_drv3_005_ebitda_zscore_qoq_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of the QoQ change in EBITDA coverage z-score."""
    z   = _ebitda_zscore_4q(ebitda, intexp)
    dz  = z - z.shift(_TD_QTR)
    return dz - dz.shift(_TD_QTR)


def icv_drv3_006_ncfo_zscore_qoq_d2(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of the QoQ change in ncfo coverage z-score."""
    z   = _ncfo_zscore_4q(ncfo, intexp)
    dz  = z - z.shift(_TD_QTR)
    return dz - dz.shift(_TD_QTR)


def icv_drv3_007_ebit_cov_drawdown_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change in EBIT coverage drawdown
    (acceleration of drawdown deepening).
    """
    dd = _ebit_cov_drawdown_4q(ebit, intexp)
    d1 = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_008_ebitda_cov_drawdown_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ change in EBITDA coverage drawdown."""
    dd = _ebitda_cov_drawdown_4q(ebitda, intexp)
    d1 = dd - dd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_009_effective_rate_d3(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """
    3rd-order QoQ diff of effective interest rate (intexp/debt).
    Captures the jerk in rate acceleration.
    """
    rate = _effective_rate(intexp, debt)
    d1   = rate - rate.shift(_TD_QTR)
    d2   = d1   - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icv_drv3_010_intexp_pct_revenue_d2(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of (intexp / revenue).
    Measures acceleration of the debt-burden-to-revenue trend.
    """
    base = _intexp_as_pct_revenue(intexp, revenue)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_011_ebit_ttm_cov_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of TTM EBIT coverage
    (acceleration of TTM coverage decline).
    """
    cov = _ebit_ttm_cov(ebit, intexp)
    d1  = cov - cov.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_012_ebit_cov_yoy_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ diff of the QoQ change in the YoY EBIT coverage change
    (3rd-order mixed derivative).
    """
    cov  = _ebit_cov(ebit, intexp)
    yoy  = cov - cov.shift(_TD_YEAR)
    d1   = yoy - yoy.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_013_ebitda_cov_yoy_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of the QoQ change in the YoY EBITDA coverage change."""
    cov  = _ebitda_cov(ebitda, intexp)
    yoy  = cov - cov.shift(_TD_YEAR)
    d1   = yoy - yoy.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_014_ncfo_cov_yoy_d2(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ diff of the QoQ change in the YoY ncfo coverage change."""
    cov  = _ncfo_cov(ncfo, intexp)
    yoy  = cov - cov.shift(_TD_YEAR)
    d1   = yoy - yoy.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_015_ebit_cov_slope_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of the 4-quarter OLS slope of EBIT coverage
    (3rd-order: is the slope of coverage accelerating downward?).
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
    d1    = slope - slope.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_016_composite_zscore_d2(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of composite coverage z-score
    (acceleration of composite distress worsening).
    """
    comp = (
        _ebit_zscore_4q(ebit, intexp)
        + _ebitda_zscore_4q(ebitda, intexp)
        + _ncfo_zscore_4q(ncfo, intexp)
    ) / 3.0
    d1 = comp - comp.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_017_ebit_cov_ewm_diff_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ EBIT coverage minus-EWM deviation
    (2nd derivative of the EWM-adjusted momentum signal).
    """
    cov  = _ebit_cov(ebit, intexp)
    qoq  = cov - cov.shift(_TD_QTR)
    ewm  = qoq.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    base = qoq - ewm
    return base - base.shift(_TD_QTR)


def icv_drv3_018_ebit_minus_intexp_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of (EBIT - intexp) gap
    (acceleration of gap narrowing or widening).
    """
    gap  = ebit - intexp
    d1   = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_019_ebitda_minus_intexp_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ change of (EBITDA - intexp) gap."""
    gap  = ebitda - intexp
    d1   = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_020_ncfo_minus_intexp_d2(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in the QoQ change of (ncfo - intexp) gap."""
    gap  = ncfo - intexp
    d1   = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_021_ebit_cov_qoq_pct_d2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of the YoY percent change of EBIT coverage.
    3rd-order: jerk in the year-over-year percentage deterioration rate.
    """
    cov   = _ebit_cov(ebit, intexp)
    prior = cov.shift(_TD_YEAR)
    pct   = _safe_div_abs(cov - prior, prior)
    d1    = pct - pct.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_022_ebitda_cov_qoq_pct_d2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd-order: jerk in the YoY percent change of EBITDA coverage."""
    cov   = _ebitda_cov(ebitda, intexp)
    prior = cov.shift(_TD_YEAR)
    pct   = _safe_div_abs(cov - prior, prior)
    d1    = pct - pct.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_023_effective_rate_pct_d2(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ change of the YoY percent change of effective interest rate.
    Captures jerk in rate-of-change of refinancing pressure.
    """
    rate  = _effective_rate(intexp, debt)
    prior = rate.shift(_TD_YEAR)
    pct   = _safe_div_abs(rate - prior, prior)
    d1    = pct - pct.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def icv_drv3_024_intexp_pct_revenue_d3(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    3rd-order QoQ diff of (intexp / revenue).
    Jerk in the debt-servicing-to-revenue burden trajectory.
    """
    base = _intexp_as_pct_revenue(intexp, revenue)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1   - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def icv_drv3_025_ebit_ttm_cov_d3(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    3rd-order QoQ diff of TTM EBIT coverage.
    Measures jerk in the TTM coverage decline rate.
    """
    cov = _ebit_ttm_cov(ebit, intexp)
    d1  = cov - cov.shift(_TD_QTR)
    d2  = d1  - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INTEREST_COVERAGE_REGISTRY_3RD_DERIVATIVES = {
    "icv_drv3_001_ebit_cov_d3_qoq":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_001_ebit_cov_d3_qoq},
    "icv_drv3_002_ebitda_cov_d3_qoq":        {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_002_ebitda_cov_d3_qoq},
    "icv_drv3_003_ncfo_cov_d3_qoq":          {"inputs": ["ncfo", "intexp"],                   "func": icv_drv3_003_ncfo_cov_d3_qoq},
    "icv_drv3_004_ebit_zscore_qoq_d2":       {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_004_ebit_zscore_qoq_d2},
    "icv_drv3_005_ebitda_zscore_qoq_d2":     {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_005_ebitda_zscore_qoq_d2},
    "icv_drv3_006_ncfo_zscore_qoq_d2":       {"inputs": ["ncfo", "intexp"],                   "func": icv_drv3_006_ncfo_zscore_qoq_d2},
    "icv_drv3_007_ebit_cov_drawdown_d2":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_007_ebit_cov_drawdown_d2},
    "icv_drv3_008_ebitda_cov_drawdown_d2":   {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_008_ebitda_cov_drawdown_d2},
    "icv_drv3_009_effective_rate_d3":        {"inputs": ["intexp", "debt"],                   "func": icv_drv3_009_effective_rate_d3},
    "icv_drv3_010_intexp_pct_revenue_d2":    {"inputs": ["intexp", "revenue"],                "func": icv_drv3_010_intexp_pct_revenue_d2},
    "icv_drv3_011_ebit_ttm_cov_d2":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_011_ebit_ttm_cov_d2},
    "icv_drv3_012_ebit_cov_yoy_d2":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_012_ebit_cov_yoy_d2},
    "icv_drv3_013_ebitda_cov_yoy_d2":        {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_013_ebitda_cov_yoy_d2},
    "icv_drv3_014_ncfo_cov_yoy_d2":          {"inputs": ["ncfo", "intexp"],                   "func": icv_drv3_014_ncfo_cov_yoy_d2},
    "icv_drv3_015_ebit_cov_slope_d2":        {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_015_ebit_cov_slope_d2},
    "icv_drv3_016_composite_zscore_d2":      {"inputs": ["ebit", "ebitda", "ncfo", "intexp"], "func": icv_drv3_016_composite_zscore_d2},
    "icv_drv3_017_ebit_cov_ewm_diff_d2":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_017_ebit_cov_ewm_diff_d2},
    "icv_drv3_018_ebit_minus_intexp_d2":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_018_ebit_minus_intexp_d2},
    "icv_drv3_019_ebitda_minus_intexp_d2":   {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_019_ebitda_minus_intexp_d2},
    "icv_drv3_020_ncfo_minus_intexp_d2":     {"inputs": ["ncfo", "intexp"],                   "func": icv_drv3_020_ncfo_minus_intexp_d2},
    "icv_drv3_021_ebit_cov_qoq_pct_d2":     {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_021_ebit_cov_qoq_pct_d2},
    "icv_drv3_022_ebitda_cov_qoq_pct_d2":   {"inputs": ["ebitda", "intexp"],                 "func": icv_drv3_022_ebitda_cov_qoq_pct_d2},
    "icv_drv3_023_effective_rate_pct_d2":    {"inputs": ["intexp", "debt"],                   "func": icv_drv3_023_effective_rate_pct_d2},
    "icv_drv3_024_intexp_pct_revenue_d3":    {"inputs": ["intexp", "revenue"],                "func": icv_drv3_024_intexp_pct_revenue_d3},
    "icv_drv3_025_ebit_ttm_cov_d3":          {"inputs": ["ebit", "intexp"],                   "func": icv_drv3_025_ebit_ttm_cov_d3},
}
