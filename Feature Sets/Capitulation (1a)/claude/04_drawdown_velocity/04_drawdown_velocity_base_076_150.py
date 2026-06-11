"""
04_drawdown_velocity — Base Features 076-150
Domain: speed of price decline, slope of the fall, drawdown velocity (continued)
Asset class: US equities | Daily OHLCV only (SEP folder — price/volume inputs only)
Target context: capitulation — characterizing (ticker, date) at/near absolute multi-year low.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_YEAR = 252
_QTR = 63
_MONTH = 21
_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)

def _ret(s: pd.Series, n: int = 1) -> pd.Series:
    return s.pct_change(n)

def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    return np.log(s).diff(n)

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()

def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over rolling window of length w."""
    def _slope(y):
        if len(y) < 2:
            return np.nan
        x = np.arange(len(y), dtype=float)
        xm = x - x.mean()
        ym = y - y.mean()
        denom = (xm * xm).sum()
        if denom == 0:
            return np.nan
        return (xm * ym).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)

def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int = 14) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()

# ── Feature functions ─────────────────────────────────────────────────────────

# --- Group T: velocity variability and dispersion ---

def dvel_076_vel_std_21d(close: pd.Series) -> pd.Series:
    """Standard deviation of daily log-returns over 21 days (velocity variability)."""
    return _log_ret(close, 1).rolling(21, min_periods=5).std()

def dvel_077_vel_std_63d(close: pd.Series) -> pd.Series:
    """Standard deviation of daily log-returns over 63 days."""
    return _log_ret(close, 1).rolling(63, min_periods=10).std()

def dvel_078_vel_std_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of daily log-returns over 252 days."""
    return _log_ret(close, 1).rolling(252, min_periods=42).std()

def dvel_079_vel_iqr_63d(close: pd.Series) -> pd.Series:
    """Interquartile range of daily velocity over 63 days."""
    dr = _log_ret(close, 1)
    q75 = dr.rolling(63, min_periods=10).quantile(0.75)
    q25 = dr.rolling(63, min_periods=10).quantile(0.25)
    return q75 - q25

def dvel_080_vel_mad_63d(close: pd.Series) -> pd.Series:
    """Median absolute deviation of daily returns over 63 days."""
    dr = _log_ret(close, 1)
    med = dr.rolling(63, min_periods=10).median()
    return (dr - med).abs().rolling(63, min_periods=10).median()

# --- Group U: skewness / kurtosis of velocity distribution ---

def dvel_081_vel_skew_21d(close: pd.Series) -> pd.Series:
    """Skewness of daily log-returns over 21 days."""
    return _log_ret(close, 1).rolling(21, min_periods=5).skew()

def dvel_082_vel_skew_63d(close: pd.Series) -> pd.Series:
    """Skewness of daily log-returns over 63 days."""
    return _log_ret(close, 1).rolling(63, min_periods=10).skew()

def dvel_083_vel_kurt_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily log-returns over 63 days."""
    return _log_ret(close, 1).rolling(63, min_periods=10).kurt()

def dvel_084_vel_kurt_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily log-returns over 252 days."""
    return _log_ret(close, 1).rolling(252, min_periods=42).kurt()

# --- Group V: tail velocity measures ---

def dvel_085_vel_5th_pctile_63d(close: pd.Series) -> pd.Series:
    """5th percentile of daily velocity over 63 days (extreme left tail speed)."""
    return _log_ret(close, 1).rolling(63, min_periods=10).quantile(0.05)

def dvel_086_vel_10th_pctile_63d(close: pd.Series) -> pd.Series:
    """10th percentile of daily velocity over 63 days."""
    return _log_ret(close, 1).rolling(63, min_periods=10).quantile(0.10)

def dvel_087_vel_5th_pctile_252d(close: pd.Series) -> pd.Series:
    """5th percentile of daily velocity over 252 days."""
    return _log_ret(close, 1).rolling(252, min_periods=42).quantile(0.05)

def dvel_088_cvar_vel_63d(close: pd.Series) -> pd.Series:
    """Conditional VaR of velocity: mean return below 5th-pctile threshold."""
    dr = _log_ret(close, 1)
    thresh = dr.rolling(63, min_periods=10).quantile(0.05)
    return dr.where(dr < thresh).rolling(63, min_periods=10).mean()

# --- Group W: autocorrelation of velocity ---

def dvel_089_vel_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over 63 days."""
    dr = _log_ret(close, 1)
    return dr.rolling(63, min_periods=10).apply(
        lambda x: pd.Series(x).autocorr(lag=1) if len(x) > 2 else np.nan, raw=True)

