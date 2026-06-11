"""
75_guidance_distress — 2nd-Derivative Features 001-075
Domain: rate of change of base guidance-distress / miss-severity features
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

IMPORTANT — Data availability note
------------------------------------
Analyst estimates / company guidance are not available in Sharadar SF1.
This folder uses trend-implied expectations (naive, seasonal-naive, and
extrapolated models) as the estimate proxy; the 'miss' is actual minus
model expectation.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 2nd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ── Base-concept helpers (self-contained recomputes) ─────────────────────────

def _naive_expect(s: pd.Series) -> pd.Series:
    return s.shift(_TD_QTR)


def _seasonal_naive_expect(s: pd.Series) -> pd.Series:
    return s.shift(_TD_YEAR)


def _ewm_trend_expect(s: pd.Series, span: int) -> pd.Series:
    return _ewm_mean(s, span).shift(_TD_QTR)


def _trail_avg_expect(s: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(s, w).shift(_TD_QTR)


def _naive_miss(s: pd.Series) -> pd.Series:
    return s - _naive_expect(s)


def _seasonal_miss(s: pd.Series) -> pd.Series:
    return s - _seasonal_naive_expect(s)


def _sue_naive(s: pd.Series) -> pd.Series:
    m = _naive_miss(s)
    vol = _rolling_std(s, _TD_YEAR)
    return _safe_div(m, vol)


def _miss_zscore_4q(s: pd.Series) -> pd.Series:
    m = _naive_miss(s)
    return _safe_div(m - _rolling_mean(m, _TD_YEAR), _rolling_std(m, _TD_YEAR))


def _ewm_miss(s: pd.Series) -> pd.Series:
    return s - _ewm_trend_expect(s, _TD_YEAR)


def _trail_avg_miss(s: pd.Series, w: int) -> pd.Series:
    return s - _trail_avg_expect(s, w)


def _miss_worst_4q(s: pd.Series) -> pd.Series:
    return _rolling_min(_naive_miss(s), _TD_YEAR)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def gds_drv2_001_rev_naive_miss_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue naive-miss (rate of miss deterioration)."""
    base = _naive_miss(revenue)
    return base - base.shift(_TD_QTR)


def gds_drv2_002_netinc_naive_miss_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income naive-miss."""
    base = _naive_miss(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_003_eps_naive_miss_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS naive-miss."""
    base = _naive_miss(eps)
    return base - base.shift(_TD_QTR)


def gds_drv2_004_rev_naive_miss_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in revenue naive-miss (year-over-year miss trend shift)."""
    base = _naive_miss(revenue)
    return base - base.shift(_TD_YEAR)


def gds_drv2_005_netinc_naive_miss_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in net income naive-miss."""
    base = _naive_miss(netinc)
    return base - base.shift(_TD_YEAR)


