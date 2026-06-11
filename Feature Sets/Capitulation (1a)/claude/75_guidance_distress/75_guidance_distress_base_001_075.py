"""
75_guidance_distress — Base Features 001-100
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


def _linear_trend_extrap(s: pd.Series, window: int) -> pd.Series:
    """
    For each row, fit OLS slope over the trailing `window` values and extrapolate
    one step forward (i.e., predict today's value from yesterday's trend).
    The expectation is shifted by one quarter (_TD_QTR) so it uses only past data.
    Returns the trend-extrapolated expectation series.
    """
    def _slope_intercept_predict(arr):
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
        return arr[-1] + slope  # extrapolate one step beyond window end

    return s.shift(_TD_QTR).rolling(window, min_periods=max(2, window // 4)).apply(
        _slope_intercept_predict, raw=True
    )


# ── Expectation model helpers ─────────────────────────────────────────────────

def _naive_expect(s: pd.Series) -> pd.Series:
    """Random-walk / last-quarter naive expectation: shift by one quarter."""
    return s.shift(_TD_QTR)


def _seasonal_naive_expect(s: pd.Series) -> pd.Series:
    """Seasonal-naive expectation: same quarter last year (252-day shift)."""
    return s.shift(_TD_YEAR)


def _trail_avg_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-average expectation: rolling mean of past `w` days (shifted 1Q)."""
    return _rolling_mean(s, w).shift(_TD_QTR)


def _ewm_trend_expect(s: pd.Series, span: int) -> pd.Series:
    """EWM-trend expectation: EWM mean of series, shifted 1Q so it uses past data only."""
    return _ewm_mean(s, span).shift(_TD_QTR)


def _trail_med_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-median expectation: rolling median of past `w` days (shifted 1Q)."""
    return _rolling_median(s, w).shift(_TD_QTR)


def _miss(s: pd.Series, expect: pd.Series) -> pd.Series:
    """Surprise / miss = actual minus expectation."""
    return s - expect


def _miss_norm_magnitude(s: pd.Series, expect: pd.Series) -> pd.Series:
    """Miss normalized by abs(expectation) — relative miss."""
    return _safe_div_abs(s - expect, expect)


def _miss_norm_vol(s: pd.Series, expect: pd.Series, vol_window: int) -> pd.Series:
    """Miss normalized by trailing volatility of the metric."""
    vol = _rolling_std(s, vol_window)
    return _safe_div(s - expect, vol)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Revenue miss features ---

def gds_001_rev_naive_miss(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss: actual minus last-quarter-naive expectation (absolute)."""
    return _miss(revenue, _naive_expect(revenue))


def gds_002_rev_naive_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(revenue, _naive_expect(revenue))


def gds_003_rev_seasonal_miss(revenue: pd.Series) -> pd.Series:
    """Revenue seasonal-naive miss: actual minus same-quarter-last-year (absolute)."""
    return _miss(revenue, _seasonal_naive_expect(revenue))


def gds_004_rev_seasonal_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue seasonal-naive miss normalized by abs(seasonal expectation)."""
    return _miss_norm_magnitude(revenue, _seasonal_naive_expect(revenue))


def gds_005_rev_trail_avg_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs 4Q trailing-average expectation (absolute)."""
    return _miss(revenue, _trail_avg_expect(revenue, _TD_YEAR))


def gds_006_rev_trail_avg_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs 4Q trailing-average expectation, normalized by abs(expectation)."""
    return _miss_norm_magnitude(revenue, _trail_avg_expect(revenue, _TD_YEAR))


def gds_007_rev_ewm_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs EWM-trend expectation (span=252, shifted 1Q)."""
    return _miss(revenue, _ewm_trend_expect(revenue, _TD_YEAR))


def gds_008_rev_ewm_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs EWM-trend expectation, normalized by abs(EWM expectation)."""
    return _miss_norm_magnitude(revenue, _ewm_trend_expect(revenue, _TD_YEAR))


def gds_009_rev_naive_miss_vol_norm(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss normalized by trailing 4Q volatility of revenue (SUE-style)."""
    return _miss_norm_vol(revenue, _naive_expect(revenue), _TD_YEAR)


def gds_010_rev_seasonal_miss_vol_norm(revenue: pd.Series) -> pd.Series:
    """Revenue seasonal-naive miss normalized by trailing 4Q revenue volatility."""
    return _miss_norm_vol(revenue, _seasonal_naive_expect(revenue), _TD_YEAR)


def gds_011_rev_lintrend_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs linear-trend extrapolation over 4Q window."""
    return revenue - _linear_trend_extrap(revenue, _TD_YEAR)


def gds_012_rev_lintrend_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue linear-trend miss normalized by abs(trend expectation)."""
    expect = _linear_trend_extrap(revenue, _TD_YEAR)
    return _miss_norm_magnitude(revenue, expect)


def gds_013_rev_consecutive_miss_streak(revenue: pd.Series) -> pd.Series:
    """Consecutive quarters of negative naive-miss in revenue (streak in daily obs)."""
    miss = (revenue - _naive_expect(revenue)) < 0
    miss_int = miss.astype(int).values
    streak = np.zeros(len(miss_int), dtype=float)
    for i in range(1, len(miss_int)):
        streak[i] = (streak[i - 1] + 1) * miss_int[i]
    return pd.Series(streak, index=revenue.index)


