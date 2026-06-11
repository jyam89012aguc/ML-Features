"""session_open_close_dynamics d3 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Heikin-Ashi states / multi-bar candlestick patterns (engulfing, harami, stars, crows,
3-line-strike, tweezers) / Marubozu / specialty doji (gravestone, dragonfly) /
pivot points (Floor, Camarilla, Fibonacci) / Ease of Movement / Klinger / NVI/PVI /
range-overlap / inside-outside-day streaks.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _heikin_ashi(open_, high, low, close):
    """Heikin-Ashi candles. HA_close = (O+H+L+C)/4. HA_open = (HA_open[t-1]+HA_close[t-1])/2.
    HA_high = max(H, HA_open, HA_close). HA_low = min(L, HA_open, HA_close).
    Returns (ha_open, ha_high, ha_low, ha_close)."""
    ha_close = (open_ + high + low + close) / 4.0
    arr_o = open_.values.astype(float)
    arr_c = close.values.astype(float)
    arr_hac = ha_close.values
    n = len(close)
    ha_open_arr = np.full(n, np.nan)
    for i in range(n):
        if i == 0 or np.isnan(arr_o[i]) or np.isnan(arr_c[i]):
            ha_open_arr[i] = (arr_o[i] + arr_c[i]) / 2.0 if (not np.isnan(arr_o[i]) and not np.isnan(arr_c[i])) else np.nan
        else:
            prev_open = ha_open_arr[i-1] if not np.isnan(ha_open_arr[i-1]) else (arr_o[i-1] + arr_c[i-1]) / 2.0
            prev_close = arr_hac[i-1] if not np.isnan(arr_hac[i-1]) else (arr_o[i-1] + arr_c[i-1]) / 2.0
            ha_open_arr[i] = (prev_open + prev_close) / 2.0
    ha_open = pd.Series(ha_open_arr, index=open_.index)
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return ha_open, ha_high, ha_low, ha_close


def _floor_pivot_levels(high, low, close):
    """Classic Floor Pivot Points using prior bar. PP, S1, S2, R1, R2."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pp - low.shift(1)
    s1 = 2.0 * pp - high.shift(1)
    r2 = pp + (high.shift(1) - low.shift(1))
    s2 = pp - (high.shift(1) - low.shift(1))
    return pp, s1, s2, r1, r2


def _camarilla_levels(high, low, close):
    """Camarilla Pivots: H4, H3, L3, L4 (most-used). Using prior bar."""
    rng = high.shift(1) - low.shift(1)
    h4 = close.shift(1) + rng * 1.1 / 2.0
    h3 = close.shift(1) + rng * 1.1 / 4.0
    l3 = close.shift(1) - rng * 1.1 / 4.0
    l4 = close.shift(1) - rng * 1.1 / 2.0
    return h4, h3, l3, l4


