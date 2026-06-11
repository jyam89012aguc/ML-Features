"""ma_crossover_failure_dynamics d2 features 076-150 - Pipeline 1b-technical.

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


def f13_mcxf_076_mean_bars_between_crosses_252d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the ema12_26 over 252d."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_077_mean_bars_between_crosses_252d_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the ema9_21 over 252d."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_078_mean_bars_between_crosses_252d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the ema50_200 over 252d."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_079_mean_bars_between_crosses_252d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the sma20_50 over 252d."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_080_mean_bars_between_crosses_252d_hma20_50_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the hma20_50 over 252d."""
    fast = _hma(close, 20)
    slow = _hma(close, 50)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_081_mean_bars_between_crosses_252d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Approximate mean bars between crossings (=252/count) in the close_sma200 over 252d."""
    fast = close
    slow = _sma(close, 200)
    cc = _count_crosses(fast, slow, YDAYS)
    return (_safe_div(pd.Series(float(YDAYS), index=close.index), cc)).diff().diff()

def f13_mcxf_082_fast_ma_slope_at_cross_sma50_200_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in sma50_200 - cross energy."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_083_fast_ma_slope_at_cross_ema12_26_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in ema12_26 - cross energy."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_084_fast_ma_slope_at_cross_ema21_55_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in ema21_55 - cross energy."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_085_fast_ma_slope_at_cross_ema50_200_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in ema50_200 - cross energy."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_086_fast_ma_slope_at_cross_sma20_50_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in sma20_50 - cross energy."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_087_fast_ma_slope_at_cross_hma50_200_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in hma50_200 - cross energy."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_088_fast_ma_slope_at_cross_close_sma200_d2(close: pd.Series) -> pd.Series:
    """21d log-slope of the FAST MA captured only at the bar of a cross in close_sma200 - cross energy."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = ((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))
    slope = _rolling_slope(_safe_log(fast.replace(0, np.nan)), MDAYS)
    energy = slope.where(event, np.nan)
    return (energy).diff().diff()

def f13_mcxf_089_log_spread_fast_minus_slow_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the sma50_200 - amplitude of trend relative to that pair."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_090_log_spread_fast_minus_slow_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the ema12_26 - amplitude of trend relative to that pair."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_091_log_spread_fast_minus_slow_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the ema21_55 - amplitude of trend relative to that pair."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_092_log_spread_fast_minus_slow_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the ema50_200 - amplitude of trend relative to that pair."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_093_log_spread_fast_minus_slow_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the sma20_50 - amplitude of trend relative to that pair."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_094_log_spread_fast_minus_slow_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the hma50_200 - amplitude of trend relative to that pair."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_095_log_spread_fast_minus_slow_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio fast/slow MA of the close_sma200 - amplitude of trend relative to that pair."""
    fast = close
    slow = _sma(close, 200)
    return (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).diff().diff()

def f13_mcxf_096_log_spread_zscore_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the sma50_200 - extreme-trend anomaly."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_097_log_spread_zscore_252d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the ema12_26 - extreme-trend anomaly."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_098_log_spread_zscore_252d_ema21_55_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the ema21_55 - extreme-trend anomaly."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_099_log_spread_zscore_252d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the ema50_200 - extreme-trend anomaly."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_100_log_spread_zscore_252d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the sma20_50 - extreme-trend anomaly."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_101_log_spread_zscore_252d_hma50_200_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the hma50_200 - extreme-trend anomaly."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_102_log_spread_zscore_252d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """252d z-score of fast-minus-slow log-spread in the close_sma200 - extreme-trend anomaly."""
    fast = close
    slow = _sma(close, 200)
    spread = _safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))
    return (_rolling_zscore(spread, YDAYS, min_periods=QDAYS)).diff().diff()

def f13_mcxf_103_sign_of_fast_minus_slow_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the sma50_200 - +1 trend-up regime, -1 trend-down."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_104_sign_of_fast_minus_slow_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the ema12_26 - +1 trend-up regime, -1 trend-down."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_105_sign_of_fast_minus_slow_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the ema21_55 - +1 trend-up regime, -1 trend-down."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_106_sign_of_fast_minus_slow_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the ema50_200 - +1 trend-up regime, -1 trend-down."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_107_sign_of_fast_minus_slow_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the sma20_50 - +1 trend-up regime, -1 trend-down."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_108_sign_of_fast_minus_slow_hma50_200_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the hma50_200 - +1 trend-up regime, -1 trend-down."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_109_sign_of_fast_minus_slow_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Sign of (fast-slow) in the close_sma200 - +1 trend-up regime, -1 trend-down."""
    fast = close
    slow = _sma(close, 200)
    valid = fast.notna() & slow.notna()
    return (np.sign((fast - slow)).where(valid, np.nan)).diff().diff()

