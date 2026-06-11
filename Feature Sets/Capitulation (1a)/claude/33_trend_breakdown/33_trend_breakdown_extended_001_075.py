"""
33_trend_breakdown — Extended Features 001-075
Domain: deeper variants of Parabolic SAR / Supertrend / Aroon / Ichimoku
        (alternate parameters, bars-since-flip, flip counts, distance z-scores,
        streaks); Vortex Indicator (VI+ / VI-); linear-regression slope and
        R-squared trend strength; Chande Kroll Stop; Donchian channel breakdown;
        ADXR; trend-intensity index; Mass Index; choppiness index;
        lower-high / lower-low structural breakdown sequences;
        multi-indicator trend-breakdown confluence scores;
        time-in-downtrend and trend-age features;
        rate-of-change and acceleration variants.
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


def _atr_wilder(close: pd.Series, high: pd.Series, low: pd.Series,
                period: int) -> pd.Series:
    """ATR using Wilder smoothing (exponential, alpha=1/period)."""
    tr = _tr(close, high, low)
    return tr.ewm(alpha=1.0 / period, min_periods=period // 2,
                  adjust=False).mean()


def _adx_components(close: pd.Series, high: pd.Series, low: pd.Series,
                    period: int = 14):
    """Return (adx, plus_di, minus_di) using Wilder smoothing."""
    tr  = _tr(close, high, low)
    dm_plus  = (high - high.shift(1)).clip(lower=0.0)
    dm_minus = (low.shift(1) - low).clip(lower=0.0)
    dm_plus  = dm_plus.where(dm_plus > dm_minus, 0.0)
    dm_minus = dm_minus.where(dm_minus > dm_plus, 0.0)
    atr   = tr.ewm(alpha=1.0 / period, min_periods=period // 2,
                   adjust=False).mean()
    sdi_p = dm_plus.ewm(alpha=1.0 / period, min_periods=period // 2,
                        adjust=False).mean()
    sdi_m = dm_minus.ewm(alpha=1.0 / period, min_periods=period // 2,
                         adjust=False).mean()
    di_p  = _safe_div(sdi_p, atr) * 100
    di_m  = _safe_div(sdi_m, atr) * 100
    dx    = _safe_div((di_p - di_m).abs(), (di_p + di_m).abs()) * 100
    adx   = dx.ewm(alpha=1.0 / period, min_periods=period // 2,
                   adjust=False).mean()
    return adx, di_p, di_m


def _psar_loop(high: pd.Series, low: pd.Series,
               af_step: float = 0.02, af_max: float = 0.2):
    """
    Parabolic SAR via forward-only loop.
    Returns (sar_series, trend_series): trend=1 uptrend, trend=-1 downtrend.
    """
    n = len(high)
    hi = high.values
    lo = low.values
    sar = np.full(n, np.nan)
    trend = np.full(n, np.nan)
    if n < 2:
        return (pd.Series(sar, index=high.index),
                pd.Series(trend, index=high.index))
    is_bull = True
    ep = hi[0]
    af = af_step
    sar[0] = lo[0]
    trend[0] = 1.0
    for i in range(1, n):
        pv = sar[i - 1]
        if is_bull:
            ns = pv + af * (ep - pv)
            ns = min(ns, lo[i - 1])
            if i >= 2:
                ns = min(ns, lo[i - 2])
            if lo[i] < ns:
                is_bull = False
                ns = ep
                ep = lo[i]
                af = af_step
                trend[i] = -1.0
            else:
                trend[i] = 1.0
                if hi[i] > ep:
                    ep = hi[i]
                    af = min(af + af_step, af_max)
        else:
            ns = pv + af * (ep - pv)
            ns = max(ns, hi[i - 1])
            if i >= 2:
                ns = max(ns, hi[i - 2])
            if hi[i] > ns:
                is_bull = True
                ns = ep
                ep = hi[i]
                af = af_step
                trend[i] = 1.0
            else:
                trend[i] = -1.0
                if lo[i] < ep:
                    ep = lo[i]
                    af = min(af + af_step, af_max)
        sar[i] = ns
    return (pd.Series(sar, index=high.index),
            pd.Series(trend, index=high.index))


def _supertrend_loop(close: pd.Series, high: pd.Series, low: pd.Series,
                     atr_period: int = 10, multiplier: float = 3.0):
    """
    Supertrend via forward-only loop.
    Returns (st_line, trend_series): trend=1 uptrend, trend=-1 downtrend.
    """
    n = len(close)
    cl = close.values
    hi = high.values
    lo = low.values
    tr_arr = np.full(n, np.nan)
    for i in range(1, n):
        tr_arr[i] = max(hi[i] - lo[i],
                        abs(hi[i] - cl[i - 1]),
                        abs(lo[i] - cl[i - 1]))
    tr_arr[0] = hi[0] - lo[0]
    atr_arr = np.full(n, np.nan)
    if n >= atr_period:
        atr_arr[atr_period - 1] = np.nanmean(tr_arr[:atr_period])
        alpha = 1.0 / atr_period
        for i in range(atr_period, n):
            atr_arr[i] = atr_arr[i - 1] * (1 - alpha) + tr_arr[i] * alpha
    hl2 = (hi + lo) / 2.0
    ub_basic = hl2 + multiplier * atr_arr
    lb_basic = hl2 - multiplier * atr_arr
    ub = np.full(n, np.nan)
    lb = np.full(n, np.nan)
    st = np.full(n, np.nan)
    trend = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(atr_arr[i]):
            continue
        if i == 0 or np.isnan(ub[i - 1]):
            ub[i] = ub_basic[i]
            lb[i] = lb_basic[i]
            trend[i] = 1.0 if cl[i] > lb_basic[i] else -1.0
            st[i] = lb[i] if trend[i] == 1.0 else ub[i]
            continue
        ub[i] = (ub_basic[i]
                 if ub_basic[i] < ub[i - 1] or cl[i - 1] > ub[i - 1]
                 else ub[i - 1])
        lb[i] = (lb_basic[i]
                 if lb_basic[i] > lb[i - 1] or cl[i - 1] < lb[i - 1]
                 else lb[i - 1])
        pt = trend[i - 1]
        trend[i] = (-1.0 if cl[i] < lb[i] else 1.0) if pt == 1.0 \
                   else (1.0 if cl[i] > ub[i] else -1.0)
        st[i] = lb[i] if trend[i] == 1.0 else ub[i]
    return (pd.Series(st, index=close.index),
            pd.Series(trend, index=close.index))


def _linreg_slope_rsq(s: pd.Series, w: int):
    """
    Rolling OLS slope and R-squared over w periods.
    Returns (slope_series, rsq_series).
    Uses raw=False apply — returns scalar per window (no array returned).
    """
    def _slope_fn(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        ss_xy = ((xi - xi_m) * (x - x_m)).sum()
        ss_xx = ((xi - xi_m) ** 2).sum()
        if ss_xx == 0:
            return np.nan
        return ss_xy / ss_xx

    def _rsq_fn(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        ss_xy = ((xi - xi_m) * (x - x_m)).sum()
        ss_xx = ((xi - xi_m) ** 2).sum()
        ss_yy = ((x - x_m) ** 2).sum()
        if ss_xx == 0 or ss_yy == 0:
            return np.nan
        b = ss_xy / ss_xx
        ss_res = ss_yy - b * ss_xy
        return max(0.0, 1.0 - ss_res / ss_yy)

    slope = s.rolling(w, min_periods=max(2, w // 2)).apply(_slope_fn, raw=False)
    rsq   = s.rolling(w, min_periods=max(2, w // 2)).apply(_rsq_fn, raw=False)
    return slope, rsq


# ── Feature functions (tbd_ext_001 … tbd_ext_075) ────────────────────────────

# ── Group A: PSAR alternate parameters (001-007) ─────────────────────────────

def tbd_ext_001_psar_slow_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Parabolic SAR with slower AF (step=0.01, max=0.1) in bearish state."""
    _, trend = _psar_loop(high, low, af_step=0.01, af_max=0.1)
    return (trend < 0).astype(float)


