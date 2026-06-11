"""
08_decline_streaks — Extended Features 001-075
Domain: consecutive down days / weeks / months — additional depth
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: within each True run the cumsum gives run length."""
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
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_streak_std(cond: pd.Series, w: int) -> pd.Series:
    """Std of streak lengths within trailing w periods (scalar apply)."""
    def _std_run(arr):
        runs = []
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur)
                cur = 0
        if cur > 0:
            runs.append(cur)
        if len(runs) < 2:
            return 0.0
        a = np.array(runs, dtype=float)
        return float(a.std())
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_std_run, raw=True)


def _rolling_streak_count(cond: pd.Series, w: int) -> pd.Series:
    """Number of distinct True runs within trailing w periods (scalar apply)."""
    def _count_runs(arr):
        runs = 0
        in_run = False
        for v in arr:
            if v and not in_run:
                runs += 1
                in_run = True
            elif not v:
                in_run = False
        return float(runs)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_count_runs, raw=True)


def _rolling_gap_between_streaks(cond: pd.Series, w: int) -> pd.Series:
    """Average gap (False run length) between True runs within trailing w periods."""
    def _avg_gap(arr):
        gaps = []
        cur_gap = 0
        started = False
        in_run = False
        for v in arr:
            if v:
                if started and cur_gap > 0:
                    gaps.append(cur_gap)
                cur_gap = 0
                in_run = True
                started = True
            else:
                if started:
                    cur_gap += 1
                in_run = False
        if len(gaps) == 0:
            return np.nan
        return float(np.mean(gaps))
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_avg_gap, raw=True)


def _vwap_proxy(close: pd.Series, high: pd.Series, low: pd.Series,
                volume: pd.Series, w: int) -> pd.Series:
    """Rolling VWAP proxy: sum(typical_price * volume) / sum(volume) over w days."""
    tp = (high + low + close) / 3.0
    return _safe_div(_rolling_sum(tp * volume, w), _rolling_sum(volume, w))


# ── Feature functions ext_001-075 ─────────────────────────────────────────────

# --- Group A (ext_001-010): 3-day and bi-period aggregation streaks ---

def dstk_ext_001_consec_down_3d_bars(close: pd.Series) -> pd.Series:
    """Current streak of consecutive 3-day bars where close[t] < close[t-3]."""
    cond = close < close.shift(3)
    return _consec_streak(cond)


def dstk_ext_002_max_down_3d_bars_63d(close: pd.Series) -> pd.Series:
    """Maximum streak of consecutive 3-day down bars within trailing 63 days."""
    cond = close < close.shift(3)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_ext_003_max_down_3d_bars_252d(close: pd.Series) -> pd.Series:
    """Maximum streak of consecutive 3-day down bars within trailing 252 days."""
    cond = close < close.shift(3)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_ext_004_consec_down_3d_bars_norm_252d(close: pd.Series) -> pd.Series:
    """Current 3-day-bar down streak normalized by 252-day average."""
    streak = dstk_ext_001_consec_down_3d_bars(close)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_ext_005_consec_down_biweekly_bars(close: pd.Series) -> pd.Series:
    """Streak of consecutive 10-day (2-week) bars where close < close 10 days prior."""
    cond = close.pct_change(10) < 0
    return _consec_streak(cond)


def dstk_ext_006_consec_down_quarterly_bars(close: pd.Series) -> pd.Series:
    """Streak of consecutive 63-day bars where close < close 63 days prior."""
    cond = close.pct_change(_TD_QTR) < 0
    return _consec_streak(cond)


def dstk_ext_007_max_down_quarterly_252d(close: pd.Series) -> pd.Series:
    """Maximum streak of consecutive quarterly down bars within trailing 252 days."""
    cond = close.pct_change(_TD_QTR) < 0
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_ext_008_down_qtr_streak_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current quarterly down streak within trailing 504-day series."""
    streak = dstk_ext_006_consec_down_quarterly_bars(close)
    return streak.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def dstk_ext_009_consec_down_42d_bars(close: pd.Series) -> pd.Series:
    """Streak of consecutive 42-day (2-month) bars where close < close 42 days prior."""
    cond = close.pct_change(42) < 0
    return _consec_streak(cond)


def dstk_ext_010_consec_down_3d_bars_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 3-day-bar down streak within trailing 252-day series."""
    streak = dstk_ext_001_consec_down_3d_bars(close)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (ext_011-018): Severity-weighted streaks ---

