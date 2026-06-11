"""
102_seasonal_distress — Base Features 001-075
Domain: calendar / seasonal context of distress — tax-loss-selling window,
        turn-of-year effects, and the calendar position of the multi-year low.
        Captures whether a (ticker, date) low coincides with seasonally-forced
        selling (December tax-loss harvesting, Q4 window-dressing).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
        Calendar attributes are derived from the close Series' DatetimeIndex,
        which is knowable at time t (no forward information).
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Calendar helpers (DatetimeIndex of the input Series) ─────────────────────
# CONTRACT: every input Series is daily and carries a DatetimeIndex aligned to
# the trading-day close index. All calendar attributes below are read from that
# index and are therefore knowable at time t.

def _dtidx(s: pd.Series) -> pd.DatetimeIndex:
    """Return the Series' index coerced to a DatetimeIndex."""
    idx = s.index
    if not isinstance(idx, pd.DatetimeIndex):
        idx = pd.DatetimeIndex(pd.to_datetime(idx, errors="coerce"))
    return idx


def _ser(values, s: pd.Series) -> pd.Series:
    """Wrap a numpy array as a Series on the input index."""
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


def _days_from_quarter_start(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    qs = pd.PeriodIndex(idx, freq="Q").start_time.normalize()
    return _ser((idx - qs).days, s)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Calendar-position encodings ---

def szd_001_month_of_year(close: pd.Series) -> pd.Series:
    """Calendar month of the observation (1-12)."""
    return _ser(_dtidx(close).month, close)


def szd_002_month_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of the calendar month (cyclical)."""
    return _ser(np.sin(2 * np.pi * _dtidx(close).month / 12.0), close)


def szd_003_month_cos(close: pd.Series) -> pd.Series:
    """Cosine encoding of the calendar month (cyclical)."""
    return _ser(np.cos(2 * np.pi * _dtidx(close).month / 12.0), close)


def szd_004_day_of_month(close: pd.Series) -> pd.Series:
    """Calendar day of the month (1-31)."""
    return _ser(_dtidx(close).day, close)


def szd_005_day_of_year(close: pd.Series) -> pd.Series:
    """Calendar day of the year (1-366)."""
    return _ser(_dtidx(close).dayofyear, close)


def szd_006_day_of_week(close: pd.Series) -> pd.Series:
    """Day of the week (0 = Monday ... 4 = Friday)."""
    return _ser(_dtidx(close).dayofweek, close)


def szd_007_week_of_year(close: pd.Series) -> pd.Series:
    """ISO week-of-year number (1-53)."""
    return _ser(_dtidx(close).isocalendar().week.to_numpy(), close)


def szd_008_quarter_of_year(close: pd.Series) -> pd.Series:
    """Calendar quarter (1-4)."""
    return _ser(_dtidx(close).quarter, close)


def szd_009_year_fraction_elapsed(close: pd.Series) -> pd.Series:
    """Fraction of the calendar year elapsed (0 = Jan 1, 1 = Dec 31)."""
    return _days_from_year_start(close) / 365.0


def szd_010_days_to_year_end(close: pd.Series) -> pd.Series:
    """Calendar days remaining until December 31."""
    return _days_to_year_end(close)


def szd_011_days_from_year_start(close: pd.Series) -> pd.Series:
    """Calendar days elapsed since January 1."""
    return _days_from_year_start(close)


def szd_012_days_to_quarter_end(close: pd.Series) -> pd.Series:
    """Calendar days remaining until the current quarter ends."""
    return _days_to_quarter_end(close)


def szd_013_days_from_quarter_start(close: pd.Series) -> pd.Series:
    """Calendar days elapsed since the current quarter began."""
    return _days_from_quarter_start(close)


def szd_014_doy_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of the day-of-year (fine-grained cyclical position)."""
    return _ser(np.sin(2 * np.pi * _dtidx(close).dayofyear / 365.0), close)


def szd_015_doy_cos(close: pd.Series) -> pd.Series:
    """Cosine encoding of the day-of-year (fine-grained cyclical position)."""
    return _ser(np.cos(2 * np.pi * _dtidx(close).dayofyear / 365.0), close)


# --- Group B (016-030): Tax-loss-selling & turn-of-year windows ---

def szd_016_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in the Nov-Dec tax-loss-selling window."""
    m = _dtidx(close).month
    return _ser(np.isin(m, [11, 12]).astype(float), close)


def szd_017_deep_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in December (peak tax-loss harvesting)."""
    return _ser((_dtidx(close).month == 12).astype(float), close)


def szd_018_october_selloff_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in October (historically weak / early harvesting)."""
    return _ser((_dtidx(close).month == 10).astype(float), close)


def szd_019_last_days_of_year_flag(close: pd.Series) -> pd.Series:
    """Flag: within the final 5 calendar days of the year."""
    return (_days_to_year_end(close) <= 5).astype(float)


def szd_020_santa_claus_window_flag(close: pd.Series) -> pd.Series:
    """Flag: last 5 days of the year or first 2 days of January."""
    last = _days_to_year_end(close) <= 5
    first = _days_from_year_start(close) <= 2
    return (last | first).astype(float)


def szd_021_january_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in January (January-effect month)."""
    return _ser((_dtidx(close).month == 1).astype(float), close)


def szd_022_january_effect_window(close: pd.Series) -> pd.Series:
    """Flag: within the first ~10 trading days of January."""
    idx = _dtidx(close)
    return _ser(((idx.month == 1) & (idx.day <= 14)).astype(float), close)


def szd_023_tax_loss_intensity(close: pd.Series) -> pd.Series:
    """Ramp 0->1 across the Oct-Dec tax-loss window (1 at year-end)."""
    m = _dtidx(close).month
    in_window = np.isin(m, [10, 11, 12])
    ramp = (1.0 - _days_to_year_end(close) / 92.0).clip(lower=0, upper=1)
    return ramp * _ser(in_window.astype(float), close)


def szd_024_days_into_tax_loss_window(close: pd.Series) -> pd.Series:
    """Calendar days elapsed since November 1 (0 outside Nov-Dec)."""
    idx = _dtidx(close)
    in_window = np.isin(idx.month, [11, 12])
    days = 92.0 - _days_to_year_end(close)
    return days.clip(lower=0) * _ser(in_window.astype(float), close)


def szd_025_turn_of_year_proximity(close: pd.Series) -> pd.Series:
    """Proximity to December 31 (1 at year-end, decaying away from it)."""
    dte = _days_to_year_end(close)
    dys = _days_from_year_start(close)
    nearest = pd.concat([dte, dys], axis=1).min(axis=1)
    return (1.0 - nearest / 30.0).clip(lower=0)


def szd_026_q4_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in the fourth calendar quarter."""
    return _ser((_dtidx(close).quarter == 4).astype(float), close)


def szd_027_q1_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in the first calendar quarter."""
    return _ser((_dtidx(close).quarter == 1).astype(float), close)


def szd_028_turn_of_month_flag(close: pd.Series) -> pd.Series:
    """Flag: within the last 3 or first 3 calendar days of a month."""
    d = _dtidx(close).day
    return _ser(((d <= 3) | (d >= 26)).astype(float), close)


def szd_029_mid_month_flag(close: pd.Series) -> pd.Series:
    """Flag: mid-month (calendar days 12-18)."""
    d = _dtidx(close).day
    return _ser(((d >= 12) & (d <= 18)).astype(float), close)


def szd_030_sell_in_may_flag(close: pd.Series) -> pd.Series:
    """Flag: within the seasonally-weak May-October half of the year."""
    m = _dtidx(close).month
    return _ser(np.isin(m, [5, 6, 7, 8, 9, 10]).astype(float), close)


# --- Group C (031-045): Seasonal interaction with drawdown / losses ---

def szd_031_dd_252d_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the Nov-Dec tax-loss window (else 0)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_016_tax_loss_window_flag(close)


def szd_032_dd_252d_in_december(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to December (peak harvesting month)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_017_deep_tax_loss_window_flag(close)


def szd_033_dd_252d_in_q4(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the fourth quarter."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_026_q4_flag(close)


def szd_034_dd_x_days_to_year_end(close: pd.Series) -> pd.Series:
    """252-day drawdown weighted by turn-of-year proximity."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_025_turn_of_year_proximity(close)


def szd_035_dd_252d_in_january(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to January (post-harvesting rebound month)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_021_january_flag(close)


def szd_036_q4_return(close: pd.Series) -> pd.Series:
    """Return accumulated since the start of the current quarter (QTD)."""
    qstart_days = _days_from_quarter_start(close)
    ret = pd.Series(np.nan, index=close.index)
    for w in (5, 21, 42, 63):
        mask = (qstart_days >= w - 5) & (qstart_days < w + 5)
        ret = ret.where(~mask, close.pct_change(w))
    return ret.fillna(close.pct_change(_TD_QTR))


def szd_037_ytd_return(close: pd.Series) -> pd.Series:
    """Approximate year-to-date return (return over days elapsed this year)."""
    elapsed = (_days_from_year_start(close) * 0.69).round().clip(lower=1, upper=_TD_YEAR)
    n = len(close)
    vals = np.full(n, np.nan)
    cv = close.values
    ev = elapsed.values.astype(int)
    for i in range(n):
        j = i - ev[i]
        if j >= 0 and cv[j] != 0:
            vals[i] = cv[i] / cv[j] - 1.0
    return pd.Series(vals, index=close.index)


def szd_038_ytd_return_in_december(close: pd.Series) -> pd.Series:
    """Year-to-date return gated to December (the loser-into-year-end view)."""
    return szd_037_ytd_return(close) * szd_017_deep_tax_loss_window_flag(close)


def szd_039_trailing_year_loser_flag(close: pd.Series) -> pd.Series:
    """Flag: trailing 252-day return below -20% (tax-loss-harvest candidate)."""
    return (close.pct_change(_TD_YEAR) < -0.20).astype(float)


def szd_040_tax_loss_candidate_score(close: pd.Series) -> pd.Series:
    """Loser magnitude times tax-loss-window intensity (harvest pressure)."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return loss * szd_023_tax_loss_intensity(close)


def szd_041_dd_63d_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """63-day drawdown gated to the Nov-Dec tax-loss window."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    return dd * szd_016_tax_loss_window_flag(close)


def szd_042_momentum_6m_in_january(close: pd.Series) -> pd.Series:
    """6-month price momentum gated to January (January-effect setup)."""
    return close.pct_change(_TD_HALF) * szd_021_january_flag(close)


def szd_043_dd_x_turn_of_month(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the turn-of-month window."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_028_turn_of_month_flag(close)


def szd_044_seasonal_distress_score(close: pd.Series) -> pd.Series:
    """Drawdown depth times tax-loss intensity times year-end proximity."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    return dd * szd_023_tax_loss_intensity(close) * szd_025_turn_of_year_proximity(close)


def szd_045_dd_at_seasonal_low_period(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the seasonally-weak May-October half."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_030_sell_in_may_flag(close)


# --- Group D (046-060): Calendar position of the trailing low ---

def szd_046_month_of_252d_low(close: pd.Series) -> pd.Series:
    """Calendar month in which the trailing 252-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_YEAR)


def szd_047_low_252d_in_december_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in December."""
    return (szd_046_month_of_252d_low(close) == 12).astype(float)


def szd_048_low_252d_in_q4_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in the fourth quarter."""
    m = szd_046_month_of_252d_low(close)
    return m.isin([10, 11, 12]).astype(float)


def szd_049_low_252d_in_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set during the Nov-Dec window."""
    m = szd_046_month_of_252d_low(close)
    return m.isin([11, 12]).astype(float)


def szd_050_doy_of_252d_low(close: pd.Series) -> pd.Series:
    """Day-of-year on which the trailing 252-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).dayofyear.to_numpy(), _TD_YEAR)


def szd_051_low_set_near_year_end_flag(close: pd.Series) -> pd.Series:
    """Flag: the 252-day low fell within the last 6 weeks of a calendar year."""
    doy = szd_050_doy_of_252d_low(close)
    return (doy >= 320).astype(float)


def szd_052_month_of_63d_low(close: pd.Series) -> pd.Series:
    """Calendar month in which the trailing 63-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), _TD_QTR)


def szd_053_low_63d_in_december_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 63-day low was set in December."""
    return (szd_052_month_of_63d_low(close) == 12).astype(float)


def szd_054_new_lows_in_q4_fraction(close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d new 21-day lows that occurred in Q4."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    q4 = szd_026_q4_flag(close)
    total = _rolling_sum(new_low, _TD_YEAR)
    in_q4 = _rolling_sum(new_low * q4, _TD_YEAR)
    return _safe_div(in_q4, total)


def szd_055_new_lows_in_december_fraction(close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d new 21-day lows that occurred in December."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    dec = szd_017_deep_tax_loss_window_flag(close)
    total = _rolling_sum(new_low, _TD_YEAR)
    in_dec = _rolling_sum(new_low * dec, _TD_YEAR)
    return _safe_div(in_dec, total)


def szd_056_days_since_252d_low(close: pd.Series) -> pd.Series:
    """Trading days since the trailing 252-day low was set."""
    return close.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)


def szd_057_low_recency_in_january(close: pd.Series) -> pd.Series:
    """Recency of the 252-day low (1 = at the low) gated to January."""
    age = szd_056_days_since_252d_low(close)
    recency = (1.0 - age / _TD_YEAR).clip(lower=0)
    return recency * szd_021_january_flag(close)


def szd_058_seasonal_low_alignment(close: pd.Series) -> pd.Series:
    """The 252-day low was both recent and set in the tax-loss window."""
    age = szd_056_days_since_252d_low(close)
    recency = (1.0 - age / _TD_QTR).clip(lower=0)
    return recency * szd_049_low_252d_in_tax_loss_window_flag(close)


def szd_059_month_of_504d_low(close: pd.Series) -> pd.Series:
    """Calendar month in which the trailing 504-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).month.to_numpy(), 504)