def tbd_ext_002_psar_slow_flip_to_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: slow-AF PSAR flips to bearish (step=0.01, max=0.1)."""
    _, trend = _psar_loop(high, low, af_step=0.01, af_max=0.1)
    b = trend < 0
    return (b & ~b.shift(1).fillna(False)).astype(float)


def tbd_ext_003_psar_slow_bars_since_bearish_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since slow-AF PSAR last flipped to bearish."""
    return _days_since(tbd_ext_002_psar_slow_flip_to_bearish_event(close, high, low))


def tbd_ext_004_psar_fast_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Parabolic SAR with faster AF (step=0.04, max=0.4) in bearish state."""
    _, trend = _psar_loop(high, low, af_step=0.04, af_max=0.4)
    return (trend < 0).astype(float)


def tbd_ext_005_psar_fast_flip_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of fast-AF PSAR bearish-flip events in trailing 63 days."""
    _, trend = _psar_loop(high, low, af_step=0.04, af_max=0.4)
    b = trend < 0
    event = (b & ~b.shift(1).fillna(False)).astype(float)
    return _rolling_sum(event, _TD_QTR)


def tbd_ext_006_psar_slow_distance_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of slow-AF PSAR (close-SAR)/close distance over 126-day window."""
    sar, _ = _psar_loop(high, low, af_step=0.01, af_max=0.1)
    dist = _safe_div(close - sar, close)
    m = _rolling_mean(dist, _TD_HALF)
    s = _rolling_std(dist, _TD_HALF)
    return _safe_div(dist - m, s)


def tbd_ext_007_psar_dual_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: both slow-AF and fast-AF Parabolic SAR are simultaneously bearish."""
    _, t_slow = _psar_loop(high, low, af_step=0.01, af_max=0.1)
    _, t_fast = _psar_loop(high, low, af_step=0.04, af_max=0.4)
    return ((t_slow < 0) & (t_fast < 0)).astype(float)


# ── Group B: Supertrend alternate parameters (008-015) ───────────────────────

def tbd_ext_008_supertrend_7_2_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Supertrend(ATR=7, mult=2.0) in bearish/downtrend state."""
    _, trend = _supertrend_loop(close, high, low, atr_period=7, multiplier=2.0)
    return (trend < 0).astype(float)


def tbd_ext_009_supertrend_7_2_flip_to_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Supertrend(7,2) flips from uptrend to downtrend."""
    _, trend = _supertrend_loop(close, high, low, atr_period=7, multiplier=2.0)
    b = trend < 0
    return (b & ~b.shift(1).fillna(False)).astype(float)


def tbd_ext_010_supertrend_7_2_bars_since_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars elapsed since Supertrend(7,2) last flipped to bearish."""
    return _days_since(tbd_ext_009_supertrend_7_2_flip_to_bearish_event(close, high, low))


def tbd_ext_011_supertrend_14_4_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Supertrend(ATR=14, mult=4.0) in bearish state — loose/wide band."""
    _, trend = _supertrend_loop(close, high, low, atr_period=14, multiplier=4.0)
    return (trend < 0).astype(float)


def tbd_ext_012_supertrend_14_4_flip_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Supertrend(14,4) bearish-flip events in trailing 252 days."""
    _, trend = _supertrend_loop(close, high, low, atr_period=14, multiplier=4.0)
    b = trend < 0
    event = (b & ~b.shift(1).fillna(False)).astype(float)
    return _rolling_sum(event, _TD_YEAR)


def tbd_ext_013_supertrend_7_2_distance_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Supertrend(7,2) distance (close-ST)/close over 63-day window."""
    st_line, _ = _supertrend_loop(close, high, low, atr_period=7, multiplier=2.0)
    dist = _safe_div(close - st_line, close)
    m = _rolling_mean(dist, _TD_QTR)
    s = _rolling_std(dist, _TD_QTR)
    return _safe_div(dist - m, s)


