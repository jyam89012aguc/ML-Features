"""sma_ema_extension_dynamics d2 features 076-150 - Pipeline 1b-technical.

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


def f11_smae_076_days_since_last_cross_close_hma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - HMA50)."""
    ma = _hma(close, 50)
    days = _days_since_last_cross(close, ma)
    return (days).diff().diff()

def f11_smae_077_days_since_last_cross_close_dema50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - DEMA50)."""
    ma = _dema(close, 50)
    days = _days_since_last_cross(close, ma)
    return (days).diff().diff()

def f11_smae_078_days_since_last_cross_close_lsma50_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - LSMA50)."""
    ma = _lsma(close, 50)
    days = _days_since_last_cross(close, ma)
    return (days).diff().diff()

def f11_smae_079_days_since_last_cross_close_kama_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - KAMA)."""
    ma = _kama(close, 10)
    days = _days_since_last_cross(close, ma)
    return (days).diff().diff()

def f11_smae_080_slope_log_sma50_21d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of SMA50 over recent MDAYS window - trend velocity."""
    ma = _sma(close, 50)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, MDAYS)).diff().diff()

def f11_smae_081_slope_log_sma200_63d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of SMA200 over recent QDAYS window - trend velocity."""
    ma = _sma(close, 200)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, QDAYS)).diff().diff()

def f11_smae_082_slope_log_ema50_21d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of EMA50 over recent MDAYS window - trend velocity."""
    ma = _ema(close, 50)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, MDAYS)).diff().diff()

def f11_smae_083_slope_log_ema200_63d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of EMA200 over recent QDAYS window - trend velocity."""
    ma = _ema(close, 200)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, QDAYS)).diff().diff()

def f11_smae_084_slope_log_hma50_21d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of HMA50 over recent MDAYS window - trend velocity."""
    ma = _hma(close, 50)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, MDAYS)).diff().diff()

def f11_smae_085_slope_log_kama_21d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of KAMA over recent MDAYS window - trend velocity."""
    ma = _kama(close, 10)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, MDAYS)).diff().diff()

def f11_smae_086_slope_log_lsma200_63d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of LSMA200 over recent QDAYS window - trend velocity."""
    ma = _lsma(close, 200)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, QDAYS)).diff().diff()

def f11_smae_087_slope_log_tema50_21d_d2(close: pd.Series) -> pd.Series:
    """Per-bar log-slope of TEMA50 over recent MDAYS window - trend velocity."""
    ma = _tema(close, 50)
    lma = _safe_log(ma)
    return (_rolling_slope(lma, MDAYS)).diff().diff()

def f11_smae_088_curvature_log_sma50_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-SMA50 - trend acceleration (positive = curving up)."""
    ma = _sma(close, 50)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_089_curvature_log_ema50_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-EMA50 - trend acceleration (positive = curving up)."""
    ma = _ema(close, 50)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_090_curvature_log_hma50_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-HMA50 - trend acceleration (positive = curving up)."""
    ma = _hma(close, 50)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_091_curvature_log_dema50_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-DEMA50 - trend acceleration (positive = curving up)."""
    ma = _dema(close, 50)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_092_curvature_log_tema50_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-TEMA50 - trend acceleration (positive = curving up)."""
    ma = _tema(close, 50)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_093_curvature_log_sma200_2nddiff_d2(close: pd.Series) -> pd.Series:
    """Second difference of log-SMA200 - trend acceleration (positive = curving up)."""
    ma = _sma(close, 200)
    lma = _safe_log(ma)
    return (lma.diff().diff()).diff().diff()

def f11_smae_094_consecutive_bars_close_above_sma50_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > SMA50."""
    ma = _sma(close, 50)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_095_consecutive_bars_close_above_sma200_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > SMA200."""
    ma = _sma(close, 200)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_096_consecutive_bars_close_above_ema50_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > EMA50."""
    ma = _ema(close, 50)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_097_consecutive_bars_close_above_ema200_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > EMA200."""
    ma = _ema(close, 200)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_098_consecutive_bars_close_above_hma50_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > HMA50."""
    ma = _hma(close, 50)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_099_consecutive_bars_close_above_kama_d2(close: pd.Series) -> pd.Series:
    """Current run-length of consecutive bars with close > KAMA."""
    ma = _kama(close, 10)
    above = (close > ma).where(ma.notna(), np.nan)
    return (_consecutive_true_streak(above)).diff().diff()

