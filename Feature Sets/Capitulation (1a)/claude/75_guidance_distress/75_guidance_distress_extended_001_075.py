"""
75_guidance_distress — Extended Features 001-075
Domain: estimate-vs-actual gaps, miss severity — additional miss-model proxies,
        new windows, cross-metric miss confluence, miss-streak and miss-acceleration variants
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These are EXTENDED features in the guidance-distress domain: net-new variants that
do NOT duplicate base_001_075, base_076_150, 2nd_derivatives or 3rd_derivatives.
They explore additional expectation models (trailing-min naive, drift-extrapolated,
damped-trend), new lookback windows (1Q, 3Q, 12Q), miss-of-margin metrics, and
cross-metric miss confluence and breadth.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
forward-filled from the most recent quarterly Sharadar SF1 report known as of
each date.  A forward-filled quarterly series steps at most 4 times per year;
flat stretches between report dates are correct and expected.  Functions look
strictly backward using .shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days, 1 year = 252.
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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _consec_neg_streak(s: pd.Series) -> pd.Series:
    """Consecutive-row streak of negative values in s (backward-looking)."""
    arr = (s < 0).astype(int).values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=s.index)


# ── Expectation model helpers ─────────────────────────────────────────────────

def _naive_expect(s: pd.Series) -> pd.Series:
    """Random-walk / last-quarter naive expectation: shift by one quarter."""
    return s.shift(_TD_QTR)


def _seasonal_naive_expect(s: pd.Series) -> pd.Series:
    """Seasonal-naive expectation: same quarter last year (252-day shift)."""
    return s.shift(_TD_YEAR)


def _trail_min_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-minimum expectation: rolling min of past w days, shifted 1Q."""
    return _rolling_min(s, w).shift(_TD_QTR)


def _trail_max_expect(s: pd.Series, w: int) -> pd.Series:
    """Trailing-maximum expectation: rolling max of past w days, shifted 1Q."""
    return _rolling_max(s, w).shift(_TD_QTR)


def _drift_expect(s: pd.Series) -> pd.Series:
    """Drift expectation: last quarter value plus the prior QoQ change (random-walk with drift)."""
    last = s.shift(_TD_QTR)
    drift = s.shift(_TD_QTR) - s.shift(_TD_2Q)
    return last + drift


def _damped_trend_expect(s: pd.Series, damp: float = 0.5) -> pd.Series:
    """Damped-trend expectation: last value plus damped prior QoQ change."""
    last = s.shift(_TD_QTR)
    drift = s.shift(_TD_QTR) - s.shift(_TD_2Q)
    return last + damp * drift


def _avg2model_expect(s: pd.Series) -> pd.Series:
    """Average of naive and seasonal-naive expectations (ensemble model)."""
    return (s.shift(_TD_QTR) + s.shift(_TD_YEAR)) / 2.0


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

# --- Group A (001-012): Drift-model and damped-trend miss variants ---

def gds_ext_001_rev_drift_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs random-walk-with-drift expectation (absolute)."""
    return _miss(revenue, _drift_expect(revenue))


def gds_ext_002_rev_drift_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue drift-model miss normalized by abs(drift expectation)."""
    return _miss_norm_magnitude(revenue, _drift_expect(revenue))


def gds_ext_003_netinc_drift_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs random-walk-with-drift expectation (absolute)."""
    return _miss(netinc, _drift_expect(netinc))


def gds_ext_004_netinc_drift_miss_norm(netinc: pd.Series) -> pd.Series:
    """Net income drift-model miss normalized by abs(drift expectation)."""
    return _miss_norm_magnitude(netinc, _drift_expect(netinc))


def gds_ext_005_eps_drift_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs random-walk-with-drift expectation (absolute)."""
    return _miss(eps, _drift_expect(eps))


def gds_ext_006_rev_damped_trend_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs damped-trend expectation (damp=0.5)."""
    return _miss(revenue, _damped_trend_expect(revenue))


def gds_ext_007_netinc_damped_trend_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs damped-trend expectation (damp=0.5)."""
    return _miss(netinc, _damped_trend_expect(netinc))


def gds_ext_008_eps_damped_trend_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs damped-trend expectation (damp=0.5)."""
    return _miss(eps, _damped_trend_expect(eps))


def gds_ext_009_ebitda_drift_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA miss vs random-walk-with-drift expectation (absolute)."""
    return _miss(ebitda, _drift_expect(ebitda))


def gds_ext_010_fcf_drift_miss(fcf: pd.Series) -> pd.Series:
    """FCF miss vs random-walk-with-drift expectation (absolute)."""
    return _miss(fcf, _drift_expect(fcf))


