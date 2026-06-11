"""
84_insider_buy_size — Base Features 001-100
Domain: dollar magnitude of insider purchases (buy size / dollar scale)
Asset class: US equities | Sharadar SF2 insider transactions (daily aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
aggregated from Sharadar SF2 insider transaction filings to one row per
(ticker, date).  These are EVENT-DRIVEN series: most days are ZERO; positive
values appear only on filing days.  Do NOT forward-fill these series.
Aggregate over trailing windows using rolling SUMS.  Functions look strictly
backward using .shift(positive), .rolling(), or .expanding().
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
_W21  = 21    # 1 month
_W63  = 63    # 1 quarter
_W126 = 126   # 2 quarters
_W252 = 252   # 1 year
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Rolling total buy-value over multiple windows ---

def ibs_001_buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 21-day window."""
    return _rolling_sum(insider_buy_value, _W21)


def ibs_002_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 63-day (1 quarter) window."""
    return _rolling_sum(insider_buy_value, _W63)


def ibs_003_buy_value_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 126-day (2 quarter) window."""
    return _rolling_sum(insider_buy_value, _W126)


def ibs_004_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 252-day (1 year) window."""
    return _rolling_sum(insider_buy_value, _W252)


def ibs_005_buy_value_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 504-day (2 year) window."""
    return _rolling_sum(insider_buy_value, _W504)


def ibs_006_buy_value_5d(insider_buy_value: pd.Series) -> pd.Series:
    """Total insider buy dollar value over trailing 5-day (1 week) window."""
    return _rolling_sum(insider_buy_value, _W5)


def ibs_007_buy_shares_21d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 21-day window."""
    return _rolling_sum(insider_buy_shares, _W21)


def ibs_008_buy_shares_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 63-day window."""
    return _rolling_sum(insider_buy_shares, _W63)


def ibs_009_buy_shares_126d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 126-day window."""
    return _rolling_sum(insider_buy_shares, _W126)


def ibs_010_buy_shares_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 252-day window."""
    return _rolling_sum(insider_buy_shares, _W252)


def ibs_011_buy_shares_504d(insider_buy_shares: pd.Series) -> pd.Series:
    """Total insider buy shares over trailing 504-day window."""
    return _rolling_sum(insider_buy_shares, _W504)


def ibs_012_officer_buy_value_63d(officer_buy_value: pd.Series) -> pd.Series:
    """Total officer insider buy dollar value over trailing 63-day window."""
    return _rolling_sum(officer_buy_value, _W63)


def ibs_013_officer_buy_value_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Total officer insider buy dollar value over trailing 252-day window."""
    return _rolling_sum(officer_buy_value, _W252)


def ibs_014_ceo_buy_value_63d(ceo_buy_value: pd.Series) -> pd.Series:
    """Total CEO buy dollar value over trailing 63-day window."""
    return _rolling_sum(ceo_buy_value, _W63)


def ibs_015_ceo_buy_value_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Total CEO buy dollar value over trailing 252-day window."""
    return _rolling_sum(ceo_buy_value, _W252)


# --- Group B (016-030): Average transaction size features ---

def ibs_016_avg_buy_size_21d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over 21-day window."""
    val = _rolling_sum(insider_buy_value, _W21)
    cnt = _rolling_sum(insider_buy_count, _W21)
    return _safe_div(val, cnt)


def ibs_017_avg_buy_size_63d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over 63-day window."""
    val = _rolling_sum(insider_buy_value, _W63)
    cnt = _rolling_sum(insider_buy_count, _W63)
    return _safe_div(val, cnt)


def ibs_018_avg_buy_size_126d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over 126-day window."""
    val = _rolling_sum(insider_buy_value, _W126)
    cnt = _rolling_sum(insider_buy_count, _W126)
    return _safe_div(val, cnt)


def ibs_019_avg_buy_size_252d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over 252-day window."""
    val = _rolling_sum(insider_buy_value, _W252)
    cnt = _rolling_sum(insider_buy_count, _W252)
    return _safe_div(val, cnt)


