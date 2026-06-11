"""
08_decline_streaks — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative streak features — acceleration of velocity
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


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
# Each 3rd-derivative = diff/slope/pct-change applied to a 2nd-derivative concept

def dstk_drv3_001_consec_down_days_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of down-streak length (acceleration of streak velocity)."""
    streak = _consec_streak(close < close.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_002_consec_down_days_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day-velocity of down-streak (jerk in monthly streak change)."""
    streak = _consec_streak(close < close.shift(1))
    vel21 = streak.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_003_max_down_streak_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day change in 63-day max streak (2nd accel)."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_QTR)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_004_below_sma200_streak_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of below-SMA200 streak (acceleration of breakdown pace)."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak(close < sma200)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_005_down_up_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day change in 21-day down/up ratio."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_MON)
    up = _rolling_count_true(ret > 0, _TD_MON)
    ratio = _safe_div(down, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_006_streak_severity_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day severity sum (jerk in pain accumulation)."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev = daily_log.where(daily_log < 0, 0.0)
    sev21 = _rolling_sum(sev, _TD_MON)
    vel = sev21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_007_streak_severity_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day severity sum."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev = daily_log.where(daily_log < 0, 0.0)
    sev63 = _rolling_sum(sev, _TD_QTR)
    vel21 = sev63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_008_down_day_fraction_21d_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of down-day fraction."""
    ret = close.pct_change(1)
    frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dstk_drv3_009_streak_zscore_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of down-streak z-score."""
    streak = _consec_streak(close < close.shift(1))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dstk_drv3_010_lower_low_streak_5d_diff_5d_diff(low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive lower-lows streak."""
    streak = _consec_streak(low < low.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_011_new_52wk_low_count_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day new-52wk-low count."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = (close < roll_min).astype(float)
    count63 = _rolling_sum(new_low, _TD_QTR)
    vel21 = count63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_012_below_sma200_streak_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of below-SMA200 streak (rate of slope change)."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak(close < sma200)
    slp = _linslope(streak, _TD_MON)
    return slp.diff(_TD_WEEK)


def dstk_drv3_013_streak_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite streak score."""
    dd = _consec_streak(close < close.shift(1))
    dw = _consec_streak(close.pct_change(_TD_WEEK) < 0)
    dm = _consec_streak(close.pct_change(_TD_MON) < 0)
    dd_n = _safe_div(dd, _rolling_mean(dd, _TD_YEAR).clip(lower=_EPS))
    dw_n = _safe_div(dw, _rolling_mean(dw, _TD_YEAR).clip(lower=_EPS))
    dm_n = _safe_div(dm, _rolling_mean(dm, _TD_YEAR).clip(lower=_EPS))
    composite = (dd_n + dw_n + dm_n) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_014_gap_down_fraction_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gap-down fraction."""
    cond = open < close.shift(1)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_015_streak_vol_interaction_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of streak-volume interaction."""
    streak = _consec_streak(close < close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = streak * vol_norm
    vel = interaction.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_016_down_up_ratio_63d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day down/up ratio."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_QTR)
    up = _rolling_count_true(ret > 0, _TD_QTR)
    ratio = _safe_div(down, up)
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def dstk_drv3_017_max_down_streak_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day max streak."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_YEAR)
    vel21 = mx.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_018_worst_streak_loss_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day worst streak loss."""
    cond = close < close.shift(1)
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    group = (~cond).cumsum()
    cum = daily_log.groupby(group).cumsum().where(cond, 0.0)
    worst = _rolling_min(cum, _TD_YEAR)
    vel21 = worst.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_019_vol_ratio_down_up_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down/up volume ratio."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(down_vol, up_vol)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_020_down_week_streak_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive down-week streak."""
    streak = _consec_streak(close.pct_change(_TD_WEEK) < 0)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dstk_drv3_021_max_streak_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day max streak over 63-day window."""
    cond = close < close.shift(1)
    mx21 = _rolling_max_streak(cond, _TD_MON)
    slp = _linslope(mx21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def dstk_drv3_022_down_day_fraction_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day down-day fraction."""
    ret = close.pct_change(1)
    frac = _rolling_count_true(ret < 0, _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dstk_drv3_023_avg_down_streak_63d_21d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day change in avg-streak-len-63d."""
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
        if num_runs == 0:
            return 0.0
        return float(total) / float(num_runs)
    cond = close < close.shift(1)
    avg63 = cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_avg_run, raw=True)
    vel21 = avg63.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def dstk_drv3_024_streak_severity_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day severity sum."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev = daily_log.where(daily_log < 0, 0.0)
    sev21 = _rolling_sum(sev, _TD_MON)
    vel = sev21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dstk_drv3_025_down_month_streak_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in consecutive down-month streak."""
    streak = _consec_streak(close.pct_change(_TD_MON) < 0)
    vel21 = streak.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DECLINE_STREAKS_REGISTRY_3RD_DERIVATIVES = {
    "dstk_drv3_001_consec_down_days_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_001_consec_down_days_5d_diff_5d_diff},
    "dstk_drv3_002_consec_down_days_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_002_consec_down_days_21d_diff_5d_diff},
    "dstk_drv3_003_max_down_streak_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_003_max_down_streak_63d_5d_diff_5d_diff},
    "dstk_drv3_004_below_sma200_streak_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_004_below_sma200_streak_5d_diff_5d_diff},
    "dstk_drv3_005_down_up_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_005_down_up_ratio_21d_5d_diff_5d_diff},
    "dstk_drv3_006_streak_severity_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_006_streak_severity_21d_5d_diff_5d_diff},
    "dstk_drv3_007_streak_severity_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_007_streak_severity_63d_21d_diff_5d_diff},
    "dstk_drv3_008_down_day_fraction_21d_5d_diff_slope": {"inputs": ["close"], "func": dstk_drv3_008_down_day_fraction_21d_5d_diff_slope},
    "dstk_drv3_009_streak_zscore_5d_diff_slope_21d": {"inputs": ["close"], "func": dstk_drv3_009_streak_zscore_5d_diff_slope_21d},
    "dstk_drv3_010_lower_low_streak_5d_diff_5d_diff": {"inputs": ["low"], "func": dstk_drv3_010_lower_low_streak_5d_diff_5d_diff},
    "dstk_drv3_011_new_52wk_low_count_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_011_new_52wk_low_count_63d_21d_diff_5d_diff},
    "dstk_drv3_012_below_sma200_streak_slope_5d_diff": {"inputs": ["close"], "func": dstk_drv3_012_below_sma200_streak_slope_5d_diff},
    "dstk_drv3_013_streak_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_013_streak_composite_5d_diff_5d_diff},
    "dstk_drv3_014_gap_down_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": dstk_drv3_014_gap_down_fraction_21d_5d_diff_5d_diff},
    "dstk_drv3_015_streak_vol_interaction_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dstk_drv3_015_streak_vol_interaction_5d_diff_5d_diff},
    "dstk_drv3_016_down_up_ratio_63d_slope_5d_diff": {"inputs": ["close"], "func": dstk_drv3_016_down_up_ratio_63d_slope_5d_diff},
    "dstk_drv3_017_max_down_streak_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_017_max_down_streak_252d_21d_diff_5d_diff},
    "dstk_drv3_018_worst_streak_loss_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_018_worst_streak_loss_21d_diff_5d_diff},
    "dstk_drv3_019_vol_ratio_down_up_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dstk_drv3_019_vol_ratio_down_up_63d_21d_diff_5d_diff},
    "dstk_drv3_020_down_week_streak_5d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_020_down_week_streak_5d_diff_5d_diff},
    "dstk_drv3_021_max_streak_21d_slope_5d_diff": {"inputs": ["close"], "func": dstk_drv3_021_max_streak_21d_slope_5d_diff},
    "dstk_drv3_022_down_day_fraction_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_022_down_day_fraction_252d_21d_diff_5d_diff},
    "dstk_drv3_023_avg_down_streak_63d_21d_diff_slope": {"inputs": ["close"], "func": dstk_drv3_023_avg_down_streak_63d_21d_diff_slope},
    "dstk_drv3_024_streak_severity_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": dstk_drv3_024_streak_severity_21d_5d_diff_slope_21d},
    "dstk_drv3_025_down_month_streak_21d_diff_5d_diff": {"inputs": ["close"], "func": dstk_drv3_025_down_month_streak_21d_diff_5d_diff},
}