def f11_smae_100_spread_log_ema20_minus_ema50_d2(close: pd.Series) -> pd.Series:
    """Log-ratio EMA20 over EMA50 - short-vs-medium golden-cross proxy."""
    fast = _ema(close, 20)
    slow = _ema(close, 50)
    return (_safe_log(fast) - _safe_log(slow)).diff().diff()

def f11_smae_101_spread_log_ema50_minus_ema200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio EMA50 over EMA200 - medium-vs-long trend spread."""
    fast = _ema(close, 50)
    slow = _ema(close, 200)
    return (_safe_log(fast) - _safe_log(slow)).diff().diff()

def f11_smae_102_spread_log_sma50_minus_sma200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio SMA50 over SMA200 - classic golden/death-cross proxy."""
    fast = _sma(close, 50)
    slow = _sma(close, 200)
    return (_safe_log(fast) - _safe_log(slow)).diff().diff()

def f11_smae_103_spread_log_hma20_minus_hma200_d2(close: pd.Series) -> pd.Series:
    """Log-ratio HMA20 over HMA200 - responsive fast vs slow Hull spread."""
    fast = _hma(close, 20)
    slow = _hma(close, 200)
    return (_safe_log(fast) - _safe_log(slow)).diff().diff()

def f11_smae_104_upside_semi_dist_above_sma50_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of positive log-distance above SMA50 over 252d - upside extension intensity."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    pos = dist.where(dist > 0, np.nan)
    return (pos.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f11_smae_105_downside_semi_dist_below_sma50_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of negative log-distance below SMA50 over 252d - downside excursion intensity."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    neg = dist.where(dist < 0, np.nan)
    return (neg.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f11_smae_106_up_down_ratio_dist_from_sma50_252d_d2(close: pd.Series) -> pd.Series:
    """Ratio of upside-semi to |downside-semi| log-distance vs SMA50 over 252d."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    up = dist.where(dist > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = (-dist.where(dist < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(up, dn)).diff().diff()

def f11_smae_107_up_down_ratio_dist_from_ema50_252d_d2(close: pd.Series) -> pd.Series:
    """Same up/down ratio computed against EMA50 baseline."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    up = dist.where(dist > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = (-dist.where(dist < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(up, dn)).diff().diff()

def f11_smae_108_composite_signed_log_dist_sma_short_med_long_d2(close: pd.Series) -> pd.Series:
    """Sum of log-distance above SMA21+50+200 - multi-horizon composite extension."""
    m21 = _sma(close, MDAYS)
    m50 = _sma(close, 50)
    m200 = _sma(close, 200)
    lc = _safe_log(close)
    return ((lc - _safe_log(m21)) + (lc - _safe_log(m50)) + (lc - _safe_log(m200))).diff().diff()

def f11_smae_109_composite_signed_log_dist_ema_short_med_long_d2(close: pd.Series) -> pd.Series:
    """Sum of log-distance above EMA21+50+200 - multi-horizon composite extension."""
    m21 = _ema(close, MDAYS)
    m50 = _ema(close, 50)
    m200 = _ema(close, 200)
    lc = _safe_log(close)
    return ((lc - _safe_log(m21)) + (lc - _safe_log(m50)) + (lc - _safe_log(m200))).diff().diff()

def f11_smae_110_composite_signed_log_dist_hma_short_med_long_d2(close: pd.Series) -> pd.Series:
    """Sum of log-distance above HMA21+50+200 - multi-horizon composite extension."""
    m21 = _hma(close, MDAYS)
    m50 = _hma(close, 50)
    m200 = _hma(close, 200)
    lc = _safe_log(close)
    return ((lc - _safe_log(m21)) + (lc - _safe_log(m50)) + (lc - _safe_log(m200))).diff().diff()

def f11_smae_111_composite_signed_log_dist_dema_short_med_long_d2(close: pd.Series) -> pd.Series:
    """Sum of log-distance above DEMA21+50+200 - multi-horizon composite extension."""
    m21 = _dema(close, MDAYS)
    m50 = _dema(close, 50)
    m200 = _dema(close, 200)
    lc = _safe_log(close)
    return ((lc - _safe_log(m21)) + (lc - _safe_log(m50)) + (lc - _safe_log(m200))).diff().diff()

def f11_smae_112_dist_to_volofdist_ratio_sma50_63d_d2(close: pd.Series) -> pd.Series:
    """Distance from SMA50 divided by 63d std of that distance - stability of extension."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    vol = dist.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(dist, vol)).diff().diff()

def f11_smae_113_dist_to_volofdist_ratio_ema50_63d_d2(close: pd.Series) -> pd.Series:
    """Distance from EMA50 divided by 63d std of that distance - stability of extension."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    vol = dist.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(dist, vol)).diff().diff()

def f11_smae_114_dist_to_volofdist_ratio_hma50_63d_d2(close: pd.Series) -> pd.Series:
    """Distance from HMA50 divided by 63d std of that distance - stability of extension."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    vol = dist.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(dist, vol)).diff().diff()

def f11_smae_115_dist_to_volofdist_ratio_dema50_63d_d2(close: pd.Series) -> pd.Series:
    """Distance from DEMA50 divided by 63d std of that distance - stability of extension."""
    ma = _dema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    vol = dist.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(dist, vol)).diff().diff()

def f11_smae_116_ewma_decay_dist_sma50_21span_d2(close: pd.Series) -> pd.Series:
    """EWMA(span=21) of log-distance from SMA50 - smoothed extension trajectory."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    smoothed = dist.ewm(span=21, adjust=False, min_periods=5).mean()
    return (smoothed).diff().diff()

def f11_smae_117_ewma_decay_dist_ema50_21span_d2(close: pd.Series) -> pd.Series:
    """EWMA(span=21) of log-distance from EMA50 - smoothed extension trajectory."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    smoothed = dist.ewm(span=21, adjust=False, min_periods=5).mean()
    return (smoothed).diff().diff()

def f11_smae_118_ewma_decay_dist_hma50_21span_d2(close: pd.Series) -> pd.Series:
    """EWMA(span=21) of log-distance from HMA50 - smoothed extension trajectory."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    smoothed = dist.ewm(span=21, adjust=False, min_periods=5).mean()
    return (smoothed).diff().diff()

def f11_smae_119_ewma_decay_dist_dema50_21span_d2(close: pd.Series) -> pd.Series:
    """EWMA(span=21) of log-distance from DEMA50 - smoothed extension trajectory."""
    ma = _dema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    smoothed = dist.ewm(span=21, adjust=False, min_periods=5).mean()
    return (smoothed).diff().diff()

def f11_smae_120_atr21_when_topquintile_dist_sma50_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21/close when distance above SMA50 is in top 20% of 252d distribution - vol-crush-at-top."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    rank = dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_norm = _safe_div(atr21, close)
    return (atr_norm.where(rank >= 0.80, np.nan)).diff().diff()

def f11_smae_121_atr21_when_topquintile_dist_ema50_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21/close when distance above EMA50 is in top 20% of 252d distribution - vol-crush-at-top."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    rank = dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_norm = _safe_div(atr21, close)
    return (atr_norm.where(rank >= 0.80, np.nan)).diff().diff()

def f11_smae_122_atr21_when_topquintile_dist_hma50_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21/close when distance above HMA50 is in top 20% of 252d distribution - vol-crush-at-top."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    rank = dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_norm = _safe_div(atr21, close)
    return (atr_norm.where(rank >= 0.80, np.nan)).diff().diff()

def f11_smae_123_atr21_when_topquintile_dist_dema50_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21/close when distance above DEMA50 is in top 20% of 252d distribution - vol-crush-at-top."""
    ma = _dema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    rank = dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    atr21 = _atr(high, low, close, n=MDAYS)
    atr_norm = _safe_div(atr21, close)
    return (atr_norm.where(rank >= 0.80, np.nan)).diff().diff()

def f11_smae_124_robust_mad_zscore_dist_sma50_252d_d2(close: pd.Series) -> pd.Series:
    """Robust (median-MAD) z-score of log-distance from SMA50 over 252d."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    med = dist.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (dist - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(dist - med, 1.4826 * mad)).diff().diff()

def f11_smae_125_robust_mad_zscore_dist_ema50_252d_d2(close: pd.Series) -> pd.Series:
    """Robust (median-MAD) z-score of log-distance from EMA50 over 252d."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    med = dist.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (dist - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(dist - med, 1.4826 * mad)).diff().diff()

def f11_smae_126_robust_mad_zscore_dist_hma50_252d_d2(close: pd.Series) -> pd.Series:
    """Robust (median-MAD) z-score of log-distance from HMA50 over 252d."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    med = dist.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (dist - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(dist - med, 1.4826 * mad)).diff().diff()

def f11_smae_127_robust_mad_zscore_dist_kama_252d_d2(close: pd.Series) -> pd.Series:
    """Robust (median-MAD) z-score of log-distance from KAMA over 252d."""
    ma = _kama(close, 10)
    dist = _safe_log(close) - _safe_log(ma)
    med = dist.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (dist - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return (_safe_div(dist - med, 1.4826 * mad)).diff().diff()

def f11_smae_128_count_close_sma50_crossings_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of close-vs-SMA50 sign-flips - chop intensity."""
    ma = _sma(close, 50)
    return (_count_crosses(close, ma, QDAYS)).diff().diff()

def f11_smae_129_count_close_ema50_crossings_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of close-vs-EMA50 sign-flips - chop intensity."""
    ma = _ema(close, 50)
    return (_count_crosses(close, ma, QDAYS)).diff().diff()

def f11_smae_130_count_close_hma50_crossings_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of close-vs-HMA50 sign-flips - chop intensity."""
    ma = _hma(close, 50)
    return (_count_crosses(close, ma, QDAYS)).diff().diff()

def f11_smae_131_count_close_kama_crossings_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling 63d count of close-vs-KAMA sign-flips - chop intensity."""
    ma = _kama(close, 10)
    return (_count_crosses(close, ma, QDAYS)).diff().diff()

def f11_smae_132_residual_std_log_close_vs_sma50_252d_d2(close: pd.Series) -> pd.Series:
    """252d std of log-residual from SMA50 - extension volatility."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f11_smae_133_residual_std_log_close_vs_ema50_252d_d2(close: pd.Series) -> pd.Series:
    """252d std of log-residual from EMA50 - extension volatility."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f11_smae_134_residual_std_log_close_vs_hma50_252d_d2(close: pd.Series) -> pd.Series:
    """252d std of log-residual from HMA50 - extension volatility."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f11_smae_135_residual_std_log_close_vs_lsma50_252d_d2(close: pd.Series) -> pd.Series:
    """252d std of log-residual from LSMA50 - extension volatility."""
    ma = _lsma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f11_smae_136_max_log_dist_above_sma50_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling-max of log-distance above SMA50 over QDAYS - peak extension captured."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).max()).diff().diff()

def f11_smae_137_max_log_dist_above_ema50_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling-max of log-distance above EMA50 over QDAYS - peak extension captured."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).max()).diff().diff()

def f11_smae_138_max_log_dist_above_hma50_63d_d2(close: pd.Series) -> pd.Series:
    """Rolling-max of log-distance above HMA50 over QDAYS - peak extension captured."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).max()).diff().diff()

def f11_smae_139_max_log_dist_above_sma200_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling-max of log-distance above SMA200 over YDAYS - peak extension captured."""
    ma = _sma(close, 200)
    dist = _safe_log(close) - _safe_log(ma)
    return (dist.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).max()).diff().diff()

def f11_smae_140_range_normalized_dist_above_sma50_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance above SMA50 divided by 252d high-low range - extension as fraction of full range."""
    ma = _sma(close, 50)
    rng = high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - ma, rng)).diff().diff()

def f11_smae_141_range_normalized_dist_above_ema50_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance above EMA50 divided by 252d high-low range."""
    ma = _ema(close, 50)
    rng = high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - ma, rng)).diff().diff()

def f11_smae_142_range_normalized_dist_above_hma50_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Distance above HMA50 divided by 252d high-low range."""
    ma = _hma(close, 50)
    rng = high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - ma, rng)).diff().diff()

