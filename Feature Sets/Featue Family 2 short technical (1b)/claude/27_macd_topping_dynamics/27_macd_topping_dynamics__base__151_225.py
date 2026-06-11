"""macd_topping_dynamics base features 151-225 — Pipeline 1b-technical.

Extends 001-150 with alternative-MA MACDs, nested MACDs, Schaff Trend Cycle (STC),
log/HA/TP/VWAP-base MACDs, adaptive/TRIX-base/dynamic-period variants, MACD pattern
detectors, cross-config interactions, and additional signal-quality measures.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return macd, sig, histo


def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return ppo, sig, histo


def _wma(s, n):
    def _f(x):
        m = len(x)
        ww = np.arange(1, m + 1, dtype=float)
        v = ~np.isnan(x)
        if v.sum() < max(n // 2, 2):
            return np.nan
        if v.all():
            return float((x * ww).sum() / ww.sum())
        xx = x[v]; w2 = ww[v]
        return float((xx * w2).sum() / w2.sum())
    return s.rolling(n, min_periods=max(n // 2, 2)).apply(_f, raw=True)


def _hma(s, n):
    """Hull MA: WMA(2*WMA(n/2) - WMA(n), sqrt(n))."""
    half = max(int(n / 2), 2)
    sq = max(int(np.sqrt(n)), 2)
    return _wma(2 * _wma(s, half) - _wma(s, n), sq)


def _dema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _kama(s, n=10, fast=2, slow=30):
    """Kaufman Adaptive MA — efficiency-ratio weighted recursive smoother (vectorized loop)."""
    ch = s.diff(n).abs()
    vol = s.diff().abs().rolling(n, min_periods=max(n // 2, 2)).sum()
    er = _safe_div(ch, vol).clip(0, 1).fillna(0)
    sc = (er * (2.0 / (fast + 1) - 2.0 / (slow + 1)) + 2.0 / (slow + 1)) ** 2
    out = np.full(len(s), np.nan)
    x = s.to_numpy(dtype=float)
    sca = sc.to_numpy(dtype=float)
    prev = np.nan
    for i in range(len(s)):
        if np.isnan(x[i]):
            out[i] = prev
            continue
        if np.isnan(prev):
            prev = x[i]
            out[i] = prev
        else:
            prev = prev + sca[i] * (x[i] - prev)
            out[i] = prev
    return pd.Series(out, index=s.index)


def _zlema(s, n):
    """Zero-Lag EMA: EMA( 2*s - s.shift((n-1)/2), n )."""
    k = max(int((n - 1) / 2), 1)
    return _ema(2.0 * s - s.shift(k), n)


def _macd_generic(ma_func, close, fast=12, slow=26, signal=9):
    """MACD using an arbitrary moving-average function."""
    m = ma_func(close, fast) - ma_func(close, slow)
    sig = _ema(m, signal)
    return m, sig, m - sig


def _bars_since_true(mask: pd.Series) -> pd.Series:
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _stoch(s, n):
    """Stochastic-K: (s - min(n)) / (max(n) - min(n)) scaled 0-100."""
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return 100.0 * _safe_div(s - lo, hi - lo)


def _stc(close, fast=23, slow=50, cyc=10):
    """Schaff Trend Cycle: double-stochastic of MACD line. Standard params (23,50,10).
    Simplified — directly compute %K twice with EMA smoothing factor 0.5."""
    m = _ema(close, fast) - _ema(close, slow)
    k1 = _stoch(m, cyc)
    k1_smooth = k1.ewm(alpha=0.5, adjust=False, min_periods=max(cyc // 2, 2)).mean()
    k2 = _stoch(k1_smooth, cyc)
    return k2.ewm(alpha=0.5, adjust=False, min_periods=max(cyc // 2, 2)).mean()


def _vwma(close, volume, n):
    pv = close * volume
    return _safe_div(
        pv.rolling(n, min_periods=max(n // 3, 2)).sum(),
        volume.rolling(n, min_periods=max(n // 3, 2)).sum(),
    )


def _sign_persist_window(w):
    valid = ~np.isnan(w)
    if valid.sum() < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[valid]
    return float((np.sign(v) == np.sign(last)).sum()) / float(v.size)


def _pct_rank_window(w):
    if np.isnan(w).all():
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[~np.isnan(w)]
    if v.size == 0:
        return np.nan
    return float((v <= last).sum()) / float(v.size)


# ============================================================
# Hull/DEMA/TEMA/KAMA/ZLEMA-based MACD (151-160)
# ============================================================

def f27_mcdt_151_hull_macd_12_26(close: pd.Series) -> pd.Series:
    """Hull-MA-based MACD line (HMA12 - HMA26) — low-lag trend signal."""
    return _hma(close, 12) - _hma(close, 26)


def f27_mcdt_152_dema_macd_12_26(close: pd.Series) -> pd.Series:
    """DEMA-based MACD line (DEMA12 - DEMA26) — reduced-lag trend signal."""
    return _dema(close, 12) - _dema(close, 26)


def f27_mcdt_153_tema_macd_12_26(close: pd.Series) -> pd.Series:
    """TEMA-based MACD line (TEMA12 - TEMA26) — triple-smoothed reduced-lag trend."""
    return _tema(close, 12) - _tema(close, 26)


def f27_mcdt_154_kama_macd_12_26(close: pd.Series) -> pd.Series:
    """KAMA-based MACD line (KAMA12 - KAMA26) — efficiency-ratio adaptive MA difference."""
    return _kama(close, 12) - _kama(close, 26)


def f27_mcdt_155_hull_macd_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if Hull-MACD > 0 — low-lag bullish regime."""
    m = _hma(close, 12) - _hma(close, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_156_dema_macd_signal_bearish_cross(close: pd.Series) -> pd.Series:
    """1 if DEMA-MACD crossed below its 9-EMA signal — DEMA bearish cross trigger."""
    m = _dema(close, 12) - _dema(close, 26)
    s = _ema(m, 9)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_157_tema_macd_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if TEMA-MACD > 0 — low-lag triple-smoothed bullish regime."""
    m = _tema(close, 12) - _tema(close, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_158_kama_macd_zero_cross_down(close: pd.Series) -> pd.Series:
    """1 if KAMA-MACD crossed below zero — adaptive trend rollover."""
    m = _kama(close, 12) - _kama(close, 26)
    return ((m.shift(1) >= 0) & (m < 0)).astype(float).where(m.notna(), np.nan)


def f27_mcdt_159_zero_lag_ema_macd_12_26(close: pd.Series) -> pd.Series:
    """Zero-Lag EMA-based MACD (ZLEMA12 - ZLEMA26) — phase-lead trend signal."""
    return _zlema(close, 12) - _zlema(close, 26)


def f27_mcdt_160_zero_lag_ema_macd_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using ZLEMA-MACD over 63d: price new high but ZLEMA-MACD below prior max."""
    m = _zlema(close, 12) - _zlema(close, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


# ============================================================
# MACD-of-MACD / nested / curl / jerk (161-168)
# ============================================================

def f27_mcdt_161_macd_of_macd_5_13(close: pd.Series) -> pd.Series:
    """MACD applied to the MACD line itself (5,13,5 of MACD line) — nested second-order trend."""
    m, _, _ = _macd(close, 12, 26, 9)
    return _ema(m, 5) - _ema(m, 13)


def f27_mcdt_162_macd_of_macd_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if nested MACD-of-MACD > 0 — second-order bullish state."""
    m, _, _ = _macd(close, 12, 26, 9)
    mm = _ema(m, 5) - _ema(m, 13)
    return (mm > 0).astype(float).where(mm.notna(), np.nan)


def f27_mcdt_163_macd_of_macd_signal_cross(close: pd.Series) -> pd.Series:
    """1 if MACD-of-MACD crossed below its signal — nested bearish-cross trigger."""
    m, _, _ = _macd(close, 12, 26, 9)
    mm = _ema(m, 5) - _ema(m, 13)
    s = _ema(mm, 5)
    d = mm - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_164_macd_of_signal_5_13(close: pd.Series) -> pd.Series:
    """MACD applied to the SIGNAL line (5,13 of signal) — nested smoothed-trend signal."""
    _, s, _ = _macd(close, 12, 26, 9)
    return _ema(s, 5) - _ema(s, 13)


def f27_mcdt_165_macd_of_signal_above_zero(close: pd.Series) -> pd.Series:
    """1 if MACD-of-signal > 0 — nested smoothed-trend bullish state."""
    _, s, _ = _macd(close, 12, 26, 9)
    ms = _ema(s, 5) - _ema(s, 13)
    return (ms > 0).astype(float).where(ms.notna(), np.nan)


def f27_mcdt_166_macd_curl_5d(close: pd.Series) -> pd.Series:
    """5d slope of (5d slope of MACD histogram) — curl-of-histogram (second derivative proxy)."""
    _, _, h = _macd(close)
    sl = _rolling_slope(h, WDAYS)
    return _rolling_slope(sl, WDAYS)


def f27_mcdt_167_macd_jerk_5d_proxy(close: pd.Series) -> pd.Series:
    """First diff of curl-of-histogram — jerk (third-order) proxy."""
    _, _, h = _macd(close)
    sl = _rolling_slope(h, WDAYS)
    return _rolling_slope(sl, WDAYS).diff()


def f27_mcdt_168_macd_second_order_alignment(close: pd.Series) -> pd.Series:
    """1 if MACD < 0 AND 21d slope of MACD < 0 AND curl of histo < 0 — all second-order signs negative."""
    m, _, h = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    sl_h = _rolling_slope(h, WDAYS)
    curl = _rolling_slope(sl_h, WDAYS)
    return ((m < 0) & (sl < 0) & (curl < 0)).astype(float).where(
        m.notna() & sl.notna() & curl.notna(), np.nan)


# ============================================================
# Schaff Trend Cycle (STC, MACD-based) (169-176)
# ============================================================

def f27_mcdt_169_stc_classical_23_50_10(close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle classical (23/50/10) — double-stochastic of MACD line."""
    return _stc(close, 23, 50, 10)


def f27_mcdt_170_stc_above_75_state(close: pd.Series) -> pd.Series:
    """1 if STC > 75 — overbought-zone state."""
    s = _stc(close, 23, 50, 10)
    return (s > 75.0).astype(float).where(s.notna(), np.nan)


def f27_mcdt_171_stc_just_exited_above_75(close: pd.Series) -> pd.Series:
    """1 if STC was > 75 last bar AND <= 75 this bar — OB-exit trigger."""
    s = _stc(close, 23, 50, 10)
    return ((s.shift(1) > 75.0) & (s <= 75.0)).astype(float).where(s.notna(), np.nan)


def f27_mcdt_172_stc_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using STC (price new 63d high but STC below prior 63d STC max)."""
    s = _stc(close, 23, 50, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    s_below = s < s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & s_below).astype(float).where(s.notna(), np.nan)


def f27_mcdt_173_stc_dwell_above_75_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with STC > 75 — quarterly OB dwell."""
    s = _stc(close, 23, 50, 10)
    return (s > 75.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)


def f27_mcdt_174_stc_zscore_252(close: pd.Series) -> pd.Series:
    """252d z-score of STC — distribution-position of STC."""
    return _rolling_zscore(_stc(close, 23, 50, 10), YDAYS, min_periods=QDAYS)


def f27_mcdt_175_stc_bars_since_252_max(close: pd.Series) -> pd.Series:
    """Bars since STC hit its 252d max — recency of STC peak."""
    s = _stc(close, 23, 50, 10)
    at_max = s == s.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f27_mcdt_176_stc_peak_decay_63(close: pd.Series) -> pd.Series:
    """(63d STC max) - STC now — quarterly STC decay since peak."""
    s = _stc(close, 23, 50, 10)
    return s.rolling(QDAYS, min_periods=MDAYS).max() - s


# ============================================================
# Log / HA / TP / VWAP-base MACD (177-185)
# ============================================================

def f27_mcdt_177_macd_on_log_close_12_26(close: pd.Series) -> pd.Series:
    """MACD on log(close) — multiplicative-trend variant, robust to price level."""
    lc = _safe_log(close)
    return _ema(lc, 12) - _ema(lc, 26)


def f27_mcdt_178_macd_on_log_above_zero_state(close: pd.Series) -> pd.Series:
    """1 if MACD-on-log-close > 0 — multiplicative-trend bullish state."""
    lc = _safe_log(close)
    m = _ema(lc, 12) - _ema(lc, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_179_macd_on_log_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using MACD-on-log-close vs price 63d."""
    lc = _safe_log(close)
    m = _ema(lc, 12) - _ema(lc, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


def f27_mcdt_180_volume_weighted_macd_12_26(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VW-MACD: VWMA12(close) - VWMA26(close) — order-flow-weighted trend signal."""
    return _vwma(close, volume, 12) - _vwma(close, volume, 26)


def f27_mcdt_181_vwmacd_above_zero_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VW-MACD > 0 — volume-weighted bullish regime."""
    m = _vwma(close, volume, 12) - _vwma(close, volume, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_182_macd_on_heiken_ashi_close_12_26(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD on Heiken-Ashi close (O+H+L+C)/4 — smoothed-candle trend signal."""
    ha = (open + high + low + close) / 4.0
    return _ema(ha, 12) - _ema(ha, 26)


def f27_mcdt_183_macd_on_heiken_ashi_above_zero(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD-on-Heiken-Ashi > 0 — smoothed-candle bullish state."""
    ha = (open + high + low + close) / 4.0
    m = _ema(ha, 12) - _ema(ha, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_184_macd_on_typical_price_12_26(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD on typical price (H+L+C)/3 — broader-price trend signal."""
    tp = (high + low + close) / 3.0
    return _ema(tp, 12) - _ema(tp, 26)


def f27_mcdt_185_macd_on_typical_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using MACD-on-typical-price vs high (63d horizon)."""
    tp = (high + low + close) / 3.0
    m = _ema(tp, 12) - _ema(tp, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


# ============================================================
# Adaptive / TRIX-base / dynamic-period (186-193)
# ============================================================

def f27_mcdt_186_er_weighted_macd(close: pd.Series) -> pd.Series:
    """Kaufman ER-weighted MACD: classical MACD scaled by efficiency ratio (n=10)."""
    n = 10
    ch = close.diff(n).abs()
    vol = close.diff().abs().rolling(n, min_periods=max(n // 2, 2)).sum()
    er = _safe_div(ch, vol).clip(0, 1)
    m, _, _ = _macd(close, 12, 26, 9)
    return m * er


def f27_mcdt_187_er_weighted_macd_above_zero(close: pd.Series) -> pd.Series:
    """1 if ER-weighted MACD > 0 — efficient-trend bullish state."""
    n = 10
    ch = close.diff(n).abs()
    vol = close.diff().abs().rolling(n, min_periods=max(n // 2, 2)).sum()
    er = _safe_div(ch, vol).clip(0, 1)
    m, _, _ = _macd(close, 12, 26, 9)
    out = m * er
    return (out > 0).astype(float).where(out.notna(), np.nan)


def f27_mcdt_188_adaptive_macd_dc_period_proxy(close: pd.Series) -> pd.Series:
    """Adaptive MACD where the EMA periods scale with rolling std of returns: low-vol -> longer
    periods, high-vol -> shorter. Simplified DC-period proxy.
    Implemented as: classical MACD divided by (1 + 21d return-std z-score relative to 252d)."""
    r = close.pct_change()
    vol21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    z = _rolling_zscore(vol21, YDAYS, min_periods=QDAYS).fillna(0)
    m, _, _ = _macd(close, 12, 26, 9)
    return _safe_div(m, 1.0 + z.abs())


def f27_mcdt_189_frama_macd_proxy(close: pd.Series) -> pd.Series:
    """FRAMA-MACD proxy: fractal-adaptive MA difference, simplified with
    alpha derived from Hurst-like ratio of 16d range vs two 8d ranges."""
    n = 16
    half = n // 2
    hi = close.rolling(n, min_periods=max(n // 2, 2)).max()
    lo = close.rolling(n, min_periods=max(n // 2, 2)).min()
    hi1 = close.rolling(half, min_periods=max(half // 2, 2)).max()
    lo1 = close.rolling(half, min_periods=max(half // 2, 2)).min()
    hi2 = close.shift(half).rolling(half, min_periods=max(half // 2, 2)).max()
    lo2 = close.shift(half).rolling(half, min_periods=max(half // 2, 2)).min()
    n1 = _safe_div(hi1 - lo1, half)
    n2 = _safe_div(hi2 - lo2, half)
    n3 = _safe_div(hi - lo, n)
    d_dim = _safe_div(_safe_log(n1 + n2) - _safe_log(n3), float(np.log(2)))
    alpha = np.exp(-4.6 * (d_dim - 1.0)).clip(0.01, 1.0)
    out = np.full(len(close), np.nan)
    x = close.to_numpy(dtype=float); a = alpha.to_numpy(dtype=float)
    prev = np.nan
    for i in range(len(close)):
        if np.isnan(x[i]) or np.isnan(a[i]):
            out[i] = prev
            continue
        if np.isnan(prev):
            prev = x[i]
        else:
            prev = a[i] * x[i] + (1 - a[i]) * prev
        out[i] = prev
    frama = pd.Series(out, index=close.index)
    return frama - _ema(close, 26)


def f27_mcdt_190_trix_macd_15_5(close: pd.Series) -> pd.Series:
    """TRIX-base MACD: use TRIX(15) = 100 * ROC(EMA(EMA(EMA(close,15),15),15)) as the source
    series, then take MACD(5,13,5) on it."""
    e1 = _ema(close, 15)
    e2 = _ema(e1, 15)
    e3 = _ema(e2, 15)
    trix = 100.0 * e3.pct_change()
    return _ema(trix, 5) - _ema(trix, 13)


def f27_mcdt_191_trix_macd_15_5_above_zero(close: pd.Series) -> pd.Series:
    """1 if TRIX-MACD > 0 — triple-smoothed-momentum bullish state."""
    e1 = _ema(close, 15); e2 = _ema(e1, 15); e3 = _ema(e2, 15)
    trix = 100.0 * e3.pct_change()
    m = _ema(trix, 5) - _ema(trix, 13)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f27_mcdt_192_trix_macd_15_5_signal_cross_down(close: pd.Series) -> pd.Series:
    """1 if TRIX-MACD crossed below its signal (5-EMA) — triple-smooth bearish cross."""
    e1 = _ema(close, 15); e2 = _ema(e1, 15); e3 = _ema(e2, 15)
    trix = 100.0 * e3.pct_change()
    m = _ema(trix, 5) - _ema(trix, 13)
    s = _ema(m, 5)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_193_trix_macd_15_5_div_vs_price_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence using TRIX-MACD vs price 63d."""
    e1 = _ema(close, 15); e2 = _ema(e1, 15); e3 = _ema(e2, 15)
    trix = 100.0 * e3.pct_change()
    m = _ema(trix, 5) - _ema(trix, 13)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan)


# ============================================================
# MACD pattern detectors (194-205)
# ============================================================

def f27_mcdt_194_macd_triangle_pattern_indicator_63(close: pd.Series) -> pd.Series:
    """Converging histogram amplitude over 63 bars — std(histo over last 21) < 0.5 * std(histo over 21-42 ago)."""
    _, _, h = _macd(close)
    recent = h.rolling(MDAYS, min_periods=WDAYS).std()
    prior = h.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).std()
    return ((recent < 0.5 * prior) & (recent.notna()) & (prior.notna())).astype(float).where(h.notna(), np.nan)


def f27_mcdt_195_macd_head_shoulders_in_histo_63(close: pd.Series) -> pd.Series:
    """Histogram H&S proxy: middle 21d max > first 21d max AND middle > last 21d max,
    with first and last similar. 1 = pattern present."""
    _, _, h = _macd(close)
    p1 = h.shift(42).rolling(MDAYS, min_periods=WDAYS).max()
    p2 = h.shift(21).rolling(MDAYS, min_periods=WDAYS).max()
    p3 = h.rolling(MDAYS, min_periods=WDAYS).max()
    sim = (p1 - p3).abs() < 0.5 * (p2 - ((p1 + p3) / 2.0)).abs()
    return ((p2 > p1) & (p2 > p3) & sim).astype(float).where(h.notna(), np.nan)


def f27_mcdt_196_macd_failure_after_signal_cross_count_252(close: pd.Series) -> pd.Series:
    """Count of bullish MACD/signal crosses followed by bearish cross within 5 bars, past 252."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    bu_5_ago = bu.shift(WDAYS)
    be_in_5 = be.rolling(WDAYS, min_periods=1).sum()
    fail = (bu_5_ago > 0) & (be_in_5 > 0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_197_macd_three_peaks_pattern_63(close: pd.Series) -> pd.Series:
    """Three sequential lower histo peaks in past 63d (split into 3 21-bar windows): p1>p2>p3."""
    _, _, h = _macd(close)
    p1 = h.shift(42).rolling(MDAYS, min_periods=WDAYS).max()
    p2 = h.shift(21).rolling(MDAYS, min_periods=WDAYS).max()
    p3 = h.rolling(MDAYS, min_periods=WDAYS).max()
    return ((p1 > p2) & (p2 > p3) & (p1 > 0)).astype(float).where(h.notna(), np.nan)


def f27_mcdt_198_macd_w_pattern_histo_63(close: pd.Series) -> pd.Series:
    """W-pattern in histo: low-high-low-high-low across 5 successive 13-bar windows over 63d."""
    _, _, h = _macd(close)
    s1 = h.shift(52).rolling(13, min_periods=4).min()
    s2 = h.shift(39).rolling(13, min_periods=4).max()
    s3 = h.shift(26).rolling(13, min_periods=4).min()
    s4 = h.shift(13).rolling(13, min_periods=4).max()
    s5 = h.rolling(13, min_periods=4).min()
    cond = (s1 < s2) & (s2 > s3) & (s3 < s4) & (s4 > s5)
    return cond.astype(float).where(h.notna(), np.nan)


def f27_mcdt_199_macd_consecutive_failures_count_252(close: pd.Series) -> pd.Series:
    """Count of consecutive bullish-cross failures (failed within 21d) over past 252d — 2+ failures back-to-back."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    bu_21_ago = bu.shift(MDAYS)
    be_in_21 = be.rolling(MDAYS, min_periods=1).sum()
    fail = ((bu_21_ago > 0) & (be_in_21 > 0)).astype(float)
    # consecutive: fail this bar AND fail within prior 21 bars too
    consec = (fail > 0) & (fail.shift(MDAYS).rolling(MDAYS, min_periods=1).sum() > 0)
    return consec.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_200_macd_premature_cross_count_252(close: pd.Series) -> pd.Series:
    """Count of crosses within 5 bars of an opposite cross — chop/whipsaw count."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    opp_recent = (bu.rolling(WDAYS, min_periods=1).sum() > 0) & (be.rolling(WDAYS, min_periods=1).sum() > 0)
    return opp_recent.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan)


def f27_mcdt_201_macd_dragon_pattern_indicator(close: pd.Series) -> pd.Series:
    """Sharp histo spike then sharp drop: |histo[t-5]| > 2 * 21d-std-of-histo AND
    histo[t] within 25% of zero AND opposite-sign."""
    _, _, h = _macd(close)
    sd = h.rolling(MDAYS, min_periods=WDAYS).std()
    spike = h.shift(WDAYS).abs() > 2.0 * sd.shift(WDAYS)
    flip = (np.sign(h) != np.sign(h.shift(WDAYS))) & (h.abs() < 0.25 * sd)
    return (spike & flip).astype(float).where(sd.notna(), np.nan)


def f27_mcdt_202_macd_three_river_bottom_pattern_proxy(close: pd.Series) -> pd.Series:
    """Three-river-bottom proxy in histo: 3 successive 5-bar windows with declining lows,
    third low is higher than second (failed continuation)."""
    _, _, h = _macd(close)
    l1 = h.shift(10).rolling(WDAYS, min_periods=2).min()
    l2 = h.shift(5).rolling(WDAYS, min_periods=2).min()
    l3 = h.rolling(WDAYS, min_periods=2).min()
    cond = (l1 > l2) & (l3 > l2) & (l2 < 0)
    return cond.astype(float).where(h.notna(), np.nan)


def f27_mcdt_203_macd_consolidation_then_break_indicator(close: pd.Series) -> pd.Series:
    """Low MACD range (21d range < 252d 25th-pct of 21d range) followed by 5d breakout (|histo| > 21d std)."""
    m, _, h = _macd(close)
    r21 = m.rolling(MDAYS, min_periods=WDAYS).max() - m.rolling(MDAYS, min_periods=WDAYS).min()
    q25 = r21.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cons = (r21.shift(WDAYS) < q25.shift(WDAYS))
    sd = h.rolling(MDAYS, min_periods=WDAYS).std()
    brk = h.abs() > sd
    return (cons & brk).astype(float).where(m.notna() & sd.notna(), np.nan)


def f27_mcdt_204_macd_squeeze_indicator_63(close: pd.Series) -> pd.Series:
    """1 if histo 63d range < trailing 252d 10th-percentile of 63d ranges — extreme histo squeeze."""
    _, _, h = _macd(close)
    rng63 = h.rolling(QDAYS, min_periods=MDAYS).max() - h.rolling(QDAYS, min_periods=MDAYS).min()
    q10 = rng63.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (rng63 < q10).astype(float).where(rng63.notna() & q10.notna(), np.nan)


def f27_mcdt_205_macd_breakout_post_squeeze_indicator(close: pd.Series) -> pd.Series:
    """1 if a squeeze (rng63 < q10) was active within last 21 bars AND now |histo| > 21d-std."""
    _, _, h = _macd(close)
    rng63 = h.rolling(QDAYS, min_periods=MDAYS).max() - h.rolling(QDAYS, min_periods=MDAYS).min()
    q10 = rng63.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    sq = (rng63 < q10).astype(float)
    sq_recent = sq.rolling(MDAYS, min_periods=1).sum() > 0
    sd = h.rolling(MDAYS, min_periods=WDAYS).std()
    brk = h.abs() > sd
    return (sq_recent & brk).astype(float).where(h.notna() & sd.notna(), np.nan)


# ============================================================
# Cross-config interaction (206-215)
# ============================================================

def f27_mcdt_206_fast_signal_vs_slow_signal_cross_down(close: pd.Series) -> pd.Series:
    """1 if signal(MACD(5,35,5)) crossed below signal(MACD(19,39,9)) — fast-signal/slow-signal bearish cross."""
    mf = _ema(close, 5) - _ema(close, 35)
    ms = _ema(close, 19) - _ema(close, 39)
    sf = _ema(mf, 5)
    ss = _ema(ms, 9)
    d = sf - ss
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)


def f27_mcdt_207_fast_histo_minus_slow_histo(close: pd.Series) -> pd.Series:
    """Fast-config histo (5,35,5) - slow-config histo (19,39,9) — cycle disagreement in histo."""
    mf = _ema(close, 5) - _ema(close, 35)
    hf = mf - _ema(mf, 5)
    ms = _ema(close, 19) - _ema(close, 39)
    hs = ms - _ema(ms, 9)
    return hf - hs


def f27_mcdt_208_cross_period_macd_dominance(close: pd.Series) -> pd.Series:
    """Which MACD config currently has the largest z-score (0=fast, 1=classical, 2=slow)."""
    z1 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    c, _, _ = _macd(close, 12, 26, 9)
    z2 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    diffs = pd.concat([z1.rename(0), z2.rename(1), z3.rename(2)], axis=1)
    result = diffs.fillna(-np.inf).idxmax(axis=1).where(diffs.notna().any(axis=1), np.nan).astype(float)
    return result


def f27_mcdt_209_macd_period_lead_lag(close: pd.Series) -> pd.Series:
    """Difference between 5d-slope of fast MACD and 5d-slope of slow MACD —
    sign indicates which config is changing first (fast leads / lags slow)."""
    fast = _ema(close, 5) - _ema(close, 35)
    slow = _ema(close, 19) - _ema(close, 39)
    return _rolling_slope(fast, WDAYS) - _rolling_slope(slow, WDAYS)


def f27_mcdt_210_configs_in_agreement_pct_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where all 3 MACD configs share the same sign (all positive or all negative)."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, _ = _macd(close, 12, 26, 9)
    s = _ema(close, 19) - _ema(close, 39)
    agree = ((f * c > 0) & (c * s > 0)).astype(float)
    return agree.rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna(), np.nan)


def f27_mcdt_211_bullish_to_bearish_regime_transition_count_252(close: pd.Series) -> pd.Series:
    """Count of all-3-configs-bullish -> any-config-bearish transitions in past 252d."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, _ = _macd(close, 12, 26, 9)
    s = _ema(close, 19) - _ema(close, 39)
    all_bu = ((f > 0) & (c > 0) & (s > 0)).astype(float)
    any_be = ((f < 0) | (c < 0) | (s < 0)).astype(float)
    trans = (all_bu.shift(1) > 0) & (any_be > 0)
    return trans.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(c.notna(), np.nan)


def f27_mcdt_212_regime_age_macd_above_zero_252(close: pd.Series) -> pd.Series:
    """Average length of MACD-above-zero episodes over trailing 252d."""
    m, _, _ = _macd(close)
    pos = (m > 0).astype(int)
    block = (pos != pos.shift(1)).fillna(False).cumsum()
    seg = pos.groupby(block).cumcount() + 1
    seg = (seg * pos).where(m.notna(), np.nan)
    # average of segment lengths where pos==1
    return seg.where(pos > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f27_mcdt_213_macd_basket_extreme_count(close: pd.Series) -> pd.Series:
    """Count of MACD configs with z-score > 2 (across fast/classical/slow/long basket)."""
    z1 = _rolling_zscore(_ema(close, 5) - _ema(close, 35), YDAYS, min_periods=QDAYS)
    c, _, _ = _macd(close, 12, 26, 9)
    z2 = _rolling_zscore(c, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(_ema(close, 19) - _ema(close, 39), YDAYS, min_periods=QDAYS)
    z4 = _rolling_zscore(_ema(close, 50) - _ema(close, 200), YDAYS, min_periods=QDAYS)
    return ((z1 > 2).astype(float).fillna(0) + (z2 > 2).astype(float).fillna(0)
            + (z3 > 2).astype(float).fillna(0) + (z4 > 2).astype(float).fillna(0)).where(z2.notna(), np.nan)


def f27_mcdt_214_macd_basket_bullish_failure_count(close: pd.Series) -> pd.Series:
    """Count of MACD configs in basket {fast,classical,slow} where a bullish cross failed within 21d (past 252d)."""
    cnt = pd.Series(0.0, index=close.index)
    for f, sl, sg in [(5, 35, 5), (12, 26, 9), (19, 39, 9)]:
        m, s, _ = _macd(close, f, sl, sg)
        d = m - s
        bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
        be = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        bu21 = bu.shift(MDAYS)
        be_in21 = be.rolling(MDAYS, min_periods=1).sum()
        fail = ((bu21 > 0) & (be_in21 > 0)).astype(float)
        cnt = cnt + (fail.rolling(YDAYS, min_periods=QDAYS).sum() > 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f27_mcdt_215_macd_basket_correlation_break_63(close: pd.Series) -> pd.Series:
    """Average pairwise 63d correlation between MACD configs minus same from 21 bars ago — drop signals break."""
    f = _ema(close, 5) - _ema(close, 35)
    c, _, _ = _macd(close, 12, 26, 9)
    s = _ema(close, 19) - _ema(close, 39)
    fc = f.rolling(QDAYS, min_periods=MDAYS).corr(c)
    fs = f.rolling(QDAYS, min_periods=MDAYS).corr(s)
    cs = c.rolling(QDAYS, min_periods=MDAYS).corr(s)
    avg = (fc + fs + cs) / 3.0
    return avg - avg.shift(MDAYS)


# ============================================================
# Additional signal-quality (216-225)
# ============================================================

def f27_mcdt_216_signal_above_macd_state(close: pd.Series) -> pd.Series:
    """1 if signal line > MACD line — flipped (bearish) state."""
    m, s, _ = _macd(close)
    return (s > m).astype(float).where(m.notna() & s.notna(), np.nan)


def f27_mcdt_217_macd_consecutive_diff_signs_streak(close: pd.Series) -> pd.Series:
    """Current consecutive run of MACD-line alternating sign of diff(MACD) — chop streak."""
    m, _, _ = _macd(close)
    d = m.diff()
    alt = (np.sign(d) != np.sign(d.shift(1)))
    return _streak_true(alt).where(m.notna(), np.nan)


def f27_mcdt_218_macd_signal_distance_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score (252d) of (MACD - signal) — distribution-position of histogram itself."""
    m, s, _ = _macd(close)
    return _rolling_zscore(m - s, YDAYS, min_periods=QDAYS)


def f27_mcdt_219_macd_normality_test_jb_252(close: pd.Series) -> pd.Series:
    """Jarque-Bera-like statistic of MACD over 252d: (n/6)*(skew^2 + (kurt-3)^2/4)."""
    m, _, _ = _macd(close)
    sk = m.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = m.rolling(YDAYS, min_periods=QDAYS).kurt()
    return (YDAYS / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)


def f27_mcdt_220_macd_persistence_of_slope_sign_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where 5d-slope-of-MACD has same sign as current — slope-sign persistence."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, WDAYS)
    return sl.rolling(QDAYS, min_periods=MDAYS).apply(_sign_persist_window, raw=True)


def f27_mcdt_221_histo_above_zero_count_in_recent_25d(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 25 with histo > 0 — short-window momentum-of-momentum bullish dwell."""
    _, _, h = _macd(close)
    return (h > 0).astype(float).rolling(25, min_periods=WDAYS).sum().where(h.notna(), np.nan)


def f27_mcdt_222_histo_max_streak_above_zero_252(close: pd.Series) -> pd.Series:
    """Longest histo > 0 streak in past 252 — annual peak histogram-positive streak."""
    _, _, h = _macd(close)
    return _streak_true(h > 0).rolling(YDAYS, min_periods=QDAYS).max().where(h.notna(), np.nan)


def f27_mcdt_223_macd_above_signal_count_above_zero_252(close: pd.Series) -> pd.Series:
    """Count of past 252 bars where MACD > signal AND MACD > 0 — premium-bullish dwell."""
    m, s, _ = _macd(close)
    cond = ((m > s) & (m > 0)).astype(float)
    return cond.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan)


def f27_mcdt_224_macd_signal_distance_pct_rank_252(close: pd.Series) -> pd.Series:
    """252d percentile rank of |MACD - signal| — distribution rank of histogram magnitude."""
    m, s, _ = _macd(close)
    a = (m - s).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)


def f27_mcdt_225_macd_topping_composite_extended_score(high: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate extended-topping score combining new 151-224 indicators:
    sum of {STC OB-exit in 21d, MACD-of-MACD signal cross in 21d, hull MACD<0, dema bearish cross in 21d,
    fast-signal-vs-slow-signal cross-down in 21d, MACD-on-log div in 21d}."""
    s = _stc(close, 23, 50, 10)
    obx = ((s.shift(1) > 75) & (s <= 75)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    m, _, _ = _macd(close, 12, 26, 9)
    mm = _ema(m, 5) - _ema(m, 13)
    mms = _ema(mm, 5)
    mmd = mm - mms
    mmx = ((mmd.shift(1) > 0) & (mmd <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    hm = _hma(close, 12) - _hma(close, 26)
    hm_neg = (hm < 0).astype(float)
    dm = _dema(close, 12) - _dema(close, 26)
    ds = _ema(dm, 9)
    dd = dm - ds
    dmx = ((dd.shift(1) > 0) & (dd <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    mf = _ema(close, 5) - _ema(close, 35)
    msl = _ema(close, 19) - _ema(close, 39)
    sf = _ema(mf, 5); ss = _ema(msl, 9)
    fsd = sf - ss
    fsx = ((fsd.shift(1) > 0) & (fsd <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    lc = _safe_log(close)
    lm = _ema(lc, 12) - _ema(lc, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    lm_below = lm < lm.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    lmdv = (p_new & lm_below).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return (obx.astype(float).fillna(0)
            + mmx.astype(float).fillna(0)
            + hm_neg.fillna(0)
            + dmx.astype(float).fillna(0)
            + fsx.astype(float).fillna(0)
            + lmdv.astype(float).fillna(0)).where(m.notna(), np.nan)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

MACD_TOPPING_DYNAMICS_BASE_REGISTRY_151_225 = {
    "f27_mcdt_151_hull_macd_12_26": {"inputs": ["close"], "func": f27_mcdt_151_hull_macd_12_26},
    "f27_mcdt_152_dema_macd_12_26": {"inputs": ["close"], "func": f27_mcdt_152_dema_macd_12_26},
    "f27_mcdt_153_tema_macd_12_26": {"inputs": ["close"], "func": f27_mcdt_153_tema_macd_12_26},
    "f27_mcdt_154_kama_macd_12_26": {"inputs": ["close"], "func": f27_mcdt_154_kama_macd_12_26},
    "f27_mcdt_155_hull_macd_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_155_hull_macd_above_zero_state},
    "f27_mcdt_156_dema_macd_signal_bearish_cross": {"inputs": ["close"], "func": f27_mcdt_156_dema_macd_signal_bearish_cross},
    "f27_mcdt_157_tema_macd_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_157_tema_macd_above_zero_state},
    "f27_mcdt_158_kama_macd_zero_cross_down": {"inputs": ["close"], "func": f27_mcdt_158_kama_macd_zero_cross_down},
    "f27_mcdt_159_zero_lag_ema_macd_12_26": {"inputs": ["close"], "func": f27_mcdt_159_zero_lag_ema_macd_12_26},
    "f27_mcdt_160_zero_lag_ema_macd_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_160_zero_lag_ema_macd_div_vs_price_63},
    "f27_mcdt_161_macd_of_macd_5_13": {"inputs": ["close"], "func": f27_mcdt_161_macd_of_macd_5_13},
    "f27_mcdt_162_macd_of_macd_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_162_macd_of_macd_above_zero_state},
    "f27_mcdt_163_macd_of_macd_signal_cross": {"inputs": ["close"], "func": f27_mcdt_163_macd_of_macd_signal_cross},
    "f27_mcdt_164_macd_of_signal_5_13": {"inputs": ["close"], "func": f27_mcdt_164_macd_of_signal_5_13},
    "f27_mcdt_165_macd_of_signal_above_zero": {"inputs": ["close"], "func": f27_mcdt_165_macd_of_signal_above_zero},
    "f27_mcdt_166_macd_curl_5d": {"inputs": ["close"], "func": f27_mcdt_166_macd_curl_5d},
    "f27_mcdt_167_macd_jerk_5d_proxy": {"inputs": ["close"], "func": f27_mcdt_167_macd_jerk_5d_proxy},
    "f27_mcdt_168_macd_second_order_alignment": {"inputs": ["close"], "func": f27_mcdt_168_macd_second_order_alignment},
    "f27_mcdt_169_stc_classical_23_50_10": {"inputs": ["close"], "func": f27_mcdt_169_stc_classical_23_50_10},
    "f27_mcdt_170_stc_above_75_state": {"inputs": ["close"], "func": f27_mcdt_170_stc_above_75_state},
    "f27_mcdt_171_stc_just_exited_above_75": {"inputs": ["close"], "func": f27_mcdt_171_stc_just_exited_above_75},
    "f27_mcdt_172_stc_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_172_stc_div_vs_price_63},
    "f27_mcdt_173_stc_dwell_above_75_63": {"inputs": ["close"], "func": f27_mcdt_173_stc_dwell_above_75_63},
    "f27_mcdt_174_stc_zscore_252": {"inputs": ["close"], "func": f27_mcdt_174_stc_zscore_252},
    "f27_mcdt_175_stc_bars_since_252_max": {"inputs": ["close"], "func": f27_mcdt_175_stc_bars_since_252_max},
    "f27_mcdt_176_stc_peak_decay_63": {"inputs": ["close"], "func": f27_mcdt_176_stc_peak_decay_63},
    "f27_mcdt_177_macd_on_log_close_12_26": {"inputs": ["close"], "func": f27_mcdt_177_macd_on_log_close_12_26},
    "f27_mcdt_178_macd_on_log_above_zero_state": {"inputs": ["close"], "func": f27_mcdt_178_macd_on_log_above_zero_state},
    "f27_mcdt_179_macd_on_log_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_179_macd_on_log_div_vs_price_63},
    "f27_mcdt_180_volume_weighted_macd_12_26": {"inputs": ["close", "volume"], "func": f27_mcdt_180_volume_weighted_macd_12_26},
    "f27_mcdt_181_vwmacd_above_zero_state": {"inputs": ["close", "volume"], "func": f27_mcdt_181_vwmacd_above_zero_state},
    "f27_mcdt_182_macd_on_heiken_ashi_close_12_26": {"inputs": ["open", "high", "low", "close"], "func": f27_mcdt_182_macd_on_heiken_ashi_close_12_26},
    "f27_mcdt_183_macd_on_heiken_ashi_above_zero": {"inputs": ["open", "high", "low", "close"], "func": f27_mcdt_183_macd_on_heiken_ashi_above_zero},
    "f27_mcdt_184_macd_on_typical_price_12_26": {"inputs": ["high", "low", "close"], "func": f27_mcdt_184_macd_on_typical_price_12_26},
    "f27_mcdt_185_macd_on_typical_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f27_mcdt_185_macd_on_typical_div_vs_price_63},
    "f27_mcdt_186_er_weighted_macd": {"inputs": ["close"], "func": f27_mcdt_186_er_weighted_macd},
    "f27_mcdt_187_er_weighted_macd_above_zero": {"inputs": ["close"], "func": f27_mcdt_187_er_weighted_macd_above_zero},
    "f27_mcdt_188_adaptive_macd_dc_period_proxy": {"inputs": ["close"], "func": f27_mcdt_188_adaptive_macd_dc_period_proxy},
    "f27_mcdt_189_frama_macd_proxy": {"inputs": ["close"], "func": f27_mcdt_189_frama_macd_proxy},
    "f27_mcdt_190_trix_macd_15_5": {"inputs": ["close"], "func": f27_mcdt_190_trix_macd_15_5},
    "f27_mcdt_191_trix_macd_15_5_above_zero": {"inputs": ["close"], "func": f27_mcdt_191_trix_macd_15_5_above_zero},
    "f27_mcdt_192_trix_macd_15_5_signal_cross_down": {"inputs": ["close"], "func": f27_mcdt_192_trix_macd_15_5_signal_cross_down},
    "f27_mcdt_193_trix_macd_15_5_div_vs_price_63": {"inputs": ["high", "close"], "func": f27_mcdt_193_trix_macd_15_5_div_vs_price_63},
    "f27_mcdt_194_macd_triangle_pattern_indicator_63": {"inputs": ["close"], "func": f27_mcdt_194_macd_triangle_pattern_indicator_63},
    "f27_mcdt_195_macd_head_shoulders_in_histo_63": {"inputs": ["close"], "func": f27_mcdt_195_macd_head_shoulders_in_histo_63},
    "f27_mcdt_196_macd_failure_after_signal_cross_count_252": {"inputs": ["close"], "func": f27_mcdt_196_macd_failure_after_signal_cross_count_252},
    "f27_mcdt_197_macd_three_peaks_pattern_63": {"inputs": ["close"], "func": f27_mcdt_197_macd_three_peaks_pattern_63},
    "f27_mcdt_198_macd_w_pattern_histo_63": {"inputs": ["close"], "func": f27_mcdt_198_macd_w_pattern_histo_63},
    "f27_mcdt_199_macd_consecutive_failures_count_252": {"inputs": ["close"], "func": f27_mcdt_199_macd_consecutive_failures_count_252},
    "f27_mcdt_200_macd_premature_cross_count_252": {"inputs": ["close"], "func": f27_mcdt_200_macd_premature_cross_count_252},
    "f27_mcdt_201_macd_dragon_pattern_indicator": {"inputs": ["close"], "func": f27_mcdt_201_macd_dragon_pattern_indicator},
    "f27_mcdt_202_macd_three_river_bottom_pattern_proxy": {"inputs": ["close"], "func": f27_mcdt_202_macd_three_river_bottom_pattern_proxy},
    "f27_mcdt_203_macd_consolidation_then_break_indicator": {"inputs": ["close"], "func": f27_mcdt_203_macd_consolidation_then_break_indicator},
    "f27_mcdt_204_macd_squeeze_indicator_63": {"inputs": ["close"], "func": f27_mcdt_204_macd_squeeze_indicator_63},
    "f27_mcdt_205_macd_breakout_post_squeeze_indicator": {"inputs": ["close"], "func": f27_mcdt_205_macd_breakout_post_squeeze_indicator},
    "f27_mcdt_206_fast_signal_vs_slow_signal_cross_down": {"inputs": ["close"], "func": f27_mcdt_206_fast_signal_vs_slow_signal_cross_down},
    "f27_mcdt_207_fast_histo_minus_slow_histo": {"inputs": ["close"], "func": f27_mcdt_207_fast_histo_minus_slow_histo},
    "f27_mcdt_208_cross_period_macd_dominance": {"inputs": ["close"], "func": f27_mcdt_208_cross_period_macd_dominance},
    "f27_mcdt_209_macd_period_lead_lag": {"inputs": ["close"], "func": f27_mcdt_209_macd_period_lead_lag},
    "f27_mcdt_210_configs_in_agreement_pct_252": {"inputs": ["close"], "func": f27_mcdt_210_configs_in_agreement_pct_252},
    "f27_mcdt_211_bullish_to_bearish_regime_transition_count_252": {"inputs": ["close"], "func": f27_mcdt_211_bullish_to_bearish_regime_transition_count_252},
    "f27_mcdt_212_regime_age_macd_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_212_regime_age_macd_above_zero_252},
    "f27_mcdt_213_macd_basket_extreme_count": {"inputs": ["close"], "func": f27_mcdt_213_macd_basket_extreme_count},
    "f27_mcdt_214_macd_basket_bullish_failure_count": {"inputs": ["close"], "func": f27_mcdt_214_macd_basket_bullish_failure_count},
    "f27_mcdt_215_macd_basket_correlation_break_63": {"inputs": ["close"], "func": f27_mcdt_215_macd_basket_correlation_break_63},
    "f27_mcdt_216_signal_above_macd_state": {"inputs": ["close"], "func": f27_mcdt_216_signal_above_macd_state},
    "f27_mcdt_217_macd_consecutive_diff_signs_streak": {"inputs": ["close"], "func": f27_mcdt_217_macd_consecutive_diff_signs_streak},
    "f27_mcdt_218_macd_signal_distance_zscore_252": {"inputs": ["close"], "func": f27_mcdt_218_macd_signal_distance_zscore_252},
    "f27_mcdt_219_macd_normality_test_jb_252": {"inputs": ["close"], "func": f27_mcdt_219_macd_normality_test_jb_252},
    "f27_mcdt_220_macd_persistence_of_slope_sign_63": {"inputs": ["close"], "func": f27_mcdt_220_macd_persistence_of_slope_sign_63},
    "f27_mcdt_221_histo_above_zero_count_in_recent_25d": {"inputs": ["close"], "func": f27_mcdt_221_histo_above_zero_count_in_recent_25d},
    "f27_mcdt_222_histo_max_streak_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_222_histo_max_streak_above_zero_252},
    "f27_mcdt_223_macd_above_signal_count_above_zero_252": {"inputs": ["close"], "func": f27_mcdt_223_macd_above_signal_count_above_zero_252},
    "f27_mcdt_224_macd_signal_distance_pct_rank_252": {"inputs": ["close"], "func": f27_mcdt_224_macd_signal_distance_pct_rank_252},
    "f27_mcdt_225_macd_topping_composite_extended_score": {"inputs": ["high", "close"], "func": f27_mcdt_225_macd_topping_composite_extended_score},
}
