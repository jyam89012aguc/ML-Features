"""
29_consecutive_loss — Base Features 076-150
Domain: magnitude/severity of cumulative loss within losing runs — max-run loss
    windows, loss acceleration, intraday-range loss, weekly/monthly run losses,
    drawdown-run composition, loss-rate z-scores, tail distribution features.
    Does NOT count streak lengths (folder 08); measures LOSS RETURN MAGNITUDE.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _completed_run_loss(close: pd.Series) -> pd.Series:
    """Series: total log-return of a completed run, placed on the first non-run day
    (the day after the run ends) and NaN elsewhere.  Strictly backward-looking."""
    lr = _daily_log_ret(close)
    cond = _is_loss_day(close)
    grp = _run_group(cond)
    run_cum = lr.groupby(grp).cumsum().where(cond, 0.0)
    run_ended = (~cond) & cond.shift(1).fillna(False)
    return run_cum.shift(1).where(run_ended)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-087): Run-loss over weekly / monthly horizons ---

def ccl_076_weekly_run_loss_21d(close: pd.Series) -> pd.Series:
    """Sum of negative 5-day returns over trailing 21 days (weekly loss runs)."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_sum(r5.where(r5 < 0, 0.0), _TD_MON)


def ccl_077_weekly_run_loss_63d(close: pd.Series) -> pd.Series:
    """Sum of negative 5-day returns over trailing 63 days."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_sum(r5.where(r5 < 0, 0.0), _TD_QTR)


def ccl_078_weekly_run_loss_252d(close: pd.Series) -> pd.Series:
    """Sum of negative 5-day returns over trailing 252 days."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_sum(r5.where(r5 < 0, 0.0), _TD_YEAR)


def ccl_079_worst_weekly_run_loss_63d(close: pd.Series) -> pd.Series:
    """Minimum (worst) 5-day rolling return over trailing 63 days."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_min(r5, _TD_QTR)


def ccl_080_worst_weekly_run_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum 5-day rolling return over trailing 252 days."""
    r5 = close.pct_change(_TD_WEEK)
    return _rolling_min(r5, _TD_YEAR)


def ccl_081_monthly_run_loss_63d(close: pd.Series) -> pd.Series:
    """Sum of negative 21-day returns over trailing 63 days."""
    r21 = close.pct_change(_TD_MON)
    return _rolling_sum(r21.where(r21 < 0, 0.0), _TD_QTR)


def ccl_082_monthly_run_loss_252d(close: pd.Series) -> pd.Series:
    """Sum of negative 21-day returns over trailing 252 days."""
    r21 = close.pct_change(_TD_MON)
    return _rolling_sum(r21.where(r21 < 0, 0.0), _TD_YEAR)


def ccl_083_worst_monthly_run_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum 21-day rolling return over trailing 252 days."""
    r21 = close.pct_change(_TD_MON)
    return _rolling_min(r21, _TD_YEAR)


def ccl_084_qtr_run_loss_252d(close: pd.Series) -> pd.Series:
    """Sum of negative 63-day returns over trailing 252 days."""
    r63 = close.pct_change(_TD_QTR)
    return _rolling_sum(r63.where(r63 < 0, 0.0), _TD_YEAR)


def ccl_085_worst_qtr_run_loss_252d(close: pd.Series) -> pd.Series:
    """Minimum 63-day rolling return over trailing 252 days."""
    r63 = close.pct_change(_TD_QTR)
    return _rolling_min(r63, _TD_YEAR)


def ccl_086_weekly_loss_norm_21d_avg(close: pd.Series) -> pd.Series:
    """Worst weekly run loss normalized by 21-day avg weekly loss."""
    r5 = close.pct_change(_TD_WEEK)
    worst = _rolling_min(r5, _TD_QTR)
    avg = _rolling_mean(r5.where(r5 < 0, np.nan), _TD_MON)
    return _safe_div(worst, avg.abs())


def ccl_087_monthly_loss_norm_252d_avg(close: pd.Series) -> pd.Series:
    """Worst monthly run loss normalized by 252-day avg monthly loss."""
    r21 = close.pct_change(_TD_MON)
    worst = _rolling_min(r21, _TD_YEAR)
    avg = _rolling_mean(r21.where(r21 < 0, np.nan), _TD_YEAR)
    return _safe_div(worst, avg.abs())


# --- Group I (088-099): Loss severity with intraday range components ---

def ccl_088_intraday_loss_range_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of high-low range on loss days over 21 days (panic range cost)."""
    ret = _daily_log_ret(close)
    rng = (high - low) / close.shift(1)
    return _rolling_sum(rng.where(ret < 0, 0.0), _TD_MON)


