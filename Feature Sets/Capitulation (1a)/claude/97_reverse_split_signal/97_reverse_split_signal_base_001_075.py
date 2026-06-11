"""
97_reverse_split_signal — Base Features 001-100
Domain: reverse splits as late-stage distress flags; nominal-price exhaustion signals
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Functions look strictly backward using .shift(positive),
.rolling(), or .expanding().  Trading-day constants: 1 year = 252 td,
1 quarter = 63 td, 1 month = 21 td, 1 week = 5 td.

  split_factor  : per-day split factor; 1.0 on normal days.
                  < 1.0 on reverse-split effective dates (e.g. 1-for-10 -> 0.1).
                  > 1.0 on forward-split effective dates (e.g. 2-for-1 -> 2.0).
  closeunadj    : raw unadjusted daily close price (USD); nominally raised by
                  reverse splits; driven toward sub-$1 by distress.
  close         : split/dividend-adjusted daily close price (USD).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_TD_MO    = 21    # 1 month in trading days
_TD_WK    = 5     # 1 week in trading days
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


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


def _is_reverse_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor < 1 (reverse split), else 0."""
    return (split_factor < 1.0).astype(float)


def _is_forward_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor > 1 (forward split), else 0."""
    return (split_factor > 1.0).astype(float)


def _reverse_split_magnitude(split_factor: pd.Series) -> pd.Series:
    """Reverse-split magnitude: 1/split_factor on RS days, NaN otherwise."""
    rs = split_factor.copy().astype(float)
    rs[rs >= 1.0] = np.nan
    return 1.0 / rs.replace(0, np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Reverse-split occurrence flags and recency ---

def rss_001_reverse_split_flag(split_factor: pd.Series) -> pd.Series:
    """Binary: 1 on days where a reverse split was effective (split_factor < 1)."""
    return _is_reverse_split(split_factor)


def rss_002_forward_split_flag(split_factor: pd.Series) -> pd.Series:
    """Binary: 1 on days where a forward split was effective (split_factor > 1)."""
    return _is_forward_split(split_factor)


def rss_003_split_event_flag(split_factor: pd.Series) -> pd.Series:
    """Binary: 1 on any split day (forward or reverse); 0 otherwise."""
    return (split_factor != 1.0).astype(float)


def rss_004_days_since_last_reverse_split(split_factor: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent reverse split (NaN if none yet)."""
    rs = _is_reverse_split(split_factor)
    result = np.full(len(rs), np.nan)
    last = -1
    arr = rs.values
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            result[i] = float(i - last)
    return pd.Series(result, index=split_factor.index)


