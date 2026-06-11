"""
16_volume_persistence — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume-persistence features — velocity / acceleration
of sustained elevated-volume behavior.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vp_drv2_001_consec_elev_vol_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of current elevated-vol (21d base) streak length (velocity)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    return streak.diff(_TD_WEEK)


def vp_drv2_002_consec_elev_vol_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of current elevated-vol streak (monthly velocity)."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    return streak.diff(_TD_MON)


def vp_drv2_003_max_elev_streak_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of trailing 63-day max elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_QTR)
    return mx.diff(_TD_WEEK)


def vp_drv2_004_max_elev_streak_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of trailing 252-day max elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_YEAR)
    return mx.diff(_TD_MON)


def vp_drv2_005_elev_vol_fraction_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vp_drv2_006_elev_vol_fraction_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_QTR)
    frac = _rolling_count_true(volume > base, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vp_drv2_007_avg_vol_ratio_21d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d average volume ratio."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    return ratio.diff(_TD_WEEK)


def vp_drv2_008_avg_vol_ratio_21d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d/63d average volume ratio."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg63 = _rolling_mean(volume, _TD_QTR)
    ratio = _safe_div(avg21, avg63)
    return ratio.diff(_TD_WEEK)


def vp_drv2_009_elev_vol_count_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    return cnt.diff(_TD_WEEK)


def vp_drv2_010_elev_vol_count_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_QTR)
    return cnt.diff(_TD_MON)


def vp_drv2_011_avg_vol_ratio_21d_vs_252d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21d/252d average volume ratio."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    ratio = _safe_div(avg21, avg252)
    return _linslope(ratio, _TD_MON)


def vp_drv2_012_elev_vol_fraction_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_QTR)


def vp_drv2_013_elev_vol_streak_zscore_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of elevated-vol streak z-score."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    return z.diff(_TD_WEEK)


def vp_drv2_014_avg_vol_ratio_5d_vs_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5d/21d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vp_drv2_015_elev_vol_down_fraction_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day elevated-vol-on-down-day fraction."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vp_drv2_016_elev_vol_down_count_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day elevated-vol-on-down-day count."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    cnt = _rolling_count_true(cond, _TD_QTR)
    return cnt.diff(_TD_MON)


def vp_drv2_017_vol_ewm_ratio_21d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EMA21/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_018_consec_ewm5_above_ewm21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive EMA5>EMA21 volume streak."""
    cond = _ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def vp_drv2_019_elev_vol_fraction_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_YEAR)
    frac = _rolling_count_true(volume > base, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


def vp_drv2_020_max_elev_streak_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of trailing 63-day max elevated streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_QTR)
    return _linslope(mx, _TD_QTR)


def vp_drv2_021_avg_elev_streak_len_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of rolling average elevated-streak length (63-day)."""
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
    return avg63.diff(_TD_MON)


def vp_drv2_022_vol_above_prior_day_fraction_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of days with volume > prior-day volume."""
    cond = volume > volume.shift(1)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vp_drv2_023_elev_vol_persistence_score_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day persistence score (fraction * avg elevation * norm streak)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    avg_ratio = _rolling_mean(_safe_div(volume, base), _TD_MON)
    streak = _consec_streak(cond)
    norm_streak = _safe_div(streak, _rolling_mean(streak, _TD_YEAR).clip(lower=_EPS))
    score = frac * avg_ratio * norm_streak
    return score.diff(_TD_WEEK)


def vp_drv2_024_elev_vol_count_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    return _linslope(cnt, _TD_MON)


