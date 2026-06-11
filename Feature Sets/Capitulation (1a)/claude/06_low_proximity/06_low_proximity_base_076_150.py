"""
06_low_proximity — Base Features 076-150
Domain: closeness to trailing minimum, new-low flags, and low-frequency behavior
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Anchors on the trailing LOW, not the high.
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

# --- Group H (076-085): Volatility-normalized proximity to low ---

def lp_076_vol_adj_dist_to_252d_min(close: pd.Series) -> pd.Series:
    """Distance above 252d low divided by 252d realized vol (vol-normalized floor proximity)."""
    m = _rolling_min(close, _TD_YEAR)
    raw = _safe_div(close - m, m)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(raw, vol)


def lp_077_vol_adj_dist_to_63d_min(close: pd.Series) -> pd.Series:
    """Distance above 63d low divided by 63d realized vol."""
    m = _rolling_min(close, _TD_QTR)
    raw = _safe_div(close - m, m)
    vol = _rolling_std(_daily_ret(close), _TD_QTR)
    return _safe_div(raw, vol)


def lp_078_zscore_dist_to_252d_min(close: pd.Series) -> pd.Series:
    """Z-score of (close - 252d min) over trailing 252-day window."""
    dist = close - _rolling_min(close, _TD_YEAR)
    return _zscore_rolling(dist, _TD_YEAR)


def lp_079_zscore_dist_to_63d_min(close: pd.Series) -> pd.Series:
    """Z-score of (close - 63d min) over trailing 63-day window."""
    dist = close - _rolling_min(close, _TD_QTR)
    return _zscore_rolling(dist, _TD_QTR)


def lp_080_pct_rank_dist_to_252d_min(close: pd.Series) -> pd.Series:
    """Percentile rank of (close - 252d min) within trailing 252-day window."""
    dist = close - _rolling_min(close, _TD_YEAR)
    return _rolling_rank_pct(dist, _TD_YEAR)


def lp_081_pct_rank_dist_to_504d_min(close: pd.Series) -> pd.Series:
    """Percentile rank of (close - 504d min) within trailing 504-day window."""
    dist = close - _rolling_min(close, 504)
    return _rolling_rank_pct(dist, 504)


def lp_082_bollinger_pct_b_at_low(close: pd.Series) -> pd.Series:
    """Bollinger %B on 21-day bands — how close the price is to the lower band."""
    ma = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = ma - 2.0 * sd
    upper = ma + 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def lp_083_bollinger_pct_b_63d(close: pd.Series) -> pd.Series:
    """Bollinger %B on 63-day bands (quarterly distance from lower band)."""
    ma = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    lower = ma - 2.0 * sd
    upper = ma + 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def lp_084_bollinger_pct_b_252d(close: pd.Series) -> pd.Series:
    """Bollinger %B on 252-day bands (annual scale lower band proximity)."""
    ma = _rolling_mean(close, _TD_YEAR)
    sd = _rolling_std(close, _TD_YEAR)
    lower = ma - 2.0 * sd
    upper = ma + 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def lp_085_atr_normalized_dist_to_63d_min(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance above 63d close low expressed in 63d ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_QTR)
    m = _rolling_min(close, _TD_QTR)
    return _safe_div(close - m, atr)


# --- Group I (086-096): EWM proximity and smoothed-low distance ---

def lp_086_close_vs_ewm_min_21d(close: pd.Series) -> pd.Series:
    """Close minus EWM (span=21) of rolling 21d min, normalized by EWM min."""
    m = _rolling_min(close, _TD_MON)
    ewm_m = _ewm_mean(m, _TD_MON)
    return _safe_div(close - ewm_m, ewm_m)


def lp_087_close_vs_ewm_min_63d(close: pd.Series) -> pd.Series:
    """Close minus EWM (span=63) of rolling 63d min, normalized by EWM min."""
    m = _rolling_min(close, _TD_QTR)
    ewm_m = _ewm_mean(m, _TD_QTR)
    return _safe_div(close - ewm_m, ewm_m)


def lp_088_close_vs_ewm_min_252d(close: pd.Series) -> pd.Series:
    """Close minus EWM (span=252) of rolling 252d min, normalized by EWM min."""
    m = _rolling_min(close, _TD_YEAR)
    ewm_m = _ewm_mean(m, _TD_YEAR)
    return _safe_div(close - ewm_m, ewm_m)


def lp_089_smoothed_stoch_21d_ewm(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=5) stochastic %K within 21-day range."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    raw = _safe_div(close - l, h - l)
    return raw.ewm(span=_TD_WEEK, min_periods=1).mean()


def lp_090_smoothed_stoch_63d_ewm(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=5) stochastic %K within 63-day range."""
    h = _rolling_max(close, _TD_QTR)
    l = _rolling_min(close, _TD_QTR)
    raw = _safe_div(close - l, h - l)
    return raw.ewm(span=_TD_WEEK, min_periods=1).mean()


