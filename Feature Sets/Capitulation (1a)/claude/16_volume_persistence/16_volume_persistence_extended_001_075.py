"""
16_volume_persistence — Extended Features 001-075
Domain: sustained elevated volume — multi-day aggregates and volume-above-MA duration.
Fills gaps NOT covered by the 200 base/derivative features:
  (A) Rolling SUM of volume over 3/5/10/21/63 days, that sum vs its own trailing
      baseline; multi-day dollar-volume aggregates; ratio of recent-window volume
      sum to a longer-window average.
  (B) Count and fraction of days in a window with volume above its MA (21/63/252);
      current consecutive run above the volume MA; longest such run in a window;
      time-since volume last dropped below its MA; fraction of a window elevated.
  (C) Volume persistence autocorrelation (clustering), EWM-vs-SMA spread,
      sustained-elevated-volume intensity scores, above-median persistence,
      volume-plateau detection, and rates-of-change of these.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (raw apply, safe)."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _days_since_false(cond: pd.Series) -> pd.Series:
    """Number of days since cond was last False (i.e. since last drop below threshold).
    Returns 0 on days where cond is False; counts up on True days since last False."""
    c = cond.astype(int)
    # Use cumsum-group trick: within each True-run, index within run
    group = (~cond).cumsum()
    since = c.groupby(group).cumsum()
    return since.astype(float)


# ── Group A (001-015): Rolling SUM of volume vs its own baseline ──────────────

def vp_ext_001_vol_sum_3d(volume: pd.Series) -> pd.Series:
    """Rolling 3-day sum of raw volume (multi-day aggregate)."""
    return _rolling_sum(volume, 3)


def vp_ext_002_vol_sum_5d(volume: pd.Series) -> pd.Series:
    """Rolling 5-day sum of raw volume."""
    return _rolling_sum(volume, _TD_WEEK)


def vp_ext_003_vol_sum_10d(volume: pd.Series) -> pd.Series:
    """Rolling 10-day sum of raw volume."""
    return _rolling_sum(volume, 10)


def vp_ext_004_vol_sum_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day sum of raw volume."""
    return _rolling_sum(volume, _TD_MON)


def vp_ext_005_vol_sum_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day sum of raw volume."""
    return _rolling_sum(volume, _TD_QTR)


def vp_ext_006_vol_sum_3d_vs_63d_baseline(volume: pd.Series) -> pd.Series:
    """3-day volume sum divided by its own 63-day trailing average (short burst vs norm)."""
    s3 = _rolling_sum(volume, 3)
    base = _rolling_mean(s3, _TD_QTR)
    return _safe_div(s3, base)


def vp_ext_007_vol_sum_5d_vs_63d_baseline(volume: pd.Series) -> pd.Series:
    """5-day volume sum divided by its own 63-day trailing average."""
    s5 = _rolling_sum(volume, _TD_WEEK)
    base = _rolling_mean(s5, _TD_QTR)
    return _safe_div(s5, base)


def vp_ext_008_vol_sum_10d_vs_63d_baseline(volume: pd.Series) -> pd.Series:
    """10-day volume sum divided by its own 63-day trailing average."""
    s10 = _rolling_sum(volume, 10)
    base = _rolling_mean(s10, _TD_QTR)
    return _safe_div(s10, base)


def vp_ext_009_vol_sum_21d_vs_252d_baseline(volume: pd.Series) -> pd.Series:
    """21-day volume sum divided by its own 252-day trailing average."""
    s21 = _rolling_sum(volume, _TD_MON)
    base = _rolling_mean(s21, _TD_YEAR)
    return _safe_div(s21, base)


def vp_ext_010_vol_sum_63d_vs_252d_baseline(volume: pd.Series) -> pd.Series:
    """63-day volume sum divided by its own 252-day trailing average."""
    s63 = _rolling_sum(volume, _TD_QTR)
    base = _rolling_mean(s63, _TD_YEAR)
    return _safe_div(s63, base)


def vp_ext_011_vol_sum_5d_vs_252d_mean_daily(volume: pd.Series) -> pd.Series:
    """5-day volume sum divided by 252-day mean daily volume (normalized burst)."""
    s5 = _rolling_sum(volume, _TD_WEEK)
    mean_daily = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(s5, mean_daily * _TD_WEEK)


def vp_ext_012_vol_sum_21d_vs_expected_63d(volume: pd.Series) -> pd.Series:
    """21-day vol sum vs expected 21-day sum from 63-day run rate (cumulative vs expected)."""
    s21 = _rolling_sum(volume, _TD_MON)
    expected = _rolling_mean(volume, _TD_QTR) * _TD_MON
    return _safe_div(s21, expected)


def vp_ext_013_vol_sum_10d_ratio_to_126d_avg_daily(volume: pd.Series) -> pd.Series:
    """10-day volume sum divided by 10x 126-day average daily volume."""
    s10 = _rolling_sum(volume, 10)
    expected = _rolling_mean(volume, _TD_HALF) * 10
    return _safe_div(s10, expected)


def vp_ext_014_vol_sum_3d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 3-day volume sum within its trailing 252-day distribution."""
    s3 = _rolling_sum(volume, 3)
    m = _rolling_mean(s3, _TD_YEAR)
    s = _rolling_std(s3, _TD_YEAR)
    return _safe_div(s3 - m, s)


