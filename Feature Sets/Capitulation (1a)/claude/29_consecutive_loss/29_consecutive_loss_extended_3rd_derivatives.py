"""
29_consecutive_loss — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative concepts — acceleration of
    velocity for streak-length trends, vol-concentration shifts, gap/session
    decomposition changes, composite-score jerk, exhaustion/inflection signals.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero denominator becomes NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_log_ret(close: pd.Series) -> pd.Series:
    return _log_safe(close) - _log_safe(close.shift(1))


def _is_loss_day(close: pd.Series) -> pd.Series:
    return close < close.shift(1)


def _run_group(cond: pd.Series) -> pd.Series:
    return (~cond).cumsum()


def _cum_log_loss_in_run(close: pd.Series) -> pd.Series:
    """Cumulative log-return within current losing run (0 on non-loss days)."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = lr.groupby(grp).cumsum()
    return cum.where(cond, 0.0)


def _completed_run_len(close: pd.Series) -> pd.Series:
    """Length of each completed run placed on the first non-run day; NaN elsewhere."""
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    length = cond.astype(int).groupby(grp).cumsum()
    run_ended = (~cond) & cond.shift(1).fillna(False)
    return length.shift(1).astype(float).where(run_ended)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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
# Each = diff/slope of a 2nd-derivative concept (velocity of velocity)

