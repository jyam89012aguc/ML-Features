"""
84_insider_buy_size — Extended Features 001-075
Domain: dollar magnitude of insider purchases — additional buy-size variants:
        new windows, tail/dispersion measures, active-day intensity, depth-below
        thresholds, percentile/z-score angles, streaks, drought timing, composites.
Asset class: US equities | Sharadar SF2 insider transactions (daily aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings to one row per (ticker, date).  These are EVENT-DRIVEN
series: most days are ZERO, positive values appear only on filing days.  Do NOT
forward-fill.  Aggregate over trailing windows using rolling SUMS so sparse
filing days accumulate correctly.  Functions look strictly backward using
.shift(positive), .rolling(), or .expanding().
Trading-day cadence: 1 week = 5, 1 month = 21, 1 quarter = 63, 1 year = 252.

Canonical input fields (lowercase):
    insider_buy_value, insider_buy_shares, insider_buy_count,
    officer_buy_value, ceo_buy_value, cfo_buy_value, tenpct_buy_value,
    director_buy_value, insider_sell_value, insider_shares_held
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_W5   = 5     # 1 week
_W10  = 10    # 2 weeks
_W21  = 21    # 1 month
_W42  = 42    # 2 months
_W63  = 63    # 1 quarter
_W126 = 126   # 2 quarters
_W189 = 189   # 3 quarters
_W252 = 252   # 1 year
_W378 = 378   # 1.5 years
_W504 = 504   # 2 years
_EPS  = 1e-9

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
    """Count of filing days (value > 0) within trailing window — sparse-event helper."""
    return _rolling_sum((s > 0).astype(float), w)


def _consec_zero(s: pd.Series) -> pd.Series:
    """Consecutive days with zero activity up to each row (event-drought streak)."""
    is_zero = (s <= 0)
    grp = (~is_zero).cumsum()
    return is_zero.astype(int).groupby(grp).cumsum().astype(float)


def _days_since_positive(s: pd.Series) -> pd.Series:
    """Days elapsed since the series was last strictly positive (0 = today positive)."""
    pos = (s > 0).astype(float)
    idx = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    last = idx.where(pos == 1.0).ffill()
    return (idx - last)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional rolling-window buy-value sums ---

def ibs_ext_001_buy_value_10d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 10-day window."""
    return _rolling_sum(insider_buy_value, _W10)


def ibs_ext_002_buy_value_42d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 42-day (2-month) window."""
    return _rolling_sum(insider_buy_value, _W42)


def ibs_ext_003_buy_value_189d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 189-day (3-quarter) window."""
    return _rolling_sum(insider_buy_value, _W189)


def ibs_ext_004_buy_value_378d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 378-day (1.5-year) window."""
    return _rolling_sum(insider_buy_value, _W378)


def ibs_ext_005_buy_shares_10d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 10-day window."""
    return _rolling_sum(insider_buy_shares, _W10)


def ibs_ext_006_buy_shares_42d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 42-day window."""
    return _rolling_sum(insider_buy_shares, _W42)


def ibs_ext_007_buy_count_42d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transaction count over trailing 42-day window."""
    return _rolling_sum(insider_buy_count, _W42)


def ibs_ext_008_buy_count_189d(insider_buy_count: pd.Series) -> pd.Series:
    """Total insider buy transaction count over trailing 189-day window."""
    return _rolling_sum(insider_buy_count, _W189)


def ibs_ext_009_officer_buy_value_42d(officer_buy_value: pd.Series) -> pd.Series:
    """Total officer buy dollar value over trailing 42-day window."""
    return _rolling_sum(officer_buy_value, _W42)


def ibs_ext_010_ceo_buy_value_126d(ceo_buy_value: pd.Series) -> pd.Series:
    """Total CEO buy dollar value over trailing 126-day window."""
    return _rolling_sum(ceo_buy_value, _W126)


def ibs_ext_011_cfo_buy_value_504d(cfo_buy_value: pd.Series) -> pd.Series:
    """Total CFO buy dollar value over trailing 504-day window."""
    return _rolling_sum(cfo_buy_value, _W504)


