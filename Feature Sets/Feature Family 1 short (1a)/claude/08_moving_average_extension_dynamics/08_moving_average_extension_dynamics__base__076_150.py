"""moving_average_extension_dynamics base features 076_150 — short blowup pipeline 1a-inverse.

Dynamics of price extension above/below moving averages, multi-MA structure, and extension-regime characterization.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _dema(s, span):
    e = _ema(s, span)
    return 2 * e - _ema(e, span)


def _tema(s, span):
    e1 = _ema(s, span)
    e2 = _ema(e1, span)
    e3 = _ema(e2, span)
    return 3 * e1 - 3 * e2 + e3


def _wma(s, n):
    def _calc(x):
        m = len(x)
        w = np.arange(1, m + 1, dtype=float)
        return float(np.dot(x, w) / w.sum())
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_calc, raw=True)


def _hma(s, n):
    half = max(n // 2, 1)
    sqrt_n = max(int(np.sqrt(n)), 1)
    return _wma(2 * _wma(s, half) - _wma(s, n), sqrt_n)


def _kama(s, n=21, fast=2, slow=30):
    change = s.diff(n).abs()
    volatility = s.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = (change / volatility.replace(0, np.nan)).fillna(0)
    fast_sc = 2.0 / (fast + 1)
    slow_sc = 2.0 / (slow + 1)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    out = np.full(len(s), np.nan)
    arr = s.values
    sca = sc.values
    last = np.nan
    for i in range(len(s)):
        x = arr[i]
        a = sca[i]
        if np.isnan(x):
            out[i] = last
            continue
        if np.isnan(last):
            last = x
        else:
            last = last + a * (x - last)
        out[i] = last
    return pd.Series(out, index=s.index)


def _days_since_cross(a, b):
    """Bars since a crossed b (either direction). Right-anchored, causal."""
    diff = (a - b)
    sign = np.sign(diff.fillna(0))
    cross = (sign != sign.shift(1)) & sign.shift(1).ne(0)
    idx = np.arange(len(a))
    last = np.where(cross.values, idx, np.nan)
    last = pd.Series(last, index=a.index).ffill()
    out = pd.Series(idx, index=a.index) - last
    return out


def _bb_width(s, n=20, k=2.0):
    m = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = s.rolling(n, min_periods=max(n // 3, 2)).std()
    return (2 * k * sd) / m.replace(0, np.nan)


def _bb_pctb(s, n=20, k=2.0):
    m = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = s.rolling(n, min_periods=max(n // 3, 2)).std()
    upper = m + k * sd
    lower = m - k * sd
    return _safe_div(s - lower, upper - lower)


def _keltner_pos(close, high, low, n=20, k=2.0):
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n)
    upper = m + k * atr
    lower = m - k * atr
    return _safe_div(close - lower, upper - lower)


def _donchian_pos(close, high, low, n=20):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return _safe_div(close - ll, hh - ll)

# ============================================================
#                    BASE FEATURES 076-150
# ============================================================

def f08_maed_076_bollinger_pctb_20(close: pd.Series) -> pd.Series:
    """Bollinger %B at 20d, k=2 — close position within band."""
    return _bb_pctb(close, 20, 2.0)


def f08_maed_077_bollinger_bandwidth_20(close: pd.Series) -> pd.Series:
    """Bollinger bandwidth at 20d, k=2 (upper-lower over middle)."""
    return _bb_width(close, 20, 2.0)


def f08_maed_078_bollinger_pctb_63(close: pd.Series) -> pd.Series:
    """Bollinger %B at 63d, k=2 — medium-horizon band position."""
    return _bb_pctb(close, 63, 2.0)


def f08_maed_079_bollinger_pctb_252(close: pd.Series) -> pd.Series:
    """Bollinger %B at 252d, k=2 — long-horizon band position."""
    return _bb_pctb(close, 252, 2.0)


def f08_maed_080_bollinger_bandwidth_20_pctrank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 20d Bollinger bandwidth over 504d — squeeze regime."""
    bw = _bb_width(close, 20, 2.0)
    return _rolling_pctrank(bw, 504)


def f08_maed_081_bollinger_bandwidth_20_velocity(close: pd.Series) -> pd.Series:
    """Day-over-day change in 20d Bollinger bandwidth."""
    return _bb_width(close, 20, 2.0).diff()


def f08_maed_082_keltner_pos_20_2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Keltner %position at 20d, k=2*ATR(20)."""
    return _keltner_pos(close, high, low, 20, 2.0)


def f08_maed_083_keltner_pos_63_2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Keltner %position at 63d."""
    return _keltner_pos(close, high, low, 63, 2.0)