def rss_005_reverse_split_within_21d(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 21 trading days."""
    rs = _is_reverse_split(split_factor)
    return (_rolling_sum(rs, _TD_MO) > 0).astype(float)


def rss_006_reverse_split_within_63d(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 63 trading days."""
    rs = _is_reverse_split(split_factor)
    return (_rolling_sum(rs, _TD_QTR) > 0).astype(float)


def rss_007_reverse_split_within_126d(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 126 trading days."""
    rs = _is_reverse_split(split_factor)
    return (_rolling_sum(rs, _TD_2Q) > 0).astype(float)


def rss_008_reverse_split_within_252d(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 252 trading days."""
    rs = _is_reverse_split(split_factor)
    return (_rolling_sum(rs, _TD_YEAR) > 0).astype(float)


def rss_009_reverse_split_within_504d(split_factor: pd.Series) -> pd.Series:
    """1 if any reverse split occurred in the trailing 504 trading days."""
    rs = _is_reverse_split(split_factor)
    return (_rolling_sum(rs, _TD_2Y) > 0).astype(float)


def rss_010_days_since_last_reverse_split_log(split_factor: pd.Series) -> pd.Series:
    """Log(1 + days since last reverse split); NaN if no prior reverse split."""
    raw = rss_004_days_since_last_reverse_split(split_factor)
    return np.log1p(raw)


def rss_011_days_since_last_forward_split(split_factor: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent forward split (NaN if none yet)."""
    fs = _is_forward_split(split_factor)
    result = np.full(len(fs), np.nan)
    last = -1
    arr = fs.values
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            result[i] = float(i - last)
    return pd.Series(result, index=split_factor.index)


def rss_012_reverse_minus_forward_split_flag(split_factor: pd.Series) -> pd.Series:
    """Difference: reverse_split_flag minus forward_split_flag (+1=RS, -1=FS, 0=none)."""
    return _is_reverse_split(split_factor) - _is_forward_split(split_factor)


def rss_013_expanding_reverse_split_count(split_factor: pd.Series) -> pd.Series:
    """Cumulative count of reverse-split events from the beginning of history."""
    rs = _is_reverse_split(split_factor)
    return rs.expanding(min_periods=1).sum()


def rss_014_reverse_split_recency_decay(split_factor: pd.Series) -> pd.Series:
    """EWM-decayed reverse-split flag (span=63); high near recent RS events."""
    rs = _is_reverse_split(split_factor)
    return _ewm_mean(rs, _TD_QTR)


def rss_015_reverse_split_recency_decay_slow(split_factor: pd.Series) -> pd.Series:
    """EWM-decayed reverse-split flag with slow decay (span=252)."""
    rs = _is_reverse_split(split_factor)
    return _ewm_mean(rs, _TD_YEAR)


# --- Group B (016-030): Trailing counts of reverse splits ---

def rss_016_rs_count_21d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 21 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_MO)


def rss_017_rs_count_63d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 63 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_QTR)


def rss_018_rs_count_126d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 126 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Q)


def rss_019_rs_count_252d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 252 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)


def rss_020_rs_count_504d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 504 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Y)


def rss_021_rs_count_756d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 756 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_3Y)


def rss_022_rs_count_1260d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 1260 trading days (5 years)."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_5Y)


def rss_023_fs_count_252d(split_factor: pd.Series) -> pd.Series:
    """Count of forward-split days in trailing 252 trading days."""
    return _rolling_sum(_is_forward_split(split_factor), _TD_YEAR)


def rss_024_rs_minus_fs_count_252d(split_factor: pd.Series) -> pd.Series:
    """Reverse-split count minus forward-split count in trailing 252 days."""
    return rss_019_rs_count_252d(split_factor) - rss_023_fs_count_252d(split_factor)


def rss_025_rs_count_252d_gt1_flag(split_factor: pd.Series) -> pd.Series:
    """1 if more than 1 reverse split occurred in trailing 252 days (repeat offender)."""
    return (rss_019_rs_count_252d(split_factor) > 1).astype(float)


def rss_026_rs_count_504d_gt2_flag(split_factor: pd.Series) -> pd.Series:
    """1 if more than 2 reverse splits occurred in trailing 504 days."""
    return (rss_020_rs_count_504d(split_factor) > 2).astype(float)


def rss_027_rs_count_expanding_gt0_flag(split_factor: pd.Series) -> pd.Series:
    """1 if the stock has ever had a reverse split in history."""
    return (rss_013_expanding_reverse_split_count(split_factor) > 0).astype(float)


def rss_028_rs_cluster_density_63d(split_factor: pd.Series) -> pd.Series:
    """Fraction of days in trailing 63 days that were reverse-split effective dates."""
    return _rolling_mean(_is_reverse_split(split_factor), _TD_QTR)


def rss_029_rs_cluster_density_252d(split_factor: pd.Series) -> pd.Series:
    """Fraction of days in trailing 252 days that were reverse-split effective dates."""
    return _rolling_mean(_is_reverse_split(split_factor), _TD_YEAR)


def rss_030_rs_acceleration_63d_vs_252d(split_factor: pd.Series) -> pd.Series:
    """Ratio of RS density in 63d vs 252d window — detects recent clustering."""
    d63  = rss_028_rs_cluster_density_63d(split_factor)
    d252 = rss_029_rs_cluster_density_252d(split_factor)
    return _safe_div(d63, d252 + _EPS)


# --- Group C (031-045): Reverse-split severity (magnitude) ---

def rss_031_rs_magnitude_current(split_factor: pd.Series) -> pd.Series:
    """Reverse-split magnitude (1/split_factor) on RS days; NaN otherwise."""
    return _reverse_split_magnitude(split_factor)


def rss_032_rs_log_magnitude_current(split_factor: pd.Series) -> pd.Series:
    """Log of reverse-split magnitude on RS days; NaN otherwise."""
    mag = _reverse_split_magnitude(split_factor)
    return np.log(mag.replace(0, np.nan))


def rss_033_rs_magnitude_max_21d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude (1/sf) observed in trailing 21 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_MO)


def rss_034_rs_magnitude_max_63d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude observed in trailing 63 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_QTR)


def rss_035_rs_magnitude_max_252d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude observed in trailing 252 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_YEAR)


def rss_036_rs_magnitude_max_504d(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude observed in trailing 504 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _rolling_max(mag, _TD_2Y)


def rss_037_rs_magnitude_max_expanding(split_factor: pd.Series) -> pd.Series:
    """Maximum reverse-split magnitude ever observed (expanding max)."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return mag.expanding(min_periods=1).max()


def rss_038_cumulative_rs_factor_252d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 252 days (rolling)."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_YEAR))


def rss_039_cumulative_rs_factor_504d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 504 days."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_2Y))


def rss_040_cumulative_rs_factor_756d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 756 days."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_3Y))


def rss_041_cumulative_rs_factor_expanding(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over entire history (expanding)."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(log_sf.expanding(min_periods=1).sum())


def rss_042_rs_severity_gte10_flag(split_factor: pd.Series) -> pd.Series:
    """1 on days with a reverse split magnitude >= 10 (1-for-10 or worse)."""
    mag = _reverse_split_magnitude(split_factor)
    return (mag >= 10.0).fillna(False).astype(float)


def rss_043_rs_severity_gte5_flag(split_factor: pd.Series) -> pd.Series:
    """1 on days with a reverse split magnitude >= 5 (1-for-5 or worse)."""
    mag = _reverse_split_magnitude(split_factor)
    return (mag >= 5.0).fillna(False).astype(float)


def rss_044_rs_severity_gte20_flag(split_factor: pd.Series) -> pd.Series:
    """1 on days with a reverse split magnitude >= 20 (1-for-20 or worse)."""
    mag = _reverse_split_magnitude(split_factor)
    return (mag >= 20.0).fillna(False).astype(float)


def rss_045_rs_severe_count_504d(split_factor: pd.Series) -> pd.Series:
    """Count of RS events with magnitude >= 10 in trailing 504 days."""
    severe = rss_042_rs_severity_gte10_flag(split_factor)
    return _rolling_sum(severe, _TD_2Y)


# --- Group D (046-060): Nominal price distress (closeunadj sub-threshold flags) ---

def rss_046_closeunadj_below_1_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $1.00 (penny stock threshold)."""
    return (closeunadj < 1.0).astype(float)


def rss_047_closeunadj_below_2_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $2.00."""
    return (closeunadj < 2.0).astype(float)


def rss_048_closeunadj_below_5_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $5.00."""
    return (closeunadj < 5.0).astype(float)


def rss_049_closeunadj_below_10_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $10.00."""
    return (closeunadj < 10.0).astype(float)


def rss_050_days_below_1_count_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $1 in trailing 63 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_QTR)


def rss_051_days_below_1_count_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $1 in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 1.0).astype(float), _TD_YEAR)


def rss_052_days_below_2_count_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $2 in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 2.0).astype(float), _TD_YEAR)


