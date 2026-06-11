"""
102_seasonal_distress — Extended Features 001-075
Domain: calendar / seasonal context of distress — additional angles not in the
        four base files: bi-monthly and intra-quarter encodings, half-year and
        season interactions, holiday-effect windows, day-count-into-season
        ramps, seasonal streaks, seasonal percentile ranks and z-scores, and
        gated volume/return composites on fresh window combinations.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
        Calendar attributes are derived from the input Series' DatetimeIndex,
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


# ── Calendar helpers (DatetimeIndex of the input Series) ─────────────────────
# CONTRACT: every input Series is daily with a DatetimeIndex aligned to the
# trading-day close index; all calendar attributes are knowable at time t.

def _dtidx(s: pd.Series) -> pd.DatetimeIndex:
    """Return the Series' index coerced to a DatetimeIndex."""
    idx = s.index
    if not isinstance(idx, pd.DatetimeIndex):
        idx = pd.DatetimeIndex(pd.to_datetime(idx, errors="coerce"))
    return idx


def _ser(values, s: pd.Series) -> pd.Series:
    """Wrap a numpy array as a float Series on the input index."""
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


def _days_from_month_start(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    ms = pd.PeriodIndex(idx, freq="M").start_time.normalize()
    return _ser((idx - ms).days, s)


def _days_to_month_end(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    me = pd.PeriodIndex(idx, freq="M").end_time.normalize()
    return _ser((me - idx).days, s)


def _month(s: pd.Series) -> np.ndarray:
    return _dtidx(s).month.to_numpy()


def _half1_flag(s: pd.Series) -> pd.Series:
    """Flag: in the first calendar half of the year (Jan-Jun)."""
    return _ser((_dtidx(s).month <= 6).astype(float), s)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional calendar-position encodings ---

def szd_ext_001_bimonthly_index(close: pd.Series) -> pd.Series:
    """Bi-monthly bucket of the observation (1-6, two months per bucket)."""
    return _ser(np.ceil(_dtidx(close).month / 2.0), close)


def szd_ext_002_half_year_index(close: pd.Series) -> pd.Series:
    """Calendar half-year index (1 = Jan-Jun, 2 = Jul-Dec)."""
    return _ser(np.where(_dtidx(close).month <= 6, 1.0, 2.0), close)


def szd_ext_003_third_of_year_index(close: pd.Series) -> pd.Series:
    """Third-of-year bucket of the observation (1-3, four months each)."""
    return _ser(np.ceil(_dtidx(close).month / 4.0), close)


def szd_ext_004_quarter_fraction_elapsed(close: pd.Series) -> pd.Series:
    """Fraction of the current calendar quarter elapsed (0 at start, ~1 at end)."""
    dfs = _days_from_quarter_start(close)
    dte = _days_to_quarter_end(close)
    return _safe_div(dfs, dfs + dte)


def szd_ext_005_month_fraction_elapsed(close: pd.Series) -> pd.Series:
    """Fraction of the current calendar month elapsed (0 at start, ~1 at end)."""
    dfs = _days_from_month_start(close)
    dte = _days_to_month_end(close)
    return _safe_div(dfs, dfs + dte)


def szd_ext_006_days_to_month_end(close: pd.Series) -> pd.Series:
    """Calendar days remaining until the current month ends."""
    return _days_to_month_end(close)


def szd_ext_007_days_from_month_start(close: pd.Series) -> pd.Series:
    """Calendar days elapsed since the current month began."""
    return _days_from_month_start(close)


def szd_ext_008_quarter_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of the calendar quarter (cyclical)."""
    return _ser(np.sin(2 * np.pi * _dtidx(close).quarter / 4.0), close)


def szd_ext_009_quarter_cos(close: pd.Series) -> pd.Series:
    """Cosine encoding of the calendar quarter (cyclical)."""
    return _ser(np.cos(2 * np.pi * _dtidx(close).quarter / 4.0), close)


def szd_ext_010_week_of_month(close: pd.Series) -> pd.Series:
    """Week-of-month bucket (1-5) based on the calendar day."""
    return _ser(np.ceil(_dtidx(close).day / 7.0), close)


def szd_ext_011_is_leap_year_flag(close: pd.Series) -> pd.Series:
    """Flag: the observation falls within a leap calendar year."""
    return _ser(_dtidx(close).is_leap_year.astype(float), close)


def szd_ext_012_days_to_quarter_end_sin(close: pd.Series) -> pd.Series:
    """Sine encoding of intra-quarter position from days-to-quarter-end."""
    frac = _days_to_quarter_end(close) / 92.0
    return _ser(np.sin(2 * np.pi * frac.values), close)


# --- Group B (013-026): Holiday-effect & seasonal window flags ---

def szd_ext_013_pre_holiday_year_end_flag(close: pd.Series) -> pd.Series:
    """Flag: within the last 8 calendar days of the year (holiday-effect run)."""
    return (_days_to_year_end(close) <= 8).astype(float)


def szd_ext_014_early_january_window_flag(close: pd.Series) -> pd.Series:
    """Flag: within the first 5 calendar days of January."""
    idx = _dtidx(close)
    return _ser(((idx.month == 1) & (idx.day <= 5)).astype(float), close)


def szd_ext_015_summer_doldrums_flag(close: pd.Series) -> pd.Series:
    """Flag: in the low-liquidity July-August summer window."""
    return _ser(np.isin(_dtidx(close).month, [7, 8]).astype(float), close)


def szd_ext_016_spring_window_flag(close: pd.Series) -> pd.Series:
    """Flag: in the March-May spring window."""
    return _ser(np.isin(_dtidx(close).month, [3, 4, 5]).astype(float), close)


def szd_ext_017_q3_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in the third calendar quarter."""
    return _ser((_dtidx(close).quarter == 3).astype(float), close)


def szd_ext_018_q2_flag(close: pd.Series) -> pd.Series:
    """Flag: observation falls in the second calendar quarter."""
    return _ser((_dtidx(close).quarter == 2).astype(float), close)


def szd_ext_019_fiscal_q4_extended_flag(close: pd.Series) -> pd.Series:
    """Flag: in the extended fiscal-year-end window (Sept-Dec)."""
    return _ser(np.isin(_dtidx(close).month, [9, 10, 11, 12]).astype(float), close)


def szd_ext_020_mid_quarter_flag(close: pd.Series) -> pd.Series:
    """Flag: mid-quarter (days 25-45 into the quarter)."""
    d = _days_from_quarter_start(close)
    return ((d >= 25) & (d <= 45)).astype(float)


def szd_ext_021_quarter_end_window_flag(close: pd.Series) -> pd.Series:
    """Flag: within the last 7 calendar days of a quarter (window-dressing)."""
    return (_days_to_quarter_end(close) <= 7).astype(float)


def szd_ext_022_quarter_start_window_flag(close: pd.Series) -> pd.Series:
    """Flag: within the first 7 calendar days of a quarter."""
    return (_days_from_quarter_start(close) <= 7).astype(float)


def szd_ext_023_options_expiry_week_flag(close: pd.Series) -> pd.Series:
    """Flag: third calendar week of the month (monthly options-expiry week)."""
    d = _dtidx(close).day
    return _ser(((d >= 15) & (d <= 21)).astype(float), close)


def szd_ext_024_first_trading_week_flag(close: pd.Series) -> pd.Series:
    """Flag: within the first 7 calendar days of a month."""
    return _ser((_dtidx(close).day <= 7).astype(float), close)


def szd_ext_025_thanksgiving_window_flag(close: pd.Series) -> pd.Series:
    """Flag: late-November window (Nov 20-30, Thanksgiving liquidity dip)."""
    idx = _dtidx(close)
    return _ser(((idx.month == 11) & (idx.day >= 20)).astype(float), close)


def szd_ext_026_year_end_runup_ramp(close: pd.Series) -> pd.Series:
    """Linear ramp 0->1 over the final 21 calendar days of the year."""
    return (1.0 - _days_to_year_end(close) / 21.0).clip(lower=0, upper=1)


# --- Group C (027-040): Seasonal interaction with drawdown / loss (new windows) ---

def szd_ext_027_dd_42d_in_q4(close: pd.Series) -> pd.Series:
    """42-day drawdown gated to the fourth quarter."""
    dd = _safe_div(close - _rolling_max(close, 42), _rolling_max(close, 42))
    return dd * _q4_flag(close)


def szd_ext_028_dd_126d_in_december(close: pd.Series) -> pd.Series:
    """126-day drawdown gated to December (deep harvesting month)."""
    dd = _safe_div(close - _rolling_max(close, _TD_HALF), _rolling_max(close, _TD_HALF))
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return dd * dec


def szd_ext_029_dd_252d_in_september(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to September (historically weakest month)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    sep = _ser((_dtidx(close).month == 9).astype(float), close)
    return dd * sep


def szd_ext_030_dd_21d_in_quarter_end_window(close: pd.Series) -> pd.Series:
    """21-day drawdown gated to the last 7 days of a quarter."""
    dd = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    return dd * szd_ext_021_quarter_end_window_flag(close)


def szd_ext_031_loss_63d_in_q4(close: pd.Series) -> pd.Series:
    """63-day loss magnitude gated to the fourth quarter."""
    loss = (-close.pct_change(_TD_QTR)).clip(lower=0)
    return loss * _q4_flag(close)


def szd_ext_032_loss_126d_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """126-day loss magnitude gated to the Nov-Dec tax-loss window."""
    loss = (-close.pct_change(_TD_HALF)).clip(lower=0)
    return loss * _tax_loss_window(close)


def szd_ext_033_dd_504d_in_q4(close: pd.Series) -> pd.Series:
    """504-day drawdown gated to the fourth quarter (multi-year distress)."""
    dd = _safe_div(close - _rolling_max(close, 504), _rolling_max(close, 504))
    return dd * _q4_flag(close)


def szd_ext_034_qtd_return(close: pd.Series) -> pd.Series:
    """Quarter-to-date return approximated over days elapsed in the quarter."""
    elapsed = (_days_from_quarter_start(close) * 0.69).round().clip(lower=1, upper=_TD_QTR)
    n = len(close)
    vals = np.full(n, np.nan)
    cv = close.values
    ev = elapsed.values.astype(int)
    for i in range(n):
        j = i - ev[i]
        if j >= 0 and cv[j] != 0:
            vals[i] = cv[i] / cv[j] - 1.0
    return pd.Series(vals, index=close.index)


def szd_ext_035_qtd_return_in_q4(close: pd.Series) -> pd.Series:
    """Quarter-to-date return gated to the fourth quarter."""
    return szd_ext_034_qtd_return(close) * _q4_flag(close)


def szd_ext_036_mtd_return(close: pd.Series) -> pd.Series:
    """Month-to-date return approximated over days elapsed in the month."""
    elapsed = (_days_from_month_start(close) * 0.69).round().clip(lower=1, upper=_TD_MON)
    n = len(close)
    vals = np.full(n, np.nan)
    cv = close.values
    ev = elapsed.values.astype(int)
    for i in range(n):
        j = i - ev[i]
        if j >= 0 and cv[j] != 0:
            vals[i] = cv[i] / cv[j] - 1.0
    return pd.Series(vals, index=close.index)


def szd_ext_037_deep_loser_in_q4_flag(close: pd.Series) -> pd.Series:
    """Flag: trailing-year loss worse than -30% during the fourth quarter."""
    deep = (close.pct_change(_TD_YEAR) < -0.30).astype(float)
    return deep * _q4_flag(close)


def szd_ext_038_dd_x_quarter_end_proximity(close: pd.Series) -> pd.Series:
    """252-day drawdown weighted by proximity to the quarter end."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    prox = (1.0 - _days_to_quarter_end(close) / 30.0).clip(lower=0)
    return dd * prox


def szd_ext_039_summer_drawdown(close: pd.Series) -> pd.Series:
    """252-day drawdown gated to the July-August summer window."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return dd * szd_ext_015_summer_doldrums_flag(close)


def szd_ext_040_loss_x_year_end_runup(close: pd.Series) -> pd.Series:
    """Trailing-year loss magnitude weighted by the year-end run-up ramp."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return loss * szd_ext_026_year_end_runup_ramp(close)


# --- Group D (041-052): Calendar position of the trailing low (new windows) ---

def szd_ext_041_month_of_126d_low(close: pd.Series) -> pd.Series:
    """Calendar month in which the trailing 126-day low was set."""
    return _attr_at_rolling_min(close, _month(close).astype(float), _TD_HALF)


def szd_ext_042_low_126d_in_q4_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 126-day low was set in the fourth quarter."""
    m = szd_ext_041_month_of_126d_low(close)
    return m.isin([10, 11, 12]).astype(float)


def szd_ext_043_quarter_of_63d_low(close: pd.Series) -> pd.Series:
    """Calendar quarter in which the trailing 63-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).quarter.to_numpy().astype(float), _TD_QTR)


def szd_ext_044_low_252d_in_summer_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in July or August."""
    m = _attr_at_rolling_min(close, _month(close).astype(float), _TD_YEAR)
    return m.isin([7, 8]).astype(float)


def szd_ext_045_low_252d_in_september_flag(close: pd.Series) -> pd.Series:
    """Flag: the trailing 252-day low was set in September."""
    m = _attr_at_rolling_min(close, _month(close).astype(float), _TD_YEAR)
    return (m == 9).astype(float)


def szd_ext_046_day_of_month_of_252d_low(close: pd.Series) -> pd.Series:
    """Calendar day-of-month on which the trailing 252-day low was set."""
    return _attr_at_rolling_min(close, _dtidx(close).day.to_numpy().astype(float), _TD_YEAR)


def szd_ext_047_low_252d_set_at_month_end_flag(close: pd.Series) -> pd.Series:
    """Flag: the 252-day low day-of-month is in the last week (day >= 25)."""
    dom = szd_ext_046_day_of_month_of_252d_low(close)
    return (dom >= 25).astype(float)


def szd_ext_048_days_since_63d_low(close: pd.Series) -> pd.Series:
    """Trading days since the trailing 63-day low was set."""
    return close.rolling(_TD_QTR, min_periods=_TD_MON).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)


def szd_ext_049_days_since_504d_low(close: pd.Series) -> pd.Series:
    """Trading days since the trailing 504-day low was set."""
    return close.rolling(504, min_periods=_TD_QTR).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)


def szd_ext_050_low_month_recency_in_q4(close: pd.Series) -> pd.Series:
    """Recency of the 252-day low (1 = at the low) gated to the fourth quarter."""
    age = close.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)
    recency = (1.0 - age / _TD_YEAR).clip(lower=0)
    return recency * _q4_flag(close)


