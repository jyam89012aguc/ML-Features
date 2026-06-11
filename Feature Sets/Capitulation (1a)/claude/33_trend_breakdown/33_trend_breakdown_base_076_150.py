"""
33_trend_breakdown — Base Features 076-150
Domain: MACD extended, ADX extended, HH/HL structure extended,
        Supertrend (ATR-band trend), Ichimoku cloud (price-vs-cloud, bearish cross),
        composite breakdown states.
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
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _days_since(cond: pd.Series) -> pd.Series:
    """Days since last True; 0 on True rows, rising integer on False rows."""
    result = pd.Series(np.nan, index=cond.index)
    counter = np.nan
    for i, v in enumerate(cond):
        if v:
            counter = 0
        elif not np.isnan(counter):
            counter += 1
        result.iloc[i] = counter
    return result.astype(float)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _macd_components(close: pd.Series):
    """Return (macd_line, signal_line, histogram)."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd  = ema12 - ema26
    sig   = _ewm_mean(macd, 9)
    hist  = macd - sig
    return macd, sig, hist


def _adx_components(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14):
    """Return (adx, plus_di, minus_di) using Wilder smoothing."""
    tr  = _tr(close, high, low)
    dm_plus  = (high - high.shift(1)).clip(lower=0.0)
    dm_minus = (low.shift(1) - low).clip(lower=0.0)
    dm_plus  = dm_plus.where(dm_plus > dm_minus, 0.0)
    dm_minus = dm_minus.where(dm_minus > dm_plus, 0.0)
    atr   = tr.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_p = dm_plus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_m = dm_minus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    di_p  = _safe_div(sdi_p, atr) * 100
    di_m  = _safe_div(sdi_m, atr) * 100
    dx    = _safe_div((di_p - di_m).abs(), (di_p + di_m).abs()) * 100
    adx   = dx.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    return adx, di_p, di_m


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _supertrend(close: pd.Series, high: pd.Series, low: pd.Series,
                atr_period: int = 10, multiplier: float = 3.0):
    """
    Compute Supertrend indicator using an explicit forward-only loop.
    Returns (supertrend_line, trend_series) where trend=1 uptrend, trend=-1 downtrend.
    Backward-looking only — no look-ahead.
    """
    n = len(close)
    cl = close.values
    hi = high.values
    lo = low.values

    # Compute ATR with Wilder smoothing
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i] - lo[i],
                        abs(hi[i] - cl[i - 1]),
                        abs(lo[i] - cl[i - 1]))
    tr_arr[0] = hi[0] - lo[0]

    atr_arr = np.full(n, np.nan)
    # seed with simple mean for first atr_period bars
    if n >= atr_period:
        atr_arr[atr_period - 1] = np.nanmean(tr_arr[:atr_period])
        alpha = 1.0 / atr_period
        for i in range(atr_period, n):
            atr_arr[i] = atr_arr[i - 1] * (1 - alpha) + tr_arr[i] * alpha

    hl2 = (hi + lo) / 2.0
    upper_basic = hl2 + multiplier * atr_arr
    lower_basic = hl2 - multiplier * atr_arr

    upper_band = np.full(n, np.nan)
    lower_band = np.full(n, np.nan)
    st_line    = np.full(n, np.nan)
    trend      = np.full(n, np.nan)

    for i in range(n):
        if np.isnan(atr_arr[i]):
            continue
        if i == 0 or np.isnan(upper_band[i - 1]):
            upper_band[i] = upper_basic[i]
            lower_band[i] = lower_basic[i]
            trend[i]      = 1.0 if cl[i] > lower_basic[i] else -1.0
            st_line[i]    = lower_band[i] if trend[i] == 1.0 else upper_band[i]
            continue

        # Update bands (cannot widen in direction of trend)
        upper_band[i] = (upper_basic[i]
                         if upper_basic[i] < upper_band[i - 1] or cl[i - 1] > upper_band[i - 1]
                         else upper_band[i - 1])
        lower_band[i] = (lower_basic[i]
                         if lower_basic[i] > lower_band[i - 1] or cl[i - 1] < lower_band[i - 1]
                         else lower_band[i - 1])

        prev_trend = trend[i - 1]
        if prev_trend == 1.0:
            trend[i] = -1.0 if cl[i] < lower_band[i] else 1.0
        else:
            trend[i] = 1.0 if cl[i] > upper_band[i] else -1.0

        st_line[i] = lower_band[i] if trend[i] == 1.0 else upper_band[i]

    return (pd.Series(st_line, index=close.index),
            pd.Series(trend,   index=close.index))