def dstk_ext_011_severity_weighted_streak_current(close: pd.Series) -> pd.Series:
    """Sum of squared daily log-returns during current down streak (nonlinear severity)."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    sq_loss = (daily_log ** 2).where(cond, 0.0)
    group = (~cond).cumsum()
    return sq_loss.groupby(group).cumsum()


def dstk_ext_012_severity_weighted_streak_norm_252d(close: pd.Series) -> pd.Series:
    """Current severity-weighted streak normalized by 252-day average."""
    sev = dstk_ext_011_severity_weighted_streak_current(close)
    avg = _rolling_mean(sev, _TD_YEAR)
    return _safe_div(sev, avg)


def dstk_ext_013_cum_loss_per_streak_day_squared(close: pd.Series) -> pd.Series:
    """Squared cumulative log-loss divided by streak length (accelerating severity)."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    group = (~cond).cumsum()
    cum = daily_log.groupby(group).cumsum().where(cond, 0.0)
    length = _consec_streak(cond).replace(0, np.nan)
    return _safe_div(cum ** 2, length)


def dstk_ext_014_max_severity_weighted_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum severity-weighted streak value within trailing 63 days."""
    sev = dstk_ext_011_severity_weighted_streak_current(close)
    return _rolling_max(sev, _TD_QTR)


def dstk_ext_015_max_severity_weighted_streak_252d(close: pd.Series) -> pd.Series:
    """Maximum severity-weighted streak value within trailing 252 days."""
    sev = dstk_ext_011_severity_weighted_streak_current(close)
    return _rolling_max(sev, _TD_YEAR)


def dstk_ext_016_severity_weighted_streak_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of severity-weighted streak relative to 252-day distribution."""
    sev = dstk_ext_011_severity_weighted_streak_current(close)
    m = _rolling_mean(sev, _TD_YEAR)
    s = _rolling_std(sev, _TD_YEAR)
    return _safe_div(sev - m, s)


def dstk_ext_017_vol_weighted_cum_loss_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume-weighted log-loss during current consecutive down streak."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = close < close.shift(1)
    wt_loss = (daily_log * vol_norm).where(cond, 0.0)
    group = (~cond).cumsum()
    return wt_loss.groupby(group).cumsum()


def dstk_ext_018_vol_weighted_severity_norm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted cum-loss streak normalized by 252-day average."""
    sev = dstk_ext_017_vol_weighted_cum_loss_streak(close, volume)
    avg = _rolling_mean(sev, _TD_YEAR)
    return _safe_div(sev, avg)


# --- Group C (ext_019-027): Streak-length distribution moments ---

def dstk_ext_019_streak_len_std_63d(close: pd.Series) -> pd.Series:
    """Standard deviation of down-day streak lengths within trailing 63 days."""
    cond = close < close.shift(1)
    return _rolling_streak_std(cond, _TD_QTR)


def dstk_ext_020_streak_len_std_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of down-day streak lengths within trailing 252 days."""
    cond = close < close.shift(1)
    return _rolling_streak_std(cond, _TD_YEAR)


def dstk_ext_021_streak_len_cv_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of down-streak lengths, trailing 252 days."""
    cond = close < close.shift(1)
    std = _rolling_streak_std(cond, _TD_YEAR)
    mn = _rolling_mean(_consec_streak(cond), _TD_YEAR)
    return _safe_div(std, mn)


def dstk_ext_022_streak_count_21d(close: pd.Series) -> pd.Series:
    """Number of distinct down-day streaks started within trailing 21 days."""
    cond = close < close.shift(1)
    return _rolling_streak_count(cond, _TD_MON)


def dstk_ext_023_streak_count_252d(close: pd.Series) -> pd.Series:
    """Number of distinct down-day streaks within trailing 252 days."""
    cond = close < close.shift(1)
    return _rolling_streak_count(cond, _TD_YEAR)


def dstk_ext_024_avg_gap_between_streaks_63d(close: pd.Series) -> pd.Series:
    """Average gap (up-day run length) between down-streaks within trailing 63 days."""
    cond = close < close.shift(1)
    return _rolling_gap_between_streaks(cond, _TD_QTR)


def dstk_ext_025_avg_gap_between_streaks_252d(close: pd.Series) -> pd.Series:
    """Average gap (up-day run length) between down-streaks within trailing 252 days."""
    cond = close < close.shift(1)
    return _rolling_gap_between_streaks(cond, _TD_YEAR)


def dstk_ext_026_streak_to_gap_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day max down-streak to avg gap between streaks (compression)."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_QTR)
    gap = _rolling_gap_between_streaks(cond, _TD_QTR)
    return _safe_div(mx, gap)


def dstk_ext_027_streak_to_gap_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252-day max down-streak to avg gap between streaks."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_YEAR)
    gap = _rolling_gap_between_streaks(cond, _TD_YEAR)
    return _safe_div(mx, gap)


# --- Group D (ext_028-033): Max historical vs current streak framing ---

def dstk_ext_028_current_vs_expanding_max_streak(close: pd.Series) -> pd.Series:
    """Current down streak as fraction of expanding all-time maximum streak."""
    streak = _consec_streak(close < close.shift(1))
    exp_max = streak.expanding(min_periods=1).max()
    return _safe_div(streak, exp_max)


def dstk_ext_029_current_streak_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of current streak length (all-history rank)."""
    streak = _consec_streak(close < close.shift(1))
    return streak.expanding(min_periods=5).rank(pct=True)


