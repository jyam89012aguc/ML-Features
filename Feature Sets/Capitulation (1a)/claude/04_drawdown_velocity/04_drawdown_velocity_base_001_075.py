"""
04_drawdown_velocity — Base Features 001-075
Domain: speed of price decline, slope of the fall, drawdown velocity
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

# --- Group A: raw log-price velocity over fixed horizons ---

def dvel_001_log_vel_1d(close: pd.Series) -> pd.Series:
    """Single-day log-return: immediate price velocity."""
    return _log_ret(close, 1)

def dvel_002_log_vel_5d(close: pd.Series) -> pd.Series:
    """5-day log return normalized per day."""
    return _log_ret(close, 5) / 5.0

def dvel_003_log_vel_10d(close: pd.Series) -> pd.Series:
    """10-day log return normalized per day."""
    return _log_ret(close, 10) / 10.0

def dvel_004_log_vel_21d(close: pd.Series) -> pd.Series:
    """21-day log return normalized per day."""
    return _log_ret(close, 21) / 21.0

def dvel_005_log_vel_63d(close: pd.Series) -> pd.Series:
    """63-day log return normalized per day."""
    return _log_ret(close, 63) / 63.0

def dvel_006_log_vel_126d(close: pd.Series) -> pd.Series:
    """126-day log return normalized per day."""
    return _log_ret(close, 126) / 126.0

def dvel_007_log_vel_252d(close: pd.Series) -> pd.Series:
    """252-day log return normalized per day."""
    return _log_ret(close, 252) / 252.0

# --- Group B: OLS slope of log-price (linear descent speed) ---

def dvel_008_ols_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of log-price over 5-day window — instantaneous descent rate."""
    return _rolling_slope(np.log(close), 5)

def dvel_009_ols_slope_10d(close: pd.Series) -> pd.Series:
    """OLS slope of log-price over 10-day window."""
    return _rolling_slope(np.log(close), 10)

def dvel_010_ols_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of log-price over 21-day window."""
    return _rolling_slope(np.log(close), 21)

def dvel_011_ols_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of log-price over 63-day window."""
    return _rolling_slope(np.log(close), 63)

def dvel_012_ols_slope_126d(close: pd.Series) -> pd.Series:
    """OLS slope of log-price over 126-day window."""
    return _rolling_slope(np.log(close), 126)

# --- Group C: fastest N-day drop in a window ---

def dvel_013_worst_5d_drop_in_21d(close: pd.Series) -> pd.Series:
    """Most negative 5-day log return within last 21 days."""
    return _log_ret(close, 5).rolling(21, min_periods=5).min()

def dvel_014_worst_5d_drop_in_63d(close: pd.Series) -> pd.Series:
    """Most negative 5-day log return within last 63 days."""
    return _log_ret(close, 5).rolling(63, min_periods=10).min()

def dvel_015_worst_10d_drop_in_63d(close: pd.Series) -> pd.Series:
    """Most negative 10-day log return within last 63 days."""
    return _log_ret(close, 10).rolling(63, min_periods=10).min()

def dvel_016_worst_21d_drop_in_126d(close: pd.Series) -> pd.Series:
    """Most negative 21-day log return within last 126 days."""
    return _log_ret(close, 21).rolling(126, min_periods=21).min()

def dvel_017_worst_21d_drop_in_252d(close: pd.Series) -> pd.Series:
    """Most negative 21-day log return within last 252 days."""
    return _log_ret(close, 21).rolling(252, min_periods=42).min()

def dvel_018_worst_63d_drop_in_252d(close: pd.Series) -> pd.Series:
    """Most negative 63-day log return within last 252 days."""
    return _log_ret(close, 63).rolling(252, min_periods=63).min()

# --- Group D: drawdown / time-since-high velocity ---

def dvel_019_dd_over_days_since_high_21d(close: pd.Series) -> pd.Series:
    """Drawdown depth divided by days since rolling 21-day high — velocity of fall."""
    roll_max = _rolling_max(close, 21)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd, days_since + 1)

def dvel_020_dd_over_days_since_high_63d(close: pd.Series) -> pd.Series:
    """Drawdown depth / days since 63-day high."""
    roll_max = _rolling_max(close, 63)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(63, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd, days_since + 1)

def dvel_021_dd_over_days_since_high_252d(close: pd.Series) -> pd.Series:
    """Drawdown depth / days since 252-day high."""
    roll_max = _rolling_max(close, 252)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(252, min_periods=21).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd, days_since + 1)

