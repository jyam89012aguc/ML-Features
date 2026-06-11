"""
102_seasonal_distress — Base Features 076-150
Domain: calendar / seasonal context of distress (extended encodings, tax-loss
        interactions, calendar position of multi-year lows, seasonal composites).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
        Calendar attributes are derived from the close Series' DatetimeIndex.
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Calendar helpers (DatetimeIndex of the input Series) ─────────────────────
# CONTRACT: every input Series is daily with a DatetimeIndex aligned to the
# trading-day close index; all calendar attributes are knowable at time t.

def _dtidx(s: pd.Series) -> pd.DatetimeIndex:
    idx = s.index
    if not isinstance(idx, pd.DatetimeIndex):
        idx = pd.DatetimeIndex(pd.to_datetime(idx, errors="coerce"))
    return idx


def _ser(values, s: pd.Series) -> pd.Series:
    return pd.Series(np.asarray(values, dtype=float), index=s.index)


def _days_to_year_end(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    ye = pd.PeriodIndex(idx, freq="Y").end_time.normalize()
    return _ser((ye - idx).days, s)


def _days_from_year_start(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    ys = pd.PeriodIndex(idx, freq="Y").start_time.normalize()
    return _ser((idx - ys).days, s)


def _days_to_quarter_end(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    qe = pd.PeriodIndex(idx, freq="Q").end_time.normalize()
    return _ser((qe - idx).days, s)


def _tax_loss_intensity(s: pd.Series) -> pd.Series:
    m = _dtidx(s).month
    in_window = np.isin(m, [10, 11, 12])
    ramp = (1.0 - _days_to_year_end(s) / 92.0).clip(lower=0, upper=1)
    return ramp * _ser(in_window.astype(float), s)


def _tax_loss_window(s: pd.Series) -> pd.Series:
    return _ser(np.isin(_dtidx(s).month, [11, 12]).astype(float), s)


def _q4_flag(s: pd.Series) -> pd.Series:
    return _ser((_dtidx(s).quarter == 4).astype(float), s)


def _attr_at_rolling_min(ref: pd.Series, attr: np.ndarray, w: int) -> pd.Series:
    """Value of `attr` at the position of the rolling minimum of `ref`."""
    n = len(ref)
    off = ref.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)
    pos = np.arange(n, dtype=float) - off.values
    valid = ~np.isnan(pos)
    pos_i = np.where(valid, pos, 0).astype(int)
    out = np.asarray(attr, dtype=float)[pos_i]
    out[~valid] = np.nan
    return pd.Series(out, index=ref.index)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group A (076-090): Finer calendar encodings ---

def szd_076_days_to_quarter_end_norm(close: pd.Series) -> pd.Series:
    """Days to quarter end normalized to roughly [0, 1]."""
    return _days_to_quarter_end(close) / 92.0


def szd_077_days_to_year_end_norm(close: pd.Series) -> pd.Series:
    """Days to year end normalized to roughly [0, 1]."""
    return _days_to_year_end(close) / 365.0


def szd_078_year_progress_sin(close: pd.Series) -> pd.Series:
    """Sine of the fractional year position (smooth annual cycle)."""
    frac = _days_from_year_start(close) / 365.0
    return _ser(np.sin(2 * np.pi * frac.values), close)


def szd_079_year_progress_cos(close: pd.Series) -> pd.Series:
    """Cosine of the fractional year position (smooth annual cycle)."""
    frac = _days_from_year_start(close) / 365.0
    return _ser(np.cos(2 * np.pi * frac.values), close)


def szd_080_first_days_of_month_flag(close: pd.Series) -> pd.Series:
    """Flag: within the first 2 calendar days of a month."""
    return _ser((_dtidx(close).day <= 2).astype(float), close)


def szd_081_last_days_of_month_flag(close: pd.Series) -> pd.Series:
    """Flag: within the last few calendar days of a month (day >= 27)."""
    return _ser((_dtidx(close).day >= 27).astype(float), close)


def szd_082_first_half_of_month_flag(close: pd.Series) -> pd.Series:
    """Flag: in the first half of the calendar month (day <= 15)."""
    return _ser((_dtidx(close).day <= 15).astype(float), close)


def szd_083_year_end_quarter_flag(close: pd.Series) -> pd.Series:
    """Flag: in the fourth quarter (common fiscal-year-end window)."""
    return _q4_flag(close)


def szd_084_weeks_to_year_end(close: pd.Series) -> pd.Series:
    """Whole calendar weeks remaining until December 31."""
    return (_days_to_year_end(close) / 7.0).round()


def szd_085_months_to_year_end(close: pd.Series) -> pd.Series:
    """Whole months remaining until December (12 minus current month)."""
    return _ser(12 - _dtidx(close).month, close)


def szd_086_september_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in September (historically the weakest month)."""
    return _ser((_dtidx(close).month == 9).astype(float), close)


