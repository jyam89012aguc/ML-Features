"""
08_decline_streaks — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base streak features — velocity / acceleration of streak behavior
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dstk_drv2_001_consec_down_days_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current down-day streak length (velocity of streak growth)."""
    streak = _consec_streak(close < close.shift(1))
    return streak.diff(_TD_WEEK)


def dstk_drv2_002_consec_down_days_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of current down-day streak (monthly velocity)."""
    streak = _consec_streak(close < close.shift(1))
    return streak.diff(_TD_MON)


def dstk_drv2_003_max_down_streak_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63-day maximum down streak."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_QTR)
    return mx.diff(_TD_WEEK)


def dstk_drv2_004_max_down_streak_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day max down streak (monthly change in worst streak)."""
    cond = close < close.shift(1)
    mx = _rolling_max_streak(cond, _TD_YEAR)
    return mx.diff(_TD_MON)


def dstk_drv2_005_down_week_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive down-week streak."""
    streak = _consec_streak(close.pct_change(_TD_WEEK) < 0)
    return streak.diff(_TD_WEEK)


def dstk_drv2_006_down_month_streak_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of consecutive down-month streak."""
    streak = _consec_streak(close.pct_change(_TD_MON) < 0)
    return streak.diff(_TD_MON)


def dstk_drv2_007_below_sma200_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-below-SMA200 streak."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak(close < sma200)
    return streak.diff(_TD_WEEK)


def dstk_drv2_008_down_up_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up ratio."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_MON)
    up = _rolling_count_true(ret > 0, _TD_MON)
    ratio = _safe_div(down, up)
    return ratio.diff(_TD_WEEK)


def dstk_drv2_009_streak_severity_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-return severity sum."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev = daily_log.where(daily_log < 0, 0.0)
    sev21 = _rolling_sum(sev, _TD_MON)
    return sev21.diff(_TD_WEEK)


def dstk_drv2_010_streak_severity_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-return severity sum."""
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    sev = daily_log.where(daily_log < 0, 0.0)
    sev63 = _rolling_sum(sev, _TD_QTR)
    return sev63.diff(_TD_MON)


def dstk_drv2_011_down_day_fraction_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-day fraction."""
    ret = close.pct_change(1)
    frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def dstk_drv2_012_lower_low_streak_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of consecutive lower-lows streak."""
    streak = _consec_streak(low < low.shift(1))
    return streak.diff(_TD_WEEK)


def dstk_drv2_013_new_52wk_low_count_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day new-52wk-low count."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = (close < roll_min).astype(float)
    count63 = _rolling_sum(new_low, _TD_QTR)
    return count63.diff(_TD_MON)


def dstk_drv2_014_streak_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of down-streak z-score (accelerating extremity)."""
    streak = _consec_streak(close < close.shift(1))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    return z.diff(_TD_WEEK)


def dstk_drv2_015_below_sma200_streak_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of below-SMA200 streak over trailing 21 days."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak(close < sma200)
    return _linslope(streak, _TD_MON)