def dstk_ext_030_streak_count_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day streak frequency (annualized) to 252-day streak frequency."""
    cond = close < close.shift(1)
    cnt21 = _rolling_streak_count(cond, _TD_MON)
    cnt252 = _rolling_streak_count(cond, _TD_YEAR)
    return _safe_div(cnt21 * (_TD_YEAR / float(_TD_MON)), cnt252)


def dstk_ext_031_streak_count_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day streak frequency (annualized) to 252-day streak frequency."""
    cond = close < close.shift(1)
    cnt63 = _rolling_streak_count(cond, _TD_QTR)
    cnt252 = _rolling_streak_count(cond, _TD_YEAR)
    return _safe_div(cnt63 * (_TD_YEAR / float(_TD_QTR)), cnt252)


def dstk_ext_032_streak_count_252d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day streak count (all-history frequency rank)."""
    cond = close < close.shift(1)
    cnt252 = _rolling_streak_count(cond, _TD_YEAR)
    return cnt252.expanding(min_periods=5).rank(pct=True)


# --- Group E (ext_033-040): Streak-of-streaks and cluster indicators ---

def dstk_ext_033_streak_of_streaks_current(close: pd.Series) -> pd.Series:
    """Streak of consecutive 5-day windows each containing at least 3 down days."""
    cond = close < close.shift(1)
    has_dense_week = _rolling_count_true(cond, _TD_WEEK) >= 3
    return _consec_streak(has_dense_week)


def dstk_ext_034_cluster_density_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day window that falls inside a down-streak of length >= 2."""
    streak = _consec_streak(close < close.shift(1))
    in_streak2 = (streak >= 2).astype(float)
    return _rolling_sum(in_streak2, _TD_MON) / _TD_MON


def dstk_ext_035_cluster_density_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day window that falls inside a down-streak of length >= 2."""
    streak = _consec_streak(close < close.shift(1))
    in_streak2 = (streak >= 2).astype(float)
    return _rolling_sum(in_streak2, _TD_QTR) / _TD_QTR


def dstk_ext_036_max_streak_cluster_63d(close: pd.Series) -> pd.Series:
    """Max consecutive-True run of streak >= 2 within trailing 63 days."""
    cond = _consec_streak(close < close.shift(1)) >= 2
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_ext_037_no_up_day_in_10d_flag(close: pd.Series) -> pd.Series:
    """Flag: zero up-days (close > prior close) in last 10 trading days."""
    ret = close.pct_change(1)
    return (_rolling_count_true(ret > 0, 10) == 0).astype(float)


def dstk_ext_038_no_up_day_in_15d_flag(close: pd.Series) -> pd.Series:
    """Flag: zero up-days in last 15 trading days."""
    ret = close.pct_change(1)
    return (_rolling_count_true(ret > 0, 15) == 0).astype(float)


def dstk_ext_039_up_day_count_21d(close: pd.Series) -> pd.Series:
    """Raw count of up-days in last 21 days (lower = more distressed)."""
    ret = close.pct_change(1)
    return _rolling_count_true(ret > 0, _TD_MON)


def dstk_ext_040_up_day_count_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day up-day count relative to 252-day distribution."""
    ret = close.pct_change(1)
    cnt21 = _rolling_count_true(ret > 0, _TD_MON)
    m = _rolling_mean(cnt21, _TD_YEAR)
    s = _rolling_std(cnt21, _TD_YEAR)
    return _safe_div(cnt21 - m, s)


# --- Group F (ext_041-045): Close below VWAP-proxy streaks ---