def ccl_089_intraday_loss_range_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of intraday range on loss days over 63 days."""
    ret = _daily_log_ret(close)
    rng = (high - low) / close.shift(1)
    return _rolling_sum(rng.where(ret < 0, 0.0), _TD_QTR)


def ccl_090_avg_intraday_range_loss_days_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday range on loss days over 21 days."""
    ret = _daily_log_ret(close)
    rng = (high - low) / close.shift(1)
    return rng.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


def ccl_091_avg_intraday_range_loss_days_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday range on loss days over 63 days."""
    ret = _daily_log_ret(close)
    rng = (high - low) / close.shift(1)
    return rng.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def ccl_092_atr_normalized_neg_ret_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of ATR(14)-normalized negative returns over 21 days."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    norm = _safe_div(lr, atr14)
    return _rolling_sum(norm.where(lr < 0, 0.0), _TD_MON)


def ccl_093_atr_normalized_neg_ret_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of ATR(14)-normalized negative returns over 63 days."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    norm = _safe_div(lr, atr14)
    return _rolling_sum(norm.where(lr < 0, 0.0), _TD_QTR)


def ccl_094_worst_atr_normalized_loss_day_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Worst single-day ATR-normalized log-loss over trailing 63 days."""
    atr14 = _rolling_mean(_tr(close, high, low), 14)
    lr = _daily_log_ret(close)
    norm = _safe_div(lr, atr14)
    return _rolling_min(norm, _TD_QTR)


def ccl_095_close_to_low_loss_sum_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of (close-low)/close on loss days over 21 days (close-to-low severity)."""
    ret = _daily_log_ret(close)
    c2l = _safe_div(close - low, close)
    return _rolling_sum(c2l.where(ret < 0, 0.0), _TD_MON)


def ccl_096_close_to_low_loss_sum_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of (close-low)/close on loss days over 63 days."""
    ret = _daily_log_ret(close)
    c2l = _safe_div(close - low, close)
    return _rolling_sum(c2l.where(ret < 0, 0.0), _TD_QTR)


def ccl_097_open_to_close_loss_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of (open-close)/open on loss days over 21 days (intraday-session loss)."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    return _rolling_sum(o2c.where(ret < 0, 0.0), _TD_MON)


def ccl_098_open_to_close_loss_sum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of (open-close)/open on loss days over 63 days."""
    ret = _daily_log_ret(close)
    o2c = _safe_div(open - close, open)
    return _rolling_sum(o2c.where(ret < 0, 0.0), _TD_QTR)


def ccl_099_overnight_gap_loss_sum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of gap-down returns (open < prior close) over 21 days."""
    gap = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum(gap.where(gap < 0, 0.0), _TD_MON)


# --- Group J (100-111): Loss-run composite and interaction scores ---

def ccl_100_loss_run_vol_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative-return sum times avg relative volume on loss days over 21 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    score = lr.where(lr < 0, 0.0) * vol_norm
    return _rolling_sum(score, _TD_MON)


def ccl_101_loss_run_vol_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative-return sum times relative volume on loss days over 63 days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    score = lr.where(lr < 0, 0.0) * vol_norm
    return _rolling_sum(score, _TD_QTR)


def ccl_102_current_run_loss_times_vol_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current run cumulative loss scaled by normalized volume (panic index)."""
    cum = _cum_log_loss_in_run(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return cum * vol_norm


def ccl_103_worst_run_loss_252d_norm_by_std(close: pd.Series) -> pd.Series:
    """252-day worst run loss divided by 252-day std of log returns."""
    cum = _cum_log_loss_in_run(close)
    worst = _rolling_min(cum, _TD_YEAR)
    lr = _daily_log_ret(close)
    s = _rolling_std(lr, _TD_YEAR)
    return _safe_div(worst, s)


def ccl_104_neg_ret_sum_21d_norm_by_std_252d(close: pd.Series) -> pd.Series:
    """21-day negative-return sum normalized by 252-day return std."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    s = _rolling_std(lr, _TD_YEAR)
    return _safe_div(s21, s)


