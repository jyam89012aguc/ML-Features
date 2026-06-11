"""moving_average_ribbon_structure d1 features 076-150 - Pipeline 1b-technical.

150 distinct hypotheses across __base__001_075.py and __base__076_150.py.
Each feature encodes a *different concept*.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers - no cross-family imports.
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


# ---------------------------- MA helpers ----------------------------

def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float)
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _dema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _hma(s, n):
    half = max(int(n / 2), 2)
    sqrtn = max(int(np.sqrt(n)), 2)
    wma_half = _wma(s, half)
    wma_full = _wma(s, n)
    return _wma(2.0 * wma_half - wma_full, sqrtn)


def _kama(s, n=10, fast=2, slow=30):
    change = (s - s.shift(n)).abs()
    volatility = s.diff().abs().rolling(n, min_periods=max(n // 2, 2)).sum()
    er = change / volatility.replace(0, np.nan)
    fast_alpha = 2.0 / (fast + 1)
    slow_alpha = 2.0 / (slow + 1)
    sc = (er * (fast_alpha - slow_alpha) + slow_alpha) ** 2
    sc = sc.fillna(slow_alpha ** 2)
    arr = s.values
    sc_arr = sc.values
    out = np.full(len(arr), np.nan, dtype=float)
    prev = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            prev = float(v)
            initialized = True
            out[i] = prev
        else:
            prev = prev + sc_arr[i] * (float(v) - prev)
            out[i] = prev
    return pd.Series(out, index=s.index)


def _zlema(s, n):
    lag = max((n - 1) // 2, 1)
    de_lagged = 2.0 * s - s.shift(lag)
    return _ema(de_lagged, n)


def _smma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _mcginley(s, n):
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    md = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            md = float(v)
            initialized = True
            out[i] = md
        else:
            denom = n * (float(v) / md) ** 4 if md > 0 else float(n)
            if denom == 0:
                denom = float(n)
            md = md + (float(v) - md) / denom
            out[i] = md
    return pd.Series(out, index=s.index)


def _lsma(s, n):
    mp = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            return np.nan
        x_full = np.arange(len(w), dtype=float)
        if valid.all():
            x = x_full; y = w
        else:
            x = x_full[valid]; y = w[valid]
        xm = x.mean(); ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = ym - slope * xm
        return float(intercept + slope * (len(w) - 1))
    return s.rolling(n, min_periods=mp).apply(_f, raw=True)


def _alma(s, n, sigma=6.0, offset=0.85):
    m = offset * (n - 1)
    w = np.exp(-((np.arange(n) - m) ** 2) / (2 * (n / sigma) ** 2))
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _t3(s, n, v=0.7):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    e4 = _ema(e3, n)
    e5 = _ema(e4, n)
    e6 = _ema(e5, n)
    c1 = -v ** 3
    c2 = 3 * v ** 2 + 3 * v ** 3
    c3 = -6 * v ** 2 - 3 * v - 3 * v ** 3
    c4 = 1 + 3 * v + v ** 3 + 3 * v ** 2
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _frama(s, n=16):
    if n % 2 != 0:
        n = n + 1
    half = n // 2
    def _alpha_fn(w):
        valid = ~np.isnan(w)
        if valid.sum() < n:
            return np.nan
        a = w[:half]; b = w[half:]
        h1 = np.nanmax(a); l1 = np.nanmin(a)
        h2 = np.nanmax(b); l2 = np.nanmin(b)
        h3 = np.nanmax(w); l3 = np.nanmin(w)
        n1 = (h1 - l1) / half if half > 0 else 0.0
        n2 = (h2 - l2) / half if half > 0 else 0.0
        n3 = (h3 - l3) / n if n > 0 else 0.0
        if n1 + n2 <= 0 or n3 <= 0:
            return 0.01
        d = (np.log(n1 + n2) - np.log(n3)) / np.log(2.0)
        alpha = np.exp(-4.6 * (d - 1.0))
        return float(np.clip(alpha, 0.01, 1.0))
    alpha_s = s.rolling(n, min_periods=n).apply(_alpha_fn, raw=True)
    arr = s.values
    alpha_arr = alpha_s.fillna(2.0 / (n + 1)).values
    out = np.full(len(arr), np.nan, dtype=float)
    md = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            md = float(v)
            initialized = True
        else:
            md = alpha_arr[i] * float(v) + (1.0 - alpha_arr[i]) * md
        out[i] = md
    return pd.Series(out, index=s.index)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    """Length of current run of True. NaN-aware: NaN breaks the streak to NaN."""
    arr = b.astype("float").values
    out = np.full(len(arr), np.nan, dtype=float)
    run = 0
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            run = 0
            out[i] = np.nan
        elif v > 0.5:
            run += 1
            out[i] = float(run)
        else:
            run = 0
            out[i] = 0.0
    return pd.Series(out, index=b.index)


def _days_since_last_cross(a: pd.Series, b: pd.Series) -> pd.Series:
    """Bars since the sign of (a - b) last flipped."""
    sign = np.sign((a - b).fillna(0.0))
    flipped = (sign != sign.shift(1)) & (sign != 0)
    arr = flipped.values
    out = np.full(len(arr), np.nan, dtype=float)
    last_flip = -1
    for i in range(len(arr)):
        if arr[i]:
            last_flip = i
        if last_flip >= 0:
            out[i] = float(i - last_flip)
    return pd.Series(out, index=a.index)


def _count_crosses(a: pd.Series, b: pd.Series, window: int) -> pd.Series:
    """Rolling count of sign-changes in (a - b) over window bars."""
    sign = np.sign((a - b).fillna(0.0))
    flipped = ((sign != sign.shift(1)) & (sign != 0)).astype(float)
    return flipped.rolling(window, min_periods=max(window // 3, 2)).sum()


def f12_mrib_076_ribbon_slope_dispersion_21d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Cross-sectional std of per-MA log-slopes (21d) across the guppy_full ribbon - regime disagreement."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    disp = df.std(axis=1)
    return (disp).diff()

def f12_mrib_077_breadth_close_above_count_8sma_d1(close: pd.Series) -> pd.Series:
    """Count of 8sma ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_078_breadth_close_above_count_8ema_d1(close: pd.Series) -> pd.Series:
    """Count of 8ema ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_079_breadth_close_above_count_8hma_d1(close: pd.Series) -> pd.Series:
    """Count of 8hma ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_080_breadth_close_above_count_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Count of guppy_full ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_081_breadth_close_above_count_fib_sma_d1(close: pd.Series) -> pd.Series:
    """Count of fib_sma ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_082_breadth_close_above_count_fib_ema_d1(close: pd.Series) -> pd.Series:
    """Count of fib_ema ribbon MAs strictly below close - breadth of bullish regime (0..N)."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    breadth = above.where(valid, np.nan)
    return (breadth).diff()