def lp_091_min_series_slope_21d(close: pd.Series) -> pd.Series:
    """5-day simple slope of the 21d rolling min series (floor trending down or up)."""
    m = _rolling_min(close, _TD_MON)
    return m.diff(5)


def lp_092_min_series_slope_63d(close: pd.Series) -> pd.Series:
    """5-day simple slope of the 63d rolling min series."""
    m = _rolling_min(close, _TD_QTR)
    return m.diff(5)


def lp_093_min_series_slope_252d(close: pd.Series) -> pd.Series:
    """5-day simple slope of the 252d rolling min series."""
    m = _rolling_min(close, _TD_YEAR)
    return m.diff(5)


def lp_094_min_pct_change_21d(close: pd.Series) -> pd.Series:
    """21-day percent change in the 21d rolling minimum (floor itself declining)."""
    m = _rolling_min(close, _TD_MON)
    return m.pct_change(_TD_MON)


def lp_095_min_pct_change_63d(close: pd.Series) -> pd.Series:
    """63-day percent change in the 63d rolling minimum."""
    m = _rolling_min(close, _TD_QTR)
    return m.pct_change(_TD_QTR)


def lp_096_min_pct_change_252d(close: pd.Series) -> pd.Series:
    """252-day percent change in the 252d rolling minimum (multi-year floor erosion)."""
    m = _rolling_min(close, _TD_YEAR)
    return m.pct_change(_TD_YEAR)


# --- Group J (097-107): Multi-window stochastic ratios and cross-comparisons ---

def lp_097_stoch_ratio_21d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d stochastic to 252d stochastic (recent positioning vs annual)."""
    h21 = _rolling_max(close, _TD_MON)
    l21 = _rolling_min(close, _TD_MON)
    s21 = _safe_div(close - l21, h21 - l21)
    h252 = _rolling_max(close, _TD_YEAR)
    l252 = _rolling_min(close, _TD_YEAR)
    s252 = _safe_div(close - l252, h252 - l252)
    return _safe_div(s21, s252.replace(0, np.nan))


def lp_098_stoch_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d stochastic to 252d stochastic (quarterly vs annual floor position)."""
    h63 = _rolling_max(close, _TD_QTR)
    l63 = _rolling_min(close, _TD_QTR)
    s63 = _safe_div(close - l63, h63 - l63)
    h252 = _rolling_max(close, _TD_YEAR)
    l252 = _rolling_min(close, _TD_YEAR)
    s252 = _safe_div(close - l252, h252 - l252)
    return _safe_div(s63, s252.replace(0, np.nan))


def lp_099_stoch_diff_252d_minus_21d(close: pd.Series) -> pd.Series:
    """252d stochastic minus 21d stochastic (divergence of long-term vs short-term position)."""
    h21 = _rolling_max(close, _TD_MON)
    l21 = _rolling_min(close, _TD_MON)
    s21 = _safe_div(close - l21, h21 - l21)
    h252 = _rolling_max(close, _TD_YEAR)
    l252 = _rolling_min(close, _TD_YEAR)
    s252 = _safe_div(close - l252, h252 - l252)
    return s252 - s21


def lp_100_stoch_weighted_avg_4windows(close: pd.Series) -> pd.Series:
    """Weighted average stochastic: 40%*21d + 30%*63d + 20%*126d + 10%*252d."""
    def _stoch(w):
        h = _rolling_max(close, w)
        l = _rolling_min(close, w)
        return _safe_div(close - l, h - l)
    return 0.40 * _stoch(_TD_MON) + 0.30 * _stoch(_TD_QTR) + 0.20 * _stoch(_TD_HALF) + 0.10 * _stoch(_TD_YEAR)


