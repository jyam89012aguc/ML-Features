"""
17_volume_climax — Base Features 076-200
Domain: single-day extreme volume events — the largest volume day(s) in trailing windows,
their magnitude vs all other days, days-since the extreme event, whether today IS the
extreme day, the #1-vs-#2 volume gap, and climax-day price action (wide-range down bar).
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _days_since_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars since the rolling-window maximum occurred."""
    def _dsm(arr):
        idx = int(np.argmax(arr))
        return float(len(arr) - 1 - idx)
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_dsm, raw=True)


def _rolling_second_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling second-largest value over trailing w periods."""
    def _s2(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        return float(top2[0])
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_s2, raw=True)


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-087): Climax-day open/gap and intraday structure ---

def vcx_076_climax_day_gap_up_63d(close: pd.Series, open: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Gap (open/prior_close - 1) on the 63-day peak-volume day."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return gap.where(is_climax, np.nan).ffill()


def vcx_077_climax_day_gap_up_252d(close: pd.Series, open: pd.Series,
                                    volume: pd.Series) -> pd.Series:
    """Gap (open/prior_close - 1) on the 252-day peak-volume day."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return gap.where(is_climax, np.nan).ffill()


def vcx_078_climax_day_open_to_close_63d(close: pd.Series, open: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """Open-to-close return on the 63-day peak-volume day."""
    otc = _safe_div(close - open, open)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return otc.where(is_climax, np.nan).ffill()


def vcx_079_climax_day_open_to_close_252d(close: pd.Series, open: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Open-to-close return on the 252-day peak-volume day."""
    otc = _safe_div(close - open, open)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return otc.where(is_climax, np.nan).ffill()


def vcx_080_climax_day_upper_wick_norm_63d(high: pd.Series, close: pd.Series, open: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Upper wick (high - max(open,close)) normalized by range on 63-day climax day."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    rng = (high - pd.concat([open, close], axis=1).min(axis=1)).replace(0, np.nan)
    upper_wick = _safe_div(high - body_top, rng)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return upper_wick.where(is_climax, np.nan).ffill()


def vcx_081_climax_day_lower_wick_norm_63d(low: pd.Series, close: pd.Series, open: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Lower wick (min(open,close) - low) normalized by range on 63-day climax day."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    rng = (pd.concat([open, close], axis=1).max(axis=1) - low).replace(0, np.nan)
    lower_wick = _safe_div(body_bot - low, rng)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return lower_wick.where(is_climax, np.nan).ffill()


def vcx_082_climax_day_body_pct_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                     open: pd.Series, volume: pd.Series) -> pd.Series:
    """Body size as fraction of total range on 63-day climax day."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    body_frac = _safe_div(body, rng)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return body_frac.where(is_climax, np.nan).ffill()


def vcx_083_climax_day_body_pct_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                      open: pd.Series, volume: pd.Series) -> pd.Series:
    """Body size as fraction of total range on 252-day climax day."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    body_frac = _safe_div(body, rng)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return body_frac.where(is_climax, np.nan).ffill()


def vcx_084_climax_down_bar_magnitude_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Return on 63-day climax day if negative, else 0 (signed down-bar magnitude)."""
    ret = close.pct_change(1)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    val = ret.where(ret < 0, 0.0)
    return val.where(is_climax, np.nan).ffill()


def vcx_085_climax_down_bar_magnitude_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Return on 252-day climax day if negative, else 0."""
    ret = close.pct_change(1)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    val = ret.where(ret < 0, 0.0)
    return val.where(is_climax, np.nan).ffill()


def vcx_086_climax_bear_candle_score_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                          open: pd.Series, volume: pd.Series) -> pd.Series:
    """Bear candle score on 63-day climax day: negative return * range / close."""
    ret = close.pct_change(1).clip(upper=0)
    rng = _safe_div(high - low, close.shift(1))
    score = ret.abs() * rng
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return score.where(is_climax, np.nan).ffill()


def vcx_087_climax_bear_candle_score_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                           open: pd.Series, volume: pd.Series) -> pd.Series:
    """Bear candle score on 252-day climax day: abs(neg return) * normalized range."""
    ret = close.pct_change(1).clip(upper=0)
    rng = _safe_div(high - low, close.shift(1))
    score = ret.abs() * rng
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return score.where(is_climax, np.nan).ffill()


# --- Group H (088-100): Post-climax price behavior and follow-through ---

def vcx_088_return_1d_after_climax_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Next-day return after the 63-day peak-volume day (carried forward)."""
    ret = close.pct_change(1)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    climax_ret = ret.where(is_climax, np.nan)
    return climax_ret.shift(1).ffill()


def vcx_089_return_5d_after_climax_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day cumulative return starting the day after 63-day climax (held forward)."""
    ret5 = close.pct_change(_TD_WEEK)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    val = ret5.where(is_climax, np.nan).shift(1)
    return val.ffill()


def vcx_090_close_vs_climax_close_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's close relative to the 21-day peak-volume day's close."""
    mx_vol = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx_vol)
    climax_close = close.where(is_climax, np.nan).ffill()
    return _safe_div(close, climax_close) - 1.0


def vcx_091_close_vs_climax_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's close relative to the 63-day peak-volume day's close."""
    mx_vol = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx_vol)
    climax_close = close.where(is_climax, np.nan).ffill()
    return _safe_div(close, climax_close) - 1.0


def vcx_092_close_vs_climax_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's close relative to the 252-day peak-volume day's close."""
    mx_vol = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx_vol)
    climax_close = close.where(is_climax, np.nan).ffill()
    return _safe_div(close, climax_close) - 1.0


