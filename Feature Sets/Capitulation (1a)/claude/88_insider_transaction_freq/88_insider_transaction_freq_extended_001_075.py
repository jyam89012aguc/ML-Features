"""
88_insider_transaction_freq — Extended Features 001-075
Domain: frequency, rate, and acceleration of insider trading ACTIVITY —
        additional angles: inter-event gap statistics, clustering/burstiness,
        longer/shorter windows, regularity, quiet-period detection, role-mix
        frequency, percentile/z-score and composite variants not in the base
        files.
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Series Contract
--------------------------------------
Inputs are daily-frequency pandas Series derived from Sharadar SF2 insider
transaction filings, aggregated to one row per (ticker, date).  Most days
carry ZERO — the series are event-driven and NOT forward-filled.  Feature
functions aggregate over trailing rolling windows using rolling SUMS and
COUNTS; they do NOT forward-fill gaps.  Trading-day conventions:
  5 = week, 21 = month, 63 = quarter, 126 = 2 quarters, 252 = year, 504 = 2y.

Field names used (lowercase, identical to the folder's base files):
  insider_buy_count, insider_sell_count, officer_buy_count,
  director_buy_count, insider_buyers, insider_sellers

All functions look strictly backward via .shift(positive_int), .rolling(),
or .expanding().  No negative shifts, no iloc[i+n].
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
    """Backward-only: trading days since the most recent nonzero (>0) value.
    NaN until the first nonzero ever appears; NaN throughout an all-zero series."""
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


def _streak_false(cond: pd.Series) -> pd.Series:
    """Count of consecutive trailing False (zero-activity) values up to each row."""
    return _streak_true(~cond.astype(bool))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Inter-event gap statistics ---

def itf_ext_001_current_quiet_run_any_txn(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Length of the current consecutive-day run with zero insider transactions."""
    any_txn = (insider_buy_count + insider_sell_count) > 0
    return _streak_false(any_txn)


def itf_ext_002_current_quiet_run_buys(insider_buy_count: pd.Series) -> pd.Series:
    """Length of the current consecutive-day run with zero insider buys."""
    return _streak_false(insider_buy_count > 0)


def itf_ext_003_current_quiet_run_sells(insider_sell_count: pd.Series) -> pd.Series:
    """Length of the current consecutive-day run with zero insider sells."""
    return _streak_false(insider_sell_count > 0)


def itf_ext_004_max_gap_any_txn_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Longest days-since-last-transaction observed within the trailing 252-day window."""
    any_txn = insider_buy_count + insider_sell_count
    return _rolling_max(_days_since_last_nonzero(any_txn), _TD_YEAR)


def itf_ext_005_max_gap_buys_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Longest days-since-last-buy observed within the trailing 252-day window."""
    return _rolling_max(_days_since_last_nonzero(insider_buy_count), _TD_YEAR)


def itf_ext_006_mean_gap_any_txn_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """504-day mean of days-since-last-transaction (average inter-event gap)."""
    any_txn = insider_buy_count + insider_sell_count
    return _rolling_mean(_days_since_last_nonzero(any_txn), _TD_2Y)


def itf_ext_007_gap_dispersion_buys_252d(insider_buy_count: pd.Series) -> pd.Series:
    """252-day std of days-since-last-buy — irregularity of buy timing."""
    return _rolling_std(_days_since_last_nonzero(insider_buy_count), _TD_YEAR)


