"""
85_insider_role_weight — Extended Features 001-075
Domain: insider role/seniority weighting — additional variants: new windows,
        alternative weight schemes, role-mix dispersion/diversity, count-based
        seniority, role-rotation timing, percentile/z-score and composite angles.
Asset class: US equities | Sharadar SF2 insider transactions (daily event-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily Event-Aggregated Series Contract
-------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings — one row per (ticker, date) summing all transactions filed
that day.  These are EVENT-DRIVEN series: most days are ZERO because no filing
occurred.  Do NOT forward-fill.  Features aggregate over trailing windows using
rolling SUMS so sparse filing days accumulate correctly.  Functions look
strictly backward using .shift(positive), .rolling(), or .expanding().
Trading-day cadence: 1 week = 5, 1 month = 21, 1 quarter = 63, 1 year = 252,
2 years = 504.

Canonical input fields (lowercase):
    ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value,
    tenpct_buy_value, insider_buy_value,
    officer_buy_count, director_buy_count, tenpct_buy_count,
    officer_sell_value, director_sell_value
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WEEK  = 5
_TD_MONTH = 21
_TD_2MON  = 42
_TD_QTR   = 63
_TD_HALF  = 126
_TD_3QTR  = 189
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _active_days(s: pd.Series, w: int) -> pd.Series:
    """Count of filing days (value > 0) within trailing window — sparse-event helper."""
    return _rolling_sum((s > 0).astype(float), w)


def _days_since_positive(s: pd.Series) -> pd.Series:
    """Days elapsed since the series was last strictly positive (0 = today positive)."""
    pos = (s > 0).astype(float)
    idx = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    last = idx.where(pos == 1.0).ffill()
    return (idx - last)


def _alt_role_score(ceo, cfo, officer, director, tenpct, w):
    """Alternative steeper role-weighted score: CEO=5, CFO=4, officer=2, director=1.5, 10%=1."""
    return (
        5.0 * _rolling_sum(ceo, w)
        + 4.0 * _rolling_sum(cfo, w)
        + 2.0 * _rolling_sum(officer, w)
        + 1.5 * _rolling_sum(director, w)
        + 1.0 * _rolling_sum(tenpct, w)
    )


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Role-weighted score on new windows / alt weight schemes ---

def irw_ext_001_role_weighted_buy_score_week(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1 week: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_WEEK)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_WEEK)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_WEEK)
        + 2.0 * _rolling_sum(director_buy_value, _TD_WEEK)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_WEEK)
    )


def irw_ext_002_role_weighted_buy_score_2mon(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 2 months: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_2MON)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_2MON)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_2MON)
        + 2.0 * _rolling_sum(director_buy_value, _TD_2MON)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_2MON)
    )


def irw_ext_003_role_weighted_buy_score_3qtr(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 3 quarters: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_3QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_3QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_3QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_3QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_3QTR)
    )


def irw_ext_004_alt_role_score_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Steep role-weighted buy score over 1Q: CEO=5, CFO=4, officer=2, director=1.5, 10%=1."""
    return _alt_role_score(ceo_buy_value, cfo_buy_value, officer_buy_value,
                           director_buy_value, tenpct_buy_value, _TD_QTR)


def irw_ext_005_alt_role_score_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Steep role-weighted buy score over 1Y: CEO=5, CFO=4, officer=2, director=1.5, 10%=1."""
    return _alt_role_score(ceo_buy_value, cfo_buy_value, officer_buy_value,
                           director_buy_value, tenpct_buy_value, _TD_YEAR)


def irw_ext_006_alt_role_score_normalized_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Steep role-weighted 1Q buy score divided by total insider buy value (normalized)."""
    num = _alt_role_score(ceo_buy_value, cfo_buy_value, officer_buy_value,
                          director_buy_value, tenpct_buy_value, _TD_QTR)
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_QTR))


def irw_ext_007_ceo_only_weighted_score_1q(ceo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CEO buy value weighted at 4x as a fraction of total 1Q insider buy value."""
    return _safe_div(4.0 * _rolling_sum(ceo_buy_value, _TD_QTR),
                     _rolling_sum(insider_buy_value, _TD_QTR))


def irw_ext_008_role_weighted_score_half(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over half year: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_HALF)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_HALF)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_HALF)
        + 2.0 * _rolling_sum(director_buy_value, _TD_HALF)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_HALF)
    )


def irw_ext_009_top_officer_weighted_value_1q(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """4x-weighted CEO+CFO buy value over 1 quarter (top-officer conviction magnitude)."""
    return 4.0 * _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)


def irw_ext_010_role_weighted_score_2mon_normalized(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted 2-month buy score divided by total insider buy value (normalized)."""
    num = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_2MON)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_2MON)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_2MON)
        + 2.0 * _rolling_sum(director_buy_value, _TD_2MON)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_2MON)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_2MON))


