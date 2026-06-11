"""atr_extension_signature base features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket J: Multi-horizon extension differences (short vs long extension gap).
Bucket K: ATR-normalized HL range / candle body extensions.
Bucket L: Extension trend (rolling slope of normalized-extension).
Bucket M: Cumulative extension area / saturation.
Bucket N: Extension volatility / distribution shape.
Bucket O: Extension from anchor points (52-week low, cum-min, anchored VWAP).
Bucket P: ATR-normalized gap & overshoot.
Bucket Q: Composite ATR-extension signatures.
Bucket R: ATR-normalized peak-distance signatures.

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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _rolling_vwap(close, volume, n):
    num = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _anchored_vwap_from_rolling_low(close, volume, n):
    pv = close * volume
    out = pd.Series(np.nan, index=close.index)
    close_arr = close.to_numpy()
    vol_arr = volume.to_numpy()
    pv_arr = pv.to_numpy()
    for t in range(close_arr.size):
        lo = max(0, t - n + 1)
        w = close_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmin(w))
        k = lo + rel
        sum_pv = np.nansum(pv_arr[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        out.iloc[t] = sum_pv / sum_v
    return out


# ============================================================
# Bucket J — Multi-horizon extension differences (076-083)
# ============================================================

def f47_atxs_076_short_minus_medium_ext_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-SMA21)/ATR21 - (close-SMA63)/ATR21 — short vs medium extension gap."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _sma(close, MDAYS), a) - _safe_div(close - _sma(close, QDAYS), a)


def f47_atxs_077_medium_minus_long_ext_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-SMA63)/ATR21 - (close-SMA252)/ATR21 — quarterly vs annual ext gap."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _sma(close, QDAYS), a) - _safe_div(close - _sma(close, YDAYS), a)


def f47_atxs_078_short_minus_long200_ext_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-SMA21)/ATR21 - (close-SMA200)/ATR21 — short vs 200d ext gap."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _sma(close, MDAYS), a) - _safe_div(close - _sma(close, 200), a)


def f47_atxs_079_ema_minus_sma_ext_21_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-EMA21)/ATR21 - (close-SMA21)/ATR21 — EMA vs SMA extension difference."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - _ema(close, MDAYS), a) - _safe_div(close - _sma(close, MDAYS), a)


def f47_atxs_080_high_gap_21_minus_63_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-21d high)/ATR21 - (close-63d high)/ATR21 — short vs medium high-gap."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - high.rolling(MDAYS, min_periods=WDAYS).max(), a) - _safe_div(close - high.rolling(QDAYS, min_periods=MDAYS).max(), a)


def f47_atxs_081_high_gap_63_minus_252_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-63d high)/ATR21 - (close-252d high)/ATR21 — medium vs annual high-gap."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - high.rolling(QDAYS, min_periods=MDAYS).max(), a) - _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), a)


def f47_atxs_082_extension_horizon_mean_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (close-SMA_k)/ATR21 across k in {21,63,252} — average MA-extension across horizons."""
    a = _atr(high, low, close, MDAYS)
    e1 = _safe_div(close - _sma(close, MDAYS), a)
    e2 = _safe_div(close - _sma(close, QDAYS), a)
    e3 = _safe_div(close - _sma(close, YDAYS), a)
    return (e1 + e2 + e3) / 3.0


def f47_atxs_083_extension_horizon_std_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std (over k in {21,63,252}) of (close-SMA_k)/ATR21 — dispersion of extension across horizons."""
    a = _atr(high, low, close, MDAYS)
    e = pd.concat([
        _safe_div(close - _sma(close, MDAYS), a).rename("e21"),
        _safe_div(close - _sma(close, QDAYS), a).rename("e63"),
        _safe_div(close - _sma(close, YDAYS), a).rename("e252"),
    ], axis=1)
    return e.std(axis=1)


# ============================================================
# Bucket K — HL range / candle body extensions in ATR units (084-090)
# ============================================================

def f47_atxs_084_hl_range_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - low) / ATR21 — today's bar range vs ATR21."""
    return _safe_div(high - low, _atr(high, low, close, MDAYS))


