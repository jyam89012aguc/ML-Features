"""
01_drawdown_depth — Base Features 076-150
Domain: decline magnitude vs trailing highs (1/3/5y, ATH)
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Drawdown with volume interaction ---

def dd_076_dd_252d_on_high_volume_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean 252-day drawdown on days where volume exceeds 252-day avg vol."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    high_vol_dd = dd.where(volume > avg_vol, other=np.nan)
    return _rolling_mean(high_vol_dd, _TD_YEAR)


def dd_077_volume_surge_at_new_lows(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on days that set new 252-day closing lows (panic selling proxy)."""
    new_low = (close <= _rolling_min(close.shift(1), _TD_YEAR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_ratio = _safe_div(volume, avg_vol)
    surging = vol_ratio.where(new_low == 1, other=np.nan)
    return _rolling_mean(surging, _TD_YEAR)


def dd_078_avg_vol_at_bottom_decile(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume ratio on days in bottom 10% of 252-day price range."""
    l = _rolling_min(close, _TD_YEAR)
    h = _rolling_max(close, _TD_YEAR)
    pct_pos = _safe_div(close - l, h - l)
    in_decile = (pct_pos <= 0.10).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_ratio = _safe_div(volume, avg_vol)
    decile_vol = vol_ratio.where(in_decile == 1, other=np.nan)
    return _rolling_mean(decile_vol, _TD_YEAR)


def dd_079_dd_momentum_5d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day return to 252-day return (short-term vs long-term momentum divergence)."""
    r5 = _safe_div(close - close.shift(_TD_WEEK), close.shift(_TD_WEEK))
    r252 = _safe_div(close - close.shift(_TD_YEAR), close.shift(_TD_YEAR))
    return _safe_div(r5, r252.abs())


def dd_080_dd_momentum_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day return to 252-day return."""
    r21 = _safe_div(close - close.shift(_TD_MON), close.shift(_TD_MON))
    r252 = _safe_div(close - close.shift(_TD_YEAR), close.shift(_TD_YEAR))
    return _safe_div(r21, r252.abs())


def dd_081_dd_vwap_252d_deviation(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from 252-day VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return _safe_div(close - vwap, vwap)


def dd_082_dd_vwap_63d_deviation(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent deviation of close from 63-day VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _safe_div(close - vwap, vwap)


def dd_083_dd_high_low_close_position_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 252-day OHLC range (intraday + high-low range)."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _rolling_min(low, _TD_YEAR)
    return _safe_div(close - l252, h252 - l252)


def dd_084_dd_high_low_close_position_504d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 504-day OHLC range."""
    h504 = _rolling_max(high, 504)
    l504 = _rolling_min(low, 504)
    return _safe_div(close - l504, h504 - l504)


def dd_085_true_range_normalized_dd_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day drawdown expressed in 21-day ATR units."""
    atr21 = _rolling_mean(_tr(close, high, low), _TD_MON)
    h21 = _rolling_max(close, _TD_MON)
    return _safe_div(close - h21, atr21)


# --- Group I (086-095): Prior-period high anchors ---

def dd_086_dd_from_lagged_63d_high(close: pd.Series) -> pd.Series:
    """Drawdown from high of the quarter that ended 63 days ago."""
    prior = close.shift(_TD_QTR)
    h = _rolling_max(prior, _TD_QTR)
    return _safe_div(close - h, h)


def dd_087_dd_from_lagged_252d_high(close: pd.Series) -> pd.Series:
    """Drawdown from the high of the year that ended 252 days ago."""
    prior = close.shift(_TD_YEAR)
    h = _rolling_max(prior, _TD_YEAR)
    return _safe_div(close - h, h)


def dd_088_dd_from_lagged_504d_high(close: pd.Series) -> pd.Series:
    """Drawdown from the high of the 2-year window ending 504 days ago."""
    prior = close.shift(504)
    h = _rolling_max(prior, 504)
    return _safe_div(close - h, h)


def dd_089_dd_from_peak_of_peak_windows(close: pd.Series) -> pd.Series:
    """Drawdown from the higher of: 252d high or 1-year-ago 252d high."""
    h_now = _rolling_max(close, _TD_YEAR)
    h_ago = _rolling_max(close.shift(_TD_YEAR), _TD_YEAR)
    h = pd.concat([h_now, h_ago], axis=1).max(axis=1)
    return _safe_div(close - h, h)


def dd_090_dd_joint_ath_intraday(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close vs all-time intraday high (expanding max of daily high)."""
    ath = high.expanding(min_periods=1).max()
    return _safe_div(close - ath, ath)


def dd_091_high_vs_252d_high(high: pd.Series) -> pd.Series:
    """Today's intraday high vs 252-day rolling max of intraday highs."""
    h252 = _rolling_max(high, _TD_YEAR)
    return _safe_div(high - h252, h252)


def dd_092_low_vs_252d_low(low: pd.Series) -> pd.Series:
    """Today's intraday low vs 252-day rolling min of intraday lows."""
    l252 = _rolling_min(low, _TD_YEAR)
    return _safe_div(low - l252, l252.abs())


def dd_093_open_vs_252d_range_position(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price position within 252-day close high-low range."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(open - l, h - l)


def dd_094_dd_avg_of_21_63_252(close: pd.Series) -> pd.Series:
    """Simple average of 21d, 63d, and 252d drawdowns."""
    dd21 = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    dd63 = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    dd252 = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return (dd21 + dd63 + dd252) / 3.0


def dd_095_dd_max_of_21_63_252(close: pd.Series) -> pd.Series:
    """Most negative (deepest) of 21d, 63d, and 252d drawdowns."""
    dd21 = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    dd63 = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    dd252 = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return pd.concat([dd21, dd63, dd252], axis=1).min(axis=1)


# --- Group J (096-105): Consecutive down-day and streak measures ---

def dd_096_consec_down_days_21d(close: pd.Series) -> pd.Series:
    """Count of negative daily return days in trailing 21-day window."""
    down = (close.diff(1) < 0).astype(float)
    return _rolling_sum(down, _TD_MON)


def dd_097_consec_down_days_63d(close: pd.Series) -> pd.Series:
    """Count of negative daily return days in trailing 63-day window."""
    down = (close.diff(1) < 0).astype(float)
    return _rolling_sum(down, _TD_QTR)


def dd_098_down_day_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with negative daily return."""
    down = (close.diff(1) < 0).astype(float)
    return _rolling_mean(down, _TD_YEAR)


def dd_099_max_consec_down_streak_63d(close: pd.Series) -> pd.Series:
    """Rolling max of consecutive losing-day streaks over 63 days (exhaustion proxy)."""
    down = (close.diff(1) < 0).astype(int)
    # Build streak series
    streak = down.copy().astype(float)
    for lag in range(1, 11):
        still_down = down.copy()
        for k in range(1, lag + 1):
            still_down = still_down & down.shift(k).fillna(0).astype(int)
        streak = streak + still_down.astype(float)
    return _rolling_max(streak, _TD_QTR)


def dd_100_loss_magnitude_sum_21d(close: pd.Series) -> pd.Series:
    """Sum of absolute negative daily returns over trailing 21 days."""
    ret = _daily_ret(close)
    losses = ret.clip(upper=0).abs()
    return _rolling_sum(losses, _TD_MON)


def dd_101_loss_magnitude_sum_63d(close: pd.Series) -> pd.Series:
    """Sum of absolute negative daily returns over trailing 63 days."""
    ret = _daily_ret(close)
    losses = ret.clip(upper=0).abs()
    return _rolling_sum(losses, _TD_QTR)


def dd_102_loss_magnitude_sum_252d(close: pd.Series) -> pd.Series:
    """Sum of absolute negative daily returns over trailing 252 days."""
    ret = _daily_ret(close)
    losses = ret.clip(upper=0).abs()
    return _rolling_sum(losses, _TD_YEAR)


def dd_103_gain_loss_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of average gain to average loss magnitude over 63 days."""
    ret = _daily_ret(close)
    gains = ret.clip(lower=0)
    losses = ret.clip(upper=0).abs()
    avg_gain = _rolling_mean(gains, _TD_QTR)
    avg_loss = _rolling_mean(losses, _TD_QTR)
    return _safe_div(avg_gain, avg_loss)


def dd_104_gain_loss_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of average gain to average loss magnitude over 252 days."""
    ret = _daily_ret(close)
    gains = ret.clip(lower=0)
    losses = ret.clip(upper=0).abs()
    avg_gain = _rolling_mean(gains, _TD_YEAR)
    avg_loss = _rolling_mean(losses, _TD_YEAR)
    return _safe_div(avg_gain, avg_loss)


def dd_105_net_ret_vs_gross_loss_63d(close: pd.Series) -> pd.Series:
    """Net 63-day return divided by gross loss sum (pain per unit of drift)."""
    net_ret = _safe_div(close - close.shift(_TD_QTR), close.shift(_TD_QTR))
    ret = _daily_ret(close)
    gross_loss = _rolling_sum(ret.clip(upper=0).abs(), _TD_QTR)
    return _safe_div(net_ret, gross_loss)


# --- Group K (106-115): Bollinger / band distance measures ---

def dd_106_pct_b_21d(close: pd.Series) -> pd.Series:
    """Percent Bollinger Band position over 21 days (0=lower band, 1=upper)."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    upper = ma + 2 * sd
    lower = ma - 2 * sd
    return _safe_div(close - lower, upper - lower)


def dd_107_pct_b_63d(close: pd.Series) -> pd.Series:
    """Percent Bollinger Band position over 63 days."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    upper = ma + 2 * sd
    lower = ma - 2 * sd
    return _safe_div(close - lower, upper - lower)


def dd_108_pct_b_252d(close: pd.Series) -> pd.Series:
    """Percent Bollinger Band position over 252 days."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    upper = ma + 2 * sd
    lower = ma - 2 * sd
    return _safe_div(close - lower, upper - lower)


def dd_109_below_lower_bb_21d(close: pd.Series) -> pd.Series:
    """1 if close is below lower 2-sigma Bollinger Band (21d), else 0."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = ma - 2 * sd
    return (close < lower).astype(float)


def dd_110_below_lower_bb_63d(close: pd.Series) -> pd.Series:
    """1 if close is below lower 2-sigma Bollinger Band (63d), else 0."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    lower = ma - 2 * sd
    return (close < lower).astype(float)


def dd_111_bb_width_21d(close: pd.Series) -> pd.Series:
    """Bollinger Band width (upper-lower / mid) over 21 days."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    return _safe_div(4 * sd, ma)


def dd_112_bb_width_252d(close: pd.Series) -> pd.Series:
    """Bollinger Band width over 252 days (measures long-run volatility regime)."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    return _safe_div(4 * sd, ma)


def dd_113_close_vs_lower_bb_3sigma_21d(close: pd.Series) -> pd.Series:
    """Distance of close below 3-sigma lower band (21d), positive when below."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = ma - 3 * sd
    return _safe_div(lower - close, ma)


def dd_114_close_vs_lower_bb_3sigma_63d(close: pd.Series) -> pd.Series:
    """Distance of close below 3-sigma lower band (63d), positive when below."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    lower = ma - 3 * sd
    return _safe_div(lower - close, ma)


def dd_115_bb_squeeze_21d(close: pd.Series) -> pd.Series:
    """Ratio of current 21d BB width to 252d median BB width (squeeze detection)."""
    ma21 = _rolling_mean(close, _TD_MON)
    sd21 = _rolling_std(close, _TD_MON)
    bw21 = _safe_div(4 * sd21, ma21)
    return _safe_div(bw21, _rolling_median(bw21, _TD_YEAR))


# --- Group L (116-125): RSI / Wilder overbought-oversold at distress ---

def dd_116_rsi_14d(close: pd.Series) -> pd.Series:
    """Wilder RSI over 14 days (oversold at capitulation)."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    avg_up = up.ewm(alpha=1 / 14, min_periods=7).mean()
    avg_dn = down.ewm(alpha=1 / 14, min_periods=7).mean()
    rs = _safe_div(avg_up, avg_dn)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def dd_117_rsi_28d(close: pd.Series) -> pd.Series:
    """Wilder RSI over 28 days."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    avg_up = up.ewm(alpha=1 / 28, min_periods=14).mean()
    avg_dn = down.ewm(alpha=1 / 28, min_periods=14).mean()
    rs = _safe_div(avg_up, avg_dn)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def dd_118_rsi_63d(close: pd.Series) -> pd.Series:
    """Wilder RSI over 63 days."""
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    avg_up = up.ewm(alpha=1 / 63, min_periods=30).mean()
    avg_dn = down.ewm(alpha=1 / 63, min_periods=30).mean()
    rs = _safe_div(avg_up, avg_dn)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def dd_119_stoch_k_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic %K (21-day) — position of close within recent trading range."""
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    return _safe_div(close - l21, h21 - l21) * 100.0


def dd_120_stoch_k_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stochastic %K (63-day) — position within quarterly trading range."""
    h63 = _rolling_max(high, _TD_QTR)
    l63 = _rolling_min(low, _TD_QTR)
    return _safe_div(close - l63, h63 - l63) * 100.0


# --- Group M (126-135): Geometric-mean and harmonic-mean anchors ---

def dd_121_geom_mean_dd_252d(close: pd.Series) -> pd.Series:
    """Ratio of close to 252-day geometric mean of close prices."""
    log_close = _log_safe(close)
    geom_mean = np.exp(_rolling_mean(log_close, _TD_YEAR))
    return _safe_div(close - geom_mean, geom_mean)


def dd_122_geom_mean_dd_504d(close: pd.Series) -> pd.Series:
    """Ratio of close to 504-day geometric mean of close prices."""
    log_close = _log_safe(close)
    geom_mean = np.exp(_rolling_mean(log_close, 504))
    return _safe_div(close - geom_mean, geom_mean)


def dd_123_harmonic_mean_dd_252d(close: pd.Series) -> pd.Series:
    """Drawdown from 252-day harmonic mean of close prices."""
    hmean = _safe_div(1.0, _rolling_mean(_safe_div(pd.Series(np.ones(len(close)), index=close.index), close), _TD_YEAR))
    return _safe_div(close - hmean, hmean)


def dd_124_quadratic_mean_dd_252d(close: pd.Series) -> pd.Series:
    """Drawdown from 252-day quadratic (RMS) mean of close prices."""
    qmean = np.sqrt(_rolling_mean(close ** 2, _TD_YEAR))
    return _safe_div(close - qmean, qmean)


def dd_125_log_geom_mean_dd_ath(close: pd.Series) -> pd.Series:
    """Log-distance of close from expanding geometric mean of all closes."""
    log_close = _log_safe(close)
    exp_geom = log_close.expanding(min_periods=5).mean()
    return log_close - exp_geom


def dd_126_median_dd_63d(close: pd.Series) -> pd.Series:
    """Drawdown from 63-day median close (robust center)."""
    med = _rolling_median(close, _TD_QTR)
    return _safe_div(close - med, med)


def dd_127_median_dd_252d(close: pd.Series) -> pd.Series:
    """Drawdown from 252-day median close."""
    med = _rolling_median(close, _TD_YEAR)
    return _safe_div(close - med, med)


def dd_128_median_dd_504d(close: pd.Series) -> pd.Series:
    """Drawdown from 504-day median close."""
    med = _rolling_median(close, 504)
    return _safe_div(close - med, med)


def dd_129_close_vs_252d_q25(close: pd.Series) -> pd.Series:
    """Deviation of close from 25th percentile of 252-day price distribution."""
    q25 = close.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return _safe_div(close - q25, q25)


def dd_130_close_vs_252d_q10(close: pd.Series) -> pd.Series:
    """Deviation of close from 10th percentile of 252-day price distribution."""
    q10 = close.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return _safe_div(close - q10, q10)


# --- Group N (131-140): Trend-break and SMA-cascade measures ---

def dd_131_sma_cascade_alignment(close: pd.Series) -> pd.Series:
    """Fraction of {21,63,126,252} SMA levels that close is below (0=none, 1=all)."""
    below = (
        (close < _rolling_mean(close, _TD_MON)).astype(float) +
        (close < _rolling_mean(close, _TD_QTR)).astype(float) +
        (close < _rolling_mean(close, _TD_HALF)).astype(float) +
        (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    )
    return below / 4.0


def dd_132_sma_death_cross_depth_21_63(close: pd.Series) -> pd.Series:
    """Degree of 21-day SMA below 63-day SMA (negative = bearish)."""
    ma21 = _rolling_mean(close, _TD_MON)
    ma63 = _rolling_mean(close, _TD_QTR)
    return _safe_div(ma21 - ma63, ma63)


def dd_133_sma_death_cross_depth_63_126(close: pd.Series) -> pd.Series:
    """Degree of 63-day SMA below 126-day SMA."""
    ma63 = _rolling_mean(close, _TD_QTR)
    ma126 = _rolling_mean(close, _TD_HALF)
    return _safe_div(ma63 - ma126, ma126)


def dd_134_sma_death_cross_depth_126_252(close: pd.Series) -> pd.Series:
    """Degree of 126-day SMA below 252-day SMA."""
    ma126 = _rolling_mean(close, _TD_HALF)
    ma252 = _rolling_mean(close, _TD_YEAR)
    return _safe_div(ma126 - ma252, ma252)


def dd_135_ema_cascade_alignment(close: pd.Series) -> pd.Series:
    """Fraction of {21,63,200} EMA levels that close is below (0=none, 1=all)."""
    below = (
        (close < _ewm_mean(close, _TD_MON)).astype(float) +
        (close < _ewm_mean(close, _TD_QTR)).astype(float) +
        (close < _ewm_mean(close, 200)).astype(float)
    )
    return below / 3.0


def dd_136_dd_from_200d_sma_high(close: pd.Series) -> pd.Series:
    """Drawdown of 200-day SMA from its own 252-day peak (trend-level distress)."""
    ma200 = _rolling_mean(close, 200)
    h = _rolling_max(ma200, _TD_YEAR)
    return _safe_div(ma200 - h, h)


def dd_137_dd_from_63d_sma_peak(close: pd.Series) -> pd.Series:
    """Drawdown of 63-day SMA from its own 252-day peak."""
    ma63 = _rolling_mean(close, _TD_QTR)
    h = _rolling_max(ma63, _TD_YEAR)
    return _safe_div(ma63 - h, h)


def dd_138_ema200_from_ath(close: pd.Series) -> pd.Series:
    """Drawdown of 200-day EMA from its own all-time high."""
    ema200 = _ewm_mean(close, 200)
    h = ema200.expanding(min_periods=1).max()
    return _safe_div(ema200 - h, h)


def dd_139_close_vs_ema200_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (close - EMA200) / EMA200 over trailing 252 days."""
    dev = _safe_div(close - _ewm_mean(close, 200), _ewm_mean(close, 200))
    return _zscore_rolling(dev, _TD_YEAR)


def dd_140_price_acceleration_21d(close: pd.Series) -> pd.Series:
    """Second difference of price over 21 days (acceleration of price movement)."""
    r5 = close.diff(5)
    return r5.diff(5)


# --- Group O (141-150): Quantile, entropy, and power-law drawdown metrics ---

def dd_141_dd_q95_vs_mean_252d(close: pd.Series) -> pd.Series:
    """Ratio of 95th pct drawdown to mean drawdown (tail heaviness)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    q95 = dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)  # most negative
    m = _rolling_mean(dd, _TD_YEAR)
    return _safe_div(q95, m)


def dd_142_dd_interquartile_range_252d(close: pd.Series) -> pd.Series:
    """IQR of 252-day drawdown distribution (spread of distress episodes)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    q75 = dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def dd_143_log_return_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of log daily returns over 63 days."""
    log_ret = _log_safe(close).diff(1)
    return log_ret.rolling(_TD_QTR, min_periods=_TD_MON).skew()


def dd_144_log_return_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of log daily returns over 252 days."""
    log_ret = _log_safe(close).diff(1)
    return log_ret.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def dd_145_log_return_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log daily returns over 63 days."""
    log_ret = _log_safe(close).diff(1)
    return log_ret.rolling(_TD_QTR, min_periods=_TD_MON).kurt()


def dd_146_dd_entropy_21d(close: pd.Series) -> pd.Series:
    """Volatility of daily dd changes over 21 days (entropy proxy)."""
    dd = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    return _rolling_std(dd.diff(1), _TD_MON)


def dd_147_dd_entropy_63d(close: pd.Series) -> pd.Series:
    """Volatility of daily dd changes over 63 days."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    return _rolling_std(dd.diff(1), _TD_QTR)


def dd_148_dd_entropy_252d(close: pd.Series) -> pd.Series:
    """Volatility of daily dd changes over 252 days."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _rolling_std(dd.diff(1), _TD_YEAR)


def dd_149_dd_convexity_252d(close: pd.Series) -> pd.Series:
    """Ratio of avg-dd area to max-dd depth (convexity of the drawdown curve)."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    avg_dd = _rolling_mean(dd, _TD_YEAR)
    max_dd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(avg_dd, max_dd)


def dd_150_dd_normalized_by_ath_and_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATH drawdown divided by 252-day ATR (dollar drawdown per unit of range)."""
    ath_dd = _safe_div(close - close.expanding(min_periods=1).max(), close.expanding(min_periods=1).max())
    atr252 = _rolling_mean(_tr(close, high, low), _TD_YEAR)
    price_norm = _safe_div(atr252, close)
    return _safe_div(ath_dd, price_norm)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DEPTH_REGISTRY_076_150 = {
    "dd_076_dd_252d_on_high_volume_days": {"inputs": ["close", "volume"], "func": dd_076_dd_252d_on_high_volume_days},
    "dd_077_volume_surge_at_new_lows": {"inputs": ["close", "volume"], "func": dd_077_volume_surge_at_new_lows},
    "dd_078_avg_vol_at_bottom_decile": {"inputs": ["close", "volume"], "func": dd_078_avg_vol_at_bottom_decile},
    "dd_079_dd_momentum_5d_vs_252d": {"inputs": ["close"], "func": dd_079_dd_momentum_5d_vs_252d},
    "dd_080_dd_momentum_21d_vs_252d": {"inputs": ["close"], "func": dd_080_dd_momentum_21d_vs_252d},
    "dd_081_dd_vwap_252d_deviation": {"inputs": ["close", "volume"], "func": dd_081_dd_vwap_252d_deviation},
    "dd_082_dd_vwap_63d_deviation": {"inputs": ["close", "volume"], "func": dd_082_dd_vwap_63d_deviation},
    "dd_083_dd_high_low_close_position_252d": {"inputs": ["close", "high", "low"], "func": dd_083_dd_high_low_close_position_252d},
    "dd_084_dd_high_low_close_position_504d": {"inputs": ["close", "high", "low"], "func": dd_084_dd_high_low_close_position_504d},
    "dd_085_true_range_normalized_dd_21d": {"inputs": ["close", "high", "low"], "func": dd_085_true_range_normalized_dd_21d},
    "dd_086_dd_from_lagged_63d_high": {"inputs": ["close"], "func": dd_086_dd_from_lagged_63d_high},
    "dd_087_dd_from_lagged_252d_high": {"inputs": ["close"], "func": dd_087_dd_from_lagged_252d_high},
    "dd_088_dd_from_lagged_504d_high": {"inputs": ["close"], "func": dd_088_dd_from_lagged_504d_high},
    "dd_089_dd_from_peak_of_peak_windows": {"inputs": ["close"], "func": dd_089_dd_from_peak_of_peak_windows},
    "dd_090_dd_joint_ath_intraday": {"inputs": ["close", "high"], "func": dd_090_dd_joint_ath_intraday},
    "dd_091_high_vs_252d_high": {"inputs": ["high"], "func": dd_091_high_vs_252d_high},
    "dd_092_low_vs_252d_low": {"inputs": ["low"], "func": dd_092_low_vs_252d_low},
    "dd_093_open_vs_252d_range_position": {"inputs": ["close", "open"], "func": dd_093_open_vs_252d_range_position},
    "dd_094_dd_avg_of_21_63_252": {"inputs": ["close"], "func": dd_094_dd_avg_of_21_63_252},
    "dd_095_dd_max_of_21_63_252": {"inputs": ["close"], "func": dd_095_dd_max_of_21_63_252},
    "dd_096_consec_down_days_21d": {"inputs": ["close"], "func": dd_096_consec_down_days_21d},
    "dd_097_consec_down_days_63d": {"inputs": ["close"], "func": dd_097_consec_down_days_63d},
    "dd_098_down_day_fraction_252d": {"inputs": ["close"], "func": dd_098_down_day_fraction_252d},
    "dd_099_max_consec_down_streak_63d": {"inputs": ["close"], "func": dd_099_max_consec_down_streak_63d},
    "dd_100_loss_magnitude_sum_21d": {"inputs": ["close"], "func": dd_100_loss_magnitude_sum_21d},
    "dd_101_loss_magnitude_sum_63d": {"inputs": ["close"], "func": dd_101_loss_magnitude_sum_63d},
    "dd_102_loss_magnitude_sum_252d": {"inputs": ["close"], "func": dd_102_loss_magnitude_sum_252d},
    "dd_103_gain_loss_ratio_63d": {"inputs": ["close"], "func": dd_103_gain_loss_ratio_63d},
    "dd_104_gain_loss_ratio_252d": {"inputs": ["close"], "func": dd_104_gain_loss_ratio_252d},
    "dd_105_net_ret_vs_gross_loss_63d": {"inputs": ["close"], "func": dd_105_net_ret_vs_gross_loss_63d},
    "dd_106_pct_b_21d": {"inputs": ["close"], "func": dd_106_pct_b_21d},
    "dd_107_pct_b_63d": {"inputs": ["close"], "func": dd_107_pct_b_63d},
    "dd_108_pct_b_252d": {"inputs": ["close"], "func": dd_108_pct_b_252d},
    "dd_109_below_lower_bb_21d": {"inputs": ["close"], "func": dd_109_below_lower_bb_21d},
    "dd_110_below_lower_bb_63d": {"inputs": ["close"], "func": dd_110_below_lower_bb_63d},
    "dd_111_bb_width_21d": {"inputs": ["close"], "func": dd_111_bb_width_21d},
    "dd_112_bb_width_252d": {"inputs": ["close"], "func": dd_112_bb_width_252d},
    "dd_113_close_vs_lower_bb_3sigma_21d": {"inputs": ["close"], "func": dd_113_close_vs_lower_bb_3sigma_21d},
    "dd_114_close_vs_lower_bb_3sigma_63d": {"inputs": ["close"], "func": dd_114_close_vs_lower_bb_3sigma_63d},
    "dd_115_bb_squeeze_21d": {"inputs": ["close"], "func": dd_115_bb_squeeze_21d},
    "dd_116_rsi_14d": {"inputs": ["close"], "func": dd_116_rsi_14d},
    "dd_117_rsi_28d": {"inputs": ["close"], "func": dd_117_rsi_28d},
    "dd_118_rsi_63d": {"inputs": ["close"], "func": dd_118_rsi_63d},
    "dd_119_stoch_k_21d": {"inputs": ["close", "high", "low"], "func": dd_119_stoch_k_21d},
    "dd_120_stoch_k_63d": {"inputs": ["close", "high", "low"], "func": dd_120_stoch_k_63d},
    "dd_121_geom_mean_dd_252d": {"inputs": ["close"], "func": dd_121_geom_mean_dd_252d},
    "dd_122_geom_mean_dd_504d": {"inputs": ["close"], "func": dd_122_geom_mean_dd_504d},
    "dd_123_harmonic_mean_dd_252d": {"inputs": ["close"], "func": dd_123_harmonic_mean_dd_252d},
    "dd_124_quadratic_mean_dd_252d": {"inputs": ["close"], "func": dd_124_quadratic_mean_dd_252d},
    "dd_125_log_geom_mean_dd_ath": {"inputs": ["close"], "func": dd_125_log_geom_mean_dd_ath},
    "dd_126_median_dd_63d": {"inputs": ["close"], "func": dd_126_median_dd_63d},
    "dd_127_median_dd_252d": {"inputs": ["close"], "func": dd_127_median_dd_252d},
    "dd_128_median_dd_504d": {"inputs": ["close"], "func": dd_128_median_dd_504d},
    "dd_129_close_vs_252d_q25": {"inputs": ["close"], "func": dd_129_close_vs_252d_q25},
    "dd_130_close_vs_252d_q10": {"inputs": ["close"], "func": dd_130_close_vs_252d_q10},
    "dd_131_sma_cascade_alignment": {"inputs": ["close"], "func": dd_131_sma_cascade_alignment},
    "dd_132_sma_death_cross_depth_21_63": {"inputs": ["close"], "func": dd_132_sma_death_cross_depth_21_63},
    "dd_133_sma_death_cross_depth_63_126": {"inputs": ["close"], "func": dd_133_sma_death_cross_depth_63_126},
    "dd_134_sma_death_cross_depth_126_252": {"inputs": ["close"], "func": dd_134_sma_death_cross_depth_126_252},
    "dd_135_ema_cascade_alignment": {"inputs": ["close"], "func": dd_135_ema_cascade_alignment},
    "dd_136_dd_from_200d_sma_high": {"inputs": ["close"], "func": dd_136_dd_from_200d_sma_high},
    "dd_137_dd_from_63d_sma_peak": {"inputs": ["close"], "func": dd_137_dd_from_63d_sma_peak},
    "dd_138_ema200_from_ath": {"inputs": ["close"], "func": dd_138_ema200_from_ath},
    "dd_139_close_vs_ema200_zscore_252d": {"inputs": ["close"], "func": dd_139_close_vs_ema200_zscore_252d},
    "dd_140_price_acceleration_21d": {"inputs": ["close"], "func": dd_140_price_acceleration_21d},
    "dd_141_dd_q95_vs_mean_252d": {"inputs": ["close"], "func": dd_141_dd_q95_vs_mean_252d},
    "dd_142_dd_interquartile_range_252d": {"inputs": ["close"], "func": dd_142_dd_interquartile_range_252d},
    "dd_143_log_return_skew_63d": {"inputs": ["close"], "func": dd_143_log_return_skew_63d},
    "dd_144_log_return_skew_252d": {"inputs": ["close"], "func": dd_144_log_return_skew_252d},
    "dd_145_log_return_kurtosis_63d": {"inputs": ["close"], "func": dd_145_log_return_kurtosis_63d},
    "dd_146_dd_entropy_21d": {"inputs": ["close"], "func": dd_146_dd_entropy_21d},
    "dd_147_dd_entropy_63d": {"inputs": ["close"], "func": dd_147_dd_entropy_63d},
    "dd_148_dd_entropy_252d": {"inputs": ["close"], "func": dd_148_dd_entropy_252d},
    "dd_149_dd_convexity_252d": {"inputs": ["close"], "func": dd_149_dd_convexity_252d},
    "dd_150_dd_normalized_by_ath_and_atr": {"inputs": ["close", "high", "low"], "func": dd_150_dd_normalized_by_ath_and_atr},
}
