"""
83_insider_buy_cluster — Extended Features 001-075
Domain: insider buy clustering — additional angles not in the base files:
        buy-value-weighted clusters, gap-since-cluster recency, role-mix
        diversity, acceleration of buy flow, dollar-value concentration,
        EWM-smoothed buy flow, breadth percentiles, drought lengths, and
        composite capitulation cluster scores.
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

Feature numbering: ibc_ext_001 .. ibc_ext_075
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK = 5     # 1 week
_TD_MO = 21    # 1 month
_TD_QTR = 63   # 1 quarter
_TD_2Q = 126   # 2 quarters
_TD_YEAR = 252  # 1 year
_TD_2Y = 504   # 2 years
_EPS = 1e-9

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
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _active_days(s: pd.Series, w: int) -> pd.Series:
    """Count of days with s > 0 in trailing w-day window."""
    return _rolling_sum((s > 0).astype(float), w)


def _days_since(cond: pd.Series) -> pd.Series:
    """Trading days since cond was last True (0 on a True day, increasing otherwise)."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = 0.0 if arr[i] else (out[i - 1] + 1.0)
    return pd.Series(out, index=cond.index)


def _streak(cond: pd.Series) -> pd.Series:
    """Current consecutive-True streak length ending at each row."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1.0) if arr[i] else 0.0
    return pd.Series(out, index=cond.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Buy-value flow over multiple windows ---


def ibc_ext_001_buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 21-day window."""
    return _rolling_sum(insider_buy_value, _TD_MO)


def ibc_ext_002_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 63-day window."""
    return _rolling_sum(insider_buy_value, _TD_QTR)


def ibc_ext_003_buy_value_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 126-day window."""
    return _rolling_sum(insider_buy_value, _TD_2Q)


def ibc_ext_004_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 252-day window."""
    return _rolling_sum(insider_buy_value, _TD_YEAR)


def ibc_ext_005_buy_value_5d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 5-day window."""
    return _rolling_sum(insider_buy_value, _TD_WK)


def ibc_ext_006_avg_buy_value_per_txn_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar value per insider buy transaction over trailing 63 days."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_QTR), _rolling_sum(insider_buy_count, _TD_QTR))


def ibc_ext_007_avg_buy_value_per_txn_21d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar value per insider buy transaction over trailing 21 days."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_MO), _rolling_sum(insider_buy_count, _TD_MO))