def vcx_093_close_below_climax_close_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's close is below the 63-day climax day's close."""
    return (vcx_091_close_vs_climax_close_63d(close, volume) < 0).astype(float)


def vcx_094_close_below_climax_close_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today's close is below the 252-day climax day's close."""
    return (vcx_092_close_vs_climax_close_252d(close, volume) < 0).astype(float)


def vcx_095_climax_low_today_vs_climax_day_low_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's low relative to the intraday low of the 63-day climax day."""
    mx_vol = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx_vol)
    climax_low = low.where(is_climax, np.nan).ffill()
    return _safe_div(low, climax_low) - 1.0


def vcx_096_climax_low_today_vs_climax_day_low_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's low relative to the intraday low of the 252-day climax day."""
    mx_vol = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx_vol)
    climax_low = low.where(is_climax, np.nan).ffill()
    return _safe_div(low, climax_low) - 1.0


def vcx_097_max_drawdown_from_climax_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max drawdown from 63-day climax day's close to rolling min of subsequent closes."""
    mx_vol = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx_vol)
    climax_close = close.where(is_climax, np.nan).ffill()
    min_since = close.rolling(_TD_QTR, min_periods=1).min()
    return _safe_div(min_since - climax_close, climax_close)


def vcx_098_max_drawdown_from_climax_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max drawdown from 252-day climax day's close to rolling min of subsequent closes."""
    mx_vol = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx_vol)
    climax_close = close.where(is_climax, np.nan).ffill()
    min_since = close.rolling(_TD_YEAR, min_periods=1).min()
    return _safe_div(min_since - climax_close, climax_close)


def vcx_099_vol_ratio_today_vs_climax_63d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of the 63-day peak volume (fading from climax)."""
    mx = _rolling_max(volume, _TD_QTR)
    return _safe_div(volume, mx)


def vcx_100_vol_ratio_today_vs_climax_252d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of the 252-day peak volume."""
    mx = _rolling_max(volume, _TD_YEAR)
    return _safe_div(volume, mx)


# --- Group I (101-112): Climax vs ATR/true-range context ---

def vcx_101_climax_day_tr_vs_atr14_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """True range on 63-day climax day divided by 14-day ATR (range extremity)."""
    tr = _tr(close, high, low)
    atr14 = _rolling_mean(tr, 14)
    tr_norm = _safe_div(tr, atr14)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return tr_norm.where(is_climax, np.nan).ffill()


def vcx_102_climax_day_tr_vs_atr14_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """True range on 252-day climax day divided by 14-day ATR."""
    tr = _tr(close, high, low)
    atr14 = _rolling_mean(tr, 14)
    tr_norm = _safe_div(tr, atr14)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return tr_norm.where(is_climax, np.nan).ffill()


def vcx_103_max_vol_day_atr_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """21-day rolling max of (true_range / atr14) weighted to peak-volume days."""
    tr = _tr(close, high, low)
    atr14 = _rolling_mean(tr, 14)
    tr_norm = _safe_div(tr, atr14)
    vol_weight = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_max(tr_norm * vol_weight, _TD_MON)


def vcx_104_climax_day_vol_x_range_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Volume times normalized range on 63-day climax day (liquidity force)."""
    rng = _safe_div(high - low, close.shift(1))
    force = volume * rng
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return force.where(is_climax, np.nan).ffill()


def vcx_105_climax_day_vol_x_range_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Volume times normalized range on 252-day climax day."""
    rng = _safe_div(high - low, close.shift(1))
    force = volume * rng
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return force.where(is_climax, np.nan).ffill()


def vcx_106_climax_vol_force_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Percentile rank of volume*range on peak-volume day within 252-day distribution."""
    rng = _safe_div(high - low, close.shift(1))
    force = volume * rng
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    climax_force = force.where(is_climax, np.nan).ffill()
    return climax_force.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcx_107_days_since_max_vol_day_high_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since the 63-day peak-volume day's intraday high was set."""
    mx_vol = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx_vol)
    climax_high = high.where(is_climax, np.nan).ffill()
    return (high < climax_high).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def vcx_108_days_since_max_vol_day_low_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since the 63-day peak-volume day's intraday low was set."""
    mx_vol = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx_vol)
    climax_low = low.where(is_climax, np.nan).ffill()
    return (low > climax_low).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def vcx_109_climax_day_ret_x_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Return times volume on 63-day climax day (signed price-force)."""
    ret = close.pct_change(1)
    pf = ret * volume
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return pf.where(is_climax, np.nan).ffill()


def vcx_110_climax_day_ret_x_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Return times volume on 252-day climax day (signed price-force)."""
    ret = close.pct_change(1)
    pf = ret * volume
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return pf.where(is_climax, np.nan).ffill()


def vcx_111_climax_day_ret_x_vol_norm_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax day return*volume normalized by 63-day mean volume."""
    ret = close.pct_change(1)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    pf_norm = _safe_div(ret * volume, avg_vol)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return pf_norm.where(is_climax, np.nan).ffill()


def vcx_112_climax_day_ret_x_vol_norm_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax day return*volume normalized by 252-day mean volume."""
    ret = close.pct_change(1)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    pf_norm = _safe_div(ret * volume, avg_vol)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return pf_norm.where(is_climax, np.nan).ffill()