def lp_101_stoch_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d z-score of 21d stochastic (how extreme the floor hug is historically)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s21 = _safe_div(close - l, h - l)
    return _zscore_rolling(s21, _TD_YEAR)


def lp_102_stoch_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d stochastic over trailing 504-day window."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    return _rolling_rank_pct(s, 504)


def lp_103_stoch_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d stochastic within trailing 252-day window."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    return _rolling_rank_pct(s, _TD_YEAR)


def lp_104_stoch_avg_rolling_min_21d(close: pd.Series) -> pd.Series:
    """21d rolling average of the 21d stochastic (smoothed floor proximity)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    return _rolling_mean(s, _TD_MON)


def lp_105_stoch_63d_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM (span=21) of 63d stochastic (exponentially-weighted floor proximity trend)."""
    h = _rolling_max(close, _TD_QTR)
    l = _rolling_min(close, _TD_QTR)
    s = _safe_div(close - l, h - l)
    return s.ewm(span=_TD_MON, min_periods=1).mean()


def lp_106_stoch_below_20pct_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: 21d stochastic below 20% (near bottom of 1-month range)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    return (s < 0.20).astype(float)


def lp_107_stoch_below_10pct_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: 252d stochastic below 10% (extreme bottom of annual range)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    return (s < 0.10).astype(float)


# --- Group K (108-118): Volume-conditioned low proximity signals ---

def lp_108_vol_weighted_stoch_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 252d stochastic (distress-weighted floor position)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    s = _safe_div(close - l, h - l)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return _rolling_mean(s * vol_norm, _TD_YEAR)


def lp_109_high_vol_new_low_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63d-new-low days with above-average volume in last 63 days."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag_low * high_vol, _TD_QTR)


def lp_110_high_vol_new_low_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 252d-new-low days with above-average volume in last 252 days."""
    flag_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag_low * high_vol, _TD_YEAR)


def lp_111_vol_on_new_low_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on 63d-new-low days as ratio to overall average volume."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_on_lows = _rolling_sum(volume * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return _safe_div(vol_on_lows / count_lows, avg_vol)


def lp_112_vol_on_new_low_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on 252d-new-low days relative to 252d average volume."""
    flag_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_on_lows = _rolling_sum(volume * flag_low, _TD_YEAR)
    count_lows = _rolling_sum(flag_low, _TD_YEAR).replace(0, np.nan)
    return _safe_div(vol_on_lows / count_lows, avg_vol)


def lp_113_vol_at_atl_vs_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on ATL-touch days divided by expanding-avg volume (ATL capitulation intensity)."""
    flag_atl = (close <= close.expanding(min_periods=1).min()).astype(float)
    avg_vol = volume.expanding(min_periods=1).mean()
    return _safe_div(volume * flag_atl, avg_vol)


def lp_114_intraday_range_at_new_lows_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg intraday range (high-low)/close on 63d-new-low days over 63d window."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    range_pct = _safe_div(high - low, close)
    weighted = _rolling_sum(range_pct * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_115_close_to_low_ratio_at_new_lows_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Avg close/low ratio on 63d-new-low days (how much bounce from intraday low at new lows)."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    ratio = _safe_div(close, low)
    weighted = _rolling_sum(ratio * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_116_vol_surge_on_new_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of excess volume (above 252d avg) specifically on 252d-new-low days."""
    flag_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    excess = (volume - avg_vol).clip(lower=0)
    return _rolling_sum(excess * flag_low, _TD_YEAR)


def lp_117_turnover_floor_proximity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume (close * volume) relative to 252d avg when near the 252d floor (within 5%)."""
    m = _rolling_min(close, _TD_YEAR)
    near = (close <= m * 1.05).astype(float)
    dollar_vol = close * volume
    avg_dv = _rolling_mean(dollar_vol, _TD_YEAR)
    return _rolling_sum(_safe_div(dollar_vol, avg_dv) * near, _TD_YEAR)


def lp_118_open_below_prior_low_freq_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days where open gapped below prior day's intraday low (panic opens)."""
    prior_low = low.shift(1)
    gap_down = (open < prior_low).astype(float)
    return _rolling_mean(gap_down, _TD_QTR)


# --- Group L (119-129): Spread and range position at the floor ---