def szd_087_weak_season_flag(close: pd.Series) -> pd.Series:
    """Flag: in the seasonally-weak September-October window."""
    return _ser(np.isin(_dtidx(close).month, [9, 10]).astype(float), close)


def szd_088_strong_season_flag(close: pd.Series) -> pd.Series:
    """Flag: in the seasonally-strong November-April window."""
    return _ser(np.isin(_dtidx(close).month, [11, 12, 1, 2, 3, 4]).astype(float), close)


def szd_089_day_of_week_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of the day-of-week (cyclical week position)."""
    return _ser(np.sin(2 * np.pi * _dtidx(close).dayofweek / 5.0), close)


def szd_090_day_of_week_cos(close: pd.Series) -> pd.Series:
    """Cosine encoding of the day-of-week (cyclical week position)."""
    return _ser(np.cos(2 * np.pi * _dtidx(close).dayofweek / 5.0), close)


# --- Group B (091-105): Extended tax-loss interactions ---

def szd_091_dd_504d_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """504-day drawdown gated to the Nov-Dec tax-loss window."""
    dd = _safe_div(close - _rolling_max(close, 504), _rolling_max(close, 504))
    return dd * _tax_loss_window(close)


def szd_092_dd_126d_in_q4(close: pd.Series) -> pd.Series:
    """126-day drawdown gated to the fourth quarter."""
    dd = _safe_div(close - _rolling_max(close, _TD_HALF), _rolling_max(close, _TD_HALF))
    return dd * _q4_flag(close)


def szd_093_loss_magnitude_in_december(close: pd.Series) -> pd.Series:
    """Trailing 252-day loss magnitude gated to December."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return loss * dec


def szd_094_loser_in_q4_score(close: pd.Series) -> pd.Series:
    """Trailing 126-day loss magnitude gated to the fourth quarter."""
    loss = (-close.pct_change(_TD_HALF)).clip(lower=0)
    return loss * _q4_flag(close)


def szd_095_underwater_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """252-day underwater fraction gated by tax-loss-window intensity."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    uw = _rolling_mean((dd < 0).astype(float), _TD_YEAR)
    return uw * _tax_loss_intensity(close)


def szd_096_new_low_in_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: a new 252-day low is being set during the Nov-Dec window."""
    new_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return new_low * _tax_loss_window(close)


def szd_097_new_low_in_december_flag(close: pd.Series) -> pd.Series:
    """Flag: a new 252-day low is being set in December."""
    new_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return new_low * dec


def szd_098_days_since_low_x_tax_loss_window(close: pd.Series) -> pd.Series:
    """Recency of the 252-day low gated to the tax-loss window."""
    age = close.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)
    recency = (1.0 - age / _TD_YEAR).clip(lower=0)
    return recency * _tax_loss_window(close)


def szd_099_deep_loss_into_year_end(close: pd.Series) -> pd.Series:
    """Flag: trailing-year loss worse than -40% during December."""
    deep = (close.pct_change(_TD_YEAR) < -0.40).astype(float)
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return deep * dec