def itf_ext_008_gap_shrinking_flag(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """1 when the 21-day mean inter-event gap is below the 252-day mean inter-event gap."""
    any_txn = insider_buy_count + insider_sell_count
    dsl = _days_since_last_nonzero(any_txn)
    return (_rolling_mean(dsl, _TD_MO) < _rolling_mean(dsl, _TD_YEAR)).astype(float)


def itf_ext_009_days_since_buy_minus_baseline(insider_buy_count: pd.Series) -> pd.Series:
    """Days-since-last-buy minus its trailing 252-day mean (recency vs own norm)."""
    dsl = _days_since_last_nonzero(insider_buy_count)
    return dsl - _rolling_mean(dsl, _TD_YEAR)


def itf_ext_010_gap_median_any_txn_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day median of days-since-last-transaction."""
    any_txn = insider_buy_count + insider_sell_count
    return _rolling_median(_days_since_last_nonzero(any_txn), _TD_YEAR)


def itf_ext_011_days_since_last_officer_buy_63d_max(officer_buy_count: pd.Series) -> pd.Series:
    """63-day rolling max of days-since-last-officer-buy."""
    return _rolling_max(_days_since_last_nonzero(officer_buy_count), _TD_QTR)


def itf_ext_012_days_since_buy_pct_rank_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of days-since-last-buy within trailing 252-day window."""
    return _rolling_rank_pct(_days_since_last_nonzero(insider_buy_count), _TD_YEAR)


# --- Group B (013-024): Burstiness and clustering of activity ---

def itf_ext_013_txn_burstiness_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of daily total transactions over 63 days."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_std(total, _TD_QTR), _rolling_mean(total, _TD_QTR))


def itf_ext_014_txn_burstiness_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Coefficient of variation of daily total transactions over 252 days."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_std(total, _TD_YEAR), _rolling_mean(total, _TD_YEAR))


def itf_ext_015_buy_burstiness_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy count over 252 days."""
    return _safe_div(_rolling_std(insider_buy_count, _TD_YEAR), _rolling_mean(insider_buy_count, _TD_YEAR))


def itf_ext_016_max_single_day_txn_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Largest single-day total transaction count in trailing 63 days (cluster peak)."""
    total = insider_buy_count + insider_sell_count
    return _rolling_max(total, _TD_QTR)


def itf_ext_017_max_single_day_buy_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Largest single-day buy count in trailing 252 days."""
    return _rolling_max(insider_buy_count, _TD_YEAR)


def itf_ext_018_txn_concentration_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Share of 63-day transaction total contributed by the single busiest day."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_max(total, _TD_QTR), _rolling_sum(total, _TD_QTR))


def itf_ext_019_buy_concentration_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Share of 252-day buy total contributed by the single busiest buy day."""
    return _safe_div(_rolling_max(insider_buy_count, _TD_YEAR), _rolling_sum(insider_buy_count, _TD_YEAR))


def itf_ext_020_cluster_density_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Transactions per active day over 63 days (mean cluster size on filing days)."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_sum(total, _TD_QTR), _active_days(total, _TD_QTR))


def itf_ext_021_buy_cluster_density_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Buys per active buy day over 252 days (mean buy cluster size)."""
    return _safe_div(_rolling_sum(insider_buy_count, _TD_YEAR), _active_days(insider_buy_count, _TD_YEAR))


def itf_ext_022_multi_txn_day_count_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days in 63d window with 3 or more total insider transactions."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum((total >= 3).astype(float), _TD_QTR)


def itf_ext_023_heavy_txn_day_count_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of days in 252d window with 5 or more total insider transactions."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum((total >= 5).astype(float), _TD_YEAR)


def itf_ext_024_txn_gini_proxy_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Activity inequality proxy: 252d std of total transactions divided by 252d sum."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_rolling_std(total, _TD_YEAR), _rolling_sum(total, _TD_YEAR))


# --- Group C (025-036): Additional window counts and rates ---

def itf_ext_025_total_txn_count_5d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 5-day (weekly) window."""
    return _rolling_sum(insider_buy_count + insider_sell_count, _TD_WK)


def itf_ext_026_buy_count_5d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 5-day window."""
    return _rolling_sum(insider_buy_count, _TD_WK)


def itf_ext_027_buy_count_42d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 42-day (two-month) window."""
    return _rolling_sum(insider_buy_count, 42)


def itf_ext_028_total_txn_count_756d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 756-day (three-year) window."""
    return _rolling_sum(insider_buy_count + insider_sell_count, 756)


def itf_ext_029_buy_count_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy transaction count over trailing 126-day window."""
    return _rolling_sum(insider_buy_count, _TD_2Q)


def itf_ext_030_sell_count_42d(insider_sell_count: pd.Series) -> pd.Series:
    """Insider sell transaction count over trailing 42-day window."""
    return _rolling_sum(insider_sell_count, 42)


def itf_ext_031_buy_rate_per_day_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per trading day over 21-day window."""
    return _rolling_sum(insider_buy_count, _TD_MO) / float(_TD_MO)


def itf_ext_032_buy_rate_per_day_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Average buy transactions per trading day over 126-day window."""
    return _rolling_sum(insider_buy_count, _TD_2Q) / float(_TD_2Q)


def itf_ext_033_txn_rate_per_day_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Average total transactions per trading day over 504-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_2Y) / float(_TD_2Y)