def tbd_ext_014_supertrend_triple_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ST(7,2), ST(10,3), and ST(14,4) all simultaneously in bearish state."""
    _, t1 = _supertrend_loop(close, high, low, atr_period=7,  multiplier=2.0)
    _, t2 = _supertrend_loop(close, high, low, atr_period=10, multiplier=3.0)
    _, t3 = _supertrend_loop(close, high, low, atr_period=14, multiplier=4.0)
    return ((t1 < 0) & (t2 < 0) & (t3 < 0)).astype(float)


def tbd_ext_015_supertrend_7_2_bearish_fraction_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days Supertrend(7,2) was in bearish state."""
    _, trend = _supertrend_loop(close, high, low, atr_period=7, multiplier=2.0)
    return _rolling_count_true(trend < 0, _TD_HALF) / _TD_HALF


# ── Group C: Aroon deeper variants (016-022) ─────────────────────────────────

def tbd_ext_016_aroon_down50_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Down(50) > Aroon Up(50) — long-period bearish Aroon dominance."""
    w = 51
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    dn = (50 - bsl) / 50 * 100
    up = (50 - bsh) / 50 * 100
    return (dn > up).astype(float)


def tbd_ext_017_aroon_oscillator50_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator(50) value: Up50 - Down50; negative = bearish."""
    w = 51
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    up = (50 - bsh) / 50 * 100
    dn = (50 - bsl) / 50 * 100
    return up - dn


def tbd_ext_018_aroon_bearish_cross_event25(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Aroon Down(25) crosses above Aroon Up(25) (bearish cross event)."""
    w = 26
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    dn = (25 - bsl) / 25 * 100
    up = (25 - bsh) / 25 * 100
    b = dn > up
    return (b & ~b.shift(1).fillna(False)).astype(float)


def tbd_ext_019_aroon_down14_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars Aroon Down(14) has been above Aroon Up(14)."""
    w = 15
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    dn = (14 - bsl) / 14 * 100
    up = (14 - bsh) / 14 * 100
    return _consec_streak(dn > up)


def tbd_ext_020_aroon_down25_above_90_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Down(25) >= 90 (extreme recent-low dominance, 25-period)."""
    w = 26
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    dn = (25 - bsl) / 25 * 100
    return (dn >= 90).astype(float)


def tbd_ext_021_aroon_bearish_cross_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Aroon(25) bearish cross events in trailing 252 days."""
    return _rolling_sum(tbd_ext_018_aroon_bearish_cross_event25(close, high, low), _TD_YEAR)


def tbd_ext_022_aroon_osc14_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Aroon Oscillator(14) over 126-day rolling window."""
    w = 15
    def _bs_h(arr): return float(len(arr) - 1 - np.argmax(arr))
    def _bs_l(arr): return float(len(arr) - 1 - np.argmin(arr))
    bsh = high.rolling(w, min_periods=w).apply(_bs_h, raw=True)
    bsl = low.rolling(w, min_periods=w).apply(_bs_l, raw=True)
    osc = ((14 - bsh) / 14 * 100) - ((14 - bsl) / 14 * 100)
    m = _rolling_mean(osc, _TD_HALF)
    s = _rolling_std(osc, _TD_HALF)
    return _safe_div(osc - m, s)


# ── Group D: Ichimoku deeper variants (023-030) ───────────────────────────────

def tbd_ext_023_ichimoku_below_cloud_days_since(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since close last entered below the entire Ichimoku cloud."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    cloud_bot = pd.concat([span_a, span_b], axis=1).min(axis=1)
    below = close < cloud_bot
    entry = (below & ~below.shift(1).fillna(False))
    return _days_since(entry)


def tbd_ext_024_ichimoku_cloud_thickness_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ichimoku cloud thickness (|Span A - Span B|) normalized by close."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    return _safe_div((span_a - span_b).abs(), close)


def tbd_ext_025_ichimoku_kijun_slope_negative_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Kijun-sen (base line) slope is negative (declining medium-term level)."""
    kijun = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    return (kijun < kijun.shift(1)).astype(float)


def tbd_ext_026_ichimoku_tenkan_slope_negative_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Tenkan-sen (conversion) slope is negative (short-term deterioration)."""
    tenkan = (_rolling_max(high, 9) + _rolling_min(low, 9)) / 2.0
    return (tenkan < tenkan.shift(1)).astype(float)


def tbd_ext_027_ichimoku_spanb_slope_negative_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Span B slope is negative (52-period cloud base declining)."""
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    return (span_b < span_b.shift(1)).astype(float)


def tbd_ext_028_ichimoku_all_lines_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Tenkan < Kijun AND cloud is bearish (Span B > Span A)."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    return ((close < tenkan) & (tenkan < kijun) & (span_b > span_a)).astype(float)


def tbd_ext_029_ichimoku_distance_below_cloud_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Ichimoku distance-below-cloud over 252-day window."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    span_a = (tenkan + kijun) / 2.0
    span_b = (_rolling_max(high, 52) + _rolling_min(low, 52)) / 2.0
    cloud_bot = pd.concat([span_a, span_b], axis=1).min(axis=1)
    dist = _safe_div((cloud_bot - close).clip(lower=0.0), close)
    m = _rolling_mean(dist, _TD_YEAR)
    s = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - m, s)


def tbd_ext_030_ichimoku_tenkan_kijun_bearish_cross_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Ichimoku Tenkan/Kijun bearish cross events in trailing 63 days."""
    tenkan = (_rolling_max(high, 9)  + _rolling_min(low, 9))  / 2.0
    kijun  = (_rolling_max(high, 26) + _rolling_min(low, 26)) / 2.0
    below = tenkan < kijun
    event = (below & ~below.shift(1).fillna(False)).astype(float)
    return _rolling_sum(event, _TD_QTR)


# ── Group E: Vortex Indicator (031-036) ──────────────────────────────────────

def _vortex_components(high: pd.Series, low: pd.Series, close: pd.Series,
                       period: int = 14):
    """
    Vortex Indicator: VI+ and VI-.
    VM+  = |High[i] - Low[i-1]|
    VM-  = |Low[i]  - High[i-1]|
    TR   = max(H-L, |H-PC|, |L-PC|)
    VI+  = sum(VM+, n) / sum(TR, n)
    VI-  = sum(VM-, n) / sum(TR, n)
    Returns (vi_plus, vi_minus).
    """
    vm_plus  = (high - low.shift(1)).abs()
    vm_minus = (low - high.shift(1)).abs()
    tr = _tr(close, high, low)
    vi_plus  = _safe_div(_rolling_sum(vm_plus,  period),
                         _rolling_sum(tr, period))
    vi_minus = _safe_div(_rolling_sum(vm_minus, period),
                         _rolling_sum(tr, period))
    return vi_plus, vi_minus


def tbd_ext_031_vortex14_vi_minus_above_vi_plus_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Vortex VI-(14) > VI+(14) — negative vortex dominance (bearish)."""
    vp, vm = _vortex_components(high, low, close, 14)
    return (vm > vp).astype(float)


