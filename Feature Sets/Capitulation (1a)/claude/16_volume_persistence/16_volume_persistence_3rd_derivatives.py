"""
16_volume_persistence — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative volume-persistence features — acceleration
of velocity, inflection and exhaustion in sustained elevated-volume behavior.
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
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
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope of a 2nd-derivative concept

def vp_drv3_001_consec_elev_vol_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of elevated-vol streak (acceleration of streak velocity)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_002_consec_elev_vol_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day-velocity of elevated-vol streak (jerk)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    vel21 = streak.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_003_max_elev_streak_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day max elevated streak (2nd accel)."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_QTR)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_004_elev_vol_fraction_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_005_avg_vol_ratio_21d_vs_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/252d avg-volume ratio."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_006_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/63d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_007_elev_vol_count_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day elevated-vol count (jerk of count velocity)."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_008_elev_vol_fraction_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_QTR)
    frac = _rolling_count_true(volume > base, _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_009_elev_vol_streak_zscore_5d_diff_slope(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of elevated-streak z-score."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_010_vol_ewm_ratio_21d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_011_elev_vol_down_fraction_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day elevated-vol-on-down-day fraction."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_012_avg_vol_ratio_21d_vs_252d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 21d/252d volume ratio."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vp_drv3_013_elev_vol_fraction_21d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    slp = _linslope(frac, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_014_max_elev_streak_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day max elevated streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_YEAR)
    vel21 = mx.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_015_consec_ewm5_above_ewm21_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive EMA5>EMA21 volume streak."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_016_elev_vol_persistence_score_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day persistence score (inflection detector)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    avg_ratio = _rolling_mean(_safe_div(volume, base), _TD_MON)
    streak = _consec_streak(cond)
    norm_streak = _safe_div(streak, _rolling_mean(streak, _TD_YEAR).clip(lower=_EPS))
    score = frac * avg_ratio * norm_streak
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_017_avg_elev_streak_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day average elevated-streak length."""
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

    avg63 = cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_avg_run, raw=True)
    vel21 = avg63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_018_elev_vol_count_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day elevated-vol count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_019_vol_above_prior_day_fraction_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day fraction of volume > prior-day volume."""
    cond = volume > volume.shift(1)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_020_avg_vol_ratio_5d_vs_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/21d avg-volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_021_max_elev_streak_63d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of 63-day max elevated streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_QTR)
    slp = _linslope(mx, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_022_elev_vol_fraction_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_YEAR)
    frac = _rolling_count_true(volume > base, _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_023_elev_vol_streak_zscore_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of elevated-vol streak z-score (exhaustion signal)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_024_elev_vol_down_count_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day elevated-vol-on-down-day count."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_025_elev_vol_count_21d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 21-day elevated-vol count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    slp = _linslope(cnt, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- 3rd Derivatives 026-075 ---

def vp_drv3_026_avg_vol_ratio_63d_vs_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_027_avg_vol_ratio_63d_vs_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_028_elev_vol_count_126d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_HALF)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_029_elev_vol_fraction_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_HALF) / _TD_HALF
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_030_vol_ewm_ratio_5d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA5/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_031_vol_ewm_ratio_21d_vs_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA21/EMA252 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_032_elev_vol_2x_count_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day count of volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_033_vol_above_90th_pct_consec_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive above-90th-pct volume streak."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    streak = _consec_streak(volume > pct90)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_034_elev_vol_down_fraction_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day elevated-vol-on-down-day fraction."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_035_vol_ewm_ratio_5d_vs_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in EMA5/EMA21 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_MON))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_036_elev_vol_persistence_index_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of the persistence-index (streak * frac * zscore)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    streak = _consec_streak(cond)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s).fillna(0.0)
    idx = frac * z
    vel = idx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_037_vol_sum_ratio_5d_vs_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/21d total volume ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_WEEK), _rolling_sum(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_038_avg_vol_ratio_21d_vs_63d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 21d/63d avg-volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_039_elev_vol_fraction_5d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_WEEK) / _TD_WEEK
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_040_vol_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume coefficient of variation."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_041_elev_vol_count_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 21-day elevated-vol count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    slp = _linslope(cnt, _TD_MON)
    return slp.diff(_TD_WEEK)


def vp_drv3_042_vol_pct_rank_current_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of daily volume percentile rank (252d window)."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_043_avg_vol_ratio_21d_vs_252d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 21d/252d volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vp_drv3_044_elev_vol_count_63d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 63-day elevated-vol count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_QTR)
    slp = _linslope(cnt, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_045_elev_vol_fraction_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    slp = _linslope(frac, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_046_consec_elev_vol_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    vel = streak.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_047_elev_vol_fraction_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of 21d elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_048_avg_vol_ratio_21d_vs_252d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of 21d/252d volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_049_vol_ewm_ratio_21d_vs_63d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of EMA21/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_050_max_elev_streak_63d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of 63d max elevated streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_QTR)
    vel = mx.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_051_elev_vol_2x_count_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day count of volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_052_vol_above_prior_day_fraction_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day fraction days with vol > prior-day vol."""
    cond = volume > volume.shift(1)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_053_vol_log_ratio_21d_vs_252d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 5-day velocity of log(21d/252d) volume ratio."""
    log_r = np.log(_rolling_mean(volume, _TD_MON).clip(lower=_EPS)) - np.log(_rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    vel = log_r.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vp_drv3_054_elev_vol_down_vs_up_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day elevated-vol-down/up count ratio."""
    base = _rolling_mean(volume, _TD_MON)
    dn = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_MON)
    up = _rolling_count_true((volume > base) & (close > close.shift(1)), _TD_MON)
    ratio = _safe_div(dn, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_055_elev_vol_start_freq_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in elevated-streak start frequency (63d)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    is_start = (cond & ~cond.shift(1).fillna(False)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_056_avg_vol_ratio_21d_vs_126d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/126d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_HALF))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_057_elev_vol_fraction_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    slp = _linslope(frac, _TD_MON)
    return slp.diff(_TD_WEEK)