def dstk_drv2_016_streak_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite streak score (day+week+month)."""
    dd = _consec_streak(close < close.shift(1))
    dw = _consec_streak(close.pct_change(_TD_WEEK) < 0)
    dm = _consec_streak(close.pct_change(_TD_MON) < 0)
    dd_n = _safe_div(dd, _rolling_mean(dd, _TD_YEAR).clip(lower=_EPS))
    dw_n = _safe_div(dw, _rolling_mean(dw, _TD_YEAR).clip(lower=_EPS))
    dm_n = _safe_div(dm, _rolling_mean(dm, _TD_YEAR).clip(lower=_EPS))
    composite = (dd_n + dw_n + dm_n) / 3.0
    return composite.diff(_TD_WEEK)


def dstk_drv2_017_gap_down_fraction_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap-down fraction."""
    cond = open < close.shift(1)
    frac = _rolling_count_true(cond, _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def dstk_drv2_018_streak_vol_interaction_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of streak-times-vol-norm interaction."""
    streak = _consec_streak(close < close.shift(1))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = streak * vol_norm
    return interaction.diff(_TD_WEEK)


def dstk_drv2_019_down_up_ratio_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day down/up ratio over trailing 21 days."""
    ret = close.pct_change(1)
    down = _rolling_count_true(ret < 0, _TD_QTR)
    up = _rolling_count_true(ret > 0, _TD_QTR)
    ratio = _safe_div(down, up)
    return _linslope(ratio, _TD_MON)


def dstk_drv2_020_consec_lower_lows_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of consecutive lower-lows AND lower-highs streak."""
    streak = _consec_streak(low < low.shift(1))
    return streak.diff(_TD_WEEK)


def dstk_drv2_021_avg_down_streak_len_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of rolling average down-streak length (63-day)."""
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
    return avg63.diff(_TD_MON)


def dstk_drv2_022_worst_streak_loss_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day worst streak cumulative loss."""
    cond = close < close.shift(1)
    daily_log = _log_safe(close) - _log_safe(close.shift(1))
    group = (~cond).cumsum()
    cum = daily_log.groupby(group).cumsum().where(cond, 0.0)
    worst = _rolling_min(cum, _TD_YEAR)
    return worst.diff(_TD_MON)


def dstk_drv2_023_vol_ratio_down_up_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume ratio (down vs up days)."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_vol = volume.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(down_vol, up_vol)
    return ratio.diff(_TD_MON)


def dstk_drv2_024_max_down_streak_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day max down streak over trailing 63 days."""
    cond = close < close.shift(1)
    mx21 = _rolling_max_streak(cond, _TD_MON)
    return _linslope(mx21, _TD_QTR)


def dstk_drv2_025_down_day_fraction_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day down-day fraction."""
    ret = close.pct_change(1)
    frac = _rolling_count_true(ret < 0, _TD_YEAR) / _TD_YEAR
    return frac.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DECLINE_STREAKS_REGISTRY_2ND_DERIVATIVES = {
    "dstk_drv2_001_consec_down_days_5d_diff": {"inputs": ["close"], "func": dstk_drv2_001_consec_down_days_5d_diff},
    "dstk_drv2_002_consec_down_days_21d_diff": {"inputs": ["close"], "func": dstk_drv2_002_consec_down_days_21d_diff},
    "dstk_drv2_003_max_down_streak_63d_5d_diff": {"inputs": ["close"], "func": dstk_drv2_003_max_down_streak_63d_5d_diff},
    "dstk_drv2_004_max_down_streak_252d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_004_max_down_streak_252d_21d_diff},
    "dstk_drv2_005_down_week_streak_5d_diff": {"inputs": ["close"], "func": dstk_drv2_005_down_week_streak_5d_diff},
    "dstk_drv2_006_down_month_streak_21d_diff": {"inputs": ["close"], "func": dstk_drv2_006_down_month_streak_21d_diff},
    "dstk_drv2_007_below_sma200_streak_5d_diff": {"inputs": ["close"], "func": dstk_drv2_007_below_sma200_streak_5d_diff},
    "dstk_drv2_008_down_up_ratio_21d_5d_diff": {"inputs": ["close"], "func": dstk_drv2_008_down_up_ratio_21d_5d_diff},
    "dstk_drv2_009_streak_severity_21d_5d_diff": {"inputs": ["close"], "func": dstk_drv2_009_streak_severity_21d_5d_diff},
    "dstk_drv2_010_streak_severity_63d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_010_streak_severity_63d_21d_diff},
    "dstk_drv2_011_down_day_fraction_21d_5d_diff": {"inputs": ["close"], "func": dstk_drv2_011_down_day_fraction_21d_5d_diff},
    "dstk_drv2_012_lower_low_streak_5d_diff": {"inputs": ["low"], "func": dstk_drv2_012_lower_low_streak_5d_diff},
    "dstk_drv2_013_new_52wk_low_count_63d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_013_new_52wk_low_count_63d_21d_diff},
    "dstk_drv2_014_streak_zscore_5d_diff": {"inputs": ["close"], "func": dstk_drv2_014_streak_zscore_5d_diff},
    "dstk_drv2_015_below_sma200_streak_slope_21d": {"inputs": ["close"], "func": dstk_drv2_015_below_sma200_streak_slope_21d},
    "dstk_drv2_016_streak_composite_5d_diff": {"inputs": ["close"], "func": dstk_drv2_016_streak_composite_5d_diff},
    "dstk_drv2_017_gap_down_fraction_21d_5d_diff": {"inputs": ["close", "open"], "func": dstk_drv2_017_gap_down_fraction_21d_5d_diff},
    "dstk_drv2_018_streak_vol_interaction_5d_diff": {"inputs": ["close", "volume"], "func": dstk_drv2_018_streak_vol_interaction_5d_diff},
    "dstk_drv2_019_down_up_ratio_63d_slope_21d": {"inputs": ["close"], "func": dstk_drv2_019_down_up_ratio_63d_slope_21d},
    "dstk_drv2_020_consec_lower_lows_5d_diff": {"inputs": ["low"], "func": dstk_drv2_020_consec_lower_lows_5d_diff},
    "dstk_drv2_021_avg_down_streak_len_63d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_021_avg_down_streak_len_63d_21d_diff},
    "dstk_drv2_022_worst_streak_loss_252d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_022_worst_streak_loss_252d_21d_diff},
    "dstk_drv2_023_vol_ratio_down_up_63d_21d_diff": {"inputs": ["close", "volume"], "func": dstk_drv2_023_vol_ratio_down_up_63d_21d_diff},
    "dstk_drv2_024_max_down_streak_21d_slope_63d": {"inputs": ["close"], "func": dstk_drv2_024_max_down_streak_21d_slope_63d},
    "dstk_drv2_025_down_day_fraction_252d_21d_diff": {"inputs": ["close"], "func": dstk_drv2_025_down_day_fraction_252d_21d_diff},
}