def f47_atxs_085_hl_range_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - low) / ATR63 — bar range vs quarterly ATR."""
    return _safe_div(high - low, _atr(high, low, close, QDAYS))


def f47_atxs_086_body_signed_over_atr21(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - open) / ATR21 — signed candle body in ATR units."""
    return _safe_div(close - open_, _atr(high, low, close, MDAYS))


def f47_atxs_087_body_abs_over_atr21(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close - open| / ATR21 — body magnitude in ATR units."""
    return _safe_div((close - open_).abs(), _atr(high, low, close, MDAYS))


def f47_atxs_088_upper_shadow_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - close) / ATR21 — upper shadow length in ATR units (rejection above)."""
    return _safe_div(high - close, _atr(high, low, close, MDAYS))


def f47_atxs_089_lower_shadow_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - low) / ATR21 — lower-side close position in ATR units."""
    return _safe_div(close - low, _atr(high, low, close, MDAYS))


def f47_atxs_090_max5_tr_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max(TR over past 5) / ATR63 — recent 5-bar TR extreme vs quarterly ATR."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(WDAYS, min_periods=2).max(), _atr(high, low, close, QDAYS))


# ============================================================
# Bucket L — Extension trend (slope of normalized-ext) (091-098)
# ============================================================

def f47_atxs_091_slope21_close_minus_sma21_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of (close - SMA21) / ATR21 — extension trend (monthly)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, MDAYS)


def f47_atxs_092_slope63_close_minus_sma63_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of (close - SMA63) / ATR21 — quarterly extension trend."""
    e = _safe_div(close - _sma(close, QDAYS), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, QDAYS)


def f47_atxs_093_slope252_close_minus_sma252_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d slope of (close - SMA252) / ATR21 — annual extension trend."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, YDAYS)


def f47_atxs_094_slope21_close_minus_252d_high_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of (close - 252d high) / ATR21 — recovery/decay rate from annual high."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, MDAYS)


def f47_atxs_095_slope63_close_minus_vwap63_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of (close - VWAP63) / ATR63 — VWAP-extension trend (quarterly)."""
    e = _safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, QDAYS))
    return _rolling_slope(e, QDAYS)


def f47_atxs_096_slope252_close_minus_ema200_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d slope of (close - EMA200) / ATR21 — long-horizon EMA-extension trend."""
    e = _safe_div(close - _ema(close, 200), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, YDAYS)


def f47_atxs_097_slope63_high_minus_sma252_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d slope of (high - SMA252) / ATR21 — intra-bar extension trend (quarterly)."""
    e = _safe_div(high - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return _rolling_slope(e, QDAYS)


def f47_atxs_098_slope252_close_minus_504d_high_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d slope of (close - 504d high) / ATR252 — multi-year recovery/decay trend."""
    e = _safe_div(close - high.rolling(DDAYS_2Y, min_periods=YDAYS).max(), _atr(high, low, close, YDAYS))
    return _rolling_slope(e, YDAYS)


# ============================================================
# Bucket M — Cumulative extension area (saturation) (099-106)
# ============================================================

def f47_atxs_099_sum_positive_ext_sma21_atr21_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum past 63 of clip((close-SMA21)/ATR21, 0, +inf) — area-above-SMA21 in ATR-units, quarterly."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS)).clip(lower=0)
    return e.rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_100_sum_positive_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum past 252 of clip((close-SMA21)/ATR21, 0, +inf) — annual area-above-SMA21."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS)).clip(lower=0)
    return e.rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_101_sum_positive_ext_sma200_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum past 252 of clip((close-SMA200)/ATR21, 0, +inf) — area-above-SMA200, annual."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS)).clip(lower=0)
    return e.rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_102_sum_positive_ext_vwap63_atr63_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum past 252 of clip((close-VWAP63)/ATR63, 0, +inf) — area-above-VWAP, annual."""
    e = _safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, QDAYS)).clip(lower=0)
    return e.rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_103_signed_integral_ext_sma21_atr21_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum past 63 (signed) of (close-SMA21)/ATR21 — signed quarterly extension area."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_104_signed_integral_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual signed integral of (close-SMA21)/ATR21."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_105_signed_integral_ext_sma252_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual signed integral of (close-SMA252)/ATR21."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).sum().where(e.notna(), np.nan)


def f47_atxs_106_signed_integral_ext_252d_high_atr21_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum past 63 of (close-252d high)/ATR21 — quarterly cumulative gap-from-peak (signed)."""
    e = _safe_div(close - high.rolling(YDAYS, min_periods=QDAYS).max(), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).sum().where(e.notna(), np.nan)