def rss_053_days_below_5_count_252d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $5 in trailing 252 trading days."""
    return _rolling_sum((closeunadj < 5.0).astype(float), _TD_YEAR)


def rss_054_fraction_below_1_63d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1 in trailing 63 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_QTR)


def rss_055_fraction_below_1_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $1 in trailing 252 days."""
    return _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)


def rss_056_fraction_below_2_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $2 in trailing 252 days."""
    return _rolling_mean((closeunadj < 2.0).astype(float), _TD_YEAR)


def rss_057_fraction_below_5_252d(closeunadj: pd.Series) -> pd.Series:
    """Fraction of days below $5 in trailing 252 days."""
    return _rolling_mean((closeunadj < 5.0).astype(float), _TD_YEAR)


def rss_058_consecutive_days_below_1(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days the unadjusted close has been below $1; resets on crossing."""
    below = (closeunadj < 1.0).astype(int)
    streak = np.zeros(len(below), dtype=float)
    arr = below.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=closeunadj.index)


def rss_059_consecutive_days_below_5(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days the unadjusted close has been below $5; resets on crossing."""
    below = (closeunadj < 5.0).astype(int)
    streak = np.zeros(len(below), dtype=float)
    arr = below.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=closeunadj.index)


def rss_060_closeunadj_distance_to_1(closeunadj: pd.Series) -> pd.Series:
    """Signed distance of unadjusted close from $1 threshold (negative = below $1)."""
    return closeunadj - 1.0


# --- Group E (061-075): Price level vs thresholds and interaction with RS events ---

def rss_061_closeunadj_log_price(closeunadj: pd.Series) -> pd.Series:
    """Log of unadjusted close price; captures price-level magnitude on log scale."""
    return np.log(closeunadj.clip(lower=_EPS))


def rss_062_closeunadj_zscore_252d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 252 trading days."""
    return _zscore_rolling(closeunadj, _TD_YEAR)


def rss_063_closeunadj_pct_rank_252d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 252 trading days."""
    return _rolling_rank_pct(closeunadj, _TD_YEAR)


def rss_064_closeunadj_vs_252d_mean(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its 252-day rolling mean."""
    return closeunadj - _rolling_mean(closeunadj, _TD_YEAR)


def rss_065_closeunadj_pct_vs_252d_mean(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close percent deviation from its 252-day rolling mean."""
    avg = _rolling_mean(closeunadj, _TD_YEAR)
    return _safe_div_abs(closeunadj - avg, avg)


def rss_066_rs_flag_and_below1_interaction(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if reverse split occurred AND unadjusted close is below $1 on the same day."""
    return (_is_reverse_split(split_factor) * (closeunadj < 1.0).astype(float))


def rss_067_rs_flag_and_below5_interaction(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if reverse split occurred AND unadjusted close is below $5 on same day."""
    return (_is_reverse_split(split_factor) * (closeunadj < 5.0).astype(float))


def rss_068_closeunadj_min_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of unadjusted close price."""
    return _rolling_min(closeunadj, _TD_YEAR)


def rss_069_closeunadj_drawdown_from_252d_peak(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its 252-day rolling maximum (drawdown from recent peak)."""
    return closeunadj - _rolling_max(closeunadj, _TD_YEAR)


def rss_070_closeunadj_pct_drawdown_252d(closeunadj: pd.Series) -> pd.Series:
    """Percent drawdown of unadjusted close from its 252-day peak."""
    peak = _rolling_max(closeunadj, _TD_YEAR)
    return _safe_div_abs(closeunadj - peak, peak)


def rss_071_close_adj_vs_unadj_ratio(close: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Ratio of adjusted close to unadjusted close; reflects cumulative split adjustment."""
    return _safe_div(close, closeunadj)


def rss_072_close_adj_vs_unadj_log_ratio(close: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Log ratio of adjusted close to unadjusted close."""
    return np.log(_safe_div(close, closeunadj).clip(lower=_EPS))


def rss_073_rs_count_252d_times_below1_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS count in 252 days multiplied by sub-$1 flag; joint distress severity."""
    return rss_019_rs_count_252d(split_factor) * (closeunadj < 1.0).astype(float)


def rss_074_closeunadj_expanding_min(closeunadj: pd.Series) -> pd.Series:
    """Expanding (all-history) minimum of unadjusted close price."""
    return closeunadj.expanding(min_periods=1).min()


def rss_075_closeunadj_pct_above_expanding_min(closeunadj: pd.Series) -> pd.Series:
    """Percent of unadjusted close above its all-time expanding minimum."""
    emin = closeunadj.expanding(min_periods=1).min()
    return _safe_div_abs(closeunadj - emin, emin)


# --- Group K (076-100 in file 001): More price distress, split interaction, and composites ---

def rss_151_closeunadj_below_504d_min_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close just reached a new 504-day low."""
    return (closeunadj <= _rolling_min(closeunadj.shift(1), _TD_2Y)).astype(float)


def rss_152_closeunadj_pct_rank_63d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 63 trading days."""
    return _rolling_rank_pct(closeunadj, _TD_QTR)


def rss_153_closeunadj_pct_rank_126d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 126 trading days."""
    return _rolling_rank_pct(closeunadj, _TD_2Q)


def rss_154_closeunadj_zscore_63d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 63 trading days."""
    return _zscore_rolling(closeunadj, _TD_QTR)


def rss_155_rs_count_126d(split_factor: pd.Series) -> pd.Series:
    """Count of reverse-split days in trailing 126 trading days."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Q)


def rss_156_rs_count_126d_gt1_flag(split_factor: pd.Series) -> pd.Series:
    """1 if more than 1 reverse split occurred in trailing 126 days."""
    return (_rolling_sum(_is_reverse_split(split_factor), _TD_2Q) > 1).astype(float)


def rss_157_rs_magnitude_sum_252d(split_factor: pd.Series) -> pd.Series:
    """Sum of reverse-split magnitudes (1/sf) over trailing 252 days; 0 on non-RS days."""
    mag = _reverse_split_magnitude(split_factor).fillna(0.0)
    return _rolling_sum(mag, _TD_YEAR)


def rss_158_rs_magnitude_sum_504d(split_factor: pd.Series) -> pd.Series:
    """Sum of reverse-split magnitudes over trailing 504 days."""
    mag = _reverse_split_magnitude(split_factor).fillna(0.0)
    return _rolling_sum(mag, _TD_2Y)


def rss_159_rs_magnitude_mean_252d(split_factor: pd.Series) -> pd.Series:
    """Mean RS magnitude (1/sf) over RS days in trailing 252 days; NaN if no RS."""
    mag = _reverse_split_magnitude(split_factor).fillna(0.0)
    rs  = _is_reverse_split(split_factor)
    sum_mag = _rolling_sum(mag, _TD_YEAR)
    cnt     = _rolling_sum(rs, _TD_YEAR)
    return _safe_div(sum_mag, cnt)


def rss_160_cumulative_rs_factor_1260d(split_factor: pd.Series) -> pd.Series:
    """Cumulative product of split_factor over trailing 1260 days (5 years)."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return np.exp(_rolling_sum(log_sf, _TD_5Y))


def rss_161_rs_severity_gte50_flag(split_factor: pd.Series) -> pd.Series:
    """1 on days with a reverse split magnitude >= 50 (1-for-50 or worse)."""
    mag = _reverse_split_magnitude(split_factor)
    return (mag >= 50.0).fillna(False).astype(float)


def rss_162_rs_severe_count_252d(split_factor: pd.Series) -> pd.Series:
    """Count of RS events with magnitude >= 10 in trailing 252 days."""
    severe = (_reverse_split_magnitude(split_factor) >= 10.0).fillna(False).astype(float)
    return _rolling_sum(severe, _TD_YEAR)


def rss_163_fs_count_126d(split_factor: pd.Series) -> pd.Series:
    """Count of forward-split days in trailing 126 trading days."""
    return _rolling_sum(_is_forward_split(split_factor), _TD_2Q)


def rss_164_rs_minus_fs_count_126d(split_factor: pd.Series) -> pd.Series:
    """Reverse-split count minus forward-split count in trailing 126 days."""
    return rss_155_rs_count_126d(split_factor) - rss_163_fs_count_126d(split_factor)


def rss_165_closeunadj_range_504d(closeunadj: pd.Series) -> pd.Series:
    """504-day range (max - min) of unadjusted close."""
    return _rolling_max(closeunadj, _TD_2Y) - _rolling_min(closeunadj, _TD_2Y)


def rss_166_closeunadj_normalized_position_504d(closeunadj: pd.Series) -> pd.Series:
    """Position of close within 504d range: (close - min504) / (max504 - min504)."""
    lo  = _rolling_min(closeunadj, _TD_2Y)
    hi  = _rolling_max(closeunadj, _TD_2Y)
    rng = (hi - lo).replace(0, np.nan)
    return (closeunadj - lo) / rng


def rss_167_closeunadj_pct_drawdown_504d(closeunadj: pd.Series) -> pd.Series:
    """Percent drawdown of unadjusted close from its 504-day rolling peak."""
    peak = _rolling_max(closeunadj, _TD_2Y)
    return _safe_div_abs(closeunadj - peak, peak)


def rss_168_closeunadj_pct_drawdown_expanding(closeunadj: pd.Series) -> pd.Series:
    """Percent drawdown of unadjusted close from its all-history expanding peak."""
    peak = closeunadj.expanding(min_periods=1).max()
    return _safe_div_abs(closeunadj - peak, peak)


def rss_169_consecutive_days_below_2(closeunadj: pd.Series) -> pd.Series:
    """Consecutive trading days unadjusted close has been below $2; resets on crossing."""
    below = (closeunadj < 2.0).astype(int)
    streak = np.zeros(len(below), dtype=float)
    arr = below.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=closeunadj.index)


def rss_170_rs_flag_and_below2_interaction(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if reverse split occurred AND unadjusted close is below $2 on same day."""
    return (_is_reverse_split(split_factor) * (closeunadj < 2.0).astype(float))


def rss_171_closeunadj_median_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day median of unadjusted close."""
    return _rolling_median(closeunadj, _TD_QTR)


def rss_172_closeunadj_below_median_63d_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close is below its 63-day rolling median."""
    return (closeunadj < _rolling_median(closeunadj, _TD_QTR)).astype(float)


def rss_173_rs_count_252d_x_below5_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS count in 252d multiplied by sub-$5 unadjusted close flag."""
    count = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    return count * (closeunadj < 5.0).astype(float)


def rss_174_closeunadj_cv_252d(closeunadj: pd.Series) -> pd.Series:
    """Coefficient of variation of unadjusted close over 252 days (std/mean)."""
    return _safe_div(_rolling_std(closeunadj, _TD_YEAR),
                     _rolling_mean(closeunadj, _TD_YEAR).replace(0, np.nan))


def rss_175_close_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 504 trading days."""
    return _rolling_rank_pct(close, _TD_2Y)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

REVERSE_SPLIT_SIGNAL_REGISTRY_001_075 = {
    "rss_001_reverse_split_flag":                     {"inputs": ["split_factor"],                    "func": rss_001_reverse_split_flag},
    "rss_002_forward_split_flag":                     {"inputs": ["split_factor"],                    "func": rss_002_forward_split_flag},
    "rss_003_split_event_flag":                       {"inputs": ["split_factor"],                    "func": rss_003_split_event_flag},
    "rss_004_days_since_last_reverse_split":          {"inputs": ["split_factor"],                    "func": rss_004_days_since_last_reverse_split},
    "rss_005_reverse_split_within_21d":               {"inputs": ["split_factor"],                    "func": rss_005_reverse_split_within_21d},
    "rss_006_reverse_split_within_63d":               {"inputs": ["split_factor"],                    "func": rss_006_reverse_split_within_63d},
    "rss_007_reverse_split_within_126d":              {"inputs": ["split_factor"],                    "func": rss_007_reverse_split_within_126d},
    "rss_008_reverse_split_within_252d":              {"inputs": ["split_factor"],                    "func": rss_008_reverse_split_within_252d},
    "rss_009_reverse_split_within_504d":              {"inputs": ["split_factor"],                    "func": rss_009_reverse_split_within_504d},
    "rss_010_days_since_last_reverse_split_log":      {"inputs": ["split_factor"],                    "func": rss_010_days_since_last_reverse_split_log},
    "rss_011_days_since_last_forward_split":          {"inputs": ["split_factor"],                    "func": rss_011_days_since_last_forward_split},
    "rss_012_reverse_minus_forward_split_flag":       {"inputs": ["split_factor"],                    "func": rss_012_reverse_minus_forward_split_flag},
    "rss_013_expanding_reverse_split_count":          {"inputs": ["split_factor"],                    "func": rss_013_expanding_reverse_split_count},
    "rss_014_reverse_split_recency_decay":            {"inputs": ["split_factor"],                    "func": rss_014_reverse_split_recency_decay},
    "rss_015_reverse_split_recency_decay_slow":       {"inputs": ["split_factor"],                    "func": rss_015_reverse_split_recency_decay_slow},
    "rss_016_rs_count_21d":                           {"inputs": ["split_factor"],                    "func": rss_016_rs_count_21d},
    "rss_017_rs_count_63d":                           {"inputs": ["split_factor"],                    "func": rss_017_rs_count_63d},
    "rss_018_rs_count_126d":                          {"inputs": ["split_factor"],                    "func": rss_018_rs_count_126d},
    "rss_019_rs_count_252d":                          {"inputs": ["split_factor"],                    "func": rss_019_rs_count_252d},
    "rss_020_rs_count_504d":                          {"inputs": ["split_factor"],                    "func": rss_020_rs_count_504d},
    "rss_021_rs_count_756d":                          {"inputs": ["split_factor"],                    "func": rss_021_rs_count_756d},
    "rss_022_rs_count_1260d":                         {"inputs": ["split_factor"],                    "func": rss_022_rs_count_1260d},
    "rss_023_fs_count_252d":                          {"inputs": ["split_factor"],                    "func": rss_023_fs_count_252d},
    "rss_024_rs_minus_fs_count_252d":                 {"inputs": ["split_factor"],                    "func": rss_024_rs_minus_fs_count_252d},
    "rss_025_rs_count_252d_gt1_flag":                 {"inputs": ["split_factor"],                    "func": rss_025_rs_count_252d_gt1_flag},
    "rss_026_rs_count_504d_gt2_flag":                 {"inputs": ["split_factor"],                    "func": rss_026_rs_count_504d_gt2_flag},
    "rss_027_rs_count_expanding_gt0_flag":            {"inputs": ["split_factor"],                    "func": rss_027_rs_count_expanding_gt0_flag},
    "rss_028_rs_cluster_density_63d":                 {"inputs": ["split_factor"],                    "func": rss_028_rs_cluster_density_63d},
    "rss_029_rs_cluster_density_252d":                {"inputs": ["split_factor"],                    "func": rss_029_rs_cluster_density_252d},
    "rss_030_rs_acceleration_63d_vs_252d":            {"inputs": ["split_factor"],                    "func": rss_030_rs_acceleration_63d_vs_252d},
    "rss_031_rs_magnitude_current":                   {"inputs": ["split_factor"],                    "func": rss_031_rs_magnitude_current},
    "rss_032_rs_log_magnitude_current":               {"inputs": ["split_factor"],                    "func": rss_032_rs_log_magnitude_current},
    "rss_033_rs_magnitude_max_21d":                   {"inputs": ["split_factor"],                    "func": rss_033_rs_magnitude_max_21d},
    "rss_034_rs_magnitude_max_63d":                   {"inputs": ["split_factor"],                    "func": rss_034_rs_magnitude_max_63d},
    "rss_035_rs_magnitude_max_252d":                  {"inputs": ["split_factor"],                    "func": rss_035_rs_magnitude_max_252d},
    "rss_036_rs_magnitude_max_504d":                  {"inputs": ["split_factor"],                    "func": rss_036_rs_magnitude_max_504d},
    "rss_037_rs_magnitude_max_expanding":             {"inputs": ["split_factor"],                    "func": rss_037_rs_magnitude_max_expanding},
    "rss_038_cumulative_rs_factor_252d":              {"inputs": ["split_factor"],                    "func": rss_038_cumulative_rs_factor_252d},
    "rss_039_cumulative_rs_factor_504d":              {"inputs": ["split_factor"],                    "func": rss_039_cumulative_rs_factor_504d},
    "rss_040_cumulative_rs_factor_756d":              {"inputs": ["split_factor"],                    "func": rss_040_cumulative_rs_factor_756d},
    "rss_041_cumulative_rs_factor_expanding":         {"inputs": ["split_factor"],                    "func": rss_041_cumulative_rs_factor_expanding},
    "rss_042_rs_severity_gte10_flag":                 {"inputs": ["split_factor"],                    "func": rss_042_rs_severity_gte10_flag},
    "rss_043_rs_severity_gte5_flag":                  {"inputs": ["split_factor"],                    "func": rss_043_rs_severity_gte5_flag},
    "rss_044_rs_severity_gte20_flag":                 {"inputs": ["split_factor"],                    "func": rss_044_rs_severity_gte20_flag},
    "rss_045_rs_severe_count_504d":                   {"inputs": ["split_factor"],                    "func": rss_045_rs_severe_count_504d},
    "rss_046_closeunadj_below_1_flag":                {"inputs": ["closeunadj"],                      "func": rss_046_closeunadj_below_1_flag},
    "rss_047_closeunadj_below_2_flag":                {"inputs": ["closeunadj"],                      "func": rss_047_closeunadj_below_2_flag},
    "rss_048_closeunadj_below_5_flag":                {"inputs": ["closeunadj"],                      "func": rss_048_closeunadj_below_5_flag},
    "rss_049_closeunadj_below_10_flag":               {"inputs": ["closeunadj"],                      "func": rss_049_closeunadj_below_10_flag},
    "rss_050_days_below_1_count_63d":                 {"inputs": ["closeunadj"],                      "func": rss_050_days_below_1_count_63d},
    "rss_051_days_below_1_count_252d":                {"inputs": ["closeunadj"],                      "func": rss_051_days_below_1_count_252d},
    "rss_052_days_below_2_count_252d":                {"inputs": ["closeunadj"],                      "func": rss_052_days_below_2_count_252d},
    "rss_053_days_below_5_count_252d":                {"inputs": ["closeunadj"],                      "func": rss_053_days_below_5_count_252d},
    "rss_054_fraction_below_1_63d":                   {"inputs": ["closeunadj"],                      "func": rss_054_fraction_below_1_63d},
    "rss_055_fraction_below_1_252d":                  {"inputs": ["closeunadj"],                      "func": rss_055_fraction_below_1_252d},
    "rss_056_fraction_below_2_252d":                  {"inputs": ["closeunadj"],                      "func": rss_056_fraction_below_2_252d},
    "rss_057_fraction_below_5_252d":                  {"inputs": ["closeunadj"],                      "func": rss_057_fraction_below_5_252d},
    "rss_058_consecutive_days_below_1":               {"inputs": ["closeunadj"],                      "func": rss_058_consecutive_days_below_1},
    "rss_059_consecutive_days_below_5":               {"inputs": ["closeunadj"],                      "func": rss_059_consecutive_days_below_5},
    "rss_060_closeunadj_distance_to_1":               {"inputs": ["closeunadj"],                      "func": rss_060_closeunadj_distance_to_1},
    "rss_061_closeunadj_log_price":                   {"inputs": ["closeunadj"],                      "func": rss_061_closeunadj_log_price},
    "rss_062_closeunadj_zscore_252d":                 {"inputs": ["closeunadj"],                      "func": rss_062_closeunadj_zscore_252d},
    "rss_063_closeunadj_pct_rank_252d":               {"inputs": ["closeunadj"],                      "func": rss_063_closeunadj_pct_rank_252d},
    "rss_064_closeunadj_vs_252d_mean":                {"inputs": ["closeunadj"],                      "func": rss_064_closeunadj_vs_252d_mean},
    "rss_065_closeunadj_pct_vs_252d_mean":            {"inputs": ["closeunadj"],                      "func": rss_065_closeunadj_pct_vs_252d_mean},
    "rss_066_rs_flag_and_below1_interaction":         {"inputs": ["split_factor", "closeunadj"],      "func": rss_066_rs_flag_and_below1_interaction},
    "rss_067_rs_flag_and_below5_interaction":         {"inputs": ["split_factor", "closeunadj"],      "func": rss_067_rs_flag_and_below5_interaction},
    "rss_068_closeunadj_min_252d":                    {"inputs": ["closeunadj"],                      "func": rss_068_closeunadj_min_252d},
    "rss_069_closeunadj_drawdown_from_252d_peak":     {"inputs": ["closeunadj"],                      "func": rss_069_closeunadj_drawdown_from_252d_peak},
    "rss_070_closeunadj_pct_drawdown_252d":           {"inputs": ["closeunadj"],                      "func": rss_070_closeunadj_pct_drawdown_252d},
    "rss_071_close_adj_vs_unadj_ratio":               {"inputs": ["close", "closeunadj"],             "func": rss_071_close_adj_vs_unadj_ratio},
    "rss_072_close_adj_vs_unadj_log_ratio":           {"inputs": ["close", "closeunadj"],             "func": rss_072_close_adj_vs_unadj_log_ratio},
    "rss_073_rs_count_252d_times_below1_flag":        {"inputs": ["split_factor", "closeunadj"],      "func": rss_073_rs_count_252d_times_below1_flag},
    "rss_074_closeunadj_expanding_min":               {"inputs": ["closeunadj"],                      "func": rss_074_closeunadj_expanding_min},
    "rss_075_closeunadj_pct_above_expanding_min":     {"inputs": ["closeunadj"],                      "func": rss_075_closeunadj_pct_above_expanding_min},
    "rss_151_closeunadj_below_504d_min_flag":         {"inputs": ["closeunadj"],                      "func": rss_151_closeunadj_below_504d_min_flag},
    "rss_152_closeunadj_pct_rank_63d":                {"inputs": ["closeunadj"],                      "func": rss_152_closeunadj_pct_rank_63d},
    "rss_153_closeunadj_pct_rank_126d":               {"inputs": ["closeunadj"],                      "func": rss_153_closeunadj_pct_rank_126d},
    "rss_154_closeunadj_zscore_63d":                  {"inputs": ["closeunadj"],                      "func": rss_154_closeunadj_zscore_63d},
    "rss_155_rs_count_126d":                          {"inputs": ["split_factor"],                    "func": rss_155_rs_count_126d},
    "rss_156_rs_count_126d_gt1_flag":                 {"inputs": ["split_factor"],                    "func": rss_156_rs_count_126d_gt1_flag},
    "rss_157_rs_magnitude_sum_252d":                  {"inputs": ["split_factor"],                    "func": rss_157_rs_magnitude_sum_252d},
    "rss_158_rs_magnitude_sum_504d":                  {"inputs": ["split_factor"],                    "func": rss_158_rs_magnitude_sum_504d},
    "rss_159_rs_magnitude_mean_252d":                 {"inputs": ["split_factor"],                    "func": rss_159_rs_magnitude_mean_252d},
    "rss_160_cumulative_rs_factor_1260d":             {"inputs": ["split_factor"],                    "func": rss_160_cumulative_rs_factor_1260d},
    "rss_161_rs_severity_gte50_flag":                 {"inputs": ["split_factor"],                    "func": rss_161_rs_severity_gte50_flag},
    "rss_162_rs_severe_count_252d":                   {"inputs": ["split_factor"],                    "func": rss_162_rs_severe_count_252d},
    "rss_163_fs_count_126d":                          {"inputs": ["split_factor"],                    "func": rss_163_fs_count_126d},
    "rss_164_rs_minus_fs_count_126d":                 {"inputs": ["split_factor"],                    "func": rss_164_rs_minus_fs_count_126d},
    "rss_165_closeunadj_range_504d":                  {"inputs": ["closeunadj"],                      "func": rss_165_closeunadj_range_504d},
    "rss_166_closeunadj_normalized_position_504d":    {"inputs": ["closeunadj"],                      "func": rss_166_closeunadj_normalized_position_504d},
    "rss_167_closeunadj_pct_drawdown_504d":           {"inputs": ["closeunadj"],                      "func": rss_167_closeunadj_pct_drawdown_504d},
    "rss_168_closeunadj_pct_drawdown_expanding":      {"inputs": ["closeunadj"],                      "func": rss_168_closeunadj_pct_drawdown_expanding},
    "rss_169_consecutive_days_below_2":               {"inputs": ["closeunadj"],                      "func": rss_169_consecutive_days_below_2},
    "rss_170_rs_flag_and_below2_interaction":         {"inputs": ["split_factor", "closeunadj"],      "func": rss_170_rs_flag_and_below2_interaction},
    "rss_171_closeunadj_median_63d":                  {"inputs": ["closeunadj"],                      "func": rss_171_closeunadj_median_63d},
    "rss_172_closeunadj_below_median_63d_flag":       {"inputs": ["closeunadj"],                      "func": rss_172_closeunadj_below_median_63d_flag},
    "rss_173_rs_count_252d_x_below5_flag":            {"inputs": ["split_factor", "closeunadj"],      "func": rss_173_rs_count_252d_x_below5_flag},
    "rss_174_closeunadj_cv_252d":                     {"inputs": ["closeunadj"],                      "func": rss_174_closeunadj_cv_252d},
    "rss_175_close_pct_rank_504d":                    {"inputs": ["close"],                           "func": rss_175_close_pct_rank_504d},
}