def f11_smae_143_log_dist_above_avg_sma_ema_50_d2(close: pd.Series) -> pd.Series:
    """Log distance above the simple average of SMA50 and EMA50 - consensus MA extension."""
    s = _sma(close, 50)
    e = _ema(close, 50)
    ma = (s + e) / 2.0
    return (_safe_log(close) - _safe_log(ma)).diff().diff()

def f11_smae_144_log_dist_above_avg_sma_ema_hma_50_d2(close: pd.Series) -> pd.Series:
    """Log distance above the average of SMA50, EMA50, HMA50 - three-way consensus extension."""
    s = _sma(close, 50)
    e = _ema(close, 50)
    h = _hma(close, 50)
    ma = (s + e + h) / 3.0
    return (_safe_log(close) - _safe_log(ma)).diff().diff()

def f11_smae_145_signed_count_above_all_three_consensus_50_d2(close: pd.Series) -> pd.Series:
    """Signed indicator: +1 if close above all three (SMA50,EMA50,HMA50), -1 if below all, else 0."""
    s = _sma(close, 50)
    e = _ema(close, 50)
    h = _hma(close, 50)
    above = ((close > s) & (close > e) & (close > h)).astype(float)
    below = ((close < s) & (close < e) & (close < h)).astype(float)
    valid = s.notna() & e.notna() & h.notna()
    sig = (above - below).where(valid, np.nan)
    return (sig).diff().diff()