def dvel_090_vel_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of daily returns over 63 days."""
    dr = _log_ret(close, 1)
    return dr.rolling(63, min_periods=10).apply(
        lambda x: pd.Series(x).autocorr(lag=5) if len(x) > 6 else np.nan, raw=True)

def dvel_091_vel_autocorr_lag1_252d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns over 252 days."""
    dr = _log_ret(close, 1)
    return dr.rolling(252, min_periods=42).apply(
        lambda x: pd.Series(x).autocorr(lag=1) if len(x) > 2 else np.nan, raw=True)

# --- Group X: velocity convergence / divergence ---

def dvel_092_vel_mean_reversion_speed_63d(close: pd.Series) -> pd.Series:
    """Slope of (price - 63-day SMA) / SMA — rate at which price reverts to mean."""
    sma = _rolling_mean(close, 63)
    deviation = _safe_div(close - sma, sma)
    return _rolling_slope(deviation, 21)

def dvel_093_vel_below_ma21_depth_rate(close: pd.Series) -> pd.Series:
    """Rate of change in distance below 21-day MA per day (deepening below MA)."""
    sma = _rolling_mean(close, 21)
    gap = _safe_div(close - sma, sma)
    return _rolling_slope(gap, 10)

def dvel_094_vel_below_ma63_depth_rate(close: pd.Series) -> pd.Series:
    """Rate of change in distance below 63-day MA per day."""
    sma = _rolling_mean(close, 63)
    gap = _safe_div(close - sma, sma)
    return _rolling_slope(gap, 21)

# --- Group Y: relative velocity (price vs moving averages) ---

def dvel_095_price_vs_ma21_vel_21d(close: pd.Series) -> pd.Series:
    """Velocity of close relative to 21-day MA: (close/MA21) 5-day log change."""
    ratio = _safe_div(close, _rolling_mean(close, 21))
    return _log_ret(ratio, 5) / 5.0

def dvel_096_price_vs_ma63_vel_21d(close: pd.Series) -> pd.Series:
    """Velocity of close relative to 63-day MA."""
    ratio = _safe_div(close, _rolling_mean(close, 63))
    return _log_ret(ratio, 5) / 5.0

def dvel_097_price_vs_ma252_vel_21d(close: pd.Series) -> pd.Series:
    """Velocity of close relative to 252-day MA."""
    ratio = _safe_div(close, _rolling_mean(close, 252))
    return _log_ret(ratio, 21) / 21.0

# --- Group Z: volume-velocity interaction (expanded) ---

def dvel_098_obv_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-balance volume velocity: OBV 21-day log rate of change."""
    dr = _log_ret(close, 1)
    obv = (volume * np.sign(dr)).cumsum()
    return _log_ret(obv.abs() + 1, 21) / 21.0

def dvel_099_turnover_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-turnover velocity: 21-day log change in rolling dollar volume."""
    dv = close * volume
    return _log_ret(dv.rolling(21, min_periods=5).sum(), 5) / 5.0

def dvel_100_vol_accel_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of recent volume to longer-term volume (volume participation speed)."""
    return _safe_div(
        volume.rolling(5, min_periods=2).mean(),
        volume.rolling(21, min_periods=5).mean())

def dvel_101_vol_accel_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day average volume to 63-day average volume."""
    return _safe_div(
        volume.rolling(5, min_periods=2).mean(),
        volume.rolling(63, min_periods=10).mean())

def dvel_102_down_vol_up_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total volume on down-days to up-days over 21 days."""
    dr = _log_ret(close, 1)
    down_vol = volume.where(dr < 0, 0).rolling(21, min_periods=5).sum()
    up_vol = volume.where(dr > 0, 0).rolling(21, min_periods=5).sum()
    return _safe_div(down_vol, up_vol)

def dvel_103_down_vol_up_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total volume on down-days to up-days over 63 days."""
    dr = _log_ret(close, 1)
    down_vol = volume.where(dr < 0, 0).rolling(63, min_periods=10).sum()
    up_vol = volume.where(dr > 0, 0).rolling(63, min_periods=10).sum()
    return _safe_div(down_vol, up_vol)