def f12_mrib_083_fan_direction_sign_short_minus_long_8sma_d1(close: pd.Series) -> pd.Series:
    """Sign of (shortest-MA - longest-MA) of the 8sma ribbon - fan-up / fan-down indicator."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    fan = np.sign(_safe_log(first) - _safe_log(last))
    return (fan).diff()

def f12_mrib_084_fan_direction_sign_short_minus_long_8ema_d1(close: pd.Series) -> pd.Series:
    """Sign of (shortest-MA - longest-MA) of the 8ema ribbon - fan-up / fan-down indicator."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    fan = np.sign(_safe_log(first) - _safe_log(last))
    return (fan).diff()

def f12_mrib_085_fan_direction_sign_short_minus_long_8hma_d1(close: pd.Series) -> pd.Series:
    """Sign of (shortest-MA - longest-MA) of the 8hma ribbon - fan-up / fan-down indicator."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    fan = np.sign(_safe_log(first) - _safe_log(last))
    return (fan).diff()

def f12_mrib_086_fan_direction_sign_short_minus_long_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Sign of (shortest-MA - longest-MA) of the guppy_full ribbon - fan-up / fan-down indicator."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    first = mas[0]
    last = mas[-1]
    fan = np.sign(_safe_log(first) - _safe_log(last))
    return (fan).diff()

def f12_mrib_087_guppy_bundle_separation_log_short_minus_long_d1(close: pd.Series) -> pd.Series:
    """Log-ratio of mean(Guppy short EMAs) over mean(Guppy long EMAs) - bundle spread."""
    short_mas = [_ema(close, n) for n in [3, 5, 8, 10, 12, 15]]
    long_mas  = [_ema(close, n) for n in [30, 35, 40, 45, 50, 60]]
    ms = pd.concat([m.rename(i) for i, m in enumerate(short_mas)], axis=1).mean(axis=1)
    ml = pd.concat([m.rename(i) for i, m in enumerate(long_mas)],  axis=1).mean(axis=1)
    return (_safe_log(ms) - _safe_log(ml)).diff()

def f12_mrib_088_guppy_short_bundle_internal_width_norm_d1(close: pd.Series) -> pd.Series:
    """(max-min) within Guppy short-bundle EMAs / close - internal compression of fast group."""
    mas = [_ema(close, n) for n in [3, 5, 8, 10, 12, 15]]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return ((df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)).diff()

def f12_mrib_089_guppy_long_bundle_internal_width_norm_d1(close: pd.Series) -> pd.Series:
    """(max-min) within Guppy long-bundle EMAs / close - internal compression of slow group."""
    mas = [_ema(close, n) for n in [30, 35, 40, 45, 50, 60]]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return ((df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)).diff()

def f12_mrib_090_guppy_bundle_distance_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """252d z-score of Guppy bundle log-separation - anomalous fast/slow gap."""
    short_mas = [_ema(close, n) for n in [3, 5, 8, 10, 12, 15]]
    long_mas  = [_ema(close, n) for n in [30, 35, 40, 45, 50, 60]]
    ms = pd.concat([m.rename(i) for i, m in enumerate(short_mas)], axis=1).mean(axis=1)
    ml = pd.concat([m.rename(i) for i, m in enumerate(long_mas)],  axis=1).mean(axis=1)
    sep = _safe_log(ms) - _safe_log(ml)
    return (_rolling_zscore(sep, YDAYS, min_periods=QDAYS)).diff()

def f12_mrib_091_ribbon_compression_event_below_p10_252d_8sma_d1(close: pd.Series) -> pd.Series:
    """Indicator: 8sma ribbon width <= 252d 10th-percentile - squeeze event."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    p10 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    ev = (width <= p10).astype(float).where(p10.notna(), np.nan)
    return (ev).diff()

def f12_mrib_092_ribbon_compression_event_below_p10_252d_8ema_d1(close: pd.Series) -> pd.Series:
    """Indicator: 8ema ribbon width <= 252d 10th-percentile - squeeze event."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    p10 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    ev = (width <= p10).astype(float).where(p10.notna(), np.nan)
    return (ev).diff()

def f12_mrib_093_ribbon_compression_event_below_p10_252d_8hma_d1(close: pd.Series) -> pd.Series:
    """Indicator: 8hma ribbon width <= 252d 10th-percentile - squeeze event."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    p10 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    ev = (width <= p10).astype(float).where(p10.notna(), np.nan)
    return (ev).diff()