def dvel_022_ath_dd_over_days_since_ath(close: pd.Series) -> pd.Series:
    """All-time-high drawdown velocity: ATH drawdown / days since ATH."""
    ath = close.cummax()
    dd = _safe_div(close - ath, ath)
    is_high = (close >= ath)
    idx_arr = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_ath_idx = idx_arr.where(is_high).ffill().fillna(0)
    days_since = idx_arr - last_ath_idx
    return _safe_div(dd, days_since + 1)

# --- Group E: drawdown points per day (absolute $ velocity) ---

def dvel_023_abs_dollar_drop_per_day_21d(close: pd.Series) -> pd.Series:
    """Absolute dollar decline from 21-day high per trading day elapsed."""
    roll_max = _rolling_max(close, 21)
    dollar_dd = close - roll_max
    days_since = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dollar_dd, days_since + 1)

def dvel_024_abs_dollar_drop_per_day_63d(close: pd.Series) -> pd.Series:
    """Absolute dollar decline from 63-day high per trading day elapsed."""
    roll_max = _rolling_max(close, 63)
    dollar_dd = close - roll_max
    days_since = close.rolling(63, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dollar_dd, days_since + 1)

# --- Group F: ATR-normalized velocity ---

def dvel_025_atr_norm_vel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day price change normalized by ATR(14)."""
    return _safe_div(close - close.shift(5), _atr(high, low, close, 14))

def dvel_026_atr_norm_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day price change normalized by ATR(21)."""
    return _safe_div(close - close.shift(21), _atr(high, low, close, 21))

def dvel_027_atr_norm_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day price change normalized by ATR(63)."""
    return _safe_div(close - close.shift(63), _atr(high, low, close, 63))

# --- Group G: volatility-scaled velocity ---

def dvel_028_vol_scaled_vel_21d(close: pd.Series) -> pd.Series:
    """21-day log return divided by 21-day realized vol (Sharpe-like speed)."""
    r = _log_ret(close, 21)
    vol = _log_ret(close, 1).rolling(21, min_periods=5).std() * np.sqrt(21)
    return _safe_div(r, vol)

def dvel_029_vol_scaled_vel_63d(close: pd.Series) -> pd.Series:
    """63-day log return divided by 63-day realized vol."""
    r = _log_ret(close, 63)
    vol = _log_ret(close, 1).rolling(63, min_periods=10).std() * np.sqrt(63)
    return _safe_div(r, vol)

def dvel_030_vol_scaled_vel_126d(close: pd.Series) -> pd.Series:
    """126-day log return divided by 126-day realized vol."""
    r = _log_ret(close, 126)
    vol = _log_ret(close, 1).rolling(126, min_periods=21).std() * np.sqrt(126)
    return _safe_div(r, vol)

# --- Group H: z-score of velocity ---

def dvel_031_vel_zscore_252d_5d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day log-return vs trailing 252-day distribution."""
    v = _log_ret(close, 5)
    return _safe_div(v - v.rolling(252, min_periods=42).mean(),
                     v.rolling(252, min_periods=42).std())

def dvel_032_vel_zscore_252d_21d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day log-return vs trailing 252-day distribution."""
    v = _log_ret(close, 21)
    return _safe_div(v - v.rolling(252, min_periods=42).mean(),
                     v.rolling(252, min_periods=42).std())

def dvel_033_vel_zscore_252d_63d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day log-return vs trailing 252-day distribution."""
    v = _log_ret(close, 63)
    return _safe_div(v - v.rolling(252, min_periods=63).mean(),
                     v.rolling(252, min_periods=63).std())

# --- Group I: average descent rate while underwater ---

def dvel_034_avg_neg_daily_vel_21d(close: pd.Series) -> pd.Series:
    """Mean of negative daily log-returns over 21-day window (avg down-day speed)."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0).rolling(21, min_periods=5).mean()

def dvel_035_avg_neg_daily_vel_63d(close: pd.Series) -> pd.Series:
    """Mean of negative daily log-returns over 63-day window."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0).rolling(63, min_periods=10).mean()

def dvel_036_avg_neg_daily_vel_126d(close: pd.Series) -> pd.Series:
    """Mean of negative daily log-returns over 126-day window."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0).rolling(126, min_periods=21).mean()

def dvel_037_sum_neg_vel_21d(close: pd.Series) -> pd.Series:
    """Sum of negative daily log-returns over 21 days (total downward thrust)."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0, 0).rolling(21, min_periods=5).sum()