def f08_maed_084_donchian_pos_20(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian channel position over 20d."""
    return _donchian_pos(close, high, low, 20)


def f08_maed_085_donchian_pos_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian channel position over 50d."""
    return _donchian_pos(close, high, low, 50)


def f08_maed_086_donchian_pos_252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Donchian channel position over 252d."""
    return _donchian_pos(close, high, low, 252)


def f08_maed_087_starc_pos_20(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """STARC band position (SMA(20) ± 2*ATR(15))."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    atr = _atr(high, low, close, 15)
    upper = m + 2 * atr
    lower = m - 2 * atr
    return _safe_div(close - lower, upper - lower)


def f08_maed_088_bb_top_break_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars closing above 20d Bollinger upper band over trailing 63d."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    sd = close.rolling(20, min_periods=max(20 // 3, 2)).std()
    above = (close > m + 2 * sd).astype(float)
    return above.rolling(63, min_periods=21).sum()


def f08_maed_089_bb_bottom_break_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars closing below 20d Bollinger lower band over trailing 63d."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    sd = close.rolling(20, min_periods=max(20 // 3, 2)).std()
    below = (close < m - 2 * sd).astype(float)
    return below.rolling(63, min_periods=21).sum()


def f08_maed_090_keltner_top_break_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars above Keltner upper band over 63d."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    atr = _atr(high, low, close, 20)
    above = (close > m + 2 * atr).astype(float)
    return above.rolling(63, min_periods=21).sum()


def f08_maed_091_donchian_top_break_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars closing at the 50d Donchian high over 63d."""
    hh = high.rolling(50, min_periods=max(50 // 3, 2)).max()
    touch = (close >= hh - 1e-12).astype(float)
    return touch.rolling(63, min_periods=21).sum()


def f08_maed_092_bb_pctb_max_21d(close: pd.Series) -> pd.Series:
    """Max Bollinger %B in trailing 21d — peak overshoot."""
    pb = _bb_pctb(close, 20, 2.0)
    return pb.rolling(21, min_periods=7).max()


def f08_maed_093_bb_bandwidth_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 20d Bollinger bandwidth within 504d."""
    bw = _bb_width(close, 20, 2.0)
    return _rolling_zscore(bw, 504)


def f08_maed_094_days_since_bb_bandwidth_max_252d(close: pd.Series) -> pd.Series:
    """Bars since Bollinger bandwidth reached its 252d max."""
    bw = _bb_width(close, 20, 2.0)
    def _b(w):
        return (len(w) - 1) - int(np.argmax(w))
    return bw.rolling(252, min_periods=63).apply(_b, raw=True)


def f08_maed_095_days_since_bb_bandwidth_min_252d(close: pd.Series) -> pd.Series:
    """Bars since Bollinger bandwidth reached its 252d min (squeeze freshness)."""
    bw = _bb_width(close, 20, 2.0)
    def _b(w):
        return (len(w) - 1) - int(np.argmin(w))
    return bw.rolling(252, min_periods=63).apply(_b, raw=True)


def f08_maed_096_bb_pctb_above_1_streak_max_63d(close: pd.Series) -> pd.Series:
    """Max consecutive days with %B > 1 in trailing 63d — overshoot persistence."""
    pb = _bb_pctb(close, 20, 2.0)
    above = (pb > 1).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.rolling(63, min_periods=21).max().astype(float)


def f08_maed_097_bb_pctb_above_08_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with %B > 0.8 — near-upper-band crowding."""
    pb = _bb_pctb(close, 20, 2.0)
    above = (pb > 0.8).astype(float)
    return above.rolling(63, min_periods=21).mean()


def f08_maed_098_bb_pctb_above_1_area_63d(close: pd.Series) -> pd.Series:
    """Cumulative %B excess above 1 over trailing 63d."""
    pb = _bb_pctb(close, 20, 2.0)
    excess = (pb - 1).clip(lower=0)
    return excess.rolling(63, min_periods=21).sum()


def f08_maed_099_bb_keltner_squeeze_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary squeeze: Bollinger upper < Keltner upper at 20d."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    sd = close.rolling(20, min_periods=max(20 // 3, 2)).std()
    atr = _atr(high, low, close, 20)
    bb_up = m + 2 * sd
    kc_up = m + 2 * atr
    return (bb_up < kc_up).astype(float)


def f08_maed_100_bb_squeeze_release_direction_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Squeeze release direction: post-squeeze (BB > KC) sign of close vs 20d MA."""
    m = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    sd = close.rolling(20, min_periods=max(20 // 3, 2)).std()
    atr = _atr(high, low, close, 20)
    bb_up = m + 2 * sd
    kc_up = m + 2 * atr
    released = (bb_up > kc_up).astype(float)
    return released * np.sign(close - m)


def f08_maed_101_ribbon_dispersion_5ma(close: pd.Series) -> pd.Series:
    """Std of 5 SMAs (20/50/100/200/500) over price — ribbon dispersion."""
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in [20, 50, 100, 200, 500]], axis=1)
    return mas.std(axis=1) / close


def f08_maed_102_ribbon_order_entropy_21d(close: pd.Series) -> pd.Series:
    """Entropy of 5-MA ranking over 21d — order-stability proxy."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    ranks = mas.rank(axis=1, method='first')
    code = (ranks * (10 ** np.arange(len(periods)))).sum(axis=1)
    def _ent(w):
        u, c = np.unique(w, return_counts=True)
        p = c / c.sum()
        return float(-(p * np.log(p)).sum())
    return code.rolling(21, min_periods=7).apply(_ent, raw=True)


def f08_maed_103_ribbon_max_spread_5ma(close: pd.Series) -> pd.Series:
    """Max-minus-min across 5 SMAs over price — instantaneous fan width."""
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in [20, 50, 100, 200, 500]], axis=1)
    return (mas.max(axis=1) - mas.min(axis=1)) / close


def f08_maed_104_ribbon_compression_vs_expansion_ratio_21_63(close: pd.Series) -> pd.Series:
    """Ratio of ribbon max-spread mean over 21d vs 63d."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    spread = (mas.max(axis=1) - mas.min(axis=1)) / close
    return _safe_div(spread.rolling(21, min_periods=7).mean(), spread.rolling(63, min_periods=21).mean())


def f08_maed_105_ribbon_fan_out_velocity_21d(close: pd.Series) -> pd.Series:
    """21d change in ribbon max-spread — fan-out velocity."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    spread = (mas.max(axis=1) - mas.min(axis=1)) / close
    return spread.diff(21)


def f08_maed_106_ribbon_cross_flip_count_252d(close: pd.Series) -> pd.Series:
    """Count of changes in 5-MA ranking-code over 252d."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    ranks = mas.rank(axis=1, method='first')
    code = (ranks * (10 ** np.arange(len(periods)))).sum(axis=1)
    flips = (code != code.shift(1)).astype(float)
    return flips.rolling(252, min_periods=63).sum()


def f08_maed_107_price_above_n_smas_5(close: pd.Series) -> pd.Series:
    """Count of SMAs out of 5 that close is above."""
    mas = [close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in [20, 50, 100, 200, 500]]
    above = sum((close > m).astype(float) for m in mas)
    return above


def f08_maed_108_price_above_n_emas_5(close: pd.Series) -> pd.Series:
    """Count of EMAs out of 5 that close is above."""
    mas = [_ema(close, n) for n in [20, 50, 100, 200, 500]]
    above = sum((close > m).astype(float) for m in mas)
    return above


def f08_maed_109_time_since_all_smas_stacked_bullish(close: pd.Series) -> pd.Series:
    """Bars since all 5 SMAs were in strict bullish order (20>50>100>200>500)."""
    periods = [20, 50, 100, 200, 500]
    mas = [close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods]
    stacked = (mas[0] > mas[1]) & (mas[1] > mas[2]) & (mas[2] > mas[3]) & (mas[3] > mas[4])
    idx = np.arange(len(close))
    last = np.where(stacked.values, idx, np.nan)
    last = pd.Series(last, index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f08_maed_110_time_since_ribbon_inverted(close: pd.Series) -> pd.Series:
    """Bars since 5 SMAs were in strict bearish order (20<50<100<200<500)."""
    periods = [20, 50, 100, 200, 500]
    mas = [close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods]
    inv = (mas[0] < mas[1]) & (mas[1] < mas[2]) & (mas[2] < mas[3]) & (mas[3] < mas[4])
    idx = np.arange(len(close))
    last = np.where(inv.values, idx, np.nan)
    last = pd.Series(last, index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f08_maed_111_ribbon_dispersion_pctrank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of ribbon dispersion within 504d."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    disp = mas.std(axis=1) / close
    return _rolling_pctrank(disp, 504)


def f08_maed_112_ribbon_mean_slope_21d(close: pd.Series) -> pd.Series:
    """Mean 21d slope across 5 SMAs."""
    periods = [20, 50, 100, 200, 500]
    sl = pd.concat([_rolling_slope(_safe_log(close.rolling(n, min_periods=max(n // 3, 2)).mean()), 21) for n in periods], axis=1)
    return sl.mean(axis=1)


def f08_maed_113_ribbon_slope_agreement_21d(close: pd.Series) -> pd.Series:
    """Fraction of 5 SMAs with positive 21d slope."""
    periods = [20, 50, 100, 200, 500]
    sl = pd.concat([_rolling_slope(_safe_log(close.rolling(n, min_periods=max(n // 3, 2)).mean()), 21) for n in periods], axis=1)
    return (sl > 0).sum(axis=1) / float(len(periods))


def f08_maed_114_ribbon_stretch_to_nearest_ma(close: pd.Series) -> pd.Series:
    """Distance from close to nearest MA divided by MA spread."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    dist = (mas.sub(close, axis=0)).abs().min(axis=1)
    spread = mas.max(axis=1) - mas.min(axis=1)
    return _safe_div(dist, spread)


def f08_maed_115_max_consecutive_bullish_ribbon_252d(close: pd.Series) -> pd.Series:
    """Max consecutive days with bullish-ordered ribbon in trailing 252d."""
    periods = [20, 50, 100, 200, 500]
    mas = [close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods]
    bull = ((mas[0] > mas[1]) & (mas[1] > mas[2]) & (mas[2] > mas[3]) & (mas[3] > mas[4])).astype(int)
    grp = (bull.diff().ne(0)).cumsum()
    streak = bull.groupby(grp).cumsum() * bull
    return streak.rolling(252, min_periods=63).max().astype(float)


def f08_maed_116_ribbon_emas_dispersion_5ema(close: pd.Series) -> pd.Series:
    """Std of 5 EMAs (20/50/100/200/500) over price."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([_ema(close, n) for n in periods], axis=1)
    return mas.std(axis=1) / close


def f08_maed_117_sma_vs_ema_ribbon_divergence(close: pd.Series) -> pd.Series:
    """Mean SMA-EMA gap across (20,50,100,200,500)."""
    periods = [20, 50, 100, 200, 500]
    sma_avg = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1).mean(axis=1)
    ema_avg = pd.concat([_ema(close, n) for n in periods], axis=1).mean(axis=1)
    return _safe_log(sma_avg) - _safe_log(ema_avg)


def f08_maed_118_ribbon_swap_count_63d(close: pd.Series) -> pd.Series:
    """Sum of adjacent rank-swaps among 5 SMAs over 63d."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    swaps = 0.0
    pairs = [(0, 1), (1, 2), (2, 3), (3, 4)]
    swap_series = []
    for i, j in pairs:
        a = mas.iloc[:, i]; b = mas.iloc[:, j]
        sign = np.sign((a - b).fillna(0))
        swap_series.append(((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float))
    swaps_total = sum(swap_series)
    return swaps_total.rolling(63, min_periods=21).sum()


def f08_maed_119_ribbon_dispersion_velocity_21d(close: pd.Series) -> pd.Series:
    """21d change in ribbon dispersion."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    disp = mas.std(axis=1) / close
    return disp.diff(21)


def f08_maed_120_short_long_gap_zscore_504d_sma20_sma500(close: pd.Series) -> pd.Series:
    """Z-score of SMA(20)/SMA(500) log gap within 504d."""
    a = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    b = close.rolling(500, min_periods=max(500 // 3, 2)).mean()
    gap = _safe_log(a) - _safe_log(b)
    return _rolling_zscore(gap, 504)


def f08_maed_121_consecutive_close_above_sma_50(close: pd.Series) -> pd.Series:
    """Consecutive bars close > SMA(50)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    above = (close > sma).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.astype(float)


def f08_maed_122_consecutive_close_above_sma_200(close: pd.Series) -> pd.Series:
    """Consecutive bars close > SMA(200)."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    above = (close > sma).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.astype(float)


def f08_maed_123_fraction_above_sma_50_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d close > SMA(50)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    above = (close > sma).astype(float)
    return above.rolling(63, min_periods=max(63 // 3, 2)).mean()


def f08_maed_124_fraction_above_sma_200_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252d close > SMA(200)."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    above = (close > sma).astype(float)
    return above.rolling(252, min_periods=max(252 // 3, 2)).mean()


def f08_maed_125_cumulative_area_above_sma_50_21d(close: pd.Series) -> pd.Series:
    """Cumulative log-excess of close above SMA(50) over 21d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    excess = (_safe_log(close) - _safe_log(sma)).clip(lower=0)
    return excess.rolling(21, min_periods=max(21 // 3, 2)).sum()


def f08_maed_126_cumulative_area_above_sma_200_63d(close: pd.Series) -> pd.Series:
    """Cumulative log-excess of close above SMA(200) over 63d."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    excess = (_safe_log(close) - _safe_log(sma)).clip(lower=0)
    return excess.rolling(63, min_periods=max(63 // 3, 2)).sum()


def f08_maed_127_extension_half_life_sma_50(close: pd.Series) -> pd.Series:
    """Proxy half-life of SMA(50) extension AR(1) decay (rolling 63d)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    lag = ext.shift(1)
    cov = (ext * lag).rolling(63, min_periods=21).mean() - ext.rolling(63, min_periods=21).mean() * lag.rolling(63, min_periods=21).mean()
    var = lag.rolling(63, min_periods=21).var()
    phi = _safe_div(cov, var).clip(-0.999, 0.999)
    return -np.log(2.0) / np.log(phi.abs().replace(0, np.nan))


def f08_maed_128_extension_pctrank_504d_sma_50(close: pd.Series) -> pd.Series:
    """Percentile rank of SMA(50) extension over 504d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return _rolling_pctrank(ext, 504)


def f08_maed_129_extension_entropy_63d_sma_50(close: pd.Series) -> pd.Series:
    """Shannon entropy of binned SMA(50) extension over 63d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    def _h(w):
        v = w[~np.isnan(w)]
        if len(v) < 5:
            return np.nan
        bins = np.histogram(v, bins=8)[0].astype(float)
        s = bins.sum()
        if s == 0:
            return np.nan
        p = bins / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum()) if len(p) else np.nan
    return ext.rolling(63, min_periods=21).apply(_h, raw=True)


def f08_maed_130_days_since_extension_max_252d_sma_50(close: pd.Series) -> pd.Series:
    """Bars since SMA(50) extension reached its 252d max."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    def _b(w):
        return (len(w) - 1) - int(np.argmax(w))
    return ext.rolling(252, min_periods=max(252 // 3, 2)).apply(_b, raw=True)


def f08_maed_131_sma_50_touch_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars whose range straddled SMA(50) ± 0.25*ATR over 252d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    tol = atr * 0.25
    touch = ((low <= sma + tol) & (high >= sma - tol)).astype(float)
    return touch.rolling(252, min_periods=max(252 // 3, 2)).sum()


def f08_maed_132_sma_200_touch_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars whose range straddled SMA(200) ± 0.25*ATR over 252d."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    tol = atr * 0.25
    touch = ((low <= sma + tol) & (high >= sma - tol)).astype(float)
    return touch.rolling(252, min_periods=max(252 // 3, 2)).sum()


def f08_maed_133_sma_50_bounce_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of confirmed SMA(50) bounces over 252d (touch on day t-1 + up close on day t)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    tol = atr * 0.25
    touch = ((low <= sma + tol) & (high >= sma - tol)).astype(float)
    up_today = (close > close.shift(1)).astype(float)
    bounce = touch.shift(1).fillna(0) * up_today
    return bounce.rolling(252, min_periods=63).sum()


def f08_maed_134_sma_200_bounce_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of confirmed SMA(200) bounces over 252d."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    tol = atr * 0.25
    touch = ((low <= sma + tol) & (high >= sma - tol)).astype(float)
    up_today = (close > close.shift(1)).astype(float)
    bounce = touch.shift(1).fillna(0) * up_today
    return bounce.rolling(252, min_periods=63).sum()


def f08_maed_135_max_extension_63d_sma_50(close: pd.Series) -> pd.Series:
    """Max SMA(50) log-extension over trailing 63d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return ext.rolling(63, min_periods=21).max()


def f08_maed_136_extension_upper_tail_intensity_63d_sma_50(close: pd.Series) -> pd.Series:
    """Mean of positive SMA(50) extension values over 63d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    pos = ext.clip(lower=0)
    return pos.rolling(63, min_periods=21).mean()


def f08_maed_137_extension_drawdown_from_peak_63d_sma_50(close: pd.Series) -> pd.Series:
    """Current SMA(50) extension minus its 63d rolling max."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    rmax = ext.rolling(63, min_periods=max(63 // 3, 2)).max()
    return ext - rmax


def f08_maed_138_current_ext_to_max_21d_ratio_sma_50(close: pd.Series) -> pd.Series:
    """Ratio of current SMA(50) extension to its 21d rolling max."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return _safe_div(ext, ext.rolling(21, min_periods=7).max())


def f08_maed_139_extension_oscillation_count_63d_sma_50(close: pd.Series) -> pd.Series:
    """Sign-flip count of SMA(50) extension over trailing 63d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    sign = np.sign(ext.fillna(0))
    flips = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return flips.rolling(63, min_periods=21).sum()


def f08_maed_140_extension_mean_reversion_speed_sma_50(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of SMA(50) extension on 63d window (lower=faster mean rev)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    lag = ext.shift(1)
    cov = (ext * lag).rolling(63, min_periods=21).mean() - ext.rolling(63, min_periods=21).mean() * lag.rolling(63, min_periods=21).mean()
    var = lag.rolling(63, min_periods=21).var()
    return _safe_div(cov, var)


def f08_maed_141_days_since_extension_99pct_504d_sma_200(close: pd.Series) -> pd.Series:
    """Bars since SMA(200) extension last exceeded its 504d 99th percentile."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    q99 = ext.rolling(504, min_periods=126).quantile(0.99)
    cond = (ext >= q99)
    idx = np.arange(len(close))
    last = np.where(cond.values, idx, np.nan)
    last = pd.Series(last, index=close.index).ffill()
    return pd.Series(idx, index=close.index) - last


def f08_maed_142_count_extension_gt_1sigma_63d_sma_50(close: pd.Series) -> pd.Series:
    """Count of days SMA(50) extension exceeded its 252d sigma over trailing 63d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    sig = ext.rolling(252, min_periods=63).std()
    cond = (ext > sig).astype(float)
    return cond.rolling(63, min_periods=21).sum()


def f08_maed_143_extension_atr_normalized_zscore_252d_sma_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (close-SMA(50))/ATR(21) within 252d."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    e = _safe_div(close - sma, atr)
    return _rolling_zscore(e, 252)


def f08_maed_144_extension_to_atr_252d_ratio_sma_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """SMA(50) extension scaled by long-horizon ATR(252)."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 252)
    return _safe_div(close - sma, atr)


def f08_maed_145_extension_pctrank_1260d_sma_200(close: pd.Series) -> pd.Series:
    """Percentile rank of SMA(200) extension within 1260d."""
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return _rolling_pctrank(ext, 1260)


def f08_maed_146_distance_to_nearest_ma_above(close: pd.Series) -> pd.Series:
    """Log distance from close to nearest of (SMA20/50/100/200/500) above price."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    diff = mas.sub(close, axis=0)
    above = diff.where(diff > 0, np.inf)
    nearest = above.min(axis=1)
    nearest = nearest.replace(np.inf, np.nan)
    return _safe_div(nearest, close)


def f08_maed_147_distance_to_nearest_ma_below(close: pd.Series) -> pd.Series:
    """Log distance from close to nearest of (SMA20/50/100/200/500) below price."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    diff = mas.sub(close, axis=0)
    below = diff.where(diff < 0, -np.inf)
    nearest = below.max(axis=1)
    nearest = nearest.replace(-np.inf, np.nan)
    return _safe_div(nearest, close)


def f08_maed_148_mean_ma_cushion_5ma(close: pd.Series) -> pd.Series:
    """Mean log-distance from close to each of 5 SMAs."""
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    arr = np.log(close.values[:, None] / mas.replace(0, np.nan).values)
    return pd.Series(np.nanmean(arr, axis=1), index=close.index)


def f08_maed_149_ma_support_test_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 63d where low touched any of (SMA50/100/200) within 0.25*ATR."""
    atr = _atr(high, low, close, 21)
    tol = atr * 0.25
    s50 = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    s100 = close.rolling(100, min_periods=max(100 // 3, 2)).mean()
    s200 = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    touch = (((low <= s50 + tol) & (low >= s50 - tol)) | ((low <= s100 + tol) & (low >= s100 - tol)) | ((low <= s200 + tol) & (low >= s200 - tol))).astype(float)
    return touch.rolling(63, min_periods=21).sum()


def f08_maed_150_composite_extension_exhaustion_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: ATR-extension z-score + Bollinger %B excess + ribbon dispersion z-score."""
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    e_atr = _safe_div(close - sma, atr)
    z_e = _rolling_zscore(e_atr, 252)
    pb = _bb_pctb(close, 20, 2.0)
    excess = (pb - 1).clip(lower=0)
    periods = [20, 50, 100, 200, 500]
    mas = pd.concat([close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in periods], axis=1)
    disp = mas.std(axis=1) / close
    z_d = _rolling_zscore(disp, 252)
    return z_e + excess + z_d


MOVING_AVERAGE_EXTENSION_DYNAMICS_BASE_REGISTRY_076_150 = {
    "f08_maed_076_bollinger_pctb_20": {"inputs": ["close"], "func": f08_maed_076_bollinger_pctb_20},
    "f08_maed_077_bollinger_bandwidth_20": {"inputs": ["close"], "func": f08_maed_077_bollinger_bandwidth_20},
    "f08_maed_078_bollinger_pctb_63": {"inputs": ["close"], "func": f08_maed_078_bollinger_pctb_63},
    "f08_maed_079_bollinger_pctb_252": {"inputs": ["close"], "func": f08_maed_079_bollinger_pctb_252},
    "f08_maed_080_bollinger_bandwidth_20_pctrank_504d": {"inputs": ["close"], "func": f08_maed_080_bollinger_bandwidth_20_pctrank_504d},
    "f08_maed_081_bollinger_bandwidth_20_velocity": {"inputs": ["close"], "func": f08_maed_081_bollinger_bandwidth_20_velocity},
    "f08_maed_082_keltner_pos_20_2": {"inputs": ["close", "high", "low"], "func": f08_maed_082_keltner_pos_20_2},
    "f08_maed_083_keltner_pos_63_2": {"inputs": ["close", "high", "low"], "func": f08_maed_083_keltner_pos_63_2},
    "f08_maed_084_donchian_pos_20": {"inputs": ["close", "high", "low"], "func": f08_maed_084_donchian_pos_20},
    "f08_maed_085_donchian_pos_50": {"inputs": ["close", "high", "low"], "func": f08_maed_085_donchian_pos_50},
    "f08_maed_086_donchian_pos_252": {"inputs": ["close", "high", "low"], "func": f08_maed_086_donchian_pos_252},
    "f08_maed_087_starc_pos_20": {"inputs": ["close", "high", "low"], "func": f08_maed_087_starc_pos_20},
    "f08_maed_088_bb_top_break_count_63d": {"inputs": ["close"], "func": f08_maed_088_bb_top_break_count_63d},
    "f08_maed_089_bb_bottom_break_count_63d": {"inputs": ["close"], "func": f08_maed_089_bb_bottom_break_count_63d},
    "f08_maed_090_keltner_top_break_count_63d": {"inputs": ["close", "high", "low"], "func": f08_maed_090_keltner_top_break_count_63d},
    "f08_maed_091_donchian_top_break_count_63d": {"inputs": ["close", "high"], "func": f08_maed_091_donchian_top_break_count_63d},
    "f08_maed_092_bb_pctb_max_21d": {"inputs": ["close"], "func": f08_maed_092_bb_pctb_max_21d},
    "f08_maed_093_bb_bandwidth_zscore_504d": {"inputs": ["close"], "func": f08_maed_093_bb_bandwidth_zscore_504d},
    "f08_maed_094_days_since_bb_bandwidth_max_252d": {"inputs": ["close"], "func": f08_maed_094_days_since_bb_bandwidth_max_252d},
    "f08_maed_095_days_since_bb_bandwidth_min_252d": {"inputs": ["close"], "func": f08_maed_095_days_since_bb_bandwidth_min_252d},
    "f08_maed_096_bb_pctb_above_1_streak_max_63d": {"inputs": ["close"], "func": f08_maed_096_bb_pctb_above_1_streak_max_63d},
    "f08_maed_097_bb_pctb_above_08_fraction_63d": {"inputs": ["close"], "func": f08_maed_097_bb_pctb_above_08_fraction_63d},
    "f08_maed_098_bb_pctb_above_1_area_63d": {"inputs": ["close"], "func": f08_maed_098_bb_pctb_above_1_area_63d},
    "f08_maed_099_bb_keltner_squeeze_indicator": {"inputs": ["close", "high", "low"], "func": f08_maed_099_bb_keltner_squeeze_indicator},
    "f08_maed_100_bb_squeeze_release_direction_21d": {"inputs": ["close", "high", "low"], "func": f08_maed_100_bb_squeeze_release_direction_21d},
    "f08_maed_101_ribbon_dispersion_5ma": {"inputs": ["close"], "func": f08_maed_101_ribbon_dispersion_5ma},
    "f08_maed_102_ribbon_order_entropy_21d": {"inputs": ["close"], "func": f08_maed_102_ribbon_order_entropy_21d},
    "f08_maed_103_ribbon_max_spread_5ma": {"inputs": ["close"], "func": f08_maed_103_ribbon_max_spread_5ma},
    "f08_maed_104_ribbon_compression_vs_expansion_ratio_21_63": {"inputs": ["close"], "func": f08_maed_104_ribbon_compression_vs_expansion_ratio_21_63},
    "f08_maed_105_ribbon_fan_out_velocity_21d": {"inputs": ["close"], "func": f08_maed_105_ribbon_fan_out_velocity_21d},
    "f08_maed_106_ribbon_cross_flip_count_252d": {"inputs": ["close"], "func": f08_maed_106_ribbon_cross_flip_count_252d},
    "f08_maed_107_price_above_n_smas_5": {"inputs": ["close"], "func": f08_maed_107_price_above_n_smas_5},
    "f08_maed_108_price_above_n_emas_5": {"inputs": ["close"], "func": f08_maed_108_price_above_n_emas_5},
    "f08_maed_109_time_since_all_smas_stacked_bullish": {"inputs": ["close"], "func": f08_maed_109_time_since_all_smas_stacked_bullish},
    "f08_maed_110_time_since_ribbon_inverted": {"inputs": ["close"], "func": f08_maed_110_time_since_ribbon_inverted},
    "f08_maed_111_ribbon_dispersion_pctrank_504d": {"inputs": ["close"], "func": f08_maed_111_ribbon_dispersion_pctrank_504d},
    "f08_maed_112_ribbon_mean_slope_21d": {"inputs": ["close"], "func": f08_maed_112_ribbon_mean_slope_21d},
    "f08_maed_113_ribbon_slope_agreement_21d": {"inputs": ["close"], "func": f08_maed_113_ribbon_slope_agreement_21d},
    "f08_maed_114_ribbon_stretch_to_nearest_ma": {"inputs": ["close"], "func": f08_maed_114_ribbon_stretch_to_nearest_ma},
    "f08_maed_115_max_consecutive_bullish_ribbon_252d": {"inputs": ["close"], "func": f08_maed_115_max_consecutive_bullish_ribbon_252d},
    "f08_maed_116_ribbon_emas_dispersion_5ema": {"inputs": ["close"], "func": f08_maed_116_ribbon_emas_dispersion_5ema},
    "f08_maed_117_sma_vs_ema_ribbon_divergence": {"inputs": ["close"], "func": f08_maed_117_sma_vs_ema_ribbon_divergence},
    "f08_maed_118_ribbon_swap_count_63d": {"inputs": ["close"], "func": f08_maed_118_ribbon_swap_count_63d},
    "f08_maed_119_ribbon_dispersion_velocity_21d": {"inputs": ["close"], "func": f08_maed_119_ribbon_dispersion_velocity_21d},
    "f08_maed_120_short_long_gap_zscore_504d_sma20_sma500": {"inputs": ["close"], "func": f08_maed_120_short_long_gap_zscore_504d_sma20_sma500},
    "f08_maed_121_consecutive_close_above_sma_50": {"inputs": ["close"], "func": f08_maed_121_consecutive_close_above_sma_50},
    "f08_maed_122_consecutive_close_above_sma_200": {"inputs": ["close"], "func": f08_maed_122_consecutive_close_above_sma_200},
    "f08_maed_123_fraction_above_sma_50_63d": {"inputs": ["close"], "func": f08_maed_123_fraction_above_sma_50_63d},
    "f08_maed_124_fraction_above_sma_200_252d": {"inputs": ["close"], "func": f08_maed_124_fraction_above_sma_200_252d},
    "f08_maed_125_cumulative_area_above_sma_50_21d": {"inputs": ["close"], "func": f08_maed_125_cumulative_area_above_sma_50_21d},
    "f08_maed_126_cumulative_area_above_sma_200_63d": {"inputs": ["close"], "func": f08_maed_126_cumulative_area_above_sma_200_63d},
    "f08_maed_127_extension_half_life_sma_50": {"inputs": ["close"], "func": f08_maed_127_extension_half_life_sma_50},
    "f08_maed_128_extension_pctrank_504d_sma_50": {"inputs": ["close"], "func": f08_maed_128_extension_pctrank_504d_sma_50},
    "f08_maed_129_extension_entropy_63d_sma_50": {"inputs": ["close"], "func": f08_maed_129_extension_entropy_63d_sma_50},
    "f08_maed_130_days_since_extension_max_252d_sma_50": {"inputs": ["close"], "func": f08_maed_130_days_since_extension_max_252d_sma_50},
    "f08_maed_131_sma_50_touch_count_252d": {"inputs": ["close", "high", "low"], "func": f08_maed_131_sma_50_touch_count_252d},
    "f08_maed_132_sma_200_touch_count_252d": {"inputs": ["close", "high", "low"], "func": f08_maed_132_sma_200_touch_count_252d},
    "f08_maed_133_sma_50_bounce_count_252d": {"inputs": ["close", "high", "low"], "func": f08_maed_133_sma_50_bounce_count_252d},
    "f08_maed_134_sma_200_bounce_count_252d": {"inputs": ["close", "high", "low"], "func": f08_maed_134_sma_200_bounce_count_252d},
    "f08_maed_135_max_extension_63d_sma_50": {"inputs": ["close"], "func": f08_maed_135_max_extension_63d_sma_50},
    "f08_maed_136_extension_upper_tail_intensity_63d_sma_50": {"inputs": ["close"], "func": f08_maed_136_extension_upper_tail_intensity_63d_sma_50},
    "f08_maed_137_extension_drawdown_from_peak_63d_sma_50": {"inputs": ["close"], "func": f08_maed_137_extension_drawdown_from_peak_63d_sma_50},
    "f08_maed_138_current_ext_to_max_21d_ratio_sma_50": {"inputs": ["close"], "func": f08_maed_138_current_ext_to_max_21d_ratio_sma_50},
    "f08_maed_139_extension_oscillation_count_63d_sma_50": {"inputs": ["close"], "func": f08_maed_139_extension_oscillation_count_63d_sma_50},
    "f08_maed_140_extension_mean_reversion_speed_sma_50": {"inputs": ["close"], "func": f08_maed_140_extension_mean_reversion_speed_sma_50},
    "f08_maed_141_days_since_extension_99pct_504d_sma_200": {"inputs": ["close"], "func": f08_maed_141_days_since_extension_99pct_504d_sma_200},
    "f08_maed_142_count_extension_gt_1sigma_63d_sma_50": {"inputs": ["close"], "func": f08_maed_142_count_extension_gt_1sigma_63d_sma_50},
    "f08_maed_143_extension_atr_normalized_zscore_252d_sma_50": {"inputs": ["close", "high", "low"], "func": f08_maed_143_extension_atr_normalized_zscore_252d_sma_50},
    "f08_maed_144_extension_to_atr_252d_ratio_sma_50": {"inputs": ["close", "high", "low"], "func": f08_maed_144_extension_to_atr_252d_ratio_sma_50},
    "f08_maed_145_extension_pctrank_1260d_sma_200": {"inputs": ["close"], "func": f08_maed_145_extension_pctrank_1260d_sma_200},
    "f08_maed_146_distance_to_nearest_ma_above": {"inputs": ["close"], "func": f08_maed_146_distance_to_nearest_ma_above},
    "f08_maed_147_distance_to_nearest_ma_below": {"inputs": ["close"], "func": f08_maed_147_distance_to_nearest_ma_below},
    "f08_maed_148_mean_ma_cushion_5ma": {"inputs": ["close"], "func": f08_maed_148_mean_ma_cushion_5ma},
    "f08_maed_149_ma_support_test_count_63d": {"inputs": ["close", "high", "low"], "func": f08_maed_149_ma_support_test_count_63d},
    "f08_maed_150_composite_extension_exhaustion_score": {"inputs": ["close", "high", "low"], "func": f08_maed_150_composite_extension_exhaustion_score},
}