def f12_mrib_094_ribbon_compression_event_below_p10_252d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Indicator: guppy_full ribbon width <= 252d 10th-percentile - squeeze event."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    p10 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    ev = (width <= p10).astype(float).where(p10.notna(), np.nan)
    return (ev).diff()

def f12_mrib_095_days_since_last_bull_stack_break_8sma_d1(close: pd.Series) -> pd.Series:
    """Bars since the last loss of full bullish-stack ordering in the 8sma ribbon - regime age."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    arr = bull.values
    out = np.full(len(arr), np.nan, dtype=float)
    last_break = -1
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            if last_break >= 0:
                out[i] = float(i - last_break)
            continue
        if v < 0.5:
            last_break = i
            out[i] = 0.0
        else:
            if last_break >= 0:
                out[i] = float(i - last_break)
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_096_days_since_last_bull_stack_break_8ema_d1(close: pd.Series) -> pd.Series:
    """Bars since the last loss of full bullish-stack ordering in the 8ema ribbon - regime age."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    arr = bull.values
    out = np.full(len(arr), np.nan, dtype=float)
    last_break = -1
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            if last_break >= 0:
                out[i] = float(i - last_break)
            continue
        if v < 0.5:
            last_break = i
            out[i] = 0.0
        else:
            if last_break >= 0:
                out[i] = float(i - last_break)
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_097_days_since_last_bull_stack_break_8hma_d1(close: pd.Series) -> pd.Series:
    """Bars since the last loss of full bullish-stack ordering in the 8hma ribbon - regime age."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    arr = bull.values
    out = np.full(len(arr), np.nan, dtype=float)
    last_break = -1
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            if last_break >= 0:
                out[i] = float(i - last_break)
            continue
        if v < 0.5:
            last_break = i
            out[i] = 0.0
        else:
            if last_break >= 0:
                out[i] = float(i - last_break)
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_098_days_since_last_bull_stack_break_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Bars since the last loss of full bullish-stack ordering in the guppy_full ribbon - regime age."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    arr = bull.values
    out = np.full(len(arr), np.nan, dtype=float)
    last_break = -1
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            if last_break >= 0:
                out[i] = float(i - last_break)
            continue
        if v < 0.5:
            last_break = i
            out[i] = 0.0
        else:
            if last_break >= 0:
                out[i] = float(i - last_break)
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_099_ribbon_fan_flips_63d_8sma_d1(close: pd.Series) -> pd.Series:
    """63d count of fan-direction flips in the 8sma ribbon (first-MA vs last-MA crossings)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    return (_count_crosses(first, last, QDAYS)).diff()

def f12_mrib_100_ribbon_fan_flips_63d_8ema_d1(close: pd.Series) -> pd.Series:
    """63d count of fan-direction flips in the 8ema ribbon (first-MA vs last-MA crossings)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    return (_count_crosses(first, last, QDAYS)).diff()

def f12_mrib_101_ribbon_fan_flips_63d_8hma_d1(close: pd.Series) -> pd.Series:
    """63d count of fan-direction flips in the 8hma ribbon (first-MA vs last-MA crossings)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    return (_count_crosses(first, last, QDAYS)).diff()

def f12_mrib_102_ribbon_fan_flips_63d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """63d count of fan-direction flips in the guppy_full ribbon (first-MA vs last-MA crossings)."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    first = mas[0]
    last = mas[-1]
    return (_count_crosses(first, last, QDAYS)).diff()

def f12_mrib_103_log_dist_close_above_median_ribbon_8sma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional median of 8sma ribbon - consensus extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    med = df.median(axis=1)
    return (_safe_log(close) - _safe_log(med)).diff()

def f12_mrib_104_log_dist_close_above_median_ribbon_8ema_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional median of 8ema ribbon - consensus extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    med = df.median(axis=1)
    return (_safe_log(close) - _safe_log(med)).diff()

def f12_mrib_105_log_dist_close_above_median_ribbon_8hma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional median of 8hma ribbon - consensus extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    med = df.median(axis=1)
    return (_safe_log(close) - _safe_log(med)).diff()

def f12_mrib_106_log_dist_close_above_median_ribbon_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional median of guppy_full ribbon - consensus extension."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    med = df.median(axis=1)
    return (_safe_log(close) - _safe_log(med)).diff()

def f12_mrib_107_ribbon_cross_sectional_skew_8sma_d1(close: pd.Series) -> pd.Series:
    """Skewness across MA values in the 8sma ribbon - asymmetric distribution of trend horizons."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return (df.skew(axis=1)).diff()

def f12_mrib_108_ribbon_cross_sectional_skew_8ema_d1(close: pd.Series) -> pd.Series:
    """Skewness across MA values in the 8ema ribbon - asymmetric distribution of trend horizons."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return (df.skew(axis=1)).diff()

def f12_mrib_109_ribbon_cross_sectional_skew_8hma_d1(close: pd.Series) -> pd.Series:
    """Skewness across MA values in the 8hma ribbon - asymmetric distribution of trend horizons."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return (df.skew(axis=1)).diff()

def f12_mrib_110_ribbon_cross_sectional_skew_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Skewness across MA values in the guppy_full ribbon - asymmetric distribution of trend horizons."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    return (df.skew(axis=1)).diff()

def f12_mrib_111_ribbon_convergence_speed_21d_8sma_d1(close: pd.Series) -> pd.Series:
    """Negative 21d slope of normalized 8sma ribbon width - speed of compression."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    conv = -_rolling_slope(width, MDAYS)
    return (conv).diff()

def f12_mrib_112_ribbon_convergence_speed_21d_8ema_d1(close: pd.Series) -> pd.Series:
    """Negative 21d slope of normalized 8ema ribbon width - speed of compression."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    conv = -_rolling_slope(width, MDAYS)
    return (conv).diff()

