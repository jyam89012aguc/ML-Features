"""
88_insider_transaction_freq — Base Features 001-100
Domain: frequency, rate, and acceleration of insider trading ACTIVITY
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Series Contract
--------------------------------------
Inputs are daily-frequency pandas Series derived from Sharadar SF2 insider
transaction filings, aggregated to one row per (ticker, date).  Most days
carry ZERO — the series are event-driven and are NOT forward-filled.  A
positive value appears only on days when a filing was recorded.  Feature
functions aggregate over trailing rolling windows using rolling SUMS and
COUNTS; they do NOT forward-fill gaps.  Trading-day conventions used:
  5 trading days  = 1 week
  21 trading days = 1 month
  63 trading days = 1 quarter
  126 trading days = 2 quarters
  252 trading days = 1 year
  504 trading days = 2 years

All functions look strictly backward via .shift(positive_int), .rolling(),
or .expanding().  No negative shifts, no iloc[i+n], no .diff(negative).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK    = 5
_TD_MO    = 21
_TD_QTR   = 63
_TD_2Q    = 126
_TD_YEAR  = 252
_TD_2Y    = 504
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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _active_days(s: pd.Series, w: int) -> pd.Series:
    """Count of days with nonzero values in a rolling window."""
    return _rolling_sum((s > 0).astype(float), w)


def _days_since_last_nonzero(s: pd.Series) -> pd.Series:
    """
    Backward-only helper: number of trading days since the most recent day
    with a nonzero (>0) value.  Returns NaN if no nonzero has ever appeared.
    On an all-zero series, returns NaN throughout.
    """
    nonzero = (s > 0).astype(float)
    cumcount = nonzero.cumsum()
    # For each row, reset counter when nonzero fires; count forward from there
    n = len(s)
    arr = nonzero.values
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=s.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Rolling transaction counts (total activity) ---

def itf_001_total_txn_count_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions (buys + sells) over trailing 21-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_MO)


def itf_002_total_txn_count_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 63-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_QTR)


def itf_003_total_txn_count_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 126-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_2Q)


def itf_004_total_txn_count_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_YEAR)


def itf_005_total_txn_count_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 504-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_2Y)


def itf_006_buy_count_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 21-day window."""
    return _rolling_sum(insider_buy_count, _TD_MO)


def itf_007_buy_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 63-day window."""
    return _rolling_sum(insider_buy_count, _TD_QTR)


def itf_008_buy_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 252-day window."""
    return _rolling_sum(insider_buy_count, _TD_YEAR)


def itf_009_sell_count_21d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 21-day window."""
    return _rolling_sum(insider_sell_count, _TD_MO)


def itf_010_sell_count_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 63-day window."""
    return _rolling_sum(insider_sell_count, _TD_QTR)


def itf_011_sell_count_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 252-day window."""
    return _rolling_sum(insider_sell_count, _TD_YEAR)


def itf_012_officer_buy_count_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transaction count over trailing 63-day window."""
    return _rolling_sum(officer_buy_count, _TD_QTR)


def itf_013_officer_buy_count_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transaction count over trailing 252-day window."""
    return _rolling_sum(officer_buy_count, _TD_YEAR)


def itf_014_director_buy_count_63d(director_buy_count: pd.Series) -> pd.Series:
    """Director buy transaction count over trailing 63-day window."""
    return _rolling_sum(director_buy_count, _TD_QTR)


def itf_015_director_buy_count_252d(director_buy_count: pd.Series) -> pd.Series:
    """Director buy transaction count over trailing 252-day window."""
    return _rolling_sum(director_buy_count, _TD_YEAR)


# --- Group B (016-030): Active trading days in windows ---

def itf_016_active_days_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with any insider transaction in trailing 21-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_sum(any_txn, _TD_MO)


def itf_017_active_days_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with any insider transaction in trailing 63-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_sum(any_txn, _TD_QTR)


def itf_018_active_days_126d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with any insider transaction in trailing 126-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_sum(any_txn, _TD_2Q)


def itf_019_active_days_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with any insider transaction in trailing 252-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_sum(any_txn, _TD_YEAR)


def itf_020_buy_active_days_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with a buy transaction in trailing 63-day window."""
    return _active_days(insider_buy_count, _TD_QTR)


def itf_021_buy_active_days_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with a buy transaction in trailing 252-day window."""
    return _active_days(insider_buy_count, _TD_YEAR)


def itf_022_sell_active_days_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with a sell transaction in trailing 63-day window."""
    return _active_days(insider_sell_count, _TD_QTR)