def tbd_ext_032_vortex14_bearish_cross_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: VI-(14) crosses above VI+(14) (bearish Vortex crossover event)."""
    vp, vm = _vortex_components(high, low, close, 14)
    b = vm > vp
    return (b & ~b.shift(1).fillna(False)).astype(float)


def tbd_ext_033_vortex14_days_since_bearish_cross(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since last Vortex(14) VI- crossed above VI+."""
    return _days_since(tbd_ext_032_vortex14_bearish_cross_event(close, high, low))


def tbd_ext_034_vortex14_vi_minus_minus_vi_plus(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Vortex(14) spread: VI- minus VI+; positive = bearish dominance."""
    vp, vm = _vortex_components(high, low, close, 14)
    return vm - vp


def tbd_ext_035_vortex21_vi_minus_above_vi_plus_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Vortex VI-(21) > VI+(21) — longer-period bearish vortex state."""
    vp, vm = _vortex_components(high, low, close, 21)
    return (vm > vp).astype(float)


def tbd_ext_036_vortex14_bearish_cross_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Vortex(14) bearish cross events in trailing 252 days."""
    return _rolling_sum(tbd_ext_032_vortex14_bearish_cross_event(close, high, low), _TD_YEAR)


# ── Group F: Linear-regression slope and R-squared (037-044) ─────────────────

def tbd_ext_037_linreg_slope_21d_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: OLS slope of close over 21-day window is negative."""
    slope, _ = _linreg_slope_rsq(close, _TD_MON)
    return (slope < 0).astype(float)


def tbd_ext_038_linreg_slope_63d_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: OLS slope of close over 63-day window is negative."""
    slope, _ = _linreg_slope_rsq(close, _TD_QTR)
    return (slope < 0).astype(float)


def tbd_ext_039_linreg_slope_21d_value(close: pd.Series) -> pd.Series:
    """OLS slope of close over 21-day window (raw slope value per bar)."""
    slope, _ = _linreg_slope_rsq(close, _TD_MON)
    return slope


def tbd_ext_040_linreg_slope_63d_value(close: pd.Series) -> pd.Series:
    """OLS slope of close over 63-day window (raw slope value per bar)."""
    slope, _ = _linreg_slope_rsq(close, _TD_QTR)
    return slope


def tbd_ext_041_linreg_rsq_21d_value(close: pd.Series) -> pd.Series:
    """OLS R-squared of close over 21-day window (trend-line fit quality)."""
    _, rsq = _linreg_slope_rsq(close, _TD_MON)
    return rsq


def tbd_ext_042_linreg_rsq_63d_value(close: pd.Series) -> pd.Series:
    """OLS R-squared of close over 63-day window."""
    _, rsq = _linreg_slope_rsq(close, _TD_QTR)
    return rsq


def tbd_ext_043_linreg_bearish_trend_strength_21d(close: pd.Series) -> pd.Series:
    """Bearish trend strength: R-squared * (1 if slope<0 else 0), 21-day."""
    slope, rsq = _linreg_slope_rsq(close, _TD_MON)
    return rsq * (slope < 0).astype(float)


def tbd_ext_044_linreg_slope_neg_streak_21d(close: pd.Series) -> pd.Series:
    """Consecutive days 21-day OLS slope has been negative."""
    slope, _ = _linreg_slope_rsq(close, _TD_MON)
    return _consec_streak(slope < 0)


# ── Group G: Chande Kroll Stop (045-049) ─────────────────────────────────────

def _chande_kroll_stop(close: pd.Series, high: pd.Series, low: pd.Series,
                       atr_p: int = 10, atr_q: int = 3, stop_p: int = 9):
    """
    Chande Kroll Stop (backward-looking only).
    Step 1: ATR(atr_p) using Wilder smoothing.
    Step 2: first_high = rolling_max(high, atr_p) - atr_q * ATR(atr_p)
            first_low  = rolling_min(low,  atr_p) + atr_q * ATR(atr_p)
    Step 3: stop_short = rolling_max(first_high, stop_p)
            stop_long  = rolling_min(first_low,  stop_p)
    Returns (stop_short, stop_long).
    Price below stop_short = bearish.
    """
    atr = _atr_wilder(close, high, low, atr_p)
    first_high = _rolling_max(high, atr_p) - atr_q * atr
    first_low  = _rolling_min(low,  atr_p) + atr_q * atr
    stop_short = _rolling_max(first_high, stop_p)
    stop_long  = _rolling_min(first_low,  stop_p)
    return stop_short, stop_long


def tbd_ext_045_chande_kroll_bearish_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close < Chande Kroll Stop_Short (CKS bearish state, default params)."""
    stop_short, _ = _chande_kroll_stop(close, high, low)
    return (close < stop_short).astype(float)


def tbd_ext_046_chande_kroll_flip_to_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: close drops below Chande Kroll Stop_Short (CKS bearish flip)."""
    stop_short, _ = _chande_kroll_stop(close, high, low)
    b = close < stop_short
    return (b & ~b.shift(1).fillna(False)).astype(float)


def tbd_ext_047_chande_kroll_bars_since_bearish_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars elapsed since close last crossed below Chande Kroll Stop_Short."""
    return _days_since(tbd_ext_046_chande_kroll_flip_to_bearish_event(close, high, low))


def tbd_ext_048_chande_kroll_distance_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - CKS_Stop_Short) / close; negative = bearish (below stop)."""
    stop_short, _ = _chande_kroll_stop(close, high, low)
    return _safe_div(close - stop_short, close)


def tbd_ext_049_chande_kroll_bearish_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars close has been below Chande Kroll Stop_Short."""
    stop_short, _ = _chande_kroll_stop(close, high, low)
    return _consec_streak(close < stop_short)