def vp_drv2_025_vol_log_ratio_21d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(21d avg vol / 252d avg vol)."""
    avg21 = _rolling_mean(volume, _TD_MON)
    avg252 = _rolling_mean(volume, _TD_YEAR)
    import numpy as _np
    log_ratio = _np.log(avg21.clip(lower=_EPS)) - _np.log(avg252.clip(lower=_EPS))
    return log_ratio.diff(_TD_WEEK)


# --- 2nd Derivatives 026-075 ---

def vp_drv2_026_avg_vol_ratio_63d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_027_avg_vol_ratio_63d_vs_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vp_drv2_028_elev_vol_count_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_HALF)
    return cnt.diff(_TD_WEEK)


def vp_drv2_029_elev_vol_fraction_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_HALF) / _TD_HALF
    return frac.diff(_TD_MON)


def vp_drv2_030_max_elev_streak_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day max elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_HALF)
    return mx.diff(_TD_WEEK)


def vp_drv2_031_vol_ewm_ratio_5d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EMA5/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_032_vol_ewm_ratio_21d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EMA21/EMA252 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_033_consec_elev_vol_252d_baseline_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive days volume > 252-day average."""
    base = _rolling_mean(volume, _TD_YEAR)
    streak = _consec_streak(volume > base)
    return streak.diff(_TD_WEEK)


def vp_drv2_034_elev_vol_fraction_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day elevated-vol fraction (vs 252d avg baseline)."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_WEEK)


def vp_drv2_035_avg_vol_ratio_5d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_036_elev_vol_2x_count_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_MON)
    return cnt.diff(_TD_WEEK)


def vp_drv2_037_elev_vol_2x_count_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_QTR)
    return cnt.diff(_TD_MON)


def vp_drv2_038_vol_above_90th_pct_consec_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of current streak of above-90th-pct volume days."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    streak = _consec_streak(volume > pct90)
    return streak.diff(_TD_WEEK)


def vp_drv2_039_vol_above_75th_pct_count_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of above-75th-pct volume days."""
    pct75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    cnt = _rolling_count_true(volume > pct75, _TD_QTR)
    return cnt.diff(_TD_MON)


def vp_drv2_040_vol_pct_rank_21d_avg_in_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 21-day avg volume in 252-day window."""
    avg21 = _rolling_mean(volume, _TD_MON)
    rank = avg21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vp_drv2_041_elev_vol_down_fraction_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction of elevated-vol on down-price days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = (volume > base) & (close < close.shift(1))
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vp_drv2_042_elev_vol_down_vs_up_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day elevated-vol-down/up count ratio."""
    base = _rolling_mean(volume, _TD_MON)
    dn = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_MON)
    up = _rolling_count_true((volume > base) & (close > close.shift(1)), _TD_MON)
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_WEEK)


def vp_drv2_043_vol_ewm_ratio_5d_vs_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EMA5/EMA21 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_MON))
    return ratio.diff(_TD_MON)


def vp_drv2_044_vol_log_ratio_5d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(5d avg vol / 63d avg vol)."""
    log_r = np.log(_rolling_mean(volume, _TD_WEEK).clip(lower=_EPS)) - np.log(_rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return log_r.diff(_TD_WEEK)


def vp_drv2_045_elev_vol_count_21d_vs_252d_avg_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of ratio of 21-day elevated count to 252-day avg of that count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_MON)
    avg_cnt = _rolling_mean(cnt, _TD_YEAR)
    ratio = _safe_div(cnt, avg_cnt)
    return ratio.diff(_TD_WEEK)


