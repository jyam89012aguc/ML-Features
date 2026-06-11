"""
85_insider_role_weight — Base Features 001-100
Domain: insider role/seniority weighting — CEO/CFO vs officer vs director vs 10%-owner
Asset class: US equities | Sharadar SF2 insider transactions (daily event-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily Event-Aggregated Series Contract
-------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series
aggregated from Sharadar SF2 insider transaction filings.  The pipeline produces
one row per (ticker, date) summing all transactions filed on that date.
IMPORTANT: these are EVENT-DRIVEN series — most days are ZERO because no filing
occurred.  Do NOT forward-fill.  Features aggregate over trailing windows using
rolling SUMS so that sparse filing days accumulate correctly.
All functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day cadence: 1 week = 5 days, 1 month = 21 days,
1 quarter = 63 days, 1 year = 252 days, 2 years = 504 days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WEEK  = 5
_TD_MONTH = 21
_TD_QTR   = 63
_TD_HALF  = 126
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Role-weighted buy score ---

def irw_001_role_weighted_buy_score_1m(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1 month: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    w = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_MONTH)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_MONTH)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_MONTH)
        + 2.0 * _rolling_sum(director_buy_value, _TD_MONTH)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_MONTH)
    )
    return w


def irw_002_role_weighted_buy_score_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1 quarter: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    w = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    return w


def irw_003_role_weighted_buy_score_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1 year: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    w = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_YEAR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_YEAR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_YEAR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_YEAR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_YEAR)
    )
    return w


def irw_004_role_weighted_buy_score_normalized_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1Q divided by total insider buy value (normalized intensity)."""
    num = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_005_ceo_cfo_combined_buy_value_1m(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling 1-month sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_MONTH)


def irw_006_ceo_cfo_combined_buy_value_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling 1-quarter sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)


def irw_007_ceo_cfo_combined_buy_value_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling 1-year sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)


def irw_008_ceo_buy_value_1q(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_QTR)


def irw_009_cfo_buy_value_1q(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_QTR)


def irw_010_officer_buy_value_1q(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of all-officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_QTR)


def irw_011_director_buy_value_1q(director_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of director buy value."""
    return _rolling_sum(director_buy_value, _TD_QTR)


def irw_012_tenpct_buy_value_1q(tenpct_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of 10%-owner buy value."""
    return _rolling_sum(tenpct_buy_value, _TD_QTR)


def irw_013_role_weighted_buy_score_2y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 2 years: CEO/CFO=4, officer=3, director=2, 10%-owner=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_2Y)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_2Y)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_2Y)
        + 2.0 * _rolling_sum(director_buy_value, _TD_2Y)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_2Y)
    )


