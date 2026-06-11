"""moving_average_extension_dynamics d2 features 001_075 — short blowup pipeline 1a-inverse.

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
#                    D2 FEATURES 001-075
# ============================================================

def f08_maed_001_sma_50_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_002_sma_100_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(100, min_periods=max(100 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_003_sma_150_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(150, min_periods=max(150 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_004_sma_200_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_005_sma_504_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(504, min_periods=max(504 // 3, 2)).mean()
    atr = _atr(high, low, close, 252)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_006_sma_1260_atr_extension_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sma = close.rolling(1260, min_periods=max(1260 // 3, 2)).mean()
    atr = _atr(high, low, close, 252)
    return (_safe_div(close - sma, atr)).diff().diff()


def f08_maed_007_sma_50_log_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_safe_log(close) - _safe_log(sma)).diff().diff()


def f08_maed_008_sma_200_log_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_safe_log(close) - _safe_log(sma)).diff().diff()


def f08_maed_009_sma_504_log_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(504, min_periods=max(504 // 3, 2)).mean()
    return (_safe_log(close) - _safe_log(sma)).diff().diff()


def f08_maed_010_sma_1260_log_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(1260, min_periods=max(1260 // 3, 2)).mean()
    return (_safe_log(close) - _safe_log(sma)).diff().diff()


def f08_maed_011_sma_100_pct_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(100, min_periods=max(100 // 3, 2)).mean()
    return (_safe_div(close - sma, sma)).diff().diff()


def f08_maed_012_sma_200_pct_extension_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_safe_div(close - sma, sma)).diff().diff()


def f08_maed_013_sma_50_ext_zscore_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return (_rolling_zscore(ext, 252)).diff().diff()


def f08_maed_014_sma_200_ext_zscore_504d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return (_rolling_zscore(ext, 504)).diff().diff()


def f08_maed_015_sma_50_ext_pctrank_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return (_rolling_pctrank(ext, 252)).diff().diff()


def f08_maed_016_sma_200_ext_pctrank_504d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return (_rolling_pctrank(ext, 504)).diff().diff()


def f08_maed_017_sma_200_ext_pctrank_1260d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    ext = _safe_log(close) - _safe_log(sma)
    return (_rolling_pctrank(ext, 1260)).diff().diff()


def f08_maed_018_days_since_close_crossed_sma_50_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_days_since_cross(close, sma)).diff().diff()


def f08_maed_019_days_since_close_crossed_sma_200_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_days_since_cross(close, sma)).diff().diff()


def f08_maed_020_days_since_close_crossed_sma_1260_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(1260, min_periods=max(1260 // 3, 2)).mean()
    return (_days_since_cross(close, sma)).diff().diff()


def f08_maed_021_ema_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 50)
    return (_safe_log(close) - _safe_log(ema)).diff().diff()


def f08_maed_022_ema_100_log_extension_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 100)
    return (_safe_log(close) - _safe_log(ema)).diff().diff()


def f08_maed_023_ema_200_log_extension_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 200)
    return (_safe_log(close) - _safe_log(ema)).diff().diff()


def f08_maed_024_dema_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _dema(close, 50)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_025_dema_100_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _dema(close, 100)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_026_tema_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _tema(close, 50)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_027_tema_100_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _tema(close, 100)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_028_hma_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _hma(close, 50)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_029_hma_100_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _hma(close, 100)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_030_kama_21_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _kama(close, 21)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_031_kama_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _kama(close, 50)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_032_wma_50_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _wma(close, 50)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_033_wma_200_log_extension_d2(close: pd.Series) -> pd.Series:
    ma = _wma(close, 200)
    return (_safe_log(close) - _safe_log(ma)).diff().diff()


def f08_maed_034_ema_50_minus_ema_200_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _ema(close, 50)
    b = _ema(close, 200)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_035_dema_50_minus_dema_200_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _dema(close, 50)
    b = _dema(close, 200)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_036_tema_50_minus_tema_200_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _tema(close, 50)
    b = _tema(close, 200)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_037_hma_50_minus_hma_200_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _hma(close, 50)
    b = _hma(close, 200)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_038_kama_21_minus_kama_50_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _kama(close, 21)
    b = _kama(close, 50)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_039_wma_50_minus_wma_200_log_gap_d2(close: pd.Series) -> pd.Series:
    a = _wma(close, 50)
    b = _wma(close, 200)
    return (_safe_log(a) - _safe_log(b)).diff().diff()


def f08_maed_040_ema_50_vs_sma_50_log_divergence_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 50)
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_safe_log(ema) - _safe_log(sma)).diff().diff()


def f08_maed_041_sma_50_slope_21d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_rolling_slope(_safe_log(sma), 21)).diff().diff()


def f08_maed_042_sma_200_slope_63d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_rolling_slope(_safe_log(sma), 63)).diff().diff()


def f08_maed_043_sma_504_slope_63d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(504, min_periods=max(504 // 3, 2)).mean()
    return (_rolling_slope(_safe_log(sma), 63)).diff().diff()


def f08_maed_044_ema_50_slope_21d_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 50)
    return (_rolling_slope(_safe_log(ema), 21)).diff().diff()


def f08_maed_045_ema_200_slope_63d_d2(close: pd.Series) -> pd.Series:
    ema = _ema(close, 200)
    return (_rolling_slope(_safe_log(ema), 63)).diff().diff()


def f08_maed_046_hma_50_slope_21d_d2(close: pd.Series) -> pd.Series:
    ma = _hma(close, 50)
    return (_rolling_slope(_safe_log(ma), 21)).diff().diff()


def f08_maed_047_sma_50_slope_zscore_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 21)
    return (_rolling_zscore(sl, 252)).diff().diff()


def f08_maed_048_sma_200_slope_zscore_504d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 63)
    return (_rolling_zscore(sl, 504)).diff().diff()


def f08_maed_049_sma_50_slope_accel_21d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 21)
    return (sl.diff()).diff().diff()


def f08_maed_050_sma_200_slope_accel_63d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 63)
    return (sl.diff()).diff().diff()


def f08_maed_051_sma_50_slope_flip_count_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 21)
    sign = np.sign(sl.fillna(0))
    flips = (sign != sign.shift(1)).astype(float)
    return (flips.rolling(252, min_periods=max(252 // 3, 2)).sum()).diff().diff()


def f08_maed_052_sma_200_slope_flip_count_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 63)
    sign = np.sign(sl.fillna(0))
    flips = (sign != sign.shift(1)).astype(float)
    return (flips.rolling(252, min_periods=max(252 // 3, 2)).sum()).diff().diff()


def f08_maed_053_sma_50_slope_max_minus_current_63d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 21)
    return (sl.rolling(63, min_periods=21).max() - sl).diff().diff()


def f08_maed_054_sma_50_slope_pctrank_504d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 21)
    return (_rolling_pctrank(sl, 504)).diff().diff()


def f08_maed_055_sma_200_slope_pctrank_1260d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sl = _rolling_slope(_safe_log(sma), 63)
    return (_rolling_pctrank(sl, 1260)).diff().diff()


def f08_maed_056_sma_50_curvature_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_safe_log(sma).diff().diff()).diff().diff()


def f08_maed_057_sma_200_curvature_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_safe_log(sma).diff().diff()).diff().diff()


def f08_maed_058_log_price_minus_sma_200_slope_divergence_63d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_rolling_slope(_safe_log(close), 63) - _rolling_slope(_safe_log(sma), 63)).diff().diff()


def f08_maed_059_sma_50_slope_decay_21_vs_63_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    s21 = _rolling_slope(_safe_log(sma), 21)
    s63 = _rolling_slope(_safe_log(sma), 63)
    return (_safe_div(s21, s63)).diff().diff()


def f08_maed_060_hma_200_flatness_21d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    ma = _hma(close, 200)
    sl = _rolling_slope(_safe_log(ma), 21)
    atr = _atr(high, low, close, 21)
    return (1.0 - _safe_div(sl.abs() * close, atr)).diff().diff()


def f08_maed_061_days_since_sma_50_crossed_sma_200_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    return (_days_since_cross(a, b)).diff().diff()


def f08_maed_062_days_since_sma_20_crossed_sma_50_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    b = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (_days_since_cross(a, b)).diff().diff()


def f08_maed_063_days_since_ema_50_crossed_ema_200_d2(close: pd.Series) -> pd.Series:
    a = _ema(close, 50)
    b = _ema(close, 200)
    return (_days_since_cross(a, b)).diff().diff()


def f08_maed_064_sma_50_sma_200_cross_count_252d_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sign = np.sign((a - b).fillna(0))
    crosses = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (crosses.rolling(252, min_periods=max(252 // 3, 2)).sum()).diff().diff()


def f08_maed_065_close_cross_sma_50_count_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    sign = np.sign((close - sma).fillna(0))
    crosses = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (crosses.rolling(252, min_periods=max(252 // 3, 2)).sum()).diff().diff()


def f08_maed_066_close_cross_sma_200_count_252d_d2(close: pd.Series) -> pd.Series:
    sma = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    sign = np.sign((close - sma).fillna(0))
    crosses = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (crosses.rolling(252, min_periods=max(252 // 3, 2)).sum()).diff().diff()


def f08_maed_067_golden_cross_state_50_200_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    state = (a > b).astype(float)
    return (state).diff().diff()


def f08_maed_068_golden_cross_state_20_100_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    b = close.rolling(100, min_periods=max(100 // 3, 2)).mean()
    state = (a > b).astype(float)
    return (state).diff().diff()


def f08_maed_069_ma_stack_count_5_d2(close: pd.Series) -> pd.Series:
    mas = [close.rolling(n, min_periods=max(n // 3, 2)).mean() for n in [20, 50, 100, 200, 500]]
    above = sum((close > m).astype(float) for m in mas)
    return (above).diff().diff()


def f08_maed_070_ema_stack_count_5_d2(close: pd.Series) -> pd.Series:
    mas = [_ema(close, n) for n in [20, 50, 100, 200, 500]]
    above = sum((close > m).astype(float) for m in mas)
    return (above).diff().diff()


def f08_maed_071_ma_fan_width_50_200_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    return (_safe_div(a - b, atr)).diff().diff()


def f08_maed_072_ma_fan_width_50_200_pctrank_504d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    atr = _atr(high, low, close, 21)
    w = _safe_div(a - b, atr)
    return (_rolling_pctrank(w, 504)).diff().diff()


def f08_maed_073_days_since_fan_50_200_max_252d_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    b = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    gap = a - b
    def _b(w):
        return (len(w) - 1) - int(np.argmax(w))
    return (gap.rolling(252, min_periods=63).apply(_b, raw=True)).diff().diff()


def f08_maed_074_sma_20_50_cross_direction_63d_d2(close: pd.Series) -> pd.Series:
    a = close.rolling(20, min_periods=max(20 // 3, 2)).mean()
    b = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    return (np.sign((a - b).rolling(63, min_periods=21).mean())).diff().diff()


def f08_maed_075_ema_21_50_cross_direction_63d_d2(close: pd.Series) -> pd.Series:
    a = _ema(close, 21)
    b = _ema(close, 50)
    return (np.sign((a - b).rolling(63, min_periods=21).mean())).diff().diff()


MOVING_AVERAGE_EXTENSION_DYNAMICS_D2_REGISTRY_001_075 = {
    "f08_maed_001_sma_50_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_001_sma_50_atr_extension_d2},
    "f08_maed_002_sma_100_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_002_sma_100_atr_extension_d2},
    "f08_maed_003_sma_150_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_003_sma_150_atr_extension_d2},
    "f08_maed_004_sma_200_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_004_sma_200_atr_extension_d2},
    "f08_maed_005_sma_504_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_005_sma_504_atr_extension_d2},
    "f08_maed_006_sma_1260_atr_extension_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_006_sma_1260_atr_extension_d2},
    "f08_maed_007_sma_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_007_sma_50_log_extension_d2},
    "f08_maed_008_sma_200_log_extension_d2": {"inputs": ["close"], "func": f08_maed_008_sma_200_log_extension_d2},
    "f08_maed_009_sma_504_log_extension_d2": {"inputs": ["close"], "func": f08_maed_009_sma_504_log_extension_d2},
    "f08_maed_010_sma_1260_log_extension_d2": {"inputs": ["close"], "func": f08_maed_010_sma_1260_log_extension_d2},
    "f08_maed_011_sma_100_pct_extension_d2": {"inputs": ["close"], "func": f08_maed_011_sma_100_pct_extension_d2},
    "f08_maed_012_sma_200_pct_extension_d2": {"inputs": ["close"], "func": f08_maed_012_sma_200_pct_extension_d2},
    "f08_maed_013_sma_50_ext_zscore_252d_d2": {"inputs": ["close"], "func": f08_maed_013_sma_50_ext_zscore_252d_d2},
    "f08_maed_014_sma_200_ext_zscore_504d_d2": {"inputs": ["close"], "func": f08_maed_014_sma_200_ext_zscore_504d_d2},
    "f08_maed_015_sma_50_ext_pctrank_252d_d2": {"inputs": ["close"], "func": f08_maed_015_sma_50_ext_pctrank_252d_d2},
    "f08_maed_016_sma_200_ext_pctrank_504d_d2": {"inputs": ["close"], "func": f08_maed_016_sma_200_ext_pctrank_504d_d2},
    "f08_maed_017_sma_200_ext_pctrank_1260d_d2": {"inputs": ["close"], "func": f08_maed_017_sma_200_ext_pctrank_1260d_d2},
    "f08_maed_018_days_since_close_crossed_sma_50_d2": {"inputs": ["close"], "func": f08_maed_018_days_since_close_crossed_sma_50_d2},
    "f08_maed_019_days_since_close_crossed_sma_200_d2": {"inputs": ["close"], "func": f08_maed_019_days_since_close_crossed_sma_200_d2},
    "f08_maed_020_days_since_close_crossed_sma_1260_d2": {"inputs": ["close"], "func": f08_maed_020_days_since_close_crossed_sma_1260_d2},
    "f08_maed_021_ema_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_021_ema_50_log_extension_d2},
    "f08_maed_022_ema_100_log_extension_d2": {"inputs": ["close"], "func": f08_maed_022_ema_100_log_extension_d2},
    "f08_maed_023_ema_200_log_extension_d2": {"inputs": ["close"], "func": f08_maed_023_ema_200_log_extension_d2},
    "f08_maed_024_dema_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_024_dema_50_log_extension_d2},
    "f08_maed_025_dema_100_log_extension_d2": {"inputs": ["close"], "func": f08_maed_025_dema_100_log_extension_d2},
    "f08_maed_026_tema_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_026_tema_50_log_extension_d2},
    "f08_maed_027_tema_100_log_extension_d2": {"inputs": ["close"], "func": f08_maed_027_tema_100_log_extension_d2},
    "f08_maed_028_hma_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_028_hma_50_log_extension_d2},
    "f08_maed_029_hma_100_log_extension_d2": {"inputs": ["close"], "func": f08_maed_029_hma_100_log_extension_d2},
    "f08_maed_030_kama_21_log_extension_d2": {"inputs": ["close"], "func": f08_maed_030_kama_21_log_extension_d2},
    "f08_maed_031_kama_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_031_kama_50_log_extension_d2},
    "f08_maed_032_wma_50_log_extension_d2": {"inputs": ["close"], "func": f08_maed_032_wma_50_log_extension_d2},
    "f08_maed_033_wma_200_log_extension_d2": {"inputs": ["close"], "func": f08_maed_033_wma_200_log_extension_d2},
    "f08_maed_034_ema_50_minus_ema_200_log_gap_d2": {"inputs": ["close"], "func": f08_maed_034_ema_50_minus_ema_200_log_gap_d2},
    "f08_maed_035_dema_50_minus_dema_200_log_gap_d2": {"inputs": ["close"], "func": f08_maed_035_dema_50_minus_dema_200_log_gap_d2},
    "f08_maed_036_tema_50_minus_tema_200_log_gap_d2": {"inputs": ["close"], "func": f08_maed_036_tema_50_minus_tema_200_log_gap_d2},
    "f08_maed_037_hma_50_minus_hma_200_log_gap_d2": {"inputs": ["close"], "func": f08_maed_037_hma_50_minus_hma_200_log_gap_d2},
    "f08_maed_038_kama_21_minus_kama_50_log_gap_d2": {"inputs": ["close"], "func": f08_maed_038_kama_21_minus_kama_50_log_gap_d2},
    "f08_maed_039_wma_50_minus_wma_200_log_gap_d2": {"inputs": ["close"], "func": f08_maed_039_wma_50_minus_wma_200_log_gap_d2},
    "f08_maed_040_ema_50_vs_sma_50_log_divergence_d2": {"inputs": ["close"], "func": f08_maed_040_ema_50_vs_sma_50_log_divergence_d2},
    "f08_maed_041_sma_50_slope_21d_d2": {"inputs": ["close"], "func": f08_maed_041_sma_50_slope_21d_d2},
    "f08_maed_042_sma_200_slope_63d_d2": {"inputs": ["close"], "func": f08_maed_042_sma_200_slope_63d_d2},
    "f08_maed_043_sma_504_slope_63d_d2": {"inputs": ["close"], "func": f08_maed_043_sma_504_slope_63d_d2},
    "f08_maed_044_ema_50_slope_21d_d2": {"inputs": ["close"], "func": f08_maed_044_ema_50_slope_21d_d2},
    "f08_maed_045_ema_200_slope_63d_d2": {"inputs": ["close"], "func": f08_maed_045_ema_200_slope_63d_d2},
    "f08_maed_046_hma_50_slope_21d_d2": {"inputs": ["close"], "func": f08_maed_046_hma_50_slope_21d_d2},
    "f08_maed_047_sma_50_slope_zscore_252d_d2": {"inputs": ["close"], "func": f08_maed_047_sma_50_slope_zscore_252d_d2},
    "f08_maed_048_sma_200_slope_zscore_504d_d2": {"inputs": ["close"], "func": f08_maed_048_sma_200_slope_zscore_504d_d2},
    "f08_maed_049_sma_50_slope_accel_21d_d2": {"inputs": ["close"], "func": f08_maed_049_sma_50_slope_accel_21d_d2},
    "f08_maed_050_sma_200_slope_accel_63d_d2": {"inputs": ["close"], "func": f08_maed_050_sma_200_slope_accel_63d_d2},
    "f08_maed_051_sma_50_slope_flip_count_252d_d2": {"inputs": ["close"], "func": f08_maed_051_sma_50_slope_flip_count_252d_d2},
    "f08_maed_052_sma_200_slope_flip_count_252d_d2": {"inputs": ["close"], "func": f08_maed_052_sma_200_slope_flip_count_252d_d2},
    "f08_maed_053_sma_50_slope_max_minus_current_63d_d2": {"inputs": ["close"], "func": f08_maed_053_sma_50_slope_max_minus_current_63d_d2},
    "f08_maed_054_sma_50_slope_pctrank_504d_d2": {"inputs": ["close"], "func": f08_maed_054_sma_50_slope_pctrank_504d_d2},
    "f08_maed_055_sma_200_slope_pctrank_1260d_d2": {"inputs": ["close"], "func": f08_maed_055_sma_200_slope_pctrank_1260d_d2},
    "f08_maed_056_sma_50_curvature_d2": {"inputs": ["close"], "func": f08_maed_056_sma_50_curvature_d2},
    "f08_maed_057_sma_200_curvature_d2": {"inputs": ["close"], "func": f08_maed_057_sma_200_curvature_d2},
    "f08_maed_058_log_price_minus_sma_200_slope_divergence_63d_d2": {"inputs": ["close"], "func": f08_maed_058_log_price_minus_sma_200_slope_divergence_63d_d2},
    "f08_maed_059_sma_50_slope_decay_21_vs_63_d2": {"inputs": ["close"], "func": f08_maed_059_sma_50_slope_decay_21_vs_63_d2},
    "f08_maed_060_hma_200_flatness_21d_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_060_hma_200_flatness_21d_d2},
    "f08_maed_061_days_since_sma_50_crossed_sma_200_d2": {"inputs": ["close"], "func": f08_maed_061_days_since_sma_50_crossed_sma_200_d2},
    "f08_maed_062_days_since_sma_20_crossed_sma_50_d2": {"inputs": ["close"], "func": f08_maed_062_days_since_sma_20_crossed_sma_50_d2},
    "f08_maed_063_days_since_ema_50_crossed_ema_200_d2": {"inputs": ["close"], "func": f08_maed_063_days_since_ema_50_crossed_ema_200_d2},
    "f08_maed_064_sma_50_sma_200_cross_count_252d_d2": {"inputs": ["close"], "func": f08_maed_064_sma_50_sma_200_cross_count_252d_d2},
    "f08_maed_065_close_cross_sma_50_count_252d_d2": {"inputs": ["close"], "func": f08_maed_065_close_cross_sma_50_count_252d_d2},
    "f08_maed_066_close_cross_sma_200_count_252d_d2": {"inputs": ["close"], "func": f08_maed_066_close_cross_sma_200_count_252d_d2},
    "f08_maed_067_golden_cross_state_50_200_d2": {"inputs": ["close"], "func": f08_maed_067_golden_cross_state_50_200_d2},
    "f08_maed_068_golden_cross_state_20_100_d2": {"inputs": ["close"], "func": f08_maed_068_golden_cross_state_20_100_d2},
    "f08_maed_069_ma_stack_count_5_d2": {"inputs": ["close"], "func": f08_maed_069_ma_stack_count_5_d2},
    "f08_maed_070_ema_stack_count_5_d2": {"inputs": ["close"], "func": f08_maed_070_ema_stack_count_5_d2},
    "f08_maed_071_ma_fan_width_50_200_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_071_ma_fan_width_50_200_d2},
    "f08_maed_072_ma_fan_width_50_200_pctrank_504d_d2": {"inputs": ["close", "high", "low"], "func": f08_maed_072_ma_fan_width_50_200_pctrank_504d_d2},
    "f08_maed_073_days_since_fan_50_200_max_252d_d2": {"inputs": ["close"], "func": f08_maed_073_days_since_fan_50_200_max_252d_d2},
    "f08_maed_074_sma_20_50_cross_direction_63d_d2": {"inputs": ["close"], "func": f08_maed_074_sma_20_50_cross_direction_63d_d2},
    "f08_maed_075_ema_21_50_cross_direction_63d_d2": {"inputs": ["close"], "func": f08_maed_075_ema_21_50_cross_direction_63d_d2},
}
