"""moving_average_ribbon_structure d3 features 001-075 - Pipeline 1b-technical.

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


def f12_mrib_001_bullish_stack_indicator_8sma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8sma ribbon is below the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_002_bullish_stack_indicator_8ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8ema ribbon is below the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_003_bullish_stack_indicator_8hma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8hma ribbon is below the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_004_bullish_stack_indicator_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_short_ema ribbon is below the shorter one."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_005_bullish_stack_indicator_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_long_ema ribbon is below the shorter one."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_006_bullish_stack_indicator_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_full_ema ribbon is below the shorter one."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_007_bullish_stack_indicator_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the fib_sma ribbon is below the shorter one."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_008_bullish_stack_indicator_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the fib_ema ribbon is below the shorter one."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bull.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_009_bearish_stack_indicator_8sma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8sma ribbon is above the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_010_bearish_stack_indicator_8ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8ema ribbon is above the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_011_bearish_stack_indicator_8hma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the 8hma ribbon is above the shorter one."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_012_bearish_stack_indicator_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_short_ema ribbon is above the shorter one."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_013_bearish_stack_indicator_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_long_ema ribbon is above the shorter one."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_014_bearish_stack_indicator_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the guppy_full_ema ribbon is above the shorter one."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_015_bearish_stack_indicator_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the fib_sma ribbon is above the shorter one."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_016_bearish_stack_indicator_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Indicator 1.0 if every successive (longer) MA in the fib_ema ribbon is above the shorter one."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bear = (diffs.gt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    sig = bear.where(valid, np.nan)
    return (sig).diff().diff().diff()

def f12_mrib_017_spearman_value_length_corr_8sma_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the 8sma ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_018_spearman_value_length_corr_8ema_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the 8ema ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_019_spearman_value_length_corr_8hma_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the 8hma ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_020_spearman_value_length_corr_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the guppy_short_ema ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_021_spearman_value_length_corr_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the guppy_long_ema ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_022_spearman_value_length_corr_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the guppy_full_ema ribbon. +1 bearish-stacked, -1 bullish."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_023_spearman_value_length_corr_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the fib_sma ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_024_spearman_value_length_corr_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Spearman rank-correlation of (MA value, MA length) across the fib_ema ribbon. +1 bearish-stacked, -1 bullish."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _sp(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        d = vr - len_rank
        return 1.0 - (6.0 * (d * d).sum()) / (n * (n * n - 1.0))
    vals = df.values
    out = np.array([_sp(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_025_ribbon_dispersion_std_norm_close_8sma_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of 8sma ribbon MAs, normalized by close - ribbon width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_026_ribbon_dispersion_std_norm_close_8ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of 8ema ribbon MAs, normalized by close - ribbon width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_027_ribbon_dispersion_std_norm_close_8hma_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of 8hma ribbon MAs, normalized by close - ribbon width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_028_ribbon_dispersion_std_norm_close_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of guppy_short_ema ribbon MAs, normalized by close - ribbon width."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_029_ribbon_dispersion_std_norm_close_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of guppy_long_ema ribbon MAs, normalized by close - ribbon width."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_030_ribbon_dispersion_std_norm_close_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of guppy_full_ema ribbon MAs, normalized by close - ribbon width."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_031_ribbon_dispersion_std_norm_close_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of fib_sma ribbon MAs, normalized by close - ribbon width."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_032_ribbon_dispersion_std_norm_close_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of fib_ema ribbon MAs, normalized by close - ribbon width."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    disp = df.std(axis=1) / close.replace(0, np.nan)
    return (disp).diff().diff().diff()

def f12_mrib_033_ribbon_width_normalized_close_8sma_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the 8sma ribbon - peak-to-trough width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_034_ribbon_width_normalized_close_8ema_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the 8ema ribbon - peak-to-trough width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_035_ribbon_width_normalized_close_8hma_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the 8hma ribbon - peak-to-trough width."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_036_ribbon_width_normalized_close_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the guppy_short_ema ribbon - peak-to-trough width."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_037_ribbon_width_normalized_close_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the guppy_long_ema ribbon - peak-to-trough width."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_038_ribbon_width_normalized_close_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the guppy_full_ema ribbon - peak-to-trough width."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_039_ribbon_width_normalized_close_fib_sma_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the fib_sma ribbon - peak-to-trough width."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_040_ribbon_width_normalized_close_fib_ema_d3(close: pd.Series) -> pd.Series:
    """(Max MA - Min MA) / close across the fib_ema ribbon - peak-to-trough width."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (width).diff().diff().diff()

