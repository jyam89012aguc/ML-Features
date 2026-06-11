"""
29_consecutive_loss — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative consecutive-loss features — acceleration
    of velocity of cumulative-run-loss magnitudes, neg-return sums, worst-run trends.
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
# Each = diff/slope applied to a 2nd-derivative concept (vel of vel)

def ccl_drv3_001_cum_loss_run_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of current-run cumulative loss (acceleration of loss growth)."""
    cum = _cum_log_loss_in_run(close)
    vel = cum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_002_cum_loss_run_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    vel21 = cum.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_003_neg_ret_sum_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day negative-return sum (acceleration of pain rate)."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_004_neg_ret_sum_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day negative-return sum."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    vel21 = s63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_005_worst_run_loss_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day worst run loss (jerk in worst-case worsening)."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    vel = w63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_006_worst_run_loss_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w252 = _rolling_min(cum, _TD_YEAR)
    vel21 = w252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_007_neg_vs_pos_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day neg/pos sum ratio."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_MON)
    ratio = _safe_div(neg, pos)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_008_cum_loss_52wk_high_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown from 52-week high (acceleration of drawdown)."""
    high252 = _rolling_max(close, _TD_YEAR)
    dd = _log_safe(close) - _log_safe(high252)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_009_cum_loss_52wk_high_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 52wk-high drawdown."""
    high252 = _rolling_max(close, _TD_YEAR)
    dd = _log_safe(close) - _log_safe(high252)
    vel21 = dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_010_neg_ret_sum_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day neg-return sum over 63 days."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    slp = _linslope(s21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def ccl_drv3_011_worst_run_loss_63d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day worst run loss over 63 days."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    slp = _linslope(w63, _TD_QTR)
    return slp.diff(_TD_WEEK)


