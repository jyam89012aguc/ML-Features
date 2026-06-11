"""atr_extension_signature base features 301-375 — Pipeline 1b-technical.

Third gap-fill batch. Each feature isolates an independent predictive angle —
multi-time-frame agreement (separate signal from any single-horizon extension),
robust (MAD/IQR/trimmed) extension (distinct from ATR-based), regime-stratified
extension (extension during vol/momentum regimes), classical pivot-point levels,
Fibonacci retracement/extension distances, volatility-cone position, extension
dynamics/velocity/dwell, AR-persistence / Hurst-style features, and extreme-
extension survivorship counters.

Bucket LL: Multi-time-frame extension agreement (301-310).
Bucket MM: Robust extension via MAD / IQR / trimmed-std (311-318).
Bucket NN: Conditional / regime-stratified extension (319-326).
Bucket OO: Pivot point distances (standard) (327-336).
Bucket PP: Fibonacci pivot distances (337-342).
Bucket QQ: Volatility-cone / vol-regime position (343-350).
Bucket RR: Extension dynamics / velocity / dwell (351-360).
Bucket SS: AR / Hurst persistence (361-368).
Bucket TT: Extreme-extension survivorship (369-375).

Inputs: SEP OHLCV. Self-contained helpers; PIT-clean.
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


def _bars_since_true(mask):
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


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(au, ad))


def _mad(s, n):
    """Median absolute deviation over rolling n bars."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = w[valid]
        med = np.median(v)
        return float(np.median(np.abs(v - med)))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _iqr(s, n):
    """Inter-quartile range over rolling n bars."""
    q75 = s.rolling(n, min_periods=max(n // 3, 2)).quantile(0.75)
    q25 = s.rolling(n, min_periods=max(n // 3, 2)).quantile(0.25)
    return q75 - q25


def _trimmed_mean(s, n, trim=0.1):
    """Trimmed mean (trim from each end) over rolling n bars."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = np.sort(w[valid])
        k = int(len(v) * trim)
        if len(v) - 2 * k <= 0:
            return float(np.mean(v))
        return float(np.mean(v[k:len(v) - k]))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _trimmed_std(s, n, trim=0.1):
    """Trimmed std over rolling n bars."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        v = np.sort(w[valid])
        k = int(len(v) * trim)
        if len(v) - 2 * k <= 1:
            return float(np.std(v, ddof=1)) if len(v) > 1 else np.nan
        return float(np.std(v[k:len(v) - k], ddof=1))
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hurst_rs(s, n):
    """Hurst exponent via R/S analysis approximation over rolling n bars."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid].astype(float)
        if v.size < 20:
            return np.nan
        mean = v.mean()
        dev = v - mean
        cum = np.cumsum(dev)
        r = cum.max() - cum.min()
        sd = v.std(ddof=1)
        if sd == 0 or r <= 0:
            return np.nan
        return float(np.log(r / sd) / np.log(len(v)))
    return s.rolling(n, min_periods=20).apply(_f, raw=True)


# ============================================================
# Bucket LL — Multi-time-frame extension agreement (301-310)
# ============================================================

def f47_atxs_301_multi_tf_2way_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if sign((c-SMA21)/ATR21) > 0 AND sign((c-SMA63)/ATR21) > 0 — short+medium bullish agreement."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    return ((e21 > 0) & (e63 > 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_302_multi_tf_3way_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if all three extensions (SMA21/63/252) positive — 3-tf bullish stack."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_303_multi_tf_3way_bear_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if all three extensions negative — 3-tf bearish stack."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return ((e21 < 0) & (e63 < 0) & (e252 < 0)).astype(float).where(a.notna(), np.nan)


def f47_atxs_304_count_multi_tf_bull_agreement_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars with 3-tf bullish-stack agreement."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    f = ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float)
    return f.rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna(), np.nan)


def f47_atxs_305_count_multi_tf_bull_agreement_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of 3-tf bullish-stack bars."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    f = ((e21 > 0) & (e63 > 0) & (e252 > 0)).astype(float)
    return f.rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna(), np.nan)


def f47_atxs_306_longest_multi_tf_bull_streak_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest consecutive 3-tf bullish-stack streak in past 252."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    s = _streak_true((e21 > 0) & (e63 > 0) & (e252 > 0))
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(a.notna(), np.nan)


def f47_atxs_307_multi_tf_short_vs_long_disagree(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if sign((c-SMA21)/atr) != sign((c-SMA252)/atr) — short vs long-tf disagreement state."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return (np.sign(e21) != np.sign(e252)).astype(float).where(a.notna(), np.nan)


def f47_atxs_308_bars_since_multi_tf_bull_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last 3-tf bullish-stack agreement — recency of multi-tf bull regime."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return _bars_since_true((e21 > 0) & (e63 > 0) & (e252 > 0))


def f47_atxs_309_bars_since_multi_tf_bear_agreement(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last 3-tf bearish-stack agreement."""
    a = _atr(high, low, close, MDAYS)
    e21 = _safe_div(close - _sma(close, MDAYS), a)
    e63 = _safe_div(close - _sma(close, QDAYS), a)
    e252 = _safe_div(close - _sma(close, YDAYS), a)
    return _bars_since_true((e21 < 0) & (e63 < 0) & (e252 < 0))


def f47_atxs_310_multi_tf_magnitude_divergence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(c-SMA21)/atr - (c-SMA252)/atr — magnitude divergence between short and long extension."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _sma(close, MDAYS), a) - _safe_div(close - _sma(close, YDAYS), a)


# ============================================================
# Bucket MM — Robust extension via MAD / IQR / trimmed (311-318)
# ============================================================

def f47_atxs_311_close_minus_sma21_over_mad21(close: pd.Series) -> pd.Series:
    """(close - SMA21) / MAD(close, 21) — MAD-normalized extension (robust to outliers)."""
    return _safe_div(close - _sma(close, MDAYS), _mad(close, MDAYS))


def f47_atxs_312_close_minus_sma63_over_mad63(close: pd.Series) -> pd.Series:
    """(close - SMA63) / MAD(close, 63) — robust quarterly extension."""
    return _safe_div(close - _sma(close, QDAYS), _mad(close, QDAYS))


def f47_atxs_313_close_minus_median21_over_iqr21(close: pd.Series) -> pd.Series:
    """(close - rolling-median21) / rolling-IQR21 — robust monthly extension."""
    med = close.rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(close - med, _iqr(close, MDAYS))


def f47_atxs_314_close_minus_median252_over_iqr252(close: pd.Series) -> pd.Series:
    """(close - rolling-median252) / rolling-IQR252 — robust annual extension."""
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(close - med, _iqr(close, YDAYS))


def f47_atxs_315_close_minus_q75_close_past_21(close: pd.Series) -> pd.Series:
    """close - 75th-percentile of close past 21 — signed gap above own upper-quartile (monthly)."""
    return close - close.rolling(MDAYS, min_periods=WDAYS).quantile(0.75)


def f47_atxs_316_close_minus_q95_close_past_252(close: pd.Series) -> pd.Series:
    """close - 95th-percentile of close past 252 — signed gap above own annual 95th-pct."""
    return close - close.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f47_atxs_317_close_minus_median252_over_mad252(close: pd.Series) -> pd.Series:
    """(close - median252) / MAD(close, 252) — annual robust extension (MAD)."""
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(close - med, _mad(close, YDAYS))


def f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21(close: pd.Series) -> pd.Series:
    """(close - trimmed-mean(close, 21)) / trimmed-std(close, 21) — robust to monthly outliers."""
    return _safe_div(close - _trimmed_mean(close, MDAYS), _trimmed_std(close, MDAYS))


# ============================================================
# Bucket NN — Conditional / regime-stratified extension (319-326)
# ============================================================

def f47_atxs_319_mean_ext_in_high_vol_regime_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (c-SMA21)/ATR21 over past 21 bars where ATR21 > 252d median ATR — extension during high-vol."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (a > med)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_320_mean_ext_in_low_vol_regime_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean extension over past 21 bars where ATR21 <= 252d median — extension during low-vol."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (a <= med)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_321_count_extreme_ext_in_high_vol_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 bars with extension > 2 AND ATR21 > 252d median — extreme-ext in high-vol regime."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = ((e > 2.0) & (a > med)).astype(float)
    return cond.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f47_atxs_322_count_extreme_ext_in_low_vol_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 bars with extension > 2 AND ATR21 <= 252d median — extreme-ext in low-vol regime."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = ((e > 2.0) & (a <= med)).astype(float)
    return cond.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f47_atxs_323_current_streak_ext_above_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive bars with (c-SMA21)/ATR21 > 3 — strong-overext streak."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 3.0).where(e.notna(), np.nan)


def f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean extension over past 21 bars where close was in bottom-25% of 252d HL range — atypical: stretched at bottom."""
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos < 0.25)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_325_mean_ext_when_rsi_above_70_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean extension past 21 bars conditioned on RSI(14) > 70 — extension during OB regime."""
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (_rsi(close, 14) > 70.0)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


def f47_atxs_326_mean_ext_when_rsi_below_30_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean extension past 21 conditioned on RSI < 30 — extension during OS regime (rare/distress)."""
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    cond = (_rsi(close, 14) < 30.0)
    return e.where(cond, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()


# ============================================================
# Bucket OO — Pivot point distances (327-336)
# ============================================================

def f47_atxs_327_close_minus_pivot_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - standard pivot) / ATR21 where pivot = (H_prev + L_prev + C_prev)/3."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    return _safe_div(close - p, _atr(high, low, close, MDAYS))


def f47_atxs_328_close_minus_R1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - R1) / ATR21 where R1 = 2*pivot - L_prev — distance from first resistance."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    return _safe_div(close - r1, _atr(high, low, close, MDAYS))


def f47_atxs_329_close_minus_R2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - R2) / ATR21 where R2 = pivot + (H_prev - L_prev)."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return _safe_div(close - r2, _atr(high, low, close, MDAYS))


def f47_atxs_330_close_minus_R3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - R3) / ATR21 where R3 = H_prev + 2*(pivot - L_prev)."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2.0 * (p - low.shift(1))
    return _safe_div(close - r3, _atr(high, low, close, MDAYS))


def f47_atxs_331_close_minus_S1_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - S1) / ATR21 where S1 = 2*pivot - H_prev — distance from first support."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * p - high.shift(1)
    return _safe_div(close - s1, _atr(high, low, close, MDAYS))


def f47_atxs_332_close_minus_S2_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - S2) / ATR21 where S2 = pivot - (H_prev - L_prev)."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = p - (high.shift(1) - low.shift(1))
    return _safe_div(close - s2, _atr(high, low, close, MDAYS))


def f47_atxs_333_close_minus_S3_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - S3) / ATR21 where S3 = L_prev - 2*(H_prev - pivot)."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s3 = low.shift(1) - 2.0 * (high.shift(1) - p)
    return _safe_div(close - s3, _atr(high, low, close, MDAYS))


def f47_atxs_334_pivot_band_position(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - pivot) / (R1 - S1) — position relative to nearest R/S band."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * p - low.shift(1)
    s1 = 2.0 * p - high.shift(1)
    return _safe_div(close - p, r1 - s1)


def f47_atxs_335_close_above_R2_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close > R2 — strong-trend-up indicator (beyond second resistance)."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    return (close > r2).astype(float).where(r2.notna(), np.nan)


def f47_atxs_336_close_above_R3_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close > R3 — extreme overextension above third resistance."""
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2.0 * (p - low.shift(1))
    return (close > r3).astype(float).where(r3.notna(), np.nan)


# ============================================================
# Bucket PP — Fibonacci pivot distances (337-342)
# ============================================================

def f47_atxs_337_close_minus_fib_382_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - (252d-high - 0.382*(252d-range))) / ATR21 — distance from 0.382 Fib retracement."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = hh - 0.382 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_338_close_minus_fib_618_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 0.618 retracement) / ATR21 — golden-ratio retracement distance."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = hh - 0.618 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_339_close_minus_fib_50_retrace_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 50% retracement) / ATR21 — midpoint Fib distance."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = (hh + ll) / 2.0
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_340_close_minus_fib_1272_extension_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - (252d-low + 1.272*range)) / ATR21 — distance from 1.272 Fib extension target."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = ll + 1.272 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_341_close_minus_fib_1618_extension_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 1.618 Fib extension) / ATR21 — distance from golden-ratio extension target."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = ll + 1.618 * (hh - ll)
    return _safe_div(close - fib, _atr(high, low, close, MDAYS))


def f47_atxs_342_position_in_fib_236_786_channel(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - fib236)/(fib786 - fib236) — position within the 0.236-0.786 Fib retracement channel."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    f236 = hh - 0.236 * (hh - ll)
    f786 = hh - 0.786 * (hh - ll)
    return _safe_div(close - f786, f236 - f786)


# ============================================================
# Bucket QQ — Volatility-cone / vol-regime position (343-350)
# ============================================================

def f47_atxs_343_realized_vol_21_pct_rank_252(close: pd.Series) -> pd.Series:
    """Pct rank of 21d realized vol vs trailing 252d distribution."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return rv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_344_realized_vol_63_pct_rank_252(close: pd.Series) -> pd.Series:
    """Pct rank of 63d realized vol."""
    rv = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return rv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_345_vol_cone_position(close: pd.Series) -> pd.Series:
    """(current 21d realized vol - 252d median realized vol) / IQR of realized vol — vol-cone position."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    med = rv.rolling(YDAYS, min_periods=QDAYS).median()
    iqr = _iqr(rv, YDAYS)
    return _safe_div(rv - med, iqr)


def f47_atxs_346_realized_vol_zscore_504(close: pd.Series) -> pd.Series:
    """Z-score of 21d realized vol vs trailing 504d — long-horizon vol-extreme."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(rv, DDAYS_2Y, min_periods=YDAYS)


def f47_atxs_347_vol_of_vol_pct_rank_252(close: pd.Series) -> pd.Series:
    """Pct rank of (21d std of 21d-realized-vol) vs 252d — vol-of-vol percentile."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f47_atxs_348_mean_ext_when_vol_top_quartile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (c-SMA21)/ATR21 past 63 conditioned on ATR21 > 75th-pct of 252d — vol-bucket extension."""
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    q75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    cond = (a > q75)
    return e.where(cond, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f47_atxs_349_mean_ext_when_vol_bottom_quartile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean extension past 63 conditioned on ATR21 < 25th-pct of 252d — extension in vol-drought."""
    a = _atr(high, low, close, MDAYS)
    e = _safe_div(close - _sma(close, MDAYS), a)
    q25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cond = (a < q25)
    return e.where(cond, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f47_atxs_350_vol_top_decile_with_close_above_sma21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 in top decile of 252d AND close > SMA21 — vol-extreme + trend-up state."""
    a = _atr(high, low, close, MDAYS)
    q90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((a > q90) & (close > _sma(close, MDAYS))).astype(float).where(q90.notna(), np.nan)


# ============================================================
# Bucket RR — Extension dynamics / velocity / dwell (351-360)
# ============================================================

def f47_atxs_351_bars_since_ext_crossed_above_zero(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since (c-SMA21)/ATR21 crossed above 0 (from negative) — time-since-trend-flip."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    ev = (e.shift(1) <= 0) & (e > 0)
    return _bars_since_true(ev)


def f47_atxs_352_max_ext_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max (c-SMA21)/ATR21 over past 21 bars — monthly peak extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).max()


def f47_atxs_353_max_ext_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max extension past 63 — quarterly peak extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).max()


def f47_atxs_354_max_ext_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max extension past 252 — annual peak extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).max()