def vp_ext_015_vol_sum_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume sum within its trailing 252-day distribution."""
    s21 = _rolling_sum(volume, _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    return _safe_div(s21 - m, s)


# ── Group B (016-025): Multi-day dollar-volume aggregates ─────────────────────

def vp_ext_016_dollar_vol_sum_3d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 3-day sum of dollar volume (close * volume)."""
    dv = close * volume
    return _rolling_sum(dv, 3)


def vp_ext_017_dollar_vol_sum_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 5-day sum of dollar volume."""
    dv = close * volume
    return _rolling_sum(dv, _TD_WEEK)


def vp_ext_018_dollar_vol_sum_10d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 10-day sum of dollar volume."""
    dv = close * volume
    return _rolling_sum(dv, 10)


def vp_ext_019_dollar_vol_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day sum of dollar volume."""
    dv = close * volume
    return _rolling_sum(dv, _TD_MON)


def vp_ext_020_dollar_vol_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day sum of dollar volume."""
    dv = close * volume
    return _rolling_sum(dv, _TD_QTR)


def vp_ext_021_dollar_vol_sum_5d_vs_63d_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day dollar-volume sum divided by its own 63-day trailing average."""
    dv = close * volume
    s5 = _rolling_sum(dv, _TD_WEEK)
    base = _rolling_mean(s5, _TD_QTR)
    return _safe_div(s5, base)


def vp_ext_022_dollar_vol_sum_21d_vs_252d_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day dollar-volume sum divided by its own 252-day trailing average."""
    dv = close * volume
    s21 = _rolling_sum(dv, _TD_MON)
    base = _rolling_mean(s21, _TD_YEAR)
    return _safe_div(s21, base)


def vp_ext_023_dollar_vol_sum_10d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 10-day dollar-volume sum within trailing 252-day distribution."""
    dv = close * volume
    s10 = _rolling_sum(dv, 10)
    m = _rolling_mean(s10, _TD_YEAR)
    s = _rolling_std(s10, _TD_YEAR)
    return _safe_div(s10 - m, s)


def vp_ext_024_dollar_vol_sum_5d_vs_21d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day dollar-volume sum to 21-day dollar-volume sum (burst fraction)."""
    dv = close * volume
    s5 = _rolling_sum(dv, _TD_WEEK)
    s21 = _rolling_sum(dv, _TD_MON)
    return _safe_div(s5 * (_TD_MON / _TD_WEEK), s21)