def dvel_038_sum_neg_vel_63d(close: pd.Series) -> pd.Series:
    """Sum of negative daily log-returns over 63 days."""
    dr = _log_ret(close, 1)
    return dr.where(dr < 0, 0).rolling(63, min_periods=10).sum()

# --- Group J: time to fall X% ---

def dvel_039_days_to_fall_10pct(close: pd.Series) -> pd.Series:
    """Rolling: how many days ago was price 10% higher (proxy for speed to -10%)."""
    target = close * 1.10
    def _days(x):
        crosses = np.where(x >= target.iloc[len(x) - 1])[0]  # type: ignore
        return (len(x) - 1 - crosses[-1]) if len(crosses) > 0 else np.nan
    return close.rolling(252, min_periods=21).apply(
        lambda x: (len(x) - 1 - np.argmax(x >= x[-1] * 1.10)) if np.any(x >= x[-1] * 1.10) else np.nan,
        raw=True)

def dvel_040_days_to_fall_20pct(close: pd.Series) -> pd.Series:
    """How many days ago was price 20% higher (days elapsed to -20%)."""
    return close.rolling(252, min_periods=21).apply(
        lambda x: (len(x) - 1 - np.argmax(x >= x[-1] * 1.20)) if np.any(x >= x[-1] * 1.20) else np.nan,
        raw=True)

def dvel_041_days_to_fall_30pct(close: pd.Series) -> pd.Series:
    """How many days ago was price 30% higher."""
    return close.rolling(504, min_periods=42).apply(
        lambda x: (len(x) - 1 - np.argmax(x >= x[-1] * 1.30)) if np.any(x >= x[-1] * 1.30) else np.nan,
        raw=True)

def dvel_042_days_to_fall_50pct(close: pd.Series) -> pd.Series:
    """How many days ago was price 50% higher (days elapsed to -50%)."""
    return close.rolling(756, min_periods=63).apply(
        lambda x: (len(x) - 1 - np.argmax(x >= x[-1] * 1.50)) if np.any(x >= x[-1] * 1.50) else np.nan,
        raw=True)

# --- Group K: velocity spread (short minus long horizon) ---

def dvel_043_vel_spread_5_vs_21(close: pd.Series) -> pd.Series:
    """5-day velocity minus 21-day velocity — short-term vs medium-term speed."""
    return _log_ret(close, 5) / 5.0 - _log_ret(close, 21) / 21.0

def dvel_044_vel_spread_21_vs_63(close: pd.Series) -> pd.Series:
    """21-day velocity minus 63-day velocity."""
    return _log_ret(close, 21) / 21.0 - _log_ret(close, 63) / 63.0

def dvel_045_vel_spread_63_vs_252(close: pd.Series) -> pd.Series:
    """63-day velocity minus 252-day velocity."""
    return _log_ret(close, 63) / 63.0 - _log_ret(close, 252) / 252.0

def dvel_046_vel_ratio_5_vs_63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day to 63-day per-day velocity."""
    return _safe_div(_log_ret(close, 5) / 5.0, _log_ret(close, 63) / 63.0)

def dvel_047_vel_ratio_21_vs_252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day per-day velocity."""
    return _safe_div(_log_ret(close, 21) / 21.0, _log_ret(close, 252) / 252.0)

# --- Group L: EMA-based velocity ---

def dvel_048_ema10_slope(close: pd.Series) -> pd.Series:
    """5-day log return of EMA(10) — smooth short-term descent speed."""
    return _log_ret(close.ewm(span=10, adjust=False).mean(), 5) / 5.0

def dvel_049_ema21_slope(close: pd.Series) -> pd.Series:
    """5-day log return of EMA(21)."""
    return _log_ret(close.ewm(span=21, adjust=False).mean(), 5) / 5.0

def dvel_050_ema50_slope(close: pd.Series) -> pd.Series:
    """10-day log return of EMA(50)."""
    return _log_ret(close.ewm(span=50, adjust=False).mean(), 10) / 10.0

def dvel_051_ema200_slope(close: pd.Series) -> pd.Series:
    """21-day log return of EMA(200)."""
    return _log_ret(close.ewm(span=200, adjust=False).mean(), 21) / 21.0