def _ichimoku_lines(close: pd.Series, high: pd.Series, low: pd.Series):
    """
    Compute Ichimoku lines using only trailing (backward-looking) data.
    Tenkan-sen  (conversion): (9-period high + 9-period low) / 2
    Kijun-sen   (base):       (26-period high + 26-period low) / 2
    Senkou Span A (cloud A):  (Tenkan + Kijun) / 2  — at current bar (no forward shift)
    Senkou Span B (cloud B):  (52-period high + 52-period low) / 2 — at current bar

    NOTE: traditional Ichimoku forward-projects spans by 26 bars, which is
    look-ahead. Here we use the spans computed at the CURRENT bar position
    (no shift) so all values are strictly backward-looking.

    Returns (tenkan, kijun, span_a, span_b).
    """
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    return tenkan, kijun, span_a, span_b


# ── Feature functions 076-115  (MACD extended, ADX extended, HH/HL extended) ──

# --- Group I (076-085): MACD extended — divergence, histogram depth ---

def tbd_076_macd_histogram_depth_21d_min(close: pd.Series) -> pd.Series:
    """Most negative MACD histogram value in trailing 21 days."""
    _, _, hist = _macd_components(close)
    return _rolling_min(hist, _TD_MON)


def tbd_077_macd_histogram_depth_63d_min(close: pd.Series) -> pd.Series:
    """Most negative MACD histogram value in trailing 63 days."""
    _, _, hist = _macd_components(close)
    return _rolling_min(hist, _TD_QTR)


def tbd_078_macd_histogram_neg_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days MACD histogram was negative."""
    _, _, hist = _macd_components(close)
    return _rolling_count_true(hist < 0, _TD_QTR) / _TD_QTR


def tbd_079_macd_line_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive days MACD line has been below zero."""
    macd, _, _ = _macd_components(close)
    return _consec_streak(macd < 0)


def tbd_080_macd_cross_count_63d(close: pd.Series) -> pd.Series:
    """Total MACD bearish crossover events (line cross + hist flip) in 63 days."""
    macd, sig, hist = _macd_components(close)
    below1 = macd < sig
    e1 = (below1 & ~below1.shift(1).fillna(False)).astype(float)
    neg2 = hist < 0
    e2 = (neg2 & ~neg2.shift(1).fillna(False)).astype(float)
    return _rolling_sum(e1 + e2, _TD_QTR)


def tbd_081_macd_histogram_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: MACD histogram declining (today's hist < yesterday's hist)."""
    _, _, hist = _macd_components(close)
    return ((hist < hist.shift(1)).astype(float))


def tbd_082_macd_signal_below_zero_flag(close: pd.Series) -> pd.Series:
    """Flag: MACD signal line < 0 (signal confirms bearish regime)."""
    _, sig, _ = _macd_components(close)
    return ((sig < 0).astype(float))


def tbd_083_macd_both_lines_below_zero_flag(close: pd.Series) -> pd.Series:
    """Flag: both MACD line and signal line below zero."""
    macd, sig, _ = _macd_components(close)
    return ((macd < 0) & (sig < 0)).astype(float)


def tbd_084_macd_histogram_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of MACD histogram relative to 63-day distribution."""
    _, _, hist = _macd_components(close)
    m = _rolling_mean(hist, _TD_QTR)
    s = _rolling_std(hist, _TD_QTR)
    return _safe_div(hist - m, s)


def tbd_085_days_since_macd_line_crossed_zero_neg(close: pd.Series) -> pd.Series:
    """Days since MACD line crossed below zero."""
    macd, _, _ = _macd_components(close)
    neg = macd < 0
    event = (neg & ~neg.shift(1).fillna(False))
    return _days_since(event)


# --- Group J (086-095): ADX extended — period variations, collapse streaks ---

def tbd_086_adx20_below_25_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX(20) < 25 (medium-period ADX weak)."""
    adx, _, _ = _adx_components(close, high, low, 20)
    return ((adx < 25).astype(float))


def tbd_087_adx14_neg_slope_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days ADX(14) has been declining."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return _consec_streak(adx < adx.shift(1))


def tbd_088_adx14_below_15_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX(14) < 15 (extreme trend weakness / trendless)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return ((adx < 15).astype(float))


def tbd_089_dmi_bearish_cross_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of DI- above DI+ crossover events in trailing 252 days."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    above = di_m > di_p
    event = (above & ~above.shift(1).fillna(False)).astype(float)
    return _rolling_sum(event, _TD_YEAR)


def tbd_090_dmi_bearish_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days DI- > DI+ (bearish DMI streak)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    return _consec_streak(di_m > di_p)


def tbd_091_adx14_collapse_from_peak_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADX drop from 252-day peak ADX value."""
    adx, _, _ = _adx_components(close, high, low, 14)
    peak = _rolling_max(adx, _TD_YEAR)
    return peak - adx