def irw_ext_011_role_weighted_count_score_half(
    officer_buy_count: pd.Series, director_buy_count: pd.Series, tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Role-weighted buy count score over half year: officer=3, director=2, 10%-owner=1."""
    return (
        3.0 * _rolling_sum(officer_buy_count, _TD_HALF)
        + 2.0 * _rolling_sum(director_buy_count, _TD_HALF)
        + 1.0 * _rolling_sum(tenpct_buy_count, _TD_HALF)
    )


def irw_ext_012_role_weighted_count_score_2y(
    officer_buy_count: pd.Series, director_buy_count: pd.Series, tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Role-weighted buy count score over 2 years: officer=3, director=2, 10%-owner=1."""
    return (
        3.0 * _rolling_sum(officer_buy_count, _TD_2Y)
        + 2.0 * _rolling_sum(director_buy_count, _TD_2Y)
        + 1.0 * _rolling_sum(tenpct_buy_count, _TD_2Y)
    )


# --- Group B (013-024): Role-mix dispersion / diversity / Herfindahl ---

def irw_ext_013_role_mix_herfindahl_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Herfindahl concentration of 1Q buy value across 5 role classes (1=single role)."""
    c = _rolling_sum(ceo_buy_value, _TD_QTR)
    f = _rolling_sum(cfo_buy_value, _TD_QTR)
    o = _rolling_sum(officer_buy_value, _TD_QTR)
    d = _rolling_sum(director_buy_value, _TD_QTR)
    t = _rolling_sum(tenpct_buy_value, _TD_QTR)
    total = (c + f + o + d + t).replace(0, np.nan)
    return ((c / total) ** 2 + (f / total) ** 2 + (o / total) ** 2
            + (d / total) ** 2 + (t / total) ** 2)


def irw_ext_014_role_mix_herfindahl_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Herfindahl concentration of 1Y buy value across 5 role classes."""
    c = _rolling_sum(ceo_buy_value, _TD_YEAR)
    f = _rolling_sum(cfo_buy_value, _TD_YEAR)
    o = _rolling_sum(officer_buy_value, _TD_YEAR)
    d = _rolling_sum(director_buy_value, _TD_YEAR)
    t = _rolling_sum(tenpct_buy_value, _TD_YEAR)
    total = (c + f + o + d + t).replace(0, np.nan)
    return ((c / total) ** 2 + (f / total) ** 2 + (o / total) ** 2
            + (d / total) ** 2 + (t / total) ** 2)


def irw_ext_015_distinct_roles_buying_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Count of distinct role classes (0-5) with any buy value over 1 quarter."""
    return (
        (_rolling_sum(ceo_buy_value, _TD_QTR) > 0).astype(float)
        + (_rolling_sum(cfo_buy_value, _TD_QTR) > 0).astype(float)
        + (_rolling_sum(officer_buy_value, _TD_QTR) > 0).astype(float)
        + (_rolling_sum(director_buy_value, _TD_QTR) > 0).astype(float)
        + (_rolling_sum(tenpct_buy_value, _TD_QTR) > 0).astype(float)
    )


def irw_ext_016_distinct_roles_buying_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Count of distinct role classes (0-5) with any buy value over 1 year."""
    return (
        (_rolling_sum(ceo_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(cfo_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(officer_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(director_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(tenpct_buy_value, _TD_YEAR) > 0).astype(float)
    )


def irw_ext_017_all_roles_buying_flag_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if all 5 role classes had buy value over 1 year (broad-based conviction)."""
    return (
        (_rolling_sum(ceo_buy_value, _TD_YEAR) > 0)
        & (_rolling_sum(cfo_buy_value, _TD_YEAR) > 0)
        & (_rolling_sum(officer_buy_value, _TD_YEAR) > 0)
        & (_rolling_sum(director_buy_value, _TD_YEAR) > 0)
        & (_rolling_sum(tenpct_buy_value, _TD_YEAR) > 0)
    ).astype(float)


def irw_ext_018_role_value_max_share_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Largest single-role share of total 1Q role buy value (dominant-role concentration)."""
    c = _rolling_sum(ceo_buy_value, _TD_QTR)
    f = _rolling_sum(cfo_buy_value, _TD_QTR)
    o = _rolling_sum(officer_buy_value, _TD_QTR)
    d = _rolling_sum(director_buy_value, _TD_QTR)
    t = _rolling_sum(tenpct_buy_value, _TD_QTR)
    total = (c + f + o + d + t).replace(0, np.nan)
    mx = pd.concat([c, f, o, d, t], axis=1).max(axis=1)
    return _safe_div(mx, total)


def irw_ext_019_role_diversity_score_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role diversity over 1Y: 1 minus Herfindahl of buy value across 5 role classes."""
    c = _rolling_sum(ceo_buy_value, _TD_YEAR)
    f = _rolling_sum(cfo_buy_value, _TD_YEAR)
    o = _rolling_sum(officer_buy_value, _TD_YEAR)
    d = _rolling_sum(director_buy_value, _TD_YEAR)
    t = _rolling_sum(tenpct_buy_value, _TD_YEAR)
    total = (c + f + o + d + t).replace(0, np.nan)
    hhi = ((c / total) ** 2 + (f / total) ** 2 + (o / total) ** 2
           + (d / total) ** 2 + (t / total) ** 2)
    return 1.0 - hhi


def irw_ext_020_senior_vs_junior_value_ratio_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of senior (CEO+CFO+officer) to junior (director+10%) buy value over 1Q."""
    senior = _rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_QTR)
    junior = _rolling_sum(director_buy_value + tenpct_buy_value, _TD_QTR)
    return _safe_div(senior, junior)


def irw_ext_021_senior_vs_junior_value_ratio_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of senior (CEO+CFO+officer) to junior (director+10%) buy value over 1Y."""
    senior = _rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_YEAR)
    junior = _rolling_sum(director_buy_value + tenpct_buy_value, _TD_YEAR)
    return _safe_div(senior, junior)


def irw_ext_022_senior_value_share_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1Q total insider buy value from senior insiders (CEO+CFO+officer)."""
    return _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_QTR),
                     _rolling_sum(insider_buy_value, _TD_QTR))


def irw_ext_023_role_count_diversity_1y(
    officer_buy_count: pd.Series, director_buy_count: pd.Series, tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Count-role diversity over 1Y: 1 minus Herfindahl of buy count across 3 role classes."""
    o = _rolling_sum(officer_buy_count, _TD_YEAR)
    d = _rolling_sum(director_buy_count, _TD_YEAR)
    t = _rolling_sum(tenpct_buy_count, _TD_YEAR)
    total = (o + d + t).replace(0, np.nan)
    hhi = (o / total) ** 2 + (d / total) ** 2 + (t / total) ** 2
    return 1.0 - hhi


def irw_ext_024_top_officer_dominance_flag_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if CEO+CFO account for over half of 1Q insider buy value."""
    share = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR))
    return (share > 0.5).astype(float)


# --- Group C (025-038): Count-based seniority and active-day intensity ---

def irw_ext_025_ceo_buy_active_days_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Count of days with any CEO buy filing in trailing 1 year."""
    return _active_days(ceo_buy_value, _TD_YEAR)


def irw_ext_026_cfo_buy_active_days_1y(cfo_buy_value: pd.Series) -> pd.Series:
    """Count of days with any CFO buy filing in trailing 1 year."""
    return _active_days(cfo_buy_value, _TD_YEAR)


def irw_ext_027_officer_buy_active_days_1q(officer_buy_value: pd.Series) -> pd.Series:
    """Count of days with any officer buy filing in trailing 1 quarter."""
    return _active_days(officer_buy_value, _TD_QTR)


def irw_ext_028_director_buy_active_days_1y(director_buy_value: pd.Series) -> pd.Series:
    """Count of days with any director buy filing in trailing 1 year."""
    return _active_days(director_buy_value, _TD_YEAR)


def irw_ext_029_senior_buy_active_days_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
) -> pd.Series:
    """Count of days with any senior (CEO/CFO/officer) buy filing in trailing 1Q."""
    return _active_days(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_QTR)


def irw_ext_030_days_since_ceo_buy(ceo_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last CEO buy filing day."""
    return _days_since_positive(ceo_buy_value)


def irw_ext_031_days_since_cfo_buy(cfo_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last CFO buy filing day."""
    return _days_since_positive(cfo_buy_value)


def irw_ext_032_days_since_top_officer_buy(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last CEO or CFO buy filing day."""
    return _days_since_positive(ceo_buy_value + cfo_buy_value)


def irw_ext_033_days_since_officer_buy(officer_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last officer buy filing day."""
    return _days_since_positive(officer_buy_value)


def irw_ext_034_ceo_buy_count_2y(ceo_buy_value: pd.Series) -> pd.Series:
    """Count of CEO buy filing days over trailing 2 years (long-horizon conviction)."""
    return _active_days(ceo_buy_value, _TD_2Y)


def irw_ext_035_role_weighted_active_days_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """
    Role-weighted active-day score over 1Q: each filing day weighted by role
    seniority (CEO/CFO=4, officer=3, director=2, 10%-owner=1) and summed.
    """
    return (
        4.0 * _active_days(ceo_buy_value, _TD_QTR)
        + 4.0 * _active_days(cfo_buy_value, _TD_QTR)
        + 3.0 * _active_days(officer_buy_value, _TD_QTR)
        + 2.0 * _active_days(director_buy_value, _TD_QTR)
        + 1.0 * _active_days(tenpct_buy_value, _TD_QTR)
    )


def irw_ext_036_top_officer_active_day_fraction_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series,
) -> pd.Series:
    """Fraction of trailing 1Y days with a CEO or CFO buy filing."""
    return _active_days(ceo_buy_value + cfo_buy_value, _TD_YEAR) / float(_TD_YEAR)


def irw_ext_037_officer_to_director_active_day_ratio_1y(
    officer_buy_value: pd.Series, director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy filing days to director buy filing days over 1 year."""
    return _safe_div(_active_days(officer_buy_value, _TD_YEAR),
                     _active_days(director_buy_value, _TD_YEAR))


def irw_ext_038_ceo_buy_drought_flag_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary flag: zero CEO buy value over the trailing 1-year window (top-insider drought)."""
    return (_rolling_sum(ceo_buy_value, _TD_YEAR) <= _EPS).astype(float)


# --- Group D (039-050): Cross-role ratios and shares on new windows ---

def irw_ext_039_ceo_to_director_value_ratio_1q(
    ceo_buy_value: pd.Series, director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of CEO buy value to director buy value over 1 quarter."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_QTR),
                     _rolling_sum(director_buy_value, _TD_QTR))


def irw_ext_040_cfo_to_director_value_ratio_1q(
    cfo_buy_value: pd.Series, director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of CFO buy value to director buy value over 1 quarter."""
    return _safe_div(_rolling_sum(cfo_buy_value, _TD_QTR),
                     _rolling_sum(director_buy_value, _TD_QTR))


def irw_ext_041_ceo_to_cfo_value_ratio_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of CEO buy value to CFO buy value over 1 year."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_YEAR),
                     _rolling_sum(cfo_buy_value, _TD_YEAR))


def irw_ext_042_officer_to_tenpct_value_ratio_1y(
    officer_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy value to 10%-owner buy value over 1 year."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_YEAR),
                     _rolling_sum(tenpct_buy_value, _TD_YEAR))


def irw_ext_043_top_officer_value_share_2mon(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 2-month insider buy value attributable to CEO + CFO."""
    return _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_2MON),
                     _rolling_sum(insider_buy_value, _TD_2MON))


def irw_ext_044_officer_value_share_3qtr(
    officer_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 3-quarter insider buy value from all officers."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_3QTR),
                     _rolling_sum(insider_buy_value, _TD_3QTR))


def irw_ext_045_director_value_share_2y(
    director_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 2-year insider buy value from directors."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_2Y),
                     _rolling_sum(insider_buy_value, _TD_2Y))


def irw_ext_046_tenpct_value_share_2y(
    tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 2-year insider buy value from 10%-owners."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _TD_2Y),
                     _rolling_sum(insider_buy_value, _TD_2Y))


def irw_ext_047_ceo_value_share_1y(
    ceo_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from CEO alone."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_YEAR),
                     _rolling_sum(insider_buy_value, _TD_YEAR))


def irw_ext_048_top_officer_concentration_2mon(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
) -> pd.Series:
    """CEO+CFO buy value as share of all-officer buy value over 2 months."""
    return _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_2MON),
                     _rolling_sum(officer_buy_value, _TD_2MON))


def irw_ext_049_officer_to_director_count_ratio_half(
    officer_buy_count: pd.Series, director_buy_count: pd.Series,
) -> pd.Series:
    """Ratio of officer buy count to director buy count over half year."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_HALF),
                     _rolling_sum(director_buy_count, _TD_HALF))


def irw_ext_050_top_officer_count_share_half(
    officer_buy_count: pd.Series, director_buy_count: pd.Series, tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Share of half-year insider buy count from officers (vs directors + 10%-owners)."""
    num = _rolling_sum(officer_buy_count, _TD_HALF)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_HALF)
    return _safe_div(num, den)


# --- Group E (051-062): Seniority conviction on new windows / smoothing ---

def irw_ext_051_seniority_conviction_index_2mon(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority-weighted conviction index over 2 months (CEO=1.0,CFO=0.9,off=0.6,dir=0.4,10%=0.2)."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_2MON)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_2MON)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_2MON)
        + 0.4 * _rolling_sum(director_buy_value, _TD_2MON)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_2MON)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_2MON))


def irw_ext_052_seniority_conviction_index_3qtr(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority-weighted conviction index over 3 quarters."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_3QTR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_3QTR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_3QTR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_3QTR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_3QTR)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_3QTR))


def irw_ext_053_seniority_conviction_index_week(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority-weighted conviction index over 1 week (very recent dollar seniority)."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_WEEK)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_WEEK)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_WEEK)
        + 0.4 * _rolling_sum(director_buy_value, _TD_WEEK)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_WEEK)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_WEEK))


def irw_ext_054_seniority_conviction_ewm(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=63) of the daily seniority-weighted conviction ratio."""
    num = (1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
           + 0.4 * director_buy_value + 0.2 * tenpct_buy_value)
    daily = _safe_div(num, insider_buy_value).fillna(0.0)
    return _ewm_mean(daily, _TD_QTR)


def irw_ext_055_seniority_conviction_index_2y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority-weighted conviction index over 2 years (long-horizon baseline)."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_2Y)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_2Y)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_2Y)
        + 0.4 * _rolling_sum(director_buy_value, _TD_2Y)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_2Y)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_2Y))


