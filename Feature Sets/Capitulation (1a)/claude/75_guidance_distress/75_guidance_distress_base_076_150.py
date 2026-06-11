"""
75_guidance_distress — Base Features 076-200
Domain: estimate-vs-actual gaps, miss severity (trend-implied expectations)
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
_TD_5Y   = 1260
_TD_QTR  = 63
_TD_2Q   = 126
_TD_3Q   = 189
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Expectation model helpers ─────────────────────────────────────────────────

def _naive_expect(s: pd.Series) -> pd.Series:
    """Random-walk / last-quarter naive expectation: shift by one quarter."""
    return s.shift(_TD_QTR)


def _seasonal_naive_expect(s: pd.Series) -> pd.Series:
    """Seasonal-naive expectation: same quarter last year (252-day shift)."""
    return s.shift(_TD_YEAR)


def _trail_avg_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-average expectation shifted 1Q forward."""
    return _rolling_mean(s, w).shift(_TD_QTR)


def _ewm_trend_expect(s: pd.Series, span: int) -> pd.Series:
    """EWM-trend expectation: EWM mean shifted 1Q."""
    return _ewm_mean(s, span).shift(_TD_QTR)


def _trail_med_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-median expectation shifted 1Q forward."""
    return _rolling_median(s, w).shift(_TD_QTR)


def _linear_trend_extrap(s: pd.Series, window: int) -> pd.Series:
    """
    For each row, fit OLS slope over trailing `window` values (shifted 1Q) and
    extrapolate one step; returns trend-extrapolated expectation series.
    """
    def _predict(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom == 0.0:
            return arr[-1]
        slope = ((x - xm) * (arr - ym)).sum() / denom
        return arr[-1] + slope

    return s.shift(_TD_QTR).rolling(window, min_periods=max(2, window // 4)).apply(
        _predict, raw=True
    )


def _miss(s: pd.Series, expect: pd.Series) -> pd.Series:
    return s - expect


def _miss_norm_magnitude(s: pd.Series, expect: pd.Series) -> pd.Series:
    return _safe_div_abs(s - expect, expect)


def _miss_norm_vol(s: pd.Series, expect: pd.Series, vol_window: int) -> pd.Series:
    vol = _rolling_std(s, vol_window)
    return _safe_div(s - expect, vol)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Long-window / multi-year miss patterns ---

def gds_076_rev_miss_worst_8q(revenue: pd.Series) -> pd.Series:
    """Worst (most negative) naive-miss of revenue in trailing 8Q (504 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_min(m, _TD_2Y)


def gds_077_netinc_miss_worst_8q(netinc: pd.Series) -> pd.Series:
    """Worst naive-miss of net income in trailing 8Q (504 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_min(m, _TD_2Y)


def gds_078_rev_miss_worst_12q(revenue: pd.Series) -> pd.Series:
    """Worst naive-miss of revenue in trailing 12Q (756 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_min(m, _TD_3Y)


def gds_079_netinc_miss_worst_12q(netinc: pd.Series) -> pd.Series:
    """Worst naive-miss of net income in trailing 12Q (756 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_min(m, _TD_3Y)


def gds_080_rev_miss_fraction_4q(revenue: pd.Series) -> pd.Series:
    """Fraction of 4Q window where revenue had a negative naive-miss."""
    miss_flag = (revenue - _naive_expect(revenue) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_YEAR)


def gds_081_netinc_miss_fraction_4q(netinc: pd.Series) -> pd.Series:
    """Fraction of 4Q window where net income had a negative naive-miss."""
    miss_flag = (netinc - _naive_expect(netinc) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_YEAR)


def gds_082_rev_miss_fraction_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of 8Q window where revenue had a negative naive-miss."""
    miss_flag = (revenue - _naive_expect(revenue) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_2Y)


def gds_083_netinc_miss_fraction_8q(netinc: pd.Series) -> pd.Series:
    """Fraction of 8Q window where net income had a negative naive-miss."""
    miss_flag = (netinc - _naive_expect(netinc) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_2Y)


def gds_084_eps_miss_fraction_4q(eps: pd.Series) -> pd.Series:
    """Fraction of 4Q window where EPS had a negative naive-miss."""
    miss_flag = (eps - _naive_expect(eps) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_YEAR)


def gds_085_eps_miss_fraction_8q(eps: pd.Series) -> pd.Series:
    """Fraction of 8Q window where EPS had a negative naive-miss."""
    miss_flag = (eps - _naive_expect(eps) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_2Y)


def gds_086_rev_cumulative_miss_12q(revenue: pd.Series) -> pd.Series:
    """Cumulative naive-miss of revenue over trailing 12Q (756 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_sum(m, _TD_3Y)


def gds_087_netinc_cumulative_miss_12q(netinc: pd.Series) -> pd.Series:
    """Cumulative naive-miss of net income over trailing 12Q (756 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_sum(m, _TD_3Y)


def gds_088_fcf_miss_worst_4q(fcf: pd.Series) -> pd.Series:
    """Worst naive-miss of FCF in trailing 4Q (252 days)."""
    m = fcf - _naive_expect(fcf)
    return _rolling_min(m, _TD_YEAR)


def gds_089_ncfo_miss_worst_4q(ncfo: pd.Series) -> pd.Series:
    """Worst naive-miss of operating CF in trailing 4Q (252 days)."""
    m = ncfo - _naive_expect(ncfo)
    return _rolling_min(m, _TD_YEAR)


def gds_090_ebitda_miss_worst_4q(ebitda: pd.Series) -> pd.Series:
    """Worst naive-miss of EBITDA in trailing 4Q (252 days)."""
    m = ebitda - _naive_expect(ebitda)
    return _rolling_min(m, _TD_YEAR)


# --- Group G (091-105): Seasonal-model based SUE and miss-vol features ---

def gds_091_rev_sue_seasonal(revenue: pd.Series) -> pd.Series:
    """SUE-style score for revenue using seasonal-naive expectation."""
    return _miss_norm_vol(revenue, _seasonal_naive_expect(revenue), _TD_YEAR)


def gds_092_netinc_sue_8q(netinc: pd.Series) -> pd.Series:
    """SUE-style score for net income using 8Q volatility window."""
    return _miss_norm_vol(netinc, _naive_expect(netinc), _TD_2Y)


def gds_093_eps_sue_seasonal(eps: pd.Series) -> pd.Series:
    """SUE-style score for EPS using seasonal-naive expectation."""
    return _miss_norm_vol(eps, _seasonal_naive_expect(eps), _TD_YEAR)


def gds_094_epsdil_sue_seasonal(epsdil: pd.Series) -> pd.Series:
    """SUE-style score for diluted EPS using seasonal-naive expectation."""
    return _miss_norm_vol(epsdil, _seasonal_naive_expect(epsdil), _TD_YEAR)


def gds_095_gp_sue_seasonal(gp: pd.Series) -> pd.Series:
    """SUE-style score for gross profit using seasonal-naive expectation."""
    return _miss_norm_vol(gp, _seasonal_naive_expect(gp), _TD_YEAR)


def gds_096_opinc_sue_seasonal(opinc: pd.Series) -> pd.Series:
    """SUE-style score for operating income using seasonal-naive expectation."""
    return _miss_norm_vol(opinc, _seasonal_naive_expect(opinc), _TD_YEAR)


def gds_097_ebitda_sue_seasonal(ebitda: pd.Series) -> pd.Series:
    """SUE-style score for EBITDA using seasonal-naive expectation."""
    return _miss_norm_vol(ebitda, _seasonal_naive_expect(ebitda), _TD_YEAR)


def gds_098_fcf_sue_seasonal(fcf: pd.Series) -> pd.Series:
    """SUE-style score for FCF using seasonal-naive expectation."""
    return _miss_norm_vol(fcf, _seasonal_naive_expect(fcf), _TD_YEAR)


def gds_099_ncfo_sue_seasonal(ncfo: pd.Series) -> pd.Series:
    """SUE-style score for operating cash flow using seasonal-naive expectation."""
    return _miss_norm_vol(ncfo, _seasonal_naive_expect(ncfo), _TD_YEAR)


def gds_100_rev_trail_med_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(revenue, _trail_med_expect(revenue, _TD_YEAR))


def gds_101_netinc_trail_med_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(netinc, _trail_med_expect(netinc, _TD_YEAR))


def gds_102_eps_trail_avg_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs 4Q trailing-average expectation (absolute)."""
    return _miss(eps, _trail_avg_expect(eps, _TD_YEAR))


def gds_103_eps_trail_avg_miss_norm(eps: pd.Series) -> pd.Series:
    """EPS miss vs 4Q trailing-average expectation, normalized by abs(avg)."""
    return _miss_norm_magnitude(eps, _trail_avg_expect(eps, _TD_YEAR))


def gds_104_epsdil_trail_avg_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS miss vs 4Q trailing-average expectation."""
    return _miss(epsdil, _trail_avg_expect(epsdil, _TD_YEAR))


def gds_105_gp_lintrend_miss(gp: pd.Series) -> pd.Series:
    """Gross profit miss vs 4Q linear-trend extrapolation."""
    return gp - _linear_trend_extrap(gp, _TD_YEAR)


# --- Group H (106-120): Margin-level miss and cross-metric miss signals ---

def gds_106_gp_margin_naive_miss(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Gross-margin naive-miss: actual GP/Rev margin minus last-quarter GP/Rev margin.
    Captures deterioration in profitability structure.
    """
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def gds_107_opinc_margin_naive_miss(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating-margin naive-miss: actual Op/Rev minus last-quarter Op/Rev."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def gds_108_netinc_margin_naive_miss(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net-margin naive-miss: actual Net/Rev minus last-quarter Net/Rev."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def gds_109_ebitda_margin_naive_miss(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA-margin naive-miss: actual EBITDA/Rev minus last-quarter EBITDA/Rev."""
    margin = _safe_div(ebitda, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def gds_110_gp_margin_seasonal_miss(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross-margin seasonal-naive miss (vs same quarter last year margin)."""
    margin = _safe_div(gp, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def gds_111_opinc_margin_seasonal_miss(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating-margin seasonal-naive miss."""
    margin = _safe_div(opinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def gds_112_fcf_to_netinc_miss(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    FCF-to-netinc ratio miss: actual FCF/netinc minus last-quarter FCF/netinc.
    Deteriorating ratio signals earnings quality degradation.
    """
    ratio = _safe_div(fcf, netinc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def gds_113_ncfo_to_netinc_miss(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Operating CF-to-netinc ratio naive-miss (earnings quality proxy)."""
    ratio = _safe_div(ncfo, netinc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def gds_114_rev_miss_vs_gp_miss_diverge(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """
    Revenue beats (positive naive-miss) while GP misses (negative naive-miss):
    positive when this divergence occurs (margin squeeze signal).
    """
    rev_miss = revenue - _naive_expect(revenue)
    gp_miss  = gp      - _naive_expect(gp)
    return rev_miss - gp_miss


def gds_115_rev_miss_vs_opinc_miss_diverge(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Revenue naive-miss minus operating income naive-miss (opex blow-out signal)."""
    rev_miss   = revenue - _naive_expect(revenue)
    opinc_miss = opinc   - _naive_expect(opinc)
    return rev_miss - opinc_miss


def gds_116_netinc_miss_sum_4q_norm(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """4Q cumulative net income naive-miss normalized by 4Q mean revenue."""
    cum_miss = _rolling_sum(netinc - _naive_expect(netinc), _TD_YEAR)
    avg_rev  = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div_abs(cum_miss, avg_rev)


def gds_117_rev_miss_sum_4q_norm(revenue: pd.Series) -> pd.Series:
    """4Q cumulative revenue naive-miss normalized by 4Q mean revenue."""
    cum_miss = _rolling_sum(revenue - _naive_expect(revenue), _TD_YEAR)
    avg_rev  = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div_abs(cum_miss, avg_rev)


def gds_118_eps_miss_zscore_4q(eps: pd.Series) -> pd.Series:
    """Z-score of EPS naive-miss within trailing 4Q window."""
    m = eps - _naive_expect(eps)
    return _zscore_rolling(m, _TD_YEAR)


def gds_119_netinc_miss_zscore_4q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income naive-miss within trailing 4Q window."""
    m = netinc - _naive_expect(netinc)
    return _zscore_rolling(m, _TD_YEAR)


def gds_120_rev_miss_zscore_4q(revenue: pd.Series) -> pd.Series:
    """Z-score of revenue naive-miss within trailing 4Q window."""
    m = revenue - _naive_expect(revenue)
    return _zscore_rolling(m, _TD_YEAR)


# --- Group I (121-135): EWM expectation gap widening and acceleration ---

def gds_121_rev_ewm_expect_gap_zscore_4q(revenue: pd.Series) -> pd.Series:
    """
    Z-score of (revenue - EWM-trend expectation) within its own trailing 4q
    (252-day) window.  Captures how extreme the current revenue shortfall vs
    the EWM trend is relative to recent history.
    """
    gap = revenue - _ewm_trend_expect(revenue, _TD_YEAR)
    return _zscore_rolling(gap, _TD_YEAR)


def gds_122_netinc_ewm_expect_gap_zscore_4q(netinc: pd.Series) -> pd.Series:
    """
    Z-score of (net income - EWM-trend expectation) within its own trailing 4q
    (252-day) window.  Low z-score = current miss vs EWM trend is extreme.
    """
    gap = netinc - _ewm_trend_expect(netinc, _TD_YEAR)
    return _zscore_rolling(gap, _TD_YEAR)


def gds_123_eps_ewm_expect_gap_widening(eps: pd.Series) -> pd.Series:
    """QoQ change in (EPS - EWM-trend expectation): gap widening for EPS."""
    gap = eps - _ewm_trend_expect(eps, _TD_YEAR)
    return gap - gap.shift(_TD_QTR)


def gds_124_ebitda_ewm_expect_gap_widening(ebitda: pd.Series) -> pd.Series:
    """QoQ change in (EBITDA - EWM-trend expectation): gap widening for EBITDA."""
    gap = ebitda - _ewm_trend_expect(ebitda, _TD_YEAR)
    return gap - gap.shift(_TD_QTR)


def gds_125_fcf_ewm_expect_gap_widening(fcf: pd.Series) -> pd.Series:
    """QoQ change in (FCF - EWM-trend expectation): gap widening for FCF."""
    gap = fcf - _ewm_trend_expect(fcf, _TD_YEAR)
    return gap - gap.shift(_TD_QTR)


def gds_126_rev_lintrend_expect_gap(revenue: pd.Series) -> pd.Series:
    """Revenue minus 8Q linear-trend extrapolation (longer-horizon miss)."""
    return revenue - _linear_trend_extrap(revenue, _TD_2Y)


def gds_127_netinc_lintrend_expect_gap_8q(netinc: pd.Series) -> pd.Series:
    """Net income minus 8Q linear-trend extrapolation."""
    return netinc - _linear_trend_extrap(netinc, _TD_2Y)


def gds_128_eps_lintrend_miss_8q(eps: pd.Series) -> pd.Series:
    """EPS minus 8Q linear-trend extrapolation."""
    return eps - _linear_trend_extrap(eps, _TD_2Y)


def gds_129_opinc_lintrend_miss(opinc: pd.Series) -> pd.Series:
    """Operating income minus 4Q linear-trend extrapolation."""
    return opinc - _linear_trend_extrap(opinc, _TD_YEAR)


def gds_130_ncfo_lintrend_miss(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow minus 4Q linear-trend extrapolation."""
    return ncfo - _linear_trend_extrap(ncfo, _TD_YEAR)


def gds_131_rev_expectation_model_spread(revenue: pd.Series) -> pd.Series:
    """
    Spread between seasonal-naive and naive expectations for revenue:
    seasonal_naive - naive_expect.  Large positive = naive overstates seasonality.
    """
    return _seasonal_naive_expect(revenue) - _naive_expect(revenue)


def gds_132_netinc_expectation_model_spread(netinc: pd.Series) -> pd.Series:
    """Spread between seasonal-naive and naive expectations for net income."""
    return _seasonal_naive_expect(netinc) - _naive_expect(netinc)


def gds_133_rev_miss_pct_rank_4q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of revenue naive-miss within trailing 4Q window."""
    m = revenue - _naive_expect(revenue)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_134_netinc_miss_pct_rank_4q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income naive-miss within trailing 4Q window."""
    m = netinc - _naive_expect(netinc)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_135_eps_miss_pct_rank_4q(eps: pd.Series) -> pd.Series:
    """Percentile rank of EPS naive-miss within trailing 4Q window."""
    m = eps - _naive_expect(eps)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


# --- Group J (136-150): Composite, cross-metric, and expanding miss analytics ---

def gds_136_composite_miss_5metrics(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                     gp: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    Composite miss z-score: equal-weighted average of 4Q miss z-scores for
    revenue, net income, EPS, gross profit, and EBITDA.
    """
    def _mz(s):
        m = s - _naive_expect(s)
        return _zscore_rolling(m, _TD_YEAR)
    return (_mz(revenue) + _mz(netinc) + _mz(eps) + _mz(gp) + _mz(ebitda)) / 5.0


def gds_137_miss_breadth_9metrics(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                   gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
                                   fcf: pd.Series, ncfo: pd.Series, epsdil: pd.Series) -> pd.Series:
    """Count of metrics (0-9) with a negative naive-miss in current period."""
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, epsdil]
    return sum(((s - _naive_expect(s)) < 0).astype(float) for s in metrics)


def gds_138_rev_expanding_miss_min(revenue: pd.Series) -> pd.Series:
    """All-history expanding minimum of revenue naive-miss."""
    m = revenue - _naive_expect(revenue)
    return m.expanding(min_periods=1).min()


def gds_139_netinc_expanding_miss_min(netinc: pd.Series) -> pd.Series:
    """All-history expanding minimum of net income naive-miss."""
    m = netinc - _naive_expect(netinc)
    return m.expanding(min_periods=1).min()


def gds_140_eps_expanding_miss_min(eps: pd.Series) -> pd.Series:
    """All-history expanding minimum of EPS naive-miss."""
    m = eps - _naive_expect(eps)
    return m.expanding(min_periods=1).min()


def gds_141_rev_miss_to_expanding_min_ratio(revenue: pd.Series) -> pd.Series:
    """Current revenue naive-miss divided by its all-history expanding min."""
    m    = revenue - _naive_expect(revenue)
    emin = m.expanding(min_periods=1).min()
    return _safe_div(m, emin.abs().replace(0, np.nan))


def gds_142_netinc_miss_to_expanding_min_ratio(netinc: pd.Series) -> pd.Series:
    """Current net income naive-miss divided by expanding-min miss."""
    m    = netinc - _naive_expect(netinc)
    emin = m.expanding(min_periods=1).min()
    return _safe_div(m, emin.abs().replace(0, np.nan))


def gds_143_rev_miss_zscore_8q(revenue: pd.Series) -> pd.Series:
    """
    Z-score of the current revenue naive-miss within its own trailing 8q
    (504-day) window.  Captures how extreme the current miss level is vs
    the medium-term distribution of misses.
    """
    m = revenue - _naive_expect(revenue)
    return _zscore_rolling(m, _TD_2Y)


def gds_144_netinc_miss_zscore_8q(netinc: pd.Series) -> pd.Series:
    """
    Z-score of the current net income naive-miss within its own trailing 8q
    (504-day) window.  Captures how extreme the current miss level is vs
    the medium-term distribution of misses.
    """
    m = netinc - _naive_expect(netinc)
    return _zscore_rolling(m, _TD_2Y)


def gds_145_eps_consecutive_miss_streak(eps: pd.Series) -> pd.Series:
    """Consecutive negative naive-miss quarters for EPS (streak in daily obs)."""
    miss_int = ((eps - _naive_expect(eps)) < 0).astype(int).values
    streak = np.zeros(len(miss_int), dtype=float)
    for i in range(1, len(miss_int)):
        streak[i] = (streak[i - 1] + 1) * miss_int[i]
    return pd.Series(streak, index=eps.index)


def gds_146_epsdil_consecutive_miss_streak(epsdil: pd.Series) -> pd.Series:
    """Consecutive negative naive-miss quarters for diluted EPS (daily streak)."""
    miss_int = ((epsdil - _naive_expect(epsdil)) < 0).astype(int).values
    streak = np.zeros(len(miss_int), dtype=float)
    for i in range(1, len(miss_int)):
        streak[i] = (streak[i - 1] + 1) * miss_int[i]
    return pd.Series(streak, index=epsdil.index)


def gds_147_fcf_miss_sign_flip(fcf: pd.Series) -> pd.Series:
    """1 when FCF naive-miss direction flips vs prior quarter."""
    sign = np.sign(fcf - _naive_expect(fcf))
    return (sign != sign.shift(_TD_QTR)).astype(float)


def gds_148_composite_sue_9metrics(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
                                    fcf: pd.Series, ncfo: pd.Series, epsdil: pd.Series) -> pd.Series:
    """
    Composite SUE score across all 9 core metrics (equal-weighted average of
    naive-miss / trailing-4Q-std for each).
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, epsdil]
    sue_list = [_safe_div(s - _naive_expect(s), _rolling_std(s, _TD_YEAR)) for s in metrics]
    return sum(sue_list) / 9.0


def gds_149_netinc_miss_trend_slope(netinc: pd.Series) -> pd.Series:
    """
    Rolling 4Q OLS slope of the net income naive-miss series.
    Negative slope = miss trend is deteriorating over time.
    """
    m = netinc - _naive_expect(netinc)

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

    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_slope, raw=True)


def gds_150_multi_model_miss_consensus(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Count of expectation models (0-4) where net income misses:
    naive, seasonal-naive, trail-avg, EWM.  Higher = more robust miss signal.
    """
    models = [
        _naive_expect(netinc),
        _seasonal_naive_expect(netinc),
        _trail_avg_expect(netinc, _TD_YEAR),
        _ewm_trend_expect(netinc, _TD_YEAR),
    ]
    return sum(((netinc - e) < 0).astype(float) for e in models)


# --- Group K-ext (176-200): Extended windows, cross-metric, and normalization variants ---

def gds_176_gp_miss_zscore_4q(gp: pd.Series) -> pd.Series:
    """Z-score of gross profit naive-miss within trailing 4Q window."""
    m = gp - _naive_expect(gp)
    return _zscore_rolling(m, _TD_YEAR)


def gds_177_opinc_miss_zscore_4q(opinc: pd.Series) -> pd.Series:
    """Z-score of operating income naive-miss within trailing 4Q window."""
    m = opinc - _naive_expect(opinc)
    return _zscore_rolling(m, _TD_YEAR)


def gds_178_ebitda_miss_zscore_4q(ebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA naive-miss within trailing 4Q window."""
    m = ebitda - _naive_expect(ebitda)
    return _zscore_rolling(m, _TD_YEAR)


def gds_179_fcf_miss_zscore_4q(fcf: pd.Series) -> pd.Series:
    """Z-score of FCF naive-miss within trailing 4Q window."""
    m = fcf - _naive_expect(fcf)
    return _zscore_rolling(m, _TD_YEAR)


def gds_180_ncfo_miss_zscore_4q(ncfo: pd.Series) -> pd.Series:
    """Z-score of operating CF naive-miss within trailing 4Q window."""
    m = ncfo - _naive_expect(ncfo)
    return _zscore_rolling(m, _TD_YEAR)


def gds_181_rev_miss_worst_3q(revenue: pd.Series) -> pd.Series:
    """Worst naive-miss of revenue in trailing 3Q (189 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_min(m, _TD_3Q)


def gds_182_netinc_miss_worst_3q(netinc: pd.Series) -> pd.Series:
    """Worst naive-miss of net income in trailing 3Q (189 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_min(m, _TD_3Q)


def gds_183_eps_miss_worst_3q(eps: pd.Series) -> pd.Series:
    """Worst naive-miss of EPS in trailing 3Q (189 days)."""
    m = eps - _naive_expect(eps)
    return _rolling_min(m, _TD_3Q)


def gds_184_ebitda_miss_worst_8q(ebitda: pd.Series) -> pd.Series:
    """Worst naive-miss of EBITDA in trailing 8Q (504 days)."""
    m = ebitda - _naive_expect(ebitda)
    return _rolling_min(m, _TD_2Y)


def gds_185_fcf_miss_worst_8q(fcf: pd.Series) -> pd.Series:
    """Worst naive-miss of FCF in trailing 8Q (504 days)."""
    m = fcf - _naive_expect(fcf)
    return _rolling_min(m, _TD_2Y)


def gds_186_ncfo_miss_worst_8q(ncfo: pd.Series) -> pd.Series:
    """Worst naive-miss of operating CF in trailing 8Q (504 days)."""
    m = ncfo - _naive_expect(ncfo)
    return _rolling_min(m, _TD_2Y)


def gds_187_gp_miss_pct_rank_8q(gp: pd.Series) -> pd.Series:
    """Percentile rank of gross profit naive-miss within trailing 8Q window."""
    m = gp - _naive_expect(gp)
    return m.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def gds_188_opinc_miss_pct_rank_8q(opinc: pd.Series) -> pd.Series:
    """Percentile rank of operating income naive-miss within trailing 8Q window."""
    m = opinc - _naive_expect(opinc)
    return m.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def gds_189_ebitda_miss_pct_rank_4q(ebitda: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA naive-miss within trailing 4Q window."""
    m = ebitda - _naive_expect(ebitda)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_190_fcf_miss_pct_rank_4q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of FCF naive-miss within trailing 4Q window."""
    m = fcf - _naive_expect(fcf)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_191_ncfo_miss_pct_rank_4q(ncfo: pd.Series) -> pd.Series:
    """Percentile rank of operating CF naive-miss within trailing 4Q window."""
    m = ncfo - _naive_expect(ncfo)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_192_rev_miss_fraction_12q(revenue: pd.Series) -> pd.Series:
    """Fraction of 12Q window where revenue had a negative naive-miss."""
    miss_flag = (revenue - _naive_expect(revenue) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_3Y)


def gds_193_netinc_miss_fraction_12q(netinc: pd.Series) -> pd.Series:
    """Fraction of 12Q window where net income had a negative naive-miss."""
    miss_flag = (netinc - _naive_expect(netinc) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_3Y)


def gds_194_eps_miss_fraction_12q(eps: pd.Series) -> pd.Series:
    """Fraction of 12Q window where EPS had a negative naive-miss."""
    miss_flag = (eps - _naive_expect(eps) < 0).astype(float)
    return _rolling_mean(miss_flag, _TD_3Y)


def gds_195_rev_multi_model_consensus(revenue: pd.Series) -> pd.Series:
    """Count of models (0-4) where revenue misses: naive, seasonal, trail-avg, EWM."""
    models = [
        _naive_expect(revenue),
        _seasonal_naive_expect(revenue),
        _trail_avg_expect(revenue, _TD_YEAR),
        _ewm_trend_expect(revenue, _TD_YEAR),
    ]
    return sum(((revenue - e) < 0).astype(float) for e in models)


def gds_196_eps_multi_model_consensus(eps: pd.Series) -> pd.Series:
    """Count of models (0-4) where EPS misses: naive, seasonal, trail-avg, EWM."""
    models = [
        _naive_expect(eps),
        _seasonal_naive_expect(eps),
        _trail_avg_expect(eps, _TD_YEAR),
        _ewm_trend_expect(eps, _TD_YEAR),
    ]
    return sum(((eps - e) < 0).astype(float) for e in models)


def gds_197_ebitda_margin_seasonal_miss(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA-margin seasonal-naive miss (vs same quarter last year margin)."""
    margin = _safe_div(ebitda, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_YEAR)


def gds_198_netinc_miss_ewm_deviation(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss minus its own EWM (span=4Q): anomaly vs trend of misses."""
    m = netinc - _naive_expect(netinc)
    return m - _ewm_mean(m, _TD_YEAR)


def gds_199_rev_miss_ewm_deviation_seasonal(revenue: pd.Series) -> pd.Series:
    """Revenue seasonal-miss minus its own EWM: anomaly vs trend of seasonal misses."""
    m = revenue - _seasonal_naive_expect(revenue)
    return m - _ewm_mean(m, _TD_YEAR)


def gds_200_composite_miss_breadth_norm(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                         gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
                                         fcf: pd.Series, ncfo: pd.Series, epsdil: pd.Series) -> pd.Series:
    """
    Fraction of 9 core metrics with negative naive-miss, normalized as a 0-1 score.
    1 = all metrics miss simultaneously (maximum distress breadth).
    """
    metrics = [revenue, netinc, eps, gp, opinc, ebitda, fcf, ncfo, epsdil]
    count = sum(((s - _naive_expect(s)) < 0).astype(float) for s in metrics)
    return count / 9.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

GUIDANCE_DISTRESS_REGISTRY_076_150 = {
    "gds_076_rev_miss_worst_8q":                {"inputs": ["revenue"],                                                                        "func": gds_076_rev_miss_worst_8q},
    "gds_077_netinc_miss_worst_8q":             {"inputs": ["netinc"],                                                                         "func": gds_077_netinc_miss_worst_8q},
    "gds_078_rev_miss_worst_12q":               {"inputs": ["revenue"],                                                                        "func": gds_078_rev_miss_worst_12q},
    "gds_079_netinc_miss_worst_12q":            {"inputs": ["netinc"],                                                                         "func": gds_079_netinc_miss_worst_12q},
    "gds_080_rev_miss_fraction_4q":             {"inputs": ["revenue"],                                                                        "func": gds_080_rev_miss_fraction_4q},
    "gds_081_netinc_miss_fraction_4q":          {"inputs": ["netinc"],                                                                         "func": gds_081_netinc_miss_fraction_4q},
    "gds_082_rev_miss_fraction_8q":             {"inputs": ["revenue"],                                                                        "func": gds_082_rev_miss_fraction_8q},
    "gds_083_netinc_miss_fraction_8q":          {"inputs": ["netinc"],                                                                         "func": gds_083_netinc_miss_fraction_8q},
    "gds_084_eps_miss_fraction_4q":             {"inputs": ["eps"],                                                                            "func": gds_084_eps_miss_fraction_4q},
    "gds_085_eps_miss_fraction_8q":             {"inputs": ["eps"],                                                                            "func": gds_085_eps_miss_fraction_8q},
    "gds_086_rev_cumulative_miss_12q":          {"inputs": ["revenue"],                                                                        "func": gds_086_rev_cumulative_miss_12q},
    "gds_087_netinc_cumulative_miss_12q":       {"inputs": ["netinc"],                                                                         "func": gds_087_netinc_cumulative_miss_12q},
    "gds_088_fcf_miss_worst_4q":                {"inputs": ["fcf"],                                                                            "func": gds_088_fcf_miss_worst_4q},
    "gds_089_ncfo_miss_worst_4q":               {"inputs": ["ncfo"],                                                                           "func": gds_089_ncfo_miss_worst_4q},
    "gds_090_ebitda_miss_worst_4q":             {"inputs": ["ebitda"],                                                                         "func": gds_090_ebitda_miss_worst_4q},
    "gds_091_rev_sue_seasonal":                 {"inputs": ["revenue"],                                                                        "func": gds_091_rev_sue_seasonal},
    "gds_092_netinc_sue_8q":                    {"inputs": ["netinc"],                                                                         "func": gds_092_netinc_sue_8q},
    "gds_093_eps_sue_seasonal":                 {"inputs": ["eps"],                                                                            "func": gds_093_eps_sue_seasonal},
    "gds_094_epsdil_sue_seasonal":              {"inputs": ["epsdil"],                                                                         "func": gds_094_epsdil_sue_seasonal},
    "gds_095_gp_sue_seasonal":                  {"inputs": ["gp"],                                                                             "func": gds_095_gp_sue_seasonal},
    "gds_096_opinc_sue_seasonal":               {"inputs": ["opinc"],                                                                          "func": gds_096_opinc_sue_seasonal},
    "gds_097_ebitda_sue_seasonal":              {"inputs": ["ebitda"],                                                                         "func": gds_097_ebitda_sue_seasonal},
    "gds_098_fcf_sue_seasonal":                 {"inputs": ["fcf"],                                                                            "func": gds_098_fcf_sue_seasonal},
    "gds_099_ncfo_sue_seasonal":                {"inputs": ["ncfo"],                                                                           "func": gds_099_ncfo_sue_seasonal},
    "gds_100_rev_trail_med_miss":               {"inputs": ["revenue"],                                                                        "func": gds_100_rev_trail_med_miss},
    "gds_101_netinc_trail_med_miss":            {"inputs": ["netinc"],                                                                         "func": gds_101_netinc_trail_med_miss},
    "gds_102_eps_trail_avg_miss":               {"inputs": ["eps"],                                                                            "func": gds_102_eps_trail_avg_miss},
    "gds_103_eps_trail_avg_miss_norm":          {"inputs": ["eps"],                                                                            "func": gds_103_eps_trail_avg_miss_norm},
    "gds_104_epsdil_trail_avg_miss":            {"inputs": ["epsdil"],                                                                         "func": gds_104_epsdil_trail_avg_miss},
    "gds_105_gp_lintrend_miss":                 {"inputs": ["gp"],                                                                             "func": gds_105_gp_lintrend_miss},
    "gds_106_gp_margin_naive_miss":             {"inputs": ["gp", "revenue"],                                                                  "func": gds_106_gp_margin_naive_miss},
    "gds_107_opinc_margin_naive_miss":          {"inputs": ["opinc", "revenue"],                                                               "func": gds_107_opinc_margin_naive_miss},
    "gds_108_netinc_margin_naive_miss":         {"inputs": ["netinc", "revenue"],                                                              "func": gds_108_netinc_margin_naive_miss},
    "gds_109_ebitda_margin_naive_miss":         {"inputs": ["ebitda", "revenue"],                                                              "func": gds_109_ebitda_margin_naive_miss},
    "gds_110_gp_margin_seasonal_miss":          {"inputs": ["gp", "revenue"],                                                                  "func": gds_110_gp_margin_seasonal_miss},
    "gds_111_opinc_margin_seasonal_miss":       {"inputs": ["opinc", "revenue"],                                                               "func": gds_111_opinc_margin_seasonal_miss},
    "gds_112_fcf_to_netinc_miss":               {"inputs": ["fcf", "netinc"],                                                                  "func": gds_112_fcf_to_netinc_miss},
    "gds_113_ncfo_to_netinc_miss":              {"inputs": ["ncfo", "netinc"],                                                                 "func": gds_113_ncfo_to_netinc_miss},
    "gds_114_rev_miss_vs_gp_miss_diverge":      {"inputs": ["revenue", "gp"],                                                                  "func": gds_114_rev_miss_vs_gp_miss_diverge},
    "gds_115_rev_miss_vs_opinc_miss_diverge":   {"inputs": ["revenue", "opinc"],                                                               "func": gds_115_rev_miss_vs_opinc_miss_diverge},
    "gds_116_netinc_miss_sum_4q_norm":          {"inputs": ["netinc", "revenue"],                                                              "func": gds_116_netinc_miss_sum_4q_norm},
    "gds_117_rev_miss_sum_4q_norm":             {"inputs": ["revenue"],                                                                        "func": gds_117_rev_miss_sum_4q_norm},
    "gds_118_eps_miss_zscore_4q":               {"inputs": ["eps"],                                                                            "func": gds_118_eps_miss_zscore_4q},
    "gds_119_netinc_miss_zscore_4q":            {"inputs": ["netinc"],                                                                         "func": gds_119_netinc_miss_zscore_4q},
    "gds_120_rev_miss_zscore_4q":               {"inputs": ["revenue"],                                                                        "func": gds_120_rev_miss_zscore_4q},
    "gds_121_rev_ewm_expect_gap_zscore_4q":      {"inputs": ["revenue"],                                                                        "func": gds_121_rev_ewm_expect_gap_zscore_4q},
    "gds_122_netinc_ewm_expect_gap_zscore_4q":  {"inputs": ["netinc"],                                                                         "func": gds_122_netinc_ewm_expect_gap_zscore_4q},
    "gds_123_eps_ewm_expect_gap_widening":      {"inputs": ["eps"],                                                                            "func": gds_123_eps_ewm_expect_gap_widening},
    "gds_124_ebitda_ewm_expect_gap_widening":   {"inputs": ["ebitda"],                                                                         "func": gds_124_ebitda_ewm_expect_gap_widening},
    "gds_125_fcf_ewm_expect_gap_widening":      {"inputs": ["fcf"],                                                                            "func": gds_125_fcf_ewm_expect_gap_widening},
    "gds_126_rev_lintrend_expect_gap":          {"inputs": ["revenue"],                                                                        "func": gds_126_rev_lintrend_expect_gap},
    "gds_127_netinc_lintrend_expect_gap_8q":    {"inputs": ["netinc"],                                                                         "func": gds_127_netinc_lintrend_expect_gap_8q},
    "gds_128_eps_lintrend_miss_8q":             {"inputs": ["eps"],                                                                            "func": gds_128_eps_lintrend_miss_8q},
    "gds_129_opinc_lintrend_miss":              {"inputs": ["opinc"],                                                                          "func": gds_129_opinc_lintrend_miss},
    "gds_130_ncfo_lintrend_miss":               {"inputs": ["ncfo"],                                                                           "func": gds_130_ncfo_lintrend_miss},
    "gds_131_rev_expectation_model_spread":     {"inputs": ["revenue"],                                                                        "func": gds_131_rev_expectation_model_spread},
    "gds_132_netinc_expectation_model_spread":  {"inputs": ["netinc"],                                                                         "func": gds_132_netinc_expectation_model_spread},
    "gds_133_rev_miss_pct_rank_4q":             {"inputs": ["revenue"],                                                                        "func": gds_133_rev_miss_pct_rank_4q},
    "gds_134_netinc_miss_pct_rank_4q":          {"inputs": ["netinc"],                                                                         "func": gds_134_netinc_miss_pct_rank_4q},
    "gds_135_eps_miss_pct_rank_4q":             {"inputs": ["eps"],                                                                            "func": gds_135_eps_miss_pct_rank_4q},
    "gds_136_composite_miss_5metrics":          {"inputs": ["revenue", "netinc", "eps", "gp", "ebitda"],                                       "func": gds_136_composite_miss_5metrics},
    "gds_137_miss_breadth_9metrics":            {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "epsdil"],     "func": gds_137_miss_breadth_9metrics},
    "gds_138_rev_expanding_miss_min":           {"inputs": ["revenue"],                                                                        "func": gds_138_rev_expanding_miss_min},
    "gds_139_netinc_expanding_miss_min":        {"inputs": ["netinc"],                                                                         "func": gds_139_netinc_expanding_miss_min},
    "gds_140_eps_expanding_miss_min":           {"inputs": ["eps"],                                                                            "func": gds_140_eps_expanding_miss_min},
    "gds_141_rev_miss_to_expanding_min_ratio":  {"inputs": ["revenue"],                                                                        "func": gds_141_rev_miss_to_expanding_min_ratio},
    "gds_142_netinc_miss_to_expanding_min_ratio": {"inputs": ["netinc"],                                                                       "func": gds_142_netinc_miss_to_expanding_min_ratio},
    "gds_143_rev_miss_zscore_8q":               {"inputs": ["revenue"],                                                                        "func": gds_143_rev_miss_zscore_8q},
    "gds_144_netinc_miss_zscore_8q":            {"inputs": ["netinc"],                                                                         "func": gds_144_netinc_miss_zscore_8q},
    "gds_145_eps_consecutive_miss_streak":      {"inputs": ["eps"],                                                                            "func": gds_145_eps_consecutive_miss_streak},
    "gds_146_epsdil_consecutive_miss_streak":   {"inputs": ["epsdil"],                                                                         "func": gds_146_epsdil_consecutive_miss_streak},
    "gds_147_fcf_miss_sign_flip":               {"inputs": ["fcf"],                                                                            "func": gds_147_fcf_miss_sign_flip},
    "gds_148_composite_sue_9metrics":           {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "epsdil"],     "func": gds_148_composite_sue_9metrics},
    "gds_149_netinc_miss_trend_slope":          {"inputs": ["netinc"],                                                                         "func": gds_149_netinc_miss_trend_slope},
    "gds_150_multi_model_miss_consensus":       {"inputs": ["revenue", "netinc"],                                                              "func": gds_150_multi_model_miss_consensus},
    "gds_176_gp_miss_zscore_4q":               {"inputs": ["gp"],                                                                             "func": gds_176_gp_miss_zscore_4q},
    "gds_177_opinc_miss_zscore_4q":            {"inputs": ["opinc"],                                                                          "func": gds_177_opinc_miss_zscore_4q},
    "gds_178_ebitda_miss_zscore_4q":           {"inputs": ["ebitda"],                                                                         "func": gds_178_ebitda_miss_zscore_4q},
    "gds_179_fcf_miss_zscore_4q":              {"inputs": ["fcf"],                                                                            "func": gds_179_fcf_miss_zscore_4q},
    "gds_180_ncfo_miss_zscore_4q":             {"inputs": ["ncfo"],                                                                           "func": gds_180_ncfo_miss_zscore_4q},
    "gds_181_rev_miss_worst_3q":               {"inputs": ["revenue"],                                                                        "func": gds_181_rev_miss_worst_3q},
    "gds_182_netinc_miss_worst_3q":            {"inputs": ["netinc"],                                                                         "func": gds_182_netinc_miss_worst_3q},
    "gds_183_eps_miss_worst_3q":               {"inputs": ["eps"],                                                                            "func": gds_183_eps_miss_worst_3q},
    "gds_184_ebitda_miss_worst_8q":            {"inputs": ["ebitda"],                                                                         "func": gds_184_ebitda_miss_worst_8q},
    "gds_185_fcf_miss_worst_8q":               {"inputs": ["fcf"],                                                                            "func": gds_185_fcf_miss_worst_8q},
    "gds_186_ncfo_miss_worst_8q":              {"inputs": ["ncfo"],                                                                           "func": gds_186_ncfo_miss_worst_8q},
    "gds_187_gp_miss_pct_rank_8q":             {"inputs": ["gp"],                                                                             "func": gds_187_gp_miss_pct_rank_8q},
    "gds_188_opinc_miss_pct_rank_8q":          {"inputs": ["opinc"],                                                                          "func": gds_188_opinc_miss_pct_rank_8q},
    "gds_189_ebitda_miss_pct_rank_4q":         {"inputs": ["ebitda"],                                                                         "func": gds_189_ebitda_miss_pct_rank_4q},
    "gds_190_fcf_miss_pct_rank_4q":            {"inputs": ["fcf"],                                                                            "func": gds_190_fcf_miss_pct_rank_4q},
    "gds_191_ncfo_miss_pct_rank_4q":           {"inputs": ["ncfo"],                                                                           "func": gds_191_ncfo_miss_pct_rank_4q},
    "gds_192_rev_miss_fraction_12q":           {"inputs": ["revenue"],                                                                        "func": gds_192_rev_miss_fraction_12q},
    "gds_193_netinc_miss_fraction_12q":        {"inputs": ["netinc"],                                                                         "func": gds_193_netinc_miss_fraction_12q},
    "gds_194_eps_miss_fraction_12q":           {"inputs": ["eps"],                                                                            "func": gds_194_eps_miss_fraction_12q},
    "gds_195_rev_multi_model_consensus":       {"inputs": ["revenue"],                                                                        "func": gds_195_rev_multi_model_consensus},
    "gds_196_eps_multi_model_consensus":       {"inputs": ["eps"],                                                                            "func": gds_196_eps_multi_model_consensus},
    "gds_197_ebitda_margin_seasonal_miss":     {"inputs": ["ebitda", "revenue"],                                                              "func": gds_197_ebitda_margin_seasonal_miss},
    "gds_198_netinc_miss_ewm_deviation":       {"inputs": ["netinc"],                                                                         "func": gds_198_netinc_miss_ewm_deviation},
    "gds_199_rev_miss_ewm_deviation_seasonal": {"inputs": ["revenue"],                                                                        "func": gds_199_rev_miss_ewm_deviation_seasonal},
    "gds_200_composite_miss_breadth_norm":     {"inputs": ["revenue", "netinc", "eps", "gp", "opinc", "ebitda", "fcf", "ncfo", "epsdil"],     "func": gds_200_composite_miss_breadth_norm},
}