def f12_mrib_041_frac_bars_bullish_stack_63d_8sma_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the 8sma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_042_frac_bars_bullish_stack_63d_8ema_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the 8ema ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_043_frac_bars_bullish_stack_63d_8hma_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the 8hma ribbon."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_044_frac_bars_bullish_stack_63d_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the guppy_short_ema ribbon."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_045_frac_bars_bullish_stack_63d_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the guppy_long_ema ribbon."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_046_frac_bars_bullish_stack_63d_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the guppy_full_ema ribbon."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_047_frac_bars_bullish_stack_63d_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the fib_sma ribbon."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_048_frac_bars_bullish_stack_63d_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Fraction of last 63d in bullish stack for the fib_ema ribbon."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    diffs = df.diff(axis=1).iloc[:, 1:]
    bull = (diffs.lt(0)).all(axis=1).astype(float)
    valid = df.notna().all(axis=1)
    bull = bull.where(valid, np.nan)
    return (bull.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f12_mrib_049_ribbon_internal_crossings_count_63d_8sma_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the 8sma ribbon - intra-ribbon chop."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_050_ribbon_internal_crossings_count_63d_8ema_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the 8ema ribbon - intra-ribbon chop."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_051_ribbon_internal_crossings_count_63d_8hma_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the 8hma ribbon - intra-ribbon chop."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_052_ribbon_internal_crossings_count_63d_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the guppy_short_ema ribbon - intra-ribbon chop."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_053_ribbon_internal_crossings_count_63d_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the guppy_long_ema ribbon - intra-ribbon chop."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_054_ribbon_internal_crossings_count_63d_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the guppy_full_ema ribbon - intra-ribbon chop."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_055_ribbon_internal_crossings_count_63d_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the fib_sma ribbon - intra-ribbon chop."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_056_ribbon_internal_crossings_count_63d_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d count of adjacent-pair MA crossings within the fib_ema ribbon - intra-ribbon chop."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    total = pd.Series(0.0, index=close.index)
    for i in range(len(mas) - 1):
        total = total.add(_count_crosses(mas[i], mas[i + 1], QDAYS), fill_value=0.0)
    return (total).diff().diff().diff()

def f12_mrib_057_ribbon_kendall_disorder_8sma_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of 8sma ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_058_ribbon_kendall_disorder_8ema_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of 8ema ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_059_ribbon_kendall_disorder_8hma_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of 8hma ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_060_ribbon_kendall_disorder_guppy_short_ema_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of guppy_short_ema ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [3, 5, 8, 10, 12, 15]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_061_ribbon_kendall_disorder_guppy_long_ema_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of guppy_long_ema ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [30, 35, 40, 45, 50, 60]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_062_ribbon_kendall_disorder_guppy_full_ema_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of guppy_full_ema ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_063_ribbon_kendall_disorder_fib_sma_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of fib_sma ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_064_ribbon_kendall_disorder_fib_ema_d3(close: pd.Series) -> pd.Series:
    """Kendall-tau-like disorder of fib_ema ribbon ordering: -1 perfectly ordered, +1 reversed, 0 random."""
    lens = [5, 8, 13, 21, 34, 55, 89, 144]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    len_rank = np.argsort(np.argsort(lens)).astype(float)
    def _kt(row):
        if np.isnan(row).any():
            return np.nan
        vr = pd.Series(row).rank().values
        n = len(row)
        if n < 3:
            return np.nan
        disc = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (vr[i] - vr[j]) * (len_rank[i] - len_rank[j]) < 0:
                    disc += 1
        return 4.0 * disc / (n * (n - 1)) - 1.0
    vals = df.values
    out = np.array([_kt(vals[i]) for i in range(len(vals))], dtype=float)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f12_mrib_065_ribbon_width_zscore_252d_8sma_252z_d3(close: pd.Series) -> pd.Series:
    """252d z-score of 8sma_252z ribbon width - anomalous compression/expansion."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (_rolling_zscore(width, YDAYS, min_periods=QDAYS)).diff().diff().diff()

def f12_mrib_066_ribbon_width_zscore_252d_8ema_252z_d3(close: pd.Series) -> pd.Series:
    """252d z-score of 8ema_252z ribbon width - anomalous compression/expansion."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (_rolling_zscore(width, YDAYS, min_periods=QDAYS)).diff().diff().diff()

def f12_mrib_067_ribbon_width_zscore_252d_8hma_252z_d3(close: pd.Series) -> pd.Series:
    """252d z-score of 8hma_252z ribbon width - anomalous compression/expansion."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (_rolling_zscore(width, YDAYS, min_periods=QDAYS)).diff().diff().diff()

def f12_mrib_068_ribbon_width_zscore_252d_guppy_full_252z_d3(close: pd.Series) -> pd.Series:
    """252d z-score of guppy_full_252z ribbon width - anomalous compression/expansion."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    df = pd.concat([m.rename(i) for i, m in enumerate(mas)], axis=1)
    width = (df.max(axis=1) - df.min(axis=1)) / close.replace(0, np.nan)
    return (_rolling_zscore(width, YDAYS, min_periods=QDAYS)).diff().diff().diff()

def f12_mrib_069_ribbon_mean_slope_21d_8sma_d3(close: pd.Series) -> pd.Series:
    """Mean of per-MA log-slopes (21d) across the 8sma ribbon - aggregate trend velocity."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    avg = df.mean(axis=1)
    return (avg).diff().diff().diff()

def f12_mrib_070_ribbon_mean_slope_21d_8ema_d3(close: pd.Series) -> pd.Series:
    """Mean of per-MA log-slopes (21d) across the 8ema ribbon - aggregate trend velocity."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    avg = df.mean(axis=1)
    return (avg).diff().diff().diff()

def f12_mrib_071_ribbon_mean_slope_21d_8hma_d3(close: pd.Series) -> pd.Series:
    """Mean of per-MA log-slopes (21d) across the 8hma ribbon - aggregate trend velocity."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    avg = df.mean(axis=1)
    return (avg).diff().diff().diff()

def f12_mrib_072_ribbon_mean_slope_21d_guppy_full_d3(close: pd.Series) -> pd.Series:
    """Mean of per-MA log-slopes (21d) across the guppy_full ribbon - aggregate trend velocity."""
    short_lens = [3, 5, 8, 10, 12, 15]
    long_lens  = [30, 35, 40, 45, 50, 60]
    lens = short_lens + long_lens
    short_mas = [_ema(close, n) for n in short_lens]
    long_mas  = [_ema(close, n) for n in long_lens]
    mas = short_mas + long_mas
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    avg = df.mean(axis=1)
    return (avg).diff().diff().diff()

def f12_mrib_073_ribbon_slope_dispersion_21d_8sma_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of per-MA log-slopes (21d) across the 8sma ribbon - regime disagreement."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_sma(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    disp = df.std(axis=1)
    return (disp).diff().diff().diff()

def f12_mrib_074_ribbon_slope_dispersion_21d_8ema_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of per-MA log-slopes (21d) across the 8ema ribbon - regime disagreement."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_ema(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    disp = df.std(axis=1)
    return (disp).diff().diff().diff()

def f12_mrib_075_ribbon_slope_dispersion_21d_8hma_d3(close: pd.Series) -> pd.Series:
    """Cross-sectional std of per-MA log-slopes (21d) across the 8hma ribbon - regime disagreement."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = [_hma(close, n) for n in lens]
    slopes = [_rolling_slope(_safe_log(m), MDAYS) for m in mas]
    df = pd.concat([s.rename(i) for i, s in enumerate(slopes)], axis=1)
    disp = df.std(axis=1)
    return (disp).diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

MOVING_AVERAGE_RIBBON_STRUCTURE_D3_REGISTRY_001_075 = {
    "f12_mrib_001_bullish_stack_indicator_8sma_d3": {"inputs": ["close"], "func": f12_mrib_001_bullish_stack_indicator_8sma_d3},
    "f12_mrib_002_bullish_stack_indicator_8ema_d3": {"inputs": ["close"], "func": f12_mrib_002_bullish_stack_indicator_8ema_d3},
    "f12_mrib_003_bullish_stack_indicator_8hma_d3": {"inputs": ["close"], "func": f12_mrib_003_bullish_stack_indicator_8hma_d3},
    "f12_mrib_004_bullish_stack_indicator_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_004_bullish_stack_indicator_guppy_short_ema_d3},
    "f12_mrib_005_bullish_stack_indicator_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_005_bullish_stack_indicator_guppy_long_ema_d3},
    "f12_mrib_006_bullish_stack_indicator_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_006_bullish_stack_indicator_guppy_full_ema_d3},
    "f12_mrib_007_bullish_stack_indicator_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_007_bullish_stack_indicator_fib_sma_d3},
    "f12_mrib_008_bullish_stack_indicator_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_008_bullish_stack_indicator_fib_ema_d3},
    "f12_mrib_009_bearish_stack_indicator_8sma_d3": {"inputs": ["close"], "func": f12_mrib_009_bearish_stack_indicator_8sma_d3},
    "f12_mrib_010_bearish_stack_indicator_8ema_d3": {"inputs": ["close"], "func": f12_mrib_010_bearish_stack_indicator_8ema_d3},
    "f12_mrib_011_bearish_stack_indicator_8hma_d3": {"inputs": ["close"], "func": f12_mrib_011_bearish_stack_indicator_8hma_d3},
    "f12_mrib_012_bearish_stack_indicator_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_012_bearish_stack_indicator_guppy_short_ema_d3},
    "f12_mrib_013_bearish_stack_indicator_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_013_bearish_stack_indicator_guppy_long_ema_d3},
    "f12_mrib_014_bearish_stack_indicator_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_014_bearish_stack_indicator_guppy_full_ema_d3},
    "f12_mrib_015_bearish_stack_indicator_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_015_bearish_stack_indicator_fib_sma_d3},
    "f12_mrib_016_bearish_stack_indicator_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_016_bearish_stack_indicator_fib_ema_d3},
    "f12_mrib_017_spearman_value_length_corr_8sma_d3": {"inputs": ["close"], "func": f12_mrib_017_spearman_value_length_corr_8sma_d3},
    "f12_mrib_018_spearman_value_length_corr_8ema_d3": {"inputs": ["close"], "func": f12_mrib_018_spearman_value_length_corr_8ema_d3},
    "f12_mrib_019_spearman_value_length_corr_8hma_d3": {"inputs": ["close"], "func": f12_mrib_019_spearman_value_length_corr_8hma_d3},
    "f12_mrib_020_spearman_value_length_corr_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_020_spearman_value_length_corr_guppy_short_ema_d3},
    "f12_mrib_021_spearman_value_length_corr_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_021_spearman_value_length_corr_guppy_long_ema_d3},
    "f12_mrib_022_spearman_value_length_corr_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_022_spearman_value_length_corr_guppy_full_ema_d3},
    "f12_mrib_023_spearman_value_length_corr_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_023_spearman_value_length_corr_fib_sma_d3},
    "f12_mrib_024_spearman_value_length_corr_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_024_spearman_value_length_corr_fib_ema_d3},
    "f12_mrib_025_ribbon_dispersion_std_norm_close_8sma_d3": {"inputs": ["close"], "func": f12_mrib_025_ribbon_dispersion_std_norm_close_8sma_d3},
    "f12_mrib_026_ribbon_dispersion_std_norm_close_8ema_d3": {"inputs": ["close"], "func": f12_mrib_026_ribbon_dispersion_std_norm_close_8ema_d3},
    "f12_mrib_027_ribbon_dispersion_std_norm_close_8hma_d3": {"inputs": ["close"], "func": f12_mrib_027_ribbon_dispersion_std_norm_close_8hma_d3},
    "f12_mrib_028_ribbon_dispersion_std_norm_close_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_028_ribbon_dispersion_std_norm_close_guppy_short_ema_d3},
    "f12_mrib_029_ribbon_dispersion_std_norm_close_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_029_ribbon_dispersion_std_norm_close_guppy_long_ema_d3},
    "f12_mrib_030_ribbon_dispersion_std_norm_close_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_030_ribbon_dispersion_std_norm_close_guppy_full_ema_d3},
    "f12_mrib_031_ribbon_dispersion_std_norm_close_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_031_ribbon_dispersion_std_norm_close_fib_sma_d3},
    "f12_mrib_032_ribbon_dispersion_std_norm_close_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_032_ribbon_dispersion_std_norm_close_fib_ema_d3},
    "f12_mrib_033_ribbon_width_normalized_close_8sma_d3": {"inputs": ["close"], "func": f12_mrib_033_ribbon_width_normalized_close_8sma_d3},
    "f12_mrib_034_ribbon_width_normalized_close_8ema_d3": {"inputs": ["close"], "func": f12_mrib_034_ribbon_width_normalized_close_8ema_d3},
    "f12_mrib_035_ribbon_width_normalized_close_8hma_d3": {"inputs": ["close"], "func": f12_mrib_035_ribbon_width_normalized_close_8hma_d3},
    "f12_mrib_036_ribbon_width_normalized_close_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_036_ribbon_width_normalized_close_guppy_short_ema_d3},
    "f12_mrib_037_ribbon_width_normalized_close_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_037_ribbon_width_normalized_close_guppy_long_ema_d3},
    "f12_mrib_038_ribbon_width_normalized_close_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_038_ribbon_width_normalized_close_guppy_full_ema_d3},
    "f12_mrib_039_ribbon_width_normalized_close_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_039_ribbon_width_normalized_close_fib_sma_d3},
    "f12_mrib_040_ribbon_width_normalized_close_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_040_ribbon_width_normalized_close_fib_ema_d3},
    "f12_mrib_041_frac_bars_bullish_stack_63d_8sma_d3": {"inputs": ["close"], "func": f12_mrib_041_frac_bars_bullish_stack_63d_8sma_d3},
    "f12_mrib_042_frac_bars_bullish_stack_63d_8ema_d3": {"inputs": ["close"], "func": f12_mrib_042_frac_bars_bullish_stack_63d_8ema_d3},
    "f12_mrib_043_frac_bars_bullish_stack_63d_8hma_d3": {"inputs": ["close"], "func": f12_mrib_043_frac_bars_bullish_stack_63d_8hma_d3},
    "f12_mrib_044_frac_bars_bullish_stack_63d_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_044_frac_bars_bullish_stack_63d_guppy_short_ema_d3},
    "f12_mrib_045_frac_bars_bullish_stack_63d_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_045_frac_bars_bullish_stack_63d_guppy_long_ema_d3},
    "f12_mrib_046_frac_bars_bullish_stack_63d_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_046_frac_bars_bullish_stack_63d_guppy_full_ema_d3},
    "f12_mrib_047_frac_bars_bullish_stack_63d_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_047_frac_bars_bullish_stack_63d_fib_sma_d3},
    "f12_mrib_048_frac_bars_bullish_stack_63d_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_048_frac_bars_bullish_stack_63d_fib_ema_d3},
    "f12_mrib_049_ribbon_internal_crossings_count_63d_8sma_d3": {"inputs": ["close"], "func": f12_mrib_049_ribbon_internal_crossings_count_63d_8sma_d3},
    "f12_mrib_050_ribbon_internal_crossings_count_63d_8ema_d3": {"inputs": ["close"], "func": f12_mrib_050_ribbon_internal_crossings_count_63d_8ema_d3},
    "f12_mrib_051_ribbon_internal_crossings_count_63d_8hma_d3": {"inputs": ["close"], "func": f12_mrib_051_ribbon_internal_crossings_count_63d_8hma_d3},
    "f12_mrib_052_ribbon_internal_crossings_count_63d_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_052_ribbon_internal_crossings_count_63d_guppy_short_ema_d3},
    "f12_mrib_053_ribbon_internal_crossings_count_63d_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_053_ribbon_internal_crossings_count_63d_guppy_long_ema_d3},
    "f12_mrib_054_ribbon_internal_crossings_count_63d_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_054_ribbon_internal_crossings_count_63d_guppy_full_ema_d3},
    "f12_mrib_055_ribbon_internal_crossings_count_63d_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_055_ribbon_internal_crossings_count_63d_fib_sma_d3},
    "f12_mrib_056_ribbon_internal_crossings_count_63d_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_056_ribbon_internal_crossings_count_63d_fib_ema_d3},
    "f12_mrib_057_ribbon_kendall_disorder_8sma_d3": {"inputs": ["close"], "func": f12_mrib_057_ribbon_kendall_disorder_8sma_d3},
    "f12_mrib_058_ribbon_kendall_disorder_8ema_d3": {"inputs": ["close"], "func": f12_mrib_058_ribbon_kendall_disorder_8ema_d3},
    "f12_mrib_059_ribbon_kendall_disorder_8hma_d3": {"inputs": ["close"], "func": f12_mrib_059_ribbon_kendall_disorder_8hma_d3},
    "f12_mrib_060_ribbon_kendall_disorder_guppy_short_ema_d3": {"inputs": ["close"], "func": f12_mrib_060_ribbon_kendall_disorder_guppy_short_ema_d3},
    "f12_mrib_061_ribbon_kendall_disorder_guppy_long_ema_d3": {"inputs": ["close"], "func": f12_mrib_061_ribbon_kendall_disorder_guppy_long_ema_d3},
    "f12_mrib_062_ribbon_kendall_disorder_guppy_full_ema_d3": {"inputs": ["close"], "func": f12_mrib_062_ribbon_kendall_disorder_guppy_full_ema_d3},
    "f12_mrib_063_ribbon_kendall_disorder_fib_sma_d3": {"inputs": ["close"], "func": f12_mrib_063_ribbon_kendall_disorder_fib_sma_d3},
    "f12_mrib_064_ribbon_kendall_disorder_fib_ema_d3": {"inputs": ["close"], "func": f12_mrib_064_ribbon_kendall_disorder_fib_ema_d3},
    "f12_mrib_065_ribbon_width_zscore_252d_8sma_252z_d3": {"inputs": ["close"], "func": f12_mrib_065_ribbon_width_zscore_252d_8sma_252z_d3},
    "f12_mrib_066_ribbon_width_zscore_252d_8ema_252z_d3": {"inputs": ["close"], "func": f12_mrib_066_ribbon_width_zscore_252d_8ema_252z_d3},
    "f12_mrib_067_ribbon_width_zscore_252d_8hma_252z_d3": {"inputs": ["close"], "func": f12_mrib_067_ribbon_width_zscore_252d_8hma_252z_d3},
    "f12_mrib_068_ribbon_width_zscore_252d_guppy_full_252z_d3": {"inputs": ["close"], "func": f12_mrib_068_ribbon_width_zscore_252d_guppy_full_252z_d3},
    "f12_mrib_069_ribbon_mean_slope_21d_8sma_d3": {"inputs": ["close"], "func": f12_mrib_069_ribbon_mean_slope_21d_8sma_d3},
    "f12_mrib_070_ribbon_mean_slope_21d_8ema_d3": {"inputs": ["close"], "func": f12_mrib_070_ribbon_mean_slope_21d_8ema_d3},
    "f12_mrib_071_ribbon_mean_slope_21d_8hma_d3": {"inputs": ["close"], "func": f12_mrib_071_ribbon_mean_slope_21d_8hma_d3},
    "f12_mrib_072_ribbon_mean_slope_21d_guppy_full_d3": {"inputs": ["close"], "func": f12_mrib_072_ribbon_mean_slope_21d_guppy_full_d3},
    "f12_mrib_073_ribbon_slope_dispersion_21d_8sma_d3": {"inputs": ["close"], "func": f12_mrib_073_ribbon_slope_dispersion_21d_8sma_d3},
    "f12_mrib_074_ribbon_slope_dispersion_21d_8ema_d3": {"inputs": ["close"], "func": f12_mrib_074_ribbon_slope_dispersion_21d_8ema_d3},
    "f12_mrib_075_ribbon_slope_dispersion_21d_8hma_d3": {"inputs": ["close"], "func": f12_mrib_075_ribbon_slope_dispersion_21d_8hma_d3},
}
