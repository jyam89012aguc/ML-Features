"""
83_insider_buy_cluster — Base Features 001-100
Domain: insider buy clustering — multiple distinct insiders buying within a trailing window
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings to one row per (ticker, date).  These are EVENT-DRIVEN
flow series: most days are ZERO (no insider transaction filed); positive values
appear only on filing days.  Do NOT forward-fill — a transaction count is a
flow, not a stock.  All features aggregate over trailing windows with rolling
sums/counts.  The sparsity (mostly-zero) is correct and expected.

Canonical SF2 field names used in this file (lowercase):
    insider_buy_count, insider_buyers, insider_buy_value,
    officer_buy_count, director_buy_count, tenpct_buy_count

Feature numbering: ibc_001 .. ibc_100
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK   = 5     # 1 week
_TD_MO   = 21    # 1 month
_TD_QTR  = 63    # 1 quarter
_TD_2Q   = 126   # 2 quarters
_TD_YEAR = 252   # 1 year
_TD_2Y   = 504   # 2 years
_EPS     = 1e-9

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
    """Count of days with s > 0 in trailing w-day window."""
    return _rolling_sum((s > 0).astype(float), w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Distinct buyer counts over multiple windows ---

def ibc_001_distinct_buyers_21d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 21-day (monthly) window."""
    return _rolling_sum(insider_buyers, _TD_MO)


def ibc_002_distinct_buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 63-day (quarterly) window."""
    return _rolling_sum(insider_buyers, _TD_QTR)


def ibc_003_distinct_buyers_126d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 126-day (2-quarter) window."""
    return _rolling_sum(insider_buyers, _TD_2Q)


def ibc_004_distinct_buyers_252d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 252-day (annual) window."""
    return _rolling_sum(insider_buyers, _TD_YEAR)


def ibc_005_distinct_buyers_5d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 5-day (weekly) window."""
    return _rolling_sum(insider_buyers, _TD_WK)


def ibc_006_buyer_count_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transactions over trailing 21-day window."""
    return _rolling_sum(insider_buy_count, _TD_MO)


def ibc_007_buyer_count_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transactions over trailing 63-day window."""
    return _rolling_sum(insider_buy_count, _TD_QTR)


def ibc_008_buyer_count_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transactions over trailing 126-day window."""
    return _rolling_sum(insider_buy_count, _TD_2Q)


def ibc_009_buyer_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transactions over trailing 252-day window."""
    return _rolling_sum(insider_buy_count, _TD_YEAR)


def ibc_010_buyer_count_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transactions over trailing 504-day (2-year) window."""
    return _rolling_sum(insider_buy_count, _TD_2Y)


def ibc_011_officer_buyers_21d(officer_buy_count: pd.Series) -> pd.Series:
    """Total officer buy transactions over trailing 21-day window."""
    return _rolling_sum(officer_buy_count, _TD_MO)


def ibc_012_officer_buyers_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Total officer buy transactions over trailing 63-day window."""
    return _rolling_sum(officer_buy_count, _TD_QTR)


def ibc_013_director_buyers_21d(director_buy_count: pd.Series) -> pd.Series:
    """Total director buy transactions over trailing 21-day window."""
    return _rolling_sum(director_buy_count, _TD_MO)


def ibc_014_director_buyers_63d(director_buy_count: pd.Series) -> pd.Series:
    """Total director buy transactions over trailing 63-day window."""
    return _rolling_sum(director_buy_count, _TD_QTR)


def ibc_015_tenpct_buyers_63d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Total 10%-holder buy transactions over trailing 63-day window."""
    return _rolling_sum(tenpct_buy_count, _TD_QTR)


# --- Group B (016-030): Active-day density (days with any buy) ---

def ibc_016_active_buy_days_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one insider buy in trailing 21-day window."""
    return _active_days(insider_buy_count, _TD_MO)


def ibc_017_active_buy_days_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one insider buy in trailing 63-day window."""
    return _active_days(insider_buy_count, _TD_QTR)


def ibc_018_active_buy_days_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one insider buy in trailing 126-day window."""
    return _active_days(insider_buy_count, _TD_2Q)


def ibc_019_active_buy_days_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one insider buy in trailing 252-day window."""
    return _active_days(insider_buy_count, _TD_YEAR)


def ibc_020_buy_day_density_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 21 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_MO),
                     pd.Series(_TD_MO, index=insider_buy_count.index, dtype=float))


def ibc_021_buy_day_density_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_QTR),
                     pd.Series(_TD_QTR, index=insider_buy_count.index, dtype=float))


def ibc_022_buy_day_density_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_2Q),
                     pd.Series(_TD_2Q, index=insider_buy_count.index, dtype=float))


def ibc_023_buy_day_density_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_YEAR),
                     pd.Series(_TD_YEAR, index=insider_buy_count.index, dtype=float))


def ibc_024_active_officer_days_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one officer buy in trailing 63-day window."""
    return _active_days(officer_buy_count, _TD_QTR)