# ============================================================
# Bucket N — Extension volatility / shape (107-114)
# ============================================================

def f47_atxs_107_std_ext_sma21_atr21_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std past 63 of (close-SMA21)/ATR21 — quarterly extension volatility."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).std()


def f47_atxs_108_std_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std past 252 of (close-SMA21)/ATR21 — annual extension volatility."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).std()


def f47_atxs_109_skew_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew past 252 of (close-SMA21)/ATR21 — extension distribution asymmetry."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).skew()


def f47_atxs_110_kurt_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurt past 252 of (close-SMA21)/ATR21 — fat-tail measure of extension regime."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).kurt()


def f47_atxs_111_max_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d max of (close-SMA21)/ATR21 — annual peak monthly-extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).max()


def f47_atxs_112_min_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d min of (close-SMA21)/ATR21 — annual trough monthly-extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).min()


def f47_atxs_113_range_ext_sma21_atr21_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d range (max-min) of (close-SMA21)/ATR21 — annual extension oscillation amplitude."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(YDAYS, min_periods=QDAYS).max() - e.rolling(YDAYS, min_periods=QDAYS).min()


def f47_atxs_114_frac_above_sma21_in_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with close > SMA21 — annual above-SMA-dwell ratio."""
    sma = _sma(close, MDAYS)
    return (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(sma.notna(), np.nan)


# ============================================================
# Bucket O — Extension from anchor points (115-122)
# ============================================================

def f47_atxs_115_close_minus_252d_low_over_atr21_alt(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d low) / ATR21 — extension above 52-week trough (alt formulation, monthly ATR)."""
    return _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, MDAYS))


def f47_atxs_116_close_minus_252d_low_over_atr252_alt(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 252d low) / ATR252 — extension above 52w low, annual ATR."""
    return _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, YDAYS))


def f47_atxs_117_close_minus_cummin_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - cumulative min low) / ATR21 — extension above all-time low (IPO-anchored)."""
    return _safe_div(close - low.cummin(), _atr(high, low, close, MDAYS))


def f47_atxs_118_close_minus_aVWAP_from_252d_low_over_atr21_alt(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Alt label: (close - aVWAP-from-252d-low) / ATR21 — extension above swing-anchored VWAP."""
    return _safe_div(close - _anchored_vwap_from_rolling_low(close, volume, YDAYS), _atr(high, low, close, MDAYS))


def f47_atxs_119_close_minus_aVWAP_from_504d_low_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - aVWAP-from-504d-low) / ATR252 — multi-year swing-anchored VWAP extension."""
    return _safe_div(close - _anchored_vwap_from_rolling_low(close, volume, DDAYS_2Y), _atr(high, low, close, YDAYS))


def f47_atxs_120_close_minus_cummax_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - cumulative max high) / ATR21 — distance below all-time peak in ATR units (<=0)."""
    return _safe_div(close - high.cummax(), _atr(high, low, close, MDAYS))


def f47_atxs_121_close_minus_cummin_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - cumulative min low) / ATR252 — annual-ATR-normalized extension above ATH-trough."""
    return _safe_div(close - low.cummin(), _atr(high, low, close, YDAYS))


def f47_atxs_122_extension_accel_sma21_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-SMA21)/ATR21 minus (close-SMA21)/ATR21 21 bars ago — monthly extension acceleration."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e - e.shift(MDAYS)


# ============================================================
# Bucket P — ATR-normalized gap & overshoot (123-130)
# ============================================================