def itf_023_sell_active_days_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with a sell transaction in trailing 252-day window."""
    return _active_days(insider_sell_count, _TD_YEAR)


def itf_024_officer_buy_active_days_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with an officer buy in trailing 252-day window."""
    return _active_days(officer_buy_count, _TD_YEAR)


def itf_025_director_buy_active_days_252d(director_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with a director buy in trailing 252-day window."""
    return _active_days(director_buy_count, _TD_YEAR)


# --- Group C (026-040): Days-since-last and inter-event timing ---

def itf_026_days_since_last_any_txn(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Trading days since the most recent insider transaction of any type."""
    any_txn = insider_buy_count + insider_sell_count
    return _days_since_last_nonzero(any_txn)


def itf_027_days_since_last_buy(insider_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent insider buy transaction."""
    return _days_since_last_nonzero(insider_buy_count)


def itf_028_days_since_last_sell(insider_sell_count: pd.Series) -> pd.Series:
    """Trading days since the most recent insider sell transaction."""
    return _days_since_last_nonzero(insider_sell_count)


def itf_029_days_since_last_officer_buy(officer_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent officer buy transaction."""
    return _days_since_last_nonzero(officer_buy_count)


def itf_030_days_since_last_director_buy(director_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent director buy transaction."""
    return _days_since_last_nonzero(director_buy_count)


def itf_031_days_since_last_buy_21d_min(insider_buy_count: pd.Series) -> pd.Series:
    """
    Rolling 21-day minimum of days-since-last-buy.
    Captures how recently a buy occurred within the month window.
    """
    dslb = _days_since_last_nonzero(insider_buy_count)
    return _rolling_min(dslb, _TD_MO)


def itf_032_days_since_last_buy_63d_mean(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 63-day mean of days-since-last-buy (average recency over the quarter)."""
    dslb = _days_since_last_nonzero(insider_buy_count)
    return _rolling_mean(dslb, _TD_QTR)


def itf_033_days_since_last_any_txn_63d_mean(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 63-day mean of days-since-last-any-transaction."""
    any_txn = insider_buy_count + insider_sell_count
    dsl = _days_since_last_nonzero(any_txn)
    return _rolling_mean(dsl, _TD_QTR)


def itf_034_days_since_last_any_txn_252d_mean(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Rolling 252-day mean of days-since-last-any-transaction."""
    any_txn = insider_buy_count + insider_sell_count
    dsl = _days_since_last_nonzero(any_txn)
    return _rolling_mean(dsl, _TD_YEAR)


def itf_035_gap_shrinkage_buy_21v63(insider_buy_count: pd.Series) -> pd.Series:
    """
    Ratio of 21-day active-buy-days to 63-day active-buy-days, scaled to window.
    > 1/3 means buys are accelerating into the recent window.
    """
    act_21 = _active_days(insider_buy_count, _TD_MO)
    act_63 = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR)
    # Annualize both to per-63-day rate
    rate_21 = act_21 * (_TD_QTR / _TD_MO)
    return _safe_div(rate_21, act_63.replace(0, np.nan))


# --- Group D (036-050): Frequency rates (transactions per window, normalized) ---

def itf_036_txn_rate_per_month_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Transactions per 21-day window divided by window length (daily rate)."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_sum(total, _TD_MO), pd.Series(_TD_MO, index=total.index))


def itf_037_buy_rate_per_day_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per trading day over 63-day window."""
    return _safe_div(_rolling_sum(insider_buy_count, _TD_QTR),
                     pd.Series(float(_TD_QTR), index=insider_buy_count.index))


def itf_038_sell_rate_per_day_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Average sell transactions per trading day over 63-day window."""
    return _safe_div(_rolling_sum(insider_sell_count, _TD_QTR),
                     pd.Series(float(_TD_QTR), index=insider_sell_count.index))


def itf_039_txn_rate_per_day_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Average total transactions per trading day over 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_sum(total, _TD_YEAR),
                     pd.Series(float(_TD_YEAR), index=total.index))


def itf_040_active_day_density_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 21-day window with any insider transaction."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_mean(any_txn, _TD_MO)


def itf_041_active_day_density_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 63-day window with any insider transaction."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_mean(any_txn, _TD_QTR)


def itf_042_active_day_density_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 252-day window with any insider transaction."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_mean(any_txn, _TD_YEAR)


def itf_043_buy_day_density_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 63-day window with a buy transaction."""
    return _rolling_mean((insider_buy_count > 0).astype(float), _TD_QTR)


def itf_044_buy_day_density_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 252-day window with a buy transaction."""
    return _rolling_mean((insider_buy_count > 0).astype(float), _TD_YEAR)


def itf_045_officer_buy_rate_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transactions per trading day over 252-day window."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_YEAR),
                     pd.Series(float(_TD_YEAR), index=officer_buy_count.index))


# --- Group E (046-060): Acceleration — recent window vs longer-term baseline ---

def itf_046_txn_accel_21v63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Activity acceleration: 21-day rate vs 63-day rate.
    Rate = transactions / window_days.  Positive means recent activity > baseline.
    """
    total = insider_buy_count + insider_sell_count
    rate_21 = _safe_div(_rolling_sum(total, _TD_MO),
                        pd.Series(float(_TD_MO), index=total.index))
    rate_63 = _safe_div(_rolling_sum(total, _TD_QTR),
                        pd.Series(float(_TD_QTR), index=total.index))
    return rate_21 - rate_63


def itf_047_txn_accel_21v252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Activity acceleration: 21-day rate vs 252-day rate."""
    total = insider_buy_count + insider_sell_count
    rate_21  = _safe_div(_rolling_sum(total, _TD_MO),   pd.Series(float(_TD_MO),   index=total.index))
    rate_252 = _safe_div(_rolling_sum(total, _TD_YEAR), pd.Series(float(_TD_YEAR), index=total.index))
    return rate_21 - rate_252


def itf_048_txn_accel_63v252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Activity acceleration: 63-day rate vs 252-day rate."""
    total = insider_buy_count + insider_sell_count
    rate_63  = _safe_div(_rolling_sum(total, _TD_QTR),  pd.Series(float(_TD_QTR),  index=total.index))
    rate_252 = _safe_div(_rolling_sum(total, _TD_YEAR), pd.Series(float(_TD_YEAR), index=total.index))
    return rate_63 - rate_252


def itf_049_buy_accel_21v63(insider_buy_count: pd.Series) -> pd.Series:
    """Buy activity acceleration: 21-day rate vs 63-day rate."""
    rate_21 = _safe_div(_rolling_sum(insider_buy_count, _TD_MO),
                        pd.Series(float(_TD_MO), index=insider_buy_count.index))
    rate_63 = _safe_div(_rolling_sum(insider_buy_count, _TD_QTR),
                        pd.Series(float(_TD_QTR), index=insider_buy_count.index))
    return rate_21 - rate_63


def itf_050_buy_accel_63v252(insider_buy_count: pd.Series) -> pd.Series:
    """Buy activity acceleration: 63-day rate vs 252-day rate."""
    rate_63  = _safe_div(_rolling_sum(insider_buy_count, _TD_QTR),
                         pd.Series(float(_TD_QTR), index=insider_buy_count.index))
    rate_252 = _safe_div(_rolling_sum(insider_buy_count, _TD_YEAR),
                         pd.Series(float(_TD_YEAR), index=insider_buy_count.index))
    return rate_63 - rate_252


def itf_051_txn_accel_ratio_21v63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 21-day rate to 63-day rate (ratio form of acceleration)."""
    total = insider_buy_count + insider_sell_count
    rate_21 = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_63 = _rolling_sum(total, _TD_QTR) / _TD_QTR
    return _safe_div(rate_21, rate_63)


def itf_052_buy_accel_ratio_21v252(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21-day buy rate to 252-day buy rate."""
    rate_21  = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(insider_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


def itf_053_officer_buy_accel_21v252(officer_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21-day officer-buy rate to 252-day officer-buy rate."""
    rate_21  = _rolling_sum(officer_buy_count, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(officer_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


def itf_054_director_buy_accel_21v252(director_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21-day director-buy rate to 252-day director-buy rate."""
    rate_21  = _rolling_sum(director_buy_count, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(director_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


def itf_055_txn_surge_21d_vs_504d_baseline(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Surge indicator: 21-day total transactions vs 504-day daily-rate baseline.
    = (21d_count / 21) / (504d_count / 504).  >1 means recent surge.
    """
    total = insider_buy_count + insider_sell_count
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_504 = _rolling_sum(total, _TD_2Y) / _TD_2Y
    return _safe_div(rate_21, rate_504)


# --- Group F (056-065): Active-insider participant counts ---

def itf_056_buyers_21d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider_buyers (unique buyers per filing day, summed)."""
    return _rolling_sum(insider_buyers, _TD_MO)


def itf_057_buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider_buyers."""
    return _rolling_sum(insider_buyers, _TD_QTR)


def itf_058_buyers_252d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider_buyers."""
    return _rolling_sum(insider_buyers, _TD_YEAR)


def itf_059_sellers_63d(insider_sellers: pd.Series) -> pd.Series:
    """Rolling 63-day sum of insider_sellers."""
    return _rolling_sum(insider_sellers, _TD_QTR)


def itf_060_sellers_252d(insider_sellers: pd.Series) -> pd.Series:
    """Rolling 252-day sum of insider_sellers."""
    return _rolling_sum(insider_sellers, _TD_YEAR)


def itf_061_total_participants_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Total insider participants (buyers + sellers) over 63-day window."""
    return _rolling_sum(insider_buyers + insider_sellers, _TD_QTR)


def itf_062_total_participants_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Total insider participants (buyers + sellers) over 252-day window."""
    return _rolling_sum(insider_buyers + insider_sellers, _TD_YEAR)


def itf_063_buyer_accel_21v252(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 21-day buyer sum rate to 252-day buyer sum rate."""
    rate_21  = _rolling_sum(insider_buyers, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(insider_buyers, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


def itf_064_buyer_density_63d(insider_buyers: pd.Series) -> pd.Series:
    """Mean daily insider buyer count over 63-day window."""
    return _rolling_mean(insider_buyers, _TD_QTR)


def itf_065_buyer_density_252d(insider_buyers: pd.Series) -> pd.Series:
    """Mean daily insider buyer count over 252-day window."""
    return _rolling_mean(insider_buyers, _TD_YEAR)


# --- Group G (066-075): Burstiness, regularity, and post-quiet bursts ---

def itf_066_txn_zscore_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily total transaction count within a 63-day rolling window."""
    total = insider_buy_count + insider_sell_count
    return _zscore_rolling(total, _TD_QTR)


def itf_067_txn_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily total transaction count within a 252-day rolling window."""
    total = insider_buy_count + insider_sell_count
    return _zscore_rolling(total, _TD_YEAR)


def itf_068_buy_count_ewm_21(insider_buy_count: pd.Series) -> pd.Series:
    """EWM (span=21) of daily buy count — smoothed recent buy activity."""
    return _ewm_mean(insider_buy_count, _TD_MO)


def itf_069_txn_count_ewm_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM (span=63) of daily total transaction count."""
    total = insider_buy_count + insider_sell_count
    return _ewm_mean(total, _TD_QTR)


def itf_070_txn_std_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Standard deviation of daily total transaction count over 63-day window (burstiness)."""
    total = insider_buy_count + insider_sell_count
    return _rolling_std(total, _TD_QTR)


def itf_071_txn_std_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Standard deviation of daily total transaction count over 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_std(total, _TD_YEAR)


def itf_072_new_burst_after_quiet_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Post-quiet burst flag: 1 when 21-day transaction count > 0 AND
    prior 63-day (shifted) count was zero.  Detects new activity erupting
    after a completely quiet period.
    """
    total = insider_buy_count + insider_sell_count
    recent_21  = _rolling_sum(total, _TD_MO)
    prior_63   = _rolling_sum(total.shift(_TD_MO), _TD_QTR)
    flag = ((recent_21 > 0) & (prior_63 == 0)).astype(float)
    return flag


def itf_073_txn_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of daily total transaction count within 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_rank_pct(total, _TD_YEAR)


def itf_074_buy_count_pct_rank_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily buy count within 252-day window."""
    return _rolling_rank_pct(insider_buy_count, _TD_YEAR)


def itf_075_activity_composite_score(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Composite activity score: equally weighted sum of three z-scores:
      (1) total txn count 63d z-score, (2) active-day density 63d z-score,
      (3) buyers 63d sum z-score.
    Higher = more recent activity vs own history.
    """
    total = insider_buy_count + insider_sell_count
    z_txn     = _zscore_rolling(_rolling_sum(total, _TD_QTR), _TD_YEAR)
    z_density = _zscore_rolling(_rolling_mean((total > 0).astype(float), _TD_QTR), _TD_YEAR)
    z_buyers  = _zscore_rolling(_rolling_sum(insider_buyers, _TD_QTR), _TD_YEAR)
    return (z_txn + z_density + z_buyers) / 3.0


# ── Feature functions 151-175 ─────────────────────────────────────────────────

# --- Group H-ext (151-160): Sell-side and net-flow frequency features ---

def itf_151_sell_count_126d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 126-day window."""
    return _rolling_sum(insider_sell_count, _TD_2Q)


def itf_152_sell_count_504d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 504-day window."""
    return _rolling_sum(insider_sell_count, _TD_2Y)


def itf_153_net_txn_count_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net insider transactions (buys minus sells) over trailing 63-day window."""
    return _rolling_sum(insider_buy_count - insider_sell_count, _TD_QTR)


def itf_154_net_txn_count_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Net insider transactions (buys minus sells) over trailing 252-day window."""
    return _rolling_sum(insider_buy_count - insider_sell_count, _TD_YEAR)


def itf_155_buy_to_sell_ratio_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 63-day buy count to 63-day sell count."""
    return _safe_div(_rolling_sum(insider_buy_count, _TD_QTR),
                     _rolling_sum(insider_sell_count, _TD_QTR))


def itf_156_buy_to_sell_ratio_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 252-day buy count to 252-day sell count."""
    return _safe_div(_rolling_sum(insider_buy_count, _TD_YEAR),
                     _rolling_sum(insider_sell_count, _TD_YEAR))


def itf_157_sell_active_days_126d(insider_sell_count: pd.Series) -> pd.Series:
    """Number of distinct days with a sell transaction in trailing 126-day window."""
    return _active_days(insider_sell_count, _TD_2Q)


def itf_158_buy_active_days_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with a buy transaction in trailing 126-day window."""
    return _active_days(insider_buy_count, _TD_2Q)


def itf_159_net_buyer_density_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of 63-day window where buys exceeded sells on that day."""
    net_positive = ((insider_buy_count - insider_sell_count) > 0).astype(float)
    return _rolling_mean(net_positive, _TD_QTR)


def itf_160_sell_zscore_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of daily sell count within 252-day rolling window."""
    return _zscore_rolling(insider_sell_count, _TD_YEAR)


# --- Group I-ext (161-168): Participant and seller frequency features ---

def itf_161_sellers_21d(insider_sellers: pd.Series) -> pd.Series:
    """Rolling 21-day sum of insider_sellers."""
    return _rolling_sum(insider_sellers, _TD_MO)


def itf_162_sellers_126d(insider_sellers: pd.Series) -> pd.Series:
    """Rolling 126-day sum of insider_sellers."""
    return _rolling_sum(insider_sellers, _TD_2Q)


def itf_163_buyers_126d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 126-day sum of insider_buyers."""
    return _rolling_sum(insider_buyers, _TD_2Q)


def itf_164_buyer_to_seller_ratio_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Ratio of 63-day buyer sum to 63-day seller sum."""
    return _safe_div(_rolling_sum(insider_buyers, _TD_QTR),
                     _rolling_sum(insider_sellers, _TD_QTR))


def itf_165_buyer_to_seller_ratio_252d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Ratio of 252-day buyer sum to 252-day seller sum."""
    return _safe_div(_rolling_sum(insider_buyers, _TD_YEAR),
                     _rolling_sum(insider_sellers, _TD_YEAR))


def itf_166_seller_density_63d(insider_sellers: pd.Series) -> pd.Series:
    """Mean daily insider seller count over 63-day window."""
    return _rolling_mean(insider_sellers, _TD_QTR)


def itf_167_multi_seller_day_count_252d(insider_sellers: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where insider_sellers >= 2."""
    return _rolling_sum((insider_sellers >= 2).astype(float), _TD_YEAR)


def itf_168_net_participants_63d(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Net participants (buyers minus sellers) over trailing 63-day window."""
    return _rolling_sum(insider_buyers - insider_sellers, _TD_QTR)


# --- Group J-ext (169-175): Officer/director sell-side and cross-role ---

def itf_169_officer_buy_count_126d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transaction count over trailing 126-day window."""
    return _rolling_sum(officer_buy_count, _TD_2Q)


def itf_170_director_buy_count_126d(director_buy_count: pd.Series) -> pd.Series:
    """Director buy transaction count over trailing 126-day window."""
    return _rolling_sum(director_buy_count, _TD_2Q)


def itf_171_officer_buy_density_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 252-day window with an officer buy."""
    return _rolling_mean((officer_buy_count > 0).astype(float), _TD_YEAR)


def itf_172_director_buy_density_252d(director_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 252-day window with a director buy."""
    return _rolling_mean((director_buy_count > 0).astype(float), _TD_YEAR)


def itf_173_officer_director_buy_count_126d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy count over 126-day window."""
    return _rolling_sum(officer_buy_count + director_buy_count, _TD_2Q)


def itf_174_officer_buy_pct_rank_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily officer buy count within 63-day window."""
    return _rolling_rank_pct(officer_buy_count, _TD_QTR)


def itf_175_txn_count_126d_pct_of_504d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """126-day transaction count as a fraction of its 504-day rolling peak."""
    total   = insider_buy_count + insider_sell_count
    cnt_126 = _rolling_sum(total, _TD_2Q)
    peak    = _rolling_max(cnt_126, _TD_2Y)
    return _safe_div(cnt_126, peak)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_TRANSACTION_FREQ_REGISTRY_001_075 = {
    "itf_001_total_txn_count_21d":              {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_001_total_txn_count_21d},
    "itf_002_total_txn_count_63d":              {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_002_total_txn_count_63d},
    "itf_003_total_txn_count_126d":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_003_total_txn_count_126d},
    "itf_004_total_txn_count_252d":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_004_total_txn_count_252d},
    "itf_005_total_txn_count_504d":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_005_total_txn_count_504d},
    "itf_006_buy_count_21d":                    {"inputs": ["insider_buy_count"],                       "func": itf_006_buy_count_21d},
    "itf_007_buy_count_63d":                    {"inputs": ["insider_buy_count"],                       "func": itf_007_buy_count_63d},
    "itf_008_buy_count_252d":                   {"inputs": ["insider_buy_count"],                       "func": itf_008_buy_count_252d},
    "itf_009_sell_count_21d":                   {"inputs": ["insider_sell_count"],                      "func": itf_009_sell_count_21d},
    "itf_010_sell_count_63d":                   {"inputs": ["insider_sell_count"],                      "func": itf_010_sell_count_63d},
    "itf_011_sell_count_252d":                  {"inputs": ["insider_sell_count"],                      "func": itf_011_sell_count_252d},
    "itf_012_officer_buy_count_63d":            {"inputs": ["officer_buy_count"],                       "func": itf_012_officer_buy_count_63d},
    "itf_013_officer_buy_count_252d":           {"inputs": ["officer_buy_count"],                       "func": itf_013_officer_buy_count_252d},
    "itf_014_director_buy_count_63d":           {"inputs": ["director_buy_count"],                      "func": itf_014_director_buy_count_63d},
    "itf_015_director_buy_count_252d":          {"inputs": ["director_buy_count"],                      "func": itf_015_director_buy_count_252d},
    "itf_016_active_days_21d":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_016_active_days_21d},
    "itf_017_active_days_63d":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_017_active_days_63d},
    "itf_018_active_days_126d":                 {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_018_active_days_126d},
    "itf_019_active_days_252d":                 {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_019_active_days_252d},
    "itf_020_buy_active_days_63d":              {"inputs": ["insider_buy_count"],                       "func": itf_020_buy_active_days_63d},
    "itf_021_buy_active_days_252d":             {"inputs": ["insider_buy_count"],                       "func": itf_021_buy_active_days_252d},
    "itf_022_sell_active_days_63d":             {"inputs": ["insider_sell_count"],                      "func": itf_022_sell_active_days_63d},
    "itf_023_sell_active_days_252d":            {"inputs": ["insider_sell_count"],                      "func": itf_023_sell_active_days_252d},
    "itf_024_officer_buy_active_days_252d":     {"inputs": ["officer_buy_count"],                       "func": itf_024_officer_buy_active_days_252d},
    "itf_025_director_buy_active_days_252d":    {"inputs": ["director_buy_count"],                      "func": itf_025_director_buy_active_days_252d},
    "itf_026_days_since_last_any_txn":          {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_026_days_since_last_any_txn},
    "itf_027_days_since_last_buy":              {"inputs": ["insider_buy_count"],                       "func": itf_027_days_since_last_buy},
    "itf_028_days_since_last_sell":             {"inputs": ["insider_sell_count"],                      "func": itf_028_days_since_last_sell},
    "itf_029_days_since_last_officer_buy":      {"inputs": ["officer_buy_count"],                       "func": itf_029_days_since_last_officer_buy},
    "itf_030_days_since_last_director_buy":     {"inputs": ["director_buy_count"],                      "func": itf_030_days_since_last_director_buy},
    "itf_031_days_since_last_buy_21d_min":      {"inputs": ["insider_buy_count"],                       "func": itf_031_days_since_last_buy_21d_min},
    "itf_032_days_since_last_buy_63d_mean":     {"inputs": ["insider_buy_count"],                       "func": itf_032_days_since_last_buy_63d_mean},
    "itf_033_days_since_last_any_txn_63d_mean": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_033_days_since_last_any_txn_63d_mean},
    "itf_034_days_since_last_any_txn_252d_mean":{"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_034_days_since_last_any_txn_252d_mean},
    "itf_035_gap_shrinkage_buy_21v63":          {"inputs": ["insider_buy_count"],                       "func": itf_035_gap_shrinkage_buy_21v63},
    "itf_036_txn_rate_per_month_21d":           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_036_txn_rate_per_month_21d},
    "itf_037_buy_rate_per_day_63d":             {"inputs": ["insider_buy_count"],                       "func": itf_037_buy_rate_per_day_63d},
    "itf_038_sell_rate_per_day_63d":            {"inputs": ["insider_sell_count"],                      "func": itf_038_sell_rate_per_day_63d},
    "itf_039_txn_rate_per_day_252d":            {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_039_txn_rate_per_day_252d},
    "itf_040_active_day_density_21d":           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_040_active_day_density_21d},
    "itf_041_active_day_density_63d":           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_041_active_day_density_63d},
    "itf_042_active_day_density_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_042_active_day_density_252d},
    "itf_043_buy_day_density_63d":              {"inputs": ["insider_buy_count"],                       "func": itf_043_buy_day_density_63d},
    "itf_044_buy_day_density_252d":             {"inputs": ["insider_buy_count"],                       "func": itf_044_buy_day_density_252d},
    "itf_045_officer_buy_rate_252d":            {"inputs": ["officer_buy_count"],                       "func": itf_045_officer_buy_rate_252d},
    "itf_046_txn_accel_21v63":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_046_txn_accel_21v63},
    "itf_047_txn_accel_21v252":                 {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_047_txn_accel_21v252},
    "itf_048_txn_accel_63v252":                 {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_048_txn_accel_63v252},
    "itf_049_buy_accel_21v63":                  {"inputs": ["insider_buy_count"],                       "func": itf_049_buy_accel_21v63},
    "itf_050_buy_accel_63v252":                 {"inputs": ["insider_buy_count"],                       "func": itf_050_buy_accel_63v252},
    "itf_051_txn_accel_ratio_21v63":            {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_051_txn_accel_ratio_21v63},
    "itf_052_buy_accel_ratio_21v252":           {"inputs": ["insider_buy_count"],                       "func": itf_052_buy_accel_ratio_21v252},
    "itf_053_officer_buy_accel_21v252":         {"inputs": ["officer_buy_count"],                       "func": itf_053_officer_buy_accel_21v252},
    "itf_054_director_buy_accel_21v252":        {"inputs": ["director_buy_count"],                      "func": itf_054_director_buy_accel_21v252},
    "itf_055_txn_surge_21d_vs_504d_baseline":   {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_055_txn_surge_21d_vs_504d_baseline},
    "itf_056_buyers_21d":                       {"inputs": ["insider_buyers"],                          "func": itf_056_buyers_21d},
    "itf_057_buyers_63d":                       {"inputs": ["insider_buyers"],                          "func": itf_057_buyers_63d},
    "itf_058_buyers_252d":                      {"inputs": ["insider_buyers"],                          "func": itf_058_buyers_252d},
    "itf_059_sellers_63d":                      {"inputs": ["insider_sellers"],                         "func": itf_059_sellers_63d},
    "itf_060_sellers_252d":                     {"inputs": ["insider_sellers"],                         "func": itf_060_sellers_252d},
    "itf_061_total_participants_63d":           {"inputs": ["insider_buyers", "insider_sellers"],        "func": itf_061_total_participants_63d},
    "itf_062_total_participants_252d":          {"inputs": ["insider_buyers", "insider_sellers"],        "func": itf_062_total_participants_252d},
    "itf_063_buyer_accel_21v252":               {"inputs": ["insider_buyers"],                          "func": itf_063_buyer_accel_21v252},
    "itf_064_buyer_density_63d":                {"inputs": ["insider_buyers"],                          "func": itf_064_buyer_density_63d},
    "itf_065_buyer_density_252d":               {"inputs": ["insider_buyers"],                          "func": itf_065_buyer_density_252d},
    "itf_066_txn_zscore_63d":                   {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_066_txn_zscore_63d},
    "itf_067_txn_zscore_252d":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_067_txn_zscore_252d},
    "itf_068_buy_count_ewm_21":                 {"inputs": ["insider_buy_count"],                       "func": itf_068_buy_count_ewm_21},
    "itf_069_txn_count_ewm_63":                 {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_069_txn_count_ewm_63},
    "itf_070_txn_std_63d":                      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_070_txn_std_63d},
    "itf_071_txn_std_252d":                     {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_071_txn_std_252d},
    "itf_072_new_burst_after_quiet_21d":        {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_072_new_burst_after_quiet_21d},
    "itf_073_txn_pct_rank_252d":                {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_073_txn_pct_rank_252d},
    "itf_074_buy_count_pct_rank_252d":          {"inputs": ["insider_buy_count"],                       "func": itf_074_buy_count_pct_rank_252d},
    "itf_075_activity_composite_score":         {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"], "func": itf_075_activity_composite_score},
    "itf_151_sell_count_126d":                  {"inputs": ["insider_sell_count"],                                         "func": itf_151_sell_count_126d},
    "itf_152_sell_count_504d":                  {"inputs": ["insider_sell_count"],                                         "func": itf_152_sell_count_504d},
    "itf_153_net_txn_count_63d":                {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_153_net_txn_count_63d},
    "itf_154_net_txn_count_252d":               {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_154_net_txn_count_252d},
    "itf_155_buy_to_sell_ratio_63d":            {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_155_buy_to_sell_ratio_63d},
    "itf_156_buy_to_sell_ratio_252d":           {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_156_buy_to_sell_ratio_252d},
    "itf_157_sell_active_days_126d":            {"inputs": ["insider_sell_count"],                                         "func": itf_157_sell_active_days_126d},
    "itf_158_buy_active_days_126d":             {"inputs": ["insider_buy_count"],                                          "func": itf_158_buy_active_days_126d},
    "itf_159_net_buyer_density_63d":            {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_159_net_buyer_density_63d},
    "itf_160_sell_zscore_252d":                 {"inputs": ["insider_sell_count"],                                         "func": itf_160_sell_zscore_252d},
    "itf_161_sellers_21d":                      {"inputs": ["insider_sellers"],                                            "func": itf_161_sellers_21d},
    "itf_162_sellers_126d":                     {"inputs": ["insider_sellers"],                                            "func": itf_162_sellers_126d},
    "itf_163_buyers_126d":                      {"inputs": ["insider_buyers"],                                             "func": itf_163_buyers_126d},
    "itf_164_buyer_to_seller_ratio_63d":        {"inputs": ["insider_buyers", "insider_sellers"],                          "func": itf_164_buyer_to_seller_ratio_63d},
    "itf_165_buyer_to_seller_ratio_252d":       {"inputs": ["insider_buyers", "insider_sellers"],                          "func": itf_165_buyer_to_seller_ratio_252d},
    "itf_166_seller_density_63d":               {"inputs": ["insider_sellers"],                                            "func": itf_166_seller_density_63d},
    "itf_167_multi_seller_day_count_252d":      {"inputs": ["insider_sellers"],                                            "func": itf_167_multi_seller_day_count_252d},
    "itf_168_net_participants_63d":             {"inputs": ["insider_buyers", "insider_sellers"],                          "func": itf_168_net_participants_63d},
    "itf_169_officer_buy_count_126d":           {"inputs": ["officer_buy_count"],                                          "func": itf_169_officer_buy_count_126d},
    "itf_170_director_buy_count_126d":          {"inputs": ["director_buy_count"],                                         "func": itf_170_director_buy_count_126d},
    "itf_171_officer_buy_density_252d":         {"inputs": ["officer_buy_count"],                                          "func": itf_171_officer_buy_density_252d},
    "itf_172_director_buy_density_252d":        {"inputs": ["director_buy_count"],                                         "func": itf_172_director_buy_density_252d},
    "itf_173_officer_director_buy_count_126d":  {"inputs": ["officer_buy_count", "director_buy_count"],                    "func": itf_173_officer_director_buy_count_126d},
    "itf_174_officer_buy_pct_rank_63d":         {"inputs": ["officer_buy_count"],                                          "func": itf_174_officer_buy_pct_rank_63d},
    "itf_175_txn_count_126d_pct_of_504d_peak":  {"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_175_txn_count_126d_pct_of_504d_peak},
}
