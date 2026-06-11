"""
96_dividend_distress — Base Features 001-075
Domain: dividend cuts, suspensions, omissions; distress signaled by falling or absent dividends
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_TD_MO    = 21    # ~1 calendar month
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): DPS level vs trailing peak and absolute changes ---

def dvd_001_dps_qoq_change(dps: pd.Series) -> pd.Series:
    """DPS QoQ change (absolute, 63-day lag)."""
    return dps - dps.shift(_TD_QTR)


def dvd_002_dps_yoy_change(dps: pd.Series) -> pd.Series:
    """DPS YoY change (absolute, 252-day lag)."""
    return dps - dps.shift(_TD_YEAR)


def dvd_003_dps_2y_change(dps: pd.Series) -> pd.Series:
    """DPS change over 2 years (504-day lag)."""
    return dps - dps.shift(_TD_2Y)


def dvd_004_dps_3y_change(dps: pd.Series) -> pd.Series:
    """DPS change over 3 years (756-day lag)."""
    return dps - dps.shift(_TD_3Y)


def dvd_005_dps_qoq_pct(dps: pd.Series) -> pd.Series:
    """DPS QoQ percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_QTR)
    return _safe_div_abs(dps - prior, prior)


def dvd_006_dps_yoy_pct(dps: pd.Series) -> pd.Series:
    """DPS YoY percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_YEAR)
    return _safe_div_abs(dps - prior, prior)


def dvd_007_dps_2y_pct(dps: pd.Series) -> pd.Series:
    """DPS 2-year percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_2Y)
    return _safe_div_abs(dps - prior, prior)


def dvd_008_dps_3y_pct(dps: pd.Series) -> pd.Series:
    """DPS 3-year percent change; denominator is abs(prior)."""
    prior = dps.shift(_TD_3Y)
    return _safe_div_abs(dps - prior, prior)


def dvd_009_dps_drawdown_from_1y_peak(dps: pd.Series) -> pd.Series:
    """DPS level drawdown from its 1-year rolling peak."""
    peak = _rolling_max(dps, _TD_YEAR)
    return dps - peak


def dvd_010_dps_drawdown_from_2y_peak(dps: pd.Series) -> pd.Series:
    """DPS level drawdown from its 2-year rolling peak."""
    peak = _rolling_max(dps, _TD_2Y)
    return dps - peak


def dvd_011_dps_drawdown_from_3y_peak(dps: pd.Series) -> pd.Series:
    """DPS level drawdown from its 3-year rolling peak."""
    peak = _rolling_max(dps, _TD_3Y)
    return dps - peak


def dvd_012_dps_drawdown_from_5y_peak(dps: pd.Series) -> pd.Series:
    """DPS level drawdown from its 5-year rolling peak."""
    peak = _rolling_max(dps, _TD_5Y)
    return dps - peak


def dvd_013_dps_drawdown_from_expanding_peak(dps: pd.Series) -> pd.Series:
    """DPS vs its all-history expanding maximum."""
    peak = dps.expanding(min_periods=1).max()
    return dps - peak


def dvd_014_dps_pct_drawdown_from_1y_peak(dps: pd.Series) -> pd.Series:
    """DPS percent drawdown from 1-year rolling peak."""
    peak = _rolling_max(dps, _TD_YEAR)
    return _safe_div_abs(dps - peak, peak)


def dvd_015_dps_pct_drawdown_from_expanding_peak(dps: pd.Series) -> pd.Series:
    """DPS percent drawdown from all-history expanding peak."""
    peak = dps.expanding(min_periods=1).max()
    return _safe_div_abs(dps - peak, peak)


# --- Group B (016-030): Cut / suspension / omission flags and streaks ---

def dvd_016_dps_cut_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS fell QoQ (cut detected)."""
    return (dps < dps.shift(_TD_QTR)).astype(float)


def dvd_017_dps_cut_yoy_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS fell YoY."""
    return (dps < dps.shift(_TD_YEAR)).astype(float)


def dvd_018_dps_omission_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS = 0 (no dividend paid this period)."""
    return (dps <= 0).astype(float)


def dvd_019_dps_suspension_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS just dropped to 0 from a positive prior quarter."""
    curr_zero  = (dps <= 0).astype(float)
    prior_pos  = (dps.shift(_TD_QTR) > 0).astype(float)
    return curr_zero * prior_pos