def ccl_105_neg_ret_sum_63d_norm_by_std_252d(close: pd.Series) -> pd.Series:
    """63-day negative-return sum normalized by 252-day return std."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    s = _rolling_std(lr, _TD_YEAR)
    return _safe_div(s63, s)


def ccl_106_loss_run_drawdown_ratio_252d(close: pd.Series) -> pd.Series:
    """252-day worst run loss divided by 252-day total price drawdown."""
    cum = _cum_log_loss_in_run(close)
    worst_run = _rolling_min(cum, _TD_YEAR)
    price_dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _safe_div(worst_run, price_dd)


def ccl_107_loss_run_freq_21d(close: pd.Series) -> pd.Series:
    """Count of distinct losing runs (run starts) in trailing 21 days."""
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    return _rolling_sum(is_start, _TD_MON)


def ccl_108_loss_run_freq_63d(close: pd.Series) -> pd.Series:
    """Count of distinct losing runs in trailing 63 days."""
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    return _rolling_sum(is_start, _TD_QTR)


def ccl_109_loss_run_freq_252d(close: pd.Series) -> pd.Series:
    """Count of distinct losing runs in trailing 252 days."""
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def ccl_110_avg_loss_per_run_63d(close: pd.Series) -> pd.Series:
    """Total 63-day negative-return sum divided by number of runs."""
    lr = _daily_log_ret(close)
    neg_sum = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    n_runs = _rolling_sum(is_start, _TD_QTR).replace(0, np.nan)
    return _safe_div(neg_sum, n_runs)


def ccl_111_avg_loss_per_run_252d(close: pd.Series) -> pd.Series:
    """Total 252-day negative-return sum divided by number of runs."""
    lr = _daily_log_ret(close)
    neg_sum = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR)
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    n_runs = _rolling_sum(is_start, _TD_YEAR).replace(0, np.nan)
    return _safe_div(neg_sum, n_runs)


# --- Group K (112-123): Z-scores and percentile ranks of loss magnitudes ---

def ccl_112_neg_ret_sum_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day negative-return sum vs 252-day distribution."""
    lr = _daily_log_ret(close)
    s5 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_WEEK)
    m = _rolling_mean(s5, _TD_YEAR)
    s = _rolling_std(s5, _TD_YEAR)
    return _safe_div(s5 - m, s)


def ccl_113_neg_ret_sum_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day negative-return sum vs 252-day distribution."""
    lr = _daily_log_ret(close)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    m = _rolling_mean(s63, _TD_YEAR)
    s = _rolling_std(s63, _TD_YEAR)
    return _safe_div(s63 - m, s)


def ccl_114_worst_run_loss_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day worst run loss vs 252-day distribution."""
    cum = _cum_log_loss_in_run(close)
    w21 = _rolling_min(cum, _TD_MON)
    m = _rolling_mean(w21, _TD_YEAR)
    s = _rolling_std(w21, _TD_YEAR)
    return _safe_div(w21 - m, s)


def ccl_115_worst_run_loss_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day worst run loss vs 252-day distribution."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    m = _rolling_mean(w63, _TD_YEAR)
    s = _rolling_std(w63, _TD_YEAR)
    return _safe_div(w63 - m, s)


def ccl_116_worst_run_loss_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day worst run loss within 252-day distribution."""
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    return w63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_117_neg_ret_sum_21d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day negative-return sum."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return s21.expanding(min_periods=5).rank(pct=True)


def ccl_118_avg_run_loss_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day avg run loss vs 252-day distribution."""
    run_loss = _completed_run_loss(close)
    avg63 = run_loss.rolling(_TD_QTR, min_periods=1).mean()
    m = _rolling_mean(avg63, _TD_YEAR)
    s = _rolling_std(avg63, _TD_YEAR)
    return _safe_div(avg63 - m, s)