def itf_ext_034_buy_day_density_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 21-day window with a buy transaction."""
    return _rolling_mean((insider_buy_count > 0).astype(float), _TD_MO)


def itf_ext_035_buy_day_density_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 126-day window with a buy transaction."""
    return _rolling_mean((insider_buy_count > 0).astype(float), _TD_2Q)


def itf_ext_036_active_day_density_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of trading days in 504-day window with any insider transaction."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    return _rolling_mean(any_txn, _TD_2Y)


# --- Group D (037-048): Acceleration, surges and regime shifts ---

def itf_ext_037_buy_count_5v21_ratio(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 5-day buy rate to 21-day buy rate (very-short-term acceleration)."""
    r5 = _rolling_sum(insider_buy_count, _TD_WK) / _TD_WK
    r21 = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    return _safe_div(r5, r21)


def itf_ext_038_buy_count_42v252_ratio(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 42-day buy rate to 252-day buy rate."""
    r42 = _rolling_sum(insider_buy_count, 42) / 42.0
    r252 = _rolling_sum(insider_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(r42, r252)


def itf_ext_039_txn_accel_5v63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Activity acceleration: 5-day rate minus 63-day rate."""
    total = insider_buy_count + insider_sell_count
    r5 = _rolling_sum(total, _TD_WK) / _TD_WK
    r63 = _rolling_sum(total, _TD_QTR) / _TD_QTR
    return r5 - r63


def itf_ext_040_buy_count_active_day_accel_21v126(insider_buy_count: pd.Series) -> pd.Series:
    """Active-buy-day density 21d minus 126d (broadening vs narrowing of buy days)."""
    d21 = _rolling_mean((insider_buy_count > 0).astype(float), _TD_MO)
    d126 = _rolling_mean((insider_buy_count > 0).astype(float), _TD_2Q)
    return d21 - d126


def itf_ext_041_txn_surge_63d_vs_756d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Surge: 63-day transaction rate divided by 756-day baseline rate."""
    total = insider_buy_count + insider_sell_count
    r63 = _rolling_sum(total, _TD_QTR) / _TD_QTR
    r756 = _rolling_sum(total, 756) / 756.0
    return _safe_div(r63, r756)


def itf_ext_042_buy_surge_flag_2x_baseline(insider_buy_count: pd.Series) -> pd.Series:
    """1 when the 21-day buy rate exceeds twice the 252-day buy rate."""
    r21 = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    r252 = _rolling_sum(insider_buy_count, _TD_YEAR) / _TD_YEAR
    return (r21 > 2.0 * r252).astype(float)


def itf_ext_043_buy_surge_flag_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    """252-day count of days where the 21-day buy rate exceeds twice the 252-day rate."""
    r21 = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    r252 = _rolling_sum(insider_buy_count, _TD_YEAR) / _TD_YEAR
    return _rolling_sum((r21 > 2.0 * r252).astype(float), _TD_YEAR)


def itf_ext_044_txn_count_ewm_ratio_21v126(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of EWM(21) to EWM(126) total transaction count — smoothed acceleration."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_ewm_mean(total, _TD_MO), _ewm_mean(total, _TD_2Q))


def itf_ext_045_buy_count_jerk_21v63v252(insider_buy_count: pd.Series) -> pd.Series:
    """Change in buy acceleration: (5v21 ratio) minus (21v63 ratio)."""
    r5 = _rolling_sum(insider_buy_count, _TD_WK) / _TD_WK
    r21 = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    r63 = _rolling_sum(insider_buy_count, _TD_QTR) / _TD_QTR
    return _safe_div(r5, r21) - _safe_div(r21, r63)


def itf_ext_046_officer_buy_surge_21v252(officer_buy_count: pd.Series) -> pd.Series:
    """Surge: 21-day officer-buy rate divided by 252-day officer-buy rate."""
    r21 = _rolling_sum(officer_buy_count, _TD_MO) / _TD_MO
    r252 = _rolling_sum(officer_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(r21, r252)


def itf_ext_047_director_buy_surge_21v252(director_buy_count: pd.Series) -> pd.Series:
    """Surge: 21-day director-buy rate divided by 252-day director-buy rate."""
    r21 = _rolling_sum(director_buy_count, _TD_MO) / _TD_MO
    r252 = _rolling_sum(director_buy_count, _TD_YEAR) / _TD_YEAR
    return _safe_div(r21, r252)


def itf_ext_048_first_txn_after_long_quiet_flag(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """1 on a transaction day immediately preceded by 126+ quiet days."""
    any_txn = (insider_buy_count + insider_sell_count) > 0
    quiet_before = _streak_false(any_txn).shift(1)
    return ((any_txn) & (quiet_before >= _TD_2Q)).astype(float)


# --- Group E (049-060): Regularity, streaks and quiet/active runs ---

def itf_ext_049_active_buy_streak(insider_buy_count: pd.Series) -> pd.Series:
    """Length of the current consecutive-day run with at least one insider buy."""
    return _streak_true(insider_buy_count > 0)


def itf_ext_050_active_txn_streak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Length of the current consecutive-day run with any insider transaction."""
    return _streak_true((insider_buy_count + insider_sell_count) > 0)


def itf_ext_051_max_active_buy_streak_252d(insider_buy_count: pd.Series) -> pd.Series:
    """252-day rolling max of the active-buy-streak length."""
    return _rolling_max(_streak_true(insider_buy_count > 0), _TD_YEAR)


def itf_ext_052_buy_week_count_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of 5-day windows in the past year with at least one buy (weekly participation)."""
    weekly = (_rolling_sum(insider_buy_count, _TD_WK) > 0).astype(float)
    return _rolling_sum(weekly, _TD_YEAR) / float(_TD_WK)


def itf_ext_053_buy_month_participation_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of trailing-year days where the 21-day buy count was positive."""
    monthly_active = (_rolling_sum(insider_buy_count, _TD_MO) > 0).astype(float)
    return _rolling_mean(monthly_active, _TD_YEAR)


def itf_ext_054_quiet_run_pct_rank_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of the current quiet-run length within trailing 252 days."""
    any_txn = (insider_buy_count + insider_sell_count) > 0
    return _rolling_rank_pct(_streak_false(any_txn), _TD_YEAR)


def itf_ext_055_txn_regularity_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Regularity score: 1 minus the 252d coefficient of variation of inter-event gaps."""
    any_txn = insider_buy_count + insider_sell_count
    dsl = _days_since_last_nonzero(any_txn)
    cv = _safe_div(_rolling_std(dsl, _TD_YEAR), _rolling_mean(dsl, _TD_YEAR))
    return 1.0 - cv


def itf_ext_056_buy_run_to_quiet_run_ratio(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of current active-buy-streak to current quiet-buy-run (regime balance)."""
    active = _streak_true(insider_buy_count > 0)
    quiet = _streak_false(insider_buy_count > 0)
    return _safe_div(active, quiet)


def itf_ext_057_consecutive_active_weeks_buys(insider_buy_count: pd.Series) -> pd.Series:
    """Streak of consecutive days where the trailing 5-day buy count is positive."""
    return _streak_true(_rolling_sum(insider_buy_count, _TD_WK) > 0)


def itf_ext_058_dormant_then_active_flag(insider_buy_count: pd.Series) -> pd.Series:
    """1 when buys are present in the last 21 days but absent in the prior 126 days."""
    recent = _rolling_sum(insider_buy_count, _TD_MO)
    prior = _rolling_sum(insider_buy_count.shift(_TD_MO), _TD_2Q)
    return ((recent > 0) & (prior == 0)).astype(float)


def itf_ext_059_activity_consistency_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of 21-day sub-windows within 63 days that had any transaction (consistency)."""
    total = insider_buy_count + insider_sell_count
    monthly_active = (_rolling_sum(total, _TD_MO) > 0).astype(float)
    return _rolling_mean(monthly_active, _TD_QTR)


def itf_ext_060_buy_quiet_run_max_504d(insider_buy_count: pd.Series) -> pd.Series:
    """504-day rolling max of the consecutive-day quiet-buy-run length."""
    return _rolling_max(_streak_false(insider_buy_count > 0), _TD_2Y)


# --- Group F (061-075): Role-mix frequency, normalization and composites ---

def itf_ext_061_officer_share_of_buy_days_252d(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 252d buy-active days that included an officer buy."""
    off_days = _active_days(officer_buy_count, _TD_YEAR)
    all_days = _active_days(insider_buy_count, _TD_YEAR)
    return _safe_div(off_days, all_days)


def itf_ext_062_director_share_of_buy_days_252d(director_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 252d buy-active days that included a director buy."""
    dir_days = _active_days(director_buy_count, _TD_YEAR)
    all_days = _active_days(insider_buy_count, _TD_YEAR)
    return _safe_div(dir_days, all_days)


def itf_ext_063_officer_to_director_buy_count_ratio_252d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Ratio of 252d officer buy count to 252d director buy count (role mix)."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_YEAR), _rolling_sum(director_buy_count, _TD_YEAR))


def itf_ext_064_officer_director_buy_count_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy count over trailing 63-day window."""
    return _rolling_sum(officer_buy_count + director_buy_count, _TD_QTR)


def itf_ext_065_role_concentration_buy_count_252d(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Officer buy count as a fraction of total buy count over 252 days."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_YEAR), _rolling_sum(insider_buy_count, _TD_YEAR))


def itf_ext_066_buyer_to_txn_ratio_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """63d unique buyers divided by 63d buy count — distinct-participant fraction."""
    return _safe_div(_rolling_sum(insider_buyers, _TD_QTR), _rolling_sum(insider_buy_count, _TD_QTR))


def itf_ext_067_seller_to_txn_ratio_63d(insider_sellers: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63d unique sellers divided by 63d sell count — distinct-seller fraction."""
    return _safe_div(_rolling_sum(insider_sellers, _TD_QTR), _rolling_sum(insider_sell_count, _TD_QTR))


def itf_ext_068_buyer_count_zscore_63d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of daily unique buyer count within trailing 63-day window."""
    return _zscore_rolling(insider_buyers, _TD_QTR)


def itf_ext_069_buy_count_zscore_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of daily buy count within trailing 504-day window."""
    return _zscore_rolling(insider_buy_count, _TD_2Y)


def itf_ext_070_active_day_density_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score (252d) of the 63d active-day density — activity-regime deviation."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    density = _rolling_mean(any_txn, _TD_QTR)
    return _zscore_rolling(density, _TD_YEAR)


def itf_ext_071_buy_count_pct_rank_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily buy count within trailing 63-day window."""
    return _rolling_rank_pct(insider_buy_count, _TD_QTR)


def itf_ext_072_total_txn_pct_rank_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of daily total transaction count within trailing 504-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_rank_pct(total, _TD_2Y)


def itf_ext_073_buy_count_63d_pct_of_252d_peak(insider_buy_count: pd.Series) -> pd.Series:
    """63-day buy count as a fraction of its trailing 252-day rolling peak."""
    cnt63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return _safe_div(cnt63, _rolling_max(cnt63, _TD_YEAR))


def itf_ext_074_buy_freq_acceleration_composite(insider_buy_count: pd.Series) -> pd.Series:
    """Composite: average of 252d z-scores of (21d buy rate), (21d active-buy density),
    and (21v252 buy-rate ratio) — extended buy-frequency acceleration score."""
    r21 = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    dens = _rolling_mean((insider_buy_count > 0).astype(float), _TD_MO)
    ratio = _safe_div(r21, _rolling_sum(insider_buy_count, _TD_YEAR) / _TD_YEAR)
    z1, z2, z3 = _zscore_rolling(r21, _TD_YEAR), _zscore_rolling(dens, _TD_YEAR), _zscore_rolling(ratio, _TD_YEAR)
    cnt = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
    return _safe_div(z1.fillna(0) + z2.fillna(0) + z3.fillna(0), cnt)


def itf_ext_075_activity_intensity_extended_composite(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Extended activity-intensity composite: average of 252d z-scores of
    (63d transactions per active day), (63d burstiness CV), and (63d buyer sum)."""
    total = insider_buy_count + insider_sell_count
    density = _safe_div(_rolling_sum(total, _TD_QTR), _active_days(total, _TD_QTR))
    burst = _safe_div(_rolling_std(total, _TD_QTR), _rolling_mean(total, _TD_QTR))
    buyers = _rolling_sum(insider_buyers, _TD_QTR)
    z1, z2, z3 = _zscore_rolling(density, _TD_YEAR), _zscore_rolling(burst, _TD_YEAR), _zscore_rolling(buyers, _TD_YEAR)
    cnt = z1.notna().astype(float) + z2.notna().astype(float) + z3.notna().astype(float)
    return _safe_div(z1.fillna(0) + z2.fillna(0) + z3.fillna(0), cnt)


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_TRANSACTION_FREQ_EXTENDED_REGISTRY_001_075 = {
    "itf_ext_001_current_quiet_run_any_txn": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_001_current_quiet_run_any_txn},
    "itf_ext_002_current_quiet_run_buys": {"inputs": ["insider_buy_count"], "func": itf_ext_002_current_quiet_run_buys},
    "itf_ext_003_current_quiet_run_sells": {"inputs": ["insider_sell_count"], "func": itf_ext_003_current_quiet_run_sells},
    "itf_ext_004_max_gap_any_txn_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_004_max_gap_any_txn_252d},
    "itf_ext_005_max_gap_buys_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_005_max_gap_buys_252d},
    "itf_ext_006_mean_gap_any_txn_504d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_006_mean_gap_any_txn_504d},
    "itf_ext_007_gap_dispersion_buys_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_007_gap_dispersion_buys_252d},
    "itf_ext_008_gap_shrinking_flag": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_008_gap_shrinking_flag},
    "itf_ext_009_days_since_buy_minus_baseline": {"inputs": ["insider_buy_count"], "func": itf_ext_009_days_since_buy_minus_baseline},
    "itf_ext_010_gap_median_any_txn_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_010_gap_median_any_txn_252d},
    "itf_ext_011_days_since_last_officer_buy_63d_max": {"inputs": ["officer_buy_count"], "func": itf_ext_011_days_since_last_officer_buy_63d_max},
    "itf_ext_012_days_since_buy_pct_rank_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_012_days_since_buy_pct_rank_252d},
    "itf_ext_013_txn_burstiness_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_013_txn_burstiness_63d},
    "itf_ext_014_txn_burstiness_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_014_txn_burstiness_252d},
    "itf_ext_015_buy_burstiness_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_015_buy_burstiness_252d},
    "itf_ext_016_max_single_day_txn_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_016_max_single_day_txn_63d},
    "itf_ext_017_max_single_day_buy_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_017_max_single_day_buy_252d},
    "itf_ext_018_txn_concentration_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_018_txn_concentration_63d},
    "itf_ext_019_buy_concentration_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_019_buy_concentration_252d},
    "itf_ext_020_cluster_density_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_020_cluster_density_63d},
    "itf_ext_021_buy_cluster_density_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_021_buy_cluster_density_252d},
    "itf_ext_022_multi_txn_day_count_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_022_multi_txn_day_count_63d},
    "itf_ext_023_heavy_txn_day_count_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_023_heavy_txn_day_count_252d},
    "itf_ext_024_txn_gini_proxy_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_024_txn_gini_proxy_252d},
    "itf_ext_025_total_txn_count_5d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_025_total_txn_count_5d},
    "itf_ext_026_buy_count_5d": {"inputs": ["insider_buy_count"], "func": itf_ext_026_buy_count_5d},
    "itf_ext_027_buy_count_42d": {"inputs": ["insider_buy_count"], "func": itf_ext_027_buy_count_42d},
    "itf_ext_028_total_txn_count_756d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_028_total_txn_count_756d},
    "itf_ext_029_buy_count_126d": {"inputs": ["insider_buy_count"], "func": itf_ext_029_buy_count_126d},
    "itf_ext_030_sell_count_42d": {"inputs": ["insider_sell_count"], "func": itf_ext_030_sell_count_42d},
    "itf_ext_031_buy_rate_per_day_21d": {"inputs": ["insider_buy_count"], "func": itf_ext_031_buy_rate_per_day_21d},
    "itf_ext_032_buy_rate_per_day_126d": {"inputs": ["insider_buy_count"], "func": itf_ext_032_buy_rate_per_day_126d},
    "itf_ext_033_txn_rate_per_day_504d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_033_txn_rate_per_day_504d},
    "itf_ext_034_buy_day_density_21d": {"inputs": ["insider_buy_count"], "func": itf_ext_034_buy_day_density_21d},
    "itf_ext_035_buy_day_density_126d": {"inputs": ["insider_buy_count"], "func": itf_ext_035_buy_day_density_126d},
    "itf_ext_036_active_day_density_504d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_036_active_day_density_504d},
    "itf_ext_037_buy_count_5v21_ratio": {"inputs": ["insider_buy_count"], "func": itf_ext_037_buy_count_5v21_ratio},
    "itf_ext_038_buy_count_42v252_ratio": {"inputs": ["insider_buy_count"], "func": itf_ext_038_buy_count_42v252_ratio},
    "itf_ext_039_txn_accel_5v63": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_039_txn_accel_5v63},
    "itf_ext_040_buy_count_active_day_accel_21v126": {"inputs": ["insider_buy_count"], "func": itf_ext_040_buy_count_active_day_accel_21v126},
    "itf_ext_041_txn_surge_63d_vs_756d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_041_txn_surge_63d_vs_756d},
    "itf_ext_042_buy_surge_flag_2x_baseline": {"inputs": ["insider_buy_count"], "func": itf_ext_042_buy_surge_flag_2x_baseline},
    "itf_ext_043_buy_surge_flag_count_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_043_buy_surge_flag_count_252d},
    "itf_ext_044_txn_count_ewm_ratio_21v126": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_044_txn_count_ewm_ratio_21v126},
    "itf_ext_045_buy_count_jerk_21v63v252": {"inputs": ["insider_buy_count"], "func": itf_ext_045_buy_count_jerk_21v63v252},
    "itf_ext_046_officer_buy_surge_21v252": {"inputs": ["officer_buy_count"], "func": itf_ext_046_officer_buy_surge_21v252},
    "itf_ext_047_director_buy_surge_21v252": {"inputs": ["director_buy_count"], "func": itf_ext_047_director_buy_surge_21v252},
    "itf_ext_048_first_txn_after_long_quiet_flag": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_048_first_txn_after_long_quiet_flag},
    "itf_ext_049_active_buy_streak": {"inputs": ["insider_buy_count"], "func": itf_ext_049_active_buy_streak},
    "itf_ext_050_active_txn_streak": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_050_active_txn_streak},
    "itf_ext_051_max_active_buy_streak_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_051_max_active_buy_streak_252d},
    "itf_ext_052_buy_week_count_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_052_buy_week_count_252d},
    "itf_ext_053_buy_month_participation_252d": {"inputs": ["insider_buy_count"], "func": itf_ext_053_buy_month_participation_252d},
    "itf_ext_054_quiet_run_pct_rank_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_054_quiet_run_pct_rank_252d},
    "itf_ext_055_txn_regularity_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_055_txn_regularity_252d},
    "itf_ext_056_buy_run_to_quiet_run_ratio": {"inputs": ["insider_buy_count"], "func": itf_ext_056_buy_run_to_quiet_run_ratio},
    "itf_ext_057_consecutive_active_weeks_buys": {"inputs": ["insider_buy_count"], "func": itf_ext_057_consecutive_active_weeks_buys},
    "itf_ext_058_dormant_then_active_flag": {"inputs": ["insider_buy_count"], "func": itf_ext_058_dormant_then_active_flag},
    "itf_ext_059_activity_consistency_63d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_059_activity_consistency_63d},
    "itf_ext_060_buy_quiet_run_max_504d": {"inputs": ["insider_buy_count"], "func": itf_ext_060_buy_quiet_run_max_504d},
    "itf_ext_061_officer_share_of_buy_days_252d": {"inputs": ["officer_buy_count", "insider_buy_count"], "func": itf_ext_061_officer_share_of_buy_days_252d},
    "itf_ext_062_director_share_of_buy_days_252d": {"inputs": ["director_buy_count", "insider_buy_count"], "func": itf_ext_062_director_share_of_buy_days_252d},
    "itf_ext_063_officer_to_director_buy_count_ratio_252d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_ext_063_officer_to_director_buy_count_ratio_252d},
    "itf_ext_064_officer_director_buy_count_63d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_ext_064_officer_director_buy_count_63d},
    "itf_ext_065_role_concentration_buy_count_252d": {"inputs": ["officer_buy_count", "insider_buy_count"], "func": itf_ext_065_role_concentration_buy_count_252d},
    "itf_ext_066_buyer_to_txn_ratio_63d": {"inputs": ["insider_buyers", "insider_buy_count"], "func": itf_ext_066_buyer_to_txn_ratio_63d},
    "itf_ext_067_seller_to_txn_ratio_63d": {"inputs": ["insider_sellers", "insider_sell_count"], "func": itf_ext_067_seller_to_txn_ratio_63d},
    "itf_ext_068_buyer_count_zscore_63d": {"inputs": ["insider_buyers"], "func": itf_ext_068_buyer_count_zscore_63d},
    "itf_ext_069_buy_count_zscore_504d": {"inputs": ["insider_buy_count"], "func": itf_ext_069_buy_count_zscore_504d},
    "itf_ext_070_active_day_density_zscore_252d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_070_active_day_density_zscore_252d},
    "itf_ext_071_buy_count_pct_rank_63d": {"inputs": ["insider_buy_count"], "func": itf_ext_071_buy_count_pct_rank_63d},
    "itf_ext_072_total_txn_pct_rank_504d": {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_ext_072_total_txn_pct_rank_504d},
    "itf_ext_073_buy_count_63d_pct_of_252d_peak": {"inputs": ["insider_buy_count"], "func": itf_ext_073_buy_count_63d_pct_of_252d_peak},
    "itf_ext_074_buy_freq_acceleration_composite": {"inputs": ["insider_buy_count"], "func": itf_ext_074_buy_freq_acceleration_composite},
    "itf_ext_075_activity_intensity_extended_composite": {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"], "func": itf_ext_075_activity_intensity_extended_composite},
}