# --- Group J (113-125): Climax count frequency and cluster detection ---

def vcx_113_climax_count_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63 days where volume set a new 21-day max."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    return is_climax.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def vcx_114_climax_count_in_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252 days where volume set a new 21-day max."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    return is_climax.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def vcx_115_climax_frequency_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days that had volume above the 63-day 90th percentile."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.9)
    above = (volume >= p90).astype(float)
    return above.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vcx_116_days_between_climax_events_63d(volume: pd.Series) -> pd.Series:
    """Average days between consecutive new-21d-max-volume events in trailing 63 days."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    count = is_climax.rolling(_TD_QTR, min_periods=1).sum().replace(0, np.nan)
    return _safe_div(pd.Series(_TD_QTR, index=volume.index, dtype=float), count)


def vcx_117_recent_climax_cluster_5d(volume: pd.Series) -> pd.Series:
    """Count of 21d-max-volume days occurring within the trailing 5 days."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    return is_climax.rolling(_TD_WEEK, min_periods=1).sum()


def vcx_118_recent_climax_cluster_21d(volume: pd.Series) -> pd.Series:
    """Count of 63d-max-volume days occurring within the trailing 21 days."""
    is_climax = (volume >= _rolling_max(volume, _TD_QTR)).astype(float)
    return is_climax.rolling(_TD_MON, min_periods=1).sum()


def vcx_119_climax_vol_avg_over_63d_events(volume: pd.Series) -> pd.Series:
    """Average volume on the days that set new 63-day max volume, trailing 252 days."""
    is_climax = volume >= _rolling_max(volume, _TD_QTR)
    climax_vol = volume.where(is_climax, np.nan)
    return climax_vol.rolling(_TD_YEAR, min_periods=1).mean()


def vcx_120_time_since_last_climax_63d_event(volume: pd.Series) -> pd.Series:
    """Days since the most recent day that set a new 63-day max volume."""
    is_climax = (volume >= _rolling_max(volume, _TD_QTR)).astype(float)
    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return is_climax.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)


def vcx_121_climax_beat_prior_climax_flag_252d(volume: pd.Series) -> pd.Series:
    """Flag: today's volume exceeds the previous 252-day max (new all-window climax)."""
    prior_max = volume.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return (volume > prior_max).astype(float)


def vcx_122_expanding_climax_beat_count(volume: pd.Series) -> pd.Series:
    """Expanding count of days where volume set a new all-time high."""
    prior_max = volume.shift(1).expanding(min_periods=1).max()
    return (volume > prior_max).astype(float).expanding(min_periods=1).sum()


def vcx_123_climax_days_pct_of_63d_window(volume: pd.Series) -> pd.Series:
    """Fraction of 63-day window where volume exceeded the window's 75th percentile."""
    p75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    above = (volume >= p75).astype(float)
    return above.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vcx_124_climax_days_pct_of_252d_window(volume: pd.Series) -> pd.Series:
    """Fraction of 252-day window where volume exceeded the window's 90th percentile."""
    p90 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.9)
    above = (volume >= p90).astype(float)
    return above.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vcx_125_two_climax_days_within_21d_flag(volume: pd.Series) -> pd.Series:
    """Flag: at least 2 days in last 21 days hit 63-day max volume level."""
    is_climax = (volume >= _rolling_max(volume, _TD_QTR)).astype(float)
    return (is_climax.rolling(_TD_MON, min_periods=1).sum() >= 2).astype(float)


# --- Group K (126-138): Composite and cross-dimension climax signals ---

def vcx_126_climax_vol_x_down_ret_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(volume * abs(negative_return)) day in 63-day window (worst panic score)."""
    ret = close.pct_change(1).clip(upper=0).abs()
    score = volume * ret
    return _rolling_max(score, _TD_QTR)


def vcx_127_climax_vol_x_down_ret_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(volume * abs(negative_return)) day in 252-day window."""
    ret = close.pct_change(1).clip(upper=0).abs()
    score = volume * ret
    return _rolling_max(score, _TD_YEAR)


def vcx_128_climax_vol_x_range_max_63d(high: pd.Series, low: pd.Series, close: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Max of volume*(high-low)/close in trailing 63 days (force magnitude)."""
    rng = _safe_div(high - low, close.shift(1))
    force = volume * rng
    return _rolling_max(force, _TD_QTR)


def vcx_129_climax_vol_x_range_max_252d(high: pd.Series, low: pd.Series, close: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Max of volume*(high-low)/close in trailing 252 days."""
    rng = _safe_div(high - low, close.shift(1))
    force = volume * rng
    return _rolling_max(force, _TD_YEAR)


def vcx_130_climax_vol_share_top3_63d(volume: pd.Series) -> pd.Series:
    """Sum of top-3 volume days as fraction of total 63-day volume."""
    def _top3_sum(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].sum())
    top3 = volume.rolling(_TD_QTR, min_periods=3).apply(_top3_sum, raw=True)
    total = _rolling_sum(volume, _TD_QTR)
    return _safe_div(top3, total)


def vcx_131_climax_vol_share_top3_252d(volume: pd.Series) -> pd.Series:
    """Sum of top-3 volume days as fraction of total 252-day volume."""
    def _top3_sum(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].sum())
    top3 = volume.rolling(_TD_YEAR, min_periods=3).apply(_top3_sum, raw=True)
    total = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(top3, total)