def f13_mcxf_110_recross_within_5d_count_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the sma50_200 within the last 5 bars (>=2 means recross)."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_111_recross_within_5d_count_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema12_26 within the last 5 bars (>=2 means recross)."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_112_recross_within_5d_count_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema9_21 within the last 5 bars (>=2 means recross)."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_113_recross_within_5d_count_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema21_55 within the last 5 bars (>=2 means recross)."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_114_recross_within_5d_count_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema50_200 within the last 5 bars (>=2 means recross)."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_115_recross_within_5d_count_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the close_sma200 within the last 5 bars (>=2 means recross)."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(WDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_116_recross_within_21d_count_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the sma50_200 within the last 21 bars - whipsaw chop intensity."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_117_recross_within_21d_count_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema12_26 within the last 21 bars - whipsaw chop intensity."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_118_recross_within_21d_count_ema9_21_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema9_21 within the last 21 bars - whipsaw chop intensity."""
    fast = _ema(close, 9)
    slow = _ema(close, 21)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_119_recross_within_21d_count_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema21_55 within the last 21 bars - whipsaw chop intensity."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_120_recross_within_21d_count_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the ema50_200 within the last 21 bars - whipsaw chop intensity."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_121_recross_within_21d_count_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Number of cross events in the close_sma200 within the last 21 bars - whipsaw chop intensity."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0))).astype(float)
    recent = event.rolling(MDAYS, min_periods=2).sum()
    return (recent).diff().diff()

def f13_mcxf_122_bars_since_cross_over_mean_cycle_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the sma50_200."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_123_bars_since_cross_over_mean_cycle_252d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the ema12_26."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_124_bars_since_cross_over_mean_cycle_252d_ema21_55_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the ema21_55."""
    fast = _ema(close, 21)
    slow = _ema(close, 55)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_125_bars_since_cross_over_mean_cycle_252d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the ema50_200."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_126_bars_since_cross_over_mean_cycle_252d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the sma20_50."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_127_bars_since_cross_over_mean_cycle_252d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """(bars-since-last cross) / (mean cross cycle over 252d) for the close_sma200."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    cc = _count_crosses(fast, slow, YDAYS)
    mean_cycle = _safe_div(pd.Series(float(YDAYS), index=close.index), cc)
    return (_safe_div(bars_since, mean_cycle)).diff().diff()

def f13_mcxf_128_joint_signed_cross_event_sma50_200_AND_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Signed +/-1 indicator at bars where BOTH pairs cross same direction simultaneously (sma50_200_AND_ema50_200)."""
    fast1 = _sma(close, 50);  slow1 = _sma(close, 200)
    fast2 = _ema(close, 50);  slow2 = _ema(close, 200)
    s1 = np.sign((fast1 - slow1).fillna(0.0)); p1 = s1.shift(1)
    s2 = np.sign((fast2 - slow2).fillna(0.0)); p2 = s2.shift(1)
    g1 = ((s1 > 0) & (p1 <= 0)); g2 = ((s2 > 0) & (p2 <= 0))
    d1 = ((s1 < 0) & (p1 >= 0)); d2 = ((s2 < 0) & (p2 >= 0))
    joint = ((g1 & g2).astype(float) - (d1 & d2).astype(float))
    valid = fast1.notna() & slow1.notna() & fast2.notna() & slow2.notna()
    return (joint.where(valid, np.nan)).diff().diff()

def f13_mcxf_129_joint_signed_cross_event_sma50_200_AND_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Signed +/-1 indicator at bars where BOTH pairs cross same direction simultaneously (sma50_200_AND_ema12_26)."""
    fast1 = _sma(close, 50);  slow1 = _sma(close, 200)
    fast2 = _ema(close, 12);  slow2 = _ema(close, 26)
    s1 = np.sign((fast1 - slow1).fillna(0.0)); p1 = s1.shift(1)
    s2 = np.sign((fast2 - slow2).fillna(0.0)); p2 = s2.shift(1)
    g1 = ((s1 > 0) & (p1 <= 0)); g2 = ((s2 > 0) & (p2 <= 0))
    d1 = ((s1 < 0) & (p1 >= 0)); d2 = ((s2 < 0) & (p2 >= 0))
    joint = ((g1 & g2).astype(float) - (d1 & d2).astype(float))
    valid = fast1.notna() & slow1.notna() & fast2.notna() & slow2.notna()
    return (joint.where(valid, np.nan)).diff().diff()

def f13_mcxf_130_joint_signed_cross_event_close_sma200_AND_close_ema50_d2(close: pd.Series) -> pd.Series:
    """Signed +/-1 indicator at bars where BOTH pairs cross same direction simultaneously (close_sma200_AND_close_ema50)."""
    fast1 = close;             slow1 = _sma(close, 200)
    fast2 = close;             slow2 = _ema(close, 50)
    s1 = np.sign((fast1 - slow1).fillna(0.0)); p1 = s1.shift(1)
    s2 = np.sign((fast2 - slow2).fillna(0.0)); p2 = s2.shift(1)
    g1 = ((s1 > 0) & (p1 <= 0)); g2 = ((s2 > 0) & (p2 <= 0))
    d1 = ((s1 < 0) & (p1 >= 0)); d2 = ((s2 < 0) & (p2 >= 0))
    joint = ((g1 & g2).astype(float) - (d1 & d2).astype(float))
    valid = fast1.notna() & slow1.notna() & fast2.notna() & slow2.notna()
    return (joint.where(valid, np.nan)).diff().diff()

def f13_mcxf_131_joint_signed_cross_event_ema9_21_AND_ema21_55_d2(close: pd.Series) -> pd.Series:
    """Signed +/-1 indicator at bars where BOTH pairs cross same direction simultaneously (ema9_21_AND_ema21_55)."""
    fast1 = _ema(close, 9);   slow1 = _ema(close, 21)
    fast2 = _ema(close, 21); slow2 = _ema(close, 55)
    s1 = np.sign((fast1 - slow1).fillna(0.0)); p1 = s1.shift(1)
    s2 = np.sign((fast2 - slow2).fillna(0.0)); p2 = s2.shift(1)
    g1 = ((s1 > 0) & (p1 <= 0)); g2 = ((s2 > 0) & (p2 <= 0))
    d1 = ((s1 < 0) & (p1 >= 0)); d2 = ((s2 < 0) & (p2 >= 0))
    joint = ((g1 & g2).astype(float) - (d1 & d2).astype(float))
    valid = fast1.notna() & slow1.notna() & fast2.notna() & slow2.notna()
    return (joint.where(valid, np.nan)).diff().diff()

def f13_mcxf_132_joint_signed_cross_event_hma50_200_AND_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Signed +/-1 indicator at bars where BOTH pairs cross same direction simultaneously (hma50_200_AND_sma50_200)."""
    fast1 = _hma(close, 50);  slow1 = _hma(close, 200)
    fast2 = _sma(close, 50);  slow2 = _sma(close, 200)
    s1 = np.sign((fast1 - slow1).fillna(0.0)); p1 = s1.shift(1)
    s2 = np.sign((fast2 - slow2).fillna(0.0)); p2 = s2.shift(1)
    g1 = ((s1 > 0) & (p1 <= 0)); g2 = ((s2 > 0) & (p2 <= 0))
    d1 = ((s1 < 0) & (p1 >= 0)); d2 = ((s2 < 0) & (p2 >= 0))
    joint = ((g1 & g2).astype(float) - (d1 & d2).astype(float))
    valid = fast1.notna() & slow1.notna() & fast2.notna() & slow2.notna()
    return (joint.where(valid, np.nan)).diff().diff()

def f13_mcxf_133_cross_quality_log_spread_within_21d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """Absolute log-spread of the sma50_200 during the 21 bars following each cross - cross quality."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    spread = (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).abs()
    qual = spread.where(bars_since <= MDAYS, np.nan)
    return (qual).diff().diff()

def f13_mcxf_134_cross_quality_log_spread_within_21d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """Absolute log-spread of the ema12_26 during the 21 bars following each cross - cross quality."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    spread = (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).abs()
    qual = spread.where(bars_since <= MDAYS, np.nan)
    return (qual).diff().diff()

def f13_mcxf_135_cross_quality_log_spread_within_21d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """Absolute log-spread of the ema50_200 during the 21 bars following each cross - cross quality."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    spread = (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).abs()
    qual = spread.where(bars_since <= MDAYS, np.nan)
    return (qual).diff().diff()

def f13_mcxf_136_cross_quality_log_spread_within_21d_sma20_50_d2(close: pd.Series) -> pd.Series:
    """Absolute log-spread of the sma20_50 during the 21 bars following each cross - cross quality."""
    fast = _sma(close, 20)
    slow = _sma(close, 50)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    spread = (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).abs()
    qual = spread.where(bars_since <= MDAYS, np.nan)
    return (qual).diff().diff()

def f13_mcxf_137_cross_quality_log_spread_within_21d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """Absolute log-spread of the close_sma200 during the 21 bars following each cross - cross quality."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    arr = event.values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    bars_since = pd.Series(out, index=close.index)
    spread = (_safe_log(fast.replace(0, np.nan)) - _safe_log(slow.replace(0, np.nan))).abs()
    qual = spread.where(bars_since <= MDAYS, np.nan)
    return (qual).diff().diff()

def f13_mcxf_138_slow_ma_slope_at_cross_63d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """63d log-slope of the SLOW MA captured only at bars of a sma50_200 cross - trend alignment."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    slope = _rolling_slope(_safe_log(slow.replace(0, np.nan)), QDAYS)
    res = slope.where(event, np.nan)
    return (res).diff().diff()

def f13_mcxf_139_slow_ma_slope_at_cross_63d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """63d log-slope of the SLOW MA captured only at bars of a ema12_26 cross - trend alignment."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    slope = _rolling_slope(_safe_log(slow.replace(0, np.nan)), QDAYS)
    res = slope.where(event, np.nan)
    return (res).diff().diff()

def f13_mcxf_140_slow_ma_slope_at_cross_63d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """63d log-slope of the SLOW MA captured only at bars of a ema50_200 cross - trend alignment."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    slope = _rolling_slope(_safe_log(slow.replace(0, np.nan)), QDAYS)
    res = slope.where(event, np.nan)
    return (res).diff().diff()

def f13_mcxf_141_slow_ma_slope_at_cross_63d_hma50_200_d2(close: pd.Series) -> pd.Series:
    """63d log-slope of the SLOW MA captured only at bars of a hma50_200 cross - trend alignment."""
    fast = _hma(close, 50)
    slow = _hma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    slope = _rolling_slope(_safe_log(slow.replace(0, np.nan)), QDAYS)
    res = slope.where(event, np.nan)
    return (res).diff().diff()

def f13_mcxf_142_slow_ma_slope_at_cross_63d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """63d log-slope of the SLOW MA captured only at bars of a close_sma200 cross - trend alignment."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    event = (((sign > 0) & (prev <= 0)) | ((sign < 0) & (prev >= 0)))
    slope = _rolling_slope(_safe_log(slow.replace(0, np.nan)), QDAYS)
    res = slope.where(event, np.nan)
    return (res).diff().diff()

def f13_mcxf_143_golden_minus_death_count_252d_sma50_200_d2(close: pd.Series) -> pd.Series:
    """252d count(golden) - count(death) in the sma50_200 - net trend-direction asymmetry."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    g = golden.rolling(YDAYS, min_periods=QDAYS).sum()
    d = death.rolling(YDAYS, min_periods=QDAYS).sum()
    return (g - d).diff().diff()

def f13_mcxf_144_golden_minus_death_count_252d_ema12_26_d2(close: pd.Series) -> pd.Series:
    """252d count(golden) - count(death) in the ema12_26 - net trend-direction asymmetry."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    g = golden.rolling(YDAYS, min_periods=QDAYS).sum()
    d = death.rolling(YDAYS, min_periods=QDAYS).sum()
    return (g - d).diff().diff()

def f13_mcxf_145_golden_minus_death_count_252d_ema50_200_d2(close: pd.Series) -> pd.Series:
    """252d count(golden) - count(death) in the ema50_200 - net trend-direction asymmetry."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    g = golden.rolling(YDAYS, min_periods=QDAYS).sum()
    d = death.rolling(YDAYS, min_periods=QDAYS).sum()
    return (g - d).diff().diff()

def f13_mcxf_146_golden_minus_death_count_252d_close_sma200_d2(close: pd.Series) -> pd.Series:
    """252d count(golden) - count(death) in the close_sma200 - net trend-direction asymmetry."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0)).astype(float)
    death  = ((sign < 0) & (prev >= 0)).astype(float)
    g = golden.rolling(YDAYS, min_periods=QDAYS).sum()
    d = death.rolling(YDAYS, min_periods=QDAYS).sum()
    return (g - d).diff().diff()

def f13_mcxf_147_last_cross_was_golden_indicator_sma50_200_d2(close: pd.Series) -> pd.Series:
    """1.0 if most recent cross in sma50_200 was a golden cross, 0.0 if death, NaN before first cross."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    death  = ((sign < 0) & (prev >= 0))
    arr_g = golden.values; arr_d = death.values
    out = np.full(len(arr_g), np.nan, dtype=float)
    state = np.nan
    for i in range(len(arr_g)):
        if arr_g[i]:
            state = 1.0
        elif arr_d[i]:
            state = 0.0
        out[i] = state
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_148_last_cross_was_golden_indicator_ema50_200_d2(close: pd.Series) -> pd.Series:
    """1.0 if most recent cross in ema50_200 was a golden cross, 0.0 if death, NaN before first cross."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    death  = ((sign < 0) & (prev >= 0))
    arr_g = golden.values; arr_d = death.values
    out = np.full(len(arr_g), np.nan, dtype=float)
    state = np.nan
    for i in range(len(arr_g)):
        if arr_g[i]:
            state = 1.0
        elif arr_d[i]:
            state = 0.0
        out[i] = state
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_149_last_cross_was_golden_indicator_close_sma200_d2(close: pd.Series) -> pd.Series:
    """1.0 if most recent cross in close_sma200 was a golden cross, 0.0 if death, NaN before first cross."""
    fast = close
    slow = _sma(close, 200)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    death  = ((sign < 0) & (prev >= 0))
    arr_g = golden.values; arr_d = death.values
    out = np.full(len(arr_g), np.nan, dtype=float)
    state = np.nan
    for i in range(len(arr_g)):
        if arr_g[i]:
            state = 1.0
        elif arr_d[i]:
            state = 0.0
        out[i] = state
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()

def f13_mcxf_150_last_cross_was_golden_indicator_ema12_26_d2(close: pd.Series) -> pd.Series:
    """1.0 if most recent cross in ema12_26 was a golden cross, 0.0 if death, NaN before first cross."""
    fast = _ema(close, 12)
    slow = _ema(close, 26)
    sign = np.sign((fast - slow).fillna(0.0))
    prev = sign.shift(1)
    golden = ((sign > 0) & (prev <= 0))
    death  = ((sign < 0) & (prev >= 0))
    arr_g = golden.values; arr_d = death.values
    out = np.full(len(arr_g), np.nan, dtype=float)
    state = np.nan
    for i in range(len(arr_g)):
        if arr_g[i]:
            state = 1.0
        elif arr_d[i]:
            state = 0.0
        out[i] = state
    res = pd.Series(out, index=close.index)
    return (res).diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

MA_CROSSOVER_FAILURE_DYNAMICS_D2_REGISTRY_076_150 = {
    "f13_mcxf_076_mean_bars_between_crosses_252d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_076_mean_bars_between_crosses_252d_ema12_26_d2},
    "f13_mcxf_077_mean_bars_between_crosses_252d_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_077_mean_bars_between_crosses_252d_ema9_21_d2},
    "f13_mcxf_078_mean_bars_between_crosses_252d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_078_mean_bars_between_crosses_252d_ema50_200_d2},
    "f13_mcxf_079_mean_bars_between_crosses_252d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_079_mean_bars_between_crosses_252d_sma20_50_d2},
    "f13_mcxf_080_mean_bars_between_crosses_252d_hma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_080_mean_bars_between_crosses_252d_hma20_50_d2},
    "f13_mcxf_081_mean_bars_between_crosses_252d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_081_mean_bars_between_crosses_252d_close_sma200_d2},
    "f13_mcxf_082_fast_ma_slope_at_cross_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_082_fast_ma_slope_at_cross_sma50_200_d2},
    "f13_mcxf_083_fast_ma_slope_at_cross_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_083_fast_ma_slope_at_cross_ema12_26_d2},
    "f13_mcxf_084_fast_ma_slope_at_cross_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_084_fast_ma_slope_at_cross_ema21_55_d2},
    "f13_mcxf_085_fast_ma_slope_at_cross_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_085_fast_ma_slope_at_cross_ema50_200_d2},
    "f13_mcxf_086_fast_ma_slope_at_cross_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_086_fast_ma_slope_at_cross_sma20_50_d2},
    "f13_mcxf_087_fast_ma_slope_at_cross_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_087_fast_ma_slope_at_cross_hma50_200_d2},
    "f13_mcxf_088_fast_ma_slope_at_cross_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_088_fast_ma_slope_at_cross_close_sma200_d2},
    "f13_mcxf_089_log_spread_fast_minus_slow_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_089_log_spread_fast_minus_slow_sma50_200_d2},
    "f13_mcxf_090_log_spread_fast_minus_slow_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_090_log_spread_fast_minus_slow_ema12_26_d2},
    "f13_mcxf_091_log_spread_fast_minus_slow_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_091_log_spread_fast_minus_slow_ema21_55_d2},
    "f13_mcxf_092_log_spread_fast_minus_slow_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_092_log_spread_fast_minus_slow_ema50_200_d2},
    "f13_mcxf_093_log_spread_fast_minus_slow_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_093_log_spread_fast_minus_slow_sma20_50_d2},
    "f13_mcxf_094_log_spread_fast_minus_slow_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_094_log_spread_fast_minus_slow_hma50_200_d2},
    "f13_mcxf_095_log_spread_fast_minus_slow_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_095_log_spread_fast_minus_slow_close_sma200_d2},
    "f13_mcxf_096_log_spread_zscore_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_096_log_spread_zscore_252d_sma50_200_d2},
    "f13_mcxf_097_log_spread_zscore_252d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_097_log_spread_zscore_252d_ema12_26_d2},
    "f13_mcxf_098_log_spread_zscore_252d_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_098_log_spread_zscore_252d_ema21_55_d2},
    "f13_mcxf_099_log_spread_zscore_252d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_099_log_spread_zscore_252d_ema50_200_d2},
    "f13_mcxf_100_log_spread_zscore_252d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_100_log_spread_zscore_252d_sma20_50_d2},
    "f13_mcxf_101_log_spread_zscore_252d_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_101_log_spread_zscore_252d_hma50_200_d2},
    "f13_mcxf_102_log_spread_zscore_252d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_102_log_spread_zscore_252d_close_sma200_d2},
    "f13_mcxf_103_sign_of_fast_minus_slow_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_103_sign_of_fast_minus_slow_sma50_200_d2},
    "f13_mcxf_104_sign_of_fast_minus_slow_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_104_sign_of_fast_minus_slow_ema12_26_d2},
    "f13_mcxf_105_sign_of_fast_minus_slow_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_105_sign_of_fast_minus_slow_ema21_55_d2},
    "f13_mcxf_106_sign_of_fast_minus_slow_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_106_sign_of_fast_minus_slow_ema50_200_d2},
    "f13_mcxf_107_sign_of_fast_minus_slow_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_107_sign_of_fast_minus_slow_sma20_50_d2},
    "f13_mcxf_108_sign_of_fast_minus_slow_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_108_sign_of_fast_minus_slow_hma50_200_d2},
    "f13_mcxf_109_sign_of_fast_minus_slow_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_109_sign_of_fast_minus_slow_close_sma200_d2},
    "f13_mcxf_110_recross_within_5d_count_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_110_recross_within_5d_count_sma50_200_d2},
    "f13_mcxf_111_recross_within_5d_count_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_111_recross_within_5d_count_ema12_26_d2},
    "f13_mcxf_112_recross_within_5d_count_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_112_recross_within_5d_count_ema9_21_d2},
    "f13_mcxf_113_recross_within_5d_count_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_113_recross_within_5d_count_ema21_55_d2},
    "f13_mcxf_114_recross_within_5d_count_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_114_recross_within_5d_count_ema50_200_d2},
    "f13_mcxf_115_recross_within_5d_count_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_115_recross_within_5d_count_close_sma200_d2},
    "f13_mcxf_116_recross_within_21d_count_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_116_recross_within_21d_count_sma50_200_d2},
    "f13_mcxf_117_recross_within_21d_count_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_117_recross_within_21d_count_ema12_26_d2},
    "f13_mcxf_118_recross_within_21d_count_ema9_21_d2": {"inputs": ["close"], "func": f13_mcxf_118_recross_within_21d_count_ema9_21_d2},
    "f13_mcxf_119_recross_within_21d_count_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_119_recross_within_21d_count_ema21_55_d2},
    "f13_mcxf_120_recross_within_21d_count_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_120_recross_within_21d_count_ema50_200_d2},
    "f13_mcxf_121_recross_within_21d_count_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_121_recross_within_21d_count_close_sma200_d2},
    "f13_mcxf_122_bars_since_cross_over_mean_cycle_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_122_bars_since_cross_over_mean_cycle_252d_sma50_200_d2},
    "f13_mcxf_123_bars_since_cross_over_mean_cycle_252d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_123_bars_since_cross_over_mean_cycle_252d_ema12_26_d2},
    "f13_mcxf_124_bars_since_cross_over_mean_cycle_252d_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_124_bars_since_cross_over_mean_cycle_252d_ema21_55_d2},
    "f13_mcxf_125_bars_since_cross_over_mean_cycle_252d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_125_bars_since_cross_over_mean_cycle_252d_ema50_200_d2},
    "f13_mcxf_126_bars_since_cross_over_mean_cycle_252d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_126_bars_since_cross_over_mean_cycle_252d_sma20_50_d2},
    "f13_mcxf_127_bars_since_cross_over_mean_cycle_252d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_127_bars_since_cross_over_mean_cycle_252d_close_sma200_d2},
    "f13_mcxf_128_joint_signed_cross_event_sma50_200_AND_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_128_joint_signed_cross_event_sma50_200_AND_ema50_200_d2},
    "f13_mcxf_129_joint_signed_cross_event_sma50_200_AND_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_129_joint_signed_cross_event_sma50_200_AND_ema12_26_d2},
    "f13_mcxf_130_joint_signed_cross_event_close_sma200_AND_close_ema50_d2": {"inputs": ["close"], "func": f13_mcxf_130_joint_signed_cross_event_close_sma200_AND_close_ema50_d2},
    "f13_mcxf_131_joint_signed_cross_event_ema9_21_AND_ema21_55_d2": {"inputs": ["close"], "func": f13_mcxf_131_joint_signed_cross_event_ema9_21_AND_ema21_55_d2},
    "f13_mcxf_132_joint_signed_cross_event_hma50_200_AND_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_132_joint_signed_cross_event_hma50_200_AND_sma50_200_d2},
    "f13_mcxf_133_cross_quality_log_spread_within_21d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_133_cross_quality_log_spread_within_21d_sma50_200_d2},
    "f13_mcxf_134_cross_quality_log_spread_within_21d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_134_cross_quality_log_spread_within_21d_ema12_26_d2},
    "f13_mcxf_135_cross_quality_log_spread_within_21d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_135_cross_quality_log_spread_within_21d_ema50_200_d2},
    "f13_mcxf_136_cross_quality_log_spread_within_21d_sma20_50_d2": {"inputs": ["close"], "func": f13_mcxf_136_cross_quality_log_spread_within_21d_sma20_50_d2},
    "f13_mcxf_137_cross_quality_log_spread_within_21d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_137_cross_quality_log_spread_within_21d_close_sma200_d2},
    "f13_mcxf_138_slow_ma_slope_at_cross_63d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_138_slow_ma_slope_at_cross_63d_sma50_200_d2},
    "f13_mcxf_139_slow_ma_slope_at_cross_63d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_139_slow_ma_slope_at_cross_63d_ema12_26_d2},
    "f13_mcxf_140_slow_ma_slope_at_cross_63d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_140_slow_ma_slope_at_cross_63d_ema50_200_d2},
    "f13_mcxf_141_slow_ma_slope_at_cross_63d_hma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_141_slow_ma_slope_at_cross_63d_hma50_200_d2},
    "f13_mcxf_142_slow_ma_slope_at_cross_63d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_142_slow_ma_slope_at_cross_63d_close_sma200_d2},
    "f13_mcxf_143_golden_minus_death_count_252d_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_143_golden_minus_death_count_252d_sma50_200_d2},
    "f13_mcxf_144_golden_minus_death_count_252d_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_144_golden_minus_death_count_252d_ema12_26_d2},
    "f13_mcxf_145_golden_minus_death_count_252d_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_145_golden_minus_death_count_252d_ema50_200_d2},
    "f13_mcxf_146_golden_minus_death_count_252d_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_146_golden_minus_death_count_252d_close_sma200_d2},
    "f13_mcxf_147_last_cross_was_golden_indicator_sma50_200_d2": {"inputs": ["close"], "func": f13_mcxf_147_last_cross_was_golden_indicator_sma50_200_d2},
    "f13_mcxf_148_last_cross_was_golden_indicator_ema50_200_d2": {"inputs": ["close"], "func": f13_mcxf_148_last_cross_was_golden_indicator_ema50_200_d2},
    "f13_mcxf_149_last_cross_was_golden_indicator_close_sma200_d2": {"inputs": ["close"], "func": f13_mcxf_149_last_cross_was_golden_indicator_close_sma200_d2},
    "f13_mcxf_150_last_cross_was_golden_indicator_ema12_26_d2": {"inputs": ["close"], "func": f13_mcxf_150_last_cross_was_golden_indicator_ema12_26_d2},
}