def vp_drv2_046_consec_ewm21_above_ewm63_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of consecutive days EMA21 vol > EMA63 vol."""
    cond = _ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def vp_drv2_047_elev_vol_streak_pct_rank_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of elevated-vol streak in 252-day window."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    rank = streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vp_drv2_048_vol_sum_ratio_5d_vs_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day/21-day total volume ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_WEEK), _rolling_sum(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vp_drv2_049_avg_vol_ratio_21d_vs_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d/126d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_HALF))
    return ratio.diff(_TD_WEEK)


def vp_drv2_050_elev_vol_fraction_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_MON)


def vp_drv2_051_avg_vol_ratio_21d_vs_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of 21d/63d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    return _linslope(ratio, _TD_QTR)


def vp_drv2_052_elev_vol_count_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of 63-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_QTR)
    return _linslope(cnt, _TD_QTR)


def vp_drv2_053_vol_above_prior_day_fraction_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction of days with volume > prior-day volume."""
    cond = volume > volume.shift(1)
    frac = _rolling_count_true(cond, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vp_drv2_054_elev_vol_persistence_index_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the persistence-index (streak * fraction * z-score product)."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    streak = _consec_streak(cond)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s).fillna(0.0)
    idx = frac * z
    return idx.diff(_TD_WEEK)


def vp_drv2_055_max_elev_streak_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of trailing 252-day max elevated-vol streak."""
    base = _rolling_mean(volume, _TD_MON)
    mx = _rolling_max_streak(volume > base, _TD_YEAR)
    return mx.diff(_TD_WEEK)


def vp_drv2_056_avg_elev_streak_len_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day average elevated-streak length."""
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
    return avg252.diff(_TD_MON)


def vp_drv2_057_elev_vol_2x_fraction_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction with volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def vp_drv2_058_elev_vol_2x_fraction_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction with volume > 2x average."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > 2.0 * base.replace(0, np.nan), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def vp_drv2_059_vol_ewm_ratio_21d_vs_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EMA21/EMA63 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vp_drv2_060_elev_vol_start_freq_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of count of new elevated-vol streak starts in 63 days."""
    base = _rolling_mean(volume, _TD_MON)
    cond = volume > base
    is_start = (cond & ~cond.shift(1).fillna(False)).astype(float)
    cnt = _rolling_sum(is_start, _TD_QTR)
    return cnt.diff(_TD_MON)


def vp_drv2_061_avg_vol_ratio_21d_vs_252d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of 21d/252d average volume ratio."""
    ratio = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))
    return _linslope(ratio, _TD_QTR)


def vp_drv2_062_elev_vol_fraction_5d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day elevated-vol fraction."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_WEEK) / _TD_WEEK
    return frac.diff(_TD_WEEK)


def vp_drv2_063_vol_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume coefficient of variation."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vp_drv2_064_vol_pct_rank_current_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of current day's volume percentile rank in 252-day window."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vp_drv2_065_elev_vol_count_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day elevated-vol day count."""
    base = _rolling_mean(volume, _TD_MON)
    cnt = _rolling_count_true(volume > base, _TD_YEAR)
    return cnt.diff(_TD_MON)


def vp_drv2_066_vol_above_90th_pct_count_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of above-90th-pct volume days."""
    pct90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    cnt = _rolling_count_true(volume > pct90, _TD_MON)
    return cnt.diff(_TD_WEEK)


def vp_drv2_067_elev_vol_on_down_x_streak_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the elev-vol-down-day count times current streak product."""
    base = _rolling_mean(volume, _TD_MON)
    dn_cnt = _rolling_count_true((volume > base) & (close < close.shift(1)), _TD_MON)
    streak = _consec_streak(volume > base)
    product = dn_cnt * streak
    return product.diff(_TD_WEEK)


def vp_drv2_068_vol_log_ratio_21d_vs_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of log(21d avg vol / 252d avg vol)."""
    log_r = np.log(_rolling_mean(volume, _TD_MON).clip(lower=_EPS)) - np.log(_rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))
    return log_r.diff(_TD_MON)


def vp_drv2_069_consec_vol_above_prior_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of streak of days vol > 63-day lagged average."""
    base_lagged = _rolling_mean(volume, _TD_QTR).shift(_TD_QTR)
    streak = _consec_streak(volume > base_lagged)
    return streak.diff(_TD_WEEK)


def vp_drv2_070_elev_dollar_vol_consec_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of current consecutive elevated-dollar-volume streak."""
    dv = close * volume
    streak = _consec_streak(dv > _rolling_mean(dv, _TD_MON))
    return streak.diff(_TD_WEEK)


def vp_drv2_071_avg_dollar_vol_ratio_21d_vs_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d average dollar-volume ratio."""
    dv = close * volume
    ratio = _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_072_vol_ewm_ratio_63d_vs_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EMA63/EMA252 volume ratio."""
    ratio = _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_073_elev_vol_fraction_21d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope over 252 days of 21-day elevated-vol fraction (long trend)."""
    base = _rolling_mean(volume, _TD_MON)
    frac = _rolling_count_true(volume > base, _TD_MON) / _TD_MON
    return _linslope(frac, _TD_YEAR)


def vp_drv2_074_vol_sum_ratio_5d_vs_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day/63-day total volume ratio."""
    ratio = _safe_div(_rolling_sum(volume, _TD_WEEK), _rolling_sum(volume, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def vp_drv2_075_elev_vol_streak_norm_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of current elevated-streak normalized by 252-day average streak length."""
    base = _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(volume > base)
    avg = _rolling_mean(streak, _TD_YEAR)
    norm = _safe_div(streak, avg)
    return norm.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PERSISTENCE_REGISTRY_2ND_DERIVATIVES = {
    "vp_drv2_001_consec_elev_vol_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_001_consec_elev_vol_21d_5d_diff},
    "vp_drv2_002_consec_elev_vol_21d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_002_consec_elev_vol_21d_21d_diff},
    "vp_drv2_003_max_elev_streak_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_003_max_elev_streak_63d_5d_diff},
    "vp_drv2_004_max_elev_streak_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_004_max_elev_streak_252d_21d_diff},
    "vp_drv2_005_elev_vol_fraction_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_005_elev_vol_fraction_21d_5d_diff},
    "vp_drv2_006_elev_vol_fraction_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_006_elev_vol_fraction_63d_21d_diff},
    "vp_drv2_007_avg_vol_ratio_21d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_007_avg_vol_ratio_21d_vs_252d_5d_diff},
    "vp_drv2_008_avg_vol_ratio_21d_vs_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_008_avg_vol_ratio_21d_vs_63d_5d_diff},
    "vp_drv2_009_elev_vol_count_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_009_elev_vol_count_21d_5d_diff},
    "vp_drv2_010_elev_vol_count_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_010_elev_vol_count_63d_21d_diff},
    "vp_drv2_011_avg_vol_ratio_21d_vs_252d_slope_21d": {"inputs": ["volume"], "func": vp_drv2_011_avg_vol_ratio_21d_vs_252d_slope_21d},
    "vp_drv2_012_elev_vol_fraction_21d_slope_63d": {"inputs": ["volume"], "func": vp_drv2_012_elev_vol_fraction_21d_slope_63d},
    "vp_drv2_013_elev_vol_streak_zscore_5d_diff": {"inputs": ["volume"], "func": vp_drv2_013_elev_vol_streak_zscore_5d_diff},
    "vp_drv2_014_avg_vol_ratio_5d_vs_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_014_avg_vol_ratio_5d_vs_21d_5d_diff},
    "vp_drv2_015_elev_vol_down_fraction_21d_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_015_elev_vol_down_fraction_21d_5d_diff},
    "vp_drv2_016_elev_vol_down_count_63d_21d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_016_elev_vol_down_count_63d_21d_diff},
    "vp_drv2_017_vol_ewm_ratio_21d_vs_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_017_vol_ewm_ratio_21d_vs_63d_5d_diff},
    "vp_drv2_018_consec_ewm5_above_ewm21_5d_diff": {"inputs": ["volume"], "func": vp_drv2_018_consec_ewm5_above_ewm21_5d_diff},
    "vp_drv2_019_elev_vol_fraction_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_019_elev_vol_fraction_252d_21d_diff},
    "vp_drv2_020_max_elev_streak_63d_slope_63d": {"inputs": ["volume"], "func": vp_drv2_020_max_elev_streak_63d_slope_63d},
    "vp_drv2_021_avg_elev_streak_len_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_021_avg_elev_streak_len_63d_21d_diff},
    "vp_drv2_022_vol_above_prior_day_fraction_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_022_vol_above_prior_day_fraction_21d_5d_diff},
    "vp_drv2_023_elev_vol_persistence_score_5d_diff": {"inputs": ["volume"], "func": vp_drv2_023_elev_vol_persistence_score_5d_diff},
    "vp_drv2_024_elev_vol_count_21d_slope_21d": {"inputs": ["volume"], "func": vp_drv2_024_elev_vol_count_21d_slope_21d},
    "vp_drv2_025_vol_log_ratio_21d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_025_vol_log_ratio_21d_vs_252d_5d_diff},
    "vp_drv2_026_avg_vol_ratio_63d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_026_avg_vol_ratio_63d_vs_252d_5d_diff},
    "vp_drv2_027_avg_vol_ratio_63d_vs_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_027_avg_vol_ratio_63d_vs_252d_21d_diff},
    "vp_drv2_028_elev_vol_count_126d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_028_elev_vol_count_126d_5d_diff},
    "vp_drv2_029_elev_vol_fraction_126d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_029_elev_vol_fraction_126d_21d_diff},
    "vp_drv2_030_max_elev_streak_126d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_030_max_elev_streak_126d_5d_diff},
    "vp_drv2_031_vol_ewm_ratio_5d_vs_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_031_vol_ewm_ratio_5d_vs_63d_5d_diff},
    "vp_drv2_032_vol_ewm_ratio_21d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_032_vol_ewm_ratio_21d_vs_252d_5d_diff},
    "vp_drv2_033_consec_elev_vol_252d_baseline_5d_diff": {"inputs": ["volume"], "func": vp_drv2_033_consec_elev_vol_252d_baseline_5d_diff},
    "vp_drv2_034_elev_vol_fraction_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_034_elev_vol_fraction_252d_5d_diff},
    "vp_drv2_035_avg_vol_ratio_5d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_035_avg_vol_ratio_5d_vs_252d_5d_diff},
    "vp_drv2_036_elev_vol_2x_count_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_036_elev_vol_2x_count_21d_5d_diff},
    "vp_drv2_037_elev_vol_2x_count_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_037_elev_vol_2x_count_63d_21d_diff},
    "vp_drv2_038_vol_above_90th_pct_consec_5d_diff": {"inputs": ["volume"], "func": vp_drv2_038_vol_above_90th_pct_consec_5d_diff},
    "vp_drv2_039_vol_above_75th_pct_count_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_039_vol_above_75th_pct_count_63d_21d_diff},
    "vp_drv2_040_vol_pct_rank_21d_avg_in_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_040_vol_pct_rank_21d_avg_in_252d_5d_diff},
    "vp_drv2_041_elev_vol_down_fraction_63d_21d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_041_elev_vol_down_fraction_63d_21d_diff},
    "vp_drv2_042_elev_vol_down_vs_up_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_042_elev_vol_down_vs_up_ratio_21d_5d_diff},
    "vp_drv2_043_vol_ewm_ratio_5d_vs_21d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_043_vol_ewm_ratio_5d_vs_21d_21d_diff},
    "vp_drv2_044_vol_log_ratio_5d_vs_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_044_vol_log_ratio_5d_vs_63d_5d_diff},
    "vp_drv2_045_elev_vol_count_21d_vs_252d_avg_5d_diff": {"inputs": ["volume"], "func": vp_drv2_045_elev_vol_count_21d_vs_252d_avg_5d_diff},
    "vp_drv2_046_consec_ewm21_above_ewm63_5d_diff": {"inputs": ["volume"], "func": vp_drv2_046_consec_ewm21_above_ewm63_5d_diff},
    "vp_drv2_047_elev_vol_streak_pct_rank_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_047_elev_vol_streak_pct_rank_252d_5d_diff},
    "vp_drv2_048_vol_sum_ratio_5d_vs_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_048_vol_sum_ratio_5d_vs_21d_5d_diff},
    "vp_drv2_049_avg_vol_ratio_21d_vs_126d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_049_avg_vol_ratio_21d_vs_126d_5d_diff},
    "vp_drv2_050_elev_vol_fraction_21d_slope_21d": {"inputs": ["volume"], "func": vp_drv2_050_elev_vol_fraction_21d_slope_21d},
    "vp_drv2_051_avg_vol_ratio_21d_vs_63d_slope_63d": {"inputs": ["volume"], "func": vp_drv2_051_avg_vol_ratio_21d_vs_63d_slope_63d},
    "vp_drv2_052_elev_vol_count_63d_slope_63d": {"inputs": ["volume"], "func": vp_drv2_052_elev_vol_count_63d_slope_63d},
    "vp_drv2_053_vol_above_prior_day_fraction_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_053_vol_above_prior_day_fraction_63d_21d_diff},
    "vp_drv2_054_elev_vol_persistence_index_5d_diff": {"inputs": ["volume"], "func": vp_drv2_054_elev_vol_persistence_index_5d_diff},
    "vp_drv2_055_max_elev_streak_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_055_max_elev_streak_252d_5d_diff},
    "vp_drv2_056_avg_elev_streak_len_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_056_avg_elev_streak_len_252d_21d_diff},
    "vp_drv2_057_elev_vol_2x_fraction_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_057_elev_vol_2x_fraction_21d_5d_diff},
    "vp_drv2_058_elev_vol_2x_fraction_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_058_elev_vol_2x_fraction_63d_21d_diff},
    "vp_drv2_059_vol_ewm_ratio_21d_vs_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_059_vol_ewm_ratio_21d_vs_63d_21d_diff},
    "vp_drv2_060_elev_vol_start_freq_63d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_060_elev_vol_start_freq_63d_21d_diff},
    "vp_drv2_061_avg_vol_ratio_21d_vs_252d_slope_63d": {"inputs": ["volume"], "func": vp_drv2_061_avg_vol_ratio_21d_vs_252d_slope_63d},
    "vp_drv2_062_elev_vol_fraction_5d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_062_elev_vol_fraction_5d_5d_diff},
    "vp_drv2_063_vol_cv_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_063_vol_cv_21d_5d_diff},
    "vp_drv2_064_vol_pct_rank_current_5d_diff": {"inputs": ["volume"], "func": vp_drv2_064_vol_pct_rank_current_5d_diff},
    "vp_drv2_065_elev_vol_count_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_065_elev_vol_count_252d_21d_diff},
    "vp_drv2_066_vol_above_90th_pct_count_21d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_066_vol_above_90th_pct_count_21d_5d_diff},
    "vp_drv2_067_elev_vol_on_down_x_streak_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_067_elev_vol_on_down_x_streak_5d_diff},
    "vp_drv2_068_vol_log_ratio_21d_vs_252d_21d_diff": {"inputs": ["volume"], "func": vp_drv2_068_vol_log_ratio_21d_vs_252d_21d_diff},
    "vp_drv2_069_consec_vol_above_prior_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_069_consec_vol_above_prior_63d_5d_diff},
    "vp_drv2_070_elev_dollar_vol_consec_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_070_elev_dollar_vol_consec_5d_diff},
    "vp_drv2_071_avg_dollar_vol_ratio_21d_vs_252d_5d_diff": {"inputs": ["close", "volume"], "func": vp_drv2_071_avg_dollar_vol_ratio_21d_vs_252d_5d_diff},
    "vp_drv2_072_vol_ewm_ratio_63d_vs_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_072_vol_ewm_ratio_63d_vs_252d_5d_diff},
    "vp_drv2_073_elev_vol_fraction_21d_slope_252d": {"inputs": ["volume"], "func": vp_drv2_073_elev_vol_fraction_21d_slope_252d},
    "vp_drv2_074_vol_sum_ratio_5d_vs_63d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_074_vol_sum_ratio_5d_vs_63d_5d_diff},
    "vp_drv2_075_elev_vol_streak_norm_252d_5d_diff": {"inputs": ["volume"], "func": vp_drv2_075_elev_vol_streak_norm_252d_5d_diff},
}