def vp_ext_025_dollar_vol_sum_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day dollar-volume sum within trailing 252-day distribution."""
    dv = close * volume
    s63 = _rolling_sum(dv, _TD_QTR)
    return s63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Group C (026-040): Volume-above-MA duration: count and fraction ───────────

def vp_ext_026_vol_above_ma21_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where volume > its own 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_MON)


def vp_ext_027_vol_above_ma21_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume > its own 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_QTR)


def vp_ext_028_vol_above_ma21_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume > its own 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_YEAR)


def vp_ext_029_vol_above_ma63_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume > its own 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _rolling_count_true(cond, _TD_QTR)


def vp_ext_030_vol_above_ma63_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume > its own 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _rolling_count_true(cond, _TD_YEAR)


def vp_ext_031_vol_above_ma252_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume > its own 252-day SMA."""
    ma252 = _rolling_mean(volume, _TD_YEAR)
    cond = volume > ma252
    return _rolling_count_true(cond, _TD_YEAR)


def vp_ext_032_vol_above_ma21_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 21d with volume > 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vp_ext_033_vol_above_ma21_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with volume > 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_ext_034_vol_above_ma63_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with volume > 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_ext_035_vol_above_ma252_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d with volume > 252-day SMA."""
    ma252 = _rolling_mean(volume, _TD_YEAR)
    cond = volume > ma252
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_ext_036_vol_above_ma21_fraction_126d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 126d with volume > 21-day SMA."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


def vp_ext_037_vol_above_ma63_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d with volume > 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_ext_038_vol_above_ma21_count_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day vol-above-MA21 count within 252-day distribution."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    cnt = _rolling_count_true(cond, _TD_QTR)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def vp_ext_039_vol_above_ma63_count_252d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 252-day vol-above-MA63 count (within expanding distribution)."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    cnt = _rolling_count_true(cond, _TD_YEAR)
    m = cnt.expanding(min_periods=20).mean()
    s = cnt.expanding(min_periods=20).std()
    return _safe_div(cnt - m, s)


def vp_ext_040_vol_above_ma21_fraction_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day vol-above-MA21 fraction within 252-day window."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Group D (041-052): Current consec run above MA & longest run ──────────────

def vp_ext_041_consec_days_above_ma21(volume: pd.Series) -> pd.Series:
    """Current consecutive run of days with volume > 21-day SMA (distinct from base: uses SMA directly)."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _consec_streak(cond)


def vp_ext_042_consec_days_above_ma63(volume: pd.Series) -> pd.Series:
    """Current consecutive run of days with volume > 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _consec_streak(cond)


def vp_ext_043_consec_days_above_ma252(volume: pd.Series) -> pd.Series:
    """Current consecutive run of days with volume > 252-day SMA."""
    ma252 = _rolling_mean(volume, _TD_YEAR)
    cond = volume > ma252
    return _consec_streak(cond)


def vp_ext_044_longest_run_above_ma21_in_63d(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of volume > MA21 within trailing 63 days."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_max_streak(cond, _TD_QTR)


def vp_ext_045_longest_run_above_ma21_in_252d(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of volume > MA21 within trailing 252 days."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_ext_046_longest_run_above_ma63_in_252d(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of volume > MA63 within trailing 252 days."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_ext_047_longest_run_above_ma252_in_252d(volume: pd.Series) -> pd.Series:
    """Longest consecutive run of volume > MA252 within trailing 252 days."""
    ma252 = _rolling_mean(volume, _TD_YEAR)
    cond = volume > ma252
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_ext_048_consec_above_ma21_vs_longest_63d(volume: pd.Series) -> pd.Series:
    """Current run above MA21 as fraction of longest such run in trailing 63 days."""
    cur = vp_ext_041_consec_days_above_ma21(volume)
    mx = vp_ext_044_longest_run_above_ma21_in_63d(volume)
    return _safe_div(cur, mx)


def vp_ext_049_consec_above_ma63_vs_longest_252d(volume: pd.Series) -> pd.Series:
    """Current run above MA63 as fraction of longest such run in trailing 252 days."""
    cur = vp_ext_042_consec_days_above_ma63(volume)
    mx = vp_ext_046_longest_run_above_ma63_in_252d(volume)
    return _safe_div(cur, mx)


def vp_ext_050_consec_above_ma21_log(volume: pd.Series) -> pd.Series:
    """Log1p of current consecutive run above MA21 (tail compression)."""
    return np.log1p(vp_ext_041_consec_days_above_ma21(volume))


def vp_ext_051_consec_above_ma63_log(volume: pd.Series) -> pd.Series:
    """Log1p of current consecutive run above MA63."""
    return np.log1p(vp_ext_042_consec_days_above_ma63(volume))


def vp_ext_052_longest_run_above_ma21_in_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day longest above-MA21 run within 252-day distribution."""
    mx = vp_ext_044_longest_run_above_ma21_in_63d(volume)
    m = _rolling_mean(mx, _TD_YEAR)
    s = _rolling_std(mx, _TD_YEAR)
    return _safe_div(mx - m, s)