# ── Group H: Donchian channel breakdown (050-054) ────────────────────────────

def tbd_ext_050_donchian_20_close_near_lower_band(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - Donchian_lower_20) / (Donchian_upper_20 - Donchian_lower_20); 0=bottom."""
    upper = _rolling_max(high, _TD_MON)
    lower = _rolling_min(low,  _TD_MON)
    return _safe_div(close - lower, upper - lower)


def tbd_ext_051_donchian_52_close_below_midpoint_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close below midpoint of 52-week Donchian channel."""
    upper = _rolling_max(high, 252)
    lower = _rolling_min(low,  252)
    mid   = (upper + lower) / 2.0
    return (close < mid).astype(float)


def tbd_ext_052_donchian_20_lower_band_slope_negative(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 20-day Donchian lower band is declining (lower lows trend)."""
    lower = _rolling_min(low, _TD_MON)
    return (lower < lower.shift(1)).astype(float)


def tbd_ext_053_donchian_63_close_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position of close within 63-day Donchian channel: 0=bottom, 1=top."""
    upper = _rolling_max(high, _TD_QTR)
    lower = _rolling_min(low,  _TD_QTR)
    return _safe_div(close - lower, upper - lower)


def tbd_ext_054_donchian_breakout_lower_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: close breaks below 20-day Donchian lower band (new 20-day low)."""
    lower = _rolling_min(low.shift(1), _TD_MON)
    return (close < lower).astype(float)


# ── Group I: ADXR and trend-intensity (055-059) ───────────────────────────────

def tbd_ext_055_adxr14_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADXR(14) = (ADX[today] + ADX[today-14]) / 2; slower-reacting ADX variant."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return (adx + adx.shift(14)) / 2.0


def tbd_ext_056_adxr14_below_20_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADXR(14) < 20 (weak averaged trend strength)."""
    adxr = tbd_ext_055_adxr14_value(close, high, low)
    return (adxr < 20).astype(float)


def tbd_ext_057_trend_intensity_index_21d(close: pd.Series) -> pd.Series:
    """
    Trend Intensity Index (TII, 21-day): 100 * (up_closes_above_sma) / 21.
    Counts how many of last 21 closes are above the 21-period SMA midpoint.
    Values < 50 indicate a downtrend / bearish bias.
    """
    sma = _rolling_mean(close, _TD_MON)
    above = (close > sma).astype(float)
    return _rolling_sum(above, _TD_MON) / _TD_MON * 100


def tbd_ext_058_trend_intensity_index_below_50_flag(close: pd.Series) -> pd.Series:
    """Flag: TII(21) < 50 — bearish trend intensity regime."""
    return (tbd_ext_057_trend_intensity_index_21d(close) < 50).astype(float)


def tbd_ext_059_adxr14_collapse_from_peak_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADXR(14) drop from its 63-day peak (slow-trend-strength dissipation)."""
    adxr = tbd_ext_055_adxr14_value(close, high, low)
    peak = _rolling_max(adxr, _TD_QTR)
    return peak - adxr


# ── Group J: Mass Index (060-062) ────────────────────────────────────────────

def _mass_index(high: pd.Series, low: pd.Series, fast: int = 9,
                slow: int = 25) -> pd.Series:
    """
    Mass Index = sum(EMA(H-L, fast) / EMA(EMA(H-L, fast), fast), slow).
    Identifies reversal bulges; high values signal potential trend exhaustion.
    """
    hl = high - low
    ema1 = _ewm_mean(hl, fast)
    ema2 = _ewm_mean(ema1, fast)
    ratio = _safe_div(ema1, ema2)
    return _rolling_sum(ratio, slow)


def tbd_ext_060_mass_index_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index(9,25) value; values > 27 signal potential reversal bulge."""
    return _mass_index(high, low)


def tbd_ext_061_mass_index_above_27_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Mass Index > 27 (reversal bulge — often precedes trend reversal)."""
    return (_mass_index(high, low) > 27).astype(float)


def tbd_ext_062_mass_index_above_26_5_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Mass Index > 26.5 (alert threshold for potential reversal setup)."""
    return (_mass_index(high, low) > 26.5).astype(float)


# ── Group K: Choppiness Index (063-065) ──────────────────────────────────────

def _choppiness_index(close: pd.Series, high: pd.Series, low: pd.Series,
                      period: int = 14) -> pd.Series:
    """
    Choppiness Index = 100 * log10(sum(ATR1, n) / (max_high - min_low)) / log10(n).
    Range 0-100; >61.8 = choppy/trendless, <38.2 = strongly trending.
    """
    tr1 = _tr(close, high, low)
    atr_sum = _rolling_sum(tr1, period)
    h_max   = _rolling_max(high, period)
    l_min   = _rolling_min(low,  period)
    hl_range = h_max - l_min
    ratio = _safe_div(atr_sum, hl_range)
    log_n = np.log10(float(period))
    return 100.0 * ratio.apply(lambda x: np.log10(x) if (not np.isnan(x) and x > 0) else np.nan) / log_n


def tbd_ext_063_choppiness_index_14_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Choppiness Index(14) value; >61.8 = trendless, <38.2 = strongly trending."""
    return _choppiness_index(close, high, low, 14)


def tbd_ext_064_choppiness_index_14_above_61_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Choppiness Index(14) > 61.8 — market is choppy, trend lost."""
    return (_choppiness_index(close, high, low, 14) > 61.8).astype(float)


def tbd_ext_065_choppiness_index_21_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Choppiness Index(21) value — monthly trend quality measure."""
    return _choppiness_index(close, high, low, 21)


# ── Group L: Lower-high / lower-low structural breakdown (066-069) ────────────

def tbd_ext_066_lh_only_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with a lower-high (only, regardless of low) in 21 days."""
    return _rolling_count_true(high < high.shift(1), _TD_MON)


def tbd_ext_067_ll_only_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with a lower-low (only, regardless of high) in 21 days."""
    return _rolling_count_true(low < low.shift(1), _TD_MON)


def tbd_ext_068_lh_ll_sequence_net_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(LH_count + LL_count - HH_count - HL_count) in 63-day window; positive = bearish."""
    lh = _rolling_count_true(high < high.shift(1), _TD_QTR)
    ll = _rolling_count_true(low  < low.shift(1),  _TD_QTR)
    hh = _rolling_count_true(high > high.shift(1), _TD_QTR)
    hl = _rolling_count_true(low  > low.shift(1),  _TD_QTR)
    return (lh + ll) - (hh + hl)


def tbd_ext_069_consecutive_lh_ll_days_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with EITHER lower-high OR lower-low (broad downward pressure)."""
    return _consec_streak((high < high.shift(1)) | (low < low.shift(1)))


# ── Group M: Multi-indicator confluence scores (070-073) ─────────────────────

def tbd_ext_070_vi_psar_st_bearish_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Confluence score (0-3): Vortex(14) bearish + PSAR bearish + ST(10,3) bearish."""
    vp, vm = _vortex_components(high, low, close, 14)
    vi_bear = (vm > vp).astype(float)
    _, psar_trend = _psar_loop(high, low)
    psar_bear = (psar_trend < 0).astype(float)
    _, st_trend = _supertrend_loop(close, high, low, 10, 3.0)
    st_bear = (st_trend < 0).astype(float)
    return vi_bear + psar_bear + st_bear


def tbd_ext_071_linreg_vi_adxr_confluence_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Confluence score (0-3): slope(21)<0 + VI-(14)>VI+(14) + ADXR<25."""
    slope, _ = _linreg_slope_rsq(close, _TD_MON)
    s1 = (slope < 0).astype(float)
    vp, vm = _vortex_components(high, low, close, 14)
    s2 = (vm > vp).astype(float)
    adxr = tbd_ext_055_adxr14_value(close, high, low)
    s3 = (adxr < 25).astype(float)
    return s1 + s2 + s3


def tbd_ext_072_chande_kroll_donchian_breakdown_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Confluence score (0-2): CKS bearish + Donchian 52-week below midpoint."""
    stop_short, _ = _chande_kroll_stop(close, high, low)
    s1 = (close < stop_short).astype(float)
    upper = _rolling_max(high, 252)
    lower = _rolling_min(low,  252)
    mid   = (upper + lower) / 2.0
    s2 = (close < mid).astype(float)
    return s1 + s2


def tbd_ext_073_full_extended_breakdown_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Extended breakdown confluence score (0-6):
    VI-(14)>VI+(14) + ST(7,2) bearish + CKS bearish + slope(21)<0
    + Choppiness>61.8 + Donchian(63) position<0.25.
    """
    vp, vm = _vortex_components(high, low, close, 14)
    s1 = (vm > vp).astype(float)
    _, t2 = _supertrend_loop(close, high, low, 7, 2.0)
    s2 = (t2 < 0).astype(float)
    stop_short, _ = _chande_kroll_stop(close, high, low)
    s3 = (close < stop_short).astype(float)
    slope, _ = _linreg_slope_rsq(close, _TD_MON)
    s4 = (slope < 0).astype(float)
    chop = _choppiness_index(close, high, low, 14)
    s5 = (chop > 61.8).astype(float)
    upper = _rolling_max(high, _TD_QTR)
    lower = _rolling_min(low,  _TD_QTR)
    pos = _safe_div(close - lower, upper - lower)
    s6 = (pos < 0.25).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6


# ── Group N: ROC / acceleration variants (074-075) ────────────────────────────

def tbd_ext_074_roc_21d_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day rate-of-change (ROC) is negative — price lower than 21 days ago."""
    roc = _safe_div(close - close.shift(_TD_MON), close.shift(_TD_MON)) * 100
    return (roc < 0).astype(float)


def tbd_ext_075_roc_63d_acceleration_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day ROC is declining (ROC today < ROC 21 days ago) — bearish acceleration."""
    roc = _safe_div(close - close.shift(_TD_QTR), close.shift(_TD_QTR)) * 100
    return (roc < roc.shift(_TD_MON)).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_EXTENDED_REGISTRY_001_075 = {
    "tbd_ext_001_psar_slow_bearish_flag":                       {"inputs": ["close", "high", "low"], "func": tbd_ext_001_psar_slow_bearish_flag},
    "tbd_ext_002_psar_slow_flip_to_bearish_event":              {"inputs": ["close", "high", "low"], "func": tbd_ext_002_psar_slow_flip_to_bearish_event},
    "tbd_ext_003_psar_slow_bars_since_bearish_flip":            {"inputs": ["close", "high", "low"], "func": tbd_ext_003_psar_slow_bars_since_bearish_flip},
    "tbd_ext_004_psar_fast_bearish_flag":                       {"inputs": ["close", "high", "low"], "func": tbd_ext_004_psar_fast_bearish_flag},
    "tbd_ext_005_psar_fast_flip_count_63d":                     {"inputs": ["close", "high", "low"], "func": tbd_ext_005_psar_fast_flip_count_63d},
    "tbd_ext_006_psar_slow_distance_zscore_126d":               {"inputs": ["close", "high", "low"], "func": tbd_ext_006_psar_slow_distance_zscore_126d},
    "tbd_ext_007_psar_dual_bearish_flag":                       {"inputs": ["close", "high", "low"], "func": tbd_ext_007_psar_dual_bearish_flag},
    "tbd_ext_008_supertrend_7_2_bearish_flag":                  {"inputs": ["close", "high", "low"], "func": tbd_ext_008_supertrend_7_2_bearish_flag},
    "tbd_ext_009_supertrend_7_2_flip_to_bearish_event":         {"inputs": ["close", "high", "low"], "func": tbd_ext_009_supertrend_7_2_flip_to_bearish_event},
    "tbd_ext_010_supertrend_7_2_bars_since_flip":               {"inputs": ["close", "high", "low"], "func": tbd_ext_010_supertrend_7_2_bars_since_flip},
    "tbd_ext_011_supertrend_14_4_bearish_flag":                 {"inputs": ["close", "high", "low"], "func": tbd_ext_011_supertrend_14_4_bearish_flag},
    "tbd_ext_012_supertrend_14_4_flip_count_252d":              {"inputs": ["close", "high", "low"], "func": tbd_ext_012_supertrend_14_4_flip_count_252d},
    "tbd_ext_013_supertrend_7_2_distance_zscore_63d":           {"inputs": ["close", "high", "low"], "func": tbd_ext_013_supertrend_7_2_distance_zscore_63d},
    "tbd_ext_014_supertrend_triple_bearish_flag":               {"inputs": ["close", "high", "low"], "func": tbd_ext_014_supertrend_triple_bearish_flag},
    "tbd_ext_015_supertrend_7_2_bearish_fraction_126d":         {"inputs": ["close", "high", "low"], "func": tbd_ext_015_supertrend_7_2_bearish_fraction_126d},
    "tbd_ext_016_aroon_down50_flag":                            {"inputs": ["close", "high", "low"], "func": tbd_ext_016_aroon_down50_flag},
    "tbd_ext_017_aroon_oscillator50_value":                     {"inputs": ["close", "high", "low"], "func": tbd_ext_017_aroon_oscillator50_value},
    "tbd_ext_018_aroon_bearish_cross_event25":                  {"inputs": ["close", "high", "low"], "func": tbd_ext_018_aroon_bearish_cross_event25},
    "tbd_ext_019_aroon_down14_streak":                          {"inputs": ["close", "high", "low"], "func": tbd_ext_019_aroon_down14_streak},
    "tbd_ext_020_aroon_down25_above_90_flag":                   {"inputs": ["close", "high", "low"], "func": tbd_ext_020_aroon_down25_above_90_flag},
    "tbd_ext_021_aroon_bearish_cross_count_252d":               {"inputs": ["close", "high", "low"], "func": tbd_ext_021_aroon_bearish_cross_count_252d},
    "tbd_ext_022_aroon_osc14_zscore_126d":                      {"inputs": ["close", "high", "low"], "func": tbd_ext_022_aroon_osc14_zscore_126d},
    "tbd_ext_023_ichimoku_below_cloud_days_since":              {"inputs": ["close", "high", "low"], "func": tbd_ext_023_ichimoku_below_cloud_days_since},
    "tbd_ext_024_ichimoku_cloud_thickness_norm":                {"inputs": ["close", "high", "low"], "func": tbd_ext_024_ichimoku_cloud_thickness_norm},
    "tbd_ext_025_ichimoku_kijun_slope_negative_flag":           {"inputs": ["close", "high", "low"], "func": tbd_ext_025_ichimoku_kijun_slope_negative_flag},
    "tbd_ext_026_ichimoku_tenkan_slope_negative_flag":          {"inputs": ["close", "high", "low"], "func": tbd_ext_026_ichimoku_tenkan_slope_negative_flag},
    "tbd_ext_027_ichimoku_spanb_slope_negative_flag":           {"inputs": ["close", "high", "low"], "func": tbd_ext_027_ichimoku_spanb_slope_negative_flag},
    "tbd_ext_028_ichimoku_all_lines_bearish_flag":              {"inputs": ["close", "high", "low"], "func": tbd_ext_028_ichimoku_all_lines_bearish_flag},
    "tbd_ext_029_ichimoku_distance_below_cloud_zscore_252d":    {"inputs": ["close", "high", "low"], "func": tbd_ext_029_ichimoku_distance_below_cloud_zscore_252d},
    "tbd_ext_030_ichimoku_tenkan_kijun_bearish_cross_count_63d": {"inputs": ["close", "high", "low"], "func": tbd_ext_030_ichimoku_tenkan_kijun_bearish_cross_count_63d},
    "tbd_ext_031_vortex14_vi_minus_above_vi_plus_flag":         {"inputs": ["close", "high", "low"], "func": tbd_ext_031_vortex14_vi_minus_above_vi_plus_flag},
    "tbd_ext_032_vortex14_bearish_cross_event":                 {"inputs": ["close", "high", "low"], "func": tbd_ext_032_vortex14_bearish_cross_event},
    "tbd_ext_033_vortex14_days_since_bearish_cross":            {"inputs": ["close", "high", "low"], "func": tbd_ext_033_vortex14_days_since_bearish_cross},
    "tbd_ext_034_vortex14_vi_minus_minus_vi_plus":              {"inputs": ["close", "high", "low"], "func": tbd_ext_034_vortex14_vi_minus_minus_vi_plus},
    "tbd_ext_035_vortex21_vi_minus_above_vi_plus_flag":         {"inputs": ["close", "high", "low"], "func": tbd_ext_035_vortex21_vi_minus_above_vi_plus_flag},
    "tbd_ext_036_vortex14_bearish_cross_count_252d":            {"inputs": ["close", "high", "low"], "func": tbd_ext_036_vortex14_bearish_cross_count_252d},
    "tbd_ext_037_linreg_slope_21d_negative_flag":               {"inputs": ["close"],                "func": tbd_ext_037_linreg_slope_21d_negative_flag},
    "tbd_ext_038_linreg_slope_63d_negative_flag":               {"inputs": ["close"],                "func": tbd_ext_038_linreg_slope_63d_negative_flag},
    "tbd_ext_039_linreg_slope_21d_value":                       {"inputs": ["close"],                "func": tbd_ext_039_linreg_slope_21d_value},
    "tbd_ext_040_linreg_slope_63d_value":                       {"inputs": ["close"],                "func": tbd_ext_040_linreg_slope_63d_value},
    "tbd_ext_041_linreg_rsq_21d_value":                         {"inputs": ["close"],                "func": tbd_ext_041_linreg_rsq_21d_value},
    "tbd_ext_042_linreg_rsq_63d_value":                         {"inputs": ["close"],                "func": tbd_ext_042_linreg_rsq_63d_value},
    "tbd_ext_043_linreg_bearish_trend_strength_21d":            {"inputs": ["close"],                "func": tbd_ext_043_linreg_bearish_trend_strength_21d},
    "tbd_ext_044_linreg_slope_neg_streak_21d":                  {"inputs": ["close"],                "func": tbd_ext_044_linreg_slope_neg_streak_21d},
    "tbd_ext_045_chande_kroll_bearish_flag":                    {"inputs": ["close", "high", "low"], "func": tbd_ext_045_chande_kroll_bearish_flag},
    "tbd_ext_046_chande_kroll_flip_to_bearish_event":           {"inputs": ["close", "high", "low"], "func": tbd_ext_046_chande_kroll_flip_to_bearish_event},
    "tbd_ext_047_chande_kroll_bars_since_bearish_flip":         {"inputs": ["close", "high", "low"], "func": tbd_ext_047_chande_kroll_bars_since_bearish_flip},
    "tbd_ext_048_chande_kroll_distance_norm":                   {"inputs": ["close", "high", "low"], "func": tbd_ext_048_chande_kroll_distance_norm},
    "tbd_ext_049_chande_kroll_bearish_streak":                  {"inputs": ["close", "high", "low"], "func": tbd_ext_049_chande_kroll_bearish_streak},
    "tbd_ext_050_donchian_20_close_near_lower_band":            {"inputs": ["close", "high", "low"], "func": tbd_ext_050_donchian_20_close_near_lower_band},
    "tbd_ext_051_donchian_52_close_below_midpoint_flag":        {"inputs": ["close", "high", "low"], "func": tbd_ext_051_donchian_52_close_below_midpoint_flag},
    "tbd_ext_052_donchian_20_lower_band_slope_negative":        {"inputs": ["close", "high", "low"], "func": tbd_ext_052_donchian_20_lower_band_slope_negative},
    "tbd_ext_053_donchian_63_close_pct_rank":                   {"inputs": ["close", "high", "low"], "func": tbd_ext_053_donchian_63_close_pct_rank},
    "tbd_ext_054_donchian_breakout_lower_event":                {"inputs": ["close", "high", "low"], "func": tbd_ext_054_donchian_breakout_lower_event},
    "tbd_ext_055_adxr14_value":                                 {"inputs": ["close", "high", "low"], "func": tbd_ext_055_adxr14_value},
    "tbd_ext_056_adxr14_below_20_flag":                         {"inputs": ["close", "high", "low"], "func": tbd_ext_056_adxr14_below_20_flag},
    "tbd_ext_057_trend_intensity_index_21d":                    {"inputs": ["close"],                "func": tbd_ext_057_trend_intensity_index_21d},
    "tbd_ext_058_trend_intensity_index_below_50_flag":          {"inputs": ["close"],                "func": tbd_ext_058_trend_intensity_index_below_50_flag},
    "tbd_ext_059_adxr14_collapse_from_peak_63d":                {"inputs": ["close", "high", "low"], "func": tbd_ext_059_adxr14_collapse_from_peak_63d},
    "tbd_ext_060_mass_index_value":                             {"inputs": ["close", "high", "low"], "func": tbd_ext_060_mass_index_value},
    "tbd_ext_061_mass_index_above_27_flag":                     {"inputs": ["close", "high", "low"], "func": tbd_ext_061_mass_index_above_27_flag},
    "tbd_ext_062_mass_index_above_26_5_flag":                   {"inputs": ["close", "high", "low"], "func": tbd_ext_062_mass_index_above_26_5_flag},
    "tbd_ext_063_choppiness_index_14_value":                    {"inputs": ["close", "high", "low"], "func": tbd_ext_063_choppiness_index_14_value},
    "tbd_ext_064_choppiness_index_14_above_61_flag":            {"inputs": ["close", "high", "low"], "func": tbd_ext_064_choppiness_index_14_above_61_flag},
    "tbd_ext_065_choppiness_index_21_value":                    {"inputs": ["close", "high", "low"], "func": tbd_ext_065_choppiness_index_21_value},
    "tbd_ext_066_lh_only_count_21d":                            {"inputs": ["close", "high", "low"], "func": tbd_ext_066_lh_only_count_21d},
    "tbd_ext_067_ll_only_count_21d":                            {"inputs": ["close", "high", "low"], "func": tbd_ext_067_ll_only_count_21d},
    "tbd_ext_068_lh_ll_sequence_net_score_63d":                 {"inputs": ["close", "high", "low"], "func": tbd_ext_068_lh_ll_sequence_net_score_63d},
    "tbd_ext_069_consecutive_lh_ll_days_streak":                {"inputs": ["close", "high", "low"], "func": tbd_ext_069_consecutive_lh_ll_days_streak},
    "tbd_ext_070_vi_psar_st_bearish_score":                     {"inputs": ["close", "high", "low"], "func": tbd_ext_070_vi_psar_st_bearish_score},
    "tbd_ext_071_linreg_vi_adxr_confluence_score":              {"inputs": ["close", "high", "low"], "func": tbd_ext_071_linreg_vi_adxr_confluence_score},
    "tbd_ext_072_chande_kroll_donchian_breakdown_score":        {"inputs": ["close", "high", "low"], "func": tbd_ext_072_chande_kroll_donchian_breakdown_score},
    "tbd_ext_073_full_extended_breakdown_score":                {"inputs": ["close", "high", "low"], "func": tbd_ext_073_full_extended_breakdown_score},
    "tbd_ext_074_roc_21d_negative_flag":                        {"inputs": ["close"],                "func": tbd_ext_074_roc_21d_negative_flag},
    "tbd_ext_075_roc_63d_acceleration_negative_flag":           {"inputs": ["close"],                "func": tbd_ext_075_roc_63d_acceleration_negative_flag},
}