def _fibonacci_pivots(high, low, close):
    """Fibonacci pivots: PP, R1, R2, S1, S2 using 0.382 and 0.618 levels of prior range."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    rng = high.shift(1) - low.shift(1)
    r1 = pp + 0.382 * rng
    r2 = pp + 0.618 * rng
    s1 = pp - 0.382 * rng
    s2 = pp - 0.618 * rng
    return pp, s1, s2, r1, r2


def f46_socd_151_ha_body_logclose_logopen_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    out = _safe_log(ha_close) - _safe_log(ha_open)
    return out.diff().diff().diff()


def f46_socd_152_ha_bullish_indicator_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    out = (ha_close > ha_open).astype(float).where(ha_open.notna() & ha_close.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_153_ha_bearish_indicator_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    out = (ha_close < ha_open).astype(float).where(ha_open.notna() & ha_close.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_154_consec_ha_bullish_streak_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(int).where(ha_open.notna() & ha_close.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    out = (st * (b > 0)).where(ha_open.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_155_consec_ha_bearish_streak_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close < ha_open).astype(int).where(ha_open.notna() & ha_close.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    out = (st * (b > 0)).where(ha_open.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_156_ha_bull_flip_event_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float)
    out = ((b.shift(1) < 0.5) & (b > 0.5)).astype(float).where(ha_open.notna() & ha_open.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_157_ha_bear_flip_event_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float)
    out = ((b.shift(1) > 0.5) & (b < 0.5)).astype(float).where(ha_open.notna() & ha_open.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_158_ha_color_flip_count_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float)
    fl = (b != b.shift(1)).astype(float).where(ha_open.notna() & ha_open.shift(1).notna(), np.nan)
    out = fl.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_159_ha_doji_indicator_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    body = (ha_close - ha_open).abs()
    rng = ha_high - ha_low
    out = (_safe_div(body, rng) < 0.1).astype(float).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_160_ha_no_lower_wick_bull_indicator_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float)
    out = ((ha_low >= ha_open * 0.9999) & (b > 0.5)).astype(float).where(ha_open.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_161_ha_no_upper_wick_bear_indicator_1d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close < ha_open).astype(float)
    out = ((ha_high <= ha_open * 1.0001) & (b > 0.5)).astype(float).where(ha_open.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_162_ha_bullish_fraction_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float).where(ha_open.notna() & ha_close.notna(), np.nan)
    out = b.rolling(21, min_periods=7).mean()
    return out.diff().diff().diff()


def f46_socd_163_ha_body_size_zscore_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    bs = (ha_close - ha_open).abs()
    out = _rolling_zscore(bs, 63, min_periods=21)
    return out.diff().diff().diff()


def f46_socd_164_ha_doji_after_5bull_streak_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(int).where(ha_open.notna(), 0)
    block = (b != b.shift(1)).fillna(False).cumsum()
    st = b.groupby(block).cumcount().astype(float)
    bull5 = ((st * (b > 0)).shift(1) >= 5).astype(float)
    body = (ha_close - ha_open).abs(); rng = ha_high - ha_low
    doji = (_safe_div(body, rng) < 0.15).astype(float)
    out = (bull5 * doji).where(ha_open.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_165_longest_ha_bullish_streak_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_open, ha_high, ha_low, ha_close = _heikin_ashi(open, high, low, close)
    b = (ha_close > ha_open).astype(float).where(ha_open.notna() & ha_close.notna(), np.nan)
    def _ms(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        best = 0; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = b.rolling(63, min_periods=21).apply(_ms, raw=True)
    return out.diff().diff().diff()


def f46_socd_166_bullish_engulfing_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bull = (close > open).astype(float)
    prev_bear = (close.shift(1) < open.shift(1)).astype(float)
    engulf = ((open <= close.shift(1)) & (close >= open.shift(1))).astype(float)
    out = (today_bull * prev_bear * engulf).where(open.notna() & close.notna() & open.shift(1).notna() & close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_167_bearish_engulfing_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bear = (close < open).astype(float)
    prev_bull = (close.shift(1) > open.shift(1)).astype(float)
    engulf = ((open >= close.shift(1)) & (close <= open.shift(1))).astype(float)
    out = (today_bear * prev_bull * engulf).where(open.notna() & close.notna() & open.shift(1).notna() & close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_168_bullish_engulfing_count_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bull = (close > open).astype(float)
    prev_bear = (close.shift(1) < open.shift(1)).astype(float)
    engulf = ((open <= close.shift(1)) & (close >= open.shift(1))).astype(float)
    ev = (today_bull * prev_bear * engulf).where(open.shift(1).notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_169_bearish_engulfing_count_21d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bear = (close < open).astype(float)
    prev_bull = (close.shift(1) > open.shift(1)).astype(float)
    engulf = ((open >= close.shift(1)) & (close <= open.shift(1))).astype(float)
    ev = (today_bear * prev_bull * engulf).where(open.shift(1).notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_170_bullish_harami_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bull = (close > open).astype(float)
    prev_bear = (close.shift(1) < open.shift(1)).astype(float)
    today_body = (close - open).abs()
    prev_body = (close.shift(1) - open.shift(1)).abs()
    smaller = (today_body < prev_body).astype(float)
    inside = ((open >= close.shift(1)) & (close <= open.shift(1))).astype(float)
    out = (today_bull * prev_bear * smaller * inside).where(open.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_171_bearish_harami_1d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    today_bear = (close < open).astype(float)
    prev_bull = (close.shift(1) > open.shift(1)).astype(float)
    today_body = (close - open).abs()
    prev_body = (close.shift(1) - open.shift(1)).abs()
    smaller = (today_body < prev_body).astype(float)
    inside = ((open <= close.shift(1)) & (close >= open.shift(1))).astype(float)
    out = (today_bear * prev_bull * smaller * inside).where(open.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_172_morning_star_3bar_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, n=21)
    big_bear_d2 = ((open.shift(2) - close.shift(2)) > 0.5 * atr).astype(float)
    small_body_d1 = ((close.shift(1) - open.shift(1)).abs() < 0.3 * atr).astype(float)
    gap_down_d1 = (pd.concat([open.shift(1), close.shift(1)], axis=1).max(axis=1) < close.shift(2)).astype(float)
    bull_d0 = (close > open).astype(float)
    close_above_mid = (close > (open.shift(2) + close.shift(2)) / 2.0).astype(float)
    out = (big_bear_d2 * small_body_d1 * gap_down_d1 * bull_d0 * close_above_mid).where(atr.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_173_evening_star_3bar_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, n=21)
    big_bull_d2 = ((close.shift(2) - open.shift(2)) > 0.5 * atr).astype(float)
    small_body_d1 = ((close.shift(1) - open.shift(1)).abs() < 0.3 * atr).astype(float)
    gap_up_d1 = (pd.concat([open.shift(1), close.shift(1)], axis=1).min(axis=1) > close.shift(2)).astype(float)
    bear_d0 = (close < open).astype(float)
    close_below_mid = (close < (open.shift(2) + close.shift(2)) / 2.0).astype(float)
    out = (big_bull_d2 * small_body_d1 * gap_up_d1 * bear_d0 * close_below_mid).where(atr.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_174_three_white_soldiers_indicator_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    b0 = (close > open).astype(float)
    b1 = (close.shift(1) > open.shift(1)).astype(float)
    b2 = (close.shift(2) > open.shift(2)).astype(float)
    higher = ((close > close.shift(1)) & (close.shift(1) > close.shift(2))).astype(float)
    body_grow = ((close - open) > 0.3 * (close.shift(1) - open.shift(1))).astype(float)
    out = (b0 * b1 * b2 * higher).where(open.shift(2).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_175_three_black_crows_indicator_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    b0 = (close < open).astype(float)
    b1 = (close.shift(1) < open.shift(1)).astype(float)
    b2 = (close.shift(2) < open.shift(2)).astype(float)
    lower = ((close < close.shift(1)) & (close.shift(1) < close.shift(2))).astype(float)
    out = (b0 * b1 * b2 * lower).where(open.shift(2).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_176_three_line_strike_bull_indicator_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    b1 = (close.shift(1) < open.shift(1)).astype(float)
    b2 = (close.shift(2) < open.shift(2)).astype(float)
    b3 = (close.shift(3) < open.shift(3)).astype(float)
    bull_d0 = ((close > open) & (close > open.shift(3))).astype(float)
    out = (b1 * b2 * b3 * bull_d0).where(open.shift(3).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_177_three_line_strike_bear_indicator_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    b1 = (close.shift(1) > open.shift(1)).astype(float)
    b2 = (close.shift(2) > open.shift(2)).astype(float)
    b3 = (close.shift(3) > open.shift(3)).astype(float)
    bear_d0 = ((close < open) & (close < open.shift(3))).astype(float)
    out = (b1 * b2 * b3 * bear_d0).where(open.shift(3).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_178_tweezers_top_indicator_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    same_high = ((high - high.shift(1)).abs() < 0.001 * close).astype(float)
    prev_bull = (close.shift(1) > close.shift(2)).astype(float)
    bear_d0 = (close < close.shift(1)).astype(float)
    out = (same_high * prev_bull * bear_d0).where(high.shift(2).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_179_tweezers_bottom_indicator_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    same_low = ((low - low.shift(1)).abs() < 0.001 * close).astype(float)
    prev_bear = (close.shift(1) < close.shift(2)).astype(float)
    bull_d0 = (close > close.shift(1)).astype(float)
    out = (same_low * prev_bear * bull_d0).where(low.shift(2).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_180_piercing_line_indicator_d3(open: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_bear = (close.shift(1) < open.shift(1)).astype(float)
    open_below_prev_low = (open < low.shift(1)).astype(float)
    close_above_prev_mid = (close > (open.shift(1) + close.shift(1)) / 2.0).astype(float)
    close_below_prev_open = (close < open.shift(1)).astype(float)
    out = (prev_bear * open_below_prev_low * close_above_prev_mid * close_below_prev_open).where(close.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_181_bullish_marubozu_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open).abs()
    body_share = _safe_div(body, rng)
    bull = (close > open).astype(float)
    out = ((body_share > 0.95) * bull).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_182_bearish_marubozu_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open).abs()
    body_share = _safe_div(body, rng)
    bear = (close < open).astype(float)
    out = ((body_share > 0.95) * bear).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_183_marubozu_count_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open).abs()
    body_share = _safe_div(body, rng)
    mar = (body_share > 0.95).astype(float).where(rng.notna() & body.notna(), np.nan)
    out = mar.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_184_marubozu_count_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open).abs()
    body_share = _safe_div(body, rng)
    mar = (body_share > 0.95).astype(float).where(rng.notna() & body.notna(), np.nan)
    out = mar.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_185_gravestone_doji_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    low_body = _safe_div(pd.concat([open, close], axis=1).min(axis=1) - low, rng)
    body_at_low = (low_body < 0.1).astype(float)
    long_uw = (_safe_div(high - pd.concat([open, close], axis=1).max(axis=1), rng) > 0.6).astype(float)
    out = (doji * body_at_low * long_uw).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_186_dragonfly_doji_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    high_body = _safe_div(high - pd.concat([open, close], axis=1).max(axis=1), rng)
    body_at_high = (high_body < 0.1).astype(float)
    long_lw = (_safe_div(pd.concat([open, close], axis=1).min(axis=1) - low, rng) > 0.6).astype(float)
    out = (doji * body_at_high * long_lw).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_187_long_legged_doji_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1); lb = pd.concat([open, close], axis=1).min(axis=1)
    long_uw = (_safe_div(high - ub, rng) > 0.3).astype(float)
    long_lw = (_safe_div(lb - low, rng) > 0.3).astype(float)
    out = (doji * long_uw * long_lw).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_188_spinning_top_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    small = (_safe_div(body, rng) < 0.3).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1); lb = pd.concat([open, close], axis=1).min(axis=1)
    big_uw = ((high - ub) > body).astype(float)
    big_lw = ((lb - low) > body).astype(float)
    out = (small * big_uw * big_lw).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_189_gravestone_at_252d_high_composite_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    low_body = _safe_div(pd.concat([open, close], axis=1).min(axis=1) - low, rng)
    body_at_low = (low_body < 0.1).astype(float)
    long_uw = (_safe_div(high - pd.concat([open, close], axis=1).max(axis=1), rng) > 0.6).astype(float)
    gs = (doji * body_at_low * long_uw)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (gs * at_high).where(rng.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_190_long_legged_doji_count_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1); lb = pd.concat([open, close], axis=1).min(axis=1)
    long_uw = (_safe_div(high - ub, rng) > 0.3).astype(float)
    long_lw = (_safe_div(lb - low, rng) > 0.3).astype(float)
    ev = (doji * long_uw * long_lw).where(rng.notna() & body.notna(), np.nan)
    out = ev.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_191_bear_minus_bull_marubozu_count_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low; body = (close - open).abs()
    bs = _safe_div(body, rng)
    bull_m = ((bs > 0.95) & (close > open)).astype(float).where(rng.notna() & body.notna(), np.nan)
    bear_m = ((bs > 0.95) & (close < open)).astype(float).where(rng.notna() & body.notna(), np.nan)
    out = bear_m.rolling(63, min_periods=21).sum() - bull_m.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_192_bull_marubozu_at_252d_high_composite_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low; body = (close - open).abs()
    bs = _safe_div(body, rng)
    bm = ((bs > 0.95) & (close > open)).astype(float)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    out = (bm * at_high).where(rng.notna() & body.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_193_spinning_top_count_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    small = (_safe_div(body, rng) < 0.3).astype(float)
    ub = pd.concat([open, close], axis=1).max(axis=1); lb = pd.concat([open, close], axis=1).min(axis=1)
    big_uw = ((high - ub) > body).astype(float)
    big_lw = ((lb - low) > body).astype(float)
    st = (small * big_uw * big_lw).where(rng.notna() & body.notna(), np.nan)
    out = st.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_194_dragonfly_at_252d_low_composite_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open).abs(); rng = high - low
    doji = (_safe_div(body, rng) < 0.1).astype(float)
    high_body = _safe_div(high - pd.concat([open, close], axis=1).max(axis=1), rng)
    body_at_high = (high_body < 0.1).astype(float)
    long_lw = (_safe_div(pd.concat([open, close], axis=1).min(axis=1) - low, rng) > 0.6).astype(float)
    df = (doji * body_at_high * long_lw)
    rmin = low.rolling(252, min_periods=84).min()
    at_low = (low <= 1.05 * rmin).astype(float)
    out = (df * at_low).where(rng.notna() & rmin.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_195_bear_marubozu_after_5_bull_streak_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low; body = (close - open).abs()
    bs = _safe_div(body, rng)
    bm = ((bs > 0.95) & (close < open)).astype(float)
    bull = (close > open).astype(int).where(close.notna() & open.notna(), 0)
    block = (bull != bull.shift(1)).fillna(False).cumsum()
    st = bull.groupby(block).cumcount().astype(float)
    bull5 = ((st * (bull > 0)).shift(1) >= 5).astype(float)
    out = (bm * bull5).where(rng.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_196_close_minus_floor_pp_pct_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = _safe_div(close - pp, close)
    return out.diff().diff().diff()


def f46_socd_197_close_minus_floor_r1_pct_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = _safe_div(close - r1, close)
    return out.diff().diff().diff()


def f46_socd_198_close_minus_floor_s1_pct_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = _safe_div(close - s1, close)
    return out.diff().diff().diff()


def f46_socd_199_close_above_floor_r1_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = (close > r1).astype(float).where(r1.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_200_close_below_floor_s1_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = (close < s1).astype(float).where(s1.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_201_close_above_floor_r2_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = (close > r2).astype(float).where(r2.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_202_close_below_floor_s2_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    out = (close < s2).astype(float).where(s2.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_203_close_above_camarilla_h4_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h4, h3, l3, l4 = _camarilla_levels(high, low, close)
    out = (close > h4).astype(float).where(h4.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_204_close_below_camarilla_l4_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h4, h3, l3, l4 = _camarilla_levels(high, low, close)
    out = (close < l4).astype(float).where(l4.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_205_close_minus_camarilla_h3_pct_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h4, h3, l3, l4 = _camarilla_levels(high, low, close)
    out = _safe_div(close - h3, close)
    return out.diff().diff().diff()


def f46_socd_206_close_outside_camarilla_h4_l4_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h4, h3, l3, l4 = _camarilla_levels(high, low, close)
    out = ((close > h4) | (close < l4)).astype(float).where(h4.notna() & l4.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_207_close_minus_fib_r1_pct_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _fibonacci_pivots(high, low, close)
    out = _safe_div(close - r1, close)
    return out.diff().diff().diff()


def f46_socd_208_close_above_fib_r2_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _fibonacci_pivots(high, low, close)
    out = (close > r2).astype(float).where(r2.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_209_floor_r1_break_count_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    ev = (close > r1).astype(float).where(r1.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_210_floor_s1_break_count_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pp, s1, s2, r1, r2 = _floor_pivot_levels(high, low, close)
    ev = (close < s1).astype(float).where(s1.notna(), np.nan)
    out = ev.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_211_ease_of_movement_arms_emv_1d_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    emv = (mid - mid.shift(1)) * (high - low) / volume.replace(0, np.nan)
    out = emv
    return out.diff().diff().diff()


def f46_socd_212_ease_of_movement_14d_mean_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    emv = (mid - mid.shift(1)) * (high - low) / volume.replace(0, np.nan)
    out = emv.rolling(14, min_periods=5).mean()
    return out.diff().diff().diff()


def f46_socd_213_klinger_volume_osc_simplified_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    sgn = np.sign(tp - tp.shift(1))
    vf = volume * sgn
    out = vf.ewm(span=34, adjust=False).mean() - vf.ewm(span=55, adjust=False).mean()
    return out.diff().diff().diff()


def f46_socd_214_klinger_volume_osc_signal_trigger_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    sgn = np.sign(tp - tp.shift(1))
    vf = volume * sgn
    kvo = vf.ewm(span=34, adjust=False).mean() - vf.ewm(span=55, adjust=False).mean()
    out = kvo - kvo.ewm(span=13, adjust=False).mean()
    return out.diff().diff().diff()


def f46_socd_215_neg_volume_index_pct_change_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    vol_down = (volume < volume.shift(1)).astype(float)
    nvi_step = (r * vol_down).fillna(0)
    nvi = nvi_step.cumsum()
    out = nvi - nvi.shift(252)
    return out.diff().diff().diff()


def f46_socd_216_pos_volume_index_pct_change_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    vol_up = (volume > volume.shift(1)).astype(float)
    pvi_step = (r * vol_up).fillna(0)
    pvi = pvi_step.cumsum()
    out = pvi - pvi.shift(252)
    return out.diff().diff().diff()


def f46_socd_217_nvi_minus_pvi_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    vd = (volume < volume.shift(1)).astype(float); vu = (volume > volume.shift(1)).astype(float)
    nvi = (r * vd).fillna(0).cumsum()
    pvi = (r * vu).fillna(0).cumsum()
    out = (nvi - nvi.shift(63)) - (pvi - pvi.shift(63))
    return out.diff().diff().diff()


def f46_socd_218_range_overlap_today_vs_prior_pct_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    ov_high = pd.concat([high, high.shift(1)], axis=1).min(axis=1)
    ov_low = pd.concat([low, low.shift(1)], axis=1).max(axis=1)
    ov = (ov_high - ov_low).clip(lower=0)
    out = _safe_div(ov, high - low)
    return out.diff().diff().diff()


def f46_socd_219_inside_day_indicator_1d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    out = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_220_outside_day_indicator_1d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    out = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_221_consec_inside_day_streak_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    i = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(int).where(high.shift(1).notna() & low.shift(1).notna(), 0)
    block = (i != i.shift(1)).fillna(False).cumsum()
    st = i.groupby(block).cumcount().astype(float)
    out = (st * (i > 0)).where(high.shift(1).notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_222_outside_day_count_21d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    o = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    out = o.rolling(21, min_periods=7).sum()
    return out.diff().diff().diff()


def f46_socd_223_inside_day_count_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    i = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float).where(high.shift(1).notna() & low.shift(1).notna(), np.nan)
    out = i.rolling(63, min_periods=21).sum()
    return out.diff().diff().diff()


def f46_socd_224_low_emv_at_252d_high_composite_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    emv = (mid - mid.shift(1)) * (high - low) / volume.replace(0, np.nan)
    emv14 = emv.rolling(14, min_periods=5).mean()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    low_emv = (emv14 < 0).astype(float)
    out = (low_emv * at_high).where(emv14.notna() & rmax.notna(), np.nan)
    return out.diff().diff().diff()


def f46_socd_225_bear_pattern_stack_at_252d_high_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low; body = (close - open).abs()
    body_share = _safe_div(body, rng)
    ub = pd.concat([open, close], axis=1).max(axis=1); lb = pd.concat([open, close], axis=1).min(axis=1)
    bm = ((body_share > 0.95) & (close < open)).astype(float)
    shooting_star = ((body_share < 0.3) & ((high - ub) > 2.0 * body) & (close < open)).astype(float).where(body.notna(), np.nan)
    low_body_pos = _safe_div(lb - low, rng)
    body_at_low = (low_body_pos < 0.1).astype(float)
    long_uw = (_safe_div(high - ub, rng) > 0.6).astype(float)
    doji = (body_share < 0.1).astype(float)
    gravestone = (doji * body_at_low * long_uw).where(rng.notna(), np.nan)
    bear_eng = (((close < open).astype(float)) * ((close.shift(1) > open.shift(1)).astype(float)) * (((open >= close.shift(1)) & (close <= open.shift(1))).astype(float))).where(open.shift(1).notna(), np.nan)
    b_crows = (((close < open).astype(float)) * ((close.shift(1) < open.shift(1)).astype(float)) * ((close.shift(2) < open.shift(2)).astype(float)) * ((close < close.shift(1)) & (close.shift(1) < close.shift(2))).astype(float)).where(open.shift(2).notna(), np.nan)
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(float)
    tot = bm + shooting_star + gravestone + bear_eng + b_crows
    out = (tot * at_high).where(rmax.notna() & body.notna(), np.nan)
    return out.diff().diff().diff()


# ============================================================
#                         REGISTRY 151_225 (d3)
# ============================================================

SESSION_OPEN_CLOSE_DYNAMICS_D3_REGISTRY_151_225 = {
    "f46_socd_151_ha_body_logclose_logopen_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_151_ha_body_logclose_logopen_1d_d3},
    "f46_socd_152_ha_bullish_indicator_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_152_ha_bullish_indicator_1d_d3},
    "f46_socd_153_ha_bearish_indicator_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_153_ha_bearish_indicator_1d_d3},
    "f46_socd_154_consec_ha_bullish_streak_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_154_consec_ha_bullish_streak_d3},
    "f46_socd_155_consec_ha_bearish_streak_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_155_consec_ha_bearish_streak_d3},
    "f46_socd_156_ha_bull_flip_event_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_156_ha_bull_flip_event_1d_d3},
    "f46_socd_157_ha_bear_flip_event_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_157_ha_bear_flip_event_1d_d3},
    "f46_socd_158_ha_color_flip_count_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_158_ha_color_flip_count_21d_d3},
    "f46_socd_159_ha_doji_indicator_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_159_ha_doji_indicator_1d_d3},
    "f46_socd_160_ha_no_lower_wick_bull_indicator_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_160_ha_no_lower_wick_bull_indicator_1d_d3},
    "f46_socd_161_ha_no_upper_wick_bear_indicator_1d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_161_ha_no_upper_wick_bear_indicator_1d_d3},
    "f46_socd_162_ha_bullish_fraction_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_162_ha_bullish_fraction_21d_d3},
    "f46_socd_163_ha_body_size_zscore_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_163_ha_body_size_zscore_63d_d3},
    "f46_socd_164_ha_doji_after_5bull_streak_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_164_ha_doji_after_5bull_streak_indicator_d3},
    "f46_socd_165_longest_ha_bullish_streak_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_165_longest_ha_bullish_streak_63d_d3},
    "f46_socd_166_bullish_engulfing_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_166_bullish_engulfing_1d_d3},
    "f46_socd_167_bearish_engulfing_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_167_bearish_engulfing_1d_d3},
    "f46_socd_168_bullish_engulfing_count_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_168_bullish_engulfing_count_21d_d3},
    "f46_socd_169_bearish_engulfing_count_21d_d3": {"inputs": ["open", "close"], "func": f46_socd_169_bearish_engulfing_count_21d_d3},
    "f46_socd_170_bullish_harami_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_170_bullish_harami_1d_d3},
    "f46_socd_171_bearish_harami_1d_d3": {"inputs": ["open", "close"], "func": f46_socd_171_bearish_harami_1d_d3},
    "f46_socd_172_morning_star_3bar_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_172_morning_star_3bar_indicator_d3},
    "f46_socd_173_evening_star_3bar_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_173_evening_star_3bar_indicator_d3},
    "f46_socd_174_three_white_soldiers_indicator_d3": {"inputs": ["open", "close"], "func": f46_socd_174_three_white_soldiers_indicator_d3},
    "f46_socd_175_three_black_crows_indicator_d3": {"inputs": ["open", "close"], "func": f46_socd_175_three_black_crows_indicator_d3},
    "f46_socd_176_three_line_strike_bull_indicator_d3": {"inputs": ["open", "close"], "func": f46_socd_176_three_line_strike_bull_indicator_d3},
    "f46_socd_177_three_line_strike_bear_indicator_d3": {"inputs": ["open", "close"], "func": f46_socd_177_three_line_strike_bear_indicator_d3},
    "f46_socd_178_tweezers_top_indicator_d3": {"inputs": ["high", "close"], "func": f46_socd_178_tweezers_top_indicator_d3},
    "f46_socd_179_tweezers_bottom_indicator_d3": {"inputs": ["low", "close"], "func": f46_socd_179_tweezers_bottom_indicator_d3},
    "f46_socd_180_piercing_line_indicator_d3": {"inputs": ["open", "low", "close"], "func": f46_socd_180_piercing_line_indicator_d3},
    "f46_socd_181_bullish_marubozu_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_181_bullish_marubozu_indicator_d3},
    "f46_socd_182_bearish_marubozu_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_182_bearish_marubozu_indicator_d3},
    "f46_socd_183_marubozu_count_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_183_marubozu_count_21d_d3},
    "f46_socd_184_marubozu_count_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_184_marubozu_count_63d_d3},
    "f46_socd_185_gravestone_doji_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_185_gravestone_doji_indicator_d3},
    "f46_socd_186_dragonfly_doji_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_186_dragonfly_doji_indicator_d3},
    "f46_socd_187_long_legged_doji_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_187_long_legged_doji_indicator_d3},
    "f46_socd_188_spinning_top_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_188_spinning_top_indicator_d3},
    "f46_socd_189_gravestone_at_252d_high_composite_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_189_gravestone_at_252d_high_composite_d3},
    "f46_socd_190_long_legged_doji_count_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_190_long_legged_doji_count_63d_d3},
    "f46_socd_191_bear_minus_bull_marubozu_count_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_191_bear_minus_bull_marubozu_count_63d_d3},
    "f46_socd_192_bull_marubozu_at_252d_high_composite_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_192_bull_marubozu_at_252d_high_composite_d3},
    "f46_socd_193_spinning_top_count_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_193_spinning_top_count_21d_d3},
    "f46_socd_194_dragonfly_at_252d_low_composite_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_194_dragonfly_at_252d_low_composite_d3},
    "f46_socd_195_bear_marubozu_after_5_bull_streak_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_195_bear_marubozu_after_5_bull_streak_d3},
    "f46_socd_196_close_minus_floor_pp_pct_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_196_close_minus_floor_pp_pct_d3},
    "f46_socd_197_close_minus_floor_r1_pct_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_197_close_minus_floor_r1_pct_d3},
    "f46_socd_198_close_minus_floor_s1_pct_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_198_close_minus_floor_s1_pct_d3},
    "f46_socd_199_close_above_floor_r1_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_199_close_above_floor_r1_indicator_d3},
    "f46_socd_200_close_below_floor_s1_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_200_close_below_floor_s1_indicator_d3},
    "f46_socd_201_close_above_floor_r2_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_201_close_above_floor_r2_indicator_d3},
    "f46_socd_202_close_below_floor_s2_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_202_close_below_floor_s2_indicator_d3},
    "f46_socd_203_close_above_camarilla_h4_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_203_close_above_camarilla_h4_indicator_d3},
    "f46_socd_204_close_below_camarilla_l4_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_204_close_below_camarilla_l4_indicator_d3},
    "f46_socd_205_close_minus_camarilla_h3_pct_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_205_close_minus_camarilla_h3_pct_d3},
    "f46_socd_206_close_outside_camarilla_h4_l4_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_206_close_outside_camarilla_h4_l4_indicator_d3},
    "f46_socd_207_close_minus_fib_r1_pct_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_207_close_minus_fib_r1_pct_d3},
    "f46_socd_208_close_above_fib_r2_indicator_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_208_close_above_fib_r2_indicator_d3},
    "f46_socd_209_floor_r1_break_count_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_209_floor_r1_break_count_21d_d3},
    "f46_socd_210_floor_s1_break_count_21d_d3": {"inputs": ["high", "low", "close"], "func": f46_socd_210_floor_s1_break_count_21d_d3},
    "f46_socd_211_ease_of_movement_arms_emv_1d_d3": {"inputs": ["high", "low", "volume"], "func": f46_socd_211_ease_of_movement_arms_emv_1d_d3},
    "f46_socd_212_ease_of_movement_14d_mean_d3": {"inputs": ["high", "low", "volume"], "func": f46_socd_212_ease_of_movement_14d_mean_d3},
    "f46_socd_213_klinger_volume_osc_simplified_d3": {"inputs": ["high", "low", "close", "volume"], "func": f46_socd_213_klinger_volume_osc_simplified_d3},
    "f46_socd_214_klinger_volume_osc_signal_trigger_d3": {"inputs": ["high", "low", "close", "volume"], "func": f46_socd_214_klinger_volume_osc_signal_trigger_d3},
    "f46_socd_215_neg_volume_index_pct_change_252d_d3": {"inputs": ["close", "volume"], "func": f46_socd_215_neg_volume_index_pct_change_252d_d3},
    "f46_socd_216_pos_volume_index_pct_change_252d_d3": {"inputs": ["close", "volume"], "func": f46_socd_216_pos_volume_index_pct_change_252d_d3},
    "f46_socd_217_nvi_minus_pvi_63d_d3": {"inputs": ["close", "volume"], "func": f46_socd_217_nvi_minus_pvi_63d_d3},
    "f46_socd_218_range_overlap_today_vs_prior_pct_d3": {"inputs": ["high", "low"], "func": f46_socd_218_range_overlap_today_vs_prior_pct_d3},
    "f46_socd_219_inside_day_indicator_1d_d3": {"inputs": ["high", "low"], "func": f46_socd_219_inside_day_indicator_1d_d3},
    "f46_socd_220_outside_day_indicator_1d_d3": {"inputs": ["high", "low"], "func": f46_socd_220_outside_day_indicator_1d_d3},
    "f46_socd_221_consec_inside_day_streak_d3": {"inputs": ["high", "low"], "func": f46_socd_221_consec_inside_day_streak_d3},
    "f46_socd_222_outside_day_count_21d_d3": {"inputs": ["high", "low"], "func": f46_socd_222_outside_day_count_21d_d3},
    "f46_socd_223_inside_day_count_63d_d3": {"inputs": ["high", "low"], "func": f46_socd_223_inside_day_count_63d_d3},
    "f46_socd_224_low_emv_at_252d_high_composite_d3": {"inputs": ["high", "low", "volume"], "func": f46_socd_224_low_emv_at_252d_high_composite_d3},
    "f46_socd_225_bear_pattern_stack_at_252d_high_d3": {"inputs": ["open", "high", "low", "close"], "func": f46_socd_225_bear_pattern_stack_at_252d_high_d3},
}