def ccl_119_worst_run_loss_252d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day worst run loss (all-history extremity)."""
    cum = _cum_log_loss_in_run(close)
    w252 = _rolling_min(cum, _TD_YEAR)
    m = w252.expanding(min_periods=5).mean()
    s = w252.expanding(min_periods=5).std()
    return _safe_div(w252 - m, s)


def ccl_120_loss_per_run_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of avg-loss-per-run-21d vs 252-day distribution."""
    lr = _daily_log_ret(close)
    neg_sum = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    cond = _is_loss_day(close)
    is_start = (cond & (~cond.shift(1).fillna(False))).astype(float)
    n_runs = _rolling_sum(is_start, _TD_MON).replace(0, np.nan)
    ratio = _safe_div(neg_sum, n_runs)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def ccl_121_neg_sum_pct_rank_21d_expanding(close: pd.Series) -> pd.Series:
    """Expanding rank of 21-day neg-return sum normalized by all-history."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    return s21.expanding(min_periods=5).rank(pct=True)


def ccl_122_loss_severity_composite_zscore(close: pd.Series) -> pd.Series:
    """Composite z-score: avg of z-scores of 21d neg-sum, 63d neg-sum, worst-run-63d."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR)
    cum = _cum_log_loss_in_run(close)
    w63 = _rolling_min(cum, _TD_QTR)
    def _z(x):
        m = _rolling_mean(x, _TD_YEAR)
        s = _rolling_std(x, _TD_YEAR)
        return _safe_div(x - m, s)
    return (_z(s21) + _z(s63) + _z(w63)) / 3.0


def ccl_123_neg_ret_sum_21d_ewm_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day negative-return sum to its EWM(63) average."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON)
    ewm = _ewm_mean(s21, _TD_QTR)
    return _safe_div(s21, ewm.abs())


# --- Group L (124-135): Loss magnitude vs trailing highs and price levels ---