def dvel_104_largest_single_day_drop_21d(close: pd.Series) -> pd.Series:
    """Largest single-day log return drop in last 21 days."""
    return _log_ret(close, 1).rolling(21, min_periods=5).min()

def dvel_105_largest_single_day_drop_63d(close: pd.Series) -> pd.Series:
    """Largest single-day log return drop in last 63 days."""
    return _log_ret(close, 1).rolling(63, min_periods=10).min()

# --- Group AA: gap velocity (open-to-prev-close) ---

def dvel_106_gap_down_vel_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Average downward gap (open vs prev close) over 21 days."""
    gap = np.log(open_) - np.log(close.shift(1))
    return gap.where(gap < 0).rolling(21, min_periods=5).mean()

def dvel_107_gap_down_freq_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Frequency of gap-down opens over 21 days."""
    gap = np.log(open_) - np.log(close.shift(1))
    return (gap < 0).rolling(21, min_periods=5).mean()

def dvel_108_intraday_neg_vel_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Average intraday decline (open to close negative) over 21 days."""
    oc = np.log(close) - np.log(open_)
    return oc.where(oc < 0).rolling(21, min_periods=5).mean()

# --- Group BB: high-low intraday velocity measures ---

def dvel_109_avg_high_low_drop_to_close_21d(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average (high - close) / (high - low) over 21 days — close near low."""
    hl = (high - low).replace(0, np.nan)
    return _safe_div(high - close, hl).rolling(21, min_periods=5).mean()