def gds_014_rev_miss_worst_4q(revenue: pd.Series) -> pd.Series:
    """Worst (most negative) naive-miss in trailing 4 quarters (252 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_min(m, _TD_YEAR)


def gds_015_rev_cumulative_miss_4q(revenue: pd.Series) -> pd.Series:
    """Cumulative (sum) of naive-miss values over trailing 4 quarters."""
    m = revenue - _naive_expect(revenue)
    return _rolling_sum(m, _TD_YEAR)


# --- Group B (016-030): Net income / EPS miss features ---

def gds_016_netinc_naive_miss(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss: actual minus last-quarter expectation (absolute)."""
    return _miss(netinc, _naive_expect(netinc))


def gds_017_netinc_naive_miss_norm(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(netinc, _naive_expect(netinc))


def gds_018_netinc_seasonal_miss(netinc: pd.Series) -> pd.Series:
    """Net income seasonal-naive miss (vs same quarter last year)."""
    return _miss(netinc, _seasonal_naive_expect(netinc))


def gds_019_netinc_seasonal_miss_norm(netinc: pd.Series) -> pd.Series:
    """Net income seasonal-naive miss normalized by abs(seasonal expectation)."""
    return _miss_norm_magnitude(netinc, _seasonal_naive_expect(netinc))


def gds_020_netinc_sue_naive(netinc: pd.Series) -> pd.Series:
    """SUE-style score for net income: naive miss / trailing 4Q std (standardized unexpected)."""
    return _miss_norm_vol(netinc, _naive_expect(netinc), _TD_YEAR)


def gds_021_netinc_sue_seasonal(netinc: pd.Series) -> pd.Series:
    """SUE-style score using seasonal-naive expectation for net income."""
    return _miss_norm_vol(netinc, _seasonal_naive_expect(netinc), _TD_YEAR)


def gds_022_netinc_ewm_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs EWM-trend expectation (span=252, shifted 1Q)."""
    return _miss(netinc, _ewm_trend_expect(netinc, _TD_YEAR))


def gds_023_netinc_lintrend_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs linear-trend extrapolation over 4Q window."""
    return netinc - _linear_trend_extrap(netinc, _TD_YEAR)


def gds_024_netinc_miss_direction(netinc: pd.Series) -> pd.Series:
    """Sign of naive-miss for net income: +1 beat, -1 miss, 0 exact."""
    m = netinc - _naive_expect(netinc)
    return np.sign(m)


def gds_025_netinc_miss_sign_flip(netinc: pd.Series) -> pd.Series:
    """1 when miss direction flips (beat-to-miss or miss-to-beat) vs prior quarter."""
    sign = np.sign(netinc - _naive_expect(netinc))
    return (sign != sign.shift(_TD_QTR)).astype(float)


def gds_026_netinc_consecutive_miss(netinc: pd.Series) -> pd.Series:
    """Consecutive negative naive-miss quarters for net income (streak in daily obs)."""
    miss_int = ((netinc - _naive_expect(netinc)) < 0).astype(int).values
    streak = np.zeros(len(miss_int), dtype=float)
    for i in range(1, len(miss_int)):
        streak[i] = (streak[i - 1] + 1) * miss_int[i]
    return pd.Series(streak, index=netinc.index)


def gds_027_eps_naive_miss(eps: pd.Series) -> pd.Series:
    """EPS naive-miss: actual minus last-quarter expectation."""
    return _miss(eps, _naive_expect(eps))


def gds_028_eps_naive_miss_norm(eps: pd.Series) -> pd.Series:
    """EPS naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(eps, _naive_expect(eps))


def gds_029_eps_seasonal_miss(eps: pd.Series) -> pd.Series:
    """EPS seasonal-naive miss (vs same quarter last year)."""
    return _miss(eps, _seasonal_naive_expect(eps))


def gds_030_eps_sue_naive(eps: pd.Series) -> pd.Series:
    """SUE-style score for EPS: naive miss / trailing 4Q EPS std."""
    return _miss_norm_vol(eps, _naive_expect(eps), _TD_YEAR)


# --- Group C (031-045): EPS diluted, gross profit, operating income miss ---

def gds_031_epsdil_naive_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS naive-miss (absolute)."""
    return _miss(epsdil, _naive_expect(epsdil))


def gds_032_epsdil_seasonal_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS seasonal-naive miss."""
    return _miss(epsdil, _seasonal_naive_expect(epsdil))


def gds_033_epsdil_sue_naive(epsdil: pd.Series) -> pd.Series:
    """SUE-style score for diluted EPS: naive miss / trailing 4Q std."""
    return _miss_norm_vol(epsdil, _naive_expect(epsdil), _TD_YEAR)


def gds_034_epsdil_ewm_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS miss vs EWM-trend expectation."""
    return _miss(epsdil, _ewm_trend_expect(epsdil, _TD_YEAR))


def gds_035_epsdil_lintrend_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS miss vs 4Q linear-trend extrapolation."""
    return epsdil - _linear_trend_extrap(epsdil, _TD_YEAR)


def gds_036_gp_naive_miss(gp: pd.Series) -> pd.Series:
    """Gross profit naive-miss (absolute)."""
    return _miss(gp, _naive_expect(gp))


def gds_037_gp_naive_miss_norm(gp: pd.Series) -> pd.Series:
    """Gross profit naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(gp, _naive_expect(gp))


def gds_038_gp_seasonal_miss(gp: pd.Series) -> pd.Series:
    """Gross profit seasonal-naive miss."""
    return _miss(gp, _seasonal_naive_expect(gp))


def gds_039_gp_sue_naive(gp: pd.Series) -> pd.Series:
    """SUE-style score for gross profit: naive miss / trailing 4Q std."""
    return _miss_norm_vol(gp, _naive_expect(gp), _TD_YEAR)


def gds_040_gp_ewm_miss(gp: pd.Series) -> pd.Series:
    """Gross profit miss vs EWM-trend expectation."""
    return _miss(gp, _ewm_trend_expect(gp, _TD_YEAR))


def gds_041_opinc_naive_miss(opinc: pd.Series) -> pd.Series:
    """Operating income naive-miss (absolute)."""
    return _miss(opinc, _naive_expect(opinc))


def gds_042_opinc_naive_miss_norm(opinc: pd.Series) -> pd.Series:
    """Operating income naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(opinc, _naive_expect(opinc))


def gds_043_opinc_seasonal_miss(opinc: pd.Series) -> pd.Series:
    """Operating income seasonal-naive miss."""
    return _miss(opinc, _seasonal_naive_expect(opinc))


def gds_044_opinc_sue_naive(opinc: pd.Series) -> pd.Series:
    """SUE-style score for operating income."""
    return _miss_norm_vol(opinc, _naive_expect(opinc), _TD_YEAR)


def gds_045_opinc_ewm_miss(opinc: pd.Series) -> pd.Series:
    """Operating income miss vs EWM-trend expectation."""
    return _miss(opinc, _ewm_trend_expect(opinc, _TD_YEAR))


# --- Group D (046-060): EBITDA, FCF, NCFO miss features ---

def gds_046_ebitda_naive_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA naive-miss (absolute)."""
    return _miss(ebitda, _naive_expect(ebitda))


def gds_047_ebitda_naive_miss_norm(ebitda: pd.Series) -> pd.Series:
    """EBITDA naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(ebitda, _naive_expect(ebitda))


def gds_048_ebitda_seasonal_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA seasonal-naive miss."""
    return _miss(ebitda, _seasonal_naive_expect(ebitda))


def gds_049_ebitda_sue_naive(ebitda: pd.Series) -> pd.Series:
    """SUE-style score for EBITDA."""
    return _miss_norm_vol(ebitda, _naive_expect(ebitda), _TD_YEAR)


def gds_050_ebitda_lintrend_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA miss vs 4Q linear-trend extrapolation."""
    return ebitda - _linear_trend_extrap(ebitda, _TD_YEAR)


def gds_051_fcf_naive_miss(fcf: pd.Series) -> pd.Series:
    """Free cash flow naive-miss (absolute)."""
    return _miss(fcf, _naive_expect(fcf))


def gds_052_fcf_naive_miss_norm(fcf: pd.Series) -> pd.Series:
    """FCF naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(fcf, _naive_expect(fcf))


def gds_053_fcf_seasonal_miss(fcf: pd.Series) -> pd.Series:
    """FCF seasonal-naive miss."""
    return _miss(fcf, _seasonal_naive_expect(fcf))


def gds_054_fcf_sue_naive(fcf: pd.Series) -> pd.Series:
    """SUE-style score for FCF."""
    return _miss_norm_vol(fcf, _naive_expect(fcf), _TD_YEAR)


def gds_055_fcf_ewm_miss(fcf: pd.Series) -> pd.Series:
    """FCF miss vs EWM-trend expectation."""
    return _miss(fcf, _ewm_trend_expect(fcf, _TD_YEAR))


def gds_056_ncfo_naive_miss(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow naive-miss (absolute)."""
    return _miss(ncfo, _naive_expect(ncfo))


def gds_057_ncfo_naive_miss_norm(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow naive-miss normalized by abs(naive expectation)."""
    return _miss_norm_magnitude(ncfo, _naive_expect(ncfo))


def gds_058_ncfo_seasonal_miss(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow seasonal-naive miss."""
    return _miss(ncfo, _seasonal_naive_expect(ncfo))


def gds_059_ncfo_sue_naive(ncfo: pd.Series) -> pd.Series:
    """SUE-style score for operating cash flow."""
    return _miss_norm_vol(ncfo, _naive_expect(ncfo), _TD_YEAR)


def gds_060_ncfo_ewm_miss(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow miss vs EWM-trend expectation."""
    return _miss(ncfo, _ewm_trend_expect(ncfo, _TD_YEAR))


# --- Group E (061-075): Multi-metric miss severity, buckets, composite ---

def gds_061_rev_miss_severity_bucket(revenue: pd.Series) -> pd.Series:
    """
    Bucketed miss severity for revenue naive-miss:
    0 = beat/inline, 1 = miss < 5%, 2 = miss 5-15%, 3 = miss > 15%.
    Normalized by abs(naive expectation).
    """
    norm_miss = _miss_norm_magnitude(revenue, _naive_expect(revenue))
    out = pd.Series(0.0, index=revenue.index)
    out = out.where(norm_miss >= -0.05, 1.0)
    out = out.where(norm_miss >= -0.15, 2.0)
    out = out.where(norm_miss >= 0.0, out)
    # rebuild cleanly
    b = pd.Series(0.0, index=revenue.index)
    b[norm_miss < 0.0]   = 1.0
    b[norm_miss < -0.05] = 2.0
    b[norm_miss < -0.15] = 3.0
    return b


def gds_062_netinc_miss_severity_bucket(netinc: pd.Series) -> pd.Series:
    """
    Bucketed miss severity for net income naive-miss normalized by abs(expectation):
    0 = beat, 1 = small miss (<5%), 2 = moderate (5-15%), 3 = severe (>15%).
    """
    norm_miss = _miss_norm_magnitude(netinc, _naive_expect(netinc))
    b = pd.Series(0.0, index=netinc.index)
    b[norm_miss < 0.0]   = 1.0
    b[norm_miss < -0.05] = 2.0
    b[norm_miss < -0.15] = 3.0
    return b


def gds_063_eps_miss_severity_bucket(eps: pd.Series) -> pd.Series:
    """Bucketed miss severity for EPS naive-miss (0=beat, 1=small, 2=mod, 3=severe)."""
    norm_miss = _miss_norm_magnitude(eps, _naive_expect(eps))
    b = pd.Series(0.0, index=eps.index)
    b[norm_miss < 0.0]   = 1.0
    b[norm_miss < -0.05] = 2.0
    b[norm_miss < -0.15] = 3.0
    return b


def gds_064_multi_metric_miss_flag(revenue: pd.Series, netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """1 when all three of revenue, net income, and EPS have a naive-miss simultaneously."""
    rev_miss  = (revenue - _naive_expect(revenue)) < 0
    ni_miss   = (netinc  - _naive_expect(netinc))  < 0
    eps_miss  = (eps     - _naive_expect(eps))      < 0
    return (rev_miss & ni_miss & eps_miss).astype(float)


def gds_065_miss_count_5metrics(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                  gp: pd.Series, opinc: pd.Series) -> pd.Series:
    """Count of metrics (0-5) that have a negative naive-miss in current period."""
    flags = [
        ((revenue - _naive_expect(revenue)) < 0).astype(float),
        ((netinc  - _naive_expect(netinc))  < 0).astype(float),
        ((eps     - _naive_expect(eps))     < 0).astype(float),
        ((gp      - _naive_expect(gp))      < 0).astype(float),
        ((opinc   - _naive_expect(opinc))   < 0).astype(float),
    ]
    return sum(flags)


def gds_066_rev_miss_pct_rank_8q(revenue: pd.Series) -> pd.Series:
    """
    Percentile rank of the current revenue naive-miss within its own
    trailing 8q (504-day) window.  Low rank = miss is near its recent worst.
    """
    m = revenue - _naive_expect(revenue)
    return m.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def gds_067_netinc_miss_pct_rank_8q(netinc: pd.Series) -> pd.Series:
    """
    Percentile rank of the current net income naive-miss within its own
    trailing 8q (504-day) window.  Low rank = miss is near its recent worst.
    """
    m = netinc - _naive_expect(netinc)
    return m.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def gds_068_eps_miss_pct_rank_8q(eps: pd.Series) -> pd.Series:
    """
    Percentile rank of the current EPS naive-miss within its own
    trailing 8q (504-day) window.  Low rank = miss is near its recent worst.
    """
    m = eps - _naive_expect(eps)
    return m.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def gds_069_rev_miss_distance_to_worst_8q(revenue: pd.Series) -> pd.Series:
    """
    Distance of current revenue naive-miss from its trailing 8q minimum
    (worst miss in last 8 quarters).  Zero = at record miss for the window;
    positive = some improvement from the worst point.
    """
    m = revenue - _naive_expect(revenue)
    worst = _rolling_min(m, _TD_2Y)
    return m - worst


def gds_070_netinc_miss_distance_to_worst_8q(netinc: pd.Series) -> pd.Series:
    """
    Distance of current net income naive-miss from its trailing 8q minimum.
    Zero = at record miss for the window; positive = improvement from worst point.
    """
    m = netinc - _naive_expect(netinc)
    worst = _rolling_min(m, _TD_2Y)
    return m - worst


def gds_071_cumulative_rev_miss_8q(revenue: pd.Series) -> pd.Series:
    """Cumulative naive-miss of revenue over trailing 8 quarters (504 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_sum(m, _TD_2Y)


def gds_072_cumulative_netinc_miss_8q(netinc: pd.Series) -> pd.Series:
    """Cumulative naive-miss of net income over trailing 8 quarters."""
    m = netinc - _naive_expect(netinc)
    return _rolling_sum(m, _TD_2Y)


def gds_073_rev_vs_netinc_miss_gap(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Difference between revenue naive-miss (norm) and net income naive-miss (norm).
    Revenue beating while earnings miss signals margin compression.
    """
    rev_miss_n = _miss_norm_magnitude(revenue, _naive_expect(revenue))
    ni_miss_n  = _miss_norm_magnitude(netinc,  _naive_expect(netinc))
    return rev_miss_n - ni_miss_n


def gds_074_composite_sue_score(revenue: pd.Series, netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """
    Composite SUE-style distress score: equal-weighted average of SUE scores for
    revenue, net income, and EPS (naive-miss / trailing 4Q std each).
    More negative = broader earnings distress.
    """
    sue_rev = _miss_norm_vol(revenue, _naive_expect(revenue), _TD_YEAR)
    sue_ni  = _miss_norm_vol(netinc,  _naive_expect(netinc),  _TD_YEAR)
    sue_eps = _miss_norm_vol(eps,     _naive_expect(eps),      _TD_YEAR)
    return (sue_rev + sue_ni + sue_eps) / 3.0


def gds_075_expanding_worst_miss_netinc(netinc: pd.Series) -> pd.Series:
    """Expanding all-history worst (minimum) naive-miss for net income."""
    m = netinc - _naive_expect(netinc)
    return m.expanding(min_periods=1).min()


# --- Group F-ext (151-175): Additional miss transforms, windows, and cross-metric ---

def gds_151_rev_naive_miss_2q_diff(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss change over 2 quarters (half-year miss acceleration)."""
    m = revenue - _naive_expect(revenue)
    return m - m.shift(_TD_2Q)


def gds_152_eps_lintrend_miss_norm(eps: pd.Series) -> pd.Series:
    """EPS linear-trend miss normalized by abs(trend expectation)."""
    expect = _linear_trend_extrap(eps, _TD_YEAR)
    return _miss_norm_magnitude(eps, expect)


def gds_153_epsdil_trail_avg_miss_norm(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS miss vs 4Q trailing-average expectation, normalized by abs(avg)."""
    return _miss_norm_magnitude(epsdil, _trail_avg_expect(epsdil, _TD_YEAR))


def gds_154_gp_trail_med_miss(gp: pd.Series) -> pd.Series:
    """Gross profit miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(gp, _trail_med_expect(gp, _TD_YEAR))


def gds_155_opinc_trail_med_miss(opinc: pd.Series) -> pd.Series:
    """Operating income miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(opinc, _trail_med_expect(opinc, _TD_YEAR))


def gds_156_ebitda_trail_med_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(ebitda, _trail_med_expect(ebitda, _TD_YEAR))


def gds_157_fcf_trail_med_miss(fcf: pd.Series) -> pd.Series:
    """FCF miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(fcf, _trail_med_expect(fcf, _TD_YEAR))


def gds_158_ncfo_trail_med_miss(ncfo: pd.Series) -> pd.Series:
    """Operating CF miss vs 4Q trailing-median expectation (absolute)."""
    return _miss(ncfo, _trail_med_expect(ncfo, _TD_YEAR))


def gds_159_rev_miss_2q_rolling_min(revenue: pd.Series) -> pd.Series:
    """Worst naive-miss of revenue in trailing 2Q (126 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_min(m, _TD_2Q)


def gds_160_netinc_miss_2q_rolling_min(netinc: pd.Series) -> pd.Series:
    """Worst naive-miss of net income in trailing 2Q (126 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_min(m, _TD_2Q)


def gds_161_eps_miss_2q_rolling_min(eps: pd.Series) -> pd.Series:
    """Worst naive-miss of EPS in trailing 2Q (126 days)."""
    m = eps - _naive_expect(eps)
    return _rolling_min(m, _TD_2Q)


def gds_162_rev_miss_ewm_deviation(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss minus its own EWM (span=4Q): current miss vs smoothed miss."""
    m = revenue - _naive_expect(revenue)
    return m - _ewm_mean(m, _TD_YEAR)


def gds_163_netinc_miss_ewm_deviation(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss minus its own EWM: current miss vs smoothed miss."""
    m = netinc - _naive_expect(netinc)
    return m - _ewm_mean(m, _TD_YEAR)


def gds_164_eps_miss_ewm_deviation(eps: pd.Series) -> pd.Series:
    """EPS naive-miss minus its own EWM: current miss vs smoothed miss."""
    m = eps - _naive_expect(eps)
    return m - _ewm_mean(m, _TD_YEAR)


def gds_165_rev_miss_rolling_max_4q(revenue: pd.Series) -> pd.Series:
    """Best (highest) naive-miss of revenue in trailing 4Q (252 days)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_max(m, _TD_YEAR)


def gds_166_netinc_miss_rolling_max_4q(netinc: pd.Series) -> pd.Series:
    """Best naive-miss of net income in trailing 4Q (252 days)."""
    m = netinc - _naive_expect(netinc)
    return _rolling_max(m, _TD_YEAR)


def gds_167_rev_miss_range_4q(revenue: pd.Series) -> pd.Series:
    """Range (max minus min) of revenue naive-miss over trailing 4Q: miss volatility."""
    m = revenue - _naive_expect(revenue)
    return _rolling_max(m, _TD_YEAR) - _rolling_min(m, _TD_YEAR)


def gds_168_netinc_miss_range_4q(netinc: pd.Series) -> pd.Series:
    """Range of net income naive-miss over trailing 4Q."""
    m = netinc - _naive_expect(netinc)
    return _rolling_max(m, _TD_YEAR) - _rolling_min(m, _TD_YEAR)


def gds_169_eps_miss_range_4q(eps: pd.Series) -> pd.Series:
    """Range of EPS naive-miss over trailing 4Q."""
    m = eps - _naive_expect(eps)
    return _rolling_max(m, _TD_YEAR) - _rolling_min(m, _TD_YEAR)


def gds_170_gp_miss_pct_rank_4q(gp: pd.Series) -> pd.Series:
    """Percentile rank of gross profit naive-miss within trailing 4Q window."""
    m = gp - _naive_expect(gp)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_171_opinc_miss_pct_rank_4q(opinc: pd.Series) -> pd.Series:
    """Percentile rank of operating income naive-miss within trailing 4Q window."""
    m = opinc - _naive_expect(opinc)
    return m.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def gds_172_rev_miss_median_4q(revenue: pd.Series) -> pd.Series:
    """Median naive-miss of revenue over trailing 4Q (central tendency of miss)."""
    m = revenue - _naive_expect(revenue)
    return _rolling_median(m, _TD_YEAR)


def gds_173_netinc_miss_median_4q(netinc: pd.Series) -> pd.Series:
    """Median naive-miss of net income over trailing 4Q."""
    m = netinc - _naive_expect(netinc)
    return _rolling_median(m, _TD_YEAR)


def gds_174_eps_vs_epsdil_miss_gap(eps: pd.Series, epsdil: pd.Series) -> pd.Series:
    """Difference between EPS naive-miss and diluted EPS naive-miss (dilution signal)."""
    return (eps - _naive_expect(eps)) - (epsdil - _naive_expect(epsdil))


def gds_175_fcf_vs_ncfo_miss_gap(fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    """FCF naive-miss minus operating CF naive-miss (capex-intensity of miss)."""
    return (fcf - _naive_expect(fcf)) - (ncfo - _naive_expect(ncfo))


# ── Registry 001-075 ──────────────────────────────────────────────────────────

GUIDANCE_DISTRESS_REGISTRY_001_075 = {
    "gds_001_rev_naive_miss":              {"inputs": ["revenue"],                          "func": gds_001_rev_naive_miss},
    "gds_002_rev_naive_miss_norm":         {"inputs": ["revenue"],                          "func": gds_002_rev_naive_miss_norm},
    "gds_003_rev_seasonal_miss":           {"inputs": ["revenue"],                          "func": gds_003_rev_seasonal_miss},
    "gds_004_rev_seasonal_miss_norm":      {"inputs": ["revenue"],                          "func": gds_004_rev_seasonal_miss_norm},
    "gds_005_rev_trail_avg_miss":          {"inputs": ["revenue"],                          "func": gds_005_rev_trail_avg_miss},
    "gds_006_rev_trail_avg_miss_norm":     {"inputs": ["revenue"],                          "func": gds_006_rev_trail_avg_miss_norm},
    "gds_007_rev_ewm_miss":                {"inputs": ["revenue"],                          "func": gds_007_rev_ewm_miss},
    "gds_008_rev_ewm_miss_norm":           {"inputs": ["revenue"],                          "func": gds_008_rev_ewm_miss_norm},
    "gds_009_rev_naive_miss_vol_norm":     {"inputs": ["revenue"],                          "func": gds_009_rev_naive_miss_vol_norm},
    "gds_010_rev_seasonal_miss_vol_norm":  {"inputs": ["revenue"],                          "func": gds_010_rev_seasonal_miss_vol_norm},
    "gds_011_rev_lintrend_miss":           {"inputs": ["revenue"],                          "func": gds_011_rev_lintrend_miss},
    "gds_012_rev_lintrend_miss_norm":      {"inputs": ["revenue"],                          "func": gds_012_rev_lintrend_miss_norm},
    "gds_013_rev_consecutive_miss_streak": {"inputs": ["revenue"],                          "func": gds_013_rev_consecutive_miss_streak},
    "gds_014_rev_miss_worst_4q":           {"inputs": ["revenue"],                          "func": gds_014_rev_miss_worst_4q},
    "gds_015_rev_cumulative_miss_4q":      {"inputs": ["revenue"],                          "func": gds_015_rev_cumulative_miss_4q},
    "gds_016_netinc_naive_miss":           {"inputs": ["netinc"],                           "func": gds_016_netinc_naive_miss},
    "gds_017_netinc_naive_miss_norm":      {"inputs": ["netinc"],                           "func": gds_017_netinc_naive_miss_norm},
    "gds_018_netinc_seasonal_miss":        {"inputs": ["netinc"],                           "func": gds_018_netinc_seasonal_miss},
    "gds_019_netinc_seasonal_miss_norm":   {"inputs": ["netinc"],                           "func": gds_019_netinc_seasonal_miss_norm},
    "gds_020_netinc_sue_naive":            {"inputs": ["netinc"],                           "func": gds_020_netinc_sue_naive},
    "gds_021_netinc_sue_seasonal":         {"inputs": ["netinc"],                           "func": gds_021_netinc_sue_seasonal},
    "gds_022_netinc_ewm_miss":             {"inputs": ["netinc"],                           "func": gds_022_netinc_ewm_miss},
    "gds_023_netinc_lintrend_miss":        {"inputs": ["netinc"],                           "func": gds_023_netinc_lintrend_miss},
    "gds_024_netinc_miss_direction":       {"inputs": ["netinc"],                           "func": gds_024_netinc_miss_direction},
    "gds_025_netinc_miss_sign_flip":       {"inputs": ["netinc"],                           "func": gds_025_netinc_miss_sign_flip},
    "gds_026_netinc_consecutive_miss":     {"inputs": ["netinc"],                           "func": gds_026_netinc_consecutive_miss},
    "gds_027_eps_naive_miss":              {"inputs": ["eps"],                              "func": gds_027_eps_naive_miss},
    "gds_028_eps_naive_miss_norm":         {"inputs": ["eps"],                              "func": gds_028_eps_naive_miss_norm},
    "gds_029_eps_seasonal_miss":           {"inputs": ["eps"],                              "func": gds_029_eps_seasonal_miss},
    "gds_030_eps_sue_naive":               {"inputs": ["eps"],                              "func": gds_030_eps_sue_naive},
    "gds_031_epsdil_naive_miss":           {"inputs": ["epsdil"],                           "func": gds_031_epsdil_naive_miss},
    "gds_032_epsdil_seasonal_miss":        {"inputs": ["epsdil"],                           "func": gds_032_epsdil_seasonal_miss},
    "gds_033_epsdil_sue_naive":            {"inputs": ["epsdil"],                           "func": gds_033_epsdil_sue_naive},
    "gds_034_epsdil_ewm_miss":             {"inputs": ["epsdil"],                           "func": gds_034_epsdil_ewm_miss},
    "gds_035_epsdil_lintrend_miss":        {"inputs": ["epsdil"],                           "func": gds_035_epsdil_lintrend_miss},
    "gds_036_gp_naive_miss":               {"inputs": ["gp"],                               "func": gds_036_gp_naive_miss},
    "gds_037_gp_naive_miss_norm":          {"inputs": ["gp"],                               "func": gds_037_gp_naive_miss_norm},
    "gds_038_gp_seasonal_miss":            {"inputs": ["gp"],                               "func": gds_038_gp_seasonal_miss},
    "gds_039_gp_sue_naive":                {"inputs": ["gp"],                               "func": gds_039_gp_sue_naive},
    "gds_040_gp_ewm_miss":                 {"inputs": ["gp"],                               "func": gds_040_gp_ewm_miss},
    "gds_041_opinc_naive_miss":            {"inputs": ["opinc"],                            "func": gds_041_opinc_naive_miss},
    "gds_042_opinc_naive_miss_norm":       {"inputs": ["opinc"],                            "func": gds_042_opinc_naive_miss_norm},
    "gds_043_opinc_seasonal_miss":         {"inputs": ["opinc"],                            "func": gds_043_opinc_seasonal_miss},
    "gds_044_opinc_sue_naive":             {"inputs": ["opinc"],                            "func": gds_044_opinc_sue_naive},
    "gds_045_opinc_ewm_miss":              {"inputs": ["opinc"],                            "func": gds_045_opinc_ewm_miss},
    "gds_046_ebitda_naive_miss":           {"inputs": ["ebitda"],                           "func": gds_046_ebitda_naive_miss},
    "gds_047_ebitda_naive_miss_norm":      {"inputs": ["ebitda"],                           "func": gds_047_ebitda_naive_miss_norm},
    "gds_048_ebitda_seasonal_miss":        {"inputs": ["ebitda"],                           "func": gds_048_ebitda_seasonal_miss},
    "gds_049_ebitda_sue_naive":            {"inputs": ["ebitda"],                           "func": gds_049_ebitda_sue_naive},
    "gds_050_ebitda_lintrend_miss":        {"inputs": ["ebitda"],                           "func": gds_050_ebitda_lintrend_miss},
    "gds_051_fcf_naive_miss":              {"inputs": ["fcf"],                              "func": gds_051_fcf_naive_miss},
    "gds_052_fcf_naive_miss_norm":         {"inputs": ["fcf"],                              "func": gds_052_fcf_naive_miss_norm},
    "gds_053_fcf_seasonal_miss":           {"inputs": ["fcf"],                              "func": gds_053_fcf_seasonal_miss},
    "gds_054_fcf_sue_naive":               {"inputs": ["fcf"],                              "func": gds_054_fcf_sue_naive},
    "gds_055_fcf_ewm_miss":                {"inputs": ["fcf"],                              "func": gds_055_fcf_ewm_miss},
    "gds_056_ncfo_naive_miss":             {"inputs": ["ncfo"],                             "func": gds_056_ncfo_naive_miss},
    "gds_057_ncfo_naive_miss_norm":        {"inputs": ["ncfo"],                             "func": gds_057_ncfo_naive_miss_norm},
    "gds_058_ncfo_seasonal_miss":          {"inputs": ["ncfo"],                             "func": gds_058_ncfo_seasonal_miss},
    "gds_059_ncfo_sue_naive":              {"inputs": ["ncfo"],                             "func": gds_059_ncfo_sue_naive},
    "gds_060_ncfo_ewm_miss":               {"inputs": ["ncfo"],                             "func": gds_060_ncfo_ewm_miss},
    "gds_061_rev_miss_severity_bucket":    {"inputs": ["revenue"],                          "func": gds_061_rev_miss_severity_bucket},
    "gds_062_netinc_miss_severity_bucket": {"inputs": ["netinc"],                           "func": gds_062_netinc_miss_severity_bucket},
    "gds_063_eps_miss_severity_bucket":    {"inputs": ["eps"],                              "func": gds_063_eps_miss_severity_bucket},
    "gds_064_multi_metric_miss_flag":      {"inputs": ["revenue", "netinc", "eps"],         "func": gds_064_multi_metric_miss_flag},
    "gds_065_miss_count_5metrics":         {"inputs": ["revenue", "netinc", "eps", "gp", "opinc"], "func": gds_065_miss_count_5metrics},
    "gds_066_rev_miss_pct_rank_8q":        {"inputs": ["revenue"],                          "func": gds_066_rev_miss_pct_rank_8q},
    "gds_067_netinc_miss_pct_rank_8q":    {"inputs": ["netinc"],                           "func": gds_067_netinc_miss_pct_rank_8q},
    "gds_068_eps_miss_pct_rank_8q":       {"inputs": ["eps"],                              "func": gds_068_eps_miss_pct_rank_8q},
    "gds_069_rev_miss_distance_to_worst_8q": {"inputs": ["revenue"],                       "func": gds_069_rev_miss_distance_to_worst_8q},
    "gds_070_netinc_miss_distance_to_worst_8q": {"inputs": ["netinc"],                     "func": gds_070_netinc_miss_distance_to_worst_8q},
    "gds_071_cumulative_rev_miss_8q":      {"inputs": ["revenue"],                          "func": gds_071_cumulative_rev_miss_8q},
    "gds_072_cumulative_netinc_miss_8q":   {"inputs": ["netinc"],                           "func": gds_072_cumulative_netinc_miss_8q},
    "gds_073_rev_vs_netinc_miss_gap":      {"inputs": ["revenue", "netinc"],                "func": gds_073_rev_vs_netinc_miss_gap},
    "gds_074_composite_sue_score":         {"inputs": ["revenue", "netinc", "eps"],         "func": gds_074_composite_sue_score},
    "gds_075_expanding_worst_miss_netinc": {"inputs": ["netinc"],                           "func": gds_075_expanding_worst_miss_netinc},
    "gds_151_rev_naive_miss_2q_diff":      {"inputs": ["revenue"],                          "func": gds_151_rev_naive_miss_2q_diff},
    "gds_152_eps_lintrend_miss_norm":      {"inputs": ["eps"],                              "func": gds_152_eps_lintrend_miss_norm},
    "gds_153_epsdil_trail_avg_miss_norm":  {"inputs": ["epsdil"],                           "func": gds_153_epsdil_trail_avg_miss_norm},
    "gds_154_gp_trail_med_miss":           {"inputs": ["gp"],                               "func": gds_154_gp_trail_med_miss},
    "gds_155_opinc_trail_med_miss":        {"inputs": ["opinc"],                            "func": gds_155_opinc_trail_med_miss},
    "gds_156_ebitda_trail_med_miss":       {"inputs": ["ebitda"],                           "func": gds_156_ebitda_trail_med_miss},
    "gds_157_fcf_trail_med_miss":          {"inputs": ["fcf"],                              "func": gds_157_fcf_trail_med_miss},
    "gds_158_ncfo_trail_med_miss":         {"inputs": ["ncfo"],                             "func": gds_158_ncfo_trail_med_miss},
    "gds_159_rev_miss_2q_rolling_min":     {"inputs": ["revenue"],                          "func": gds_159_rev_miss_2q_rolling_min},
    "gds_160_netinc_miss_2q_rolling_min":  {"inputs": ["netinc"],                           "func": gds_160_netinc_miss_2q_rolling_min},
    "gds_161_eps_miss_2q_rolling_min":     {"inputs": ["eps"],                              "func": gds_161_eps_miss_2q_rolling_min},
    "gds_162_rev_miss_ewm_deviation":      {"inputs": ["revenue"],                          "func": gds_162_rev_miss_ewm_deviation},
    "gds_163_netinc_miss_ewm_deviation":   {"inputs": ["netinc"],                           "func": gds_163_netinc_miss_ewm_deviation},
    "gds_164_eps_miss_ewm_deviation":      {"inputs": ["eps"],                              "func": gds_164_eps_miss_ewm_deviation},
    "gds_165_rev_miss_rolling_max_4q":     {"inputs": ["revenue"],                          "func": gds_165_rev_miss_rolling_max_4q},
    "gds_166_netinc_miss_rolling_max_4q":  {"inputs": ["netinc"],                           "func": gds_166_netinc_miss_rolling_max_4q},
    "gds_167_rev_miss_range_4q":           {"inputs": ["revenue"],                          "func": gds_167_rev_miss_range_4q},
    "gds_168_netinc_miss_range_4q":        {"inputs": ["netinc"],                           "func": gds_168_netinc_miss_range_4q},
    "gds_169_eps_miss_range_4q":           {"inputs": ["eps"],                              "func": gds_169_eps_miss_range_4q},
    "gds_170_gp_miss_pct_rank_4q":         {"inputs": ["gp"],                               "func": gds_170_gp_miss_pct_rank_4q},
    "gds_171_opinc_miss_pct_rank_4q":      {"inputs": ["opinc"],                            "func": gds_171_opinc_miss_pct_rank_4q},
    "gds_172_rev_miss_median_4q":          {"inputs": ["revenue"],                          "func": gds_172_rev_miss_median_4q},
    "gds_173_netinc_miss_median_4q":       {"inputs": ["netinc"],                           "func": gds_173_netinc_miss_median_4q},
    "gds_174_eps_vs_epsdil_miss_gap":      {"inputs": ["eps", "epsdil"],                    "func": gds_174_eps_vs_epsdil_miss_gap},
    "gds_175_fcf_vs_ncfo_miss_gap":        {"inputs": ["fcf", "ncfo"],                      "func": gds_175_fcf_vs_ncfo_miss_gap},
}
