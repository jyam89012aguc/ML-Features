"""
87_insider_timing — Base Features 001-075 (extended to 100)
Domain: insider activity timing vs price drawdown depth
Asset class: US equities | SF2 insider series + daily close price
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
Inputs are:
  (1) daily close price (standard daily closing price)
  (2) daily event-aggregated Sharadar SF2 insider transaction series, one row
      per (ticker, date).  These series are EVENT-DRIVEN: they are mostly ZERO
      on non-filing dates and must NOT be forward-filled.  They are aggregated
      with trailing rolling SUMS over various windows to capture accumulation.

Available field names (lowercase):
  close, insider_buy_count, insider_sell_count, insider_buy_shares,
  insider_sell_shares, insider_buy_value, insider_sell_value,
  insider_buyers, insider_sellers, officer_buy_value, ceo_buy_value,
  cfo_buy_value, insider_shares_held

Primary fields for this folder:
  close, insider_buy_count, insider_buy_value, insider_buyers,
  insider_sell_value, officer_buy_value

All feature functions look strictly backward: drawdown uses trailing
rolling/expanding max of close only.  No negative shifts, no forward peaks.
Every function must return a same-length pandas Series with no exception even
when all insider series inputs are zero.

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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _drawdown_from_expanding_high(close: pd.Series) -> pd.Series:
    """Price drawdown from expanding (all-history) high; always <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _drawdown_from_rolling_high(close: pd.Series, w: int) -> pd.Series:
    """Price drawdown from rolling w-day high; always <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Insider buy count/value conditioned on drawdown depth ---

def itm_001_buy_count_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider buy transaction count."""
    return _rolling_sum(insider_buy_count, _TD_MON)


def itm_002_buy_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider buy transaction count."""
    return _rolling_sum(insider_buy_count, _TD_QTR)


def itm_003_buy_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider buy transaction count."""
    return _rolling_sum(insider_buy_count, _TD_YEAR)


def itm_004_buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider buy dollar value."""
    return _rolling_sum(insider_buy_value, _TD_MON)


def itm_005_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider buy dollar value."""
    return _rolling_sum(insider_buy_value, _TD_QTR)


def itm_006_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider buy dollar value."""
    return _rolling_sum(insider_buy_value, _TD_YEAR)


def itm_007_buy_count_21d_x_ath_dd(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """21-day insider buy count multiplied by ATH drawdown depth magnitude.
    Higher when insiders buy deeper into a decline."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    buy21  = _rolling_sum(insider_buy_count, _TD_MON)
    return buy21 * dd_mag