def gds_drv2_006_eps_sue_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS SUE-style score (standardized miss acceleration)."""
    base = _sue_naive(eps)
    return base - base.shift(_TD_QTR)


def gds_drv2_007_netinc_sue_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income SUE-style score."""
    base = _sue_naive(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_008_rev_sue_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue SUE-style score."""
    base = _sue_naive(revenue)
    return base - base.shift(_TD_QTR)


def gds_drv2_009_netinc_miss_zscore_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the 4Q z-score of net income naive-miss."""
    base = _miss_zscore_4q(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_010_rev_miss_zscore_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in the 4Q z-score of revenue naive-miss."""
    base = _miss_zscore_4q(revenue)
    return base - base.shift(_TD_YEAR)


def gds_drv2_011_netinc_ewm_miss_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income EWM-miss (EWM-trend miss acceleration)."""
    base = _ewm_miss(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_012_rev_ewm_miss_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue EWM-miss."""
    base = _ewm_miss(revenue)
    return base - base.shift(_TD_QTR)


def gds_drv2_013_eps_seasonal_miss_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS seasonal-naive miss."""
    base = _seasonal_miss(eps)
    return base - base.shift(_TD_QTR)


def gds_drv2_014_netinc_seasonal_miss_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in net income seasonal-naive miss (2nd-order YoY miss)."""
    base = _seasonal_miss(netinc)
    return base - base.shift(_TD_YEAR)


def gds_drv2_015_rev_trail_avg_miss_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue trailing-average miss."""
    base = _trail_avg_miss(revenue, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def gds_drv2_016_netinc_miss_worst_4q_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q net income naive-miss (deepening trough)."""
    base = _miss_worst_4q(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_017_rev_miss_worst_4q_qoq_diff(revenue: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q revenue naive-miss."""
    base = _miss_worst_4q(revenue)
    return base - base.shift(_TD_QTR)


def gds_drv2_018_netinc_naive_miss_pct_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ percent change in net income naive-miss series."""
    base = _naive_miss(netinc)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def gds_drv2_019_eps_sue_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in EPS SUE-style score."""
    base = _sue_naive(eps)
    return base - base.shift(_TD_YEAR)


def gds_drv2_020_netinc_miss_slope_of_slope(netinc: pd.Series) -> pd.Series:
    """
    Rolling OLS slope of the QoQ net income naive-miss change series.
    Captures the trend in the first-derivative of the miss.
    """
    miss_chg = _naive_miss(netinc)
    miss_chg = miss_chg - miss_chg.shift(_TD_QTR)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom

    return miss_chg.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv2_021_gp_naive_miss_qoq_diff(gp: pd.Series) -> pd.Series:
    """QoQ change in gross profit naive-miss."""
    base = _naive_miss(gp)
    return base - base.shift(_TD_QTR)


def gds_drv2_022_ebitda_naive_miss_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in EBITDA naive-miss."""
    base = _naive_miss(ebitda)
    return base - base.shift(_TD_QTR)


def gds_drv2_023_fcf_naive_miss_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF naive-miss."""
    base = _naive_miss(fcf)
    return base - base.shift(_TD_QTR)


def gds_drv2_024_netinc_sue_ewm_diff(netinc: pd.Series) -> pd.Series:
    """
    Net income SUE score minus its own EWM (span=252):
    measures whether the current SUE is worse than its own recent trend.
    """
    base = _sue_naive(netinc)
    ewm  = _ewm_mean(base, _TD_YEAR)
    return base - ewm


def gds_drv2_025_composite_miss_accel(revenue: pd.Series, netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """
    Composite 2nd-derivative: QoQ change in the average naive-miss z-score
    for revenue, net income, and EPS.  Captures broadening miss acceleration.
    """
    def _mz(s):
        m = _naive_miss(s)
        vol = _rolling_std(s, _TD_YEAR)
        return _safe_div(m, vol)

    composite = (_mz(revenue) + _mz(netinc) + _mz(eps)) / 3.0
    return composite - composite.shift(_TD_QTR)


# ── 2nd-derivative feature functions 026-075 ─────────────────────────────────

def gds_drv2_026_gp_naive_miss_yoy_diff(gp: pd.Series) -> pd.Series:
    """YoY change in gross profit naive-miss."""
    base = _naive_miss(gp)
    return base - base.shift(_TD_YEAR)


def gds_drv2_027_ebitda_naive_miss_yoy_diff(ebitda: pd.Series) -> pd.Series:
    """YoY change in EBITDA naive-miss."""
    base = _naive_miss(ebitda)
    return base - base.shift(_TD_YEAR)


def gds_drv2_028_fcf_naive_miss_yoy_diff(fcf: pd.Series) -> pd.Series:
    """YoY change in FCF naive-miss."""
    base = _naive_miss(fcf)
    return base - base.shift(_TD_YEAR)


def gds_drv2_029_ncfo_naive_miss_qoq_diff(ncfo: pd.Series) -> pd.Series:
    """QoQ change in operating CF naive-miss."""
    base = _naive_miss(ncfo)
    return base - base.shift(_TD_QTR)


def gds_drv2_030_ncfo_naive_miss_yoy_diff(ncfo: pd.Series) -> pd.Series:
    """YoY change in operating CF naive-miss."""
    base = _naive_miss(ncfo)
    return base - base.shift(_TD_YEAR)


def gds_drv2_031_epsdil_naive_miss_qoq_diff(epsdil: pd.Series) -> pd.Series:
    """QoQ change in diluted EPS naive-miss."""
    base = _naive_miss(epsdil)
    return base - base.shift(_TD_QTR)


def gds_drv2_032_epsdil_naive_miss_yoy_diff(epsdil: pd.Series) -> pd.Series:
    """YoY change in diluted EPS naive-miss."""
    base = _naive_miss(epsdil)
    return base - base.shift(_TD_YEAR)


def gds_drv2_033_opinc_naive_miss_qoq_diff(opinc: pd.Series) -> pd.Series:
    """QoQ change in operating income naive-miss."""
    base = _naive_miss(opinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_034_opinc_naive_miss_yoy_diff(opinc: pd.Series) -> pd.Series:
    """YoY change in operating income naive-miss."""
    base = _naive_miss(opinc)
    return base - base.shift(_TD_YEAR)


def gds_drv2_035_rev_seasonal_miss_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in revenue seasonal-naive miss."""
    base = _seasonal_miss(revenue)
    return base - base.shift(_TD_YEAR)


def gds_drv2_036_netinc_seasonal_miss_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income seasonal-naive miss."""
    base = _seasonal_miss(netinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_037_eps_seasonal_miss_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in EPS seasonal-naive miss."""
    base = _seasonal_miss(eps)
    return base - base.shift(_TD_YEAR)


def gds_drv2_038_gp_sue_qoq_diff(gp: pd.Series) -> pd.Series:
    """QoQ change in gross profit SUE-style score."""
    base = _sue_naive(gp)
    return base - base.shift(_TD_QTR)


def gds_drv2_039_ebitda_sue_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in EBITDA SUE-style score."""
    base = _sue_naive(ebitda)
    return base - base.shift(_TD_QTR)


def gds_drv2_040_fcf_sue_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF SUE-style score."""
    base = _sue_naive(fcf)
    return base - base.shift(_TD_QTR)


def gds_drv2_041_ncfo_sue_qoq_diff(ncfo: pd.Series) -> pd.Series:
    """QoQ change in operating CF SUE-style score."""
    base = _sue_naive(ncfo)
    return base - base.shift(_TD_QTR)


def gds_drv2_042_opinc_sue_qoq_diff(opinc: pd.Series) -> pd.Series:
    """QoQ change in operating income SUE-style score."""
    base = _sue_naive(opinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_043_epsdil_sue_qoq_diff(epsdil: pd.Series) -> pd.Series:
    """QoQ change in diluted EPS SUE-style score."""
    base = _sue_naive(epsdil)
    return base - base.shift(_TD_QTR)


def gds_drv2_044_eps_miss_zscore_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in the 4Q z-score of EPS naive-miss."""
    base = _miss_zscore_4q(eps)
    return base - base.shift(_TD_YEAR)


def gds_drv2_045_gp_miss_zscore_qoq_diff(gp: pd.Series) -> pd.Series:
    """QoQ change in the 4Q z-score of gross profit naive-miss."""
    base = _miss_zscore_4q(gp)
    return base - base.shift(_TD_QTR)


def gds_drv2_046_ebitda_miss_zscore_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in the 4Q z-score of EBITDA naive-miss."""
    base = _miss_zscore_4q(ebitda)
    return base - base.shift(_TD_QTR)


def gds_drv2_047_fcf_ewm_miss_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF EWM-miss."""
    base = _ewm_miss(fcf)
    return base - base.shift(_TD_QTR)


def gds_drv2_048_ncfo_ewm_miss_qoq_diff(ncfo: pd.Series) -> pd.Series:
    """QoQ change in operating CF EWM-miss."""
    base = _ewm_miss(ncfo)
    return base - base.shift(_TD_QTR)


def gds_drv2_049_opinc_ewm_miss_qoq_diff(opinc: pd.Series) -> pd.Series:
    """QoQ change in operating income EWM-miss."""
    base = _ewm_miss(opinc)
    return base - base.shift(_TD_QTR)


def gds_drv2_050_epsdil_ewm_miss_qoq_diff(epsdil: pd.Series) -> pd.Series:
    """QoQ change in diluted EPS EWM-miss."""
    base = _ewm_miss(epsdil)
    return base - base.shift(_TD_QTR)


def gds_drv2_051_rev_miss_worst_4q_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in worst-4Q revenue naive-miss (multi-year trough deepening)."""
    base = _miss_worst_4q(revenue)
    return base - base.shift(_TD_YEAR)


def gds_drv2_052_netinc_miss_worst_4q_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in worst-4Q net income naive-miss."""
    base = _miss_worst_4q(netinc)
    return base - base.shift(_TD_YEAR)


def gds_drv2_053_eps_miss_worst_4q_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q EPS naive-miss."""
    base = _miss_worst_4q(eps)
    return base - base.shift(_TD_QTR)


def gds_drv2_054_gp_miss_worst_4q_qoq_diff(gp: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q gross profit naive-miss."""
    base = _miss_worst_4q(gp)
    return base - base.shift(_TD_QTR)


def gds_drv2_055_ebitda_miss_worst_4q_qoq_diff(ebitda: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q EBITDA naive-miss."""
    base = _miss_worst_4q(ebitda)
    return base - base.shift(_TD_QTR)


def gds_drv2_056_fcf_miss_worst_4q_qoq_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in worst-4Q FCF naive-miss."""
    base = _miss_worst_4q(fcf)
    return base - base.shift(_TD_QTR)


def gds_drv2_057_rev_trail_avg_miss_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in revenue trailing-average miss."""
    base = _trail_avg_miss(revenue, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def gds_drv2_058_netinc_trail_avg_miss_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income trailing-average miss."""
    base = _trail_avg_miss(netinc, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def gds_drv2_059_eps_trail_avg_miss_qoq_diff(eps: pd.Series) -> pd.Series:
    """QoQ change in EPS trailing-average miss."""
    base = _trail_avg_miss(eps, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def gds_drv2_060_rev_naive_miss_pct_yoy(revenue: pd.Series) -> pd.Series:
    """YoY percent change in revenue naive-miss series."""
    base = _naive_miss(revenue)
    return _safe_div_abs(base - base.shift(_TD_YEAR), base.shift(_TD_YEAR))


def gds_drv2_061_eps_naive_miss_pct_qoq(eps: pd.Series) -> pd.Series:
    """QoQ percent change in EPS naive-miss series."""
    base = _naive_miss(eps)
    return _safe_div_abs(base - base.shift(_TD_QTR), base.shift(_TD_QTR))


def gds_drv2_062_rev_sue_ewm_diff(revenue: pd.Series) -> pd.Series:
    """Revenue SUE score minus its own EWM (span=252): deviation from trend."""
    base = _sue_naive(revenue)
    return base - _ewm_mean(base, _TD_YEAR)


def gds_drv2_063_eps_sue_ewm_diff(eps: pd.Series) -> pd.Series:
    """EPS SUE score minus its own EWM (span=252)."""
    base = _sue_naive(eps)
    return base - _ewm_mean(base, _TD_YEAR)


def gds_drv2_064_gp_sue_ewm_diff(gp: pd.Series) -> pd.Series:
    """Gross profit SUE score minus its own EWM."""
    base = _sue_naive(gp)
    return base - _ewm_mean(base, _TD_YEAR)


def gds_drv2_065_opinc_sue_ewm_diff(opinc: pd.Series) -> pd.Series:
    """Operating income SUE score minus its own EWM."""
    base = _sue_naive(opinc)
    return base - _ewm_mean(base, _TD_YEAR)


def gds_drv2_066_rev_miss_slope_4q(revenue: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the revenue naive-miss series (miss trend)."""
    m = _naive_miss(revenue)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv2_067_eps_miss_slope_4q(eps: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the EPS naive-miss series."""
    m = _naive_miss(eps)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv2_068_gp_miss_slope_4q(gp: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the gross profit naive-miss series."""
    m = _naive_miss(gp)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv2_069_netinc_miss_2q_diff(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss change over 2 quarters (half-year deterioration)."""
    base = _naive_miss(netinc)
    return base - base.shift(_TD_2Q)


def gds_drv2_070_rev_miss_2q_diff(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss change over 2 quarters."""
    base = _naive_miss(revenue)
    return base - base.shift(_TD_2Q)


def gds_drv2_071_eps_miss_2q_diff(eps: pd.Series) -> pd.Series:
    """EPS naive-miss change over 2 quarters."""
    base = _naive_miss(eps)
    return base - base.shift(_TD_2Q)


def gds_drv2_072_composite_sue_accel_9m(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                         gp: pd.Series, opinc: pd.Series) -> pd.Series:
    """Composite 2nd-deriv: QoQ change in 5-metric equal-weighted SUE score."""
    composite = (_sue_naive(revenue) + _sue_naive(netinc) + _sue_naive(eps)
                 + _sue_naive(gp) + _sue_naive(opinc)) / 5.0
    return composite - composite.shift(_TD_QTR)


def gds_drv2_073_netinc_miss_yoy_pct(netinc: pd.Series) -> pd.Series:
    """YoY percent change in net income naive-miss series."""
    base = _naive_miss(netinc)
    return _safe_div_abs(base - base.shift(_TD_YEAR), base.shift(_TD_YEAR))


def gds_drv2_074_fcf_miss_slope_4q(fcf: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the FCF naive-miss series."""
    m = _naive_miss(fcf)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv2_075_ncfo_miss_slope_4q(ncfo: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the operating CF naive-miss series."""
    m = _naive_miss(ncfo)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

GUIDANCE_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "gds_drv2_001_rev_naive_miss_qoq_diff":         {"inputs": ["revenue"],               "func": gds_drv2_001_rev_naive_miss_qoq_diff},
    "gds_drv2_002_netinc_naive_miss_qoq_diff":      {"inputs": ["netinc"],                "func": gds_drv2_002_netinc_naive_miss_qoq_diff},
    "gds_drv2_003_eps_naive_miss_qoq_diff":         {"inputs": ["eps"],                   "func": gds_drv2_003_eps_naive_miss_qoq_diff},
    "gds_drv2_004_rev_naive_miss_yoy_diff":         {"inputs": ["revenue"],               "func": gds_drv2_004_rev_naive_miss_yoy_diff},
    "gds_drv2_005_netinc_naive_miss_yoy_diff":      {"inputs": ["netinc"],                "func": gds_drv2_005_netinc_naive_miss_yoy_diff},
    "gds_drv2_006_eps_sue_qoq_diff":                {"inputs": ["eps"],                   "func": gds_drv2_006_eps_sue_qoq_diff},
    "gds_drv2_007_netinc_sue_qoq_diff":             {"inputs": ["netinc"],                "func": gds_drv2_007_netinc_sue_qoq_diff},
    "gds_drv2_008_rev_sue_qoq_diff":                {"inputs": ["revenue"],               "func": gds_drv2_008_rev_sue_qoq_diff},
    "gds_drv2_009_netinc_miss_zscore_qoq_diff":     {"inputs": ["netinc"],                "func": gds_drv2_009_netinc_miss_zscore_qoq_diff},
    "gds_drv2_010_rev_miss_zscore_yoy_diff":        {"inputs": ["revenue"],               "func": gds_drv2_010_rev_miss_zscore_yoy_diff},
    "gds_drv2_011_netinc_ewm_miss_qoq_diff":        {"inputs": ["netinc"],                "func": gds_drv2_011_netinc_ewm_miss_qoq_diff},
    "gds_drv2_012_rev_ewm_miss_qoq_diff":           {"inputs": ["revenue"],               "func": gds_drv2_012_rev_ewm_miss_qoq_diff},
    "gds_drv2_013_eps_seasonal_miss_qoq_diff":      {"inputs": ["eps"],                   "func": gds_drv2_013_eps_seasonal_miss_qoq_diff},
    "gds_drv2_014_netinc_seasonal_miss_yoy_diff":   {"inputs": ["netinc"],                "func": gds_drv2_014_netinc_seasonal_miss_yoy_diff},
    "gds_drv2_015_rev_trail_avg_miss_qoq_diff":     {"inputs": ["revenue"],               "func": gds_drv2_015_rev_trail_avg_miss_qoq_diff},
    "gds_drv2_016_netinc_miss_worst_4q_qoq_diff":   {"inputs": ["netinc"],                "func": gds_drv2_016_netinc_miss_worst_4q_qoq_diff},
    "gds_drv2_017_rev_miss_worst_4q_qoq_diff":      {"inputs": ["revenue"],               "func": gds_drv2_017_rev_miss_worst_4q_qoq_diff},
    "gds_drv2_018_netinc_naive_miss_pct_qoq":       {"inputs": ["netinc"],                "func": gds_drv2_018_netinc_naive_miss_pct_qoq},
    "gds_drv2_019_eps_sue_yoy_diff":                {"inputs": ["eps"],                   "func": gds_drv2_019_eps_sue_yoy_diff},
    "gds_drv2_020_netinc_miss_slope_of_slope":      {"inputs": ["netinc"],                "func": gds_drv2_020_netinc_miss_slope_of_slope},
    "gds_drv2_021_gp_naive_miss_qoq_diff":          {"inputs": ["gp"],                    "func": gds_drv2_021_gp_naive_miss_qoq_diff},
    "gds_drv2_022_ebitda_naive_miss_qoq_diff":      {"inputs": ["ebitda"],                "func": gds_drv2_022_ebitda_naive_miss_qoq_diff},
    "gds_drv2_023_fcf_naive_miss_qoq_diff":         {"inputs": ["fcf"],                   "func": gds_drv2_023_fcf_naive_miss_qoq_diff},
    "gds_drv2_024_netinc_sue_ewm_diff":             {"inputs": ["netinc"],                "func": gds_drv2_024_netinc_sue_ewm_diff},
    "gds_drv2_025_composite_miss_accel":            {"inputs": ["revenue", "netinc", "eps"], "func": gds_drv2_025_composite_miss_accel},
    "gds_drv2_026_gp_naive_miss_yoy_diff":          {"inputs": ["gp"],                    "func": gds_drv2_026_gp_naive_miss_yoy_diff},
    "gds_drv2_027_ebitda_naive_miss_yoy_diff":      {"inputs": ["ebitda"],                "func": gds_drv2_027_ebitda_naive_miss_yoy_diff},
    "gds_drv2_028_fcf_naive_miss_yoy_diff":         {"inputs": ["fcf"],                   "func": gds_drv2_028_fcf_naive_miss_yoy_diff},
    "gds_drv2_029_ncfo_naive_miss_qoq_diff":        {"inputs": ["ncfo"],                  "func": gds_drv2_029_ncfo_naive_miss_qoq_diff},
    "gds_drv2_030_ncfo_naive_miss_yoy_diff":        {"inputs": ["ncfo"],                  "func": gds_drv2_030_ncfo_naive_miss_yoy_diff},
    "gds_drv2_031_epsdil_naive_miss_qoq_diff":      {"inputs": ["epsdil"],                "func": gds_drv2_031_epsdil_naive_miss_qoq_diff},
    "gds_drv2_032_epsdil_naive_miss_yoy_diff":      {"inputs": ["epsdil"],                "func": gds_drv2_032_epsdil_naive_miss_yoy_diff},
    "gds_drv2_033_opinc_naive_miss_qoq_diff":       {"inputs": ["opinc"],                 "func": gds_drv2_033_opinc_naive_miss_qoq_diff},
    "gds_drv2_034_opinc_naive_miss_yoy_diff":       {"inputs": ["opinc"],                 "func": gds_drv2_034_opinc_naive_miss_yoy_diff},
    "gds_drv2_035_rev_seasonal_miss_yoy_diff":      {"inputs": ["revenue"],               "func": gds_drv2_035_rev_seasonal_miss_yoy_diff},
    "gds_drv2_036_netinc_seasonal_miss_qoq_diff":   {"inputs": ["netinc"],                "func": gds_drv2_036_netinc_seasonal_miss_qoq_diff},
    "gds_drv2_037_eps_seasonal_miss_yoy_diff":      {"inputs": ["eps"],                   "func": gds_drv2_037_eps_seasonal_miss_yoy_diff},
    "gds_drv2_038_gp_sue_qoq_diff":                 {"inputs": ["gp"],                    "func": gds_drv2_038_gp_sue_qoq_diff},
    "gds_drv2_039_ebitda_sue_qoq_diff":             {"inputs": ["ebitda"],                "func": gds_drv2_039_ebitda_sue_qoq_diff},
    "gds_drv2_040_fcf_sue_qoq_diff":                {"inputs": ["fcf"],                   "func": gds_drv2_040_fcf_sue_qoq_diff},
    "gds_drv2_041_ncfo_sue_qoq_diff":               {"inputs": ["ncfo"],                  "func": gds_drv2_041_ncfo_sue_qoq_diff},
    "gds_drv2_042_opinc_sue_qoq_diff":              {"inputs": ["opinc"],                 "func": gds_drv2_042_opinc_sue_qoq_diff},
    "gds_drv2_043_epsdil_sue_qoq_diff":             {"inputs": ["epsdil"],                "func": gds_drv2_043_epsdil_sue_qoq_diff},
    "gds_drv2_044_eps_miss_zscore_yoy_diff":        {"inputs": ["eps"],                   "func": gds_drv2_044_eps_miss_zscore_yoy_diff},
    "gds_drv2_045_gp_miss_zscore_qoq_diff":         {"inputs": ["gp"],                    "func": gds_drv2_045_gp_miss_zscore_qoq_diff},
    "gds_drv2_046_ebitda_miss_zscore_qoq_diff":     {"inputs": ["ebitda"],                "func": gds_drv2_046_ebitda_miss_zscore_qoq_diff},
    "gds_drv2_047_fcf_ewm_miss_qoq_diff":           {"inputs": ["fcf"],                   "func": gds_drv2_047_fcf_ewm_miss_qoq_diff},
    "gds_drv2_048_ncfo_ewm_miss_qoq_diff":          {"inputs": ["ncfo"],                  "func": gds_drv2_048_ncfo_ewm_miss_qoq_diff},
    "gds_drv2_049_opinc_ewm_miss_qoq_diff":         {"inputs": ["opinc"],                 "func": gds_drv2_049_opinc_ewm_miss_qoq_diff},
    "gds_drv2_050_epsdil_ewm_miss_qoq_diff":        {"inputs": ["epsdil"],                "func": gds_drv2_050_epsdil_ewm_miss_qoq_diff},
    "gds_drv2_051_rev_miss_worst_4q_yoy_diff":      {"inputs": ["revenue"],               "func": gds_drv2_051_rev_miss_worst_4q_yoy_diff},
    "gds_drv2_052_netinc_miss_worst_4q_yoy_diff":   {"inputs": ["netinc"],                "func": gds_drv2_052_netinc_miss_worst_4q_yoy_diff},
    "gds_drv2_053_eps_miss_worst_4q_qoq_diff":      {"inputs": ["eps"],                   "func": gds_drv2_053_eps_miss_worst_4q_qoq_diff},
    "gds_drv2_054_gp_miss_worst_4q_qoq_diff":       {"inputs": ["gp"],                    "func": gds_drv2_054_gp_miss_worst_4q_qoq_diff},
    "gds_drv2_055_ebitda_miss_worst_4q_qoq_diff":   {"inputs": ["ebitda"],                "func": gds_drv2_055_ebitda_miss_worst_4q_qoq_diff},
    "gds_drv2_056_fcf_miss_worst_4q_qoq_diff":      {"inputs": ["fcf"],                   "func": gds_drv2_056_fcf_miss_worst_4q_qoq_diff},
    "gds_drv2_057_rev_trail_avg_miss_yoy_diff":     {"inputs": ["revenue"],               "func": gds_drv2_057_rev_trail_avg_miss_yoy_diff},
    "gds_drv2_058_netinc_trail_avg_miss_qoq_diff":  {"inputs": ["netinc"],                "func": gds_drv2_058_netinc_trail_avg_miss_qoq_diff},
    "gds_drv2_059_eps_trail_avg_miss_qoq_diff":     {"inputs": ["eps"],                   "func": gds_drv2_059_eps_trail_avg_miss_qoq_diff},
    "gds_drv2_060_rev_naive_miss_pct_yoy":          {"inputs": ["revenue"],               "func": gds_drv2_060_rev_naive_miss_pct_yoy},
    "gds_drv2_061_eps_naive_miss_pct_qoq":          {"inputs": ["eps"],                   "func": gds_drv2_061_eps_naive_miss_pct_qoq},
    "gds_drv2_062_rev_sue_ewm_diff":                {"inputs": ["revenue"],               "func": gds_drv2_062_rev_sue_ewm_diff},
    "gds_drv2_063_eps_sue_ewm_diff":                {"inputs": ["eps"],                   "func": gds_drv2_063_eps_sue_ewm_diff},
    "gds_drv2_064_gp_sue_ewm_diff":                 {"inputs": ["gp"],                    "func": gds_drv2_064_gp_sue_ewm_diff},
    "gds_drv2_065_opinc_sue_ewm_diff":              {"inputs": ["opinc"],                 "func": gds_drv2_065_opinc_sue_ewm_diff},
    "gds_drv2_066_rev_miss_slope_4q":               {"inputs": ["revenue"],               "func": gds_drv2_066_rev_miss_slope_4q},
    "gds_drv2_067_eps_miss_slope_4q":               {"inputs": ["eps"],                   "func": gds_drv2_067_eps_miss_slope_4q},
    "gds_drv2_068_gp_miss_slope_4q":                {"inputs": ["gp"],                    "func": gds_drv2_068_gp_miss_slope_4q},
    "gds_drv2_069_netinc_miss_2q_diff":             {"inputs": ["netinc"],                "func": gds_drv2_069_netinc_miss_2q_diff},
    "gds_drv2_070_rev_miss_2q_diff":                {"inputs": ["revenue"],               "func": gds_drv2_070_rev_miss_2q_diff},
    "gds_drv2_071_eps_miss_2q_diff":                {"inputs": ["eps"],                   "func": gds_drv2_071_eps_miss_2q_diff},
    "gds_drv2_072_composite_sue_accel_9m":          {"inputs": ["revenue", "netinc", "eps", "gp", "opinc"], "func": gds_drv2_072_composite_sue_accel_9m},
    "gds_drv2_073_netinc_miss_yoy_pct":             {"inputs": ["netinc"],                "func": gds_drv2_073_netinc_miss_yoy_pct},
    "gds_drv2_074_fcf_miss_slope_4q":               {"inputs": ["fcf"],                   "func": gds_drv2_074_fcf_miss_slope_4q},
    "gds_drv2_075_ncfo_miss_slope_4q":              {"inputs": ["ncfo"],                  "func": gds_drv2_075_ncfo_miss_slope_4q},
}