def f47_atxs_123_gap_open_over_atr21(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(open - prev close) / ATR21 — overnight gap in ATR units (signed)."""
    return _safe_div(open_ - close.shift(1), _atr(high, low, close, MDAYS))


def f47_atxs_124_gap_open_over_atr63(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(open - prev close) / ATR63 — gap normalized by quarterly ATR."""
    return _safe_div(open_ - close.shift(1), _atr(high, low, close, QDAYS))


def f47_atxs_125_high_minus_prev_close_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - prev close) / ATR21 — intra-bar upside overshoot of prior close."""
    return _safe_div(high - close.shift(1), _atr(high, low, close, MDAYS))


def f47_atxs_126_close_minus_prev_close_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - prev close) / ATR21 — 1-bar move in ATR units."""
    return _safe_div(close - close.shift(1), _atr(high, low, close, MDAYS))


def f47_atxs_127_max_5bar_move_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max past 5 of (close - close[t-5]) / ATR21 — 5-bar max move in ATR units."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - close.shift(WDAYS), a).rolling(WDAYS, min_periods=2).max()


def f47_atxs_128_ret21d_pct_over_atr21_pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d %-return / 21d ATR as %-of-close — momentum vs vol ratio (monthly)."""
    r = close.pct_change(MDAYS)
    a_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(r, a_pct)


def f47_atxs_129_ret63d_pct_over_atr63_pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d %-return / 63d ATR-as-%-of-close — quarterly momentum-vs-vol."""
    r = close.pct_change(QDAYS)
    a_pct = _safe_div(_atr(high, low, close, QDAYS), close)
    return _safe_div(r, a_pct)


def f47_atxs_130_peak_21d_ret_over_atr21_in_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max past 252 of ((close - close[t-21]) / ATR21) — peak 21-bar move in ATR units, annual."""
    a = _atr(high, low, close, MDAYS)
    m = _safe_div(close - close.shift(MDAYS), a)
    return m.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket Q — Composite ATR-extension signatures (131-140)
# ============================================================

def f47_atxs_131_count_horizons_ext_above_2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons k in {21, 63, 252} where (close-SMA_k)/ATR21 > 2 — multi-horizon OB ext count."""
    a = _atr(high, low, close, MDAYS)
    c = ((_safe_div(close - _sma(close, MDAYS), a) > 2).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, QDAYS), a) > 2).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, YDAYS), a) > 3).astype(float).fillna(0))
    return c.where(a.notna(), np.nan)


def f47_atxs_132_extension_consensus_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (close-SMA_k)/ATR21 across k in {21, 63, 252} — extension consensus index."""
    a = _atr(high, low, close, MDAYS)
    e1 = _safe_div(close - _sma(close, MDAYS), a)
    e2 = _safe_div(close - _sma(close, QDAYS), a)
    e3 = _safe_div(close - _sma(close, YDAYS), a)
    return (e1 + e2 + e3) / 3.0


def f47_atxs_133_dwell_ext_sma21_atr21_above_2_in_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction past 63 bars (close-SMA21)/ATR21 > 2 — overextension dwell (quarterly)."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(e.notna(), np.nan)


def f47_atxs_134_dwell_ext_sma252_atr21_above_3_in_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction past 63 bars (close-SMA252)/ATR21 > 3 — extreme annual overextension dwell."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return (e > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(e.notna(), np.nan)


def f47_atxs_135_peak_minus_current_ext_in_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d max((close-SMA21)/ATR21) - current value — post-peak mean-reversion velocity."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(MDAYS, min_periods=WDAYS).max() - e


def f47_atxs_136_ext_halflife_proxy_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-life proxy: bars since 63d-max of (close-SMA21)/ATR21 fell to 50% of that max."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    pmax = e.rolling(QDAYS, min_periods=MDAYS).max()
    half = pmax * 0.5
    below_half = e < half
    return _bars_since_true(~below_half)


def f47_atxs_137_ext_vol_regime_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """std past 63 of ext / std past 252 of ext — extension-volatility regime ratio."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return _safe_div(e.rolling(QDAYS, min_periods=MDAYS).std(), e.rolling(YDAYS, min_periods=QDAYS).std())