def dvel_052_ema_cross_vel_diff(close: pd.Series) -> pd.Series:
    """EMA(10) velocity minus EMA(50) velocity — short vs long smooth speed."""
    v10 = _log_ret(close.ewm(span=10, adjust=False).mean(), 5) / 5.0
    v50 = _log_ret(close.ewm(span=50, adjust=False).mean(), 10) / 10.0
    return v10 - v50

# --- Group M: volume-weighted velocity ---

def dvel_053_vwap_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day VWAP velocity: rate of change of rolling VWAP."""
    vwap = _safe_div(
        (close * volume).rolling(21, min_periods=5).sum(),
        volume.rolling(21, min_periods=5).sum())
    return _log_ret(vwap, 5) / 5.0

def dvel_054_vwap_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VWAP velocity."""
    vwap = _safe_div(
        (close * volume).rolling(63, min_periods=10).sum(),
        volume.rolling(63, min_periods=10).sum())
    return _log_ret(vwap, 10) / 10.0

def dvel_055_vol_weighted_neg_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative daily returns — heavy-volume down-days."""
    dr = _log_ret(close, 1)
    neg_vw = (dr * volume).where(dr < 0, 0)
    vol_sum = volume.rolling(21, min_periods=5).sum()
    return _safe_div(neg_vw.rolling(21, min_periods=5).sum(), vol_sum)

def dvel_056_vol_weighted_neg_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative daily returns over 63 days."""
    dr = _log_ret(close, 1)
    neg_vw = (dr * volume).where(dr < 0, 0)
    vol_sum = volume.rolling(63, min_periods=10).sum()
    return _safe_div(neg_vw.rolling(63, min_periods=10).sum(), vol_sum)

def dvel_057_vol_surge_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down-days relative to mean volume — how heavy selling is."""
    dr = _log_ret(close, 1)
    vol_avg = _rolling_mean(volume, 21)
    down_vol = volume.where(dr < 0)
    return _safe_div(down_vol.rolling(21, min_periods=5).mean(), vol_avg)

# --- Group N: velocity persistence and frequency ---

def dvel_058_neg_vel_freq_21d(close: pd.Series) -> pd.Series:
    """Fraction of days with negative return in last 21 days."""
    dr = _log_ret(close, 1)
    return (dr < 0).rolling(21, min_periods=5).mean()

def dvel_059_neg_vel_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of days with negative return in last 63 days."""
    dr = _log_ret(close, 1)
    return (dr < 0).rolling(63, min_periods=10).mean()

def dvel_060_neg_5d_vel_freq_63d(close: pd.Series) -> pd.Series:
    """Fraction of overlapping 5-day windows with negative return over last 63 days."""
    v5 = _log_ret(close, 5)
    return (v5 < 0).rolling(63, min_periods=10).mean()

def dvel_061_streak_down_days(close: pd.Series) -> pd.Series:
    """Rolling count of consecutive down days (current streak)."""
    dr = _log_ret(close, 1)
    def _streak(x):
        cnt = 0
        for v in reversed(x):
            if v < 0:
                cnt += 1
            else:
                break
        return cnt
    return dr.rolling(63, min_periods=1).apply(_streak, raw=True)

# --- Group O: velocity rank (percentile) ---

def dvel_062_vel_pct_rank_252d_5d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day velocity in last 252-day distribution."""
    return _log_ret(close, 5).rolling(252, min_periods=42).rank(pct=True)

def dvel_063_vel_pct_rank_252d_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21-day velocity in last 252-day distribution."""
    return _log_ret(close, 21).rolling(252, min_periods=42).rank(pct=True)

# --- Group P: high-low velocity (intraday speed) ---

def dvel_064_hl_range_vel_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average daily high-low range / close as fraction — intraday velocity spread."""
    hl_frac = _safe_div(high - low, close)
    return _rolling_mean(hl_frac, 21)

def dvel_065_hl_range_vel_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average daily high-low range fraction over 63 days."""
    hl_frac = _safe_div(high - low, close)
    return _rolling_mean(hl_frac, 63)