def dvd_020_dps_first_cut_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 on the first QoQ cut after a non-cut (previous QoQ was flat-or-rise)."""
    cut   = (dps < dps.shift(_TD_QTR)).astype(float)
    prior_no_cut = (dps.shift(_TD_QTR) >= dps.shift(_TD_2Q)).astype(float)
    return cut * prior_no_cut


def dvd_021_dps_consecutive_cut_streak(dps: pd.Series) -> pd.Series:
    """Current consecutive-cut streak length in daily observations (resets on any non-cut)."""
    cut = (dps < dps.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(cut), dtype=float)
    arr = cut.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=dps.index)


def dvd_022_dps_consecutive_zero_streak(dps: pd.Series) -> pd.Series:
    """Current consecutive streak of zero-DPS days (omission streak)."""
    zero = (dps <= 0).astype(int)
    streak = np.zeros(len(zero), dtype=float)
    arr = zero.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=dps.index)


def dvd_023_dps_cuts_count_1y(dps: pd.Series) -> pd.Series:
    """Number of QoQ cut observations in trailing 1-year window."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_YEAR)


def dvd_024_dps_cuts_count_2y(dps: pd.Series) -> pd.Series:
    """Number of QoQ cut observations in trailing 2-year window."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_2Y)


def dvd_025_dps_cuts_count_3y(dps: pd.Series) -> pd.Series:
    """Number of QoQ cut observations in trailing 3-year window."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_3Y)


def dvd_026_dps_cut_fraction_1y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 1-year window where DPS was cut QoQ."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(cut, _TD_YEAR)


def dvd_027_dps_cut_fraction_2y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 2-year window where DPS was cut QoQ."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(cut, _TD_2Y)


def dvd_028_dps_cut_fraction_3y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where DPS was cut QoQ."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(cut, _TD_3Y)


def dvd_029_dps_omission_fraction_1y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 1-year window with zero DPS."""
    zero = (dps <= 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def dvd_030_dps_omission_fraction_3y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window with zero DPS."""
    zero = (dps <= 0).astype(float)
    return _rolling_mean(zero, _TD_3Y)


# --- Group C (031-045): Dividend yield proxies and yield spikes ---