def f47_atxs_138_ext_kurt_past_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurt past 63 of (close-SMA21)/ATR21 — short-term extension fat-tail measure."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return e.rolling(QDAYS, min_periods=MDAYS).kurt()


def f47_atxs_139_breadth_horizons_ext_above_1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons k in {5,21,50,100,200} where (close-SMA_k)/ATR21 > 1 — multi-horizon ext breadth."""
    a = _atr(high, low, close, MDAYS)
    c = ((_safe_div(close - _sma(close, WDAYS), a) > 1).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, MDAYS), a) > 1).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, 50), a) > 1).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, 100), a) > 1).astype(float).fillna(0)
         + (_safe_div(close - _sma(close, 200), a) > 1).astype(float).fillna(0))
    return c.where(a.notna(), np.nan)


def f47_atxs_140_extreme_ext_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if any of (close-SMA_k)/ATR21 > 5 for k in {21, 63, 252} — extreme-ext composite flag."""
    a = _atr(high, low, close, MDAYS)
    f = ((_safe_div(close - _sma(close, MDAYS), a) > 5)
         | (_safe_div(close - _sma(close, QDAYS), a) > 5)
         | (_safe_div(close - _sma(close, YDAYS), a) > 5))
    return f.astype(float).where(a.notna(), np.nan)


# ============================================================
# Bucket R — ATR-normalized peak-distance signatures (141-150)
# ============================================================

def f47_atxs_141_252d_high_minus_close_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(252d high - close) / ATR21 — distance below annual peak in ATR21 units (drawdown-like)."""
    return _safe_div(high.rolling(YDAYS, min_periods=QDAYS).max() - close, _atr(high, low, close, MDAYS))


def f47_atxs_142_252d_high_minus_close_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(252d high - close) / ATR252 — peak-distance in annual ATR."""
    return _safe_div(high.rolling(YDAYS, min_periods=QDAYS).max() - close, _atr(high, low, close, YDAYS))


def f47_atxs_143_504d_high_minus_close_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(504d high - close) / ATR252 — multi-year peak-distance in annual ATR."""
    return _safe_div(high.rolling(DDAYS_2Y, min_periods=YDAYS).max() - close, _atr(high, low, close, YDAYS))


def f47_atxs_144_drawdown_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown (cum252-max - close) / ATR21 — monthly-ATR drawdown size."""
    dd = high.rolling(YDAYS, min_periods=QDAYS).max() - close
    return _safe_div(dd, _atr(high, low, close, MDAYS))