def szd_ext_051_new_lows_in_h2_fraction(close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d new 21-day lows that occurred in the second half-year."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    h2 = _ser((_dtidx(close).month >= 7).astype(float), close)
    total = _rolling_sum(new_low, _TD_YEAR)
    in_h2 = _rolling_sum(new_low * h2, _TD_YEAR)
    return _safe_div(in_h2, total)


def szd_ext_052_new_lows_in_summer_fraction(close: pd.Series) -> pd.Series:
    """Fraction of trailing-252d new 21-day lows that occurred in Jul-Aug."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    summer = szd_ext_015_summer_doldrums_flag(close)
    total = _rolling_sum(new_low, _TD_YEAR)
    in_summer = _rolling_sum(new_low * summer, _TD_YEAR)
    return _safe_div(in_summer, total)


# --- Group E (053-062): Seasonal streaks and counts ---

def szd_ext_053_consec_down_days_in_q4(close: pd.Series) -> pd.Series:
    """Consecutive down-day streak, evaluated only on fourth-quarter days."""
    streak = _consec_streak(_daily_ret(close) < 0)
    return streak * _q4_flag(close)


def szd_ext_054_consec_down_days_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """Consecutive down-day streak, evaluated only in the Nov-Dec window."""
    streak = _consec_streak(_daily_ret(close) < 0)
    return streak * _tax_loss_window(close)


def szd_ext_055_down_day_count_21d_in_q4(close: pd.Series) -> pd.Series:
    """Count of down days in the trailing 21 days, gated to the fourth quarter."""
    down = (_daily_ret(close) < 0).astype(float)
    return _rolling_sum(down, _TD_MON) * _q4_flag(close)


def szd_ext_056_new_low_count_63d_in_q4(close: pd.Series) -> pd.Series:
    """Count of new 21-day lows in the trailing 63 days, gated to the fourth quarter."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    return _rolling_sum(new_low, _TD_QTR) * _q4_flag(close)


def szd_ext_057_consec_days_in_q4_below_sma200(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of close below its 200-day mean, gated to Q4."""
    streak = _consec_streak(close < _rolling_mean(close, 200))
    return streak * _q4_flag(close)


def szd_ext_058_year_low_streak_in_december(close: pd.Series) -> pd.Series:
    """Consecutive-day streak at/near the trailing 252-day low, gated to December."""
    near_low = close <= _rolling_min(close, _TD_YEAR) * 1.03
    streak = _consec_streak(near_low)
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return streak * dec


def szd_ext_059_negative_qtd_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of negative quarter-to-date return."""
    qtd = szd_ext_034_qtd_return(close)
    return _consec_streak(qtd < 0)


def szd_ext_060_down_month_count_in_h2(close: pd.Series) -> pd.Series:
    """Count of down days in the trailing 126 days, gated to the second half-year."""
    down = (_daily_ret(close) < 0).astype(float)
    h2 = _ser((_dtidx(close).month >= 7).astype(float), close)
    return _rolling_sum(down, _TD_HALF) * h2


def szd_ext_061_consec_weak_season_down_streak(close: pd.Series) -> pd.Series:
    """Consecutive down-day streak gated to the Sept-Oct weak season."""
    streak = _consec_streak(_daily_ret(close) < 0)
    weak = _ser(np.isin(_dtidx(close).month, [9, 10]).astype(float), close)
    return streak * weak


def szd_ext_062_new_low_count_252d_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """Count of new 21-day lows in the trailing 252 days, gated to Nov-Dec."""
    new_low = (close <= _rolling_min(close, _TD_MON)).astype(float)
    return _rolling_sum(new_low, _TD_YEAR) * _tax_loss_window(close)


# --- Group F (063-070): Seasonal percentile ranks and z-scores ---

def szd_ext_063_dd_pctile_in_q4(close: pd.Series) -> pd.Series:
    """Percentile rank of the 252-day drawdown over 252 days, gated to Q4."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _rolling_rank_pct(dd, _TD_YEAR) * _q4_flag(close)


def szd_ext_064_dd_pctile_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """Percentile rank of the 252-day drawdown over 252 days, gated to Nov-Dec."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _rolling_rank_pct(dd, _TD_YEAR) * _tax_loss_window(close)


def szd_ext_065_return_zscore_in_december(close: pd.Series) -> pd.Series:
    """Z-score of daily return over 63 days, gated to December."""
    ret = _daily_ret(close)
    z = _safe_div(ret - _rolling_mean(ret, _TD_QTR), _rolling_std(ret, _TD_QTR))
    dec = _ser((_dtidx(close).month == 12).astype(float), close)
    return z * dec


def szd_ext_066_volume_zscore_in_december(volume: pd.Series) -> pd.Series:
    """Z-score of volume over 126 days, gated to December."""
    z = _safe_div(volume - _rolling_mean(volume, _TD_HALF), _rolling_std(volume, _TD_HALF))
    dec = _ser((_dtidx(volume).month == 12).astype(float), volume)
    return z * dec


def szd_ext_067_volume_pctile_in_q4(volume: pd.Series) -> pd.Series:
    """Percentile rank of volume over 252 days, gated to the fourth quarter."""
    return _rolling_rank_pct(volume, _TD_YEAR) * _q4_flag(volume)


def szd_ext_068_loss_pctile_in_tax_loss_window(close: pd.Series) -> pd.Series:
    """Percentile rank of the trailing-year loss over 252 days, gated to Nov-Dec."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return _rolling_rank_pct(loss, _TD_YEAR) * _tax_loss_window(close)


def szd_ext_069_realized_vol_zscore_in_q4(close: pd.Series) -> pd.Series:
    """Z-score of 21-day realized volatility over 252 days, gated to Q4."""
    vol = _rolling_std(_daily_ret(close), _TD_MON)
    z = _safe_div(vol - _rolling_mean(vol, _TD_YEAR), _rolling_std(vol, _TD_YEAR))
    return z * _q4_flag(close)


def szd_ext_070_drawdown_zscore_in_september(close: pd.Series) -> pd.Series:
    """Z-score of the 252-day drawdown over 252 days, gated to September."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    z = _safe_div(dd - _rolling_mean(dd, _TD_YEAR), _rolling_std(dd, _TD_YEAR))
    sep = _ser((_dtidx(close).month == 9).astype(float), close)
    return z * sep


# --- Group G (071-075): Gated composites on fresh window combinations ---

def szd_ext_071_quarter_end_distress_score(close: pd.Series) -> pd.Series:
    """126-day drawdown depth scaled by proximity to the quarter end."""
    dd = _safe_div(_rolling_max(close, _TD_HALF) - close, _rolling_max(close, _TD_HALF))
    prox = (1.0 - _days_to_quarter_end(close) / 21.0).clip(lower=0)
    return dd * prox


def szd_ext_072_summer_capitulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Summer-gated composite: drawdown depth and elevated down-day volume."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return dd * (1.0 + vr) * szd_ext_015_summer_doldrums_flag(close)


def szd_ext_073_weak_season_distress_intensity(close: pd.Series) -> pd.Series:
    """126-day drawdown depth gated to the Sept-Oct weak season."""
    dd = _safe_div(_rolling_max(close, _TD_HALF) - close, _rolling_max(close, _TD_HALF))
    weak = _ser(np.isin(_dtidx(close).month, [9, 10]).astype(float), close)
    return dd * weak


def szd_ext_074_year_end_volume_distress(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day volume ratio weighted by the year-end run-up ramp."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_QTR))
    return vr * szd_ext_026_year_end_runup_ramp(close)


def szd_ext_075_seasonal_distress_composite_ext(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: drawdown depth, quarter-end proximity and down-day volume.
    Higher = deeper distress aligned with the quarter-end window."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    qe_prox = (1.0 - _days_to_quarter_end(close) / 45.0).clip(lower=0)
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return dd * (1.0 + qe_prox) * (1.0 + vr) / 2.0


# ── Registry ──────────────────────────────────────────────────────────────────

SEASONAL_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "szd_ext_001_bimonthly_index": {"inputs": ["close"], "func": szd_ext_001_bimonthly_index},
    "szd_ext_002_half_year_index": {"inputs": ["close"], "func": szd_ext_002_half_year_index},
    "szd_ext_003_third_of_year_index": {"inputs": ["close"], "func": szd_ext_003_third_of_year_index},
    "szd_ext_004_quarter_fraction_elapsed": {"inputs": ["close"], "func": szd_ext_004_quarter_fraction_elapsed},
    "szd_ext_005_month_fraction_elapsed": {"inputs": ["close"], "func": szd_ext_005_month_fraction_elapsed},
    "szd_ext_006_days_to_month_end": {"inputs": ["close"], "func": szd_ext_006_days_to_month_end},
    "szd_ext_007_days_from_month_start": {"inputs": ["close"], "func": szd_ext_007_days_from_month_start},
    "szd_ext_008_quarter_sin": {"inputs": ["close"], "func": szd_ext_008_quarter_sin},
    "szd_ext_009_quarter_cos": {"inputs": ["close"], "func": szd_ext_009_quarter_cos},
    "szd_ext_010_week_of_month": {"inputs": ["close"], "func": szd_ext_010_week_of_month},
    "szd_ext_011_is_leap_year_flag": {"inputs": ["close"], "func": szd_ext_011_is_leap_year_flag},
    "szd_ext_012_days_to_quarter_end_sin": {"inputs": ["close"], "func": szd_ext_012_days_to_quarter_end_sin},
    "szd_ext_013_pre_holiday_year_end_flag": {"inputs": ["close"], "func": szd_ext_013_pre_holiday_year_end_flag},
    "szd_ext_014_early_january_window_flag": {"inputs": ["close"], "func": szd_ext_014_early_january_window_flag},
    "szd_ext_015_summer_doldrums_flag": {"inputs": ["close"], "func": szd_ext_015_summer_doldrums_flag},
    "szd_ext_016_spring_window_flag": {"inputs": ["close"], "func": szd_ext_016_spring_window_flag},
    "szd_ext_017_q3_flag": {"inputs": ["close"], "func": szd_ext_017_q3_flag},
    "szd_ext_018_q2_flag": {"inputs": ["close"], "func": szd_ext_018_q2_flag},
    "szd_ext_019_fiscal_q4_extended_flag": {"inputs": ["close"], "func": szd_ext_019_fiscal_q4_extended_flag},
    "szd_ext_020_mid_quarter_flag": {"inputs": ["close"], "func": szd_ext_020_mid_quarter_flag},
    "szd_ext_021_quarter_end_window_flag": {"inputs": ["close"], "func": szd_ext_021_quarter_end_window_flag},
    "szd_ext_022_quarter_start_window_flag": {"inputs": ["close"], "func": szd_ext_022_quarter_start_window_flag},
    "szd_ext_023_options_expiry_week_flag": {"inputs": ["close"], "func": szd_ext_023_options_expiry_week_flag},
    "szd_ext_024_first_trading_week_flag": {"inputs": ["close"], "func": szd_ext_024_first_trading_week_flag},
    "szd_ext_025_thanksgiving_window_flag": {"inputs": ["close"], "func": szd_ext_025_thanksgiving_window_flag},
    "szd_ext_026_year_end_runup_ramp": {"inputs": ["close"], "func": szd_ext_026_year_end_runup_ramp},
    "szd_ext_027_dd_42d_in_q4": {"inputs": ["close"], "func": szd_ext_027_dd_42d_in_q4},
    "szd_ext_028_dd_126d_in_december": {"inputs": ["close"], "func": szd_ext_028_dd_126d_in_december},
    "szd_ext_029_dd_252d_in_september": {"inputs": ["close"], "func": szd_ext_029_dd_252d_in_september},
    "szd_ext_030_dd_21d_in_quarter_end_window": {"inputs": ["close"], "func": szd_ext_030_dd_21d_in_quarter_end_window},
    "szd_ext_031_loss_63d_in_q4": {"inputs": ["close"], "func": szd_ext_031_loss_63d_in_q4},
    "szd_ext_032_loss_126d_in_tax_loss_window": {"inputs": ["close"], "func": szd_ext_032_loss_126d_in_tax_loss_window},
    "szd_ext_033_dd_504d_in_q4": {"inputs": ["close"], "func": szd_ext_033_dd_504d_in_q4},
    "szd_ext_034_qtd_return": {"inputs": ["close"], "func": szd_ext_034_qtd_return},
    "szd_ext_035_qtd_return_in_q4": {"inputs": ["close"], "func": szd_ext_035_qtd_return_in_q4},
    "szd_ext_036_mtd_return": {"inputs": ["close"], "func": szd_ext_036_mtd_return},
    "szd_ext_037_deep_loser_in_q4_flag": {"inputs": ["close"], "func": szd_ext_037_deep_loser_in_q4_flag},
    "szd_ext_038_dd_x_quarter_end_proximity": {"inputs": ["close"], "func": szd_ext_038_dd_x_quarter_end_proximity},
    "szd_ext_039_summer_drawdown": {"inputs": ["close"], "func": szd_ext_039_summer_drawdown},
    "szd_ext_040_loss_x_year_end_runup": {"inputs": ["close"], "func": szd_ext_040_loss_x_year_end_runup},
    "szd_ext_041_month_of_126d_low": {"inputs": ["close"], "func": szd_ext_041_month_of_126d_low},
    "szd_ext_042_low_126d_in_q4_flag": {"inputs": ["close"], "func": szd_ext_042_low_126d_in_q4_flag},
    "szd_ext_043_quarter_of_63d_low": {"inputs": ["close"], "func": szd_ext_043_quarter_of_63d_low},
    "szd_ext_044_low_252d_in_summer_flag": {"inputs": ["close"], "func": szd_ext_044_low_252d_in_summer_flag},
    "szd_ext_045_low_252d_in_september_flag": {"inputs": ["close"], "func": szd_ext_045_low_252d_in_september_flag},
    "szd_ext_046_day_of_month_of_252d_low": {"inputs": ["close"], "func": szd_ext_046_day_of_month_of_252d_low},
    "szd_ext_047_low_252d_set_at_month_end_flag": {"inputs": ["close"], "func": szd_ext_047_low_252d_set_at_month_end_flag},
    "szd_ext_048_days_since_63d_low": {"inputs": ["close"], "func": szd_ext_048_days_since_63d_low},
    "szd_ext_049_days_since_504d_low": {"inputs": ["close"], "func": szd_ext_049_days_since_504d_low},
    "szd_ext_050_low_month_recency_in_q4": {"inputs": ["close"], "func": szd_ext_050_low_month_recency_in_q4},
    "szd_ext_051_new_lows_in_h2_fraction": {"inputs": ["close"], "func": szd_ext_051_new_lows_in_h2_fraction},
    "szd_ext_052_new_lows_in_summer_fraction": {"inputs": ["close"], "func": szd_ext_052_new_lows_in_summer_fraction},
    "szd_ext_053_consec_down_days_in_q4": {"inputs": ["close"], "func": szd_ext_053_consec_down_days_in_q4},
    "szd_ext_054_consec_down_days_in_tax_loss_window": {"inputs": ["close"], "func": szd_ext_054_consec_down_days_in_tax_loss_window},
    "szd_ext_055_down_day_count_21d_in_q4": {"inputs": ["close"], "func": szd_ext_055_down_day_count_21d_in_q4},
    "szd_ext_056_new_low_count_63d_in_q4": {"inputs": ["close"], "func": szd_ext_056_new_low_count_63d_in_q4},
    "szd_ext_057_consec_days_in_q4_below_sma200": {"inputs": ["close"], "func": szd_ext_057_consec_days_in_q4_below_sma200},
    "szd_ext_058_year_low_streak_in_december": {"inputs": ["close"], "func": szd_ext_058_year_low_streak_in_december},
    "szd_ext_059_negative_qtd_streak": {"inputs": ["close"], "func": szd_ext_059_negative_qtd_streak},
    "szd_ext_060_down_month_count_in_h2": {"inputs": ["close"], "func": szd_ext_060_down_month_count_in_h2},
    "szd_ext_061_consec_weak_season_down_streak": {"inputs": ["close"], "func": szd_ext_061_consec_weak_season_down_streak},
    "szd_ext_062_new_low_count_252d_in_tax_loss_window": {"inputs": ["close"], "func": szd_ext_062_new_low_count_252d_in_tax_loss_window},
    "szd_ext_063_dd_pctile_in_q4": {"inputs": ["close"], "func": szd_ext_063_dd_pctile_in_q4},
    "szd_ext_064_dd_pctile_in_tax_loss_window": {"inputs": ["close"], "func": szd_ext_064_dd_pctile_in_tax_loss_window},
    "szd_ext_065_return_zscore_in_december": {"inputs": ["close"], "func": szd_ext_065_return_zscore_in_december},
    "szd_ext_066_volume_zscore_in_december": {"inputs": ["volume"], "func": szd_ext_066_volume_zscore_in_december},
    "szd_ext_067_volume_pctile_in_q4": {"inputs": ["volume"], "func": szd_ext_067_volume_pctile_in_q4},
    "szd_ext_068_loss_pctile_in_tax_loss_window": {"inputs": ["close"], "func": szd_ext_068_loss_pctile_in_tax_loss_window},
    "szd_ext_069_realized_vol_zscore_in_q4": {"inputs": ["close"], "func": szd_ext_069_realized_vol_zscore_in_q4},
    "szd_ext_070_drawdown_zscore_in_september": {"inputs": ["close"], "func": szd_ext_070_drawdown_zscore_in_september},
    "szd_ext_071_quarter_end_distress_score": {"inputs": ["close"], "func": szd_ext_071_quarter_end_distress_score},
    "szd_ext_072_summer_capitulation_score": {"inputs": ["close", "volume"], "func": szd_ext_072_summer_capitulation_score},
    "szd_ext_073_weak_season_distress_intensity": {"inputs": ["close"], "func": szd_ext_073_weak_season_distress_intensity},
    "szd_ext_074_year_end_volume_distress": {"inputs": ["close", "volume"], "func": szd_ext_074_year_end_volume_distress},
    "szd_ext_075_seasonal_distress_composite_ext": {"inputs": ["close", "volume"], "func": szd_ext_075_seasonal_distress_composite_ext},
}