# ── Group E (053-062): Time-since volume dropped below its MA ─────────────────

def vp_ext_053_days_since_below_ma21(volume: pd.Series) -> pd.Series:
    """Days since volume last dropped below its 21-day SMA (0 on drop-below days)."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    return _days_since_false(cond)


def vp_ext_054_days_since_below_ma63(volume: pd.Series) -> pd.Series:
    """Days since volume last dropped below its 63-day SMA."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    return _days_since_false(cond)


def vp_ext_055_days_since_below_ma252(volume: pd.Series) -> pd.Series:
    """Days since volume last dropped below its 252-day SMA."""
    ma252 = _rolling_mean(volume, _TD_YEAR)
    cond = volume > ma252
    return _days_since_false(cond)


def vp_ext_056_days_since_below_ma21_log(volume: pd.Series) -> pd.Series:
    """Log1p of days since last below-MA21 event (compresses long continuous runs)."""
    return np.log1p(vp_ext_053_days_since_below_ma21(volume))


def vp_ext_057_days_since_below_ma63_log(volume: pd.Series) -> pd.Series:
    """Log1p of days since last below-MA63 event."""
    return np.log1p(vp_ext_054_days_since_below_ma63(volume))


def vp_ext_058_days_since_below_ma21_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of days-since-below-MA21 within trailing 252-day distribution."""
    since = vp_ext_053_days_since_below_ma21(volume)
    return since.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_ext_059_days_since_below_ma63_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of days-since-below-MA63 within trailing 252-day distribution."""
    since = vp_ext_054_days_since_below_ma63(volume)
    return since.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_ext_060_days_since_below_ma21_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of days-since-below-MA21 within trailing 252-day distribution."""
    since = vp_ext_053_days_since_below_ma21(volume)
    m = _rolling_mean(since, _TD_YEAR)
    s = _rolling_std(since, _TD_YEAR)
    return _safe_div(since - m, s)


def vp_ext_061_vol_above_ma21_run_normalized_by_hist_max(volume: pd.Series) -> pd.Series:
    """Current run above MA21 divided by trailing 252-day max run above MA21."""
    cur = vp_ext_041_consec_days_above_ma21(volume)
    mx252 = vp_ext_045_longest_run_above_ma21_in_252d(volume)
    return _safe_div(cur, mx252)


def vp_ext_062_vol_above_ma63_run_normalized_by_hist_max(volume: pd.Series) -> pd.Series:
    """Current run above MA63 divided by trailing 252-day max run above MA63."""
    cur = vp_ext_042_consec_days_above_ma63(volume)
    mx252 = vp_ext_046_longest_run_above_ma63_in_252d(volume)
    return _safe_div(cur, mx252)


# ── Group F (063-075): Deeper signal: autocorr, EWM-SMA spread,
#    above-median persistence, plateau, RoC ────────────────────────────────────

def vp_ext_063_vol_above_median_count_21d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where volume > 21-day rolling median."""
    med21 = _rolling_median(volume, _TD_MON)
    cond = volume > med21
    return _rolling_count_true(cond, _TD_MON)


def vp_ext_064_vol_above_median_count_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where volume > 63-day rolling median."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond = volume > med63
    return _rolling_count_true(cond, _TD_QTR)