def f12_mrib_113_ribbon_convergence_speed_21d_8hma_d1(close: pd.Series) -> pd.Series:
    """Negative 21d slope of normalized 8hma ribbon width - speed of compression."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    conv = -_rolling_slope(width, MDAYS)
    return (conv).diff()

def f12_mrib_114_ribbon_convergence_speed_21d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Negative 21d slope of normalized guppy_full ribbon width - speed of compression."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    conv = -_rolling_slope(width, MDAYS)
    return (conv).diff()

def f12_mrib_115_close_short_minus_long_ribbon_spread_8sma_d1(close: pd.Series) -> pd.Series:
    """(log close - log shortest MA) minus (log close - log longest MA) of the 8sma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    spread_short = _safe_log(close) - _safe_log(first)
    spread_long  = _safe_log(close) - _safe_log(last)
    return (spread_short - spread_long).diff()

def f12_mrib_116_close_short_minus_long_ribbon_spread_8ema_d1(close: pd.Series) -> pd.Series:
    """(log close - log shortest MA) minus (log close - log longest MA) of the 8ema ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    spread_short = _safe_log(close) - _safe_log(first)
    spread_long  = _safe_log(close) - _safe_log(last)
    return (spread_short - spread_long).diff()

def f12_mrib_117_close_short_minus_long_ribbon_spread_8hma_d1(close: pd.Series) -> pd.Series:
    """(log close - log shortest MA) minus (log close - log longest MA) of the 8hma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    first = mas[0]
    last = mas[-1]
    spread_short = _safe_log(close) - _safe_log(first)
    spread_long  = _safe_log(close) - _safe_log(last)
    return (spread_short - spread_long).diff()

def f12_mrib_118_close_short_minus_long_ribbon_spread_guppy_full_d1(close: pd.Series) -> pd.Series:
    """(log close - log shortest MA) minus (log close - log longest MA) of the guppy_full ribbon."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    first = mas[0]
    last = mas[-1]
    spread_short = _safe_log(close) - _safe_log(first)
    spread_long  = _safe_log(close) - _safe_log(last)
    return (spread_short - spread_long).diff()

def f12_mrib_119_bull_minus_bear_stack_frac_63d_8sma_d1(close: pd.Series) -> pd.Series:
    """Fraction-bullish-stack minus fraction-bearish-stack over 63d in the 8sma ribbon - net regime sign."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    bear = (diffs.gt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    delta = bull.rolling(QDAYS, min_periods=MDAYS).mean() - bear.rolling(QDAYS, min_periods=MDAYS).mean()
    return (delta).diff()

def f12_mrib_120_bull_minus_bear_stack_frac_63d_8ema_d1(close: pd.Series) -> pd.Series:
    """Fraction-bullish-stack minus fraction-bearish-stack over 63d in the 8ema ribbon - net regime sign."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    bear = (diffs.gt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    delta = bull.rolling(QDAYS, min_periods=MDAYS).mean() - bear.rolling(QDAYS, min_periods=MDAYS).mean()
    return (delta).diff()

def f12_mrib_121_bull_minus_bear_stack_frac_63d_8hma_d1(close: pd.Series) -> pd.Series:
    """Fraction-bullish-stack minus fraction-bearish-stack over 63d in the 8hma ribbon - net regime sign."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    bear = (diffs.gt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    delta = bull.rolling(QDAYS, min_periods=MDAYS).mean() - bear.rolling(QDAYS, min_periods=MDAYS).mean()
    return (delta).diff()

def f12_mrib_122_bull_minus_bear_stack_frac_63d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Fraction-bullish-stack minus fraction-bearish-stack over 63d in the guppy_full ribbon - net regime sign."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    bear = (diffs.gt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    delta = bull.rolling(QDAYS, min_periods=MDAYS).mean() - bear.rolling(QDAYS, min_periods=MDAYS).mean()
    return (delta).diff()

def f12_mrib_123_breadth_slope_21d_8sma_d1(close: pd.Series) -> pd.Series:
    """21d slope of close-above-MA breadth count in the 8sma ribbon - regime-change rate."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (_rolling_slope(above, MDAYS)).diff()

def f12_mrib_124_breadth_slope_21d_8ema_d1(close: pd.Series) -> pd.Series:
    """21d slope of close-above-MA breadth count in the 8ema ribbon - regime-change rate."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (_rolling_slope(above, MDAYS)).diff()

def f12_mrib_125_breadth_slope_21d_8hma_d1(close: pd.Series) -> pd.Series:
    """21d slope of close-above-MA breadth count in the 8hma ribbon - regime-change rate."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (_rolling_slope(above, MDAYS)).diff()

def f12_mrib_126_breadth_slope_21d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """21d slope of close-above-MA breadth count in the guppy_full ribbon - regime-change rate."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    above = df.lt(close, axis=0).sum(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (_rolling_slope(above, MDAYS)).diff()

def f12_mrib_127_current_bull_stack_streak_bars_8sma_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-bar run with full bullish-stack ordering in 8sma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).where(df.notna().all(axis=1), np.nan)
    streak = _consecutive_true_streak(bull.fillna(False))
    streak = streak.where(bull.notna(), np.nan)
    return (streak).diff()