def ibs_020_avg_shares_per_buy_63d(insider_buy_shares: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average shares per buy transaction over 63-day window."""
    shrs = _rolling_sum(insider_buy_shares, _W63)
    cnt  = _rolling_sum(insider_buy_count, _W63)
    return _safe_div(shrs, cnt)


def ibs_021_avg_shares_per_buy_252d(insider_buy_shares: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average shares per buy transaction over 252-day window."""
    shrs = _rolling_sum(insider_buy_shares, _W252)
    cnt  = _rolling_sum(insider_buy_count, _W252)
    return _safe_div(shrs, cnt)


def ibs_022_avg_officer_buy_size_252d(officer_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average officer buy dollar size per total-count transaction over 252-day window."""
    val = _rolling_sum(officer_buy_value, _W252)
    cnt = _rolling_sum(insider_buy_count, _W252)
    return _safe_div(val, cnt)


def ibs_023_cfo_buy_value_63d(cfo_buy_value: pd.Series) -> pd.Series:
    """Total CFO buy dollar value over trailing 63-day window."""
    return _rolling_sum(cfo_buy_value, _W63)


def ibs_024_cfo_buy_value_252d(cfo_buy_value: pd.Series) -> pd.Series:
    """Total CFO buy dollar value over trailing 252-day window."""
    return _rolling_sum(cfo_buy_value, _W252)


def ibs_025_tenpct_buy_value_63d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Total 10%+ holder buy dollar value over trailing 63-day window."""
    return _rolling_sum(tenpct_buy_value, _W63)


def ibs_026_tenpct_buy_value_252d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Total 10%+ holder buy dollar value over trailing 252-day window."""
    return _rolling_sum(tenpct_buy_value, _W252)


def ibs_027_director_buy_value_63d(director_buy_value: pd.Series) -> pd.Series:
    """Total director buy dollar value over trailing 63-day window."""
    return _rolling_sum(director_buy_value, _W63)


def ibs_028_director_buy_value_252d(director_buy_value: pd.Series) -> pd.Series:
    """Total director buy dollar value over trailing 252-day window."""
    return _rolling_sum(director_buy_value, _W252)


def ibs_029_ceo_plus_cfo_buy_value_63d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO buy dollar value over trailing 63-day window."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _W63)


def ibs_030_ceo_plus_cfo_buy_value_252d(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Combined CEO + CFO buy dollar value over trailing 252-day window."""
    return _rolling_sum(ceo_buy_value + cfo_buy_value, _W252)


# --- Group C (031-045): Rolling maximum single-window buy (peak size) ---

def ibs_031_peak_daily_buy_value_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day insider buy dollar value over trailing 21-day window."""
    return _rolling_max(insider_buy_value, _W21)


def ibs_032_peak_daily_buy_value_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day insider buy dollar value over trailing 63-day window."""
    return _rolling_max(insider_buy_value, _W63)


def ibs_033_peak_daily_buy_value_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day insider buy dollar value over trailing 126-day window."""
    return _rolling_max(insider_buy_value, _W126)


def ibs_034_peak_daily_buy_value_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day insider buy dollar value over trailing 252-day window."""
    return _rolling_max(insider_buy_value, _W252)


def ibs_035_peak_daily_buy_value_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Largest single-day insider buy dollar value over trailing 504-day window."""
    return _rolling_max(insider_buy_value, _W504)


def ibs_036_peak_officer_buy_value_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Largest single-day officer buy dollar value over trailing 252-day window."""
    return _rolling_max(officer_buy_value, _W252)


def ibs_037_peak_ceo_buy_value_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Largest single-day CEO buy dollar value over trailing 252-day window."""
    return _rolling_max(ceo_buy_value, _W252)


def ibs_038_peak_daily_buy_shares_63d(insider_buy_shares: pd.Series) -> pd.Series:
    """Largest single-day insider buy shares over trailing 63-day window."""
    return _rolling_max(insider_buy_shares, _W63)


def ibs_039_peak_daily_buy_shares_252d(insider_buy_shares: pd.Series) -> pd.Series:
    """Largest single-day insider buy shares over trailing 252-day window."""
    return _rolling_max(insider_buy_shares, _W252)


def ibs_040_buy_value_at_252d_high_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's buy value equals the 252-day rolling maximum."""
    mx = _rolling_max(insider_buy_value, _W252)
    return ((insider_buy_value > 0) & (insider_buy_value >= mx - _EPS)).astype(float)


def ibs_041_buy_value_at_504d_high_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's buy value equals the 504-day rolling maximum."""
    mx = _rolling_max(insider_buy_value, _W504)
    return ((insider_buy_value > 0) & (insider_buy_value >= mx - _EPS)).astype(float)


def ibs_042_buy_value_at_126d_high_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's buy value equals the 126-day rolling maximum."""
    mx = _rolling_max(insider_buy_value, _W126)
    return ((insider_buy_value > 0) & (insider_buy_value >= mx - _EPS)).astype(float)


def ibs_043_officer_buy_at_252d_high_flag(officer_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if today's officer buy value equals the 252-day rolling maximum."""
    mx = _rolling_max(officer_buy_value, _W252)
    return ((officer_buy_value > 0) & (officer_buy_value >= mx - _EPS)).astype(float)


def ibs_044_big_buy_flag_100k_21d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if trailing 21-day buy value exceeds $100k."""
    return (_rolling_sum(insider_buy_value, _W21) > 100_000).astype(float)


def ibs_045_big_buy_flag_500k_63d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: 1 if trailing 63-day buy value exceeds $500k."""
    return (_rolling_sum(insider_buy_value, _W63) > 500_000).astype(float)


# --- Group D (046-060): Buy value vs trailing baseline / z-score / rank ---

def ibs_046_buy_value_21d_vs_252d_avg(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 21-day buy value divided by trailing 252-day mean daily buy value."""
    short = _rolling_sum(insider_buy_value, _W21)
    base  = _rolling_mean(insider_buy_value, _W252)
    return _safe_div(short, base)


def ibs_047_buy_value_63d_vs_252d_avg(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy value sum divided by trailing 252-day mean daily buy value."""
    short = _rolling_sum(insider_buy_value, _W63)
    base  = _rolling_mean(insider_buy_value, _W252)
    return _safe_div(short, base)


def ibs_048_buy_value_21d_vs_504d_avg(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 21-day buy value divided by trailing 504-day mean daily buy value."""
    short = _rolling_sum(insider_buy_value, _W21)
    base  = _rolling_mean(insider_buy_value, _W504)
    return _safe_div(short, base)


def ibs_049_buy_value_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily buy value within trailing 252-day window."""
    return _zscore_rolling(insider_buy_value, _W252)


def ibs_050_buy_value_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily buy value within trailing 504-day window."""
    return _zscore_rolling(insider_buy_value, _W504)


def ibs_051_buy_value_pct_rank_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of daily buy value within trailing 252-day window."""
    return _rolling_rank_pct(insider_buy_value, _W252)


def ibs_052_buy_value_pct_rank_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of daily buy value within trailing 504-day window."""
    return _rolling_rank_pct(insider_buy_value, _W504)


def ibs_053_buy_value_63d_pct_of_peak_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy value sum as fraction of its 252-day rolling peak."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W252)
    return _safe_div(val, peak)


def ibs_054_buy_value_63d_pct_of_peak_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy value sum as fraction of its 504-day rolling peak."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = _rolling_max(val, _W504)
    return _safe_div(val, peak)


def ibs_055_buy_value_252d_expanding_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding z-score of trailing 252-day cumulative buy value (all-history)."""
    val = _rolling_sum(insider_buy_value, _W252)
    m   = val.expanding(min_periods=2).mean()
    sd  = val.expanding(min_periods=2).std()
    return _safe_div(val - m, sd)


def ibs_056_buy_value_21d_ewm_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 21-day buy value divided by its 252-day EWM (momentum ratio)."""
    val = _rolling_sum(insider_buy_value, _W21)
    ewm = _ewm_mean(val, _W252)
    return _safe_div(val, ewm)


def ibs_057_officer_buy_value_63d_vs_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day officer buy value sum vs its 252-day mean (normalized)."""
    short = _rolling_sum(officer_buy_value, _W63)
    base  = _rolling_mean(officer_buy_value, _W252)
    return _safe_div(short, base)


def ibs_058_ceo_buy_value_63d_vs_252d(ceo_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day CEO buy value sum vs its 252-day mean (normalized)."""
    short = _rolling_sum(ceo_buy_value, _W63)
    base  = _rolling_mean(ceo_buy_value, _W252)
    return _safe_div(short, base)


def ibs_059_buy_value_63d_expanding_pct_rank(insider_buy_value: pd.Series) -> pd.Series:
    """Expanding percentile rank of trailing 63-day buy value sum (all-history)."""
    val = _rolling_sum(insider_buy_value, _W63)
    return val.expanding(min_periods=2).rank(pct=True)


def ibs_060_buy_value_252d_pct_rank_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of trailing 252-day buy sum within a 504-day window."""
    val = _rolling_sum(insider_buy_value, _W252)
    return _rolling_rank_pct(val, _W504)


# --- Group E (061-075): Net buy magnitude, composites, and derived ---

def ibs_061_net_buy_value_21d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider buy value (buys minus sells) over 21-day window."""
    buys  = _rolling_sum(insider_buy_value, _W21)
    sells = _rolling_sum(insider_sell_value, _W21)
    return buys - sells


def ibs_062_net_buy_value_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider buy value (buys minus sells) over 63-day window."""
    buys  = _rolling_sum(insider_buy_value, _W63)
    sells = _rolling_sum(insider_sell_value, _W63)
    return buys - sells


def ibs_063_net_buy_value_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider buy value (buys minus sells) over 252-day window."""
    buys  = _rolling_sum(insider_buy_value, _W252)
    sells = _rolling_sum(insider_sell_value, _W252)
    return buys - sells


def ibs_064_buy_to_sell_value_ratio_63d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of total buy value to total sell value over 63-day window."""
    buys  = _rolling_sum(insider_buy_value, _W63)
    sells = _rolling_sum(insider_sell_value, _W63)
    return _safe_div(buys, sells)


def ibs_065_buy_to_sell_value_ratio_252d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of total buy value to total sell value over 252-day window."""
    buys  = _rolling_sum(insider_buy_value, _W252)
    sells = _rolling_sum(insider_sell_value, _W252)
    return _safe_div(buys, sells)


def ibs_066_buy_value_63d_per_share_held(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """63-day buy value sum normalized by reported insider shares held."""
    val  = _rolling_sum(insider_buy_value, _W63)
    held = _rolling_mean(insider_shares_held, _W63)
    return _safe_div(val, held)


def ibs_067_buy_value_252d_per_share_held(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """252-day buy value sum normalized by reported insider shares held."""
    val  = _rolling_sum(insider_buy_value, _W252)
    held = _rolling_mean(insider_shares_held, _W252)
    return _safe_div(val, held)


def ibs_068_officer_frac_of_total_buy_value_63d(officer_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Officer buy value as fraction of total insider buy value over 63-day window."""
    off   = _rolling_sum(officer_buy_value, _W63)
    total = _rolling_sum(insider_buy_value, _W63)
    return _safe_div(off, total)


def ibs_069_ceo_frac_of_total_buy_value_252d(ceo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CEO buy value as fraction of total insider buy value over 252-day window."""
    ceo   = _rolling_sum(ceo_buy_value, _W252)
    total = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(ceo, total)


def ibs_070_tenpct_frac_of_total_buy_value_252d(tenpct_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """10%+ holder buy value as fraction of total insider buy value over 252-day window."""
    ten   = _rolling_sum(tenpct_buy_value, _W252)
    total = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(ten, total)


def ibs_071_buy_value_63d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + trailing 63-day buy value sum) — compresses heavy right tail."""
    val = _rolling_sum(insider_buy_value, _W63)
    return np.log1p(val.clip(lower=0))


def ibs_072_buy_value_252d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + trailing 252-day buy value sum) — compresses heavy right tail."""
    val = _rolling_sum(insider_buy_value, _W252)
    return np.log1p(val.clip(lower=0))


def ibs_073_buy_shares_to_shares_held_ratio_63d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """63-day buy shares sum relative to mean insider shares held (acquisition rate)."""
    shrs = _rolling_sum(insider_buy_shares, _W63)
    held = _rolling_mean(insider_shares_held, _W63)
    return _safe_div(shrs, held)


def ibs_074_buy_value_63d_expanding_max_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy value as fraction of all-time expanding max of that sum."""
    val  = _rolling_sum(insider_buy_value, _W63)
    peak = val.expanding(min_periods=1).max()
    return _safe_div(val, peak)


def ibs_075_buy_size_composite_zscore(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series) -> pd.Series:
    """
    Composite buy-size z-score: equally weighted average of three 252-day z-scores
    (total buy value, officer buy value, CEO buy value).
    """
    z_total  = _zscore_rolling(_rolling_sum(insider_buy_value, _W252), _W252)
    z_off    = _zscore_rolling(_rolling_sum(officer_buy_value,  _W252), _W252)
    z_ceo    = _zscore_rolling(_rolling_sum(ceo_buy_value,      _W252), _W252)
    return (z_total + z_off + z_ceo) / 3.0


# --- Group F new (151-175): Additional transforms, thresholds, composites ---

def ibs_151_buy_value_126d_vs_252d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 126-day buy sum to 252-day buy sum (recency concentration over half-year)."""
    short = _rolling_sum(insider_buy_value, _W126)
    lng   = _rolling_sum(insider_buy_value, _W252)
    return _safe_div(short, lng)


def ibs_152_buy_value_5d_vs_21d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 5-day buy sum to 21-day buy sum (very near-term vs monthly concentration)."""
    short = _rolling_sum(insider_buy_value, _W5)
    med   = _rolling_sum(insider_buy_value, _W21)
    return _safe_div(short, med)


def ibs_153_cfo_buy_value_126d(cfo_buy_value: pd.Series) -> pd.Series:
    """Total CFO buy dollar value over trailing 126-day window."""
    return _rolling_sum(cfo_buy_value, _W126)


def ibs_154_director_buy_value_504d(director_buy_value: pd.Series) -> pd.Series:
    """Total director buy dollar value over trailing 504-day window."""
    return _rolling_sum(director_buy_value, _W504)


def ibs_155_tenpct_buy_value_504d(tenpct_buy_value: pd.Series) -> pd.Series:
    """Total 10%+ holder buy dollar value over trailing 504-day window."""
    return _rolling_sum(tenpct_buy_value, _W504)


def ibs_156_buy_value_126d_zscore_504d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of trailing 126-day buy value sum within a 504-day window."""
    val = _rolling_sum(insider_buy_value, _W126)
    m   = _rolling_mean(val, _W504)
    sd  = _rolling_std(val, _W504)
    return _safe_div(val - m, sd)


def ibs_157_buy_value_5d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + trailing 5-day buy value sum) — captures spike activity."""
    val = _rolling_sum(insider_buy_value, _W5)
    return np.log1p(val.clip(lower=0))


def ibs_158_buy_value_126d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + trailing 126-day buy value sum)."""
    val = _rolling_sum(insider_buy_value, _W126)
    return np.log1p(val.clip(lower=0))


def ibs_159_buy_value_504d_log(insider_buy_value: pd.Series) -> pd.Series:
    """Log(1 + trailing 504-day buy value sum)."""
    val = _rolling_sum(insider_buy_value, _W504)
    return np.log1p(val.clip(lower=0))


def ibs_160_buy_value_pct_rank_126d(insider_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of daily buy value within trailing 126-day window."""
    return _rolling_rank_pct(insider_buy_value, _W126)


def ibs_161_officer_buy_value_pct_rank_252d(officer_buy_value: pd.Series) -> pd.Series:
    """Percentile rank of daily officer buy value within trailing 252-day window."""
    return _rolling_rank_pct(officer_buy_value, _W252)


def ibs_162_net_buy_value_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Net insider buy value (buys minus sells) over 126-day window."""
    return _rolling_sum(insider_buy_value, _W126) - _rolling_sum(insider_sell_value, _W126)


def ibs_163_buy_to_sell_value_ratio_126d(insider_buy_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """Ratio of total buy value to total sell value over 126-day window."""
    return _safe_div(_rolling_sum(insider_buy_value, _W126),
                     _rolling_sum(insider_sell_value, _W126))


def ibs_164_buy_value_126d_per_share_held(insider_buy_value: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """126-day buy value sum normalized by mean insider shares held (126-day window)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W126),
                     _rolling_mean(insider_shares_held, _W126))


def ibs_165_buy_shares_to_shares_held_ratio_252d(insider_buy_shares: pd.Series, insider_shares_held: pd.Series) -> pd.Series:
    """252-day buy shares sum relative to mean insider shares held (acquisition rate)."""
    return _safe_div(_rolling_sum(insider_buy_shares, _W252),
                     _rolling_mean(insider_shares_held, _W252))


def ibs_166_big_buy_flag_2m_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Binary flag: trailing 252-day buy value exceeds $2 million."""
    return (_rolling_sum(insider_buy_value, _W252) > 2_000_000).astype(float)


def ibs_167_ceo_buy_value_504d(ceo_buy_value: pd.Series) -> pd.Series:
    """Total CEO buy dollar value over trailing 504-day window."""
    return _rolling_sum(ceo_buy_value, _W504)


def ibs_168_officer_buy_value_504d(officer_buy_value: pd.Series) -> pd.Series:
    """Total officer buy dollar value over trailing 504-day window."""
    return _rolling_sum(officer_buy_value, _W504)


def ibs_169_cfo_frac_of_total_buy_value_252d(cfo_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """CFO buy value as fraction of total insider buy value over 252-day window."""
    return _safe_div(_rolling_sum(cfo_buy_value, _W252),
                     _rolling_sum(insider_buy_value, _W252))


def ibs_170_director_frac_of_total_buy_value_252d(director_buy_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Director buy value as fraction of total insider buy value over 252-day window."""
    return _safe_div(_rolling_sum(director_buy_value, _W252),
                     _rolling_sum(insider_buy_value, _W252))


def ibs_171_buy_value_252d_vs_504d_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of 252-day buy sum to 504-day buy sum (recent-year vs 2-year concentration)."""
    return _safe_div(_rolling_sum(insider_buy_value, _W252),
                     _rolling_sum(insider_buy_value, _W504))


def ibs_172_buy_value_5d_zscore_252d(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of daily 5-day rolling buy value within a 252-day window."""
    val = _rolling_sum(insider_buy_value, _W5)
    m   = _rolling_mean(val, _W252)
    sd  = _rolling_std(val, _W252)
    return _safe_div(val - m, sd)


def ibs_173_avg_buy_size_504d(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Average dollar size per buy transaction over 504-day window."""
    return _safe_div(_rolling_sum(insider_buy_value, _W504),
                     _rolling_sum(insider_buy_count, _W504))


def ibs_174_buy_shares_126d_log(insider_buy_shares: pd.Series) -> pd.Series:
    """Log(1 + trailing 126-day buy shares sum)."""
    return np.log1p(_rolling_sum(insider_buy_shares, _W126).clip(lower=0))


def ibs_175_four_role_buy_composite_zscore(insider_buy_value: pd.Series, officer_buy_value: pd.Series, ceo_buy_value: pd.Series, director_buy_value: pd.Series) -> pd.Series:
    """Composite buy-size z-score: equally weighted average of four 252-day z-scores (total, officer, CEO, director)."""
    def _zs(s):
        return _zscore_rolling(_rolling_sum(s, _W252), _W252)
    return (_zs(insider_buy_value) + _zs(officer_buy_value) + _zs(ceo_buy_value) + _zs(director_buy_value)) / 4.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

INSIDER_BUY_SIZE_REGISTRY_001_075 = {
    "ibs_001_buy_value_21d":                      {"inputs": ["insider_buy_value"],                                   "func": ibs_001_buy_value_21d},
    "ibs_002_buy_value_63d":                      {"inputs": ["insider_buy_value"],                                   "func": ibs_002_buy_value_63d},
    "ibs_003_buy_value_126d":                     {"inputs": ["insider_buy_value"],                                   "func": ibs_003_buy_value_126d},
    "ibs_004_buy_value_252d":                     {"inputs": ["insider_buy_value"],                                   "func": ibs_004_buy_value_252d},
    "ibs_005_buy_value_504d":                     {"inputs": ["insider_buy_value"],                                   "func": ibs_005_buy_value_504d},
    "ibs_006_buy_value_5d":                       {"inputs": ["insider_buy_value"],                                   "func": ibs_006_buy_value_5d},
    "ibs_007_buy_shares_21d":                     {"inputs": ["insider_buy_shares"],                                  "func": ibs_007_buy_shares_21d},
    "ibs_008_buy_shares_63d":                     {"inputs": ["insider_buy_shares"],                                  "func": ibs_008_buy_shares_63d},
    "ibs_009_buy_shares_126d":                    {"inputs": ["insider_buy_shares"],                                  "func": ibs_009_buy_shares_126d},
    "ibs_010_buy_shares_252d":                    {"inputs": ["insider_buy_shares"],                                  "func": ibs_010_buy_shares_252d},
    "ibs_011_buy_shares_504d":                    {"inputs": ["insider_buy_shares"],                                  "func": ibs_011_buy_shares_504d},
    "ibs_012_officer_buy_value_63d":              {"inputs": ["officer_buy_value"],                                   "func": ibs_012_officer_buy_value_63d},
    "ibs_013_officer_buy_value_252d":             {"inputs": ["officer_buy_value"],                                   "func": ibs_013_officer_buy_value_252d},
    "ibs_014_ceo_buy_value_63d":                  {"inputs": ["ceo_buy_value"],                                       "func": ibs_014_ceo_buy_value_63d},
    "ibs_015_ceo_buy_value_252d":                 {"inputs": ["ceo_buy_value"],                                       "func": ibs_015_ceo_buy_value_252d},
    "ibs_016_avg_buy_size_21d":                   {"inputs": ["insider_buy_value", "insider_buy_count"],              "func": ibs_016_avg_buy_size_21d},
    "ibs_017_avg_buy_size_63d":                   {"inputs": ["insider_buy_value", "insider_buy_count"],              "func": ibs_017_avg_buy_size_63d},
    "ibs_018_avg_buy_size_126d":                  {"inputs": ["insider_buy_value", "insider_buy_count"],              "func": ibs_018_avg_buy_size_126d},
    "ibs_019_avg_buy_size_252d":                  {"inputs": ["insider_buy_value", "insider_buy_count"],              "func": ibs_019_avg_buy_size_252d},
    "ibs_020_avg_shares_per_buy_63d":             {"inputs": ["insider_buy_shares", "insider_buy_count"],             "func": ibs_020_avg_shares_per_buy_63d},
    "ibs_021_avg_shares_per_buy_252d":            {"inputs": ["insider_buy_shares", "insider_buy_count"],             "func": ibs_021_avg_shares_per_buy_252d},
    "ibs_022_avg_officer_buy_size_252d":          {"inputs": ["officer_buy_value", "insider_buy_count"],              "func": ibs_022_avg_officer_buy_size_252d},
    "ibs_023_cfo_buy_value_63d":                  {"inputs": ["cfo_buy_value"],                                       "func": ibs_023_cfo_buy_value_63d},
    "ibs_024_cfo_buy_value_252d":                 {"inputs": ["cfo_buy_value"],                                       "func": ibs_024_cfo_buy_value_252d},
    "ibs_025_tenpct_buy_value_63d":               {"inputs": ["tenpct_buy_value"],                                    "func": ibs_025_tenpct_buy_value_63d},
    "ibs_026_tenpct_buy_value_252d":              {"inputs": ["tenpct_buy_value"],                                    "func": ibs_026_tenpct_buy_value_252d},
    "ibs_027_director_buy_value_63d":             {"inputs": ["director_buy_value"],                                  "func": ibs_027_director_buy_value_63d},
    "ibs_028_director_buy_value_252d":            {"inputs": ["director_buy_value"],                                  "func": ibs_028_director_buy_value_252d},
    "ibs_029_ceo_plus_cfo_buy_value_63d":         {"inputs": ["ceo_buy_value", "cfo_buy_value"],                      "func": ibs_029_ceo_plus_cfo_buy_value_63d},
    "ibs_030_ceo_plus_cfo_buy_value_252d":        {"inputs": ["ceo_buy_value", "cfo_buy_value"],                      "func": ibs_030_ceo_plus_cfo_buy_value_252d},
    "ibs_031_peak_daily_buy_value_21d":           {"inputs": ["insider_buy_value"],                                   "func": ibs_031_peak_daily_buy_value_21d},
    "ibs_032_peak_daily_buy_value_63d":           {"inputs": ["insider_buy_value"],                                   "func": ibs_032_peak_daily_buy_value_63d},
    "ibs_033_peak_daily_buy_value_126d":          {"inputs": ["insider_buy_value"],                                   "func": ibs_033_peak_daily_buy_value_126d},
    "ibs_034_peak_daily_buy_value_252d":          {"inputs": ["insider_buy_value"],                                   "func": ibs_034_peak_daily_buy_value_252d},
    "ibs_035_peak_daily_buy_value_504d":          {"inputs": ["insider_buy_value"],                                   "func": ibs_035_peak_daily_buy_value_504d},
    "ibs_036_peak_officer_buy_value_252d":        {"inputs": ["officer_buy_value"],                                   "func": ibs_036_peak_officer_buy_value_252d},
    "ibs_037_peak_ceo_buy_value_252d":            {"inputs": ["ceo_buy_value"],                                       "func": ibs_037_peak_ceo_buy_value_252d},
    "ibs_038_peak_daily_buy_shares_63d":          {"inputs": ["insider_buy_shares"],                                  "func": ibs_038_peak_daily_buy_shares_63d},
    "ibs_039_peak_daily_buy_shares_252d":         {"inputs": ["insider_buy_shares"],                                  "func": ibs_039_peak_daily_buy_shares_252d},
    "ibs_040_buy_value_at_252d_high_flag":        {"inputs": ["insider_buy_value"],                                   "func": ibs_040_buy_value_at_252d_high_flag},
    "ibs_041_buy_value_at_504d_high_flag":        {"inputs": ["insider_buy_value"],                                   "func": ibs_041_buy_value_at_504d_high_flag},
    "ibs_042_buy_value_at_126d_high_flag":        {"inputs": ["insider_buy_value"],                                   "func": ibs_042_buy_value_at_126d_high_flag},
    "ibs_043_officer_buy_at_252d_high_flag":      {"inputs": ["officer_buy_value"],                                   "func": ibs_043_officer_buy_at_252d_high_flag},
    "ibs_044_big_buy_flag_100k_21d":              {"inputs": ["insider_buy_value"],                                   "func": ibs_044_big_buy_flag_100k_21d},
    "ibs_045_big_buy_flag_500k_63d":              {"inputs": ["insider_buy_value"],                                   "func": ibs_045_big_buy_flag_500k_63d},
    "ibs_046_buy_value_21d_vs_252d_avg":          {"inputs": ["insider_buy_value"],                                   "func": ibs_046_buy_value_21d_vs_252d_avg},
    "ibs_047_buy_value_63d_vs_252d_avg":          {"inputs": ["insider_buy_value"],                                   "func": ibs_047_buy_value_63d_vs_252d_avg},
    "ibs_048_buy_value_21d_vs_504d_avg":          {"inputs": ["insider_buy_value"],                                   "func": ibs_048_buy_value_21d_vs_504d_avg},
    "ibs_049_buy_value_zscore_252d":              {"inputs": ["insider_buy_value"],                                   "func": ibs_049_buy_value_zscore_252d},
    "ibs_050_buy_value_zscore_504d":              {"inputs": ["insider_buy_value"],                                   "func": ibs_050_buy_value_zscore_504d},
    "ibs_051_buy_value_pct_rank_252d":            {"inputs": ["insider_buy_value"],                                   "func": ibs_051_buy_value_pct_rank_252d},
    "ibs_052_buy_value_pct_rank_504d":            {"inputs": ["insider_buy_value"],                                   "func": ibs_052_buy_value_pct_rank_504d},
    "ibs_053_buy_value_63d_pct_of_peak_252d":     {"inputs": ["insider_buy_value"],                                   "func": ibs_053_buy_value_63d_pct_of_peak_252d},
    "ibs_054_buy_value_63d_pct_of_peak_504d":     {"inputs": ["insider_buy_value"],                                   "func": ibs_054_buy_value_63d_pct_of_peak_504d},
    "ibs_055_buy_value_252d_expanding_zscore":    {"inputs": ["insider_buy_value"],                                   "func": ibs_055_buy_value_252d_expanding_zscore},
    "ibs_056_buy_value_21d_ewm_ratio":            {"inputs": ["insider_buy_value"],                                   "func": ibs_056_buy_value_21d_ewm_ratio},
    "ibs_057_officer_buy_value_63d_vs_252d":      {"inputs": ["officer_buy_value"],                                   "func": ibs_057_officer_buy_value_63d_vs_252d},
    "ibs_058_ceo_buy_value_63d_vs_252d":          {"inputs": ["ceo_buy_value"],                                       "func": ibs_058_ceo_buy_value_63d_vs_252d},
    "ibs_059_buy_value_63d_expanding_pct_rank":   {"inputs": ["insider_buy_value"],                                   "func": ibs_059_buy_value_63d_expanding_pct_rank},
    "ibs_060_buy_value_252d_pct_rank_504d":       {"inputs": ["insider_buy_value"],                                   "func": ibs_060_buy_value_252d_pct_rank_504d},
    "ibs_061_net_buy_value_21d":                  {"inputs": ["insider_buy_value", "insider_sell_value"],             "func": ibs_061_net_buy_value_21d},
    "ibs_062_net_buy_value_63d":                  {"inputs": ["insider_buy_value", "insider_sell_value"],             "func": ibs_062_net_buy_value_63d},
    "ibs_063_net_buy_value_252d":                 {"inputs": ["insider_buy_value", "insider_sell_value"],             "func": ibs_063_net_buy_value_252d},
    "ibs_064_buy_to_sell_value_ratio_63d":        {"inputs": ["insider_buy_value", "insider_sell_value"],             "func": ibs_064_buy_to_sell_value_ratio_63d},
    "ibs_065_buy_to_sell_value_ratio_252d":       {"inputs": ["insider_buy_value", "insider_sell_value"],             "func": ibs_065_buy_to_sell_value_ratio_252d},
    "ibs_066_buy_value_63d_per_share_held":       {"inputs": ["insider_buy_value", "insider_shares_held"],            "func": ibs_066_buy_value_63d_per_share_held},
    "ibs_067_buy_value_252d_per_share_held":      {"inputs": ["insider_buy_value", "insider_shares_held"],            "func": ibs_067_buy_value_252d_per_share_held},
    "ibs_068_officer_frac_of_total_buy_value_63d":{"inputs": ["officer_buy_value", "insider_buy_value"],              "func": ibs_068_officer_frac_of_total_buy_value_63d},
    "ibs_069_ceo_frac_of_total_buy_value_252d":   {"inputs": ["ceo_buy_value", "insider_buy_value"],                  "func": ibs_069_ceo_frac_of_total_buy_value_252d},
    "ibs_070_tenpct_frac_of_total_buy_value_252d":{"inputs": ["tenpct_buy_value", "insider_buy_value"],               "func": ibs_070_tenpct_frac_of_total_buy_value_252d},
    "ibs_071_buy_value_63d_log":                  {"inputs": ["insider_buy_value"],                                   "func": ibs_071_buy_value_63d_log},
    "ibs_072_buy_value_252d_log":                 {"inputs": ["insider_buy_value"],                                   "func": ibs_072_buy_value_252d_log},
    "ibs_073_buy_shares_to_shares_held_ratio_63d":{"inputs": ["insider_buy_shares", "insider_shares_held"],           "func": ibs_073_buy_shares_to_shares_held_ratio_63d},
    "ibs_074_buy_value_63d_expanding_max_ratio":  {"inputs": ["insider_buy_value"],                                   "func": ibs_074_buy_value_63d_expanding_max_ratio},
    "ibs_075_buy_size_composite_zscore":          {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value"], "func": ibs_075_buy_size_composite_zscore},
    "ibs_151_buy_value_126d_vs_252d_ratio":       {"inputs": ["insider_buy_value"],                                                           "func": ibs_151_buy_value_126d_vs_252d_ratio},
    "ibs_152_buy_value_5d_vs_21d_ratio":          {"inputs": ["insider_buy_value"],                                                           "func": ibs_152_buy_value_5d_vs_21d_ratio},
    "ibs_153_cfo_buy_value_126d":                 {"inputs": ["cfo_buy_value"],                                                               "func": ibs_153_cfo_buy_value_126d},
    "ibs_154_director_buy_value_504d":            {"inputs": ["director_buy_value"],                                                          "func": ibs_154_director_buy_value_504d},
    "ibs_155_tenpct_buy_value_504d":              {"inputs": ["tenpct_buy_value"],                                                            "func": ibs_155_tenpct_buy_value_504d},
    "ibs_156_buy_value_126d_zscore_504d":         {"inputs": ["insider_buy_value"],                                                           "func": ibs_156_buy_value_126d_zscore_504d},
    "ibs_157_buy_value_5d_log":                   {"inputs": ["insider_buy_value"],                                                           "func": ibs_157_buy_value_5d_log},
    "ibs_158_buy_value_126d_log":                 {"inputs": ["insider_buy_value"],                                                           "func": ibs_158_buy_value_126d_log},
    "ibs_159_buy_value_504d_log":                 {"inputs": ["insider_buy_value"],                                                           "func": ibs_159_buy_value_504d_log},
    "ibs_160_buy_value_pct_rank_126d":            {"inputs": ["insider_buy_value"],                                                           "func": ibs_160_buy_value_pct_rank_126d},
    "ibs_161_officer_buy_value_pct_rank_252d":    {"inputs": ["officer_buy_value"],                                                           "func": ibs_161_officer_buy_value_pct_rank_252d},
    "ibs_162_net_buy_value_126d":                 {"inputs": ["insider_buy_value", "insider_sell_value"],                                     "func": ibs_162_net_buy_value_126d},
    "ibs_163_buy_to_sell_value_ratio_126d":       {"inputs": ["insider_buy_value", "insider_sell_value"],                                     "func": ibs_163_buy_to_sell_value_ratio_126d},
    "ibs_164_buy_value_126d_per_share_held":      {"inputs": ["insider_buy_value", "insider_shares_held"],                                    "func": ibs_164_buy_value_126d_per_share_held},
    "ibs_165_buy_shares_to_shares_held_ratio_252d":{"inputs": ["insider_buy_shares", "insider_shares_held"],                                  "func": ibs_165_buy_shares_to_shares_held_ratio_252d},
    "ibs_166_big_buy_flag_2m_252d":               {"inputs": ["insider_buy_value"],                                                           "func": ibs_166_big_buy_flag_2m_252d},
    "ibs_167_ceo_buy_value_504d":                 {"inputs": ["ceo_buy_value"],                                                               "func": ibs_167_ceo_buy_value_504d},
    "ibs_168_officer_buy_value_504d":             {"inputs": ["officer_buy_value"],                                                           "func": ibs_168_officer_buy_value_504d},
    "ibs_169_cfo_frac_of_total_buy_value_252d":   {"inputs": ["cfo_buy_value", "insider_buy_value"],                                          "func": ibs_169_cfo_frac_of_total_buy_value_252d},
    "ibs_170_director_frac_of_total_buy_value_252d":{"inputs": ["director_buy_value", "insider_buy_value"],                                   "func": ibs_170_director_frac_of_total_buy_value_252d},
    "ibs_171_buy_value_252d_vs_504d_ratio":       {"inputs": ["insider_buy_value"],                                                           "func": ibs_171_buy_value_252d_vs_504d_ratio},
    "ibs_172_buy_value_5d_zscore_252d":           {"inputs": ["insider_buy_value"],                                                           "func": ibs_172_buy_value_5d_zscore_252d},
    "ibs_173_avg_buy_size_504d":                  {"inputs": ["insider_buy_value", "insider_buy_count"],                                      "func": ibs_173_avg_buy_size_504d},
    "ibs_174_buy_shares_126d_log":                {"inputs": ["insider_buy_shares"],                                                          "func": ibs_174_buy_shares_126d_log},
    "ibs_175_four_role_buy_composite_zscore":     {"inputs": ["insider_buy_value", "officer_buy_value", "ceo_buy_value", "director_buy_value"], "func": ibs_175_four_role_buy_composite_zscore},
}