def vp_ext_065_vol_above_median_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63d with volume > 63-day rolling median."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond = volume > med63
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_ext_066_vol_above_median_consec_run(volume: pd.Series) -> pd.Series:
    """Current consecutive run of days with volume > 21-day rolling median."""
    med21 = _rolling_median(volume, _TD_MON)
    cond = volume > med21
    return _consec_streak(cond)


def vp_ext_067_vol_ewm21_minus_sma21(volume: pd.Series) -> pd.Series:
    """Spread: 21-day EMA minus 21-day SMA of volume (EWM recency bias vs SMA)."""
    ewm21 = _ewm_mean(volume, _TD_MON)
    sma21 = _rolling_mean(volume, _TD_MON)
    return ewm21 - sma21


def vp_ext_068_vol_ewm63_minus_sma63(volume: pd.Series) -> pd.Series:
    """Spread: 63-day EMA minus 63-day SMA of volume."""
    ewm63 = _ewm_mean(volume, _TD_QTR)
    sma63 = _rolling_mean(volume, _TD_QTR)
    return ewm63 - sma63


def vp_ext_069_vol_ewm21_sma21_spread_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of (EMA21 - SMA21) spread within trailing 252-day distribution."""
    spread = vp_ext_067_vol_ewm21_minus_sma21(volume)
    m = _rolling_mean(spread, _TD_YEAR)
    s = _rolling_std(spread, _TD_YEAR)
    return _safe_div(spread - m, s)


def vp_ext_070_vol_plateau_score_21d(volume: pd.Series) -> pd.Series:
    """Volume plateau score: 1 - (std/mean) of volume over 21 days (high = flat-high vol)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    cv = _safe_div(s, m)
    return (1.0 - cv.clip(upper=1.0)).clip(lower=0.0)