def vcx_132_vol_concentration_herfindahl_21d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares in trailing 21 days (climax concentration)."""
    total = _rolling_sum(volume, _TD_MON)
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)


def vcx_133_vol_concentration_herfindahl_63d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares in trailing 63 days."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)


def vcx_134_vol_max_over_total_trend_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of (daily_vol / 21d_mean_vol) share over 63-day window."""
    share = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _linslope(share, _TD_QTR)


def vcx_135_climax_combined_score_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """Combined: peak-vol-multiple * range * abs(return) on 63-day climax day."""
    ret = close.pct_change(1).abs()
    rng = _safe_div(high - low, close.shift(1))
    mult = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    score = mult * rng * ret
    return score.where(is_climax, np.nan).ffill()


def vcx_136_climax_combined_score_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Combined: peak-vol-multiple * range * abs(return) on 252-day climax day."""
    ret = close.pct_change(1).abs()
    rng = _safe_div(high - low, close.shift(1))
    mult = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    score = mult * rng * ret
    return score.where(is_climax, np.nan).ffill()


def vcx_137_max_vol_day_was_down_close_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling max of (down_close_flag) on the 21-day peak-volume day."""
    ret = close.pct_change(1)
    is_climax = (volume >= _rolling_max(volume, _TD_MON))
    down_climax = (is_climax & (ret < 0)).astype(float)
    return down_climax.rolling(_TD_MON, min_periods=1).max()


def vcx_138_max_vol_day_was_down_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling max of (down_close_flag) on the 63-day peak-volume day."""
    ret = close.pct_change(1)
    is_climax = (volume >= _rolling_max(volume, _TD_QTR))
    down_climax = (is_climax & (ret < 0)).astype(float)
    return down_climax.rolling(_TD_QTR, min_periods=1).max()


# --- Group L (139-150): Climax relative to moving averages and long-run norms ---

def vcx_139_max_vol_21d_vs_ewm63(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day peak volume to 63-day EMA of volume."""
    return _safe_div(_rolling_max(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))


def vcx_140_max_vol_63d_vs_ewm126(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day peak volume to 126-day EMA of volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _ewm_mean(volume, _TD_HALF))


def vcx_141_max_vol_252d_vs_ewm252(volume: pd.Series) -> pd.Series:
    """Ratio of 252-day peak volume to 252-day EMA of volume."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _ewm_mean(volume, _TD_YEAR))


def vcx_142_days_since_vol_above_2x_mean_252d(volume: pd.Series) -> pd.Series:
    """Days since volume last exceeded 2x the 63-day mean (extreme climax threshold)."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above2x = (volume >= 2.0 * mean63).astype(float)
    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return above2x.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)


def vcx_143_days_since_vol_above_3x_mean_252d(volume: pd.Series) -> pd.Series:
    """Days since volume last exceeded 3x the 63-day mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above3x = (volume >= 3.0 * mean63).astype(float)
    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return above3x.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)


def vcx_144_climax_vol_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of today's volume vs all history (absolute extremity)."""
    m = volume.expanding(min_periods=5).mean()
    s = volume.expanding(min_periods=5).std()
    return _safe_div(volume - m, s)


def vcx_145_max_vol_21d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day peak volume."""
    mx21 = _rolling_max(volume, _TD_MON)
    return mx21.expanding(min_periods=5).rank(pct=True)


def vcx_146_max_vol_252d_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day peak volume (how record-level is the climax)."""
    mx252 = _rolling_max(volume, _TD_YEAR)
    return mx252.expanding(min_periods=5).rank(pct=True)


def vcx_147_climax_vol_mean_ratio_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of (vol / 21d_mean_vol) ratio over trailing 63 days."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _linslope(ratio, _TD_QTR)


def vcx_148_climax_recency_x_magnitude_63d(volume: pd.Series) -> pd.Series:
    """Recency score * climax magnitude multiple (recent large climax = high score)."""
    recency = (1.0 - _days_since_max(volume, _TD_QTR) / _TD_QTR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return recency * magnitude


def vcx_149_climax_recency_x_magnitude_252d(volume: pd.Series) -> pd.Series:
    """Recency score * climax magnitude multiple for 252-day window."""
    recency = (1.0 - _days_since_max(volume, _TD_YEAR) / _TD_YEAR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    return recency * magnitude


def vcx_150_climax_distress_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (climax_magnitude_252d) * (recency_252d) * (down_return_flag on climax)."""
    magnitude = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    recency = (1.0 - _days_since_max(volume, _TD_YEAR) / _TD_YEAR).clip(lower=0.0)
    ret = close.pct_change(1)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    down_flag = (is_climax & (ret < 0)).astype(float)
    carried_down = down_flag.where(is_climax, np.nan).ffill().fillna(0.0)
    return magnitude * recency * (0.5 + 0.5 * carried_down)


# --- Group M (176-200): Additional climax context features ---

def vcx_176_climax_day_close_vs_high_63d(high: pd.Series, close: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """(close - high) / high on the 63-day peak-volume day (close below intraday high)."""
    ratio = _safe_div(close - high, high)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return ratio.where(is_climax, np.nan).ffill()


def vcx_177_climax_day_close_vs_high_252d(high: pd.Series, close: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """(close - high) / high on the 252-day peak-volume day."""
    ratio = _safe_div(close - high, high)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return ratio.where(is_climax, np.nan).ffill()


def vcx_178_climax_day_vol_normalized_by_expanding_mean(volume: pd.Series) -> pd.Series:
    """Peak-volume day's volume divided by expanding mean at time of climax (historical extremity)."""
    exp_mean = volume.expanding(min_periods=5).mean()
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    norm = _safe_div(volume, exp_mean)
    return norm.where(is_climax, np.nan).ffill()


def vcx_179_vol_above_p95_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume exceeded the 95th percentile."""
    p95 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    return (volume >= p95).astype(float).rolling(_TD_YEAR, min_periods=1).sum()


def vcx_180_vol_above_p99_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume exceeded the 99th percentile."""
    p99 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.99)
    return (volume >= p99).astype(float).rolling(_TD_YEAR, min_periods=1).sum()


def vcx_181_max_vol_21d_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day peak volume to 252-day median volume (short climax vs long norm)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_median(volume, _TD_YEAR))