def dvd_031_div_yield_proxy(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS / close — forward dividend yield proxy (quarterly annualized)."""
    return _safe_div(dps * 4.0, close)


def dvd_032_div_yield_proxy_1y_avg(dps: pd.Series, close: pd.Series) -> pd.Series:
    """1-year rolling mean of the DPS/close yield proxy."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_mean(y, _TD_YEAR)


def dvd_033_div_yield_proxy_vs_1y_avg(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Current yield proxy minus its 1-year mean (yield spike vs history)."""
    y = _safe_div(dps * 4.0, close)
    return y - _rolling_mean(y, _TD_YEAR)


def dvd_034_div_yield_proxy_zscore_1y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DPS/close yield proxy in trailing 1-year window."""
    y = _safe_div(dps * 4.0, close)
    return _zscore_rolling(y, _TD_YEAR)


def dvd_035_div_yield_proxy_zscore_3y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DPS/close yield proxy in trailing 3-year window."""
    y = _safe_div(dps * 4.0, close)
    return _zscore_rolling(y, _TD_3Y)


def dvd_036_div_yield_proxy_pct_rank_1y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of DPS/close yield proxy in trailing 1-year window."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_rank_pct(y, _TD_YEAR)


def dvd_037_div_yield_proxy_pct_rank_3y(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of DPS/close yield proxy in trailing 3-year window."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_rank_pct(y, _TD_3Y)


def dvd_038_div_yield_proxy_expanding_zscore(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding z-score of DPS/close yield proxy (how extreme vs entire history)."""
    y = _safe_div(dps * 4.0, close)
    m  = y.expanding(min_periods=2).mean()
    sd = y.expanding(min_periods=2).std()
    return _safe_div(y - m, sd)


def dvd_039_yield_spike_flag(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 when current yield proxy is above its 1-year rolling 90th percentile."""
    y = _safe_div(dps * 4.0, close)
    p90 = y.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).quantile(0.9)
    return (y >= p90).astype(float)


def dvd_040_yield_collapse_flag(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 when yield proxy dropped below its 1-year 10th percentile (price rallied away or DPS cut)."""
    y = _safe_div(dps * 4.0, close)
    p10 = y.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).quantile(0.1)
    return (y <= p10).astype(float)


def dvd_041_total_div_yield_proxy(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Total dividends / close — aggregate payout yield proxy."""
    return _safe_div(dividends, close)


def dvd_042_total_div_yield_zscore_1y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of total-dividends/close proxy in trailing 1-year window."""
    y = _safe_div(dividends, close)
    return _zscore_rolling(y, _TD_YEAR)


def dvd_043_total_div_yield_pct_rank_1y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of total-dividends/close proxy in trailing 1-year window."""
    y = _safe_div(dividends, close)
    return _rolling_rank_pct(y, _TD_YEAR)


def dvd_044_dps_price_ratio_qoq_change(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ change in DPS/close ratio (yield drift signal)."""
    y = _safe_div(dps, close)
    return y - y.shift(_TD_QTR)


def dvd_045_dps_price_ratio_yoy_change(dps: pd.Series, close: pd.Series) -> pd.Series:
    """YoY change in DPS/close ratio."""
    y = _safe_div(dps, close)
    return y - y.shift(_TD_YEAR)


# --- Group D (046-060): Payment gaps and time-since-last-payment ---

def dvd_046_days_since_last_positive_dps(dps: pd.Series) -> pd.Series:
    """Number of trading days since DPS was last positive (0 when currently positive)."""
    pos = (dps > 0).astype(int)
    days = np.zeros(len(pos), dtype=float)
    arr = pos.values
    counter = 0.0
    for i in range(len(arr)):
        if arr[i] > 0:
            counter = 0.0
        else:
            counter += 1.0
        days[i] = counter
    return pd.Series(days, index=dps.index)


def dvd_047_days_since_last_div_increase(dps: pd.Series) -> pd.Series:
    """Number of trading days since DPS last increased QoQ."""
    inc = (dps > dps.shift(_TD_QTR)).astype(int)
    days = np.zeros(len(inc), dtype=float)
    arr = inc.values
    counter = 0.0
    for i in range(len(arr)):
        if arr[i] > 0:
            counter = 0.0
        else:
            counter += 1.0
        days[i] = counter
    return pd.Series(days, index=dps.index)


def dvd_048_payment_gap_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS is 0 but was positive at least once in prior 2 quarters."""
    curr_zero  = (dps <= 0).astype(float)
    recent_pos = (dps.shift(_TD_QTR) > 0).astype(float) + (dps.shift(_TD_2Q) > 0).astype(float)
    return (curr_zero * (recent_pos > 0)).astype(float)


def dvd_049_payment_gap_duration_1y(dps: pd.Series) -> pd.Series:
    """Total trading days in trailing 1 year with DPS = 0."""
    zero = (dps <= 0).astype(float)
    return _rolling_sum(zero, _TD_YEAR)


def dvd_050_payment_gap_duration_2y(dps: pd.Series) -> pd.Series:
    """Total trading days in trailing 2 years with DPS = 0."""
    zero = (dps <= 0).astype(float)
    return _rolling_sum(zero, _TD_2Y)


def dvd_051_payment_gap_duration_3y(dps: pd.Series) -> pd.Series:
    """Total trading days in trailing 3 years with DPS = 0."""
    zero = (dps <= 0).astype(float)
    return _rolling_sum(zero, _TD_3Y)


def dvd_052_dividends_qoq_change(dividends: pd.Series) -> pd.Series:
    """Total cash dividends QoQ change (absolute)."""
    return dividends - dividends.shift(_TD_QTR)


def dvd_053_dividends_yoy_change(dividends: pd.Series) -> pd.Series:
    """Total cash dividends YoY change (absolute)."""
    return dividends - dividends.shift(_TD_YEAR)


def dvd_054_dividends_qoq_pct(dividends: pd.Series) -> pd.Series:
    """Total cash dividends QoQ percent change."""
    prior = dividends.shift(_TD_QTR)
    return _safe_div_abs(dividends - prior, prior)


def dvd_055_dividends_yoy_pct(dividends: pd.Series) -> pd.Series:
    """Total cash dividends YoY percent change."""
    prior = dividends.shift(_TD_YEAR)
    return _safe_div_abs(dividends - prior, prior)


def dvd_056_dividends_cut_flag(dividends: pd.Series) -> pd.Series:
    """Binary: 1 when total dividends fell QoQ."""
    return (dividends < dividends.shift(_TD_QTR)).astype(float)


def dvd_057_dividends_omission_flag(dividends: pd.Series) -> pd.Series:
    """Binary: 1 when total dividends = 0."""
    return (dividends <= 0).astype(float)


def dvd_058_dividends_drawdown_from_1y_peak(dividends: pd.Series) -> pd.Series:
    """Total dividends drawdown from 1-year rolling peak."""
    peak = _rolling_max(dividends, _TD_YEAR)
    return dividends - peak


def dvd_059_dividends_drawdown_from_3y_peak(dividends: pd.Series) -> pd.Series:
    """Total dividends drawdown from 3-year rolling peak."""
    peak = _rolling_max(dividends, _TD_3Y)
    return dividends - peak


def dvd_060_dividends_drawdown_from_expanding_peak(dividends: pd.Series) -> pd.Series:
    """Total dividends vs all-history expanding maximum."""
    peak = dividends.expanding(min_periods=1).max()
    return dividends - peak


# --- Group E (061-075): Z-scores, rolling ranks, stability, and composites ---

def dvd_061_dps_zscore_1y(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 1-year (252-day) window."""
    return _zscore_rolling(dps, _TD_YEAR)


def dvd_062_dps_zscore_2y(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 2-year (504-day) window."""
    return _zscore_rolling(dps, _TD_2Y)


def dvd_063_dps_zscore_3y(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 3-year (756-day) window."""
    return _zscore_rolling(dps, _TD_3Y)


def dvd_064_dps_expanding_zscore(dps: pd.Series) -> pd.Series:
    """Expanding z-score of DPS (how extreme current DPS is vs entire history)."""
    m  = dps.expanding(min_periods=2).mean()
    sd = dps.expanding(min_periods=2).std()
    return _safe_div(dps - m, sd)


def dvd_065_dps_pct_rank_1y(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within a trailing 1-year window."""
    return _rolling_rank_pct(dps, _TD_YEAR)


def dvd_066_dps_pct_rank_3y(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within a trailing 3-year window."""
    return _rolling_rank_pct(dps, _TD_3Y)


def dvd_067_dps_expanding_pct_rank(dps: pd.Series) -> pd.Series:
    """Expanding percentile rank of DPS (all-history rank)."""
    return dps.expanding(min_periods=2).rank(pct=True)


def dvd_068_dps_volatility_1y(dps: pd.Series) -> pd.Series:
    """Rolling std of DPS over trailing 1 year (dividend stability)."""
    return _rolling_std(dps, _TD_YEAR)


def dvd_069_dps_volatility_2y(dps: pd.Series) -> pd.Series:
    """Rolling std of DPS over trailing 2 years."""
    return _rolling_std(dps, _TD_2Y)


def dvd_070_dps_coeff_variation_1y(dps: pd.Series) -> pd.Series:
    """Coefficient of variation of DPS over trailing 1 year (std / |mean|)."""
    m  = _rolling_mean(dps, _TD_YEAR)
    sd = _rolling_std(dps, _TD_YEAR)
    return _safe_div_abs(sd, m)


def dvd_071_dps_ewm_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 1-year EWM (span=252); captures momentum shift in dividends."""
    ewm = _ewm_mean(dps, _TD_YEAR)
    return dps - ewm


def dvd_072_dps_vs_dividends_consistency(dps: pd.Series, dividends: pd.Series) -> pd.Series:
    """
    Consistency ratio: DPS QoQ change direction vs dividends QoQ change direction.
    +1 if both move in the same direction, -1 if they diverge, 0 if either is unchanged.
    """
    dps_dir = np.sign(dps - dps.shift(_TD_QTR))
    div_dir = np.sign(dividends - dividends.shift(_TD_QTR))
    return (dps_dir * div_dir)


def dvd_073_dps_cut_severity_qoq(dps: pd.Series) -> pd.Series:
    """QoQ percent change in DPS clipped to [-10, 0] to measure cut severity."""
    chg = _safe_div_abs(dps - dps.shift(_TD_QTR), dps.shift(_TD_QTR))
    return chg.clip(upper=0)


def dvd_074_dps_cut_severity_yoy(dps: pd.Series) -> pd.Series:
    """YoY percent change in DPS clipped to [-10, 0] to measure annual cut severity."""
    chg = _safe_div_abs(dps - dps.shift(_TD_YEAR), dps.shift(_TD_YEAR))
    return chg.clip(upper=0)


def dvd_075_dividend_distress_composite(dps: pd.Series, dividends: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite dividend-distress severity score:
    equally weighted sum of three z-scores (dps, dividends, DPS/close yield proxy) in 1-year window.
    """
    z_dps  = _zscore_rolling(dps,       _TD_YEAR)
    z_div  = _zscore_rolling(dividends, _TD_YEAR)
    y      = _safe_div(dps * 4.0, close)
    z_yld  = _zscore_rolling(y,         _TD_YEAR)
    return (z_dps + z_div + z_yld) / 3.0


# --- Group K (151-165): Additional DPS stability, window, and cross-signal features ---

def dvd_151_dps_volatility_3y(dps: pd.Series) -> pd.Series:
    """Rolling std of DPS over trailing 3 years (extended instability gauge)."""
    return _rolling_std(dps, _TD_3Y)


def dvd_152_dps_coeff_variation_5y(dps: pd.Series) -> pd.Series:
    """Coefficient of variation of DPS over trailing 5 years (std / |mean|)."""
    m  = _rolling_mean(dps, _TD_5Y)
    sd = _rolling_std(dps, _TD_5Y)
    return _safe_div_abs(sd, m)


def dvd_153_dps_omission_fraction_2y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 2-year window with zero DPS."""
    zero = (dps <= 0).astype(float)
    return _rolling_mean(zero, _TD_2Y)


def dvd_154_dps_cuts_count_2q(dps: pd.Series) -> pd.Series:
    """Count of QoQ cut observations in trailing 2-quarter window."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_2Q)


def dvd_155_dps_to_2y_peak_ratio(dps: pd.Series) -> pd.Series:
    """Current DPS divided by trailing 2-year peak DPS."""
    peak = _rolling_max(dps, _TD_2Y)
    return _safe_div(dps, peak.replace(0, np.nan))


def dvd_156_dps_pct_drawdown_from_3y_peak(dps: pd.Series) -> pd.Series:
    """DPS percent drawdown from 3-year rolling peak."""
    peak = _rolling_max(dps, _TD_3Y)
    return _safe_div_abs(dps - peak, peak)


def dvd_157_dps_vs_5y_avg(dps: pd.Series) -> pd.Series:
    """DPS minus its trailing 5-year mean."""
    return dps - _rolling_mean(dps, _TD_5Y)


def dvd_158_dps_pct_vs_5y_avg(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from trailing 5-year mean."""
    avg = _rolling_mean(dps, _TD_5Y)
    return _safe_div_abs(dps - avg, avg)


def dvd_159_dps_median_deviation_5y(dps: pd.Series) -> pd.Series:
    """DPS minus trailing 5-year median."""
    return dps - _rolling_median(dps, _TD_5Y)


def dvd_160_dps_zscore_qtr(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 1-quarter (63-day) window."""
    return _zscore_rolling(dps, _TD_QTR)


def dvd_161_dps_pct_rank_2y(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within a trailing 2-year window."""
    return _rolling_rank_pct(dps, _TD_2Y)


def dvd_162_dps_ewm_2q_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 2-quarter EWM (span=126); medium-term momentum signal."""
    ewm = _ewm_mean(dps, _TD_2Q)
    return dps - ewm


def dvd_163_dps_range_2y(dps: pd.Series) -> pd.Series:
    """Trailing 2-year DPS range (max - min)."""
    return _rolling_max(dps, _TD_2Y) - _rolling_min(dps, _TD_2Y)


def dvd_164_dps_min_2y(dps: pd.Series) -> pd.Series:
    """Trailing 2-year minimum DPS value."""
    return _rolling_min(dps, _TD_2Y)


def dvd_165_dps_yoy_cut_fraction_3y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where DPS fell YoY."""
    cut = (dps < dps.shift(_TD_YEAR)).astype(float)
    return _rolling_mean(cut, _TD_3Y)


# --- Group L (166-175): Dividends extended + combined composite features ---

def dvd_166_dividends_pct_rank_2y(dividends: pd.Series) -> pd.Series:
    """Percentile rank of total dividends in trailing 2-year window."""
    return _rolling_rank_pct(dividends, _TD_2Y)


def dvd_167_dividends_volatility_3y(dividends: pd.Series) -> pd.Series:
    """Rolling std of total dividends over trailing 3 years."""
    return _rolling_std(dividends, _TD_3Y)


def dvd_168_dividends_coeff_variation_3y(dividends: pd.Series) -> pd.Series:
    """Coefficient of variation of total dividends over trailing 3 years."""
    m  = _rolling_mean(dividends, _TD_3Y)
    sd = _rolling_std(dividends, _TD_3Y)
    return _safe_div_abs(sd, m)


def dvd_169_dividends_pct_vs_5y_avg(dividends: pd.Series) -> pd.Series:
    """Total dividends percent deviation from trailing 5-year mean."""
    avg = _rolling_mean(dividends, _TD_5Y)
    return _safe_div_abs(dividends - avg, avg)


def dvd_170_dividends_to_1y_peak_ratio(dividends: pd.Series) -> pd.Series:
    """Current total dividends divided by trailing 1-year peak dividends."""
    peak = _rolling_max(dividends, _TD_YEAR)
    return _safe_div(dividends, peak.replace(0, np.nan))


def dvd_171_total_div_yield_zscore_3y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of total-dividends/close proxy in trailing 3-year window."""
    y = _safe_div(dividends, close)
    return _zscore_rolling(y, _TD_3Y)


def dvd_172_yield_proxy_2y_zscore(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DPS/close yield proxy in trailing 2-year window."""
    y = _safe_div(dps * 4.0, close)
    return _zscore_rolling(y, _TD_2Y)


def dvd_173_yield_proxy_2y_pct_rank(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of DPS/close yield proxy in trailing 2-year window."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_rank_pct(y, _TD_2Y)


def dvd_174_dps_price_ratio_2y_change(dps: pd.Series, close: pd.Series) -> pd.Series:
    """2-year change in DPS/close ratio (multi-year yield drift)."""
    y = _safe_div(dps, close)
    return y - y.shift(_TD_2Y)


def dvd_175_dividend_distress_composite_3y(dps: pd.Series, dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Composite distress score (3-year windows): equally weighted z-scores of dps, dividends, yield proxy."""
    z_dps = _zscore_rolling(dps,       _TD_3Y)
    z_div = _zscore_rolling(dividends, _TD_3Y)
    y     = _safe_div(dps * 4.0, close)
    z_yld = _zscore_rolling(y,         _TD_3Y)
    return (z_dps + z_div + z_yld) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

DIVIDEND_DISTRESS_REGISTRY_001_075 = {
    "dvd_001_dps_qoq_change":                        {"inputs": ["dps"],                          "func": dvd_001_dps_qoq_change},
    "dvd_002_dps_yoy_change":                        {"inputs": ["dps"],                          "func": dvd_002_dps_yoy_change},
    "dvd_003_dps_2y_change":                         {"inputs": ["dps"],                          "func": dvd_003_dps_2y_change},
    "dvd_004_dps_3y_change":                         {"inputs": ["dps"],                          "func": dvd_004_dps_3y_change},
    "dvd_005_dps_qoq_pct":                           {"inputs": ["dps"],                          "func": dvd_005_dps_qoq_pct},
    "dvd_006_dps_yoy_pct":                           {"inputs": ["dps"],                          "func": dvd_006_dps_yoy_pct},
    "dvd_007_dps_2y_pct":                            {"inputs": ["dps"],                          "func": dvd_007_dps_2y_pct},
    "dvd_008_dps_3y_pct":                            {"inputs": ["dps"],                          "func": dvd_008_dps_3y_pct},
    "dvd_009_dps_drawdown_from_1y_peak":             {"inputs": ["dps"],                          "func": dvd_009_dps_drawdown_from_1y_peak},
    "dvd_010_dps_drawdown_from_2y_peak":             {"inputs": ["dps"],                          "func": dvd_010_dps_drawdown_from_2y_peak},
    "dvd_011_dps_drawdown_from_3y_peak":             {"inputs": ["dps"],                          "func": dvd_011_dps_drawdown_from_3y_peak},
    "dvd_012_dps_drawdown_from_5y_peak":             {"inputs": ["dps"],                          "func": dvd_012_dps_drawdown_from_5y_peak},
    "dvd_013_dps_drawdown_from_expanding_peak":      {"inputs": ["dps"],                          "func": dvd_013_dps_drawdown_from_expanding_peak},
    "dvd_014_dps_pct_drawdown_from_1y_peak":         {"inputs": ["dps"],                          "func": dvd_014_dps_pct_drawdown_from_1y_peak},
    "dvd_015_dps_pct_drawdown_from_expanding_peak":  {"inputs": ["dps"],                          "func": dvd_015_dps_pct_drawdown_from_expanding_peak},
    "dvd_016_dps_cut_flag":                          {"inputs": ["dps"],                          "func": dvd_016_dps_cut_flag},
    "dvd_017_dps_cut_yoy_flag":                      {"inputs": ["dps"],                          "func": dvd_017_dps_cut_yoy_flag},
    "dvd_018_dps_omission_flag":                     {"inputs": ["dps"],                          "func": dvd_018_dps_omission_flag},
    "dvd_019_dps_suspension_flag":                   {"inputs": ["dps"],                          "func": dvd_019_dps_suspension_flag},
    "dvd_020_dps_first_cut_flag":                    {"inputs": ["dps"],                          "func": dvd_020_dps_first_cut_flag},
    "dvd_021_dps_consecutive_cut_streak":            {"inputs": ["dps"],                          "func": dvd_021_dps_consecutive_cut_streak},
    "dvd_022_dps_consecutive_zero_streak":           {"inputs": ["dps"],                          "func": dvd_022_dps_consecutive_zero_streak},
    "dvd_023_dps_cuts_count_1y":                     {"inputs": ["dps"],                          "func": dvd_023_dps_cuts_count_1y},
    "dvd_024_dps_cuts_count_2y":                     {"inputs": ["dps"],                          "func": dvd_024_dps_cuts_count_2y},
    "dvd_025_dps_cuts_count_3y":                     {"inputs": ["dps"],                          "func": dvd_025_dps_cuts_count_3y},
    "dvd_026_dps_cut_fraction_1y":                   {"inputs": ["dps"],                          "func": dvd_026_dps_cut_fraction_1y},
    "dvd_027_dps_cut_fraction_2y":                   {"inputs": ["dps"],                          "func": dvd_027_dps_cut_fraction_2y},
    "dvd_028_dps_cut_fraction_3y":                   {"inputs": ["dps"],                          "func": dvd_028_dps_cut_fraction_3y},
    "dvd_029_dps_omission_fraction_1y":              {"inputs": ["dps"],                          "func": dvd_029_dps_omission_fraction_1y},
    "dvd_030_dps_omission_fraction_3y":              {"inputs": ["dps"],                          "func": dvd_030_dps_omission_fraction_3y},
    "dvd_031_div_yield_proxy":                       {"inputs": ["dps", "close"],                 "func": dvd_031_div_yield_proxy},
    "dvd_032_div_yield_proxy_1y_avg":                {"inputs": ["dps", "close"],                 "func": dvd_032_div_yield_proxy_1y_avg},
    "dvd_033_div_yield_proxy_vs_1y_avg":             {"inputs": ["dps", "close"],                 "func": dvd_033_div_yield_proxy_vs_1y_avg},
    "dvd_034_div_yield_proxy_zscore_1y":             {"inputs": ["dps", "close"],                 "func": dvd_034_div_yield_proxy_zscore_1y},
    "dvd_035_div_yield_proxy_zscore_3y":             {"inputs": ["dps", "close"],                 "func": dvd_035_div_yield_proxy_zscore_3y},
    "dvd_036_div_yield_proxy_pct_rank_1y":           {"inputs": ["dps", "close"],                 "func": dvd_036_div_yield_proxy_pct_rank_1y},
    "dvd_037_div_yield_proxy_pct_rank_3y":           {"inputs": ["dps", "close"],                 "func": dvd_037_div_yield_proxy_pct_rank_3y},
    "dvd_038_div_yield_proxy_expanding_zscore":      {"inputs": ["dps", "close"],                 "func": dvd_038_div_yield_proxy_expanding_zscore},
    "dvd_039_yield_spike_flag":                      {"inputs": ["dps", "close"],                 "func": dvd_039_yield_spike_flag},
    "dvd_040_yield_collapse_flag":                   {"inputs": ["dps", "close"],                 "func": dvd_040_yield_collapse_flag},
    "dvd_041_total_div_yield_proxy":                 {"inputs": ["dividends", "close"],           "func": dvd_041_total_div_yield_proxy},
    "dvd_042_total_div_yield_zscore_1y":             {"inputs": ["dividends", "close"],           "func": dvd_042_total_div_yield_zscore_1y},
    "dvd_043_total_div_yield_pct_rank_1y":           {"inputs": ["dividends", "close"],           "func": dvd_043_total_div_yield_pct_rank_1y},
    "dvd_044_dps_price_ratio_qoq_change":            {"inputs": ["dps", "close"],                 "func": dvd_044_dps_price_ratio_qoq_change},
    "dvd_045_dps_price_ratio_yoy_change":            {"inputs": ["dps", "close"],                 "func": dvd_045_dps_price_ratio_yoy_change},
    "dvd_046_days_since_last_positive_dps":          {"inputs": ["dps"],                          "func": dvd_046_days_since_last_positive_dps},
    "dvd_047_days_since_last_div_increase":          {"inputs": ["dps"],                          "func": dvd_047_days_since_last_div_increase},
    "dvd_048_payment_gap_flag":                      {"inputs": ["dps"],                          "func": dvd_048_payment_gap_flag},
    "dvd_049_payment_gap_duration_1y":               {"inputs": ["dps"],                          "func": dvd_049_payment_gap_duration_1y},
    "dvd_050_payment_gap_duration_2y":               {"inputs": ["dps"],                          "func": dvd_050_payment_gap_duration_2y},
    "dvd_051_payment_gap_duration_3y":               {"inputs": ["dps"],                          "func": dvd_051_payment_gap_duration_3y},
    "dvd_052_dividends_qoq_change":                  {"inputs": ["dividends"],                    "func": dvd_052_dividends_qoq_change},
    "dvd_053_dividends_yoy_change":                  {"inputs": ["dividends"],                    "func": dvd_053_dividends_yoy_change},
    "dvd_054_dividends_qoq_pct":                     {"inputs": ["dividends"],                    "func": dvd_054_dividends_qoq_pct},
    "dvd_055_dividends_yoy_pct":                     {"inputs": ["dividends"],                    "func": dvd_055_dividends_yoy_pct},
    "dvd_056_dividends_cut_flag":                    {"inputs": ["dividends"],                    "func": dvd_056_dividends_cut_flag},
    "dvd_057_dividends_omission_flag":               {"inputs": ["dividends"],                    "func": dvd_057_dividends_omission_flag},
    "dvd_058_dividends_drawdown_from_1y_peak":       {"inputs": ["dividends"],                    "func": dvd_058_dividends_drawdown_from_1y_peak},
    "dvd_059_dividends_drawdown_from_3y_peak":       {"inputs": ["dividends"],                    "func": dvd_059_dividends_drawdown_from_3y_peak},
    "dvd_060_dividends_drawdown_from_expanding_peak":{"inputs": ["dividends"],                    "func": dvd_060_dividends_drawdown_from_expanding_peak},
    "dvd_061_dps_zscore_1y":                         {"inputs": ["dps"],                          "func": dvd_061_dps_zscore_1y},
    "dvd_062_dps_zscore_2y":                         {"inputs": ["dps"],                          "func": dvd_062_dps_zscore_2y},
    "dvd_063_dps_zscore_3y":                         {"inputs": ["dps"],                          "func": dvd_063_dps_zscore_3y},
    "dvd_064_dps_expanding_zscore":                  {"inputs": ["dps"],                          "func": dvd_064_dps_expanding_zscore},
    "dvd_065_dps_pct_rank_1y":                       {"inputs": ["dps"],                          "func": dvd_065_dps_pct_rank_1y},
    "dvd_066_dps_pct_rank_3y":                       {"inputs": ["dps"],                          "func": dvd_066_dps_pct_rank_3y},
    "dvd_067_dps_expanding_pct_rank":                {"inputs": ["dps"],                          "func": dvd_067_dps_expanding_pct_rank},
    "dvd_068_dps_volatility_1y":                     {"inputs": ["dps"],                          "func": dvd_068_dps_volatility_1y},
    "dvd_069_dps_volatility_2y":                     {"inputs": ["dps"],                          "func": dvd_069_dps_volatility_2y},
    "dvd_070_dps_coeff_variation_1y":                {"inputs": ["dps"],                          "func": dvd_070_dps_coeff_variation_1y},
    "dvd_071_dps_ewm_deviation":                     {"inputs": ["dps"],                          "func": dvd_071_dps_ewm_deviation},
    "dvd_072_dps_vs_dividends_consistency":          {"inputs": ["dps", "dividends"],             "func": dvd_072_dps_vs_dividends_consistency},
    "dvd_073_dps_cut_severity_qoq":                  {"inputs": ["dps"],                          "func": dvd_073_dps_cut_severity_qoq},
    "dvd_074_dps_cut_severity_yoy":                  {"inputs": ["dps"],                          "func": dvd_074_dps_cut_severity_yoy},
    "dvd_075_dividend_distress_composite":           {"inputs": ["dps", "dividends", "close"],    "func": dvd_075_dividend_distress_composite},
    "dvd_151_dps_volatility_3y":                     {"inputs": ["dps"],                          "func": dvd_151_dps_volatility_3y},
    "dvd_152_dps_coeff_variation_5y":                {"inputs": ["dps"],                          "func": dvd_152_dps_coeff_variation_5y},
    "dvd_153_dps_omission_fraction_2y":              {"inputs": ["dps"],                          "func": dvd_153_dps_omission_fraction_2y},
    "dvd_154_dps_cuts_count_2q":                     {"inputs": ["dps"],                          "func": dvd_154_dps_cuts_count_2q},
    "dvd_155_dps_to_2y_peak_ratio":                  {"inputs": ["dps"],                          "func": dvd_155_dps_to_2y_peak_ratio},
    "dvd_156_dps_pct_drawdown_from_3y_peak":         {"inputs": ["dps"],                          "func": dvd_156_dps_pct_drawdown_from_3y_peak},
    "dvd_157_dps_vs_5y_avg":                         {"inputs": ["dps"],                          "func": dvd_157_dps_vs_5y_avg},
    "dvd_158_dps_pct_vs_5y_avg":                     {"inputs": ["dps"],                          "func": dvd_158_dps_pct_vs_5y_avg},
    "dvd_159_dps_median_deviation_5y":               {"inputs": ["dps"],                          "func": dvd_159_dps_median_deviation_5y},
    "dvd_160_dps_zscore_qtr":                        {"inputs": ["dps"],                          "func": dvd_160_dps_zscore_qtr},
    "dvd_161_dps_pct_rank_2y":                       {"inputs": ["dps"],                          "func": dvd_161_dps_pct_rank_2y},
    "dvd_162_dps_ewm_2q_deviation":                  {"inputs": ["dps"],                          "func": dvd_162_dps_ewm_2q_deviation},
    "dvd_163_dps_range_2y":                          {"inputs": ["dps"],                          "func": dvd_163_dps_range_2y},
    "dvd_164_dps_min_2y":                            {"inputs": ["dps"],                          "func": dvd_164_dps_min_2y},
    "dvd_165_dps_yoy_cut_fraction_3y":               {"inputs": ["dps"],                          "func": dvd_165_dps_yoy_cut_fraction_3y},
    "dvd_166_dividends_pct_rank_2y":                 {"inputs": ["dividends"],                    "func": dvd_166_dividends_pct_rank_2y},
    "dvd_167_dividends_volatility_3y":               {"inputs": ["dividends"],                    "func": dvd_167_dividends_volatility_3y},
    "dvd_168_dividends_coeff_variation_3y":          {"inputs": ["dividends"],                    "func": dvd_168_dividends_coeff_variation_3y},
    "dvd_169_dividends_pct_vs_5y_avg":               {"inputs": ["dividends"],                    "func": dvd_169_dividends_pct_vs_5y_avg},
    "dvd_170_dividends_to_1y_peak_ratio":            {"inputs": ["dividends"],                    "func": dvd_170_dividends_to_1y_peak_ratio},
    "dvd_171_total_div_yield_zscore_3y":             {"inputs": ["dividends", "close"],           "func": dvd_171_total_div_yield_zscore_3y},
    "dvd_172_yield_proxy_2y_zscore":                 {"inputs": ["dps", "close"],                 "func": dvd_172_yield_proxy_2y_zscore},
    "dvd_173_yield_proxy_2y_pct_rank":               {"inputs": ["dps", "close"],                 "func": dvd_173_yield_proxy_2y_pct_rank},
    "dvd_174_dps_price_ratio_2y_change":             {"inputs": ["dps", "close"],                 "func": dvd_174_dps_price_ratio_2y_change},
    "dvd_175_dividend_distress_composite_3y":        {"inputs": ["dps", "dividends", "close"],    "func": dvd_175_dividend_distress_composite_3y},
}