def vp_drv3_058_max_elev_streak_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day max elevated streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_YEAR)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_059_avg_elev_streak_len_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day average elevated-streak length."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base

    def _avg_run(arr):
        total = 0; num_runs = 0; cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur; num_runs += 1
                cur = 0
        if cur > 0:
            total += cur; num_runs += 1
        return float(total) / float(num_runs) if num_runs > 0 else 0.0

    avg252 = cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_avg_run, raw=True)
    vel21 = avg252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_060_vol_pct_rank_21d_avg_in_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of percentile rank of 21-day avg vol in 252d window."""
    avg21 = _rolling_mean(volume, _TD_MON)
    rank = avg21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_061_elev_vol_down_fraction_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day elevated-vol-down-day fraction."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vp_drv3_062_consec_ewm21_above_ewm63_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive EMA21>EMA63 volume streak."""
    cond = _ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_063_elev_vol_count_21d_vs_252d_avg_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized 21d elevated count vs 252d avg."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    avg_cnt = _rolling_mean(cnt, _TD_YEAR)
    ratio = _safe_div(cnt, avg_cnt)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_064_vol_ewm_ratio_63d_vs_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EMA63/EMA252 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_065_elev_vol_streak_pct_rank_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of percentile rank of elevated-vol streak (252d)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    rank = streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_066_elev_vol_2x_fraction_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day fraction with volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_067_vol_sum_ratio_5d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/63d total volume ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_WEEK), _rolling_sum(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_068_avg_vol_ratio_21d_vs_252d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 21d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_069_elev_vol_down_count_63d_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (63d) of 63-day elevated-vol-on-down-day count."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_QTR)
    slp = _linslope(cnt, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vp_drv3_070_elev_dollar_vol_consec_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of current consecutive elevated-dollar-volume streak."""
    dv = close * volume
    streak = _consec_streak(dv > _rolling_mean(dv, _TD_MON))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_071_vol_log_ratio_5d_vs_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(5d/63d) average volume ratio."""
    log_r = np.log(_rolling_mean(volume, _TD_WEEK).clip(lower=_EPS)) - np.log(_rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    vel = log_r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_072_consec_vol_above_prior_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-days-vol-above-lagged-63d-avg streak."""
    base_lagged = _rolling_mean(volume, _TD_QTR).shift(_TD_QTR)
    streak = _consec_streak(volume > base_lagged)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vp_drv3_073_elev_vol_fraction_252d_21d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the 21-day velocity of 252-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def vp_drv3_074_elev_vol_streak_zscore_5d_diff_5d_diff_slope(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the second 5-day diff of elevated-streak z-score."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    vel1 = z.diff(_TD_WEEK)
    accel = vel1.diff(_TD_WEEK)
    return _linslope(accel, _TD_MON)


def vp_drv3_075_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff_slope(volume: pd.Series) -> pd.Series:
    """OLS slope (21d) of the second 5-day diff of 21d/63d volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _linslope(accel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PERSISTENCE_REGISTRY_3RD_DERIVATIVES = {
    "vp_drv3_001_consec_elev_vol_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_001_consec_elev_vol_5d_diff_5d_diff},
    "vp_drv3_002_consec_elev_vol_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_002_consec_elev_vol_21d_diff_5d_diff},
    "vp_drv3_003_max_elev_streak_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_003_max_elev_streak_63d_5d_diff_5d_diff},
    "vp_drv3_004_elev_vol_fraction_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_004_elev_vol_fraction_21d_5d_diff_5d_diff},
    "vp_drv3_005_avg_vol_ratio_21d_vs_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_005_avg_vol_ratio_21d_vs_252d_5d_diff_5d_diff},
    "vp_drv3_006_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_006_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff},
    "vp_drv3_007_elev_vol_count_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_007_elev_vol_count_21d_5d_diff_5d_diff},
    "vp_drv3_008_elev_vol_fraction_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_008_elev_vol_fraction_63d_21d_diff_5d_diff},
    "vp_drv3_009_elev_vol_streak_zscore_5d_diff_slope": {"inputs": ["volume"], "func": vp_drv3_009_elev_vol_streak_zscore_5d_diff_slope},
    "vp_drv3_010_vol_ewm_ratio_21d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_010_vol_ewm_ratio_21d_vs_63d_5d_diff_5d_diff},
    "vp_drv3_011_elev_vol_down_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_011_elev_vol_down_fraction_21d_5d_diff_5d_diff},
    "vp_drv3_012_avg_vol_ratio_21d_vs_252d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_012_avg_vol_ratio_21d_vs_252d_slope_5d_diff},
    "vp_drv3_013_elev_vol_fraction_21d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_013_elev_vol_fraction_21d_slope_5d_diff},
    "vp_drv3_014_max_elev_streak_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_014_max_elev_streak_252d_21d_diff_5d_diff},
    "vp_drv3_015_consec_ewm5_above_ewm21_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_015_consec_ewm5_above_ewm21_5d_diff_5d_diff},
    "vp_drv3_016_elev_vol_persistence_score_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_016_elev_vol_persistence_score_5d_diff_5d_diff},
    "vp_drv3_017_avg_elev_streak_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_017_avg_elev_streak_63d_21d_diff_5d_diff},
    "vp_drv3_018_elev_vol_count_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_018_elev_vol_count_63d_21d_diff_5d_diff},
    "vp_drv3_019_vol_above_prior_day_fraction_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_019_vol_above_prior_day_fraction_5d_diff_5d_diff},
    "vp_drv3_020_avg_vol_ratio_5d_vs_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_020_avg_vol_ratio_5d_vs_21d_5d_diff_5d_diff},
    "vp_drv3_021_max_elev_streak_63d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_021_max_elev_streak_63d_slope_5d_diff},
    "vp_drv3_022_elev_vol_fraction_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_022_elev_vol_fraction_252d_21d_diff_5d_diff},
    "vp_drv3_023_elev_vol_streak_zscore_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_023_elev_vol_streak_zscore_5d_diff_5d_diff},
    "vp_drv3_024_elev_vol_down_count_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_024_elev_vol_down_count_63d_21d_diff_5d_diff},
    "vp_drv3_025_elev_vol_count_21d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_025_elev_vol_count_21d_slope_5d_diff},
    "vp_drv3_026_avg_vol_ratio_63d_vs_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_026_avg_vol_ratio_63d_vs_252d_5d_diff_5d_diff},
    "vp_drv3_027_avg_vol_ratio_63d_vs_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_027_avg_vol_ratio_63d_vs_252d_21d_diff_5d_diff},
    "vp_drv3_028_elev_vol_count_126d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_028_elev_vol_count_126d_5d_diff_5d_diff},
    "vp_drv3_029_elev_vol_fraction_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_029_elev_vol_fraction_126d_21d_diff_5d_diff},
    "vp_drv3_030_vol_ewm_ratio_5d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_030_vol_ewm_ratio_5d_vs_63d_5d_diff_5d_diff},
    "vp_drv3_031_vol_ewm_ratio_21d_vs_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_031_vol_ewm_ratio_21d_vs_252d_5d_diff_5d_diff},
    "vp_drv3_032_elev_vol_2x_count_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_032_elev_vol_2x_count_21d_5d_diff_5d_diff},
    "vp_drv3_033_vol_above_90th_pct_consec_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_033_vol_above_90th_pct_consec_5d_diff_5d_diff},
    "vp_drv3_034_elev_vol_down_fraction_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_034_elev_vol_down_fraction_63d_21d_diff_5d_diff},
    "vp_drv3_035_vol_ewm_ratio_5d_vs_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_035_vol_ewm_ratio_5d_vs_21d_21d_diff_5d_diff},
    "vp_drv3_036_elev_vol_persistence_index_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_036_elev_vol_persistence_index_5d_diff_5d_diff},
    "vp_drv3_037_vol_sum_ratio_5d_vs_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_037_vol_sum_ratio_5d_vs_21d_5d_diff_5d_diff},
    "vp_drv3_038_avg_vol_ratio_21d_vs_63d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_038_avg_vol_ratio_21d_vs_63d_slope_5d_diff},
    "vp_drv3_039_elev_vol_fraction_5d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_039_elev_vol_fraction_5d_5d_diff_5d_diff},
    "vp_drv3_040_vol_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_040_vol_cv_21d_5d_diff_5d_diff},
    "vp_drv3_041_elev_vol_count_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv3_041_elev_vol_count_21d_slope_21d_5d_diff},
    "vp_drv3_042_vol_pct_rank_current_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_042_vol_pct_rank_current_5d_diff_5d_diff},
    "vp_drv3_043_avg_vol_ratio_21d_vs_252d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv3_043_avg_vol_ratio_21d_vs_252d_slope_21d_5d_diff},
    "vp_drv3_044_elev_vol_count_63d_slope_5d_diff": {"inputs": ["volume"], "func": vp_drv3_044_elev_vol_count_63d_slope_5d_diff},
    "vp_drv3_045_elev_vol_fraction_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv3_045_elev_vol_fraction_21d_slope_63d_5d_diff},
    "vp_drv3_046_consec_elev_vol_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_046_consec_elev_vol_21d_5d_diff_slope_21d},
    "vp_drv3_047_elev_vol_fraction_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_047_elev_vol_fraction_21d_5d_diff_slope_21d},
    "vp_drv3_048_avg_vol_ratio_21d_vs_252d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_048_avg_vol_ratio_21d_vs_252d_5d_diff_slope_21d},
    "vp_drv3_049_vol_ewm_ratio_21d_vs_63d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_049_vol_ewm_ratio_21d_vs_63d_5d_diff_slope_21d},
    "vp_drv3_050_max_elev_streak_63d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_050_max_elev_streak_63d_5d_diff_slope_21d},
    "vp_drv3_051_elev_vol_2x_count_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_051_elev_vol_2x_count_63d_21d_diff_5d_diff},
    "vp_drv3_052_vol_above_prior_day_fraction_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_052_vol_above_prior_day_fraction_21d_5d_diff_5d_diff},
    "vp_drv3_053_vol_log_ratio_21d_vs_252d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_053_vol_log_ratio_21d_vs_252d_5d_diff_slope_21d},
    "vp_drv3_054_elev_vol_down_vs_up_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_054_elev_vol_down_vs_up_ratio_21d_5d_diff_5d_diff},
    "vp_drv3_055_elev_vol_start_freq_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_055_elev_vol_start_freq_63d_21d_diff_5d_diff},
    "vp_drv3_056_avg_vol_ratio_21d_vs_126d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_056_avg_vol_ratio_21d_vs_126d_5d_diff_5d_diff},
    "vp_drv3_057_elev_vol_fraction_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv3_057_elev_vol_fraction_21d_slope_21d_5d_diff},
    "vp_drv3_058_max_elev_streak_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_058_max_elev_streak_252d_5d_diff_5d_diff},
    "vp_drv3_059_avg_elev_streak_len_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_059_avg_elev_streak_len_252d_21d_diff_5d_diff},
    "vp_drv3_060_vol_pct_rank_21d_avg_in_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_060_vol_pct_rank_21d_avg_in_252d_5d_diff_5d_diff},
    "vp_drv3_061_elev_vol_down_fraction_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_061_elev_vol_down_fraction_21d_21d_diff_5d_diff},
    "vp_drv3_062_consec_ewm21_above_ewm63_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_062_consec_ewm21_above_ewm63_5d_diff_5d_diff},
    "vp_drv3_063_elev_vol_count_21d_vs_252d_avg_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_063_elev_vol_count_21d_vs_252d_avg_5d_diff_5d_diff},
    "vp_drv3_064_vol_ewm_ratio_63d_vs_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_064_vol_ewm_ratio_63d_vs_252d_5d_diff_5d_diff},
    "vp_drv3_065_elev_vol_streak_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_065_elev_vol_streak_pct_rank_252d_5d_diff_5d_diff},
    "vp_drv3_066_elev_vol_2x_fraction_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_066_elev_vol_2x_fraction_21d_5d_diff_5d_diff},
    "vp_drv3_067_vol_sum_ratio_5d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_067_vol_sum_ratio_5d_vs_63d_5d_diff_5d_diff},
    "vp_drv3_068_avg_vol_ratio_21d_vs_252d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv3_068_avg_vol_ratio_21d_vs_252d_slope_63d_5d_diff},
    "vp_drv3_069_elev_vol_down_count_63d_slope_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_069_elev_vol_down_count_63d_slope_5d_diff},
    "vp_drv3_070_elev_dollar_vol_consec_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv3_070_elev_dollar_vol_consec_5d_diff_5d_diff},
    "vp_drv3_071_vol_log_ratio_5d_vs_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_071_vol_log_ratio_5d_vs_63d_5d_diff_5d_diff},
    "vp_drv3_072_consec_vol_above_prior_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vp_drv3_072_consec_vol_above_prior_63d_5d_diff_5d_diff},
    "vp_drv3_073_elev_vol_fraction_252d_21d_diff_slope_21d": {"inputs": ["volume"], "func": vp_drv3_073_elev_vol_fraction_252d_21d_diff_slope_21d},
    "vp_drv3_074_elev_vol_streak_zscore_5d_diff_5d_diff_slope": {"inputs": ["volume"], "func": vp_drv3_074_elev_vol_streak_zscore_5d_diff_5d_diff_slope},
    "vp_drv3_075_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff_slope": {"inputs": ["volume"], "func": vp_drv3_075_avg_vol_ratio_21d_vs_63d_5d_diff_5d_diff_slope},
}
