"""
27_momentum_exhaustion — Base Features 076-150
Domain: loss of downside momentum — deceleration / exhaustion of the decline
Candle exhaustion, return percentiles, drawdown dynamics, trend-relative decay,
intraday exhaustion, Kaufman ER, TD/DeMark sequential buy-setup counts.
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _down_ret_abs(close: pd.Series) -> pd.Series:
    """Absolute daily log-return on down days; NaN otherwise."""
    r = _log_ret(close)
    return r.abs().where(r < 0, np.nan)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


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


def _kaufman_er(close: pd.Series, n: int) -> pd.Series:
    """Kaufman Efficiency Ratio over n periods."""
    direction = (close - close.shift(n)).abs()
    volatility = close.diff(1).abs().rolling(n, min_periods=max(2, n // 2)).sum()
    return _safe_div(direction, volatility)


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of Change over n periods: (close/close.shift(n)-1)*100."""
    return _safe_div(close, close.shift(n).replace(0, np.nan)) * 100.0 - 100.0


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    """
    TD/DeMark buy-setup running count (backward-looking only).
    Increments each bar where close < close.shift(4); resets on any bar
    where close >= close.shift(4). Count is capped at 13.
    Returns a pd.Series of integer counts at each bar.
    """
    condition = (close < close.shift(4)).astype(int).values
    n = len(condition)
    counts = np.zeros(n, dtype=float)
    counts[:] = np.nan
    running = 0
    for i in range(4, n):
        if np.isnan(close.iloc[i]) or np.isnan(close.iloc[i - 4]):
            running = 0
            counts[i] = np.nan
        elif condition[i] == 1:
            running = min(running + 1, 13)
            counts[i] = float(running)
        else:
            running = 0
            counts[i] = 0.0
    return pd.Series(counts, index=close.index)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Candle-body exhaustion (close relative to open) ---

def mex_076_bear_body_ratio_5d_vs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean bear-candle body size (|close-open|) on down days: 5d vs 21d ratio."""
    r = _log_ret(close)
    body = (close - open).abs()
    dn_body = body.where(r < 0, np.nan)
    m5 = dn_body.rolling(_TD_WEEK, min_periods=1).mean()
    m21 = dn_body.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(m5, m21)


def mex_077_bear_body_ratio_21d_vs_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean bear-candle body size: 21d vs 63d ratio."""
    r = _log_ret(close)
    body = (close - open).abs()
    dn_body = body.where(r < 0, np.nan)
    m21 = dn_body.rolling(_TD_MON, min_periods=1).mean()
    m63 = dn_body.rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(m21, m63)


def mex_078_bear_body_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of bear-candle body size (down days) over 21 days."""
    r = _log_ret(close)
    body = (close - open).abs()
    dn_body = body.where(r < 0, 0.0)
    return _linslope(dn_body, _TD_MON)


def mex_079_bear_pct_body_ratio_5d_vs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean pct bear body (|close-open|/open) on down days: 5d vs 21d."""
    r = _log_ret(close)
    pct_body = _safe_div((close - open).abs(), open.replace(0, np.nan))
    dn_pct = pct_body.where(r < 0, np.nan)
    m5 = dn_pct.rolling(_TD_WEEK, min_periods=1).mean()
    m21 = dn_pct.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(m5, m21)