def gds_ext_011_gp_damped_trend_miss(gp: pd.Series) -> pd.Series:
    """Gross profit miss vs damped-trend expectation (damp=0.5)."""
    return _miss(gp, _damped_trend_expect(gp))


def gds_ext_012_opinc_drift_miss_norm(opinc: pd.Series) -> pd.Series:
    """Operating income drift-model miss normalized by abs(drift expectation)."""
    return _miss_norm_magnitude(opinc, _drift_expect(opinc))


# --- Group B (013-024): Ensemble (avg-of-2-model) miss variants ---

def gds_ext_013_rev_ensemble_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs ensemble of naive + seasonal-naive expectations (absolute)."""
    return _miss(revenue, _avg2model_expect(revenue))


def gds_ext_014_rev_ensemble_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue ensemble-model miss normalized by abs(ensemble expectation)."""
    return _miss_norm_magnitude(revenue, _avg2model_expect(revenue))


def gds_ext_015_netinc_ensemble_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(netinc, _avg2model_expect(netinc))


def gds_ext_016_netinc_ensemble_miss_norm(netinc: pd.Series) -> pd.Series:
    """Net income ensemble-model miss normalized by abs(ensemble expectation)."""
    return _miss_norm_magnitude(netinc, _avg2model_expect(netinc))


def gds_ext_017_eps_ensemble_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(eps, _avg2model_expect(eps))