def irw_ext_056_seniority_shift_2mon_vs_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """2-month seniority conviction minus 1-year seniority conviction (recent seniority rotation)."""
    def _sci(w):
        num = (1.0 * _rolling_sum(ceo_buy_value, w) + 0.9 * _rolling_sum(cfo_buy_value, w)
               + 0.6 * _rolling_sum(officer_buy_value, w) + 0.4 * _rolling_sum(director_buy_value, w)
               + 0.2 * _rolling_sum(tenpct_buy_value, w))
        return _safe_div(num, _rolling_sum(insider_buy_value, w))
    return _sci(_TD_2MON) - _sci(_TD_YEAR)


def irw_ext_057_seniority_shift_1q_vs_2y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """1-quarter seniority conviction minus 2-year seniority conviction (medium-term rotation)."""
    def _sci(w):
        num = (1.0 * _rolling_sum(ceo_buy_value, w) + 0.9 * _rolling_sum(cfo_buy_value, w)
               + 0.6 * _rolling_sum(officer_buy_value, w) + 0.4 * _rolling_sum(director_buy_value, w)
               + 0.2 * _rolling_sum(tenpct_buy_value, w))
        return _safe_div(num, _rolling_sum(insider_buy_value, w))
    return _sci(_TD_QTR) - _sci(_TD_2Y)