def dvel_066_close_to_low_vel_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Average (close - low)/close over 21 days — proximity to day-low."""
    frac = _safe_div(close - low, close)
    return _rolling_mean(frac, 21)

def dvel_067_open_to_close_neg_vel_21d(
        close: pd.Series, open_: pd.Series) -> pd.Series:
    """Average negative open-to-close log return over 21 days."""
    oc = np.log(close) - np.log(open_)
    return oc.where(oc < 0).rolling(21, min_periods=5).mean()

# --- Group Q: slope of OLS residual series (detrended speed) ---

def dvel_068_detrended_vel_21d(close: pd.Series) -> pd.Series:
    """Slope of OLS-detrended log-price over 21 days (residual velocity)."""
    lp = np.log(close)
    trend = _rolling_slope(lp, 63) * pd.Series(np.arange(len(lp)), index=lp.index)
    residual = lp - lp.rolling(63, min_periods=10).mean()
    return _rolling_slope(residual, 21)

def dvel_069_detrended_vel_63d(close: pd.Series) -> pd.Series:
    """Slope of OLS-detrended log-price over 63 days."""
    lp = np.log(close)
    residual = lp - lp.rolling(126, min_periods=21).mean()
    return _rolling_slope(residual, 63)

# --- Group R: acceleration proxy in base file (slope of velocity) ---

def dvel_070_vel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of the 5-day velocity series over 21 days — speed of speed change."""
    v5 = _log_ret(close, 5)
    return _rolling_slope(v5, 21)

def dvel_071_vel_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of the 5-day velocity series over 63 days."""
    v5 = _log_ret(close, 5)
    return _rolling_slope(v5, 63)

# --- Group S: theoretical speed measures ---

def dvel_072_days_to_zero_at_current_vel(close: pd.Series) -> pd.Series:
    """Theoretical days to reach $0 at current 21-day log velocity (negative only)."""
    v = _log_ret(close, 21) / 21.0
    # log(0) = -inf, so days = -log(close) / v  (only meaningful when v < 0)
    return _safe_div(-np.log(close), v).where(v < 0)

def dvel_073_pct_time_in_top_decile_neg_vel_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent in top decile of negative daily velocity."""
    dr = _log_ret(close, 1)
    thresh = dr.rolling(252, min_periods=42).quantile(0.10)
    return (dr < thresh).rolling(252, min_periods=42).mean()

def dvel_074_vel_consistency_score_63d(close: pd.Series) -> pd.Series:
    """Consistency: mean negative daily velocity / std of daily velocity (Sortino-speed)."""
    dr = _log_ret(close, 1)
    neg_mean = dr.where(dr < 0).rolling(63, min_periods=10).mean()
    total_std = _rolling_std(dr, 63)
    return _safe_div(neg_mean, total_std)