def mex_080_gap_down_magnitude_decay_5d_vs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean gap-down (open-to-prior-close) magnitude: 5d avg vs 21d avg."""
    gap = _safe_div(open - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_dn = gap.where(gap < 0, np.nan).abs()
    m5 = gap_dn.rolling(_TD_WEEK, min_periods=1).mean()
    m21 = gap_dn.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(m5, m21)


def mex_081_gap_down_magnitude_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of daily gap-down magnitude over 21 days."""
    gap = _safe_div(open - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_dn = gap.where(gap < 0, 0.0).abs()
    return _linslope(gap_dn, _TD_MON)


def mex_082_open_to_low_pct_decay_5d_vs_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """Mean intraday drop from open to low: 5d avg vs 21d avg ratio."""
    o2l = _safe_div((open - low).clip(lower=0.0), open.replace(0, np.nan))
    m5 = _rolling_mean(o2l, _TD_WEEK)
    m21 = _rolling_mean(o2l, _TD_MON)
    return _safe_div(m5, m21)


def mex_083_open_to_low_slope_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of intraday open-to-low percentage drop over 21 days."""
    o2l = _safe_div((open - low).clip(lower=0.0), open.replace(0, np.nan))
    return _linslope(o2l, _TD_MON)


def mex_084_bear_close_pct_decay_5d_vs_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days closing in bottom half of day's range: 5d vs 21d."""
    rng = (open - close).where(open > close, np.nan)
    frac = _safe_div(rng, (open - close).abs().replace(0, np.nan))
    f5 = frac.rolling(_TD_WEEK, min_periods=1).mean()
    f21 = frac.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(f5, f21)


def mex_085_close_vs_open_momentum_ema_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """EMA-5 of (close-open) divided by EMA-21 of (close-open)."""
    body = close - open
    e5 = _ewm_mean(body, _TD_WEEK)
    e21 = _ewm_mean(body, _TD_MON)
    return _safe_div(e5, e21)


# --- Group I (086-095): Rolling-window return percentile exhaustion ---

def mex_086_ret_pct_rank_5d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day return in trailing 252-day distribution of 5d returns."""
    r5 = close.pct_change(_TD_WEEK)
    return r5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_087_ret_pct_rank_21d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day return in trailing 252-day distribution."""
    r21 = close.pct_change(_TD_MON)
    return r21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_088_down_ret_pct_rank_5d_trend(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day pct-rank series over 63 days (rank improving = exhaustion)."""
    r5 = close.pct_change(_TD_WEEK)
    rank = r5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_QTR)


def mex_089_loss_percentile_5d_vs_63d(close: pd.Series) -> pd.Series:
    """5-day return percentile rank in 63-day window vs in 252-day window ratio."""
    r5 = close.pct_change(_TD_WEEK)
    rank63 = r5.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)
    rank252 = r5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _safe_div(rank63, rank252)


def mex_090_neg_ret_median_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Median of down-day returns: 5-day rolling vs 21-day rolling ratio."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    med5 = _rolling_median(abs_dn, _TD_WEEK)
    med21 = _rolling_median(abs_dn, _TD_MON)
    return _safe_div(med5, med21)


def mex_091_neg_ret_median_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Median of down-day returns: 21d vs 63d ratio."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    med21 = _rolling_median(abs_dn, _TD_MON)
    med63 = _rolling_median(abs_dn, _TD_QTR)
    return _safe_div(med21, med63)


def mex_092_neg_ret_median_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5d-rolling median down-return over 21 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    med5 = _rolling_median(abs_dn, _TD_WEEK)
    return _linslope(med5, _TD_MON)


def mex_093_worst_day_decay_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Max single-day loss in last 5d vs last 21d (peak-loss fading)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0).abs()
    mx5 = _rolling_max(dn, _TD_WEEK)
    mx21 = _rolling_max(dn, _TD_MON)
    return _safe_div(mx5, mx21)


def mex_094_worst_day_decay_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling 5-day max daily loss over 63 days."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0).abs()
    mx5 = _rolling_max(dn, _TD_WEEK)
    return _linslope(mx5, _TD_QTR)


def mex_095_ret_distribution_skew_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of log-returns (less negative = exhaustion of down skew)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).skew()


# --- Group J (096-105): Normalized momentum against recent maxima ---

def mex_096_price_distance_from_5d_low_slope(close: pd.Series) -> pd.Series:
    """OLS slope of (close - 5d low) / close over 21 days (rising = less downside pressure)."""
    low5 = _rolling_min(close, _TD_WEEK)
    dist = _safe_div(close - low5, close.replace(0, np.nan))
    return _linslope(dist, _TD_MON)


def mex_097_price_distance_from_21d_low_ratio(close: pd.Series) -> pd.Series:
    """(close - 21d low) / 21d low; rising = bounce from bottom."""
    low21 = _rolling_min(close, _TD_MON)
    return _safe_div(close - low21, low21.replace(0, np.nan))


def mex_098_price_distance_from_21d_low_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of (close - 21d low) / 21d low over trailing 63 days."""
    low21 = _rolling_min(close, _TD_MON)
    dist = _safe_div(close - low21, low21.replace(0, np.nan))
    return _linslope(dist, _TD_QTR)


def mex_099_close_above_recent_low_pct_5d(close: pd.Series) -> pd.Series:
    """Fraction of last 5 days where close > 5-day rolling minimum."""
    low5 = _rolling_min(close.shift(1), _TD_WEEK)
    above = (close > low5).astype(float)
    return _rolling_mean(above, _TD_WEEK)


def mex_100_close_above_recent_low_pct_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close > 21-day rolling minimum."""
    low21 = _rolling_min(close.shift(1), _TD_MON)
    above = (close > low21).astype(float)
    return _rolling_mean(above, _TD_MON)


def mex_101_drawdown_decel_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day drawdown from rolling max to 21-day drawdown."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = (close - max252) / max252.replace(0, np.nan)
    dd5 = _rolling_min(dd, _TD_WEEK)
    dd21 = _rolling_min(dd, _TD_MON)
    return _safe_div(dd5, dd21)


def mex_102_drawdown_speed_5d(close: pd.Series) -> pd.Series:
    """5-day change in running drawdown (from 252d max) divided by 5."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = (close - max252) / max252.replace(0, np.nan)
    return dd.diff(_TD_WEEK) / _TD_WEEK


def mex_103_drawdown_speed_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day drawdown speed over 21 days."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = (close - max252) / max252.replace(0, np.nan)
    spd = dd.diff(_TD_WEEK) / _TD_WEEK
    return _linslope(spd, _TD_MON)


def mex_104_drawdown_speed_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """5-day drawdown speed vs 63-day drawdown speed ratio."""
    max252 = _rolling_max(close, _TD_YEAR)
    dd = (close - max252) / max252.replace(0, np.nan)
    spd5 = dd.diff(_TD_WEEK) / _TD_WEEK
    spd63 = dd.diff(_TD_QTR) / _TD_QTR
    return _safe_div(spd5, spd63)


def mex_105_rolling_low_increment_shrink_21d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling-21d-min over 21 days (flattening = new lows stopping)."""
    low21 = _rolling_min(close, _TD_MON)
    return _linslope(low21, _TD_MON)


# --- Group K (106-115): Trend-relative momentum decay + MACD ---

def mex_106_close_vs_sma21_momentum_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of (close/sma21 - 1): EMA-5 vs EMA-21 (recent vs avg deviation)."""
    sma21 = _rolling_mean(close, _TD_MON)
    dev = _safe_div(close - sma21, sma21.replace(0, np.nan))
    e5 = _ewm_mean(dev, _TD_WEEK)
    e21 = _ewm_mean(dev, _TD_MON)
    return _safe_div(e5, e21)


def mex_107_close_vs_sma63_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of (close/sma63 - 1) over 21 days (improving = decel of downtrend)."""
    sma63 = _rolling_mean(close, _TD_QTR)
    dev = _safe_div(close - sma63, sma63.replace(0, np.nan))
    return _linslope(dev, _TD_MON)


def mex_108_close_vs_ema21_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of (close/ema21 - 1) over 63 days."""
    ema21 = _ewm_mean(close, _TD_MON)
    dev = _safe_div(close - ema21, ema21.replace(0, np.nan))
    return _linslope(dev, _TD_QTR)


def mex_109_sma21_slope_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day SMA-21 slope to 21-day SMA-21 slope."""
    sma21 = _rolling_mean(close, _TD_MON)
    slp5 = sma21.diff(_TD_WEEK) / _TD_WEEK
    slp21 = sma21.diff(_TD_MON) / _TD_MON
    return _safe_div(slp5, slp21)


def mex_110_sma63_slope_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day SMA-63 slope to 21-day SMA-63 slope."""
    sma63 = _rolling_mean(close, _TD_QTR)
    slp5 = sma63.diff(_TD_WEEK) / _TD_WEEK
    slp21 = sma63.diff(_TD_MON) / _TD_MON
    return _safe_div(slp5, slp21)


def mex_111_ema21_slope_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day change in EMA-21 slope (2nd derivative of trend — decel signal)."""
    ema21 = _ewm_mean(close, _TD_MON)
    slope = ema21.diff(1)
    return slope.diff(_TD_WEEK)


def mex_112_price_to_ema63_ratio_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of (close/ema63) over 21 days."""
    ema63 = _ewm_mean(close, _TD_QTR)
    ratio = _safe_div(close, ema63.replace(0, np.nan))
    return _linslope(ratio, _TD_MON)


def mex_113_macd_signal_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of MACD (ema12-ema26) over 21 days (MACD flattening = decel)."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd = ema12 - ema26
    return _linslope(macd, _TD_MON)


def mex_114_macd_histogram_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of MACD histogram (MACD - signal) over 21 days."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd = ema12 - ema26
    signal = _ewm_mean(macd, 9)
    hist = macd - signal
    return _linslope(hist, _TD_MON)


def mex_115_macd_ratio_recent_vs_older(close: pd.Series) -> pd.Series:
    """MACD value: EMA-5 divided by EMA-21 (recent vs average MACD level)."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd = ema12 - ema26
    e5 = _ewm_mean(macd, _TD_WEEK)
    e21 = _ewm_mean(macd, _TD_MON)
    return _safe_div(e5, e21)


# --- Group L (116-125): Down-move duration relative to magnitude ---

def mex_116_loss_per_down_day_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Avg loss per down day: 5d vs 21d ratio (loss per unit time shrinking)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    is_dn = (r < 0).astype(float)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    cnt5 = _rolling_sum(is_dn, _TD_WEEK).replace(0, np.nan)
    sum21 = _rolling_sum(dn, _TD_MON)
    cnt21 = _rolling_sum(is_dn, _TD_MON).replace(0, np.nan)
    avg5 = _safe_div(sum5, cnt5)
    avg21 = _safe_div(sum21, cnt21)
    return _safe_div(avg5, avg21)


def mex_117_loss_per_down_day_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of daily down-return (on down days, zero elsewhere) over 21 days."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    return _linslope(dn, _TD_MON)


def mex_118_avg_down_run_loss_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Recent 5-day total down-return vs 21-day: ratio measuring loss concentration."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK).abs()
    sum21 = _rolling_sum(dn, _TD_MON).abs()
    return _safe_div(sum5 / _TD_WEEK, sum21 / _TD_MON)


def mex_119_down_day_loss_per_hour_proxy_21d(close: pd.Series) -> pd.Series:
    """21-day total down-return divided by 21-day count of down days (loss density)."""
    r = _log_ret(close)
    dn_sum = _rolling_sum(r.where(r < 0, 0.0), _TD_MON)
    dn_cnt = _rolling_sum((r < 0).astype(float), _TD_MON).replace(0, np.nan)
    return _safe_div(dn_sum, dn_cnt)


def mex_120_down_day_loss_density_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day loss density (avg loss per down day) over 63 days."""
    r = _log_ret(close)
    dn_sum = _rolling_sum(r.where(r < 0, 0.0), _TD_MON)
    dn_cnt = _rolling_sum((r < 0).astype(float), _TD_MON).replace(0, np.nan)
    density = _safe_div(dn_sum, dn_cnt)
    return _linslope(density, _TD_QTR)


def mex_121_down_day_loss_per_elapsed_day_5d(close: pd.Series) -> pd.Series:
    """5-day cumulative down-return divided by 5 (avg daily loss contribution)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    return _rolling_sum(dn, _TD_WEEK) / _TD_WEEK


def mex_122_down_day_loss_per_elapsed_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """5-day avg loss contribution vs 63-day avg loss contribution ratio."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    avg5 = _rolling_sum(dn, _TD_WEEK) / _TD_WEEK
    avg63 = _rolling_sum(dn, _TD_QTR) / _TD_QTR
    return _safe_div(avg5, avg63)


def mex_123_cumulative_loss_per_day_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of (5-day avg daily down-ret) over 21 days."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    avg5 = _rolling_sum(dn, _TD_WEEK) / _TD_WEEK
    return _linslope(avg5, _TD_MON)


def mex_124_down_pct_per_day_21d_pct_rank(close: pd.Series) -> pd.Series:
    """Percentile rank of avg daily loss in 252-day distribution."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    avg21 = _rolling_sum(dn, _TD_MON) / _TD_MON
    return avg21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_125_total_loss_vs_total_gain_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of (5d loss total / 5d gain total) to (21d loss total / 21d gain total)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0).abs()
    up = r.where(r > 0, 0.0)
    loss5 = _rolling_sum(dn, _TD_WEEK)
    gain5 = _rolling_sum(up, _TD_WEEK).replace(0, np.nan)
    loss21 = _rolling_sum(dn, _TD_MON)
    gain21 = _rolling_sum(up, _TD_MON).replace(0, np.nan)
    ratio5 = _safe_div(loss5, gain5)
    ratio21 = _safe_div(loss21, gain21)
    return _safe_div(ratio5, ratio21)


# --- Group M (126-135): Intraday exhaustion (high/low relative to open/close) ---

def mex_126_lower_wick_pct_decay_5d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean lower wick pct of daily range: 5d vs 21d ratio (fading selling tail)."""
    rng = (high - low).replace(0, np.nan)
    lower_wick = (close - low).clip(lower=0.0)
    lw_pct = _safe_div(lower_wick, rng)
    m5 = _rolling_mean(lw_pct, _TD_WEEK)
    m21 = _rolling_mean(lw_pct, _TD_MON)
    return _safe_div(m5, m21)


def mex_127_lower_wick_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of lower wick size over 21 days."""
    lower_wick = (close - low).clip(lower=0.0)
    return _linslope(lower_wick, _TD_MON)


def mex_128_close_position_in_range_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of (close-low)/(high-low) over 21 days (rising = less bearish close)."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _linslope(pos, _TD_MON)


def mex_129_close_position_in_range_ratio_5d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean close-position-in-range: 5d vs 21d ratio."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    m5 = _rolling_mean(pos, _TD_WEEK)
    m21 = _rolling_mean(pos, _TD_MON)
    return _safe_div(m5, m21)


def mex_130_intraday_reversal_rate_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of days where close > open despite low < prior low (intraday reversal)."""
    reversal = ((close > open) & (low < low.shift(1))).astype(float)
    return _rolling_mean(reversal, _TD_MON)


def mex_131_intraday_reversal_rate_slope_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of intraday reversal rate over 63 days (rising = exhaustion signal)."""
    reversal = ((close > open) & (low < low.shift(1))).astype(float)
    rate = _rolling_mean(reversal, _TD_MON)
    return _linslope(rate, _TD_QTR)


def mex_132_upper_vs_lower_wick_ratio_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of (upper_wick / lower_wick) ratio over 21 days."""
    upper_wick = (high - close.where(close > open, open)).clip(lower=0.0)
    lower_wick = (close.where(close < open, open) - low).clip(lower=0.0)
    ratio = _safe_div(upper_wick, lower_wick.replace(0, np.nan))
    return _linslope(ratio, _TD_MON)


def mex_133_high_expansion_ratio_5d_vs_21d(high: pd.Series) -> pd.Series:
    """Mean daily high-rise (high - prior high) when positive: 5d vs 21d ratio."""
    hi_rise = (high - high.shift(1)).clip(lower=0.0)
    m5 = _rolling_mean(hi_rise, _TD_WEEK)
    m21 = _rolling_mean(hi_rise, _TD_MON)
    return _safe_div(m5, m21)


def mex_134_low_drop_ratio_5d_vs_21d(low: pd.Series) -> pd.Series:
    """Mean daily low-drop (prior low - low) when positive: 5d vs 21d ratio."""
    lo_drop = (low.shift(1) - low).clip(lower=0.0)
    m5 = _rolling_mean(lo_drop, _TD_WEEK)
    m21 = _rolling_mean(lo_drop, _TD_MON)
    return _safe_div(m5, m21)


def mex_135_low_drop_slope_21d(low: pd.Series) -> pd.Series:
    """OLS slope of daily low-drop magnitude over 21 days (shrinking = exhaustion)."""
    lo_drop = (low.shift(1) - low).clip(lower=0.0)
    return _linslope(lo_drop, _TD_MON)


# --- Group N (136-150): Kaufman ER extended + TD/DeMark sequential exhaustion ---

def mex_136_kaufman_er_63d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 63-day: low ER over quarter = choppy/stalling market."""
    return _kaufman_er(close, _TD_QTR)


def mex_137_kaufman_er_10d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of Kaufman ER (10d) over 21 days: declining ER = momentum fading."""
    er10 = _kaufman_er(close, 10)
    return _linslope(er10, _TD_MON)


def mex_138_kaufman_er_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of Kaufman ER (21d) over 63 days."""
    er21 = _kaufman_er(close, _TD_MON)
    return _linslope(er21, _TD_QTR)


def mex_139_kaufman_er_10d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of Kaufman ER (10d) within its 63-day distribution."""
    er10 = _kaufman_er(close, 10)
    m = _rolling_mean(er10, _TD_QTR)
    s = _rolling_std(er10, _TD_QTR)
    return _safe_div(er10 - m, s)


def mex_140_kaufman_er_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Kaufman ER (21d) in trailing 252-day distribution."""
    er21 = _kaufman_er(close, _TD_MON)
    return er21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_141_td_buy_setup_count(close: pd.Series) -> pd.Series:
    """TD/DeMark buy-setup running count: consecutive bars with close < close.shift(4), capped at 13."""
    return _td_buy_setup_count(close)


def mex_142_td_setup_9_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): current TD buy-setup count equals 9 (classic setup completion signal)."""
    counts = _td_buy_setup_count(close)
    return (counts == 9.0).astype(float)


def mex_143_td_setup_13_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): current TD buy-setup count equals 13 (extended exhaustion)."""
    counts = _td_buy_setup_count(close)
    return (counts == 13.0).astype(float)


def mex_144_td_setup_completed_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): TD setup >= 9 (setup complete at either 9 or 13 threshold)."""
    counts = _td_buy_setup_count(close)
    return (counts >= 9.0).astype(float)


def mex_145_td_bars_since_setup_9(close: pd.Series) -> pd.Series:
    """Bars elapsed since last TD count of 9 was hit; NaN if never. Capped at 63."""
    counts = _td_buy_setup_count(close)
    n = len(counts)
    result = np.full(n, np.nan)
    last_hit = -1
    for i in range(n):
        if counts.iloc[i] == 9.0:
            last_hit = i
            result[i] = 0.0
        elif last_hit >= 0:
            result[i] = float(min(i - last_hit, 63))
    return pd.Series(result, index=close.index)


def mex_146_td_setup_count_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of TD buy-setup count over trailing 21 days."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    return _linslope(counts, _TD_MON)


def mex_147_td_setup_count_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of TD buy-setup count within trailing 63-day distribution."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    m = _rolling_mean(counts, _TD_QTR)
    s = _rolling_std(counts, _TD_QTR)
    return _safe_div(counts - m, s)


def mex_148_td_setup_count_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of TD buy-setup count in trailing 252-day distribution."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    return counts.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_149_td_buy_condition_rate_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 bars with close < close.shift(4) (raw TD buy condition rate)."""
    cond = (close < close.shift(4)).astype(float)
    return _rolling_mean(cond, _TD_MON)


def mex_150_td_buy_condition_rate_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling 21-day TD-buy-condition rate over 63 days."""
    cond = (close < close.shift(4)).astype(float)
    rate21 = _rolling_mean(cond, _TD_MON)
    return _linslope(rate21, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_REGISTRY_076_150 = {
    "mex_076_bear_body_ratio_5d_vs_21d": {"inputs": ["close", "open"], "func": mex_076_bear_body_ratio_5d_vs_21d},
    "mex_077_bear_body_ratio_21d_vs_63d": {"inputs": ["close", "open"], "func": mex_077_bear_body_ratio_21d_vs_63d},
    "mex_078_bear_body_slope_21d": {"inputs": ["close", "open"], "func": mex_078_bear_body_slope_21d},
    "mex_079_bear_pct_body_ratio_5d_vs_21d": {"inputs": ["close", "open"], "func": mex_079_bear_pct_body_ratio_5d_vs_21d},
    "mex_080_gap_down_magnitude_decay_5d_vs_21d": {"inputs": ["close", "open"], "func": mex_080_gap_down_magnitude_decay_5d_vs_21d},
    "mex_081_gap_down_magnitude_slope_21d": {"inputs": ["close", "open"], "func": mex_081_gap_down_magnitude_slope_21d},
    "mex_082_open_to_low_pct_decay_5d_vs_21d": {"inputs": ["open", "low"], "func": mex_082_open_to_low_pct_decay_5d_vs_21d},
    "mex_083_open_to_low_slope_21d": {"inputs": ["open", "low"], "func": mex_083_open_to_low_slope_21d},
    "mex_084_bear_close_pct_decay_5d_vs_21d": {"inputs": ["close", "open"], "func": mex_084_bear_close_pct_decay_5d_vs_21d},
    "mex_085_close_vs_open_momentum_ema_ratio": {"inputs": ["close", "open"], "func": mex_085_close_vs_open_momentum_ema_ratio},
    "mex_086_ret_pct_rank_5d_in_252d": {"inputs": ["close"], "func": mex_086_ret_pct_rank_5d_in_252d},
    "mex_087_ret_pct_rank_21d_in_252d": {"inputs": ["close"], "func": mex_087_ret_pct_rank_21d_in_252d},
    "mex_088_down_ret_pct_rank_5d_trend": {"inputs": ["close"], "func": mex_088_down_ret_pct_rank_5d_trend},
    "mex_089_loss_percentile_5d_vs_63d": {"inputs": ["close"], "func": mex_089_loss_percentile_5d_vs_63d},
    "mex_090_neg_ret_median_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_090_neg_ret_median_ratio_5d_vs_21d},
    "mex_091_neg_ret_median_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_091_neg_ret_median_ratio_21d_vs_63d},
    "mex_092_neg_ret_median_slope_21d": {"inputs": ["close"], "func": mex_092_neg_ret_median_slope_21d},
    "mex_093_worst_day_decay_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_093_worst_day_decay_ratio_5d_vs_21d},
    "mex_094_worst_day_decay_slope_63d": {"inputs": ["close"], "func": mex_094_worst_day_decay_slope_63d},
    "mex_095_ret_distribution_skew_21d": {"inputs": ["close"], "func": mex_095_ret_distribution_skew_21d},
    "mex_096_price_distance_from_5d_low_slope": {"inputs": ["close"], "func": mex_096_price_distance_from_5d_low_slope},
    "mex_097_price_distance_from_21d_low_ratio": {"inputs": ["close"], "func": mex_097_price_distance_from_21d_low_ratio},
    "mex_098_price_distance_from_21d_low_slope_63d": {"inputs": ["close"], "func": mex_098_price_distance_from_21d_low_slope_63d},
    "mex_099_close_above_recent_low_pct_5d": {"inputs": ["close"], "func": mex_099_close_above_recent_low_pct_5d},
    "mex_100_close_above_recent_low_pct_21d": {"inputs": ["close"], "func": mex_100_close_above_recent_low_pct_21d},
    "mex_101_drawdown_decel_5d_vs_21d": {"inputs": ["close"], "func": mex_101_drawdown_decel_5d_vs_21d},
    "mex_102_drawdown_speed_5d": {"inputs": ["close"], "func": mex_102_drawdown_speed_5d},
    "mex_103_drawdown_speed_slope_21d": {"inputs": ["close"], "func": mex_103_drawdown_speed_slope_21d},
    "mex_104_drawdown_speed_ratio_5d_vs_63d": {"inputs": ["close"], "func": mex_104_drawdown_speed_ratio_5d_vs_63d},
    "mex_105_rolling_low_increment_shrink_21d": {"inputs": ["close"], "func": mex_105_rolling_low_increment_shrink_21d},
    "mex_106_close_vs_sma21_momentum_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_106_close_vs_sma21_momentum_ratio_5d_vs_21d},
    "mex_107_close_vs_sma63_slope_21d": {"inputs": ["close"], "func": mex_107_close_vs_sma63_slope_21d},
    "mex_108_close_vs_ema21_slope_63d": {"inputs": ["close"], "func": mex_108_close_vs_ema21_slope_63d},
    "mex_109_sma21_slope_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_109_sma21_slope_ratio_5d_vs_21d},
    "mex_110_sma63_slope_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_110_sma63_slope_ratio_5d_vs_21d},
    "mex_111_ema21_slope_acceleration_5d": {"inputs": ["close"], "func": mex_111_ema21_slope_acceleration_5d},
    "mex_112_price_to_ema63_ratio_slope_21d": {"inputs": ["close"], "func": mex_112_price_to_ema63_ratio_slope_21d},
    "mex_113_macd_signal_slope_21d": {"inputs": ["close"], "func": mex_113_macd_signal_slope_21d},
    "mex_114_macd_histogram_slope_21d": {"inputs": ["close"], "func": mex_114_macd_histogram_slope_21d},
    "mex_115_macd_ratio_recent_vs_older": {"inputs": ["close"], "func": mex_115_macd_ratio_recent_vs_older},
    "mex_116_loss_per_down_day_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_116_loss_per_down_day_ratio_5d_vs_21d},
    "mex_117_loss_per_down_day_slope_21d": {"inputs": ["close"], "func": mex_117_loss_per_down_day_slope_21d},
    "mex_118_avg_down_run_loss_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_118_avg_down_run_loss_ratio_5d_vs_21d},
    "mex_119_down_day_loss_per_hour_proxy_21d": {"inputs": ["close"], "func": mex_119_down_day_loss_per_hour_proxy_21d},
    "mex_120_down_day_loss_density_slope_63d": {"inputs": ["close"], "func": mex_120_down_day_loss_density_slope_63d},
    "mex_121_down_day_loss_per_elapsed_day_5d": {"inputs": ["close"], "func": mex_121_down_day_loss_per_elapsed_day_5d},
    "mex_122_down_day_loss_per_elapsed_ratio_5d_vs_63d": {"inputs": ["close"], "func": mex_122_down_day_loss_per_elapsed_ratio_5d_vs_63d},
    "mex_123_cumulative_loss_per_day_slope_21d": {"inputs": ["close"], "func": mex_123_cumulative_loss_per_day_slope_21d},
    "mex_124_down_pct_per_day_21d_pct_rank": {"inputs": ["close"], "func": mex_124_down_pct_per_day_21d_pct_rank},
    "mex_125_total_loss_vs_total_gain_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_125_total_loss_vs_total_gain_ratio_5d_vs_21d},
    "mex_126_lower_wick_pct_decay_5d_vs_21d": {"inputs": ["close", "high", "low"], "func": mex_126_lower_wick_pct_decay_5d_vs_21d},
    "mex_127_lower_wick_slope_21d": {"inputs": ["close", "high", "low"], "func": mex_127_lower_wick_slope_21d},
    "mex_128_close_position_in_range_slope_21d": {"inputs": ["close", "high", "low"], "func": mex_128_close_position_in_range_slope_21d},
    "mex_129_close_position_in_range_ratio_5d_vs_21d": {"inputs": ["close", "high", "low"], "func": mex_129_close_position_in_range_ratio_5d_vs_21d},
    "mex_130_intraday_reversal_rate_21d": {"inputs": ["close", "open", "low"], "func": mex_130_intraday_reversal_rate_21d},
    "mex_131_intraday_reversal_rate_slope_63d": {"inputs": ["close", "open", "low"], "func": mex_131_intraday_reversal_rate_slope_63d},
    "mex_132_upper_vs_lower_wick_ratio_slope_21d": {"inputs": ["close", "high", "low", "open"], "func": mex_132_upper_vs_lower_wick_ratio_slope_21d},
    "mex_133_high_expansion_ratio_5d_vs_21d": {"inputs": ["high"], "func": mex_133_high_expansion_ratio_5d_vs_21d},
    "mex_134_low_drop_ratio_5d_vs_21d": {"inputs": ["low"], "func": mex_134_low_drop_ratio_5d_vs_21d},
    "mex_135_low_drop_slope_21d": {"inputs": ["low"], "func": mex_135_low_drop_slope_21d},
    "mex_136_kaufman_er_63d": {"inputs": ["close"], "func": mex_136_kaufman_er_63d},
    "mex_137_kaufman_er_10d_slope_21d": {"inputs": ["close"], "func": mex_137_kaufman_er_10d_slope_21d},
    "mex_138_kaufman_er_21d_slope_63d": {"inputs": ["close"], "func": mex_138_kaufman_er_21d_slope_63d},
    "mex_139_kaufman_er_10d_zscore_63d": {"inputs": ["close"], "func": mex_139_kaufman_er_10d_zscore_63d},
    "mex_140_kaufman_er_21d_pct_rank_252d": {"inputs": ["close"], "func": mex_140_kaufman_er_21d_pct_rank_252d},
    "mex_141_td_buy_setup_count": {"inputs": ["close"], "func": mex_141_td_buy_setup_count},
    "mex_142_td_setup_9_flag": {"inputs": ["close"], "func": mex_142_td_setup_9_flag},
    "mex_143_td_setup_13_flag": {"inputs": ["close"], "func": mex_143_td_setup_13_flag},
    "mex_144_td_setup_completed_flag": {"inputs": ["close"], "func": mex_144_td_setup_completed_flag},
    "mex_145_td_bars_since_setup_9": {"inputs": ["close"], "func": mex_145_td_bars_since_setup_9},
    "mex_146_td_setup_count_slope_21d": {"inputs": ["close"], "func": mex_146_td_setup_count_slope_21d},
    "mex_147_td_setup_count_zscore_63d": {"inputs": ["close"], "func": mex_147_td_setup_count_zscore_63d},
    "mex_148_td_setup_count_pct_rank_252d": {"inputs": ["close"], "func": mex_148_td_setup_count_pct_rank_252d},
    "mex_149_td_buy_condition_rate_21d": {"inputs": ["close"], "func": mex_149_td_buy_condition_rate_21d},
    "mex_150_td_buy_condition_rate_slope_63d": {"inputs": ["close"], "func": mex_150_td_buy_condition_rate_slope_63d},
}