def dvel_110_avg_high_low_drop_to_close_63d(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average (high - close) / (high - low) over 63 days."""
    hl = (high - low).replace(0, np.nan)
    return _safe_div(high - close, hl).rolling(63, min_periods=10).mean()

def dvel_111_atr_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of change of ATR(14) over 21 days — expanding/contracting range speed."""
    atr14 = _atr(high, low, close, 14)
    return _log_ret(atr14, 21) / 21.0

def dvel_112_atr_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of change of ATR(14) over 63 days."""
    atr14 = _atr(high, low, close, 14)
    return _log_ret(atr14, 63) / 63.0

# --- Group CC: Stochastic-like velocity ---

def dvel_113_stoch_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of change in stochastic %K over 21 days (close position in range velocity)."""
    lo14 = _rolling_min(low, 14)
    hi14 = _rolling_max(high, 14)
    k = _safe_div(close - lo14, hi14 - lo14) * 100
    return _log_ret(k + 1, 5) / 5.0

def dvel_114_stoch_below50_freq_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Frequency of stochastic %K below 50 over 63 days."""
    lo14 = _rolling_min(low, 14)
    hi14 = _rolling_max(high, 14)
    k = _safe_div(close - lo14, hi14 - lo14) * 100
    return (k < 50).rolling(63, min_periods=10).mean()

# --- Group DD: normalized drawdown rate ---

def dvel_115_dd_rate_per_week_21d(close: pd.Series) -> pd.Series:
    """Drawdown from 21-day high, expressed as percent per week."""
    roll_max = _rolling_max(close, 21)
    dd_pct = _safe_div(close - roll_max, roll_max) * 100
    days_since = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd_pct, (days_since + 1) / 5.0)

def dvel_116_dd_rate_per_week_63d(close: pd.Series) -> pd.Series:
    """Drawdown from 63-day high, expressed as percent per week."""
    roll_max = _rolling_max(close, 63)
    dd_pct = _safe_div(close - roll_max, roll_max) * 100
    days_since = close.rolling(63, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd_pct, (days_since + 1) / 5.0)

def dvel_117_dd_rate_per_month_252d(close: pd.Series) -> pd.Series:
    """Drawdown from 252-day high, expressed as percent per month."""
    roll_max = _rolling_max(close, 252)
    dd_pct = _safe_div(close - roll_max, roll_max) * 100
    days_since = close.rolling(252, min_periods=21).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd_pct, (days_since + 1) / 21.0)

# --- Group EE: upper/lower shadow velocity ---

def dvel_118_upper_shadow_neg_vel_21d(
        close: pd.Series, high: pd.Series, open_: pd.Series) -> pd.Series:
    """Average upper shadow (high - max(open,close)) / close — rejection velocity."""
    shadow = (high - pd.concat([close, open_], axis=1).max(axis=1)) / close
    return _rolling_mean(shadow, 21)

def dvel_119_lower_shadow_vel_21d(
        close: pd.Series, low: pd.Series, open_: pd.Series) -> pd.Series:
    """Average lower shadow (min(open,close) - low) / close — support-seeking velocity."""
    shadow = (pd.concat([close, open_], axis=1).min(axis=1) - low) / close
    return _rolling_mean(shadow, 21)

# --- Group FF: multi-period velocity momentum patterns ---

def dvel_120_vel_momentum_3w(close: pd.Series) -> pd.Series:
    """Sum of signed weekly log-returns for last 3 weeks (directional thrust)."""
    w = _log_ret(close, 5)
    return w + w.shift(5) + w.shift(10)

def dvel_121_vel_momentum_3m(close: pd.Series) -> pd.Series:
    """Sum of monthly log-returns for last 3 months."""
    m = _log_ret(close, 21)
    return m + m.shift(21) + m.shift(42)

def dvel_122_vel_decel_indicator_21d(close: pd.Series) -> pd.Series:
    """Whether 5-day velocity is less negative than 21-day velocity (deceleration)."""
    v5 = _log_ret(close, 5) / 5.0
    v21 = _log_ret(close, 21) / 21.0
    return (v5 - v21).where((v5 < 0) & (v21 < 0), np.nan)

# --- Group GG: log-price level velocity ---

def dvel_123_log_price_below_trend_vel(close: pd.Series) -> pd.Series:
    """Rate of change in (log-price - 252d trend-line value) — falling below trend."""
    lp = np.log(close)
    trend = _rolling_mean(lp, 252)
    diff = lp - trend
    return _rolling_slope(diff, 21)

def dvel_124_log_price_vs_52w_low_vel(close: pd.Series) -> pd.Series:
    """Velocity of gap between current price and 52-week low (shrinking = bad)."""
    lo52 = _rolling_min(close, 252)
    gap = _safe_div(close - lo52, lo52)
    return _log_ret(gap + 1, 5) / 5.0

def dvel_125_expanding_min_gap_vel(close: pd.Series) -> pd.Series:
    """Rate of change in (close - expanding all-time-low) / close."""
    atl = close.expanding(min_periods=1).min()
    gap = _safe_div(close - atl, close)
    return _rolling_slope(gap, 21)

# --- Group HH: rolling beta-like velocity ---

def dvel_126_intra_period_range_vel_21d(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Velocity of the 21-day rolling price range (high - low) / close."""
    rng = _safe_div(_rolling_max(high, 21) - _rolling_min(low, 21), close)
    return _rolling_slope(rng, 10)

def dvel_127_intra_period_range_vel_63d(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Velocity of the 63-day rolling price range."""
    rng = _safe_div(_rolling_max(high, 63) - _rolling_min(low, 63), close)
    return _rolling_slope(rng, 21)

# --- Group II: rolling Hurst exponent as velocity persistence metric ---

def dvel_128_hurst_vel_63d(close: pd.Series) -> pd.Series:
    """Rolling Hurst-like exponent: log(std of 10-day returns) / log(std of 1-day returns)."""
    dr1 = _log_ret(close, 1)
    dr10 = _log_ret(close, 10)
    std1 = _rolling_std(dr1, 63)
    std10 = _rolling_std(dr10, 63)
    return _safe_div(np.log(std10.abs() + _EPS), np.log(std1.abs() * np.sqrt(10) + _EPS))

# --- Group JJ: cumulative velocity measures ---

def dvel_129_cum_neg_vel_ytd(close: pd.Series) -> pd.Series:
    """Cumulative negative log-return over last 252 days."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0, 0).rolling(252, min_periods=42).sum()

def dvel_130_cum_neg_vel_qtd(close: pd.Series) -> pd.Series:
    """Cumulative negative log-return over last 63 days."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0, 0).rolling(63, min_periods=10).sum()

def dvel_131_neg_vel_share_21d(close: pd.Series) -> pd.Series:
    """Fraction of total absolute velocity that is downward over 21 days."""
    dr = _log_ret(close, 1)
    neg_sum = dr.where(dr < 0, 0).rolling(21, min_periods=5).sum().abs()
    tot_sum = dr.abs().rolling(21, min_periods=5).sum()
    return _safe_div(neg_sum, tot_sum)

def dvel_132_neg_vel_share_63d(close: pd.Series) -> pd.Series:
    """Fraction of total absolute velocity that is downward over 63 days."""
    dr = _log_ret(close, 1)
    neg_sum = dr.where(dr < 0, 0).rolling(63, min_periods=10).sum().abs()
    tot_sum = dr.abs().rolling(63, min_periods=10).sum()
    return _safe_div(neg_sum, tot_sum)

# --- Group KK: signed volume velocity ---

def dvel_133_signed_vol_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day sum of volume signed by return direction, normalized by 63d avg volume."""
    dr = _log_ret(close, 1)
    signed_vol = volume * np.sign(dr)
    return _safe_div(signed_vol.rolling(5, min_periods=2).sum(),
                     volume.rolling(63, min_periods=10).mean())

def dvel_134_signed_vol_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of signed volume, normalized by 63d avg volume."""
    dr = _log_ret(close, 1)
    signed_vol = volume * np.sign(dr)
    return _safe_div(signed_vol.rolling(21, min_periods=5).sum(),
                     volume.rolling(63, min_periods=10).mean())

# --- Group LL: price momentum slope measures ---

def dvel_135_momentum_slope_21_63(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day velocity series over 63 days (trend in velocity)."""
    v21 = _log_ret(close, 21) / 21.0
    return _rolling_slope(v21, 63)

def dvel_136_momentum_slope_5_21(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day velocity series over 21 days."""
    v5 = _log_ret(close, 5) / 5.0
    return _rolling_slope(v5, 21)

def dvel_137_price_channel_vel_21d(close: pd.Series) -> pd.Series:
    """Rate of channel midpoint change: (max+min)/2 slope over 21 days."""
    channel_mid = (_rolling_max(close, 21) + _rolling_min(close, 21)) / 2.0
    return _rolling_slope(np.log(channel_mid + _EPS), 10)

def dvel_138_price_channel_vel_63d(close: pd.Series) -> pd.Series:
    """Rate of channel midpoint change over 63 days."""
    channel_mid = (_rolling_max(close, 63) + _rolling_min(close, 63)) / 2.0
    return _rolling_slope(np.log(channel_mid + _EPS), 21)

# --- Group MM: catastrophic velocity (capitulation-specific) ---

def dvel_139_max_1d_drop_in_252d(close: pd.Series) -> pd.Series:
    """Worst single-day log-return in trailing 252 days (extreme velocity event)."""
    return _log_ret(close, 1).rolling(252, min_periods=42).min()

def dvel_140_top3_worst_days_avg_252d(close: pd.Series) -> pd.Series:
    """Average of 3 worst daily log-returns in trailing 252 days."""
    dr = _log_ret(close, 1)
    return dr.rolling(252, min_periods=42).apply(
        lambda x: np.sort(x)[:3].mean() if len(x) >= 3 else np.nan, raw=True)

def dvel_141_crash_speed_score_21d(close: pd.Series) -> pd.Series:
    """Crash speed: worst 5-day drop divided by 63-day vol (normalized crash speed)."""
    worst5 = _log_ret(close, 5).rolling(21, min_periods=5).min()
    vol63 = _rolling_std(_log_ret(close, 1), 63) * np.sqrt(5)
    return _safe_div(worst5, vol63)

def dvel_142_crash_speed_score_63d(close: pd.Series) -> pd.Series:
    """Crash speed over 63-day window."""
    worst5 = _log_ret(close, 5).rolling(63, min_periods=10).min()
    vol63 = _rolling_std(_log_ret(close, 1), 63) * np.sqrt(5)
    return _safe_div(worst5, vol63)

def dvel_143_velocity_panic_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Panic index: (sum neg returns * mean vol on down days) normalized."""
    dr = _log_ret(close, 1)
    neg_ret_sum = dr.where(dr < 0, 0).rolling(21, min_periods=5).sum()
    down_vol_mean = volume.where(dr < 0).rolling(21, min_periods=5).mean()
    long_vol_mean = _rolling_mean(volume, 252)
    return neg_ret_sum * _safe_div(down_vol_mean, long_vol_mean)

# --- Group NN: velocity channel breakout speed ---

def dvel_144_channel_break_vel_21d(close: pd.Series) -> pd.Series:
    """How far below 21-day low channel close is, per day elapsed."""
    lo = _rolling_min(close, 21)
    below = (close - lo).clip(upper=0)
    days_since_low = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmin(x)), raw=True)
    return _safe_div(below / (lo + _EPS), days_since_low + 1)

def dvel_145_channel_break_vel_63d(close: pd.Series) -> pd.Series:
    """How far below 63-day low channel, per day elapsed."""
    lo = _rolling_min(close, 63)
    below = (close - lo).clip(upper=0)
    days_since_low = close.rolling(63, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmin(x)), raw=True)
    return _safe_div(below / (lo + _EPS), days_since_low + 1)