def dvel_075_composite_vel_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite velocity: equal-weight of z-scored 5d, 21d, 63d velocities."""
    v5 = _log_ret(close, 5) / 5.0
    v21 = _log_ret(close, 21) / 21.0
    v63 = _log_ret(close, 63) / 63.0
    def _zscore(s, w=252):
        return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))
    return (_zscore(v5) + _zscore(v21) + _zscore(v63)) / 3.0

# ── Registry ──────────────────────────────────────────────────────────────────
DRAWDOWN_VELOCITY_REGISTRY_001_075 = {
    "dvel_001_log_vel_1d": {"inputs": ["close"], "func": dvel_001_log_vel_1d},
    "dvel_002_log_vel_5d": {"inputs": ["close"], "func": dvel_002_log_vel_5d},
    "dvel_003_log_vel_10d": {"inputs": ["close"], "func": dvel_003_log_vel_10d},
    "dvel_004_log_vel_21d": {"inputs": ["close"], "func": dvel_004_log_vel_21d},
    "dvel_005_log_vel_63d": {"inputs": ["close"], "func": dvel_005_log_vel_63d},
    "dvel_006_log_vel_126d": {"inputs": ["close"], "func": dvel_006_log_vel_126d},
    "dvel_007_log_vel_252d": {"inputs": ["close"], "func": dvel_007_log_vel_252d},
    "dvel_008_ols_slope_5d": {"inputs": ["close"], "func": dvel_008_ols_slope_5d},
    "dvel_009_ols_slope_10d": {"inputs": ["close"], "func": dvel_009_ols_slope_10d},
    "dvel_010_ols_slope_21d": {"inputs": ["close"], "func": dvel_010_ols_slope_21d},
    "dvel_011_ols_slope_63d": {"inputs": ["close"], "func": dvel_011_ols_slope_63d},
    "dvel_012_ols_slope_126d": {"inputs": ["close"], "func": dvel_012_ols_slope_126d},
    "dvel_013_worst_5d_drop_in_21d": {"inputs": ["close"], "func": dvel_013_worst_5d_drop_in_21d},
    "dvel_014_worst_5d_drop_in_63d": {"inputs": ["close"], "func": dvel_014_worst_5d_drop_in_63d},
    "dvel_015_worst_10d_drop_in_63d": {"inputs": ["close"], "func": dvel_015_worst_10d_drop_in_63d},
    "dvel_016_worst_21d_drop_in_126d": {"inputs": ["close"], "func": dvel_016_worst_21d_drop_in_126d},
    "dvel_017_worst_21d_drop_in_252d": {"inputs": ["close"], "func": dvel_017_worst_21d_drop_in_252d},
    "dvel_018_worst_63d_drop_in_252d": {"inputs": ["close"], "func": dvel_018_worst_63d_drop_in_252d},
    "dvel_019_dd_over_days_since_high_21d": {"inputs": ["close"], "func": dvel_019_dd_over_days_since_high_21d},
    "dvel_020_dd_over_days_since_high_63d": {"inputs": ["close"], "func": dvel_020_dd_over_days_since_high_63d},
    "dvel_021_dd_over_days_since_high_252d": {"inputs": ["close"], "func": dvel_021_dd_over_days_since_high_252d},
    "dvel_022_ath_dd_over_days_since_ath": {"inputs": ["close"], "func": dvel_022_ath_dd_over_days_since_ath},
    "dvel_023_abs_dollar_drop_per_day_21d": {"inputs": ["close"], "func": dvel_023_abs_dollar_drop_per_day_21d},
    "dvel_024_abs_dollar_drop_per_day_63d": {"inputs": ["close"], "func": dvel_024_abs_dollar_drop_per_day_63d},
    "dvel_025_atr_norm_vel_5d": {"inputs": ["close", "high", "low"], "func": dvel_025_atr_norm_vel_5d},
    "dvel_026_atr_norm_vel_21d": {"inputs": ["close", "high", "low"], "func": dvel_026_atr_norm_vel_21d},
    "dvel_027_atr_norm_vel_63d": {"inputs": ["close", "high", "low"], "func": dvel_027_atr_norm_vel_63d},
    "dvel_028_vol_scaled_vel_21d": {"inputs": ["close"], "func": dvel_028_vol_scaled_vel_21d},
    "dvel_029_vol_scaled_vel_63d": {"inputs": ["close"], "func": dvel_029_vol_scaled_vel_63d},
    "dvel_030_vol_scaled_vel_126d": {"inputs": ["close"], "func": dvel_030_vol_scaled_vel_126d},
    "dvel_031_vel_zscore_252d_5d": {"inputs": ["close"], "func": dvel_031_vel_zscore_252d_5d},
    "dvel_032_vel_zscore_252d_21d": {"inputs": ["close"], "func": dvel_032_vel_zscore_252d_21d},
    "dvel_033_vel_zscore_252d_63d": {"inputs": ["close"], "func": dvel_033_vel_zscore_252d_63d},
    "dvel_034_avg_neg_daily_vel_21d": {"inputs": ["close"], "func": dvel_034_avg_neg_daily_vel_21d},
    "dvel_035_avg_neg_daily_vel_63d": {"inputs": ["close"], "func": dvel_035_avg_neg_daily_vel_63d},
    "dvel_036_avg_neg_daily_vel_126d": {"inputs": ["close"], "func": dvel_036_avg_neg_daily_vel_126d},
    "dvel_037_sum_neg_vel_21d": {"inputs": ["close"], "func": dvel_037_sum_neg_vel_21d},
    "dvel_038_sum_neg_vel_63d": {"inputs": ["close"], "func": dvel_038_sum_neg_vel_63d},
    "dvel_039_days_to_fall_10pct": {"inputs": ["close"], "func": dvel_039_days_to_fall_10pct},
    "dvel_040_days_to_fall_20pct": {"inputs": ["close"], "func": dvel_040_days_to_fall_20pct},
    "dvel_041_days_to_fall_30pct": {"inputs": ["close"], "func": dvel_041_days_to_fall_30pct},
    "dvel_042_days_to_fall_50pct": {"inputs": ["close"], "func": dvel_042_days_to_fall_50pct},
    "dvel_043_vel_spread_5_vs_21": {"inputs": ["close"], "func": dvel_043_vel_spread_5_vs_21},
    "dvel_044_vel_spread_21_vs_63": {"inputs": ["close"], "func": dvel_044_vel_spread_21_vs_63},
    "dvel_045_vel_spread_63_vs_252": {"inputs": ["close"], "func": dvel_045_vel_spread_63_vs_252},
    "dvel_046_vel_ratio_5_vs_63": {"inputs": ["close"], "func": dvel_046_vel_ratio_5_vs_63},
    "dvel_047_vel_ratio_21_vs_252": {"inputs": ["close"], "func": dvel_047_vel_ratio_21_vs_252},
    "dvel_048_ema10_slope": {"inputs": ["close"], "func": dvel_048_ema10_slope},
    "dvel_049_ema21_slope": {"inputs": ["close"], "func": dvel_049_ema21_slope},
    "dvel_050_ema50_slope": {"inputs": ["close"], "func": dvel_050_ema50_slope},
    "dvel_051_ema200_slope": {"inputs": ["close"], "func": dvel_051_ema200_slope},
    "dvel_052_ema_cross_vel_diff": {"inputs": ["close"], "func": dvel_052_ema_cross_vel_diff},
    "dvel_053_vwap_vel_21d": {"inputs": ["close", "volume"], "func": dvel_053_vwap_vel_21d},
    "dvel_054_vwap_vel_63d": {"inputs": ["close", "volume"], "func": dvel_054_vwap_vel_63d},
    "dvel_055_vol_weighted_neg_vel_21d": {"inputs": ["close", "volume"], "func": dvel_055_vol_weighted_neg_vel_21d},
    "dvel_056_vol_weighted_neg_vel_63d": {"inputs": ["close", "volume"], "func": dvel_056_vol_weighted_neg_vel_63d},
    "dvel_057_vol_surge_on_down_days_21d": {"inputs": ["close", "volume"], "func": dvel_057_vol_surge_on_down_days_21d},
    "dvel_058_neg_vel_freq_21d": {"inputs": ["close"], "func": dvel_058_neg_vel_freq_21d},
    "dvel_059_neg_vel_freq_63d": {"inputs": ["close"], "func": dvel_059_neg_vel_freq_63d},
    "dvel_060_neg_5d_vel_freq_63d": {"inputs": ["close"], "func": dvel_060_neg_5d_vel_freq_63d},
    "dvel_061_streak_down_days": {"inputs": ["close"], "func": dvel_061_streak_down_days},
    "dvel_062_vel_pct_rank_252d_5d": {"inputs": ["close"], "func": dvel_062_vel_pct_rank_252d_5d},
    "dvel_063_vel_pct_rank_252d_21d": {"inputs": ["close"], "func": dvel_063_vel_pct_rank_252d_21d},
    "dvel_064_hl_range_vel_21d": {"inputs": ["close", "high", "low"], "func": dvel_064_hl_range_vel_21d},
    "dvel_065_hl_range_vel_63d": {"inputs": ["close", "high", "low"], "func": dvel_065_hl_range_vel_63d},
    "dvel_066_close_to_low_vel_21d": {"inputs": ["close", "low"], "func": dvel_066_close_to_low_vel_21d},
    "dvel_067_open_to_close_neg_vel_21d": {"inputs": ["close", "open"], "func": dvel_067_open_to_close_neg_vel_21d},
    "dvel_068_detrended_vel_21d": {"inputs": ["close"], "func": dvel_068_detrended_vel_21d},
    "dvel_069_detrended_vel_63d": {"inputs": ["close"], "func": dvel_069_detrended_vel_63d},
    "dvel_070_vel_slope_21d": {"inputs": ["close"], "func": dvel_070_vel_slope_21d},
    "dvel_071_vel_slope_63d": {"inputs": ["close"], "func": dvel_071_vel_slope_63d},
    "dvel_072_days_to_zero_at_current_vel": {"inputs": ["close"], "func": dvel_072_days_to_zero_at_current_vel},
    "dvel_073_pct_time_in_top_decile_neg_vel_252d": {"inputs": ["close"], "func": dvel_073_pct_time_in_top_decile_neg_vel_252d},
    "dvel_074_vel_consistency_score_63d": {"inputs": ["close"], "func": dvel_074_vel_consistency_score_63d},
    "dvel_075_composite_vel_score": {"inputs": ["close", "high", "low"], "func": dvel_075_composite_vel_score},
}