def dstk_ext_041_consec_close_below_vwap_5d(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of consecutive days close < 5-day VWAP proxy (typical price * vol)."""
    vwap = _vwap_proxy(close, high, low, volume, _TD_WEEK)
    return _consec_streak(close < vwap)


def dstk_ext_042_consec_close_below_vwap_21d(close: pd.Series, high: pd.Series,
                                               low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of consecutive days close < 21-day VWAP proxy."""
    vwap = _vwap_proxy(close, high, low, volume, _TD_MON)
    return _consec_streak(close < vwap)


def dstk_ext_043_consec_close_below_vwap_63d(close: pd.Series, high: pd.Series,
                                               low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of consecutive days close < 63-day VWAP proxy."""
    vwap = _vwap_proxy(close, high, low, volume, _TD_QTR)
    return _consec_streak(close < vwap)


def dstk_ext_044_max_below_vwap21_streak_252d(close: pd.Series, high: pd.Series,
                                                low: pd.Series, volume: pd.Series) -> pd.Series:
    """Max streak of close below 21-day VWAP proxy within trailing 252 days."""
    vwap = _vwap_proxy(close, high, low, volume, _TD_MON)
    return _rolling_max_streak(close < vwap, _TD_YEAR)


def dstk_ext_045_below_vwap21_streak_norm_252d(close: pd.Series, high: pd.Series,
                                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """Below-21d-VWAP streak normalized by 252-day average."""
    vwap = _vwap_proxy(close, high, low, volume, _TD_MON)
    streak = _consec_streak(close < vwap)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


# --- Group G (ext_046-053): Extended lower-high/lower-low streak variants ---

def dstk_ext_046_consec_lower_highs_and_lower_lows_norm_252d(high: pd.Series,
                                                               low: pd.Series) -> pd.Series:
    """Streak of simultaneous lower-highs AND lower-lows, normalized by 252-day average."""
    cond = (low < low.shift(1)) & (high < high.shift(1))
    streak = _consec_streak(cond)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_ext_047_max_lower_high_streak_252d(high: pd.Series) -> pd.Series:
    """Maximum consecutive lower-high run within trailing 252 days."""
    cond = high < high.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_ext_048_lower_high_streak_zscore_252d(high: pd.Series) -> pd.Series:
    """Z-score of current lower-high streak relative to 252-day distribution."""
    streak = _consec_streak(high < high.shift(1))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def dstk_ext_049_consec_lower_close_and_lower_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """Streak of days with both a lower close AND a lower high (down-trending)."""
    cond = (close < close.shift(1)) & (high < high.shift(1))
    return _consec_streak(cond)


def dstk_ext_050_consec_new_10d_low_intraday(low: pd.Series) -> pd.Series:
    """Consecutive days where intraday low is below prior 10-day low."""
    roll_min = low.shift(1).rolling(10, min_periods=5).min()
    cond = low < roll_min
    return _consec_streak(cond)


def dstk_ext_051_consec_new_63d_low_intraday(low: pd.Series) -> pd.Series:
    """Consecutive days where intraday low is below prior 63-day low."""
    roll_min = low.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    cond = low < roll_min
    return _consec_streak(cond)


def dstk_ext_052_consec_new_252d_low_intraday(low: pd.Series) -> pd.Series:
    """Consecutive days where intraday low is below prior 252-day low."""
    roll_min = low.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    cond = low < roll_min
    return _consec_streak(cond)


def dstk_ext_053_lower_low_streak_pct_rank_252d(low: pd.Series) -> pd.Series:
    """Percentile rank of current lower-low streak within trailing 252-day series."""
    streak = _consec_streak(low < low.shift(1))
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (ext_054-060): Down-volume streak extensions ---

def dstk_ext_054_max_down_volume_streak_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive declining-volume run within trailing 63 days."""
    cond = volume < volume.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_ext_055_max_down_volume_streak_252d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive declining-volume run within trailing 252 days."""
    cond = volume < volume.shift(1)
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_ext_056_down_vol_streak_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of current declining-volume streak relative to 252-day distribution."""
    streak = _consec_streak(volume < volume.shift(1))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def dstk_ext_057_consec_below_avg_volume_days(volume: pd.Series) -> pd.Series:
    """Streak of days where volume is below its 21-day average (volume drought)."""
    avg = _rolling_mean(volume, _TD_MON)
    cond = volume < avg
    return _consec_streak(cond)


def dstk_ext_058_max_below_avg_vol_streak_252d(volume: pd.Series) -> pd.Series:
    """Max streak of below-21d-average-volume days within trailing 252 days."""
    avg = _rolling_mean(volume, _TD_MON)
    cond = volume < avg
    return _rolling_max_streak(cond, _TD_YEAR)


def dstk_ext_059_consec_price_down_vol_up(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of days: price down AND volume higher than prior day (distribution days)."""
    cond = (close < close.shift(1)) & (volume > volume.shift(1))
    return _consec_streak(cond)


def dstk_ext_060_max_distribution_day_streak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive distribution-day streak (price down + volume up) in 63 days."""
    cond = (close < close.shift(1)) & (volume > volume.shift(1))
    return _rolling_max_streak(cond, _TD_QTR)


# --- Group I (ext_061-065): Streak frequency and density statistics ---

def dstk_ext_061_streak_freq_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of annualized 21-day streak count to 63-day streak count (recency surge)."""
    cond = close < close.shift(1)
    cnt21 = _rolling_streak_count(cond, _TD_MON)
    cnt63 = _rolling_streak_count(cond, _TD_QTR)
    return _safe_div(cnt21 * (_TD_QTR / float(_TD_MON)), cnt63)


def dstk_ext_062_streak_freq_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day streak count within trailing 252-day series."""
    cond = close < close.shift(1)
    cnt21 = _rolling_streak_count(cond, _TD_MON)
    return cnt21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dstk_ext_063_avg_gap_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day avg gap between streaks within 252-day history."""
    cond = close < close.shift(1)
    gap = _rolling_gap_between_streaks(cond, _TD_QTR)
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dstk_ext_064_cluster_density_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day cluster density within 252-day distribution."""
    streak = _consec_streak(close < close.shift(1))
    in_streak2 = (streak >= 2).astype(float)
    density = _rolling_sum(in_streak2, _TD_MON) / _TD_MON
    m = _rolling_mean(density, _TD_YEAR)
    s = _rolling_std(density, _TD_YEAR)
    return _safe_div(density - m, s)


def dstk_ext_065_streak_to_gap_ratio_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day streak-to-gap ratio within trailing 252-day series."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_QTR)
    gap = _rolling_gap_between_streaks(cond, _TD_QTR)
    ratio = _safe_div(mx, gap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group J (ext_066-075): Statistical transforms and open/high-based streaks ---

def dstk_ext_066_streak_severity_per_down_day_63d(close: pd.Series) -> pd.Series:
    """Average down-day log-loss severity per down day over 63 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    down_days = _rolling_count_true(cond, _TD_QTR)
    sev63 = daily_log.where(daily_log < 0, 0.0).rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(sev63, down_days)


def dstk_ext_067_streak_severity_per_down_day_252d(close: pd.Series) -> pd.Series:
    """Average down-day log-loss severity per down day over 252 days."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    cond = close < close.shift(1)
    down_days = _rolling_count_true(cond, _TD_YEAR)
    sev252 = daily_log.where(daily_log < 0, 0.0).rolling(_TD_YEAR, min_periods=_TD_QTR).sum()
    return _safe_div(sev252, down_days)


def dstk_ext_068_down_streak_entropy_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of down/up-day distribution in trailing 63 days.
    Low entropy means more directional (persistent decline)."""
    ret = close.pct_change(1)
    p_d = (_rolling_count_true(ret < 0, _TD_QTR) / _TD_QTR).clip(lower=_EPS, upper=1 - _EPS)
    p_u = (1.0 - p_d).clip(lower=_EPS, upper=1 - _EPS)
    return -(p_d * np.log(p_d) + p_u * np.log(p_u))


def dstk_ext_069_down_streak_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of down/up-day distribution in trailing 252 days."""
    ret = close.pct_change(1)
    p_d = (_rolling_count_true(ret < 0, _TD_YEAR) / _TD_YEAR).clip(lower=_EPS, upper=1 - _EPS)
    p_u = (1.0 - p_d).clip(lower=_EPS, upper=1 - _EPS)
    return -(p_d * np.log(p_d) + p_u * np.log(p_u))


def dstk_ext_070_bear_candle_streak_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current bear-candle streak (close < open) normalized by 252-day average."""
    streak = _consec_streak(close < open)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def dstk_ext_071_max_bear_candle_vs_expanding_max(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day max bear-candle streak as fraction of expanding all-time maximum."""
    cond = close < open
    mx252 = _rolling_max_streak(cond, _TD_YEAR)
    exp_max = mx252.expanding(min_periods=5).max()
    return _safe_div(mx252, exp_max)


def dstk_ext_072_consec_high_below_prior_close(close: pd.Series, high: pd.Series) -> pd.Series:
    """Streak: today's high < prior close (gap down AND no recovery to prior close)."""
    cond = high < close.shift(1)
    return _consec_streak(cond)


def dstk_ext_073_max_high_below_prior_close_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Max streak of days where high < prior close, within trailing 63 days."""
    cond = high < close.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


def dstk_ext_074_consec_open_below_prior_low(low: pd.Series, open: pd.Series) -> pd.Series:
    """Streak of days where open < prior day's low (extreme gap-down open)."""
    cond = open < low.shift(1)
    return _consec_streak(cond)


def dstk_ext_075_severity_ema_vs_sma_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of EMA(21) to SMA(21) of absolute down-day log-returns.
    Above 1 means recent losses are accelerating vs trailing average."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    down_sev = daily_log.where(daily_log < 0, 0.0).abs()
    ema_sev = _ewm_mean(down_sev, _TD_MON)
    sma_sev = _rolling_mean(down_sev, _TD_MON)
    return _safe_div(ema_sev, sma_sev)


# ── Registry ──────────────────────────────────────────────────────────────────

DECLINE_STREAKS_EXTENDED_REGISTRY_001_075 = {
    "dstk_ext_001_consec_down_3d_bars": {
        "inputs": ["close"], "func": dstk_ext_001_consec_down_3d_bars},
    "dstk_ext_002_max_down_3d_bars_63d": {
        "inputs": ["close"], "func": dstk_ext_002_max_down_3d_bars_63d},
    "dstk_ext_003_max_down_3d_bars_252d": {
        "inputs": ["close"], "func": dstk_ext_003_max_down_3d_bars_252d},
    "dstk_ext_004_consec_down_3d_bars_norm_252d": {
        "inputs": ["close"], "func": dstk_ext_004_consec_down_3d_bars_norm_252d},
    "dstk_ext_005_consec_down_biweekly_bars": {
        "inputs": ["close"], "func": dstk_ext_005_consec_down_biweekly_bars},
    "dstk_ext_006_consec_down_quarterly_bars": {
        "inputs": ["close"], "func": dstk_ext_006_consec_down_quarterly_bars},
    "dstk_ext_007_max_down_quarterly_252d": {
        "inputs": ["close"], "func": dstk_ext_007_max_down_quarterly_252d},
    "dstk_ext_008_down_qtr_streak_pct_rank_504d": {
        "inputs": ["close"], "func": dstk_ext_008_down_qtr_streak_pct_rank_504d},
    "dstk_ext_009_consec_down_42d_bars": {
        "inputs": ["close"], "func": dstk_ext_009_consec_down_42d_bars},
    "dstk_ext_010_consec_down_3d_bars_pct_rank_252d": {
        "inputs": ["close"], "func": dstk_ext_010_consec_down_3d_bars_pct_rank_252d},
    "dstk_ext_011_severity_weighted_streak_current": {
        "inputs": ["close"], "func": dstk_ext_011_severity_weighted_streak_current},
    "dstk_ext_012_severity_weighted_streak_norm_252d": {
        "inputs": ["close"], "func": dstk_ext_012_severity_weighted_streak_norm_252d},
    "dstk_ext_013_cum_loss_per_streak_day_squared": {
        "inputs": ["close"], "func": dstk_ext_013_cum_loss_per_streak_day_squared},
    "dstk_ext_014_max_severity_weighted_streak_63d": {
        "inputs": ["close"], "func": dstk_ext_014_max_severity_weighted_streak_63d},
    "dstk_ext_015_max_severity_weighted_streak_252d": {
        "inputs": ["close"], "func": dstk_ext_015_max_severity_weighted_streak_252d},
    "dstk_ext_016_severity_weighted_streak_zscore_252d": {
        "inputs": ["close"], "func": dstk_ext_016_severity_weighted_streak_zscore_252d},
    "dstk_ext_017_vol_weighted_cum_loss_streak": {
        "inputs": ["close", "volume"], "func": dstk_ext_017_vol_weighted_cum_loss_streak},
    "dstk_ext_018_vol_weighted_severity_norm_252d": {
        "inputs": ["close", "volume"], "func": dstk_ext_018_vol_weighted_severity_norm_252d},
    "dstk_ext_019_streak_len_std_63d": {
        "inputs": ["close"], "func": dstk_ext_019_streak_len_std_63d},
    "dstk_ext_020_streak_len_std_252d": {
        "inputs": ["close"], "func": dstk_ext_020_streak_len_std_252d},
    "dstk_ext_021_streak_len_cv_252d": {
        "inputs": ["close"], "func": dstk_ext_021_streak_len_cv_252d},
    "dstk_ext_022_streak_count_21d": {
        "inputs": ["close"], "func": dstk_ext_022_streak_count_21d},
    "dstk_ext_023_streak_count_252d": {
        "inputs": ["close"], "func": dstk_ext_023_streak_count_252d},
    "dstk_ext_024_avg_gap_between_streaks_63d": {
        "inputs": ["close"], "func": dstk_ext_024_avg_gap_between_streaks_63d},
    "dstk_ext_025_avg_gap_between_streaks_252d": {
        "inputs": ["close"], "func": dstk_ext_025_avg_gap_between_streaks_252d},
    "dstk_ext_026_streak_to_gap_ratio_63d": {
        "inputs": ["close"], "func": dstk_ext_026_streak_to_gap_ratio_63d},
    "dstk_ext_027_streak_to_gap_ratio_252d": {
        "inputs": ["close"], "func": dstk_ext_027_streak_to_gap_ratio_252d},
    "dstk_ext_028_current_vs_expanding_max_streak": {
        "inputs": ["close"], "func": dstk_ext_028_current_vs_expanding_max_streak},
    "dstk_ext_029_current_streak_pct_rank_expanding": {
        "inputs": ["close"], "func": dstk_ext_029_current_streak_pct_rank_expanding},
    "dstk_ext_030_streak_count_ratio_21d_vs_252d": {
        "inputs": ["close"], "func": dstk_ext_030_streak_count_ratio_21d_vs_252d},
    "dstk_ext_031_streak_count_ratio_63d_vs_252d": {
        "inputs": ["close"], "func": dstk_ext_031_streak_count_ratio_63d_vs_252d},
    "dstk_ext_032_streak_count_252d_expanding_rank": {
        "inputs": ["close"], "func": dstk_ext_032_streak_count_252d_expanding_rank},
    "dstk_ext_033_streak_of_streaks_current": {
        "inputs": ["close"], "func": dstk_ext_033_streak_of_streaks_current},
    "dstk_ext_034_cluster_density_21d": {
        "inputs": ["close"], "func": dstk_ext_034_cluster_density_21d},
    "dstk_ext_035_cluster_density_63d": {
        "inputs": ["close"], "func": dstk_ext_035_cluster_density_63d},
    "dstk_ext_036_max_streak_cluster_63d": {
        "inputs": ["close"], "func": dstk_ext_036_max_streak_cluster_63d},
    "dstk_ext_037_no_up_day_in_10d_flag": {
        "inputs": ["close"], "func": dstk_ext_037_no_up_day_in_10d_flag},
    "dstk_ext_038_no_up_day_in_15d_flag": {
        "inputs": ["close"], "func": dstk_ext_038_no_up_day_in_15d_flag},
    "dstk_ext_039_up_day_count_21d": {
        "inputs": ["close"], "func": dstk_ext_039_up_day_count_21d},
    "dstk_ext_040_up_day_count_zscore_252d": {
        "inputs": ["close"], "func": dstk_ext_040_up_day_count_zscore_252d},
    "dstk_ext_041_consec_close_below_vwap_5d": {
        "inputs": ["close", "high", "low", "volume"],
        "func": dstk_ext_041_consec_close_below_vwap_5d},
    "dstk_ext_042_consec_close_below_vwap_21d": {
        "inputs": ["close", "high", "low", "volume"],
        "func": dstk_ext_042_consec_close_below_vwap_21d},
    "dstk_ext_043_consec_close_below_vwap_63d": {
        "inputs": ["close", "high", "low", "volume"],
        "func": dstk_ext_043_consec_close_below_vwap_63d},
    "dstk_ext_044_max_below_vwap21_streak_252d": {
        "inputs": ["close", "high", "low", "volume"],
        "func": dstk_ext_044_max_below_vwap21_streak_252d},
    "dstk_ext_045_below_vwap21_streak_norm_252d": {
        "inputs": ["close", "high", "low", "volume"],
        "func": dstk_ext_045_below_vwap21_streak_norm_252d},
    "dstk_ext_046_consec_lower_highs_and_lower_lows_norm_252d": {
        "inputs": ["high", "low"],
        "func": dstk_ext_046_consec_lower_highs_and_lower_lows_norm_252d},
    "dstk_ext_047_max_lower_high_streak_252d": {
        "inputs": ["high"], "func": dstk_ext_047_max_lower_high_streak_252d},
    "dstk_ext_048_lower_high_streak_zscore_252d": {
        "inputs": ["high"], "func": dstk_ext_048_lower_high_streak_zscore_252d},
    "dstk_ext_049_consec_lower_close_and_lower_high": {
        "inputs": ["close", "high"], "func": dstk_ext_049_consec_lower_close_and_lower_high},
    "dstk_ext_050_consec_new_10d_low_intraday": {
        "inputs": ["low"], "func": dstk_ext_050_consec_new_10d_low_intraday},
    "dstk_ext_051_consec_new_63d_low_intraday": {
        "inputs": ["low"], "func": dstk_ext_051_consec_new_63d_low_intraday},
    "dstk_ext_052_consec_new_252d_low_intraday": {
        "inputs": ["low"], "func": dstk_ext_052_consec_new_252d_low_intraday},
    "dstk_ext_053_lower_low_streak_pct_rank_252d": {
        "inputs": ["low"], "func": dstk_ext_053_lower_low_streak_pct_rank_252d},
    "dstk_ext_054_max_down_volume_streak_63d": {
        "inputs": ["volume"], "func": dstk_ext_054_max_down_volume_streak_63d},
    "dstk_ext_055_max_down_volume_streak_252d": {
        "inputs": ["volume"], "func": dstk_ext_055_max_down_volume_streak_252d},
    "dstk_ext_056_down_vol_streak_zscore_252d": {
        "inputs": ["volume"], "func": dstk_ext_056_down_vol_streak_zscore_252d},
    "dstk_ext_057_consec_below_avg_volume_days": {
        "inputs": ["volume"], "func": dstk_ext_057_consec_below_avg_volume_days},
    "dstk_ext_058_max_below_avg_vol_streak_252d": {
        "inputs": ["volume"], "func": dstk_ext_058_max_below_avg_vol_streak_252d},
    "dstk_ext_059_consec_price_down_vol_up": {
        "inputs": ["close", "volume"], "func": dstk_ext_059_consec_price_down_vol_up},
    "dstk_ext_060_max_distribution_day_streak_63d": {
        "inputs": ["close", "volume"], "func": dstk_ext_060_max_distribution_day_streak_63d},
    "dstk_ext_061_streak_freq_21d_vs_63d_ratio": {
        "inputs": ["close"], "func": dstk_ext_061_streak_freq_21d_vs_63d_ratio},
    "dstk_ext_062_streak_freq_pct_rank_252d": {
        "inputs": ["close"], "func": dstk_ext_062_streak_freq_pct_rank_252d},
    "dstk_ext_063_avg_gap_pct_rank_252d": {
        "inputs": ["close"], "func": dstk_ext_063_avg_gap_pct_rank_252d},
    "dstk_ext_064_cluster_density_21d_zscore_252d": {
        "inputs": ["close"], "func": dstk_ext_064_cluster_density_21d_zscore_252d},
    "dstk_ext_065_streak_to_gap_ratio_pct_rank_252d": {
        "inputs": ["close"], "func": dstk_ext_065_streak_to_gap_ratio_pct_rank_252d},
    "dstk_ext_066_streak_severity_per_down_day_63d": {
        "inputs": ["close"], "func": dstk_ext_066_streak_severity_per_down_day_63d},
    "dstk_ext_067_streak_severity_per_down_day_252d": {
        "inputs": ["close"], "func": dstk_ext_067_streak_severity_per_down_day_252d},
    "dstk_ext_068_down_streak_entropy_63d": {
        "inputs": ["close"], "func": dstk_ext_068_down_streak_entropy_63d},
    "dstk_ext_069_down_streak_entropy_252d": {
        "inputs": ["close"], "func": dstk_ext_069_down_streak_entropy_252d},
    "dstk_ext_070_bear_candle_streak_norm_252d": {
        "inputs": ["close", "open"], "func": dstk_ext_070_bear_candle_streak_norm_252d},
    "dstk_ext_071_max_bear_candle_vs_expanding_max": {
        "inputs": ["close", "open"], "func": dstk_ext_071_max_bear_candle_vs_expanding_max},
    "dstk_ext_072_consec_high_below_prior_close": {
        "inputs": ["close", "high"], "func": dstk_ext_072_consec_high_below_prior_close},
    "dstk_ext_073_max_high_below_prior_close_63d": {
        "inputs": ["close", "high"], "func": dstk_ext_073_max_high_below_prior_close_63d},
    "dstk_ext_074_consec_open_below_prior_low": {
        "inputs": ["low", "open"], "func": dstk_ext_074_consec_open_below_prior_low},
    "dstk_ext_075_severity_ema_vs_sma_ratio_21d": {
        "inputs": ["close"], "func": dstk_ext_075_severity_ema_vs_sma_ratio_21d},
}