def f12_mrib_128_current_bull_stack_streak_bars_8ema_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-bar run with full bullish-stack ordering in 8ema ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).where(df.notna().all(axis=1), np.nan)
    streak = _consecutive_true_streak(bull.fillna(False))
    streak = streak.where(bull.notna(), np.nan)
    return (streak).diff()

def f12_mrib_129_current_bull_stack_streak_bars_8hma_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-bar run with full bullish-stack ordering in 8hma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).where(df.notna().all(axis=1), np.nan)
    streak = _consecutive_true_streak(bull.fillna(False))
    streak = streak.where(bull.notna(), np.nan)
    return (streak).diff()

def f12_mrib_130_current_bull_stack_streak_bars_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-bar run with full bullish-stack ordering in guppy_full ribbon."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).where(df.notna().all(axis=1), np.nan)
    streak = _consecutive_true_streak(bull.fillna(False))
    streak = streak.where(bull.notna(), np.nan)
    return (streak).diff()

def f12_mrib_131_log_dist_close_to_ribbon_min_8sma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MIN of the 8sma ribbon - floor extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_min = df.min(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_min)).diff()

def f12_mrib_132_log_dist_close_to_ribbon_min_8ema_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MIN of the 8ema ribbon - floor extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_min = df.min(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_min)).diff()

def f12_mrib_133_log_dist_close_to_ribbon_min_8hma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MIN of the 8hma ribbon - floor extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_min = df.min(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_min)).diff()

def f12_mrib_134_log_dist_close_to_ribbon_min_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MIN of the guppy_full ribbon - floor extension."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_min = df.min(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_min)).diff()

def f12_mrib_135_log_dist_close_to_ribbon_max_8sma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MAX of the 8sma ribbon - ceiling extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_max = df.max(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_max)).diff()

def f12_mrib_136_log_dist_close_to_ribbon_max_8ema_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MAX of the 8ema ribbon - ceiling extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_max = df.max(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_max)).diff()

def f12_mrib_137_log_dist_close_to_ribbon_max_8hma_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MAX of the 8hma ribbon - ceiling extension."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_max = df.max(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_max)).diff()

def f12_mrib_138_log_dist_close_to_ribbon_max_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Log distance of close above the cross-sectional MAX of the guppy_full ribbon - ceiling extension."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    ribbon_max = df.max(axis=1)
    return (_safe_log(close) - _safe_log(ribbon_max)).diff()

def f12_mrib_139_ribbon_tilt_slope_vs_length_8sma_d1(close: pd.Series) -> pd.Series:
    """Per-bar slope of MA-value vs MA-length across the 8sma ribbon, normalized by close - bearish-tilt strength."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    x = np.array(lens, dtype=float)
    xm = x.mean(); ssx = ((x - xm) ** 2).sum()
    def _tlt(row):
        if np.isnan(row).any():
            return np.nan
        ym = row.mean()
        return float(((x - xm) * (row - ym)).sum() / ssx) if ssx > 0 else np.nan
    vals = df.values
    out = np.array([_tlt(vals[i]) for i in range(len(vals))], dtype=float)
    tilt = pd.Series(out, index=close.index) / close.replace(0, np.nan)
    return (tilt).diff()

def f12_mrib_140_ribbon_tilt_slope_vs_length_8ema_d1(close: pd.Series) -> pd.Series:
    """Per-bar slope of MA-value vs MA-length across the 8ema ribbon, normalized by close - bearish-tilt strength."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    x = np.array(lens, dtype=float)
    xm = x.mean(); ssx = ((x - xm) ** 2).sum()
    def _tlt(row):
        if np.isnan(row).any():
            return np.nan
        ym = row.mean()
        return float(((x - xm) * (row - ym)).sum() / ssx) if ssx > 0 else np.nan
    vals = df.values
    out = np.array([_tlt(vals[i]) for i in range(len(vals))], dtype=float)
    tilt = pd.Series(out, index=close.index) / close.replace(0, np.nan)
    return (tilt).diff()

