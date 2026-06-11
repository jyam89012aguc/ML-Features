"""
96_dividend_distress — Extended Features 001-075
Domain: dividend cuts, suspensions, omissions — additional distress angles: cut depth
        distributions, recovery-failure streaks, raise-drought, smoothed yield variants,
        semi-annual horizons, payout-decay composites
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to a shared trading-day index.
Quarterly Sharadar SF1 fields are forward-filled to the daily index so that
flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days, 1 year = 252 trading days.

  dps       : dividends per share, USD (Sharadar SF1 quarterly, forward-filled; 0.0 when none).
  dividends : total cash dividends paid, USD, positive outflow (Sharadar SF1 quarterly,
              forward-filled; 0.0 when none).
  close     : split/dividend-adjusted daily close price, USD.
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
_TD_3Q    = 189
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum().astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Semi-annual / 3-quarter horizon DPS changes ---

def dvd_ext_001_dps_2q_horizon_change(dps: pd.Series) -> pd.Series:
    """DPS change over a 2-quarter (126-day) horizon, recomputed as a distinct lag."""
    return dps - dps.shift(_TD_2Q)


def dvd_ext_002_dps_3q_horizon_change(dps: pd.Series) -> pd.Series:
    """DPS absolute change over a 3-quarter (189-day) horizon."""
    return dps - dps.shift(_TD_3Q)


def dvd_ext_003_dps_3q_horizon_pct(dps: pd.Series) -> pd.Series:
    """DPS 3-quarter percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_3Q)
    return _safe_div_abs(dps - prior, prior)


def dvd_ext_004_dps_4y_change(dps: pd.Series) -> pd.Series:
    """DPS change over 4 years (1008-day lag)."""
    return dps - dps.shift(_TD_YEAR * 4)


def dvd_ext_005_dps_4y_pct(dps: pd.Series) -> pd.Series:
    """DPS 4-year percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_YEAR * 4)
    return _safe_div_abs(dps - prior, prior)


def dvd_ext_006_dps_5y_change(dps: pd.Series) -> pd.Series:
    """DPS absolute change over 5 years (1260-day lag)."""
    return dps - dps.shift(_TD_5Y)


def dvd_ext_007_dps_5y_pct(dps: pd.Series) -> pd.Series:
    """DPS 5-year percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_5Y)
    return _safe_div_abs(dps - prior, prior)


def dvd_ext_008_dps_mo_horizon_change(dps: pd.Series) -> pd.Series:
    """DPS change over a 1-month (21-day) horizon (fast forward-fill drift)."""
    return dps - dps.shift(_TD_MO)


def dvd_ext_009_dps_log_change_qoq(dps: pd.Series) -> pd.Series:
    """Log change of DPS QoQ (floored at EPS); compresses extreme cut ratios."""
    cur = np.log(dps.clip(lower=_EPS))
    return cur - np.log(dps.shift(_TD_QTR).clip(lower=_EPS))


def dvd_ext_010_dps_log_change_yoy(dps: pd.Series) -> pd.Series:
    """Log change of DPS YoY (floored at EPS)."""
    cur = np.log(dps.clip(lower=_EPS))
    return cur - np.log(dps.shift(_TD_YEAR).clip(lower=_EPS))


def dvd_ext_011_dps_log_change_3y(dps: pd.Series) -> pd.Series:
    """Log change of DPS over 3 years (floored at EPS)."""
    cur = np.log(dps.clip(lower=_EPS))
    return cur - np.log(dps.shift(_TD_3Y).clip(lower=_EPS))


def dvd_ext_012_dps_diff_of_yoy_change(dps: pd.Series) -> pd.Series:
    """Change in the YoY DPS change between this quarter and last (cut-trend shift)."""
    yoy = dps - dps.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_QTR)


# --- Group B (013-024): Cut-depth severity distributions and ratios ---

def dvd_ext_013_dps_cut_depth_qoq(dps: pd.Series) -> pd.Series:
    """Magnitude of QoQ DPS decline (0 when not cut): how deep the cut is."""
    return (dps.shift(_TD_QTR) - dps).clip(lower=0.0)


def dvd_ext_014_dps_cut_depth_yoy(dps: pd.Series) -> pd.Series:
    """Magnitude of YoY DPS decline (0 when not lower)."""
    return (dps.shift(_TD_YEAR) - dps).clip(lower=0.0)


