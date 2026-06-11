"""
16_volume_persistence — Base Features 001-100
Domain: sustained elevated volume over multiple days — volume persistence.
Measures consecutive elevated-volume streaks, count of elevated days in trailing
windows, multi-day average elevation, fraction of recent days elevated, and
autocorrelation/stickiness of volume. Focus is on DURATION/SUSTAINMENT of high
volume, not one-off spikes, single-day climax, or volume collapse.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: within a group of True values cumsum gives run length."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (scalar apply)."""
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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _vol_baseline(volume: pd.Series, w: int) -> pd.Series:
    """Rolling mean volume baseline over w days (used as 'normal' reference)."""
    return _rolling_mean(volume, w)


def _is_elevated(volume: pd.Series, baseline: pd.Series, mult: float = 1.0) -> pd.Series:
    """Boolean: volume > mult * baseline."""
    return volume > mult * baseline.replace(0, np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Consecutive elevated-volume streak (current run length) ---

def vp_001_consec_elev_vol_21d_baseline(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 21-day average (streak count)."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _consec_streak(cond)


def vp_002_consec_elev_vol_63d_baseline(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 63-day average."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > base
    return _consec_streak(cond)


def vp_003_consec_elev_vol_252d_baseline(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 252-day average."""
    base = _vol_baseline(volume, _TD_YEAR)
    cond = volume > base
    return _consec_streak(cond)


def vp_004_consec_elev_vol_21d_1p5x(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 1.5x the 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 1.5 * base.replace(0, np.nan)
    return _consec_streak(cond)


def vp_005_consec_elev_vol_21d_2x(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 2x the 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _consec_streak(cond)


def vp_006_consec_elev_vol_63d_1p5x(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 1.5x the 63-day average."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > 1.5 * base.replace(0, np.nan)
    return _consec_streak(cond)


def vp_007_consec_elev_vol_63d_2x(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 2x the 63-day average."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _consec_streak(cond)


def vp_008_consec_elev_vol_ewm21(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 21-day EMA of volume."""
    base = _ewm_mean(volume, _TD_MON)
    cond = volume > base
    return _consec_streak(cond)


def vp_009_consec_elev_vol_ewm63(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 63-day EMA of volume."""
    base = _ewm_mean(volume, _TD_QTR)
    cond = volume > base
    return _consec_streak(cond)


def vp_010_consec_elev_vol_median_21d(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 21-day rolling median volume."""
    base = _rolling_median(volume, _TD_MON)
    cond = volume > base
    return _consec_streak(cond)


def vp_011_consec_elev_vol_21d_log(volume: pd.Series) -> pd.Series:
    """Log1p of current consecutive-above-21d-average streak (compresses tails)."""
    return np.log1p(vp_001_consec_elev_vol_21d_baseline(volume))


def vp_012_consec_elev_vol_63d_log(volume: pd.Series) -> pd.Series:
    """Log1p of current consecutive-above-63d-average streak."""
    return np.log1p(vp_002_consec_elev_vol_63d_baseline(volume))


def vp_013_consec_elev_vol_streak_norm_252d(volume: pd.Series) -> pd.Series:
    """Current above-21d-avg streak normalized by its 252-day average length."""
    streak = vp_001_consec_elev_vol_21d_baseline(volume)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def vp_014_consec_elev_vol_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current elevated-vol streak within trailing 252-day distribution."""
    streak = vp_001_consec_elev_vol_21d_baseline(volume)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_015_consec_elev_vol_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum consecutive elevated-volume streak."""
    streak = vp_001_consec_elev_vol_21d_baseline(volume)
    return streak.expanding(min_periods=1).max()


# --- Group B (016-025): Max elevated-volume streak in rolling windows ---

def vp_016_max_elev_vol_streak_21d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-21d-avg-volume run within trailing 21 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_max_streak(cond, _TD_MON)


def vp_017_max_elev_vol_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-21d-avg-volume run within trailing 63 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_max_streak(cond, _TD_QTR)


def vp_018_max_elev_vol_streak_126d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-21d-avg-volume run within trailing 126 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_max_streak(cond, _TD_HALF)


def vp_019_max_elev_vol_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-21d-avg-volume run within trailing 252 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_020_max_elev_vol_2x_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-2x-avg run within trailing 63 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_max_streak(cond, _TD_QTR)


def vp_021_max_elev_vol_2x_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-2x-avg run within trailing 252 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_max_streak(cond, _TD_YEAR)


def vp_022_current_vs_max_elev_streak_63d(volume: pd.Series) -> pd.Series:
    """Current elevated-vol streak as fraction of 63-day maximum elevated streak."""
    cur = vp_001_consec_elev_vol_21d_baseline(volume)
    mx = vp_017_max_elev_vol_streak_63d(volume)
    return _safe_div(cur, mx)


def vp_023_current_vs_max_elev_streak_252d(volume: pd.Series) -> pd.Series:
    """Current elevated-vol streak as fraction of 252-day maximum elevated streak."""
    cur = vp_001_consec_elev_vol_21d_baseline(volume)
    mx = vp_019_max_elev_vol_streak_252d(volume)
    return _safe_div(cur, mx)


def vp_024_max_elev_streak_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day max elevated streak to 252-day max (recent intensity)."""
    return _safe_div(vp_016_max_elev_vol_streak_21d(volume), vp_019_max_elev_vol_streak_252d(volume))


def vp_025_max_elev_streak_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day max elevated-volume streak."""
    mx = vp_019_max_elev_vol_streak_252d(volume)
    return mx.expanding(min_periods=5).rank(pct=True)


# --- Group C (026-035): Count of elevated-volume days in rolling windows ---

def vp_026_elev_vol_count_5d(volume: pd.Series) -> pd.Series:
    """Count of above-21d-avg-volume days in trailing 5 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_WEEK)


def vp_027_elev_vol_count_21d(volume: pd.Series) -> pd.Series:
    """Count of above-21d-avg-volume days in trailing 21 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_MON)


def vp_028_elev_vol_count_63d(volume: pd.Series) -> pd.Series:
    """Count of above-21d-avg-volume days in trailing 63 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_QTR)


def vp_029_elev_vol_count_126d(volume: pd.Series) -> pd.Series:
    """Count of above-21d-avg-volume days in trailing 126 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_HALF)


def vp_030_elev_vol_count_252d(volume: pd.Series) -> pd.Series:
    """Count of above-21d-avg-volume days in trailing 252 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_YEAR)


def vp_031_elev_vol_2x_count_21d(volume: pd.Series) -> pd.Series:
    """Count of above-2x-avg days in trailing 21 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_MON)


def vp_032_elev_vol_2x_count_63d(volume: pd.Series) -> pd.Series:
    """Count of above-2x-avg days in trailing 63 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_QTR)


def vp_033_elev_vol_1p5x_count_21d(volume: pd.Series) -> pd.Series:
    """Count of above-1.5x-avg days in trailing 21 days."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 1.5 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_MON)


def vp_034_elev_vol_1p5x_count_63d(volume: pd.Series) -> pd.Series:
    """Count of above-1.5x-avg days in trailing 63 days."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > 1.5 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_QTR)


def vp_035_elev_vol_count_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day elevated-day count within 252-day distribution."""
    cnt = vp_027_elev_vol_count_21d(volume)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (036-045): Fraction of days with elevated volume ---

def vp_036_elev_vol_fraction_5d(volume: pd.Series) -> pd.Series:
    """Fraction of last 5 days where volume > 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_WEEK) / _TD_WEEK


def vp_037_elev_vol_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume > 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > base
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vp_038_elev_vol_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume > 63-day average."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > base
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_039_elev_vol_fraction_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days where volume > 63-day average."""
    base = _vol_baseline(volume, _TD_QTR)
    cond = volume > base
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


def vp_040_elev_vol_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume > 252-day average."""
    base = _vol_baseline(volume, _TD_YEAR)
    cond = volume > base
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vp_041_elev_vol_2x_fraction_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume > 2x the 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vp_042_elev_vol_2x_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume > 2x the 21-day average."""
    base = _vol_baseline(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_043_elev_vol_fraction_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day elevated-day fraction within trailing 252-day distribution."""
    frac = vp_037_elev_vol_fraction_21d(volume)
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def vp_044_elev_vol_fraction_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day elevated-day fraction within trailing 252-day distribution."""
    frac = vp_038_elev_vol_fraction_63d(volume)
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def vp_045_elev_vol_fraction_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day elevated fraction (all-history)."""
    frac = vp_037_elev_vol_fraction_21d(volume)
    return frac.expanding(min_periods=5).rank(pct=True)


# --- Group E (046-055): Multi-day average volume elevation ratios ---

def vp_046_avg_vol_ratio_5d_vs_21d(volume: pd.Series) -> pd.Series:
    """Average volume over last 5 days divided by 21-day average (short-term elevation)."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    avg21 = _rolling_mean(volume, _TD_MON)
    return _safe_div(avg5, avg21)


def vp_047_avg_vol_ratio_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """Average volume over last 21 days divided by 63-day average."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg63 = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg21, avg63)


def vp_048_avg_vol_ratio_21d_vs_126d(volume: pd.Series) -> pd.Series:
    """Average volume over last 21 days divided by 126-day average."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg126 = _rolling_mean(volume, _TD_HALF)
    return _safe_div(avg21, avg126)


def vp_049_avg_vol_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Average volume over last 21 days divided by 252-day average."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(avg21, avg252)


def vp_050_avg_vol_ratio_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """Average volume over last 63 days divided by 252-day average."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(avg63, avg252)


def vp_051_avg_vol_ratio_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """Average volume over last 5 days divided by 252-day average."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(avg5, avg252)


def vp_052_avg_vol_ratio_10d_vs_63d(volume: pd.Series) -> pd.Series:
    """Average volume over last 10 days divided by 63-day average."""
    avg10 = _rolling_mean(volume, 10)
    avg63 = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg10, avg63)


def vp_053_avg_vol_ratio_21d_vs_63d_pct_rank(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d/63d volume ratio within trailing 252 days."""
    ratio = vp_047_avg_vol_ratio_21d_vs_63d(volume)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_054_avg_vol_ratio_21d_vs_252d_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of 21d/252d average volume ratio over trailing 252 days."""
    ratio = vp_049_avg_vol_ratio_21d_vs_252d(volume)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def vp_055_avg_vol_ewm5_vs_ewm63(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA volume to 63-day EMA volume."""
    e5 = _ewm_mean(volume, _TD_WEEK)
    e63 = _ewm_mean(volume, _TD_QTR)
    return _safe_div(e5, e63)


# --- Group F (056-065): Average elevation magnitude during elevated runs ---

def vp_056_avg_elevation_during_elev_streak(volume: pd.Series) -> pd.Series:
    """Average vol/baseline ratio during current consecutive elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    cond = volume > base
    group = (~cond).cumsum()
    cum_ratio = ratio.groupby(group).cumsum()
    streak_len = _consec_streak(cond).replace(0, np.nan)
    return _safe_div(cum_ratio.where(cond, np.nan), streak_len)


def vp_057_sum_elevation_during_elev_streak(volume: pd.Series) -> pd.Series:
    """Cumulative vol/baseline elevation accumulated over current elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    cond = volume > base
    group = (~cond).cumsum()
    cum_ratio = ratio.groupby(group).cumsum()
    return cum_ratio.where(cond, 0.0)


def vp_058_avg_vol_elevation_21d_elevated_days(volume: pd.Series) -> pd.Series:
    """Mean vol/21d-avg ratio on elevated-volume days over trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    elev = ratio.where(ratio > 1.0, np.nan)
    return elev.rolling(_TD_MON, min_periods=1).mean()


def vp_059_avg_vol_elevation_63d_elevated_days(volume: pd.Series) -> pd.Series:
    """Mean vol/21d-avg ratio on elevated-volume days over trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    elev = ratio.where(ratio > 1.0, np.nan)
    return elev.rolling(_TD_QTR, min_periods=1).mean()


def vp_060_max_elevation_21d(volume: pd.Series) -> pd.Series:
    """Maximum daily vol/21d-avg ratio within trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    return _rolling_max(ratio, _TD_MON)


def vp_061_max_elevation_63d(volume: pd.Series) -> pd.Series:
    """Maximum daily vol/21d-avg ratio within trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    return _rolling_max(ratio, _TD_QTR)


def vp_062_min_elevation_21d(volume: pd.Series) -> pd.Series:
    """Minimum daily vol/21d-avg ratio within trailing 21 days (how low dips drop)."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    return _rolling_min(ratio, _TD_MON)


def vp_063_std_vol_ratio_21d(volume: pd.Series) -> pd.Series:
    """Rolling std dev of daily vol/21d-avg ratio over trailing 21 days (consistency)."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    return _rolling_std(ratio, _TD_MON)


def vp_064_std_vol_ratio_63d(volume: pd.Series) -> pd.Series:
    """Rolling std dev of daily vol/21d-avg ratio over trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    return _rolling_std(ratio, _TD_QTR)


def vp_065_elev_vol_streak_x_avg_elevation(volume: pd.Series) -> pd.Series:
    """Current elevated-streak length times its average elevation (intensity score)."""
    streak = vp_001_consec_elev_vol_21d_baseline(volume)
    avg_elev = vp_056_avg_elevation_during_elev_streak(volume)
    return streak * avg_elev.fillna(1.0)


# --- Group G (066-075): Volume autocorrelation / stickiness measures ---

def vp_066_vol_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of volume at lag-1 (stickiness of volume level)."""
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        lambda x: pd.Series(x).autocorr(lag=1) if len(x) >= 3 else np.nan, raw=False
    )


def vp_067_vol_autocorr_lag1_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of volume at lag-1."""
    return volume.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(
        lambda x: pd.Series(x).autocorr(lag=1) if len(x) >= 3 else np.nan, raw=False
    )


def vp_068_vol_ratio_autocorr_lag1_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day autocorrelation of vol/21d-avg ratio at lag-1."""
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base).fillna(1.0)
    return ratio.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        lambda x: pd.Series(x).autocorr(lag=1) if len(x) >= 3 else np.nan, raw=False
    )


def vp_069_vol_elevated_run_start_freq_63d(volume: pd.Series) -> pd.Series:
    """Number of new elevated-vol streak starts in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    is_start = (cond & ~cond.shift(1).fillna(False)).astype(float)
    return _rolling_sum(is_start, _TD_QTR)


def vp_070_vol_elevated_run_start_freq_252d(volume: pd.Series) -> pd.Series:
    """Number of new elevated-vol streak starts in trailing 252 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    is_start = (cond & ~cond.shift(1).fillna(False)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def vp_071_avg_elev_streak_len_63d(volume: pd.Series) -> pd.Series:
    """Average length of elevated-vol streaks within trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base

    def _avg_run(arr):
        total = 0
        num_runs = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur
                    num_runs += 1
                cur = 0
        if cur > 0:
            total += cur
            num_runs += 1
        return float(total) / float(num_runs) if num_runs > 0 else 0.0

    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_avg_run, raw=True)


def vp_072_avg_elev_streak_len_252d(volume: pd.Series) -> pd.Series:
    """Average length of elevated-vol streaks within trailing 252 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base

    def _avg_run(arr):
        total = 0
        num_runs = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur
                    num_runs += 1
                cur = 0
        if cur > 0:
            total += cur
            num_runs += 1
        return float(total) / float(num_runs) if num_runs > 0 else 0.0

    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_avg_run, raw=True)


def vp_073_elev_vol_persistence_score_21d(volume: pd.Series) -> pd.Series:
    """Persistence score: fraction × avg streak len × avg elevation over 21 days."""
    frac = vp_037_elev_vol_fraction_21d(volume)
    base = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, base)
    avg_ratio = _rolling_mean(ratio, _TD_MON)
    streak = vp_001_consec_elev_vol_21d_baseline(volume)
    norm_streak = _safe_div(streak, _rolling_mean(streak, _TD_YEAR).clip(lower=_EPS))
    return frac * avg_ratio * norm_streak


def vp_074_vol_above_prior_day_consec_streak(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > prior day volume (growing vol streak)."""
    cond = volume > volume.shift(1)
    return _consec_streak(cond)


def vp_075_max_vol_above_prior_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive days of volume > prior day within trailing 63 days."""
    cond = volume > volume.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


# --- Group P (151-160): Price-range weighted volume persistence ---

def vp_151_elev_vol_on_wide_range_consec(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with elevated vol (>21d avg) AND wide daily range (>21d avg range)."""
    base = _rolling_mean(volume, _TD_MON)
    rng = high - low
    base_rng = _rolling_mean(rng, _TD_MON)
    cond = (volume > base) & (rng > base_rng)
    return _consec_streak(cond)


def vp_152_elev_vol_on_wide_range_count_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol wide-range days in trailing 21 days."""
    base = _rolling_mean(volume, _TD_MON)
    rng = high - low
    base_rng = _rolling_mean(rng, _TD_MON)
    cond = (volume > base) & (rng > base_rng)
    return _rolling_count_true(cond, _TD_MON)


def vp_153_elev_vol_on_wide_range_count_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of elevated-vol wide-range days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    rng = high - low
    base_rng = _rolling_mean(rng, _TD_MON)
    cond = (volume > base) & (rng > base_rng)
    return _rolling_count_true(cond, _TD_QTR)


def vp_154_range_weighted_vol_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average of (volume * daily_range) / 21d avg(volume * daily_range)."""
    rng = high - low
    rv = volume * rng
    avg_rv = _rolling_mean(rv, _TD_MON)
    return _safe_div(rv, avg_rv)


def vp_155_range_vol_persistence_fraction_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63 days where range-volume product > its 63d average."""
    rv = (high - low) * volume
    base = _rolling_mean(rv, _TD_QTR)
    cond = rv > base
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_156_vol_above_3x_21d_consec(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > 3x the 21-day average (panic surges)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > 3.0 * base.replace(0, np.nan)
    return _consec_streak(cond)


def vp_157_vol_above_3x_21d_count_63d(volume: pd.Series) -> pd.Series:
    """Count of above-3x-avg volume days in trailing 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > 3.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_QTR)


def vp_158_vol_above_95th_pct_consec(volume: pd.Series) -> pd.Series:
    """Current streak where volume > 95th percentile of trailing 252-day volume."""
    pct95 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    cond = volume > pct95
    return _consec_streak(cond)


def vp_159_vol_above_95th_pct_count_63d(volume: pd.Series) -> pd.Series:
    """Count of above-95th-pct volume days in trailing 63 days."""
    pct95 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    cond = volume > pct95
    return _rolling_count_true(cond, _TD_QTR)


def vp_160_vol_above_95th_pct_fraction_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days where volume > 95th percentile (252d)."""
    pct95 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    cond = volume > pct95
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


# --- Group Q (161-175): Cross-timeframe ratios, decay, and novel persistence transforms ---

def vp_161_vol_median_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day rolling median volume to 252-day rolling median volume."""
    med21 = _rolling_median(volume, _TD_MON)
    med252 = _rolling_median(volume, _TD_YEAR)
    return _safe_div(med21, med252)


def vp_162_vol_above_prior_week_consec(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume > same day 5 sessions ago."""
    cond = volume > volume.shift(_TD_WEEK)
    return _consec_streak(cond)


def vp_163_vol_above_prior_week_fraction_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where daily volume > volume 5 sessions prior."""
    cond = volume > volume.shift(_TD_WEEK)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vp_164_vol_above_prior_month_consec(volume: pd.Series) -> pd.Series:
    """Current consecutive days where daily volume > volume 21 sessions ago."""
    cond = volume > volume.shift(_TD_MON)
    return _consec_streak(cond)


def vp_165_vol_above_prior_month_fraction_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days where daily volume > volume 21 sessions prior."""
    cond = volume > volume.shift(_TD_MON)
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


def vp_166_vol_ewm_ratio_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day EMA volume to 252-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))


def vp_167_elev_vol_2x_fraction_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days where volume > 2x the 21-day average."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


def vp_168_vol_log_ratio_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """Log ratio of 5-day average volume to 252-day average volume."""
    avg5 = _rolling_mean(volume, _TD_WEEK)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    return _log_safe(avg5) - _log_safe(avg252)


def vp_169_elev_vol_1p5x_count_126d(volume: pd.Series) -> pd.Series:
    """Count of above-1.5x-avg volume days in trailing 126 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > 1.5 * base.replace(0, np.nan)
    return _rolling_count_true(cond, _TD_HALF)


def vp_170_vol_pct_rank_10d_avg_in_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 10-day average volume within trailing 252-day series."""
    avg10 = _rolling_mean(volume, 10)
    return avg10.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vp_171_avg_vol_ratio_63d_vs_126d(volume: pd.Series) -> pd.Series:
    """Average volume over last 63 days divided by 126-day average."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    avg126 = _rolling_mean(volume, _TD_HALF)
    return _safe_div(avg63, avg126)


def vp_172_elev_vol_fraction_5d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 5-day elevated-vol fraction within trailing 252-day distribution."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_WEEK) / _TD_WEEK
    m = _rolling_mean(frac, _TD_YEAR)
    s = _rolling_std(frac, _TD_YEAR)
    return _safe_div(frac - m, s)


def vp_173_vol_sum_ratio_5d_vs_21d(volume: pd.Series) -> pd.Series:
    """Sum of volume over last 5 days divided by 21-day total (short-term surge share)."""
    s5 = _rolling_sum(volume, _TD_WEEK)
    s21 = _rolling_sum(volume, _TD_MON)
    return _safe_div(s5, s21)


def vp_174_vol_above_2x_max_streak_126d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive above-2x-avg volume days within trailing 126 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > 2.0 * base.replace(0, np.nan)
    return _rolling_max_streak(cond, _TD_HALF)


def vp_175_elev_vol_streak_acc_21d(volume: pd.Series) -> pd.Series:
    """21-day change in current elevated-volume streak length."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    return streak.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PERSISTENCE_REGISTRY_001_075 = {
    "vp_001_consec_elev_vol_21d_baseline": {"inputs": ["volume"], "func": vp_001_consec_elev_vol_21d_baseline},
    "vp_002_consec_elev_vol_63d_baseline": {"inputs": ["volume"], "func": vp_002_consec_elev_vol_63d_baseline},
    "vp_003_consec_elev_vol_252d_baseline": {"inputs": ["volume"], "func": vp_003_consec_elev_vol_252d_baseline},
    "vp_004_consec_elev_vol_21d_1p5x": {"inputs": ["volume"], "func": vp_004_consec_elev_vol_21d_1p5x},
    "vp_005_consec_elev_vol_21d_2x": {"inputs": ["volume"], "func": vp_005_consec_elev_vol_21d_2x},
    "vp_006_consec_elev_vol_63d_1p5x": {"inputs": ["volume"], "func": vp_006_consec_elev_vol_63d_1p5x},
    "vp_007_consec_elev_vol_63d_2x": {"inputs": ["volume"], "func": vp_007_consec_elev_vol_63d_2x},
    "vp_008_consec_elev_vol_ewm21": {"inputs": ["volume"], "func": vp_008_consec_elev_vol_ewm21},
    "vp_009_consec_elev_vol_ewm63": {"inputs": ["volume"], "func": vp_009_consec_elev_vol_ewm63},
    "vp_010_consec_elev_vol_median_21d": {"inputs": ["volume"], "func": vp_010_consec_elev_vol_median_21d},
    "vp_011_consec_elev_vol_21d_log": {"inputs": ["volume"], "func": vp_011_consec_elev_vol_21d_log},
    "vp_012_consec_elev_vol_63d_log": {"inputs": ["volume"], "func": vp_012_consec_elev_vol_63d_log},
    "vp_013_consec_elev_vol_streak_norm_252d": {"inputs": ["volume"], "func": vp_013_consec_elev_vol_streak_norm_252d},
    "vp_014_consec_elev_vol_21d_pct_rank_252d": {"inputs": ["volume"], "func": vp_014_consec_elev_vol_21d_pct_rank_252d},
    "vp_015_consec_elev_vol_expanding_max": {"inputs": ["volume"], "func": vp_015_consec_elev_vol_expanding_max},
    "vp_016_max_elev_vol_streak_21d": {"inputs": ["volume"], "func": vp_016_max_elev_vol_streak_21d},
    "vp_017_max_elev_vol_streak_63d": {"inputs": ["volume"], "func": vp_017_max_elev_vol_streak_63d},
    "vp_018_max_elev_vol_streak_126d": {"inputs": ["volume"], "func": vp_018_max_elev_vol_streak_126d},
    "vp_019_max_elev_vol_streak_252d": {"inputs": ["volume"], "func": vp_019_max_elev_vol_streak_252d},
    "vp_020_max_elev_vol_2x_streak_63d": {"inputs": ["volume"], "func": vp_020_max_elev_vol_2x_streak_63d},
    "vp_021_max_elev_vol_2x_streak_252d": {"inputs": ["volume"], "func": vp_021_max_elev_vol_2x_streak_252d},
    "vp_022_current_vs_max_elev_streak_63d": {"inputs": ["volume"], "func": vp_022_current_vs_max_elev_streak_63d},
    "vp_023_current_vs_max_elev_streak_252d": {"inputs": ["volume"], "func": vp_023_current_vs_max_elev_streak_252d},
    "vp_024_max_elev_streak_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vp_024_max_elev_streak_21d_vs_252d_ratio},
    "vp_025_max_elev_streak_252d_expanding_rank": {"inputs": ["volume"], "func": vp_025_max_elev_streak_252d_expanding_rank},
    "vp_026_elev_vol_count_5d": {"inputs": ["volume"], "func": vp_026_elev_vol_count_5d},
    "vp_027_elev_vol_count_21d": {"inputs": ["volume"], "func": vp_027_elev_vol_count_21d},
    "vp_028_elev_vol_count_63d": {"inputs": ["volume"], "func": vp_028_elev_vol_count_63d},
    "vp_029_elev_vol_count_126d": {"inputs": ["volume"], "func": vp_029_elev_vol_count_126d},
    "vp_030_elev_vol_count_252d": {"inputs": ["volume"], "func": vp_030_elev_vol_count_252d},
    "vp_031_elev_vol_2x_count_21d": {"inputs": ["volume"], "func": vp_031_elev_vol_2x_count_21d},
    "vp_032_elev_vol_2x_count_63d": {"inputs": ["volume"], "func": vp_032_elev_vol_2x_count_63d},
    "vp_033_elev_vol_1p5x_count_21d": {"inputs": ["volume"], "func": vp_033_elev_vol_1p5x_count_21d},
    "vp_034_elev_vol_1p5x_count_63d": {"inputs": ["volume"], "func": vp_034_elev_vol_1p5x_count_63d},
    "vp_035_elev_vol_count_21d_pct_rank_252d": {"inputs": ["volume"], "func": vp_035_elev_vol_count_21d_pct_rank_252d},
    "vp_036_elev_vol_fraction_5d": {"inputs": ["volume"], "func": vp_036_elev_vol_fraction_5d},
    "vp_037_elev_vol_fraction_21d": {"inputs": ["volume"], "func": vp_037_elev_vol_fraction_21d},
    "vp_038_elev_vol_fraction_63d": {"inputs": ["volume"], "func": vp_038_elev_vol_fraction_63d},
    "vp_039_elev_vol_fraction_126d": {"inputs": ["volume"], "func": vp_039_elev_vol_fraction_126d},
    "vp_040_elev_vol_fraction_252d": {"inputs": ["volume"], "func": vp_040_elev_vol_fraction_252d},
    "vp_041_elev_vol_2x_fraction_21d": {"inputs": ["volume"], "func": vp_041_elev_vol_2x_fraction_21d},
    "vp_042_elev_vol_2x_fraction_63d": {"inputs": ["volume"], "func": vp_042_elev_vol_2x_fraction_63d},
    "vp_043_elev_vol_fraction_21d_zscore_252d": {"inputs": ["volume"], "func": vp_043_elev_vol_fraction_21d_zscore_252d},
    "vp_044_elev_vol_fraction_63d_zscore_252d": {"inputs": ["volume"], "func": vp_044_elev_vol_fraction_63d_zscore_252d},
    "vp_045_elev_vol_fraction_21d_expanding_rank": {"inputs": ["volume"], "func": vp_045_elev_vol_fraction_21d_expanding_rank},
    "vp_046_avg_vol_ratio_5d_vs_21d": {"inputs": ["volume"], "func": vp_046_avg_vol_ratio_5d_vs_21d},
    "vp_047_avg_vol_ratio_21d_vs_63d": {"inputs": ["volume"], "func": vp_047_avg_vol_ratio_21d_vs_63d},
    "vp_048_avg_vol_ratio_21d_vs_126d": {"inputs": ["volume"], "func": vp_048_avg_vol_ratio_21d_vs_126d},
    "vp_049_avg_vol_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vp_049_avg_vol_ratio_21d_vs_252d},
    "vp_050_avg_vol_ratio_63d_vs_252d": {"inputs": ["volume"], "func": vp_050_avg_vol_ratio_63d_vs_252d},
    "vp_051_avg_vol_ratio_5d_vs_252d": {"inputs": ["volume"], "func": vp_051_avg_vol_ratio_5d_vs_252d},
    "vp_052_avg_vol_ratio_10d_vs_63d": {"inputs": ["volume"], "func": vp_052_avg_vol_ratio_10d_vs_63d},
    "vp_053_avg_vol_ratio_21d_vs_63d_pct_rank": {"inputs": ["volume"], "func": vp_053_avg_vol_ratio_21d_vs_63d_pct_rank},
    "vp_054_avg_vol_ratio_21d_vs_252d_zscore": {"inputs": ["volume"], "func": vp_054_avg_vol_ratio_21d_vs_252d_zscore},
    "vp_055_avg_vol_ewm5_vs_ewm63": {"inputs": ["volume"], "func": vp_055_avg_vol_ewm5_vs_ewm63},
    "vp_056_avg_elevation_during_elev_streak": {"inputs": ["volume"], "func": vp_056_avg_elevation_during_elev_streak},
    "vp_057_sum_elevation_during_elev_streak": {"inputs": ["volume"], "func": vp_057_sum_elevation_during_elev_streak},
    "vp_058_avg_vol_elevation_21d_elevated_days": {"inputs": ["volume"], "func": vp_058_avg_vol_elevation_21d_elevated_days},
    "vp_059_avg_vol_elevation_63d_elevated_days": {"inputs": ["volume"], "func": vp_059_avg_vol_elevation_63d_elevated_days},
    "vp_060_max_elevation_21d": {"inputs": ["volume"], "func": vp_060_max_elevation_21d},
    "vp_061_max_elevation_63d": {"inputs": ["volume"], "func": vp_061_max_elevation_63d},
    "vp_062_min_elevation_21d": {"inputs": ["volume"], "func": vp_062_min_elevation_21d},
    "vp_063_std_vol_ratio_21d": {"inputs": ["volume"], "func": vp_063_std_vol_ratio_21d},
    "vp_064_std_vol_ratio_63d": {"inputs": ["volume"], "func": vp_064_std_vol_ratio_63d},
    "vp_065_elev_vol_streak_x_avg_elevation": {"inputs": ["volume"], "func": vp_065_elev_vol_streak_x_avg_elevation},
    "vp_066_vol_autocorr_lag1_21d": {"inputs": ["volume"], "func": vp_066_vol_autocorr_lag1_21d},
    "vp_067_vol_autocorr_lag1_63d": {"inputs": ["volume"], "func": vp_067_vol_autocorr_lag1_63d},
    "vp_068_vol_ratio_autocorr_lag1_21d": {"inputs": ["volume"], "func": vp_068_vol_ratio_autocorr_lag1_21d},
    "vp_069_vol_elevated_run_start_freq_63d": {"inputs": ["volume"], "func": vp_069_vol_elevated_run_start_freq_63d},
    "vp_070_vol_elevated_run_start_freq_252d": {"inputs": ["volume"], "func": vp_070_vol_elevated_run_start_freq_252d},
    "vp_071_avg_elev_streak_len_63d": {"inputs": ["volume"], "func": vp_071_avg_elev_streak_len_63d},
    "vp_072_avg_elev_streak_len_252d": {"inputs": ["volume"], "func": vp_072_avg_elev_streak_len_252d},
    "vp_073_elev_vol_persistence_score_21d": {"inputs": ["volume"], "func": vp_073_elev_vol_persistence_score_21d},
    "vp_074_vol_above_prior_day_consec_streak": {"inputs": ["volume"], "func": vp_074_vol_above_prior_day_consec_streak},
    "vp_075_max_vol_above_prior_streak_63d": {"inputs": ["volume"], "func": vp_075_max_vol_above_prior_streak_63d},
    "vp_151_elev_vol_on_wide_range_consec": {"inputs": ["high", "low", "volume"], "func": vp_151_elev_vol_on_wide_range_consec},
    "vp_152_elev_vol_on_wide_range_count_21d": {"inputs": ["high", "low", "volume"], "func": vp_152_elev_vol_on_wide_range_count_21d},
    "vp_153_elev_vol_on_wide_range_count_63d": {"inputs": ["high", "low", "volume"], "func": vp_153_elev_vol_on_wide_range_count_63d},
    "vp_154_range_weighted_vol_ratio_21d": {"inputs": ["high", "low", "volume"], "func": vp_154_range_weighted_vol_ratio_21d},
    "vp_155_range_vol_persistence_fraction_63d": {"inputs": ["high", "low", "volume"], "func": vp_155_range_vol_persistence_fraction_63d},
    "vp_156_vol_above_3x_21d_consec": {"inputs": ["volume"], "func": vp_156_vol_above_3x_21d_consec},
    "vp_157_vol_above_3x_21d_count_63d": {"inputs": ["volume"], "func": vp_157_vol_above_3x_21d_count_63d},
    "vp_158_vol_above_95th_pct_consec": {"inputs": ["volume"], "func": vp_158_vol_above_95th_pct_consec},
    "vp_159_vol_above_95th_pct_count_63d": {"inputs": ["volume"], "func": vp_159_vol_above_95th_pct_count_63d},
    "vp_160_vol_above_95th_pct_fraction_126d": {"inputs": ["volume"], "func": vp_160_vol_above_95th_pct_fraction_126d},
    "vp_161_vol_median_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vp_161_vol_median_ratio_21d_vs_252d},
    "vp_162_vol_above_prior_week_consec": {"inputs": ["volume"], "func": vp_162_vol_above_prior_week_consec},
    "vp_163_vol_above_prior_week_fraction_63d": {"inputs": ["volume"], "func": vp_163_vol_above_prior_week_fraction_63d},
    "vp_164_vol_above_prior_month_consec": {"inputs": ["volume"], "func": vp_164_vol_above_prior_month_consec},
    "vp_165_vol_above_prior_month_fraction_126d": {"inputs": ["volume"], "func": vp_165_vol_above_prior_month_fraction_126d},
    "vp_166_vol_ewm_ratio_63d_vs_252d": {"inputs": ["volume"], "func": vp_166_vol_ewm_ratio_63d_vs_252d},
    "vp_167_elev_vol_2x_fraction_126d": {"inputs": ["volume"], "func": vp_167_elev_vol_2x_fraction_126d},
    "vp_168_vol_log_ratio_5d_vs_252d": {"inputs": ["volume"], "func": vp_168_vol_log_ratio_5d_vs_252d},
    "vp_169_elev_vol_1p5x_count_126d": {"inputs": ["volume"], "func": vp_169_elev_vol_1p5x_count_126d},
    "vp_170_vol_pct_rank_10d_avg_in_252d": {"inputs": ["volume"], "func": vp_170_vol_pct_rank_10d_avg_in_252d},
    "vp_171_avg_vol_ratio_63d_vs_126d": {"inputs": ["volume"], "func": vp_171_avg_vol_ratio_63d_vs_126d},
    "vp_172_elev_vol_fraction_5d_zscore_252d": {"inputs": ["volume"], "func": vp_172_elev_vol_fraction_5d_zscore_252d},
    "vp_173_vol_sum_ratio_5d_vs_21d": {"inputs": ["volume"], "func": vp_173_vol_sum_ratio_5d_vs_21d},
    "vp_174_vol_above_2x_max_streak_126d": {"inputs": ["volume"], "func": vp_174_vol_above_2x_max_streak_126d},
    "vp_175_elev_vol_streak_acc_21d": {"inputs": ["volume"], "func": vp_175_elev_vol_streak_acc_21d},
}
