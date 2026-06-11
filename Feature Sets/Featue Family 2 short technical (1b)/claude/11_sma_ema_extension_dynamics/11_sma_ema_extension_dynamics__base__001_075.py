"""sma_ema_extension_dynamics base features 001-075 - Pipeline 1b-technical.

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


def f11_smae_001_log_dist_above_sma50(close: pd.Series) -> pd.Series:
    """Log distance of close above simple MA50 - canonical meso-trend extension."""
    ma = _sma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_002_log_dist_above_ema50(close: pd.Series) -> pd.Series:
    """Log distance above EMA50 - exponential-decay meso-trend extension."""
    ma = _ema(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_003_log_dist_above_dema50(close: pd.Series) -> pd.Series:
    """Log distance above DEMA50 - reduced-lag double-EMA extension."""
    ma = _dema(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_004_log_dist_above_tema50(close: pd.Series) -> pd.Series:
    """Log distance above TEMA50 - triple-EMA further-reduced-lag extension."""
    ma = _tema(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_005_log_dist_above_wma50(close: pd.Series) -> pd.Series:
    """Log distance above linearly-weighted MA50 - recency-emphasized extension."""
    ma = _wma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_006_log_dist_above_hma50(close: pd.Series) -> pd.Series:
    """Log distance above Hull MA50 - low-lag responsive extension."""
    ma = _hma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_007_log_dist_above_kama_default(close: pd.Series) -> pd.Series:
    """Log distance above Kaufman KAMA - adaptive (volatility-aware) extension."""
    ma = _kama(close, 10)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_008_log_dist_above_zlema50(close: pd.Series) -> pd.Series:
    """Log distance above zero-lag EMA50 - de-lagged extension."""
    ma = _zlema(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_009_log_dist_above_smma50(close: pd.Series) -> pd.Series:
    """Log distance above Wilder smoothed MA50 - low-alpha smoothed extension."""
    ma = _smma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_010_log_dist_above_mcginley50(close: pd.Series) -> pd.Series:
    """Log distance above McGinley Dynamic - self-adjusting-length extension."""
    ma = _mcginley(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_011_log_dist_above_lsma50(close: pd.Series) -> pd.Series:
    """Log distance above least-squares regression MA50 - trend-projection extension."""
    ma = _lsma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_012_log_dist_above_alma50(close: pd.Series) -> pd.Series:
    """Log distance above Arnaud Legoux MA50 - Gaussian-weighted recency extension."""
    ma = _alma(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_013_log_dist_above_t3_50(close: pd.Series) -> pd.Series:
    """Log distance above Tillson T3-50 - smoothed low-lag MA extension."""
    ma = _t3(close, 50)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_014_log_dist_above_frama_default(close: pd.Series) -> pd.Series:
    """Log distance above fractal-adaptive MA (Ehlers) - fractal-dim-aware extension."""
    ma = _frama(close, 16)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_015_log_dist_above_sma21_short_trend(close: pd.Series) -> pd.Series:
    """Log distance above SMA21 - monthly/short-trend extension."""
    ma = _sma(close, MDAYS)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_016_log_dist_above_sma100_med_trend(close: pd.Series) -> pd.Series:
    """Log distance above SMA100 - intermediate/distribution-horizon extension."""
    ma = _sma(close, 100)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_017_log_dist_above_sma200_regime(close: pd.Series) -> pd.Series:
    """Log distance above SMA200 - long-term regime extension (classic 200d filter)."""
    ma = _sma(close, 200)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_018_log_dist_above_ema21_short_decay(close: pd.Series) -> pd.Series:
    """Log distance above EMA21 - short-horizon exponential-decay extension."""
    ma = _ema(close, MDAYS)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_019_log_dist_above_ema100_med_decay(close: pd.Series) -> pd.Series:
    """Log distance above EMA100 - intermediate exponential-decay extension."""
    ma = _ema(close, 100)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_020_log_dist_above_ema200_long_decay(close: pd.Series) -> pd.Series:
    """Log distance above EMA200 - long-term exponential-decay extension."""
    ma = _ema(close, 200)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_021_log_dist_above_hma21_responsive_short(close: pd.Series) -> pd.Series:
    """Log distance above HMA21 - low-lag short responsive extension."""
    ma = _hma(close, MDAYS)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_022_log_dist_above_hma100_responsive_med(close: pd.Series) -> pd.Series:
    """Log distance above HMA100 - low-lag medium responsive extension."""
    ma = _hma(close, 100)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_023_log_dist_above_hma200_responsive_long(close: pd.Series) -> pd.Series:
    """Log distance above HMA200 - low-lag long-horizon responsive extension."""
    ma = _hma(close, 200)
    return (_safe_log(close) - _safe_log(ma))

def f11_smae_024_atr21_dist_above_sma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above SMA50 - vol-scaled extension."""
    ma = _sma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_025_atr21_dist_above_ema50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above EMA50 - vol-scaled extension."""
    ma = _ema(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_026_atr21_dist_above_dema50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above DEMA50 - vol-scaled extension."""
    ma = _dema(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_027_atr21_dist_above_tema50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above TEMA50 - vol-scaled extension."""
    ma = _tema(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_028_atr21_dist_above_wma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above WMA50 - vol-scaled extension."""
    ma = _wma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_029_atr21_dist_above_hma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above HMA50 - vol-scaled extension."""
    ma = _hma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_030_atr21_dist_above_kama50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above KAMA50 - vol-scaled extension."""
    ma = _kama(close, 10)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_031_atr21_dist_above_zlema50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above ZLEMA50 - vol-scaled extension."""
    ma = _zlema(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_032_atr21_dist_above_smma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above SMMA50 - vol-scaled extension."""
    ma = _smma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_033_atr21_dist_above_mcginley50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above MCGINLEY50 - vol-scaled extension."""
    ma = _mcginley(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_034_atr21_dist_above_lsma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above LSMA50 - vol-scaled extension."""
    ma = _lsma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_035_atr21_dist_above_alma50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above ALMA50 - vol-scaled extension."""
    ma = _alma(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_036_atr21_dist_above_t350(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above T350 - vol-scaled extension."""
    ma = _t3(close, 50)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_037_atr21_dist_above_frama50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21-normalized distance of close above FRAMA50 - vol-scaled extension."""
    ma = _frama(close, 16)
    atr = _atr(high, low, close, n=MDAYS)
    return (_safe_div(close - ma, atr))

def f11_smae_038_sigma_dist_above_sma50_monthly_sigma(close: pd.Series) -> pd.Series:
    """Distance above SMA50 normalized by monthly sigma of log-returns."""
    ma = _sma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_039_sigma_dist_above_sma50_quarterly_sigma(close: pd.Series) -> pd.Series:
    """Distance above SMA50 normalized by quarterly sigma of log-returns."""
    ma = _sma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_040_sigma_dist_above_sma50_annual_sigma(close: pd.Series) -> pd.Series:
    """Distance above SMA50 normalized by annual sigma of log-returns."""
    ma = _sma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_041_sigma_dist_above_ema50_monthly_sigma(close: pd.Series) -> pd.Series:
    """Distance above EMA50 normalized by monthly sigma of log-returns."""
    ma = _ema(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_042_sigma_dist_above_ema50_quarterly_sigma(close: pd.Series) -> pd.Series:
    """Distance above EMA50 normalized by quarterly sigma of log-returns."""
    ma = _ema(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_043_sigma_dist_above_ema50_annual_sigma(close: pd.Series) -> pd.Series:
    """Distance above EMA50 normalized by annual sigma of log-returns."""
    ma = _ema(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_044_sigma_dist_above_hma50_monthly_sigma(close: pd.Series) -> pd.Series:
    """Distance above HMA50 normalized by monthly sigma of log-returns."""
    ma = _hma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(MDAYS, min_periods=max(MDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_045_sigma_dist_above_hma50_quarterly_sigma(close: pd.Series) -> pd.Series:
    """Distance above HMA50 normalized by quarterly sigma of log-returns."""
    ma = _hma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_046_sigma_dist_above_hma50_annual_sigma(close: pd.Series) -> pd.Series:
    """Distance above HMA50 normalized by annual sigma of log-returns."""
    ma = _hma(close, 50)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).std()
    return (_safe_div(_safe_log(close) - _safe_log(ma), sigma))

def f11_smae_047_zscore_252d_log_dist_above_sma50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above SMA50 - extension anomaly."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_048_zscore_252d_log_dist_above_ema50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above EMA50 - extension anomaly."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_049_zscore_252d_log_dist_above_dema50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above DEMA50 - extension anomaly."""
    ma = _dema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_050_zscore_252d_log_dist_above_tema50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above TEMA50 - extension anomaly."""
    ma = _tema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_051_zscore_252d_log_dist_above_wma50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above WMA50 - extension anomaly."""
    ma = _wma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_052_zscore_252d_log_dist_above_hma50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above HMA50 - extension anomaly."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_053_zscore_252d_log_dist_above_kama(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above KAMA - extension anomaly."""
    ma = _kama(close, 10)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_054_zscore_252d_log_dist_above_lsma50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above LSMA50 - extension anomaly."""
    ma = _lsma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_055_zscore_252d_log_dist_above_alma50(close: pd.Series) -> pd.Series:
    """Z-score (252d window) of log-distance above ALMA50 - extension anomaly."""
    ma = _alma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
    return (_rolling_zscore(dist, YDAYS, min_periods=QDAYS))

def f11_smae_056_pctrank_252d_log_dist_above_sma50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above SMA50."""
    ma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_057_pctrank_252d_log_dist_above_ema50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above EMA50."""
    ma = _ema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_058_pctrank_252d_log_dist_above_dema50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above DEMA50."""
    ma = _dema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_059_pctrank_252d_log_dist_above_tema50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above TEMA50."""
    ma = _tema(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_060_pctrank_252d_log_dist_above_hma50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above HMA50."""
    ma = _hma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_061_pctrank_252d_log_dist_above_kama(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above KAMA."""
    ma = _kama(close, 10)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_062_pctrank_252d_log_dist_above_lsma50(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above LSMA50."""
    ma = _lsma(close, 50)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_063_pctrank_252d_log_dist_above_frama(close: pd.Series) -> pd.Series:
    """Empirical 252d percentile rank of log-distance above FRAMA."""
    ma = _frama(close, 16)
    dist = _safe_log(close) - _safe_log(ma)
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
    rank = dist.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return (rank)

def f11_smae_064_frac_close_above_sma50_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling QDAYS) where close > SMA50 - regime persistence."""
    ma = _sma(close, 50)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean())

def f11_smae_065_frac_close_above_sma200_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling YDAYS) where close > SMA200 - regime persistence."""
    ma = _sma(close, 200)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean())