def szd_100_santa_window_drawdown(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the last 5 / first 2 days of the year."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    last = _days_to_year_end(close) <= 5
    first = _days_from_year_start(close) <= 2
    return dd * (last | first).astype(float)


def szd_101_tax_loss_pressure_ramp(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Loss magnitude times tax-loss intensity times relative volume."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    vol_ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR)).clip(upper=5)
    return loss * _tax_loss_intensity(close) * vol_ratio


def szd_102_january_recovery_setup(close: pd.Series) -> pd.Series:
    """Prior-year loss magnitude carried into January (rebound setup)."""
    jan = _ser((_dtidx(close).month == 1).astype(float), close)
    prior_loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return prior_loss * jan


def szd_103_q4_decline_streak(close: pd.Series) -> pd.Series:
    """Consecutive down-day streak gated to the fourth quarter."""
    f = (_daily_ret(close) < 0).astype(float)
    streak = f.groupby((f == 0).cumsum()).cumsum()
    return streak * _q4_flag(close)


def szd_104_tax_loss_window_volatility(close: pd.Series) -> pd.Series:
    """21-day realized volatility gated by tax-loss-window intensity."""
    vol = _rolling_std(_daily_ret(close), _TD_MON)
    return vol * _tax_loss_intensity(close)


def szd_105_seasonal_capitulation_flag(close: pd.Series) -> pd.Series:
    """Flag: a new 252-day low coincides with the Nov-Dec tax-loss window."""
    new_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    return new_low * _tax_loss_window(close)


# --- Group C (106-120): Calendar position of the low (extended) ---

def szd_106_doy_of_63d_low(close: pd.Series) -> pd.Series:
    """Day-of-year on which the trailing 63-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).dayofyear.to_numpy(), _TD_QTR)


def szd_107_doy_of_504d_low(close: pd.Series) -> pd.Series:
    """Day-of-year on which the trailing 504-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).dayofyear.to_numpy(), 504)


def szd_108_quarter_of_252d_low(close: pd.Series) -> pd.Series:
    """Calendar quarter in which the trailing 252-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).quarter.to_numpy(), _TD_YEAR)


def szd_109_low_252d_in_january_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in January."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    return (m == 1).astype(float)


def szd_110_low_252d_in_weak_season_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in September or October."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    return m.isin([9, 10]).astype(float)


def szd_111_week_of_252d_low(close: pd.Series) -> pd.Series:
    """ISO week-of-year on which the trailing 252-day low was set."""
    woy = _dtidx(close).isocalendar().week.to_numpy()
    return _attr_at_rolling_min(close, woy, _TD_YEAR)


def szd_112_month_of_1260d_low(close: pd.Series) -> pd.Series:
    """Calendar month in which the trailing 1260-day (5y) low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), 1260)


def szd_113_low_1260d_in_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 1260-day low was set during the Nov-Dec window."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), 1260)
    return m.isin([11, 12]).astype(float)


def szd_114_days_from_252d_low_to_year_end(close: pd.Series) -> pd.Series:
    """Calendar days between the 252-day low's day-of-year and year end."""
    doy = _attr_at_rolling_min(close, _dtidx(close).dayofyear.to_numpy(), _TD_YEAR)
    return (365.0 - doy).clip(lower=0)


def szd_115_low_clustered_in_q4_flag(close: pd.Series) -> pd.Series:
    """Flag: most trailing-252d new 21-day lows occurred in the fourth quarter."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    q4 = _q4_flag(close)
    total = _rolling_sum(new_low, _TD_YEAR)
    in_q4 = _rolling_sum(new_low * q4, _TD_YEAR)
    return (_safe_div(in_q4, total) > 0.5).astype(float)


def szd_116_seasonal_low_concentration(close: pd.Series) -> pd.Series:
    """Herfindahl concentration of new-low months over the trailing 252 days."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    month = _ser(_dtidx(close).month, close)
    total = _rolling_sum(new_low, _TD_YEAR)
    hhi = pd.Series(0.0, index=close.index)
    for mth in range(1, 13):
        cnt = _rolling_sum(new_low * (month == mth).astype(float), _TD_YEAR)
        hhi = hhi + _safe_div(cnt, total) ** 2
    return hhi


