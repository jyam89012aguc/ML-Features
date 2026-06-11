"""
66_interest_coverage — Base Features 001-075
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): EBIT/intexp coverage level and changes ---

def icv_001_ebit_coverage(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT interest coverage ratio: ebit / intexp. NaN when intexp=0."""
    return _safe_div(ebit, intexp)


def icv_002_ebit_coverage_qoq_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in EBIT coverage ratio (63-day lag)."""
    cov = _safe_div(ebit, intexp)
    return cov - cov.shift(_TD_QTR)


def icv_003_ebit_coverage_yoy_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in EBIT coverage ratio (252-day lag)."""
    cov = _safe_div(ebit, intexp)
    return cov - cov.shift(_TD_YEAR)


def icv_004_ebit_coverage_qoq_pct(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ percent change in EBIT coverage ratio."""
    cov   = _safe_div(ebit, intexp)
    prior = cov.shift(_TD_QTR)
    return _safe_div_abs(cov - prior, prior)


def icv_005_ebit_coverage_yoy_pct(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY percent change in EBIT coverage ratio."""
    cov   = _safe_div(ebit, intexp)
    prior = cov.shift(_TD_YEAR)
    return _safe_div_abs(cov - prior, prior)


def icv_006_ebit_coverage_2y_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """2-year change in EBIT coverage ratio (504-day lag)."""
    cov = _safe_div(ebit, intexp)
    return cov - cov.shift(_TD_2Y)


def icv_007_ebit_coverage_3y_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """3-year change in EBIT coverage ratio (756-day lag)."""
    cov = _safe_div(ebit, intexp)
    return cov - cov.shift(_TD_3Y)


def icv_008_ebit_coverage_below_1(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT coverage < 1.0 (EBIT cannot cover interest)."""
    cov = _safe_div(ebit, intexp)
    return (cov < 1.0).astype(float)


def icv_009_ebit_coverage_below_2(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT coverage < 2.0 (thin coverage buffer)."""
    cov = _safe_div(ebit, intexp)
    return (cov < 2.0).astype(float)


def icv_010_ebit_coverage_below_zero(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT coverage < 0 (operating loss cannot cover interest)."""
    cov = _safe_div(ebit, intexp)
    return (cov < 0.0).astype(float)


def icv_011_ebit_coverage_drawdown_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage drawdown from its 4-quarter (252-day) rolling peak."""
    cov  = _safe_div(ebit, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def icv_012_ebit_coverage_drawdown_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage drawdown from its 8-quarter (504-day) rolling peak."""
    cov  = _safe_div(ebit, intexp)
    peak = _rolling_max(cov, _TD_2Y)
    return cov - peak


def icv_013_ebit_coverage_drawdown_expanding(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage drawdown from its all-history expanding peak."""
    cov  = _safe_div(ebit, intexp)
    peak = cov.expanding(min_periods=1).max()
    return cov - peak


def icv_014_ebit_coverage_vs_4q_avg(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage minus its trailing 4-quarter mean."""
    cov = _safe_div(ebit, intexp)
    return cov - _rolling_mean(cov, _TD_YEAR)


def icv_015_ebit_coverage_zscore_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBIT coverage within a trailing 4-quarter (252-day) window."""
    cov = _safe_div(ebit, intexp)
    return _zscore_rolling(cov, _TD_YEAR)


# --- Group B (016-030): EBITDA/intexp coverage ---

def icv_016_ebitda_coverage(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA interest coverage ratio: ebitda / intexp. NaN when intexp=0."""
    return _safe_div(ebitda, intexp)


def icv_017_ebitda_coverage_qoq_change(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return cov - cov.shift(_TD_QTR)


def icv_018_ebitda_coverage_yoy_change(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return cov - cov.shift(_TD_YEAR)


def icv_019_ebitda_coverage_below_1(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBITDA coverage < 1.0."""
    cov = _safe_div(ebitda, intexp)
    return (cov < 1.0).astype(float)


def icv_020_ebitda_coverage_below_2(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBITDA coverage < 2.0."""
    cov = _safe_div(ebitda, intexp)
    return (cov < 2.0).astype(float)


def icv_021_ebitda_coverage_drawdown_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage drawdown from trailing 4-quarter peak."""
    cov  = _safe_div(ebitda, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def icv_022_ebitda_coverage_drawdown_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage drawdown from trailing 8-quarter peak."""
    cov  = _safe_div(ebitda, intexp)
    peak = _rolling_max(cov, _TD_2Y)
    return cov - peak


def icv_023_ebitda_coverage_zscore_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBITDA coverage within a trailing 4-quarter window."""
    cov = _safe_div(ebitda, intexp)
    return _zscore_rolling(cov, _TD_YEAR)


def icv_024_ebitda_coverage_vs_4q_avg(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage minus its trailing 4-quarter mean."""
    cov = _safe_div(ebitda, intexp)
    return cov - _rolling_mean(cov, _TD_YEAR)


def icv_025_ebitda_coverage_2y_change(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """2-year change in EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return cov - cov.shift(_TD_2Y)


def icv_026_ebitda_coverage_pct_rank_4q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA coverage within trailing 4-quarter window."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_rank_pct(cov, _TD_YEAR)


def icv_027_ebitda_coverage_expanding_min(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding minimum of EBITDA coverage (worst-ever level)."""
    cov = _safe_div(ebitda, intexp)
    return cov.expanding(min_periods=1).min()


def icv_028_ebitda_coverage_qoq_pct(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ percent change in EBITDA coverage ratio."""
    cov   = _safe_div(ebitda, intexp)
    prior = cov.shift(_TD_QTR)
    return _safe_div_abs(cov - prior, prior)


def icv_029_ebitda_coverage_yoy_pct(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY percent change in EBITDA coverage ratio."""
    cov   = _safe_div(ebitda, intexp)
    prior = cov.shift(_TD_YEAR)
    return _safe_div_abs(cov - prior, prior)


def icv_030_ebitda_minus_ebit_coverage_gap(ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    EBITDA coverage minus EBIT coverage: measures how much of coverage
    depends on D&A add-back (larger gap = more D&A-dependent)."""
    return _safe_div(ebitda, intexp) - _safe_div(ebit, intexp)


# --- Group C (031-045): opinc/intexp and (EBITDA-capex)/intexp coverage ---

def icv_031_opinc_coverage(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Operating income interest coverage: opinc / intexp."""
    return _safe_div(opinc, intexp)


def icv_032_opinc_coverage_qoq_change(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in opinc coverage ratio."""
    cov = _safe_div(opinc, intexp)
    return cov - cov.shift(_TD_QTR)


def icv_033_opinc_coverage_yoy_change(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in opinc coverage ratio."""
    cov = _safe_div(opinc, intexp)
    return cov - cov.shift(_TD_YEAR)


def icv_034_opinc_coverage_below_1(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if opinc coverage < 1.0."""
    cov = _safe_div(opinc, intexp)
    return (cov < 1.0).astype(float)


def icv_035_opinc_coverage_drawdown_4q(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """opinc coverage drawdown from trailing 4-quarter peak."""
    cov  = _safe_div(opinc, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def icv_036_ebitda_minus_capex_coverage(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    (EBITDA - |capex|) / intexp: cash-flow-after-maintenance coverage.
    Capex is typically negative in SF1; we use abs so the subtraction
    reduces coverage as capex rises.
    """
    return _safe_div(ebitda - capex.abs(), intexp)


def icv_037_ebitda_minus_capex_coverage_qoq(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in (EBITDA - |capex|) coverage."""
    cov = _safe_div(ebitda - capex.abs(), intexp)
    return cov - cov.shift(_TD_QTR)


def icv_038_ebitda_minus_capex_coverage_below_1(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if (EBITDA - |capex|) coverage < 1.0."""
    cov = _safe_div(ebitda - capex.abs(), intexp)
    return (cov < 1.0).astype(float)


def icv_039_ebitda_minus_capex_coverage_drawdown_4q(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """(EBITDA - |capex|) coverage drawdown from trailing 4-quarter peak."""
    cov  = _safe_div(ebitda - capex.abs(), intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def icv_040_opinc_coverage_zscore_4q(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of opinc coverage within a trailing 4-quarter window."""
    cov = _safe_div(opinc, intexp)
    return _zscore_rolling(cov, _TD_YEAR)


def icv_041_opinc_coverage_2y_change(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """2-year change in opinc coverage ratio."""
    cov = _safe_div(opinc, intexp)
    return cov - cov.shift(_TD_2Y)


def icv_042_opinc_coverage_pct_rank_4q(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of opinc coverage within trailing 4-quarter window."""
    cov = _safe_div(opinc, intexp)
    return _rolling_rank_pct(cov, _TD_YEAR)


def icv_043_ebitda_minus_capex_coverage_yoy_change(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in (EBITDA - |capex|) coverage."""
    cov = _safe_div(ebitda - capex.abs(), intexp)
    return cov - cov.shift(_TD_YEAR)


def icv_044_opinc_coverage_expanding_min(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding minimum of opinc coverage."""
    cov = _safe_div(opinc, intexp)
    return cov.expanding(min_periods=1).min()


def icv_045_ebitda_minus_capex_coverage_zscore_4q(ebitda: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of (EBITDA - |capex|) coverage within trailing 4-quarter window."""
    cov = _safe_div(ebitda - capex.abs(), intexp)
    return _zscore_rolling(cov, _TD_YEAR)


# --- Group D (046-060): ncfo/intexp cash-flow coverage ---

def icv_046_ncfo_coverage(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Operating cash flow interest coverage: ncfo / intexp."""
    return _safe_div(ncfo, intexp)


def icv_047_ncfo_coverage_qoq_change(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in ncfo coverage ratio."""
    cov = _safe_div(ncfo, intexp)
    return cov - cov.shift(_TD_QTR)


def icv_048_ncfo_coverage_yoy_change(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in ncfo coverage ratio."""
    cov = _safe_div(ncfo, intexp)
    return cov - cov.shift(_TD_YEAR)


def icv_049_ncfo_coverage_below_1(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if ncfo coverage < 1.0 (operating cash flow cannot cover interest)."""
    cov = _safe_div(ncfo, intexp)
    return (cov < 1.0).astype(float)


def icv_050_ncfo_coverage_below_zero(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if ncfo < 0 (negative operating cash flow regardless of interest)."""
    return (ncfo < 0).astype(float)


def icv_051_ncfo_coverage_drawdown_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """ncfo coverage drawdown from trailing 4-quarter peak."""
    cov  = _safe_div(ncfo, intexp)
    peak = _rolling_max(cov, _TD_YEAR)
    return cov - peak


def icv_052_ncfo_coverage_drawdown_8q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """ncfo coverage drawdown from trailing 8-quarter peak."""
    cov  = _safe_div(ncfo, intexp)
    peak = _rolling_max(cov, _TD_2Y)
    return cov - peak


def icv_053_ncfo_coverage_zscore_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of ncfo coverage within a trailing 4-quarter window."""
    cov = _safe_div(ncfo, intexp)
    return _zscore_rolling(cov, _TD_YEAR)


def icv_054_ncfo_coverage_2y_change(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """2-year change in ncfo coverage ratio."""
    cov = _safe_div(ncfo, intexp)
    return cov - cov.shift(_TD_2Y)


def icv_055_ncfo_coverage_pct_rank_4q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of ncfo coverage within trailing 4-quarter window."""
    cov = _safe_div(ncfo, intexp)
    return _rolling_rank_pct(cov, _TD_YEAR)


def icv_056_ncfo_minus_capex_coverage(ncfo: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """Free cash flow coverage: (ncfo - |capex|) / intexp."""
    return _safe_div(ncfo - capex.abs(), intexp)


def icv_057_ncfo_minus_capex_coverage_qoq(ncfo: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """QoQ change in free-cash-flow coverage (ncfo - |capex|) / intexp."""
    cov = _safe_div(ncfo - capex.abs(), intexp)
    return cov - cov.shift(_TD_QTR)


def icv_058_ncfo_minus_capex_coverage_below_1(ncfo: pd.Series, capex: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if (ncfo - |capex|) coverage < 1.0."""
    cov = _safe_div(ncfo - capex.abs(), intexp)
    return (cov < 1.0).astype(float)


def icv_059_ncfo_coverage_expanding_min(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding minimum of ncfo coverage."""
    cov = _safe_div(ncfo, intexp)
    return cov.expanding(min_periods=1).min()


def icv_060_ncfo_coverage_vs_4q_avg(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """ncfo coverage minus its trailing 4-quarter mean."""
    cov = _safe_div(ncfo, intexp)
    return cov - _rolling_mean(cov, _TD_YEAR)


# --- Group E (061-075): Interest expense growth, effective rate, intexp share ---

def icv_061_intexp_yoy_change(intexp: pd.Series) -> pd.Series:
    """YoY absolute change in interest expense (rising = more debt-servicing cost)."""
    return intexp - intexp.shift(_TD_YEAR)


def icv_062_intexp_qoq_change(intexp: pd.Series) -> pd.Series:
    """QoQ absolute change in interest expense."""
    return intexp - intexp.shift(_TD_QTR)


def icv_063_intexp_yoy_pct(intexp: pd.Series) -> pd.Series:
    """YoY percent change in interest expense."""
    prior = intexp.shift(_TD_YEAR)
    return _safe_div_abs(intexp - prior, prior)


def icv_064_intexp_as_pct_revenue(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Interest expense as a fraction of revenue (higher = more revenue consumed by debt)."""
    return _safe_div(intexp, revenue.abs().replace(0, np.nan))


def icv_065_intexp_as_pct_revenue_zscore_4q(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Z-score of the interest-expense-to-revenue ratio within a trailing 4-quarter (252-day)
    window.  High positive z-score = interest burden near its worst recent level.
    """
    ratio = _safe_div(intexp, revenue.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


def icv_066_intexp_as_pct_opinc(intexp: pd.Series, opinc: pd.Series) -> pd.Series:
    """Interest expense as a fraction of operating income (>1 means interest > opinc)."""
    return _safe_div(intexp, opinc.abs().replace(0, np.nan))


def icv_067_intexp_as_pct_ebitda(intexp: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Interest expense as a fraction of EBITDA."""
    return _safe_div(intexp, ebitda.abs().replace(0, np.nan))


def icv_068_effective_interest_rate(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Effective interest rate: intexp / debt.
    Rising rate signals refinancing risk or floating-rate exposure.
    NaN when debt=0.
    """
    return _safe_div(intexp, debt.abs().replace(0, np.nan))


def icv_069_effective_rate_yoy_change(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """YoY change in effective interest rate (intexp/debt)."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return rate - rate.shift(_TD_YEAR)


def icv_070_effective_rate_zscore_4q(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of effective interest rate within trailing 4-quarter window."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return _zscore_rolling(rate, _TD_YEAR)


def icv_071_ebit_falling_intexp_rising_flag(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Binary: 1 when EBIT is lower YoY AND intexp is higher YoY simultaneously.
    Classic double-squeeze — operating income shrinks while interest burden grows.
    """
    ebit_down    = (ebit < ebit.shift(_TD_YEAR)).astype(float)
    intexp_up    = (intexp > intexp.shift(_TD_YEAR)).astype(float)
    return ebit_down * intexp_up


def icv_072_ebitda_falling_intexp_rising_flag(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 when EBITDA lower YoY AND intexp higher YoY."""
    ebitda_down  = (ebitda < ebitda.shift(_TD_YEAR)).astype(float)
    intexp_up    = (intexp > intexp.shift(_TD_YEAR)).astype(float)
    return ebitda_down * intexp_up


def icv_073_coverage_distance_to_distress(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Distance of EBIT coverage ratio to the 1.0 distress line:
    (ebit/intexp) - 1.0.  Negative means already in distress.
    NaN when intexp=0.
    """
    cov = _safe_div(ebit, intexp)
    return cov - 1.0


def icv_074_ncfo_coverage_consecutive_below_1(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Consecutive-day streak of ncfo coverage < 1.0.
    Resets to 0 whenever coverage rises to or above 1.0.
    """
    cov  = _safe_div(ncfo, intexp)
    flag = (cov < 1.0).fillna(False).astype(int)
    arr  = flag.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ncfo.index)


def icv_075_coverage_composite_4q(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """
    Composite interest-coverage severity score: equally weighted average of
    the 4-quarter z-scores of EBIT, EBITDA, and ncfo coverage ratios.
    Lower (more negative) = more distressed.
    """
    z_ebit   = _zscore_rolling(_safe_div(ebit,   intexp), _TD_YEAR)
    z_ebitda = _zscore_rolling(_safe_div(ebitda, intexp), _TD_YEAR)
    z_ncfo   = _zscore_rolling(_safe_div(ncfo,   intexp), _TD_YEAR)
    return (z_ebit + z_ebitda + z_ncfo) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INTEREST_COVERAGE_REGISTRY_001_075 = {
    "icv_001_ebit_coverage":                          {"inputs": ["ebit", "intexp"],                      "func": icv_001_ebit_coverage},
    "icv_002_ebit_coverage_qoq_change":               {"inputs": ["ebit", "intexp"],                      "func": icv_002_ebit_coverage_qoq_change},
    "icv_003_ebit_coverage_yoy_change":               {"inputs": ["ebit", "intexp"],                      "func": icv_003_ebit_coverage_yoy_change},
    "icv_004_ebit_coverage_qoq_pct":                  {"inputs": ["ebit", "intexp"],                      "func": icv_004_ebit_coverage_qoq_pct},
    "icv_005_ebit_coverage_yoy_pct":                  {"inputs": ["ebit", "intexp"],                      "func": icv_005_ebit_coverage_yoy_pct},
    "icv_006_ebit_coverage_2y_change":                {"inputs": ["ebit", "intexp"],                      "func": icv_006_ebit_coverage_2y_change},
    "icv_007_ebit_coverage_3y_change":                {"inputs": ["ebit", "intexp"],                      "func": icv_007_ebit_coverage_3y_change},
    "icv_008_ebit_coverage_below_1":                  {"inputs": ["ebit", "intexp"],                      "func": icv_008_ebit_coverage_below_1},
    "icv_009_ebit_coverage_below_2":                  {"inputs": ["ebit", "intexp"],                      "func": icv_009_ebit_coverage_below_2},
    "icv_010_ebit_coverage_below_zero":               {"inputs": ["ebit", "intexp"],                      "func": icv_010_ebit_coverage_below_zero},
    "icv_011_ebit_coverage_drawdown_4q":              {"inputs": ["ebit", "intexp"],                      "func": icv_011_ebit_coverage_drawdown_4q},
    "icv_012_ebit_coverage_drawdown_8q":              {"inputs": ["ebit", "intexp"],                      "func": icv_012_ebit_coverage_drawdown_8q},
    "icv_013_ebit_coverage_drawdown_expanding":       {"inputs": ["ebit", "intexp"],                      "func": icv_013_ebit_coverage_drawdown_expanding},
    "icv_014_ebit_coverage_vs_4q_avg":                {"inputs": ["ebit", "intexp"],                      "func": icv_014_ebit_coverage_vs_4q_avg},
    "icv_015_ebit_coverage_zscore_4q":                {"inputs": ["ebit", "intexp"],                      "func": icv_015_ebit_coverage_zscore_4q},
    "icv_016_ebitda_coverage":                        {"inputs": ["ebitda", "intexp"],                    "func": icv_016_ebitda_coverage},
    "icv_017_ebitda_coverage_qoq_change":             {"inputs": ["ebitda", "intexp"],                    "func": icv_017_ebitda_coverage_qoq_change},
    "icv_018_ebitda_coverage_yoy_change":             {"inputs": ["ebitda", "intexp"],                    "func": icv_018_ebitda_coverage_yoy_change},
    "icv_019_ebitda_coverage_below_1":                {"inputs": ["ebitda", "intexp"],                    "func": icv_019_ebitda_coverage_below_1},
    "icv_020_ebitda_coverage_below_2":                {"inputs": ["ebitda", "intexp"],                    "func": icv_020_ebitda_coverage_below_2},
    "icv_021_ebitda_coverage_drawdown_4q":            {"inputs": ["ebitda", "intexp"],                    "func": icv_021_ebitda_coverage_drawdown_4q},
    "icv_022_ebitda_coverage_drawdown_8q":            {"inputs": ["ebitda", "intexp"],                    "func": icv_022_ebitda_coverage_drawdown_8q},
    "icv_023_ebitda_coverage_zscore_4q":              {"inputs": ["ebitda", "intexp"],                    "func": icv_023_ebitda_coverage_zscore_4q},
    "icv_024_ebitda_coverage_vs_4q_avg":              {"inputs": ["ebitda", "intexp"],                    "func": icv_024_ebitda_coverage_vs_4q_avg},
    "icv_025_ebitda_coverage_2y_change":              {"inputs": ["ebitda", "intexp"],                    "func": icv_025_ebitda_coverage_2y_change},
    "icv_026_ebitda_coverage_pct_rank_4q":            {"inputs": ["ebitda", "intexp"],                    "func": icv_026_ebitda_coverage_pct_rank_4q},
    "icv_027_ebitda_coverage_expanding_min":          {"inputs": ["ebitda", "intexp"],                    "func": icv_027_ebitda_coverage_expanding_min},
    "icv_028_ebitda_coverage_qoq_pct":                {"inputs": ["ebitda", "intexp"],                    "func": icv_028_ebitda_coverage_qoq_pct},
    "icv_029_ebitda_coverage_yoy_pct":                {"inputs": ["ebitda", "intexp"],                    "func": icv_029_ebitda_coverage_yoy_pct},
    "icv_030_ebitda_minus_ebit_coverage_gap":         {"inputs": ["ebitda", "ebit", "intexp"],            "func": icv_030_ebitda_minus_ebit_coverage_gap},
    "icv_031_opinc_coverage":                         {"inputs": ["opinc", "intexp"],                     "func": icv_031_opinc_coverage},
    "icv_032_opinc_coverage_qoq_change":              {"inputs": ["opinc", "intexp"],                     "func": icv_032_opinc_coverage_qoq_change},
    "icv_033_opinc_coverage_yoy_change":              {"inputs": ["opinc", "intexp"],                     "func": icv_033_opinc_coverage_yoy_change},
    "icv_034_opinc_coverage_below_1":                 {"inputs": ["opinc", "intexp"],                     "func": icv_034_opinc_coverage_below_1},
    "icv_035_opinc_coverage_drawdown_4q":             {"inputs": ["opinc", "intexp"],                     "func": icv_035_opinc_coverage_drawdown_4q},
    "icv_036_ebitda_minus_capex_coverage":            {"inputs": ["ebitda", "capex", "intexp"],           "func": icv_036_ebitda_minus_capex_coverage},
    "icv_037_ebitda_minus_capex_coverage_qoq":        {"inputs": ["ebitda", "capex", "intexp"],           "func": icv_037_ebitda_minus_capex_coverage_qoq},
    "icv_038_ebitda_minus_capex_coverage_below_1":    {"inputs": ["ebitda", "capex", "intexp"],           "func": icv_038_ebitda_minus_capex_coverage_below_1},
    "icv_039_ebitda_minus_capex_coverage_drawdown_4q": {"inputs": ["ebitda", "capex", "intexp"],          "func": icv_039_ebitda_minus_capex_coverage_drawdown_4q},
    "icv_040_opinc_coverage_zscore_4q":               {"inputs": ["opinc", "intexp"],                     "func": icv_040_opinc_coverage_zscore_4q},
    "icv_041_opinc_coverage_2y_change":               {"inputs": ["opinc", "intexp"],                     "func": icv_041_opinc_coverage_2y_change},
    "icv_042_opinc_coverage_pct_rank_4q":             {"inputs": ["opinc", "intexp"],                     "func": icv_042_opinc_coverage_pct_rank_4q},
    "icv_043_ebitda_minus_capex_coverage_yoy_change": {"inputs": ["ebitda", "capex", "intexp"],           "func": icv_043_ebitda_minus_capex_coverage_yoy_change},
    "icv_044_opinc_coverage_expanding_min":           {"inputs": ["opinc", "intexp"],                     "func": icv_044_opinc_coverage_expanding_min},
    "icv_045_ebitda_minus_capex_coverage_zscore_4q":  {"inputs": ["ebitda", "capex", "intexp"],           "func": icv_045_ebitda_minus_capex_coverage_zscore_4q},
    "icv_046_ncfo_coverage":                          {"inputs": ["ncfo", "intexp"],                      "func": icv_046_ncfo_coverage},
    "icv_047_ncfo_coverage_qoq_change":               {"inputs": ["ncfo", "intexp"],                      "func": icv_047_ncfo_coverage_qoq_change},
    "icv_048_ncfo_coverage_yoy_change":               {"inputs": ["ncfo", "intexp"],                      "func": icv_048_ncfo_coverage_yoy_change},
    "icv_049_ncfo_coverage_below_1":                  {"inputs": ["ncfo", "intexp"],                      "func": icv_049_ncfo_coverage_below_1},
    "icv_050_ncfo_coverage_below_zero":               {"inputs": ["ncfo", "intexp"],                      "func": icv_050_ncfo_coverage_below_zero},
    "icv_051_ncfo_coverage_drawdown_4q":              {"inputs": ["ncfo", "intexp"],                      "func": icv_051_ncfo_coverage_drawdown_4q},
    "icv_052_ncfo_coverage_drawdown_8q":              {"inputs": ["ncfo", "intexp"],                      "func": icv_052_ncfo_coverage_drawdown_8q},
    "icv_053_ncfo_coverage_zscore_4q":                {"inputs": ["ncfo", "intexp"],                      "func": icv_053_ncfo_coverage_zscore_4q},
    "icv_054_ncfo_coverage_2y_change":                {"inputs": ["ncfo", "intexp"],                      "func": icv_054_ncfo_coverage_2y_change},
    "icv_055_ncfo_coverage_pct_rank_4q":              {"inputs": ["ncfo", "intexp"],                      "func": icv_055_ncfo_coverage_pct_rank_4q},
    "icv_056_ncfo_minus_capex_coverage":              {"inputs": ["ncfo", "capex", "intexp"],             "func": icv_056_ncfo_minus_capex_coverage},
    "icv_057_ncfo_minus_capex_coverage_qoq":          {"inputs": ["ncfo", "capex", "intexp"],             "func": icv_057_ncfo_minus_capex_coverage_qoq},
    "icv_058_ncfo_minus_capex_coverage_below_1":      {"inputs": ["ncfo", "capex", "intexp"],             "func": icv_058_ncfo_minus_capex_coverage_below_1},
    "icv_059_ncfo_coverage_expanding_min":            {"inputs": ["ncfo", "intexp"],                      "func": icv_059_ncfo_coverage_expanding_min},
    "icv_060_ncfo_coverage_vs_4q_avg":                {"inputs": ["ncfo", "intexp"],                      "func": icv_060_ncfo_coverage_vs_4q_avg},
    "icv_061_intexp_yoy_change":                      {"inputs": ["intexp"],                              "func": icv_061_intexp_yoy_change},
    "icv_062_intexp_qoq_change":                      {"inputs": ["intexp"],                              "func": icv_062_intexp_qoq_change},
    "icv_063_intexp_yoy_pct":                         {"inputs": ["intexp"],                              "func": icv_063_intexp_yoy_pct},
    "icv_064_intexp_as_pct_revenue":                  {"inputs": ["intexp", "revenue"],                   "func": icv_064_intexp_as_pct_revenue},
    "icv_065_intexp_as_pct_revenue_zscore_4q":        {"inputs": ["intexp", "revenue"],                   "func": icv_065_intexp_as_pct_revenue_zscore_4q},
    "icv_066_intexp_as_pct_opinc":                    {"inputs": ["intexp", "opinc"],                     "func": icv_066_intexp_as_pct_opinc},
    "icv_067_intexp_as_pct_ebitda":                   {"inputs": ["intexp", "ebitda"],                    "func": icv_067_intexp_as_pct_ebitda},
    "icv_068_effective_interest_rate":                {"inputs": ["intexp", "debt"],                      "func": icv_068_effective_interest_rate},
    "icv_069_effective_rate_yoy_change":              {"inputs": ["intexp", "debt"],                      "func": icv_069_effective_rate_yoy_change},
    "icv_070_effective_rate_zscore_4q":               {"inputs": ["intexp", "debt"],                      "func": icv_070_effective_rate_zscore_4q},
    "icv_071_ebit_falling_intexp_rising_flag":        {"inputs": ["ebit", "intexp"],                      "func": icv_071_ebit_falling_intexp_rising_flag},
    "icv_072_ebitda_falling_intexp_rising_flag":      {"inputs": ["ebitda", "intexp"],                    "func": icv_072_ebitda_falling_intexp_rising_flag},
    "icv_073_coverage_distance_to_distress":          {"inputs": ["ebit", "intexp"],                      "func": icv_073_coverage_distance_to_distress},
    "icv_074_ncfo_coverage_consecutive_below_1":      {"inputs": ["ncfo", "intexp"],                      "func": icv_074_ncfo_coverage_consecutive_below_1},
    "icv_075_coverage_composite_4q":                  {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],    "func": icv_075_coverage_composite_4q},
}