# --- Group OO: velocity relative to open-interest proxy ---

def dvel_146_vol_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of volume itself over 21 days."""
    return _log_ret(volume.rolling(5, min_periods=2).mean(), 21) / 21.0

def dvel_147_vol_roc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rate of change of volume over 63 days."""
    return _log_ret(volume.rolling(5, min_periods=2).mean(), 63) / 63.0

# --- Group PP: rolling max-drawdown-rate ---

def dvel_148_rolling_mdd_rate_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day max drawdown divided by its duration (avg dd rate in window)."""
    def _mdd_rate(x):
        cum_max = np.maximum.accumulate(x)
        dd = (x - cum_max) / cum_max
        mdd = dd.min()
        if mdd == 0:
            return 0.0
        trough_idx = np.argmin(dd)
        peak_idx = np.argmax(x[:trough_idx + 1]) if trough_idx > 0 else 0
        duration = trough_idx - peak_idx
        return mdd / (duration + 1)
    return close.rolling(63, min_periods=10).apply(_mdd_rate, raw=True)

def dvel_149_rolling_mdd_rate_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day max drawdown rate."""
    def _mdd_rate(x):
        cum_max = np.maximum.accumulate(x)
        dd = (x - cum_max) / cum_max
        mdd = dd.min()
        if mdd == 0:
            return 0.0
        trough_idx = np.argmin(dd)
        peak_idx = np.argmax(x[:trough_idx + 1]) if trough_idx > 0 else 0
        duration = trough_idx - peak_idx
        return mdd / (duration + 1)
    return close.rolling(252, min_periods=42).apply(_mdd_rate, raw=True)