def irw_ext_058_seniority_conviction_zscore_2y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of the daily seniority conviction ratio within a trailing 2-year window."""
    num = (1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
           + 0.4 * director_buy_value + 0.2 * tenpct_buy_value)
    daily = _safe_div(num, insider_buy_value).fillna(0.0)
    return _zscore_rolling(daily, _TD_2Y)


def irw_ext_059_seniority_conviction_pct_rank_2y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Percentile rank of the daily seniority conviction ratio within a 2-year window."""
    num = (1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
           + 0.4 * director_buy_value + 0.2 * tenpct_buy_value)
    daily = _safe_div(num, insider_buy_value).fillna(0.0)
    return _rolling_rank_pct(daily, _TD_2Y)


def irw_ext_060_role_weighted_score_pct_rank_2y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Percentile rank of the 1Q role-weighted buy score within a trailing 2-year window."""
    score = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    return _rolling_rank_pct(score, _TD_2Y)


def irw_ext_061_role_weighted_score_zscore_half(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of the daily role-weighted buy score within a trailing half-year window."""
    score = (4.0 * ceo_buy_value + 4.0 * cfo_buy_value + 3.0 * officer_buy_value
             + 2.0 * director_buy_value + 1.0 * tenpct_buy_value)
    return _zscore_rolling(score, _TD_HALF)