def vp_ext_071_vol_plateau_score_63d(volume: pd.Series) -> pd.Series:
    """Volume plateau score: 1 - (std/mean) of volume over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    cv = _safe_div(s, m)
    return (1.0 - cv.clip(upper=1.0)).clip(lower=0.0)


def vp_ext_072_vol_sum_5d_roc_21d(volume: pd.Series) -> pd.Series:
    """Rate-of-change of 5-day volume sum over 21 days (21d diff of rolling 5d sum)."""
    s5 = _rolling_sum(volume, _TD_WEEK)
    return s5.diff(_TD_MON)


def vp_ext_073_vol_above_ma21_fraction_21d_roc_21d(volume: pd.Series) -> pd.Series:
    """21-day rate-of-change of 21d vol-above-MA21 fraction."""
    ma21 = _rolling_mean(volume, _TD_MON)
    cond = volume > ma21
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_MON)


def vp_ext_074_vol_above_ma63_fraction_63d_roc_21d(volume: pd.Series) -> pd.Series:
    """21-day rate-of-change of 63d vol-above-MA63 fraction."""
    ma63 = _rolling_mean(volume, _TD_QTR)
    cond = volume > ma63
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vp_ext_075_vol_sum_21d_vs_63d_avg_sum_ratio(volume: pd.Series) -> pd.Series:
    """21-day volume sum divided by the 63-day average of the 21-day rolling sum
    (recent window sum vs longer-window average — the canonical missing metric)."""
    s21 = _rolling_sum(volume, _TD_MON)
    avg63_of_s21 = _rolling_mean(s21, _TD_QTR)
    return _safe_div(s21, avg63_of_s21)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PERSISTENCE_EXTENDED_REGISTRY_001_075 = {
    "vp_ext_001_vol_sum_3d": {"inputs": ["volume"], "func": vp_ext_001_vol_sum_3d},
    "vp_ext_002_vol_sum_5d": {"inputs": ["volume"], "func": vp_ext_002_vol_sum_5d},
    "vp_ext_003_vol_sum_10d": {"inputs": ["volume"], "func": vp_ext_003_vol_sum_10d},
    "vp_ext_004_vol_sum_21d": {"inputs": ["volume"], "func": vp_ext_004_vol_sum_21d},
    "vp_ext_005_vol_sum_63d": {"inputs": ["volume"], "func": vp_ext_005_vol_sum_63d},
    "vp_ext_006_vol_sum_3d_vs_63d_baseline": {"inputs": ["volume"], "func": vp_ext_006_vol_sum_3d_vs_63d_baseline},
    "vp_ext_007_vol_sum_5d_vs_63d_baseline": {"inputs": ["volume"], "func": vp_ext_007_vol_sum_5d_vs_63d_baseline},
    "vp_ext_008_vol_sum_10d_vs_63d_baseline": {"inputs": ["volume"], "func": vp_ext_008_vol_sum_10d_vs_63d_baseline},
    "vp_ext_009_vol_sum_21d_vs_252d_baseline": {"inputs": ["volume"], "func": vp_ext_009_vol_sum_21d_vs_252d_baseline},
    "vp_ext_010_vol_sum_63d_vs_252d_baseline": {"inputs": ["volume"], "func": vp_ext_010_vol_sum_63d_vs_252d_baseline},
    "vp_ext_011_vol_sum_5d_vs_252d_mean_daily": {"inputs": ["volume"], "func": vp_ext_011_vol_sum_5d_vs_252d_mean_daily},
    "vp_ext_012_vol_sum_21d_vs_expected_63d": {"inputs": ["volume"], "func": vp_ext_012_vol_sum_21d_vs_expected_63d},
    "vp_ext_013_vol_sum_10d_ratio_to_126d_avg_daily": {"inputs": ["volume"], "func": vp_ext_013_vol_sum_10d_ratio_to_126d_avg_daily},
    "vp_ext_014_vol_sum_3d_zscore_252d": {"inputs": ["volume"], "func": vp_ext_014_vol_sum_3d_zscore_252d},
    "vp_ext_015_vol_sum_21d_zscore_252d": {"inputs": ["volume"], "func": vp_ext_015_vol_sum_21d_zscore_252d},
    "vp_ext_016_dollar_vol_sum_3d": {"inputs": ["close", "volume"], "func": vp_ext_016_dollar_vol_sum_3d},
    "vp_ext_017_dollar_vol_sum_5d": {"inputs": ["close", "volume"], "func": vp_ext_017_dollar_vol_sum_5d},
    "vp_ext_018_dollar_vol_sum_10d": {"inputs": ["close", "volume"], "func": vp_ext_018_dollar_vol_sum_10d},
    "vp_ext_019_dollar_vol_sum_21d": {"inputs": ["close", "volume"], "func": vp_ext_019_dollar_vol_sum_21d},
    "vp_ext_020_dollar_vol_sum_63d": {"inputs": ["close", "volume"], "func": vp_ext_020_dollar_vol_sum_63d},
    "vp_ext_021_dollar_vol_sum_5d_vs_63d_baseline": {"inputs": ["close", "volume"], "func": vp_ext_021_dollar_vol_sum_5d_vs_63d_baseline},
    "vp_ext_022_dollar_vol_sum_21d_vs_252d_baseline": {"inputs": ["close", "volume"], "func": vp_ext_022_dollar_vol_sum_21d_vs_252d_baseline},
    "vp_ext_023_dollar_vol_sum_10d_zscore_252d": {"inputs": ["close", "volume"], "func": vp_ext_023_dollar_vol_sum_10d_zscore_252d},
    "vp_ext_024_dollar_vol_sum_5d_vs_21d_ratio": {"inputs": ["close", "volume"], "func": vp_ext_024_dollar_vol_sum_5d_vs_21d_ratio},
    "vp_ext_025_dollar_vol_sum_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vp_ext_025_dollar_vol_sum_63d_pct_rank_252d},
    "vp_ext_026_vol_above_ma21_count_21d": {"inputs": ["volume"], "func": vp_ext_026_vol_above_ma21_count_21d},
    "vp_ext_027_vol_above_ma21_count_63d": {"inputs": ["volume"], "func": vp_ext_027_vol_above_ma21_count_63d},
    "vp_ext_028_vol_above_ma21_count_252d": {"inputs": ["volume"], "func": vp_ext_028_vol_above_ma21_count_252d},
    "vp_ext_029_vol_above_ma63_count_63d": {"inputs": ["volume"], "func": vp_ext_029_vol_above_ma63_count_63d},
    "vp_ext_030_vol_above_ma63_count_252d": {"inputs": ["volume"], "func": vp_ext_030_vol_above_ma63_count_252d},
    "vp_ext_031_vol_above_ma252_count_252d": {"inputs": ["volume"], "func": vp_ext_031_vol_above_ma252_count_252d},
    "vp_ext_032_vol_above_ma21_fraction_21d": {"inputs": ["volume"], "func": vp_ext_032_vol_above_ma21_fraction_21d},
    "vp_ext_033_vol_above_ma21_fraction_63d": {"inputs": ["volume"], "func": vp_ext_033_vol_above_ma21_fraction_63d},
    "vp_ext_034_vol_above_ma63_fraction_63d": {"inputs": ["volume"], "func": vp_ext_034_vol_above_ma63_fraction_63d},
    "vp_ext_035_vol_above_ma252_fraction_252d": {"inputs": ["volume"], "func": vp_ext_035_vol_above_ma252_fraction_252d},
    "vp_ext_036_vol_above_ma21_fraction_126d": {"inputs": ["volume"], "func": vp_ext_036_vol_above_ma21_fraction_126d},
    "vp_ext_037_vol_above_ma63_fraction_252d": {"inputs": ["volume"], "func": vp_ext_037_vol_above_ma63_fraction_252d},
    "vp_ext_038_vol_above_ma21_count_63d_zscore_252d": {"inputs": ["volume"], "func": vp_ext_038_vol_above_ma21_count_63d_zscore_252d},
    "vp_ext_039_vol_above_ma63_count_252d_zscore_252d": {"inputs": ["volume"], "func": vp_ext_039_vol_above_ma63_count_252d_zscore_252d},
    "vp_ext_040_vol_above_ma21_fraction_21d_pct_rank_252d": {"inputs": ["volume"], "func": vp_ext_040_vol_above_ma21_fraction_21d_pct_rank_252d},
    "vp_ext_041_consec_days_above_ma21": {"inputs": ["volume"], "func": vp_ext_041_consec_days_above_ma21},
    "vp_ext_042_consec_days_above_ma63": {"inputs": ["volume"], "func": vp_ext_042_consec_days_above_ma63},
    "vp_ext_043_consec_days_above_ma252": {"inputs": ["volume"], "func": vp_ext_043_consec_days_above_ma252},
    "vp_ext_044_longest_run_above_ma21_in_63d": {"inputs": ["volume"], "func": vp_ext_044_longest_run_above_ma21_in_63d},
    "vp_ext_045_longest_run_above_ma21_in_252d": {"inputs": ["volume"], "func": vp_ext_045_longest_run_above_ma21_in_252d},
    "vp_ext_046_longest_run_above_ma63_in_252d": {"inputs": ["volume"], "func": vp_ext_046_longest_run_above_ma63_in_252d},
    "vp_ext_047_longest_run_above_ma252_in_252d": {"inputs": ["volume"], "func": vp_ext_047_longest_run_above_ma252_in_252d},
    "vp_ext_048_consec_above_ma21_vs_longest_63d": {"inputs": ["volume"], "func": vp_ext_048_consec_above_ma21_vs_longest_63d},
    "vp_ext_049_consec_above_ma63_vs_longest_252d": {"inputs": ["volume"], "func": vp_ext_049_consec_above_ma63_vs_longest_252d},
    "vp_ext_050_consec_above_ma21_log": {"inputs": ["volume"], "func": vp_ext_050_consec_above_ma21_log},
    "vp_ext_051_consec_above_ma63_log": {"inputs": ["volume"], "func": vp_ext_051_consec_above_ma63_log},
    "vp_ext_052_longest_run_above_ma21_in_63d_zscore_252d": {"inputs": ["volume"], "func": vp_ext_052_longest_run_above_ma21_in_63d_zscore_252d},
    "vp_ext_053_days_since_below_ma21": {"inputs": ["volume"], "func": vp_ext_053_days_since_below_ma21},
    "vp_ext_054_days_since_below_ma63": {"inputs": ["volume"], "func": vp_ext_054_days_since_below_ma63},
    "vp_ext_055_days_since_below_ma252": {"inputs": ["volume"], "func": vp_ext_055_days_since_below_ma252},
    "vp_ext_056_days_since_below_ma21_log": {"inputs": ["volume"], "func": vp_ext_056_days_since_below_ma21_log},
    "vp_ext_057_days_since_below_ma63_log": {"inputs": ["volume"], "func": vp_ext_057_days_since_below_ma63_log},
    "vp_ext_058_days_since_below_ma21_pct_rank_252d": {"inputs": ["volume"], "func": vp_ext_058_days_since_below_ma21_pct_rank_252d},
    "vp_ext_059_days_since_below_ma63_pct_rank_252d": {"inputs": ["volume"], "func": vp_ext_059_days_since_below_ma63_pct_rank_252d},
    "vp_ext_060_days_since_below_ma21_zscore_252d": {"inputs": ["volume"], "func": vp_ext_060_days_since_below_ma21_zscore_252d},
    "vp_ext_061_vol_above_ma21_run_normalized_by_hist_max": {"inputs": ["volume"], "func": vp_ext_061_vol_above_ma21_run_normalized_by_hist_max},
    "vp_ext_062_vol_above_ma63_run_normalized_by_hist_max": {"inputs": ["volume"], "func": vp_ext_062_vol_above_ma63_run_normalized_by_hist_max},
    "vp_ext_063_vol_above_median_count_21d": {"inputs": ["volume"], "func": vp_ext_063_vol_above_median_count_21d},
    "vp_ext_064_vol_above_median_count_63d": {"inputs": ["volume"], "func": vp_ext_064_vol_above_median_count_63d},
    "vp_ext_065_vol_above_median_fraction_63d": {"inputs": ["volume"], "func": vp_ext_065_vol_above_median_fraction_63d},
    "vp_ext_066_vol_above_median_consec_run": {"inputs": ["volume"], "func": vp_ext_066_vol_above_median_consec_run},
    "vp_ext_067_vol_ewm21_minus_sma21": {"inputs": ["volume"], "func": vp_ext_067_vol_ewm21_minus_sma21},
    "vp_ext_068_vol_ewm63_minus_sma63": {"inputs": ["volume"], "func": vp_ext_068_vol_ewm63_minus_sma63},
    "vp_ext_069_vol_ewm21_sma21_spread_zscore_252d": {"inputs": ["volume"], "func": vp_ext_069_vol_ewm21_sma21_spread_zscore_252d},
    "vp_ext_070_vol_plateau_score_21d": {"inputs": ["volume"], "func": vp_ext_070_vol_plateau_score_21d},
    "vp_ext_071_vol_plateau_score_63d": {"inputs": ["volume"], "func": vp_ext_071_vol_plateau_score_63d},
    "vp_ext_072_vol_sum_5d_roc_21d": {"inputs": ["volume"], "func": vp_ext_072_vol_sum_5d_roc_21d},
    "vp_ext_073_vol_above_ma21_fraction_21d_roc_21d": {"inputs": ["volume"], "func": vp_ext_073_vol_above_ma21_fraction_21d_roc_21d},
    "vp_ext_074_vol_above_ma63_fraction_63d_roc_21d": {"inputs": ["volume"], "func": vp_ext_074_vol_above_ma63_fraction_63d_roc_21d},
    "vp_ext_075_vol_sum_21d_vs_63d_avg_sum_ratio": {"inputs": ["volume"], "func": vp_ext_075_vol_sum_21d_vs_63d_avg_sum_ratio},
}