def f11_smae_146_log_dist_above_ewma_alpha_002_d2(close: pd.Series) -> pd.Series:
    """Log dist above EWMA(alpha=0.02) - very-slow-decay smoothed close."""
    ma = close.ewm(alpha=0.02, adjust=False, min_periods=21).mean()
    return (_safe_log(close) - _safe_log(ma)).diff().diff()

def f11_smae_147_log_dist_above_ewma_alpha_01_d2(close: pd.Series) -> pd.Series:
    """Log dist above EWMA(alpha=0.10) - medium-decay smoothed close."""
    ma = close.ewm(alpha=0.10, adjust=False, min_periods=10).mean()
    return (_safe_log(close) - _safe_log(ma)).diff().diff()

def f11_smae_148_log_dist_above_ewma_alpha_30_d2(close: pd.Series) -> pd.Series:
    """Log dist above EWMA(alpha=0.30) - fast-decay smoothed close."""
    ma = close.ewm(alpha=0.30, adjust=False, min_periods=5).mean()
    return (_safe_log(close) - _safe_log(ma)).diff().diff()

def f11_smae_149_ratio_close_to_sma50_minus_one_d2(close: pd.Series) -> pd.Series:
    """Simple percentage above SMA50 (close/SMA50 - 1) - linear-units extension."""
    ma = _sma(close, 50)
    return (_safe_div(close - ma, ma)).diff().diff()