def ibs_ext_012_director_buy_value_126d(director_buy_value: pd.Series) -> pd.Series:
    """Total director buy dollar value over trailing 126-day window."""
    return _rolling_sum(director_buy_value, _W126)


# --- Group B (013-024): Mean/median per-day buy magnitude and dispersion ---

def ibs_ext_013_mean_daily_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Mean daily insider buy value over trailing 63-day window."""
    return _rolling_mean(insider_buy_value, _W63)


def ibs_ext_014_mean_daily_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Mean daily insider buy value over trailing 252-day window."""
    return _rolling_mean(insider_buy_value, _W252)


def ibs_ext_015_median_buy_value_on_active_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Median single-day buy value over 252 days, computed on filing days only."""
    active = insider_buy_value.where(insider_buy_value > 0)
    return _rolling_median(active, _W252)


def ibs_ext_016_buy_value_std_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Standard deviation of daily buy value over trailing 252-day window."""
    return _rolling_std(insider_buy_value, _W252)


def ibs_ext_017_buy_value_dispersion_ratio_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy value over 252 days (std / mean)."""
    return _safe_div(_rolling_std(insider_buy_value, _W252),
                     _rolling_mean(insider_buy_value, _W252))


def ibs_ext_018_buy_value_range_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Range (max minus min) of daily buy value over trailing 252-day window."""
    return _rolling_max(insider_buy_value, _W252) - _rolling_min(insider_buy_value, _W252)


def ibs_ext_019_peak_to_mean_buy_ratio_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of largest single-day buy to mean daily buy value over 252 days (lumpiness)."""
    return _safe_div(_rolling_max(insider_buy_value, _W252),
                     _rolling_mean(insider_buy_value, _W252))


def ibs_ext_020_buy_shares_std_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Standard deviation of daily buy shares over trailing 252-day window."""
    return _rolling_std(insider_buy_shares, _W252)


def ibs_ext_021_mean_officer_buy_value_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Mean daily officer buy value over trailing 252-day window."""
    return _rolling_mean(officer_buy_value, _W252)


def ibs_ext_022_largest_buy_share_of_63d_total(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day buy as fraction of trailing 63-day total buy value (concentration)."""
    return _safe_div(_rolling_max(insider_buy_value, _W63),
                     _rolling_sum(insider_buy_value, _W63))


