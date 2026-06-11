"""
96_dividend_distress — Base Features 076-150
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
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): DPS vs trailing averages and mean-reversion signals ---

def dvd_076_dps_vs_1y_avg(dps: pd.Series) -> pd.Series:
    """DPS minus its trailing 1-year mean (level deviation from recent norm)."""
    return dps - _rolling_mean(dps, _TD_YEAR)


def dvd_077_dps_vs_2y_avg(dps: pd.Series) -> pd.Series:
    """DPS minus its trailing 2-year mean."""
    return dps - _rolling_mean(dps, _TD_2Y)


def dvd_078_dps_vs_3y_avg(dps: pd.Series) -> pd.Series:
    """DPS minus its trailing 3-year mean."""
    return dps - _rolling_mean(dps, _TD_3Y)


def dvd_079_dps_pct_vs_1y_avg(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from trailing 1-year mean."""
    avg = _rolling_mean(dps, _TD_YEAR)
    return _safe_div_abs(dps - avg, avg)


def dvd_080_dps_pct_vs_2y_avg(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from trailing 2-year mean."""
    avg = _rolling_mean(dps, _TD_2Y)
    return _safe_div_abs(dps - avg, avg)


def dvd_081_dps_pct_vs_3y_avg(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from trailing 3-year mean."""
    avg = _rolling_mean(dps, _TD_3Y)
    return _safe_div_abs(dps - avg, avg)


def dvd_082_dps_median_deviation_1y(dps: pd.Series) -> pd.Series:
    """DPS minus trailing 1-year median."""
    return dps - _rolling_median(dps, _TD_YEAR)


def dvd_083_dps_median_deviation_3y(dps: pd.Series) -> pd.Series:
    """DPS minus trailing 3-year median."""
    return dps - _rolling_median(dps, _TD_3Y)


def dvd_084_dps_to_1y_peak_ratio(dps: pd.Series) -> pd.Series:
    """Current DPS divided by trailing 1-year peak DPS (peak-ratio)."""
    peak = _rolling_max(dps, _TD_YEAR)
    return _safe_div(dps, peak.replace(0, np.nan))


def dvd_085_dps_to_3y_peak_ratio(dps: pd.Series) -> pd.Series:
    """Current DPS divided by trailing 3-year peak DPS."""
    peak = _rolling_max(dps, _TD_3Y)
    return _safe_div(dps, peak.replace(0, np.nan))


def dvd_086_dps_to_expanding_peak_ratio(dps: pd.Series) -> pd.Series:
    """Current DPS divided by all-history expanding peak DPS."""
    peak = dps.expanding(min_periods=1).max()
    return _safe_div(dps, peak.replace(0, np.nan))


def dvd_087_dps_min_1y(dps: pd.Series) -> pd.Series:
    """Trailing 1-year minimum DPS value."""
    return _rolling_min(dps, _TD_YEAR)


def dvd_088_dps_min_3y(dps: pd.Series) -> pd.Series:
    """Trailing 3-year minimum DPS value."""
    return _rolling_min(dps, _TD_3Y)


def dvd_089_dps_range_1y(dps: pd.Series) -> pd.Series:
    """Trailing 1-year DPS range (max - min): dividend volatility band."""
    return _rolling_max(dps, _TD_YEAR) - _rolling_min(dps, _TD_YEAR)


def dvd_090_dps_range_3y(dps: pd.Series) -> pd.Series:
    """Trailing 3-year DPS range (max - min)."""
    return _rolling_max(dps, _TD_3Y) - _rolling_min(dps, _TD_3Y)


# --- Group G (091-105): Dividends total-amount features with windows ---

def dvd_091_dividends_zscore_1y(dividends: pd.Series) -> pd.Series:
    """Z-score of total dividends in trailing 1-year window."""
    return _zscore_rolling(dividends, _TD_YEAR)


def dvd_092_dividends_zscore_2y(dividends: pd.Series) -> pd.Series:
    """Z-score of total dividends in trailing 2-year window."""
    return _zscore_rolling(dividends, _TD_2Y)


def dvd_093_dividends_zscore_3y(dividends: pd.Series) -> pd.Series:
    """Z-score of total dividends in trailing 3-year window."""
    return _zscore_rolling(dividends, _TD_3Y)


def dvd_094_dividends_pct_rank_1y(dividends: pd.Series) -> pd.Series:
    """Percentile rank of total dividends in trailing 1-year window."""
    return _rolling_rank_pct(dividends, _TD_YEAR)


def dvd_095_dividends_pct_rank_3y(dividends: pd.Series) -> pd.Series:
    """Percentile rank of total dividends in trailing 3-year window."""
    return _rolling_rank_pct(dividends, _TD_3Y)


def dvd_096_dividends_expanding_zscore(dividends: pd.Series) -> pd.Series:
    """Expanding z-score of total dividends vs entire history."""
    m  = dividends.expanding(min_periods=2).mean()
    sd = dividends.expanding(min_periods=2).std()
    return _safe_div(dividends - m, sd)


def dvd_097_dividends_vs_1y_avg(dividends: pd.Series) -> pd.Series:
    """Total dividends minus trailing 1-year mean (level deviation)."""
    return dividends - _rolling_mean(dividends, _TD_YEAR)


def dvd_098_dividends_vs_3y_avg(dividends: pd.Series) -> pd.Series:
    """Total dividends minus trailing 3-year mean."""
    return dividends - _rolling_mean(dividends, _TD_3Y)


def dvd_099_dividends_pct_vs_1y_avg(dividends: pd.Series) -> pd.Series:
    """Total dividends percent deviation from trailing 1-year mean."""
    avg = _rolling_mean(dividends, _TD_YEAR)
    return _safe_div_abs(dividends - avg, avg)


def dvd_100_dividends_pct_vs_3y_avg(dividends: pd.Series) -> pd.Series:
    """Total dividends percent deviation from trailing 3-year mean."""
    avg = _rolling_mean(dividends, _TD_3Y)
    return _safe_div_abs(dividends - avg, avg)


def dvd_101_dividends_cut_count_1y(dividends: pd.Series) -> pd.Series:
    """Count of QoQ dividend-cut observations in trailing 1-year window."""
    cut = (dividends < dividends.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_YEAR)


def dvd_102_dividends_cut_count_3y(dividends: pd.Series) -> pd.Series:
    """Count of QoQ dividend-cut observations in trailing 3-year window."""
    cut = (dividends < dividends.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_3Y)


def dvd_103_dividends_min_1y(dividends: pd.Series) -> pd.Series:
    """Trailing 1-year minimum total dividends paid."""
    return _rolling_min(dividends, _TD_YEAR)


def dvd_104_dividends_min_3y(dividends: pd.Series) -> pd.Series:
    """Trailing 3-year minimum total dividends paid."""
    return _rolling_min(dividends, _TD_3Y)


def dvd_105_dividends_ewm_deviation(dividends: pd.Series) -> pd.Series:
    """Total dividends minus its 1-year EWM (span=252); momentum-shift in payout."""
    ewm = _ewm_mean(dividends, _TD_YEAR)
    return dividends - ewm


# --- Group H (106-120): Extended window / longer horizon features ---

def dvd_106_dps_zscore_5y(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 5-year (1260-day) window."""
    return _zscore_rolling(dps, _TD_5Y)


def dvd_107_dps_pct_rank_5y(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within trailing 5-year window."""
    return _rolling_rank_pct(dps, _TD_5Y)


def dvd_108_dps_cuts_count_5y(dps: pd.Series) -> pd.Series:
    """Count of QoQ cut observations in trailing 5-year window."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_5Y)


def dvd_109_dps_omission_fraction_5y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 5-year window with zero DPS."""
    zero = (dps <= 0).astype(float)
    return _rolling_mean(zero, _TD_5Y)


def dvd_110_dps_drawdown_from_5y_pct(dps: pd.Series) -> pd.Series:
    """DPS percent drawdown from 5-year rolling peak."""
    peak = _rolling_max(dps, _TD_5Y)
    return _safe_div_abs(dps - peak, peak)


def dvd_111_dps_min_5y(dps: pd.Series) -> pd.Series:
    """Trailing 5-year minimum DPS value."""
    return _rolling_min(dps, _TD_5Y)


def dvd_112_dps_range_5y(dps: pd.Series) -> pd.Series:
    """Trailing 5-year DPS range (max - min)."""
    return _rolling_max(dps, _TD_5Y) - _rolling_min(dps, _TD_5Y)


def dvd_113_dps_5y_pct_vs_avg(dps: pd.Series) -> pd.Series:
    """DPS percent deviation from trailing 5-year mean."""
    avg = _rolling_mean(dps, _TD_5Y)
    return _safe_div_abs(dps - avg, avg)


def dvd_114_dividends_zscore_5y(dividends: pd.Series) -> pd.Series:
    """Z-score of total dividends in trailing 5-year window."""
    return _zscore_rolling(dividends, _TD_5Y)


def dvd_115_dividends_pct_rank_5y(dividends: pd.Series) -> pd.Series:
    """Percentile rank of total dividends in trailing 5-year window."""
    return _rolling_rank_pct(dividends, _TD_5Y)


def dvd_116_dividends_cut_count_5y(dividends: pd.Series) -> pd.Series:
    """Count of QoQ dividend-cut observations in trailing 5-year window."""
    cut = (dividends < dividends.shift(_TD_QTR)).astype(float)
    return _rolling_sum(cut, _TD_5Y)


def dvd_117_dividends_drawdown_from_5y_peak(dividends: pd.Series) -> pd.Series:
    """Total dividends drawdown from 5-year rolling peak."""
    peak = _rolling_max(dividends, _TD_5Y)
    return dividends - peak


def dvd_118_dps_yoy_cut_fraction_5y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 5-year window where DPS fell YoY."""
    cut = (dps < dps.shift(_TD_YEAR)).astype(float)
    return _rolling_mean(cut, _TD_5Y)


def dvd_119_dps_mean_5y(dps: pd.Series) -> pd.Series:
    """Trailing 5-year mean DPS (baseline payout level)."""
    return _rolling_mean(dps, _TD_5Y)


def dvd_120_dps_volatility_5y(dps: pd.Series) -> pd.Series:
    """Rolling std of DPS over trailing 5 years."""
    return _rolling_std(dps, _TD_5Y)


# --- Group I (121-135): DPS acceleration, 2Q horizon, EWM features ---

def dvd_121_dps_2q_change(dps: pd.Series) -> pd.Series:
    """DPS change over 2 quarters (126-day lag)."""
    return dps - dps.shift(_TD_2Q)


def dvd_122_dps_2q_pct(dps: pd.Series) -> pd.Series:
    """DPS 2-quarter percent change."""
    prior = dps.shift(_TD_2Q)
    return _safe_div_abs(dps - prior, prior)


def dvd_123_dps_qoq_acceleration(dps: pd.Series) -> pd.Series:
    """Second difference of DPS over 63-day steps: acceleration of dividend trend."""
    d1 = dps - dps.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dvd_124_dps_ewm_short_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 1-quarter EWM (span=63); short-term momentum signal."""
    ewm = _ewm_mean(dps, _TD_QTR)
    return dps - ewm


def dvd_125_dps_ewm_long_deviation(dps: pd.Series) -> pd.Series:
    """DPS minus its 2-year EWM (span=504); long-term structural shift."""
    ewm = _ewm_mean(dps, _TD_2Y)
    return dps - ewm


def dvd_126_dps_ewm_ratio_short_to_long(dps: pd.Series) -> pd.Series:
    """Ratio of DPS 1-quarter EWM to 2-year EWM (trend momentum ratio)."""
    ewm_short = _ewm_mean(dps, _TD_QTR)
    ewm_long  = _ewm_mean(dps, _TD_2Y)
    return _safe_div(ewm_short, ewm_long.replace(0, np.nan))


def dvd_127_dps_1q_vs_1y_avg_ratio(dps: pd.Series) -> pd.Series:
    """DPS divided by its 1-year rolling mean (normalized payout level)."""
    avg = _rolling_mean(dps, _TD_YEAR)
    return _safe_div(dps, avg.replace(0, np.nan))


def dvd_128_dps_wk_rolling_mean(dps: pd.Series) -> pd.Series:
    """5-day (1 week) rolling mean of DPS (smoothed current level)."""
    return _rolling_mean(dps, _TD_WK)


def dvd_129_dps_mo_rolling_mean(dps: pd.Series) -> pd.Series:
    """21-day (1 month) rolling mean of DPS."""
    return _rolling_mean(dps, _TD_MO)


def dvd_130_dps_qtr_rolling_mean(dps: pd.Series) -> pd.Series:
    """63-day (1 quarter) rolling mean of DPS."""
    return _rolling_mean(dps, _TD_QTR)


def dvd_131_dividends_2q_change(dividends: pd.Series) -> pd.Series:
    """Total dividends change over 2 quarters (126-day lag)."""
    return dividends - dividends.shift(_TD_2Q)


def dvd_132_dividends_3y_pct(dividends: pd.Series) -> pd.Series:
    """Total dividends 3-year percent change."""
    prior = dividends.shift(_TD_3Y)
    return _safe_div_abs(dividends - prior, prior)


def dvd_133_dividends_5y_change(dividends: pd.Series) -> pd.Series:
    """Total dividends change over 5 years (1260-day lag)."""
    return dividends - dividends.shift(_TD_5Y)


def dvd_134_dividends_acceleration(dividends: pd.Series) -> pd.Series:
    """Second difference of total dividends over 63-day steps: payout acceleration."""
    d1 = dividends - dividends.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def dvd_135_dps_cumulative_4q_sum(dps: pd.Series) -> pd.Series:
    """Rolling 4-quarter (252-day) sum of DPS (trailing-twelve-month DPS proxy)."""
    return _rolling_sum(dps, _TD_YEAR)


# --- Group J (136-150): Cross-series, compound, and distress-composite features ---

def dvd_136_dps_cum_4q_vs_2y_avg(dps: pd.Series) -> pd.Series:
    """Trailing 4-quarter DPS sum vs its 2-year rolling mean."""
    ttm = _rolling_sum(dps, _TD_YEAR)
    return ttm - _rolling_mean(ttm, _TD_2Y)


def dvd_137_dividends_cum_4q_sum(dividends: pd.Series) -> pd.Series:
    """Rolling 4-quarter (252-day) sum of total dividends."""
    return _rolling_sum(dividends, _TD_YEAR)


def dvd_138_dividends_cum_4q_vs_3y_avg(dividends: pd.Series) -> pd.Series:
    """Rolling 4-quarter dividends sum vs its 3-year rolling mean."""
    ttm = _rolling_sum(dividends, _TD_YEAR)
    return ttm - _rolling_mean(ttm, _TD_3Y)


def dvd_139_dps_omission_flag_1q_lag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS was 0 one quarter ago (lagged omission)."""
    return (dps.shift(_TD_QTR) <= 0).astype(float)


def dvd_140_dps_double_cut_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS was cut QoQ this quarter AND last quarter."""
    cut_now  = (dps < dps.shift(_TD_QTR)).astype(float)
    cut_prev = (dps.shift(_TD_QTR) < dps.shift(_TD_2Q)).astype(float)
    return cut_now * cut_prev


def dvd_141_dps_cut_after_raise_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS cut this quarter but was raised two quarters ago."""
    cut_now  = (dps < dps.shift(_TD_QTR)).astype(float)
    raise_2q = (dps.shift(_TD_QTR) > dps.shift(_TD_2Q)).astype(float)
    return cut_now * raise_2q


def dvd_142_dps_vs_dividends_pct_gap(dps: pd.Series, dividends: pd.Series) -> pd.Series:
    """Percent gap between DPS QoQ change and dividends QoQ change (consistency check)."""
    dps_chg = _safe_div_abs(dps - dps.shift(_TD_QTR), dps.shift(_TD_QTR))
    div_chg = _safe_div_abs(dividends - dividends.shift(_TD_QTR), dividends.shift(_TD_QTR))
    return dps_chg - div_chg


def dvd_143_yield_proxy_vs_3y_max(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy vs its 3-year rolling max (is yield at all-time high = distress?)."""
    y = _safe_div(dps * 4.0, close)
    peak = _rolling_max(y, _TD_3Y)
    return _safe_div_abs(y - peak, peak)


def dvd_144_yield_proxy_vs_5y_max(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy vs its 5-year rolling max."""
    y = _safe_div(dps * 4.0, close)
    peak = _rolling_max(y, _TD_5Y)
    return _safe_div_abs(y - peak, peak)


def dvd_145_yield_proxy_5y_zscore(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of DPS/close yield proxy in trailing 5-year window."""
    y = _safe_div(dps * 4.0, close)
    return _zscore_rolling(y, _TD_5Y)


def dvd_146_yield_proxy_5y_pct_rank(dps: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of DPS/close yield proxy in trailing 5-year window."""
    y = _safe_div(dps * 4.0, close)
    return _rolling_rank_pct(y, _TD_5Y)


def dvd_147_dps_coeff_variation_3y(dps: pd.Series) -> pd.Series:
    """Coefficient of variation of DPS over trailing 3 years (std / |mean|)."""
    m  = _rolling_mean(dps, _TD_3Y)
    sd = _rolling_std(dps, _TD_3Y)
    return _safe_div_abs(sd, m)


def dvd_148_dividends_volatility_1y(dividends: pd.Series) -> pd.Series:
    """Rolling std of total dividends over trailing 1 year."""
    return _rolling_std(dividends, _TD_YEAR)


def dvd_149_dividends_coeff_variation_1y(dividends: pd.Series) -> pd.Series:
    """Coefficient of variation of total dividends over trailing 1 year."""
    m  = _rolling_mean(dividends, _TD_YEAR)
    sd = _rolling_std(dividends, _TD_YEAR)
    return _safe_div_abs(sd, m)


def dvd_150_dividend_distress_composite_5y(dps: pd.Series, dividends: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite dividend-distress severity score using 5-year windows:
    equally weighted sum of three z-scores (dps, dividends, DPS/close proxy).
    """
    z_dps  = _zscore_rolling(dps,       _TD_5Y)
    z_div  = _zscore_rolling(dividends, _TD_5Y)
    y      = _safe_div(dps * 4.0, close)
    z_yld  = _zscore_rolling(y,         _TD_5Y)
    return (z_dps + z_div + z_yld) / 3.0


# --- Group K2 (176-190): Additional per-share, aggregate, and ratio features ---

def dvd_176_dps_qoq_change_abs(dps: pd.Series) -> pd.Series:
    """Absolute value of QoQ DPS change (magnitude regardless of direction)."""
    return (dps - dps.shift(_TD_QTR)).abs()


def dvd_177_dps_yoy_change_abs(dps: pd.Series) -> pd.Series:
    """Absolute value of YoY DPS change (magnitude of annual shift)."""
    return (dps - dps.shift(_TD_YEAR)).abs()


def dvd_178_dps_avg_abs_qoq_change_1y(dps: pd.Series) -> pd.Series:
    """Trailing 1-year mean of absolute QoQ DPS changes (average chop)."""
    return _rolling_mean((dps - dps.shift(_TD_QTR)).abs(), _TD_YEAR)


def dvd_179_dps_avg_abs_qoq_change_3y(dps: pd.Series) -> pd.Series:
    """Trailing 3-year mean of absolute QoQ DPS changes."""
    return _rolling_mean((dps - dps.shift(_TD_QTR)).abs(), _TD_3Y)


def dvd_180_dps_positive_fraction_1y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 1-year window where DPS was strictly positive."""
    pos = (dps > 0).astype(float)
    return _rolling_mean(pos, _TD_YEAR)


def dvd_181_dps_positive_fraction_3y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where DPS was strictly positive."""
    pos = (dps > 0).astype(float)
    return _rolling_mean(pos, _TD_3Y)


def dvd_182_dps_raise_count_1y(dps: pd.Series) -> pd.Series:
    """Count of QoQ DPS increase observations in trailing 1-year window."""
    inc = (dps > dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(inc, _TD_YEAR)


def dvd_183_dps_raise_count_3y(dps: pd.Series) -> pd.Series:
    """Count of QoQ DPS increase observations in trailing 3-year window."""
    inc = (dps > dps.shift(_TD_QTR)).astype(float)
    return _rolling_sum(inc, _TD_3Y)


def dvd_184_dps_cut_to_raise_ratio_1y(dps: pd.Series) -> pd.Series:
    """Ratio of QoQ cuts to QoQ raises in trailing 1-year window."""
    cut = _rolling_sum((dps < dps.shift(_TD_QTR)).astype(float), _TD_YEAR)
    inc = _rolling_sum((dps > dps.shift(_TD_QTR)).astype(float), _TD_YEAR)
    return _safe_div(cut, inc.replace(0, np.nan))


def dvd_185_dps_flat_fraction_1y(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 1-year window where DPS was unchanged QoQ."""
    flat = (dps == dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(flat, _TD_YEAR)


def dvd_186_dividends_min_2y(dividends: pd.Series) -> pd.Series:
    """Trailing 2-year minimum total dividends."""
    return _rolling_min(dividends, _TD_2Y)


def dvd_187_dividends_range_1y(dividends: pd.Series) -> pd.Series:
    """Trailing 1-year total-dividends range (max - min)."""
    return _rolling_max(dividends, _TD_YEAR) - _rolling_min(dividends, _TD_YEAR)


def dvd_188_dividends_range_3y(dividends: pd.Series) -> pd.Series:
    """Trailing 3-year total-dividends range (max - min)."""
    return _rolling_max(dividends, _TD_3Y) - _rolling_min(dividends, _TD_3Y)


def dvd_189_dividends_to_3y_peak_ratio(dividends: pd.Series) -> pd.Series:
    """Current total dividends divided by trailing 3-year peak."""
    peak = _rolling_max(dividends, _TD_3Y)
    return _safe_div(dividends, peak.replace(0, np.nan))


def dvd_190_dividends_pct_drawdown_from_1y_peak(dividends: pd.Series) -> pd.Series:
    """Total dividends percent drawdown from 1-year rolling peak."""
    peak = _rolling_max(dividends, _TD_YEAR)
    return _safe_div_abs(dividends - peak, peak)


# --- Group L2 (191-200): Cross-field, composite, and distress extremity features ---

def dvd_191_dps_vs_dividends_level_ratio(dps: pd.Series, dividends: pd.Series) -> pd.Series:
    """Ratio of DPS to total dividends (per-share payout concentration)."""
    return _safe_div(dps, dividends.replace(0, np.nan))


def dvd_192_yield_proxy_qoq_change(dps: pd.Series, close: pd.Series) -> pd.Series:
    """QoQ absolute change in DPS/close yield proxy (yield momentum)."""
    y = _safe_div(dps * 4.0, close)
    return y - y.shift(_TD_QTR)


def dvd_193_yield_proxy_vs_2y_avg(dps: pd.Series, close: pd.Series) -> pd.Series:
    """DPS/close yield proxy minus its trailing 2-year mean."""
    y = _safe_div(dps * 4.0, close)
    return y - _rolling_mean(y, _TD_2Y)


def dvd_194_total_div_yield_pct_rank_3y(dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of total-dividends/close proxy in trailing 3-year window."""
    y = _safe_div(dividends, close)
    return _rolling_rank_pct(y, _TD_3Y)


def dvd_195_dps_cut_fraction_qtr(dps: pd.Series) -> pd.Series:
    """Fraction of trailing 1-quarter window where DPS was cut QoQ."""
    cut = (dps < dps.shift(_TD_QTR)).astype(float)
    return _rolling_mean(cut, _TD_QTR)


def dvd_196_dps_zscore_2q(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within a trailing 2-quarter (126-day) window."""
    return _zscore_rolling(dps, _TD_2Q)


def dvd_197_dps_expanding_min(dps: pd.Series) -> pd.Series:
    """All-history expanding minimum DPS (absolute low watermark)."""
    return dps.expanding(min_periods=1).min()


def dvd_198_dividends_expanding_min(dividends: pd.Series) -> pd.Series:
    """All-history expanding minimum total dividends (absolute low watermark)."""
    return dividends.expanding(min_periods=1).min()


def dvd_199_dps_at_expanding_min_flag(dps: pd.Series) -> pd.Series:
    """Binary: 1 when DPS equals its all-history expanding minimum (new all-time low)."""
    exp_min = dps.expanding(min_periods=1).min()
    return (dps <= exp_min).astype(float)


def dvd_200_dividend_distress_composite_expanding(dps: pd.Series, dividends: pd.Series, close: pd.Series) -> pd.Series:
    """Composite distress score using expanding z-scores: how extreme dps, dividends, and yield are vs all history."""
    def _exp_z(s):
        m  = s.expanding(min_periods=2).mean()
        sd = s.expanding(min_periods=2).std()
        return _safe_div(s - m, sd)
    y = _safe_div(dps * 4.0, close)
    return (_exp_z(dps) + _exp_z(dividends) + _exp_z(y)) / 3.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

DIVIDEND_DISTRESS_REGISTRY_076_150 = {
    "dvd_076_dps_vs_1y_avg":                         {"inputs": ["dps"],                          "func": dvd_076_dps_vs_1y_avg},
    "dvd_077_dps_vs_2y_avg":                         {"inputs": ["dps"],                          "func": dvd_077_dps_vs_2y_avg},
    "dvd_078_dps_vs_3y_avg":                         {"inputs": ["dps"],                          "func": dvd_078_dps_vs_3y_avg},
    "dvd_079_dps_pct_vs_1y_avg":                     {"inputs": ["dps"],                          "func": dvd_079_dps_pct_vs_1y_avg},
    "dvd_080_dps_pct_vs_2y_avg":                     {"inputs": ["dps"],                          "func": dvd_080_dps_pct_vs_2y_avg},
    "dvd_081_dps_pct_vs_3y_avg":                     {"inputs": ["dps"],                          "func": dvd_081_dps_pct_vs_3y_avg},
    "dvd_082_dps_median_deviation_1y":               {"inputs": ["dps"],                          "func": dvd_082_dps_median_deviation_1y},
    "dvd_083_dps_median_deviation_3y":               {"inputs": ["dps"],                          "func": dvd_083_dps_median_deviation_3y},
    "dvd_084_dps_to_1y_peak_ratio":                  {"inputs": ["dps"],                          "func": dvd_084_dps_to_1y_peak_ratio},
    "dvd_085_dps_to_3y_peak_ratio":                  {"inputs": ["dps"],                          "func": dvd_085_dps_to_3y_peak_ratio},
    "dvd_086_dps_to_expanding_peak_ratio":           {"inputs": ["dps"],                          "func": dvd_086_dps_to_expanding_peak_ratio},
    "dvd_087_dps_min_1y":                            {"inputs": ["dps"],                          "func": dvd_087_dps_min_1y},
    "dvd_088_dps_min_3y":                            {"inputs": ["dps"],                          "func": dvd_088_dps_min_3y},
    "dvd_089_dps_range_1y":                          {"inputs": ["dps"],                          "func": dvd_089_dps_range_1y},
    "dvd_090_dps_range_3y":                          {"inputs": ["dps"],                          "func": dvd_090_dps_range_3y},
    "dvd_091_dividends_zscore_1y":                   {"inputs": ["dividends"],                    "func": dvd_091_dividends_zscore_1y},
    "dvd_092_dividends_zscore_2y":                   {"inputs": ["dividends"],                    "func": dvd_092_dividends_zscore_2y},
    "dvd_093_dividends_zscore_3y":                   {"inputs": ["dividends"],                    "func": dvd_093_dividends_zscore_3y},
    "dvd_094_dividends_pct_rank_1y":                 {"inputs": ["dividends"],                    "func": dvd_094_dividends_pct_rank_1y},
    "dvd_095_dividends_pct_rank_3y":                 {"inputs": ["dividends"],                    "func": dvd_095_dividends_pct_rank_3y},
    "dvd_096_dividends_expanding_zscore":            {"inputs": ["dividends"],                    "func": dvd_096_dividends_expanding_zscore},
    "dvd_097_dividends_vs_1y_avg":                   {"inputs": ["dividends"],                    "func": dvd_097_dividends_vs_1y_avg},
    "dvd_098_dividends_vs_3y_avg":                   {"inputs": ["dividends"],                    "func": dvd_098_dividends_vs_3y_avg},
    "dvd_099_dividends_pct_vs_1y_avg":               {"inputs": ["dividends"],                    "func": dvd_099_dividends_pct_vs_1y_avg},
    "dvd_100_dividends_pct_vs_3y_avg":               {"inputs": ["dividends"],                    "func": dvd_100_dividends_pct_vs_3y_avg},
    "dvd_101_dividends_cut_count_1y":                {"inputs": ["dividends"],                    "func": dvd_101_dividends_cut_count_1y},
    "dvd_102_dividends_cut_count_3y":                {"inputs": ["dividends"],                    "func": dvd_102_dividends_cut_count_3y},
    "dvd_103_dividends_min_1y":                      {"inputs": ["dividends"],                    "func": dvd_103_dividends_min_1y},
    "dvd_104_dividends_min_3y":                      {"inputs": ["dividends"],                    "func": dvd_104_dividends_min_3y},
    "dvd_105_dividends_ewm_deviation":               {"inputs": ["dividends"],                    "func": dvd_105_dividends_ewm_deviation},
    "dvd_106_dps_zscore_5y":                         {"inputs": ["dps"],                          "func": dvd_106_dps_zscore_5y},
    "dvd_107_dps_pct_rank_5y":                       {"inputs": ["dps"],                          "func": dvd_107_dps_pct_rank_5y},
    "dvd_108_dps_cuts_count_5y":                     {"inputs": ["dps"],                          "func": dvd_108_dps_cuts_count_5y},
    "dvd_109_dps_omission_fraction_5y":              {"inputs": ["dps"],                          "func": dvd_109_dps_omission_fraction_5y},
    "dvd_110_dps_drawdown_from_5y_pct":              {"inputs": ["dps"],                          "func": dvd_110_dps_drawdown_from_5y_pct},
    "dvd_111_dps_min_5y":                            {"inputs": ["dps"],                          "func": dvd_111_dps_min_5y},
    "dvd_112_dps_range_5y":                          {"inputs": ["dps"],                          "func": dvd_112_dps_range_5y},
    "dvd_113_dps_5y_pct_vs_avg":                     {"inputs": ["dps"],                          "func": dvd_113_dps_5y_pct_vs_avg},
    "dvd_114_dividends_zscore_5y":                   {"inputs": ["dividends"],                    "func": dvd_114_dividends_zscore_5y},
    "dvd_115_dividends_pct_rank_5y":                 {"inputs": ["dividends"],                    "func": dvd_115_dividends_pct_rank_5y},
    "dvd_116_dividends_cut_count_5y":                {"inputs": ["dividends"],                    "func": dvd_116_dividends_cut_count_5y},
    "dvd_117_dividends_drawdown_from_5y_peak":       {"inputs": ["dividends"],                    "func": dvd_117_dividends_drawdown_from_5y_peak},
    "dvd_118_dps_yoy_cut_fraction_5y":               {"inputs": ["dps"],                          "func": dvd_118_dps_yoy_cut_fraction_5y},
    "dvd_119_dps_mean_5y":                           {"inputs": ["dps"],                          "func": dvd_119_dps_mean_5y},
    "dvd_120_dps_volatility_5y":                     {"inputs": ["dps"],                          "func": dvd_120_dps_volatility_5y},
    "dvd_121_dps_2q_change":                         {"inputs": ["dps"],                          "func": dvd_121_dps_2q_change},
    "dvd_122_dps_2q_pct":                            {"inputs": ["dps"],                          "func": dvd_122_dps_2q_pct},
    "dvd_123_dps_qoq_acceleration":                  {"inputs": ["dps"],                          "func": dvd_123_dps_qoq_acceleration},
    "dvd_124_dps_ewm_short_deviation":               {"inputs": ["dps"],                          "func": dvd_124_dps_ewm_short_deviation},
    "dvd_125_dps_ewm_long_deviation":                {"inputs": ["dps"],                          "func": dvd_125_dps_ewm_long_deviation},
    "dvd_126_dps_ewm_ratio_short_to_long":           {"inputs": ["dps"],                          "func": dvd_126_dps_ewm_ratio_short_to_long},
    "dvd_127_dps_1q_vs_1y_avg_ratio":               {"inputs": ["dps"],                          "func": dvd_127_dps_1q_vs_1y_avg_ratio},
    "dvd_128_dps_wk_rolling_mean":                   {"inputs": ["dps"],                          "func": dvd_128_dps_wk_rolling_mean},
    "dvd_129_dps_mo_rolling_mean":                   {"inputs": ["dps"],                          "func": dvd_129_dps_mo_rolling_mean},
    "dvd_130_dps_qtr_rolling_mean":                  {"inputs": ["dps"],                          "func": dvd_130_dps_qtr_rolling_mean},
    "dvd_131_dividends_2q_change":                   {"inputs": ["dividends"],                    "func": dvd_131_dividends_2q_change},
    "dvd_132_dividends_3y_pct":                      {"inputs": ["dividends"],                    "func": dvd_132_dividends_3y_pct},
    "dvd_133_dividends_5y_change":                   {"inputs": ["dividends"],                    "func": dvd_133_dividends_5y_change},
    "dvd_134_dividends_acceleration":                {"inputs": ["dividends"],                    "func": dvd_134_dividends_acceleration},
    "dvd_135_dps_cumulative_4q_sum":                 {"inputs": ["dps"],                          "func": dvd_135_dps_cumulative_4q_sum},
    "dvd_136_dps_cum_4q_vs_2y_avg":                  {"inputs": ["dps"],                          "func": dvd_136_dps_cum_4q_vs_2y_avg},
    "dvd_137_dividends_cum_4q_sum":                  {"inputs": ["dividends"],                    "func": dvd_137_dividends_cum_4q_sum},
    "dvd_138_dividends_cum_4q_vs_3y_avg":            {"inputs": ["dividends"],                    "func": dvd_138_dividends_cum_4q_vs_3y_avg},
    "dvd_139_dps_omission_flag_1q_lag":              {"inputs": ["dps"],                          "func": dvd_139_dps_omission_flag_1q_lag},
    "dvd_140_dps_double_cut_flag":                   {"inputs": ["dps"],                          "func": dvd_140_dps_double_cut_flag},
    "dvd_141_dps_cut_after_raise_flag":              {"inputs": ["dps"],                          "func": dvd_141_dps_cut_after_raise_flag},
    "dvd_142_dps_vs_dividends_pct_gap":              {"inputs": ["dps", "dividends"],             "func": dvd_142_dps_vs_dividends_pct_gap},
    "dvd_143_yield_proxy_vs_3y_max":                 {"inputs": ["dps", "close"],                 "func": dvd_143_yield_proxy_vs_3y_max},
    "dvd_144_yield_proxy_vs_5y_max":                 {"inputs": ["dps", "close"],                 "func": dvd_144_yield_proxy_vs_5y_max},
    "dvd_145_yield_proxy_5y_zscore":                 {"inputs": ["dps", "close"],                 "func": dvd_145_yield_proxy_5y_zscore},
    "dvd_146_yield_proxy_5y_pct_rank":               {"inputs": ["dps", "close"],                 "func": dvd_146_yield_proxy_5y_pct_rank},
    "dvd_147_dps_coeff_variation_3y":                {"inputs": ["dps"],                          "func": dvd_147_dps_coeff_variation_3y},
    "dvd_148_dividends_volatility_1y":               {"inputs": ["dividends"],                    "func": dvd_148_dividends_volatility_1y},
    "dvd_149_dividends_coeff_variation_1y":          {"inputs": ["dividends"],                    "func": dvd_149_dividends_coeff_variation_1y},
    "dvd_150_dividend_distress_composite_5y":        {"inputs": ["dps", "dividends", "close"],    "func": dvd_150_dividend_distress_composite_5y},
    "dvd_176_dps_qoq_change_abs":                    {"inputs": ["dps"],                          "func": dvd_176_dps_qoq_change_abs},
    "dvd_177_dps_yoy_change_abs":                    {"inputs": ["dps"],                          "func": dvd_177_dps_yoy_change_abs},
    "dvd_178_dps_avg_abs_qoq_change_1y":             {"inputs": ["dps"],                          "func": dvd_178_dps_avg_abs_qoq_change_1y},
    "dvd_179_dps_avg_abs_qoq_change_3y":             {"inputs": ["dps"],                          "func": dvd_179_dps_avg_abs_qoq_change_3y},
    "dvd_180_dps_positive_fraction_1y":              {"inputs": ["dps"],                          "func": dvd_180_dps_positive_fraction_1y},
    "dvd_181_dps_positive_fraction_3y":              {"inputs": ["dps"],                          "func": dvd_181_dps_positive_fraction_3y},
    "dvd_182_dps_raise_count_1y":                    {"inputs": ["dps"],                          "func": dvd_182_dps_raise_count_1y},
    "dvd_183_dps_raise_count_3y":                    {"inputs": ["dps"],                          "func": dvd_183_dps_raise_count_3y},
    "dvd_184_dps_cut_to_raise_ratio_1y":             {"inputs": ["dps"],                          "func": dvd_184_dps_cut_to_raise_ratio_1y},
    "dvd_185_dps_flat_fraction_1y":                  {"inputs": ["dps"],                          "func": dvd_185_dps_flat_fraction_1y},
    "dvd_186_dividends_min_2y":                      {"inputs": ["dividends"],                    "func": dvd_186_dividends_min_2y},
    "dvd_187_dividends_range_1y":                    {"inputs": ["dividends"],                    "func": dvd_187_dividends_range_1y},
    "dvd_188_dividends_range_3y":                    {"inputs": ["dividends"],                    "func": dvd_188_dividends_range_3y},
    "dvd_189_dividends_to_3y_peak_ratio":            {"inputs": ["dividends"],                    "func": dvd_189_dividends_to_3y_peak_ratio},
    "dvd_190_dividends_pct_drawdown_from_1y_peak":   {"inputs": ["dividends"],                    "func": dvd_190_dividends_pct_drawdown_from_1y_peak},
    "dvd_191_dps_vs_dividends_level_ratio":          {"inputs": ["dps", "dividends"],             "func": dvd_191_dps_vs_dividends_level_ratio},
    "dvd_192_yield_proxy_qoq_change":                {"inputs": ["dps", "close"],                 "func": dvd_192_yield_proxy_qoq_change},
    "dvd_193_yield_proxy_vs_2y_avg":                 {"inputs": ["dps", "close"],                 "func": dvd_193_yield_proxy_vs_2y_avg},
    "dvd_194_total_div_yield_pct_rank_3y":           {"inputs": ["dividends", "close"],           "func": dvd_194_total_div_yield_pct_rank_3y},
    "dvd_195_dps_cut_fraction_qtr":                  {"inputs": ["dps"],                          "func": dvd_195_dps_cut_fraction_qtr},
    "dvd_196_dps_zscore_2q":                         {"inputs": ["dps"],                          "func": dvd_196_dps_zscore_2q},
    "dvd_197_dps_expanding_min":                     {"inputs": ["dps"],                          "func": dvd_197_dps_expanding_min},
    "dvd_198_dividends_expanding_min":               {"inputs": ["dividends"],                    "func": dvd_198_dividends_expanding_min},
    "dvd_199_dps_at_expanding_min_flag":             {"inputs": ["dps"],                          "func": dvd_199_dps_at_expanding_min_flag},
    "dvd_200_dividend_distress_composite_expanding": {"inputs": ["dps", "dividends", "close"],    "func": dvd_200_dividend_distress_composite_expanding},
}