def szd_117_low_month_recurrence(close: pd.Series) -> pd.Series:
    """Share of trailing-504d new 21-day lows landing in the 252d-low's month."""
    low_month = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    month = _ser(_dtidx(close).month, close)
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    same = (month == low_month).astype(float)
    return _safe_div(_rolling_sum(new_low * same, 504), _rolling_sum(new_low, 504))


def szd_118_low_month_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of the month in which the 252-day low was set."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    return np.sin(2 * np.pi * m / 12.0)


def szd_119_low_month_cos(close: pd.Series) -> pd.Series:
    """Cosine encoding of the month in which the 252-day low was set."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    return np.cos(2 * np.pi * m / 12.0)


def szd_120_low_in_seasonally_weak_period_flag(close: pd.Series) -> pd.Series:
    """Flag: the 252-day low was set in the May-October weak half-year."""
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)
    return m.isin([5, 6, 7, 8, 9, 10]).astype(float)


# --- Group D (121-135): Seasonal volume / return patterns (extended) ---

def szd_121_q4_down_volume_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day volume vs 252-day median, gated to the fourth quarter."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    return _safe_div(dv, _rolling_median(volume, _TD_YEAR)) * _q4_flag(close)


def szd_122_december_realized_vol_ratio(close: pd.Series) -> pd.Series:
    """21-day vs 252-day realized-vol ratio gated to December."""
    vr = _safe_div(_rolling_std(_daily_ret(close), _TD_MON),
                   _rolling_std(_daily_ret(close), _TD_YEAR))
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return vr * dec


def szd_123_january_realized_vol_ratio(close: pd.Series) -> pd.Series:
    """21-day vs 252-day realized-vol ratio gated to January."""
    vr = _safe_div(_rolling_std(_daily_ret(close), _TD_MON),
                   _rolling_std(_daily_ret(close), _TD_YEAR))
    jan = _ser((_dtidx(close).month == 1).astype(float), close)
    return vr * jan


def szd_124_turn_of_month_volume_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume vs 63-day median gated to the turn-of-month window."""
    d = _dtidx(close).day
    tom = _ser(((d <= 3) | (d >= 26)).astype(float), close)
    return _safe_div(volume, _rolling_median(volume, _TD_QTR)) * tom


def szd_125_monday_return_mean_63d(close: pd.Series) -> pd.Series:
    """Mean Monday daily return over the trailing 63 days."""
    ret = _daily_ret(close)
    mon = _ser((_dtidx(close).dayofweek == 0), close).astype(bool)
    return ret.where(mon).rolling(_TD_QTR, min_periods=3).mean()


def szd_126_friday_return_mean_63d(close: pd.Series) -> pd.Series:
    """Mean Friday daily return over the trailing 63 days."""
    ret = _daily_ret(close)
    fri = _ser((_dtidx(close).dayofweek == 4), close).astype(bool)
    return ret.where(fri).rolling(_TD_QTR, min_periods=3).mean()


def szd_127_q4_mean_return_252d(close: pd.Series) -> pd.Series:
    """Mean daily return on Q4 days over the trailing 252 days."""
    ret = _daily_ret(close)
    return ret.where(_q4_flag(close).astype(bool)).rolling(_TD_YEAR, min_periods=_TD_MON).mean()


def szd_128_seasonal_return_spread(close: pd.Series) -> pd.Series:
    """Mean Q4-day return minus mean Q1-day return over trailing 252 days."""
    ret = _daily_ret(close)
    q4 = _q4_flag(close).astype(bool)
    q1 = _ser((_dtidx(close).quarter == 1), close).astype(bool)
    q4m = ret.where(q4).rolling(_TD_YEAR, min_periods=_TD_MON).mean()
    q1m = ret.where(q1).rolling(_TD_YEAR, min_periods=_TD_MON).mean()
    return q4m - q1m


def szd_129_down_streak_in_december(close: pd.Series) -> pd.Series:
    """Consecutive down-day streak gated to December."""
    f = (_daily_ret(close) < 0).astype(float)
    streak = f.groupby((f == 0).cumsum()).cumsum()
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return streak * dec