def ibc_025_active_director_days_63d(director_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one director buy in trailing 63-day window."""
    return _active_days(director_buy_count, _TD_QTR)


def ibc_026_active_buyer_days_21d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with at least one distinct buyer reported in trailing 21 days."""
    return _active_days(insider_buyers, _TD_MO)


def ibc_027_active_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with at least one distinct buyer reported in trailing 63 days."""
    return _active_days(insider_buyers, _TD_QTR)


def ibc_028_active_buyer_days_126d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with at least one distinct buyer reported in trailing 126 days."""
    return _active_days(insider_buyers, _TD_2Q)


def ibc_029_active_buyer_days_252d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with at least one distinct buyer reported in trailing 252 days."""
    return _active_days(insider_buyers, _TD_YEAR)


def ibc_030_active_tenpct_days_63d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one 10%-holder buy in trailing 63-day window."""
    return _active_days(tenpct_buy_count, _TD_QTR)


# --- Group C (031-045): Cluster intensity — buyers per active day ---

def ibc_031_avg_buyers_per_active_day_21d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average distinct buyers per active buy day over trailing 21 days."""
    active = _active_days(insider_buy_count, _TD_MO).replace(0, np.nan)
    return _rolling_sum(insider_buyers, _TD_MO) / active


def ibc_032_avg_buyers_per_active_day_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average distinct buyers per active buy day over trailing 63 days."""
    active = _active_days(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(insider_buyers, _TD_QTR) / active


def ibc_033_avg_buyers_per_active_day_126d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average distinct buyers per active buy day over trailing 126 days."""
    active = _active_days(insider_buy_count, _TD_2Q).replace(0, np.nan)
    return _rolling_sum(insider_buyers, _TD_2Q) / active


def ibc_034_avg_buys_per_active_day_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per active buy day over trailing 21 days."""
    active = _active_days(insider_buy_count, _TD_MO).replace(0, np.nan)
    return _rolling_sum(insider_buy_count, _TD_MO) / active


def ibc_035_avg_buys_per_active_day_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per active buy day over trailing 63 days."""
    active = _active_days(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(insider_buy_count, _TD_QTR) / active


def ibc_036_officer_dir_joint_buy_days_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Days where BOTH an officer and a director bought in the same 21-day window.
    Proxy: minimum of their rolling active-day counts in the window."""
    o_active = _active_days(officer_buy_count, _TD_MO)
    d_active = _active_days(director_buy_count, _TD_MO)
    return o_active.where(o_active < d_active, d_active)


def ibc_037_officer_dir_joint_buy_days_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Days where BOTH an officer and a director bought in the same 63-day window."""
    o_active = _active_days(officer_buy_count, _TD_QTR)
    d_active = _active_days(director_buy_count, _TD_QTR)
    return o_active.where(o_active < d_active, d_active)


def ibc_038_officer_dir_combined_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy transaction count over trailing 21 days."""
    return _rolling_sum(officer_buy_count, _TD_MO) + _rolling_sum(director_buy_count, _TD_MO)


def ibc_039_officer_dir_combined_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy transaction count over trailing 63 days."""
    return _rolling_sum(officer_buy_count, _TD_QTR) + _rolling_sum(director_buy_count, _TD_QTR)


def ibc_040_multi_buyer_days_21d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 2+ distinct buyers reported in trailing 21-day window."""
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_MO)


def ibc_041_multi_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 2+ distinct buyers reported in trailing 63-day window."""
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_QTR)


def ibc_042_multi_buyer_days_126d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 2+ distinct buyers reported in trailing 126-day window."""
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_2Q)


def ibc_043_triple_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 3+ distinct buyers in trailing 63-day window."""
    return _rolling_sum((insider_buyers >= 3).astype(float), _TD_QTR)


def ibc_044_triple_buyer_days_126d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 3+ distinct buyers in trailing 126-day window."""
    return _rolling_sum((insider_buyers >= 3).astype(float), _TD_2Q)


def ibc_045_peak_buyers_single_day_21d(insider_buyers: pd.Series) -> pd.Series:
    """Maximum distinct buyers on any single day in the trailing 21-day window."""
    return _rolling_max(insider_buyers, _TD_MO)


# --- Group D (046-060): Cluster breadth ratios and normalized scores ---

def ibc_046_peak_buyers_single_day_63d(insider_buyers: pd.Series) -> pd.Series:
    """Maximum distinct buyers on any single day in the trailing 63-day window."""
    return _rolling_max(insider_buyers, _TD_QTR)


def ibc_047_peak_buyers_single_day_126d(insider_buyers: pd.Series) -> pd.Series:
    """Maximum distinct buyers on any single day in the trailing 126-day window."""
    return _rolling_max(insider_buyers, _TD_2Q)