def f11_smae_150_ratio_close_to_sma200_minus_one_long_d2(close: pd.Series) -> pd.Series:
    """Simple percentage above SMA200 (close/SMA200 - 1) - long-term linear-units extension."""
    ma = _sma(close, 200)
    return (_safe_div(close - ma, ma)).diff().diff()


# ============================================================
#                         REGISTRY 076_150 (d2)
# ============================================================

SMA_EMA_EXTENSION_DYNAMICS_D2_REGISTRY_076_150 = {
    "f11_smae_076_days_since_last_cross_close_hma50_d2": {"inputs": ["close"], "func": f11_smae_076_days_since_last_cross_close_hma50_d2},
    "f11_smae_077_days_since_last_cross_close_dema50_d2": {"inputs": ["close"], "func": f11_smae_077_days_since_last_cross_close_dema50_d2},
    "f11_smae_078_days_since_last_cross_close_lsma50_d2": {"inputs": ["close"], "func": f11_smae_078_days_since_last_cross_close_lsma50_d2},
    "f11_smae_079_days_since_last_cross_close_kama_d2": {"inputs": ["close"], "func": f11_smae_079_days_since_last_cross_close_kama_d2},
    "f11_smae_080_slope_log_sma50_21d_d2": {"inputs": ["close"], "func": f11_smae_080_slope_log_sma50_21d_d2},
    "f11_smae_081_slope_log_sma200_63d_d2": {"inputs": ["close"], "func": f11_smae_081_slope_log_sma200_63d_d2},
    "f11_smae_082_slope_log_ema50_21d_d2": {"inputs": ["close"], "func": f11_smae_082_slope_log_ema50_21d_d2},
    "f11_smae_083_slope_log_ema200_63d_d2": {"inputs": ["close"], "func": f11_smae_083_slope_log_ema200_63d_d2},
    "f11_smae_084_slope_log_hma50_21d_d2": {"inputs": ["close"], "func": f11_smae_084_slope_log_hma50_21d_d2},
    "f11_smae_085_slope_log_kama_21d_d2": {"inputs": ["close"], "func": f11_smae_085_slope_log_kama_21d_d2},
    "f11_smae_086_slope_log_lsma200_63d_d2": {"inputs": ["close"], "func": f11_smae_086_slope_log_lsma200_63d_d2},
    "f11_smae_087_slope_log_tema50_21d_d2": {"inputs": ["close"], "func": f11_smae_087_slope_log_tema50_21d_d2},
    "f11_smae_088_curvature_log_sma50_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_088_curvature_log_sma50_2nddiff_d2},
    "f11_smae_089_curvature_log_ema50_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_089_curvature_log_ema50_2nddiff_d2},
    "f11_smae_090_curvature_log_hma50_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_090_curvature_log_hma50_2nddiff_d2},
    "f11_smae_091_curvature_log_dema50_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_091_curvature_log_dema50_2nddiff_d2},
    "f11_smae_092_curvature_log_tema50_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_092_curvature_log_tema50_2nddiff_d2},
    "f11_smae_093_curvature_log_sma200_2nddiff_d2": {"inputs": ["close"], "func": f11_smae_093_curvature_log_sma200_2nddiff_d2},
    "f11_smae_094_consecutive_bars_close_above_sma50_d2": {"inputs": ["close"], "func": f11_smae_094_consecutive_bars_close_above_sma50_d2},
    "f11_smae_095_consecutive_bars_close_above_sma200_d2": {"inputs": ["close"], "func": f11_smae_095_consecutive_bars_close_above_sma200_d2},
    "f11_smae_096_consecutive_bars_close_above_ema50_d2": {"inputs": ["close"], "func": f11_smae_096_consecutive_bars_close_above_ema50_d2},
    "f11_smae_097_consecutive_bars_close_above_ema200_d2": {"inputs": ["close"], "func": f11_smae_097_consecutive_bars_close_above_ema200_d2},
    "f11_smae_098_consecutive_bars_close_above_hma50_d2": {"inputs": ["close"], "func": f11_smae_098_consecutive_bars_close_above_hma50_d2},
    "f11_smae_099_consecutive_bars_close_above_kama_d2": {"inputs": ["close"], "func": f11_smae_099_consecutive_bars_close_above_kama_d2},
    "f11_smae_100_spread_log_ema20_minus_ema50_d2": {"inputs": ["close"], "func": f11_smae_100_spread_log_ema20_minus_ema50_d2},
    "f11_smae_101_spread_log_ema50_minus_ema200_d2": {"inputs": ["close"], "func": f11_smae_101_spread_log_ema50_minus_ema200_d2},
    "f11_smae_102_spread_log_sma50_minus_sma200_d2": {"inputs": ["close"], "func": f11_smae_102_spread_log_sma50_minus_sma200_d2},
    "f11_smae_103_spread_log_hma20_minus_hma200_d2": {"inputs": ["close"], "func": f11_smae_103_spread_log_hma20_minus_hma200_d2},
    "f11_smae_104_upside_semi_dist_above_sma50_252d_d2": {"inputs": ["close"], "func": f11_smae_104_upside_semi_dist_above_sma50_252d_d2},
    "f11_smae_105_downside_semi_dist_below_sma50_252d_d2": {"inputs": ["close"], "func": f11_smae_105_downside_semi_dist_below_sma50_252d_d2},
    "f11_smae_106_up_down_ratio_dist_from_sma50_252d_d2": {"inputs": ["close"], "func": f11_smae_106_up_down_ratio_dist_from_sma50_252d_d2},
    "f11_smae_107_up_down_ratio_dist_from_ema50_252d_d2": {"inputs": ["close"], "func": f11_smae_107_up_down_ratio_dist_from_ema50_252d_d2},
    "f11_smae_108_composite_signed_log_dist_sma_short_med_long_d2": {"inputs": ["close"], "func": f11_smae_108_composite_signed_log_dist_sma_short_med_long_d2},
    "f11_smae_109_composite_signed_log_dist_ema_short_med_long_d2": {"inputs": ["close"], "func": f11_smae_109_composite_signed_log_dist_ema_short_med_long_d2},
    "f11_smae_110_composite_signed_log_dist_hma_short_med_long_d2": {"inputs": ["close"], "func": f11_smae_110_composite_signed_log_dist_hma_short_med_long_d2},
    "f11_smae_111_composite_signed_log_dist_dema_short_med_long_d2": {"inputs": ["close"], "func": f11_smae_111_composite_signed_log_dist_dema_short_med_long_d2},
    "f11_smae_112_dist_to_volofdist_ratio_sma50_63d_d2": {"inputs": ["close"], "func": f11_smae_112_dist_to_volofdist_ratio_sma50_63d_d2},
    "f11_smae_113_dist_to_volofdist_ratio_ema50_63d_d2": {"inputs": ["close"], "func": f11_smae_113_dist_to_volofdist_ratio_ema50_63d_d2},
    "f11_smae_114_dist_to_volofdist_ratio_hma50_63d_d2": {"inputs": ["close"], "func": f11_smae_114_dist_to_volofdist_ratio_hma50_63d_d2},
    "f11_smae_115_dist_to_volofdist_ratio_dema50_63d_d2": {"inputs": ["close"], "func": f11_smae_115_dist_to_volofdist_ratio_dema50_63d_d2},
    "f11_smae_116_ewma_decay_dist_sma50_21span_d2": {"inputs": ["close"], "func": f11_smae_116_ewma_decay_dist_sma50_21span_d2},
    "f11_smae_117_ewma_decay_dist_ema50_21span_d2": {"inputs": ["close"], "func": f11_smae_117_ewma_decay_dist_ema50_21span_d2},
    "f11_smae_118_ewma_decay_dist_hma50_21span_d2": {"inputs": ["close"], "func": f11_smae_118_ewma_decay_dist_hma50_21span_d2},
    "f11_smae_119_ewma_decay_dist_dema50_21span_d2": {"inputs": ["close"], "func": f11_smae_119_ewma_decay_dist_dema50_21span_d2},
    "f11_smae_120_atr21_when_topquintile_dist_sma50_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_120_atr21_when_topquintile_dist_sma50_d2},
    "f11_smae_121_atr21_when_topquintile_dist_ema50_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_121_atr21_when_topquintile_dist_ema50_d2},
    "f11_smae_122_atr21_when_topquintile_dist_hma50_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_122_atr21_when_topquintile_dist_hma50_d2},
    "f11_smae_123_atr21_when_topquintile_dist_dema50_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_123_atr21_when_topquintile_dist_dema50_d2},
    "f11_smae_124_robust_mad_zscore_dist_sma50_252d_d2": {"inputs": ["close"], "func": f11_smae_124_robust_mad_zscore_dist_sma50_252d_d2},
    "f11_smae_125_robust_mad_zscore_dist_ema50_252d_d2": {"inputs": ["close"], "func": f11_smae_125_robust_mad_zscore_dist_ema50_252d_d2},
    "f11_smae_126_robust_mad_zscore_dist_hma50_252d_d2": {"inputs": ["close"], "func": f11_smae_126_robust_mad_zscore_dist_hma50_252d_d2},
    "f11_smae_127_robust_mad_zscore_dist_kama_252d_d2": {"inputs": ["close"], "func": f11_smae_127_robust_mad_zscore_dist_kama_252d_d2},
    "f11_smae_128_count_close_sma50_crossings_63d_d2": {"inputs": ["close"], "func": f11_smae_128_count_close_sma50_crossings_63d_d2},
    "f11_smae_129_count_close_ema50_crossings_63d_d2": {"inputs": ["close"], "func": f11_smae_129_count_close_ema50_crossings_63d_d2},
    "f11_smae_130_count_close_hma50_crossings_63d_d2": {"inputs": ["close"], "func": f11_smae_130_count_close_hma50_crossings_63d_d2},
    "f11_smae_131_count_close_kama_crossings_63d_d2": {"inputs": ["close"], "func": f11_smae_131_count_close_kama_crossings_63d_d2},
    "f11_smae_132_residual_std_log_close_vs_sma50_252d_d2": {"inputs": ["close"], "func": f11_smae_132_residual_std_log_close_vs_sma50_252d_d2},
    "f11_smae_133_residual_std_log_close_vs_ema50_252d_d2": {"inputs": ["close"], "func": f11_smae_133_residual_std_log_close_vs_ema50_252d_d2},
    "f11_smae_134_residual_std_log_close_vs_hma50_252d_d2": {"inputs": ["close"], "func": f11_smae_134_residual_std_log_close_vs_hma50_252d_d2},
    "f11_smae_135_residual_std_log_close_vs_lsma50_252d_d2": {"inputs": ["close"], "func": f11_smae_135_residual_std_log_close_vs_lsma50_252d_d2},
    "f11_smae_136_max_log_dist_above_sma50_63d_d2": {"inputs": ["close"], "func": f11_smae_136_max_log_dist_above_sma50_63d_d2},
    "f11_smae_137_max_log_dist_above_ema50_63d_d2": {"inputs": ["close"], "func": f11_smae_137_max_log_dist_above_ema50_63d_d2},
    "f11_smae_138_max_log_dist_above_hma50_63d_d2": {"inputs": ["close"], "func": f11_smae_138_max_log_dist_above_hma50_63d_d2},
    "f11_smae_139_max_log_dist_above_sma200_252d_d2": {"inputs": ["close"], "func": f11_smae_139_max_log_dist_above_sma200_252d_d2},
    "f11_smae_140_range_normalized_dist_above_sma50_252d_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_140_range_normalized_dist_above_sma50_252d_d2},
    "f11_smae_141_range_normalized_dist_above_ema50_252d_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_141_range_normalized_dist_above_ema50_252d_d2},
    "f11_smae_142_range_normalized_dist_above_hma50_252d_d2": {"inputs": ["high", "low", "close"], "func": f11_smae_142_range_normalized_dist_above_hma50_252d_d2},
    "f11_smae_143_log_dist_above_avg_sma_ema_50_d2": {"inputs": ["close"], "func": f11_smae_143_log_dist_above_avg_sma_ema_50_d2},
    "f11_smae_144_log_dist_above_avg_sma_ema_hma_50_d2": {"inputs": ["close"], "func": f11_smae_144_log_dist_above_avg_sma_ema_hma_50_d2},
    "f11_smae_145_signed_count_above_all_three_consensus_50_d2": {"inputs": ["close"], "func": f11_smae_145_signed_count_above_all_three_consensus_50_d2},
    "f11_smae_146_log_dist_above_ewma_alpha_002_d2": {"inputs": ["close"], "func": f11_smae_146_log_dist_above_ewma_alpha_002_d2},
    "f11_smae_147_log_dist_above_ewma_alpha_01_d2": {"inputs": ["close"], "func": f11_smae_147_log_dist_above_ewma_alpha_01_d2},
    "f11_smae_148_log_dist_above_ewma_alpha_30_d2": {"inputs": ["close"], "func": f11_smae_148_log_dist_above_ewma_alpha_30_d2},
    "f11_smae_149_ratio_close_to_sma50_minus_one_d2": {"inputs": ["close"], "func": f11_smae_149_ratio_close_to_sma50_minus_one_d2},
    "f11_smae_150_ratio_close_to_sma200_minus_one_long_d2": {"inputs": ["close"], "func": f11_smae_150_ratio_close_to_sma200_minus_one_long_d2},
}