def szd_130_volume_seasonality_index(volume: pd.Series) -> pd.Series:
    """Current-month mean volume vs trailing 252-day mean volume."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def szd_131_q4_volume_trend(volume: pd.Series) -> pd.Series:
    """63-day vs 252-day mean-volume ratio gated to the fourth quarter."""
    vt = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return vt * _q4_flag(volume)


def szd_132_month_end_return(close: pd.Series) -> pd.Series:
    """Trailing 3-day return gated to the last days of the month (day >= 27)."""
    me = _ser((_dtidx(close).day >= 27).astype(float), close)
    return close.pct_change(3) * me


def szd_133_holiday_week_volume(volume: pd.Series) -> pd.Series:
    """Volume vs 63-day median during the final calendar week of the year."""
    last_week = _days_to_year_end(volume) <= 7
    return _safe_div(volume, _rolling_median(volume, _TD_QTR)) * last_week.astype(float)


def szd_134_january_volume_spike(volume: pd.Series) -> pd.Series:
    """Volume vs 63-day median gated to the first half of January."""
    idx = _dtidx(volume)
    jan = _ser(((idx.month == 1) & (idx.day <= 15)).astype(float), volume)
    return _safe_div(volume, _rolling_median(volume, _TD_QTR)) * jan


def szd_135_december_volume_share(volume: pd.Series) -> pd.Series:
    """December mean volume relative to the trailing-252d mean (seasonality)."""
    dec = _ser((_dtidx(volume).month == 12), volume).astype(bool)
    dec_mean = volume.where(dec).rolling(_TD_YEAR, min_periods=_TD_MON).mean()
    return _safe_div(dec_mean, _rolling_mean(volume, _TD_YEAR))


# --- Group E (136-150): Composites & multi-year seasonal ---

def szd_136_multi_year_low_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """Flag: a new 504-day low is being set during the Nov-Dec window."""
    new_low = (close <= _rolling_min(close, 504)).astype(float)
    return new_low * _tax_loss_window(close)


def szd_137_seasonal_distress_intensity(close: pd.Series) -> pd.Series:
    """126-day drawdown depth scaled by tax-loss-window intensity."""
    dd = _safe_div(_rolling_max(close, _TD_HALF) - close, _rolling_max(close, _TD_HALF))
    return dd * _tax_loss_intensity(close)


def szd_138_tax_loss_harvest_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Loser magnitude, tax-loss intensity and elevated volume combined."""
    loss = (-close.pct_change(_TD_HALF)).clip(lower=0)
    vol_ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR)).clip(upper=4) / 4.0
    return loss * _tax_loss_intensity(close) * (1.0 + vol_ratio)


def szd_139_q4_capitulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Q4-gated composite: drawdown depth and elevated down-day volume."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return dd * (1.0 + vr) * _q4_flag(close)


def szd_140_year_end_low_proximity_score(close: pd.Series) -> pd.Series:
    """Closeness to the 252-day low scaled by turn-of-year proximity."""
    prox_low = _safe_div(_rolling_min(close, _TD_YEAR), close)
    dte = _days_to_year_end(close)
    dys = _days_from_year_start(close)
    nearest = pd.concat([dte, dys], axis=1).min(axis=1)
    toy = (1.0 - nearest / 30.0).clip(lower=0)
    return prox_low * toy


def szd_141_january_effect_loser_score(close: pd.Series) -> pd.Series:
    """Prior-year loss magnitude gated to the early-January effect window."""
    idx = _dtidx(close)
    jan = _ser(((idx.month == 1) & (idx.day <= 14)).astype(float), close)
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return loss * jan


def szd_142_seasonal_low_alignment_504d(close: pd.Series) -> pd.Series:
    """Recent 504-day low set in the tax-loss window (alignment score)."""
    age = close.rolling(504, min_periods=_TD_QTR).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)
    recency = (1.0 - age / _TD_QTR).clip(lower=0)
    m = _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), 504)
    return recency * m.isin([11, 12]).astype(float)


