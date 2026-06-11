"""
87_insider_timing — Extended Features 001-075
Domain: insider activity timing vs price drawdown depth — additional angles:
        recency-weighted timing, drawdown-percentile conditioned buying,
        velocity/lag of buys vs decline, fresh-low timing, role-specific
        timing, ratio/streak and composite variants not in the base files.
Asset class: US equities | SF2 insider series + daily close price
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
Inputs are (1) daily close price and (2) daily event-aggregated Sharadar SF2
insider transaction series (one row per (ticker, date)).  The insider series
are EVENT-DRIVEN: mostly ZERO on non-filing dates and must NOT be
forward-filled.  They are aggregated via trailing rolling SUMS / COUNTS.

Field names used (lowercase, identical to the folder's base files):
  close, insider_buy_count, insider_buy_value, insider_buyers,
  insider_sell_value, officer_buy_value

All features look strictly backward: drawdowns use trailing rolling /
expanding max of close only.  No negative shifts, no forward peaks.

Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_HALF  = 126
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


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


def _log1p_pos(s: pd.Series) -> pd.Series:
    """Log1p of the non-negative part of a series."""
    return np.log1p(s.clip(lower=0.0))


def _drawdown_from_expanding_high(close: pd.Series) -> pd.Series:
    """Price drawdown from expanding (all-history) high; always <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _drawdown_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    """Price drawdown from rolling w-day high; always <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _price_pct_in_range(close: pd.Series, w: int) -> pd.Series:
    """Position of close within trailing w-day [low, high] range, 0-1."""
    lo = _rolling_min(close, w)
    hi = _rolling_max(close, w)
    return _safe_div(close - lo, (hi - lo).replace(0, np.nan))


def _days_since_last_nonzero(s: pd.Series) -> pd.Series:
    """Backward-only: trading days since the most recent nonzero (>0) value.
    NaN until the first nonzero ever appears."""
    arr = (s.values > 0)
    out = np.full(len(arr), np.nan)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=s.index)


def _streak_true(cond: pd.Series) -> pd.Series:
    """Count of consecutive trailing True values up to each row."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(len(arr)):
        out[i] = (out[i - 1] + 1) * arr[i] if i > 0 else float(arr[i])
    return pd.Series(out, index=cond.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Recency-weighted insider buy timing ---

def itm_ext_001_buy_value_ewm_63(insider_buy_value: pd.Series) -> pd.Series:
    """EWM (span=63) of daily insider buy value — recency-weighted quarterly buying."""
    return _ewm_mean(insider_buy_value, _TD_QTR)


def itm_ext_002_buy_count_ewm_63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM (span=63) of daily insider buy count."""
    return _ewm_mean(insider_buy_count, _TD_QTR)


def itm_ext_003_buy_value_ewm_126(insider_buy_value: pd.Series) -> pd.Series:
    """EWM (span=126) of daily insider buy value — half-year recency weighting."""
    return _ewm_mean(insider_buy_value, _TD_HALF)


def itm_ext_004_ewm_buy_value_x_ath_dd(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """EWM(63) buy value (log1p) times ATH drawdown magnitude — recent timing into decline."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    return _log1p_pos(_ewm_mean(insider_buy_value, _TD_QTR)) * dd_mag


def itm_ext_005_buyers_ewm_63(insider_buyers: pd.Series) -> pd.Series:
    """EWM (span=63) of daily unique insider buyer count."""
    return _ewm_mean(insider_buyers, _TD_QTR)


def itm_ext_006_officer_buy_value_ewm_63(officer_buy_value: pd.Series) -> pd.Series:
    """EWM (span=63) of daily officer buy value — recency-weighted officer buying."""
    return _ewm_mean(officer_buy_value, _TD_QTR)


def itm_ext_007_buy_value_ewm_ratio_21v126(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of EWM(21) buy value to EWM(126) buy value — recent vs slow timing."""
    return _safe_div(_ewm_mean(insider_buy_value, _TD_MON), _ewm_mean(insider_buy_value, _TD_HALF))


def itm_ext_008_ewm_buy_count_x_1y_dd(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """EWM(63) buy count times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    return _ewm_mean(insider_buy_count, _TD_QTR) * dd_mag


def itm_ext_009_buy_value_ewm_42(insider_buy_value: pd.Series) -> pd.Series:
    """EWM (span=42) of daily insider buy value — two-month recency weighting."""
    return _ewm_mean(insider_buy_value, 42)


def itm_ext_010_buy_count_ewm_252(insider_buy_count: pd.Series) -> pd.Series:
    """EWM (span=252) of daily insider buy count — slow annual recency weighting."""
    return _ewm_mean(insider_buy_count, _TD_YEAR)


def itm_ext_011_ewm_net_value_x_ath_dd(close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM(63) net insider value (buy minus sell) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    net = _ewm_mean(insider_buy_value, _TD_QTR) - _ewm_mean(insider_sell_value, _TD_QTR)
    return net * dd_mag


def itm_ext_012_buy_value_ewm_x_dd_pctile(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """EWM(63) buy value (log1p) times (1 - price percentile in 252d range)."""
    depth = 1.0 - _price_pct_in_range(close, _TD_YEAR)
    return _log1p_pos(_ewm_mean(insider_buy_value, _TD_QTR)) * depth


# --- Group B (013-024): Buying conditioned on drawdown percentile / range depth ---

def itm_ext_013_buy_value_in_bottom_quartile_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d sum of buy value occurring while close is in bottom 25% of 252d range."""
    pct = _price_pct_in_range(close, _TD_YEAR)
    deep = insider_buy_value.where(pct <= 0.25, other=0.0)
    return _rolling_sum(deep, _TD_QTR)


def itm_ext_014_buy_count_in_bottom_quartile_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d count of buy days occurring while close is in bottom 25% of 252d range."""
    pct = _price_pct_in_range(close, _TD_YEAR)
    deep = ((pct <= 0.25) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(deep, _TD_QTR)


def itm_ext_015_buy_value_in_bottom_5pct_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """252d sum of buy value occurring while close is in bottom 5% of 252d range."""
    pct = _price_pct_in_range(close, _TD_YEAR)
    deep = insider_buy_value.where(pct <= 0.05, other=0.0)
    return _rolling_sum(deep, _TD_YEAR)


def itm_ext_016_dd_pct_rank_at_buy_mean_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean 252d price percentile on insider-buy days over 63 days (low = deep buying)."""
    pct = _price_pct_in_range(close, _TD_YEAR)
    mask = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(pct * mask, _TD_QTR), _rolling_sum(mask, _TD_QTR))


def itm_ext_017_buy_in_dd_30pct_flag(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """1 on days where stock is >=30% below ATH and an insider buy occurs."""
    dd = _drawdown_from_expanding_high(close)
    return ((dd <= -0.30) & (insider_buy_count > 0)).astype(float)


def itm_ext_018_buy_in_dd_60pct_flag(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """1 on days where stock is >=60% below ATH and an insider buy occurs."""
    dd = _drawdown_from_expanding_high(close)
    return ((dd <= -0.60) & (insider_buy_count > 0)).astype(float)


def itm_ext_019_buy_in_dd_80pct_flag(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """1 on days where stock is >=80% below ATH and an insider buy occurs."""
    dd = _drawdown_from_expanding_high(close)
    return ((dd <= -0.80) & (insider_buy_count > 0)).astype(float)


def itm_ext_020_buy_sum_dd_60pct_window_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """252d count of days with ATH DD >= 60% AND insider buy."""
    dd = _drawdown_from_expanding_high(close)
    deep = ((dd <= -0.60) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(deep, _TD_YEAR)


def itm_ext_021_buy_value_in_dd_30pct_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """252d sum of buy value while stock is >=30% below ATH."""
    dd = _drawdown_from_expanding_high(close)
    return _rolling_sum(insider_buy_value.where(dd <= -0.30, other=0.0), _TD_YEAR)


def itm_ext_022_buy_value_in_2y_dd_50pct_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d sum of buy value while 2-year DD >= 50%."""
    dd = _drawdown_from_rolling_high(close, _TD_2Y)
    return _rolling_sum(insider_buy_value.where(dd <= -0.50, other=0.0), _TD_QTR)


def itm_ext_023_buy_value_bottom_quartile_fraction_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of 252d insider buy value occurring in the bottom quartile of price range."""
    pct = _price_pct_in_range(close, _TD_YEAR)
    deep = insider_buy_value.where(pct <= 0.25, other=0.0)
    return _safe_div(_rolling_sum(deep, _TD_YEAR), _rolling_sum(insider_buy_value, _TD_YEAR))


def itm_ext_024_officer_buy_in_dd_60pct_63d(close: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """63d officer buy value while stock is >=60% below ATH."""
    dd = _drawdown_from_expanding_high(close)
    return _rolling_sum(officer_buy_value.where(dd <= -0.60, other=0.0), _TD_QTR)


# --- Group C (025-036): Timing relative to fresh lows and decline velocity ---

def itm_ext_025_days_since_buy_at_new_252d_low(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Days elapsed since the most recent insider buy that set a new 252-day low."""
    low = _rolling_min(close, _TD_YEAR)
    event = ((close <= low + _EPS) & (insider_buy_count > 0)).astype(float)
    return _days_since_last_nonzero(event)


def itm_ext_026_buy_within_5pct_of_252d_low_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d count of buy days where close is within 5% above the 252d low."""
    low = _rolling_min(close, _TD_YEAR)
    near = ((close <= low * 1.05) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(near, _TD_QTR)


def itm_ext_027_buy_within_5pct_of_ath_low_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """252d count of buy days where close is within 5% above the expanding all-time low."""
    atl = close.expanding(min_periods=1).min()
    near = ((close <= atl * 1.05) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(near, _TD_YEAR)


def itm_ext_028_buy_value_velocity_x_dd(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Buy value acceleration (21d sum minus 63d-mean*21) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    accel = _rolling_sum(insider_buy_value, _TD_MON) - _rolling_mean(insider_buy_value, _TD_QTR) * _TD_MON
    return accel * dd_mag


def itm_ext_029_decline_speed_at_buy_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean 21-day price return on insider-buy days over 63 days (negative = buying into fast decline)."""
    ret21 = _safe_div(close - close.shift(_TD_MON), close.shift(_TD_MON))
    mask = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(ret21 * mask, _TD_QTR), _rolling_sum(mask, _TD_QTR))


def itm_ext_030_buy_after_steep_drop_flag(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """1 on insider-buy days where the trailing 21-day return is below -20%."""
    ret21 = _safe_div(close - close.shift(_TD_MON), close.shift(_TD_MON))
    return ((ret21 <= -0.20) & (insider_buy_count > 0)).astype(float)


def itm_ext_031_buy_after_steep_drop_count_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """252d count of insider-buy days following a trailing 21-day return below -20%."""
    ret21 = _safe_div(close - close.shift(_TD_MON), close.shift(_TD_MON))
    flag = ((ret21 <= -0.20) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def itm_ext_032_dd_worsening_since_last_buy_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """ATH drawdown minus the drawdown rolling-max over the days since last buy proxy (63d)."""
    dd = _drawdown_from_expanding_high(close)
    mask = (insider_buy_count > 0)
    dd_at_buy = dd.where(mask).ffill()
    return dd - dd_at_buy


def itm_ext_033_buy_value_x_decline_velocity_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d buy value (log1p) times absolute trailing 63-day decline magnitude."""
    ret63 = _safe_div(close - close.shift(_TD_QTR), close.shift(_TD_QTR))
    drop = (-ret63).clip(lower=0.0)
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * drop


def itm_ext_034_time_since_deep_dd_buy(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Days since the most recent insider buy occurring with ATH DD >= 50%."""
    dd = _drawdown_from_expanding_high(close)
    event = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    return _days_since_last_nonzero(event)


def itm_ext_035_buy_at_fresh_2y_low_count_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """252d count of buy days that set a new 2-year (504d) closing low."""
    low = _rolling_min(close, _TD_2Y)
    event = ((close <= low + _EPS) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(event, _TD_YEAR)


def itm_ext_036_buy_value_x_drop_from_63d_high(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d buy value (log1p) times magnitude of drawdown from 63d high."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_QTR).abs()
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * dd_mag


# --- Group D (037-048): Role-specific and breadth-conditioned timing ---

def itm_ext_037_officer_buy_value_x_1y_dd(close: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """63d officer buy value (log1p) times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    return _log1p_pos(_rolling_sum(officer_buy_value, _TD_QTR)) * dd_mag


def itm_ext_038_officer_buy_value_252d_x_ath_dd(close: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """252d officer buy value (log1p) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    return _log1p_pos(_rolling_sum(officer_buy_value, _TD_YEAR)) * dd_mag


def itm_ext_039_officer_buy_dd_at_buy_mean_63d(close: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Mean ATH drawdown on officer-buy days (officer_buy_value>0) over 63 days."""
    dd = _drawdown_from_expanding_high(close)
    mask = (officer_buy_value > 0).astype(float)
    return _safe_div(_rolling_sum(dd * mask, _TD_QTR), _rolling_sum(mask, _TD_QTR))


def itm_ext_040_buyers_x_ath_dd_252d(close: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """252d unique buyer count times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    return _rolling_sum(insider_buyers, _TD_YEAR) * dd_mag


def itm_ext_041_buyers_in_deep_dd_50pct_63d(close: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """63d sum of unique buyers on days the stock is >=50% below ATH."""
    dd = _drawdown_from_expanding_high(close)
    return _rolling_sum(insider_buyers.where(dd <= -0.50, other=0.0), _TD_QTR)


def itm_ext_042_multi_buyer_deep_dd_flag(close: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """1 on days with >=2 unique buyers while ATH drawdown >= 50%."""
    dd = _drawdown_from_expanding_high(close)
    return ((insider_buyers >= 2) & (dd <= -0.50)).astype(float)


def itm_ext_043_multi_buyer_deep_dd_count_252d(close: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """252d count of days with >=2 unique buyers while ATH drawdown >= 50%."""
    dd = _drawdown_from_expanding_high(close)
    flag = ((insider_buyers >= 2) & (dd <= -0.50)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def itm_ext_044_officer_fraction_in_deep_dd_63d(close: pd.Series, insider_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """Officer fraction of total buy value, computed only on deep-DD (>=50%) days, 63d."""
    dd = _drawdown_from_expanding_high(close)
    off = _rolling_sum(officer_buy_value.where(dd <= -0.50, other=0.0), _TD_QTR)
    tot = _rolling_sum(insider_buy_value.where(dd <= -0.50, other=0.0), _TD_QTR)
    return _safe_div(off, tot)


def itm_ext_045_buyers_breadth_x_dd_pctile(close: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """63d unique buyers times (1 - price percentile in 252d range)."""
    depth = 1.0 - _price_pct_in_range(close, _TD_YEAR)
    return _rolling_sum(insider_buyers, _TD_QTR) * depth


def itm_ext_046_officer_buy_value_x_drop_velocity(close: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """63d officer buy value (log1p) times absolute 63-day decline magnitude."""
    ret63 = _safe_div(close - close.shift(_TD_QTR), close.shift(_TD_QTR))
    drop = (-ret63).clip(lower=0.0)
    return _log1p_pos(_rolling_sum(officer_buy_value, _TD_QTR)) * drop


def itm_ext_047_days_since_officer_buy(officer_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the most recent officer buy event."""
    return _days_since_last_nonzero(officer_buy_value)


def itm_ext_048_days_since_multi_buyer_day(insider_buyers: pd.Series) -> pd.Series:
    """Days elapsed since the most recent day with >=2 unique insider buyers."""
    return _days_since_last_nonzero((insider_buyers >= 2).astype(float))


# --- Group E (049-060): Streaks, ratios and normalized timing intensity ---

def itm_ext_049_buy_streak_in_dd_50pct(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Consecutive days within an active 63d deep-DD-buying regime (>=1 deep buy in 63d)."""
    dd = _drawdown_from_expanding_high(close)
    deep_buy = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    return _streak_true(_rolling_sum(deep_buy, _TD_QTR) > 0)


def itm_ext_050_consec_quarters_with_deep_buy(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Streak of days where the trailing 63d deep-DD (>=50%) buy count is positive."""
    dd = _drawdown_from_expanding_high(close)
    deep_buy = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    return _streak_true(_rolling_sum(deep_buy, _TD_QTR) >= 1.0)


def itm_ext_051_deep_buy_fraction_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 252d insider buy days that occurred with ATH DD >= 50%."""
    dd = _drawdown_from_expanding_high(close)
    deep = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    allb = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(deep, _TD_YEAR), _rolling_sum(allb, _TD_YEAR))


def itm_ext_052_buy_value_dd_weighted_per_count_63d(close: pd.Series, insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d DD-weighted buy value divided by 63d buy count — DD-weighted per-event size."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val = _rolling_sum(insider_buy_value, _TD_QTR) * dd_mag
    cnt = _rolling_sum(insider_buy_count, _TD_QTR)
    return _safe_div(val, cnt)


def itm_ext_053_buy_value_x_ath_dd_zscore_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Z-score (252d) of (63d buy value log1p times ATH drawdown magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sig = _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * dd_mag
    return _zscore_rolling(sig, _TD_YEAR)


def itm_ext_054_buy_count_x_ath_dd_zscore_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Z-score (252d) of (63d buy count times ATH drawdown magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sig = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    return _zscore_rolling(sig, _TD_YEAR)


def itm_ext_055_buy_value_x_dd_pct_rank_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank (252d) of (63d buy value log1p times ATH drawdown magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    sig = _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * dd_mag
    return _rolling_rank_pct(sig, _TD_YEAR)


def itm_ext_056_deep_buy_value_to_total_ratio_252d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """252d deep-DD (>=50%) buy value as a fraction of total 252d buy value."""
    dd = _drawdown_from_expanding_high(close)
    deep = _rolling_sum(insider_buy_value.where(dd <= -0.50, other=0.0), _TD_YEAR)
    tot = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(deep, tot)


def itm_ext_057_buy_value_dd_product_median_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d rolling median of daily (buy value log1p times ATH drawdown magnitude)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    daily = _log1p_pos(insider_buy_value) * dd_mag
    return _rolling_median(daily, _TD_QTR)


def itm_ext_058_buy_count_x_dd_per_active_day_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d DD-weighted buy count divided by number of active buy days in 63d."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    weighted = _rolling_sum(insider_buy_count * dd_mag, _TD_QTR)
    active = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR)
    return _safe_div(weighted, active)


def itm_ext_059_net_value_dd_weighted_ewm(close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """EWM(63) of daily net insider value times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    net = (insider_buy_value - insider_sell_value) * dd_mag
    return _ewm_mean(net, _TD_QTR)


def itm_ext_060_buy_timing_purity_ratio_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of DD-weighted 63d buy value to raw 63d buy value — average DD depth at buys."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    weighted = _rolling_sum(insider_buy_value * dd_mag, _TD_QTR)
    raw = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(weighted, raw)


# --- Group F (061-075): Multi-horizon, lag and composite timing scores ---

def itm_ext_061_buy_value_x_3y_dd_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d buy value (log1p) times 3-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_3Y).abs()
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * dd_mag


def itm_ext_062_buy_count_x_half_year_dd_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d buy count times 126-day (half-year) drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_HALF).abs()
    return _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag


def itm_ext_063_buy_value_x_ath_dd_21d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """21d buy value (log1p) times ATH drawdown magnitude — fast-window timing."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_MON)) * dd_mag


def itm_ext_064_buy_value_x_ath_dd_126d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """126d buy value (log1p) times ATH drawdown magnitude — half-year window timing."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_HALF)) * dd_mag


def itm_ext_065_dd_change_over_21d_at_buy(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean 21-day change in ATH drawdown on insider-buy days over 63 days."""
    dd = _drawdown_from_expanding_high(close)
    dd_chg = dd - dd.shift(_TD_MON)
    mask = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(dd_chg * mask, _TD_QTR), _rolling_sum(mask, _TD_QTR))


def itm_ext_066_buy_lag_behind_low_63d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Mean (close / 63d-low) on insider-buy days over 63 days (1 = buying exactly at low)."""
    low = _rolling_min(close, _TD_QTR)
    ratio = _safe_div(close, low)
    mask = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(ratio * mask, _TD_QTR), _rolling_sum(mask, _TD_QTR))


def itm_ext_067_buy_value_recency_decay_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of EWM(10) to EWM(63) of buy value — recency-decay timing intensity."""
    return _safe_div(_ewm_mean(insider_buy_value, 10), _ewm_mean(insider_buy_value, _TD_QTR))


def itm_ext_068_buy_count_acceleration_63v252(insider_buy_count: pd.Series) -> pd.Series:
    """63d buy count rate minus 252d buy count rate scaled to 63d (medium-term acceleration)."""
    rate63 = _rolling_sum(insider_buy_count, _TD_QTR)
    rate252 = _rolling_mean(insider_buy_count, _TD_YEAR) * _TD_QTR
    return rate63 - rate252


def itm_ext_069_buy_value_x_dd_streak_length(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d buy value (log1p) times current consecutive-day streak below the 63d SMA."""
    sma = _rolling_mean(close, _TD_QTR)
    streak = _streak_true(close < sma)
    return _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * streak


def itm_ext_070_buy_value_in_below_sma_252_63d(close: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63d sum of buy value on days where close is below the 252-day SMA."""
    sma = _rolling_mean(close, _TD_YEAR)
    return _rolling_sum(insider_buy_value.where(close < sma, other=0.0), _TD_QTR)


def itm_ext_071_buy_count_below_sma_252_fraction_252d(close: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 252d insider buy days occurring below the 252-day SMA."""
    sma = _rolling_mean(close, _TD_YEAR)
    dip = ((close < sma) & (insider_buy_count > 0)).astype(float)
    allb = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(dip, _TD_YEAR), _rolling_sum(allb, _TD_YEAR))


def itm_ext_072_net_buy_dd_weighted_252d(close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """252d net insider value (buy minus sell) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    net = _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)
    return net * dd_mag


def itm_ext_073_buy_value_dd_weighted_x_officer_frac_252d(close: pd.Series, insider_buy_value: pd.Series, officer_buy_value: pd.Series) -> pd.Series:
    """252d composite: buy value (log1p) * ATH DD magnitude * officer fraction of buy value."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    tot = _rolling_sum(insider_buy_value, _TD_YEAR)
    off = _rolling_sum(officer_buy_value, _TD_YEAR)
    frac = _safe_div(off, tot.replace(0, np.nan)).fillna(0.0)
    return _log1p_pos(tot) * dd_mag * frac


def itm_ext_074_extended_timing_zcomposite(close: pd.Series, insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Composite: average of 252d z-scores of (deep-DD buy value), (deep-DD buy count),
    and (bottom-quartile buy value) — extended capitulation-timing score."""
    dd = _drawdown_from_expanding_high(close)
    pct = _price_pct_in_range(close, _TD_YEAR)
    s1 = _log1p_pos(_rolling_sum(insider_buy_value.where(dd <= -0.50, other=0.0), _TD_QTR))
    s2 = _rolling_sum(((dd <= -0.50) & (insider_buy_count > 0)).astype(float), _TD_QTR)
    s3 = _log1p_pos(_rolling_sum(insider_buy_value.where(pct <= 0.25, other=0.0), _TD_QTR))
    z1, z2, z3 = _zscore_rolling(s1, _TD_YEAR), _zscore_rolling(s2, _TD_YEAR), _zscore_rolling(s3, _TD_YEAR)
    cnt = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
    return _safe_div(z1.fillna(0) + z2.fillna(0) + z3.fillna(0), cnt)


def itm_ext_075_capitulation_timing_intensity(close: pd.Series, insider_buy_value: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Capitulation timing intensity: 63d DD-weighted buy value (log1p) plus 63d
    DD-weighted unique buyers, each normalized by its 252d max, summed (higher = more extreme)."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    v = _log1p_pos(_rolling_sum(insider_buy_value, _TD_QTR)) * dd_mag
    b = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    v_norm = _safe_div(v, _rolling_max(v, _TD_YEAR))
    b_norm = _safe_div(b, _rolling_max(b, _TD_YEAR))
    return v_norm.fillna(0.0) + b_norm.fillna(0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_TIMING_EXTENDED_REGISTRY_001_075 = {
    "itm_ext_001_buy_value_ewm_63": {"inputs": ["insider_buy_value"], "func": itm_ext_001_buy_value_ewm_63},
    "itm_ext_002_buy_count_ewm_63": {"inputs": ["insider_buy_count"], "func": itm_ext_002_buy_count_ewm_63},
    "itm_ext_003_buy_value_ewm_126": {"inputs": ["insider_buy_value"], "func": itm_ext_003_buy_value_ewm_126},
    "itm_ext_004_ewm_buy_value_x_ath_dd": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_004_ewm_buy_value_x_ath_dd},
    "itm_ext_005_buyers_ewm_63": {"inputs": ["insider_buyers"], "func": itm_ext_005_buyers_ewm_63},
    "itm_ext_006_officer_buy_value_ewm_63": {"inputs": ["officer_buy_value"], "func": itm_ext_006_officer_buy_value_ewm_63},
    "itm_ext_007_buy_value_ewm_ratio_21v126": {"inputs": ["insider_buy_value"], "func": itm_ext_007_buy_value_ewm_ratio_21v126},
    "itm_ext_008_ewm_buy_count_x_1y_dd": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_008_ewm_buy_count_x_1y_dd},
    "itm_ext_009_buy_value_ewm_42": {"inputs": ["insider_buy_value"], "func": itm_ext_009_buy_value_ewm_42},
    "itm_ext_010_buy_count_ewm_252": {"inputs": ["insider_buy_count"], "func": itm_ext_010_buy_count_ewm_252},
    "itm_ext_011_ewm_net_value_x_ath_dd": {"inputs": ["close", "insider_buy_value", "insider_sell_value"], "func": itm_ext_011_ewm_net_value_x_ath_dd},
    "itm_ext_012_buy_value_ewm_x_dd_pctile": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_012_buy_value_ewm_x_dd_pctile},
    "itm_ext_013_buy_value_in_bottom_quartile_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_013_buy_value_in_bottom_quartile_63d},
    "itm_ext_014_buy_count_in_bottom_quartile_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_014_buy_count_in_bottom_quartile_63d},
    "itm_ext_015_buy_value_in_bottom_5pct_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_015_buy_value_in_bottom_5pct_252d},
    "itm_ext_016_dd_pct_rank_at_buy_mean_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_016_dd_pct_rank_at_buy_mean_63d},
    "itm_ext_017_buy_in_dd_30pct_flag": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_017_buy_in_dd_30pct_flag},
    "itm_ext_018_buy_in_dd_60pct_flag": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_018_buy_in_dd_60pct_flag},
    "itm_ext_019_buy_in_dd_80pct_flag": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_019_buy_in_dd_80pct_flag},
    "itm_ext_020_buy_sum_dd_60pct_window_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_020_buy_sum_dd_60pct_window_252d},
    "itm_ext_021_buy_value_in_dd_30pct_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_021_buy_value_in_dd_30pct_252d},
    "itm_ext_022_buy_value_in_2y_dd_50pct_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_022_buy_value_in_2y_dd_50pct_63d},
    "itm_ext_023_buy_value_bottom_quartile_fraction_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_023_buy_value_bottom_quartile_fraction_252d},
    "itm_ext_024_officer_buy_in_dd_60pct_63d": {"inputs": ["close", "officer_buy_value"], "func": itm_ext_024_officer_buy_in_dd_60pct_63d},
    "itm_ext_025_days_since_buy_at_new_252d_low": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_025_days_since_buy_at_new_252d_low},
    "itm_ext_026_buy_within_5pct_of_252d_low_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_026_buy_within_5pct_of_252d_low_63d},
    "itm_ext_027_buy_within_5pct_of_ath_low_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_027_buy_within_5pct_of_ath_low_252d},
    "itm_ext_028_buy_value_velocity_x_dd": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_028_buy_value_velocity_x_dd},
    "itm_ext_029_decline_speed_at_buy_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_029_decline_speed_at_buy_63d},
    "itm_ext_030_buy_after_steep_drop_flag": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_030_buy_after_steep_drop_flag},
    "itm_ext_031_buy_after_steep_drop_count_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_031_buy_after_steep_drop_count_252d},
    "itm_ext_032_dd_worsening_since_last_buy_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_032_dd_worsening_since_last_buy_63d},
    "itm_ext_033_buy_value_x_decline_velocity_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_033_buy_value_x_decline_velocity_63d},
    "itm_ext_034_time_since_deep_dd_buy": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_034_time_since_deep_dd_buy},
    "itm_ext_035_buy_at_fresh_2y_low_count_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_035_buy_at_fresh_2y_low_count_252d},
    "itm_ext_036_buy_value_x_drop_from_63d_high": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_036_buy_value_x_drop_from_63d_high},
    "itm_ext_037_officer_buy_value_x_1y_dd": {"inputs": ["close", "officer_buy_value"], "func": itm_ext_037_officer_buy_value_x_1y_dd},
    "itm_ext_038_officer_buy_value_252d_x_ath_dd": {"inputs": ["close", "officer_buy_value"], "func": itm_ext_038_officer_buy_value_252d_x_ath_dd},
    "itm_ext_039_officer_buy_dd_at_buy_mean_63d": {"inputs": ["close", "officer_buy_value"], "func": itm_ext_039_officer_buy_dd_at_buy_mean_63d},
    "itm_ext_040_buyers_x_ath_dd_252d": {"inputs": ["close", "insider_buyers"], "func": itm_ext_040_buyers_x_ath_dd_252d},
    "itm_ext_041_buyers_in_deep_dd_50pct_63d": {"inputs": ["close", "insider_buyers"], "func": itm_ext_041_buyers_in_deep_dd_50pct_63d},
    "itm_ext_042_multi_buyer_deep_dd_flag": {"inputs": ["close", "insider_buyers"], "func": itm_ext_042_multi_buyer_deep_dd_flag},
    "itm_ext_043_multi_buyer_deep_dd_count_252d": {"inputs": ["close", "insider_buyers"], "func": itm_ext_043_multi_buyer_deep_dd_count_252d},
    "itm_ext_044_officer_fraction_in_deep_dd_63d": {"inputs": ["close", "insider_buy_value", "officer_buy_value"], "func": itm_ext_044_officer_fraction_in_deep_dd_63d},
    "itm_ext_045_buyers_breadth_x_dd_pctile": {"inputs": ["close", "insider_buyers"], "func": itm_ext_045_buyers_breadth_x_dd_pctile},
    "itm_ext_046_officer_buy_value_x_drop_velocity": {"inputs": ["close", "officer_buy_value"], "func": itm_ext_046_officer_buy_value_x_drop_velocity},
    "itm_ext_047_days_since_officer_buy": {"inputs": ["officer_buy_value"], "func": itm_ext_047_days_since_officer_buy},
    "itm_ext_048_days_since_multi_buyer_day": {"inputs": ["insider_buyers"], "func": itm_ext_048_days_since_multi_buyer_day},
    "itm_ext_049_buy_streak_in_dd_50pct": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_049_buy_streak_in_dd_50pct},
    "itm_ext_050_consec_quarters_with_deep_buy": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_050_consec_quarters_with_deep_buy},
    "itm_ext_051_deep_buy_fraction_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_051_deep_buy_fraction_252d},
    "itm_ext_052_buy_value_dd_weighted_per_count_63d": {"inputs": ["close", "insider_buy_value", "insider_buy_count"], "func": itm_ext_052_buy_value_dd_weighted_per_count_63d},
    "itm_ext_053_buy_value_x_ath_dd_zscore_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_053_buy_value_x_ath_dd_zscore_252d},
    "itm_ext_054_buy_count_x_ath_dd_zscore_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_054_buy_count_x_ath_dd_zscore_252d},
    "itm_ext_055_buy_value_x_dd_pct_rank_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_055_buy_value_x_dd_pct_rank_252d},
    "itm_ext_056_deep_buy_value_to_total_ratio_252d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_056_deep_buy_value_to_total_ratio_252d},
    "itm_ext_057_buy_value_dd_product_median_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_057_buy_value_dd_product_median_63d},
    "itm_ext_058_buy_count_x_dd_per_active_day_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_058_buy_count_x_dd_per_active_day_63d},
    "itm_ext_059_net_value_dd_weighted_ewm": {"inputs": ["close", "insider_buy_value", "insider_sell_value"], "func": itm_ext_059_net_value_dd_weighted_ewm},
    "itm_ext_060_buy_timing_purity_ratio_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_060_buy_timing_purity_ratio_63d},
    "itm_ext_061_buy_value_x_3y_dd_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_061_buy_value_x_3y_dd_63d},
    "itm_ext_062_buy_count_x_half_year_dd_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_062_buy_count_x_half_year_dd_63d},
    "itm_ext_063_buy_value_x_ath_dd_21d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_063_buy_value_x_ath_dd_21d},
    "itm_ext_064_buy_value_x_ath_dd_126d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_064_buy_value_x_ath_dd_126d},
    "itm_ext_065_dd_change_over_21d_at_buy": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_065_dd_change_over_21d_at_buy},
    "itm_ext_066_buy_lag_behind_low_63d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_066_buy_lag_behind_low_63d},
    "itm_ext_067_buy_value_recency_decay_63d": {"inputs": ["insider_buy_value"], "func": itm_ext_067_buy_value_recency_decay_63d},
    "itm_ext_068_buy_count_acceleration_63v252": {"inputs": ["insider_buy_count"], "func": itm_ext_068_buy_count_acceleration_63v252},
    "itm_ext_069_buy_value_x_dd_streak_length": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_069_buy_value_x_dd_streak_length},
    "itm_ext_070_buy_value_in_below_sma_252_63d": {"inputs": ["close", "insider_buy_value"], "func": itm_ext_070_buy_value_in_below_sma_252_63d},
    "itm_ext_071_buy_count_below_sma_252_fraction_252d": {"inputs": ["close", "insider_buy_count"], "func": itm_ext_071_buy_count_below_sma_252_fraction_252d},
    "itm_ext_072_net_buy_dd_weighted_252d": {"inputs": ["close", "insider_buy_value", "insider_sell_value"], "func": itm_ext_072_net_buy_dd_weighted_252d},
    "itm_ext_073_buy_value_dd_weighted_x_officer_frac_252d": {"inputs": ["close", "insider_buy_value", "officer_buy_value"], "func": itm_ext_073_buy_value_dd_weighted_x_officer_frac_252d},
    "itm_ext_074_extended_timing_zcomposite": {"inputs": ["close", "insider_buy_value", "insider_buy_count"], "func": itm_ext_074_extended_timing_zcomposite},
    "itm_ext_075_capitulation_timing_intensity": {"inputs": ["close", "insider_buy_value", "insider_buyers"], "func": itm_ext_075_capitulation_timing_intensity},
}