def tbd_092_dmi_spread_di_minus_minus_di_plus(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """DI- minus DI+ (positive = bearish alignment, negative = bullish)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    return di_m - di_p


def tbd_093_dmi_spread_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of DI- minus DI+ spread over 252-day window."""
    spread = tbd_092_dmi_spread_di_minus_minus_di_plus(close, high, low)
    m = _rolling_mean(spread, _TD_YEAR)
    s = _rolling_std(spread, _TD_YEAR)
    return _safe_div(spread - m, s)


def tbd_094_adx14_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of ADX(14) in trailing 252-day distribution."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return adx.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tbd_095_adx_dmi_event_density_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of ADX collapse + DMI bearish cross events in trailing 63 days."""
    adx, di_p, di_m = _adx_components(close, high, low, 14)
    collapse = (adx < adx.shift(1)) & (adx < 25)
    above = di_m > di_p
    cross = (above & ~above.shift(1).fillna(False)).astype(float)
    return _rolling_sum(collapse.astype(float) + cross, _TD_QTR)


# --- Group K (096-105): MA slope magnitude and duration ---

def tbd_096_sma20_slope_1d(close: pd.Series) -> pd.Series:
    """Daily change in SMA20 (slope magnitude)."""
    sma20 = _rolling_mean(close, _TD_MON)
    return sma20.diff(1)


def tbd_097_sma50_slope_1d(close: pd.Series) -> pd.Series:
    """Daily change in SMA50 (slope magnitude)."""
    sma50 = _rolling_mean(close, 50)
    return sma50.diff(1)


def tbd_098_sma200_slope_1d(close: pd.Series) -> pd.Series:
    """Daily change in SMA200 (slope magnitude)."""
    sma200 = _rolling_mean(close, 200)
    return sma200.diff(1)


def tbd_099_ema12_slope_1d(close: pd.Series) -> pd.Series:
    """Daily change in EMA12."""
    ema12 = _ewm_mean(close, 12)
    return ema12.diff(1)


def tbd_100_ema26_slope_1d(close: pd.Series) -> pd.Series:
    """Daily change in EMA26."""
    ema26 = _ewm_mean(close, 26)
    return ema26.diff(1)


def tbd_101_sma20_slope_rolling_avg_21d(close: pd.Series) -> pd.Series:
    """21-day rolling average of SMA20 daily slope (smoothed slope)."""
    return _rolling_mean(_rolling_mean(close, _TD_MON).diff(1), _TD_MON)


def tbd_102_sma200_slope_rolling_avg_63d(close: pd.Series) -> pd.Series:
    """63-day rolling average of SMA200 daily slope."""
    return _rolling_mean(_rolling_mean(close, 200).diff(1), _TD_QTR)


def tbd_103_sma50_neg_slope_streak(close: pd.Series) -> pd.Series:
    """Consecutive days SMA50 slope is negative."""
    sma50 = _rolling_mean(close, 50)
    return _consec_streak(sma50 < sma50.shift(1))


def tbd_104_ema12_neg_slope_streak(close: pd.Series) -> pd.Series:
    """Consecutive days EMA12 slope is negative."""
    ema12 = _ewm_mean(close, 12)
    return _consec_streak(ema12 < ema12.shift(1))


def tbd_105_all_ema_slopes_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA12, EMA26, EMA50 all declining simultaneously."""
    e12 = _ewm_mean(close, 12)
    e26 = _ewm_mean(close, 26)
    e50 = _ewm_mean(close, 50)
    return ((e12 < e12.shift(1)) &
            (e26 < e26.shift(1)) &
            (e50 < e50.shift(1))).astype(float)


# --- Group L (106-115): Higher-high/higher-low extended analysis ---

def tbd_106_hh_hl_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with higher-high AND higher-low (uptrend run)."""
    return _consec_streak((high > high.shift(1)) & (low > low.shift(1)))


def tbd_107_lh_ll_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with lower-high AND lower-low (downtrend run)."""
    return _consec_streak((high < high.shift(1)) & (low < low.shift(1)))


def tbd_108_lh_ll_streak_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum LH+LL run length in trailing 63 days."""
    cond = (high < high.shift(1)) & (low < low.shift(1))
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx: mx = cur
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def tbd_109_lh_ll_streak_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum LH+LL run length in trailing 252 days."""
    cond = (high < high.shift(1)) & (low < low.shift(1))
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx: mx = cur
        return float(mx)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def tbd_110_hh_hl_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days with higher-high AND higher-low."""
    cond = (high > high.shift(1)) & (low > low.shift(1))
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def tbd_111_lh_ll_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days with lower-high AND lower-low."""
    cond = (high < high.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def tbd_112_structure_net_score_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Net structure score: LH+LL count minus HH+HL count in 21 days."""
    hh_hl = _rolling_count_true((high > high.shift(1)) & (low > low.shift(1)), _TD_MON)
    lh_ll = _rolling_count_true((high < high.shift(1)) & (low < low.shift(1)), _TD_MON)
    return lh_ll - hh_hl


def tbd_113_days_since_last_hh_hl(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last day with both higher-high AND higher-low."""
    cond = (high > high.shift(1)) & (low > low.shift(1))
    return _days_since(cond)


def tbd_114_higher_high_count_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of higher-high days in trailing 21 days."""
    return _rolling_count_true(high > high.shift(1), _TD_MON)


def tbd_115_lower_low_count_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of lower-low days in trailing 21 days."""
    return _rolling_count_true(low < low.shift(1), _TD_MON)


# --- Group M (116-125): Supertrend (ATR-band trend indicator) ---

def tbd_116_supertrend_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Supertrend(10,3) in downtrend — price below Supertrend band."""
    _, trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    return ((trend < 0).astype(float))


def tbd_117_supertrend_flip_to_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Supertrend(10,3) flips from uptrend to downtrend."""
    _, trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    bearish = trend < 0
    return (bearish & ~bearish.shift(1).fillna(False)).astype(float)


def tbd_118_supertrend_bars_in_downtrend(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars Supertrend(10,3) has been in downtrend."""
    _, trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    return _consec_streak(trend < 0)


def tbd_119_supertrend_bars_since_bearish_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars elapsed since last Supertrend bearish flip."""
    return _days_since(tbd_117_supertrend_flip_to_bearish_event(close, high, low))


def tbd_120_supertrend_distance_from_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Signed distance (close - Supertrend line) / close; negative = bearish."""
    st_line, _ = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    return _safe_div(close - st_line, close)


def tbd_121_supertrend_bearish_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days Supertrend was in bearish (downtrend) state."""
    _, trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    return _rolling_count_true(trend < 0, _TD_QTR) / _TD_QTR


def tbd_122_supertrend_flip_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Supertrend bearish-flip events in trailing 63 days."""
    return _rolling_sum(tbd_117_supertrend_flip_to_bearish_event(close, high, low), _TD_QTR)


def tbd_123_supertrend_distance_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Supertrend distance from price over trailing 63 days."""
    dist = tbd_120_supertrend_distance_from_price(close, high, low)
    m = _rolling_mean(dist, _TD_QTR)
    s = _rolling_std(dist, _TD_QTR)
    return _safe_div(dist - m, s)


def tbd_124_supertrend_and_psar_both_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: both Supertrend AND Parabolic SAR in bearish state simultaneously."""
    _, st_trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    # Compute Parabolic SAR inline (self-contained)
    n = len(high)
    hi = high.values; lo = low.values; cl = close.values
    sar_t = np.full(n, np.nan)
    is_bull = True; ep = hi[0]; af = 0.02; sar_t[0] = lo[0]
    for i in range(1, n):
        psar = sar_t[i - 1]
        if is_bull:
            ns = psar + af * (ep - psar)
            ns = min(ns, lo[i - 1])
            if i >= 2: ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False; ns = ep; ep = lo[i]; af = 0.02
            else:
                if hi[i] > ep: ep = hi[i]; af = min(af + 0.02, 0.2)
        else:
            ns = psar + af * (ep - psar)
            ns = max(ns, hi[i - 1])
            if i >= 2: ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True; ns = ep; ep = hi[i]; af = 0.02
            else:
                if lo[i] < ep: ep = lo[i]; af = min(af + 0.02, 0.2)
        sar_t[i] = ns
    psar_s = pd.Series(sar_t, index=close.index)
    psar_bearish = close < psar_s
    return ((st_trend < 0) & psar_bearish).astype(float)


def tbd_125_supertrend_bearish_streak_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum Supertrend bearish streak length in trailing 252 days."""
    _, trend = _supertrend(close, high, low, atr_period=10, multiplier=3.0)
    cond = trend < 0
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx: mx = cur
        return float(mx)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


# --- Group N (126-140): Ichimoku — price vs cloud, cross events, distance ---

def tbd_126_ichimoku_price_below_cloud_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < min(Span A, Span B) — price below the entire Ichimoku cloud."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    return ((close < cloud_bottom).astype(float))


def tbd_127_ichimoku_price_above_cloud_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close > max(Span A, Span B) — price above entire cloud (bullish reference)."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    cloud_top = pd.concat([span_a, span_b], axis=1).max(axis=1)
    return ((close > cloud_top).astype(float))


def tbd_128_ichimoku_tenkan_below_kijun_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Tenkan-sen < Kijun-sen (bearish short/medium term cross state)."""
    tenkan, kijun, _, _ = _ichimoku_lines(close, high, low)
    return ((tenkan < kijun).astype(float))


def tbd_129_ichimoku_tenkan_kijun_bearish_cross_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Tenkan-sen crosses below Kijun-sen (bearish Ichimoku cross)."""
    tenkan, kijun, _, _ = _ichimoku_lines(close, high, low)
    below = tenkan < kijun
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_130_ichimoku_days_since_tenkan_kijun_bearish_cross(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since Tenkan-sen last crossed below Kijun-sen."""
    return _days_since(tbd_129_ichimoku_tenkan_kijun_bearish_cross_event(close, high, low))


def tbd_131_ichimoku_close_vs_tenkan_distance(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - Tenkan) / close; negative = below Tenkan (bearish short-term signal)."""
    tenkan, _, _, _ = _ichimoku_lines(close, high, low)
    return _safe_div(close - tenkan, close)


def tbd_132_ichimoku_close_vs_kijun_distance(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - Kijun) / close; negative = below Kijun (bearish medium-term signal)."""
    _, kijun, _, _ = _ichimoku_lines(close, high, low)
    return _safe_div(close - kijun, close)


def tbd_133_ichimoku_distance_below_cloud(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Distance below cloud bottom / close; 0 if above cloud. Bearish depth measure."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    gap = cloud_bottom - close
    return _safe_div(gap.clip(lower=0.0), close)


def tbd_134_ichimoku_cloud_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Span B > Span A (bearish/red cloud — cloud signals continuation of downtrend)."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    return ((span_b > span_a).astype(float))


def tbd_135_ichimoku_close_below_tenkan_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Tenkan-sen (short-term bearish momentum)."""
    tenkan, _, _, _ = _ichimoku_lines(close, high, low)
    return ((close < tenkan).astype(float))


def tbd_136_ichimoku_close_below_kijun_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Kijun-sen (medium-term bearish momentum)."""
    _, kijun, _, _ = _ichimoku_lines(close, high, low)
    return ((close < kijun).astype(float))


def tbd_137_ichimoku_close_below_spana_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Span A (price inside or below cloud top)."""
    _, _, span_a, _ = _ichimoku_lines(close, high, low)
    return ((close < span_a).astype(float))


def tbd_138_ichimoku_close_below_spanb_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Span B (price at or below lower cloud boundary)."""
    _, _, _, span_b = _ichimoku_lines(close, high, low)
    return ((close < span_b).astype(float))


def tbd_139_ichimoku_bearish_cross_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Tenkan/Kijun bearish cross events in trailing 252 days."""
    return _rolling_sum(tbd_129_ichimoku_tenkan_kijun_bearish_cross_event(close, high, low), _TD_YEAR)


def tbd_140_ichimoku_below_cloud_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars price has been below entire Ichimoku cloud."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    return _consec_streak(close < cloud_bottom)


# --- Group O (141-150): Composite and aggregate breakdown indicators ---

def tbd_141_supertrend_psar_aroon_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Supertrend, PSAR, and Aroon Down(14) all bearish simultaneously."""
    _, st_trend = _supertrend(close, high, low, 10, 3.0)
    # Inline PSAR trend
    n = len(high); hi = high.values; lo = low.values
    ps_trend = np.full(n, np.nan)
    is_bull = True; ep = hi[0]; af = 0.02; sar_v = lo[0]; ps_trend[0] = 1.0
    for i in range(1, n):
        if is_bull:
            ns = sar_v + af * (ep - sar_v)
            ns = min(ns, lo[i - 1])
            if i >= 2: ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False; ns = ep; ep = lo[i]; af = 0.02; ps_trend[i] = -1.0
            else:
                ps_trend[i] = 1.0
                if hi[i] > ep: ep = hi[i]; af = min(af + 0.02, 0.2)
        else:
            ns = sar_v + af * (ep - sar_v)
            ns = max(ns, hi[i - 1])
            if i >= 2: ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True; ns = ep; ep = hi[i]; af = 0.02; ps_trend[i] = 1.0
            else:
                ps_trend[i] = -1.0
                if lo[i] < ep: ep = lo[i]; af = min(af + 0.02, 0.2)
        sar_v = ns
    psar_bear = pd.Series(ps_trend, index=close.index) < 0
    # Aroon Down > Aroon Up inline
    w = 15
    def _bs_high(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_low(arr):  return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_high, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_low,  raw=True)
    aroon_bear = ((14 - bsl) / 14 * 100) > ((14 - bsh) / 14 * 100)
    return ((st_trend < 0) & psar_bear & aroon_bear).astype(float)


def tbd_142_ichimoku_breakdown_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of active Ichimoku bearish states (0-4): below cloud, bear cloud, T<K, close<Kijun."""
    _, _, span_a, span_b = _ichimoku_lines(close, high, low)
    tenkan, kijun, _, _ = _ichimoku_lines(close, high, low)
    cloud_bottom = pd.concat([span_a, span_b], axis=1).min(axis=1)
    s1 = (close < cloud_bottom).astype(float)
    s2 = (span_b > span_a).astype(float)
    s3 = (tenkan < kijun).astype(float)
    s4 = (close < kijun).astype(float)
    return s1 + s2 + s3 + s4


def tbd_143_total_breakdown_state_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of active breakdown states: DC + EMA-DC + MACD-bear + DMI-bear + triple-slope-neg."""
    dc   = (_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float)
    edc  = (_ewm_mean(close, 50) < _ewm_mean(close, 200)).astype(float)
    mb   = ((_ewm_mean(close, 12) - _ewm_mean(close, 26)) < 0).astype(float)
    _, di_p, di_m = _adx_components(close, high, low, 14)
    dmi  = (di_m > di_p).astype(float)
    sma20  = _rolling_mean(close, _TD_MON)
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    slp  = ((sma20 < sma20.shift(1)) & (sma50 < sma50.shift(1)) & (sma200 < sma200.shift(1))).astype(float)
    return dc + edc + mb + dmi + slp


def tbd_144_breakdown_score_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pct rank of breakdown state count in trailing 252-day distribution."""
    score = tbd_143_total_breakdown_state_count(close, high, low)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tbd_145_days_in_full_breakdown_state(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days all 5 breakdown states simultaneously active."""
    return _consec_streak(tbd_143_total_breakdown_state_count(close, high, low) >= 5)


def tbd_146_total_bearish_sma_cross_252d(close: pd.Series) -> pd.Series:
    """Total SMA bearish crossover count (5/20 + 20/50 + 50/200) in 252 days."""
    s5   = _rolling_mean(close, _TD_WEEK)
    s20  = _rolling_mean(close, _TD_MON)
    s50  = _rolling_mean(close, 50)
    s200 = _rolling_mean(close, 200)
    b1 = s5 < s20; b2 = s20 < s50; b3 = s50 < s200
    e1 = (b1 & ~b1.shift(1).fillna(False)).astype(float)
    e2 = (b2 & ~b2.shift(1).fillna(False)).astype(float)
    e3 = (b3 & ~b3.shift(1).fillna(False)).astype(float)
    return _rolling_sum(e1 + e2 + e3, _TD_YEAR)


def tbd_147_breakdown_event_count_63d_all_types(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Total count of all bearish crossover events (SMA + EMA + MACD + DMI) in 63 days."""
    s5  = _rolling_mean(close, _TD_WEEK); s20 = _rolling_mean(close, _TD_MON)
    s50 = _rolling_mean(close, 50);      s200 = _rolling_mean(close, 200)
    e12 = _ewm_mean(close, 12);          e26  = _ewm_mean(close, 26)
    e50 = _ewm_mean(close, 50)
    macd = e12 - e26; sig = _ewm_mean(macd, 9)
    _, di_p, di_m = _adx_components(close, high, low, 14)
    def _ev(b):
        return (b & ~b.shift(1).fillna(False)).astype(float)
    total = (_ev(s5 < s20) + _ev(s20 < s50) + _ev(s50 < s200) +
             _ev(e12 < e26) + _ev(e50 < _ewm_mean(close, 200)) +
             _ev(macd < sig) + _ev(di_m > di_p))
    return _rolling_sum(total, _TD_QTR)


def tbd_148_sma_fan_spread_sma20_sma200(close: pd.Series) -> pd.Series:
    """SMA20 minus SMA200 divided by SMA200 (negative = fan breakdown below)."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma200 = _rolling_mean(close, 200)
    return _safe_div(sma20 - sma200, sma200)


def tbd_149_all_breakdown_composite_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: death cross + MACD bearish + DI->DI+ all simultaneously."""
    dc   = (_rolling_mean(close, 50) < _rolling_mean(close, 200))
    macd_bear = (_ewm_mean(close, 12) < _ewm_mean(close, 26))
    _, di_p, di_m = _adx_components(close, high, low, 14)
    dmi_bear = di_m > di_p
    return (dc & macd_bear & dmi_bear).astype(float)


def tbd_150_master_breakdown_index(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite breakdown index: state count * (1 + event density), z-scored 252d."""
    states = tbd_143_total_breakdown_state_count(close, high, low)
    events = tbd_147_breakdown_event_count_63d_all_types(close, high, low)
    raw    = states * (1.0 + events)
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_REGISTRY_076_150 = {
    "tbd_076_macd_histogram_depth_21d_min": {"inputs": ["close"], "func": tbd_076_macd_histogram_depth_21d_min},
    "tbd_077_macd_histogram_depth_63d_min": {"inputs": ["close"], "func": tbd_077_macd_histogram_depth_63d_min},
    "tbd_078_macd_histogram_neg_fraction_63d": {"inputs": ["close"], "func": tbd_078_macd_histogram_neg_fraction_63d},
    "tbd_079_macd_line_neg_streak": {"inputs": ["close"], "func": tbd_079_macd_line_neg_streak},
    "tbd_080_macd_cross_count_63d": {"inputs": ["close"], "func": tbd_080_macd_cross_count_63d},
    "tbd_081_macd_histogram_slope_negative_flag": {"inputs": ["close"], "func": tbd_081_macd_histogram_slope_negative_flag},
    "tbd_082_macd_signal_below_zero_flag": {"inputs": ["close"], "func": tbd_082_macd_signal_below_zero_flag},
    "tbd_083_macd_both_lines_below_zero_flag": {"inputs": ["close"], "func": tbd_083_macd_both_lines_below_zero_flag},
    "tbd_084_macd_histogram_zscore_63d": {"inputs": ["close"], "func": tbd_084_macd_histogram_zscore_63d},
    "tbd_085_days_since_macd_line_crossed_zero_neg": {"inputs": ["close"], "func": tbd_085_days_since_macd_line_crossed_zero_neg},
    "tbd_086_adx20_below_25_flag": {"inputs": ["close", "high", "low"], "func": tbd_086_adx20_below_25_flag},
    "tbd_087_adx14_neg_slope_streak": {"inputs": ["close", "high", "low"], "func": tbd_087_adx14_neg_slope_streak},
    "tbd_088_adx14_below_15_flag": {"inputs": ["close", "high", "low"], "func": tbd_088_adx14_below_15_flag},
    "tbd_089_dmi_bearish_cross_count_252d": {"inputs": ["close", "high", "low"], "func": tbd_089_dmi_bearish_cross_count_252d},
    "tbd_090_dmi_bearish_streak": {"inputs": ["close", "high", "low"], "func": tbd_090_dmi_bearish_streak},
    "tbd_091_adx14_collapse_from_peak_252d": {"inputs": ["close", "high", "low"], "func": tbd_091_adx14_collapse_from_peak_252d},
    "tbd_092_dmi_spread_di_minus_minus_di_plus": {"inputs": ["close", "high", "low"], "func": tbd_092_dmi_spread_di_minus_minus_di_plus},
    "tbd_093_dmi_spread_zscore_252d": {"inputs": ["close", "high", "low"], "func": tbd_093_dmi_spread_zscore_252d},
    "tbd_094_adx14_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": tbd_094_adx14_pct_rank_252d},
    "tbd_095_adx_dmi_event_density_63d": {"inputs": ["close", "high", "low"], "func": tbd_095_adx_dmi_event_density_63d},
    "tbd_096_sma20_slope_1d": {"inputs": ["close"], "func": tbd_096_sma20_slope_1d},
    "tbd_097_sma50_slope_1d": {"inputs": ["close"], "func": tbd_097_sma50_slope_1d},
    "tbd_098_sma200_slope_1d": {"inputs": ["close"], "func": tbd_098_sma200_slope_1d},
    "tbd_099_ema12_slope_1d": {"inputs": ["close"], "func": tbd_099_ema12_slope_1d},
    "tbd_100_ema26_slope_1d": {"inputs": ["close"], "func": tbd_100_ema26_slope_1d},
    "tbd_101_sma20_slope_rolling_avg_21d": {"inputs": ["close"], "func": tbd_101_sma20_slope_rolling_avg_21d},
    "tbd_102_sma200_slope_rolling_avg_63d": {"inputs": ["close"], "func": tbd_102_sma200_slope_rolling_avg_63d},
    "tbd_103_sma50_neg_slope_streak": {"inputs": ["close"], "func": tbd_103_sma50_neg_slope_streak},
    "tbd_104_ema12_neg_slope_streak": {"inputs": ["close"], "func": tbd_104_ema12_neg_slope_streak},
    "tbd_105_all_ema_slopes_negative_flag": {"inputs": ["close"], "func": tbd_105_all_ema_slopes_negative_flag},
    "tbd_106_hh_hl_streak": {"inputs": ["close", "high", "low"], "func": tbd_106_hh_hl_streak},
    "tbd_107_lh_ll_streak": {"inputs": ["close", "high", "low"], "func": tbd_107_lh_ll_streak},
    "tbd_108_lh_ll_streak_max_63d": {"inputs": ["close", "high", "low"], "func": tbd_108_lh_ll_streak_max_63d},
    "tbd_109_lh_ll_streak_max_252d": {"inputs": ["close", "high", "low"], "func": tbd_109_lh_ll_streak_max_252d},
    "tbd_110_hh_hl_fraction_252d": {"inputs": ["close", "high", "low"], "func": tbd_110_hh_hl_fraction_252d},
    "tbd_111_lh_ll_fraction_252d": {"inputs": ["close", "high", "low"], "func": tbd_111_lh_ll_fraction_252d},
    "tbd_112_structure_net_score_21d": {"inputs": ["close", "high", "low"], "func": tbd_112_structure_net_score_21d},
    "tbd_113_days_since_last_hh_hl": {"inputs": ["close", "high", "low"], "func": tbd_113_days_since_last_hh_hl},
    "tbd_114_higher_high_count_21d": {"inputs": ["close", "high"], "func": tbd_114_higher_high_count_21d},
    "tbd_115_lower_low_count_21d": {"inputs": ["close", "low"], "func": tbd_115_lower_low_count_21d},
    "tbd_116_supertrend_bearish_flag": {"inputs": ["close", "high", "low"], "func": tbd_116_supertrend_bearish_flag},
    "tbd_117_supertrend_flip_to_bearish_event": {"inputs": ["close", "high", "low"], "func": tbd_117_supertrend_flip_to_bearish_event},
    "tbd_118_supertrend_bars_in_downtrend": {"inputs": ["close", "high", "low"], "func": tbd_118_supertrend_bars_in_downtrend},
    "tbd_119_supertrend_bars_since_bearish_flip": {"inputs": ["close", "high", "low"], "func": tbd_119_supertrend_bars_since_bearish_flip},
    "tbd_120_supertrend_distance_from_price": {"inputs": ["close", "high", "low"], "func": tbd_120_supertrend_distance_from_price},
    "tbd_121_supertrend_bearish_fraction_63d": {"inputs": ["close", "high", "low"], "func": tbd_121_supertrend_bearish_fraction_63d},
    "tbd_122_supertrend_flip_count_63d": {"inputs": ["close", "high", "low"], "func": tbd_122_supertrend_flip_count_63d},
    "tbd_123_supertrend_distance_zscore_63d": {"inputs": ["close", "high", "low"], "func": tbd_123_supertrend_distance_zscore_63d},
    "tbd_124_supertrend_and_psar_both_bearish_flag": {"inputs": ["close", "high", "low"], "func": tbd_124_supertrend_and_psar_both_bearish_flag},
    "tbd_125_supertrend_bearish_streak_max_252d": {"inputs": ["close", "high", "low"], "func": tbd_125_supertrend_bearish_streak_max_252d},
    "tbd_126_ichimoku_price_below_cloud_flag": {"inputs": ["close", "high", "low"], "func": tbd_126_ichimoku_price_below_cloud_flag},
    "tbd_127_ichimoku_price_above_cloud_flag": {"inputs": ["close", "high", "low"], "func": tbd_127_ichimoku_price_above_cloud_flag},
    "tbd_128_ichimoku_tenkan_below_kijun_flag": {"inputs": ["close", "high", "low"], "func": tbd_128_ichimoku_tenkan_below_kijun_flag},
    "tbd_129_ichimoku_tenkan_kijun_bearish_cross_event": {"inputs": ["close", "high", "low"], "func": tbd_129_ichimoku_tenkan_kijun_bearish_cross_event},
    "tbd_130_ichimoku_days_since_tenkan_kijun_bearish_cross": {"inputs": ["close", "high", "low"], "func": tbd_130_ichimoku_days_since_tenkan_kijun_bearish_cross},
    "tbd_131_ichimoku_close_vs_tenkan_distance": {"inputs": ["close", "high", "low"], "func": tbd_131_ichimoku_close_vs_tenkan_distance},
    "tbd_132_ichimoku_close_vs_kijun_distance": {"inputs": ["close", "high", "low"], "func": tbd_132_ichimoku_close_vs_kijun_distance},
    "tbd_133_ichimoku_distance_below_cloud": {"inputs": ["close", "high", "low"], "func": tbd_133_ichimoku_distance_below_cloud},
    "tbd_134_ichimoku_cloud_bearish_flag": {"inputs": ["close", "high", "low"], "func": tbd_134_ichimoku_cloud_bearish_flag},
    "tbd_135_ichimoku_close_below_tenkan_flag": {"inputs": ["close", "high", "low"], "func": tbd_135_ichimoku_close_below_tenkan_flag},
    "tbd_136_ichimoku_close_below_kijun_flag": {"inputs": ["close", "high", "low"], "func": tbd_136_ichimoku_close_below_kijun_flag},
    "tbd_137_ichimoku_close_below_spana_flag": {"inputs": ["close", "high", "low"], "func": tbd_137_ichimoku_close_below_spana_flag},
    "tbd_138_ichimoku_close_below_spanb_flag": {"inputs": ["close", "high", "low"], "func": tbd_138_ichimoku_close_below_spanb_flag},
    "tbd_139_ichimoku_bearish_cross_count_252d": {"inputs": ["close", "high", "low"], "func": tbd_139_ichimoku_bearish_cross_count_252d},
    "tbd_140_ichimoku_below_cloud_streak": {"inputs": ["close", "high", "low"], "func": tbd_140_ichimoku_below_cloud_streak},
    "tbd_141_supertrend_psar_aroon_bearish_flag": {"inputs": ["close", "high", "low"], "func": tbd_141_supertrend_psar_aroon_bearish_flag},
    "tbd_142_ichimoku_breakdown_score": {"inputs": ["close", "high", "low"], "func": tbd_142_ichimoku_breakdown_score},
    "tbd_143_total_breakdown_state_count": {"inputs": ["close", "high", "low"], "func": tbd_143_total_breakdown_state_count},
    "tbd_144_breakdown_score_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": tbd_144_breakdown_score_pct_rank_252d},
    "tbd_145_days_in_full_breakdown_state": {"inputs": ["close", "high", "low"], "func": tbd_145_days_in_full_breakdown_state},
    "tbd_146_total_bearish_sma_cross_252d": {"inputs": ["close"], "func": tbd_146_total_bearish_sma_cross_252d},
    "tbd_147_breakdown_event_count_63d_all_types": {"inputs": ["close", "high", "low"], "func": tbd_147_breakdown_event_count_63d_all_types},
    "tbd_148_sma_fan_spread_sma20_sma200": {"inputs": ["close"], "func": tbd_148_sma_fan_spread_sma20_sma200},
    "tbd_149_all_breakdown_composite_flag": {"inputs": ["close", "high", "low"], "func": tbd_149_all_breakdown_composite_flag},
    "tbd_150_master_breakdown_index": {"inputs": ["close", "high", "low"], "func": tbd_150_master_breakdown_index},
}