def ibc_ext_008_avg_buy_value_per_buyer_63d(insider_buy_value: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Average dollar value per distinct insider buyer over trailing 63 days."""
    return _safe_div(_rolling_sum(insider_buy_value, _TD_QTR), _rolling_sum(insider_buyers, _TD_QTR))


def ibc_ext_009_peak_buy_value_single_day_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Maximum single-day insider buy dollar value within trailing 63 days."""
    return _rolling_max(insider_buy_value, _TD_QTR)


def ibc_ext_010_buy_value_concentration_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Share of 63-day buy value contributed by its single largest day (0..1; high = lumpy)."""
    return _safe_div(_rolling_max(insider_buy_value, _TD_QTR), _rolling_sum(insider_buy_value, _TD_QTR))


def ibc_ext_011_buy_value_zscore_63d_in_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of 63-day buy value relative to its trailing 252-day distribution."""
    return _zscore_rolling(_rolling_sum(insider_buy_value, _TD_QTR), _TD_YEAR)


def ibc_ext_012_buy_value_zscore_21d_in_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of 21-day buy value relative to its trailing 252-day distribution."""
    return _zscore_rolling(_rolling_sum(insider_buy_value, _TD_MO), _TD_YEAR)


# --- Group B (013-022): EWM-smoothed buy flow ---


def ibc_ext_013_buy_count_ewm21(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(21)-smoothed daily insider buy transaction count."""
    return _ewm_mean(insider_buy_count, _TD_MO)


def ibc_ext_014_buy_count_ewm63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(63)-smoothed daily insider buy transaction count."""
    return _ewm_mean(insider_buy_count, _TD_QTR)


def ibc_ext_015_buyers_ewm21(insider_buyers: pd.Series) -> pd.Series:
    """EWM(21)-smoothed daily distinct insider buyer count."""
    return _ewm_mean(insider_buyers, _TD_MO)


def ibc_ext_016_buyers_ewm63(insider_buyers: pd.Series) -> pd.Series:
    """EWM(63)-smoothed daily distinct insider buyer count."""
    return _ewm_mean(insider_buyers, _TD_QTR)


def ibc_ext_017_buy_value_ewm21(insider_buy_value: pd.Series) -> pd.Series:
    """EWM(21)-smoothed daily insider buy dollar value."""
    return _ewm_mean(insider_buy_value, _TD_MO)


def ibc_ext_018_buy_value_ewm63(insider_buy_value: pd.Series) -> pd.Series:
    """EWM(63)-smoothed daily insider buy dollar value."""
    return _ewm_mean(insider_buy_value, _TD_QTR)


def ibc_ext_019_officer_buy_count_ewm21(officer_buy_count: pd.Series) -> pd.Series:
    """EWM(21)-smoothed daily officer buy transaction count."""
    return _ewm_mean(officer_buy_count, _TD_MO)


def ibc_ext_020_director_buy_count_ewm21(director_buy_count: pd.Series) -> pd.Series:
    """EWM(21)-smoothed daily director buy transaction count."""
    return _ewm_mean(director_buy_count, _TD_MO)


def ibc_ext_021_buy_count_ewm_fast_slow_diff(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of buy count (positive = accelerating buy flow)."""
    return _ewm_mean(insider_buy_count, _TD_MO) - _ewm_mean(insider_buy_count, _TD_QTR)


def ibc_ext_022_buyers_ewm_fast_slow_diff(insider_buyers: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of distinct buyers (positive = accelerating breadth)."""
    return _ewm_mean(insider_buyers, _TD_MO) - _ewm_mean(insider_buyers, _TD_QTR)


# --- Group C (023-034): Acceleration / momentum of buy flow ---


def ibc_ext_023_buy_count_accel_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Recent 21-day buy count minus the prior 21-day buy count (window-on-window change)."""
    s21 = _rolling_sum(insider_buy_count, _TD_MO)
    return s21 - s21.shift(_TD_MO)


def ibc_ext_024_buy_count_accel_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Recent 63-day buy count minus the prior 63-day buy count."""
    s63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return s63 - s63.shift(_TD_QTR)


def ibc_ext_025_buyers_accel_21d(insider_buyers: pd.Series) -> pd.Series:
    """Recent 21-day distinct buyer count minus the prior 21-day buyer count."""
    s21 = _rolling_sum(insider_buyers, _TD_MO)
    return s21 - s21.shift(_TD_MO)


def ibc_ext_026_buyers_accel_63d(insider_buyers: pd.Series) -> pd.Series:
    """Recent 63-day distinct buyer count minus the prior 63-day buyer count."""
    s63 = _rolling_sum(insider_buyers, _TD_QTR)
    return s63 - s63.shift(_TD_QTR)


def ibc_ext_027_buy_value_accel_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Recent 63-day buy value minus the prior 63-day buy value."""
    s63 = _rolling_sum(insider_buy_value, _TD_QTR)
    return s63 - s63.shift(_TD_QTR)


def ibc_ext_028_buy_count_growth_ratio_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Recent 21-day buy count divided by the prior 21-day buy count (growth ratio)."""
    s21 = _rolling_sum(insider_buy_count, _TD_MO)
    return _safe_div(s21, s21.shift(_TD_MO))


def ibc_ext_029_buyers_growth_ratio_63d(insider_buyers: pd.Series) -> pd.Series:
    """Recent 63-day distinct buyer count divided by the prior 63-day buyer count."""
    s63 = _rolling_sum(insider_buyers, _TD_QTR)
    return _safe_div(s63, s63.shift(_TD_QTR))


def ibc_ext_030_active_days_accel_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Recent 63-day active-buy-day count minus the prior 63-day count."""
    a63 = _active_days(insider_buy_count, _TD_QTR)
    return a63 - a63.shift(_TD_QTR)


def ibc_ext_031_buy_count_5d_vs_63d_mean(insider_buy_count: pd.Series) -> pd.Series:
    """5-day buy count minus its 63-day rolling-sum mean-equivalent (short-burst detector)."""
    s5 = _rolling_sum(insider_buy_count, _TD_WK)
    base = _rolling_mean(insider_buy_count, _TD_QTR) * float(_TD_WK)
    return s5 - base


def ibc_ext_032_buy_value_growth_ratio_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Recent 63-day buy value divided by the prior 63-day buy value."""
    s63 = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(s63, s63.shift(_TD_QTR))


def ibc_ext_033_buyers_ewm_slope_proxy_21d(insider_buyers: pd.Series) -> pd.Series:
    """EWM(21) of distinct buyers minus its value 21 days ago (smoothed breadth momentum)."""
    e = _ewm_mean(insider_buyers, _TD_MO)
    return e - e.shift(_TD_MO)


def ibc_ext_034_buy_count_accel_normalized_63d(insider_buy_count: pd.Series) -> pd.Series:
    """63-day buy-count acceleration normalized by the prior 63-day count (relative acceleration)."""
    s63 = _rolling_sum(insider_buy_count, _TD_QTR)
    prior = s63.shift(_TD_QTR)
    return _safe_div(s63 - prior, prior)


# --- Group D (035-046): Cluster recency, droughts and streaks ---


def ibc_ext_035_days_since_cluster_21d(insider_buyers: pd.Series) -> pd.Series:
    """Trading days since the trailing 21-day distinct-buyer count last reached 2+ (cluster)."""
    return _days_since(_rolling_sum(insider_buyers, _TD_MO) >= 2)


def ibc_ext_036_days_since_strong_cluster_21d(insider_buyers: pd.Series) -> pd.Series:
    """Trading days since the trailing 21-day distinct-buyer count last reached 3+."""
    return _days_since(_rolling_sum(insider_buyers, _TD_MO) >= 3)


def ibc_ext_037_days_since_cluster_63d(insider_buyers: pd.Series) -> pd.Series:
    """Trading days since the trailing 63-day distinct-buyer count last reached 3+."""
    return _days_since(_rolling_sum(insider_buyers, _TD_QTR) >= 3)


def ibc_ext_038_days_since_last_officer_buy(officer_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent officer buy filing."""
    return _days_since(officer_buy_count > 0)


def ibc_ext_039_days_since_last_director_buy(director_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent director buy filing."""
    return _days_since(director_buy_count > 0)


def ibc_ext_040_days_since_last_tenpct_buy(tenpct_buy_count: pd.Series) -> pd.Series:
    """Trading days since the most recent 10%-holder buy filing."""
    return _days_since(tenpct_buy_count > 0)


def ibc_ext_041_buy_drought_length(insider_buy_count: pd.Series) -> pd.Series:
    """Current consecutive-day run with no insider buy filing (buy drought length)."""
    return _streak(insider_buy_count <= 0)


def ibc_ext_042_max_buy_drought_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Longest no-buy drought observed within the trailing 252 days."""
    return _rolling_max(_streak(insider_buy_count <= 0), _TD_YEAR)


def ibc_ext_043_consec_days_with_buy(insider_buy_count: pd.Series) -> pd.Series:
    """Current consecutive-day run with at least one insider buy filing."""
    return _streak(insider_buy_count > 0)


def ibc_ext_044_consec_weeks_with_cluster(insider_buyers: pd.Series) -> pd.Series:
    """Current consecutive-week run where the 5-day buyer count reached 2+."""
    return _streak(_rolling_sum(insider_buyers, _TD_WK) >= 2)


def ibc_ext_045_days_since_buy_value_spike_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Trading days since insider_buy_value last hit its trailing 63-day maximum."""
    return _days_since(insider_buy_value >= _rolling_max(insider_buy_value, _TD_QTR))


def ibc_ext_046_days_since_peak_buyers_63d(insider_buyers: pd.Series) -> pd.Series:
    """Trading days since the daily distinct-buyer count last hit its trailing 63-day maximum."""
    return _days_since(insider_buyers >= _rolling_max(insider_buyers, _TD_QTR))


# --- Group E (047-058): Role-mix diversity and balance ---


def ibc_ext_047_role_diversity_count_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                         tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of distinct insider role types active over trailing 63 days (0-3)."""
    o = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_QTR) > 0).astype(float)
    return o + d + t


def ibc_ext_048_role_diversity_count_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                         tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of distinct insider role types active over trailing 21 days (0-3)."""
    o = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_MO) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_MO) > 0).astype(float)
    return o + d + t


def ibc_ext_049_officer_director_balance_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Officer minus director buy count over 63 days, scaled by their combined total (-1..1)."""
    o = _rolling_sum(officer_buy_count, _TD_QTR)
    d = _rolling_sum(director_buy_count, _TD_QTR)
    return _safe_div(o - d, o + d)


def ibc_ext_050_officer_director_balance_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Officer minus director buy count over 21 days, scaled by their combined total (-1..1)."""
    o = _rolling_sum(officer_buy_count, _TD_MO)
    d = _rolling_sum(director_buy_count, _TD_MO)
    return _safe_div(o - d, o + d)


def ibc_ext_051_role_concentration_hhi_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                           tenpct_buy_count: pd.Series) -> pd.Series:
    """Herfindahl concentration of 63-day buy counts across the three role types (1/3..1)."""
    o = _rolling_sum(officer_buy_count, _TD_QTR)
    d = _rolling_sum(director_buy_count, _TD_QTR)
    t = _rolling_sum(tenpct_buy_count, _TD_QTR)
    total = (o + d + t).replace(0, np.nan)
    return (o / total) ** 2 + (d / total) ** 2 + (t / total) ** 2


def ibc_ext_052_tenpct_share_of_value_proxy_63d(tenpct_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day buy transactions attributable to 10%-holders."""
    return _safe_div(_rolling_sum(tenpct_buy_count, _TD_QTR), _rolling_sum(insider_buy_count, _TD_QTR))


def ibc_ext_053_officer_director_combined_252d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy transaction count over trailing 252 days."""
    return _rolling_sum(officer_buy_count, _TD_YEAR) + _rolling_sum(director_buy_count, _TD_YEAR)


def ibc_ext_054_all_roles_combined_252d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                        tenpct_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director + 10%-holder buy count over trailing 252 days."""
    return (_rolling_sum(officer_buy_count, _TD_YEAR)
            + _rolling_sum(director_buy_count, _TD_YEAR)
            + _rolling_sum(tenpct_buy_count, _TD_YEAR))


def ibc_ext_055_officer_dir_dual_flag_126d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Binary flag: both officer(s) and director(s) bought within trailing 126 days."""
    o = (_rolling_sum(officer_buy_count, _TD_2Q) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_2Q) > 0).astype(float)
    return o * d


def ibc_ext_056_all_three_roles_flag_126d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                          tenpct_buy_count: pd.Series) -> pd.Series:
    """Binary flag: officers, directors AND 10%-holders all bought within trailing 126 days."""
    o = (_rolling_sum(officer_buy_count, _TD_2Q) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_2Q) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_2Q) > 0).astype(float)
    return o * d * t


def ibc_ext_057_officer_active_day_share_63d(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day active buy days that included an officer buy."""
    return _safe_div(_active_days(officer_buy_count, _TD_QTR), _active_days(insider_buy_count, _TD_QTR))


def ibc_ext_058_director_active_day_share_63d(director_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day active buy days that included a director buy."""
    return _safe_div(_active_days(director_buy_count, _TD_QTR), _active_days(insider_buy_count, _TD_QTR))


# --- Group F (059-068): Breadth percentiles and dispersion ---


def ibc_ext_059_buyers_21d_pctrank_252d(insider_buyers: pd.Series) -> pd.Series:
    """252-day percentile rank of the trailing 21-day distinct-buyer count."""
    return _rolling_rank_pct(_rolling_sum(insider_buyers, _TD_MO), _TD_YEAR)


def ibc_ext_060_buyers_63d_pctrank_504d(insider_buyers: pd.Series) -> pd.Series:
    """504-day percentile rank of the trailing 63-day distinct-buyer count."""
    return _rolling_rank_pct(_rolling_sum(insider_buyers, _TD_QTR), _TD_2Y)


def ibc_ext_061_buy_count_63d_pctrank_252d(insider_buy_count: pd.Series) -> pd.Series:
    """252-day percentile rank of the trailing 63-day buy-transaction count."""
    return _rolling_rank_pct(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)


def ibc_ext_062_buy_value_63d_pctrank_252d(insider_buy_value: pd.Series) -> pd.Series:
    """252-day percentile rank of the trailing 63-day insider buy value."""
    return _rolling_rank_pct(_rolling_sum(insider_buy_value, _TD_QTR), _TD_YEAR)


def ibc_ext_063_buyers_21d_expanding_pctrank(insider_buyers: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the trailing 21-day distinct-buyer count."""
    s21 = _rolling_sum(insider_buyers, _TD_MO)
    return s21.expanding(min_periods=_TD_MO).rank(pct=True)


def ibc_ext_064_buy_value_21d_expanding_pctrank(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the trailing 21-day insider buy value."""
    s21 = _rolling_sum(insider_buy_value, _TD_MO)
    return s21.expanding(min_periods=_TD_MO).rank(pct=True)


def ibc_ext_065_buyers_63d_at_252d_max_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: trailing 63-day distinct-buyer count equals its trailing 252-day maximum."""
    s63 = _rolling_sum(insider_buyers, _TD_QTR)
    return (s63 >= _rolling_max(s63, _TD_YEAR)).astype(float)


def ibc_ext_066_buy_count_63d_at_252d_max_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary flag: trailing 63-day buy-transaction count equals its trailing 252-day maximum."""
    s63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return (s63 >= _rolling_max(s63, _TD_YEAR)).astype(float)


def ibc_ext_067_buyers_daily_std_63d(insider_buyers: pd.Series) -> pd.Series:
    """Standard deviation of daily distinct-buyer counts over trailing 63 days (burstiness)."""
    return _rolling_std(insider_buyers, _TD_QTR)


def ibc_ext_068_buy_count_daily_cv_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy counts over trailing 63 days (flow irregularity)."""
    return _safe_div(_rolling_std(insider_buy_count, _TD_QTR), _rolling_mean(insider_buy_count, _TD_QTR))


# --- Group G (069-075): Composite capitulation cluster signals ---


def ibc_ext_069_value_weighted_cluster_intensity_63d(insider_buyers: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """63-day distinct buyers multiplied by 63-day buy value (dollar-weighted cluster intensity)."""
    return _rolling_sum(insider_buyers, _TD_QTR) * _rolling_sum(insider_buy_value, _TD_QTR)


def ibc_ext_070_cluster_breadth_score_126d(insider_buyers: pd.Series, officer_buy_count: pd.Series,
                                           director_buy_count: pd.Series) -> pd.Series:
    """Composite breadth score over 126 days: [buyers>=3] + [officer active] + [director active] (0-3)."""
    b = (_rolling_sum(insider_buyers, _TD_2Q) >= 3).astype(float)
    o = (_rolling_sum(officer_buy_count, _TD_2Q) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_2Q) > 0).astype(float)
    return b + o + d


def ibc_ext_071_strong_cluster_flag_126d(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: at least 4 distinct buyers bought within trailing 126 days."""
    return (_rolling_sum(insider_buyers, _TD_2Q) >= 4).astype(float)


def ibc_ext_072_recent_cluster_acceleration_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: 21-day buyer count is 2+ and exceeds the prior 21-day count (fresh accelerating cluster)."""
    s21 = _rolling_sum(insider_buyers, _TD_MO)
    return ((s21 >= 2) & (s21 > s21.shift(_TD_MO))).astype(float)


def ibc_ext_073_buy_flow_zscore_composite(insider_buyers: pd.Series, insider_buy_count: pd.Series,
                                          insider_buy_value: pd.Series) -> pd.Series:
    """Mean of 63d-in-252d z-scores for buyers, buy count and buy value (composite buy-flow extremity)."""
    z_b = _zscore_rolling(_rolling_sum(insider_buyers, _TD_QTR), _TD_YEAR)
    z_c = _zscore_rolling(_rolling_sum(insider_buy_count, _TD_QTR), _TD_YEAR)
    z_v = _zscore_rolling(_rolling_sum(insider_buy_value, _TD_QTR), _TD_YEAR)
    return (z_b + z_c + z_v) / 3.0


def ibc_ext_074_cluster_persistence_score_126d(insider_buyers: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days on which the 21-day buyer count stood at 2+ (cluster persistence)."""
    cluster_day = (_rolling_sum(insider_buyers, _TD_MO) >= 2).astype(float)
    return _rolling_mean(cluster_day, _TD_2Q)


def ibc_ext_075_capitulation_cluster_composite(insider_buyers: pd.Series, officer_buy_count: pd.Series,
                                               director_buy_count: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Capitulation cluster composite: sum of [buyers>=3 in 63d], [officer & director both active in 63d],
    [63d buy value in top quartile of its 252d history]. Higher = stronger conviction insider cluster."""
    breadth = (_rolling_sum(insider_buyers, _TD_QTR) >= 3).astype(float)
    o = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    dual = o * d
    val63 = _rolling_sum(insider_buy_value, _TD_QTR)
    val_rank = _rolling_rank_pct(val63, _TD_YEAR)
    val_flag = (val_rank >= 0.75).astype(float)
    return breadth + dual + val_flag


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_BUY_CLUSTER_EXTENDED_REGISTRY_001_075 = {
    "ibc_ext_001_buy_value_21d": {"inputs": ["insider_buy_value"], "func": ibc_ext_001_buy_value_21d},
    "ibc_ext_002_buy_value_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_002_buy_value_63d},
    "ibc_ext_003_buy_value_126d": {"inputs": ["insider_buy_value"], "func": ibc_ext_003_buy_value_126d},
    "ibc_ext_004_buy_value_252d": {"inputs": ["insider_buy_value"], "func": ibc_ext_004_buy_value_252d},
    "ibc_ext_005_buy_value_5d": {"inputs": ["insider_buy_value"], "func": ibc_ext_005_buy_value_5d},
    "ibc_ext_006_avg_buy_value_per_txn_63d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibc_ext_006_avg_buy_value_per_txn_63d},
    "ibc_ext_007_avg_buy_value_per_txn_21d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibc_ext_007_avg_buy_value_per_txn_21d},
    "ibc_ext_008_avg_buy_value_per_buyer_63d": {"inputs": ["insider_buy_value", "insider_buyers"], "func": ibc_ext_008_avg_buy_value_per_buyer_63d},
    "ibc_ext_009_peak_buy_value_single_day_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_009_peak_buy_value_single_day_63d},
    "ibc_ext_010_buy_value_concentration_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_010_buy_value_concentration_63d},
    "ibc_ext_011_buy_value_zscore_63d_in_252d": {"inputs": ["insider_buy_value"], "func": ibc_ext_011_buy_value_zscore_63d_in_252d},
    "ibc_ext_012_buy_value_zscore_21d_in_252d": {"inputs": ["insider_buy_value"], "func": ibc_ext_012_buy_value_zscore_21d_in_252d},
    "ibc_ext_013_buy_count_ewm21": {"inputs": ["insider_buy_count"], "func": ibc_ext_013_buy_count_ewm21},
    "ibc_ext_014_buy_count_ewm63": {"inputs": ["insider_buy_count"], "func": ibc_ext_014_buy_count_ewm63},
    "ibc_ext_015_buyers_ewm21": {"inputs": ["insider_buyers"], "func": ibc_ext_015_buyers_ewm21},
    "ibc_ext_016_buyers_ewm63": {"inputs": ["insider_buyers"], "func": ibc_ext_016_buyers_ewm63},
    "ibc_ext_017_buy_value_ewm21": {"inputs": ["insider_buy_value"], "func": ibc_ext_017_buy_value_ewm21},
    "ibc_ext_018_buy_value_ewm63": {"inputs": ["insider_buy_value"], "func": ibc_ext_018_buy_value_ewm63},
    "ibc_ext_019_officer_buy_count_ewm21": {"inputs": ["officer_buy_count"], "func": ibc_ext_019_officer_buy_count_ewm21},
    "ibc_ext_020_director_buy_count_ewm21": {"inputs": ["director_buy_count"], "func": ibc_ext_020_director_buy_count_ewm21},
    "ibc_ext_021_buy_count_ewm_fast_slow_diff": {"inputs": ["insider_buy_count"], "func": ibc_ext_021_buy_count_ewm_fast_slow_diff},
    "ibc_ext_022_buyers_ewm_fast_slow_diff": {"inputs": ["insider_buyers"], "func": ibc_ext_022_buyers_ewm_fast_slow_diff},
    "ibc_ext_023_buy_count_accel_21d": {"inputs": ["insider_buy_count"], "func": ibc_ext_023_buy_count_accel_21d},
    "ibc_ext_024_buy_count_accel_63d": {"inputs": ["insider_buy_count"], "func": ibc_ext_024_buy_count_accel_63d},
    "ibc_ext_025_buyers_accel_21d": {"inputs": ["insider_buyers"], "func": ibc_ext_025_buyers_accel_21d},
    "ibc_ext_026_buyers_accel_63d": {"inputs": ["insider_buyers"], "func": ibc_ext_026_buyers_accel_63d},
    "ibc_ext_027_buy_value_accel_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_027_buy_value_accel_63d},
    "ibc_ext_028_buy_count_growth_ratio_21d": {"inputs": ["insider_buy_count"], "func": ibc_ext_028_buy_count_growth_ratio_21d},
    "ibc_ext_029_buyers_growth_ratio_63d": {"inputs": ["insider_buyers"], "func": ibc_ext_029_buyers_growth_ratio_63d},
    "ibc_ext_030_active_days_accel_63d": {"inputs": ["insider_buy_count"], "func": ibc_ext_030_active_days_accel_63d},
    "ibc_ext_031_buy_count_5d_vs_63d_mean": {"inputs": ["insider_buy_count"], "func": ibc_ext_031_buy_count_5d_vs_63d_mean},
    "ibc_ext_032_buy_value_growth_ratio_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_032_buy_value_growth_ratio_63d},
    "ibc_ext_033_buyers_ewm_slope_proxy_21d": {"inputs": ["insider_buyers"], "func": ibc_ext_033_buyers_ewm_slope_proxy_21d},
    "ibc_ext_034_buy_count_accel_normalized_63d": {"inputs": ["insider_buy_count"], "func": ibc_ext_034_buy_count_accel_normalized_63d},
    "ibc_ext_035_days_since_cluster_21d": {"inputs": ["insider_buyers"], "func": ibc_ext_035_days_since_cluster_21d},
    "ibc_ext_036_days_since_strong_cluster_21d": {"inputs": ["insider_buyers"], "func": ibc_ext_036_days_since_strong_cluster_21d},
    "ibc_ext_037_days_since_cluster_63d": {"inputs": ["insider_buyers"], "func": ibc_ext_037_days_since_cluster_63d},
    "ibc_ext_038_days_since_last_officer_buy": {"inputs": ["officer_buy_count"], "func": ibc_ext_038_days_since_last_officer_buy},
    "ibc_ext_039_days_since_last_director_buy": {"inputs": ["director_buy_count"], "func": ibc_ext_039_days_since_last_director_buy},
    "ibc_ext_040_days_since_last_tenpct_buy": {"inputs": ["tenpct_buy_count"], "func": ibc_ext_040_days_since_last_tenpct_buy},
    "ibc_ext_041_buy_drought_length": {"inputs": ["insider_buy_count"], "func": ibc_ext_041_buy_drought_length},
    "ibc_ext_042_max_buy_drought_252d": {"inputs": ["insider_buy_count"], "func": ibc_ext_042_max_buy_drought_252d},
    "ibc_ext_043_consec_days_with_buy": {"inputs": ["insider_buy_count"], "func": ibc_ext_043_consec_days_with_buy},
    "ibc_ext_044_consec_weeks_with_cluster": {"inputs": ["insider_buyers"], "func": ibc_ext_044_consec_weeks_with_cluster},
    "ibc_ext_045_days_since_buy_value_spike_63d": {"inputs": ["insider_buy_value"], "func": ibc_ext_045_days_since_buy_value_spike_63d},
    "ibc_ext_046_days_since_peak_buyers_63d": {"inputs": ["insider_buyers"], "func": ibc_ext_046_days_since_peak_buyers_63d},
    "ibc_ext_047_role_diversity_count_63d": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_ext_047_role_diversity_count_63d},
    "ibc_ext_048_role_diversity_count_21d": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_ext_048_role_diversity_count_21d},
    "ibc_ext_049_officer_director_balance_63d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": ibc_ext_049_officer_director_balance_63d},
    "ibc_ext_050_officer_director_balance_21d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": ibc_ext_050_officer_director_balance_21d},
    "ibc_ext_051_role_concentration_hhi_63d": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_ext_051_role_concentration_hhi_63d},
    "ibc_ext_052_tenpct_share_of_value_proxy_63d": {"inputs": ["tenpct_buy_count", "insider_buy_count"], "func": ibc_ext_052_tenpct_share_of_value_proxy_63d},
    "ibc_ext_053_officer_director_combined_252d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": ibc_ext_053_officer_director_combined_252d},
    "ibc_ext_054_all_roles_combined_252d": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_ext_054_all_roles_combined_252d},
    "ibc_ext_055_officer_dir_dual_flag_126d": {"inputs": ["officer_buy_count", "director_buy_count"], "func": ibc_ext_055_officer_dir_dual_flag_126d},
    "ibc_ext_056_all_three_roles_flag_126d": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": ibc_ext_056_all_three_roles_flag_126d},
    "ibc_ext_057_officer_active_day_share_63d": {"inputs": ["officer_buy_count", "insider_buy_count"], "func": ibc_ext_057_officer_active_day_share_63d},
    "ibc_ext_058_director_active_day_share_63d": {"inputs": ["director_buy_count", "insider_buy_count"], "func": ibc_ext_058_director_active_day_share_63d},
    "ibc_ext_059_buyers_21d_pctrank_252d": {"inputs": ["insider_buyers"], "func": ibc_ext_059_buyers_21d_pctrank_252d},
    "ibc_ext_060_buyers_63d_pctrank_504d": {"inputs": ["insider_buyers"], "func": ibc_ext_060_buyers_63d_pctrank_504d},
    "ibc_ext_061_buy_count_63d_pctrank_252d": {"inputs": ["insider_buy_count"], "func": ibc_ext_061_buy_count_63d_pctrank_252d},
    "ibc_ext_062_buy_value_63d_pctrank_252d": {"inputs": ["insider_buy_value"], "func": ibc_ext_062_buy_value_63d_pctrank_252d},
    "ibc_ext_063_buyers_21d_expanding_pctrank": {"inputs": ["insider_buyers"], "func": ibc_ext_063_buyers_21d_expanding_pctrank},
    "ibc_ext_064_buy_value_21d_expanding_pctrank": {"inputs": ["insider_buy_value"], "func": ibc_ext_064_buy_value_21d_expanding_pctrank},
    "ibc_ext_065_buyers_63d_at_252d_max_flag": {"inputs": ["insider_buyers"], "func": ibc_ext_065_buyers_63d_at_252d_max_flag},
    "ibc_ext_066_buy_count_63d_at_252d_max_flag": {"inputs": ["insider_buy_count"], "func": ibc_ext_066_buy_count_63d_at_252d_max_flag},
    "ibc_ext_067_buyers_daily_std_63d": {"inputs": ["insider_buyers"], "func": ibc_ext_067_buyers_daily_std_63d},
    "ibc_ext_068_buy_count_daily_cv_63d": {"inputs": ["insider_buy_count"], "func": ibc_ext_068_buy_count_daily_cv_63d},
    "ibc_ext_069_value_weighted_cluster_intensity_63d": {"inputs": ["insider_buyers", "insider_buy_value"], "func": ibc_ext_069_value_weighted_cluster_intensity_63d},
    "ibc_ext_070_cluster_breadth_score_126d": {"inputs": ["insider_buyers", "officer_buy_count", "director_buy_count"], "func": ibc_ext_070_cluster_breadth_score_126d},
    "ibc_ext_071_strong_cluster_flag_126d": {"inputs": ["insider_buyers"], "func": ibc_ext_071_strong_cluster_flag_126d},
    "ibc_ext_072_recent_cluster_acceleration_flag": {"inputs": ["insider_buyers"], "func": ibc_ext_072_recent_cluster_acceleration_flag},
    "ibc_ext_073_buy_flow_zscore_composite": {"inputs": ["insider_buyers", "insider_buy_count", "insider_buy_value"], "func": ibc_ext_073_buy_flow_zscore_composite},
    "ibc_ext_074_cluster_persistence_score_126d": {"inputs": ["insider_buyers"], "func": ibc_ext_074_cluster_persistence_score_126d},
    "ibc_ext_075_capitulation_cluster_composite": {"inputs": ["insider_buyers", "officer_buy_count", "director_buy_count", "insider_buy_value"], "func": ibc_ext_075_capitulation_cluster_composite},
}