def dvel_150_vel_composite_capitulation(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite capitulation velocity: blend of neg-vel-freq, worst-drop, vol-surge."""
    freq63 = (_log_ret(close, 1) < 0).rolling(63, min_periods=10).mean()
    worst21 = _log_ret(close, 5).rolling(21, min_periods=5).min()
    worst_z = _safe_div(
        worst21 - _rolling_mean(worst21, 252),
        _rolling_std(worst21, 252))
    down_vol = volume.where(_log_ret(close, 1) < 0).rolling(21, min_periods=5).mean()
    vol_ratio = _safe_div(down_vol, _rolling_mean(volume, 63))
    return (freq63 + worst_z.clip(-3, 0) / 3.0 + vol_ratio.clip(0, 3) / 3.0) / 3.0

# ── Registry ──────────────────────────────────────────────────────────────────
DRAWDOWN_VELOCITY_REGISTRY_076_150 = {
    "dvel_076_vel_std_21d": {"inputs": ["close"], "func": dvel_076_vel_std_21d},
    "dvel_077_vel_std_63d": {"inputs": ["close"], "func": dvel_077_vel_std_63d},
    "dvel_078_vel_std_252d": {"inputs": ["close"], "func": dvel_078_vel_std_252d},
    "dvel_079_vel_iqr_63d": {"inputs": ["close"], "func": dvel_079_vel_iqr_63d},
    "dvel_080_vel_mad_63d": {"inputs": ["close"], "func": dvel_080_vel_mad_63d},
    "dvel_081_vel_skew_21d": {"inputs": ["close"], "func": dvel_081_vel_skew_21d},
    "dvel_082_vel_skew_63d": {"inputs": ["close"], "func": dvel_082_vel_skew_63d},
    "dvel_083_vel_kurt_63d": {"inputs": ["close"], "func": dvel_083_vel_kurt_63d},
    "dvel_084_vel_kurt_252d": {"inputs": ["close"], "func": dvel_084_vel_kurt_252d},
    "dvel_085_vel_5th_pctile_63d": {"inputs": ["close"], "func": dvel_085_vel_5th_pctile_63d},
    "dvel_086_vel_10th_pctile_63d": {"inputs": ["close"], "func": dvel_086_vel_10th_pctile_63d},
    "dvel_087_vel_5th_pctile_252d": {"inputs": ["close"], "func": dvel_087_vel_5th_pctile_252d},
    "dvel_088_cvar_vel_63d": {"inputs": ["close"], "func": dvel_088_cvar_vel_63d},
    "dvel_089_vel_autocorr_lag1_63d": {"inputs": ["close"], "func": dvel_089_vel_autocorr_lag1_63d},
    "dvel_090_vel_autocorr_lag5_63d": {"inputs": ["close"], "func": dvel_090_vel_autocorr_lag5_63d},
    "dvel_091_vel_autocorr_lag1_252d": {"inputs": ["close"], "func": dvel_091_vel_autocorr_lag1_252d},
    "dvel_092_vel_mean_reversion_speed_63d": {"inputs": ["close"], "func": dvel_092_vel_mean_reversion_speed_63d},
    "dvel_093_vel_below_ma21_depth_rate": {"inputs": ["close"], "func": dvel_093_vel_below_ma21_depth_rate},
    "dvel_094_vel_below_ma63_depth_rate": {"inputs": ["close"], "func": dvel_094_vel_below_ma63_depth_rate},
    "dvel_095_price_vs_ma21_vel_21d": {"inputs": ["close"], "func": dvel_095_price_vs_ma21_vel_21d},
    "dvel_096_price_vs_ma63_vel_21d": {"inputs": ["close"], "func": dvel_096_price_vs_ma63_vel_21d},
    "dvel_097_price_vs_ma252_vel_21d": {"inputs": ["close"], "func": dvel_097_price_vs_ma252_vel_21d},
    "dvel_098_obv_vel_21d": {"inputs": ["close", "volume"], "func": dvel_098_obv_vel_21d},
    "dvel_099_turnover_vel_21d": {"inputs": ["close", "volume"], "func": dvel_099_turnover_vel_21d},
    "dvel_100_vol_accel_ratio_21d": {"inputs": ["close", "volume"], "func": dvel_100_vol_accel_ratio_21d},
    "dvel_101_vol_accel_ratio_63d": {"inputs": ["close", "volume"], "func": dvel_101_vol_accel_ratio_63d},
    "dvel_102_down_vol_up_vol_ratio_21d": {"inputs": ["close", "volume"], "func": dvel_102_down_vol_up_vol_ratio_21d},
    "dvel_103_down_vol_up_vol_ratio_63d": {"inputs": ["close", "volume"], "func": dvel_103_down_vol_up_vol_ratio_63d},
    "dvel_104_largest_single_day_drop_21d": {"inputs": ["close"], "func": dvel_104_largest_single_day_drop_21d},
    "dvel_105_largest_single_day_drop_63d": {"inputs": ["close"], "func": dvel_105_largest_single_day_drop_63d},
    "dvel_106_gap_down_vel_21d": {"inputs": ["close", "open"], "func": dvel_106_gap_down_vel_21d},
    "dvel_107_gap_down_freq_21d": {"inputs": ["close", "open"], "func": dvel_107_gap_down_freq_21d},
    "dvel_108_intraday_neg_vel_21d": {"inputs": ["close", "open"], "func": dvel_108_intraday_neg_vel_21d},
    "dvel_109_avg_high_low_drop_to_close_21d": {"inputs": ["close", "high", "low"], "func": dvel_109_avg_high_low_drop_to_close_21d},
    "dvel_110_avg_high_low_drop_to_close_63d": {"inputs": ["close", "high", "low"], "func": dvel_110_avg_high_low_drop_to_close_63d},
    "dvel_111_atr_vel_21d": {"inputs": ["close", "high", "low"], "func": dvel_111_atr_vel_21d},
    "dvel_112_atr_vel_63d": {"inputs": ["close", "high", "low"], "func": dvel_112_atr_vel_63d},
    "dvel_113_stoch_vel_21d": {"inputs": ["close", "high", "low"], "func": dvel_113_stoch_vel_21d},
    "dvel_114_stoch_below50_freq_63d": {"inputs": ["close", "high", "low"], "func": dvel_114_stoch_below50_freq_63d},
    "dvel_115_dd_rate_per_week_21d": {"inputs": ["close"], "func": dvel_115_dd_rate_per_week_21d},
    "dvel_116_dd_rate_per_week_63d": {"inputs": ["close"], "func": dvel_116_dd_rate_per_week_63d},
    "dvel_117_dd_rate_per_month_252d": {"inputs": ["close"], "func": dvel_117_dd_rate_per_month_252d},
    "dvel_118_upper_shadow_neg_vel_21d": {"inputs": ["close", "high", "open"], "func": dvel_118_upper_shadow_neg_vel_21d},
    "dvel_119_lower_shadow_vel_21d": {"inputs": ["close", "low", "open"], "func": dvel_119_lower_shadow_vel_21d},
    "dvel_120_vel_momentum_3w": {"inputs": ["close"], "func": dvel_120_vel_momentum_3w},
    "dvel_121_vel_momentum_3m": {"inputs": ["close"], "func": dvel_121_vel_momentum_3m},
    "dvel_122_vel_decel_indicator_21d": {"inputs": ["close"], "func": dvel_122_vel_decel_indicator_21d},
    "dvel_123_log_price_below_trend_vel": {"inputs": ["close"], "func": dvel_123_log_price_below_trend_vel},
    "dvel_124_log_price_vs_52w_low_vel": {"inputs": ["close"], "func": dvel_124_log_price_vs_52w_low_vel},
    "dvel_125_expanding_min_gap_vel": {"inputs": ["close"], "func": dvel_125_expanding_min_gap_vel},
    "dvel_126_intra_period_range_vel_21d": {"inputs": ["close", "high", "low"], "func": dvel_126_intra_period_range_vel_21d},
    "dvel_127_intra_period_range_vel_63d": {"inputs": ["close", "high", "low"], "func": dvel_127_intra_period_range_vel_63d},
    "dvel_128_hurst_vel_63d": {"inputs": ["close"], "func": dvel_128_hurst_vel_63d},
    "dvel_129_cum_neg_vel_ytd": {"inputs": ["close"], "func": dvel_129_cum_neg_vel_ytd},
    "dvel_130_cum_neg_vel_qtd": {"inputs": ["close"], "func": dvel_130_cum_neg_vel_qtd},
    "dvel_131_neg_vel_share_21d": {"inputs": ["close"], "func": dvel_131_neg_vel_share_21d},
    "dvel_132_neg_vel_share_63d": {"inputs": ["close"], "func": dvel_132_neg_vel_share_63d},
    "dvel_133_signed_vol_vel_5d": {"inputs": ["close", "volume"], "func": dvel_133_signed_vol_vel_5d},
    "dvel_134_signed_vol_vel_21d": {"inputs": ["close", "volume"], "func": dvel_134_signed_vol_vel_21d},
    "dvel_135_momentum_slope_21_63": {"inputs": ["close"], "func": dvel_135_momentum_slope_21_63},
    "dvel_136_momentum_slope_5_21": {"inputs": ["close"], "func": dvel_136_momentum_slope_5_21},
    "dvel_137_price_channel_vel_21d": {"inputs": ["close"], "func": dvel_137_price_channel_vel_21d},
    "dvel_138_price_channel_vel_63d": {"inputs": ["close"], "func": dvel_138_price_channel_vel_63d},
    "dvel_139_max_1d_drop_in_252d": {"inputs": ["close"], "func": dvel_139_max_1d_drop_in_252d},
    "dvel_140_top3_worst_days_avg_252d": {"inputs": ["close"], "func": dvel_140_top3_worst_days_avg_252d},
    "dvel_141_crash_speed_score_21d": {"inputs": ["close"], "func": dvel_141_crash_speed_score_21d},
    "dvel_142_crash_speed_score_63d": {"inputs": ["close"], "func": dvel_142_crash_speed_score_63d},
    "dvel_143_velocity_panic_index_21d": {"inputs": ["close", "volume"], "func": dvel_143_velocity_panic_index_21d},
    "dvel_144_channel_break_vel_21d": {"inputs": ["close"], "func": dvel_144_channel_break_vel_21d},
    "dvel_145_channel_break_vel_63d": {"inputs": ["close"], "func": dvel_145_channel_break_vel_63d},
    "dvel_146_vol_roc_21d": {"inputs": ["close", "volume"], "func": dvel_146_vol_roc_21d},
    "dvel_147_vol_roc_63d": {"inputs": ["close", "volume"], "func": dvel_147_vol_roc_63d},
    "dvel_148_rolling_mdd_rate_63d": {"inputs": ["close"], "func": dvel_148_rolling_mdd_rate_63d},
    "dvel_149_rolling_mdd_rate_252d": {"inputs": ["close"], "func": dvel_149_rolling_mdd_rate_252d},
    "dvel_150_vel_composite_capitulation": {"inputs": ["close", "volume"], "func": dvel_150_vel_composite_capitulation},
}