def ccl_124_cum_loss_from_52wk_high(close: pd.Series) -> pd.Series:
    """Log-return of close from 252-day trailing high (drawdown from peak)."""
    high252 = _rolling_max(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(high252)


def ccl_125_cum_loss_from_63d_high(close: pd.Series) -> pd.Series:
    """Log-return of close from 63-day trailing high."""
    high63 = _rolling_max(close, _TD_QTR)
    return _log_safe(close) - _log_safe(high63)


def ccl_126_cum_loss_from_21d_high(close: pd.Series) -> pd.Series:
    """Log-return of close from 21-day trailing high."""
    high21 = _rolling_max(close, _TD_MON)
    return _log_safe(close) - _log_safe(high21)


def ccl_127_cum_loss_from_52wk_high_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 52wk-high drawdown within trailing 252 days."""
    dd = ccl_124_cum_loss_from_52wk_high(close)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ccl_128_cum_loss_from_52wk_high_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 52wk-high drawdown vs 252-day distribution."""
    dd = ccl_124_cum_loss_from_52wk_high(close)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    return _safe_div(dd - m, s)


def ccl_129_run_loss_vs_52wk_dd_ratio(close: pd.Series) -> pd.Series:
    """Current run cumulative loss as fraction of 52-week drawdown."""
    cum = _cum_log_loss_in_run(close)
    dd = ccl_124_cum_loss_from_52wk_high(close)
    return _safe_div(cum, dd.abs())


def ccl_130_run_loss_vs_sma200_gap(close: pd.Series) -> pd.Series:
    """Current run loss divided by pct distance of close below SMA200."""
    cum = _cum_log_loss_in_run(close)
    sma200 = _rolling_mean(close, 200)
    gap = _safe_div(close - sma200, sma200)
    return _safe_div(cum, gap.abs())


def ccl_131_cum_loss_from_ema21_high(close: pd.Series) -> pd.Series:
    """Log-return of close from 21-day EMA (distance below EMA21)."""
    ema21 = _ewm_mean(close, _TD_MON)
    return _log_safe(close) - _log_safe(ema21)


def ccl_132_cum_loss_from_ema63_high(close: pd.Series) -> pd.Series:
    """Log-return of close from 63-day EMA."""
    ema63 = _ewm_mean(close, _TD_QTR)
    return _log_safe(close) - _log_safe(ema63)


def ccl_133_neg_ret_below_sma200_sum_21d(close: pd.Series) -> pd.Series:
    """Sum of negative returns on days when close < SMA200, over 21 days."""
    lr = _daily_log_ret(close)
    sma200 = _rolling_mean(close, 200)
    below = close < sma200
    return _rolling_sum(lr.where(below & (lr < 0), 0.0), _TD_MON)


def ccl_134_neg_ret_below_sma200_sum_63d(close: pd.Series) -> pd.Series:
    """Sum of negative returns on days when close < SMA200, over 63 days."""
    lr = _daily_log_ret(close)
    sma200 = _rolling_mean(close, 200)
    below = close < sma200
    return _rolling_sum(lr.where(below & (lr < 0), 0.0), _TD_QTR)


def ccl_135_run_loss_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day change in current-run cumulative loss (how fast run loss is growing)."""
    cum = _cum_log_loss_in_run(close)
    return cum.diff(_TD_WEEK)


# --- Group M (136-150): Tail risk, vol-adjusted, and cross-window ratios ---

def ccl_136_var_1pct_daily_loss_63d(close: pd.Series) -> pd.Series:
    """1% VaR of daily log-returns over trailing 63 days (worst 1st-percentile loss)."""
    lr = _daily_log_ret(close)
    return lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.01)


def ccl_137_var_5pct_daily_loss_63d(close: pd.Series) -> pd.Series:
    """5% VaR of daily log-returns over trailing 63 days."""
    lr = _daily_log_ret(close)
    return lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)


def ccl_138_var_5pct_daily_loss_252d(close: pd.Series) -> pd.Series:
    """5% VaR of daily log-returns over trailing 252 days."""
    lr = _daily_log_ret(close)
    return lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)


def ccl_139_cvar_5pct_daily_loss_63d(close: pd.Series) -> pd.Series:
    """Conditional VaR (CVaR/ES) at 5%: avg of bottom-5% log-returns over 63 days."""
    lr = _daily_log_ret(close)
    q5 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    tail = lr.where(lr <= q5, np.nan)
    return tail.rolling(_TD_QTR, min_periods=1).mean()


def ccl_140_cvar_5pct_daily_loss_252d(close: pd.Series) -> pd.Series:
    """CVaR at 5%: avg of bottom-5% log-returns over 252 days."""
    lr = _daily_log_ret(close)
    q5 = lr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.05)
    tail = lr.where(lr <= q5, np.nan)
    return tail.rolling(_TD_YEAR, min_periods=1).mean()


def ccl_141_loss_to_gain_ratio_vol_adjusted_21d(close: pd.Series) -> pd.Series:
    """Vol-adjusted loss/gain ratio over 21 days: (neg sum / pos sum) / std."""
    lr = _daily_log_ret(close)
    neg = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    pos = _rolling_sum(lr.where(lr > 0, 0.0), _TD_MON)
    s = _rolling_std(lr, _TD_MON)
    raw = _safe_div(neg, pos)
    return _safe_div(raw, s)


def ccl_142_run_loss_count_gt20pct_252d(close: pd.Series) -> pd.Series:
    """Count of completed runs with cumulative loss > 20% in trailing 252 days."""
    run_loss = _completed_run_loss(close)
    big = (run_loss.abs() > 0.20).astype(float).fillna(0.0)
    return _rolling_sum(big, _TD_YEAR)


def ccl_143_run_loss_90th_pct_vs_median_252d(close: pd.Series) -> pd.Series:
    """Ratio of worst-10th-pct run loss to median run loss over 252 days."""
    run_loss = _completed_run_loss(close)
    q10 = run_loss.rolling(_TD_YEAR, min_periods=5).quantile(0.10)
    med = run_loss.rolling(_TD_YEAR, min_periods=5).median()
    return _safe_div(q10.abs(), med.abs())


def ccl_144_neg_ret_sum_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day negative-return sum to 63-day negative-return sum."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    s63 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR).abs()
    return _safe_div(s21, s63)


def ccl_145_neg_ret_sum_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day negative-return sum to 252-day negative-return sum."""
    lr = _daily_log_ret(close)
    s21 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    s252 = _rolling_sum(lr.where(lr < 0, 0.0), _TD_YEAR).abs()
    return _safe_div(s21, s252)


def ccl_146_worst_run_loss_5d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5-day worst run loss to 252-day worst run loss."""
    cum = _cum_log_loss_in_run(close)
    w5   = _rolling_min(cum, _TD_WEEK)
    w252 = _rolling_min(cum, _TD_YEAR)
    return _safe_div(w5.abs(), w252.abs())


def ccl_147_loss_run_pain_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pain index: 21-day neg-return sum times avg vol-ratio on loss days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    loss_vol = vol_norm.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    neg_sum = _rolling_sum(lr.where(lr < 0, 0.0), _TD_MON).abs()
    return neg_sum * loss_vol.fillna(1.0)


def ccl_148_loss_run_pain_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pain index: 63-day neg-return sum times avg vol-ratio on loss days."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    loss_vol = vol_norm.where(lr < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    neg_sum = _rolling_sum(lr.where(lr < 0, 0.0), _TD_QTR).abs()
    return neg_sum * loss_vol.fillna(1.0)


def ccl_149_neg_ret_sum_half_year(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over trailing 126 days."""
    lr = _daily_log_ret(close)
    return _rolling_sum(lr.where(lr < 0, 0.0), _TD_HALF)


def ccl_150_loss_severity_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite distress: vol-weighted 21d neg-sum / 252d avg, scaled by loss fraction."""
    lr = _daily_log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    w_loss = lr.where(lr < 0, 0.0) * vol_norm
    s21 = _rolling_sum(w_loss, _TD_MON)
    avg252 = _rolling_mean(s21.abs(), _TD_YEAR)
    loss_frac = _rolling_sum((lr < 0).astype(float), _TD_MON) / _TD_MON
    return _safe_div(s21.abs(), avg252.clip(lower=_EPS)) * loss_frac


# ── Registry ──────────────────────────────────────────────────────────────────

CONSECUTIVE_LOSS_REGISTRY_076_150 = {
    "ccl_076_weekly_run_loss_21d": {"inputs": ["close"], "func": ccl_076_weekly_run_loss_21d},
    "ccl_077_weekly_run_loss_63d": {"inputs": ["close"], "func": ccl_077_weekly_run_loss_63d},
    "ccl_078_weekly_run_loss_252d": {"inputs": ["close"], "func": ccl_078_weekly_run_loss_252d},
    "ccl_079_worst_weekly_run_loss_63d": {"inputs": ["close"], "func": ccl_079_worst_weekly_run_loss_63d},
    "ccl_080_worst_weekly_run_loss_252d": {"inputs": ["close"], "func": ccl_080_worst_weekly_run_loss_252d},
    "ccl_081_monthly_run_loss_63d": {"inputs": ["close"], "func": ccl_081_monthly_run_loss_63d},
    "ccl_082_monthly_run_loss_252d": {"inputs": ["close"], "func": ccl_082_monthly_run_loss_252d},
    "ccl_083_worst_monthly_run_loss_252d": {"inputs": ["close"], "func": ccl_083_worst_monthly_run_loss_252d},
    "ccl_084_qtr_run_loss_252d": {"inputs": ["close"], "func": ccl_084_qtr_run_loss_252d},
    "ccl_085_worst_qtr_run_loss_252d": {"inputs": ["close"], "func": ccl_085_worst_qtr_run_loss_252d},
    "ccl_086_weekly_loss_norm_21d_avg": {"inputs": ["close"], "func": ccl_086_weekly_loss_norm_21d_avg},
    "ccl_087_monthly_loss_norm_252d_avg": {"inputs": ["close"], "func": ccl_087_monthly_loss_norm_252d_avg},
    "ccl_088_intraday_loss_range_sum_21d": {"inputs": ["close", "high", "low"], "func": ccl_088_intraday_loss_range_sum_21d},
    "ccl_089_intraday_loss_range_sum_63d": {"inputs": ["close", "high", "low"], "func": ccl_089_intraday_loss_range_sum_63d},
    "ccl_090_avg_intraday_range_loss_days_21d": {"inputs": ["close", "high", "low"], "func": ccl_090_avg_intraday_range_loss_days_21d},
    "ccl_091_avg_intraday_range_loss_days_63d": {"inputs": ["close", "high", "low"], "func": ccl_091_avg_intraday_range_loss_days_63d},
    "ccl_092_atr_normalized_neg_ret_sum_21d": {"inputs": ["close", "high", "low"], "func": ccl_092_atr_normalized_neg_ret_sum_21d},
    "ccl_093_atr_normalized_neg_ret_sum_63d": {"inputs": ["close", "high", "low"], "func": ccl_093_atr_normalized_neg_ret_sum_63d},
    "ccl_094_worst_atr_normalized_loss_day_63d": {"inputs": ["close", "high", "low"], "func": ccl_094_worst_atr_normalized_loss_day_63d},
    "ccl_095_close_to_low_loss_sum_21d": {"inputs": ["close", "low"], "func": ccl_095_close_to_low_loss_sum_21d},
    "ccl_096_close_to_low_loss_sum_63d": {"inputs": ["close", "low"], "func": ccl_096_close_to_low_loss_sum_63d},
    "ccl_097_open_to_close_loss_sum_21d": {"inputs": ["close", "open"], "func": ccl_097_open_to_close_loss_sum_21d},
    "ccl_098_open_to_close_loss_sum_63d": {"inputs": ["close", "open"], "func": ccl_098_open_to_close_loss_sum_63d},
    "ccl_099_overnight_gap_loss_sum_21d": {"inputs": ["close", "open"], "func": ccl_099_overnight_gap_loss_sum_21d},
    "ccl_100_loss_run_vol_score_21d": {"inputs": ["close", "volume"], "func": ccl_100_loss_run_vol_score_21d},
    "ccl_101_loss_run_vol_score_63d": {"inputs": ["close", "volume"], "func": ccl_101_loss_run_vol_score_63d},
    "ccl_102_current_run_loss_times_vol_norm": {"inputs": ["close", "volume"], "func": ccl_102_current_run_loss_times_vol_norm},
    "ccl_103_worst_run_loss_252d_norm_by_std": {"inputs": ["close"], "func": ccl_103_worst_run_loss_252d_norm_by_std},
    "ccl_104_neg_ret_sum_21d_norm_by_std_252d": {"inputs": ["close"], "func": ccl_104_neg_ret_sum_21d_norm_by_std_252d},
    "ccl_105_neg_ret_sum_63d_norm_by_std_252d": {"inputs": ["close"], "func": ccl_105_neg_ret_sum_63d_norm_by_std_252d},
    "ccl_106_loss_run_drawdown_ratio_252d": {"inputs": ["close"], "func": ccl_106_loss_run_drawdown_ratio_252d},
    "ccl_107_loss_run_freq_21d": {"inputs": ["close"], "func": ccl_107_loss_run_freq_21d},
    "ccl_108_loss_run_freq_63d": {"inputs": ["close"], "func": ccl_108_loss_run_freq_63d},
    "ccl_109_loss_run_freq_252d": {"inputs": ["close"], "func": ccl_109_loss_run_freq_252d},
    "ccl_110_avg_loss_per_run_63d": {"inputs": ["close"], "func": ccl_110_avg_loss_per_run_63d},
    "ccl_111_avg_loss_per_run_252d": {"inputs": ["close"], "func": ccl_111_avg_loss_per_run_252d},
    "ccl_112_neg_ret_sum_5d_zscore_252d": {"inputs": ["close"], "func": ccl_112_neg_ret_sum_5d_zscore_252d},
    "ccl_113_neg_ret_sum_63d_zscore_252d": {"inputs": ["close"], "func": ccl_113_neg_ret_sum_63d_zscore_252d},
    "ccl_114_worst_run_loss_21d_zscore_252d": {"inputs": ["close"], "func": ccl_114_worst_run_loss_21d_zscore_252d},
    "ccl_115_worst_run_loss_63d_zscore_252d": {"inputs": ["close"], "func": ccl_115_worst_run_loss_63d_zscore_252d},
    "ccl_116_worst_run_loss_63d_pct_rank_252d": {"inputs": ["close"], "func": ccl_116_worst_run_loss_63d_pct_rank_252d},
    "ccl_117_neg_ret_sum_21d_expanding_rank": {"inputs": ["close"], "func": ccl_117_neg_ret_sum_21d_expanding_rank},
    "ccl_118_avg_run_loss_63d_zscore_252d": {"inputs": ["close"], "func": ccl_118_avg_run_loss_63d_zscore_252d},
    "ccl_119_worst_run_loss_252d_expanding_zscore": {"inputs": ["close"], "func": ccl_119_worst_run_loss_252d_expanding_zscore},
    "ccl_120_loss_per_run_21d_zscore_252d": {"inputs": ["close"], "func": ccl_120_loss_per_run_21d_zscore_252d},
    "ccl_121_neg_sum_pct_rank_21d_expanding": {"inputs": ["close"], "func": ccl_121_neg_sum_pct_rank_21d_expanding},
    "ccl_122_loss_severity_composite_zscore": {"inputs": ["close"], "func": ccl_122_loss_severity_composite_zscore},
    "ccl_123_neg_ret_sum_21d_ewm_ratio": {"inputs": ["close"], "func": ccl_123_neg_ret_sum_21d_ewm_ratio},
    "ccl_124_cum_loss_from_52wk_high": {"inputs": ["close"], "func": ccl_124_cum_loss_from_52wk_high},
    "ccl_125_cum_loss_from_63d_high": {"inputs": ["close"], "func": ccl_125_cum_loss_from_63d_high},
    "ccl_126_cum_loss_from_21d_high": {"inputs": ["close"], "func": ccl_126_cum_loss_from_21d_high},
    "ccl_127_cum_loss_from_52wk_high_pct_rank_252d": {"inputs": ["close"], "func": ccl_127_cum_loss_from_52wk_high_pct_rank_252d},
    "ccl_128_cum_loss_from_52wk_high_zscore": {"inputs": ["close"], "func": ccl_128_cum_loss_from_52wk_high_zscore},
    "ccl_129_run_loss_vs_52wk_dd_ratio": {"inputs": ["close"], "func": ccl_129_run_loss_vs_52wk_dd_ratio},
    "ccl_130_run_loss_vs_sma200_gap": {"inputs": ["close"], "func": ccl_130_run_loss_vs_sma200_gap},
    "ccl_131_cum_loss_from_ema21_high": {"inputs": ["close"], "func": ccl_131_cum_loss_from_ema21_high},
    "ccl_132_cum_loss_from_ema63_high": {"inputs": ["close"], "func": ccl_132_cum_loss_from_ema63_high},
    "ccl_133_neg_ret_below_sma200_sum_21d": {"inputs": ["close"], "func": ccl_133_neg_ret_below_sma200_sum_21d},
    "ccl_134_neg_ret_below_sma200_sum_63d": {"inputs": ["close"], "func": ccl_134_neg_ret_below_sma200_sum_63d},
    "ccl_135_run_loss_acceleration_5d": {"inputs": ["close"], "func": ccl_135_run_loss_acceleration_5d},
    "ccl_136_var_1pct_daily_loss_63d": {"inputs": ["close"], "func": ccl_136_var_1pct_daily_loss_63d},
    "ccl_137_var_5pct_daily_loss_63d": {"inputs": ["close"], "func": ccl_137_var_5pct_daily_loss_63d},
    "ccl_138_var_5pct_daily_loss_252d": {"inputs": ["close"], "func": ccl_138_var_5pct_daily_loss_252d},
    "ccl_139_cvar_5pct_daily_loss_63d": {"inputs": ["close"], "func": ccl_139_cvar_5pct_daily_loss_63d},
    "ccl_140_cvar_5pct_daily_loss_252d": {"inputs": ["close"], "func": ccl_140_cvar_5pct_daily_loss_252d},
    "ccl_141_loss_to_gain_ratio_vol_adjusted_21d": {"inputs": ["close"], "func": ccl_141_loss_to_gain_ratio_vol_adjusted_21d},
    "ccl_142_run_loss_count_gt20pct_252d": {"inputs": ["close"], "func": ccl_142_run_loss_count_gt20pct_252d},
    "ccl_143_run_loss_90th_pct_vs_median_252d": {"inputs": ["close"], "func": ccl_143_run_loss_90th_pct_vs_median_252d},
    "ccl_144_neg_ret_sum_21d_vs_63d_ratio": {"inputs": ["close"], "func": ccl_144_neg_ret_sum_21d_vs_63d_ratio},
    "ccl_145_neg_ret_sum_21d_vs_252d_ratio": {"inputs": ["close"], "func": ccl_145_neg_ret_sum_21d_vs_252d_ratio},
    "ccl_146_worst_run_loss_5d_vs_252d_ratio": {"inputs": ["close"], "func": ccl_146_worst_run_loss_5d_vs_252d_ratio},
    "ccl_147_loss_run_pain_index_21d": {"inputs": ["close", "volume"], "func": ccl_147_loss_run_pain_index_21d},
    "ccl_148_loss_run_pain_index_63d": {"inputs": ["close", "volume"], "func": ccl_148_loss_run_pain_index_63d},
    "ccl_149_neg_ret_sum_half_year": {"inputs": ["close"], "func": ccl_149_neg_ret_sum_half_year},
    "ccl_150_loss_severity_distress_index": {"inputs": ["close", "volume"], "func": ccl_150_loss_severity_distress_index},
}
