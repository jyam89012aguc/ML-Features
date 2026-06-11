"""
29_consecutive_loss — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended consecutive-loss base concepts — velocity /
    acceleration of streak-length distributions, vol-concentration on loss days,
    gap/session decomposition, adaptive-threshold regime shifts, composite scores.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def ccl_extdrv2_001_run_len_avg_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day avg completed-run length (velocity of streak elongation)."""
    rl = _completed_run_len(close)
    avg63 = rl.rolling(_TD_QTR, min_periods=1).mean()
    return avg63.diff(_TD_WEEK)


def ccl_extdrv2_002_run_len_avg_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day avg completed-run length."""
    rl = _completed_run_len(close)
    avg252 = rl.rolling(_TD_YEAR, min_periods=1).mean()
    return avg252.diff(_TD_MON)


def ccl_extdrv2_003_current_run_len_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current run length (rate of streak growth)."""
    cur = _consec_streak(_is_loss_day(close)).astype(float)
    return cur.diff(_TD_WEEK)


def ccl_extdrv2_004_cum_loss_run_times_len_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (current-run-loss * run-length) product (severity*duration velocity)."""
    cum = _cum_log_loss_in_run(close).abs()
    rlen = _consec_streak(_is_loss_day(close)).astype(float)
    product = cum * rlen
    return product.diff(_TD_WEEK)


def ccl_extdrv2_005_cum_loss_run_zscore_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day z-score of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    m = _rolling_mean(cum, _TD_QTR)
    s = _rolling_std(cum, _TD_QTR)
    z = _safe_div(cum - m, s)
    return z.diff(_TD_WEEK)


def ccl_extdrv2_006_loss_day_frac_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day loss-day fraction (velocity of loss-day frequency change)."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def ccl_extdrv2_007_loss_day_frac_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day loss-day fraction."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def ccl_extdrv2_008_overnight_gap_loss_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 63-day overnight gap-down sum."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    s63 = _rolling_sum(gap.where(gap < 0, 0.0), _TD_QTR)
    return s63.diff(_TD_WEEK)


def ccl_extdrv2_009_intraday_session_loss_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 63-day intraday-session loss sum."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    s63 = _rolling_sum(o2c.where(ret < 0, 0.0), _TD_QTR)
    return s63.diff(_TD_WEEK)


def ccl_extdrv2_010_vol_frac_loss_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume fraction on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    vfrac = _safe_div(loss_vol, total_vol)
    return vfrac.diff(_TD_WEEK)


def ccl_extdrv2_011_vol_frac_loss_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume fraction on loss days."""
    cond = _is_loss_day(close).astype(float)
    loss_vol = _rolling_sum(volume * cond, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    vfrac = _safe_div(loss_vol, total_vol)
    return vfrac.diff(_TD_MON)


def ccl_extdrv2_012_vol_on_loss_vs_gain_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day avg-vol-loss-day / avg-vol-gain-day ratio."""
    cond = _is_loss_day(close)
    avg_loss_vol = volume.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    avg_gain_vol = volume.where(~cond, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(avg_loss_vol, avg_gain_vol)
    return ratio.diff(_TD_WEEK)


def ccl_extdrv2_013_loss_persistence_score_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day loss-persistence score (frac * normalized neg-sum)."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    avg252 = _rolling_mean(s21, _TD_YEAR)
    score = _safe_div(s21, avg252) * frac
    return score.diff(_TD_WEEK)


def ccl_extdrv2_014_capitulation_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 4-component capitulation z-score composite."""
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
    return score.diff(_TD_WEEK)


def ccl_extdrv2_015_loss_acceleration_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of loss-acceleration score (5d-neg-sum / 21d-neg-sum ratio)."""
    lr = _daily_log_ret(close)
    s5  = _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK).abs()
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    score = _safe_div(s5, s21)
    return score.diff(_TD_WEEK)


def ccl_extdrv2_016_vol_surge_loss_flag_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of high-volume loss days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = _is_loss_day(close)
    high_vol = volume > avg_vol * 1.5
    cnt = _rolling_sum((cond & high_vol).astype(float), _TD_QTR)
    return cnt.diff(_TD_MON)


def ccl_extdrv2_017_loss_day_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day loss-day count."""
    cond = _is_loss_day(close)
    cnt = _rolling_sum(cond.astype(float), _TD_MON)
    return cnt.diff(_TD_WEEK)


def ccl_extdrv2_018_worst_run_loss_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 126-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w126 = _rolling_min(cum, _TD_HALF)
    return w126.diff(_TD_MON)


def ccl_extdrv2_019_neg_ret_sum_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 126-day negative-return sum."""
    lr = _daily_log_ret(close)
    s126 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_HALF)
    return s126.diff(_TD_MON)


def ccl_extdrv2_020_loss_breadth_score_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day loss-breadth score (frac * run-frequency)."""
    cond = _is_loss_day(close)
    frac = _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    freq = _rolling_sum(is_start, _TD_QTR)
    score = frac * freq
    return score.diff(_TD_WEEK)


def ccl_extdrv2_021_run_len_max_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day maximum completed-run length."""
    rl = _completed_run_len(close)
    mx = rl.rolling(_TD_YEAR, min_periods=1).max()
    return mx.diff(_TD_MON)


def ccl_extdrv2_022_cum_loss_run_pct_rank_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 126-day percentile rank of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    pr = cum.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)
    return pr.diff(_TD_WEEK)


def ccl_extdrv2_023_neg_ret_sum_21d_ewm_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21-day neg-sum vs its EWM(63) baseline."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    ewm = _ewm_mean(s21, _TD_QTR)
    diff = s21 - ewm
    s = _rolling_std(diff, _TD_YEAR)
    z = _safe_div(diff, s)
    return z.diff(_TD_WEEK)


def ccl_extdrv2_024_vol_adj_cum_loss_run_zscore_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of vol-adjusted current-run cumulative loss z-score."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    cum = (lr * vol_norm).groupby(grp).cumsum().where(cond, 0.0)
    m = _rolling_mean(cum, _TD_YEAR)
    s = _rolling_std(cum, _TD_YEAR)
    z = _safe_div(cum - m, s)
    return z.diff(_TD_WEEK)


def ccl_extdrv2_025_var_1pct_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day 1%-VaR of daily log-returns."""
    lr = _daily_log_ret(close)
    var1 = lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.01)
    return var1.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "ccl_extdrv2_001_run_len_avg_63d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_001_run_len_avg_63d_5d_diff},
    "ccl_extdrv2_002_run_len_avg_252d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_002_run_len_avg_252d_21d_diff},
    "ccl_extdrv2_003_current_run_len_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_003_current_run_len_5d_diff},
    "ccl_extdrv2_004_cum_loss_run_times_len_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_004_cum_loss_run_times_len_5d_diff},
    "ccl_extdrv2_005_cum_loss_run_zscore_63d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_005_cum_loss_run_zscore_63d_5d_diff},
    "ccl_extdrv2_006_loss_day_frac_21d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_006_loss_day_frac_21d_5d_diff},
    "ccl_extdrv2_007_loss_day_frac_63d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_007_loss_day_frac_63d_21d_diff},
    "ccl_extdrv2_008_overnight_gap_loss_63d_5d_diff": {"inputs": ["close", "open"], "func": ccl_extdrv2_008_overnight_gap_loss_63d_5d_diff},
    "ccl_extdrv2_009_intraday_session_loss_63d_5d_diff": {"inputs": ["close", "open"], "func": ccl_extdrv2_009_intraday_session_loss_63d_5d_diff},
    "ccl_extdrv2_010_vol_frac_loss_21d_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv2_010_vol_frac_loss_21d_5d_diff},
    "ccl_extdrv2_011_vol_frac_loss_63d_21d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv2_011_vol_frac_loss_63d_21d_diff},
    "ccl_extdrv2_012_vol_on_loss_vs_gain_21d_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv2_012_vol_on_loss_vs_gain_21d_5d_diff},
    "ccl_extdrv2_013_loss_persistence_score_21d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_013_loss_persistence_score_21d_5d_diff},
    "ccl_extdrv2_014_capitulation_score_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_014_capitulation_score_5d_diff},
    "ccl_extdrv2_015_loss_acceleration_score_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_015_loss_acceleration_score_5d_diff},
    "ccl_extdrv2_016_vol_surge_loss_flag_63d_21d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv2_016_vol_surge_loss_flag_63d_21d_diff},
    "ccl_extdrv2_017_loss_day_count_21d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_017_loss_day_count_21d_5d_diff},
    "ccl_extdrv2_018_worst_run_loss_126d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_018_worst_run_loss_126d_21d_diff},
    "ccl_extdrv2_019_neg_ret_sum_126d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_019_neg_ret_sum_126d_21d_diff},
    "ccl_extdrv2_020_loss_breadth_score_63d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_020_loss_breadth_score_63d_5d_diff},
    "ccl_extdrv2_021_run_len_max_252d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_021_run_len_max_252d_21d_diff},
    "ccl_extdrv2_022_cum_loss_run_pct_rank_126d_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_022_cum_loss_run_pct_rank_126d_5d_diff},
    "ccl_extdrv2_023_neg_ret_sum_21d_ewm_zscore_5d_diff": {"inputs": ["close"], "func": ccl_extdrv2_023_neg_ret_sum_21d_ewm_zscore_5d_diff},
    "ccl_extdrv2_024_vol_adj_cum_loss_run_zscore_5d_diff": {"inputs": ["close", "volume"], "func": ccl_extdrv2_024_vol_adj_cum_loss_run_zscore_5d_diff},
    "ccl_extdrv2_025_var_1pct_252d_21d_diff": {"inputs": ["close"], "func": ccl_extdrv2_025_var_1pct_252d_21d_diff},
}