def dvd_ext_015_dps_cut_depth_pct_qoq(dps: pd.Series) -> pd.Series:
    """QoQ cut depth as a fraction of prior DPS (0 when not cut)."""
    prior = dps.shift(_TD_QTR)
    depth = (prior - dps).clip(lower=0.0)
    return _safe_div(depth, prior.abs())


def dvd_ext_016_dps_cut_depth_pct_yoy(dps: pd.Series) -> pd.Series:
    """YoY cut depth as a fraction of prior-year DPS (0 when not lower)."""
    prior = dps.shift(_TD_YEAR)
    depth = (prior - dps).clip(lower=0.0)
    return _safe_div(depth, prior.abs())


def dvd_ext_017_dps_cut_depth_max_1y(dps: pd.Series) -> pd.Series:
    """Largest QoQ cut depth observed in the trailing 1-year window."""
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return _rolling_max(depth, _TD_YEAR)


def dvd_ext_018_dps_cut_depth_max_3y(dps: pd.Series) -> pd.Series:
    """Largest QoQ cut depth observed in the trailing 3-year window."""
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return _rolling_max(depth, _TD_3Y)


def dvd_ext_019_dps_cut_depth_sum_3y(dps: pd.Series) -> pd.Series:
    """Cumulative QoQ cut depth summed across the trailing 3-year window."""
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return _rolling_sum(depth, _TD_3Y)


