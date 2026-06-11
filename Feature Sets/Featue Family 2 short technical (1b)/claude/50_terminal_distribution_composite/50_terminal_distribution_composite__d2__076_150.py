"""terminal_distribution_composite base features 076-150 — Pipeline 1b-technical.

Continues 001-075 with:
F: multi-horizon alignment (MA-break breadth, drawdown across horizons).
G: vol / range expansion (post-peak vol, climax-down bars).
H: time-since / age / structural age indicators.
I: pre-breakdown / late-cycle signatures (peak-extension, parabolic-pre-peak).
J: master composite topping/breakdown scores.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket F — multi-horizon alignment (076-095)
# ============================================================

def f50_tdco_076_short_med_long_breakdown_alignment(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close broke prior 21d low AND prior 63d low AND prior 252d low simultaneously — full-horizon breakdown."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    ll252 = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    return ((close < ll21) & (close < ll63) & (close < ll252)).astype(float).where(ll252.notna(), np.nan)


def f50_tdco_077_ma_violation_count_50_100_200_state(close: pd.Series) -> pd.Series:
    """Count of MA states {below SMA50, SMA100, SMA200} currently in violation — multi-MA bearish breadth."""
    s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    return ((close < s50).astype(float) + (close < s100).astype(float) + (close < s200).astype(float)).where(s200.notna(), np.nan)


def f50_tdco_078_ma_break_sequence_indicator(close: pd.Series) -> pd.Series:
    """1 if SMA50 break happened first, then SMA100, then SMA200 within past 252 bars — sequential MA breakdown."""
    s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    b50_age = _bars_since_true((close.shift(1) >= s50.shift(1)) & (close < s50))
    b100_age = _bars_since_true((close.shift(1) >= s100.shift(1)) & (close < s100))
    b200_age = _bars_since_true((close.shift(1) >= s200.shift(1)) & (close < s200))
    seq = (b50_age > b100_age) & (b100_age > b200_age) & (b50_age <= YDAYS)
    return seq.astype(float).where(s200.notna(), np.nan)


def f50_tdco_079_multi_horizon_drawdown_count_above_20(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons {21, 63, 252, 504} with drawdown > 20% — multi-horizon drawdown breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS, DDAYS_2Y):
        rmax = high.rolling(n, min_periods=max(n // 3, MDAYS)).max()
        dd = _safe_div(rmax - close, rmax)
        cnt = cnt + (dd > 0.20).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f50_tdco_080_avg_drawdown_across_horizons(high: pd.Series, close: pd.Series) -> pd.Series:
    """Average drawdown across horizons {21, 63, 252, 504} — average drawdown magnitude."""
    tot = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS, DDAYS_2Y):
        rmax = high.rolling(n, min_periods=max(n // 3, MDAYS)).max()
        tot = tot + _safe_div(rmax - close, rmax).fillna(0)
    return (tot / 4.0).where(close.notna(), np.nan)


def f50_tdco_081_count_horizons_in_decline_63(close: pd.Series) -> pd.Series:
    """Count of horizons {5, 21, 63, 252} with 63d-slope < 0 — multi-horizon decline breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        sma_n = _sma(close, n)
        sl = _rolling_slope(sma_n, QDAYS)
        cnt = cnt + (sl < 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f50_tdco_082_monotonic_decline_across_horizons(close: pd.Series) -> pd.Series:
    """1 if SMA(5) < SMA(21) < SMA(50) < SMA(200) — monotonic short<long ribbon (bearish stack)."""
    s5 = _sma(close, WDAYS); s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    return ((s5 < s21) & (s21 < s50) & (s50 < s200)).astype(float).where(s200.notna(), np.nan)


def f50_tdco_083_short_leads_long_decline_indicator(close: pd.Series) -> pd.Series:
    """1 if 21d slope < 0 AND 252d slope >= 0 — short-horizon leading decline (early-stage breakdown)."""
    sl21 = _rolling_slope(close, MDAYS)
    sl252 = _rolling_slope(close, YDAYS)
    return ((sl21 < 0) & (sl252 >= 0)).astype(float).where(sl21.notna() & sl252.notna(), np.nan)


def f50_tdco_084_short_break_in_long_uptrend_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < prior 21d low BUT close > SMA(200) — short break inside long-uptrend (early warning)."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    s200 = _sma(close, 200)
    return ((close < ll21) & (close > s200)).astype(float).where(ll21.notna() & s200.notna(), np.nan)


def f50_tdco_085_short_below_50ma_long_above_200ma_state(close: pd.Series) -> pd.Series:
    """1 if close < SMA50 AND close > SMA200 — mixed-trend state (early bear vs intact long bull)."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    return ((close < s50) & (close > s200)).astype(float).where(s200.notna(), np.nan)


def f50_tdco_086_all_horizons_below_respective_ma(close: pd.Series) -> pd.Series:
    """1 if close below SMA20 AND SMA50 AND SMA100 AND SMA200 — full bearish MA stack."""
    return (((close < _sma(close, 20)) & (close < _sma(close, 50)) & (close < _sma(close, 100)) & (close < _sma(close, 200)))
            .astype(float).where(_sma(close, 200).notna(), np.nan))


def f50_tdco_087_count_mas_breached_in_21d(close: pd.Series) -> pd.Series:
    """Count of MA-break events {SMA20, SMA50, SMA100, SMA200} in past 21 bars — MA-break breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (20, 50, 100, 200):
        sma = _sma(close, n)
        ev = ((close.shift(1) >= sma.shift(1)) & (close < sma)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    return cnt.where(_sma(close, 200).notna(), np.nan)


def f50_tdco_088_rolling_correlation_break_close_50ma_63(close: pd.Series) -> pd.Series:
    """63d rolling correlation between close and SMA50 — drops when close decouples downward from MA."""
    return close.rolling(QDAYS, min_periods=MDAYS).corr(_sma(close, 50))


def f50_tdco_089_ma_distance_decay_63(close: pd.Series) -> pd.Series:
    """63d slope of (close / SMA50 - 1) — rate of change of close-distance-from-MA (negative = MA gap closing/inverting)."""
    return _rolling_slope(_safe_div(close, _sma(close, 50)) - 1.0, QDAYS)


def f50_tdco_090_ribbon_compression_breakdown_indicator(close: pd.Series) -> pd.Series:
    """1 if dispersion of {SMA20, SMA50, SMA100, SMA200} is below its 252d 25th percentile AND close < SMA50
    — compression-then-break setup."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    disp = pd.concat([s20.rename("a"), s50.rename("b"), s100.rename("c"), s200.rename("d")], axis=1).std(axis=1)
    q = disp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return ((disp < q) & (close < s50)).astype(float).where(s200.notna(), np.nan)


def f50_tdco_091_cross_below_50ma_count_252(close: pd.Series) -> pd.Series:
    """Count of SMA50 down-cross events in past 252 — annual SMA50 churn frequency."""
    s50 = _sma(close, 50)
    ev = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(s50.notna(), np.nan)


def f50_tdco_092_cross_below_200ma_count_252(close: pd.Series) -> pd.Series:
    """Count of SMA200 down-cross events in past 252 — annual major-trend break frequency."""
    s200 = _sma(close, 200)
    ev = ((close.shift(1) >= s200.shift(1)) & (close < s200)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(s200.notna(), np.nan)


def f50_tdco_093_multi_ma_below_count_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where ALL of {SMA20, SMA50, SMA100, SMA200} are above close — annual full-bearish-stack dwell."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    all_below = (close < s20) & (close < s50) & (close < s100) & (close < s200)
    return all_below.astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(s200.notna(), np.nan)


def f50_tdco_094_alignment_at_break_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < prior 21d low AND ALL of SMA20, SMA50, SMA100 are declining (21d slope < 0) — aligned break."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    sl20 = _rolling_slope(_sma(close, 20), MDAYS)
    sl50 = _rolling_slope(_sma(close, 50), MDAYS)
    sl100 = _rolling_slope(_sma(close, 100), MDAYS)
    return ((close < ll21) & (sl20 < 0) & (sl50 < 0) & (sl100 < 0)).astype(float).where(ll21.notna(), np.nan)


def f50_tdco_095_post_break_alignment_decay_63(close: pd.Series) -> pd.Series:
    """Slope (63d) of count-of-MAs-below: if increasing, alignment of breakdown is intensifying."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    cnt = (close < s20).astype(float) + (close < s50).astype(float) + (close < s100).astype(float) + (close < s200).astype(float)
    return _rolling_slope(cnt, QDAYS)


# ============================================================
# Bucket G — vol / range expansion (096-110)
# ============================================================

def f50_tdco_096_vol_expansion_post_peak_21(close: pd.Series) -> pd.Series:
    """Ratio: (21d std of returns) / (21d std of returns from 21 bars ago) — short-horizon vol expansion."""
    sd = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(sd, sd.shift(MDAYS))


def f50_tdco_097_vol_expansion_post_peak_63(close: pd.Series) -> pd.Series:
    """Ratio: (63d std of returns) / (63d std from 63 bars ago) — quarterly vol expansion."""
    sd = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sd, sd.shift(QDAYS))


def f50_tdco_098_range_expansion_indicator_21(high: pd.Series, low: pd.Series) -> pd.Series:
    """(current 21d range) / (21d range from 21 bars ago) — range expansion ratio."""
    rng = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    return _safe_div(rng, rng.shift(MDAYS))


def f50_tdco_099_atr_doubling_post_peak_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR(21) > 2 * ATR(21) from 21 bars ago — ATR doubled (vol shock)."""
    atr = _atr(high, low, close, MDAYS)
    return (atr > 2.0 * atr.shift(MDAYS)).astype(float).where(atr.notna(), np.nan)


def f50_tdco_100_vol_regime_shift_252(close: pd.Series) -> pd.Series:
    """(63d std) / (63d std from 252 bars ago) — annual vol-regime shift ratio."""
    sd = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sd, sd.shift(YDAYS))


def f50_tdco_101_vol_post_peak_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of 21d std-of-returns over 252d — distribution-based vol extreme."""
    sd = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(sd, YDAYS, min_periods=QDAYS)


def f50_tdco_102_tail_widening_skew_decay_63(close: pd.Series) -> pd.Series:
    """63d skewness of returns — negative = left-tail-heavy distribution (post-peak)."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).skew()


def f50_tdco_103_wide_range_red_bar_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars where (H-L)/ATR21 > 2 AND close < open-proxy (close < prior close) — wide-range red bars."""
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    wide = rng > 2.0 * atr
    red = close.diff() < 0
    return (wide & red).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(atr.notna(), np.nan)


def f50_tdco_104_max_single_bar_drop_post_peak_63(close: pd.Series) -> pd.Series:
    """Min (most-negative) single-bar return in past 63 bars — worst single-day drop."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).min()


def f50_tdco_105_max_single_bar_volume_post_peak_63(volume: pd.Series) -> pd.Series:
    """Max single-bar volume in past 63 bars / SMA50 of volume — peak volume ratio (climax detection)."""
    return _safe_div(volume.rolling(QDAYS, min_periods=MDAYS).max(),
                     volume.shift(1).rolling(50, min_periods=10).mean())


def f50_tdco_106_post_peak_volume_climax_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if volume > 2x prior-50d-avg AND close down > 3% AND in past 63 bars of 252d high — capitulation-day flag."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    in_post = (bs > 0) & (bs <= QDAYS)
    return ((volume > 2.0 * vavg) & (ret < -0.03) & in_post).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_107_distribution_volume_zscore_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (over 252d) of volume on down-close days — distribution-volume extreme."""
    down_vol = volume.where(close.diff() < 0, np.nan)
    return _rolling_zscore(down_vol, YDAYS, min_periods=QDAYS)


def f50_tdco_108_drawdown_acceleration_21(high: pd.Series, close: pd.Series) -> pd.Series:
    """First diff of 21d-drawdown — drawdown acceleration."""
    rmax = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(rmax - close, rmax).diff()


def f50_tdco_109_drawdown_acceleration_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """First diff of 63d-drawdown — quarterly drawdown acceleration."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_div(rmax - close, rmax).diff()


def f50_tdco_110_vol_breakout_index_at_top_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price within 1% of 252d high: (ATR21 / ATR21-from-63-bars-ago). Else NaN.
    Vol expansion specifically at top."""
    atr = _atr(high, low, close, MDAYS)
    near_top = high >= 0.99 * high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(atr, atr.shift(QDAYS)).where(near_top, np.nan)


# ============================================================
# Bucket H — time-since / age / decay (111-130)
# ============================================================

def f50_tdco_111_bars_since_252_high(high: pd.Series) -> pd.Series:
    """Bars since the most-recent 252d-high — annual peak recency."""
    return _bars_since_true(high == high.rolling(YDAYS, min_periods=QDAYS).max())


def f50_tdco_112_bars_since_first_lower_high_post_252_high(high: pd.Series) -> pd.Series:
    """Bars since first lower-high event AFTER the most-recent 252d-high — time since trend-failure."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = h5 < h5.shift(WDAYS)
    bs_peak = _bars_since_true(high == rmax)
    post_peak = (bs_peak > 0) & (bs_peak <= YDAYS)
    return _bars_since_true(lh & post_peak)


def f50_tdco_113_bars_since_50ma_break(close: pd.Series) -> pd.Series:
    """Bars since most-recent close-below-SMA50 cross."""
    s = _sma(close, 50)
    ev = (close.shift(1) >= s.shift(1)) & (close < s)
    return _bars_since_true(ev)


def f50_tdco_114_bars_since_200ma_break(close: pd.Series) -> pd.Series:
    """Bars since most-recent close-below-SMA200 cross."""
    s = _sma(close, 200)
    ev = (close.shift(1) >= s.shift(1)) & (close < s)
    return _bars_since_true(ev)


def f50_tdco_115_bars_since_death_cross_50_200(close: pd.Series) -> pd.Series:
    """Bars since most-recent SMA50-SMA200 death-cross."""
    d = _sma(close, 50) - _sma(close, 200)
    ev = (d.shift(1) >= 0) & (d < 0)
    return _bars_since_true(ev)


def f50_tdco_116_bars_since_first_minus10pct_drawdown(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since drawdown from 252d-max first exceeded 10% — bear-onset (mild) recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.10)


def f50_tdco_117_bars_since_first_minus30pct_drawdown(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since drawdown from 252d-max first exceeded 30% — bear-onset (severe) recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.30)


def f50_tdco_118_bars_since_first_minus50pct_drawdown(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since drawdown from 252d-max first exceeded 50% — bear-onset (extreme) recency."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _bars_since_true(dd > 0.50)


def f50_tdco_119_age_current_below_50ma_episode(close: pd.Series) -> pd.Series:
    """Live age (consecutive bars) of close < SMA50 — current below-MA-streak length."""
    s = _sma(close, 50)
    return _streak_true(close < s).where(s.notna(), np.nan)


def f50_tdco_120_age_current_below_200ma_episode(close: pd.Series) -> pd.Series:
    """Live age of close < SMA200 — current below-major-MA-streak length."""
    s = _sma(close, 200)
    return _streak_true(close < s).where(s.notna(), np.nan)


def f50_tdco_121_age_current_drawdown_below_10pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """Live age of current drawdown > 10% from 252d-max episode."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return _streak_true(dd > 0.10).where(dd.notna(), np.nan)


def f50_tdco_122_time_to_first_minus20_from_peak_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Within trailing 252 bars: # bars between the 252d peak and the first time dd > 20% appeared.
    NaN if dd never reached 20%."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    bs_dd20 = _bars_since_true(dd > 0.20)
    diff = bs_peak - bs_dd20
    return diff.where((bs_peak <= YDAYS) & (bs_dd20 <= YDAYS) & (bs_peak >= bs_dd20), np.nan)


def f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """(fraction time dd > 10% in 252d) / (fraction time near 252d-high in 252d) — drawdown vs top dwell ratio."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    in_dd = (dd > 0.10).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    near_top = (high >= 0.99 * rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(in_dd, near_top)


def f50_tdco_124_longest_below_50ma_episode_252(close: pd.Series) -> pd.Series:
    """Longest consecutive run of close < SMA50 in past 252 bars."""
    s = _sma(close, 50)
    return _streak_true(close < s).rolling(YDAYS, min_periods=QDAYS).max().where(s.notna(), np.nan)


def f50_tdco_125_longest_below_200ma_episode_252(close: pd.Series) -> pd.Series:
    """Longest consecutive run of close < SMA200 in past 252 bars."""
    s = _sma(close, 200)
    return _streak_true(close < s).rolling(YDAYS, min_periods=QDAYS).max().where(s.notna(), np.nan)


def f50_tdco_126_time_since_last_higher_high_63(high: pd.Series) -> pd.Series:
    """Bars since the most-recent 5d-high > prior 5d-high — time since trend continuation."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    hh = h5 > h5.shift(WDAYS)
    return _bars_since_true(hh)


def f50_tdco_127_time_between_consecutive_lower_lows_63(low: pd.Series) -> pd.Series:
    """Mean time-between-lower-lows in past 63 bars (using 5d-low events) — bear-step cadence."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll = (l5 < l5.shift(WDAYS)).astype(float)
    cnt = ll.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(float(QDAYS), cnt)


def f50_tdco_128_hazard_rate_new_lower_low_63(low: pd.Series) -> pd.Series:
    """(count of new 21d lows in 63 bars) / 63 — new-low hazard rate."""
    ll21 = low == low.rolling(MDAYS, min_periods=WDAYS).min()
    return (ll21.astype(float).rolling(QDAYS, min_periods=MDAYS).sum() / float(QDAYS)).where(low.notna(), np.nan)


def f50_tdco_129_streak_length_current_lower_lows(low: pd.Series) -> pd.Series:
    """Current consecutive run of bars where 5d-low < prior 5d-low — live lower-low streak."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    return _streak_true(l5 < l5.shift(WDAYS)).where(low.notna(), np.nan)


def f50_tdco_130_streak_length_current_lower_highs(high: pd.Series) -> pd.Series:
    """Current consecutive run of bars where 5d-high < prior 5d-high — live lower-high streak."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    return _streak_true(h5 < h5.shift(WDAYS)).where(high.notna(), np.nan)


# ============================================================
# Bucket I — pre-breakdown / late-cycle signatures (131-145)
# ============================================================

def f50_tdco_131_pre_peak_extension_ratio_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d high: (252d high / 252d-rolling-SMA close). Else NaN. Pre-peak overextension."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high == rmax
    return _safe_div(rmax, _sma(close, YDAYS)).where(at_max, np.nan)


def f50_tdco_132_pre_peak_volume_climax_252(high: pd.Series, volume: pd.Series) -> pd.Series:
    """At bars where price = 252d high: (volume / 50d avg volume). Else NaN. Peak-volume-at-peak ratio."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high == rmax
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return _safe_div(volume, vavg).where(at_max, np.nan)


def f50_tdco_133_pre_peak_acceleration_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d high: 63d return. Else NaN. Pre-peak run-up magnitude."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high == rmax
    return close.pct_change(QDAYS).where(at_max, np.nan)


def f50_tdco_134_pre_peak_parabolic_score(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where price = 252d high: quadratic curvature of log(close) over past 63 (positive = parabolic up).
    Else NaN."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high == rmax
    def _curv(w):
        if np.isnan(w).any() or len(w) < 21:
            return np.nan
        x = np.arange(len(w), dtype=float)
        try:
            a, _, _ = np.polyfit(x, w, 2)
            return float(a)
        except Exception:
            return np.nan
    curv = _safe_log(close).rolling(QDAYS, min_periods=MDAYS).apply(_curv, raw=True)
    return curv.where(at_max, np.nan)


def f50_tdco_135_peak_to_minus5pct_decay_velocity(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where drawdown from 252d-max first exceeded 5%: bars-since-252d-max at that moment.
    Smaller = faster decay velocity."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    first_5 = (dd.shift(1) <= 0.05) & (dd > 0.05)
    return bs_peak.where(first_5, np.nan)


def f50_tdco_136_peak_to_minus10pct_decay_velocity(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where drawdown first exceeded 10%: bars-since-252d-max — speed to first -10%."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    first_10 = (dd.shift(1) <= 0.10) & (dd > 0.10)
    return bs_peak.where(first_10, np.nan)


def f50_tdco_137_peak_to_minus20pct_decay_velocity(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where drawdown first exceeded 20%: bars-since-252d-max — speed to first -20%."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    first_20 = (dd.shift(1) <= 0.20) & (dd > 0.20)
    return bs_peak.where(first_20, np.nan)


def f50_tdco_138_post_peak_first_lower_high_distance(high: pd.Series) -> pd.Series:
    """Bars since the 252d peak, conditioned on the first lower-high event having occurred — peak-to-lower-high distance."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = h5 < h5.shift(WDAYS)
    post_peak = bs_peak > 0
    first_lh = lh & post_peak
    return bs_peak.where(first_lh, np.nan)


def f50_tdco_139_post_peak_first_breakdown_distance(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since 252d peak when the first close < 21d low fired after the peak — peak-to-first-break distance."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    broke = (close < prev_ll21)
    post = bs_peak > 0
    return bs_peak.where(broke & post, np.nan)


def f50_tdco_140_post_peak_first_50ma_break_distance(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since 252d peak when the first SMA50 break-down fired after the peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    s50 = _sma(close, 50)
    broke = (close.shift(1) >= s50.shift(1)) & (close < s50)
    post = bs_peak > 0
    return bs_peak.where(broke & post, np.nan)


def f50_tdco_141_post_peak_first_200ma_break_distance(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since 252d peak when the first SMA200 break-down fired after the peak — major-trend-break delay."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    s200 = _sma(close, 200)
    broke = (close.shift(1) >= s200.shift(1)) & (close < s200)
    post = bs_peak > 0
    return bs_peak.where(broke & post, np.nan)


def f50_tdco_142_pre_breakdown_distribution_count_63(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distribution-day count in past 63 conditioned on a 63d-low break within last 21 bars — pre-break distribution."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    broke_recent = (close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return dd.rolling(QDAYS, min_periods=MDAYS).sum().where(broke_recent, np.nan)


def f50_tdco_143_pre_breakdown_lower_high_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-high count in past 63 conditioned on 63d-low break within last 21 — pre-break lower-high count."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_count = (h5 < h5.shift(WDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    broke_recent = (close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return lh_count.where(broke_recent, np.nan)


def f50_tdco_144_pre_breakdown_volume_imbalance_63(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(down-vol - up-vol)/(total) over past 63 conditioned on 63d-low break in past 21 — pre-break vol imbalance."""
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    imb = _safe_div(dv - uv, dv + uv)
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    broke_recent = (close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return imb.where(broke_recent, np.nan)


def f50_tdco_145_pre_breakdown_topping_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite topping score in past 63 bars conditioned on 63d-low break in past 21:
    sum of {top_dwell>0.3, lower-high count>=3, distribution-day count>=3, drawdown_from_63d_max>0.05}."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * top).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_count = (h5 < h5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    rmax_q = high.rolling(QDAYS, min_periods=MDAYS).max()
    dd_q = _safe_div(rmax_q - close, rmax_q)
    score = ((near > 0.3).astype(float).fillna(0)
             + (lh_count >= 3.0).astype(float).fillna(0)
             + (dd_count >= 3.0).astype(float).fillna(0)
             + (dd_q > 0.05).astype(float).fillna(0))
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    broke_recent = (close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return score.where(broke_recent, np.nan)


# ============================================================
# Bucket J — master composite scores (146-150)
# ============================================================

def f50_tdco_146_terminal_distribution_master_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master "terminal distribution" composite score (always defined):
    sum of {distribution_day_count_25 >= 5, lower_high_count_63 >= 10, drawdown_from_252_max > 0.10,
            close < SMA50, close < SMA200, count_mas_breached_in_21d >= 2}."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_count = (h5 < h5.shift(WDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cnt = pd.Series(0.0, index=close.index)
    for n in (20, 50, 100, 200):
        sma = _sma(close, n)
        ev = ((close.shift(1) >= sma.shift(1)) & (close < sma)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=WDAYS).sum() > 0).astype(float)
    score = ((dd_count >= 5.0).astype(float).fillna(0)
             + (lh_count >= 10.0).astype(float).fillna(0)
             + (dd > 0.10).astype(float).fillna(0)
             + (close < s50).astype(float).fillna(0)
             + (close < s200).astype(float).fillna(0)
             + (cnt >= 2.0).astype(float).fillna(0))
    return score.where(s200.notna(), np.nan)


def f50_tdco_147_stuck_probability_proxy_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Proxy for "stuck" probability: drawdown_from_252max × (time_underwater_below_20pct_252) — combines depth & duration."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (dd * tu).where(rmax.notna(), np.nan)


def f50_tdco_148_composite_breakdown_severity_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual breakdown severity: count of distinct breakdown events {21d-low break, 63d-low break,
    SMA50 break, SMA200 break, death cross} in past 252 — total triggers fired."""
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    prev_ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    e1 = ((close < prev_ll21) & (close.shift(1) >= prev_ll21.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e2 = ((close < prev_ll63) & (close.shift(1) >= prev_ll63.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e3 = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e4 = ((close.shift(1) >= s200.shift(1)) & (close < s200)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    d = s50 - s200
    e5 = ((d.shift(1) >= 0) & (d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (e1.fillna(0) + e2.fillna(0) + e3.fillna(0) + e4.fillna(0) + e5.fillna(0)).where(s200.notna(), np.nan)


def f50_tdco_149_multi_signal_topping_aggregate_at_252_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At bars where price = 252d high: sum of {distribution at top, failed-retest count, lower-high streak >=3,
    plateau/mean low, top-dwell >50%, post-peak red-bar count}. Else NaN."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high == top
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    near_top = high >= 0.95 * top
    dist_at_top = ((ret < -0.002) & (volume > vavg) & near_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fr = ((high >= 0.95 * top) & (high < top)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_streak = _streak_true(h5 < h5.shift(WDAYS))
    plat = _safe_div(close.rolling(QDAYS, min_periods=MDAYS).std(), close.rolling(QDAYS, min_periods=MDAYS).mean())
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    dwell = (pos > 0.9).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    red_cnt = (close.diff() < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    score = ((dist_at_top >= 3.0).astype(float).fillna(0)
             + (fr >= 2.0).astype(float).fillna(0)
             + (lh_streak >= 3.0).astype(float).fillna(0)
             + (plat < 0.02).astype(float).fillna(0)
             + (dwell > 0.5).astype(float).fillna(0)
             + (red_cnt >= 12.0).astype(float).fillna(0))
    return score.where(at_max, np.nan)


def f50_tdco_150_terminal_pattern_combined_intensity_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined intensity = (drawdown_from_252max) × (master topping score components).
    Captures both depth and breadth of bearish signals."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    breadth = ((dd_count >= 5.0).astype(float).fillna(0)
               + (close < s50).astype(float).fillna(0)
               + (close < s200).astype(float).fillna(0))
    return (dd * breadth).where(s200.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_076_150 = {
    "f50_tdco_076_short_med_long_breakdown_alignment": {"inputs": ["low", "close"], "func": f50_tdco_076_short_med_long_breakdown_alignment},
    "f50_tdco_077_ma_violation_count_50_100_200_state": {"inputs": ["close"], "func": f50_tdco_077_ma_violation_count_50_100_200_state},
    "f50_tdco_078_ma_break_sequence_indicator": {"inputs": ["close"], "func": f50_tdco_078_ma_break_sequence_indicator},
    "f50_tdco_079_multi_horizon_drawdown_count_above_20": {"inputs": ["high", "close"], "func": f50_tdco_079_multi_horizon_drawdown_count_above_20},
    "f50_tdco_080_avg_drawdown_across_horizons": {"inputs": ["high", "close"], "func": f50_tdco_080_avg_drawdown_across_horizons},
    "f50_tdco_081_count_horizons_in_decline_63": {"inputs": ["close"], "func": f50_tdco_081_count_horizons_in_decline_63},
    "f50_tdco_082_monotonic_decline_across_horizons": {"inputs": ["close"], "func": f50_tdco_082_monotonic_decline_across_horizons},
    "f50_tdco_083_short_leads_long_decline_indicator": {"inputs": ["close"], "func": f50_tdco_083_short_leads_long_decline_indicator},
    "f50_tdco_084_short_break_in_long_uptrend_indicator": {"inputs": ["low", "close"], "func": f50_tdco_084_short_break_in_long_uptrend_indicator},
    "f50_tdco_085_short_below_50ma_long_above_200ma_state": {"inputs": ["close"], "func": f50_tdco_085_short_below_50ma_long_above_200ma_state},
    "f50_tdco_086_all_horizons_below_respective_ma": {"inputs": ["close"], "func": f50_tdco_086_all_horizons_below_respective_ma},
    "f50_tdco_087_count_mas_breached_in_21d": {"inputs": ["close"], "func": f50_tdco_087_count_mas_breached_in_21d},
    "f50_tdco_088_rolling_correlation_break_close_50ma_63": {"inputs": ["close"], "func": f50_tdco_088_rolling_correlation_break_close_50ma_63},
    "f50_tdco_089_ma_distance_decay_63": {"inputs": ["close"], "func": f50_tdco_089_ma_distance_decay_63},
    "f50_tdco_090_ribbon_compression_breakdown_indicator": {"inputs": ["close"], "func": f50_tdco_090_ribbon_compression_breakdown_indicator},
    "f50_tdco_091_cross_below_50ma_count_252": {"inputs": ["close"], "func": f50_tdco_091_cross_below_50ma_count_252},
    "f50_tdco_092_cross_below_200ma_count_252": {"inputs": ["close"], "func": f50_tdco_092_cross_below_200ma_count_252},
    "f50_tdco_093_multi_ma_below_count_252": {"inputs": ["close"], "func": f50_tdco_093_multi_ma_below_count_252},
    "f50_tdco_094_alignment_at_break_indicator": {"inputs": ["low", "close"], "func": f50_tdco_094_alignment_at_break_indicator},
    "f50_tdco_095_post_break_alignment_decay_63": {"inputs": ["close"], "func": f50_tdco_095_post_break_alignment_decay_63},
    "f50_tdco_096_vol_expansion_post_peak_21": {"inputs": ["close"], "func": f50_tdco_096_vol_expansion_post_peak_21},
    "f50_tdco_097_vol_expansion_post_peak_63": {"inputs": ["close"], "func": f50_tdco_097_vol_expansion_post_peak_63},
    "f50_tdco_098_range_expansion_indicator_21": {"inputs": ["high", "low"], "func": f50_tdco_098_range_expansion_indicator_21},
    "f50_tdco_099_atr_doubling_post_peak_21": {"inputs": ["high", "low", "close"], "func": f50_tdco_099_atr_doubling_post_peak_21},
    "f50_tdco_100_vol_regime_shift_252": {"inputs": ["close"], "func": f50_tdco_100_vol_regime_shift_252},
    "f50_tdco_101_vol_post_peak_zscore_252": {"inputs": ["close"], "func": f50_tdco_101_vol_post_peak_zscore_252},
    "f50_tdco_102_tail_widening_skew_decay_63": {"inputs": ["close"], "func": f50_tdco_102_tail_widening_skew_decay_63},
    "f50_tdco_103_wide_range_red_bar_count_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_103_wide_range_red_bar_count_63},
    "f50_tdco_104_max_single_bar_drop_post_peak_63": {"inputs": ["close"], "func": f50_tdco_104_max_single_bar_drop_post_peak_63},
    "f50_tdco_105_max_single_bar_volume_post_peak_63": {"inputs": ["volume"], "func": f50_tdco_105_max_single_bar_volume_post_peak_63},
    "f50_tdco_106_post_peak_volume_climax_indicator": {"inputs": ["high", "close", "volume"], "func": f50_tdco_106_post_peak_volume_climax_indicator},
    "f50_tdco_107_distribution_volume_zscore_252": {"inputs": ["close", "volume"], "func": f50_tdco_107_distribution_volume_zscore_252},
    "f50_tdco_108_drawdown_acceleration_21": {"inputs": ["high", "close"], "func": f50_tdco_108_drawdown_acceleration_21},
    "f50_tdco_109_drawdown_acceleration_63": {"inputs": ["high", "close"], "func": f50_tdco_109_drawdown_acceleration_63},
    "f50_tdco_110_vol_breakout_index_at_top_21": {"inputs": ["high", "low", "close"], "func": f50_tdco_110_vol_breakout_index_at_top_21},
    "f50_tdco_111_bars_since_252_high": {"inputs": ["high"], "func": f50_tdco_111_bars_since_252_high},
    "f50_tdco_112_bars_since_first_lower_high_post_252_high": {"inputs": ["high"], "func": f50_tdco_112_bars_since_first_lower_high_post_252_high},
    "f50_tdco_113_bars_since_50ma_break": {"inputs": ["close"], "func": f50_tdco_113_bars_since_50ma_break},
    "f50_tdco_114_bars_since_200ma_break": {"inputs": ["close"], "func": f50_tdco_114_bars_since_200ma_break},
    "f50_tdco_115_bars_since_death_cross_50_200": {"inputs": ["close"], "func": f50_tdco_115_bars_since_death_cross_50_200},
    "f50_tdco_116_bars_since_first_minus10pct_drawdown": {"inputs": ["high", "close"], "func": f50_tdco_116_bars_since_first_minus10pct_drawdown},
    "f50_tdco_117_bars_since_first_minus30pct_drawdown": {"inputs": ["high", "close"], "func": f50_tdco_117_bars_since_first_minus30pct_drawdown},
    "f50_tdco_118_bars_since_first_minus50pct_drawdown": {"inputs": ["high", "close"], "func": f50_tdco_118_bars_since_first_minus50pct_drawdown},
    "f50_tdco_119_age_current_below_50ma_episode": {"inputs": ["close"], "func": f50_tdco_119_age_current_below_50ma_episode},
    "f50_tdco_120_age_current_below_200ma_episode": {"inputs": ["close"], "func": f50_tdco_120_age_current_below_200ma_episode},
    "f50_tdco_121_age_current_drawdown_below_10pct": {"inputs": ["high", "close"], "func": f50_tdco_121_age_current_drawdown_below_10pct},
    "f50_tdco_122_time_to_first_minus20_from_peak_252": {"inputs": ["high", "close"], "func": f50_tdco_122_time_to_first_minus20_from_peak_252},
    "f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252": {"inputs": ["high", "close"], "func": f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252},
    "f50_tdco_124_longest_below_50ma_episode_252": {"inputs": ["close"], "func": f50_tdco_124_longest_below_50ma_episode_252},
    "f50_tdco_125_longest_below_200ma_episode_252": {"inputs": ["close"], "func": f50_tdco_125_longest_below_200ma_episode_252},
    "f50_tdco_126_time_since_last_higher_high_63": {"inputs": ["high"], "func": f50_tdco_126_time_since_last_higher_high_63},
    "f50_tdco_127_time_between_consecutive_lower_lows_63": {"inputs": ["low"], "func": f50_tdco_127_time_between_consecutive_lower_lows_63},
    "f50_tdco_128_hazard_rate_new_lower_low_63": {"inputs": ["low"], "func": f50_tdco_128_hazard_rate_new_lower_low_63},
    "f50_tdco_129_streak_length_current_lower_lows": {"inputs": ["low"], "func": f50_tdco_129_streak_length_current_lower_lows},
    "f50_tdco_130_streak_length_current_lower_highs": {"inputs": ["high"], "func": f50_tdco_130_streak_length_current_lower_highs},
    "f50_tdco_131_pre_peak_extension_ratio_252": {"inputs": ["high", "close"], "func": f50_tdco_131_pre_peak_extension_ratio_252},
    "f50_tdco_132_pre_peak_volume_climax_252": {"inputs": ["high", "volume"], "func": f50_tdco_132_pre_peak_volume_climax_252},
    "f50_tdco_133_pre_peak_acceleration_63": {"inputs": ["high", "close"], "func": f50_tdco_133_pre_peak_acceleration_63},
    "f50_tdco_134_pre_peak_parabolic_score": {"inputs": ["high", "close"], "func": f50_tdco_134_pre_peak_parabolic_score},
    "f50_tdco_135_peak_to_minus5pct_decay_velocity": {"inputs": ["high", "close"], "func": f50_tdco_135_peak_to_minus5pct_decay_velocity},
    "f50_tdco_136_peak_to_minus10pct_decay_velocity": {"inputs": ["high", "close"], "func": f50_tdco_136_peak_to_minus10pct_decay_velocity},
    "f50_tdco_137_peak_to_minus20pct_decay_velocity": {"inputs": ["high", "close"], "func": f50_tdco_137_peak_to_minus20pct_decay_velocity},
    "f50_tdco_138_post_peak_first_lower_high_distance": {"inputs": ["high"], "func": f50_tdco_138_post_peak_first_lower_high_distance},
    "f50_tdco_139_post_peak_first_breakdown_distance": {"inputs": ["high", "low", "close"], "func": f50_tdco_139_post_peak_first_breakdown_distance},
    "f50_tdco_140_post_peak_first_50ma_break_distance": {"inputs": ["high", "close"], "func": f50_tdco_140_post_peak_first_50ma_break_distance},
    "f50_tdco_141_post_peak_first_200ma_break_distance": {"inputs": ["high", "close"], "func": f50_tdco_141_post_peak_first_200ma_break_distance},
    "f50_tdco_142_pre_breakdown_distribution_count_63": {"inputs": ["low", "close", "volume"], "func": f50_tdco_142_pre_breakdown_distribution_count_63},
    "f50_tdco_143_pre_breakdown_lower_high_count_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_143_pre_breakdown_lower_high_count_63},
    "f50_tdco_144_pre_breakdown_volume_imbalance_63": {"inputs": ["low", "close", "volume"], "func": f50_tdco_144_pre_breakdown_volume_imbalance_63},
    "f50_tdco_145_pre_breakdown_topping_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_145_pre_breakdown_topping_score},
    "f50_tdco_146_terminal_distribution_master_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_146_terminal_distribution_master_score},
    "f50_tdco_147_stuck_probability_proxy_252": {"inputs": ["high", "close"], "func": f50_tdco_147_stuck_probability_proxy_252},
    "f50_tdco_148_composite_breakdown_severity_252": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_148_composite_breakdown_severity_252},
    "f50_tdco_149_multi_signal_topping_aggregate_at_252_high": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_149_multi_signal_topping_aggregate_at_252_high},
    "f50_tdco_150_terminal_pattern_combined_intensity_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_150_terminal_pattern_combined_intensity_score},
}


# === D2 wrappers + registry (076_150) ===
def f50_tdco_076_short_med_long_breakdown_alignment_d2(low, close): return f50_tdco_076_short_med_long_breakdown_alignment(low, close).diff().diff()
def f50_tdco_077_ma_violation_count_50_100_200_state_d2(close): return f50_tdco_077_ma_violation_count_50_100_200_state(close).diff().diff()
def f50_tdco_078_ma_break_sequence_indicator_d2(close): return f50_tdco_078_ma_break_sequence_indicator(close).diff().diff()
def f50_tdco_079_multi_horizon_drawdown_count_above_20_d2(high, close): return f50_tdco_079_multi_horizon_drawdown_count_above_20(high, close).diff().diff()
def f50_tdco_080_avg_drawdown_across_horizons_d2(high, close): return f50_tdco_080_avg_drawdown_across_horizons(high, close).diff().diff()
def f50_tdco_081_count_horizons_in_decline_63_d2(close): return f50_tdco_081_count_horizons_in_decline_63(close).diff().diff()
def f50_tdco_082_monotonic_decline_across_horizons_d2(close): return f50_tdco_082_monotonic_decline_across_horizons(close).diff().diff()
def f50_tdco_083_short_leads_long_decline_indicator_d2(close): return f50_tdco_083_short_leads_long_decline_indicator(close).diff().diff()
def f50_tdco_084_short_break_in_long_uptrend_indicator_d2(low, close): return f50_tdco_084_short_break_in_long_uptrend_indicator(low, close).diff().diff()
def f50_tdco_085_short_below_50ma_long_above_200ma_state_d2(close): return f50_tdco_085_short_below_50ma_long_above_200ma_state(close).diff().diff()
def f50_tdco_086_all_horizons_below_respective_ma_d2(close): return f50_tdco_086_all_horizons_below_respective_ma(close).diff().diff()
def f50_tdco_087_count_mas_breached_in_21d_d2(close): return f50_tdco_087_count_mas_breached_in_21d(close).diff().diff()
def f50_tdco_088_rolling_correlation_break_close_50ma_63_d2(close): return f50_tdco_088_rolling_correlation_break_close_50ma_63(close).diff().diff()
def f50_tdco_089_ma_distance_decay_63_d2(close): return f50_tdco_089_ma_distance_decay_63(close).diff().diff()
def f50_tdco_090_ribbon_compression_breakdown_indicator_d2(close): return f50_tdco_090_ribbon_compression_breakdown_indicator(close).diff().diff()
def f50_tdco_091_cross_below_50ma_count_252_d2(close): return f50_tdco_091_cross_below_50ma_count_252(close).diff().diff()
def f50_tdco_092_cross_below_200ma_count_252_d2(close): return f50_tdco_092_cross_below_200ma_count_252(close).diff().diff()
def f50_tdco_093_multi_ma_below_count_252_d2(close): return f50_tdco_093_multi_ma_below_count_252(close).diff().diff()
def f50_tdco_094_alignment_at_break_indicator_d2(low, close): return f50_tdco_094_alignment_at_break_indicator(low, close).diff().diff()
def f50_tdco_095_post_break_alignment_decay_63_d2(close): return f50_tdco_095_post_break_alignment_decay_63(close).diff().diff()
def f50_tdco_096_vol_expansion_post_peak_21_d2(close): return f50_tdco_096_vol_expansion_post_peak_21(close).diff().diff()
def f50_tdco_097_vol_expansion_post_peak_63_d2(close): return f50_tdco_097_vol_expansion_post_peak_63(close).diff().diff()
def f50_tdco_098_range_expansion_indicator_21_d2(high, low): return f50_tdco_098_range_expansion_indicator_21(high, low).diff().diff()
def f50_tdco_099_atr_doubling_post_peak_21_d2(high, low, close): return f50_tdco_099_atr_doubling_post_peak_21(high, low, close).diff().diff()
def f50_tdco_100_vol_regime_shift_252_d2(close): return f50_tdco_100_vol_regime_shift_252(close).diff().diff()
def f50_tdco_101_vol_post_peak_zscore_252_d2(close): return f50_tdco_101_vol_post_peak_zscore_252(close).diff().diff()
def f50_tdco_102_tail_widening_skew_decay_63_d2(close): return f50_tdco_102_tail_widening_skew_decay_63(close).diff().diff()
def f50_tdco_103_wide_range_red_bar_count_63_d2(high, low, close): return f50_tdco_103_wide_range_red_bar_count_63(high, low, close).diff().diff()
def f50_tdco_104_max_single_bar_drop_post_peak_63_d2(close): return f50_tdco_104_max_single_bar_drop_post_peak_63(close).diff().diff()
def f50_tdco_105_max_single_bar_volume_post_peak_63_d2(volume): return f50_tdco_105_max_single_bar_volume_post_peak_63(volume).diff().diff()
def f50_tdco_106_post_peak_volume_climax_indicator_d2(high, close, volume): return f50_tdco_106_post_peak_volume_climax_indicator(high, close, volume).diff().diff()
def f50_tdco_107_distribution_volume_zscore_252_d2(close, volume): return f50_tdco_107_distribution_volume_zscore_252(close, volume).diff().diff()
def f50_tdco_108_drawdown_acceleration_21_d2(high, close): return f50_tdco_108_drawdown_acceleration_21(high, close).diff().diff()
def f50_tdco_109_drawdown_acceleration_63_d2(high, close): return f50_tdco_109_drawdown_acceleration_63(high, close).diff().diff()
def f50_tdco_110_vol_breakout_index_at_top_21_d2(high, low, close): return f50_tdco_110_vol_breakout_index_at_top_21(high, low, close).diff().diff()
def f50_tdco_111_bars_since_252_high_d2(high): return f50_tdco_111_bars_since_252_high(high).diff().diff()
def f50_tdco_112_bars_since_first_lower_high_post_252_high_d2(high): return f50_tdco_112_bars_since_first_lower_high_post_252_high(high).diff().diff()
def f50_tdco_113_bars_since_50ma_break_d2(close): return f50_tdco_113_bars_since_50ma_break(close).diff().diff()
def f50_tdco_114_bars_since_200ma_break_d2(close): return f50_tdco_114_bars_since_200ma_break(close).diff().diff()
def f50_tdco_115_bars_since_death_cross_50_200_d2(close): return f50_tdco_115_bars_since_death_cross_50_200(close).diff().diff()
def f50_tdco_116_bars_since_first_minus10pct_drawdown_d2(high, close): return f50_tdco_116_bars_since_first_minus10pct_drawdown(high, close).diff().diff()
def f50_tdco_117_bars_since_first_minus30pct_drawdown_d2(high, close): return f50_tdco_117_bars_since_first_minus30pct_drawdown(high, close).diff().diff()
def f50_tdco_118_bars_since_first_minus50pct_drawdown_d2(high, close): return f50_tdco_118_bars_since_first_minus50pct_drawdown(high, close).diff().diff()
def f50_tdco_119_age_current_below_50ma_episode_d2(close): return f50_tdco_119_age_current_below_50ma_episode(close).diff().diff()
def f50_tdco_120_age_current_below_200ma_episode_d2(close): return f50_tdco_120_age_current_below_200ma_episode(close).diff().diff()
def f50_tdco_121_age_current_drawdown_below_10pct_d2(high, close): return f50_tdco_121_age_current_drawdown_below_10pct(high, close).diff().diff()
def f50_tdco_122_time_to_first_minus20_from_peak_252_d2(high, close): return f50_tdco_122_time_to_first_minus20_from_peak_252(high, close).diff().diff()
def f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252_d2(high, close): return f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252(high, close).diff().diff()
def f50_tdco_124_longest_below_50ma_episode_252_d2(close): return f50_tdco_124_longest_below_50ma_episode_252(close).diff().diff()
def f50_tdco_125_longest_below_200ma_episode_252_d2(close): return f50_tdco_125_longest_below_200ma_episode_252(close).diff().diff()
def f50_tdco_126_time_since_last_higher_high_63_d2(high): return f50_tdco_126_time_since_last_higher_high_63(high).diff().diff()
def f50_tdco_127_time_between_consecutive_lower_lows_63_d2(low): return f50_tdco_127_time_between_consecutive_lower_lows_63(low).diff().diff()
def f50_tdco_128_hazard_rate_new_lower_low_63_d2(low): return f50_tdco_128_hazard_rate_new_lower_low_63(low).diff().diff()
def f50_tdco_129_streak_length_current_lower_lows_d2(low): return f50_tdco_129_streak_length_current_lower_lows(low).diff().diff()
def f50_tdco_130_streak_length_current_lower_highs_d2(high): return f50_tdco_130_streak_length_current_lower_highs(high).diff().diff()
def f50_tdco_131_pre_peak_extension_ratio_252_d2(high, close): return f50_tdco_131_pre_peak_extension_ratio_252(high, close).diff().diff()
def f50_tdco_132_pre_peak_volume_climax_252_d2(high, volume): return f50_tdco_132_pre_peak_volume_climax_252(high, volume).diff().diff()
def f50_tdco_133_pre_peak_acceleration_63_d2(high, close): return f50_tdco_133_pre_peak_acceleration_63(high, close).diff().diff()
def f50_tdco_134_pre_peak_parabolic_score_d2(high, close): return f50_tdco_134_pre_peak_parabolic_score(high, close).diff().diff()
def f50_tdco_135_peak_to_minus5pct_decay_velocity_d2(high, close): return f50_tdco_135_peak_to_minus5pct_decay_velocity(high, close).diff().diff()
def f50_tdco_136_peak_to_minus10pct_decay_velocity_d2(high, close): return f50_tdco_136_peak_to_minus10pct_decay_velocity(high, close).diff().diff()
def f50_tdco_137_peak_to_minus20pct_decay_velocity_d2(high, close): return f50_tdco_137_peak_to_minus20pct_decay_velocity(high, close).diff().diff()
def f50_tdco_138_post_peak_first_lower_high_distance_d2(high): return f50_tdco_138_post_peak_first_lower_high_distance(high).diff().diff()
def f50_tdco_139_post_peak_first_breakdown_distance_d2(high, low, close): return f50_tdco_139_post_peak_first_breakdown_distance(high, low, close).diff().diff()
def f50_tdco_140_post_peak_first_50ma_break_distance_d2(high, close): return f50_tdco_140_post_peak_first_50ma_break_distance(high, close).diff().diff()
def f50_tdco_141_post_peak_first_200ma_break_distance_d2(high, close): return f50_tdco_141_post_peak_first_200ma_break_distance(high, close).diff().diff()
def f50_tdco_142_pre_breakdown_distribution_count_63_d2(low, close, volume): return f50_tdco_142_pre_breakdown_distribution_count_63(low, close, volume).diff().diff()
def f50_tdco_143_pre_breakdown_lower_high_count_63_d2(high, low, close): return f50_tdco_143_pre_breakdown_lower_high_count_63(high, low, close).diff().diff()
def f50_tdco_144_pre_breakdown_volume_imbalance_63_d2(low, close, volume): return f50_tdco_144_pre_breakdown_volume_imbalance_63(low, close, volume).diff().diff()
def f50_tdco_145_pre_breakdown_topping_score_d2(high, low, close, volume): return f50_tdco_145_pre_breakdown_topping_score(high, low, close, volume).diff().diff()
def f50_tdco_146_terminal_distribution_master_score_d2(high, low, close, volume): return f50_tdco_146_terminal_distribution_master_score(high, low, close, volume).diff().diff()
def f50_tdco_147_stuck_probability_proxy_252_d2(high, close): return f50_tdco_147_stuck_probability_proxy_252(high, close).diff().diff()
def f50_tdco_148_composite_breakdown_severity_252_d2(high, low, close, volume): return f50_tdco_148_composite_breakdown_severity_252(high, low, close, volume).diff().diff()
def f50_tdco_149_multi_signal_topping_aggregate_at_252_high_d2(high, low, close, volume): return f50_tdco_149_multi_signal_topping_aggregate_at_252_high(high, low, close, volume).diff().diff()
def f50_tdco_150_terminal_pattern_combined_intensity_score_d2(high, low, close, volume): return f50_tdco_150_terminal_pattern_combined_intensity_score(high, low, close, volume).diff().diff()

TERMINAL_DISTRIBUTION_COMPOSITE_D2_REGISTRY_076_150 = {
    "f50_tdco_076_short_med_long_breakdown_alignment_d2": {"inputs": ["low", "close"], "func": f50_tdco_076_short_med_long_breakdown_alignment_d2},
    "f50_tdco_077_ma_violation_count_50_100_200_state_d2": {"inputs": ["close"], "func": f50_tdco_077_ma_violation_count_50_100_200_state_d2},
    "f50_tdco_078_ma_break_sequence_indicator_d2": {"inputs": ["close"], "func": f50_tdco_078_ma_break_sequence_indicator_d2},
    "f50_tdco_079_multi_horizon_drawdown_count_above_20_d2": {"inputs": ["high", "close"], "func": f50_tdco_079_multi_horizon_drawdown_count_above_20_d2},
    "f50_tdco_080_avg_drawdown_across_horizons_d2": {"inputs": ["high", "close"], "func": f50_tdco_080_avg_drawdown_across_horizons_d2},
    "f50_tdco_081_count_horizons_in_decline_63_d2": {"inputs": ["close"], "func": f50_tdco_081_count_horizons_in_decline_63_d2},
    "f50_tdco_082_monotonic_decline_across_horizons_d2": {"inputs": ["close"], "func": f50_tdco_082_monotonic_decline_across_horizons_d2},
    "f50_tdco_083_short_leads_long_decline_indicator_d2": {"inputs": ["close"], "func": f50_tdco_083_short_leads_long_decline_indicator_d2},
    "f50_tdco_084_short_break_in_long_uptrend_indicator_d2": {"inputs": ["low", "close"], "func": f50_tdco_084_short_break_in_long_uptrend_indicator_d2},
    "f50_tdco_085_short_below_50ma_long_above_200ma_state_d2": {"inputs": ["close"], "func": f50_tdco_085_short_below_50ma_long_above_200ma_state_d2},
    "f50_tdco_086_all_horizons_below_respective_ma_d2": {"inputs": ["close"], "func": f50_tdco_086_all_horizons_below_respective_ma_d2},
    "f50_tdco_087_count_mas_breached_in_21d_d2": {"inputs": ["close"], "func": f50_tdco_087_count_mas_breached_in_21d_d2},
    "f50_tdco_088_rolling_correlation_break_close_50ma_63_d2": {"inputs": ["close"], "func": f50_tdco_088_rolling_correlation_break_close_50ma_63_d2},
    "f50_tdco_089_ma_distance_decay_63_d2": {"inputs": ["close"], "func": f50_tdco_089_ma_distance_decay_63_d2},
    "f50_tdco_090_ribbon_compression_breakdown_indicator_d2": {"inputs": ["close"], "func": f50_tdco_090_ribbon_compression_breakdown_indicator_d2},
    "f50_tdco_091_cross_below_50ma_count_252_d2": {"inputs": ["close"], "func": f50_tdco_091_cross_below_50ma_count_252_d2},
    "f50_tdco_092_cross_below_200ma_count_252_d2": {"inputs": ["close"], "func": f50_tdco_092_cross_below_200ma_count_252_d2},
    "f50_tdco_093_multi_ma_below_count_252_d2": {"inputs": ["close"], "func": f50_tdco_093_multi_ma_below_count_252_d2},
    "f50_tdco_094_alignment_at_break_indicator_d2": {"inputs": ["low", "close"], "func": f50_tdco_094_alignment_at_break_indicator_d2},
    "f50_tdco_095_post_break_alignment_decay_63_d2": {"inputs": ["close"], "func": f50_tdco_095_post_break_alignment_decay_63_d2},
    "f50_tdco_096_vol_expansion_post_peak_21_d2": {"inputs": ["close"], "func": f50_tdco_096_vol_expansion_post_peak_21_d2},
    "f50_tdco_097_vol_expansion_post_peak_63_d2": {"inputs": ["close"], "func": f50_tdco_097_vol_expansion_post_peak_63_d2},
    "f50_tdco_098_range_expansion_indicator_21_d2": {"inputs": ["high", "low"], "func": f50_tdco_098_range_expansion_indicator_21_d2},
    "f50_tdco_099_atr_doubling_post_peak_21_d2": {"inputs": ["high", "low", "close"], "func": f50_tdco_099_atr_doubling_post_peak_21_d2},
    "f50_tdco_100_vol_regime_shift_252_d2": {"inputs": ["close"], "func": f50_tdco_100_vol_regime_shift_252_d2},
    "f50_tdco_101_vol_post_peak_zscore_252_d2": {"inputs": ["close"], "func": f50_tdco_101_vol_post_peak_zscore_252_d2},
    "f50_tdco_102_tail_widening_skew_decay_63_d2": {"inputs": ["close"], "func": f50_tdco_102_tail_widening_skew_decay_63_d2},
    "f50_tdco_103_wide_range_red_bar_count_63_d2": {"inputs": ["high", "low", "close"], "func": f50_tdco_103_wide_range_red_bar_count_63_d2},
    "f50_tdco_104_max_single_bar_drop_post_peak_63_d2": {"inputs": ["close"], "func": f50_tdco_104_max_single_bar_drop_post_peak_63_d2},
    "f50_tdco_105_max_single_bar_volume_post_peak_63_d2": {"inputs": ["volume"], "func": f50_tdco_105_max_single_bar_volume_post_peak_63_d2},
    "f50_tdco_106_post_peak_volume_climax_indicator_d2": {"inputs": ["high", "close", "volume"], "func": f50_tdco_106_post_peak_volume_climax_indicator_d2},
    "f50_tdco_107_distribution_volume_zscore_252_d2": {"inputs": ["close", "volume"], "func": f50_tdco_107_distribution_volume_zscore_252_d2},
    "f50_tdco_108_drawdown_acceleration_21_d2": {"inputs": ["high", "close"], "func": f50_tdco_108_drawdown_acceleration_21_d2},
    "f50_tdco_109_drawdown_acceleration_63_d2": {"inputs": ["high", "close"], "func": f50_tdco_109_drawdown_acceleration_63_d2},
    "f50_tdco_110_vol_breakout_index_at_top_21_d2": {"inputs": ["high", "low", "close"], "func": f50_tdco_110_vol_breakout_index_at_top_21_d2},
    "f50_tdco_111_bars_since_252_high_d2": {"inputs": ["high"], "func": f50_tdco_111_bars_since_252_high_d2},
    "f50_tdco_112_bars_since_first_lower_high_post_252_high_d2": {"inputs": ["high"], "func": f50_tdco_112_bars_since_first_lower_high_post_252_high_d2},
    "f50_tdco_113_bars_since_50ma_break_d2": {"inputs": ["close"], "func": f50_tdco_113_bars_since_50ma_break_d2},
    "f50_tdco_114_bars_since_200ma_break_d2": {"inputs": ["close"], "func": f50_tdco_114_bars_since_200ma_break_d2},
    "f50_tdco_115_bars_since_death_cross_50_200_d2": {"inputs": ["close"], "func": f50_tdco_115_bars_since_death_cross_50_200_d2},
    "f50_tdco_116_bars_since_first_minus10pct_drawdown_d2": {"inputs": ["high", "close"], "func": f50_tdco_116_bars_since_first_minus10pct_drawdown_d2},
    "f50_tdco_117_bars_since_first_minus30pct_drawdown_d2": {"inputs": ["high", "close"], "func": f50_tdco_117_bars_since_first_minus30pct_drawdown_d2},
    "f50_tdco_118_bars_since_first_minus50pct_drawdown_d2": {"inputs": ["high", "close"], "func": f50_tdco_118_bars_since_first_minus50pct_drawdown_d2},
    "f50_tdco_119_age_current_below_50ma_episode_d2": {"inputs": ["close"], "func": f50_tdco_119_age_current_below_50ma_episode_d2},
    "f50_tdco_120_age_current_below_200ma_episode_d2": {"inputs": ["close"], "func": f50_tdco_120_age_current_below_200ma_episode_d2},
    "f50_tdco_121_age_current_drawdown_below_10pct_d2": {"inputs": ["high", "close"], "func": f50_tdco_121_age_current_drawdown_below_10pct_d2},
    "f50_tdco_122_time_to_first_minus20_from_peak_252_d2": {"inputs": ["high", "close"], "func": f50_tdco_122_time_to_first_minus20_from_peak_252_d2},
    "f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252_d2": {"inputs": ["high", "close"], "func": f50_tdco_123_ratio_time_in_drawdown_to_time_at_top_252_d2},
    "f50_tdco_124_longest_below_50ma_episode_252_d2": {"inputs": ["close"], "func": f50_tdco_124_longest_below_50ma_episode_252_d2},
    "f50_tdco_125_longest_below_200ma_episode_252_d2": {"inputs": ["close"], "func": f50_tdco_125_longest_below_200ma_episode_252_d2},
    "f50_tdco_126_time_since_last_higher_high_63_d2": {"inputs": ["high"], "func": f50_tdco_126_time_since_last_higher_high_63_d2},
    "f50_tdco_127_time_between_consecutive_lower_lows_63_d2": {"inputs": ["low"], "func": f50_tdco_127_time_between_consecutive_lower_lows_63_d2},
    "f50_tdco_128_hazard_rate_new_lower_low_63_d2": {"inputs": ["low"], "func": f50_tdco_128_hazard_rate_new_lower_low_63_d2},
    "f50_tdco_129_streak_length_current_lower_lows_d2": {"inputs": ["low"], "func": f50_tdco_129_streak_length_current_lower_lows_d2},
    "f50_tdco_130_streak_length_current_lower_highs_d2": {"inputs": ["high"], "func": f50_tdco_130_streak_length_current_lower_highs_d2},
    "f50_tdco_131_pre_peak_extension_ratio_252_d2": {"inputs": ["high", "close"], "func": f50_tdco_131_pre_peak_extension_ratio_252_d2},
    "f50_tdco_132_pre_peak_volume_climax_252_d2": {"inputs": ["high", "volume"], "func": f50_tdco_132_pre_peak_volume_climax_252_d2},
    "f50_tdco_133_pre_peak_acceleration_63_d2": {"inputs": ["high", "close"], "func": f50_tdco_133_pre_peak_acceleration_63_d2},
    "f50_tdco_134_pre_peak_parabolic_score_d2": {"inputs": ["high", "close"], "func": f50_tdco_134_pre_peak_parabolic_score_d2},
    "f50_tdco_135_peak_to_minus5pct_decay_velocity_d2": {"inputs": ["high", "close"], "func": f50_tdco_135_peak_to_minus5pct_decay_velocity_d2},
    "f50_tdco_136_peak_to_minus10pct_decay_velocity_d2": {"inputs": ["high", "close"], "func": f50_tdco_136_peak_to_minus10pct_decay_velocity_d2},
    "f50_tdco_137_peak_to_minus20pct_decay_velocity_d2": {"inputs": ["high", "close"], "func": f50_tdco_137_peak_to_minus20pct_decay_velocity_d2},
    "f50_tdco_138_post_peak_first_lower_high_distance_d2": {"inputs": ["high"], "func": f50_tdco_138_post_peak_first_lower_high_distance_d2},
    "f50_tdco_139_post_peak_first_breakdown_distance_d2": {"inputs": ["high", "low", "close"], "func": f50_tdco_139_post_peak_first_breakdown_distance_d2},
    "f50_tdco_140_post_peak_first_50ma_break_distance_d2": {"inputs": ["high", "close"], "func": f50_tdco_140_post_peak_first_50ma_break_distance_d2},
    "f50_tdco_141_post_peak_first_200ma_break_distance_d2": {"inputs": ["high", "close"], "func": f50_tdco_141_post_peak_first_200ma_break_distance_d2},
    "f50_tdco_142_pre_breakdown_distribution_count_63_d2": {"inputs": ["low", "close", "volume"], "func": f50_tdco_142_pre_breakdown_distribution_count_63_d2},
    "f50_tdco_143_pre_breakdown_lower_high_count_63_d2": {"inputs": ["high", "low", "close"], "func": f50_tdco_143_pre_breakdown_lower_high_count_63_d2},
    "f50_tdco_144_pre_breakdown_volume_imbalance_63_d2": {"inputs": ["low", "close", "volume"], "func": f50_tdco_144_pre_breakdown_volume_imbalance_63_d2},
    "f50_tdco_145_pre_breakdown_topping_score_d2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_145_pre_breakdown_topping_score_d2},
    "f50_tdco_146_terminal_distribution_master_score_d2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_146_terminal_distribution_master_score_d2},
    "f50_tdco_147_stuck_probability_proxy_252_d2": {"inputs": ["high", "close"], "func": f50_tdco_147_stuck_probability_proxy_252_d2},
    "f50_tdco_148_composite_breakdown_severity_252_d2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_148_composite_breakdown_severity_252_d2},
    "f50_tdco_149_multi_signal_topping_aggregate_at_252_high_d2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_149_multi_signal_topping_aggregate_at_252_high_d2},
    "f50_tdco_150_terminal_pattern_combined_intensity_score_d2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_150_terminal_pattern_combined_intensity_score_d2},
}