def irw_014_role_weighted_count_score_1q(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Role-weighted buy count score over 1Q: officer=3, director=2, 10%-owner=1."""
    return (
        3.0 * _rolling_sum(officer_buy_count, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_count, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_count, _TD_QTR)
    )


def irw_015_role_weighted_count_score_1y(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Role-weighted buy count score over 1 year: officer=3, director=2, 10%-owner=1."""
    return (
        3.0 * _rolling_sum(officer_buy_count, _TD_YEAR)
        + 2.0 * _rolling_sum(director_buy_count, _TD_YEAR)
        + 1.0 * _rolling_sum(tenpct_buy_count, _TD_YEAR)
    )


# --- Group B (016-030): Top-officer (CEO+CFO) share of total buying ---

def irw_016_top_officer_value_share_1m(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-month insider buy value attributable to CEO + CFO."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_MONTH)
    den = _rolling_sum(insider_buy_value, _TD_MONTH)
    return _safe_div(num, den)


def irw_017_top_officer_value_share_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value attributable to CEO + CFO."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_018_top_officer_value_share_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value attributable to CEO + CFO."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_019_officer_value_share_1q(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value from all officers."""
    num = _rolling_sum(officer_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_020_officer_value_share_1y(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from all officers."""
    num = _rolling_sum(officer_buy_value, _TD_YEAR)
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_021_director_value_share_1q(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value from directors."""
    num = _rolling_sum(director_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_022_director_value_share_1y(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from directors."""
    num = _rolling_sum(director_buy_value, _TD_YEAR)
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_023_tenpct_value_share_1q(
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value from 10%-owners."""
    num = _rolling_sum(tenpct_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_024_tenpct_value_share_1y(
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from 10%-owners."""
    num = _rolling_sum(tenpct_buy_value, _TD_YEAR)
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_025_ceo_value_share_1q(
    ceo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value from CEO alone."""
    num = _rolling_sum(ceo_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_026_cfo_value_share_1q(
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-quarter insider buy value from CFO alone."""
    num = _rolling_sum(cfo_buy_value, _TD_QTR)
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_027_top_officer_count_share_1q(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Share of 1Q insider buy count from officers (vs directors + 10%-owners)."""
    num = _rolling_sum(officer_buy_count, _TD_QTR)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_QTR)
    return _safe_div(num, den)


def irw_028_top_officer_count_share_1y(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy count from officers."""
    num = _rolling_sum(officer_buy_count, _TD_YEAR)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_YEAR)
    return _safe_div(num, den)


def irw_029_director_count_share_1q(
    director_buy_count: pd.Series,
    officer_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Share of 1Q insider buy count from directors."""
    num = _rolling_sum(director_buy_count, _TD_QTR)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_QTR)
    return _safe_div(num, den)


def irw_030_tenpct_count_share_1q(
    tenpct_buy_count: pd.Series,
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
) -> pd.Series:
    """Share of 1Q insider buy count from 10%-owners."""
    num = _rolling_sum(tenpct_buy_count, _TD_QTR)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_QTR)
    return _safe_div(num, den)


# --- Group C (031-045): Officer-vs-director buy ratio ---

def irw_031_officer_to_director_value_ratio_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy value to director buy value over 1 quarter."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(director_buy_value, _TD_QTR))


def irw_032_officer_to_director_value_ratio_1y(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy value to director buy value over 1 year."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_YEAR),
                     _rolling_sum(director_buy_value, _TD_YEAR))


def irw_033_officer_to_director_count_ratio_1q(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
) -> pd.Series:
    """Ratio of officer buy count to director buy count over 1 quarter."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_QTR),
                     _rolling_sum(director_buy_count, _TD_QTR))


def irw_034_officer_to_director_count_ratio_1y(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
) -> pd.Series:
    """Ratio of officer buy count to director buy count over 1 year."""
    return _safe_div(_rolling_sum(officer_buy_count, _TD_YEAR),
                     _rolling_sum(director_buy_count, _TD_YEAR))


def irw_035_top_officer_to_director_value_ratio_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of CEO+CFO buy value to director buy value over 1 quarter."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    den = _rolling_sum(director_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_036_top_officer_to_director_value_ratio_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of CEO+CFO buy value to director buy value over 1 year."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)
    den = _rolling_sum(director_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_037_officer_minus_director_value_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Officer buy value minus director buy value over 1 quarter (signed difference)."""
    return _rolling_sum(officer_buy_value - director_buy_value, _TD_QTR)


def irw_038_officer_minus_director_value_1y(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Officer buy value minus director buy value over 1 year (signed difference)."""
    return _rolling_sum(officer_buy_value - director_buy_value, _TD_YEAR)


def irw_039_officer_minus_director_count_1q(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
) -> pd.Series:
    """Officer buy count minus director buy count over 1 quarter."""
    return _rolling_sum(officer_buy_count - director_buy_count, _TD_QTR)


def irw_040_officer_led_flag_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if officer buy value exceeds director buy value over 1 quarter."""
    return (_rolling_sum(officer_buy_value, _TD_QTR) >
            _rolling_sum(director_buy_value, _TD_QTR)).astype(float)


def irw_041_officer_led_flag_1y(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if officer buy value exceeds director buy value over 1 year."""
    return (_rolling_sum(officer_buy_value, _TD_YEAR) >
            _rolling_sum(director_buy_value, _TD_YEAR)).astype(float)


def irw_042_director_only_flag_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if only directors bought (officer buy value = 0, director > 0) over 1Q."""
    off_sum = _rolling_sum(officer_buy_value, _TD_QTR)
    dir_sum = _rolling_sum(director_buy_value, _TD_QTR)
    return ((off_sum == 0) & (dir_sum > 0)).astype(float)


def irw_043_officer_only_flag_1q(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if only officers bought (director buy value = 0, officer > 0) over 1Q."""
    off_sum = _rolling_sum(officer_buy_value, _TD_QTR)
    dir_sum = _rolling_sum(director_buy_value, _TD_QTR)
    return ((off_sum > 0) & (dir_sum == 0)).astype(float)


def irw_044_officer_to_tenpct_value_ratio_1q(
    officer_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy value to 10%-owner buy value over 1 quarter."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(tenpct_buy_value, _TD_QTR))


def irw_045_director_to_tenpct_value_ratio_1q(
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of director buy value to 10%-owner buy value over 1 quarter."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_QTR),
                     _rolling_sum(tenpct_buy_value, _TD_QTR))


# --- Group D (046-060): CEO/CFO binary presence and intensity ---

def irw_046_ceo_buy_any_1m(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if any CEO buy occurred in trailing 1 month."""
    return (_rolling_sum(ceo_buy_value, _TD_MONTH) > 0).astype(float)


def irw_047_ceo_buy_any_1q(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if any CEO buy occurred in trailing 1 quarter."""
    return (_rolling_sum(ceo_buy_value, _TD_QTR) > 0).astype(float)


def irw_048_cfo_buy_any_1q(cfo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if any CFO buy occurred in trailing 1 quarter."""
    return (_rolling_sum(cfo_buy_value, _TD_QTR) > 0).astype(float)


def irw_049_ceo_or_cfo_buy_any_1m(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if CEO or CFO bought anything in trailing 1 month."""
    combined = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_MONTH)
    return (combined > 0).astype(float)


def irw_050_ceo_or_cfo_buy_any_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if CEO or CFO bought anything in trailing 1 quarter."""
    combined = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    return (combined > 0).astype(float)


def irw_051_ceo_and_cfo_both_buy_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if BOTH CEO and CFO bought in trailing 1 quarter."""
    ceo_sum = _rolling_sum(ceo_buy_value, _TD_QTR)
    cfo_sum = _rolling_sum(cfo_buy_value, _TD_QTR)
    return ((ceo_sum > 0) & (cfo_sum > 0)).astype(float)


def irw_052_ceo_buy_intensity_1q(
    ceo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """CEO buy value / total insider buy value over 1Q (CEO intensity ratio)."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_QTR),
                     _rolling_sum(insider_buy_value, _TD_QTR))


def irw_053_cfo_buy_intensity_1q(
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """CFO buy value / total insider buy value over 1Q (CFO intensity ratio)."""
    return _safe_div(_rolling_sum(cfo_buy_value, _TD_QTR),
                     _rolling_sum(insider_buy_value, _TD_QTR))


def irw_054_ceo_buy_any_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if any CEO buy occurred in trailing 1 year."""
    return (_rolling_sum(ceo_buy_value, _TD_YEAR) > 0).astype(float)


def irw_055_ceo_cfo_buy_value_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling 1-year sum of CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)


def irw_056_ceo_cfo_zscore_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of combined CEO+CFO buy value within trailing 1-year window."""
    combined = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(combined, _TD_YEAR)


def irw_057_ceo_buy_active_days_1q(ceo_buy_value: pd.Series) -> pd.Series:
    """Count of days with any CEO buy filing in trailing 1 quarter."""
    indicator = (ceo_buy_value > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR)


def irw_058_cfo_buy_active_days_1q(cfo_buy_value: pd.Series) -> pd.Series:
    """Count of days with any CFO buy filing in trailing 1 quarter."""
    indicator = (cfo_buy_value > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR)


def irw_059_top_officer_buy_active_days_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Count of days with any CEO or CFO buy filing in trailing 1 year."""
    indicator = ((ceo_buy_value + cfo_buy_value) > 0).astype(float)
    return _rolling_sum(indicator, _TD_YEAR)


def irw_060_ceo_cfo_buy_value_2y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling 2-year sum of combined CEO + CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_2Y)


# --- Group E (061-075): Seniority-weighted conviction index and role-mix rotation ---

def irw_061_seniority_conviction_index_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Seniority-weighted conviction index over 1Q.
    = sum(weight_i * value_i) / total_value, weights: CEO=1.0, CFO=0.9, officer=0.6, director=0.4, 10%=0.2.
    Captures the average seniority of dollars spent.
    """
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_QTR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_062_seniority_conviction_index_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Seniority-weighted conviction index over 1 year.
    Weights: CEO=1.0, CFO=0.9, officer=0.6, director=0.4, 10%-owner=0.2.
    """
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_YEAR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_YEAR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_YEAR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_YEAR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_YEAR)
    )
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_063_seniority_conviction_index_2y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority-weighted conviction index over 2 years."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_2Y)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_2Y)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_2Y)
        + 0.4 * _rolling_sum(director_buy_value, _TD_2Y)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_2Y)
    )
    den = _rolling_sum(insider_buy_value, _TD_2Y)
    return _safe_div(num, den)


def irw_064_top_officer_concentration_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
) -> pd.Series:
    """CEO+CFO buy value as share of all-officer buy value over 1Q (concentration within officer class)."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR)
    den = _rolling_sum(officer_buy_value, _TD_QTR)
    return _safe_div(num, den)


def irw_065_top_officer_concentration_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
) -> pd.Series:
    """CEO+CFO buy value as share of all-officer buy value over 1 year."""
    num = _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR)
    den = _rolling_sum(officer_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_066_role_mix_seniority_shift_1q_vs_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Rotation of role mix toward seniority: 1Q seniority conviction minus 1Y seniority conviction.
    Positive means recent buying is more senior than the trailing-year baseline.
    """
    def _sci(window: int) -> pd.Series:
        num = (
            1.0 * _rolling_sum(ceo_buy_value, window)
            + 0.9 * _rolling_sum(cfo_buy_value, window)
            + 0.6 * _rolling_sum(officer_buy_value, window)
            + 0.4 * _rolling_sum(director_buy_value, window)
            + 0.2 * _rolling_sum(tenpct_buy_value, window)
        )
        den = _rolling_sum(insider_buy_value, window)
        return _safe_div(num, den)
    return _sci(_TD_QTR) - _sci(_TD_YEAR)


def irw_067_role_mix_seniority_shift_1m_vs_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    1M seniority conviction minus 1Q seniority conviction.
    Detects very recent shift toward senior buyers.
    """
    def _sci(window: int) -> pd.Series:
        num = (
            1.0 * _rolling_sum(ceo_buy_value, window)
            + 0.9 * _rolling_sum(cfo_buy_value, window)
            + 0.6 * _rolling_sum(officer_buy_value, window)
            + 0.4 * _rolling_sum(director_buy_value, window)
            + 0.2 * _rolling_sum(tenpct_buy_value, window)
        )
        den = _rolling_sum(insider_buy_value, window)
        return _safe_div(num, den)
    return _sci(_TD_MONTH) - _sci(_TD_QTR)


def irw_068_officer_share_ewm(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=63) of the daily officer buy value share (officer / total)."""
    daily_share = _safe_div(officer_buy_value, insider_buy_value)
    return _ewm_mean(daily_share.fillna(0.0), _TD_QTR)


def irw_069_top_officer_share_ewm(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=63) of the daily CEO+CFO buy value share."""
    daily_share = _safe_div(ceo_buy_value + cfo_buy_value, insider_buy_value)
    return _ewm_mean(daily_share.fillna(0.0), _TD_QTR)


def irw_070_director_share_ewm(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=63) of the daily director buy value share."""
    daily_share = _safe_div(director_buy_value, insider_buy_value)
    return _ewm_mean(daily_share.fillna(0.0), _TD_QTR)


def irw_071_tenpct_share_ewm(
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=63) of the daily 10%-owner buy value share."""
    daily_share = _safe_div(tenpct_buy_value, insider_buy_value)
    return _ewm_mean(daily_share.fillna(0.0), _TD_QTR)


def irw_072_role_weighted_buy_score_zscore_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of the role-weighted buy score within a trailing 1-year window."""
    score = (
        4.0 * ceo_buy_value
        + 4.0 * cfo_buy_value
        + 3.0 * officer_buy_value
        + 2.0 * director_buy_value
        + 1.0 * tenpct_buy_value
    )
    return _zscore_rolling(score, _TD_YEAR)


def irw_073_seniority_conviction_pct_rank_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Percentile rank of the 1Q seniority conviction index within a trailing 1-year window."""
    num = (
        1.0 * ceo_buy_value
        + 0.9 * cfo_buy_value
        + 0.6 * officer_buy_value
        + 0.4 * director_buy_value
        + 0.2 * tenpct_buy_value
    )
    daily_sci = _safe_div(num, insider_buy_value).fillna(0.0)
    return daily_sci.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def irw_074_officer_sell_vs_buy_role_skew_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """
    Officer net-buy share minus director net-buy share (role-level net skew).
    = (officer_buy - officer_sell) / (officer_buy + officer_sell + eps)
    - (director_buy - director_sell) / (director_buy + director_sell + eps).
    """
    off_buy  = _rolling_sum(officer_buy_value, _TD_QTR)
    off_sell = _rolling_sum(officer_sell_value, _TD_QTR)
    dir_buy  = _rolling_sum(director_buy_value, _TD_QTR)
    dir_sell = _rolling_sum(director_sell_value, _TD_QTR)
    off_skew = _safe_div(off_buy - off_sell, (off_buy + off_sell).replace(0, np.nan))
    dir_skew = _safe_div(dir_buy - dir_sell, (dir_buy + dir_sell).replace(0, np.nan))
    return off_skew.fillna(0.0) - dir_skew.fillna(0.0)


def irw_075_composite_senior_buy_signal_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Composite senior-buyer signal over 1Q combining:
    (a) top-officer value share, (b) officer-to-director value ratio (normalized),
    (c) CEO/CFO binary presence. All normalized and equally weighted.
    """
    top_share = _safe_div(
        _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
        _rolling_sum(insider_buy_value, _TD_QTR)
    ).fillna(0.0)
    off_sum = _rolling_sum(officer_buy_value, _TD_QTR)
    dir_sum = _rolling_sum(director_buy_value, _TD_QTR)
    total   = (off_sum + dir_sum).replace(0, np.nan)
    off_dir_share = _safe_div(off_sum, total).fillna(0.0)
    ceo_cfo_binary = (
        _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR) > 0
    ).astype(float)
    return (top_share + off_dir_share + ceo_cfo_binary) / 3.0


# --- Group F-ext (151-175): Additional seniority constructs, half-window, cross-role ---

def irw_151_ceo_buy_value_half(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling half-year (126d) sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_HALF)


def irw_152_cfo_buy_value_half(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_HALF)


def irw_153_officer_buy_value_half(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_HALF)


def irw_154_director_buy_value_half(director_buy_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of director buy value."""
    return _rolling_sum(director_buy_value, _TD_HALF)


def irw_155_tenpct_buy_value_half(tenpct_buy_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of 10%-owner buy value."""
    return _rolling_sum(tenpct_buy_value, _TD_HALF)


def irw_156_ceo_cfo_buy_value_half(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Rolling half-year sum of combined CEO+CFO buy value."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _TD_HALF)


def irw_157_top_officer_value_share_half(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of half-year insider buy value from CEO+CFO."""
    return _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_HALF),
                     _rolling_sum(insider_buy_value, _TD_HALF))


def irw_158_officer_value_share_half(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of half-year insider buy value from all officers."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_HALF),
                     _rolling_sum(insider_buy_value, _TD_HALF))


def irw_159_director_value_share_half(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of half-year insider buy value from directors."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_HALF),
                     _rolling_sum(insider_buy_value, _TD_HALF))


def irw_160_seniority_conviction_index_half(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Seniority conviction index over half-year window."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_HALF)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_HALF)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_HALF)
        + 0.4 * _rolling_sum(director_buy_value, _TD_HALF)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_HALF)
    )
    return _safe_div(num, _rolling_sum(insider_buy_value, _TD_HALF))


def irw_161_ceo_buy_value_week(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-week (5d) sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_WEEK)


def irw_162_cfo_buy_value_week(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-week sum of CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_WEEK)


def irw_163_officer_net_buy_value_half(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy value (buy - sell) over half year."""
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_HALF)


def irw_164_director_net_buy_value_half(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy value (buy - sell) over half year."""
    return _rolling_sum(director_buy_value - director_sell_value, _TD_HALF)


def irw_165_officer_buy_to_sell_ratio_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer buy/sell value ratio over 1 year."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_YEAR),
                     _rolling_sum(officer_sell_value, _TD_YEAR))


def irw_166_director_buy_to_sell_ratio_1y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director buy/sell value ratio over 1 year."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_YEAR),
                     _rolling_sum(director_sell_value, _TD_YEAR))


def irw_167_officer_net_buy_fraction_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy as fraction of total officer flow over 1 year."""
    buy  = _rolling_sum(officer_buy_value, _TD_YEAR)
    sell = _rolling_sum(officer_sell_value, _TD_YEAR)
    return _safe_div(buy - sell, (buy + sell).replace(0, np.nan))


def irw_168_director_net_buy_fraction_1y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy as fraction of total director flow over 1 year."""
    buy  = _rolling_sum(director_buy_value, _TD_YEAR)
    sell = _rolling_sum(director_sell_value, _TD_YEAR)
    return _safe_div(buy - sell, (buy + sell).replace(0, np.nan))


def irw_169_ceo_buy_value_1m(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-month (21d) sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_MONTH)


def irw_170_cfo_buy_value_1m(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-month sum of CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_MONTH)


def irw_171_officer_buy_value_1m(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-month sum of officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_MONTH)


def irw_172_director_buy_value_1m(director_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-month sum of director buy value."""
    return _rolling_sum(director_buy_value, _TD_MONTH)


def irw_173_tenpct_buy_value_1m(tenpct_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-month sum of 10%-owner buy value."""
    return _rolling_sum(tenpct_buy_value, _TD_MONTH)


def irw_174_role_weighted_buy_score_zscore_2y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of the daily role-weighted buy score within a trailing 2-year window."""
    score = (
        4.0 * ceo_buy_value + 4.0 * cfo_buy_value + 3.0 * officer_buy_value
        + 2.0 * director_buy_value + 1.0 * tenpct_buy_value
    )
    return _zscore_rolling(score, _TD_2Y)


def irw_175_officer_count_share_half(
    officer_buy_count: pd.Series,
    director_buy_count: pd.Series,
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Officer share of total insider buy count over half year."""
    num = _rolling_sum(officer_buy_count, _TD_HALF)
    den = _rolling_sum(officer_buy_count + director_buy_count + tenpct_buy_count, _TD_HALF)
    return _safe_div(num, den)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_ROLE_WEIGHT_REGISTRY_001_075 = {
    "irw_001_role_weighted_buy_score_1m": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_001_role_weighted_buy_score_1m,
    },
    "irw_002_role_weighted_buy_score_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_002_role_weighted_buy_score_1q,
    },
    "irw_003_role_weighted_buy_score_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_003_role_weighted_buy_score_1y,
    },
    "irw_004_role_weighted_buy_score_normalized_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_004_role_weighted_buy_score_normalized_1q,
    },
    "irw_005_ceo_cfo_combined_buy_value_1m": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_005_ceo_cfo_combined_buy_value_1m,
    },
    "irw_006_ceo_cfo_combined_buy_value_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_006_ceo_cfo_combined_buy_value_1q,
    },
    "irw_007_ceo_cfo_combined_buy_value_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_007_ceo_cfo_combined_buy_value_1y,
    },
    "irw_008_ceo_buy_value_1q": {
        "inputs": ["ceo_buy_value"],
        "func": irw_008_ceo_buy_value_1q,
    },
    "irw_009_cfo_buy_value_1q": {
        "inputs": ["cfo_buy_value"],
        "func": irw_009_cfo_buy_value_1q,
    },
    "irw_010_officer_buy_value_1q": {
        "inputs": ["officer_buy_value"],
        "func": irw_010_officer_buy_value_1q,
    },
    "irw_011_director_buy_value_1q": {
        "inputs": ["director_buy_value"],
        "func": irw_011_director_buy_value_1q,
    },
    "irw_012_tenpct_buy_value_1q": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_012_tenpct_buy_value_1q,
    },
    "irw_013_role_weighted_buy_score_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_013_role_weighted_buy_score_2y,
    },
    "irw_014_role_weighted_count_score_1q": {
        "inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],
        "func": irw_014_role_weighted_count_score_1q,
    },
    "irw_015_role_weighted_count_score_1y": {
        "inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],
        "func": irw_015_role_weighted_count_score_1y,
    },
    "irw_016_top_officer_value_share_1m": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_016_top_officer_value_share_1m,
    },
    "irw_017_top_officer_value_share_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_017_top_officer_value_share_1q,
    },
    "irw_018_top_officer_value_share_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_018_top_officer_value_share_1y,
    },
    "irw_019_officer_value_share_1q": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_019_officer_value_share_1q,
    },
    "irw_020_officer_value_share_1y": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_020_officer_value_share_1y,
    },
    "irw_021_director_value_share_1q": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_021_director_value_share_1q,
    },
    "irw_022_director_value_share_1y": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_022_director_value_share_1y,
    },
    "irw_023_tenpct_value_share_1q": {
        "inputs": ["tenpct_buy_value", "insider_buy_value"],
        "func": irw_023_tenpct_value_share_1q,
    },
    "irw_024_tenpct_value_share_1y": {
        "inputs": ["tenpct_buy_value", "insider_buy_value"],
        "func": irw_024_tenpct_value_share_1y,
    },
    "irw_025_ceo_value_share_1q": {
        "inputs": ["ceo_buy_value", "insider_buy_value"],
        "func": irw_025_ceo_value_share_1q,
    },
    "irw_026_cfo_value_share_1q": {
        "inputs": ["cfo_buy_value", "insider_buy_value"],
        "func": irw_026_cfo_value_share_1q,
    },
    "irw_027_top_officer_count_share_1q": {
        "inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],
        "func": irw_027_top_officer_count_share_1q,
    },
    "irw_028_top_officer_count_share_1y": {
        "inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],
        "func": irw_028_top_officer_count_share_1y,
    },
    "irw_029_director_count_share_1q": {
        "inputs": ["director_buy_count", "officer_buy_count", "tenpct_buy_count"],
        "func": irw_029_director_count_share_1q,
    },
    "irw_030_tenpct_count_share_1q": {
        "inputs": ["tenpct_buy_count", "officer_buy_count", "director_buy_count"],
        "func": irw_030_tenpct_count_share_1q,
    },
    "irw_031_officer_to_director_value_ratio_1q": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_031_officer_to_director_value_ratio_1q,
    },
    "irw_032_officer_to_director_value_ratio_1y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_032_officer_to_director_value_ratio_1y,
    },
    "irw_033_officer_to_director_count_ratio_1q": {
        "inputs": ["officer_buy_count", "director_buy_count"],
        "func": irw_033_officer_to_director_count_ratio_1q,
    },
    "irw_034_officer_to_director_count_ratio_1y": {
        "inputs": ["officer_buy_count", "director_buy_count"],
        "func": irw_034_officer_to_director_count_ratio_1y,
    },
    "irw_035_top_officer_to_director_value_ratio_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "director_buy_value"],
        "func": irw_035_top_officer_to_director_value_ratio_1q,
    },
    "irw_036_top_officer_to_director_value_ratio_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "director_buy_value"],
        "func": irw_036_top_officer_to_director_value_ratio_1y,
    },
    "irw_037_officer_minus_director_value_1q": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_037_officer_minus_director_value_1q,
    },
    "irw_038_officer_minus_director_value_1y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_038_officer_minus_director_value_1y,
    },
    "irw_039_officer_minus_director_count_1q": {
        "inputs": ["officer_buy_count", "director_buy_count"],
        "func": irw_039_officer_minus_director_count_1q,
    },
    "irw_040_officer_led_flag_1q": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_040_officer_led_flag_1q,
    },
    "irw_041_officer_led_flag_1y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_041_officer_led_flag_1y,
    },
    "irw_042_director_only_flag_1q": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_042_director_only_flag_1q,
    },
    "irw_043_officer_only_flag_1q": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_043_officer_only_flag_1q,
    },
    "irw_044_officer_to_tenpct_value_ratio_1q": {
        "inputs": ["officer_buy_value", "tenpct_buy_value"],
        "func": irw_044_officer_to_tenpct_value_ratio_1q,
    },
    "irw_045_director_to_tenpct_value_ratio_1q": {
        "inputs": ["director_buy_value", "tenpct_buy_value"],
        "func": irw_045_director_to_tenpct_value_ratio_1q,
    },
    "irw_046_ceo_buy_any_1m": {
        "inputs": ["ceo_buy_value"],
        "func": irw_046_ceo_buy_any_1m,
    },
    "irw_047_ceo_buy_any_1q": {
        "inputs": ["ceo_buy_value"],
        "func": irw_047_ceo_buy_any_1q,
    },
    "irw_048_cfo_buy_any_1q": {
        "inputs": ["cfo_buy_value"],
        "func": irw_048_cfo_buy_any_1q,
    },
    "irw_049_ceo_or_cfo_buy_any_1m": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_049_ceo_or_cfo_buy_any_1m,
    },
    "irw_050_ceo_or_cfo_buy_any_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_050_ceo_or_cfo_buy_any_1q,
    },
    "irw_051_ceo_and_cfo_both_buy_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_051_ceo_and_cfo_both_buy_1q,
    },
    "irw_052_ceo_buy_intensity_1q": {
        "inputs": ["ceo_buy_value", "insider_buy_value"],
        "func": irw_052_ceo_buy_intensity_1q,
    },
    "irw_053_cfo_buy_intensity_1q": {
        "inputs": ["cfo_buy_value", "insider_buy_value"],
        "func": irw_053_cfo_buy_intensity_1q,
    },
    "irw_054_ceo_buy_any_1y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_054_ceo_buy_any_1y,
    },
    "irw_055_ceo_cfo_buy_value_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_055_ceo_cfo_buy_value_1y,
    },
    "irw_056_ceo_cfo_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_056_ceo_cfo_zscore_1y,
    },
    "irw_057_ceo_buy_active_days_1q": {
        "inputs": ["ceo_buy_value"],
        "func": irw_057_ceo_buy_active_days_1q,
    },
    "irw_058_cfo_buy_active_days_1q": {
        "inputs": ["cfo_buy_value"],
        "func": irw_058_cfo_buy_active_days_1q,
    },
    "irw_059_top_officer_buy_active_days_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_059_top_officer_buy_active_days_1y,
    },
    "irw_060_ceo_cfo_buy_value_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_060_ceo_cfo_buy_value_2y,
    },
    "irw_061_seniority_conviction_index_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_061_seniority_conviction_index_1q,
    },
    "irw_062_seniority_conviction_index_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_062_seniority_conviction_index_1y,
    },
    "irw_063_seniority_conviction_index_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_063_seniority_conviction_index_2y,
    },
    "irw_064_top_officer_concentration_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"],
        "func": irw_064_top_officer_concentration_1q,
    },
    "irw_065_top_officer_concentration_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value"],
        "func": irw_065_top_officer_concentration_1y,
    },
    "irw_066_role_mix_seniority_shift_1q_vs_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_066_role_mix_seniority_shift_1q_vs_1y,
    },
    "irw_067_role_mix_seniority_shift_1m_vs_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_067_role_mix_seniority_shift_1m_vs_1q,
    },
    "irw_068_officer_share_ewm": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_068_officer_share_ewm,
    },
    "irw_069_top_officer_share_ewm": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_069_top_officer_share_ewm,
    },
    "irw_070_director_share_ewm": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_070_director_share_ewm,
    },
    "irw_071_tenpct_share_ewm": {
        "inputs": ["tenpct_buy_value", "insider_buy_value"],
        "func": irw_071_tenpct_share_ewm,
    },
    "irw_072_role_weighted_buy_score_zscore_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_072_role_weighted_buy_score_zscore_1y,
    },
    "irw_073_seniority_conviction_pct_rank_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_073_seniority_conviction_pct_rank_1y,
    },
    "irw_074_officer_sell_vs_buy_role_skew_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"],
        "func": irw_074_officer_sell_vs_buy_role_skew_1q,
    },
    "irw_075_composite_senior_buy_signal_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_075_composite_senior_buy_signal_1q,
    },
    "irw_151_ceo_buy_value_half": {
        "inputs": ["ceo_buy_value"],
        "func": irw_151_ceo_buy_value_half,
    },
    "irw_152_cfo_buy_value_half": {
        "inputs": ["cfo_buy_value"],
        "func": irw_152_cfo_buy_value_half,
    },
    "irw_153_officer_buy_value_half": {
        "inputs": ["officer_buy_value"],
        "func": irw_153_officer_buy_value_half,
    },
    "irw_154_director_buy_value_half": {
        "inputs": ["director_buy_value"],
        "func": irw_154_director_buy_value_half,
    },
    "irw_155_tenpct_buy_value_half": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_155_tenpct_buy_value_half,
    },
    "irw_156_ceo_cfo_buy_value_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_156_ceo_cfo_buy_value_half,
    },
    "irw_157_top_officer_value_share_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_157_top_officer_value_share_half,
    },
    "irw_158_officer_value_share_half": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_158_officer_value_share_half,
    },
    "irw_159_director_value_share_half": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_159_director_value_share_half,
    },
    "irw_160_seniority_conviction_index_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_160_seniority_conviction_index_half,
    },
    "irw_161_ceo_buy_value_week": {
        "inputs": ["ceo_buy_value"],
        "func": irw_161_ceo_buy_value_week,
    },
    "irw_162_cfo_buy_value_week": {
        "inputs": ["cfo_buy_value"],
        "func": irw_162_cfo_buy_value_week,
    },
    "irw_163_officer_net_buy_value_half": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_163_officer_net_buy_value_half,
    },
    "irw_164_director_net_buy_value_half": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_164_director_net_buy_value_half,
    },
    "irw_165_officer_buy_to_sell_ratio_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_165_officer_buy_to_sell_ratio_1y,
    },
    "irw_166_director_buy_to_sell_ratio_1y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_166_director_buy_to_sell_ratio_1y,
    },
    "irw_167_officer_net_buy_fraction_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_167_officer_net_buy_fraction_1y,
    },
    "irw_168_director_net_buy_fraction_1y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_168_director_net_buy_fraction_1y,
    },
    "irw_169_ceo_buy_value_1m": {
        "inputs": ["ceo_buy_value"],
        "func": irw_169_ceo_buy_value_1m,
    },
    "irw_170_cfo_buy_value_1m": {
        "inputs": ["cfo_buy_value"],
        "func": irw_170_cfo_buy_value_1m,
    },
    "irw_171_officer_buy_value_1m": {
        "inputs": ["officer_buy_value"],
        "func": irw_171_officer_buy_value_1m,
    },
    "irw_172_director_buy_value_1m": {
        "inputs": ["director_buy_value"],
        "func": irw_172_director_buy_value_1m,
    },
    "irw_173_tenpct_buy_value_1m": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_173_tenpct_buy_value_1m,
    },
    "irw_174_role_weighted_buy_score_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_174_role_weighted_buy_score_zscore_2y,
    },
    "irw_175_officer_count_share_half": {
        "inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],
        "func": irw_175_officer_count_share_half,
    },
}