def vcx_182_max_vol_63d_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day peak volume to 252-day median volume."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_YEAR))


def vcx_183_vol_rolling_max_drawdown_21d(volume: pd.Series) -> pd.Series:
    """Max proportional drop from rolling 21-day peak to trailing min (climax fade)."""
    mx21 = _rolling_max(volume, _TD_MON)
    mn21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return _safe_div(mn21 - mx21, mx21)


def vcx_184_vol_rolling_max_drawdown_63d(volume: pd.Series) -> pd.Series:
    """Max proportional drop from rolling 63-day peak to trailing min."""
    mx63 = _rolling_max(volume, _TD_QTR)
    mn63 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return _safe_div(mn63 - mx63, mx63)


def vcx_185_vol_std_normalized_by_max_21d(volume: pd.Series) -> pd.Series:
    """Rolling 21-day std of volume divided by 21-day max (dispersion vs peak)."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_max(volume, _TD_MON))


def vcx_186_vol_std_normalized_by_max_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day std of volume divided by 63-day max."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_max(volume, _TD_QTR))


def vcx_187_climax_day_ret_vs_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """Climax day return divided by 21-day ATR (return size vs recent volatility)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    ret = close.pct_change(1)
    ret_vs_atr = _safe_div(ret, _safe_div(atr21, close.shift(1)))
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return ret_vs_atr.where(is_climax, np.nan).ffill()


def vcx_188_climax_count_down_bar_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63d-climax days with negative return in trailing 252d."""
    ret = close.pct_change(1)
    is_climax = (volume >= _rolling_max(volume, _TD_QTR))
    down_climax = (is_climax & (ret < 0)).astype(float)
    return down_climax.rolling(_TD_YEAR, min_periods=1).sum()


def vcx_189_climax_count_up_bar_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63d-climax days with positive return in trailing 252d."""
    ret = close.pct_change(1)
    is_climax = (volume >= _rolling_max(volume, _TD_QTR))
    up_climax = (is_climax & (ret >= 0)).astype(float)
    return up_climax.rolling(_TD_YEAR, min_periods=1).sum()


def vcx_190_vol_mean_top3_over_mean_21d(volume: pd.Series) -> pd.Series:
    """Mean of top-3 volume days divided by 21-day mean volume."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_MON, min_periods=3).apply(_mean_top3, raw=True)
    return _safe_div(top3_mean, _rolling_mean(volume, _TD_MON))


def vcx_191_vol_mean_top3_over_mean_63d(volume: pd.Series) -> pd.Series:
    """Mean of top-3 volume days divided by 63-day mean volume."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_QTR, min_periods=3).apply(_mean_top3, raw=True)
    return _safe_div(top3_mean, _rolling_mean(volume, _TD_QTR))


def vcx_192_climax_day_hl_midpoint_vs_close_63d(high: pd.Series, low: pd.Series,
                                                  close: pd.Series, volume: pd.Series) -> pd.Series:
    """(HL midpoint - close) / close on 63-day climax day (close below midpoint = bearish)."""
    midpoint = (high + low) / 2.0
    val = _safe_div(midpoint - close, close)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return val.where(is_climax, np.nan).ffill()


def vcx_193_climax_day_hl_midpoint_vs_close_252d(high: pd.Series, low: pd.Series,
                                                   close: pd.Series, volume: pd.Series) -> pd.Series:
    """(HL midpoint - close) / close on 252-day climax day."""
    midpoint = (high + low) / 2.0
    val = _safe_div(midpoint - close, close)
    mx = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx)
    return val.where(is_climax, np.nan).ffill()


def vcx_194_vol_max_to_second_max_gap_log_21d(volume: pd.Series) -> pd.Series:
    """Log ratio of max to second-max volume in 21-day window (log singularity)."""
    top1 = _rolling_max(volume, _TD_MON)
    top2 = _rolling_second_max(volume, _TD_MON)
    return _log_safe(top1) - _log_safe(top2)


def vcx_195_vol_max_to_second_max_gap_log_63d(volume: pd.Series) -> pd.Series:
    """Log ratio of max to second-max volume in 63-day window."""
    top1 = _rolling_max(volume, _TD_QTR)
    top2 = _rolling_second_max(volume, _TD_QTR)
    return _log_safe(top1) - _log_safe(top2)


def vcx_196_vol_above_2x_mean_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where volume exceeded 2x the 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    return (volume >= 2.0 * mean63).astype(float).rolling(_TD_YEAR, min_periods=1).sum()