def f47_atxs_145_drawdown_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown / ATR252 — annual-ATR drawdown size."""
    dd = high.rolling(YDAYS, min_periods=QDAYS).max() - close
    return _safe_div(dd, _atr(high, low, close, YDAYS))


def f47_atxs_146_drawdown_atr21_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (Drawdown / ATR21) — peak-distance percentile context."""
    dd = high.rolling(YDAYS, min_periods=QDAYS).max() - close
    return _rolling_zscore(_safe_div(dd, _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS)


def f47_atxs_147_21d_high_minus_close_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(21d high - close) / ATR21 — short-term gap below monthly high in ATR units."""
    return _safe_div(high.rolling(MDAYS, min_periods=WDAYS).max() - close, _atr(high, low, close, MDAYS))


def f47_atxs_148_63d_high_minus_close_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(63d high - close) / ATR63 — quarterly gap-from-peak in quarterly ATR."""
    return _safe_div(high.rolling(QDAYS, min_periods=MDAYS).max() - close, _atr(high, low, close, QDAYS))


def f47_atxs_149_ext_per_bar_since_252_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized peak-distance / (1 + bars-since-252d-high) — avg decay rate per bar."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = high >= rmax
    bs = _bars_since_true(at_max)
    dd_atr = _safe_div(rmax - close, _atr(high, low, close, MDAYS))
    return _safe_div(dd_atr, bs + 1.0)


def f47_atxs_150_intrabar_excess_over_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - close) / ATR21 — intra-bar excess range (upper shadow as ATR fraction); confirms rejection."""
    return _safe_div(high - close, _atr(high, low, close, MDAYS))


# ============================================================
#                         REGISTRY 076-150
# ============================================================

_OHLC = ["open", "high", "low", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]

ATR_EXTENSION_SIGNATURE_BASE_REGISTRY_076_150 = {
    "f47_atxs_076_short_minus_medium_ext_atr21": {"inputs": _HLC, "func": f47_atxs_076_short_minus_medium_ext_atr21},
    "f47_atxs_077_medium_minus_long_ext_atr21": {"inputs": _HLC, "func": f47_atxs_077_medium_minus_long_ext_atr21},
    "f47_atxs_078_short_minus_long200_ext_atr21": {"inputs": _HLC, "func": f47_atxs_078_short_minus_long200_ext_atr21},
    "f47_atxs_079_ema_minus_sma_ext_21_atr21": {"inputs": _HLC, "func": f47_atxs_079_ema_minus_sma_ext_21_atr21},
    "f47_atxs_080_high_gap_21_minus_63_over_atr21": {"inputs": _HLC, "func": f47_atxs_080_high_gap_21_minus_63_over_atr21},
    "f47_atxs_081_high_gap_63_minus_252_over_atr21": {"inputs": _HLC, "func": f47_atxs_081_high_gap_63_minus_252_over_atr21},
    "f47_atxs_082_extension_horizon_mean_atr21": {"inputs": _HLC, "func": f47_atxs_082_extension_horizon_mean_atr21},
    "f47_atxs_083_extension_horizon_std_atr21": {"inputs": _HLC, "func": f47_atxs_083_extension_horizon_std_atr21},
    "f47_atxs_084_hl_range_over_atr21": {"inputs": _HLC, "func": f47_atxs_084_hl_range_over_atr21},
    "f47_atxs_085_hl_range_over_atr63": {"inputs": _HLC, "func": f47_atxs_085_hl_range_over_atr63},
    "f47_atxs_086_body_signed_over_atr21": {"inputs": _OHLC, "func": f47_atxs_086_body_signed_over_atr21},
    "f47_atxs_087_body_abs_over_atr21": {"inputs": _OHLC, "func": f47_atxs_087_body_abs_over_atr21},
    "f47_atxs_088_upper_shadow_over_atr21": {"inputs": _HLC, "func": f47_atxs_088_upper_shadow_over_atr21},
    "f47_atxs_089_lower_shadow_over_atr21": {"inputs": _HLC, "func": f47_atxs_089_lower_shadow_over_atr21},
    "f47_atxs_090_max5_tr_over_atr63": {"inputs": _HLC, "func": f47_atxs_090_max5_tr_over_atr63},
    "f47_atxs_091_slope21_close_minus_sma21_over_atr21": {"inputs": _HLC, "func": f47_atxs_091_slope21_close_minus_sma21_over_atr21},
    "f47_atxs_092_slope63_close_minus_sma63_over_atr21": {"inputs": _HLC, "func": f47_atxs_092_slope63_close_minus_sma63_over_atr21},
    "f47_atxs_093_slope252_close_minus_sma252_over_atr21": {"inputs": _HLC, "func": f47_atxs_093_slope252_close_minus_sma252_over_atr21},
    "f47_atxs_094_slope21_close_minus_252d_high_over_atr21": {"inputs": _HLC, "func": f47_atxs_094_slope21_close_minus_252d_high_over_atr21},
    "f47_atxs_095_slope63_close_minus_vwap63_over_atr63": {"inputs": _HLCV, "func": f47_atxs_095_slope63_close_minus_vwap63_over_atr63},
    "f47_atxs_096_slope252_close_minus_ema200_over_atr21": {"inputs": _HLC, "func": f47_atxs_096_slope252_close_minus_ema200_over_atr21},
    "f47_atxs_097_slope63_high_minus_sma252_over_atr21": {"inputs": _HLC, "func": f47_atxs_097_slope63_high_minus_sma252_over_atr21},
    "f47_atxs_098_slope252_close_minus_504d_high_over_atr252": {"inputs": _HLC, "func": f47_atxs_098_slope252_close_minus_504d_high_over_atr252},
    "f47_atxs_099_sum_positive_ext_sma21_atr21_63": {"inputs": _HLC, "func": f47_atxs_099_sum_positive_ext_sma21_atr21_63},
    "f47_atxs_100_sum_positive_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_100_sum_positive_ext_sma21_atr21_252},
    "f47_atxs_101_sum_positive_ext_sma200_atr21_252": {"inputs": _HLC, "func": f47_atxs_101_sum_positive_ext_sma200_atr21_252},
    "f47_atxs_102_sum_positive_ext_vwap63_atr63_252": {"inputs": _HLCV, "func": f47_atxs_102_sum_positive_ext_vwap63_atr63_252},
    "f47_atxs_103_signed_integral_ext_sma21_atr21_63": {"inputs": _HLC, "func": f47_atxs_103_signed_integral_ext_sma21_atr21_63},
    "f47_atxs_104_signed_integral_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_104_signed_integral_ext_sma21_atr21_252},
    "f47_atxs_105_signed_integral_ext_sma252_atr21_252": {"inputs": _HLC, "func": f47_atxs_105_signed_integral_ext_sma252_atr21_252},
    "f47_atxs_106_signed_integral_ext_252d_high_atr21_63": {"inputs": _HLC, "func": f47_atxs_106_signed_integral_ext_252d_high_atr21_63},
    "f47_atxs_107_std_ext_sma21_atr21_63": {"inputs": _HLC, "func": f47_atxs_107_std_ext_sma21_atr21_63},
    "f47_atxs_108_std_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_108_std_ext_sma21_atr21_252},
    "f47_atxs_109_skew_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_109_skew_ext_sma21_atr21_252},
    "f47_atxs_110_kurt_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_110_kurt_ext_sma21_atr21_252},
    "f47_atxs_111_max_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_111_max_ext_sma21_atr21_252},
    "f47_atxs_112_min_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_112_min_ext_sma21_atr21_252},
    "f47_atxs_113_range_ext_sma21_atr21_252": {"inputs": _HLC, "func": f47_atxs_113_range_ext_sma21_atr21_252},
    "f47_atxs_114_frac_above_sma21_in_252": {"inputs": ["close"], "func": f47_atxs_114_frac_above_sma21_in_252},
    "f47_atxs_115_close_minus_252d_low_over_atr21_alt": {"inputs": _HLC, "func": f47_atxs_115_close_minus_252d_low_over_atr21_alt},
    "f47_atxs_116_close_minus_252d_low_over_atr252_alt": {"inputs": _HLC, "func": f47_atxs_116_close_minus_252d_low_over_atr252_alt},
    "f47_atxs_117_close_minus_cummin_over_atr21": {"inputs": _HLC, "func": f47_atxs_117_close_minus_cummin_over_atr21},
    "f47_atxs_118_close_minus_aVWAP_from_252d_low_over_atr21_alt": {"inputs": _HLCV, "func": f47_atxs_118_close_minus_aVWAP_from_252d_low_over_atr21_alt},
    "f47_atxs_119_close_minus_aVWAP_from_504d_low_over_atr252": {"inputs": _HLCV, "func": f47_atxs_119_close_minus_aVWAP_from_504d_low_over_atr252},
    "f47_atxs_120_close_minus_cummax_over_atr21": {"inputs": _HLC, "func": f47_atxs_120_close_minus_cummax_over_atr21},
    "f47_atxs_121_close_minus_cummin_over_atr252": {"inputs": _HLC, "func": f47_atxs_121_close_minus_cummin_over_atr252},
    "f47_atxs_122_extension_accel_sma21_atr21": {"inputs": _HLC, "func": f47_atxs_122_extension_accel_sma21_atr21},
    "f47_atxs_123_gap_open_over_atr21": {"inputs": _OHLC, "func": f47_atxs_123_gap_open_over_atr21},
    "f47_atxs_124_gap_open_over_atr63": {"inputs": _OHLC, "func": f47_atxs_124_gap_open_over_atr63},
    "f47_atxs_125_high_minus_prev_close_over_atr21": {"inputs": _HLC, "func": f47_atxs_125_high_minus_prev_close_over_atr21},
    "f47_atxs_126_close_minus_prev_close_over_atr21": {"inputs": _HLC, "func": f47_atxs_126_close_minus_prev_close_over_atr21},
    "f47_atxs_127_max_5bar_move_over_atr21": {"inputs": _HLC, "func": f47_atxs_127_max_5bar_move_over_atr21},
    "f47_atxs_128_ret21d_pct_over_atr21_pct": {"inputs": _HLC, "func": f47_atxs_128_ret21d_pct_over_atr21_pct},
    "f47_atxs_129_ret63d_pct_over_atr63_pct": {"inputs": _HLC, "func": f47_atxs_129_ret63d_pct_over_atr63_pct},
    "f47_atxs_130_peak_21d_ret_over_atr21_in_252": {"inputs": _HLC, "func": f47_atxs_130_peak_21d_ret_over_atr21_in_252},
    "f47_atxs_131_count_horizons_ext_above_2": {"inputs": _HLC, "func": f47_atxs_131_count_horizons_ext_above_2},
    "f47_atxs_132_extension_consensus_mean": {"inputs": _HLC, "func": f47_atxs_132_extension_consensus_mean},
    "f47_atxs_133_dwell_ext_sma21_atr21_above_2_in_63": {"inputs": _HLC, "func": f47_atxs_133_dwell_ext_sma21_atr21_above_2_in_63},
    "f47_atxs_134_dwell_ext_sma252_atr21_above_3_in_63": {"inputs": _HLC, "func": f47_atxs_134_dwell_ext_sma252_atr21_above_3_in_63},
    "f47_atxs_135_peak_minus_current_ext_in_21": {"inputs": _HLC, "func": f47_atxs_135_peak_minus_current_ext_in_21},
    "f47_atxs_136_ext_halflife_proxy_63": {"inputs": _HLC, "func": f47_atxs_136_ext_halflife_proxy_63},
    "f47_atxs_137_ext_vol_regime_ratio": {"inputs": _HLC, "func": f47_atxs_137_ext_vol_regime_ratio},
    "f47_atxs_138_ext_kurt_past_63": {"inputs": _HLC, "func": f47_atxs_138_ext_kurt_past_63},
    "f47_atxs_139_breadth_horizons_ext_above_1": {"inputs": _HLC, "func": f47_atxs_139_breadth_horizons_ext_above_1},
    "f47_atxs_140_extreme_ext_flag": {"inputs": _HLC, "func": f47_atxs_140_extreme_ext_flag},
    "f47_atxs_141_252d_high_minus_close_over_atr21": {"inputs": _HLC, "func": f47_atxs_141_252d_high_minus_close_over_atr21},
    "f47_atxs_142_252d_high_minus_close_over_atr252": {"inputs": _HLC, "func": f47_atxs_142_252d_high_minus_close_over_atr252},
    "f47_atxs_143_504d_high_minus_close_over_atr252": {"inputs": _HLC, "func": f47_atxs_143_504d_high_minus_close_over_atr252},
    "f47_atxs_144_drawdown_over_atr21": {"inputs": _HLC, "func": f47_atxs_144_drawdown_over_atr21},
    "f47_atxs_145_drawdown_over_atr252": {"inputs": _HLC, "func": f47_atxs_145_drawdown_over_atr252},
    "f47_atxs_146_drawdown_atr21_zscore_252": {"inputs": _HLC, "func": f47_atxs_146_drawdown_atr21_zscore_252},
    "f47_atxs_147_21d_high_minus_close_over_atr21": {"inputs": _HLC, "func": f47_atxs_147_21d_high_minus_close_over_atr21},
    "f47_atxs_148_63d_high_minus_close_over_atr63": {"inputs": _HLC, "func": f47_atxs_148_63d_high_minus_close_over_atr63},
    "f47_atxs_149_ext_per_bar_since_252_high": {"inputs": _HLC, "func": f47_atxs_149_ext_per_bar_since_252_high},
    "f47_atxs_150_intrabar_excess_over_atr21": {"inputs": _HLC, "func": f47_atxs_150_intrabar_excess_over_atr21},
}