def ibs_ext_023_largest_buy_share_of_252d_total(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day buy as fraction of trailing 252-day total buy value."""
    return _safe_div(_rolling_max(insider_buy_value, _W252),
                     _rolling_sum(insider_buy_value, _W252))


def ibs_ext_024_buy_value_iqr_proxy_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Median-to-max gap of daily buy value over 252 days (upper-tail dispersion proxy)."""
    return _rolling_max(insider_buy_value, _W252) - _rolling_median(insider_buy_value, _W252)


# --- Group C (025-036): Active-day intensity and event-frequency measures ---

def ibs_ext_025_buy_active_days_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Count of insider buy filing days within trailing 21-day window."""
    return _active_days(insider_buy_value, _W21)


def ibs_ext_026_buy_active_days_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Count of insider buy filing days within trailing 63-day window."""
    return _active_days(insider_buy_value, _W63)


def ibs_ext_027_buy_active_days_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Count of insider buy filing days within trailing 252-day window."""
    return _active_days(insider_buy_value, _W252)


def ibs_ext_028_officer_buy_active_days_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Count of officer buy filing days within trailing 252-day window."""
    return _active_days(officer_buy_value, _W252)


def ibs_ext_029_ceo_buy_active_days_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Count of CEO buy filing days within trailing 252-day window."""
    return _active_days(ceo_buy_value, _W252)


def ibs_ext_030_buy_active_fraction_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days that had an insider buy filing."""
    return _active_days(insider_buy_value, _W63) / float(_W63)


def ibs_ext_031_buy_active_fraction_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days that had an insider buy filing."""
    return _active_days(insider_buy_value, _W252) / float(_W252)


def ibs_ext_032_avg_value_per_active_day_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Average buy value per filing day over 252 days (total / active-day count)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W252),
                     _active_days(insider_buy_value, _W252))


def ibs_ext_033_avg_value_per_active_day_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Average buy value per filing day over 63 days (total / active-day count)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W63),
                     _active_days(insider_buy_value, _W63))


def ibs_ext_034_buy_active_days_21d_vs_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Recent buy-activity intensity: 21-day active-day rate vs 252-day rate."""
    short = _active_days(insider_buy_value, _W21) / float(_W21)
    base  = _active_days(insider_buy_value, _W252) / float(_W252)
    return _safe_div(short, base)


def ibs_ext_035_consec_zero_buy_days(insider_buy_value: pd.Series) -> pd.Series:
    """Consecutive days with zero insider buy activity (buy-drought streak)."""
    return _consec_zero(insider_buy_value)


def ibs_ext_036_days_since_last_buy(insider_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last insider buy filing day."""
    return _days_since_positive(insider_buy_value)


# --- Group D (037-046): Days-since / timing of notable buys ---

def ibs_ext_037_days_since_officer_buy(officer_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last officer buy filing day."""
    return _days_since_positive(officer_buy_value)


def ibs_ext_038_days_since_ceo_buy(ceo_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last CEO buy filing day."""
    return _days_since_positive(ceo_buy_value)


def ibs_ext_039_days_since_big_buy_100k(insider_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last single-day buy exceeding $100k."""
    return _days_since_positive((insider_buy_value > 100_000).astype(float))


def ibs_ext_040_days_since_big_buy_500k(insider_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since the last single-day buy exceeding $500k."""
    return _days_since_positive((insider_buy_value > 500_000).astype(float))


def ibs_ext_041_days_since_buy_252d_high(insider_buy_value: pd.Series) -> pd.Series:
    """Days elapsed since daily buy value last set a 252-day rolling maximum."""
    mx = _rolling_max(insider_buy_value, _W252)
    at_high = ((insider_buy_value > 0) & (insider_buy_value >= mx - _EPS)).astype(float)
    return _days_since_positive(at_high)


def ibs_ext_042_buy_value_5d_vs_63d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 5-day buy sum to 63-day buy sum (very near-term concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W5),
                     _rolling_sum(insider_buy_value, _W63))


def ibs_ext_043_buy_value_21d_vs_126d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 21-day buy sum to 126-day buy sum (monthly vs half-year concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W21),
                     _rolling_sum(insider_buy_value, _W126))


def ibs_ext_044_buy_value_63d_vs_504d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 63-day buy sum to 504-day buy sum (quarter vs two-year concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W63),
                     _rolling_sum(insider_buy_value, _W504))


def ibs_ext_045_buy_value_42d_vs_252d_avg(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 42-day buy sum divided by trailing 252-day mean daily buy value."""
    return _safe_div(_rolling_sum(insider_buy_value, _W42),
                     _rolling_mean(insider_buy_value, _W252))


def ibs_ext_046_buy_value_189d_vs_504d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 189-day buy sum to 504-day buy sum (3-quarter vs two-year concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W189),
                     _rolling_sum(insider_buy_value, _W504))


# --- Group E (047-056): Depth-below-baseline distress / drought measures ---

def ibs_ext_047_buy_value_63d_depth_below_median_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Shortfall of 63-day buy sum below its 252-day rolling median (0 when above)."""
    val = _rolling_sum(insider_buy_value, _W63)
    med = _rolling_median(val, _W252)
    return (med - val).clip(lower=0.0)


def ibs_ext_048_buy_value_21d_shortfall_vs_252d_avg(insider_buy_value: pd.Series) -> pd.Series:
    """Shortfall of 21-day buy sum below the 252d mean-scaled expected level (0 when above)."""
    val = _rolling_sum(insider_buy_value, _W21)
    base = _rolling_mean(insider_buy_value, _W252) * float(_W21)
    return (base - val).clip(lower=0.0)


def ibs_ext_049_buy_drought_flag_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: zero insider buy value over the trailing 63-day window."""
    return (_rolling_sum(insider_buy_value, _W63) <= _EPS).astype(float)


def ibs_ext_050_buy_drought_flag_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: zero insider buy value over the trailing 126-day window."""
    return (_rolling_sum(insider_buy_value, _W126) <= _EPS).astype(float)


def ibs_ext_051_officer_buy_drought_flag_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Binary flag: zero officer buy value over the trailing 252-day window."""
    return (_rolling_sum(officer_buy_value, _W252) <= _EPS).astype(float)


def ibs_ext_052_buy_value_below_25pct_flag_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 63-day buy sum in bottom quartile of its 252-day percentile distribution."""
    val = _rolling_sum(insider_buy_value, _W63)
    return (_rolling_rank_pct(val, _W252) < 0.25).astype(float)


def ibs_ext_053_buy_value_63d_pct_of_504d_peak(insider_buy_value: pd.Series) -> pd.Series:
    """63-day buy sum as fraction of its 504-day rolling peak (1.0 = at peak, low = drought)."""
    val = _rolling_sum(insider_buy_value, _W63)
    return _safe_div(val, _rolling_max(val, _W504))


def ibs_ext_054_buy_value_21d_drawdown_from_252d_peak(insider_buy_value: pd.Series) -> pd.Series:
    """Drawdown of 21-day buy sum from its 252-day rolling peak (peak minus current, clipped)."""
    val = _rolling_sum(insider_buy_value, _W21)
    return (_rolling_max(val, _W252) - val).clip(lower=0.0)


def ibs_ext_055_consec_quarters_buy_below_median(insider_buy_value: pd.Series) -> pd.Series:
    """Consecutive days the 63-day buy sum has stayed below its 252-day median."""
    val = _rolling_sum(insider_buy_value, _W63)
    below = (val < _rolling_median(val, _W252))
    grp = (~below).cumsum()
    return below.astype(int).groupby(grp).cumsum().astype(float)


def ibs_ext_056_buy_value_log_shortfall_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Log-gap of 252-day buy sum below its 504-day rolling peak (compressed drought depth)."""
    val = _rolling_sum(insider_buy_value, _W252)
    peak = _rolling_max(val, _W504)
    return np.log1p(peak.clip(lower=0.0)) - np.log1p(val.clip(lower=0.0))


# --- Group F (057-064): Percentile-rank and z-score angles on new windows ---

def ibs_ext_057_buy_value_21d_pct_rank_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of the 21-day buy sum within a trailing 252-day window."""
    return _rolling_rank_pct(_rolling_sum(insider_buy_value, _W21), _W252)


def ibs_ext_058_buy_value_63d_pct_rank_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day buy sum within a trailing 504-day window."""
    return _rolling_rank_pct(_rolling_sum(insider_buy_value, _W63), _W504)


def ibs_ext_059_buy_value_126d_pct_rank_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of the 126-day buy sum within a trailing 504-day window."""
    return _rolling_rank_pct(_rolling_sum(insider_buy_value, _W126), _W504)


def ibs_ext_060_buy_value_63d_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 63-day buy sum within a trailing 504-day window."""
    return _zscore_rolling(_rolling_sum(insider_buy_value, _W63), _W504)


def ibs_ext_061_buy_value_21d_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of the 21-day buy sum within a trailing 504-day window."""
    return _zscore_rolling(_rolling_sum(insider_buy_value, _W21), _W504)


def ibs_ext_062_buy_shares_63d_zscore_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Z-score of the 63-day buy shares sum within a trailing 252-day window."""
    return _zscore_rolling(_rolling_sum(insider_buy_shares, _W63), _W252)


def ibs_ext_063_officer_buy_value_63d_pct_rank_504d(officer_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day officer buy sum within a trailing 504-day window."""
    return _rolling_rank_pct(_rolling_sum(officer_buy_value, _W63), _W504)


def ibs_ext_064_buy_value_252d_expanding_pct_rank(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of the trailing 252-day buy sum."""
    val = _rolling_sum(insider_buy_value, _W252)
    return val.expanding(min_periods=2).rank(pct=True)


# --- Group G (065-070): Average-buy-size variants on new windows/roles ---

def ibs_ext_065_avg_buy_size_42d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over trailing 42-day window."""
    return _safe_div(_rolling_sum(insider_buy_value, _W42),
                     _rolling_sum(insider_buy_count, _W42))


def ibs_ext_066_avg_buy_size_126d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over trailing 126-day window."""
    return _safe_div(_rolling_sum(insider_buy_value, _W126),
                     _rolling_sum(insider_buy_count, _W126))


def ibs_ext_067_avg_buy_size_63d_vs_252d_ratio(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of 63-day average buy size to 252-day average buy size (recent size tilt)."""
    short = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_buy_count, _W63))
    base  = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_buy_count, _W252))
    return _safe_div(short, base)


def ibs_ext_068_avg_shares_per_buy_126d(insider_buy_shares: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average shares per buy transaction over trailing 126-day window."""
    return _safe_div(_rolling_sum(insider_buy_shares, _W126),
                     _rolling_sum(insider_buy_count, _W126))


def ibs_ext_069_avg_buy_size_zscore_504d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of the 63-day average buy size within a trailing 504-day window."""
    avg = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_buy_count, _W63))
    return _zscore_rolling(avg, _W504)


def ibs_ext_070_avg_buy_size_252d_pct_rank_504d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of the 252-day average buy size within a 504-day window."""
    avg = _safe_div(_rolling_sum(insider_buy_value, _W252), _rolling_sum(insider_buy_count, _W252))
    return _rolling_rank_pct(avg, _W504)


# --- Group H (071-075): Threshold flags and composites ---

def ibs_ext_071_big_buy_flag_1m_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 126-day buy value exceeds $1 million."""
    return (_rolling_sum(insider_buy_value, _W126) > 1_000_000).astype(float)


def ibs_ext_072_big_buy_flag_5m_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 504-day buy value exceeds $5 million."""
    return (_rolling_sum(insider_buy_value, _W504) > 5_000_000).astype(float)


def ibs_ext_073_buy_value_42d_ewm_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 42-day buy sum divided by its 252-day EWM (buy-magnitude momentum ratio)."""
    val = _rolling_sum(insider_buy_value, _W42)
    return _safe_div(val, _ewm_mean(val, _W252))


def ibs_ext_074_buy_size_intensity_composite_63d(
    insider_buy_value: pd.Series,
    insider_buy_count: pd.Series,
) -> pd.Series:
    """
    Buy-size intensity composite over 63 days: equally-weighted average of the
    63-day buy-value percentile rank, the average-buy-size percentile rank, and
    the active-day fraction — all within a 252-day reference. Higher = larger,
    more frequent, more concentrated insider buying.
    """
    val_rank = _rolling_rank_pct(_rolling_sum(insider_buy_value, _W63), _W252).fillna(0.0)
    avg_size = _safe_div(_rolling_sum(insider_buy_value, _W63), _rolling_sum(insider_buy_count, _W63))
    size_rank = _rolling_rank_pct(avg_size, _W252).fillna(0.0)
    active = _active_days(insider_buy_value, _W63) / float(_W63)
    return (val_rank + size_rank + active) / 3.0


def ibs_ext_075_buy_magnitude_extreme_composite(
    insider_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    ceo_buy_value: pd.Series,
) -> pd.Series:
    """
    Extreme buy-magnitude composite: equally-weighted average of three 504-day
    z-scores (total, officer, CEO 252-day buy sums). Captures broad-based,
    historically large insider buying at distress lows.
    """
    z_total = _zscore_rolling(_rolling_sum(insider_buy_value, _W252), _W504)
    z_off   = _zscore_rolling(_rolling_sum(officer_buy_value, _W252), _W504)
    z_ceo   = _zscore_rolling(_rolling_sum(ceo_buy_value, _W252), _W504)
    return (z_total + z_off + z_ceo) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

INSIDER_BUY_SIZE_EXTENDED_REGISTRY_001_075 = {
    "ibs_ext_001_buy_value_10d": {"inputs": ["insider_buy_value"], "func": ibs_ext_001_buy_value_10d},
    "ibs_ext_002_buy_value_42d": {"inputs": ["insider_buy_value"], "func": ibs_ext_002_buy_value_42d},
    "ibs_ext_003_buy_value_189d": {"inputs": ["insider_buy_value"], "func": ibs_ext_003_buy_value_189d},
    "ibs_ext_004_buy_value_378d": {"inputs": ["insider_buy_value"], "func": ibs_ext_004_buy_value_378d},
    "ibs_ext_005_buy_shares_10d": {"inputs": ["insider_buy_shares"], "func": ibs_ext_005_buy_shares_10d},
    "ibs_ext_006_buy_shares_42d": {"inputs": ["insider_buy_shares"], "func": ibs_ext_006_buy_shares_42d},
    "ibs_ext_007_buy_count_42d": {"inputs": ["insider_buy_count"], "func": ibs_ext_007_buy_count_42d},
    "ibs_ext_008_buy_count_189d": {"inputs": ["insider_buy_count"], "func": ibs_ext_008_buy_count_189d},
    "ibs_ext_009_officer_buy_value_42d": {"inputs": ["officer_buy_value"], "func": ibs_ext_009_officer_buy_value_42d},
    "ibs_ext_010_ceo_buy_value_126d": {"inputs": ["ceo_buy_value"], "func": ibs_ext_010_ceo_buy_value_126d},
    "ibs_ext_011_cfo_buy_value_504d": {"inputs": ["cfo_buy_value"], "func": ibs_ext_011_cfo_buy_value_504d},
    "ibs_ext_012_director_buy_value_126d": {"inputs": ["director_buy_value"], "func": ibs_ext_012_director_buy_value_126d},
    "ibs_ext_013_mean_daily_buy_value_63d": {"inputs": ["insider_buy_value"], "func": ibs_ext_013_mean_daily_buy_value_63d},
    "ibs_ext_014_mean_daily_buy_value_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_014_mean_daily_buy_value_252d},
    "ibs_ext_015_median_buy_value_on_active_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_015_median_buy_value_on_active_252d},
    "ibs_ext_016_buy_value_std_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_016_buy_value_std_252d},
    "ibs_ext_017_buy_value_dispersion_ratio_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_017_buy_value_dispersion_ratio_252d},
    "ibs_ext_018_buy_value_range_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_018_buy_value_range_252d},
    "ibs_ext_019_peak_to_mean_buy_ratio_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_019_peak_to_mean_buy_ratio_252d},
    "ibs_ext_020_buy_shares_std_252d": {"inputs": ["insider_buy_shares"], "func": ibs_ext_020_buy_shares_std_252d},
    "ibs_ext_021_mean_officer_buy_value_252d": {"inputs": ["officer_buy_value"], "func": ibs_ext_021_mean_officer_buy_value_252d},
    "ibs_ext_022_largest_buy_share_of_63d_total": {"inputs": ["insider_buy_value"], "func": ibs_ext_022_largest_buy_share_of_63d_total},
    "ibs_ext_023_largest_buy_share_of_252d_total": {"inputs": ["insider_buy_value"], "func": ibs_ext_023_largest_buy_share_of_252d_total},
    "ibs_ext_024_buy_value_iqr_proxy_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_024_buy_value_iqr_proxy_252d},
    "ibs_ext_025_buy_active_days_21d": {"inputs": ["insider_buy_value"], "func": ibs_ext_025_buy_active_days_21d},
    "ibs_ext_026_buy_active_days_63d": {"inputs": ["insider_buy_value"], "func": ibs_ext_026_buy_active_days_63d},
    "ibs_ext_027_buy_active_days_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_027_buy_active_days_252d},
    "ibs_ext_028_officer_buy_active_days_252d": {"inputs": ["officer_buy_value"], "func": ibs_ext_028_officer_buy_active_days_252d},
    "ibs_ext_029_ceo_buy_active_days_252d": {"inputs": ["ceo_buy_value"], "func": ibs_ext_029_ceo_buy_active_days_252d},
    "ibs_ext_030_buy_active_fraction_63d": {"inputs": ["insider_buy_value"], "func": ibs_ext_030_buy_active_fraction_63d},
    "ibs_ext_031_buy_active_fraction_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_031_buy_active_fraction_252d},
    "ibs_ext_032_avg_value_per_active_day_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_032_avg_value_per_active_day_252d},
    "ibs_ext_033_avg_value_per_active_day_63d": {"inputs": ["insider_buy_value"], "func": ibs_ext_033_avg_value_per_active_day_63d},
    "ibs_ext_034_buy_active_days_21d_vs_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_034_buy_active_days_21d_vs_252d},
    "ibs_ext_035_consec_zero_buy_days": {"inputs": ["insider_buy_value"], "func": ibs_ext_035_consec_zero_buy_days},
    "ibs_ext_036_days_since_last_buy": {"inputs": ["insider_buy_value"], "func": ibs_ext_036_days_since_last_buy},
    "ibs_ext_037_days_since_officer_buy": {"inputs": ["officer_buy_value"], "func": ibs_ext_037_days_since_officer_buy},
    "ibs_ext_038_days_since_ceo_buy": {"inputs": ["ceo_buy_value"], "func": ibs_ext_038_days_since_ceo_buy},
    "ibs_ext_039_days_since_big_buy_100k": {"inputs": ["insider_buy_value"], "func": ibs_ext_039_days_since_big_buy_100k},
    "ibs_ext_040_days_since_big_buy_500k": {"inputs": ["insider_buy_value"], "func": ibs_ext_040_days_since_big_buy_500k},
    "ibs_ext_041_days_since_buy_252d_high": {"inputs": ["insider_buy_value"], "func": ibs_ext_041_days_since_buy_252d_high},
    "ibs_ext_042_buy_value_5d_vs_63d_ratio": {"inputs": ["insider_buy_value"], "func": ibs_ext_042_buy_value_5d_vs_63d_ratio},
    "ibs_ext_043_buy_value_21d_vs_126d_ratio": {"inputs": ["insider_buy_value"], "func": ibs_ext_043_buy_value_21d_vs_126d_ratio},
    "ibs_ext_044_buy_value_63d_vs_504d_ratio": {"inputs": ["insider_buy_value"], "func": ibs_ext_044_buy_value_63d_vs_504d_ratio},
    "ibs_ext_045_buy_value_42d_vs_252d_avg": {"inputs": ["insider_buy_value"], "func": ibs_ext_045_buy_value_42d_vs_252d_avg},
    "ibs_ext_046_buy_value_189d_vs_504d_ratio": {"inputs": ["insider_buy_value"], "func": ibs_ext_046_buy_value_189d_vs_504d_ratio},
    "ibs_ext_047_buy_value_63d_depth_below_median_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_047_buy_value_63d_depth_below_median_252d},
    "ibs_ext_048_buy_value_21d_shortfall_vs_252d_avg": {"inputs": ["insider_buy_value"], "func": ibs_ext_048_buy_value_21d_shortfall_vs_252d_avg},
    "ibs_ext_049_buy_drought_flag_63d": {"inputs": ["insider_buy_value"], "func": ibs_ext_049_buy_drought_flag_63d},
    "ibs_ext_050_buy_drought_flag_126d": {"inputs": ["insider_buy_value"], "func": ibs_ext_050_buy_drought_flag_126d},
    "ibs_ext_051_officer_buy_drought_flag_252d": {"inputs": ["officer_buy_value"], "func": ibs_ext_051_officer_buy_drought_flag_252d},
    "ibs_ext_052_buy_value_below_25pct_flag_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_052_buy_value_below_25pct_flag_252d},
    "ibs_ext_053_buy_value_63d_pct_of_504d_peak": {"inputs": ["insider_buy_value"], "func": ibs_ext_053_buy_value_63d_pct_of_504d_peak},
    "ibs_ext_054_buy_value_21d_drawdown_from_252d_peak": {"inputs": ["insider_buy_value"], "func": ibs_ext_054_buy_value_21d_drawdown_from_252d_peak},
    "ibs_ext_055_consec_quarters_buy_below_median": {"inputs": ["insider_buy_value"], "func": ibs_ext_055_consec_quarters_buy_below_median},
    "ibs_ext_056_buy_value_log_shortfall_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_056_buy_value_log_shortfall_252d},
    "ibs_ext_057_buy_value_21d_pct_rank_252d": {"inputs": ["insider_buy_value"], "func": ibs_ext_057_buy_value_21d_pct_rank_252d},
    "ibs_ext_058_buy_value_63d_pct_rank_504d": {"inputs": ["insider_buy_value"], "func": ibs_ext_058_buy_value_63d_pct_rank_504d},
    "ibs_ext_059_buy_value_126d_pct_rank_504d": {"inputs": ["insider_buy_value"], "func": ibs_ext_059_buy_value_126d_pct_rank_504d},
    "ibs_ext_060_buy_value_63d_zscore_504d": {"inputs": ["insider_buy_value"], "func": ibs_ext_060_buy_value_63d_zscore_504d},
    "ibs_ext_061_buy_value_21d_zscore_504d": {"inputs": ["insider_buy_value"], "func": ibs_ext_061_buy_value_21d_zscore_504d},
    "ibs_ext_062_buy_shares_63d_zscore_252d": {"inputs": ["insider_buy_shares"], "func": ibs_ext_062_buy_shares_63d_zscore_252d},
    "ibs_ext_063_officer_buy_value_63d_pct_rank_504d": {"inputs": ["officer_buy_value"], "func": ibs_ext_063_officer_buy_value_63d_pct_rank_504d},
    "ibs_ext_064_buy_value_252d_expanding_pct_rank": {"inputs": ["insider_buy_value"], "func": ibs_ext_064_buy_value_252d_expanding_pct_rank},
    "ibs_ext_065_avg_buy_size_42d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_065_avg_buy_size_42d},
    "ibs_ext_066_avg_buy_size_126d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_066_avg_buy_size_126d},
    "ibs_ext_067_avg_buy_size_63d_vs_252d_ratio": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_067_avg_buy_size_63d_vs_252d_ratio},
    "ibs_ext_068_avg_shares_per_buy_126d": {"inputs": ["insider_buy_shares", "insider_buy_count"], "func": ibs_ext_068_avg_shares_per_buy_126d},
    "ibs_ext_069_avg_buy_size_zscore_504d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_069_avg_buy_size_zscore_504d},
    "ibs_ext_070_avg_buy_size_252d_pct_rank_504d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_070_avg_buy_size_252d_pct_rank_504d},
    "ibs_ext_071_big_buy_flag_1m_126d": {"inputs": ["insider_buy_value"], "func": ibs_ext_071_big_buy_flag_1m_126d},
    "ibs_ext_072_big_buy_flag_5m_504d": {"inputs": ["insider_buy_value"], "func": ibs_ext_072_big_buy_flag_5m_504d},
    "ibs_ext_073_buy_value_42d_ewm_ratio": {"inputs": ["insider_buy_value"], "func": ibs_ext_073_buy_value_42d_ewm_ratio},
    "ibs_ext_074_buy_size_intensity_composite_63d": {"inputs": ["insider_buy_value", "insider_buy_count"], "func": ibs_ext_074_buy_size_intensity_composite_63d},
    "ibs_ext_075_buy_magnitude_extreme_composite": {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value"], "func": ibs_ext_075_buy_magnitude_extreme_composite},
}
