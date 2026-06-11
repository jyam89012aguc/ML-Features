"""
12_high_water_distance — Base Features 076-150
Domain: distance, time, and regain-multiple relative to prior all-time / expanding-window
        high-water mark (HWM). Continues 001-075 with more specialized HWM features.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _expanding_hwm(s: pd.Series) -> pd.Series:
    """Expanding (all-time) high-water mark."""
    return s.expanding(min_periods=1).max()


def _days_since_expanding_max(s: pd.Series) -> pd.Series:
    """Number of bars elapsed since the expanding-window maximum was last set."""
    hwm = _expanding_hwm(s)
    at_peak = (s >= hwm).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _days_since_rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars elapsed since the rolling-w maximum was last set."""
    roll_max = _rolling_max(s, w)
    at_peak = (s >= roll_max).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        xm = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - xm)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-088): HWM distance using open / high / low prices ---

def hwd_076_hwm_open_pct_below_ath(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price vs expanding ATH close HWM: (open - ATH) / ATH."""
    hwm = _expanding_hwm(close)
    return _safe_div(open - hwm, hwm)


def hwd_077_hwm_low_pct_below_ath(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs expanding ATH close HWM."""
    hwm = _expanding_hwm(close)
    return _safe_div(low - hwm, hwm)


def hwd_078_hwm_high_pct_below_ath(close: pd.Series, high: pd.Series) -> pd.Series:
    """Intraday high vs expanding ATH close HWM."""
    hwm = _expanding_hwm(close)
    return _safe_div(high - hwm, hwm)


def hwd_079_hwm_intraday_ath_pct_below(high: pd.Series) -> pd.Series:
    """Intraday high vs expanding intraday ATH (all-time intraday high)."""
    hwm = high.expanding(min_periods=1).max()
    return _safe_div(high - hwm, hwm)


def hwd_080_hwm_low_log_dist_ath(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log distance from intraday low to expanding ATH close."""
    hwm = _expanding_hwm(close)
    return _log_safe(hwm) - _log_safe(low)


def hwd_081_hwm_open_log_dist_ath(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log distance from open to expanding ATH close."""
    hwm = _expanding_hwm(close)
    return _log_safe(hwm) - _log_safe(open)


def hwd_082_hwm_low_vs_intraday_ath(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log distance from intraday low to expanding intraday all-time high."""
    hwm = high.expanding(min_periods=1).max()
    return _log_safe(hwm) - _log_safe(low)


def hwd_083_hwm_range_pct_ath(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday range (high-low) as percent of ATH level (absolute range vs peak)."""
    hwm = _expanding_hwm(close)
    rng = high - low
    return _safe_div(rng, hwm)


def hwd_084_hwm_close_in_day_range_vs_ath(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close within intraday range, scaled by ATH distance."""
    pos = _safe_div(close - low, (high - low).replace(0, np.nan))
    hwm = _expanding_hwm(close)
    ath_dist = _safe_div(close - hwm, hwm)
    return pos * ath_dist.abs()


def hwd_085_hwm_open_vs_1y_hwm(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price vs 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(open - hwm, hwm)


def hwd_086_hwm_low_vs_1y_hwm(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(low - hwm, hwm)


def hwd_087_hwm_high_vs_1y_hwm(close: pd.Series, high: pd.Series) -> pd.Series:
    """Intraday high vs 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(high - hwm, hwm)


def hwd_088_hwm_intraday_range_vs_ath_gap(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday range (H-L) expressed as fraction of the absolute ATH gap."""
    hwm = _expanding_hwm(close)
    gap = (hwm - close).replace(0, np.nan)
    rng = high - low
    return _safe_div(rng, gap)


# --- Group I (089-100): Velocity of time accumulation since peak ---

def hwd_089_hwm_days_since_ath_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in days-since-ATH (normally +5 unless new ATH made)."""
    d = _days_since_expanding_max(close)
    return d.diff(5)


def hwd_090_hwm_days_since_ath_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in days-since-ATH."""
    d = _days_since_expanding_max(close)
    return d.diff(_TD_MON)


def hwd_091_hwm_days_since_ath_63d_chg(close: pd.Series) -> pd.Series:
    """63-day change in days-since-ATH (resets when new ATH formed)."""
    d = _days_since_expanding_max(close)
    return d.diff(_TD_QTR)


def hwd_092_hwm_days_since_1y_hwm_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in days-since-1y-HWM."""
    d = _days_since_rolling_max(close, _TD_YEAR)
    return d.diff(5)


def hwd_093_hwm_time_accel_ath(close: pd.Series) -> pd.Series:
    """Acceleration of time-since-ATH: second difference over 5-day spans."""
    d = _days_since_expanding_max(close)
    return d.diff(5).diff(5)


def hwd_094_hwm_log_dist_rate_5d(close: pd.Series) -> pd.Series:
    """5-day rate of change of log-distance from ATH (worsening pace)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return ld.diff(5)


def hwd_095_hwm_log_dist_rate_21d(close: pd.Series) -> pd.Series:
    """21-day rate of change of log-distance from ATH."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return ld.diff(_TD_MON)


def hwd_096_hwm_pct_below_ath_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in pct-below-ATH (velocity of deterioration from peak)."""
    pct = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return pct.diff(5)


def hwd_097_hwm_pct_below_ath_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in pct-below-ATH."""
    pct = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return pct.diff(_TD_MON)


def hwd_098_hwm_pct_below_1y_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in pct-below-1y-HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    pct = _safe_div(close - hwm, hwm)
    return pct.diff(5)


def hwd_099_hwm_regain_multiple_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in ATH regain multiple (how much harder is recovery getting)."""
    rm = _safe_div(_expanding_hwm(close), close)
    return rm.diff(5)


def hwd_100_hwm_regain_multiple_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in ATH regain multiple."""
    rm = _safe_div(_expanding_hwm(close), close)
    return rm.diff(_TD_MON)


# --- Group J (101-112): Rolling HWM staleness and decay metrics ---

def hwd_101_hwm_ath_age_fraction_252d(close: pd.Series) -> pd.Series:
    """Days-since-ATH as fraction of 252 trading days (1 = ATH is >=1 year old)."""
    d = _days_since_expanding_max(close)
    return _safe_div(d, pd.Series(_TD_YEAR, index=close.index, dtype=float))


def hwd_102_hwm_ath_age_fraction_504d(close: pd.Series) -> pd.Series:
    """Days-since-ATH as fraction of 504 trading days."""
    d = _days_since_expanding_max(close)
    return _safe_div(d, pd.Series(504.0, index=close.index))


def hwd_103_hwm_ath_age_fraction_1260d(close: pd.Series) -> pd.Series:
    """Days-since-ATH as fraction of 1260 trading days."""
    d = _days_since_expanding_max(close)
    return _safe_div(d, pd.Series(1260.0, index=close.index))


def hwd_104_hwm_staleness_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 252-day window."""
    d = _days_since_expanding_max(close)
    return _zscore_rolling(d, _TD_YEAR)


def hwd_105_hwm_staleness_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 1260-day window."""
    d = _days_since_expanding_max(close)
    return _zscore_rolling(d, 1260)


def hwd_106_hwm_staleness_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of days-since-ATH (vs full history)."""
    d = _days_since_expanding_max(close)
    m  = d.expanding(min_periods=5).mean()
    sd = d.expanding(min_periods=5).std()
    return _safe_div(d - m, sd)


def hwd_107_hwm_staleness_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-ATH within trailing 252-day window."""
    d = _days_since_expanding_max(close)
    return _rolling_rank_pct(d, _TD_YEAR)


def hwd_108_hwm_staleness_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-ATH within trailing 1260-day window."""
    d = _days_since_expanding_max(close)
    return _rolling_rank_pct(d, 1260)


def hwd_109_hwm_dist_x_staleness_composite(close: pd.Series) -> pd.Series:
    """Product of log-dist-from-ATH and log(days_since_ATH+1) — distress composite."""
    ld   = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    dlog = np.log1p(_days_since_expanding_max(close).fillna(0))
    return ld * dlog


def hwd_110_hwm_dist_1y_x_staleness_1y(close: pd.Series) -> pd.Series:
    """Product of 1y-HWM log-dist and log(days_since_1y_hwm+1)."""
    hwm1y = _rolling_max(close, _TD_YEAR)
    ld    = _log_safe(hwm1y) - _log_safe(close)
    dlog  = np.log1p(_days_since_rolling_max(close, _TD_YEAR).fillna(0))
    return ld * dlog


def hwd_111_hwm_avg_dist_below_ath_252d(close: pd.Series) -> pd.Series:
    """Mean log-distance from ATH over trailing 252 days (average staleness)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _rolling_mean(ld, _TD_YEAR)


def hwd_112_hwm_avg_dist_below_ath_1260d(close: pd.Series) -> pd.Series:
    """Mean log-distance from ATH over trailing 1260 days."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _rolling_mean(ld, 1260)


# --- Group K (113-124): Recovery multiple variations and cross-window ratios ---

def hwd_113_hwm_regain_multiple_log_1y(close: pd.Series) -> pd.Series:
    """Log regain multiple for 1-year HWM: log(max_252d / close)."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _log_safe(_safe_div(hwm, close))


def hwd_114_hwm_regain_multiple_log_2y(close: pd.Series) -> pd.Series:
    """Log regain multiple for 2-year HWM."""
    hwm = _rolling_max(close, 504)
    return _log_safe(_safe_div(hwm, close))


def hwd_115_hwm_regain_multiple_log_5y(close: pd.Series) -> pd.Series:
    """Log regain multiple for 5-year HWM."""
    hwm = _rolling_max(close, 1260)
    return _log_safe(_safe_div(hwm, close))


def hwd_116_hwm_regain_multiple_ath_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of ATH regain multiple over trailing 252-day window."""
    rm = _safe_div(_expanding_hwm(close), close)
    return _zscore_rolling(rm, _TD_YEAR)


def hwd_117_hwm_regain_multiple_ath_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of ATH regain multiple within trailing 252-day window."""
    rm = _safe_div(_expanding_hwm(close), close)
    return _rolling_rank_pct(rm, _TD_YEAR)


def hwd_118_hwm_regain_multiple_ath_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of ATH regain multiple (all history)."""
    rm = _safe_div(_expanding_hwm(close), close)
    return rm.expanding(min_periods=5).rank(pct=True)


def hwd_119_hwm_ratio_1y_regain_to_ath_regain(close: pd.Series) -> pd.Series:
    """Ratio of 1-year regain multiple to ATH regain multiple."""
    rm1y  = _safe_div(_rolling_max(close, _TD_YEAR), close)
    rmATH = _safe_div(_expanding_hwm(close), close)
    return _safe_div(rm1y, rmATH)


def hwd_120_hwm_ratio_2y_regain_to_ath_regain(close: pd.Series) -> pd.Series:
    """Ratio of 2-year regain multiple to ATH regain multiple."""
    rm2y  = _safe_div(_rolling_max(close, 504), close)
    rmATH = _safe_div(_expanding_hwm(close), close)
    return _safe_div(rm2y, rmATH)


def hwd_121_hwm_log_regain_ath_vol_adj_expanding(close: pd.Series) -> pd.Series:
    """Expanding volatility-adjusted log regain multiple (divides by expanding vol)."""
    lrm = _log_safe(_safe_div(_expanding_hwm(close), close))
    vol = _daily_ret(close).expanding(min_periods=5).std()
    return _safe_div(lrm, vol)


def hwd_122_hwm_double_dist_product(close: pd.Series) -> pd.Series:
    """Product of ATH log-dist and 1y log-dist (both large at deep old drawdowns)."""
    ldATH = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ld1y  = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    return ldATH * ld1y


def hwd_123_hwm_dist_spread_ath_minus_1y(close: pd.Series) -> pd.Series:
    """ATH log-dist minus 1y log-dist (how much extra distance beyond 1-year HWM)."""
    ldATH = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ld1y  = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    return ldATH - ld1y


def hwd_124_hwm_dist_spread_5y_minus_1y(close: pd.Series) -> pd.Series:
    """5y log-dist minus 1y log-dist (incremental distance from longer HWM)."""
    ld5y = _log_safe(_rolling_max(close, 1260)) - _log_safe(close)
    ld1y = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    return ld5y - ld1y


# --- Group L (125-136): Volume-conditioned HWM metrics ---

def hwd_125_hwm_vol_weighted_days_since_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of days-since-ATH over trailing 252 days."""
    d = _days_since_expanding_max(close)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return _rolling_mean(d * v_norm, _TD_YEAR)


def hwd_126_hwm_vol_at_new_ath_vs_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on new-ATH days divided by trailing 252-day average volume."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    vol_on_peak = volume * at_peak
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(_rolling_mean(vol_on_peak, _TD_YEAR), avg_vol)


def hwd_127_hwm_vol_ratio_peak_vs_trough(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day volume on new-ATH days / volume on most-distressed days ratio."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    pct = _safe_div(close - hwm, hwm)
    at_trough = (pct <= pct.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)).astype(float)
    vol_peak   = _rolling_mean(volume * at_peak,   _TD_YEAR)
    vol_trough = _rolling_mean(volume * at_trough, _TD_YEAR)
    return _safe_div(vol_peak, vol_trough)


def hwd_128_hwm_vwap_vs_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day VWAP distance from ATH: log(ATH / VWAP_252d)."""
    vwap = _safe_div(_rolling_mean(close * volume, _TD_YEAR),
                     _rolling_mean(volume, _TD_YEAR))
    hwm  = _expanding_hwm(close)
    return _log_safe(hwm) - _log_safe(vwap)


def hwd_129_hwm_vol_weighted_pct_below_ath_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 252-day mean of pct-below-ATH."""
    hwm  = _expanding_hwm(close)
    pct  = _safe_div(close - hwm, hwm)
    v_n  = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return _rolling_mean(pct * v_n, _TD_YEAR)


def hwd_130_hwm_high_vol_days_near_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume days (>2x avg) within 5% of ATH in trailing 252d."""
    hwm      = _expanding_hwm(close)
    near_ath = (close >= 0.95 * hwm).astype(float)
    high_vol = (volume > 2.0 * _rolling_mean(volume, _TD_YEAR)).astype(float)
    return _rolling_sum(near_ath * high_vol, _TD_YEAR)


def hwd_131_hwm_low_vol_days_below_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of low-volume days (<0.5x avg) more than 20% below ATH in trailing 252d."""
    hwm      = _expanding_hwm(close)
    far_ath  = (close < 0.80 * hwm).astype(float)
    low_vol  = (volume < 0.5 * _rolling_mean(volume, _TD_YEAR)).astype(float)
    return _rolling_sum(far_ath * low_vol, _TD_YEAR)


def hwd_132_hwm_avg_vol_since_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean daily volume since the expanding ATH was set vs 252d avg volume."""
    avg_all = _rolling_mean(volume, _TD_YEAR)
    d = _days_since_expanding_max(close).fillna(1).clip(lower=1)
    # Use expanding mean divided by 252d avg as a proxy for volume trend since peak
    exp_mean = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(exp_mean, avg_all)


def hwd_133_hwm_volume_spike_at_ath_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Peak daily volume in last 252 days on days close set new ATH (momentum quality)."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    vol_on_peak = volume * at_peak
    return _rolling_max(vol_on_peak, _TD_YEAR)


def hwd_134_hwm_turnover_since_ath_log(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of cumulative volume since ATH was set (proxy for post-peak trading)."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm)
    # Mark day ATH was set; cumsum volume from that point using expanding approach
    cum_vol = _rolling_sum(volume, _TD_YEAR)
    return _log_safe(cum_vol + 1)


def hwd_135_hwm_vol_trend_since_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over trailing 63 days (is volume declining post-ATH?)."""
    return _linslope(volume, _TD_QTR)


def hwd_136_hwm_dollar_vol_vs_ath_gap_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day average daily dollar volume vs ATH dollar gap (liquidity vs gap size)."""
    hwm     = _expanding_hwm(close)
    gap_usd = (hwm - close).clip(lower=_EPS)
    dv      = close * volume
    avg_dv  = _rolling_mean(dv, _TD_YEAR)
    return _safe_div(avg_dv, gap_usd)


# --- Group M (137-150): Cross-window, OLS trend, and final composites ---

def hwd_137_hwm_log_dist_ath_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of log-dist-from-ATH over trailing 21 days (short-term worsening)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _linslope(ld, _TD_MON)


def hwd_138_hwm_log_dist_ath_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of log-dist-from-ATH over trailing 63 days."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _linslope(ld, _TD_QTR)


def hwd_139_hwm_log_dist_ath_slope_252d(close: pd.Series) -> pd.Series:
    """OLS slope of log-dist-from-ATH over trailing 252 days."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _linslope(ld, _TD_YEAR)


def hwd_140_hwm_pct_below_1y_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of pct-below-1y-HWM over trailing 63 days."""
    pct = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _linslope(pct, _TD_QTR)


def hwd_141_hwm_days_since_ath_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of days-since-ATH over trailing 63 days (time accumulation rate)."""
    d = _days_since_expanding_max(close)
    return _linslope(d, _TD_QTR)


def hwd_142_hwm_regain_multiple_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of ATH regain multiple over trailing 63 days."""
    rm = _safe_div(_expanding_hwm(close), close)
    return _linslope(rm, _TD_QTR)


def hwd_143_hwm_regain_multiple_pct_chg_63d(close: pd.Series) -> pd.Series:
    """63-day pct-change in ATH regain multiple."""
    rm = _safe_div(_expanding_hwm(close), close)
    return _safe_div(rm - rm.shift(_TD_QTR), rm.shift(_TD_QTR).abs().replace(0, np.nan))


def hwd_144_hwm_log_dist_ath_ewm21(close: pd.Series) -> pd.Series:
    """21-day EMA of log-distance from ATH (smoothed trend in distress)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _ewm_mean(ld, _TD_MON)


def hwd_145_hwm_log_dist_ath_ewm63(close: pd.Series) -> pd.Series:
    """63-day EMA of log-distance from ATH."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _ewm_mean(ld, _TD_QTR)


def hwd_146_hwm_log_dist_ath_ewm252(close: pd.Series) -> pd.Series:
    """252-day EMA of log-distance from ATH."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _ewm_mean(ld, _TD_YEAR)


def hwd_147_hwm_log_dist_spread_ewm21_ewm63(close: pd.Series) -> pd.Series:
    """EWM-21 minus EWM-63 of log-dist from ATH (short- vs medium-term signal)."""
    ld = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    return _ewm_mean(ld, _TD_MON) - _ewm_mean(ld, _TD_QTR)


def hwd_148_hwm_close_vs_ath_percentile_history(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of pct-below-ATH in full history (how extreme)."""
    pct = _safe_div(close - _expanding_hwm(close), _expanding_hwm(close))
    return pct.expanding(min_periods=5).rank(pct=True)


def hwd_149_hwm_composite_distress_index(close: pd.Series) -> pd.Series:
    """Composite HWM distress: 0.35*log_dist_ATH + 0.25*log_dist_1y + 0.25*days_since_ATH_log + 0.15*log_regain."""
    ld_ath   = _log_safe(_expanding_hwm(close)) - _log_safe(close)
    ld_1y    = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(close)
    d_log    = np.log1p(_days_since_expanding_max(close).fillna(0))
    lr       = _log_safe(_safe_div(_expanding_hwm(close), close))
    d_zs     = _zscore_rolling(d_log, _TD_YEAR)
    ld_zs    = _zscore_rolling(ld_ath, _TD_YEAR)
    ld1y_zs  = _zscore_rolling(ld_1y, _TD_YEAR)
    lr_zs    = _zscore_rolling(lr, _TD_YEAR)
    return 0.35 * ld_zs + 0.25 * ld1y_zs + 0.25 * d_zs + 0.15 * lr_zs


def hwd_150_hwm_peak_age_vs_history_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of time_ratio_peak_to_history (all history)."""
    d     = _days_since_expanding_max(close)
    total = pd.Series(np.arange(1, len(close) + 1), index=close.index, dtype=float)
    ratio = _safe_div(d, total)
    return ratio.expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

HIGH_WATER_DISTANCE_REGISTRY_076_150 = {
    "hwd_076_hwm_open_pct_below_ath":              {"inputs": ["close", "open"],              "func": hwd_076_hwm_open_pct_below_ath},
    "hwd_077_hwm_low_pct_below_ath":               {"inputs": ["close", "low"],               "func": hwd_077_hwm_low_pct_below_ath},
    "hwd_078_hwm_high_pct_below_ath":              {"inputs": ["close", "high"],              "func": hwd_078_hwm_high_pct_below_ath},
    "hwd_079_hwm_intraday_ath_pct_below":          {"inputs": ["high"],                       "func": hwd_079_hwm_intraday_ath_pct_below},
    "hwd_080_hwm_low_log_dist_ath":                {"inputs": ["close", "low"],               "func": hwd_080_hwm_low_log_dist_ath},
    "hwd_081_hwm_open_log_dist_ath":               {"inputs": ["close", "open"],              "func": hwd_081_hwm_open_log_dist_ath},
    "hwd_082_hwm_low_vs_intraday_ath":             {"inputs": ["high", "low"],                "func": hwd_082_hwm_low_vs_intraday_ath},
    "hwd_083_hwm_range_pct_ath":                   {"inputs": ["close", "high", "low"],       "func": hwd_083_hwm_range_pct_ath},
    "hwd_084_hwm_close_in_day_range_vs_ath":       {"inputs": ["close", "high", "low"],       "func": hwd_084_hwm_close_in_day_range_vs_ath},
    "hwd_085_hwm_open_vs_1y_hwm":                  {"inputs": ["close", "open"],              "func": hwd_085_hwm_open_vs_1y_hwm},
    "hwd_086_hwm_low_vs_1y_hwm":                   {"inputs": ["close", "low"],               "func": hwd_086_hwm_low_vs_1y_hwm},
    "hwd_087_hwm_high_vs_1y_hwm":                  {"inputs": ["close", "high"],              "func": hwd_087_hwm_high_vs_1y_hwm},
    "hwd_088_hwm_intraday_range_vs_ath_gap":       {"inputs": ["close", "high", "low"],       "func": hwd_088_hwm_intraday_range_vs_ath_gap},
    "hwd_089_hwm_days_since_ath_5d_chg":           {"inputs": ["close"],                      "func": hwd_089_hwm_days_since_ath_5d_chg},
    "hwd_090_hwm_days_since_ath_21d_chg":          {"inputs": ["close"],                      "func": hwd_090_hwm_days_since_ath_21d_chg},
    "hwd_091_hwm_days_since_ath_63d_chg":          {"inputs": ["close"],                      "func": hwd_091_hwm_days_since_ath_63d_chg},
    "hwd_092_hwm_days_since_1y_hwm_5d_chg":        {"inputs": ["close"],                      "func": hwd_092_hwm_days_since_1y_hwm_5d_chg},
    "hwd_093_hwm_time_accel_ath":                  {"inputs": ["close"],                      "func": hwd_093_hwm_time_accel_ath},
    "hwd_094_hwm_log_dist_rate_5d":                {"inputs": ["close"],                      "func": hwd_094_hwm_log_dist_rate_5d},
    "hwd_095_hwm_log_dist_rate_21d":               {"inputs": ["close"],                      "func": hwd_095_hwm_log_dist_rate_21d},
    "hwd_096_hwm_pct_below_ath_5d_chg":            {"inputs": ["close"],                      "func": hwd_096_hwm_pct_below_ath_5d_chg},
    "hwd_097_hwm_pct_below_ath_21d_chg":           {"inputs": ["close"],                      "func": hwd_097_hwm_pct_below_ath_21d_chg},
    "hwd_098_hwm_pct_below_1y_5d_chg":             {"inputs": ["close"],                      "func": hwd_098_hwm_pct_below_1y_5d_chg},
    "hwd_099_hwm_regain_multiple_5d_chg":          {"inputs": ["close"],                      "func": hwd_099_hwm_regain_multiple_5d_chg},
    "hwd_100_hwm_regain_multiple_21d_chg":         {"inputs": ["close"],                      "func": hwd_100_hwm_regain_multiple_21d_chg},
    "hwd_101_hwm_ath_age_fraction_252d":           {"inputs": ["close"],                      "func": hwd_101_hwm_ath_age_fraction_252d},
    "hwd_102_hwm_ath_age_fraction_504d":           {"inputs": ["close"],                      "func": hwd_102_hwm_ath_age_fraction_504d},
    "hwd_103_hwm_ath_age_fraction_1260d":          {"inputs": ["close"],                      "func": hwd_103_hwm_ath_age_fraction_1260d},
    "hwd_104_hwm_staleness_zscore_252d":           {"inputs": ["close"],                      "func": hwd_104_hwm_staleness_zscore_252d},
    "hwd_105_hwm_staleness_zscore_1260d":          {"inputs": ["close"],                      "func": hwd_105_hwm_staleness_zscore_1260d},
    "hwd_106_hwm_staleness_expanding_zscore":      {"inputs": ["close"],                      "func": hwd_106_hwm_staleness_expanding_zscore},
    "hwd_107_hwm_staleness_pct_rank_252d":         {"inputs": ["close"],                      "func": hwd_107_hwm_staleness_pct_rank_252d},
    "hwd_108_hwm_staleness_pct_rank_1260d":        {"inputs": ["close"],                      "func": hwd_108_hwm_staleness_pct_rank_1260d},
    "hwd_109_hwm_dist_x_staleness_composite":      {"inputs": ["close"],                      "func": hwd_109_hwm_dist_x_staleness_composite},
    "hwd_110_hwm_dist_1y_x_staleness_1y":          {"inputs": ["close"],                      "func": hwd_110_hwm_dist_1y_x_staleness_1y},
    "hwd_111_hwm_avg_dist_below_ath_252d":         {"inputs": ["close"],                      "func": hwd_111_hwm_avg_dist_below_ath_252d},
    "hwd_112_hwm_avg_dist_below_ath_1260d":        {"inputs": ["close"],                      "func": hwd_112_hwm_avg_dist_below_ath_1260d},
    "hwd_113_hwm_regain_multiple_log_1y":          {"inputs": ["close"],                      "func": hwd_113_hwm_regain_multiple_log_1y},
    "hwd_114_hwm_regain_multiple_log_2y":          {"inputs": ["close"],                      "func": hwd_114_hwm_regain_multiple_log_2y},
    "hwd_115_hwm_regain_multiple_log_5y":          {"inputs": ["close"],                      "func": hwd_115_hwm_regain_multiple_log_5y},
    "hwd_116_hwm_regain_multiple_ath_zscore_252d": {"inputs": ["close"],                      "func": hwd_116_hwm_regain_multiple_ath_zscore_252d},
    "hwd_117_hwm_regain_multiple_ath_pct_rank_252d":{"inputs": ["close"],                     "func": hwd_117_hwm_regain_multiple_ath_pct_rank_252d},
    "hwd_118_hwm_regain_multiple_ath_expanding_pct_rank":{"inputs": ["close"],                "func": hwd_118_hwm_regain_multiple_ath_expanding_pct_rank},
    "hwd_119_hwm_ratio_1y_regain_to_ath_regain":   {"inputs": ["close"],                      "func": hwd_119_hwm_ratio_1y_regain_to_ath_regain},
    "hwd_120_hwm_ratio_2y_regain_to_ath_regain":   {"inputs": ["close"],                      "func": hwd_120_hwm_ratio_2y_regain_to_ath_regain},
    "hwd_121_hwm_log_regain_ath_vol_adj_expanding": {"inputs": ["close"],                     "func": hwd_121_hwm_log_regain_ath_vol_adj_expanding},
    "hwd_122_hwm_double_dist_product":             {"inputs": ["close"],                      "func": hwd_122_hwm_double_dist_product},
    "hwd_123_hwm_dist_spread_ath_minus_1y":        {"inputs": ["close"],                      "func": hwd_123_hwm_dist_spread_ath_minus_1y},
    "hwd_124_hwm_dist_spread_5y_minus_1y":         {"inputs": ["close"],                      "func": hwd_124_hwm_dist_spread_5y_minus_1y},
    "hwd_125_hwm_vol_weighted_days_since_ath":     {"inputs": ["close", "volume"],            "func": hwd_125_hwm_vol_weighted_days_since_ath},
    "hwd_126_hwm_vol_at_new_ath_vs_avg":           {"inputs": ["close", "volume"],            "func": hwd_126_hwm_vol_at_new_ath_vs_avg},
    "hwd_127_hwm_vol_ratio_peak_vs_trough":        {"inputs": ["close", "volume"],            "func": hwd_127_hwm_vol_ratio_peak_vs_trough},
    "hwd_128_hwm_vwap_vs_ath":                     {"inputs": ["close", "volume"],            "func": hwd_128_hwm_vwap_vs_ath},
    "hwd_129_hwm_vol_weighted_pct_below_ath_252d": {"inputs": ["close", "volume"],            "func": hwd_129_hwm_vol_weighted_pct_below_ath_252d},
    "hwd_130_hwm_high_vol_days_near_ath":          {"inputs": ["close", "volume"],            "func": hwd_130_hwm_high_vol_days_near_ath},
    "hwd_131_hwm_low_vol_days_below_ath":          {"inputs": ["close", "volume"],            "func": hwd_131_hwm_low_vol_days_below_ath},
    "hwd_132_hwm_avg_vol_since_ath":               {"inputs": ["close", "volume"],            "func": hwd_132_hwm_avg_vol_since_ath},
    "hwd_133_hwm_volume_spike_at_ath_252d":        {"inputs": ["close", "volume"],            "func": hwd_133_hwm_volume_spike_at_ath_252d},
    "hwd_134_hwm_turnover_since_ath_log":          {"inputs": ["close", "volume"],            "func": hwd_134_hwm_turnover_since_ath_log},
    "hwd_135_hwm_vol_trend_since_ath":             {"inputs": ["close", "volume"],            "func": hwd_135_hwm_vol_trend_since_ath},
    "hwd_136_hwm_dollar_vol_vs_ath_gap_ratio":     {"inputs": ["close", "volume"],            "func": hwd_136_hwm_dollar_vol_vs_ath_gap_ratio},
    "hwd_137_hwm_log_dist_ath_slope_21d":          {"inputs": ["close"],                      "func": hwd_137_hwm_log_dist_ath_slope_21d},
    "hwd_138_hwm_log_dist_ath_slope_63d":          {"inputs": ["close"],                      "func": hwd_138_hwm_log_dist_ath_slope_63d},
    "hwd_139_hwm_log_dist_ath_slope_252d":         {"inputs": ["close"],                      "func": hwd_139_hwm_log_dist_ath_slope_252d},
    "hwd_140_hwm_pct_below_1y_slope_63d":          {"inputs": ["close"],                      "func": hwd_140_hwm_pct_below_1y_slope_63d},
    "hwd_141_hwm_days_since_ath_slope_63d":        {"inputs": ["close"],                      "func": hwd_141_hwm_days_since_ath_slope_63d},
    "hwd_142_hwm_regain_multiple_slope_63d":       {"inputs": ["close"],                      "func": hwd_142_hwm_regain_multiple_slope_63d},
    "hwd_143_hwm_regain_multiple_pct_chg_63d":     {"inputs": ["close"],                      "func": hwd_143_hwm_regain_multiple_pct_chg_63d},
    "hwd_144_hwm_log_dist_ath_ewm21":              {"inputs": ["close"],                      "func": hwd_144_hwm_log_dist_ath_ewm21},
    "hwd_145_hwm_log_dist_ath_ewm63":              {"inputs": ["close"],                      "func": hwd_145_hwm_log_dist_ath_ewm63},
    "hwd_146_hwm_log_dist_ath_ewm252":             {"inputs": ["close"],                      "func": hwd_146_hwm_log_dist_ath_ewm252},
    "hwd_147_hwm_log_dist_spread_ewm21_ewm63":     {"inputs": ["close"],                      "func": hwd_147_hwm_log_dist_spread_ewm21_ewm63},
    "hwd_148_hwm_close_vs_ath_percentile_history": {"inputs": ["close"],                      "func": hwd_148_hwm_close_vs_ath_percentile_history},
    "hwd_149_hwm_composite_distress_index":        {"inputs": ["close"],                      "func": hwd_149_hwm_composite_distress_index},
    "hwd_150_hwm_peak_age_vs_history_pct_rank":    {"inputs": ["close"],                      "func": hwd_150_hwm_peak_age_vs_history_pct_rank},
}