def irw_ext_062_top_officer_value_share_zscore_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of the rolling 63-day top-officer value share within a 252-day window."""
    share = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR))
    return _zscore_rolling(share, _TD_YEAR)


# --- Group F (063-070): Role net-buy skew using sell data ---

def irw_ext_063_officer_net_buy_skew_1y(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net-buy fraction over 1 year: (buy-sell)/(buy+sell)."""
    b = _rolling_sum(officer_buy_value, _TD_YEAR)
    s = _rolling_sum(officer_sell_value, _TD_YEAR)
    return _safe_div(b - s, (b + s).replace(0, np.nan))


def irw_ext_064_director_net_buy_skew_1y(
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Director net-buy fraction over 1 year: (buy-sell)/(buy+sell)."""
    b = _rolling_sum(director_buy_value, _TD_YEAR)
    s = _rolling_sum(director_sell_value, _TD_YEAR)
    return _safe_div(b - s, (b + s).replace(0, np.nan))


def irw_ext_065_officer_net_buy_value_1q(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy value (buy minus sell) over 1 quarter."""
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)


def irw_ext_066_director_net_buy_value_1q(
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy value (buy minus sell) over 1 quarter."""
    return _rolling_sum(director_buy_value - director_sell_value, _TD_QTR)


def irw_ext_067_senior_class_net_buy_value_1y(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Combined officer+director net buy value (buy minus sell) over 1 year."""
    return _rolling_sum((officer_buy_value + director_buy_value)
                        - (officer_sell_value + director_sell_value), _TD_YEAR)


def irw_ext_068_officer_minus_director_net_skew_1y(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Officer net-buy fraction minus director net-buy fraction over 1 year (role skew gap)."""
    ob = _rolling_sum(officer_buy_value, _TD_YEAR)
    os = _rolling_sum(officer_sell_value, _TD_YEAR)
    db = _rolling_sum(director_buy_value, _TD_YEAR)
    ds = _rolling_sum(director_sell_value, _TD_YEAR)
    off = _safe_div(ob - os, (ob + os).replace(0, np.nan)).fillna(0.0)
    dirr = _safe_div(db - ds, (db + ds).replace(0, np.nan)).fillna(0.0)
    return off - dirr


def irw_ext_069_officer_net_buyer_flag_1y(
    officer_buy_value: pd.Series, officer_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if officers were net buyers (buy value exceeds sell value) over 1 year."""
    return (_rolling_sum(officer_buy_value, _TD_YEAR)
            > _rolling_sum(officer_sell_value, _TD_YEAR)).astype(float)


def irw_ext_070_director_net_buyer_flag_1y(
    director_buy_value: pd.Series, director_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if directors were net buyers (buy value exceeds sell value) over 1 year."""
    return (_rolling_sum(director_buy_value, _TD_YEAR)
            > _rolling_sum(director_sell_value, _TD_YEAR)).astype(float)


# --- Group G (071-075): Composites ---

def irw_ext_071_senior_buy_breadth_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
) -> pd.Series:
    """Count of distinct senior role classes (CEO/CFO/officer, 0-3) buying over 1 year."""
    return (
        (_rolling_sum(ceo_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(cfo_buy_value, _TD_YEAR) > 0).astype(float)
        + (_rolling_sum(officer_buy_value, _TD_YEAR) > 0).astype(float)
    )


def irw_ext_072_role_weighted_score_2mon_ewm_ratio(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series,
) -> pd.Series:
    """2-month role-weighted score divided by its 252-day EWM (role-conviction momentum ratio)."""
    score = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_2MON)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_2MON)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_2MON)
        + 2.0 * _rolling_sum(director_buy_value, _TD_2MON)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_2MON)
    )
    return _safe_div(score, _ewm_mean(score, _TD_YEAR))


def irw_ext_073_seniority_conviction_expanding_pct_rank(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """Expanding all-history percentile rank of the 1Q seniority conviction index."""
    num = (1.0 * _rolling_sum(ceo_buy_value, _TD_QTR) + 0.9 * _rolling_sum(cfo_buy_value, _TD_QTR)
           + 0.6 * _rolling_sum(officer_buy_value, _TD_QTR) + 0.4 * _rolling_sum(director_buy_value, _TD_QTR)
           + 0.2 * _rolling_sum(tenpct_buy_value, _TD_QTR))
    sci = _safe_div(num, _rolling_sum(insider_buy_value, _TD_QTR))
    return sci.expanding(min_periods=2).rank(pct=True)


def irw_ext_074_top_officer_capitulation_signal_1q(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Top-officer capitulation signal over 1Q: equally-weighted average of the
    top-officer (CEO+CFO) value share, the senior-value share, and a binary
    CEO+CFO presence flag. Higher = stronger senior-led distress buying.
    """
    top_share = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
                          _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    senior_share = _safe_div(
        _rolling_sum(ceo_buy_value + cfo_buy_value + officer_buy_value, _TD_QTR),
        _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    presence = (_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR) > 0).astype(float)
    return (top_share + senior_share + presence) / 3.0


def irw_ext_075_seniority_extreme_composite_1y(
    ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_value: pd.Series,
    director_buy_value: pd.Series, tenpct_buy_value: pd.Series, insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Seniority-extreme composite: equally-weighted average of the 1Y seniority
    conviction percentile rank, the 1Y role-weighted-score percentile rank, and
    the role-diversity score — all over a 2-year reference. Captures broad,
    historically extreme, senior-tilted insider buying at distress lows.
    """
    num = (1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
           + 0.4 * director_buy_value + 0.2 * tenpct_buy_value)
    sci = _safe_div(num, insider_buy_value).fillna(0.0)
    sci_rank = _rolling_rank_pct(sci, _TD_2Y).fillna(0.0)
    score = (4.0 * ceo_buy_value + 4.0 * cfo_buy_value + 3.0 * officer_buy_value
             + 2.0 * director_buy_value + 1.0 * tenpct_buy_value)
    score_rank = _rolling_rank_pct(score, _TD_2Y).fillna(0.0)
    c = _rolling_sum(ceo_buy_value, _TD_YEAR)
    f = _rolling_sum(cfo_buy_value, _TD_YEAR)
    o = _rolling_sum(officer_buy_value, _TD_YEAR)
    d = _rolling_sum(director_buy_value, _TD_YEAR)
    t = _rolling_sum(tenpct_buy_value, _TD_YEAR)
    total = (c + f + o + d + t).replace(0, np.nan)
    hhi = ((c / total) ** 2 + (f / total) ** 2 + (o / total) ** 2
           + (d / total) ** 2 + (t / total) ** 2)
    diversity = (1.0 - hhi).fillna(0.0)
    return (sci_rank + score_rank + diversity) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_ROLE_WEIGHT_EXTENDED_REGISTRY_001_075 = {
    "irw_ext_001_role_weighted_buy_score_week": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_001_role_weighted_buy_score_week},
    "irw_ext_002_role_weighted_buy_score_2mon": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_002_role_weighted_buy_score_2mon},
    "irw_ext_003_role_weighted_buy_score_3qtr": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_003_role_weighted_buy_score_3qtr},
    "irw_ext_004_alt_role_score_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_004_alt_role_score_1q},
    "irw_ext_005_alt_role_score_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_005_alt_role_score_1y},
    "irw_ext_006_alt_role_score_normalized_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_006_alt_role_score_normalized_1q},
    "irw_ext_007_ceo_only_weighted_score_1q": {"inputs": ["ceo_buy_value", "insider_buy_value"], "func": irw_ext_007_ceo_only_weighted_score_1q},
    "irw_ext_008_role_weighted_score_half": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_008_role_weighted_score_half},
    "irw_ext_009_top_officer_weighted_value_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value"], "func": irw_ext_009_top_officer_weighted_value_1q},
    "irw_ext_010_role_weighted_score_2mon_normalized": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_010_role_weighted_score_2mon_normalized},
    "irw_ext_011_role_weighted_count_score_half": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": irw_ext_011_role_weighted_count_score_half},
    "irw_ext_012_role_weighted_count_score_2y": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": irw_ext_012_role_weighted_count_score_2y},
    "irw_ext_013_role_mix_herfindahl_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_013_role_mix_herfindahl_1q},
    "irw_ext_014_role_mix_herfindahl_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_014_role_mix_herfindahl_1y},
    "irw_ext_015_distinct_roles_buying_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_015_distinct_roles_buying_1q},
    "irw_ext_016_distinct_roles_buying_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_016_distinct_roles_buying_1y},
    "irw_ext_017_all_roles_buying_flag_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_017_all_roles_buying_flag_1y},
    "irw_ext_018_role_value_max_share_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_018_role_value_max_share_1q},
    "irw_ext_019_role_diversity_score_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_019_role_diversity_score_1y},
    "irw_ext_020_senior_vs_junior_value_ratio_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_020_senior_vs_junior_value_ratio_1q},
    "irw_ext_021_senior_vs_junior_value_ratio_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_021_senior_vs_junior_value_ratio_1y},
    "irw_ext_022_senior_value_share_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "insider_buy_value"], "func": irw_ext_022_senior_value_share_1q},
    "irw_ext_023_role_count_diversity_1y": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": irw_ext_023_role_count_diversity_1y},
    "irw_ext_024_top_officer_dominance_flag_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"], "func": irw_ext_024_top_officer_dominance_flag_1q},
    "irw_ext_025_ceo_buy_active_days_1y": {"inputs": ["ceo_buy_value"], "func": irw_ext_025_ceo_buy_active_days_1y},
    "irw_ext_026_cfo_buy_active_days_1y": {"inputs": ["cfo_buy_value"], "func": irw_ext_026_cfo_buy_active_days_1y},
    "irw_ext_027_officer_buy_active_days_1q": {"inputs": ["officer_buy_value"], "func": irw_ext_027_officer_buy_active_days_1q},
    "irw_ext_028_director_buy_active_days_1y": {"inputs": ["director_buy_value"], "func": irw_ext_028_director_buy_active_days_1y},
    "irw_ext_029_senior_buy_active_days_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"], "func": irw_ext_029_senior_buy_active_days_1q},
    "irw_ext_030_days_since_ceo_buy": {"inputs": ["ceo_buy_value"], "func": irw_ext_030_days_since_ceo_buy},
    "irw_ext_031_days_since_cfo_buy": {"inputs": ["cfo_buy_value"], "func": irw_ext_031_days_since_cfo_buy},
    "irw_ext_032_days_since_top_officer_buy": {"inputs": ["ceo_buy_value", "cfo_buy_value"], "func": irw_ext_032_days_since_top_officer_buy},
    "irw_ext_033_days_since_officer_buy": {"inputs": ["officer_buy_value"], "func": irw_ext_033_days_since_officer_buy},
    "irw_ext_034_ceo_buy_count_2y": {"inputs": ["ceo_buy_value"], "func": irw_ext_034_ceo_buy_count_2y},
    "irw_ext_035_role_weighted_active_days_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_035_role_weighted_active_days_1q},
    "irw_ext_036_top_officer_active_day_fraction_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value"], "func": irw_ext_036_top_officer_active_day_fraction_1y},
    "irw_ext_037_officer_to_director_active_day_ratio_1y": {"inputs": ["officer_buy_value", "director_buy_value"], "func": irw_ext_037_officer_to_director_active_day_ratio_1y},
    "irw_ext_038_ceo_buy_drought_flag_1y": {"inputs": ["ceo_buy_value"], "func": irw_ext_038_ceo_buy_drought_flag_1y},
    "irw_ext_039_ceo_to_director_value_ratio_1q": {"inputs": ["ceo_buy_value", "director_buy_value"], "func": irw_ext_039_ceo_to_director_value_ratio_1q},
    "irw_ext_040_cfo_to_director_value_ratio_1q": {"inputs": ["cfo_buy_value", "director_buy_value"], "func": irw_ext_040_cfo_to_director_value_ratio_1q},
    "irw_ext_041_ceo_to_cfo_value_ratio_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value"], "func": irw_ext_041_ceo_to_cfo_value_ratio_1y},
    "irw_ext_042_officer_to_tenpct_value_ratio_1y": {"inputs": ["officer_buy_value", "tenpct_buy_value"], "func": irw_ext_042_officer_to_tenpct_value_ratio_1y},
    "irw_ext_043_top_officer_value_share_2mon": {"inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"], "func": irw_ext_043_top_officer_value_share_2mon},
    "irw_ext_044_officer_value_share_3qtr": {"inputs": ["officer_buy_value", "insider_buy_value"], "func": irw_ext_044_officer_value_share_3qtr},
    "irw_ext_045_director_value_share_2y": {"inputs": ["director_buy_value", "insider_buy_value"], "func": irw_ext_045_director_value_share_2y},
    "irw_ext_046_tenpct_value_share_2y": {"inputs": ["tenpct_buy_value", "insider_buy_value"], "func": irw_ext_046_tenpct_value_share_2y},
    "irw_ext_047_ceo_value_share_1y": {"inputs": ["ceo_buy_value", "insider_buy_value"], "func": irw_ext_047_ceo_value_share_1y},
    "irw_ext_048_top_officer_concentration_2mon": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"], "func": irw_ext_048_top_officer_concentration_2mon},
    "irw_ext_049_officer_to_director_count_ratio_half": {"inputs": ["officer_buy_count", "director_buy_count"], "func": irw_ext_049_officer_to_director_count_ratio_half},
    "irw_ext_050_top_officer_count_share_half": {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"], "func": irw_ext_050_top_officer_count_share_half},
    "irw_ext_051_seniority_conviction_index_2mon": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_051_seniority_conviction_index_2mon},
    "irw_ext_052_seniority_conviction_index_3qtr": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_052_seniority_conviction_index_3qtr},
    "irw_ext_053_seniority_conviction_index_week": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_053_seniority_conviction_index_week},
    "irw_ext_054_seniority_conviction_ewm": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_054_seniority_conviction_ewm},
    "irw_ext_055_seniority_conviction_index_2y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_055_seniority_conviction_index_2y},
    "irw_ext_056_seniority_shift_2mon_vs_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_056_seniority_shift_2mon_vs_1y},
    "irw_ext_057_seniority_shift_1q_vs_2y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_057_seniority_shift_1q_vs_2y},
    "irw_ext_058_seniority_conviction_zscore_2y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_058_seniority_conviction_zscore_2y},
    "irw_ext_059_seniority_conviction_pct_rank_2y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_059_seniority_conviction_pct_rank_2y},
    "irw_ext_060_role_weighted_score_pct_rank_2y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_060_role_weighted_score_pct_rank_2y},
    "irw_ext_061_role_weighted_score_zscore_half": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_061_role_weighted_score_zscore_half},
    "irw_ext_062_top_officer_value_share_zscore_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"], "func": irw_ext_062_top_officer_value_share_zscore_1y},
    "irw_ext_063_officer_net_buy_skew_1y": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": irw_ext_063_officer_net_buy_skew_1y},
    "irw_ext_064_director_net_buy_skew_1y": {"inputs": ["director_buy_value", "director_sell_value"], "func": irw_ext_064_director_net_buy_skew_1y},
    "irw_ext_065_officer_net_buy_value_1q": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": irw_ext_065_officer_net_buy_value_1q},
    "irw_ext_066_director_net_buy_value_1q": {"inputs": ["director_buy_value", "director_sell_value"], "func": irw_ext_066_director_net_buy_value_1q},
    "irw_ext_067_senior_class_net_buy_value_1y": {"inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"], "func": irw_ext_067_senior_class_net_buy_value_1y},
    "irw_ext_068_officer_minus_director_net_skew_1y": {"inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"], "func": irw_ext_068_officer_minus_director_net_skew_1y},
    "irw_ext_069_officer_net_buyer_flag_1y": {"inputs": ["officer_buy_value", "officer_sell_value"], "func": irw_ext_069_officer_net_buyer_flag_1y},
    "irw_ext_070_director_net_buyer_flag_1y": {"inputs": ["director_buy_value", "director_sell_value"], "func": irw_ext_070_director_net_buyer_flag_1y},
    "irw_ext_071_senior_buy_breadth_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"], "func": irw_ext_071_senior_buy_breadth_1y},
    "irw_ext_072_role_weighted_score_2mon_ewm_ratio": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"], "func": irw_ext_072_role_weighted_score_2mon_ewm_ratio},
    "irw_ext_073_seniority_conviction_expanding_pct_rank": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_073_seniority_conviction_expanding_pct_rank},
    "irw_ext_074_top_officer_capitulation_signal_1q": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "insider_buy_value"], "func": irw_ext_074_top_officer_capitulation_signal_1q},
    "irw_ext_075_seniority_extreme_composite_1y": {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"], "func": irw_ext_075_seniority_extreme_composite_1y},
}