def gds_ext_018_epsdil_ensemble_miss(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(epsdil, _avg2model_expect(epsdil))


def gds_ext_019_gp_ensemble_miss(gp: pd.Series) -> pd.Series:
    """Gross profit miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(gp, _avg2model_expect(gp))


def gds_ext_020_opinc_ensemble_miss(opinc: pd.Series) -> pd.Series:
    """Operating income miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(opinc, _avg2model_expect(opinc))


def gds_ext_021_ebitda_ensemble_miss(ebitda: pd.Series) -> pd.Series:
    """EBITDA miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(ebitda, _avg2model_expect(ebitda))


def gds_ext_022_fcf_ensemble_miss(fcf: pd.Series) -> pd.Series:
    """FCF miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(fcf, _avg2model_expect(fcf))


def gds_ext_023_ncfo_ensemble_miss(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow miss vs ensemble of naive + seasonal-naive expectations."""
    return _miss(ncfo, _avg2model_expect(ncfo))


def gds_ext_024_ebitda_ensemble_miss_norm(ebitda: pd.Series) -> pd.Series:
    """EBITDA ensemble-model miss normalized by abs(ensemble expectation)."""
    return _miss_norm_magnitude(ebitda, _avg2model_expect(ebitda))


# --- Group C (025-036): Trailing-min / trailing-max expectation miss ---

def gds_ext_025_rev_vs_trail_min_4q(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 4Q minimum expectation (distance above recent floor)."""
    return _miss(revenue, _trail_min_expect(revenue, _TD_YEAR))


def gds_ext_026_netinc_vs_trail_min_4q(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 4Q minimum expectation."""
    return _miss(netinc, _trail_min_expect(netinc, _TD_YEAR))


def gds_ext_027_eps_vs_trail_min_4q(eps: pd.Series) -> pd.Series:
    """EPS minus its trailing 4Q minimum expectation."""
    return _miss(eps, _trail_min_expect(eps, _TD_YEAR))


def gds_ext_028_rev_vs_trail_max_4q(revenue: pd.Series) -> pd.Series:
    """Revenue minus its trailing 4Q maximum expectation (distance below recent ceiling)."""
    return _miss(revenue, _trail_max_expect(revenue, _TD_YEAR))


def gds_ext_029_netinc_vs_trail_max_4q(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 4Q maximum expectation."""
    return _miss(netinc, _trail_max_expect(netinc, _TD_YEAR))


def gds_ext_030_eps_vs_trail_max_8q(eps: pd.Series) -> pd.Series:
    """EPS minus its trailing 8Q maximum expectation."""
    return _miss(eps, _trail_max_expect(eps, _TD_2Y))


def gds_ext_031_gp_vs_trail_min_4q(gp: pd.Series) -> pd.Series:
    """Gross profit minus its trailing 4Q minimum expectation."""
    return _miss(gp, _trail_min_expect(gp, _TD_YEAR))


def gds_ext_032_opinc_vs_trail_min_4q(opinc: pd.Series) -> pd.Series:
    """Operating income minus its trailing 4Q minimum expectation."""
    return _miss(opinc, _trail_min_expect(opinc, _TD_YEAR))


def gds_ext_033_ebitda_vs_trail_min_8q(ebitda: pd.Series) -> pd.Series:
    """EBITDA minus its trailing 8Q minimum expectation."""
    return _miss(ebitda, _trail_min_expect(ebitda, _TD_2Y))


def gds_ext_034_fcf_vs_trail_min_4q(fcf: pd.Series) -> pd.Series:
    """FCF minus its trailing 4Q minimum expectation."""
    return _miss(fcf, _trail_min_expect(fcf, _TD_YEAR))


def gds_ext_035_rev_vs_trail_max_4q_norm(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 4Q maximum expectation, normalized by abs(max)."""
    return _miss_norm_magnitude(revenue, _trail_max_expect(revenue, _TD_YEAR))


def gds_ext_036_netinc_vs_trail_min_8q_norm(netinc: pd.Series) -> pd.Series:
    """Net income vs trailing 8Q minimum expectation, normalized by abs(min)."""
    return _miss_norm_magnitude(netinc, _trail_min_expect(netinc, _TD_2Y))


# --- Group D (037-048): New-window naive miss (3Q lag, 12Q baseline) ---

def gds_ext_037_rev_3q_lag_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs 3-quarter-lag expectation (189-day shift)."""
    return _miss(revenue, revenue.shift(_TD_3Q))


def gds_ext_038_netinc_3q_lag_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs 3-quarter-lag expectation (189-day shift)."""
    return _miss(netinc, netinc.shift(_TD_3Q))


def gds_ext_039_eps_3q_lag_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs 3-quarter-lag expectation (189-day shift)."""
    return _miss(eps, eps.shift(_TD_3Q))


def gds_ext_040_rev_2y_lag_miss(revenue: pd.Series) -> pd.Series:
    """Revenue miss vs 2-year-lag expectation (504-day shift)."""
    return _miss(revenue, revenue.shift(_TD_2Y))


def gds_ext_041_netinc_2y_lag_miss(netinc: pd.Series) -> pd.Series:
    """Net income miss vs 2-year-lag expectation (504-day shift)."""
    return _miss(netinc, netinc.shift(_TD_2Y))


def gds_ext_042_rev_12q_baseline_miss_norm(revenue: pd.Series) -> pd.Series:
    """Revenue vs trailing 12Q mean baseline (shifted 1Q), normalized by abs(baseline)."""
    baseline = _rolling_mean(revenue, _TD_3Y).shift(_TD_QTR)
    return _miss_norm_magnitude(revenue, baseline)


def gds_ext_043_netinc_12q_baseline_miss_norm(netinc: pd.Series) -> pd.Series:
    """Net income vs trailing 12Q mean baseline (shifted 1Q), normalized by abs(baseline)."""
    baseline = _rolling_mean(netinc, _TD_3Y).shift(_TD_QTR)
    return _miss_norm_magnitude(netinc, baseline)


def gds_ext_044_eps_12q_baseline_miss(eps: pd.Series) -> pd.Series:
    """EPS miss vs trailing 12Q mean baseline (shifted 1Q), absolute."""
    baseline = _rolling_mean(eps, _TD_3Y).shift(_TD_QTR)
    return _miss(eps, baseline)


def gds_ext_045_rev_naive_miss_vol_norm_8q(revenue: pd.Series) -> pd.Series:
    """Revenue naive-miss normalized by trailing 8Q revenue volatility (long SUE)."""
    return _miss_norm_vol(revenue, _naive_expect(revenue), _TD_2Y)


def gds_ext_046_netinc_naive_miss_vol_norm_8q(netinc: pd.Series) -> pd.Series:
    """Net income naive-miss normalized by trailing 8Q volatility (long SUE)."""
    return _miss_norm_vol(netinc, _naive_expect(netinc), _TD_2Y)


def gds_ext_047_eps_naive_miss_vol_norm_8q(eps: pd.Series) -> pd.Series:
    """EPS naive-miss normalized by trailing 8Q volatility (long SUE)."""
    return _miss_norm_vol(eps, _naive_expect(eps), _TD_2Y)


def gds_ext_048_rev_seasonal_miss_vol_norm_8q(revenue: pd.Series) -> pd.Series:
    """Revenue seasonal-naive miss normalized by trailing 8Q volatility."""
    return _miss_norm_vol(revenue, _seasonal_naive_expect(revenue), _TD_2Y)


# --- Group E (049-060): Margin-metric miss features ---

def gds_ext_049_gross_margin_naive_miss(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin (gp/revenue) naive-miss vs last-quarter margin."""
    margin = _safe_div(gp, revenue)
    return _miss(margin, _naive_expect(margin))


def gds_ext_050_gross_margin_seasonal_miss(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin seasonal-naive miss vs same-quarter-last-year margin."""
    margin = _safe_div(gp, revenue)
    return _miss(margin, _seasonal_naive_expect(margin))


def gds_ext_051_op_margin_naive_miss(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin (opinc/revenue) naive-miss vs last-quarter margin."""
    margin = _safe_div(opinc, revenue)
    return _miss(margin, _naive_expect(margin))


def gds_ext_052_op_margin_seasonal_miss(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin seasonal-naive miss vs same-quarter-last-year margin."""
    margin = _safe_div(opinc, revenue)
    return _miss(margin, _seasonal_naive_expect(margin))


def gds_ext_053_net_margin_naive_miss(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin (netinc/revenue) naive-miss vs last-quarter margin."""
    margin = _safe_div(netinc, revenue)
    return _miss(margin, _naive_expect(margin))


def gds_ext_054_ebitda_margin_naive_miss(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin (ebitda/revenue) naive-miss vs last-quarter margin."""
    margin = _safe_div(ebitda, revenue)
    return _miss(margin, _naive_expect(margin))


def gds_ext_055_fcf_margin_naive_miss(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """FCF margin (fcf/revenue) naive-miss vs last-quarter margin."""
    margin = _safe_div(fcf, revenue)
    return _miss(margin, _naive_expect(margin))


def gds_ext_056_net_margin_miss_worst_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Worst (most negative) net-margin naive-miss in trailing 4Q."""
    margin = _safe_div(netinc, revenue)
    m = _miss(margin, _naive_expect(margin))
    return _rolling_min(m, _TD_YEAR)


def gds_ext_057_op_margin_miss_cumulative_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cumulative operating-margin naive-miss over trailing 8Q."""
    margin = _safe_div(opinc, revenue)
    m = _miss(margin, _naive_expect(margin))
    return _rolling_sum(m, _TD_2Y)


def gds_ext_058_gross_margin_miss_streak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Consecutive negative gross-margin naive-miss streak (daily-row count)."""
    margin = _safe_div(gp, revenue)
    m = _miss(margin, _naive_expect(margin))
    return _consec_neg_streak(m)


def gds_ext_059_net_margin_miss_zscore_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of net-margin naive-miss within its trailing 8Q distribution."""
    margin = _safe_div(netinc, revenue)
    m = _miss(margin, _naive_expect(margin))
    return _zscore_rolling(m, _TD_2Y)


def gds_ext_060_margin_miss_count_3metrics(gp: pd.Series, opinc: pd.Series,
                                            netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of margins (gross, operating, net) with a negative naive-miss (0-3)."""
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    nm = _safe_div(netinc, revenue)
    f1 = (_miss(gm, _naive_expect(gm)) < 0).astype(float)
    f2 = (_miss(om, _naive_expect(om)) < 0).astype(float)
    f3 = (_miss(nm, _naive_expect(nm)) < 0).astype(float)
    return f1 + f2 + f3


# --- Group F (061-068): Miss-acceleration, persistence and worsening flags ---

def gds_ext_061_rev_miss_qoq_accel(revenue: pd.Series) -> pd.Series:
    """QoQ change in revenue naive-miss (miss acceleration over one quarter)."""
    m = _miss(revenue, _naive_expect(revenue))
    return m - m.shift(_TD_QTR)


def gds_ext_062_netinc_miss_qoq_accel(netinc: pd.Series) -> pd.Series:
    """QoQ change in net income naive-miss (miss acceleration)."""
    m = _miss(netinc, _naive_expect(netinc))
    return m - m.shift(_TD_QTR)


def gds_ext_063_eps_miss_yoy_accel(eps: pd.Series) -> pd.Series:
    """YoY change in EPS naive-miss (year-over-year miss acceleration)."""
    m = _miss(eps, _naive_expect(eps))
    return m - m.shift(_TD_YEAR)


def gds_ext_064_rev_miss_worsening_flag(revenue: pd.Series) -> pd.Series:
    """1 when revenue naive-miss is both negative and worse than one quarter ago."""
    m = _miss(revenue, _naive_expect(revenue))
    return ((m < 0) & (m < m.shift(_TD_QTR))).astype(float)


def gds_ext_065_netinc_miss_worsening_flag(netinc: pd.Series) -> pd.Series:
    """1 when net income naive-miss is both negative and worse than one quarter ago."""
    m = _miss(netinc, _naive_expect(netinc))
    return ((m < 0) & (m < m.shift(_TD_QTR))).astype(float)


def gds_ext_066_rev_miss_negative_quarters_8q(revenue: pd.Series) -> pd.Series:
    """Count of quarters with negative revenue naive-miss over trailing 8Q."""
    m = _miss(revenue, _naive_expect(revenue))
    return _rolling_sum((m < 0).astype(float), _TD_2Y) / float(_TD_QTR)


def gds_ext_067_netinc_miss_negative_fraction_8q(netinc: pd.Series) -> pd.Series:
    """Fraction of trailing 8Q days with a negative net income naive-miss."""
    m = _miss(netinc, _naive_expect(netinc))
    return _rolling_mean((m < 0).astype(float), _TD_2Y)


def gds_ext_068_eps_miss_negative_fraction_4q(eps: pd.Series) -> pd.Series:
    """Fraction of trailing 4Q days with a negative EPS naive-miss."""
    m = _miss(eps, _naive_expect(eps))
    return _rolling_mean((m < 0).astype(float), _TD_YEAR)


# --- Group G (069-075): Cross-metric confluence and composite distress ---

def gds_ext_069_seasonal_miss_count_5metrics(revenue: pd.Series, netinc: pd.Series,
                                              eps: pd.Series, gp: pd.Series,
                                              opinc: pd.Series) -> pd.Series:
    """Count of metrics (0-5) with a negative seasonal-naive miss this period."""
    flags = [
        (_miss(revenue, _seasonal_naive_expect(revenue)) < 0).astype(float),
        (_miss(netinc,  _seasonal_naive_expect(netinc))  < 0).astype(float),
        (_miss(eps,     _seasonal_naive_expect(eps))     < 0).astype(float),
        (_miss(gp,      _seasonal_naive_expect(gp))      < 0).astype(float),
        (_miss(opinc,   _seasonal_naive_expect(opinc))   < 0).astype(float),
    ]
    return sum(flags)


def gds_ext_070_all5_drift_miss_flag(revenue: pd.Series, netinc: pd.Series, eps: pd.Series,
                                      gp: pd.Series, opinc: pd.Series) -> pd.Series:
    """1 when all five metrics have a negative drift-model miss simultaneously."""
    f = ((_miss(revenue, _drift_expect(revenue)) < 0) &
         (_miss(netinc,  _drift_expect(netinc))  < 0) &
         (_miss(eps,     _drift_expect(eps))     < 0) &
         (_miss(gp,      _drift_expect(gp))      < 0) &
         (_miss(opinc,   _drift_expect(opinc))   < 0))
    return f.astype(float)


def gds_ext_071_cashflow_miss_count(fcf: pd.Series, ncfo: pd.Series,
                                     ebitda: pd.Series) -> pd.Series:
    """Count of cash-flow metrics (fcf, ncfo, ebitda) with a negative naive-miss (0-3)."""
    flags = [
        (_miss(fcf,    _naive_expect(fcf))    < 0).astype(float),
        (_miss(ncfo,   _naive_expect(ncfo))   < 0).astype(float),
        (_miss(ebitda, _naive_expect(ebitda)) < 0).astype(float),
    ]
    return sum(flags)


def gds_ext_072_composite_ensemble_sue(revenue: pd.Series, netinc: pd.Series,
                                        eps: pd.Series) -> pd.Series:
    """Composite SUE-style score using ensemble-model miss for revenue/netinc/eps."""
    sue_rev = _miss_norm_vol(revenue, _avg2model_expect(revenue), _TD_YEAR)
    sue_ni  = _miss_norm_vol(netinc,  _avg2model_expect(netinc),  _TD_YEAR)
    sue_eps = _miss_norm_vol(eps,     _avg2model_expect(eps),      _TD_YEAR)
    return (sue_rev + sue_ni + sue_eps) / 3.0


def gds_ext_073_rev_netinc_miss_both_worsening_flag(revenue: pd.Series,
                                                     netinc: pd.Series) -> pd.Series:
    """1 when both revenue and net income naive-miss are negative and worsening QoQ."""
    rm = _miss(revenue, _naive_expect(revenue))
    nm = _miss(netinc,  _naive_expect(netinc))
    rev_w = (rm < 0) & (rm < rm.shift(_TD_QTR))
    ni_w  = (nm < 0) & (nm < nm.shift(_TD_QTR))
    return (rev_w & ni_w).astype(float)


def gds_ext_074_composite_miss_severity_index(revenue: pd.Series, netinc: pd.Series,
                                               eps: pd.Series) -> pd.Series:
    """
    Composite miss-severity index: average of normalized naive-miss magnitudes
    for revenue, net income and EPS, clipped to keep negative misses bounded.
    More negative = broader, deeper distress.
    """
    rev = _miss_norm_magnitude(revenue, _naive_expect(revenue)).clip(-3.0, 3.0)
    ni  = _miss_norm_magnitude(netinc,  _naive_expect(netinc)).clip(-3.0, 3.0)
    eps_n = _miss_norm_magnitude(eps,   _naive_expect(eps)).clip(-3.0, 3.0)
    return (rev + ni + eps_n) / 3.0


def gds_ext_075_expanding_worst_miss_eps(eps: pd.Series) -> pd.Series:
    """Expanding all-history worst (minimum) naive-miss for EPS."""
    m = _miss(eps, _naive_expect(eps))
    return m.expanding(min_periods=1).min()


# ── Registry ──────────────────────────────────────────────────────────────────

GUIDANCE_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "gds_ext_001_rev_drift_miss":                  {"inputs": ["revenue"],                                  "func": gds_ext_001_rev_drift_miss},
    "gds_ext_002_rev_drift_miss_norm":             {"inputs": ["revenue"],                                  "func": gds_ext_002_rev_drift_miss_norm},
    "gds_ext_003_netinc_drift_miss":               {"inputs": ["netinc"],                                   "func": gds_ext_003_netinc_drift_miss},
    "gds_ext_004_netinc_drift_miss_norm":          {"inputs": ["netinc"],                                   "func": gds_ext_004_netinc_drift_miss_norm},
    "gds_ext_005_eps_drift_miss":                  {"inputs": ["eps"],                                      "func": gds_ext_005_eps_drift_miss},
    "gds_ext_006_rev_damped_trend_miss":           {"inputs": ["revenue"],                                  "func": gds_ext_006_rev_damped_trend_miss},
    "gds_ext_007_netinc_damped_trend_miss":        {"inputs": ["netinc"],                                   "func": gds_ext_007_netinc_damped_trend_miss},
    "gds_ext_008_eps_damped_trend_miss":           {"inputs": ["eps"],                                      "func": gds_ext_008_eps_damped_trend_miss},
    "gds_ext_009_ebitda_drift_miss":               {"inputs": ["ebitda"],                                   "func": gds_ext_009_ebitda_drift_miss},
    "gds_ext_010_fcf_drift_miss":                  {"inputs": ["fcf"],                                      "func": gds_ext_010_fcf_drift_miss},
    "gds_ext_011_gp_damped_trend_miss":            {"inputs": ["gp"],                                       "func": gds_ext_011_gp_damped_trend_miss},
    "gds_ext_012_opinc_drift_miss_norm":           {"inputs": ["opinc"],                                    "func": gds_ext_012_opinc_drift_miss_norm},
    "gds_ext_013_rev_ensemble_miss":               {"inputs": ["revenue"],                                  "func": gds_ext_013_rev_ensemble_miss},
    "gds_ext_014_rev_ensemble_miss_norm":          {"inputs": ["revenue"],                                  "func": gds_ext_014_rev_ensemble_miss_norm},
    "gds_ext_015_netinc_ensemble_miss":            {"inputs": ["netinc"],                                   "func": gds_ext_015_netinc_ensemble_miss},
    "gds_ext_016_netinc_ensemble_miss_norm":       {"inputs": ["netinc"],                                   "func": gds_ext_016_netinc_ensemble_miss_norm},
    "gds_ext_017_eps_ensemble_miss":               {"inputs": ["eps"],                                      "func": gds_ext_017_eps_ensemble_miss},
    "gds_ext_018_epsdil_ensemble_miss":            {"inputs": ["epsdil"],                                   "func": gds_ext_018_epsdil_ensemble_miss},
    "gds_ext_019_gp_ensemble_miss":                {"inputs": ["gp"],                                       "func": gds_ext_019_gp_ensemble_miss},
    "gds_ext_020_opinc_ensemble_miss":             {"inputs": ["opinc"],                                    "func": gds_ext_020_opinc_ensemble_miss},
    "gds_ext_021_ebitda_ensemble_miss":            {"inputs": ["ebitda"],                                   "func": gds_ext_021_ebitda_ensemble_miss},
    "gds_ext_022_fcf_ensemble_miss":               {"inputs": ["fcf"],                                      "func": gds_ext_022_fcf_ensemble_miss},
    "gds_ext_023_ncfo_ensemble_miss":              {"inputs": ["ncfo"],                                     "func": gds_ext_023_ncfo_ensemble_miss},
    "gds_ext_024_ebitda_ensemble_miss_norm":       {"inputs": ["ebitda"],                                   "func": gds_ext_024_ebitda_ensemble_miss_norm},
    "gds_ext_025_rev_vs_trail_min_4q":             {"inputs": ["revenue"],                                  "func": gds_ext_025_rev_vs_trail_min_4q},
    "gds_ext_026_netinc_vs_trail_min_4q":          {"inputs": ["netinc"],                                   "func": gds_ext_026_netinc_vs_trail_min_4q},
    "gds_ext_027_eps_vs_trail_min_4q":             {"inputs": ["eps"],                                      "func": gds_ext_027_eps_vs_trail_min_4q},
    "gds_ext_028_rev_vs_trail_max_4q":             {"inputs": ["revenue"],                                  "func": gds_ext_028_rev_vs_trail_max_4q},
    "gds_ext_029_netinc_vs_trail_max_4q":          {"inputs": ["netinc"],                                   "func": gds_ext_029_netinc_vs_trail_max_4q},
    "gds_ext_030_eps_vs_trail_max_8q":             {"inputs": ["eps"],                                      "func": gds_ext_030_eps_vs_trail_max_8q},
    "gds_ext_031_gp_vs_trail_min_4q":              {"inputs": ["gp"],                                       "func": gds_ext_031_gp_vs_trail_min_4q},
    "gds_ext_032_opinc_vs_trail_min_4q":           {"inputs": ["opinc"],                                    "func": gds_ext_032_opinc_vs_trail_min_4q},
    "gds_ext_033_ebitda_vs_trail_min_8q":          {"inputs": ["ebitda"],                                   "func": gds_ext_033_ebitda_vs_trail_min_8q},
    "gds_ext_034_fcf_vs_trail_min_4q":             {"inputs": ["fcf"],                                      "func": gds_ext_034_fcf_vs_trail_min_4q},
    "gds_ext_035_rev_vs_trail_max_4q_norm":        {"inputs": ["revenue"],                                  "func": gds_ext_035_rev_vs_trail_max_4q_norm},
    "gds_ext_036_netinc_vs_trail_min_8q_norm":     {"inputs": ["netinc"],                                   "func": gds_ext_036_netinc_vs_trail_min_8q_norm},
    "gds_ext_037_rev_3q_lag_miss":                 {"inputs": ["revenue"],                                  "func": gds_ext_037_rev_3q_lag_miss},
    "gds_ext_038_netinc_3q_lag_miss":              {"inputs": ["netinc"],                                   "func": gds_ext_038_netinc_3q_lag_miss},
    "gds_ext_039_eps_3q_lag_miss":                 {"inputs": ["eps"],                                      "func": gds_ext_039_eps_3q_lag_miss},
    "gds_ext_040_rev_2y_lag_miss":                 {"inputs": ["revenue"],                                  "func": gds_ext_040_rev_2y_lag_miss},
    "gds_ext_041_netinc_2y_lag_miss":              {"inputs": ["netinc"],                                   "func": gds_ext_041_netinc_2y_lag_miss},
    "gds_ext_042_rev_12q_baseline_miss_norm":      {"inputs": ["revenue"],                                  "func": gds_ext_042_rev_12q_baseline_miss_norm},
    "gds_ext_043_netinc_12q_baseline_miss_norm":   {"inputs": ["netinc"],                                   "func": gds_ext_043_netinc_12q_baseline_miss_norm},
    "gds_ext_044_eps_12q_baseline_miss":           {"inputs": ["eps"],                                      "func": gds_ext_044_eps_12q_baseline_miss},
    "gds_ext_045_rev_naive_miss_vol_norm_8q":      {"inputs": ["revenue"],                                  "func": gds_ext_045_rev_naive_miss_vol_norm_8q},
    "gds_ext_046_netinc_naive_miss_vol_norm_8q":   {"inputs": ["netinc"],                                   "func": gds_ext_046_netinc_naive_miss_vol_norm_8q},
    "gds_ext_047_eps_naive_miss_vol_norm_8q":      {"inputs": ["eps"],                                      "func": gds_ext_047_eps_naive_miss_vol_norm_8q},
    "gds_ext_048_rev_seasonal_miss_vol_norm_8q":   {"inputs": ["revenue"],                                  "func": gds_ext_048_rev_seasonal_miss_vol_norm_8q},
    "gds_ext_049_gross_margin_naive_miss":         {"inputs": ["gp", "revenue"],                            "func": gds_ext_049_gross_margin_naive_miss},
    "gds_ext_050_gross_margin_seasonal_miss":      {"inputs": ["gp", "revenue"],                            "func": gds_ext_050_gross_margin_seasonal_miss},
    "gds_ext_051_op_margin_naive_miss":            {"inputs": ["opinc", "revenue"],                         "func": gds_ext_051_op_margin_naive_miss},
    "gds_ext_052_op_margin_seasonal_miss":         {"inputs": ["opinc", "revenue"],                         "func": gds_ext_052_op_margin_seasonal_miss},
    "gds_ext_053_net_margin_naive_miss":           {"inputs": ["netinc", "revenue"],                        "func": gds_ext_053_net_margin_naive_miss},
    "gds_ext_054_ebitda_margin_naive_miss":        {"inputs": ["ebitda", "revenue"],                        "func": gds_ext_054_ebitda_margin_naive_miss},
    "gds_ext_055_fcf_margin_naive_miss":           {"inputs": ["fcf", "revenue"],                           "func": gds_ext_055_fcf_margin_naive_miss},
    "gds_ext_056_net_margin_miss_worst_4q":        {"inputs": ["netinc", "revenue"],                        "func": gds_ext_056_net_margin_miss_worst_4q},
    "gds_ext_057_op_margin_miss_cumulative_8q":    {"inputs": ["opinc", "revenue"],                         "func": gds_ext_057_op_margin_miss_cumulative_8q},
    "gds_ext_058_gross_margin_miss_streak":        {"inputs": ["gp", "revenue"],                            "func": gds_ext_058_gross_margin_miss_streak},
    "gds_ext_059_net_margin_miss_zscore_8q":       {"inputs": ["netinc", "revenue"],                        "func": gds_ext_059_net_margin_miss_zscore_8q},
    "gds_ext_060_margin_miss_count_3metrics":      {"inputs": ["gp", "opinc", "netinc", "revenue"],         "func": gds_ext_060_margin_miss_count_3metrics},
    "gds_ext_061_rev_miss_qoq_accel":              {"inputs": ["revenue"],                                  "func": gds_ext_061_rev_miss_qoq_accel},
    "gds_ext_062_netinc_miss_qoq_accel":           {"inputs": ["netinc"],                                   "func": gds_ext_062_netinc_miss_qoq_accel},
    "gds_ext_063_eps_miss_yoy_accel":              {"inputs": ["eps"],                                      "func": gds_ext_063_eps_miss_yoy_accel},
    "gds_ext_064_rev_miss_worsening_flag":         {"inputs": ["revenue"],                                  "func": gds_ext_064_rev_miss_worsening_flag},
    "gds_ext_065_netinc_miss_worsening_flag":      {"inputs": ["netinc"],                                   "func": gds_ext_065_netinc_miss_worsening_flag},
    "gds_ext_066_rev_miss_negative_quarters_8q":   {"inputs": ["revenue"],                                  "func": gds_ext_066_rev_miss_negative_quarters_8q},
    "gds_ext_067_netinc_miss_negative_fraction_8q":{"inputs": ["netinc"],                                   "func": gds_ext_067_netinc_miss_negative_fraction_8q},
    "gds_ext_068_eps_miss_negative_fraction_4q":   {"inputs": ["eps"],                                      "func": gds_ext_068_eps_miss_negative_fraction_4q},
    "gds_ext_069_seasonal_miss_count_5metrics":    {"inputs": ["revenue", "netinc", "eps", "gp", "opinc"],  "func": gds_ext_069_seasonal_miss_count_5metrics},
    "gds_ext_070_all5_drift_miss_flag":            {"inputs": ["revenue", "netinc", "eps", "gp", "opinc"],  "func": gds_ext_070_all5_drift_miss_flag},
    "gds_ext_071_cashflow_miss_count":             {"inputs": ["fcf", "ncfo", "ebitda"],                    "func": gds_ext_071_cashflow_miss_count},
    "gds_ext_072_composite_ensemble_sue":          {"inputs": ["revenue", "netinc", "eps"],                 "func": gds_ext_072_composite_ensemble_sue},
    "gds_ext_073_rev_netinc_miss_both_worsening_flag": {"inputs": ["revenue", "netinc"],                    "func": gds_ext_073_rev_netinc_miss_both_worsening_flag},
    "gds_ext_074_composite_miss_severity_index":   {"inputs": ["revenue", "netinc", "eps"],                 "func": gds_ext_074_composite_miss_severity_index},
    "gds_ext_075_expanding_worst_miss_eps":        {"inputs": ["eps"],                                      "func": gds_ext_075_expanding_worst_miss_eps},
}