def szd_060_low_504d_in_tax_loss_window_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 504-day low was set during the Nov-Dec window."""
    m = szd_059_month_of_504d_low(close)
    return m.isin([11, 12]).astype(float)


# --- Group E (061-075): Seasonal volume / return patterns ---

def szd_061_december_volume_ratio(volume: pd.Series) -> pd.Series:
    """Current volume vs 252-day median, gated to December."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return ratio * szd_017_deep_tax_loss_window_flag(volume)


def szd_062_q4_volume_ratio(volume: pd.Series) -> pd.Series:
    """Current volume vs 252-day median, gated to the fourth quarter."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return ratio * szd_026_q4_flag(volume)


def szd_063_january_volume_ratio(volume: pd.Series) -> pd.Series:
    """Current volume vs 252-day median, gated to January."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return ratio * szd_021_january_flag(volume)


def szd_064_turn_of_year_volume_spike(volume: pd.Series) -> pd.Series:
    """Volume vs 63-day median, weighted by turn-of-year proximity."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_QTR))
    return ratio * szd_025_turn_of_year_proximity(volume)


def szd_065_tax_loss_window_volume_ratio(volume: pd.Series) -> pd.Series:
    """Volume vs 252-day median, weighted by tax-loss-window intensity."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return ratio * szd_023_tax_loss_intensity(volume)