def f11_smae_066_frac_close_above_ema50_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling QDAYS) where close > EMA50 - regime persistence."""
    ma = _ema(close, 50)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean())

def f11_smae_067_frac_close_above_ema200_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling YDAYS) where close > EMA200 - regime persistence."""
    ma = _ema(close, 200)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean())

def f11_smae_068_frac_close_above_hma50_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling QDAYS) where close > HMA50 - regime persistence."""
    ma = _hma(close, 50)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean())

def f11_smae_069_frac_close_above_kama_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling QDAYS) where close > KAMA - regime persistence."""
    ma = _kama(close, 10)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean())

def f11_smae_070_frac_close_above_lsma50_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling YDAYS) where close > LSMA50 - regime persistence."""
    ma = _lsma(close, 50)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(YDAYS, min_periods=max(YDAYS // 3, 2)).mean())

def f11_smae_071_frac_close_above_dema50_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of bars (rolling QDAYS) where close > DEMA50 - regime persistence."""
    ma = _dema(close, 50)
    above = (close > ma).astype(float).where(ma.notna(), np.nan)
    return (above.rolling(QDAYS, min_periods=max(QDAYS // 3, 2)).mean())

def f11_smae_072_days_since_last_cross_close_sma50(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - SMA50)."""
    ma = _sma(close, 50)
    days = _days_since_last_cross(close, ma)
    return (days)

def f11_smae_073_days_since_last_cross_close_sma200(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - SMA200)."""
    ma = _sma(close, 200)
    days = _days_since_last_cross(close, ma)
    return (days)

def f11_smae_074_days_since_last_cross_close_ema50(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - EMA50)."""
    ma = _ema(close, 50)
    days = _days_since_last_cross(close, ma)
    return (days)

def f11_smae_075_days_since_last_cross_close_ema200(close: pd.Series) -> pd.Series:
    """Bars since the most recent sign-flip of (close - EMA200)."""
    ma = _ema(close, 200)
    days = _days_since_last_cross(close, ma)
    return (days)


# ============================================================
#                         REGISTRY 001_075 (base)
# ============================================================

SMA_EMA_EXTENSION_DYNAMICS_BASE_REGISTRY_001_075 = {
    "f11_smae_001_log_dist_above_sma50": {"inputs": ["close"], "func": f11_smae_001_log_dist_above_sma50},
    "f11_smae_002_log_dist_above_ema50": {"inputs": ["close"], "func": f11_smae_002_log_dist_above_ema50},
    "f11_smae_003_log_dist_above_dema50": {"inputs": ["close"], "func": f11_smae_003_log_dist_above_dema50},
    "f11_smae_004_log_dist_above_tema50": {"inputs": ["close"], "func": f11_smae_004_log_dist_above_tema50},
    "f11_smae_005_log_dist_above_wma50": {"inputs": ["close"], "func": f11_smae_005_log_dist_above_wma50},
    "f11_smae_006_log_dist_above_hma50": {"inputs": ["close"], "func": f11_smae_006_log_dist_above_hma50},
    "f11_smae_007_log_dist_above_kama_default": {"inputs": ["close"], "func": f11_smae_007_log_dist_above_kama_default},
    "f11_smae_008_log_dist_above_zlema50": {"inputs": ["close"], "func": f11_smae_008_log_dist_above_zlema50},
    "f11_smae_009_log_dist_above_smma50": {"inputs": ["close"], "func": f11_smae_009_log_dist_above_smma50},
    "f11_smae_010_log_dist_above_mcginley50": {"inputs": ["close"], "func": f11_smae_010_log_dist_above_mcginley50},
    "f11_smae_011_log_dist_above_lsma50": {"inputs": ["close"], "func": f11_smae_011_log_dist_above_lsma50},
    "f11_smae_012_log_dist_above_alma50": {"inputs": ["close"], "func": f11_smae_012_log_dist_above_alma50},
    "f11_smae_013_log_dist_above_t3_50": {"inputs": ["close"], "func": f11_smae_013_log_dist_above_t3_50},
    "f11_smae_014_log_dist_above_frama_default": {"inputs": ["close"], "func": f11_smae_014_log_dist_above_frama_default},
    "f11_smae_015_log_dist_above_sma21_short_trend": {"inputs": ["close"], "func": f11_smae_015_log_dist_above_sma21_short_trend},
    "f11_smae_016_log_dist_above_sma100_med_trend": {"inputs": ["close"], "func": f11_smae_016_log_dist_above_sma100_med_trend},
    "f11_smae_017_log_dist_above_sma200_regime": {"inputs": ["close"], "func": f11_smae_017_log_dist_above_sma200_regime},
    "f11_smae_018_log_dist_above_ema21_short_decay": {"inputs": ["close"], "func": f11_smae_018_log_dist_above_ema21_short_decay},
    "f11_smae_019_log_dist_above_ema100_med_decay": {"inputs": ["close"], "func": f11_smae_019_log_dist_above_ema100_med_decay},
    "f11_smae_020_log_dist_above_ema200_long_decay": {"inputs": ["close"], "func": f11_smae_020_log_dist_above_ema200_long_decay},
    "f11_smae_021_log_dist_above_hma21_responsive_short": {"inputs": ["close"], "func": f11_smae_021_log_dist_above_hma21_responsive_short},
    "f11_smae_022_log_dist_above_hma100_responsive_med": {"inputs": ["close"], "func": f11_smae_022_log_dist_above_hma100_responsive_med},
    "f11_smae_023_log_dist_above_hma200_responsive_long": {"inputs": ["close"], "func": f11_smae_023_log_dist_above_hma200_responsive_long},
    "f11_smae_024_atr21_dist_above_sma50": {"inputs": ["high", "low", "close"], "func": f11_smae_024_atr21_dist_above_sma50},
    "f11_smae_025_atr21_dist_above_ema50": {"inputs": ["high", "low", "close"], "func": f11_smae_025_atr21_dist_above_ema50},
    "f11_smae_026_atr21_dist_above_dema50": {"inputs": ["high", "low", "close"], "func": f11_smae_026_atr21_dist_above_dema50},
    "f11_smae_027_atr21_dist_above_tema50": {"inputs": ["high", "low", "close"], "func": f11_smae_027_atr21_dist_above_tema50},
    "f11_smae_028_atr21_dist_above_wma50": {"inputs": ["high", "low", "close"], "func": f11_smae_028_atr21_dist_above_wma50},
    "f11_smae_029_atr21_dist_above_hma50": {"inputs": ["high", "low", "close"], "func": f11_smae_029_atr21_dist_above_hma50},
    "f11_smae_030_atr21_dist_above_kama50": {"inputs": ["high", "low", "close"], "func": f11_smae_030_atr21_dist_above_kama50},
    "f11_smae_031_atr21_dist_above_zlema50": {"inputs": ["high", "low", "close"], "func": f11_smae_031_atr21_dist_above_zlema50},
    "f11_smae_032_atr21_dist_above_smma50": {"inputs": ["high", "low", "close"], "func": f11_smae_032_atr21_dist_above_smma50},
    "f11_smae_033_atr21_dist_above_mcginley50": {"inputs": ["high", "low", "close"], "func": f11_smae_033_atr21_dist_above_mcginley50},
    "f11_smae_034_atr21_dist_above_lsma50": {"inputs": ["high", "low", "close"], "func": f11_smae_034_atr21_dist_above_lsma50},
    "f11_smae_035_atr21_dist_above_alma50": {"inputs": ["high", "low", "close"], "func": f11_smae_035_atr21_dist_above_alma50},
    "f11_smae_036_atr21_dist_above_t350": {"inputs": ["high", "low", "close"], "func": f11_smae_036_atr21_dist_above_t350},
    "f11_smae_037_atr21_dist_above_frama50": {"inputs": ["high", "low", "close"], "func": f11_smae_037_atr21_dist_above_frama50},
    "f11_smae_038_sigma_dist_above_sma50_monthly_sigma": {"inputs": ["close"], "func": f11_smae_038_sigma_dist_above_sma50_monthly_sigma},
    "f11_smae_039_sigma_dist_above_sma50_quarterly_sigma": {"inputs": ["close"], "func": f11_smae_039_sigma_dist_above_sma50_quarterly_sigma},
    "f11_smae_040_sigma_dist_above_sma50_annual_sigma": {"inputs": ["close"], "func": f11_smae_040_sigma_dist_above_sma50_annual_sigma},
    "f11_smae_041_sigma_dist_above_ema50_monthly_sigma": {"inputs": ["close"], "func": f11_smae_041_sigma_dist_above_ema50_monthly_sigma},
    "f11_smae_042_sigma_dist_above_ema50_quarterly_sigma": {"inputs": ["close"], "func": f11_smae_042_sigma_dist_above_ema50_quarterly_sigma},
    "f11_smae_043_sigma_dist_above_ema50_annual_sigma": {"inputs": ["close"], "func": f11_smae_043_sigma_dist_above_ema50_annual_sigma},
    "f11_smae_044_sigma_dist_above_hma50_monthly_sigma": {"inputs": ["close"], "func": f11_smae_044_sigma_dist_above_hma50_monthly_sigma},
    "f11_smae_045_sigma_dist_above_hma50_quarterly_sigma": {"inputs": ["close"], "func": f11_smae_045_sigma_dist_above_hma50_quarterly_sigma},
    "f11_smae_046_sigma_dist_above_hma50_annual_sigma": {"inputs": ["close"], "func": f11_smae_046_sigma_dist_above_hma50_annual_sigma},
    "f11_smae_047_zscore_252d_log_dist_above_sma50": {"inputs": ["close"], "func": f11_smae_047_zscore_252d_log_dist_above_sma50},
    "f11_smae_048_zscore_252d_log_dist_above_ema50": {"inputs": ["close"], "func": f11_smae_048_zscore_252d_log_dist_above_ema50},
    "f11_smae_049_zscore_252d_log_dist_above_dema50": {"inputs": ["close"], "func": f11_smae_049_zscore_252d_log_dist_above_dema50},
    "f11_smae_050_zscore_252d_log_dist_above_tema50": {"inputs": ["close"], "func": f11_smae_050_zscore_252d_log_dist_above_tema50},
    "f11_smae_051_zscore_252d_log_dist_above_wma50": {"inputs": ["close"], "func": f11_smae_051_zscore_252d_log_dist_above_wma50},
    "f11_smae_052_zscore_252d_log_dist_above_hma50": {"inputs": ["close"], "func": f11_smae_052_zscore_252d_log_dist_above_hma50},
    "f11_smae_053_zscore_252d_log_dist_above_kama": {"inputs": ["close"], "func": f11_smae_053_zscore_252d_log_dist_above_kama},
    "f11_smae_054_zscore_252d_log_dist_above_lsma50": {"inputs": ["close"], "func": f11_smae_054_zscore_252d_log_dist_above_lsma50},
    "f11_smae_055_zscore_252d_log_dist_above_alma50": {"inputs": ["close"], "func": f11_smae_055_zscore_252d_log_dist_above_alma50},
    "f11_smae_056_pctrank_252d_log_dist_above_sma50": {"inputs": ["close"], "func": f11_smae_056_pctrank_252d_log_dist_above_sma50},
    "f11_smae_057_pctrank_252d_log_dist_above_ema50": {"inputs": ["close"], "func": f11_smae_057_pctrank_252d_log_dist_above_ema50},
    "f11_smae_058_pctrank_252d_log_dist_above_dema50": {"inputs": ["close"], "func": f11_smae_058_pctrank_252d_log_dist_above_dema50},
    "f11_smae_059_pctrank_252d_log_dist_above_tema50": {"inputs": ["close"], "func": f11_smae_059_pctrank_252d_log_dist_above_tema50},
    "f11_smae_060_pctrank_252d_log_dist_above_hma50": {"inputs": ["close"], "func": f11_smae_060_pctrank_252d_log_dist_above_hma50},
    "f11_smae_061_pctrank_252d_log_dist_above_kama": {"inputs": ["close"], "func": f11_smae_061_pctrank_252d_log_dist_above_kama},
    "f11_smae_062_pctrank_252d_log_dist_above_lsma50": {"inputs": ["close"], "func": f11_smae_062_pctrank_252d_log_dist_above_lsma50},
    "f11_smae_063_pctrank_252d_log_dist_above_frama": {"inputs": ["close"], "func": f11_smae_063_pctrank_252d_log_dist_above_frama},
    "f11_smae_064_frac_close_above_sma50_in_63d": {"inputs": ["close"], "func": f11_smae_064_frac_close_above_sma50_in_63d},
    "f11_smae_065_frac_close_above_sma200_in_252d": {"inputs": ["close"], "func": f11_smae_065_frac_close_above_sma200_in_252d},
    "f11_smae_066_frac_close_above_ema50_in_63d": {"inputs": ["close"], "func": f11_smae_066_frac_close_above_ema50_in_63d},
    "f11_smae_067_frac_close_above_ema200_in_252d": {"inputs": ["close"], "func": f11_smae_067_frac_close_above_ema200_in_252d},
    "f11_smae_068_frac_close_above_hma50_in_63d": {"inputs": ["close"], "func": f11_smae_068_frac_close_above_hma50_in_63d},
    "f11_smae_069_frac_close_above_kama_in_63d": {"inputs": ["close"], "func": f11_smae_069_frac_close_above_kama_in_63d},
    "f11_smae_070_frac_close_above_lsma50_in_252d": {"inputs": ["close"], "func": f11_smae_070_frac_close_above_lsma50_in_252d},
    "f11_smae_071_frac_close_above_dema50_in_63d": {"inputs": ["close"], "func": f11_smae_071_frac_close_above_dema50_in_63d},
    "f11_smae_072_days_since_last_cross_close_sma50": {"inputs": ["close"], "func": f11_smae_072_days_since_last_cross_close_sma50},
    "f11_smae_073_days_since_last_cross_close_sma200": {"inputs": ["close"], "func": f11_smae_073_days_since_last_cross_close_sma200},
    "f11_smae_074_days_since_last_cross_close_ema50": {"inputs": ["close"], "func": f11_smae_074_days_since_last_cross_close_ema50},
    "f11_smae_075_days_since_last_cross_close_ema200": {"inputs": ["close"], "func": f11_smae_075_days_since_last_cross_close_ema200},
}