def szd_143_calendar_distress_composite(close: pd.Series) -> pd.Series:
    """Drawdown depth, Q4 gating and turn-of-year proximity combined."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dte = _days_to_year_end(close)
    toy = (1.0 - dte / 60.0).clip(lower=0)
    return dd * _q4_flag(close) * (1.0 + toy)


def szd_144_tax_loss_window_drawdown_zscore(close: pd.Series) -> pd.Series:
    """Z-score of the 252-day drawdown gated to the tax-loss window."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    z = _safe_div(dd - _rolling_mean(dd, _TD_YEAR), _rolling_std(dd, _TD_YEAR))
    return z * _tax_loss_window(close)


def szd_145_seasonal_volume_distress(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day volume z-score gated by tax-loss-window intensity."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    z = _safe_div(dv - _rolling_mean(dv, _TD_YEAR), _rolling_std(dv, _TD_YEAR))
    return z * _tax_loss_intensity(close)


def szd_146_turn_of_year_capitulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """New-low flag, turn-of-year proximity and volume spike combined."""
    new_low = (close <= _rolling_min(close, _TD_YEAR) * 1.02).astype(float)
    dte = _days_to_year_end(close)
    toy = (1.0 - dte / 30.0).clip(lower=0)
    vr = _safe_div(volume, _rolling_median(volume, _TD_QTR)).clip(upper=5) / 5.0
    return new_low * toy * (1.0 + vr)


def szd_147_december_low_with_volume_spike(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: new 63-day low in December on above-median volume."""
    new_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    hi_vol = (volume > _rolling_median(volume, _TD_QTR)).astype(float)
    return new_low * dec * hi_vol


def szd_148_seasonal_phase_score(close: pd.Series) -> pd.Series:
    """Phase score: weak-season membership plus drawdown depth gating."""
    m = _dtidx(close).month
    weak = _ser(np.isin(m, [9, 10, 11, 12]).astype(float), close)
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    return weak * (0.5 + dd)


def szd_149_annual_low_season_flag(close: pd.Series) -> pd.Series:
    """Flag: current month historically hosts the trailing new-21d-low cluster."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    month = _ser(_dtidx(close).month, close)
    cur_month_lows = pd.Series(0.0, index=close.index)
    for mth in range(1, 13):
        cnt = _rolling_sum(new_low * (month == mth).astype(float), 504)
        cur_month_lows = cur_month_lows.where(month != mth, cnt)
    avg = _rolling_sum(new_low, 504) / 12.0
    return (cur_month_lows > avg).astype(float)


def szd_150_master_seasonal_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master index: drawdown, tax-loss intensity, year-end proximity, volume."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    intensity = _tax_loss_intensity(close)
    dte = _days_to_year_end(close)
    toy = (1.0 - dte / 45.0).clip(lower=0)
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return (dd * (1.0 + intensity + toy) * (1.0 + vr)) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

SEASONAL_DISTRESS_REGISTRY_076_150 = {
    "szd_076_days_to_quarter_end_norm": {"inputs": ["close"], "func": szd_076_days_to_quarter_end_norm},
    "szd_077_days_to_year_end_norm": {"inputs": ["close"], "func": szd_077_days_to_year_end_norm},
    "szd_078_year_progress_sin": {"inputs": ["close"], "func": szd_078_year_progress_sin},
    "szd_079_year_progress_cos": {"inputs": ["close"], "func": szd_079_year_progress_cos},
    "szd_080_first_days_of_month_flag": {"inputs": ["close"], "func": szd_080_first_days_of_month_flag},
    "szd_081_last_days_of_month_flag": {"inputs": ["close"], "func": szd_081_last_days_of_month_flag},
    "szd_082_first_half_of_month_flag": {"inputs": ["close"], "func": szd_082_first_half_of_month_flag},
    "szd_083_year_end_quarter_flag": {"inputs": ["close"], "func": szd_083_year_end_quarter_flag},
    "szd_084_weeks_to_year_end": {"inputs": ["close"], "func": szd_084_weeks_to_year_end},
    "szd_085_months_to_year_end": {"inputs": ["close"], "func": szd_085_months_to_year_end},
    "szd_086_september_flag": {"inputs": ["close"], "func": szd_086_september_flag},
    "szd_087_weak_season_flag": {"inputs": ["close"], "func": szd_087_weak_season_flag},
    "szd_088_strong_season_flag": {"inputs": ["close"], "func": szd_088_strong_season_flag},
    "szd_089_day_of_week_sin": {"inputs": ["close"], "func": szd_089_day_of_week_sin},
    "szd_090_day_of_week_cos": {"inputs": ["close"], "func": szd_090_day_of_week_cos},
    "szd_091_dd_504d_in_tax_loss_window": {"inputs": ["close"], "func": szd_091_dd_504d_in_tax_loss_window},
    "szd_092_dd_126d_in_q4": {"inputs": ["close"], "func": szd_092_dd_126d_in_q4},
    "szd_093_loss_magnitude_in_december": {"inputs": ["close"], "func": szd_093_loss_magnitude_in_december},
    "szd_094_loser_in_q4_score": {"inputs": ["close"], "func": szd_094_loser_in_q4_score},
    "szd_095_underwater_in_tax_loss_window": {"inputs": ["close"], "func": szd_095_underwater_in_tax_loss_window},
    "szd_096_new_low_in_tax_loss_window_flag": {"inputs": ["close"], "func": szd_096_new_low_in_tax_loss_window_flag},
    "szd_097_new_low_in_december_flag": {"inputs": ["close"], "func": szd_097_new_low_in_december_flag},
    "szd_098_days_since_low_x_tax_loss_window": {"inputs": ["close"], "func": szd_098_days_since_low_x_tax_loss_window},
    "szd_099_deep_loss_into_year_end": {"inputs": ["close"], "func": szd_099_deep_loss_into_year_end},
    "szd_100_santa_window_drawdown": {"inputs": ["close"], "func": szd_100_santa_window_drawdown},
    "szd_101_tax_loss_pressure_ramp": {"inputs": ["close", "volume"], "func": szd_101_tax_loss_pressure_ramp},
    "szd_102_january_recovery_setup": {"inputs": ["close"], "func": szd_102_january_recovery_setup},
    "szd_103_q4_decline_streak": {"inputs": ["close"], "func": szd_103_q4_decline_streak},
    "szd_104_tax_loss_window_volatility": {"inputs": ["close"], "func": szd_104_tax_loss_window_volatility},
    "szd_105_seasonal_capitulation_flag": {"inputs": ["close"], "func": szd_105_seasonal_capitulation_flag},
    "szd_106_doy_of_63d_low": {"inputs": ["close"], "func": szd_106_doy_of_63d_low},
    "szd_107_doy_of_504d_low": {"inputs": ["close"], "func": szd_107_doy_of_504d_low},
    "szd_108_quarter_of_252d_low": {"inputs": ["close"], "func": szd_108_quarter_of_252d_low},
    "szd_109_low_252d_in_january_flag": {"inputs": ["close"], "func": szd_109_low_252d_in_january_flag},
    "szd_110_low_252d_in_weak_season_flag": {"inputs": ["close"], "func": szd_110_low_252d_in_weak_season_flag},
    "szd_111_week_of_252d_low": {"inputs": ["close"], "func": szd_111_week_of_252d_low},
    "szd_112_month_of_1260d_low": {"inputs": ["close"], "func": szd_112_month_of_1260d_low},
    "szd_113_low_1260d_in_tax_loss_window_flag": {"inputs": ["close"], "func": szd_113_low_1260d_in_tax_loss_window_flag},
    "szd_114_days_from_252d_low_to_year_end": {"inputs": ["close"], "func": szd_114_days_from_252d_low_to_year_end},
    "szd_115_low_clustered_in_q4_flag": {"inputs": ["close"], "func": szd_115_low_clustered_in_q4_flag},
    "szd_116_seasonal_low_concentration": {"inputs": ["close"], "func": szd_116_seasonal_low_concentration},
    "szd_117_low_month_recurrence": {"inputs": ["close"], "func": szd_117_low_month_recurrence},
    "szd_118_low_month_sin": {"inputs": ["close"], "func": szd_118_low_month_sin},
    "szd_119_low_month_cos": {"inputs": ["close"], "func": szd_119_low_month_cos},
    "szd_120_low_in_seasonally_weak_period_flag": {"inputs": ["close"], "func": szd_120_low_in_seasonally_weak_period_flag},
    "szd_121_q4_down_volume_ratio": {"inputs": ["close", "volume"], "func": szd_121_q4_down_volume_ratio},
    "szd_122_december_realized_vol_ratio": {"inputs": ["close"], "func": szd_122_december_realized_vol_ratio},
    "szd_123_january_realized_vol_ratio": {"inputs": ["close"], "func": szd_123_january_realized_vol_ratio},
    "szd_124_turn_of_month_volume_ratio": {"inputs": ["close", "volume"], "func": szd_124_turn_of_month_volume_ratio},
    "szd_125_monday_return_mean_63d": {"inputs": ["close"], "func": szd_125_monday_return_mean_63d},
    "szd_126_friday_return_mean_63d": {"inputs": ["close"], "func": szd_126_friday_return_mean_63d},
    "szd_127_q4_mean_return_252d": {"inputs": ["close"], "func": szd_127_q4_mean_return_252d},
    "szd_128_seasonal_return_spread": {"inputs": ["close"], "func": szd_128_seasonal_return_spread},
    "szd_129_down_streak_in_december": {"inputs": ["close"], "func": szd_129_down_streak_in_december},
    "szd_130_volume_seasonality_index": {"inputs": ["volume"], "func": szd_130_volume_seasonality_index},
    "szd_131_q4_volume_trend": {"inputs": ["volume"], "func": szd_131_q4_volume_trend},
    "szd_132_month_end_return": {"inputs": ["close"], "func": szd_132_month_end_return},
    "szd_133_holiday_week_volume": {"inputs": ["volume"], "func": szd_133_holiday_week_volume},
    "szd_134_january_volume_spike": {"inputs": ["volume"], "func": szd_134_january_volume_spike},
    "szd_135_december_volume_share": {"inputs": ["volume"], "func": szd_135_december_volume_share},
    "szd_136_multi_year_low_in_tax_loss_window": {"inputs": ["close"], "func": szd_136_multi_year_low_in_tax_loss_window},
    "szd_137_seasonal_distress_intensity": {"inputs": ["close"], "func": szd_137_seasonal_distress_intensity},
    "szd_138_tax_loss_harvest_score": {"inputs": ["close", "volume"], "func": szd_138_tax_loss_harvest_score},
    "szd_139_q4_capitulation_score": {"inputs": ["close", "volume"], "func": szd_139_q4_capitulation_score},
    "szd_140_year_end_low_proximity_score": {"inputs": ["close"], "func": szd_140_year_end_low_proximity_score},
    "szd_141_january_effect_loser_score": {"inputs": ["close"], "func": szd_141_january_effect_loser_score},
    "szd_142_seasonal_low_alignment_504d": {"inputs": ["close"], "func": szd_142_seasonal_low_alignment_504d},
    "szd_143_calendar_distress_composite": {"inputs": ["close"], "func": szd_143_calendar_distress_composite},
    "szd_144_tax_loss_window_drawdown_zscore": {"inputs": ["close"], "func": szd_144_tax_loss_window_drawdown_zscore},
    "szd_145_seasonal_volume_distress": {"inputs": ["close", "volume"], "func": szd_145_seasonal_volume_distress},
    "szd_146_turn_of_year_capitulation_score": {"inputs": ["close", "volume"], "func": szd_146_turn_of_year_capitulation_score},
    "szd_147_december_low_with_volume_spike": {"inputs": ["close", "volume"], "func": szd_147_december_low_with_volume_spike},
    "szd_148_seasonal_phase_score": {"inputs": ["close"], "func": szd_148_seasonal_phase_score},
    "szd_149_annual_low_season_flag": {"inputs": ["close"], "func": szd_149_annual_low_season_flag},
    "szd_150_master_seasonal_distress_index": {"inputs": ["close", "volume"], "func": szd_150_master_seasonal_distress_index},
}
