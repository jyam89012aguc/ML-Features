"""ma_crossover_failure_dynamics d2 features 001-075 - Pipeline 1b-technical.

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


def f13_mcxf_001_signed_cross_event_indicator_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a classic golden/death cross (golden=+1, death=-1)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_002_signed_cross_event_indicator_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a MACD short-pair (golden=+1, death=-1)."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_003_signed_cross_event_indicator_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a intraday/short EMA pair (golden=+1, death=-1)."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_004_signed_cross_event_indicator_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a swing EMA pair (golden=+1, death=-1)."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_005_signed_cross_event_indicator_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a long-term EMA cross (golden=+1, death=-1)."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_006_signed_cross_event_indicator_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a short-medium SMA cross (golden=+1, death=-1)."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_007_signed_cross_event_indicator_sma10_30_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a responsive short SMA cross (golden=+1, death=-1)."""
    fast = _sma(close, 10)
    slow = _sma(close, 30)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_008_signed_cross_event_indicator_hma20_50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a Hull short-medium cross (golden=+1, death=-1)."""
    fast = _hma(close, 20)
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_009_signed_cross_event_indicator_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a Hull medium-long cross (golden=+1, death=-1)."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_010_signed_cross_event_indicator_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a close vs 200d regime filter (golden=+1, death=-1)."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_011_signed_cross_event_indicator_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a close vs EMA50 trend filter (golden=+1, death=-1)."""
    fast = close
    slow = _ema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_012_signed_cross_event_indicator_close_hma50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a close vs HMA50 trend filter (golden=+1, death=-1)."""
    fast = close
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_013_signed_cross_event_indicator_dema20_50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a DEMA reduced-lag cross (golden=+1, death=-1)."""
    fast = _dema(close, 20)
    slow = _dema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_014_signed_cross_event_indicator_tema20_50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a TEMA further-reduced-lag cross (golden=+1, death=-1)."""
    fast = _tema(close, 20)
    slow = _tema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_015_signed_cross_event_indicator_kama_sma50_d2(close: pd.Series) -> pd.Series:
    """Signed +1/-1/0 indicator at the bar of a adaptive vs static cross (golden=+1, death=-1)."""
    fast = _kama(close, 10)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    ev = (golden - death).where(fast.notna() & slow.notna(), np.nan)
    return (ev).diff().diff()

def f13_mcxf_016_days_since_last_golden_cross_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the sma50_200 (classic golden/death cross)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_017_days_since_last_golden_cross_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the ema12_26 (MACD short-pair)."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_018_days_since_last_golden_cross_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the ema9_21 (intraday/short EMA pair)."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_019_days_since_last_golden_cross_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the ema21_55 (swing EMA pair)."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_020_days_since_last_golden_cross_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the ema50_200 (long-term EMA cross)."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_021_days_since_last_golden_cross_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the sma20_50 (short-medium SMA cross)."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_022_days_since_last_golden_cross_sma10_30_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the sma10_30 (responsive short SMA cross)."""
    fast = _sma(close, 10)
    slow = _sma(close, 30)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_023_days_since_last_golden_cross_hma20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the hma20_50 (Hull short-medium cross)."""
    fast = _hma(close, 20)
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_024_days_since_last_golden_cross_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the hma50_200 (Hull medium-long cross)."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_025_days_since_last_golden_cross_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the close_sma200 (close vs 200d regime filter)."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_026_days_since_last_golden_cross_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the close_ema50 (close vs EMA50 trend filter)."""
    fast = close
    slow = _ema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_027_days_since_last_golden_cross_close_hma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the close_hma50 (close vs HMA50 trend filter)."""
    fast = close
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_028_days_since_last_golden_cross_dema20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the dema20_50 (DEMA reduced-lag cross)."""
    fast = _dema(close, 20)
    slow = _dema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_029_days_since_last_golden_cross_tema20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the tema20_50 (TEMA further-reduced-lag cross)."""
    fast = _tema(close, 20)
    slow = _tema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_030_days_since_last_golden_cross_kama_sma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent golden cross of the kama_sma50 (adaptive vs static cross)."""
    fast = _kama(close, 10)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    arr = golden.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_031_days_since_last_death_cross_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the sma50_200 (classic golden/death cross)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_032_days_since_last_death_cross_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the ema12_26 (MACD short-pair)."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_033_days_since_last_death_cross_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the ema9_21 (intraday/short EMA pair)."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_034_days_since_last_death_cross_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the ema21_55 (swing EMA pair)."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_035_days_since_last_death_cross_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the ema50_200 (long-term EMA cross)."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_036_days_since_last_death_cross_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the sma20_50 (short-medium SMA cross)."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_037_days_since_last_death_cross_sma10_30_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the sma10_30 (responsive short SMA cross)."""
    fast = _sma(close, 10)
    slow = _sma(close, 30)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_038_days_since_last_death_cross_hma20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the hma20_50 (Hull short-medium cross)."""
    fast = _hma(close, 20)
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_039_days_since_last_death_cross_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the hma50_200 (Hull medium-long cross)."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_040_days_since_last_death_cross_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the close_sma200 (close vs 200d regime filter)."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_041_days_since_last_death_cross_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the close_ema50 (close vs EMA50 trend filter)."""
    fast = close
    slow = _ema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_042_days_since_last_death_cross_close_hma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the close_hma50 (close vs HMA50 trend filter)."""
    fast = close
    slow = _hma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_043_days_since_last_death_cross_dema20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the dema20_50 (DEMA reduced-lag cross)."""
    fast = _dema(close, 20)
    slow = _dema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_044_days_since_last_death_cross_tema20_50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the tema20_50 (TEMA further-reduced-lag cross)."""
    fast = _tema(close, 20)
    slow = _tema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_045_days_since_last_death_cross_kama_sma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent death cross of the kama_sma50 (adaptive vs static cross)."""
    fast = _kama(close, 10)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0))
    arr = death.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_046_golden_cross_failure_within_21d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in sma50_200 occurred within last 21d AND fast is now below slow."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_047_golden_cross_failure_within_21d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in ema12_26 occurred within last 21d AND fast is now below slow."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_048_golden_cross_failure_within_21d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in ema50_200 occurred within last 21d AND fast is now below slow."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_049_golden_cross_failure_within_21d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in sma20_50 occurred within last 21d AND fast is now below slow."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_050_golden_cross_failure_within_21d_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in hma50_200 occurred within last 21d AND fast is now below slow."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_051_golden_cross_failure_within_21d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in close_sma200 occurred within last 21d AND fast is now below slow."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_052_golden_cross_failure_within_21d_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Indicator: a golden cross in close_ema50 occurred within last 21d AND fast is now below slow."""
    fast = close
    slow = _ema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    had_golden_recent = golden.rolling(MDAYS, min_periods=2).max() > 0.5
    below = fast < slow
    fail = (had_golden_recent & below).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_053_death_cross_failure_within_21d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in sma50_200 within last 21d AND fast is now above slow (bear-trap)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_054_death_cross_failure_within_21d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in ema12_26 within last 21d AND fast is now above slow (bear-trap)."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_055_death_cross_failure_within_21d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in ema50_200 within last 21d AND fast is now above slow (bear-trap)."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_056_death_cross_failure_within_21d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in sma20_50 within last 21d AND fast is now above slow (bear-trap)."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_057_death_cross_failure_within_21d_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in hma50_200 within last 21d AND fast is now above slow (bear-trap)."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_058_death_cross_failure_within_21d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in close_sma200 within last 21d AND fast is now above slow (bear-trap)."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_059_death_cross_failure_within_21d_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Indicator: a death cross in close_ema50 within last 21d AND fast is now above slow (bear-trap)."""
    fast = close
    slow = _ema(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    death = ((sign < 0) & (prev >= 0)).astype(float)
    had_death_recent = death.rolling(MDAYS, min_periods=2).max() > 0.5
    above = fast > slow
    fail = (had_death_recent & above).astype(float).where(fast.notna() & slow.notna(), np.nan)
    return (fail).diff().diff()

def f13_mcxf_060_cross_count_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the sma50_200."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_061_cross_count_252d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the ema12_26."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_062_cross_count_252d_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the ema9_21."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_063_cross_count_252d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the ema50_200."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_064_cross_count_252d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the sma20_50."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_065_cross_count_252d_hma20_50_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the hma20_50."""
    fast = _hma(close, 20)
    slow = _hma(close, 50)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_066_cross_count_252d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the close_sma200."""
    fast = close
    slow = _sma(close, 200)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_067_cross_count_252d_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d count of all (golden+death) cross events in the close_ema50."""
    fast = close
    slow = _ema(close, 50)
    return (_count_crosses(fast, slow, YDAYS)).diff().diff()

def f13_mcxf_068_cross_count_63d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the sma50_200 - short-horizon chop intensity."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_069_cross_count_63d_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the ema9_21 - short-horizon chop intensity."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_070_cross_count_63d_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the ema21_55 - short-horizon chop intensity."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_071_cross_count_63d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the ema12_26 - short-horizon chop intensity."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_072_cross_count_63d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the sma20_50 - short-horizon chop intensity."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_073_cross_count_63d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the close_sma200 - short-horizon chop intensity."""
    fast = close
    slow = _sma(close, 200)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_074_cross_count_63d_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of cross events in the close_ema50 - short-horizon chop intensity."""
    fast = close
    slow = _ema(close, 50)
    return (_count_crosses(fast, slow, QDAYS)).diff().diff()

def f13_mcxf_075_mean_bars_between_crosses_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the sma50_200 over 252d."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

MA_CROSSOVER_FAILURE_DYNAMICS_D2_REGISTRY_001_075 = {
    "f13_mcxf_001_signed_cross_event_indicator_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_001_signed_cross_event_indicator_sma50_200_d2},
    "f13_mcxf_002_signed_cross_event_indicator_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_002_signed_cross_event_indicator_ema12_26_d2},
    "f13_mcxf_003_signed_cross_event_indicator_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_003_signed_cross_event_indicator_ema9_21_d2},
    "f13_mcxf_004_signed_cross_event_indicator_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_004_signed_cross_event_indicator_ema21_55_d2},
    "f13_mcxf_005_signed_cross_event_indicator_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_005_signed_cross_event_indicator_ema50_200_d2},
    "f13_mcxf_006_signed_cross_event_indicator_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_006_signed_cross_event_indicator_sma20_50_d2},
    "f13_mcxf_007_signed_cross_event_indicator_sma10_30_d2": {"inputs": ["close"], "func": f13_mcxf_007_signed_cross_event_indicator_sma10_30_d2},
    "f13_mcxf_008_signed_cross_event_indicator_hma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_008_signed_cross_event_indicator_hma20_50_d2},
    "f13_mcxf_009_signed_cross_event_indicator_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_009_signed_cross_event_indicator_hma50_200_d2},
    "f13_mcxf_010_signed_cross_event_indicator_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_010_signed_cross_event_indicator_close_sma200_d2},
    "f13_mcxf_011_signed_cross_event_indicator_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_011_signed_cross_event_indicator_close_ema50_d2},
    "f13_mcxf_012_signed_cross_event_indicator_close_hma50_d2": {"inputs": ["close"], "func": f13_mcxf_012_signed_cross_event_indicator_close_hma50_d2},
    "f13_mcxf_013_signed_cross_event_indicator_dema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_013_signed_cross_event_indicator_dema20_50_d2},
    "f13_mcxf_014_signed_cross_event_indicator_tema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_014_signed_cross_event_indicator_tema20_50_d2},
    "f13_mcxf_015_signed_cross_event_indicator_kama_sma50_d2": {"inputs": ["close"], "func": f13_mcxf_015_signed_cross_event_indicator_kama_sma50_d2},
    "f13_mcxf_016_days_since_last_golden_cross_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_016_days_since_last_golden_cross_sma50_200_d2},
    "f13_mcxf_017_days_since_last_golden_cross_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_017_days_since_last_golden_cross_ema12_26_d2},
    "f13_mcxf_018_days_since_last_golden_cross_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_018_days_since_last_golden_cross_ema9_21_d2},
    "f13_mcxf_019_days_since_last_golden_cross_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_019_days_since_last_golden_cross_ema21_55_d2},
    "f13_mcxf_020_days_since_last_golden_cross_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_020_days_since_last_golden_cross_ema50_200_d2},
    "f13_mcxf_021_days_since_last_golden_cross_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_021_days_since_last_golden_cross_sma20_50_d2},
    "f13_mcxf_022_days_since_last_golden_cross_sma10_30_d2": {"inputs": ["close"], "func": f13_mcxf_022_days_since_last_golden_cross_sma10_30_d2},
    "f13_mcxf_023_days_since_last_golden_cross_hma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_023_days_since_last_golden_cross_hma20_50_d2},
    "f13_mcxf_024_days_since_last_golden_cross_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_024_days_since_last_golden_cross_hma50_200_d2},
    "f13_mcxf_025_days_since_last_golden_cross_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_025_days_since_last_golden_cross_close_sma200_d2},
    "f13_mcxf_026_days_since_last_golden_cross_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_026_days_since_last_golden_cross_close_ema50_d2},
    "f13_mcxf_027_days_since_last_golden_cross_close_hma50_d2": {"inputs": ["close"], "func": f13_mcxf_027_days_since_last_golden_cross_close_hma50_d2},
    "f13_mcxf_028_days_since_last_golden_cross_dema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_028_days_since_last_golden_cross_dema20_50_d2},
    "f13_mcxf_029_days_since_last_golden_cross_tema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_029_days_since_last_golden_cross_tema20_50_d2},
    "f13_mcxf_030_days_since_last_golden_cross_kama_sma50_d2": {"inputs": ["close"], "func": f13_mcxf_030_days_since_last_golden_cross_kama_sma50_d2},
    "f13_mcxf_031_days_since_last_death_cross_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_031_days_since_last_death_cross_sma50_200_d2},
    "f13_mcxf_032_days_since_last_death_cross_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_032_days_since_last_death_cross_ema12_26_d2},
    "f13_mcxf_033_days_since_last_death_cross_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_033_days_since_last_death_cross_ema9_21_d2},
    "f13_mcxf_034_days_since_last_death_cross_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_034_days_since_last_death_cross_ema21_55_d2},
    "f13_mcxf_035_days_since_last_death_cross_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_035_days_since_last_death_cross_ema50_200_d2},
    "f13_mcxf_036_days_since_last_death_cross_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_036_days_since_last_death_cross_sma20_50_d2},
    "f13_mcxf_037_days_since_last_death_cross_sma10_30_d2": {"inputs": ["close"], "func": f13_mcxf_037_days_since_last_death_cross_sma10_30_d2},
    "f13_mcxf_038_days_since_last_death_cross_hma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_038_days_since_last_death_cross_hma20_50_d2},
    "f13_mcxf_039_days_since_last_death_cross_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_039_days_since_last_death_cross_hma50_200_d2},
    "f13_mcxf_040_days_since_last_death_cross_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_040_days_since_last_death_cross_close_sma200_d2},
    "f13_mcxf_041_days_since_last_death_cross_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_041_days_since_last_death_cross_close_ema50_d2},
    "f13_mcxf_042_days_since_last_death_cross_close_hma50_d2": {"inputs": ["close"], "func": f13_mcxf_042_days_since_last_death_cross_close_hma50_d2},
    "f13_mcxf_043_days_since_last_death_cross_dema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_043_days_since_last_death_cross_dema20_50_d2},
    "f13_mcxf_044_days_since_last_death_cross_tema20_50_d2": {"inputs": ["close"], "func": f13_mcxf_044_days_since_last_death_cross_tema20_50_d2},
    "f13_mcxf_045_days_since_last_death_cross_kama_sma50_d2": {"inputs": ["close"], "func": f13_mcxf_045_days_since_last_death_cross_kama_sma50_d2},
    "f13_mcxf_046_golden_cross_failure_within_21d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_046_golden_cross_failure_within_21d_sma50_200_d2},
    "f13_mcxf_047_golden_cross_failure_within_21d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_047_golden_cross_failure_within_21d_ema12_26_d2},
    "f13_mcxf_048_golden_cross_failure_within_21d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_048_golden_cross_failure_within_21d_ema50_200_d2},
    "f13_mcxf_049_golden_cross_failure_within_21d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_049_golden_cross_failure_within_21d_sma20_50_d2},
    "f13_mcxf_050_golden_cross_failure_within_21d_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_050_golden_cross_failure_within_21d_hma50_200_d2},
    "f13_mcxf_051_golden_cross_failure_within_21d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_051_golden_cross_failure_within_21d_close_sma200_d2},
    "f13_mcxf_052_golden_cross_failure_within_21d_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_052_golden_cross_failure_within_21d_close_ema50_d2},
    "f13_mcxf_053_death_cross_failure_within_21d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_053_death_cross_failure_within_21d_sma50_200_d2},
    "f13_mcxf_054_death_cross_failure_within_21d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_054_death_cross_failure_within_21d_ema12_26_d2},
    "f13_mcxf_055_death_cross_failure_within_21d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_055_death_cross_failure_within_21d_ema50_200_d2},
    "f13_mcxf_056_death_cross_failure_within_21d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_056_death_cross_failure_within_21d_sma20_50_d2},
    "f13_mcxf_057_death_cross_failure_within_21d_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_057_death_cross_failure_within_21d_hma50_200_d2},
    "f13_mcxf_058_death_cross_failure_within_21d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_058_death_cross_failure_within_21d_close_sma200_d2},
    "f13_mcxf_059_death_cross_failure_within_21d_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_059_death_cross_failure_within_21d_close_ema50_d2},
    "f13_mcxf_060_cross_count_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_060_cross_count_252d_sma50_200_d2},
    "f13_mcxf_061_cross_count_252d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_061_cross_count_252d_ema12_26_d2},
    "f13_mcxf_062_cross_count_252d_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_062_cross_count_252d_ema9_21_d2},
    "f13_mcxf_063_cross_count_252d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_063_cross_count_252d_ema50_200_d2},
    "f13_mcxf_064_cross_count_252d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_064_cross_count_252d_sma20_50_d2},
    "f13_mcxf_065_cross_count_252d_hma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_065_cross_count_252d_hma20_50_d2},
    "f13_mcxf_066_cross_count_252d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_066_cross_count_252d_close_sma200_d2},
    "f13_mcxf_067_cross_count_252d_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_067_cross_count_252d_close_ema50_d2},
    "f13_mcxf_068_cross_count_63d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_068_cross_count_63d_sma50_200_d2},
    "f13_mcxf_069_cross_count_63d_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_069_cross_count_63d_ema9_21_d2},
    "f13_mcxf_070_cross_count_63d_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_070_cross_count_63d_ema21_55_d2},
    "f13_mcxf_071_cross_count_63d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_071_cross_count_63d_ema12_26_d2},
    "f13_mcxf_072_cross_count_63d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_072_cross_count_63d_sma20_50_d2},
    "f13_mcxf_073_cross_count_63d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_073_cross_count_63d_close_sma200_d2},
    "f13_mcxf_074_cross_count_63d_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_074_cross_count_63d_close_ema50_d2},
    "f13_mcxf_075_mean_bars_between_crosses_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_075_mean_bars_between_crosses_252d_sma50_200_d2},
}
