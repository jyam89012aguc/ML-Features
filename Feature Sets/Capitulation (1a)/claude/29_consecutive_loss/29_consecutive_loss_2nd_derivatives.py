"""
29_consecutive_loss — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base consecutive-loss magnitude concepts — velocity /
    acceleration of cumulative-run-loss, negative-return sums, worst-run metrics.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def ccl_drv2_001_cum_loss_current_run_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current-run cumulative loss (velocity of in-run loss growth)."""
    cum = _cum_log_loss_in_run(close)
    return cum.diff(_TD_WEEK)


def ccl_drv2_002_cum_loss_current_run_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of current-run cumulative loss (monthly velocity)."""
    cum = _cum_log_loss_in_run(close)
    return cum.diff(_TD_MON)


def ccl_drv2_003_neg_ret_sum_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day negative-return sum."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return s21.diff(_TD_WEEK)


def ccl_drv2_004_neg_ret_sum_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day negative-return sum."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    return s63.diff(_TD_MON)


def ccl_drv2_005_worst_run_loss_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day worst run loss (how fast worst-case is worsening)."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    return w63.diff(_TD_WEEK)


def ccl_drv2_006_worst_run_loss_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w252 = _rolling_min(cum, _TD_YEAR)
    return w252.diff(_TD_MON)


def ccl_drv2_007_neg_vs_pos_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day neg/pos return sum ratio."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_MON)
    ratio = _safe_div(neg, pos)
    return ratio.diff(_TD_WEEK)


def ccl_drv2_008_loss_per_day_current_run_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of average daily loss per day in current run."""
    cum = _cum_log_loss_in_run(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    length = cond.astype(int).groupby(grp).cumsum().astype(float)
    lpd = _safe_div(cum, length.where(cond, np.nan))
    return lpd.diff(_TD_WEEK)


def ccl_drv2_009_cum_loss_from_52wk_high_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown from 52-week high."""
    high252 = _rolling_max(close, _TD_YEAR)
    dd = _log_safe(close) - _log_safe(high252)
    return dd.diff(_TD_WEEK)


def ccl_drv2_010_cum_loss_from_52wk_high_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of drawdown from 52-week high."""
    high252 = _rolling_max(close, _TD_YEAR)
    dd = _log_safe(close) - _log_safe(high252)
    return dd.diff(_TD_MON)


def ccl_drv2_011_neg_ret_sum_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day negative-return sum over trailing 63 days."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return _linslope(s21, _TD_QTR)


def ccl_drv2_012_worst_run_loss_63d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day worst run loss over trailing 63 days."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    return _linslope(w63, _TD_QTR)


def ccl_drv2_013_neg_ret_sum_21d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day neg-return-sum z-score."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    z = _safe_div(s21 - m, s)
    return z.diff(_TD_WEEK)


def ccl_drv2_014_weekly_run_loss_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of weekly (5-day) run loss summed over 21 days."""
    r5 = close.pct_change(_TD_WEEK)
    s21 = _rolling_sum(r5.where(r5 < 0, 0.0), _TD_MON)
    return s21.diff(_TD_WEEK)


def ccl_drv2_015_monthly_run_loss_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day monthly run loss sum."""
    r21 = close.pct_change(_TD_MON)
    s63 = _rolling_sum(r21.where(r21 < 0, 0.0), _TD_QTR)
    return s63.diff(_TD_MON)


def ccl_drv2_016_avg_run_loss_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day avg completed run loss."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    run_loss = run_cum.shift(1).where(run_ended)
    avg252 = run_loss.rolling(_TD_YEAR, min_periods=1).mean()
    return avg252.diff(_TD_MON)


def ccl_drv2_017_var_5pct_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5% VaR of daily returns over 63 days."""
    lr = _daily_log_ret(close)
    var5 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    return var5.diff(_TD_WEEK)


def ccl_drv2_018_cvar_5pct_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of CVaR (5%) over trailing 63 days."""
    lr = _daily_log_ret(close)
    q5 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    tail = lr.where(lr <= q5, np.nan)
    cvar = tail.rolling(_TD_QTR, min_periods=1).mean()
    return cvar.diff(_TD_MON)


def ccl_drv2_019_loss_run_freq_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of losing-run starts."""
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    freq63 = _rolling_sum(is_start, _TD_QTR)
    return freq63.diff(_TD_MON)


def ccl_drv2_020_neg_ret_sum_vol_weighted_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-weighted negative-return sum."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    s21 = _rolling_sum(w_loss, _TD_MON)
    return s21.diff(_TD_WEEK)


def ccl_drv2_021_loss_run_drawdown_ratio_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of worst-run-loss / 252-day price-drawdown ratio."""
    cum = _cum_log_loss_in_run(close)
    worst_run = _rolling_min(cum, _TD_YEAR)
    high252 = _rolling_max(close, _TD_YEAR)
    price_dd = _safe_div(close - high252, high252)
    ratio = _safe_div(worst_run, price_dd)
    return ratio.diff(_TD_MON)


def ccl_drv2_022_neg_ret_below_sma200_sum_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day neg-return sum when close < SMA200."""
    lr = _daily_log_ret(close)
    sma200 = _rolling_mean(close, 200)
    below = close < sma200
    s21 = _rolling_sum(lr.where(below & (lr < 0), 0.0), _TD_MON)
    return s21.diff(_TD_WEEK)


def ccl_drv2_023_loss_per_day_avg_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day avg daily loss over trailing 63 days."""
    lr = _daily_log_ret(close)
    avg21 = _rolling_mean(lr.where(lr < 0, 0.0), _TD_MON)
    return _linslope(avg21, _TD_QTR)


def ccl_drv2_024_cum_loss_from_63d_high_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown from 63-day trailing high."""
    high63 = _rolling_max(close, _TD_QTR)
    dd = _log_safe(close) - _log_safe(high63)
    return dd.diff(_TD_WEEK)


def ccl_drv2_025_worst_run_loss_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day worst run loss over trailing 21 days."""
    cum = _cum_log_loss_in_run(close)
    w21 = _rolling_min(cum, _TD_MON)
    return _linslope(w21, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_REGISTRY_2ND_DERIVATIVES = {
    "ccl_drv2_001_cum_loss_current_run_5d_diff": {"inputs": ["close"], "func": ccl_drv2_001_cum_loss_current_run_5d_diff},
    "ccl_drv2_002_cum_loss_current_run_21d_diff": {"inputs": ["close"], "func": ccl_drv2_002_cum_loss_current_run_21d_diff},
    "ccl_drv2_003_neg_ret_sum_21d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_003_neg_ret_sum_21d_5d_diff},
    "ccl_drv2_004_neg_ret_sum_63d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_004_neg_ret_sum_63d_21d_diff},
    "ccl_drv2_005_worst_run_loss_63d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_005_worst_run_loss_63d_5d_diff},
    "ccl_drv2_006_worst_run_loss_252d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_006_worst_run_loss_252d_21d_diff},
    "ccl_drv2_007_neg_vs_pos_ratio_21d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_007_neg_vs_pos_ratio_21d_5d_diff},
    "ccl_drv2_008_loss_per_day_current_run_5d_diff": {"inputs": ["close"], "func": ccl_drv2_008_loss_per_day_current_run_5d_diff},
    "ccl_drv2_009_cum_loss_from_52wk_high_5d_diff": {"inputs": ["close"], "func": ccl_drv2_009_cum_loss_from_52wk_high_5d_diff},
    "ccl_drv2_010_cum_loss_from_52wk_high_21d_diff": {"inputs": ["close"], "func": ccl_drv2_010_cum_loss_from_52wk_high_21d_diff},
    "ccl_drv2_011_neg_ret_sum_21d_slope_63d": {"inputs": ["close"], "func": ccl_drv2_011_neg_ret_sum_21d_slope_63d},
    "ccl_drv2_012_worst_run_loss_63d_slope_63d": {"inputs": ["close"], "func": ccl_drv2_012_worst_run_loss_63d_slope_63d},
    "ccl_drv2_013_neg_ret_sum_21d_zscore_5d_diff": {"inputs": ["close"], "func": ccl_drv2_013_neg_ret_sum_21d_zscore_5d_diff},
    "ccl_drv2_014_weekly_run_loss_21d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_014_weekly_run_loss_21d_5d_diff},
    "ccl_drv2_015_monthly_run_loss_63d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_015_monthly_run_loss_63d_21d_diff},
    "ccl_drv2_016_avg_run_loss_252d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_016_avg_run_loss_252d_21d_diff},
    "ccl_drv2_017_var_5pct_63d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_017_var_5pct_63d_5d_diff},
    "ccl_drv2_018_cvar_5pct_63d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_018_cvar_5pct_63d_21d_diff},
    "ccl_drv2_019_loss_run_freq_63d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_019_loss_run_freq_63d_21d_diff},
    "ccl_drv2_020_neg_ret_sum_vol_weighted_21d_5d_diff": {"inputs": ["close", "volume"], "func": ccl_drv2_020_neg_ret_sum_vol_weighted_21d_5d_diff},
    "ccl_drv2_021_loss_run_drawdown_ratio_252d_21d_diff": {"inputs": ["close"], "func": ccl_drv2_021_loss_run_drawdown_ratio_252d_21d_diff},
    "ccl_drv2_022_neg_ret_below_sma200_sum_21d_5d_diff": {"inputs": ["close"], "func": ccl_drv2_022_neg_ret_below_sma200_sum_21d_5d_diff},
    "ccl_drv2_023_loss_per_day_avg_21d_slope_63d": {"inputs": ["close"], "func": ccl_drv2_023_loss_per_day_avg_21d_slope_63d},
    "ccl_drv2_024_cum_loss_from_63d_high_5d_diff": {"inputs": ["close"], "func": ccl_drv2_024_cum_loss_from_63d_high_5d_diff},
    "ccl_drv2_025_worst_run_loss_21d_slope_21d": {"inputs": ["close"], "func": ccl_drv2_025_worst_run_loss_21d_slope_21d},
}
