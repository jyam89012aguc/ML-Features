"""
75_guidance_distress — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative guidance-distress features
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
The 3rd-derivative series are sparse/stepwise on a daily index because the
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


# ── Base and 2nd-derivative concept helpers ──────────────────────────────────

def _naive_miss(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_QTR)


def _seasonal_miss(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_YEAR)


def _sue_naive(s: pd.Series) -> pd.Series:
    m = _naive_miss(s)
    vol = _rolling_std(s, _TD_YEAR)
    return _safe_div(m, vol)


def _miss_zscore_4q(s: pd.Series) -> pd.Series:
    m = _naive_miss(s)
    return _safe_div(m - _rolling_mean(m, _TD_YEAR), _rolling_std(m, _TD_YEAR))


def _ewm_miss(s: pd.Series) -> pd.Series:
    ewm_exp = _ewm_mean(s, _TD_YEAR).shift(_TD_QTR)
    return s - ewm_exp


def _miss_worst_4q(s: pd.Series) -> pd.Series:
    return _rolling_min(_naive_miss(s), _TD_YEAR)


# 2nd-derivative intermediates (QoQ diff of base miss concepts)

def _d2_naive_miss(s: pd.Series) -> pd.Series:
    base = _naive_miss(s)
    return base - base.shift(_TD_QTR)


def _d2_sue(s: pd.Series) -> pd.Series:
    base = _sue_naive(s)
    return base - base.shift(_TD_QTR)


def _d2_miss_zscore(s: pd.Series) -> pd.Series:
    base = _miss_zscore_4q(s)
    return base - base.shift(_TD_QTR)


def _d2_ewm_miss(s: pd.Series) -> pd.Series:
    base = _ewm_miss(s)
    return base - base.shift(_TD_QTR)


def _d2_miss_worst_4q(s: pd.Series) -> pd.Series:
    base = _miss_worst_4q(s)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def gds_drv3_001_rev_naive_miss_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue naive-miss: QoQ change of (QoQ change of miss)."""
    d2 = _d2_naive_miss(revenue)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_002_netinc_naive_miss_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income naive-miss."""
    d2 = _d2_naive_miss(netinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_003_eps_naive_miss_3rd_diff(eps: pd.Series) -> pd.Series:
    """3rd diff of EPS naive-miss."""
    d2 = _d2_naive_miss(eps)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_004_rev_sue_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue SUE-style score."""
    d2 = _d2_sue(revenue)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_005_netinc_sue_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income SUE-style score."""
    d2 = _d2_sue(netinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_006_eps_sue_3rd_diff(eps: pd.Series) -> pd.Series:
    """3rd diff of EPS SUE-style score."""
    d2 = _d2_sue(eps)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_007_netinc_miss_zscore_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income miss z-score."""
    d2 = _d2_miss_zscore(netinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_008_rev_miss_zscore_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue miss z-score."""
    d2 = _d2_miss_zscore(revenue)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_009_netinc_ewm_miss_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income EWM-miss."""
    d2 = _d2_ewm_miss(netinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_010_rev_ewm_miss_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue EWM-miss."""
    d2 = _d2_ewm_miss(revenue)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_011_netinc_miss_worst_4q_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income worst-4Q miss (deepening-trough jerk)."""
    d2 = _d2_miss_worst_4q(netinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_012_rev_miss_worst_4q_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue worst-4Q miss."""
    d2 = _d2_miss_worst_4q(revenue)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_013_netinc_miss_3rd_yoy_diff(netinc: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative (QoQ miss change) of net income naive-miss."""
    d2 = _d2_naive_miss(netinc)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_014_rev_miss_3rd_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative of revenue naive-miss."""
    d2 = _d2_naive_miss(revenue)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_015_eps_miss_3rd_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in the 2nd-derivative of EPS naive-miss."""
    d2 = _d2_naive_miss(eps)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_016_netinc_sue_slope_of_d2(netinc: pd.Series) -> pd.Series:
    """
    Rolling 4Q OLS slope of the 2nd-derivative (QoQ-change-of-SUE) series.
    Captures trend in the acceleration of net income standardized misses.
    """
    d2 = _d2_sue(netinc)

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

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv3_017_gp_naive_miss_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff of gross profit naive-miss."""
    d2 = _d2_naive_miss(gp)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_018_ebitda_naive_miss_3rd_diff(ebitda: pd.Series) -> pd.Series:
    """3rd diff of EBITDA naive-miss."""
    d2 = _d2_naive_miss(ebitda)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_019_fcf_naive_miss_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd diff of FCF naive-miss."""
    d2 = _d2_naive_miss(fcf)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_020_ncfo_naive_miss_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd diff of operating cash flow naive-miss."""
    d2 = _d2_naive_miss(ncfo)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_021_rev_seasonal_miss_3rd_diff(revenue: pd.Series) -> pd.Series:
    """3rd diff of revenue seasonal-naive miss."""
    base = _seasonal_miss(revenue)
    d2   = (base - base.shift(_TD_QTR))
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_022_netinc_seasonal_miss_3rd_diff(netinc: pd.Series) -> pd.Series:
    """3rd diff of net income seasonal-naive miss."""
    base = _seasonal_miss(netinc)
    d2   = (base - base.shift(_TD_QTR))
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_023_eps_sue_ewm_dev_d2(eps: pd.Series) -> pd.Series:
    """
    2nd-derivative EPS SUE minus its own EWM (span=252):
    whether the current acceleration of miss is worse than its own trend.
    """
    d2  = _d2_sue(eps)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_024_netinc_sue_d2_ewm_dev(netinc: pd.Series) -> pd.Series:
    """
    2nd-derivative net income SUE minus its own EWM:
    whether the current miss-acceleration is anomalous relative to recent trend.
    """
    d2  = _d2_sue(netinc)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_025_composite_miss_3rd_diff(revenue: pd.Series, netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """
    Composite 3rd-derivative: QoQ change in the average 2nd-derivative SUE
    for revenue, net income, and EPS.  Captures jerk in broadening miss dynamics.
    """
    d2_composite = (_d2_sue(revenue) + _d2_sue(netinc) + _d2_sue(eps)) / 3.0
    return d2_composite - d2_composite.shift(_TD_QTR)


# ── 3rd-derivative feature functions 026-075 ─────────────────────────────────

def gds_drv3_026_gp_naive_miss_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff (QoQ jerk) of gross profit naive-miss."""
    d2 = _d2_naive_miss(gp)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_027_fcf_naive_miss_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd diff of FCF naive-miss."""
    d2 = _d2_naive_miss(fcf)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_028_ncfo_naive_miss_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd diff of operating CF naive-miss."""
    d2 = _d2_naive_miss(ncfo)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_029_opinc_naive_miss_3rd_diff(opinc: pd.Series) -> pd.Series:
    """3rd diff of operating income naive-miss."""
    d2 = _d2_naive_miss(opinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_030_epsdil_naive_miss_3rd_diff(epsdil: pd.Series) -> pd.Series:
    """3rd diff of diluted EPS naive-miss."""
    d2 = _d2_naive_miss(epsdil)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_031_gp_sue_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff of gross profit SUE-style score."""
    d2 = _d2_sue(gp)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_032_ebitda_sue_3rd_diff(ebitda: pd.Series) -> pd.Series:
    """3rd diff of EBITDA SUE-style score."""
    d2 = _d2_sue(ebitda)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_033_fcf_sue_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd diff of FCF SUE-style score."""
    d2 = _d2_sue(fcf)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_034_ncfo_sue_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd diff of operating CF SUE-style score."""
    d2 = _d2_sue(ncfo)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_035_opinc_sue_3rd_diff(opinc: pd.Series) -> pd.Series:
    """3rd diff of operating income SUE-style score."""
    d2 = _d2_sue(opinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_036_epsdil_sue_3rd_diff(epsdil: pd.Series) -> pd.Series:
    """3rd diff of diluted EPS SUE-style score."""
    d2 = _d2_sue(epsdil)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_037_gp_miss_zscore_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff of gross profit miss z-score."""
    d2 = _d2_miss_zscore(gp)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_038_ebitda_miss_zscore_3rd_diff(ebitda: pd.Series) -> pd.Series:
    """3rd diff of EBITDA miss z-score."""
    d2 = _d2_miss_zscore(ebitda)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_039_fcf_ewm_miss_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd diff of FCF EWM-miss."""
    d2 = _d2_ewm_miss(fcf)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_040_ncfo_ewm_miss_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd diff of operating CF EWM-miss."""
    d2 = _d2_ewm_miss(ncfo)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_041_opinc_ewm_miss_3rd_diff(opinc: pd.Series) -> pd.Series:
    """3rd diff of operating income EWM-miss."""
    d2 = _d2_ewm_miss(opinc)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_042_eps_miss_worst_4q_3rd_diff(eps: pd.Series) -> pd.Series:
    """3rd diff of EPS worst-4Q miss (trough-deepening jerk)."""
    d2 = _d2_miss_worst_4q(eps)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_043_gp_miss_worst_4q_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff of gross profit worst-4Q miss."""
    d2 = _d2_miss_worst_4q(gp)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_044_ebitda_miss_worst_4q_3rd_diff(ebitda: pd.Series) -> pd.Series:
    """3rd diff of EBITDA worst-4Q miss."""
    d2 = _d2_miss_worst_4q(ebitda)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_045_rev_naive_miss_3rd_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of revenue naive-miss (long-horizon jerk)."""
    d2 = _d2_naive_miss(revenue)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_046_gp_naive_miss_3rd_yoy_diff(gp: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of gross profit naive-miss."""
    d2 = _d2_naive_miss(gp)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_047_ebitda_naive_miss_3rd_yoy_diff(ebitda: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of EBITDA naive-miss."""
    d2 = _d2_naive_miss(ebitda)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_048_fcf_naive_miss_3rd_yoy_diff(fcf: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of FCF naive-miss."""
    d2 = _d2_naive_miss(fcf)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_049_ncfo_naive_miss_3rd_yoy_diff(ncfo: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of operating CF naive-miss."""
    d2 = _d2_naive_miss(ncfo)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_050_opinc_naive_miss_3rd_yoy_diff(opinc: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative of operating income naive-miss."""
    d2 = _d2_naive_miss(opinc)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_051_rev_sue_slope_of_d2(revenue: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the 2nd-derivative (QoQ-SUE-change) of revenue."""
    d2 = _d2_sue(revenue)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv3_052_eps_sue_slope_of_d2(eps: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the 2nd-derivative (QoQ-SUE-change) of EPS."""
    d2 = _d2_sue(eps)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv3_053_gp_sue_slope_of_d2(gp: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the 2nd-derivative (QoQ-SUE-change) of gross profit."""
    d2 = _d2_sue(gp)

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        d = ((x - xm) ** 2).sum()
        return np.nan if d == 0 else ((x - xm) * (arr - ym)).sum() / d

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv3_054_gp_seasonal_miss_3rd_diff(gp: pd.Series) -> pd.Series:
    """3rd diff of gross profit seasonal-naive miss."""
    base = _seasonal_miss(gp)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_055_fcf_seasonal_miss_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd diff of FCF seasonal-naive miss."""
    base = _seasonal_miss(fcf)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_056_ncfo_seasonal_miss_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd diff of operating CF seasonal-naive miss."""
    base = _seasonal_miss(ncfo)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_057_ebitda_seasonal_miss_3rd_diff(ebitda: pd.Series) -> pd.Series:
    """3rd diff of EBITDA seasonal-naive miss."""
    base = _seasonal_miss(ebitda)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def gds_drv3_058_rev_sue_ewm_dev_d2(revenue: pd.Series) -> pd.Series:
    """2nd-deriv revenue SUE minus its own EWM: anomalous acceleration vs trend."""
    d2  = _d2_sue(revenue)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_059_gp_sue_d2_ewm_dev(gp: pd.Series) -> pd.Series:
    """2nd-deriv gross profit SUE minus its own EWM."""
    d2  = _d2_sue(gp)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_060_ebitda_sue_d2_ewm_dev(ebitda: pd.Series) -> pd.Series:
    """2nd-deriv EBITDA SUE minus its own EWM."""
    d2  = _d2_sue(ebitda)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_061_fcf_sue_d2_ewm_dev(fcf: pd.Series) -> pd.Series:
    """2nd-deriv FCF SUE minus its own EWM."""
    d2  = _d2_sue(fcf)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_062_ncfo_sue_d2_ewm_dev(ncfo: pd.Series) -> pd.Series:
    """2nd-deriv operating CF SUE minus its own EWM."""
    d2  = _d2_sue(ncfo)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_063_opinc_sue_d2_ewm_dev(opinc: pd.Series) -> pd.Series:
    """2nd-deriv operating income SUE minus its own EWM."""
    d2  = _d2_sue(opinc)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_064_epsdil_sue_d2_ewm_dev(epsdil: pd.Series) -> pd.Series:
    """2nd-deriv diluted EPS SUE minus its own EWM."""
    d2  = _d2_sue(epsdil)
    ewm = _ewm_mean(d2, _TD_YEAR)
    return d2 - ewm


def gds_drv3_065_rev_d2_miss_3rd_2q_diff(revenue: pd.Series) -> pd.Series:
    """2Q (half-year) change in 2nd-derivative of revenue naive-miss."""
    d2 = _d2_naive_miss(revenue)
    return d2 - d2.shift(_TD_2Q)


def gds_drv3_066_netinc_d2_miss_3rd_2q_diff(netinc: pd.Series) -> pd.Series:
    """2Q change in 2nd-derivative of net income naive-miss."""
    d2 = _d2_naive_miss(netinc)
    return d2 - d2.shift(_TD_2Q)


def gds_drv3_067_eps_d2_miss_3rd_2q_diff(eps: pd.Series) -> pd.Series:
    """2Q change in 2nd-derivative of EPS naive-miss."""
    d2 = _d2_naive_miss(eps)
    return d2 - d2.shift(_TD_2Q)


def gds_drv3_068_gp_d2_miss_3rd_2q_diff(gp: pd.Series) -> pd.Series:
    """2Q change in 2nd-derivative of gross profit naive-miss."""
    d2 = _d2_naive_miss(gp)
    return d2 - d2.shift(_TD_2Q)


def gds_drv3_069_ebitda_d2_sue_3rd_yoy_diff(ebitda: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative EBITDA SUE (long-horizon miss-acceleration shift)."""
    d2 = _d2_sue(ebitda)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_070_fcf_d2_sue_3rd_yoy_diff(fcf: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative FCF SUE."""
    d2 = _d2_sue(fcf)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_071_ncfo_d2_sue_3rd_yoy_diff(ncfo: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative operating CF SUE."""
    d2 = _d2_sue(ncfo)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_072_rev_d2_sue_3rd_yoy_diff(revenue: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative revenue SUE."""
    d2 = _d2_sue(revenue)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_073_eps_d2_sue_3rd_yoy_diff(eps: pd.Series) -> pd.Series:
    """YoY change in 2nd-derivative EPS SUE."""
    d2 = _d2_sue(eps)
    return d2 - d2.shift(_TD_YEAR)


def gds_drv3_074_composite_d2_sue_slope(revenue: pd.Series, netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """Rolling 4Q OLS slope of the composite 2nd-derivative (rev+ni+eps) SUE."""
    d2 = (_d2_sue(revenue) + _d2_sue(netinc) + _d2_sue(eps)) / 3.0

    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm, ym = x.mean(), arr.mean()
        denom = ((x - xm) ** 2).sum()
        return np.nan if denom == 0 else ((x - xm) * (arr - ym)).sum() / denom

    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_drv3_075_composite_miss_jerk_5m(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                         gp: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Composite 3rd-deriv: QoQ change in 5-metric average 2nd-derivative SUE."""
    d2 = (_d2_sue(revenue) + _d2_sue(netinc) + _d2_sue(eps)
          + _d2_sue(gp) + _d2_sue(ebitda)) / 5.0
    return d2 - d2.shift(_TD_QTR)


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

GUIDANCE_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "gds_drv3_001_rev_naive_miss_3rd_diff":        {"inputs": ["revenue"],               "func": gds_drv3_001_rev_naive_miss_3rd_diff},
    "gds_drv3_002_netinc_naive_miss_3rd_diff":     {"inputs": ["netinc"],                "func": gds_drv3_002_netinc_naive_miss_3rd_diff},
    "gds_drv3_003_eps_naive_miss_3rd_diff":        {"inputs": ["eps"],                   "func": gds_drv3_003_eps_naive_miss_3rd_diff},
    "gds_drv3_004_rev_sue_3rd_diff":               {"inputs": ["revenue"],               "func": gds_drv3_004_rev_sue_3rd_diff},
    "gds_drv3_005_netinc_sue_3rd_diff":            {"inputs": ["netinc"],                "func": gds_drv3_005_netinc_sue_3rd_diff},
    "gds_drv3_006_eps_sue_3rd_diff":               {"inputs": ["eps"],                   "func": gds_drv3_006_eps_sue_3rd_diff},
    "gds_drv3_007_netinc_miss_zscore_3rd_diff":    {"inputs": ["netinc"],                "func": gds_drv3_007_netinc_miss_zscore_3rd_diff},
    "gds_drv3_008_rev_miss_zscore_3rd_diff":       {"inputs": ["revenue"],               "func": gds_drv3_008_rev_miss_zscore_3rd_diff},
    "gds_drv3_009_netinc_ewm_miss_3rd_diff":       {"inputs": ["netinc"],                "func": gds_drv3_009_netinc_ewm_miss_3rd_diff},
    "gds_drv3_010_rev_ewm_miss_3rd_diff":          {"inputs": ["revenue"],               "func": gds_drv3_010_rev_ewm_miss_3rd_diff},
    "gds_drv3_011_netinc_miss_worst_4q_3rd_diff":  {"inputs": ["netinc"],                "func": gds_drv3_011_netinc_miss_worst_4q_3rd_diff},
    "gds_drv3_012_rev_miss_worst_4q_3rd_diff":     {"inputs": ["revenue"],               "func": gds_drv3_012_rev_miss_worst_4q_3rd_diff},
    "gds_drv3_013_netinc_miss_3rd_yoy_diff":       {"inputs": ["netinc"],                "func": gds_drv3_013_netinc_miss_3rd_yoy_diff},
    "gds_drv3_014_rev_miss_3rd_yoy_diff":          {"inputs": ["revenue"],               "func": gds_drv3_014_rev_miss_3rd_yoy_diff},
    "gds_drv3_015_eps_miss_3rd_yoy_diff":          {"inputs": ["eps"],                   "func": gds_drv3_015_eps_miss_3rd_yoy_diff},
    "gds_drv3_016_netinc_sue_slope_of_d2":         {"inputs": ["netinc"],                "func": gds_drv3_016_netinc_sue_slope_of_d2},
    "gds_drv3_017_gp_naive_miss_3rd_diff":         {"inputs": ["gp"],                    "func": gds_drv3_017_gp_naive_miss_3rd_diff},
    "gds_drv3_018_ebitda_naive_miss_3rd_diff":     {"inputs": ["ebitda"],                "func": gds_drv3_018_ebitda_naive_miss_3rd_diff},
    "gds_drv3_019_fcf_naive_miss_3rd_diff":        {"inputs": ["fcf"],                   "func": gds_drv3_019_fcf_naive_miss_3rd_diff},
    "gds_drv3_020_ncfo_naive_miss_3rd_diff":       {"inputs": ["ncfo"],                  "func": gds_drv3_020_ncfo_naive_miss_3rd_diff},
    "gds_drv3_021_rev_seasonal_miss_3rd_diff":     {"inputs": ["revenue"],               "func": gds_drv3_021_rev_seasonal_miss_3rd_diff},
    "gds_drv3_022_netinc_seasonal_miss_3rd_diff":  {"inputs": ["netinc"],                "func": gds_drv3_022_netinc_seasonal_miss_3rd_diff},
    "gds_drv3_023_eps_sue_ewm_dev_d2":             {"inputs": ["eps"],                   "func": gds_drv3_023_eps_sue_ewm_dev_d2},
    "gds_drv3_024_netinc_sue_d2_ewm_dev":          {"inputs": ["netinc"],                "func": gds_drv3_024_netinc_sue_d2_ewm_dev},
    "gds_drv3_025_composite_miss_3rd_diff":        {"inputs": ["revenue", "netinc", "eps"], "func": gds_drv3_025_composite_miss_3rd_diff},
    "gds_drv3_026_gp_naive_miss_3rd_diff":         {"inputs": ["gp"],                    "func": gds_drv3_026_gp_naive_miss_3rd_diff},
    "gds_drv3_027_fcf_naive_miss_3rd_diff":        {"inputs": ["fcf"],                   "func": gds_drv3_027_fcf_naive_miss_3rd_diff},
    "gds_drv3_028_ncfo_naive_miss_3rd_diff":       {"inputs": ["ncfo"],                  "func": gds_drv3_028_ncfo_naive_miss_3rd_diff},
    "gds_drv3_029_opinc_naive_miss_3rd_diff":      {"inputs": ["opinc"],                 "func": gds_drv3_029_opinc_naive_miss_3rd_diff},
    "gds_drv3_030_epsdil_naive_miss_3rd_diff":     {"inputs": ["epsdil"],                "func": gds_drv3_030_epsdil_naive_miss_3rd_diff},
    "gds_drv3_031_gp_sue_3rd_diff":                {"inputs": ["gp"],                    "func": gds_drv3_031_gp_sue_3rd_diff},
    "gds_drv3_032_ebitda_sue_3rd_diff":            {"inputs": ["ebitda"],                "func": gds_drv3_032_ebitda_sue_3rd_diff},
    "gds_drv3_033_fcf_sue_3rd_diff":               {"inputs": ["fcf"],                   "func": gds_drv3_033_fcf_sue_3rd_diff},
    "gds_drv3_034_ncfo_sue_3rd_diff":              {"inputs": ["ncfo"],                  "func": gds_drv3_034_ncfo_sue_3rd_diff},
    "gds_drv3_035_opinc_sue_3rd_diff":             {"inputs": ["opinc"],                 "func": gds_drv3_035_opinc_sue_3rd_diff},
    "gds_drv3_036_epsdil_sue_3rd_diff":            {"inputs": ["epsdil"],                "func": gds_drv3_036_epsdil_sue_3rd_diff},
    "gds_drv3_037_gp_miss_zscore_3rd_diff":        {"inputs": ["gp"],                    "func": gds_drv3_037_gp_miss_zscore_3rd_diff},
    "gds_drv3_038_ebitda_miss_zscore_3rd_diff":    {"inputs": ["ebitda"],                "func": gds_drv3_038_ebitda_miss_zscore_3rd_diff},
    "gds_drv3_039_fcf_ewm_miss_3rd_diff":          {"inputs": ["fcf"],                   "func": gds_drv3_039_fcf_ewm_miss_3rd_diff},
    "gds_drv3_040_ncfo_ewm_miss_3rd_diff":         {"inputs": ["ncfo"],                  "func": gds_drv3_040_ncfo_ewm_miss_3rd_diff},
    "gds_drv3_041_opinc_ewm_miss_3rd_diff":        {"inputs": ["opinc"],                 "func": gds_drv3_041_opinc_ewm_miss_3rd_diff},
    "gds_drv3_042_eps_miss_worst_4q_3rd_diff":     {"inputs": ["eps"],                   "func": gds_drv3_042_eps_miss_worst_4q_3rd_diff},
    "gds_drv3_043_gp_miss_worst_4q_3rd_diff":      {"inputs": ["gp"],                    "func": gds_drv3_043_gp_miss_worst_4q_3rd_diff},
    "gds_drv3_044_ebitda_miss_worst_4q_3rd_diff":  {"inputs": ["ebitda"],                "func": gds_drv3_044_ebitda_miss_worst_4q_3rd_diff},
    "gds_drv3_045_rev_naive_miss_3rd_yoy_diff":    {"inputs": ["revenue"],               "func": gds_drv3_045_rev_naive_miss_3rd_yoy_diff},
    "gds_drv3_046_gp_naive_miss_3rd_yoy_diff":     {"inputs": ["gp"],                    "func": gds_drv3_046_gp_naive_miss_3rd_yoy_diff},
    "gds_drv3_047_ebitda_naive_miss_3rd_yoy_diff": {"inputs": ["ebitda"],                "func": gds_drv3_047_ebitda_naive_miss_3rd_yoy_diff},
    "gds_drv3_048_fcf_naive_miss_3rd_yoy_diff":    {"inputs": ["fcf"],                   "func": gds_drv3_048_fcf_naive_miss_3rd_yoy_diff},
    "gds_drv3_049_ncfo_naive_miss_3rd_yoy_diff":   {"inputs": ["ncfo"],                  "func": gds_drv3_049_ncfo_naive_miss_3rd_yoy_diff},
    "gds_drv3_050_opinc_naive_miss_3rd_yoy_diff":  {"inputs": ["opinc"],                 "func": gds_drv3_050_opinc_naive_miss_3rd_yoy_diff},
    "gds_drv3_051_rev_sue_slope_of_d2":            {"inputs": ["revenue"],               "func": gds_drv3_051_rev_sue_slope_of_d2},
    "gds_drv3_052_eps_sue_slope_of_d2":            {"inputs": ["eps"],                   "func": gds_drv3_052_eps_sue_slope_of_d2},
    "gds_drv3_053_gp_sue_slope_of_d2":             {"inputs": ["gp"],                    "func": gds_drv3_053_gp_sue_slope_of_d2},
    "gds_drv3_054_gp_seasonal_miss_3rd_diff":      {"inputs": ["gp"],                    "func": gds_drv3_054_gp_seasonal_miss_3rd_diff},
    "gds_drv3_055_fcf_seasonal_miss_3rd_diff":     {"inputs": ["fcf"],                   "func": gds_drv3_055_fcf_seasonal_miss_3rd_diff},
    "gds_drv3_056_ncfo_seasonal_miss_3rd_diff":    {"inputs": ["ncfo"],                  "func": gds_drv3_056_ncfo_seasonal_miss_3rd_diff},
    "gds_drv3_057_ebitda_seasonal_miss_3rd_diff":  {"inputs": ["ebitda"],                "func": gds_drv3_057_ebitda_seasonal_miss_3rd_diff},
    "gds_drv3_058_rev_sue_ewm_dev_d2":             {"inputs": ["revenue"],               "func": gds_drv3_058_rev_sue_ewm_dev_d2},
    "gds_drv3_059_gp_sue_d2_ewm_dev":              {"inputs": ["gp"],                    "func": gds_drv3_059_gp_sue_d2_ewm_dev},
    "gds_drv3_060_ebitda_sue_d2_ewm_dev":          {"inputs": ["ebitda"],                "func": gds_drv3_060_ebitda_sue_d2_ewm_dev},
    "gds_drv3_061_fcf_sue_d2_ewm_dev":             {"inputs": ["fcf"],                   "func": gds_drv3_061_fcf_sue_d2_ewm_dev},
    "gds_drv3_062_ncfo_sue_d2_ewm_dev":            {"inputs": ["ncfo"],                  "func": gds_drv3_062_ncfo_sue_d2_ewm_dev},
    "gds_drv3_063_opinc_sue_d2_ewm_dev":           {"inputs": ["opinc"],                 "func": gds_drv3_063_opinc_sue_d2_ewm_dev},
    "gds_drv3_064_epsdil_sue_d2_ewm_dev":          {"inputs": ["epsdil"],                "func": gds_drv3_064_epsdil_sue_d2_ewm_dev},
    "gds_drv3_065_rev_d2_miss_3rd_2q_diff":        {"inputs": ["revenue"],               "func": gds_drv3_065_rev_d2_miss_3rd_2q_diff},
    "gds_drv3_066_netinc_d2_miss_3rd_2q_diff":     {"inputs": ["netinc"],                "func": gds_drv3_066_netinc_d2_miss_3rd_2q_diff},
    "gds_drv3_067_eps_d2_miss_3rd_2q_diff":        {"inputs": ["eps"],                   "func": gds_drv3_067_eps_d2_miss_3rd_2q_diff},
    "gds_drv3_068_gp_d2_miss_3rd_2q_diff":         {"inputs": ["gp"],                    "func": gds_drv3_068_gp_d2_miss_3rd_2q_diff},
    "gds_drv3_069_ebitda_d2_sue_3rd_yoy_diff":     {"inputs": ["ebitda"],                "func": gds_drv3_069_ebitda_d2_sue_3rd_yoy_diff},
    "gds_drv3_070_fcf_d2_sue_3rd_yoy_diff":        {"inputs": ["fcf"],                   "func": gds_drv3_070_fcf_d2_sue_3rd_yoy_diff},
    "gds_drv3_071_ncfo_d2_sue_3rd_yoy_diff":       {"inputs": ["ncfo"],                  "func": gds_drv3_071_ncfo_d2_sue_3rd_yoy_diff},
    "gds_drv3_072_rev_d2_sue_3rd_yoy_diff":        {"inputs": ["revenue"],               "func": gds_drv3_072_rev_d2_sue_3rd_yoy_diff},
    "gds_drv3_073_eps_d2_sue_3rd_yoy_diff":        {"inputs": ["eps"],                   "func": gds_drv3_073_eps_d2_sue_3rd_yoy_diff},
    "gds_drv3_074_composite_d2_sue_slope":         {"inputs": ["revenue", "netinc", "eps"], "func": gds_drv3_074_composite_d2_sue_slope},
    "gds_drv3_075_composite_miss_jerk_5m":         {"inputs": ["revenue", "netinc", "eps", "gp", "ebitda"], "func": gds_drv3_075_composite_miss_jerk_5m},
}