def f47_atxs_355_ext_velocity_5bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(current ext - ext 5 bars ago) / 5 — per-bar extension velocity (5-bar)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e - e.shift(WDAYS)) / float(WDAYS)


def f47_atxs_356_ext_velocity_21bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(current ext - ext 21 bars ago) / 21 — per-bar extension velocity (monthly)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e - e.shift(MDAYS)) / float(MDAYS)


def f47_atxs_357_streak_ext_above_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive bars with extension > 3 (dwell at strong-overext)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 3.0).where(e.notna(), np.nan)


def f47_atxs_358_streak_ext_above_5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive bars with extension > 5 (extreme dwell)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _streak_true(e > 5.0).where(e.notna(), np.nan)


def f47_atxs_359_ext_std_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d std of extension — extension volatility (independent of level)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).std()


def f47_atxs_360_ext_std_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d std of extension — quarterly extension volatility."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).std()


# ============================================================
# Bucket SS — AR / Hurst persistence (361-368)
# ============================================================

def _ar1(s, n):
    """AR(1) coefficient (lag-1 autocorrelation) over rolling n bars."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 4):
            return np.nan
        v = w[valid]
        if v.size < 3:
            return np.nan
        x = v[:-1]; y = v[1:]
        if x.std(ddof=1) == 0 or y.std(ddof=1) == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return s.rolling(n, min_periods=max(n // 3, 4)).apply(_f, raw=True)


def f47_atxs_361_ext_ar1_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coefficient of (c-SMA21)/ATR21 past 63 — extension persistence."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _ar1(e, QDAYS)


def f47_atxs_362_ext_ar1_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coefficient of extension past 252 — annual persistence."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _ar1(e, YDAYS)


def f47_atxs_363_hurst_rs_close_100(close: pd.Series) -> pd.Series:
    """Hurst exponent of close past 100 (R/S analysis approximation) — trend-persistence indicator."""
    return _hurst_rs(close, 100)


def f47_atxs_364_ext_autocorr_lag1_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Autocorrelation lag-1 of extension past 21 — short-window persistence."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).apply(lambda w: float(pd.Series(w).autocorr(lag=1)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f47_atxs_365_ext_autocorr_lag5_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Autocorrelation lag-5 of extension past 63 — medium-lag persistence."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float(pd.Series(w).autocorr(lag=5)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f47_atxs_366_ext_sign_change_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of (close - SMA21) sign changes — extension reversal frequency."""
    e = close - _sma(close, MDAYS)
    sgn = np.sign(e)
    flip = ((sgn != sgn.shift(1)) & e.notna() & e.shift(1).notna()).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_367_mean_reversion_success_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where extension > 2 at t-5 AND extension < 1 at t — mean-reversion success."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    cond = (e.shift(WDAYS) > 2.0) & (e < 1.0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_368_overshoot_recovery_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(21d max extension - current extension) — distance the extension has fallen from its 21d peak."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).max() - e