def dvd_ext_020_dps_severe_cut_flag_qoq(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS was cut QoQ by more than 50 percent."""
    prior = dps.shift(_TD_QTR)
    pct = _safe_div(prior - dps, prior.abs())
    return (pct > 0.5).astype(float)


def dvd_ext_021_dps_severe_cut_flag_yoy(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS fell YoY by more than 50 percent."""
    prior = dps.shift(_TD_YEAR)
    pct = _safe_div(prior - dps, prior.abs())
    return (pct > 0.5).astype(float)


def dvd_ext_022_dps_severe_cut_count_3y(dps: pd.Series) -> pd.Series:
    """Count of QoQ cuts deeper than 50 percent in trailing 3 years."""
    prior = dps.shift(_TD_QTR)
    pct = _safe_div(prior - dps, prior.abs())
    severe = (pct > 0.5).astype(float)
    return _rolling_sum(severe, _TD_3Y)


def dvd_ext_023_dps_cut_depth_vs_1y_avg_depth(dps: pd.Series) -> pd.Series:
    """Current QoQ cut depth minus its trailing 1-year mean depth."""
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return depth - _rolling_mean(depth, _TD_YEAR)


def dvd_ext_024_dps_cut_depth_zscore_3y(dps: pd.Series) -> pd.Series:
    """Z-score of QoQ cut depth within the trailing 3-year window."""
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return _zscore_rolling(depth, _TD_3Y)


# --- Group C (025-036): Raise droughts, recovery failures, time-since ---

def dvd_ext_025_days_since_last_dps_raise_yoy(dps: pd.Series) -> pd.Series:
    """Trading days since DPS last increased YoY (raise drought length)."""
    inc = (dps > dps.shift(_TD_YEAR)).astype(int)
    days = np.zeros(len(inc), dtype=float)
    arr = inc.values
    counter = 0.0
    for i in range(len(arr)):
        counter = 0.0 if arr[i] > 0 else counter + 1.0
        days[i] = counter
    return pd.Series(days, index=dps.index)


def dvd_ext_026_days_since_dps_above_1y_peak(dps: pd.Series) -> pd.Series:
    """Trading days since DPS last equalled its trailing 1-year rolling peak."""
    peak = _rolling_max(dps, _TD_YEAR)
    at_peak = (dps >= peak - _EPS).astype(int)
    days = np.zeros(len(at_peak), dtype=float)
    arr = at_peak.values
    counter = 0.0
    for i in range(len(arr)):
        counter = 0.0 if arr[i] > 0 else counter + 1.0
        days[i] = counter
    return pd.Series(days, index=dps.index)


def dvd_ext_027_dps_raise_count_3y(dps: pd.Series) -> pd.Series:
    """Count of QoQ DPS increases in trailing 3 years (payout-growth frequency)."""
    inc = (dps > dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(inc, _TD_3Y)


def dvd_ext_028_dps_raise_fraction_3y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window with QoQ DPS increases."""
    inc = (dps > dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(inc, _TD_3Y)


def dvd_ext_029_dps_no_raise_streak(dps: pd.Series) -> pd.Series:
    """Consecutive days with no QoQ DPS increase (flat-or-falling payout streak)."""
    no_raise = ~(dps > dps.shift(_TD_QTR))
    return _consec_streak(no_raise)


def dvd_ext_030_dps_flat_streak(dps: pd.Series) -> pd.Series:
    """Consecutive days where DPS is unchanged vs one quarter ago (frozen payout)."""
    flat = (dps - dps.shift(_TD_QTR)).abs() <= _EPS
    return _consec_streak(flat)


def dvd_ext_031_dps_recovery_failure_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS is still below its level of 1 year ago AND was cut QoQ."""
    below_1y = (dps < dps.shift(_TD_YEAR)).astype(float)
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return below_1y * cut


def dvd_ext_032_dps_below_peak_streak(dps: pd.Series) -> pd.Series:
    """Consecutive days DPS sits below its trailing 3-year rolling peak."""
    peak = _rolling_max(dps, _TD_3Y)
    below = dps < peak - _EPS
    return _consec_streak(below)


def dvd_ext_033_dps_below_3y_avg_streak(dps: pd.Series) -> pd.Series:
    """Consecutive days DPS sits below its trailing 3-year mean."""
    below = dps < _rolling_mean(dps, _TD_3Y)
    return _consec_streak(below)


def dvd_ext_034_days_since_dps_omission(dps: pd.Series) -> pd.Series:
    """Trading days since DPS was last zero (0 while currently zero)."""
    zero = (dps <= 0).astype(int)
    days = np.zeros(len(zero), dtype=float)
    arr = zero.values
    counter = 0.0
    for i in range(len(arr)):
        counter = 0.0 if arr[i] > 0 else counter + 1.0
        days[i] = counter
    return pd.Series(days, index=dps.index)


def dvd_ext_035_dps_raise_drought_over_1y_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS has not increased QoQ anywhere in the trailing 1 year."""
    inc = (dps > dps.shift(_TD_QTR)).astype(float)
    return (_rolling_sum(inc, _TD_YEAR) <= 0).astype(float)


def dvd_ext_036_dps_consecutive_yoy_decline_streak(dps: pd.Series) -> pd.Series:
    """Consecutive days DPS is below its level of one year ago."""
    decline = dps < dps.shift(_TD_YEAR)
    return _consec_streak(decline)


# --- Group D (037-048): Smoothed dividend levels and EWM/median variants ---

def dvd_ext_037_dps_ewm_2q(dps: pd.Series) -> pd.Series:
    """2-quarter EWM (span=126) of DPS — smoothed payout level."""
    return _ewm_mean(dps, _TD_2Q)


def dvd_ext_038_dps_ewm_3y(dps: pd.Series) -> pd.Series:
    """3-year EWM (span=756) of DPS — slow structural payout level."""
    return _ewm_mean(dps, _TD_3Y)


def dvd_ext_039_dps_ewm_2q_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 2-quarter EWM (medium-horizon momentum signal)."""
    return dps - _ewm_mean(dps, _TD_2Q)


def dvd_ext_040_dps_ewm_3y_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 3-year EWM (long-horizon structural deviation)."""
    return dps - _ewm_mean(dps, _TD_3Y)


def dvd_ext_041_dps_ewm_ratio_2q_to_3y(dps: pd.Series) -> pd.Series:
    """Ratio of DPS 2-quarter EWM to 3-year EWM (medium-vs-long trend ratio)."""
    return _safe_div(_ewm_mean(dps, _TD_2Q), _ewm_mean(dps, _TD_3Y))


def dvd_ext_042_dps_median_2y(dps: pd.Series) -> pd.Series:
    """Trailing 2-year rolling median of DPS (robust payout baseline)."""
    return _rolling_median(dps, _TD_2Y)


def dvd_ext_043_dps_median_5y(dps: pd.Series) -> pd.Series:
    """Trailing 5-year rolling median of DPS."""
    return _rolling_median(dps, _TD_5Y)


def dvd_ext_044_dps_median_deviation_2y(dps: pd.Series) -> pd.Series:
    """DPS minus its trailing 2-year median."""
    return dps - _rolling_median(dps, _TD_2Y)


def dvd_ext_045_dps_pct_vs_median_3y(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from its trailing 3-year median."""
    med = _rolling_median(dps, _TD_3Y)
    return _safe_div_abs(dps - med, med)


def dvd_ext_046_dps_to_median_5y_ratio(dps: pd.Series) -> pd.Series:
    """DPS divided by its trailing 5-year median (normalized payout level)."""
    return _safe_div(dps, _rolling_median(dps, _TD_5Y))


def dvd_ext_047_dps_2q_smoothed_vs_2y_avg(dps: pd.Series) -> pd.Series:
    """2-quarter EWM-smoothed DPS minus its 2-year rolling mean."""
    sm = _ewm_mean(dps, _TD_2Q)
    return sm - _rolling_mean(sm, _TD_2Y)


def dvd_ext_048_dps_mo_smoothed_drawdown_3y(dps: pd.Series) -> pd.Series:
    """Percent drawdown of monthly-smoothed DPS from its 3-year smoothed peak."""
    sm = _rolling_mean(dps, _TD_MO)
    peak = _rolling_max(sm, _TD_3Y)
    return _safe_div_abs(sm - peak, peak)


# --- Group E (049-060): Yield-proxy extended variants ---

def dvd_ext_049_yield_proxy_unannualized(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy without 4x annualization (raw quarterly ratio)."""
    return _safe_div(dps, close)


def dvd_ext_050_yield_proxy_qoq_pct(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ percent change in the annualized DPS/close yield proxy."""
    y = _safe_div(dps * 4.0, close)
    prior = y.shift(_TD_QTR)
    return _safe_div_abs(y - prior, prior)


def dvd_ext_051_yield_proxy_2y_zscore(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of the annualized DPS/close yield proxy in a trailing 2-year window."""
    y = _safe_div(dps * 4.0, close)
    return _zscore_rolling(y, _TD_2Y)


def dvd_ext_052_yield_proxy_2y_pct_rank(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of the DPS/close yield proxy in a trailing 2-year window."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_rank_pct(y, _TD_2Y)


def dvd_ext_053_yield_proxy_ewm_deviation(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy minus its 1-year EWM (yield-momentum shift)."""
    y = _safe_div(dps * 4.0, close)
    return y - _ewm_mean(y, _TD_YEAR)


def dvd_ext_054_yield_proxy_vs_3y_avg(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy minus its trailing 3-year mean."""
    y = _safe_div(dps * 4.0, close)
    return y - _rolling_mean(y, _TD_3Y)


def dvd_ext_055_yield_proxy_extreme_high_flag_3y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 when yield proxy is above its trailing 3-year 95th percentile (distress yield)."""
    y = _safe_div(dps * 4.0, close)
    p95 = y.rolling(_TD_3Y, min_periods=max(2, _TD_3Y // 4)).quantile(0.95)
    return (y >= p95).astype(float)


def dvd_ext_056_ttm_dps_yield_proxy(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing-twelve-month DPS sum divided by close (TTM yield proxy)."""
    ttm = _rolling_sum(dps, _TD_YEAR)
    return _safe_div(ttm, close)


def dvd_ext_057_ttm_dps_yield_zscore_2y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of the TTM-DPS yield proxy in a trailing 2-year window."""
    ttm = _rolling_sum(dps, _TD_YEAR)
    y = _safe_div(ttm, close)
    return _zscore_rolling(y, _TD_2Y)


def dvd_ext_058_total_div_yield_pct_rank_3y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of total-dividends/close proxy in a trailing 3-year window."""
    y = _safe_div(dividends, close)
    return _rolling_rank_pct(y, _TD_3Y)


def dvd_ext_059_total_div_yield_zscore_3y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of total-dividends/close proxy in a trailing 3-year window."""
    y = _safe_div(dividends, close)
    return _zscore_rolling(y, _TD_3Y)


def dvd_ext_060_yield_proxy_drawdown_from_3y_peak(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy minus its 3-year rolling peak (yield collapse depth)."""
    y = _safe_div(dps * 4.0, close)
    return y - _rolling_max(y, _TD_3Y)


# --- Group F (061-068): Total-dividends extended distress variants ---

def dvd_ext_061_dividends_cut_depth_qoq(dividends: pd.Series) -> pd.Series:
    """Magnitude of QoQ total-dividends decline (0 when not cut)."""
    return (dividends.shift(_TD_QTR) - dividends).clip(lower=0.0)


def dvd_ext_062_dividends_cut_depth_pct_qoq(dividends: pd.Series) -> pd.Series:
    """QoQ total-dividends cut depth as a fraction of prior level."""
    prior = dividends.shift(_TD_QTR)
    depth = (prior - dividends).clip(lower=0.0)
    return _safe_div(depth, prior.abs())


def dvd_ext_063_dividends_consecutive_cut_streak(dividends: pd.Series) -> pd.Series:
    """Consecutive days total dividends are below their level one quarter ago."""
    cut = dividends < dividends.shift(_TD_QTR)
    return _consec_streak(cut)


def dvd_ext_064_dividends_omission_streak(dividends: pd.Series) -> pd.Series:
    """Consecutive days with zero total dividends paid."""
    zero = dividends <= 0
    return _consec_streak(zero)


def dvd_ext_065_dividends_omission_fraction_3y(dividends: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window with zero total dividends."""
    zero = (dividends <= 0).astype(float)
    return _rolling_mean(zero, _TD_3Y)


def dvd_ext_066_dividends_log_change_yoy(dividends: pd.Series) -> pd.Series:
    """Log change of total dividends YoY (floored at EPS)."""
    cur = np.log(dividends.clip(lower=_EPS))
    return cur - np.log(dividends.shift(_TD_YEAR).clip(lower=_EPS))


def dvd_ext_067_dividends_pct_drawdown_3y(dividends: pd.Series) -> pd.Series:
    """Percent drawdown of total dividends from their trailing 3-year peak."""
    peak = _rolling_max(dividends, _TD_3Y)
    return _safe_div_abs(dividends - peak, peak)


def dvd_ext_068_dividends_ewm_3y_deviation(dividends: pd.Series) -> pd.Series:
    """Total dividends minus their 3-year EWM (long-horizon payout-shift signal)."""
    return dividends - _ewm_mean(dividends, _TD_3Y)


# --- Group G (069-075): Long-horizon ranks, stability and composites ---

def dvd_ext_069_dps_pct_rank_2y(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within a trailing 2-year window."""
    return _rolling_rank_pct(dps, _TD_2Y)


def dvd_ext_070_dps_coeff_variation_5y(dps: pd.Series) -> pd.Series:
    """Coefficient of variation of DPS over a trailing 5-year window (std / |mean|)."""
    m  = _rolling_mean(dps, _TD_5Y)
    sd = _rolling_std(dps, _TD_5Y)
    return _safe_div_abs(sd, m)


def dvd_ext_071_dps_downside_deviation_3y(dps: pd.Series) -> pd.Series:
    """Root-mean-square of negative QoQ DPS changes over trailing 3 years (downside vol)."""
    chg = dps - dps.shift(_TD_QTR)
    neg = chg.clip(upper=0.0)
    return _rolling_mean(neg ** 2, _TD_3Y) ** 0.5


def dvd_ext_072_dps_drawdown_to_range_3y(dps: pd.Series) -> pd.Series:
    """DPS drawdown from 3-year peak normalized by its 3-year max-minus-min range."""
    peak = _rolling_max(dps, _TD_3Y)
    trough = _rolling_min(dps, _TD_3Y)
    return _safe_div(dps - peak, peak - trough)


def dvd_ext_073_dps_distress_intensity_3y(dps: pd.Series) -> pd.Series:
    """Cut-fraction times mean cut depth over trailing 3 years (chronic-distress intensity)."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    depth = (dps.shift(_TD_QTR) - dps).clip(lower=0.0)
    return _rolling_mean(cut, _TD_3Y) * _rolling_mean(depth, _TD_3Y)


def dvd_ext_074_dividend_decay_composite(dps: pd.Series, dividends: pd.Series) -> pd.Series:
    """Composite payout-decay score: mean of YoY DPS and YoY total-dividends cut-depth fractions."""
    dps_prior = dps.shift(_TD_YEAR)
    dps_pct = _safe_div((dps_prior - dps).clip(lower=0.0), dps_prior.abs())
    div_prior = dividends.shift(_TD_YEAR)
    div_pct = _safe_div((div_prior - dividends).clip(lower=0.0), div_prior.abs())
    return (dps_pct + div_pct) / 2.0


def dvd_ext_075_dividend_distress_composite_3y(dps: pd.Series, dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Composite 3-year dividend-distress score: mean of negated z-scores of dps, dividends
    and the DPS/close yield proxy (higher = more distress)."""
    z_dps = _zscore_rolling(dps, _TD_3Y)
    z_div = _zscore_rolling(dividends, _TD_3Y)
    y = _safe_div(dps * 4.0, close)
    z_yld = _zscore_rolling(y, _TD_3Y)
    return (-z_dps - z_div + z_yld) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

DIVIDEND_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "dvd_ext_001_dps_2q_horizon_change":        {"inputs": ["dps"],                       "func": dvd_ext_001_dps_2q_horizon_change},
    "dvd_ext_002_dps_3q_horizon_change":        {"inputs": ["dps"],                       "func": dvd_ext_002_dps_3q_horizon_change},
    "dvd_ext_003_dps_3q_horizon_pct":           {"inputs": ["dps"],                       "func": dvd_ext_003_dps_3q_horizon_pct},
    "dvd_ext_004_dps_4y_change":                {"inputs": ["dps"],                       "func": dvd_ext_004_dps_4y_change},
    "dvd_ext_005_dps_4y_pct":                   {"inputs": ["dps"],                       "func": dvd_ext_005_dps_4y_pct},
    "dvd_ext_006_dps_5y_change":                {"inputs": ["dps"],                       "func": dvd_ext_006_dps_5y_change},
    "dvd_ext_007_dps_5y_pct":                   {"inputs": ["dps"],                       "func": dvd_ext_007_dps_5y_pct},
    "dvd_ext_008_dps_mo_horizon_change":        {"inputs": ["dps"],                       "func": dvd_ext_008_dps_mo_horizon_change},
    "dvd_ext_009_dps_log_change_qoq":           {"inputs": ["dps"],                       "func": dvd_ext_009_dps_log_change_qoq},
    "dvd_ext_010_dps_log_change_yoy":           {"inputs": ["dps"],                       "func": dvd_ext_010_dps_log_change_yoy},
    "dvd_ext_011_dps_log_change_3y":            {"inputs": ["dps"],                       "func": dvd_ext_011_dps_log_change_3y},
    "dvd_ext_012_dps_diff_of_yoy_change":       {"inputs": ["dps"],                       "func": dvd_ext_012_dps_diff_of_yoy_change},
    "dvd_ext_013_dps_cut_depth_qoq":            {"inputs": ["dps"],                       "func": dvd_ext_013_dps_cut_depth_qoq},
    "dvd_ext_014_dps_cut_depth_yoy":            {"inputs": ["dps"],                       "func": dvd_ext_014_dps_cut_depth_yoy},
    "dvd_ext_015_dps_cut_depth_pct_qoq":        {"inputs": ["dps"],                       "func": dvd_ext_015_dps_cut_depth_pct_qoq},
    "dvd_ext_016_dps_cut_depth_pct_yoy":        {"inputs": ["dps"],                       "func": dvd_ext_016_dps_cut_depth_pct_yoy},
    "dvd_ext_017_dps_cut_depth_max_1y":         {"inputs": ["dps"],                       "func": dvd_ext_017_dps_cut_depth_max_1y},
    "dvd_ext_018_dps_cut_depth_max_3y":         {"inputs": ["dps"],                       "func": dvd_ext_018_dps_cut_depth_max_3y},
    "dvd_ext_019_dps_cut_depth_sum_3y":         {"inputs": ["dps"],                       "func": dvd_ext_019_dps_cut_depth_sum_3y},
    "dvd_ext_020_dps_severe_cut_flag_qoq":      {"inputs": ["dps"],                       "func": dvd_ext_020_dps_severe_cut_flag_qoq},
    "dvd_ext_021_dps_severe_cut_flag_yoy":      {"inputs": ["dps"],                       "func": dvd_ext_021_dps_severe_cut_flag_yoy},
    "dvd_ext_022_dps_severe_cut_count_3y":      {"inputs": ["dps"],                       "func": dvd_ext_022_dps_severe_cut_count_3y},
    "dvd_ext_023_dps_cut_depth_vs_1y_avg_depth":{"inputs": ["dps"],                       "func": dvd_ext_023_dps_cut_depth_vs_1y_avg_depth},
    "dvd_ext_024_dps_cut_depth_zscore_3y":      {"inputs": ["dps"],                       "func": dvd_ext_024_dps_cut_depth_zscore_3y},
    "dvd_ext_025_days_since_last_dps_raise_yoy":{"inputs": ["dps"],                       "func": dvd_ext_025_days_since_last_dps_raise_yoy},
    "dvd_ext_026_days_since_dps_above_1y_peak": {"inputs": ["dps"],                       "func": dvd_ext_026_days_since_dps_above_1y_peak},
    "dvd_ext_027_dps_raise_count_3y":           {"inputs": ["dps"],                       "func": dvd_ext_027_dps_raise_count_3y},
    "dvd_ext_028_dps_raise_fraction_3y":        {"inputs": ["dps"],                       "func": dvd_ext_028_dps_raise_fraction_3y},
    "dvd_ext_029_dps_no_raise_streak":          {"inputs": ["dps"],                       "func": dvd_ext_029_dps_no_raise_streak},
    "dvd_ext_030_dps_flat_streak":              {"inputs": ["dps"],                       "func": dvd_ext_030_dps_flat_streak},
    "dvd_ext_031_dps_recovery_failure_flag":    {"inputs": ["dps"],                       "func": dvd_ext_031_dps_recovery_failure_flag},
    "dvd_ext_032_dps_below_peak_streak":        {"inputs": ["dps"],                       "func": dvd_ext_032_dps_below_peak_streak},
    "dvd_ext_033_dps_below_3y_avg_streak":      {"inputs": ["dps"],                       "func": dvd_ext_033_dps_below_3y_avg_streak},
    "dvd_ext_034_days_since_dps_omission":      {"inputs": ["dps"],                       "func": dvd_ext_034_days_since_dps_omission},
    "dvd_ext_035_dps_raise_drought_over_1y_flag":{"inputs": ["dps"],                      "func": dvd_ext_035_dps_raise_drought_over_1y_flag},
    "dvd_ext_036_dps_consecutive_yoy_decline_streak":{"inputs": ["dps"],                  "func": dvd_ext_036_dps_consecutive_yoy_decline_streak},
    "dvd_ext_037_dps_ewm_2q":                   {"inputs": ["dps"],                       "func": dvd_ext_037_dps_ewm_2q},
    "dvd_ext_038_dps_ewm_3y":                   {"inputs": ["dps"],                       "func": dvd_ext_038_dps_ewm_3y},
    "dvd_ext_039_dps_ewm_2q_deviation":         {"inputs": ["dps"],                       "func": dvd_ext_039_dps_ewm_2q_deviation},
    "dvd_ext_040_dps_ewm_3y_deviation":         {"inputs": ["dps"],                       "func": dvd_ext_040_dps_ewm_3y_deviation},
    "dvd_ext_041_dps_ewm_ratio_2q_to_3y":       {"inputs": ["dps"],                       "func": dvd_ext_041_dps_ewm_ratio_2q_to_3y},
    "dvd_ext_042_dps_median_2y":                {"inputs": ["dps"],                       "func": dvd_ext_042_dps_median_2y},
    "dvd_ext_043_dps_median_5y":                {"inputs": ["dps"],                       "func": dvd_ext_043_dps_median_5y},
    "dvd_ext_044_dps_median_deviation_2y":      {"inputs": ["dps"],                       "func": dvd_ext_044_dps_median_deviation_2y},
    "dvd_ext_045_dps_pct_vs_median_3y":         {"inputs": ["dps"],                       "func": dvd_ext_045_dps_pct_vs_median_3y},
    "dvd_ext_046_dps_to_median_5y_ratio":       {"inputs": ["dps"],                       "func": dvd_ext_046_dps_to_median_5y_ratio},
    "dvd_ext_047_dps_2q_smoothed_vs_2y_avg":    {"inputs": ["dps"],                       "func": dvd_ext_047_dps_2q_smoothed_vs_2y_avg},
    "dvd_ext_048_dps_mo_smoothed_drawdown_3y":  {"inputs": ["dps"],                       "func": dvd_ext_048_dps_mo_smoothed_drawdown_3y},
    "dvd_ext_049_yield_proxy_unannualized":     {"inputs": ["dps", "close"],              "func": dvd_ext_049_yield_proxy_unannualized},
    "dvd_ext_050_yield_proxy_qoq_pct":          {"inputs": ["dps", "close"],              "func": dvd_ext_050_yield_proxy_qoq_pct},
    "dvd_ext_051_yield_proxy_2y_zscore":        {"inputs": ["dps", "close"],              "func": dvd_ext_051_yield_proxy_2y_zscore},
    "dvd_ext_052_yield_proxy_2y_pct_rank":      {"inputs": ["dps", "close"],              "func": dvd_ext_052_yield_proxy_2y_pct_rank},
    "dvd_ext_053_yield_proxy_ewm_deviation":    {"inputs": ["dps", "close"],              "func": dvd_ext_053_yield_proxy_ewm_deviation},
    "dvd_ext_054_yield_proxy_vs_3y_avg":        {"inputs": ["dps", "close"],              "func": dvd_ext_054_yield_proxy_vs_3y_avg},
    "dvd_ext_055_yield_proxy_extreme_high_flag_3y":{"inputs": ["dps", "close"],           "func": dvd_ext_055_yield_proxy_extreme_high_flag_3y},
    "dvd_ext_056_ttm_dps_yield_proxy":          {"inputs": ["dps", "close"],              "func": dvd_ext_056_ttm_dps_yield_proxy},
    "dvd_ext_057_ttm_dps_yield_zscore_2y":      {"inputs": ["dps", "close"],              "func": dvd_ext_057_ttm_dps_yield_zscore_2y},
    "dvd_ext_058_total_div_yield_pct_rank_3y":  {"inputs": ["dividends", "close"],        "func": dvd_ext_058_total_div_yield_pct_rank_3y},
    "dvd_ext_059_total_div_yield_zscore_3y":    {"inputs": ["dividends", "close"],        "func": dvd_ext_059_total_div_yield_zscore_3y},
    "dvd_ext_060_yield_proxy_drawdown_from_3y_peak":{"inputs": ["dps", "close"],          "func": dvd_ext_060_yield_proxy_drawdown_from_3y_peak},
    "dvd_ext_061_dividends_cut_depth_qoq":      {"inputs": ["dividends"],                 "func": dvd_ext_061_dividends_cut_depth_qoq},
    "dvd_ext_062_dividends_cut_depth_pct_qoq":  {"inputs": ["dividends"],                 "func": dvd_ext_062_dividends_cut_depth_pct_qoq},
    "dvd_ext_063_dividends_consecutive_cut_streak":{"inputs": ["dividends"],              "func": dvd_ext_063_dividends_consecutive_cut_streak},
    "dvd_ext_064_dividends_omission_streak":    {"inputs": ["dividends"],                 "func": dvd_ext_064_dividends_omission_streak},
    "dvd_ext_065_dividends_omission_fraction_3y":{"inputs": ["dividends"],                "func": dvd_ext_065_dividends_omission_fraction_3y},
    "dvd_ext_066_dividends_log_change_yoy":     {"inputs": ["dividends"],                 "func": dvd_ext_066_dividends_log_change_yoy},
    "dvd_ext_067_dividends_pct_drawdown_3y":    {"inputs": ["dividends"],                 "func": dvd_ext_067_dividends_pct_drawdown_3y},
    "dvd_ext_068_dividends_ewm_3y_deviation":   {"inputs": ["dividends"],                 "func": dvd_ext_068_dividends_ewm_3y_deviation},
    "dvd_ext_069_dps_pct_rank_2y":              {"inputs": ["dps"],                       "func": dvd_ext_069_dps_pct_rank_2y},
    "dvd_ext_070_dps_coeff_variation_5y":       {"inputs": ["dps"],                       "func": dvd_ext_070_dps_coeff_variation_5y},
    "dvd_ext_071_dps_downside_deviation_3y":    {"inputs": ["dps"],                       "func": dvd_ext_071_dps_downside_deviation_3y},
    "dvd_ext_072_dps_drawdown_to_range_3y":     {"inputs": ["dps"],                       "func": dvd_ext_072_dps_drawdown_to_range_3y},
    "dvd_ext_073_dps_distress_intensity_3y":    {"inputs": ["dps"],                       "func": dvd_ext_073_dps_distress_intensity_3y},
    "dvd_ext_074_dividend_decay_composite":     {"inputs": ["dps", "dividends"],          "func": dvd_ext_074_dividend_decay_composite},
    "dvd_ext_075_dividend_distress_composite_3y":{"inputs": ["dps", "dividends", "close"],"func": dvd_ext_075_dividend_distress_composite_3y},
}