def f12_mrib_141_ribbon_tilt_slope_vs_length_8hma_d1(close: pd.Series) -> pd.Series:
    """Per-bar slope of MA-value vs MA-length across the 8hma ribbon, normalized by close - bearish-tilt strength."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    x = np.array(lens, dtype=float)
    xm = x.mean(); ssx = ((x - xm) ** 2).sum()
    def _tlt(row):
        if np.isnan(row).any():
            return np.nan
        ym = row.mean()
        return float(((x - xm) * (row - ym)).sum() / ssx) if ssx > 0 else np.nan
    vals = df.values
    out = np.array([_tlt(vals[i]) for i in range(len(vals))], dtype=float)
    tilt = pd.Series(out, index=close.index) / close.replace(0, np.nan)
    return (tilt).diff()

def f12_mrib_142_ribbon_tilt_slope_vs_length_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Per-bar slope of MA-value vs MA-length across the guppy_full ribbon, normalized by close - bearish-tilt strength."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    x = np.array(lens, dtype=float)
    xm = x.mean(); ssx = ((x - xm) ** 2).sum()
    def _tlt(row):
        if np.isnan(row).any():
            return np.nan
        ym = row.mean()
        return float(((x - xm) * (row - ym)).sum() / ssx) if ssx > 0 else np.nan
    vals = df.values
    out = np.array([_tlt(vals[i]) for i in range(len(vals))], dtype=float)
    tilt = pd.Series(out, index=close.index) / close.replace(0, np.nan)
    return (tilt).diff()

def f12_mrib_143_distinct_ribbon_orderings_count_63d_8sma_d1(close: pd.Series) -> pd.Series:
    """Count of distinct ribbon-orderings observed in the last 63d for the 8sma ribbon - regime variety."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    vals = df.values
    n = len(vals)
    ordhash = np.full(n, -1, dtype=np.int64)
    for i in range(n):
        row = vals[i]
        if not np.isnan(row).any():
            ranks = pd.Series(row).rank(method='first').astype(int).values
            h = 0
            for r in ranks:
                h = (h * 131 + int(r)) % 9223372036854775783
            ordhash[i] = h
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        win = ordhash[lo:i + 1]
        win = win[win != -1]
        if win.size >= MDAYS:
            out[i] = float(len(set(win.tolist())))
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_144_distinct_ribbon_orderings_count_63d_8ema_d1(close: pd.Series) -> pd.Series:
    """Count of distinct ribbon-orderings observed in the last 63d for the 8ema ribbon - regime variety."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    vals = df.values
    n = len(vals)
    ordhash = np.full(n, -1, dtype=np.int64)
    for i in range(n):
        row = vals[i]
        if not np.isnan(row).any():
            ranks = pd.Series(row).rank(method='first').astype(int).values
            h = 0
            for r in ranks:
                h = (h * 131 + int(r)) % 9223372036854775783
            ordhash[i] = h
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        win = ordhash[lo:i + 1]
        win = win[win != -1]
        if win.size >= MDAYS:
            out[i] = float(len(set(win.tolist())))
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_145_distinct_ribbon_orderings_count_63d_8hma_d1(close: pd.Series) -> pd.Series:
    """Count of distinct ribbon-orderings observed in the last 63d for the 8hma ribbon - regime variety."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    vals = df.values
    n = len(vals)
    ordhash = np.full(n, -1, dtype=np.int64)
    for i in range(n):
        row = vals[i]
        if not np.isnan(row).any():
            ranks = pd.Series(row).rank(method='first').astype(int).values
            h = 0
            for r in ranks:
                h = (h * 131 + int(r)) % 9223372036854775783
            ordhash[i] = h
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        win = ordhash[lo:i + 1]
        win = win[win != -1]
        if win.size >= MDAYS:
            out[i] = float(len(set(win.tolist())))
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_146_distinct_ribbon_orderings_count_63d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Count of distinct ribbon-orderings observed in the last 63d for the guppy_full ribbon - regime variety."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    vals = df.values
    n = len(vals)
    ordhash = np.full(n, -1, dtype=np.int64)
    for i in range(n):
        row = vals[i]
        if not np.isnan(row).any():
            ranks = pd.Series(row).rank(method='first').astype(int).values
            h = 0
            for r in ranks:
                h = (h * 131 + int(r)) % 9223372036854775783
            ordhash[i] = h
    out = np.full(n, np.nan, dtype=float)
    for i in range(n):
        lo = max(0, i - QDAYS + 1)
        win = ordhash[lo:i + 1]
        win = win[win != -1]
        if win.size >= MDAYS:
            out[i] = float(len(set(win.tolist())))
    res = pd.Series(out, index=close.index)
    return (res).diff()

def f12_mrib_147_frac_bars_bullish_stack_252d_8sma_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 252d in bullish stack for the 8sma ribbon - regime persistence."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (bull.rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f12_mrib_148_frac_bars_bullish_stack_252d_guppy_full_d1(close: pd.Series) -> pd.Series:
    """Fraction of last 252d in bullish stack for the Guppy full ribbon."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float).where(df.notna().all(axis=1), np.nan)
    return (bull.rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f12_mrib_149_ribbon_width_pctrank_252d_8ema_d1(close: pd.Series) -> pd.Series:
    """252d percentile-rank of 8ema ribbon width - relative compression/expansion regime."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    res = width.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (res).diff()