# ============================================================
# Bucket TT — Extreme-extension survivorship (369-375)
# ============================================================

def f47_atxs_369_bars_since_ext_above_5_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the last bar with (c-SMA21)/ATR21 > 5 — recency of strong-overext."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 5.0)


def f47_atxs_370_bars_since_ext_above_7_past_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since extension > 7 — extreme-overext recency."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 7.0)


def f47_atxs_371_bars_since_ext_above_10_past_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since extension > 10 — very-extreme-overext recency (rare events)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _bars_since_true(e > 10.0)


def f47_atxs_372_ext_above_5_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of bars with extension > 5 — strong-overext frequency."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 5.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_373_ext_above_7_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of bars with extension > 7."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 7.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_374_ext_above_10_count_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """2-year count of bars with extension > 10 — very-extreme-overext multi-year frequency."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 10.0).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_375_max_ext_cummax(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative max of extension since the start of series — lifetime-max extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.cummax()


# ============================================================
#                         REGISTRY 301-375
# ============================================================

_HLC = ["high", "low", "close"]

ATR_EXTENSION_SIGNATURE_BASE_REGISTRY_301_375 = {
    "f47_atxs_301_multi_tf_2way_bull_agreement": {"inputs": _HLC, "func": f47_atxs_301_multi_tf_2way_bull_agreement},
    "f47_atxs_302_multi_tf_3way_bull_agreement": {"inputs": _HLC, "func": f47_atxs_302_multi_tf_3way_bull_agreement},
    "f47_atxs_303_multi_tf_3way_bear_agreement": {"inputs": _HLC, "func": f47_atxs_303_multi_tf_3way_bear_agreement},
    "f47_atxs_304_count_multi_tf_bull_agreement_63": {"inputs": _HLC, "func": f47_atxs_304_count_multi_tf_bull_agreement_63},
    "f47_atxs_305_count_multi_tf_bull_agreement_252": {"inputs": _HLC, "func": f47_atxs_305_count_multi_tf_bull_agreement_252},
    "f47_atxs_306_longest_multi_tf_bull_streak_252": {"inputs": _HLC, "func": f47_atxs_306_longest_multi_tf_bull_streak_252},
    "f47_atxs_307_multi_tf_short_vs_long_disagree": {"inputs": _HLC, "func": f47_atxs_307_multi_tf_short_vs_long_disagree},
    "f47_atxs_308_bars_since_multi_tf_bull_agreement": {"inputs": _HLC, "func": f47_atxs_308_bars_since_multi_tf_bull_agreement},
    "f47_atxs_309_bars_since_multi_tf_bear_agreement": {"inputs": _HLC, "func": f47_atxs_309_bars_since_multi_tf_bear_agreement},
    "f47_atxs_310_multi_tf_magnitude_divergence": {"inputs": _HLC, "func": f47_atxs_310_multi_tf_magnitude_divergence},
    "f47_atxs_311_close_minus_sma21_over_mad21": {"inputs": ["close"], "func": f47_atxs_311_close_minus_sma21_over_mad21},
    "f47_atxs_312_close_minus_sma63_over_mad63": {"inputs": ["close"], "func": f47_atxs_312_close_minus_sma63_over_mad63},
    "f47_atxs_313_close_minus_median21_over_iqr21": {"inputs": ["close"], "func": f47_atxs_313_close_minus_median21_over_iqr21},
    "f47_atxs_314_close_minus_median252_over_iqr252": {"inputs": ["close"], "func": f47_atxs_314_close_minus_median252_over_iqr252},
    "f47_atxs_315_close_minus_q75_close_past_21": {"inputs": ["close"], "func": f47_atxs_315_close_minus_q75_close_past_21},
    "f47_atxs_316_close_minus_q95_close_past_252": {"inputs": ["close"], "func": f47_atxs_316_close_minus_q95_close_past_252},
    "f47_atxs_317_close_minus_median252_over_mad252": {"inputs": ["close"], "func": f47_atxs_317_close_minus_median252_over_mad252},
    "f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21": {"inputs": ["close"], "func": f47_atxs_318_close_minus_trimmed_mean_21_over_trimmed_std_21},
    "f47_atxs_319_mean_ext_in_high_vol_regime_21": {"inputs": _HLC, "func": f47_atxs_319_mean_ext_in_high_vol_regime_21},
    "f47_atxs_320_mean_ext_in_low_vol_regime_21": {"inputs": _HLC, "func": f47_atxs_320_mean_ext_in_low_vol_regime_21},
    "f47_atxs_321_count_extreme_ext_in_high_vol_63": {"inputs": _HLC, "func": f47_atxs_321_count_extreme_ext_in_high_vol_63},
    "f47_atxs_322_count_extreme_ext_in_low_vol_63": {"inputs": _HLC, "func": f47_atxs_322_count_extreme_ext_in_low_vol_63},
    "f47_atxs_323_current_streak_ext_above_3": {"inputs": _HLC, "func": f47_atxs_323_current_streak_ext_above_3},
    "f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21": {"inputs": _HLC, "func": f47_atxs_324_mean_ext_when_in_bottom_25pct_range_21},
    "f47_atxs_325_mean_ext_when_rsi_above_70_past_21": {"inputs": _HLC, "func": f47_atxs_325_mean_ext_when_rsi_above_70_past_21},
    "f47_atxs_326_mean_ext_when_rsi_below_30_past_21": {"inputs": _HLC, "func": f47_atxs_326_mean_ext_when_rsi_below_30_past_21},
    "f47_atxs_327_close_minus_pivot_over_atr21": {"inputs": _HLC, "func": f47_atxs_327_close_minus_pivot_over_atr21},
    "f47_atxs_328_close_minus_R1_over_atr21": {"inputs": _HLC, "func": f47_atxs_328_close_minus_R1_over_atr21},
    "f47_atxs_329_close_minus_R2_over_atr21": {"inputs": _HLC, "func": f47_atxs_329_close_minus_R2_over_atr21},
    "f47_atxs_330_close_minus_R3_over_atr21": {"inputs": _HLC, "func": f47_atxs_330_close_minus_R3_over_atr21},
    "f47_atxs_331_close_minus_S1_over_atr21": {"inputs": _HLC, "func": f47_atxs_331_close_minus_S1_over_atr21},
    "f47_atxs_332_close_minus_S2_over_atr21": {"inputs": _HLC, "func": f47_atxs_332_close_minus_S2_over_atr21},
    "f47_atxs_333_close_minus_S3_over_atr21": {"inputs": _HLC, "func": f47_atxs_333_close_minus_S3_over_atr21},
    "f47_atxs_334_pivot_band_position": {"inputs": _HLC, "func": f47_atxs_334_pivot_band_position},
    "f47_atxs_335_close_above_R2_state": {"inputs": _HLC, "func": f47_atxs_335_close_above_R2_state},
    "f47_atxs_336_close_above_R3_state": {"inputs": _HLC, "func": f47_atxs_336_close_above_R3_state},
    "f47_atxs_337_close_minus_fib_382_retrace_over_atr21": {"inputs": _HLC, "func": f47_atxs_337_close_minus_fib_382_retrace_over_atr21},
    "f47_atxs_338_close_minus_fib_618_retrace_over_atr21": {"inputs": _HLC, "func": f47_atxs_338_close_minus_fib_618_retrace_over_atr21},
    "f47_atxs_339_close_minus_fib_50_retrace_over_atr21": {"inputs": _HLC, "func": f47_atxs_339_close_minus_fib_50_retrace_over_atr21},
    "f47_atxs_340_close_minus_fib_1272_extension_over_atr21": {"inputs": _HLC, "func": f47_atxs_340_close_minus_fib_1272_extension_over_atr21},
    "f47_atxs_341_close_minus_fib_1618_extension_over_atr21": {"inputs": _HLC, "func": f47_atxs_341_close_minus_fib_1618_extension_over_atr21},
    "f47_atxs_342_position_in_fib_236_786_channel": {"inputs": _HLC, "func": f47_atxs_342_position_in_fib_236_786_channel},
    "f47_atxs_343_realized_vol_21_pct_rank_252": {"inputs": ["close"], "func": f47_atxs_343_realized_vol_21_pct_rank_252},
    "f47_atxs_344_realized_vol_63_pct_rank_252": {"inputs": ["close"], "func": f47_atxs_344_realized_vol_63_pct_rank_252},
    "f47_atxs_345_vol_cone_position": {"inputs": ["close"], "func": f47_atxs_345_vol_cone_position},
    "f47_atxs_346_realized_vol_zscore_504": {"inputs": ["close"], "func": f47_atxs_346_realized_vol_zscore_504},
    "f47_atxs_347_vol_of_vol_pct_rank_252": {"inputs": ["close"], "func": f47_atxs_347_vol_of_vol_pct_rank_252},
    "f47_atxs_348_mean_ext_when_vol_top_quartile": {"inputs": _HLC, "func": f47_atxs_348_mean_ext_when_vol_top_quartile},
    "f47_atxs_349_mean_ext_when_vol_bottom_quartile": {"inputs": _HLC, "func": f47_atxs_349_mean_ext_when_vol_bottom_quartile},
    "f47_atxs_350_vol_top_decile_with_close_above_sma21": {"inputs": _HLC, "func": f47_atxs_350_vol_top_decile_with_close_above_sma21},
    "f47_atxs_351_bars_since_ext_crossed_above_zero": {"inputs": _HLC, "func": f47_atxs_351_bars_since_ext_crossed_above_zero},
    "f47_atxs_352_max_ext_past_21": {"inputs": _HLC, "func": f47_atxs_352_max_ext_past_21},
    "f47_atxs_353_max_ext_past_63": {"inputs": _HLC, "func": f47_atxs_353_max_ext_past_63},
    "f47_atxs_354_max_ext_past_252": {"inputs": _HLC, "func": f47_atxs_354_max_ext_past_252},
    "f47_atxs_355_ext_velocity_5bar": {"inputs": _HLC, "func": f47_atxs_355_ext_velocity_5bar},
    "f47_atxs_356_ext_velocity_21bar": {"inputs": _HLC, "func": f47_atxs_356_ext_velocity_21bar},
    "f47_atxs_357_streak_ext_above_3": {"inputs": _HLC, "func": f47_atxs_357_streak_ext_above_3},
    "f47_atxs_358_streak_ext_above_5": {"inputs": _HLC, "func": f47_atxs_358_streak_ext_above_5},
    "f47_atxs_359_ext_std_past_21": {"inputs": _HLC, "func": f47_atxs_359_ext_std_past_21},
    "f47_atxs_360_ext_std_past_63": {"inputs": _HLC, "func": f47_atxs_360_ext_std_past_63},
    "f47_atxs_361_ext_ar1_past_63": {"inputs": _HLC, "func": f47_atxs_361_ext_ar1_past_63},
    "f47_atxs_362_ext_ar1_past_252": {"inputs": _HLC, "func": f47_atxs_362_ext_ar1_past_252},
    "f47_atxs_363_hurst_rs_close_100": {"inputs": ["close"], "func": f47_atxs_363_hurst_rs_close_100},
    "f47_atxs_364_ext_autocorr_lag1_past_21": {"inputs": _HLC, "func": f47_atxs_364_ext_autocorr_lag1_past_21},
    "f47_atxs_365_ext_autocorr_lag5_past_63": {"inputs": _HLC, "func": f47_atxs_365_ext_autocorr_lag5_past_63},
    "f47_atxs_366_ext_sign_change_count_63": {"inputs": _HLC, "func": f47_atxs_366_ext_sign_change_count_63},
    "f47_atxs_367_mean_reversion_success_count_63": {"inputs": _HLC, "func": f47_atxs_367_mean_reversion_success_count_63},
    "f47_atxs_368_overshoot_recovery_21d": {"inputs": _HLC, "func": f47_atxs_368_overshoot_recovery_21d},
    "f47_atxs_369_bars_since_ext_above_5_past_252": {"inputs": _HLC, "func": f47_atxs_369_bars_since_ext_above_5_past_252},
    "f47_atxs_370_bars_since_ext_above_7_past_252": {"inputs": _HLC, "func": f47_atxs_370_bars_since_ext_above_7_past_252},
    "f47_atxs_371_bars_since_ext_above_10_past_504": {"inputs": _HLC, "func": f47_atxs_371_bars_since_ext_above_10_past_504},
    "f47_atxs_372_ext_above_5_count_252": {"inputs": _HLC, "func": f47_atxs_372_ext_above_5_count_252},
    "f47_atxs_373_ext_above_7_count_252": {"inputs": _HLC, "func": f47_atxs_373_ext_above_7_count_252},
    "f47_atxs_374_ext_above_10_count_504": {"inputs": _HLC, "func": f47_atxs_374_ext_above_10_count_504},
    "f47_atxs_375_max_ext_cummax": {"inputs": _HLC, "func": f47_atxs_375_max_ext_cummax},
}