def itm_008_buy_count_63d_x_ath_dd(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day insider buy count multiplied by ATH drawdown depth magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    return buy63 * dd_mag


def itm_009_buy_value_21d_x_ath_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """21-day insider buy value (log-scaled) times ATH drawdown magnitude."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    buy_val  = _rolling_sum(insider_buy_value, _TD_MON)
    log_val  = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_010_buy_value_63d_x_ath_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day insider buy value (log-scaled) times ATH drawdown magnitude."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    buy_val  = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val  = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_011_buy_value_63d_x_1y_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day insider buy value (log) times 1-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_012_buy_count_63d_x_1y_dd(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day insider buy count times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    return buy63 * dd_mag


def itm_013_officer_buy_value_63d_x_ath_dd(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """Officer-only 63-day buy value (log) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov      = _rolling_sum(officer_buy_value, _TD_QTR)
    log_val = np.log1p(ov.clip(lower=0))
    return log_val * dd_mag


def itm_014_buy_value_252d_x_ath_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """252-day insider buy value (log) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_YEAR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_015_buyers_63d_x_ath_dd(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """Unique insider buyer count (63d sum) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    buyers  = _rolling_sum(insider_buyers, _TD_QTR)
    return buyers * dd_mag


# --- Group B (016-030): Drawdown depth at which insiders buy (conditional flags) ---

def itm_016_buy_in_deep_dd_50pct_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on any day where stock is >=50% below ATH and an insider buy occurs."""
    dd        = _drawdown_from_expanding_high(close)
    deep_flag = (dd <= -0.50).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return deep_flag * buy_flag


def itm_017_buy_in_deep_dd_70pct_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on days where stock is >=70% below ATH and an insider buy occurs."""
    dd        = _drawdown_from_expanding_high(close)
    deep_flag = (dd <= -0.70).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return deep_flag * buy_flag


def itm_018_buy_in_deep_dd_90pct_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on days where stock is >=90% below ATH and an insider buy occurs."""
    dd        = _drawdown_from_expanding_high(close)
    deep_flag = (dd <= -0.90).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return deep_flag * buy_flag


def itm_019_buy_sum_50pct_dd_window_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day rolling count of days with both ATH DD >= 50% AND insider buy."""
    dd        = _drawdown_from_expanding_high(close)
    deep_buy  = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(deep_buy, _TD_QTR)


def itm_020_buy_sum_70pct_dd_window_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day rolling count of days with ATH DD >= 70% AND insider buy."""
    dd       = _drawdown_from_expanding_high(close)
    deep_buy = ((dd <= -0.70) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(deep_buy, _TD_QTR)


def itm_021_buy_sum_50pct_dd_window_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """252-day rolling count of days with ATH DD >= 50% AND insider buy."""
    dd       = _drawdown_from_expanding_high(close)
    deep_buy = ((dd <= -0.50) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(deep_buy, _TD_YEAR)


def itm_022_buy_value_in_50pct_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day sum of insider buy value occurring while stock is >=50% below ATH."""
    dd       = _drawdown_from_expanding_high(close)
    deep_val = insider_buy_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(deep_val, _TD_QTR)


def itm_023_buy_value_in_70pct_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day sum of insider buy value while stock is >=70% below ATH."""
    dd       = _drawdown_from_expanding_high(close)
    deep_val = insider_buy_value.where(dd <= -0.70, other=0.0)
    return _rolling_sum(deep_val, _TD_QTR)


def itm_024_buy_value_in_1y_dd_50pct_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day insider buy value occurring while 1-year DD >= 50%."""
    dd       = _drawdown_from_rolling_high(close, _TD_YEAR)
    deep_val = insider_buy_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(deep_val, _TD_QTR)


def itm_025_officer_buy_in_deep_dd_50pct_63d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63-day officer buy value while stock is >=50% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    ov_deep = officer_buy_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(ov_deep, _TD_QTR)


def itm_026_dd_at_buy_mean_21d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Mean ATH drawdown depth on insider-buy days over trailing 21 days."""
    dd       = _drawdown_from_expanding_high(close)
    buy_mask = (insider_buy_count > 0).astype(float)
    dd_buy   = dd * buy_mask
    sum_dd   = _rolling_sum(dd_buy, _TD_MON)
    n_buys   = _rolling_sum(buy_mask, _TD_MON)
    return _safe_div(sum_dd, n_buys)


def itm_027_dd_at_buy_mean_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Mean ATH drawdown depth on insider-buy days over trailing 63 days."""
    dd       = _drawdown_from_expanding_high(close)
    buy_mask = (insider_buy_count > 0).astype(float)
    dd_buy   = dd * buy_mask
    sum_dd   = _rolling_sum(dd_buy, _TD_QTR)
    n_buys   = _rolling_sum(buy_mask, _TD_QTR)
    return _safe_div(sum_dd, n_buys)


def itm_028_dd_at_buy_mean_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Mean ATH drawdown depth on insider-buy days over trailing 252 days."""
    dd       = _drawdown_from_expanding_high(close)
    buy_mask = (insider_buy_count > 0).astype(float)
    dd_buy   = dd * buy_mask
    sum_dd   = _rolling_sum(dd_buy, _TD_YEAR)
    n_buys   = _rolling_sum(buy_mask, _TD_YEAR)
    return _safe_div(sum_dd, n_buys)


def itm_029_dd_at_buy_worst_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Most extreme (minimum) ATH drawdown on a buy day in trailing 63 days."""
    dd       = _drawdown_from_expanding_high(close)
    buy_mask = (insider_buy_count > 0).astype(float)
    dd_buy   = dd.where(buy_mask > 0, other=0.0)
    return _rolling_min(dd_buy, _TD_QTR)


def itm_030_dd_at_buy_worst_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Most extreme ATH drawdown on a buy day in trailing 252 days."""
    dd       = _drawdown_from_expanding_high(close)
    buy_mask = (insider_buy_count > 0).astype(float)
    dd_buy   = dd.where(buy_mask > 0, other=0.0)
    return _rolling_min(dd_buy, _TD_YEAR)


# --- Group C (031-045): Buy intensity scaled by drawdown depth ---

def itm_031_buy_value_per_dd_unit_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day buy value divided by current ATH drawdown magnitude.
    Measures buy conviction relative to how deep the decline is."""
    dd_mag  = _drawdown_from_expanding_high(close).abs().replace(0, np.nan)
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(buy_val, dd_mag)


def itm_032_buy_count_per_dd_unit_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day buy count divided by current ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs().replace(0, np.nan)
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    return _safe_div(buy63, dd_mag)


def itm_033_buy_value_dd_product_21d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Weighted product: 21d buy value log times 1y drawdown depth (absolute)."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_MON)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_034_buy_value_dd_product_252d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Weighted product: 252d buy value log times ATH drawdown depth."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_YEAR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_035_officer_buy_dd_product_63d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63d officer buy value (log) times ATH drawdown magnitude (product)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    ov      = _rolling_sum(officer_buy_value, _TD_QTR)
    log_val = np.log1p(ov.clip(lower=0))
    return log_val * dd_mag


def itm_036_buy_value_scaled_by_1y_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value divided by 1-year drawdown magnitude — inverse scaling."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_YEAR).abs().replace(0, np.nan)
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(buy_val, dd_mag)


def itm_037_buyers_x_dd_depth_63d(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """Unique buyers (63d) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    buyers  = _rolling_sum(insider_buyers, _TD_QTR)
    return buyers * dd_mag


def itm_038_buy_value_x_log_dd_depth_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log) times log of 1 + ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    log_dd  = np.log1p(dd_mag)
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * log_dd


def itm_039_buy_value_x_dd2_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log) times square of ATH drawdown magnitude (convex weighting)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * (dd_mag ** 2)


def itm_040_buy_count_x_2y_dd_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63d insider buy count times 2-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    buy63  = _rolling_sum(insider_buy_count, _TD_QTR)
    return buy63 * dd_mag


def itm_041_buy_value_x_2y_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log) times 2-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_042_buy_value_x_3y_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d buy value (log) times 3-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_3Y).abs()
    buy_val = _rolling_sum(insider_buy_value, _TD_QTR)
    log_val = np.log1p(buy_val.clip(lower=0))
    return log_val * dd_mag


def itm_043_officer_buy_x_2y_dd_63d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """63d officer buy value (log) times 2-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_2Y).abs()
    ov      = _rolling_sum(officer_buy_value, _TD_QTR)
    log_val = np.log1p(ov.clip(lower=0))
    return log_val * dd_mag


def itm_044_buy_value_dd_ratio_vs_sell_63d(
    close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """(63d buy value * ATH DD magnitude) divided by (63d sell value + 1)."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    buy_val  = _rolling_sum(insider_buy_value, _TD_QTR)
    sell_val = _rolling_sum(insider_sell_value, _TD_QTR)
    numer    = np.log1p(buy_val.clip(lower=0)) * dd_mag
    denom    = np.log1p(sell_val.clip(lower=0)) + 1.0
    return _safe_div(numer, denom)


def itm_045_net_buy_x_ath_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63d net buy value (buy minus sell) times ATH drawdown magnitude."""
    dd_mag   = _drawdown_from_expanding_high(close).abs()
    net_val  = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return net_val * dd_mag


# --- Group D (046-060): Buying-the-dip vs buying-strength classification ---

def itm_046_is_buying_dip_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on days where price is below 63d SMA AND insider buys; 0 otherwise."""
    sma63     = _rolling_mean(close, _TD_QTR)
    dip_flag  = (close < sma63).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return dip_flag * buy_flag


def itm_047_is_buying_strength_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on days where price is above 63d SMA AND insider buys (buying strength)."""
    sma63      = _rolling_mean(close, _TD_QTR)
    str_flag   = (close >= sma63).astype(float)
    buy_flag   = (insider_buy_count > 0).astype(float)
    return str_flag * buy_flag


def itm_048_dip_buy_fraction_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Fraction of insider buy days in 63d window that occurred below 63d SMA."""
    sma63     = _rolling_mean(close, _TD_QTR)
    dip_buy   = ((close < sma63) & (insider_buy_count > 0)).astype(float)
    all_buy   = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(dip_buy, _TD_QTR), _rolling_sum(all_buy, _TD_QTR))


def itm_049_dip_buy_fraction_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Fraction of insider buy days in 252d window that occurred below 252d SMA."""
    sma252    = _rolling_mean(close, _TD_YEAR)
    dip_buy   = ((close < sma252) & (insider_buy_count > 0)).astype(float)
    all_buy   = (insider_buy_count > 0).astype(float)
    return _safe_div(_rolling_sum(dip_buy, _TD_YEAR), _rolling_sum(all_buy, _TD_YEAR))


def itm_050_buy_below_1y_low_plus10pct(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Days where close is within 10% above the 252d low AND insider buy occurs."""
    low_1y    = _rolling_min(close, _TD_YEAR)
    near_low  = (close <= low_1y * 1.10).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return near_low * buy_flag


def itm_051_buy_near_ath_low_plus10pct(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Days where close is within 10% above the expanding all-time low AND insider buys."""
    atl       = close.expanding(min_periods=1).min()
    near_atl  = (close <= atl * 1.10).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return near_atl * buy_flag


def itm_052_dip_buy_count_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """63-day sum of insider buy days that occurred below the 63d SMA."""
    sma63   = _rolling_mean(close, _TD_QTR)
    dip_buy = ((close < sma63) & (insider_buy_count > 0)).astype(float)
    return _rolling_sum(dip_buy, _TD_QTR)


def itm_053_dip_buy_value_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63-day sum of insider buy value on days below 63d SMA."""
    sma63   = _rolling_mean(close, _TD_QTR)
    dip_val = insider_buy_value.where(close < sma63, other=0.0)
    return _rolling_sum(dip_val, _TD_QTR)


def itm_054_dip_buy_value_252d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """252-day sum of insider buy value on days below 252d SMA."""
    sma252  = _rolling_mean(close, _TD_YEAR)
    dip_val = insider_buy_value.where(close < sma252, other=0.0)
    return _rolling_sum(dip_val, _TD_YEAR)


def itm_055_buy_at_new_low_flag(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """1 on days that set a new 252-day closing low AND an insider buy occurs."""
    low_252   = _rolling_min(close, _TD_YEAR)
    new_low   = (close == low_252).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return new_low * buy_flag


def itm_056_buy_at_new_52w_low_count_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """252-day rolling count of days where 52-week low was set and insider bought."""
    low_252   = _rolling_min(close, _TD_YEAR)
    new_low   = (close == low_252).astype(float)
    buy_flag  = (insider_buy_count > 0).astype(float)
    return _rolling_sum(new_low * buy_flag, _TD_YEAR)


def itm_057_buy_price_vs_1y_high_ratio_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Mean of (close / 1y high) on insider-buy days over 63 days.
    Low value = insiders buying deep in the drawdown."""
    hi_1y    = _rolling_max(close, _TD_YEAR)
    ratio    = _safe_div(close, hi_1y)
    buy_mask = (insider_buy_count > 0).astype(float)
    r_buy    = ratio * buy_mask
    n_buys   = _rolling_sum(buy_mask, _TD_QTR)
    sum_r    = _rolling_sum(r_buy, _TD_QTR)
    return _safe_div(sum_r, n_buys)


def itm_058_buy_price_vs_ath_ratio_63d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Mean of (close / ATH) on insider-buy days over 63 days."""
    ath      = close.expanding(min_periods=1).max()
    ratio    = _safe_div(close, ath)
    buy_mask = (insider_buy_count > 0).astype(float)
    r_buy    = ratio * buy_mask
    n_buys   = _rolling_sum(buy_mask, _TD_QTR)
    sum_r    = _rolling_sum(r_buy, _TD_QTR)
    return _safe_div(sum_r, n_buys)


def itm_059_buy_days_in_bottom_decile_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """252d count of insider buy days where close was in the bottom 10th percentile
    of the trailing 252d price range."""
    lo    = _rolling_min(close, _TD_YEAR)
    hi    = _rolling_max(close, _TD_YEAR)
    range_= (hi - lo).replace(0, np.nan)
    pct   = _safe_div(close - lo, range_)
    bot   = (pct <= 0.10).astype(float)
    buy   = (insider_buy_count > 0).astype(float)
    return _rolling_sum(bot * buy, _TD_YEAR)


def itm_060_buy_value_bottom_decile_fraction_252d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Fraction of 252d insider buy value that occurred in the bottom price decile."""
    lo      = _rolling_min(close, _TD_YEAR)
    hi      = _rolling_max(close, _TD_YEAR)
    range_  = (hi - lo).replace(0, np.nan)
    pct     = _safe_div(close - lo, range_)
    bot_val = insider_buy_value.where(pct <= 0.10, other=0.0)
    total_val = _rolling_sum(insider_buy_value, _TD_YEAR)
    bot_sum   = _rolling_sum(bot_val, _TD_YEAR)
    return _safe_div(bot_sum, total_val)


# --- Group E (061-075): Lag, acceleration, and net sentiment features ---

def itm_061_days_since_last_buy(insider_buy_count: pd.Series) -> pd.Series:
    """Days elapsed since the most recent insider buy event (bounded 252d lookback)."""
    buy_flag = (insider_buy_count > 0).astype(float)
    arr      = buy_flag.values.copy()
    out      = np.full(len(arr), np.nan)
    last     = np.nan
    for i in range(len(arr)):
        if arr[i] > 0:
            last   = i
            out[i] = 0.0
        elif not np.isnan(last):
            out[i] = float(i - last)
    return pd.Series(out, index=insider_buy_count.index)


def itm_062_dd_change_since_last_buy(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """Change in ATH drawdown since the most recent insider buy day.
    Positive means drawdown worsened (more negative) after the buy."""
    dd       = _drawdown_from_expanding_high(close)
    buy_flag = (insider_buy_count > 0).astype(float)
    buy_vals = dd.values.copy()
    out      = np.full(len(buy_vals), np.nan)
    last_dd  = np.nan
    for i in range(len(buy_vals)):
        if buy_flag.values[i] > 0:
            last_dd  = buy_vals[i]
            out[i]   = 0.0
        elif not np.isnan(last_dd):
            out[i]   = buy_vals[i] - last_dd
    return pd.Series(out, index=close.index)


def itm_063_buy_count_acceleration_21d_63d(
    insider_buy_count: pd.Series
) -> pd.Series:
    """Buy count 21d rolling sum minus 63d rolling mean scaled to 21d; measures buy acceleration."""
    buy21  = _rolling_sum(insider_buy_count, _TD_MON)
    buy63m = _rolling_mean(insider_buy_count, _TD_QTR) * _TD_MON
    return buy21 - buy63m


def itm_064_buy_value_acceleration_21d_63d(
    insider_buy_value: pd.Series
) -> pd.Series:
    """Buy value 21d sum minus 63d mean*21; measures buy value acceleration."""
    val21  = _rolling_sum(insider_buy_value, _TD_MON)
    val63m = _rolling_mean(insider_buy_value, _TD_QTR) * _TD_MON
    return val21 - val63m


def itm_065_sell_to_buy_value_ratio_63d(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63d sell value divided by 63d buy value (high = net selling pressure)."""
    buy63  = _rolling_sum(insider_buy_value, _TD_QTR)
    sell63 = _rolling_sum(insider_sell_value, _TD_QTR)
    return _safe_div(sell63, buy63)


def itm_066_net_buy_value_63d(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63-day net insider buy value (buy minus sell)."""
    return _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)


def itm_067_net_buy_value_252d(
    insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """252-day net insider buy value."""
    return _rolling_sum(insider_buy_value, _TD_YEAR) - _rolling_sum(insider_sell_value, _TD_YEAR)


def itm_068_buy_count_zscore_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of daily insider buy count within trailing 252-day window."""
    return _zscore_rolling(insider_buy_count, _TD_YEAR)


def itm_069_buy_value_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily insider buy value within trailing 252-day window."""
    return _zscore_rolling(insider_buy_value, _TD_YEAR)


def itm_070_buy_value_ewm_21(insider_buy_value: pd.Series) -> pd.Series:
    """Exponentially weighted mean of insider buy value with span=21."""
    return _ewm_mean(insider_buy_value, _TD_MON)


def itm_071_buy_count_pct_rank_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily buy count within trailing 252-day window."""
    return _rolling_rank_pct(insider_buy_count, _TD_YEAR)


def itm_072_officer_buy_value_63d(officer_buy_value: pd.Series) -> pd.Series:
    """63-day rolling sum of officer-level insider buy value."""
    return _rolling_sum(officer_buy_value, _TD_QTR)


def itm_073_officer_buy_fraction_of_total_63d(
    insider_buy_value: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """Officer buy value as fraction of total insider buy value (63d window)."""
    tot63 = _rolling_sum(insider_buy_value, _TD_QTR)
    off63 = _rolling_sum(officer_buy_value, _TD_QTR)
    return _safe_div(off63, tot63)


def itm_074_buy_value_x_ath_dd_x_officer_fraction_63d(
    close: pd.Series, insider_buy_value: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """Composite: 63d buy value (log) * ATH DD magnitude * officer fraction."""
    dd_mag    = _drawdown_from_expanding_high(close).abs()
    tot63     = _rolling_sum(insider_buy_value, _TD_QTR)
    off63     = _rolling_sum(officer_buy_value, _TD_QTR)
    off_frac  = _safe_div(off63, tot63.replace(0, np.nan)).fillna(0.0)
    log_val   = np.log1p(tot63.clip(lower=0))
    return log_val * dd_mag * off_frac


def itm_075_composite_insider_timing_score(
    close: pd.Series, insider_buy_value: pd.Series,
    insider_buy_count: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """Composite insider timing score: equal-weight z-scores of
    (63d buy value x ATH DD mag), (63d buy count x ATH DD mag),
    (63d unique buyers x ATH DD mag) — all normalized over 252d window."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    s1 = np.log1p(_rolling_sum(insider_buy_value, _TD_QTR).clip(lower=0)) * dd_mag
    s2 = _rolling_sum(insider_buy_count, _TD_QTR) * dd_mag
    s3 = _rolling_sum(insider_buyers, _TD_QTR) * dd_mag
    z1 = _zscore_rolling(s1, _TD_YEAR)
    z2 = _zscore_rolling(s2, _TD_YEAR)
    z3 = _zscore_rolling(s3, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


# ── Feature functions 151-175 ─────────────────────────────────────────────────

# --- Group F2 (151-165): Sell pressure, net ratios, and drawdown-depth conditioned on selling ---

def itm_151_sell_count_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider sell transaction count."""
    return _rolling_sum(insider_sell_count, _TD_QTR)


def itm_152_sell_count_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider sell transaction count."""
    return _rolling_sum(insider_sell_count, _TD_YEAR)


def itm_153_sell_value_21d(insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider sell dollar value."""
    return _rolling_sum(insider_sell_value, _TD_MON)


def itm_154_sell_value_252d(insider_sell_value: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider sell dollar value."""
    return _rolling_sum(insider_sell_value, _TD_YEAR)


def itm_155_net_buy_count_63d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """63-day net insider transaction count (buys minus sells)."""
    return _rolling_sum(insider_buy_count, _TD_QTR) - _rolling_sum(insider_sell_count, _TD_QTR)


def itm_156_buy_sell_count_ratio_252d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """252-day insider buy count divided by sell count."""
    return _safe_div(_rolling_sum(insider_buy_count, _TD_YEAR), _rolling_sum(insider_sell_count, _TD_YEAR))


def itm_157_sell_value_x_ath_dd_63d(
    close: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63d sell value (log1p) times ATH drawdown magnitude (selling into decline)."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    sv63    = _rolling_sum(insider_sell_value, _TD_QTR)
    return np.log1p(sv63.clip(lower=0)) * dd_mag


def itm_158_net_value_x_ath_dd_21d(
    close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """21d net insider value (buy-sell) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    net21  = _rolling_sum(insider_buy_value, _TD_MON) - _rolling_sum(insider_sell_value, _TD_MON)
    return net21 * dd_mag


def itm_159_buy_count_zscore_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of daily insider buy count within trailing 63-day window."""
    return _zscore_rolling(insider_buy_count, _TD_QTR)


def itm_160_buy_value_pct_rank_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of daily buy value within trailing 63-day window."""
    return _rolling_rank_pct(insider_buy_value, _TD_QTR)


def itm_161_sell_count_zscore_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily insider sell count within trailing 252-day window."""
    return _zscore_rolling(insider_sell_count, _TD_YEAR)


def itm_162_buy_value_median_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day median of daily insider buy value."""
    return _rolling_median(insider_buy_value, _TD_QTR)


def itm_163_buy_count_median_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 252-day median of daily insider buy count."""
    return _rolling_median(insider_buy_count, _TD_YEAR)


def itm_164_sell_value_in_50pct_dd_252d(
    close: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """252d insider sell value occurring while stock is >=50% below ATH."""
    dd      = _drawdown_from_expanding_high(close)
    sv_deep = insider_sell_value.where(dd <= -0.50, other=0.0)
    return _rolling_sum(sv_deep, _TD_YEAR)


def itm_165_net_buy_value_x_1y_dd_63d(
    close: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series
) -> pd.Series:
    """63d net buy value times 1-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    net63   = _rolling_sum(insider_buy_value, _TD_QTR) - _rolling_sum(insider_sell_value, _TD_QTR)
    return net63 * dd_mag


# --- Group G2 (166-175): Buy conviction, price-level, and multi-horizon features ---

def itm_166_buy_value_ewm_63_x_ath_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """EWM(span=63) of insider buy value times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ewm63  = _ewm_mean(insider_buy_value, _TD_QTR)
    return np.log1p(ewm63.clip(lower=0)) * dd_mag


def itm_167_buyers_x_1y_dd_252d(
    close: pd.Series, insider_buyers: pd.Series
) -> pd.Series:
    """Unique insider buyers (252d sum) times 1-year drawdown magnitude."""
    dd_mag  = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    buyers  = _rolling_sum(insider_buyers, _TD_YEAR)
    return buyers * dd_mag


def itm_168_buy_value_in_bottom_quintile_63d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """63d insider buy value occurring when price is in bottom 20% of 252d range."""
    lo      = _rolling_min(close, _TD_YEAR)
    hi      = _rolling_max(close, _TD_YEAR)
    range_  = (hi - lo).replace(0, np.nan)
    pct     = _safe_div(close - lo, range_)
    bot_val = insider_buy_value.where(pct <= 0.20, other=0.0)
    return _rolling_sum(bot_val, _TD_QTR)


def itm_169_buy_count_in_bottom_quintile_252d(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """252d insider buy count occurring when price is in bottom 20% of 252d range."""
    lo     = _rolling_min(close, _TD_YEAR)
    hi     = _rolling_max(close, _TD_YEAR)
    range_ = (hi - lo).replace(0, np.nan)
    pct    = _safe_div(close - lo, range_)
    bot    = (pct <= 0.20).astype(float)
    return _rolling_sum(insider_buy_count * bot, _TD_YEAR)


def itm_170_sell_to_buy_count_ratio_252d(
    insider_buy_count: pd.Series, insider_sell_count: pd.Series
) -> pd.Series:
    """252d sell count divided by buy count (high = distribution pressure)."""
    return _safe_div(_rolling_sum(insider_sell_count, _TD_YEAR), _rolling_sum(insider_buy_count, _TD_YEAR))


def itm_171_buy_count_x_ath_dd_ewm21(
    close: pd.Series, insider_buy_count: pd.Series
) -> pd.Series:
    """EWM(span=21) of daily buy count times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    ewm21  = _ewm_mean(insider_buy_count, _TD_MON)
    return ewm21 * dd_mag


def itm_172_buy_value_rank_x_ath_dd_252d(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """Percentile rank of 252d buy value (504d window) times ATH drawdown magnitude."""
    dd_mag = _drawdown_from_expanding_high(close).abs()
    val252 = _rolling_sum(insider_buy_value, _TD_YEAR)
    pct    = _rolling_rank_pct(val252, _TD_2Y).fillna(0.0)
    return pct * dd_mag


def itm_173_officer_buy_x_1y_dd_252d(
    close: pd.Series, officer_buy_value: pd.Series
) -> pd.Series:
    """252d officer buy value (log1p) times 1-year drawdown magnitude."""
    dd_mag = _drawdown_from_rolling_high(close, _TD_YEAR).abs()
    ov252  = _rolling_sum(officer_buy_value, _TD_YEAR)
    return np.log1p(ov252.clip(lower=0)) * dd_mag


def itm_174_buyers_pct_rank_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of daily unique buyer count within trailing 252-day window."""
    return _rolling_rank_pct(insider_buyers, _TD_YEAR)


def itm_175_buy_value_halfyear_x_ath_dd(
    close: pd.Series, insider_buy_value: pd.Series
) -> pd.Series:
    """126d buy value (log1p) times ATH drawdown magnitude."""
    dd_mag  = _drawdown_from_expanding_high(close).abs()
    val126  = _rolling_sum(insider_buy_value, _TD_HALF)
    return np.log1p(val126.clip(lower=0)) * dd_mag


# ── Registry 001-075 ─────────────────────────────────────────────────────────

INSIDER_TIMING_REGISTRY_001_075 = {
    "itm_001_buy_count_21d":                          {"inputs": ["insider_buy_count"],                                          "func": itm_001_buy_count_21d},
    "itm_002_buy_count_63d":                          {"inputs": ["insider_buy_count"],                                          "func": itm_002_buy_count_63d},
    "itm_003_buy_count_252d":                         {"inputs": ["insider_buy_count"],                                          "func": itm_003_buy_count_252d},
    "itm_004_buy_value_21d":                          {"inputs": ["insider_buy_value"],                                          "func": itm_004_buy_value_21d},
    "itm_005_buy_value_63d":                          {"inputs": ["insider_buy_value"],                                          "func": itm_005_buy_value_63d},
    "itm_006_buy_value_252d":                         {"inputs": ["insider_buy_value"],                                          "func": itm_006_buy_value_252d},
    "itm_007_buy_count_21d_x_ath_dd":                 {"inputs": ["close", "insider_buy_count"],                                 "func": itm_007_buy_count_21d_x_ath_dd},
    "itm_008_buy_count_63d_x_ath_dd":                 {"inputs": ["close", "insider_buy_count"],                                 "func": itm_008_buy_count_63d_x_ath_dd},
    "itm_009_buy_value_21d_x_ath_dd":                 {"inputs": ["close", "insider_buy_value"],                                 "func": itm_009_buy_value_21d_x_ath_dd},
    "itm_010_buy_value_63d_x_ath_dd":                 {"inputs": ["close", "insider_buy_value"],                                 "func": itm_010_buy_value_63d_x_ath_dd},
    "itm_011_buy_value_63d_x_1y_dd":                  {"inputs": ["close", "insider_buy_value"],                                 "func": itm_011_buy_value_63d_x_1y_dd},
    "itm_012_buy_count_63d_x_1y_dd":                  {"inputs": ["close", "insider_buy_count"],                                 "func": itm_012_buy_count_63d_x_1y_dd},
    "itm_013_officer_buy_value_63d_x_ath_dd":         {"inputs": ["close", "officer_buy_value"],                                 "func": itm_013_officer_buy_value_63d_x_ath_dd},
    "itm_014_buy_value_252d_x_ath_dd":                {"inputs": ["close", "insider_buy_value"],                                 "func": itm_014_buy_value_252d_x_ath_dd},
    "itm_015_buyers_63d_x_ath_dd":                    {"inputs": ["close", "insider_buyers"],                                    "func": itm_015_buyers_63d_x_ath_dd},
    "itm_016_buy_in_deep_dd_50pct_flag":              {"inputs": ["close", "insider_buy_count"],                                 "func": itm_016_buy_in_deep_dd_50pct_flag},
    "itm_017_buy_in_deep_dd_70pct_flag":              {"inputs": ["close", "insider_buy_count"],                                 "func": itm_017_buy_in_deep_dd_70pct_flag},
    "itm_018_buy_in_deep_dd_90pct_flag":              {"inputs": ["close", "insider_buy_count"],                                 "func": itm_018_buy_in_deep_dd_90pct_flag},
    "itm_019_buy_sum_50pct_dd_window_63d":            {"inputs": ["close", "insider_buy_count"],                                 "func": itm_019_buy_sum_50pct_dd_window_63d},
    "itm_020_buy_sum_70pct_dd_window_63d":            {"inputs": ["close", "insider_buy_count"],                                 "func": itm_020_buy_sum_70pct_dd_window_63d},
    "itm_021_buy_sum_50pct_dd_window_252d":           {"inputs": ["close", "insider_buy_count"],                                 "func": itm_021_buy_sum_50pct_dd_window_252d},
    "itm_022_buy_value_in_50pct_dd_63d":              {"inputs": ["close", "insider_buy_value"],                                 "func": itm_022_buy_value_in_50pct_dd_63d},
    "itm_023_buy_value_in_70pct_dd_63d":              {"inputs": ["close", "insider_buy_value"],                                 "func": itm_023_buy_value_in_70pct_dd_63d},
    "itm_024_buy_value_in_1y_dd_50pct_63d":           {"inputs": ["close", "insider_buy_value"],                                 "func": itm_024_buy_value_in_1y_dd_50pct_63d},
    "itm_025_officer_buy_in_deep_dd_50pct_63d":       {"inputs": ["close", "officer_buy_value"],                                 "func": itm_025_officer_buy_in_deep_dd_50pct_63d},
    "itm_026_dd_at_buy_mean_21d":                     {"inputs": ["close", "insider_buy_count"],                                 "func": itm_026_dd_at_buy_mean_21d},
    "itm_027_dd_at_buy_mean_63d":                     {"inputs": ["close", "insider_buy_count"],                                 "func": itm_027_dd_at_buy_mean_63d},
    "itm_028_dd_at_buy_mean_252d":                    {"inputs": ["close", "insider_buy_count"],                                 "func": itm_028_dd_at_buy_mean_252d},
    "itm_029_dd_at_buy_worst_63d":                    {"inputs": ["close", "insider_buy_count"],                                 "func": itm_029_dd_at_buy_worst_63d},
    "itm_030_dd_at_buy_worst_252d":                   {"inputs": ["close", "insider_buy_count"],                                 "func": itm_030_dd_at_buy_worst_252d},
    "itm_031_buy_value_per_dd_unit_63d":              {"inputs": ["close", "insider_buy_value"],                                 "func": itm_031_buy_value_per_dd_unit_63d},
    "itm_032_buy_count_per_dd_unit_63d":              {"inputs": ["close", "insider_buy_count"],                                 "func": itm_032_buy_count_per_dd_unit_63d},
    "itm_033_buy_value_dd_product_21d":               {"inputs": ["close", "insider_buy_value"],                                 "func": itm_033_buy_value_dd_product_21d},
    "itm_034_buy_value_dd_product_252d":              {"inputs": ["close", "insider_buy_value"],                                 "func": itm_034_buy_value_dd_product_252d},
    "itm_035_officer_buy_dd_product_63d":             {"inputs": ["close", "officer_buy_value"],                                 "func": itm_035_officer_buy_dd_product_63d},
    "itm_036_buy_value_scaled_by_1y_dd_63d":          {"inputs": ["close", "insider_buy_value"],                                 "func": itm_036_buy_value_scaled_by_1y_dd_63d},
    "itm_037_buyers_x_dd_depth_63d":                  {"inputs": ["close", "insider_buyers"],                                    "func": itm_037_buyers_x_dd_depth_63d},
    "itm_038_buy_value_x_log_dd_depth_63d":           {"inputs": ["close", "insider_buy_value"],                                 "func": itm_038_buy_value_x_log_dd_depth_63d},
    "itm_039_buy_value_x_dd2_63d":                    {"inputs": ["close", "insider_buy_value"],                                 "func": itm_039_buy_value_x_dd2_63d},
    "itm_040_buy_count_x_2y_dd_63d":                  {"inputs": ["close", "insider_buy_count"],                                 "func": itm_040_buy_count_x_2y_dd_63d},
    "itm_041_buy_value_x_2y_dd_63d":                  {"inputs": ["close", "insider_buy_value"],                                 "func": itm_041_buy_value_x_2y_dd_63d},
    "itm_042_buy_value_x_3y_dd_63d":                  {"inputs": ["close", "insider_buy_value"],                                 "func": itm_042_buy_value_x_3y_dd_63d},
    "itm_043_officer_buy_x_2y_dd_63d":                {"inputs": ["close", "officer_buy_value"],                                 "func": itm_043_officer_buy_x_2y_dd_63d},
    "itm_044_buy_value_dd_ratio_vs_sell_63d":         {"inputs": ["close", "insider_buy_value", "insider_sell_value"],           "func": itm_044_buy_value_dd_ratio_vs_sell_63d},
    "itm_045_net_buy_x_ath_dd_63d":                   {"inputs": ["close", "insider_buy_value", "insider_sell_value"],           "func": itm_045_net_buy_x_ath_dd_63d},
    "itm_046_is_buying_dip_flag":                     {"inputs": ["close", "insider_buy_count"],                                 "func": itm_046_is_buying_dip_flag},
    "itm_047_is_buying_strength_flag":                {"inputs": ["close", "insider_buy_count"],                                 "func": itm_047_is_buying_strength_flag},
    "itm_048_dip_buy_fraction_63d":                   {"inputs": ["close", "insider_buy_count"],                                 "func": itm_048_dip_buy_fraction_63d},
    "itm_049_dip_buy_fraction_252d":                  {"inputs": ["close", "insider_buy_count"],                                 "func": itm_049_dip_buy_fraction_252d},
    "itm_050_buy_below_1y_low_plus10pct":             {"inputs": ["close", "insider_buy_count"],                                 "func": itm_050_buy_below_1y_low_plus10pct},
    "itm_051_buy_near_ath_low_plus10pct":             {"inputs": ["close", "insider_buy_count"],                                 "func": itm_051_buy_near_ath_low_plus10pct},
    "itm_052_dip_buy_count_63d":                      {"inputs": ["close", "insider_buy_count"],                                 "func": itm_052_dip_buy_count_63d},
    "itm_053_dip_buy_value_63d":                      {"inputs": ["close", "insider_buy_value"],                                 "func": itm_053_dip_buy_value_63d},
    "itm_054_dip_buy_value_252d":                     {"inputs": ["close", "insider_buy_value"],                                 "func": itm_054_dip_buy_value_252d},
    "itm_055_buy_at_new_low_flag":                    {"inputs": ["close", "insider_buy_count"],                                 "func": itm_055_buy_at_new_low_flag},
    "itm_056_buy_at_new_52w_low_count_252d":          {"inputs": ["close", "insider_buy_count"],                                 "func": itm_056_buy_at_new_52w_low_count_252d},
    "itm_057_buy_price_vs_1y_high_ratio_63d":         {"inputs": ["close", "insider_buy_count"],                                 "func": itm_057_buy_price_vs_1y_high_ratio_63d},
    "itm_058_buy_price_vs_ath_ratio_63d":             {"inputs": ["close", "insider_buy_count"],                                 "func": itm_058_buy_price_vs_ath_ratio_63d},
    "itm_059_buy_days_in_bottom_decile_252d":         {"inputs": ["close", "insider_buy_count"],                                 "func": itm_059_buy_days_in_bottom_decile_252d},
    "itm_060_buy_value_bottom_decile_fraction_252d":  {"inputs": ["close", "insider_buy_value"],                                 "func": itm_060_buy_value_bottom_decile_fraction_252d},
    "itm_061_days_since_last_buy":                    {"inputs": ["insider_buy_count"],                                          "func": itm_061_days_since_last_buy},
    "itm_062_dd_change_since_last_buy":               {"inputs": ["close", "insider_buy_count"],                                 "func": itm_062_dd_change_since_last_buy},
    "itm_063_buy_count_acceleration_21d_63d":         {"inputs": ["insider_buy_count"],                                          "func": itm_063_buy_count_acceleration_21d_63d},
    "itm_064_buy_value_acceleration_21d_63d":         {"inputs": ["insider_buy_value"],                                          "func": itm_064_buy_value_acceleration_21d_63d},
    "itm_065_sell_to_buy_value_ratio_63d":            {"inputs": ["insider_buy_value", "insider_sell_value"],                    "func": itm_065_sell_to_buy_value_ratio_63d},
    "itm_066_net_buy_value_63d":                      {"inputs": ["insider_buy_value", "insider_sell_value"],                    "func": itm_066_net_buy_value_63d},
    "itm_067_net_buy_value_252d":                     {"inputs": ["insider_buy_value", "insider_sell_value"],                    "func": itm_067_net_buy_value_252d},
    "itm_068_buy_count_zscore_252d":                  {"inputs": ["insider_buy_count"],                                          "func": itm_068_buy_count_zscore_252d},
    "itm_069_buy_value_zscore_252d":                  {"inputs": ["insider_buy_value"],                                          "func": itm_069_buy_value_zscore_252d},
    "itm_070_buy_value_ewm_21":                       {"inputs": ["insider_buy_value"],                                          "func": itm_070_buy_value_ewm_21},
    "itm_071_buy_count_pct_rank_252d":                {"inputs": ["insider_buy_count"],                                          "func": itm_071_buy_count_pct_rank_252d},
    "itm_072_officer_buy_value_63d":                  {"inputs": ["officer_buy_value"],                                          "func": itm_072_officer_buy_value_63d},
    "itm_073_officer_buy_fraction_of_total_63d":      {"inputs": ["insider_buy_value", "officer_buy_value"],                    "func": itm_073_officer_buy_fraction_of_total_63d},
    "itm_074_buy_value_x_ath_dd_x_officer_fraction_63d": {"inputs": ["close", "insider_buy_value", "officer_buy_value"],        "func": itm_074_buy_value_x_ath_dd_x_officer_fraction_63d},
    "itm_075_composite_insider_timing_score":         {"inputs": ["close", "insider_buy_value", "insider_buy_count", "insider_buyers"], "func": itm_075_composite_insider_timing_score},
    "itm_151_sell_count_63d":                         {"inputs": ["insider_sell_count"],                                                  "func": itm_151_sell_count_63d},
    "itm_152_sell_count_252d":                        {"inputs": ["insider_sell_count"],                                                  "func": itm_152_sell_count_252d},
    "itm_153_sell_value_21d":                         {"inputs": ["insider_sell_value"],                                                  "func": itm_153_sell_value_21d},
    "itm_154_sell_value_252d":                        {"inputs": ["insider_sell_value"],                                                  "func": itm_154_sell_value_252d},
    "itm_155_net_buy_count_63d":                      {"inputs": ["insider_buy_count", "insider_sell_count"],                             "func": itm_155_net_buy_count_63d},
    "itm_156_buy_sell_count_ratio_252d":              {"inputs": ["insider_buy_count", "insider_sell_count"],                             "func": itm_156_buy_sell_count_ratio_252d},
    "itm_157_sell_value_x_ath_dd_63d":               {"inputs": ["close", "insider_sell_value"],                                        "func": itm_157_sell_value_x_ath_dd_63d},
    "itm_158_net_value_x_ath_dd_21d":                {"inputs": ["close", "insider_buy_value", "insider_sell_value"],                    "func": itm_158_net_value_x_ath_dd_21d},
    "itm_159_buy_count_zscore_63d":                   {"inputs": ["insider_buy_count"],                                                   "func": itm_159_buy_count_zscore_63d},
    "itm_160_buy_value_pct_rank_63d":                 {"inputs": ["insider_buy_value"],                                                   "func": itm_160_buy_value_pct_rank_63d},
    "itm_161_sell_count_zscore_252d":                 {"inputs": ["insider_sell_count"],                                                  "func": itm_161_sell_count_zscore_252d},
    "itm_162_buy_value_median_63d":                   {"inputs": ["insider_buy_value"],                                                   "func": itm_162_buy_value_median_63d},
    "itm_163_buy_count_median_252d":                  {"inputs": ["insider_buy_count"],                                                   "func": itm_163_buy_count_median_252d},
    "itm_164_sell_value_in_50pct_dd_252d":            {"inputs": ["close", "insider_sell_value"],                                        "func": itm_164_sell_value_in_50pct_dd_252d},
    "itm_165_net_buy_value_x_1y_dd_63d":              {"inputs": ["close", "insider_buy_value", "insider_sell_value"],                    "func": itm_165_net_buy_value_x_1y_dd_63d},
    "itm_166_buy_value_ewm_63_x_ath_dd":              {"inputs": ["close", "insider_buy_value"],                                         "func": itm_166_buy_value_ewm_63_x_ath_dd},
    "itm_167_buyers_x_1y_dd_252d":                   {"inputs": ["close", "insider_buyers"],                                             "func": itm_167_buyers_x_1y_dd_252d},
    "itm_168_buy_value_in_bottom_quintile_63d":       {"inputs": ["close", "insider_buy_value"],                                         "func": itm_168_buy_value_in_bottom_quintile_63d},
    "itm_169_buy_count_in_bottom_quintile_252d":      {"inputs": ["close", "insider_buy_count"],                                         "func": itm_169_buy_count_in_bottom_quintile_252d},
    "itm_170_sell_to_buy_count_ratio_252d":           {"inputs": ["insider_buy_count", "insider_sell_count"],                             "func": itm_170_sell_to_buy_count_ratio_252d},
    "itm_171_buy_count_x_ath_dd_ewm21":               {"inputs": ["close", "insider_buy_count"],                                         "func": itm_171_buy_count_x_ath_dd_ewm21},
    "itm_172_buy_value_rank_x_ath_dd_252d":           {"inputs": ["close", "insider_buy_value"],                                         "func": itm_172_buy_value_rank_x_ath_dd_252d},
    "itm_173_officer_buy_x_1y_dd_252d":               {"inputs": ["close", "officer_buy_value"],                                         "func": itm_173_officer_buy_x_1y_dd_252d},
    "itm_174_buyers_pct_rank_252d":                   {"inputs": ["insider_buyers"],                                                      "func": itm_174_buyers_pct_rank_252d},
    "itm_175_buy_value_halfyear_x_ath_dd":            {"inputs": ["close", "insider_buy_value"],                                         "func": itm_175_buy_value_halfyear_x_ath_dd},
}