def f12_mrib_150_ribbon_close_position_in_minmax_range_8ema_d1(close: pd.Series) -> pd.Series:
    """Normalized position of close within (min-MA, max-MA) of the 8ema ribbon - rank inside band."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    lo = df.min(axis=1); hi = df.max(axis=1)
    return (_safe_div(close - lo, hi - lo)).diff()


# ============================================================
#                         REGISTRY 076_150 (d1)
# ============================================================

MOVING_AVERAGE_RIBBON_STRUCTURE_D1_REGISTRY_076_150 = {
    "f12_mrib_076_ribbon_slope_dispersion_21d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_076_ribbon_slope_dispersion_21d_guppy_full_d1},
    "f12_mrib_077_breadth_close_above_count_8sma_d1": {"inputs": ["close"], "func": f12_mrib_077_breadth_close_above_count_8sma_d1},
    "f12_mrib_078_breadth_close_above_count_8ema_d1": {"inputs": ["close"], "func": f12_mrib_078_breadth_close_above_count_8ema_d1},
    "f12_mrib_079_breadth_close_above_count_8hma_d1": {"inputs": ["close"], "func": f12_mrib_079_breadth_close_above_count_8hma_d1},
    "f12_mrib_080_breadth_close_above_count_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_080_breadth_close_above_count_guppy_full_d1},
    "f12_mrib_081_breadth_close_above_count_fib_sma_d1": {"inputs": ["close"], "func": f12_mrib_081_breadth_close_above_count_fib_sma_d1},
    "f12_mrib_082_breadth_close_above_count_fib_ema_d1": {"inputs": ["close"], "func": f12_mrib_082_breadth_close_above_count_fib_ema_d1},
    "f12_mrib_083_fan_direction_sign_short_minus_long_8sma_d1": {"inputs": ["close"], "func": f12_mrib_083_fan_direction_sign_short_minus_long_8sma_d1},
    "f12_mrib_084_fan_direction_sign_short_minus_long_8ema_d1": {"inputs": ["close"], "func": f12_mrib_084_fan_direction_sign_short_minus_long_8ema_d1},
    "f12_mrib_085_fan_direction_sign_short_minus_long_8hma_d1": {"inputs": ["close"], "func": f12_mrib_085_fan_direction_sign_short_minus_long_8hma_d1},
    "f12_mrib_086_fan_direction_sign_short_minus_long_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_086_fan_direction_sign_short_minus_long_guppy_full_d1},
    "f12_mrib_087_guppy_bundle_separation_log_short_minus_long_d1": {"inputs": ["close"], "func": f12_mrib_087_guppy_bundle_separation_log_short_minus_long_d1},
    "f12_mrib_088_guppy_short_bundle_internal_width_norm_d1": {"inputs": ["close"], "func": f12_mrib_088_guppy_short_bundle_internal_width_norm_d1},
    "f12_mrib_089_guppy_long_bundle_internal_width_norm_d1": {"inputs": ["close"], "func": f12_mrib_089_guppy_long_bundle_internal_width_norm_d1},
    "f12_mrib_090_guppy_bundle_distance_zscore_252d_d1": {"inputs": ["close"], "func": f12_mrib_090_guppy_bundle_distance_zscore_252d_d1},
    "f12_mrib_091_ribbon_compression_event_below_p10_252d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_091_ribbon_compression_event_below_p10_252d_8sma_d1},
    "f12_mrib_092_ribbon_compression_event_below_p10_252d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_092_ribbon_compression_event_below_p10_252d_8ema_d1},
    "f12_mrib_093_ribbon_compression_event_below_p10_252d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_093_ribbon_compression_event_below_p10_252d_8hma_d1},
    "f12_mrib_094_ribbon_compression_event_below_p10_252d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_094_ribbon_compression_event_below_p10_252d_guppy_full_d1},
    "f12_mrib_095_days_since_last_bull_stack_break_8sma_d1": {"inputs": ["close"], "func": f12_mrib_095_days_since_last_bull_stack_break_8sma_d1},
    "f12_mrib_096_days_since_last_bull_stack_break_8ema_d1": {"inputs": ["close"], "func": f12_mrib_096_days_since_last_bull_stack_break_8ema_d1},
    "f12_mrib_097_days_since_last_bull_stack_break_8hma_d1": {"inputs": ["close"], "func": f12_mrib_097_days_since_last_bull_stack_break_8hma_d1},
    "f12_mrib_098_days_since_last_bull_stack_break_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_098_days_since_last_bull_stack_break_guppy_full_d1},
    "f12_mrib_099_ribbon_fan_flips_63d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_099_ribbon_fan_flips_63d_8sma_d1},
    "f12_mrib_100_ribbon_fan_flips_63d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_100_ribbon_fan_flips_63d_8ema_d1},
    "f12_mrib_101_ribbon_fan_flips_63d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_101_ribbon_fan_flips_63d_8hma_d1},
    "f12_mrib_102_ribbon_fan_flips_63d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_102_ribbon_fan_flips_63d_guppy_full_d1},
    "f12_mrib_103_log_dist_close_above_median_ribbon_8sma_d1": {"inputs": ["close"], "func": f12_mrib_103_log_dist_close_above_median_ribbon_8sma_d1},
    "f12_mrib_104_log_dist_close_above_median_ribbon_8ema_d1": {"inputs": ["close"], "func": f12_mrib_104_log_dist_close_above_median_ribbon_8ema_d1},
    "f12_mrib_105_log_dist_close_above_median_ribbon_8hma_d1": {"inputs": ["close"], "func": f12_mrib_105_log_dist_close_above_median_ribbon_8hma_d1},
    "f12_mrib_106_log_dist_close_above_median_ribbon_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_106_log_dist_close_above_median_ribbon_guppy_full_d1},
    "f12_mrib_107_ribbon_cross_sectional_skew_8sma_d1": {"inputs": ["close"], "func": f12_mrib_107_ribbon_cross_sectional_skew_8sma_d1},
    "f12_mrib_108_ribbon_cross_sectional_skew_8ema_d1": {"inputs": ["close"], "func": f12_mrib_108_ribbon_cross_sectional_skew_8ema_d1},
    "f12_mrib_109_ribbon_cross_sectional_skew_8hma_d1": {"inputs": ["close"], "func": f12_mrib_109_ribbon_cross_sectional_skew_8hma_d1},
    "f12_mrib_110_ribbon_cross_sectional_skew_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_110_ribbon_cross_sectional_skew_guppy_full_d1},
    "f12_mrib_111_ribbon_convergence_speed_21d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_111_ribbon_convergence_speed_21d_8sma_d1},
    "f12_mrib_112_ribbon_convergence_speed_21d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_112_ribbon_convergence_speed_21d_8ema_d1},
    "f12_mrib_113_ribbon_convergence_speed_21d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_113_ribbon_convergence_speed_21d_8hma_d1},
    "f12_mrib_114_ribbon_convergence_speed_21d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_114_ribbon_convergence_speed_21d_guppy_full_d1},
    "f12_mrib_115_close_short_minus_long_ribbon_spread_8sma_d1": {"inputs": ["close"], "func": f12_mrib_115_close_short_minus_long_ribbon_spread_8sma_d1},
    "f12_mrib_116_close_short_minus_long_ribbon_spread_8ema_d1": {"inputs": ["close"], "func": f12_mrib_116_close_short_minus_long_ribbon_spread_8ema_d1},
    "f12_mrib_117_close_short_minus_long_ribbon_spread_8hma_d1": {"inputs": ["close"], "func": f12_mrib_117_close_short_minus_long_ribbon_spread_8hma_d1},
    "f12_mrib_118_close_short_minus_long_ribbon_spread_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_118_close_short_minus_long_ribbon_spread_guppy_full_d1},
    "f12_mrib_119_bull_minus_bear_stack_frac_63d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_119_bull_minus_bear_stack_frac_63d_8sma_d1},
    "f12_mrib_120_bull_minus_bear_stack_frac_63d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_120_bull_minus_bear_stack_frac_63d_8ema_d1},
    "f12_mrib_121_bull_minus_bear_stack_frac_63d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_121_bull_minus_bear_stack_frac_63d_8hma_d1},
    "f12_mrib_122_bull_minus_bear_stack_frac_63d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_122_bull_minus_bear_stack_frac_63d_guppy_full_d1},
    "f12_mrib_123_breadth_slope_21d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_123_breadth_slope_21d_8sma_d1},
    "f12_mrib_124_breadth_slope_21d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_124_breadth_slope_21d_8ema_d1},
    "f12_mrib_125_breadth_slope_21d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_125_breadth_slope_21d_8hma_d1},
    "f12_mrib_126_breadth_slope_21d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_126_breadth_slope_21d_guppy_full_d1},
    "f12_mrib_127_current_bull_stack_streak_bars_8sma_d1": {"inputs": ["close"], "func": f12_mrib_127_current_bull_stack_streak_bars_8sma_d1},
    "f12_mrib_128_current_bull_stack_streak_bars_8ema_d1": {"inputs": ["close"], "func": f12_mrib_128_current_bull_stack_streak_bars_8ema_d1},
    "f12_mrib_129_current_bull_stack_streak_bars_8hma_d1": {"inputs": ["close"], "func": f12_mrib_129_current_bull_stack_streak_bars_8hma_d1},
    "f12_mrib_130_current_bull_stack_streak_bars_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_130_current_bull_stack_streak_bars_guppy_full_d1},
    "f12_mrib_131_log_dist_close_to_ribbon_min_8sma_d1": {"inputs": ["close"], "func": f12_mrib_131_log_dist_close_to_ribbon_min_8sma_d1},
    "f12_mrib_132_log_dist_close_to_ribbon_min_8ema_d1": {"inputs": ["close"], "func": f12_mrib_132_log_dist_close_to_ribbon_min_8ema_d1},
    "f12_mrib_133_log_dist_close_to_ribbon_min_8hma_d1": {"inputs": ["close"], "func": f12_mrib_133_log_dist_close_to_ribbon_min_8hma_d1},
    "f12_mrib_134_log_dist_close_to_ribbon_min_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_134_log_dist_close_to_ribbon_min_guppy_full_d1},
    "f12_mrib_135_log_dist_close_to_ribbon_max_8sma_d1": {"inputs": ["close"], "func": f12_mrib_135_log_dist_close_to_ribbon_max_8sma_d1},
    "f12_mrib_136_log_dist_close_to_ribbon_max_8ema_d1": {"inputs": ["close"], "func": f12_mrib_136_log_dist_close_to_ribbon_max_8ema_d1},
    "f12_mrib_137_log_dist_close_to_ribbon_max_8hma_d1": {"inputs": ["close"], "func": f12_mrib_137_log_dist_close_to_ribbon_max_8hma_d1},
    "f12_mrib_138_log_dist_close_to_ribbon_max_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_138_log_dist_close_to_ribbon_max_guppy_full_d1},
    "f12_mrib_139_ribbon_tilt_slope_vs_length_8sma_d1": {"inputs": ["close"], "func": f12_mrib_139_ribbon_tilt_slope_vs_length_8sma_d1},
    "f12_mrib_140_ribbon_tilt_slope_vs_length_8ema_d1": {"inputs": ["close"], "func": f12_mrib_140_ribbon_tilt_slope_vs_length_8ema_d1},
    "f12_mrib_141_ribbon_tilt_slope_vs_length_8hma_d1": {"inputs": ["close"], "func": f12_mrib_141_ribbon_tilt_slope_vs_length_8hma_d1},
    "f12_mrib_142_ribbon_tilt_slope_vs_length_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_142_ribbon_tilt_slope_vs_length_guppy_full_d1},
    "f12_mrib_143_distinct_ribbon_orderings_count_63d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_143_distinct_ribbon_orderings_count_63d_8sma_d1},
    "f12_mrib_144_distinct_ribbon_orderings_count_63d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_144_distinct_ribbon_orderings_count_63d_8ema_d1},
    "f12_mrib_145_distinct_ribbon_orderings_count_63d_8hma_d1": {"inputs": ["close"], "func": f12_mrib_145_distinct_ribbon_orderings_count_63d_8hma_d1},
    "f12_mrib_146_distinct_ribbon_orderings_count_63d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_146_distinct_ribbon_orderings_count_63d_guppy_full_d1},
    "f12_mrib_147_frac_bars_bullish_stack_252d_8sma_d1": {"inputs": ["close"], "func": f12_mrib_147_frac_bars_bullish_stack_252d_8sma_d1},
    "f12_mrib_148_frac_bars_bullish_stack_252d_guppy_full_d1": {"inputs": ["close"], "func": f12_mrib_148_frac_bars_bullish_stack_252d_guppy_full_d1},
    "f12_mrib_149_ribbon_width_pctrank_252d_8ema_d1": {"inputs": ["close"], "func": f12_mrib_149_ribbon_width_pctrank_252d_8ema_d1},
    "f12_mrib_150_ribbon_close_position_in_minmax_range_8ema_d1": {"inputs": ["close"], "func": f12_mrib_150_ribbon_close_position_in_minmax_range_8ema_d1},
}