def vcx_197_close_vs_climax_high_252d(high: pd.Series, volume: pd.Series,
                                       close: pd.Series) -> pd.Series:
    """Today's close relative to the intraday high of the 252-day peak-volume day."""
    mx_vol = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx_vol)
    climax_high = high.where(is_climax, np.nan).ffill()
    return _safe_div(close, climax_high) - 1.0


def vcx_198_close_vs_climax_low_252d(low: pd.Series, volume: pd.Series,
                                      close: pd.Series) -> pd.Series:
    """Today's close relative to the intraday low of the 252-day peak-volume day."""
    mx_vol = _rolling_max(volume, _TD_YEAR)
    is_climax = (volume >= mx_vol)
    climax_low = low.where(is_climax, np.nan).ffill()
    return _safe_div(close, climax_low) - 1.0


def vcx_199_vol_kurtosis_63d(volume: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of volume (extreme climax fat-tail measure)."""
    return volume.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vcx_200_vol_kurtosis_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of volume."""
    return volume.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CLIMAX_REGISTRY_076_150 = {
    "vcx_076_climax_day_gap_up_63d": {"inputs": ["close", "open", "volume"], "func": vcx_076_climax_day_gap_up_63d},
    "vcx_077_climax_day_gap_up_252d": {"inputs": ["close", "open", "volume"], "func": vcx_077_climax_day_gap_up_252d},
    "vcx_078_climax_day_open_to_close_63d": {"inputs": ["close", "open", "volume"], "func": vcx_078_climax_day_open_to_close_63d},
    "vcx_079_climax_day_open_to_close_252d": {"inputs": ["close", "open", "volume"], "func": vcx_079_climax_day_open_to_close_252d},
    "vcx_080_climax_day_upper_wick_norm_63d": {"inputs": ["high", "close", "open", "volume"], "func": vcx_080_climax_day_upper_wick_norm_63d},
    "vcx_081_climax_day_lower_wick_norm_63d": {"inputs": ["low", "close", "open", "volume"], "func": vcx_081_climax_day_lower_wick_norm_63d},
    "vcx_082_climax_day_body_pct_63d": {"inputs": ["high", "low", "close", "open", "volume"], "func": vcx_082_climax_day_body_pct_63d},
    "vcx_083_climax_day_body_pct_252d": {"inputs": ["high", "low", "close", "open", "volume"], "func": vcx_083_climax_day_body_pct_252d},
    "vcx_084_climax_down_bar_magnitude_63d": {"inputs": ["close", "volume"], "func": vcx_084_climax_down_bar_magnitude_63d},
    "vcx_085_climax_down_bar_magnitude_252d": {"inputs": ["close", "volume"], "func": vcx_085_climax_down_bar_magnitude_252d},
    "vcx_086_climax_bear_candle_score_63d": {"inputs": ["high", "low", "close", "open", "volume"], "func": vcx_086_climax_bear_candle_score_63d},
    "vcx_087_climax_bear_candle_score_252d": {"inputs": ["high", "low", "close", "open", "volume"], "func": vcx_087_climax_bear_candle_score_252d},
    "vcx_088_return_1d_after_climax_63d": {"inputs": ["close", "volume"], "func": vcx_088_return_1d_after_climax_63d},
    "vcx_089_return_5d_after_climax_63d": {"inputs": ["close", "volume"], "func": vcx_089_return_5d_after_climax_63d},
    "vcx_090_close_vs_climax_close_21d": {"inputs": ["close", "volume"], "func": vcx_090_close_vs_climax_close_21d},
    "vcx_091_close_vs_climax_close_63d": {"inputs": ["close", "volume"], "func": vcx_091_close_vs_climax_close_63d},
    "vcx_092_close_vs_climax_close_252d": {"inputs": ["close", "volume"], "func": vcx_092_close_vs_climax_close_252d},
    "vcx_093_close_below_climax_close_flag_63d": {"inputs": ["close", "volume"], "func": vcx_093_close_below_climax_close_flag_63d},
    "vcx_094_close_below_climax_close_flag_252d": {"inputs": ["close", "volume"], "func": vcx_094_close_below_climax_close_flag_252d},
    "vcx_095_climax_low_today_vs_climax_day_low_63d": {"inputs": ["low", "volume"], "func": vcx_095_climax_low_today_vs_climax_day_low_63d},
    "vcx_096_climax_low_today_vs_climax_day_low_252d": {"inputs": ["low", "volume"], "func": vcx_096_climax_low_today_vs_climax_day_low_252d},
    "vcx_097_max_drawdown_from_climax_close_63d": {"inputs": ["close", "volume"], "func": vcx_097_max_drawdown_from_climax_close_63d},
    "vcx_098_max_drawdown_from_climax_close_252d": {"inputs": ["close", "volume"], "func": vcx_098_max_drawdown_from_climax_close_252d},
    "vcx_099_vol_ratio_today_vs_climax_63d": {"inputs": ["volume"], "func": vcx_099_vol_ratio_today_vs_climax_63d},
    "vcx_100_vol_ratio_today_vs_climax_252d": {"inputs": ["volume"], "func": vcx_100_vol_ratio_today_vs_climax_252d},
    "vcx_101_climax_day_tr_vs_atr14_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_101_climax_day_tr_vs_atr14_63d},
    "vcx_102_climax_day_tr_vs_atr14_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_102_climax_day_tr_vs_atr14_252d},
    "vcx_103_max_vol_day_atr_ratio_21d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_103_max_vol_day_atr_ratio_21d},
    "vcx_104_climax_day_vol_x_range_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_104_climax_day_vol_x_range_63d},
    "vcx_105_climax_day_vol_x_range_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_105_climax_day_vol_x_range_252d},
    "vcx_106_climax_vol_force_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_106_climax_vol_force_pct_rank_252d},
    "vcx_107_days_since_max_vol_day_high_63d": {"inputs": ["high", "volume"], "func": vcx_107_days_since_max_vol_day_high_63d},
    "vcx_108_days_since_max_vol_day_low_63d": {"inputs": ["low", "volume"], "func": vcx_108_days_since_max_vol_day_low_63d},
    "vcx_109_climax_day_ret_x_vol_63d": {"inputs": ["close", "volume"], "func": vcx_109_climax_day_ret_x_vol_63d},
    "vcx_110_climax_day_ret_x_vol_252d": {"inputs": ["close", "volume"], "func": vcx_110_climax_day_ret_x_vol_252d},
    "vcx_111_climax_day_ret_x_vol_norm_mean_63d": {"inputs": ["close", "volume"], "func": vcx_111_climax_day_ret_x_vol_norm_mean_63d},
    "vcx_112_climax_day_ret_x_vol_norm_mean_252d": {"inputs": ["close", "volume"], "func": vcx_112_climax_day_ret_x_vol_norm_mean_252d},
    "vcx_113_climax_count_in_63d": {"inputs": ["volume"], "func": vcx_113_climax_count_in_63d},
    "vcx_114_climax_count_in_252d": {"inputs": ["volume"], "func": vcx_114_climax_count_in_252d},
    "vcx_115_climax_frequency_21d": {"inputs": ["volume"], "func": vcx_115_climax_frequency_21d},
    "vcx_116_days_between_climax_events_63d": {"inputs": ["volume"], "func": vcx_116_days_between_climax_events_63d},
    "vcx_117_recent_climax_cluster_5d": {"inputs": ["volume"], "func": vcx_117_recent_climax_cluster_5d},
    "vcx_118_recent_climax_cluster_21d": {"inputs": ["volume"], "func": vcx_118_recent_climax_cluster_21d},
    "vcx_119_climax_vol_avg_over_63d_events": {"inputs": ["volume"], "func": vcx_119_climax_vol_avg_over_63d_events},
    "vcx_120_time_since_last_climax_63d_event": {"inputs": ["volume"], "func": vcx_120_time_since_last_climax_63d_event},
    "vcx_121_climax_beat_prior_climax_flag_252d": {"inputs": ["volume"], "func": vcx_121_climax_beat_prior_climax_flag_252d},
    "vcx_122_expanding_climax_beat_count": {"inputs": ["volume"], "func": vcx_122_expanding_climax_beat_count},
    "vcx_123_climax_days_pct_of_63d_window": {"inputs": ["volume"], "func": vcx_123_climax_days_pct_of_63d_window},
    "vcx_124_climax_days_pct_of_252d_window": {"inputs": ["volume"], "func": vcx_124_climax_days_pct_of_252d_window},
    "vcx_125_two_climax_days_within_21d_flag": {"inputs": ["volume"], "func": vcx_125_two_climax_days_within_21d_flag},
    "vcx_126_climax_vol_x_down_ret_score_63d": {"inputs": ["close", "volume"], "func": vcx_126_climax_vol_x_down_ret_score_63d},
    "vcx_127_climax_vol_x_down_ret_score_252d": {"inputs": ["close", "volume"], "func": vcx_127_climax_vol_x_down_ret_score_252d},
    "vcx_128_climax_vol_x_range_max_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_128_climax_vol_x_range_max_63d},
    "vcx_129_climax_vol_x_range_max_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_129_climax_vol_x_range_max_252d},
    "vcx_130_climax_vol_share_top3_63d": {"inputs": ["volume"], "func": vcx_130_climax_vol_share_top3_63d},
    "vcx_131_climax_vol_share_top3_252d": {"inputs": ["volume"], "func": vcx_131_climax_vol_share_top3_252d},
    "vcx_132_vol_concentration_herfindahl_21d": {"inputs": ["volume"], "func": vcx_132_vol_concentration_herfindahl_21d},
    "vcx_133_vol_concentration_herfindahl_63d": {"inputs": ["volume"], "func": vcx_133_vol_concentration_herfindahl_63d},
    "vcx_134_vol_max_over_total_trend_slope_63d": {"inputs": ["volume"], "func": vcx_134_vol_max_over_total_trend_slope_63d},
    "vcx_135_climax_combined_score_63d": {"inputs": ["close", "high", "low", "volume"], "func": vcx_135_climax_combined_score_63d},
    "vcx_136_climax_combined_score_252d": {"inputs": ["close", "high", "low", "volume"], "func": vcx_136_climax_combined_score_252d},
    "vcx_137_max_vol_day_was_down_close_21d": {"inputs": ["close", "volume"], "func": vcx_137_max_vol_day_was_down_close_21d},
    "vcx_138_max_vol_day_was_down_close_63d": {"inputs": ["close", "volume"], "func": vcx_138_max_vol_day_was_down_close_63d},
    "vcx_139_max_vol_21d_vs_ewm63": {"inputs": ["volume"], "func": vcx_139_max_vol_21d_vs_ewm63},
    "vcx_140_max_vol_63d_vs_ewm126": {"inputs": ["volume"], "func": vcx_140_max_vol_63d_vs_ewm126},
    "vcx_141_max_vol_252d_vs_ewm252": {"inputs": ["volume"], "func": vcx_141_max_vol_252d_vs_ewm252},
    "vcx_142_days_since_vol_above_2x_mean_252d": {"inputs": ["volume"], "func": vcx_142_days_since_vol_above_2x_mean_252d},
    "vcx_143_days_since_vol_above_3x_mean_252d": {"inputs": ["volume"], "func": vcx_143_days_since_vol_above_3x_mean_252d},
    "vcx_144_climax_vol_zscore_expanding": {"inputs": ["volume"], "func": vcx_144_climax_vol_zscore_expanding},
    "vcx_145_max_vol_21d_expanding_pct_rank": {"inputs": ["volume"], "func": vcx_145_max_vol_21d_expanding_pct_rank},
    "vcx_146_max_vol_252d_expanding_pct_rank": {"inputs": ["volume"], "func": vcx_146_max_vol_252d_expanding_pct_rank},
    "vcx_147_climax_vol_mean_ratio_slope_63d": {"inputs": ["volume"], "func": vcx_147_climax_vol_mean_ratio_slope_63d},
    "vcx_148_climax_recency_x_magnitude_63d": {"inputs": ["volume"], "func": vcx_148_climax_recency_x_magnitude_63d},
    "vcx_149_climax_recency_x_magnitude_252d": {"inputs": ["volume"], "func": vcx_149_climax_recency_x_magnitude_252d},
    "vcx_150_climax_distress_composite": {"inputs": ["close", "volume"], "func": vcx_150_climax_distress_composite},
    "vcx_176_climax_day_close_vs_high_63d": {"inputs": ["high", "close", "volume"], "func": vcx_176_climax_day_close_vs_high_63d},
    "vcx_177_climax_day_close_vs_high_252d": {"inputs": ["high", "close", "volume"], "func": vcx_177_climax_day_close_vs_high_252d},
    "vcx_178_climax_day_vol_normalized_by_expanding_mean": {"inputs": ["volume"], "func": vcx_178_climax_day_vol_normalized_by_expanding_mean},
    "vcx_179_vol_above_p95_count_252d": {"inputs": ["volume"], "func": vcx_179_vol_above_p95_count_252d},
    "vcx_180_vol_above_p99_count_252d": {"inputs": ["volume"], "func": vcx_180_vol_above_p99_count_252d},
    "vcx_181_max_vol_21d_vs_median_252d": {"inputs": ["volume"], "func": vcx_181_max_vol_21d_vs_median_252d},
    "vcx_182_max_vol_63d_vs_median_252d": {"inputs": ["volume"], "func": vcx_182_max_vol_63d_vs_median_252d},
    "vcx_183_vol_rolling_max_drawdown_21d": {"inputs": ["volume"], "func": vcx_183_vol_rolling_max_drawdown_21d},
    "vcx_184_vol_rolling_max_drawdown_63d": {"inputs": ["volume"], "func": vcx_184_vol_rolling_max_drawdown_63d},
    "vcx_185_vol_std_normalized_by_max_21d": {"inputs": ["volume"], "func": vcx_185_vol_std_normalized_by_max_21d},
    "vcx_186_vol_std_normalized_by_max_63d": {"inputs": ["volume"], "func": vcx_186_vol_std_normalized_by_max_63d},
    "vcx_187_climax_day_ret_vs_atr_21d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_187_climax_day_ret_vs_atr_21d},
    "vcx_188_climax_count_down_bar_252d": {"inputs": ["close", "volume"], "func": vcx_188_climax_count_down_bar_252d},
    "vcx_189_climax_count_up_bar_252d": {"inputs": ["close", "volume"], "func": vcx_189_climax_count_up_bar_252d},
    "vcx_190_vol_mean_top3_over_mean_21d": {"inputs": ["volume"], "func": vcx_190_vol_mean_top3_over_mean_21d},
    "vcx_191_vol_mean_top3_over_mean_63d": {"inputs": ["volume"], "func": vcx_191_vol_mean_top3_over_mean_63d},
    "vcx_192_climax_day_hl_midpoint_vs_close_63d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_192_climax_day_hl_midpoint_vs_close_63d},
    "vcx_193_climax_day_hl_midpoint_vs_close_252d": {"inputs": ["high", "low", "close", "volume"], "func": vcx_193_climax_day_hl_midpoint_vs_close_252d},
    "vcx_194_vol_max_to_second_max_gap_log_21d": {"inputs": ["volume"], "func": vcx_194_vol_max_to_second_max_gap_log_21d},
    "vcx_195_vol_max_to_second_max_gap_log_63d": {"inputs": ["volume"], "func": vcx_195_vol_max_to_second_max_gap_log_63d},
    "vcx_196_vol_above_2x_mean_count_252d": {"inputs": ["volume"], "func": vcx_196_vol_above_2x_mean_count_252d},
    "vcx_197_close_vs_climax_high_252d": {"inputs": ["high", "volume", "close"], "func": vcx_197_close_vs_climax_high_252d},
    "vcx_198_close_vs_climax_low_252d": {"inputs": ["low", "volume", "close"], "func": vcx_198_close_vs_climax_low_252d},
    "vcx_199_vol_kurtosis_63d": {"inputs": ["volume"], "func": vcx_199_vol_kurtosis_63d},
    "vcx_200_vol_kurtosis_252d": {"inputs": ["volume"], "func": vcx_200_vol_kurtosis_252d},
}