def ccl_extdrv3_001_run_len_avg_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day avg run length (jerk/acceleration of streak growth)."""
    rl = _completed_run_len(close)
    avg63 = rl.rolling(_TD_QTR, min_periods=1).mean()
    vel = avg63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_002_current_run_len_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of current run length (acceleration of streak growth)."""
    cur = _consec_streak(_is_loss_day(close)).astype(float)
    vel = cur.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_003_loss_day_frac_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day loss-day fraction (jerk in frequency change)."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_004_cum_loss_run_times_len_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (run-loss * run-length) product."""
    cum = _cum_log_loss_in_run(close).abs()
    rlen = _consec_streak(_is_loss_day(close)).astype(float)
    product = cum * rlen
    vel = product.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_005_cum_loss_run_zscore_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day z-score of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    m = _rolling_mean(cum, _TD_QTR)
    s = _rolling_std(cum, _TD_QTR)
    z = _safe_div(cum - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_006_overnight_gap_loss_63d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day overnight gap-down sum (acceleration of gap-selling)."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    s63 = _rolling_sum(gap.where(gap < 0, 0.0), _TD_QTR)
    vel = s63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_007_intraday_session_loss_63d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day intraday-session loss sum."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    s63 = _rolling_sum(o2c.where(ret < 0, 0.0), _TD_QTR)
    vel = s63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_008_vol_frac_loss_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume fraction on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    vfrac = _safe_div(loss_vol, total_vol)
    vel = vfrac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_009_vol_on_loss_vs_gain_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol-on-loss/vol-on-gain ratio."""
    cond = _is_loss_day(close)
    avg_loss_vol = volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    avg_gain_vol = volume.where(~cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(avg_loss_vol, avg_gain_vol)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_010_capitulation_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-component capitulation composite z-score."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    score = (_z(s21) + _z(w63) + _z(frac)) / 3.0
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_011_loss_persistence_score_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day loss-persistence score."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    avg252 = _rolling_mean(s21, _TD_YEAR)
    score = _safe_div(s21, avg252) * frac
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_012_loss_acceleration_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of loss-acceleration score (5d/21d neg-sum ratio)."""
    lr = _daily_log_ret(close)
    s5  = _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK).abs()
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    score = _safe_div(s5, s21)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_013_loss_day_frac_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day loss-day fraction."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_extdrv3_014_worst_run_loss_126d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 126-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w126 = _rolling_min(cum, _TD_HALF)
    vel21 = w126.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_extdrv3_015_neg_ret_sum_126d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 126-day negative-return sum."""
    lr = _daily_log_ret(close)
    s126 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_HALF)
    vel21 = s126.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_extdrv3_016_loss_breadth_score_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day loss-breadth score (frac * run-frequency)."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    freq = _rolling_sum(is_start, _TD_QTR)
    score = frac * freq
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_017_run_len_avg_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63-day avg run length."""
    rl = _completed_run_len(close)
    avg63 = rl.rolling(_TD_QTR, min_periods=1).mean()
    vel = avg63.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ccl_extdrv3_018_loss_day_frac_21d_vel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day loss-day fraction."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ccl_extdrv3_019_vol_frac_loss_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day vol fraction on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    vfrac = _safe_div(loss_vol, total_vol)
    vel21 = vfrac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_extdrv3_020_cum_loss_run_pct_rank_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day pct-rank of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    pr = cum.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)
    vel = pr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_021_neg_ret_sum_21d_ewm_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of z-score of 21-day neg-sum vs its EWM(63) baseline."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    ewm = _ewm_mean(s21, _TD_QTR)
    diff = s21 - ewm
    s = _rolling_std(diff, _TD_YEAR)
    z = _safe_div(diff, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_022_vol_adj_cum_loss_zscore_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol-adjusted current-run cumulative loss z-score."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = (lr * vol_norm).groupby(grp).cumsum().where(cond, 0.0)
    m = _rolling_mean(cum, _TD_YEAR)
    s = _rolling_std(cum, _TD_YEAR)
    z = _safe_div(cum - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_extdrv3_023_capitulation_score_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of the capitulation composite."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    score = (_z(s21) + _z(w63) + _z(frac)) / 3.0
    vel = score.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ccl_extdrv3_024_var_1pct_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day 1%-VaR (acceleration of tail-risk)."""
    lr = _daily_log_ret(close)
    var1 = lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.01)
    vel21 = var1.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_extdrv3_025_loss_day_count_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day loss-day count (jerk in losing-day frequency)."""
    cond = _is_loss_day(close)
    cnt = _rolling_sum(cond.astype(float), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "ccl_extdrv3_001_run_len_avg_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_001_run_len_avg_63d_5d_diff_5d_diff},
    "ccl_extdrv3_002_current_run_len_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_002_current_run_len_5d_diff_5d_diff},
    "ccl_extdrv3_003_loss_day_frac_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_003_loss_day_frac_21d_5d_diff_5d_diff},
    "ccl_extdrv3_004_cum_loss_run_times_len_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_004_cum_loss_run_times_len_5d_diff_5d_diff},
    "ccl_extdrv3_005_cum_loss_run_zscore_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_005_cum_loss_run_zscore_63d_5d_diff_5d_diff},
    "ccl_extdrv3_006_overnight_gap_loss_63d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ccl_extdrv3_006_overnight_gap_loss_63d_5d_diff_5d_diff},
    "ccl_extdrv3_007_intraday_session_loss_63d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": ccl_extdrv3_007_intraday_session_loss_63d_5d_diff_5d_diff},
    "ccl_extdrv3_008_vol_frac_loss_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv3_008_vol_frac_loss_21d_5d_diff_5d_diff},
    "ccl_extdrv3_009_vol_on_loss_vs_gain_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv3_009_vol_on_loss_vs_gain_21d_5d_diff_5d_diff},
    "ccl_extdrv3_010_capitulation_score_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_010_capitulation_score_5d_diff_5d_diff},
    "ccl_extdrv3_011_loss_persistence_score_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_011_loss_persistence_score_21d_5d_diff_5d_diff},
    "ccl_extdrv3_012_loss_acceleration_score_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_012_loss_acceleration_score_5d_diff_5d_diff},
    "ccl_extdrv3_013_loss_day_frac_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_013_loss_day_frac_63d_21d_diff_5d_diff},
    "ccl_extdrv3_014_worst_run_loss_126d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_014_worst_run_loss_126d_21d_diff_5d_diff},
    "ccl_extdrv3_015_neg_ret_sum_126d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_015_neg_ret_sum_126d_21d_diff_5d_diff},
    "ccl_extdrv3_016_loss_breadth_score_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_016_loss_breadth_score_63d_5d_diff_5d_diff},
    "ccl_extdrv3_017_run_len_avg_63d_slope_21d": {"inputs": ["close"], "func": ccl_extdrv3_017_run_len_avg_63d_slope_21d},
    "ccl_extdrv3_018_loss_day_frac_21d_vel_slope_21d": {"inputs": ["close"], "func": ccl_extdrv3_018_loss_day_frac_21d_vel_slope_21d},
    "ccl_extdrv3_019_vol_frac_loss_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv3_019_vol_frac_loss_63d_21d_diff_5d_diff},
    "ccl_extdrv3_020_cum_loss_run_pct_rank_126d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_020_cum_loss_run_pct_rank_126d_5d_diff_5d_diff},
    "ccl_extdrv3_021_neg_ret_sum_21d_ewm_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_021_neg_ret_sum_21d_ewm_zscore_5d_diff_5d_diff},
    "ccl_extdrv3_022_vol_adj_cum_loss_zscore_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv3_022_vol_adj_cum_loss_zscore_5d_diff_5d_diff},
    "ccl_extdrv3_023_capitulation_score_5d_diff_slope_21d": {"inputs": ["close"], "func": ccl_extdrv3_023_capitulation_score_5d_diff_slope_21d},
    "ccl_extdrv3_024_var_1pct_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_024_var_1pct_252d_21d_diff_5d_diff},
    "ccl_extdrv3_025_loss_day_count_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_extdrv3_025_loss_day_count_21d_5d_diff_5d_diff},
}