def ccl_drv3_012_neg_ret_sum_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day neg-return-sum z-score (jerk in extremity)."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    z = _safe_div(s21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_013_weekly_run_loss_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day weekly run loss sum."""
    r5 = close.pct_change(_TD_WEEK)
    s21 = _rolling_sum(r5.where(r5 < 0, 0.0), _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_014_monthly_run_loss_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day monthly run loss sum."""
    r21 = close.pct_change(_TD_MON)
    s63 = _rolling_sum(r21.where(r21 < 0, 0.0), _TD_QTR)
    vel21 = s63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_015_var_5pct_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day 5% VaR (acceleration of tail-risk change)."""
    lr = _daily_log_ret(close)
    var5 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    vel = var5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_016_loss_run_freq_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day losing-run frequency."""
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    freq63 = _rolling_sum(is_start, _TD_QTR)
    vel21 = freq63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_017_avg_run_loss_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day avg completed run loss."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    run_loss = run_cum.shift(1).where(run_ended)
    avg252 = run_loss.rolling(_TD_YEAR, min_periods=1).mean()
    vel21 = avg252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def ccl_drv3_018_loss_per_day_avg_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day avg daily loss."""
    lr = _daily_log_ret(close)
    avg21 = _rolling_mean(lr.where(lr < 0, 0.0), _TD_MON)
    slp = _linslope(avg21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def ccl_drv3_019_neg_ret_sum_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day neg-return sum."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ccl_drv3_020_cum_loss_63d_high_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown from 63-day high."""
    high63 = _rolling_max(close, _TD_QTR)
    dd = _log_safe(close) - _log_safe(high63)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_021_neg_ret_below_sma200_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day neg-return sum below SMA200."""
    lr = _daily_log_ret(close)
    sma200 = _rolling_mean(close, 200)
    below = close < sma200
    s21 = _rolling_sum(lr.where(below & (lr < 0), 0.0), _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def ccl_drv3_022_worst_run_loss_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w21 = _rolling_min(cum, _TD_MON)
    slp = _linslope(w21, _TD_MON)
    return slp.diff(_TD_WEEK)


def ccl_drv3_023_cum_loss_run_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of current-run cumulative loss."""
    cum = _cum_log_loss_in_run(close)
    vel = cum.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def ccl_drv3_024_neg_ret_sum_21d_ewm_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ratio of 21-day neg-return sum to its EWM(63) — acceleration of regime shift."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    ewm = _ewm_mean(s21, _TD_QTR)
    ratio = _safe_div(s21, ewm.abs())
    return ratio.diff(_TD_WEEK)


def ccl_drv3_025_loss_severity_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of the composite loss-severity z-score."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    composite = (_z(s21) + _z(s63) + _z(w63)) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_REGISTRY_3RD_DERIVATIVES = {
    "ccl_drv3_001_cum_loss_run_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_001_cum_loss_run_5d_diff_5d_diff},
    "ccl_drv3_002_cum_loss_run_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_002_cum_loss_run_21d_diff_5d_diff},
    "ccl_drv3_003_neg_ret_sum_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_003_neg_ret_sum_21d_5d_diff_5d_diff},
    "ccl_drv3_004_neg_ret_sum_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_004_neg_ret_sum_63d_21d_diff_5d_diff},
    "ccl_drv3_005_worst_run_loss_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_005_worst_run_loss_63d_5d_diff_5d_diff},
    "ccl_drv3_006_worst_run_loss_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_006_worst_run_loss_252d_21d_diff_5d_diff},
    "ccl_drv3_007_neg_vs_pos_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_007_neg_vs_pos_ratio_21d_5d_diff_5d_diff},
    "ccl_drv3_008_cum_loss_52wk_high_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_008_cum_loss_52wk_high_5d_diff_5d_diff},
    "ccl_drv3_009_cum_loss_52wk_high_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_009_cum_loss_52wk_high_21d_diff_5d_diff},
    "ccl_drv3_010_neg_ret_sum_21d_slope_5d_diff": {"inputs": ["close"], "func": ccl_drv3_010_neg_ret_sum_21d_slope_5d_diff},
    "ccl_drv3_011_worst_run_loss_63d_slope_5d_diff": {"inputs": ["close"], "func": ccl_drv3_011_worst_run_loss_63d_slope_5d_diff},
    "ccl_drv3_012_neg_ret_sum_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_012_neg_ret_sum_zscore_5d_diff_5d_diff},
    "ccl_drv3_013_weekly_run_loss_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_013_weekly_run_loss_21d_5d_diff_5d_diff},
    "ccl_drv3_014_monthly_run_loss_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_014_monthly_run_loss_63d_21d_diff_5d_diff},
    "ccl_drv3_015_var_5pct_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_015_var_5pct_63d_5d_diff_5d_diff},
    "ccl_drv3_016_loss_run_freq_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_016_loss_run_freq_63d_21d_diff_5d_diff},
    "ccl_drv3_017_avg_run_loss_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_017_avg_run_loss_252d_21d_diff_5d_diff},
    "ccl_drv3_018_loss_per_day_avg_21d_slope_5d_diff": {"inputs": ["close"], "func": ccl_drv3_018_loss_per_day_avg_21d_slope_5d_diff},
    "ccl_drv3_019_neg_ret_sum_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": ccl_drv3_019_neg_ret_sum_21d_5d_diff_slope_21d},
    "ccl_drv3_020_cum_loss_63d_high_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_020_cum_loss_63d_high_5d_diff_5d_diff},
    "ccl_drv3_021_neg_ret_below_sma200_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_021_neg_ret_below_sma200_21d_5d_diff_5d_diff},
    "ccl_drv3_022_worst_run_loss_21d_slope_5d_diff": {"inputs": ["close"], "func": ccl_drv3_022_worst_run_loss_21d_slope_5d_diff},
    "ccl_drv3_023_cum_loss_run_5d_diff_slope_21d": {"inputs": ["close"], "func": ccl_drv3_023_cum_loss_run_5d_diff_slope_21d},
    "ccl_drv3_024_neg_ret_sum_21d_ewm_5d_diff": {"inputs": ["close"], "func": ccl_drv3_024_neg_ret_sum_21d_ewm_5d_diff},
    "ccl_drv3_025_loss_severity_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": ccl_drv3_025_loss_severity_composite_5d_diff_5d_diff},
}