def lp_119_close_minus_open_at_new_lows_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Avg (close - open)/close on 63d-new-low (intraday reversal character at new lows)."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    body = _safe_div(close - open, close)
    weighted = _rolling_sum(body * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_120_lower_shadow_at_new_lows_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Avg lower shadow (min(open,close) - low)/close on 63d-new-low days."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    body_bottom = pd.concat([open, close], axis=1).min(axis=1)
    shadow = _safe_div(body_bottom - low, close)
    weighted = _rolling_sum(shadow * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_121_high_minus_close_at_new_lows_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg upper shadow (high - close)/close on 63d-new-low days (failed bounces at bottom)."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    upper_shadow = _safe_div(high - close, close)
    weighted = _rolling_sum(upper_shadow * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_122_range_compression_at_252d_min(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d avg of (high-low)/close normalized by 252d avg — range compression near floor."""
    daily_range_pct = _safe_div(high - low, close)
    roll21 = _rolling_mean(daily_range_pct, _TD_MON)
    roll252 = _rolling_mean(daily_range_pct, _TD_YEAR)
    return _safe_div(roll21, roll252)


def lp_123_true_range_at_new_lows_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Avg TR on 252d-new-low days relative to 252d avg TR (ATR signature at bottom)."""
    flag_low = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    tr = _tr(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_YEAR)
    tr_norm = _safe_div(tr, avg_tr)
    weighted = _rolling_sum(tr_norm * flag_low, _TD_YEAR)
    count_lows = _rolling_sum(flag_low, _TD_YEAR).replace(0, np.nan)
    return weighted / count_lows


def lp_124_intraday_low_vs_close_min_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of intraday low to 252d close minimum (how far intraday pierces the floor)."""
    m = _rolling_min(close, _TD_YEAR)
    return _safe_div(low, m)


def lp_125_intraday_low_vs_close_min_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of intraday low to 63d close minimum."""
    m = _rolling_min(close, _TD_QTR)
    return _safe_div(low, m)


def lp_126_log_intraday_low_vs_252d_close_min(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log distance of intraday low from 252d close minimum."""
    m = _rolling_min(close, _TD_YEAR)
    return _log_safe(low) - _log_safe(m)


def lp_127_open_close_direction_at_new_lows_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 63d-new-low days that closed UP from the open (reversal after new low)."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    closed_up = (close > open).astype(float)
    both = flag_low * closed_up
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(both, _TD_QTR) / count_lows


def lp_128_new_low_close_to_high_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """On 63d-new-low days: avg (high - close)/(high - low) — wick structure at bottom."""
    flag_low = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    denom = (high - low).replace(0, np.nan)
    metric = _safe_div(high - close, denom)
    weighted = _rolling_sum(metric * flag_low, _TD_QTR)
    count_lows = _rolling_sum(flag_low, _TD_QTR).replace(0, np.nan)
    return weighted / count_lows


def lp_129_stoch_21d_vs_prior_21d_avg(close: pd.Series) -> pd.Series:
    """21d stochastic minus its 21d lagged average (floor hug acceleration signal)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    prior_avg = s.shift(_TD_MON)
    return s - prior_avg


# --- Group M (130-140): Expanding-window all-time low statistics ---

def lp_130_expanding_pct_rank_close(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of close (0 = all-time low, 1 = all-time high)."""
    return close.expanding(min_periods=1).rank(pct=True)


def lp_131_expanding_zscore_close(close: pd.Series) -> pd.Series:
    """Expanding z-score of close (how many expanding SDs below historical mean)."""
    m = close.expanding(min_periods=2).mean()
    sd = close.expanding(min_periods=2).std()
    return _safe_div(close - m, sd)


def lp_132_close_vs_expanding_median(close: pd.Series) -> pd.Series:
    """Percent deviation of close from expanding median (how far below historical center)."""
    med = close.expanding(min_periods=1).median()
    return _safe_div(close - med, med)


def lp_133_close_vs_expanding_q10(close: pd.Series) -> pd.Series:
    """Percent deviation of close from expanding 10th percentile (proximity to historical low tail)."""
    q10 = close.expanding(min_periods=10).quantile(0.10)
    return _safe_div(close - q10, q10)


def lp_134_close_vs_expanding_q05(close: pd.Series) -> pd.Series:
    """Percent deviation of close from expanding 5th percentile (deep tail proximity)."""
    q05 = close.expanding(min_periods=10).quantile(0.05)
    return _safe_div(close - q05, q05)


def lp_135_frac_expanding_at_new_all_time_lows(close: pd.Series) -> pd.Series:
    """Fraction of all history where price was at an all-time low (expanding)."""
    atl = (close <= close.expanding(min_periods=1).min()).astype(float)
    return atl.expanding(min_periods=1).mean()


def lp_136_atl_cluster_window_252d(close: pd.Series) -> pd.Series:
    """Count of all-time-low-touch events within trailing 252 days."""
    flag = (close <= close.expanding(min_periods=1).min()).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lp_137_days_since_atl(close: pd.Series) -> pd.Series:
    """Days since the all-time (expanding) closing low was last set."""
    atl = close.expanding(min_periods=1).min()
    is_atl = (close <= atl)
    result = pd.Series(np.nan, index=close.index)
    last_atl_date = None
    for i, (idx, val) in enumerate(zip(close.index, is_atl)):
        if val:
            last_atl_date = i
        if last_atl_date is not None:
            result.iloc[i] = i - last_atl_date
    return result


def lp_138_log_dist_close_to_expanding_min(close: pd.Series) -> pd.Series:
    """Log distance of close above expanding all-time low (0 at ATL)."""
    m = close.expanding(min_periods=1).min()
    return _log_safe(close) - _log_safe(m)


def lp_139_expanding_min_drawdown_speed(close: pd.Series) -> pd.Series:
    """Rate of change of the expanding minimum itself (how fast the floor is being broken)."""
    m = close.expanding(min_periods=1).min()
    return m.pct_change(_TD_MON)


def lp_140_new_atl_run_length(close: pd.Series) -> pd.Series:
    """Length of the current consecutive run of all-time-low closes (capitulation streak)."""
    atl = close.expanding(min_periods=1).min()
    flag = (close <= atl).astype(int).values
    streak = np.zeros(len(flag), dtype=float)
    cnt = 0
    for i in range(len(flag)):
        if flag[i] == 1:
            cnt += 1
        else:
            cnt = 0
        streak[i] = cnt
    return pd.Series(streak, index=close.index)


# --- Group N (141-150): Composite and miscellaneous low proximity ---

def lp_141_multiwindow_new_low_score_weighted(close: pd.Series) -> pd.Series:
    """Weighted cascade score: 0.10*21d + 0.15*63d + 0.20*126d + 0.25*252d + 0.30*ATL flags."""
    f21 = (close <= _rolling_min(close, _TD_MON)).astype(float)
    f63 = (close <= _rolling_min(close, _TD_QTR)).astype(float)
    f126 = (close <= _rolling_min(close, _TD_HALF)).astype(float)
    f252 = (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    fatl = (close <= close.expanding(min_periods=1).min()).astype(float)
    return 0.10 * f21 + 0.15 * f63 + 0.20 * f126 + 0.25 * f252 + 0.30 * fatl


def lp_142_stoch_inversion_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Binary: 21d stochastic is lower than 252d stochastic (short-term worse than long-term)."""
    h21 = _rolling_max(close, _TD_MON)
    l21 = _rolling_min(close, _TD_MON)
    s21 = _safe_div(close - l21, h21 - l21)
    h252 = _rolling_max(close, _TD_YEAR)
    l252 = _rolling_min(close, _TD_YEAR)
    s252 = _safe_div(close - l252, h252 - l252)
    return (s21 < s252).astype(float)


def lp_143_proximity_ratio_63d_to_expanding(close: pd.Series) -> pd.Series:
    """Ratio of (close - 63d min) to (close - expanding min); near 1 = 63d min == ATL."""
    dist63 = (close - _rolling_min(close, _TD_QTR)).clip(lower=0)
    dist_atl = (close - close.expanding(min_periods=1).min()).clip(lower=0)
    return _safe_div(dist63, dist_atl.replace(0, np.nan))


def lp_144_floor_break_count_expanding(close: pd.Series) -> pd.Series:
    """Total number of times close has made a new all-time low (expanding, running count)."""
    atl = close.expanding(min_periods=1).min()
    flag = (close <= atl).astype(float)
    return flag.expanding(min_periods=1).sum()


def lp_145_frac_days_near_atl_504d(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days where close was within 10% of the expanding all-time low."""
    m = close.expanding(min_periods=1).min()
    near = (close <= m * 1.10).astype(float)
    return _rolling_mean(near, 504)


def lp_146_stoch_21d_below_5pct_days_252d(close: pd.Series) -> pd.Series:
    """Count of days in last 252 where 21d stochastic was below 5% (extreme floor hugging)."""
    h = _rolling_max(close, _TD_MON)
    l = _rolling_min(close, _TD_MON)
    s = _safe_div(close - l, h - l)
    below5 = (s < 0.05).astype(float)
    return _rolling_sum(below5, _TD_YEAR)


def lp_147_min_to_max_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252d trailing minimum to 252d trailing maximum (compression near floor)."""
    mn = _rolling_min(close, _TD_YEAR)
    mx = _rolling_max(close, _TD_YEAR)
    return _safe_div(mn, mx)


def lp_148_close_below_expanding_q20(close: pd.Series) -> pd.Series:
    """Binary: close is below expanding 20th percentile (historically cheap zone)."""
    q20 = close.expanding(min_periods=10).quantile(0.20)
    return (close < q20).astype(float)


def lp_149_days_since_63d_min(close: pd.Series) -> pd.Series:
    """Days since the 63d trailing minimum was last set (freshness of quarterly floor)."""
    def _last_min_age(x):
        if len(x) == 0:
            return np.nan
        pos = int(np.argmin(x))
        return float(len(x) - 1 - pos)
    return close.rolling(_TD_QTR, min_periods=1).apply(_last_min_age, raw=True)


def lp_150_composite_floor_intensity(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: new-low cascade score * intraday-floor-touch density * volume ratio."""
    cascade = (
        (close <= _rolling_min(close, _TD_MON)).astype(float) +
        (close <= _rolling_min(close, _TD_QTR)).astype(float) +
        (close <= _rolling_min(close, _TD_YEAR)).astype(float)
    ) / 3.0
    m = _rolling_min(close, _TD_YEAR)
    density = (low <= m * 1.03).astype(float)
    vol_ratio = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return cascade * _rolling_mean(density, _TD_MON) * vol_ratio


# ── Registry ──────────────────────────────────────────────────────────────────

LOW_PROXIMITY_REGISTRY_076_150 = {
    "lp_076_vol_adj_dist_to_252d_min": {"inputs": ["close"], "func": lp_076_vol_adj_dist_to_252d_min},
    "lp_077_vol_adj_dist_to_63d_min": {"inputs": ["close"], "func": lp_077_vol_adj_dist_to_63d_min},
    "lp_078_zscore_dist_to_252d_min": {"inputs": ["close"], "func": lp_078_zscore_dist_to_252d_min},
    "lp_079_zscore_dist_to_63d_min": {"inputs": ["close"], "func": lp_079_zscore_dist_to_63d_min},
    "lp_080_pct_rank_dist_to_252d_min": {"inputs": ["close"], "func": lp_080_pct_rank_dist_to_252d_min},
    "lp_081_pct_rank_dist_to_504d_min": {"inputs": ["close"], "func": lp_081_pct_rank_dist_to_504d_min},
    "lp_082_bollinger_pct_b_at_low": {"inputs": ["close"], "func": lp_082_bollinger_pct_b_at_low},
    "lp_083_bollinger_pct_b_63d": {"inputs": ["close"], "func": lp_083_bollinger_pct_b_63d},
    "lp_084_bollinger_pct_b_252d": {"inputs": ["close"], "func": lp_084_bollinger_pct_b_252d},
    "lp_085_atr_normalized_dist_to_63d_min": {"inputs": ["close", "high", "low"], "func": lp_085_atr_normalized_dist_to_63d_min},
    "lp_086_close_vs_ewm_min_21d": {"inputs": ["close"], "func": lp_086_close_vs_ewm_min_21d},
    "lp_087_close_vs_ewm_min_63d": {"inputs": ["close"], "func": lp_087_close_vs_ewm_min_63d},
    "lp_088_close_vs_ewm_min_252d": {"inputs": ["close"], "func": lp_088_close_vs_ewm_min_252d},
    "lp_089_smoothed_stoch_21d_ewm": {"inputs": ["close"], "func": lp_089_smoothed_stoch_21d_ewm},
    "lp_090_smoothed_stoch_63d_ewm": {"inputs": ["close"], "func": lp_090_smoothed_stoch_63d_ewm},
    "lp_091_min_series_slope_21d": {"inputs": ["close"], "func": lp_091_min_series_slope_21d},
    "lp_092_min_series_slope_63d": {"inputs": ["close"], "func": lp_092_min_series_slope_63d},
    "lp_093_min_series_slope_252d": {"inputs": ["close"], "func": lp_093_min_series_slope_252d},
    "lp_094_min_pct_change_21d": {"inputs": ["close"], "func": lp_094_min_pct_change_21d},
    "lp_095_min_pct_change_63d": {"inputs": ["close"], "func": lp_095_min_pct_change_63d},
    "lp_096_min_pct_change_252d": {"inputs": ["close"], "func": lp_096_min_pct_change_252d},
    "lp_097_stoch_ratio_21d_to_252d": {"inputs": ["close"], "func": lp_097_stoch_ratio_21d_to_252d},
    "lp_098_stoch_ratio_63d_to_252d": {"inputs": ["close"], "func": lp_098_stoch_ratio_63d_to_252d},
    "lp_099_stoch_diff_252d_minus_21d": {"inputs": ["close"], "func": lp_099_stoch_diff_252d_minus_21d},
    "lp_100_stoch_weighted_avg_4windows": {"inputs": ["close"], "func": lp_100_stoch_weighted_avg_4windows},
    "lp_101_stoch_21d_zscore_252d": {"inputs": ["close"], "func": lp_101_stoch_21d_zscore_252d},
    "lp_102_stoch_252d_pct_rank_504d": {"inputs": ["close"], "func": lp_102_stoch_252d_pct_rank_504d},
    "lp_103_stoch_21d_pct_rank_252d": {"inputs": ["close"], "func": lp_103_stoch_21d_pct_rank_252d},
    "lp_104_stoch_avg_rolling_min_21d": {"inputs": ["close"], "func": lp_104_stoch_avg_rolling_min_21d},
    "lp_105_stoch_63d_ewm_21d": {"inputs": ["close"], "func": lp_105_stoch_63d_ewm_21d},
    "lp_106_stoch_below_20pct_flag_21d": {"inputs": ["close"], "func": lp_106_stoch_below_20pct_flag_21d},
    "lp_107_stoch_below_10pct_flag_252d": {"inputs": ["close"], "func": lp_107_stoch_below_10pct_flag_252d},
    "lp_108_vol_weighted_stoch_252d": {"inputs": ["close", "volume"], "func": lp_108_vol_weighted_stoch_252d},
    "lp_109_high_vol_new_low_count_63d": {"inputs": ["close", "volume"], "func": lp_109_high_vol_new_low_count_63d},
    "lp_110_high_vol_new_low_count_252d": {"inputs": ["close", "volume"], "func": lp_110_high_vol_new_low_count_252d},
    "lp_111_vol_on_new_low_days_63d": {"inputs": ["close", "volume"], "func": lp_111_vol_on_new_low_days_63d},
    "lp_112_vol_on_new_low_days_252d": {"inputs": ["close", "volume"], "func": lp_112_vol_on_new_low_days_252d},
    "lp_113_vol_at_atl_vs_avg": {"inputs": ["close", "volume"], "func": lp_113_vol_at_atl_vs_avg},
    "lp_114_intraday_range_at_new_lows_63d": {"inputs": ["close", "high", "low"], "func": lp_114_intraday_range_at_new_lows_63d},
    "lp_115_close_to_low_ratio_at_new_lows_63d": {"inputs": ["close", "low"], "func": lp_115_close_to_low_ratio_at_new_lows_63d},
    "lp_116_vol_surge_on_new_low_252d": {"inputs": ["close", "volume"], "func": lp_116_vol_surge_on_new_low_252d},
    "lp_117_turnover_floor_proximity_252d": {"inputs": ["close", "volume"], "func": lp_117_turnover_floor_proximity_252d},
    "lp_118_open_below_prior_low_freq_63d": {"inputs": ["close", "open", "low"], "func": lp_118_open_below_prior_low_freq_63d},
    "lp_119_close_minus_open_at_new_lows_63d": {"inputs": ["close", "open", "low"], "func": lp_119_close_minus_open_at_new_lows_63d},
    "lp_120_lower_shadow_at_new_lows_63d": {"inputs": ["close", "open", "low"], "func": lp_120_lower_shadow_at_new_lows_63d},
    "lp_121_high_minus_close_at_new_lows_63d": {"inputs": ["close", "high", "low"], "func": lp_121_high_minus_close_at_new_lows_63d},
    "lp_122_range_compression_at_252d_min": {"inputs": ["close", "high", "low"], "func": lp_122_range_compression_at_252d_min},
    "lp_123_true_range_at_new_lows_252d": {"inputs": ["close", "high", "low"], "func": lp_123_true_range_at_new_lows_252d},
    "lp_124_intraday_low_vs_close_min_252d": {"inputs": ["close", "low"], "func": lp_124_intraday_low_vs_close_min_252d},
    "lp_125_intraday_low_vs_close_min_63d": {"inputs": ["close", "low"], "func": lp_125_intraday_low_vs_close_min_63d},
    "lp_126_log_intraday_low_vs_252d_close_min": {"inputs": ["close", "low"], "func": lp_126_log_intraday_low_vs_252d_close_min},
    "lp_127_open_close_direction_at_new_lows_63d": {"inputs": ["close", "open", "low"], "func": lp_127_open_close_direction_at_new_lows_63d},
    "lp_128_new_low_close_to_high_ratio_63d": {"inputs": ["close", "high", "low"], "func": lp_128_new_low_close_to_high_ratio_63d},
    "lp_129_stoch_21d_vs_prior_21d_avg": {"inputs": ["close"], "func": lp_129_stoch_21d_vs_prior_21d_avg},
    "lp_130_expanding_pct_rank_close": {"inputs": ["close"], "func": lp_130_expanding_pct_rank_close},
    "lp_131_expanding_zscore_close": {"inputs": ["close"], "func": lp_131_expanding_zscore_close},
    "lp_132_close_vs_expanding_median": {"inputs": ["close"], "func": lp_132_close_vs_expanding_median},
    "lp_133_close_vs_expanding_q10": {"inputs": ["close"], "func": lp_133_close_vs_expanding_q10},
    "lp_134_close_vs_expanding_q05": {"inputs": ["close"], "func": lp_134_close_vs_expanding_q05},
    "lp_135_frac_expanding_at_new_all_time_lows": {"inputs": ["close"], "func": lp_135_frac_expanding_at_new_all_time_lows},
    "lp_136_atl_cluster_window_252d": {"inputs": ["close"], "func": lp_136_atl_cluster_window_252d},
    "lp_137_days_since_atl": {"inputs": ["close"], "func": lp_137_days_since_atl},
    "lp_138_log_dist_close_to_expanding_min": {"inputs": ["close"], "func": lp_138_log_dist_close_to_expanding_min},
    "lp_139_expanding_min_drawdown_speed": {"inputs": ["close"], "func": lp_139_expanding_min_drawdown_speed},
    "lp_140_new_atl_run_length": {"inputs": ["close"], "func": lp_140_new_atl_run_length},
    "lp_141_multiwindow_new_low_score_weighted": {"inputs": ["close"], "func": lp_141_multiwindow_new_low_score_weighted},
    "lp_142_stoch_inversion_21d_vs_252d": {"inputs": ["close"], "func": lp_142_stoch_inversion_21d_vs_252d},
    "lp_143_proximity_ratio_63d_to_expanding": {"inputs": ["close"], "func": lp_143_proximity_ratio_63d_to_expanding},
    "lp_144_floor_break_count_expanding": {"inputs": ["close"], "func": lp_144_floor_break_count_expanding},
    "lp_145_frac_days_near_atl_504d": {"inputs": ["close"], "func": lp_145_frac_days_near_atl_504d},
    "lp_146_stoch_21d_below_5pct_days_252d": {"inputs": ["close"], "func": lp_146_stoch_21d_below_5pct_days_252d},
    "lp_147_min_to_max_ratio_252d": {"inputs": ["close"], "func": lp_147_min_to_max_ratio_252d},
    "lp_148_close_below_expanding_q20": {"inputs": ["close"], "func": lp_148_close_below_expanding_q20},
    "lp_149_days_since_63d_min": {"inputs": ["close"], "func": lp_149_days_since_63d_min},
    "lp_150_composite_floor_intensity": {"inputs": ["close", "low", "volume"], "func": lp_150_composite_floor_intensity},
}