def ibc_048_peak_buys_single_day_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Maximum buy transactions on any single day in trailing 21-day window."""
    return _rolling_max(insider_buy_count, _TD_MO)


def ibc_049_peak_buys_single_day_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Maximum buy transactions on any single day in trailing 63-day window."""
    return _rolling_max(insider_buy_count, _TD_QTR)


def ibc_050_buyer_breadth_ratio_21_to_63(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 21-day buyer count to 63-day buyer count; captures recency concentration."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    b63 = _rolling_sum(insider_buyers, _TD_QTR).replace(0, np.nan)
    return b21 / b63


def ibc_051_buyer_breadth_ratio_63_to_252(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 63-day buyer count to 252-day buyer count."""
    b63  = _rolling_sum(insider_buyers, _TD_QTR)
    b252 = _rolling_sum(insider_buyers, _TD_YEAR).replace(0, np.nan)
    return b63 / b252


def ibc_052_buyer_breadth_ratio_21_to_252(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 21-day buyer count to 252-day buyer count; extreme recency focus."""
    b21  = _rolling_sum(insider_buyers, _TD_MO)
    b252 = _rolling_sum(insider_buyers, _TD_YEAR).replace(0, np.nan)
    return b21 / b252


def ibc_053_officer_to_total_buyer_ratio_63d(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day buy transactions that were by officers."""
    total = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(officer_buy_count, _TD_QTR) / total


def ibc_054_director_to_total_buyer_ratio_63d(director_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day buy transactions that were by directors."""
    total = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(director_buy_count, _TD_QTR) / total


def ibc_055_tenpct_to_total_buyer_ratio_63d(tenpct_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day buy transactions by 10%-holders."""
    total = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(tenpct_buy_count, _TD_QTR) / total


def ibc_056_buyer_zscore_63d_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of 63-day buyer count relative to trailing 252-day distribution."""
    b63  = _rolling_sum(insider_buyers, _TD_QTR)
    return _zscore_rolling(b63, _TD_YEAR)


def ibc_057_buyer_zscore_21d_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of 21-day buyer count relative to trailing 252-day distribution."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    return _zscore_rolling(b21, _TD_YEAR)


def ibc_058_buy_count_zscore_21d_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of 21-day buy-transaction count relative to trailing 252-day distribution."""
    b21 = _rolling_sum(insider_buy_count, _TD_MO)
    return _zscore_rolling(b21, _TD_YEAR)


def ibc_059_buy_count_zscore_63d_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of 63-day buy-transaction count relative to trailing 252-day distribution."""
    b63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return _zscore_rolling(b63, _TD_YEAR)


def ibc_060_buy_day_density_ratio_21_to_63(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21-day buy-day density to 63-day buy-day density."""
    d21 = _safe_div(_active_days(insider_buy_count, _TD_MO),
                    pd.Series(float(_TD_MO), index=insider_buy_count.index))
    d63 = _safe_div(_active_days(insider_buy_count, _TD_QTR),
                    pd.Series(float(_TD_QTR), index=insider_buy_count.index))
    return _safe_div(d21, d63)


# --- Group E (061-075): Recency, streaks, and composite cluster signals ---

def ibc_061_days_since_last_buy(insider_buy_count: pd.Series) -> pd.Series:
    """
    Count of trading days since the most recent insider buy filing.
    0 on a day with a filing; increases daily otherwise.
    """
    has_buy = (insider_buy_count > 0).astype(int)
    arr = has_buy.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = 0 if arr[i] else (out[i - 1] + 1)
    return pd.Series(out, index=insider_buy_count.index)


def ibc_062_days_since_last_multi_buyer_day(insider_buyers: pd.Series) -> pd.Series:
    """
    Count of trading days since the most recent day with 2+ distinct buyers.
    """
    multi = (insider_buyers >= 2).astype(int)
    arr = multi.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = 0 if arr[i] else (out[i - 1] + 1)
    return pd.Series(out, index=insider_buyers.index)


def ibc_063_consecutive_weeks_with_buy(insider_buy_count: pd.Series) -> pd.Series:
    """
    Current consecutive-week streak of weeks containing at least one insider buy.
    Uses 5-day rolling sums stepped at each row.
    """
    weekly = _rolling_sum(insider_buy_count, _TD_WK)
    had_buy = (weekly > 0).astype(int)
    arr = had_buy.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) if arr[i] else 0.0
    return pd.Series(out, index=insider_buy_count.index)


def ibc_064_consecutive_months_with_buy(insider_buy_count: pd.Series) -> pd.Series:
    """
    Current consecutive-month streak of months containing at least one insider buy.
    Uses 21-day rolling sums stepped at each row.
    """
    monthly = _rolling_sum(insider_buy_count, _TD_MO)
    had_buy = (monthly > 0).astype(int)
    arr = had_buy.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) if arr[i] else 0.0
    return pd.Series(out, index=insider_buy_count.index)


def ibc_065_buy_cluster_flag_21d(insider_buyers: pd.Series) -> pd.Series:
    """
    Binary flag: 1 if at least 2 distinct buyers bought within the trailing 21-day window.
    Represents a minimal cluster signal.
    """
    return (_rolling_sum(insider_buyers, _TD_MO) >= 2).astype(float)


def ibc_066_buy_cluster_flag_63d(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: 1 if at least 2 distinct buyers bought within trailing 63 days."""
    return (_rolling_sum(insider_buyers, _TD_QTR) >= 2).astype(float)


def ibc_067_strong_cluster_flag_21d(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: 1 if at least 3 distinct buyers bought within trailing 21 days."""
    return (_rolling_sum(insider_buyers, _TD_MO) >= 3).astype(float)


def ibc_068_strong_cluster_flag_63d(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: 1 if at least 3 distinct buyers bought within trailing 63 days."""
    return (_rolling_sum(insider_buyers, _TD_QTR) >= 3).astype(float)


def ibc_069_officer_dir_dual_flag_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Binary flag: 1 if both officer(s) and director(s) bought within trailing 21 days."""
    o = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_MO) > 0).astype(float)
    return o * d


def ibc_070_officer_dir_dual_flag_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Binary flag: 1 if both officer(s) and director(s) bought within trailing 63 days."""
    o = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    return o * d


def ibc_071_all_three_roles_flag_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                      tenpct_buy_count: pd.Series) -> pd.Series:
    """Binary flag: 1 if officers, directors, AND 10%-holders all bought in trailing 63 days."""
    o = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_QTR) > 0).astype(float)
    return o * d * t


def ibc_072_buy_cluster_breadth_score_63d(insider_buyers: pd.Series, officer_buy_count: pd.Series,
                                           director_buy_count: pd.Series) -> pd.Series:
    """
    Composite breadth score over 63 days:
    sum of [distinct buyers >=2] + [officer active] + [director active], range 0-3.
    """
    buyers_flag   = (_rolling_sum(insider_buyers, _TD_QTR) >= 2).astype(float)
    officer_flag  = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    director_flag = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    return buyers_flag + officer_flag + director_flag


def ibc_073_buy_cluster_intensity_21d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    Cluster intensity over 21 days: product of (distinct buyers) x (active days).
    High when many buyers and many days both cluster together.
    """
    buyers   = _rolling_sum(insider_buyers, _TD_MO)
    act_days = _active_days(insider_buy_count, _TD_MO)
    return buyers * act_days


def ibc_074_buy_cluster_intensity_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    Cluster intensity over 63 days: product of (distinct buyers) x (active days).
    """
    buyers   = _rolling_sum(insider_buyers, _TD_QTR)
    act_days = _active_days(insider_buy_count, _TD_QTR)
    return buyers * act_days


def ibc_075_rolling_buyer_rank_pct_63d(insider_buyers: pd.Series) -> pd.Series:
    """
    Percentile rank of the current daily insider_buyers value within
    a trailing 63-day window.  High rank = unusual spike in buying breadth.
    """
    return _rolling_rank_pct(insider_buyers, _TD_QTR)


# --- Group K (151-175): Extended windows, new transforms, composite signals ---

def ibc_151_distinct_buyers_504d(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers over trailing 504-day (2-year) window."""
    return _rolling_sum(insider_buyers, _TD_2Y)


def ibc_152_officer_buyers_126d(officer_buy_count: pd.Series) -> pd.Series:
    """Total officer buy transactions over trailing 126-day (2-quarter) window."""
    return _rolling_sum(officer_buy_count, _TD_2Q)


def ibc_153_director_buyers_126d(director_buy_count: pd.Series) -> pd.Series:
    """Total director buy transactions over trailing 126-day window."""
    return _rolling_sum(director_buy_count, _TD_2Q)


def ibc_154_tenpct_buyers_126d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Total 10%-holder buy transactions over trailing 126-day window."""
    return _rolling_sum(tenpct_buy_count, _TD_2Q)


def ibc_155_tenpct_buyers_252d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Total 10%-holder buy transactions over trailing 252-day (annual) window."""
    return _rolling_sum(tenpct_buy_count, _TD_YEAR)


def ibc_156_active_buy_days_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one insider buy in trailing 504-day window."""
    return _active_days(insider_buy_count, _TD_2Y)


def ibc_157_active_officer_days_21d(officer_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one officer buy in trailing 21-day window."""
    return _active_days(officer_buy_count, _TD_MO)


def ibc_158_active_director_days_21d(director_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one director buy in trailing 21-day window."""
    return _active_days(director_buy_count, _TD_MO)


def ibc_159_active_tenpct_days_21d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one 10%-holder buy in trailing 21-day window."""
    return _active_days(tenpct_buy_count, _TD_MO)


def ibc_160_active_tenpct_days_252d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of days with at least one 10%-holder buy in trailing 252-day window."""
    return _active_days(tenpct_buy_count, _TD_YEAR)


def ibc_161_buy_day_density_5d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 5 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_WK),
                     pd.Series(float(_TD_WK), index=insider_buy_count.index))


def ibc_162_buy_day_density_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing 504 days that contained at least one insider buy."""
    return _safe_div(_active_days(insider_buy_count, _TD_2Y),
                     pd.Series(float(_TD_2Y), index=insider_buy_count.index))


def ibc_163_officer_dir_combined_126d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy transaction count over trailing 126 days."""
    return _rolling_sum(officer_buy_count, _TD_2Q) + _rolling_sum(director_buy_count, _TD_2Q)


def ibc_164_all_roles_combined_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                    tenpct_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director + 10%-holder buy count over trailing 21 days."""
    return (_rolling_sum(officer_buy_count, _TD_MO)
            + _rolling_sum(director_buy_count, _TD_MO)
            + _rolling_sum(tenpct_buy_count, _TD_MO))


def ibc_165_multi_buyer_days_252d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 2+ distinct buyers reported in trailing 252-day window."""
    return _rolling_sum((insider_buyers >= 2).astype(float), _TD_YEAR)


def ibc_166_quad_buyer_days_63d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days with 4+ distinct buyers in trailing 63-day window."""
    return _rolling_sum((insider_buyers >= 4).astype(float), _TD_QTR)


def ibc_167_peak_buyers_single_day_252d(insider_buyers: pd.Series) -> pd.Series:
    """Maximum distinct buyers on any single day in the trailing 252-day window."""
    return _rolling_max(insider_buyers, _TD_YEAR)


def ibc_168_peak_buys_single_day_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Maximum buy transactions on any single day in trailing 126-day window."""
    return _rolling_max(insider_buy_count, _TD_2Q)


def ibc_169_buyer_breadth_ratio_126_to_252(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 126-day buyer count to 252-day buyer count."""
    b126 = _rolling_sum(insider_buyers, _TD_2Q)
    b252 = _rolling_sum(insider_buyers, _TD_YEAR).replace(0, np.nan)
    return b126 / b252


def ibc_170_officer_to_total_buyer_ratio_21d(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 21-day buy transactions that were by officers."""
    total = _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan)
    return _rolling_sum(officer_buy_count, _TD_MO) / total


def ibc_171_director_to_total_buyer_ratio_21d(director_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 21-day buy transactions that were by directors."""
    total = _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan)
    return _rolling_sum(director_buy_count, _TD_MO) / total


def ibc_172_buy_count_zscore_126d_in_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of 126-day buy-transaction count relative to trailing 504-day distribution."""
    b126 = _rolling_sum(insider_buy_count, _TD_2Q)
    return _zscore_rolling(b126, _TD_2Y)


def ibc_173_cluster_intensity_126d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Cluster intensity over 126 days: product of (distinct buyers) x (active days)."""
    buyers   = _rolling_sum(insider_buyers, _TD_2Q)
    act_days = _active_days(insider_buy_count, _TD_2Q)
    return buyers * act_days


def ibc_174_buy_cluster_breadth_score_21d(insider_buyers: pd.Series, officer_buy_count: pd.Series,
                                           director_buy_count: pd.Series) -> pd.Series:
    """Composite breadth score over 21 days: [buyers>=2] + [officer active] + [director active], range 0-3."""
    buyers_flag   = (_rolling_sum(insider_buyers, _TD_MO) >= 2).astype(float)
    officer_flag  = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    director_flag = (_rolling_sum(director_buy_count, _TD_MO) > 0).astype(float)
    return buyers_flag + officer_flag + director_flag


def ibc_175_rolling_buyer_rank_pct_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of daily insider_buyers within a trailing 252-day window."""
    return _rolling_rank_pct(insider_buyers, _TD_YEAR)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_BUY_CLUSTER_REGISTRY_001_075 = {
    "ibc_001_distinct_buyers_21d":             {"inputs": ["insider_buyers"],                                       "func": ibc_001_distinct_buyers_21d},
    "ibc_002_distinct_buyers_63d":             {"inputs": ["insider_buyers"],                                       "func": ibc_002_distinct_buyers_63d},
    "ibc_003_distinct_buyers_126d":            {"inputs": ["insider_buyers"],                                       "func": ibc_003_distinct_buyers_126d},
    "ibc_004_distinct_buyers_252d":            {"inputs": ["insider_buyers"],                                       "func": ibc_004_distinct_buyers_252d},
    "ibc_005_distinct_buyers_5d":              {"inputs": ["insider_buyers"],                                       "func": ibc_005_distinct_buyers_5d},
    "ibc_006_buyer_count_21d":                 {"inputs": ["insider_buy_count"],                                    "func": ibc_006_buyer_count_21d},
    "ibc_007_buyer_count_63d":                 {"inputs": ["insider_buy_count"],                                    "func": ibc_007_buyer_count_63d},
    "ibc_008_buyer_count_126d":                {"inputs": ["insider_buy_count"],                                    "func": ibc_008_buyer_count_126d},
    "ibc_009_buyer_count_252d":                {"inputs": ["insider_buy_count"],                                    "func": ibc_009_buyer_count_252d},
    "ibc_010_buyer_count_504d":                {"inputs": ["insider_buy_count"],                                    "func": ibc_010_buyer_count_504d},
    "ibc_011_officer_buyers_21d":              {"inputs": ["officer_buy_count"],                                    "func": ibc_011_officer_buyers_21d},
    "ibc_012_officer_buyers_63d":              {"inputs": ["officer_buy_count"],                                    "func": ibc_012_officer_buyers_63d},
    "ibc_013_director_buyers_21d":             {"inputs": ["director_buy_count"],                                   "func": ibc_013_director_buyers_21d},
    "ibc_014_director_buyers_63d":             {"inputs": ["director_buy_count"],                                   "func": ibc_014_director_buyers_63d},
    "ibc_015_tenpct_buyers_63d":               {"inputs": ["tenpct_buy_count"],                                     "func": ibc_015_tenpct_buyers_63d},
    "ibc_016_active_buy_days_21d":             {"inputs": ["insider_buy_count"],                                    "func": ibc_016_active_buy_days_21d},
    "ibc_017_active_buy_days_63d":             {"inputs": ["insider_buy_count"],                                    "func": ibc_017_active_buy_days_63d},
    "ibc_018_active_buy_days_126d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_018_active_buy_days_126d},
    "ibc_019_active_buy_days_252d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_019_active_buy_days_252d},
    "ibc_020_buy_day_density_21d":             {"inputs": ["insider_buy_count"],                                    "func": ibc_020_buy_day_density_21d},
    "ibc_021_buy_day_density_63d":             {"inputs": ["insider_buy_count"],                                    "func": ibc_021_buy_day_density_63d},
    "ibc_022_buy_day_density_126d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_022_buy_day_density_126d},
    "ibc_023_buy_day_density_252d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_023_buy_day_density_252d},
    "ibc_024_active_officer_days_63d":         {"inputs": ["officer_buy_count"],                                    "func": ibc_024_active_officer_days_63d},
    "ibc_025_active_director_days_63d":        {"inputs": ["director_buy_count"],                                   "func": ibc_025_active_director_days_63d},
    "ibc_026_active_buyer_days_21d":           {"inputs": ["insider_buyers"],                                       "func": ibc_026_active_buyer_days_21d},
    "ibc_027_active_buyer_days_63d":           {"inputs": ["insider_buyers"],                                       "func": ibc_027_active_buyer_days_63d},
    "ibc_028_active_buyer_days_126d":          {"inputs": ["insider_buyers"],                                       "func": ibc_028_active_buyer_days_126d},
    "ibc_029_active_buyer_days_252d":          {"inputs": ["insider_buyers"],                                       "func": ibc_029_active_buyer_days_252d},
    "ibc_030_active_tenpct_days_63d":          {"inputs": ["tenpct_buy_count"],                                     "func": ibc_030_active_tenpct_days_63d},
    "ibc_031_avg_buyers_per_active_day_21d":   {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_031_avg_buyers_per_active_day_21d},
    "ibc_032_avg_buyers_per_active_day_63d":   {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_032_avg_buyers_per_active_day_63d},
    "ibc_033_avg_buyers_per_active_day_126d":  {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_033_avg_buyers_per_active_day_126d},
    "ibc_034_avg_buys_per_active_day_21d":     {"inputs": ["insider_buy_count"],                                    "func": ibc_034_avg_buys_per_active_day_21d},
    "ibc_035_avg_buys_per_active_day_63d":     {"inputs": ["insider_buy_count"],                                    "func": ibc_035_avg_buys_per_active_day_63d},
    "ibc_036_officer_dir_joint_buy_days_21d":  {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_036_officer_dir_joint_buy_days_21d},
    "ibc_037_officer_dir_joint_buy_days_63d":  {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_037_officer_dir_joint_buy_days_63d},
    "ibc_038_officer_dir_combined_21d":        {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_038_officer_dir_combined_21d},
    "ibc_039_officer_dir_combined_63d":        {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_039_officer_dir_combined_63d},
    "ibc_040_multi_buyer_days_21d":            {"inputs": ["insider_buyers"],                                       "func": ibc_040_multi_buyer_days_21d},
    "ibc_041_multi_buyer_days_63d":            {"inputs": ["insider_buyers"],                                       "func": ibc_041_multi_buyer_days_63d},
    "ibc_042_multi_buyer_days_126d":           {"inputs": ["insider_buyers"],                                       "func": ibc_042_multi_buyer_days_126d},
    "ibc_043_triple_buyer_days_63d":           {"inputs": ["insider_buyers"],                                       "func": ibc_043_triple_buyer_days_63d},
    "ibc_044_triple_buyer_days_126d":          {"inputs": ["insider_buyers"],                                       "func": ibc_044_triple_buyer_days_126d},
    "ibc_045_peak_buyers_single_day_21d":      {"inputs": ["insider_buyers"],                                       "func": ibc_045_peak_buyers_single_day_21d},
    "ibc_046_peak_buyers_single_day_63d":      {"inputs": ["insider_buyers"],                                       "func": ibc_046_peak_buyers_single_day_63d},
    "ibc_047_peak_buyers_single_day_126d":     {"inputs": ["insider_buyers"],                                       "func": ibc_047_peak_buyers_single_day_126d},
    "ibc_048_peak_buys_single_day_21d":        {"inputs": ["insider_buy_count"],                                    "func": ibc_048_peak_buys_single_day_21d},
    "ibc_049_peak_buys_single_day_63d":        {"inputs": ["insider_buy_count"],                                    "func": ibc_049_peak_buys_single_day_63d},
    "ibc_050_buyer_breadth_ratio_21_to_63":    {"inputs": ["insider_buyers"],                                       "func": ibc_050_buyer_breadth_ratio_21_to_63},
    "ibc_051_buyer_breadth_ratio_63_to_252":   {"inputs": ["insider_buyers"],                                       "func": ibc_051_buyer_breadth_ratio_63_to_252},
    "ibc_052_buyer_breadth_ratio_21_to_252":   {"inputs": ["insider_buyers"],                                       "func": ibc_052_buyer_breadth_ratio_21_to_252},
    "ibc_053_officer_to_total_buyer_ratio_63d":  {"inputs": ["officer_buy_count", "insider_buy_count"],             "func": ibc_053_officer_to_total_buyer_ratio_63d},
    "ibc_054_director_to_total_buyer_ratio_63d": {"inputs": ["director_buy_count", "insider_buy_count"],            "func": ibc_054_director_to_total_buyer_ratio_63d},
    "ibc_055_tenpct_to_total_buyer_ratio_63d":   {"inputs": ["tenpct_buy_count", "insider_buy_count"],              "func": ibc_055_tenpct_to_total_buyer_ratio_63d},
    "ibc_056_buyer_zscore_63d_in_252d":        {"inputs": ["insider_buyers"],                                       "func": ibc_056_buyer_zscore_63d_in_252d},
    "ibc_057_buyer_zscore_21d_in_252d":        {"inputs": ["insider_buyers"],                                       "func": ibc_057_buyer_zscore_21d_in_252d},
    "ibc_058_buy_count_zscore_21d_in_252d":    {"inputs": ["insider_buy_count"],                                    "func": ibc_058_buy_count_zscore_21d_in_252d},
    "ibc_059_buy_count_zscore_63d_in_252d":    {"inputs": ["insider_buy_count"],                                    "func": ibc_059_buy_count_zscore_63d_in_252d},
    "ibc_060_buy_day_density_ratio_21_to_63":  {"inputs": ["insider_buy_count"],                                    "func": ibc_060_buy_day_density_ratio_21_to_63},
    "ibc_061_days_since_last_buy":             {"inputs": ["insider_buy_count"],                                    "func": ibc_061_days_since_last_buy},
    "ibc_062_days_since_last_multi_buyer_day": {"inputs": ["insider_buyers"],                                       "func": ibc_062_days_since_last_multi_buyer_day},
    "ibc_063_consecutive_weeks_with_buy":      {"inputs": ["insider_buy_count"],                                    "func": ibc_063_consecutive_weeks_with_buy},
    "ibc_064_consecutive_months_with_buy":     {"inputs": ["insider_buy_count"],                                    "func": ibc_064_consecutive_months_with_buy},
    "ibc_065_buy_cluster_flag_21d":            {"inputs": ["insider_buyers"],                                       "func": ibc_065_buy_cluster_flag_21d},
    "ibc_066_buy_cluster_flag_63d":            {"inputs": ["insider_buyers"],                                       "func": ibc_066_buy_cluster_flag_63d},
    "ibc_067_strong_cluster_flag_21d":         {"inputs": ["insider_buyers"],                                       "func": ibc_067_strong_cluster_flag_21d},
    "ibc_068_strong_cluster_flag_63d":         {"inputs": ["insider_buyers"],                                       "func": ibc_068_strong_cluster_flag_63d},
    "ibc_069_officer_dir_dual_flag_21d":       {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_069_officer_dir_dual_flag_21d},
    "ibc_070_officer_dir_dual_flag_63d":       {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_070_officer_dir_dual_flag_63d},
    "ibc_071_all_three_roles_flag_63d":        {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_071_all_three_roles_flag_63d},
    "ibc_072_buy_cluster_breadth_score_63d":   {"inputs": ["insider_buyers", "officer_buy_count", "director_buy_count"],   "func": ibc_072_buy_cluster_breadth_score_63d},
    "ibc_073_buy_cluster_intensity_21d":       {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_073_buy_cluster_intensity_21d},
    "ibc_074_buy_cluster_intensity_63d":       {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_074_buy_cluster_intensity_63d},
    "ibc_075_rolling_buyer_rank_pct_63d":      {"inputs": ["insider_buyers"],                                       "func": ibc_075_rolling_buyer_rank_pct_63d},
    # --- New features 151-175 ---
    "ibc_151_distinct_buyers_504d":            {"inputs": ["insider_buyers"],                                       "func": ibc_151_distinct_buyers_504d},
    "ibc_152_officer_buyers_126d":             {"inputs": ["officer_buy_count"],                                    "func": ibc_152_officer_buyers_126d},
    "ibc_153_director_buyers_126d":            {"inputs": ["director_buy_count"],                                   "func": ibc_153_director_buyers_126d},
    "ibc_154_tenpct_buyers_126d":              {"inputs": ["tenpct_buy_count"],                                     "func": ibc_154_tenpct_buyers_126d},
    "ibc_155_tenpct_buyers_252d":              {"inputs": ["tenpct_buy_count"],                                     "func": ibc_155_tenpct_buyers_252d},
    "ibc_156_active_buy_days_504d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_156_active_buy_days_504d},
    "ibc_157_active_officer_days_21d":         {"inputs": ["officer_buy_count"],                                    "func": ibc_157_active_officer_days_21d},
    "ibc_158_active_director_days_21d":        {"inputs": ["director_buy_count"],                                   "func": ibc_158_active_director_days_21d},
    "ibc_159_active_tenpct_days_21d":          {"inputs": ["tenpct_buy_count"],                                     "func": ibc_159_active_tenpct_days_21d},
    "ibc_160_active_tenpct_days_252d":         {"inputs": ["tenpct_buy_count"],                                     "func": ibc_160_active_tenpct_days_252d},
    "ibc_161_buy_day_density_5d":              {"inputs": ["insider_buy_count"],                                    "func": ibc_161_buy_day_density_5d},
    "ibc_162_buy_day_density_504d":            {"inputs": ["insider_buy_count"],                                    "func": ibc_162_buy_day_density_504d},
    "ibc_163_officer_dir_combined_126d":       {"inputs": ["officer_buy_count", "director_buy_count"],              "func": ibc_163_officer_dir_combined_126d},
    "ibc_164_all_roles_combined_21d":          {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_164_all_roles_combined_21d},
    "ibc_165_multi_buyer_days_252d":           {"inputs": ["insider_buyers"],                                       "func": ibc_165_multi_buyer_days_252d},
    "ibc_166_quad_buyer_days_63d":             {"inputs": ["insider_buyers"],                                       "func": ibc_166_quad_buyer_days_63d},
    "ibc_167_peak_buyers_single_day_252d":     {"inputs": ["insider_buyers"],                                       "func": ibc_167_peak_buyers_single_day_252d},
    "ibc_168_peak_buys_single_day_126d":       {"inputs": ["insider_buy_count"],                                    "func": ibc_168_peak_buys_single_day_126d},
    "ibc_169_buyer_breadth_ratio_126_to_252":  {"inputs": ["insider_buyers"],                                       "func": ibc_169_buyer_breadth_ratio_126_to_252},
    "ibc_170_officer_to_total_buyer_ratio_21d": {"inputs": ["officer_buy_count", "insider_buy_count"],              "func": ibc_170_officer_to_total_buyer_ratio_21d},
    "ibc_171_director_to_total_buyer_ratio_21d": {"inputs": ["director_buy_count", "insider_buy_count"],            "func": ibc_171_director_to_total_buyer_ratio_21d},
    "ibc_172_buy_count_zscore_126d_in_504d":   {"inputs": ["insider_buy_count"],                                    "func": ibc_172_buy_count_zscore_126d_in_504d},
    "ibc_173_cluster_intensity_126d":          {"inputs": ["insider_buyers", "insider_buy_count"],                  "func": ibc_173_cluster_intensity_126d},
    "ibc_174_buy_cluster_breadth_score_21d":   {"inputs": ["insider_buyers", "officer_buy_count", "director_buy_count"], "func": ibc_174_buy_cluster_breadth_score_21d},
    "ibc_175_rolling_buyer_rank_pct_252d":     {"inputs": ["insider_buyers"],                                       "func": ibc_175_rolling_buyer_rank_pct_252d},
}