def szd_066_down_day_fraction_in_q4(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day down days that fell in the fourth quarter."""
    down = (_daily_ret(close) < 0).astype(float)
    q4 = szd_026_q4_flag(close)
    return _safe_div(_rolling_sum(down * q4, _TD_QTR), _rolling_sum(down, _TD_QTR))


def szd_067_trailing_month_return(close: pd.Series) -> pd.Series:
    """Trailing 21-day return (monthly seasonal return carrier)."""
    return close.pct_change(_TD_MON)


def szd_068_dow_return_tag(close: pd.Series) -> pd.Series:
    """Daily return tagged by day-of-week sign pattern (Monday-effect carrier)."""
    dow = _ser(_dtidx(close).dayofweek, close)
    return _daily_ret(close) * np.cos(2 * np.pi * dow / 5.0)


def szd_069_monday_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls on a Monday (weekend-effect carrier)."""
    return _ser((_dtidx(close).dayofweek == 0).astype(float), close)


def szd_070_friday_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls on a Friday."""
    return _ser((_dtidx(close).dayofweek == 4).astype(float), close)


def szd_071_month_end_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls on or after the 25th calendar day of a month."""
    return _ser((_dtidx(close).day >= 25).astype(float), close)


def szd_072_seasonal_volume_zscore_q4(volume: pd.Series) -> pd.Series:
    """Volume z-score over 252 days, gated to the fourth quarter."""
    z = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    return z * szd_026_q4_flag(volume)


def szd_073_volume_in_tax_loss_window(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day dollar-flow proxy gated to the Nov-Dec tax-loss window."""
    down_vol = volume.where(_daily_ret(close) < 0, 0.0)
    ratio = _safe_div(down_vol, _rolling_median(volume, _TD_YEAR))
    return ratio * szd_016_tax_loss_window_flag(close)


def szd_074_q4_realized_vol_ratio(close: pd.Series) -> pd.Series:
    """21-day vs 252-day realized-volatility ratio, gated to the fourth quarter."""
    ret = _daily_ret(close)
    vr = _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_YEAR))
    return vr * szd_026_q4_flag(close)


def szd_075_seasonal_distress_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: drawdown depth, tax-loss intensity and elevated down-volume."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    intensity = szd_023_tax_loss_intensity(close)
    down_vol = volume.where(_daily_ret(close) < 0, 0.0)
    vol_ratio = _safe_div(down_vol, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return dd * intensity * (1.0 + vol_ratio)


# ── Registry ──────────────────────────────────────────────────────────────────

SEASONAL_DISTRESS_REGISTRY_001_075 = {
    "szd_001_month_of_year": {"inputs": ["close"], "func": szd_001_month_of_year},
    "szd_002_month_sin": {"inputs": ["close"], "func": szd_002_month_sin},
    "szd_003_month_cos": {"inputs": ["close"], "func": szd_003_month_cos},
    "szd_004_day_of_month": {"inputs": ["close"], "func": szd_004_day_of_month},
    "szd_005_day_of_year": {"inputs": ["close"], "func": szd_005_day_of_year},
    "szd_006_day_of_week": {"inputs": ["close"], "func": szd_006_day_of_week},
    "szd_007_week_of_year": {"inputs": ["close"], "func": szd_007_week_of_year},
    "szd_008_quarter_of_year": {"inputs": ["close"], "func": szd_008_quarter_of_year},
    "szd_009_year_fraction_elapsed": {"inputs": ["close"], "func": szd_009_year_fraction_elapsed},
    "szd_010_days_to_year_end": {"inputs": ["close"], "func": szd_010_days_to_year_end},
    "szd_011_days_from_year_start": {"inputs": ["close"], "func": szd_011_days_from_year_start},
    "szd_012_days_to_quarter_end": {"inputs": ["close"], "func": szd_012_days_to_quarter_end},
    "szd_013_days_from_quarter_start": {"inputs": ["close"], "func": szd_013_days_from_quarter_start},
    "szd_014_doy_sin": {"inputs": ["close"], "func": szd_014_doy_sin},
    "szd_015_doy_cos": {"inputs": ["close"], "func": szd_015_doy_cos},
    "szd_016_tax_loss_window_flag": {"inputs": ["close"], "func": szd_016_tax_loss_window_flag},
    "szd_017_deep_tax_loss_window_flag": {"inputs": ["close"], "func": szd_017_deep_tax_loss_window_flag},
    "szd_018_october_selloff_flag": {"inputs": ["close"], "func": szd_018_october_selloff_flag},
    "szd_019_last_days_of_year_flag": {"inputs": ["close"], "func": szd_019_last_days_of_year_flag},
    "szd_020_santa_claus_window_flag": {"inputs": ["close"], "func": szd_020_santa_claus_window_flag},
    "szd_021_january_flag": {"inputs": ["close"], "func": szd_021_january_flag},
    "szd_022_january_effect_window": {"inputs": ["close"], "func": szd_022_january_effect_window},
    "szd_023_tax_loss_intensity": {"inputs": ["close"], "func": szd_023_tax_loss_intensity},
    "szd_024_days_into_tax_loss_window": {"inputs": ["close"], "func": szd_024_days_into_tax_loss_window},
    "szd_025_turn_of_year_proximity": {"inputs": ["close"], "func": szd_025_turn_of_year_proximity},
    "szd_026_q4_flag": {"inputs": ["close"], "func": szd_026_q4_flag},
    "szd_027_q1_flag": {"inputs": ["close"], "func": szd_027_q1_flag},
    "szd_028_turn_of_month_flag": {"inputs": ["close"], "func": szd_028_turn_of_month_flag},
    "szd_029_mid_month_flag": {"inputs": ["close"], "func": szd_029_mid_month_flag},
    "szd_030_sell_in_may_flag": {"inputs": ["close"], "func": szd_030_sell_in_may_flag},
    "szd_031_dd_252d_in_tax_loss_window": {"inputs": ["close"], "func": szd_031_dd_252d_in_tax_loss_window},
    "szd_032_dd_252d_in_december": {"inputs": ["close"], "func": szd_032_dd_252d_in_december},
    "szd_033_dd_252d_in_q4": {"inputs": ["close"], "func": szd_033_dd_252d_in_q4},
    "szd_034_dd_x_days_to_year_end": {"inputs": ["close"], "func": szd_034_dd_x_days_to_year_end},
    "szd_035_dd_252d_in_january": {"inputs": ["close"], "func": szd_035_dd_252d_in_january},
    "szd_036_q4_return": {"inputs": ["close"], "func": szd_036_q4_return},
    "szd_037_ytd_return": {"inputs": ["close"], "func": szd_037_ytd_return},
    "szd_038_ytd_return_in_december": {"inputs": ["close"], "func": szd_038_ytd_return_in_december},
    "szd_039_trailing_year_loser_flag": {"inputs": ["close"], "func": szd_039_trailing_year_loser_flag},
    "szd_040_tax_loss_candidate_score": {"inputs": ["close"], "func": szd_040_tax_loss_candidate_score},
    "szd_041_dd_63d_in_tax_loss_window": {"inputs": ["close"], "func": szd_041_dd_63d_in_tax_loss_window},
    "szd_042_momentum_6m_in_january": {"inputs": ["close"], "func": szd_042_momentum_6m_in_january},
    "szd_043_dd_x_turn_of_month": {"inputs": ["close"], "func": szd_043_dd_x_turn_of_month},
    "szd_044_seasonal_distress_score": {"inputs": ["close"], "func": szd_044_seasonal_distress_score},
    "szd_045_dd_at_seasonal_low_period": {"inputs": ["close"], "func": szd_045_dd_at_seasonal_low_period},
    "szd_046_month_of_252d_low": {"inputs": ["close"], "func": szd_046_month_of_252d_low},
    "szd_047_low_252d_in_december_flag": {"inputs": ["close"], "func": szd_047_low_252d_in_december_flag},
    "szd_048_low_252d_in_q4_flag": {"inputs": ["close"], "func": szd_048_low_252d_in_q4_flag},
    "szd_049_low_252d_in_tax_loss_window_flag": {"inputs": ["close"], "func": szd_049_low_252d_in_tax_loss_window_flag},
    "szd_050_doy_of_252d_low": {"inputs": ["close"], "func": szd_050_doy_of_252d_low},
    "szd_051_low_set_near_year_end_flag": {"inputs": ["close"], "func": szd_051_low_set_near_year_end_flag},
    "szd_052_month_of_63d_low": {"inputs": ["close"], "func": szd_052_month_of_63d_low},
    "szd_053_low_63d_in_december_flag": {"inputs": ["close"], "func": szd_053_low_63d_in_december_flag},
    "szd_054_new_lows_in_q4_fraction": {"inputs": ["close"], "func": szd_054_new_lows_in_q4_fraction},
    "szd_055_new_lows_in_december_fraction": {"inputs": ["close"], "func": szd_055_new_lows_in_december_fraction},
    "szd_056_days_since_252d_low": {"inputs": ["close"], "func": szd_056_days_since_252d_low},
    "szd_057_low_recency_in_january": {"inputs": ["close"], "func": szd_057_low_recency_in_january},
    "szd_058_seasonal_low_alignment": {"inputs": ["close"], "func": szd_058_seasonal_low_alignment},
    "szd_059_month_of_504d_low": {"inputs": ["close"], "func": szd_059_month_of_504d_low},
    "szd_060_low_504d_in_tax_loss_window_flag": {"inputs": ["close"], "func": szd_060_low_504d_in_tax_loss_window_flag},
    "szd_061_december_volume_ratio": {"inputs": ["volume"], "func": szd_061_december_volume_ratio},
    "szd_062_q4_volume_ratio": {"inputs": ["volume"], "func": szd_062_q4_volume_ratio},
    "szd_063_january_volume_ratio": {"inputs": ["volume"], "func": szd_063_january_volume_ratio},
    "szd_064_turn_of_year_volume_spike": {"inputs": ["volume"], "func": szd_064_turn_of_year_volume_spike},
    "szd_065_tax_loss_window_volume_ratio": {"inputs": ["volume"], "func": szd_065_tax_loss_window_volume_ratio},
    "szd_066_down_day_fraction_in_q4": {"inputs": ["close"], "func": szd_066_down_day_fraction_in_q4},
    "szd_067_trailing_month_return": {"inputs": ["close"], "func": szd_067_trailing_month_return},
    "szd_068_dow_return_tag": {"inputs": ["close"], "func": szd_068_dow_return_tag},
    "szd_069_monday_flag": {"inputs": ["close"], "func": szd_069_monday_flag},
    "szd_070_friday_flag": {"inputs": ["close"], "func": szd_070_friday_flag},
    "szd_071_month_end_flag": {"inputs": ["close"], "func": szd_071_month_end_flag},
    "szd_072_seasonal_volume_zscore_q4": {"inputs": ["volume"], "func": szd_072_seasonal_volume_zscore_q4},
    "szd_073_volume_in_tax_loss_window": {"inputs": ["close", "volume"], "func": szd_073_volume_in_tax_loss_window},
    "szd_074_q4_realized_vol_ratio": {"inputs": ["close"], "func": szd_074_q4_realized_vol_ratio},
    "szd_075_seasonal_distress_composite": {"inputs": ["close", "volume"], "func": szd_075_seasonal_distress_composite},
}
