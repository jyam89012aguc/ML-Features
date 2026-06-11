"""trix_tsi_cci_family d2 features 151-225 — Pipeline 1b-technical.

75 distinct hypotheses extending 001-150 with MODERN oscillators not previously covered:
Polarized Fractal Efficiency (PFE), Kaufman Efficiency Ratio (ER),
Random Walk Index (RWI), Volatility Quality Index (VQI),
Ehlers Center-Of-Gravity (COG) + Cyber-Cycle proxy,
Donald Dorsey Inertia (LinReg of RVI), Spearman rank-correlation,
TRIX/TSI/CCI/CMO smoothing variants, and cross-family ensemble composites.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers (no cross-family imports).
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _trix(close, n=15):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()


def _tsi(close, n1=25, n2=13):
    m = close.diff()
    e1 = _ema(m, n1)
    e2 = _ema(e1, n2)
    a1 = _ema(m.abs(), n1)
    a2 = _ema(a1, n2)
    return 100.0 * _safe_div(e2, a2)


def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)


def _dpo(close, n=20):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)


def _kst(close):
    roc10 = close.pct_change(10)
    roc15 = close.pct_change(15)
    roc20 = close.pct_change(20)
    roc30 = close.pct_change(30)
    r1 = roc10.rolling(10, min_periods=5).mean()
    r2 = roc15.rolling(10, min_periods=5).mean()
    r3 = roc20.rolling(10, min_periods=5).mean()
    r4 = roc30.rolling(15, min_periods=8).mean()
    return r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4


def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    su = up.rolling(n, min_periods=max(n // 3, 2)).sum()
    sd = dn.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(su - sd, su + sd)


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


# ---------- modern-oscillator helpers ----------

def _pfe(close, n=10):
    """Polarized Fractal Efficiency, smoothed EMA(5).
    PFE(n) = 100 * sign(C - C[n]) * sqrt((C-C[n])^2 + n^2) / sum_{1..n} sqrt(diff^2 + 1)."""
    diff_n = close - close.shift(n)
    num = np.sqrt(diff_n.pow(2) + float(n) ** 2)
    d1 = close.diff()
    path = np.sqrt(d1.pow(2) + 1.0).rolling(n, min_periods=max(n // 3, 2)).sum()
    raw = 100.0 * np.sign(diff_n) * _safe_div(num, path)
    return _ema(raw, 5)


def _efficiency_ratio(close, n=10):
    """Kaufman Efficiency Ratio: |C - C[n]| / sum_{1..n} |dC|."""
    num = (close - close.shift(n)).abs()
    den = close.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _rwi_high(high, low, close, n=14):
    """Random Walk Index high: (H - L[n]) / (ATR(n) * sqrt(n))."""
    atrn = _atr(high, low, close, n)
    return _safe_div(high - low.shift(n), atrn * np.sqrt(float(n)))


def _rwi_low(high, low, close, n=14):
    """Random Walk Index low: (H[n] - L) / (ATR(n) * sqrt(n))."""
    atrn = _atr(high, low, close, n)
    return _safe_div(high.shift(n) - low, atrn * np.sqrt(float(n)))


def _vqi_proxy(open_, high, low, close):
    """Volatility Quality Index proxy: cumulative ((dC/TR + (C-O)/(H-L))/2), EMA5 then EMA9 slope."""
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = _safe_div(close - pc, tr)
    b = _safe_div(close - open_, (high - low).replace(0, np.nan))
    raw = (a + b) / 2.0
    cum = raw.cumsum()
    return _ema(_ema(cum, 5), 9)


def _cog_oscillator(high, low, n=10):
    """Ehlers Center-Of-Gravity on (H+L)/2: -sum_i (i+1)*p[t-i] / sum_i p[t-i] for i=0..n-1."""
    price = (high + low) / 2.0
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        w = w[::-1]  # latest first
        idx = np.arange(1.0, len(w) + 1.0)
        s = w.sum()
        if s == 0:
            return np.nan
        return -float((idx * w).sum() / s) + (len(w) + 1.0) / 2.0  # center
    return price.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _cyber_cycle_proxy(close, alpha=0.07):
    """Simplified Ehlers Cyber-Cycle proxy: 2nd-order IIR on smoothed (H+L)/2 deltas.
    Using close as price proxy. cy[t] = (1-0.5*a)^2 *(p - 2p[1] + p[2]) + 2(1-a)*cy[1] - (1-a)^2 * cy[2]."""
    p = close.copy()
    p_arr = p.to_numpy(dtype=float)
    n = p_arr.size
    cy = np.full(n, np.nan)
    if n < 3:
        return pd.Series(cy, index=close.index)
    cy[0] = 0.0
    cy[1] = 0.0
    a = float(alpha)
    c0 = (1.0 - 0.5 * a) ** 2
    c1 = 2.0 * (1.0 - a)
    c2 = (1.0 - a) ** 2
    for i in range(2, n):
        if np.isnan(p_arr[i]) or np.isnan(p_arr[i - 1]) or np.isnan(p_arr[i - 2]):
            cy[i] = np.nan
            continue
        prev1 = cy[i - 1] if not np.isnan(cy[i - 1]) else 0.0
        prev2 = cy[i - 2] if not np.isnan(cy[i - 2]) else 0.0
        cy[i] = c0 * (p_arr[i] - 2.0 * p_arr[i - 1] + p_arr[i - 2]) + c1 * prev1 - c2 * prev2
    return pd.Series(cy, index=close.index)


def _rvi(close, n=14):
    """Relative Volatility Index variant: stdev of up bars / (stdev up + stdev down), 0..100 scale."""
    d = close.diff()
    up = d.where(d > 0, 0.0)
    dn = (-d).where(d < 0, 0.0)
    su = up.rolling(n, min_periods=max(n // 3, 2)).std()
    sd = dn.rolling(n, min_periods=max(n // 3, 2)).std()
    return 100.0 * _safe_div(su, su + sd)


def _inertia(close, n_lr=20, n_rvi=14):
    """Inertia = LinReg(RVI(n_rvi), n_lr)."""
    rvi = _rvi(close, n_rvi)
    sl = _rolling_slope(rvi, n_lr)
    m = rvi.rolling(n_lr, min_periods=max(n_lr // 3, 2)).mean()
    # endpoint of LR line = mean + slope * ((n-1)/2)
    return m + sl * ((float(n_lr) - 1.0) / 2.0)


def _spearman_rank_corr(s, window):
    """Rolling Spearman rank-correlation of series vs time index."""
    def _f(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        # ranks of values
        order = w.argsort()
        ranks = np.empty_like(order, dtype=float)
        ranks[order] = np.arange(1.0, n + 1.0)
        x = np.arange(1.0, n + 1.0)
        xm = x.mean(); rm = ranks.mean()
        num = ((x - xm) * (ranks - rm)).sum()
        den = np.sqrt(((x - xm) ** 2).sum() * ((ranks - rm) ** 2).sum())
        return float(num / den) if den != 0 else np.nan
    return s.rolling(window, min_periods=max(window // 3, 2)).apply(_f, raw=True)


def _hma(s, n):
    """Hull Moving Average: WMA(2*WMA(n/2) - WMA(n), sqrt(n))."""
    n = max(int(n), 2)
    half = max(n // 2, 1)
    sq = max(int(np.sqrt(n)), 1)
    def _wma(x, k):
        w = np.arange(1.0, k + 1.0)
        return x.rolling(k, min_periods=max(k // 3, 1)).apply(
            lambda v: np.nansum(v * w[-len(v):]) / w[-len(v):].sum() if np.isfinite(v).any() else np.nan,
            raw=True,
        )
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sq)


def _kama(close, n=10, fast=2, slow=30):
    """Kaufman Adaptive Moving Average (simplified, vectorized iterative)."""
    er = _efficiency_ratio(close, n)
    sc_fast = 2.0 / (fast + 1.0)
    sc_slow = 2.0 / (slow + 1.0)
    sc = (er * (sc_fast - sc_slow) + sc_slow) ** 2
    arr = close.to_numpy(dtype=float)
    sc_arr = sc.to_numpy(dtype=float)
    out = np.full(arr.size, np.nan)
    started = False
    prev = np.nan
    for i in range(arr.size):
        if np.isnan(arr[i]):
            continue
        if not started:
            prev = arr[i]
            out[i] = prev
            started = True
            continue
        s = sc_arr[i]
        if np.isnan(s):
            out[i] = prev
            continue
        prev = prev + s * (arr[i] - prev)
        out[i] = prev
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket P — Polarized Fractal Efficiency (151-156)
# ============================================================


def f28_ttcf_151_pfe_10_d2(close: pd.Series) -> pd.Series:
    """PFE(10) smoothed EMA5 — Polarized Fractal Efficiency: -100..+100 trend-vs-noise."""
    return (_pfe(close, 10)).diff().diff()


def f28_ttcf_152_pfe_above_zero_state_d2(close: pd.Series) -> pd.Series:
    """1 if PFE(10) > 0 — bullish polarized fractal regime."""
    p = _pfe(close, 10)
    return ((p > 0).astype(float).where(p.notna(), np.nan)).diff().diff()


def f28_ttcf_153_pfe_zero_cross_down_d2(close: pd.Series) -> pd.Series:
    """1 if PFE crossed below zero — trend-polarization sign flip down."""
    p = _pfe(close, 10)
    return (((p.shift(1) >= 0) & (p < 0)).astype(float).where(p.notna(), np.nan)).diff().diff()


def f28_ttcf_154_pfe_dwell_above_60_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with PFE > 60 — strong-bullish polarization dwell."""
    p = _pfe(close, 10)
    return ((p > 60.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(p.notna(), np.nan)).diff().diff()


def f28_ttcf_155_pfe_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of PFE — distribution-based PFE position."""
    return (_rolling_zscore(_pfe(close, 10), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_156_pfe_div_vs_price_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish PFE divergence vs price (63d horizon)."""
    p = _pfe(close, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    p_below = p < p.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & p_below).astype(float).where(p.notna(), np.nan)).diff().diff()


def f28_ttcf_157_efficiency_ratio_10_d2(close: pd.Series) -> pd.Series:
    """ER(10) — Kaufman Efficiency Ratio over 10 bars; 0 = noise, 1 = pure trend."""
    return (_efficiency_ratio(close, 10)).diff().diff()


def f28_ttcf_158_efficiency_ratio_above_05_state_d2(close: pd.Series) -> pd.Series:
    """1 if ER(10) > 0.5 — trending-regime state."""
    er = _efficiency_ratio(close, 10)
    return ((er > 0.5).astype(float).where(er.notna(), np.nan)).diff().diff()


def f28_ttcf_159_efficiency_ratio_dwell_above_05_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with ER > 0.5 — quarterly trending dwell."""
    er = _efficiency_ratio(close, 10)
    return ((er > 0.5).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(er.notna(), np.nan)).diff().diff()


def f28_ttcf_160_er_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of ER — distribution-based ER position."""
    return (_rolling_zscore(_efficiency_ratio(close, 10), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_161_er_bars_since_252_max_d2(close: pd.Series) -> pd.Series:
    """Bars since ER hit its 252d max — ER trend-strength peak recency."""
    er = _efficiency_ratio(close, 10)
    at_max = er == er.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f28_ttcf_162_er_breakdown_below_03_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if ER crossed below 0.3 (was above) — trend-breakdown to noise."""
    er = _efficiency_ratio(close, 10)
    return (((er.shift(1) >= 0.3) & (er < 0.3)).astype(float).where(er.notna(), np.nan)).diff().diff()


def f28_ttcf_163_er_combined_with_trend_direction_d2(close: pd.Series) -> pd.Series:
    """ER * sign(close - close[10]) — signed trend-strength (trend direction-weighted ER)."""
    er = _efficiency_ratio(close, 10)
    return (er * np.sign(close - close.shift(10))).diff().diff()


def f28_ttcf_164_rwi_high_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RWI high(14) — random-walk distance for bullish move."""
    return (_rwi_high(high, low, close, 14)).diff().diff()


def f28_ttcf_165_rwi_low_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RWI low(14) — random-walk distance for bearish move."""
    return (_rwi_low(high, low, close, 14)).diff().diff()


def f28_ttcf_166_rwi_diff_high_minus_low_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RWI_high(14) - RWI_low(14) — net random-walk trend direction."""
    return (_rwi_high(high, low, close, 14) - _rwi_low(high, low, close, 14)).diff().diff()


def f28_ttcf_167_rwi_high_above_1_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RWI_high(14) > 1 — confirmed non-random uptrend."""
    r = _rwi_high(high, low, close, 14)
    return ((r > 1.0).astype(float).where(r.notna(), np.nan)).diff().diff()


def f28_ttcf_168_rwi_high_just_exited_above_1_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RWI_high crossed back below 1 — trend-strength exit trigger."""
    r = _rwi_high(high, low, close, 14)
    return (((r.shift(1) > 1.0) & (r <= 1.0)).astype(float).where(r.notna(), np.nan)).diff().diff()


def f28_ttcf_169_rwi_high_dwell_above_1_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with RWI_high > 1 — quarterly trend-strength dwell."""
    r = _rwi_high(high, low, close, 14)
    return ((r > 1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff().diff()


def f28_ttcf_170_rwi_div_vs_price_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish RWI_high divergence vs price (63d horizon)."""
    r = _rwi_high(high, low, close, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & r_below).astype(float).where(r.notna(), np.nan)).diff().diff()


def f28_ttcf_171_vqi_5_9_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VQI smoothed EMA5/EMA9 — measures quality (trendiness) of price action."""
    return (_vqi_proxy(open, high, low, close)).diff().diff()


def f28_ttcf_172_vqi_above_zero_state_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if VQI > 0 — positive trend-quality regime."""
    v = _vqi_proxy(open, high, low, close)
    return ((v > 0).astype(float).where(v.notna(), np.nan)).diff().diff()


def f28_ttcf_173_vqi_zero_cross_down_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if VQI crossed below zero — trend-quality sign flip down."""
    v = _vqi_proxy(open, high, low, close)
    return (((v.shift(1) >= 0) & (v < 0)).astype(float).where(v.notna(), np.nan)).diff().diff()


def f28_ttcf_174_vqi_zscore_252_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d z-score of VQI — distribution-based VQI position."""
    return (_rolling_zscore(_vqi_proxy(open, high, low, close), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_175_vqi_div_vs_price_63_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish VQI divergence vs price (63d horizon)."""
    v = _vqi_proxy(open, high, low, close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    v_below = v < v.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & v_below).astype(float).where(v.notna(), np.nan)).diff().diff()


def f28_ttcf_176_vqi_bars_since_252_max_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since VQI hit its 252d max — VQI peak recency."""
    v = _vqi_proxy(open, high, low, close)
    at_max = v == v.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f28_ttcf_177_cog_oscillator_10_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ehlers Center-Of-Gravity oscillator on (H+L)/2, period 10 — phase indicator."""
    return (_cog_oscillator(high, low, 10)).diff().diff()


def f28_ttcf_178_cog_signal_cross_down_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if COG crossed below its EMA3 signal — COG bearish cross trigger."""
    c = _cog_oscillator(high, low, 10)
    s = _ema(c, 3)
    d = c - s
    return (((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)).diff().diff()


def f28_ttcf_179_cog_div_vs_price_63_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish COG divergence vs price (63d horizon)."""
    c = _cog_oscillator(high, low, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & c_below).astype(float).where(c.notna(), np.nan)).diff().diff()


def f28_ttcf_180_cyber_cycle_alpha_07_proxy_d2(close: pd.Series) -> pd.Series:
    """Ehlers Cyber-Cycle proxy (alpha=0.07) — recursive 2nd-order detrended cycle."""
    return (_cyber_cycle_proxy(close, 0.07)).diff().diff()


def f28_ttcf_181_cyber_cycle_above_zero_state_d2(close: pd.Series) -> pd.Series:
    """1 if Cyber-Cycle proxy > 0 — bullish cycle-phase state."""
    cy = _cyber_cycle_proxy(close, 0.07)
    return ((cy > 0).astype(float).where(cy.notna(), np.nan)).diff().diff()


def f28_ttcf_182_cyber_cycle_zero_cross_down_d2(close: pd.Series) -> pd.Series:
    """1 if Cyber-Cycle crossed below zero — cycle-phase rollover."""
    cy = _cyber_cycle_proxy(close, 0.07)
    return (((cy.shift(1) >= 0) & (cy < 0)).astype(float).where(cy.notna(), np.nan)).diff().diff()


def f28_ttcf_183_cyber_cycle_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of Cyber-Cycle proxy — distribution-based cycle position."""
    return (_rolling_zscore(_cyber_cycle_proxy(close, 0.07), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_184_inertia_oscillator_20_14_d2(close: pd.Series) -> pd.Series:
    """Inertia oscillator = LinReg(RVI(14), 20) — smoothed RVI trend indicator."""
    return (_inertia(close, 20, 14)).diff().diff()


def f28_ttcf_185_inertia_above_50_state_d2(close: pd.Series) -> pd.Series:
    """1 if Inertia > 50 — bullish inertia regime."""
    i = _inertia(close, 20, 14)
    return ((i > 50.0).astype(float).where(i.notna(), np.nan)).diff().diff()


def f28_ttcf_186_inertia_dwell_above_50_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with Inertia > 50 — quarterly bullish-inertia dwell."""
    i = _inertia(close, 20, 14)
    return ((i > 50.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(i.notna(), np.nan)).diff().diff()


def f28_ttcf_187_inertia_just_exited_above_50_d2(close: pd.Series) -> pd.Series:
    """1 if Inertia crossed back below 50 — inertia-bullish exit trigger."""
    i = _inertia(close, 20, 14)
    return (((i.shift(1) > 50.0) & (i <= 50.0)).astype(float).where(i.notna(), np.nan)).diff().diff()


def f28_ttcf_188_inertia_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of Inertia — distribution-based inertia position."""
    return (_rolling_zscore(_inertia(close, 20, 14), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_189_inertia_div_vs_price_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish Inertia divergence vs price (63d horizon)."""
    i = _inertia(close, 20, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    i_below = i < i.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & i_below).astype(float).where(i.notna(), np.nan)).diff().diff()


def f28_ttcf_190_spearman_rank_corr_close_time_21_d2(close: pd.Series) -> pd.Series:
    """21d Spearman rank-correlation of close vs time index — monthly monotonic-trend score."""
    return (_spearman_rank_corr(close, MDAYS)).diff().diff()


def f28_ttcf_191_spearman_rank_corr_close_time_63_d2(close: pd.Series) -> pd.Series:
    """63d Spearman rank-correlation of close vs time index — quarterly monotonic-trend score."""
    return (_spearman_rank_corr(close, QDAYS)).diff().diff()


def f28_ttcf_192_spearman_in_extreme_pos_state_d2(close: pd.Series) -> pd.Series:
    """1 if 63d Spearman > 0.8 — extreme-positive monotone trend."""
    s = _spearman_rank_corr(close, QDAYS)
    return ((s > 0.8).astype(float).where(s.notna(), np.nan)).diff().diff()


def f28_ttcf_193_spearman_dwell_above_07_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with 21d Spearman > 0.7 — quarterly strong-trend dwell."""
    s = _spearman_rank_corr(close, MDAYS)
    return ((s > 0.7).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)).diff().diff()


def f28_ttcf_194_spearman_zscore_252_d2(close: pd.Series) -> pd.Series:
    """252d z-score of 21d Spearman — distribution-based monotone-trend position."""
    return (_rolling_zscore(_spearman_rank_corr(close, MDAYS), YDAYS, min_periods=QDAYS)).diff().diff()


def f28_ttcf_195_spearman_just_exited_above_07_d2(close: pd.Series) -> pd.Series:
    """1 if 21d Spearman crossed back below 0.7 — trend-strength exit trigger."""
    s = _spearman_rank_corr(close, MDAYS)
    return (((s.shift(1) > 0.7) & (s <= 0.7)).astype(float).where(s.notna(), np.nan)).diff().diff()


def f28_ttcf_196_trix_hma_smoothed_15_d2(close: pd.Series) -> pd.Series:
    """HMA15-smoothed TRIX(15) — Hull-smoothed momentum (less lag than EMA)."""
    return (_hma(_trix(close, 15), 15)).diff().diff()


def f28_ttcf_197_tsi_volume_weighted_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TSI(25,13) on volume-weighted close (5d rolling VWAP proxy)."""
    vw = _safe_div((close * volume).rolling(WDAYS, min_periods=2).sum(),
                   volume.rolling(WDAYS, min_periods=2).sum())
    return (_tsi(vw, 25, 13)).diff().diff()


def f28_ttcf_198_cci_with_close_replacing_typical_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) using close in place of typical price — pure-close CCI variant."""
    n = 20
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (close - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return (_safe_div(close - sma, 0.015 * mad)).diff().diff()


def f28_ttcf_199_cci_log_normalized_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) computed on log(close) — multiplicative-scale CCI variant."""
    lc = _safe_log(close)
    n = 20
    tp = (_safe_log(high) + _safe_log(low) + lc) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return (_safe_div(tp - sma, 0.015 * mad)).diff().diff()


def f28_ttcf_200_dpo_atr_normalized_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DPO(21) / ATR(21) — vol-adjusted detrended price oscillator."""
    return (_safe_div(_dpo(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff()


def f28_ttcf_201_kst_smoothed_with_hma_d2(close: pd.Series) -> pd.Series:
    """HMA15-smoothed KST — Hull-smoothed long-cycle momentum."""
    return (_hma(_kst(close), 15)).diff().diff()


def f28_ttcf_202_cmo_volume_weighted_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMO(14) on 5d-VWAP-weighted close."""
    vw = _safe_div((close * volume).rolling(WDAYS, min_periods=2).sum(),
                   volume.rolling(WDAYS, min_periods=2).sum())
    return (_cmo(vw, 14)).diff().diff()


def f28_ttcf_203_trix_squared_residual_5_d2(close: pd.Series) -> pd.Series:
    """(TRIX - EMA5(TRIX))^2 — squared short-smoothing residual; high = TRIX volatility."""
    t = _trix(close, 15)
    return ((t - _ema(t, 5)).pow(2)).diff().diff()


def f28_ttcf_204_tsi_kama_smoothed_d2(close: pd.Series) -> pd.Series:
    """KAMA(10) on close, then TSI(25,13) — adaptive-smoothed TSI."""
    return (_tsi(_kama(close, 10), 25, 13)).diff().diff()


def f28_ttcf_205_cci_robust_with_iqr_replacing_mad_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Robust CCI(20) — replaces MAD with IQR/1.349 (Gaussian-equivalent), for tail-resistance."""
    n = 20
    tp = (high + low + close) / 3.0
    med = tp.rolling(n, min_periods=max(n // 3, 2)).median()
    q1 = tp.rolling(n, min_periods=max(n // 3, 2)).quantile(0.25)
    q3 = tp.rolling(n, min_periods=max(n // 3, 2)).quantile(0.75)
    iqr = (q3 - q1) / 1.349
    return (_safe_div(tp - med, 0.015 * iqr)).diff().diff()


def f28_ttcf_206_dpo_zscore_signal_cross_d2(close: pd.Series) -> pd.Series:
    """1 if z-DPO crossed below its EMA9 — DPO zscored signal-cross trigger."""
    z = _rolling_zscore(_dpo(close, MDAYS), YDAYS, min_periods=QDAYS)
    s = _ema(z, 9)
    d = z - s
    return (((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan)).diff().diff()


def f28_ttcf_207_kst_normalized_by_atr_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """KST normalized by ATR(21)/close — vol-adjusted long-cycle momentum."""
    norm = _safe_div(_atr(high, low, close, MDAYS), close)
    return (_safe_div(_kst(close), norm)).diff().diff()


def f28_ttcf_208_cmo_double_smoothed_3_3_d2(close: pd.Series) -> pd.Series:
    """EMA3(EMA3(CMO(14))) — double-smoothed CMO (smoother momentum)."""
    return (_ema(_ema(_cmo(close, 14), 3), 3)).diff().diff()



def _basket_zscores(close: pd.Series) -> list:
    """Returns list of 252d z-scores for the modern + classical oscillators."""
    return [
        _rolling_zscore(_pfe(close, 10), YDAYS, min_periods=QDAYS),
        _rolling_zscore(_efficiency_ratio(close, 10), YDAYS, min_periods=QDAYS),
        _rolling_zscore(_trix(close, 15), YDAYS, min_periods=QDAYS),
        _rolling_zscore(_tsi(close, 25, 13), YDAYS, min_periods=QDAYS),
        _rolling_zscore(_kst(close), YDAYS, min_periods=QDAYS),
        _rolling_zscore(_cmo(close, 14), YDAYS, min_periods=QDAYS),
    ]
def f28_ttcf_209_oscillator_basket_rotation_indicator_d2(close: pd.Series) -> pd.Series:
    """Argmax of z-scores over basket (PFE, ER, TRIX, TSI, KST, CMO). Encoded 0..5."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.fillna(-np.inf).idxmax(axis=1).where(cat.notna().any(axis=1), np.nan).astype(float)).diff().diff()


def f28_ttcf_210_cross_indicator_dispersion_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Std across z-scores of (PFE, ER, TRIX, TSI, KST, CMO) — cross-oscillator dispersion."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.std(axis=1)).diff().diff()


def f28_ttcf_211_triple_top_in_basket_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators in basket {TRIX, TSI, CCI, KST, CMO} with >=3 distinct 63d peaks within
    20% of basket-63d-max — triple-top consensus count."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        near_top = sig >= 0.8 * pmax
        # count of distinct top-touch events in past 63 (consecutive run = 1 event)
        ev = (near_top & ~near_top.shift(1, fill_value=False)).astype(float)
        cnt = cnt + (ev.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_212_lock_step_oscillator_correlation_63_d2(close: pd.Series) -> pd.Series:
    """Mean pairwise 63d Pearson correlation among (PFE, ER, TRIX, TSI, KST, CMO)."""
    cols = [_pfe(close, 10).rename("a"), _efficiency_ratio(close, 10).rename("b"),
            _trix(close, 15).rename("c"), _tsi(close, 25, 13).rename("d"),
            _kst(close).rename("e"), _cmo(close, 14).rename("f")]
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pairs.append(cols[i].rolling(QDAYS, min_periods=MDAYS).corr(cols[j]))
    return (pd.concat(pairs, axis=1).mean(axis=1)).diff().diff()


def f28_ttcf_213_lock_step_decoupling_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if mean pairwise basket correlation dropped > 0.4 vs its 252d rolling mean — decoupling event."""
    c = f28_ttcf_212_lock_step_oscillator_correlation_63_d2(close)
    base = c.rolling(YDAYS, min_periods=QDAYS).mean()
    return (((base - c) > 0.4).astype(float).where(c.notna() & base.notna(), np.nan)).diff().diff()


def f28_ttcf_214_count_indicators_at_extreme_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Count of basket indicators with |z|>2 over 252d — extreme-z breadth."""
    zs = _basket_zscores(close)
    cnt = pd.Series(0.0, index=close.index)
    for z in zs:
        cnt = cnt + (z.abs() > 2.0).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_215_count_indicators_with_failure_pattern_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators making a 63d-lower-high after a 63d-higher-high (Wilder failure)."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        pmax_now = sig.rolling(QDAYS, min_periods=MDAYS).max()
        pmax_prev = pmax_now.shift(QDAYS)
        failed = pmax_now < pmax_prev
        cnt = cnt + failed.astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_216_weighted_basket_avg_zscore_recent_21_d2(close: pd.Series) -> pd.Series:
    """Recent 21d average of mean basket-z — recent ensemble extension."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.mean(axis=1).rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()


def f28_ttcf_217_max_basket_z_score_252_d2(close: pd.Series) -> pd.Series:
    """Max z across basket indicators (252d) — strongest-extreme indicator."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.max(axis=1)).diff().diff()


def f28_ttcf_218_min_basket_z_score_63_d2(close: pd.Series) -> pd.Series:
    """Min z across basket (63d window inputs but 252d z) — weakest-indicator marker."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.min(axis=1)).diff().diff()


def f28_ttcf_219_range_of_basket_z_scores_63_d2(close: pd.Series) -> pd.Series:
    """Max minus min z across basket — spread (range) of indicator extremity."""
    zs = _basket_zscores(close)
    cat = pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1)
    return (cat.max(axis=1) - cat.min(axis=1)).diff().diff()


def f28_ttcf_220_rotation_speed_indicator_63_d2(close: pd.Series) -> pd.Series:
    """Count of changes in argmax-basket-z within last 63 bars — rotation frequency."""
    arg = f28_ttcf_209_oscillator_basket_rotation_indicator_d2(close)
    ch = (arg != arg.shift(1)).astype(float)
    return (ch.rolling(QDAYS, min_periods=MDAYS).sum().where(arg.notna(), np.nan)).diff().diff()


def f28_ttcf_221_regime_alignment_score_252_d2(close: pd.Series) -> pd.Series:
    """Count of basket indicators currently in bullish regime (z>0). Higher = more aligned."""
    zs = _basket_zscores(close)
    cnt = pd.Series(0.0, index=close.index)
    for z in zs:
        cnt = cnt + (z > 0).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_222_terminal_regime_indicator_count_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators in terminal/topping regime: z>2 OR bars-since-252-max < 63."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_pfe(close, 10), _efficiency_ratio(close, 10), _trix(close, 15),
                _tsi(close, 25, 13), _cci(high, low, close, 20), _kst(close), _cmo(close, 14)):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        at_max = sig == sig.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(at_max)
        cnt = cnt + ((z > 2.0) | (bs < QDAYS)).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_223_basket_persistence_of_topping_252_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where at least 4/6 basket indicators were z>1 — sustained topping."""
    zs = _basket_zscores(close)
    cnt = pd.Series(0.0, index=close.index)
    for z in zs:
        cnt = cnt + (z > 1.0).astype(float).fillna(0)
    return ((cnt >= 4).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(close.notna(), np.nan)).diff().diff()


def f28_ttcf_224_basket_decay_velocity_after_extreme_d2(close: pd.Series) -> pd.Series:
    """Mean fractional decline from 63d basket-z max — avg post-extreme velocity."""
    zs = _basket_zscores(close)
    out = pd.Series(0.0, index=close.index)
    cnt = pd.Series(0.0, index=close.index)
    for z in zs:
        pmax = z.rolling(QDAYS, min_periods=MDAYS).max()
        v = _safe_div(pmax - z, pmax.abs())
        out = out + v.fillna(0)
        cnt = cnt + v.notna().astype(float)
    return (_safe_div(out, cnt.replace(0, np.nan))).diff().diff()


def f28_ttcf_225_extended_terminal_topping_composite_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite extended-terminal score = terminal_regime_count + basket-extreme-z + decoupling indicator."""
    a = f28_ttcf_222_terminal_regime_indicator_count_d2(high, low, close).fillna(0)
    b = f28_ttcf_214_count_indicators_at_extreme_zscore_252_d2(close).fillna(0)
    c = f28_ttcf_213_lock_step_decoupling_indicator_d2(close).fillna(0)
    return ((a + b + c).where(close.notna(), np.nan)).diff().diff()


# ============================================================
#                         REGISTRY 151_225
# ============================================================

TRIX_TSI_CCI_FAMILY_D2_REGISTRY_151_225 = {
    "f28_ttcf_151_pfe_10_d2": {"inputs": ["close"], "func": f28_ttcf_151_pfe_10_d2},
    "f28_ttcf_152_pfe_above_zero_state_d2": {"inputs": ["close"], "func": f28_ttcf_152_pfe_above_zero_state_d2},
    "f28_ttcf_153_pfe_zero_cross_down_d2": {"inputs": ["close"], "func": f28_ttcf_153_pfe_zero_cross_down_d2},
    "f28_ttcf_154_pfe_dwell_above_60_63_d2": {"inputs": ["close"], "func": f28_ttcf_154_pfe_dwell_above_60_63_d2},
    "f28_ttcf_155_pfe_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_155_pfe_zscore_252_d2},
    "f28_ttcf_156_pfe_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f28_ttcf_156_pfe_div_vs_price_63_d2},
    "f28_ttcf_157_efficiency_ratio_10_d2": {"inputs": ["close"], "func": f28_ttcf_157_efficiency_ratio_10_d2},
    "f28_ttcf_158_efficiency_ratio_above_05_state_d2": {"inputs": ["close"], "func": f28_ttcf_158_efficiency_ratio_above_05_state_d2},
    "f28_ttcf_159_efficiency_ratio_dwell_above_05_63_d2": {"inputs": ["close"], "func": f28_ttcf_159_efficiency_ratio_dwell_above_05_63_d2},
    "f28_ttcf_160_er_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_160_er_zscore_252_d2},
    "f28_ttcf_161_er_bars_since_252_max_d2": {"inputs": ["close"], "func": f28_ttcf_161_er_bars_since_252_max_d2},
    "f28_ttcf_162_er_breakdown_below_03_indicator_d2": {"inputs": ["close"], "func": f28_ttcf_162_er_breakdown_below_03_indicator_d2},
    "f28_ttcf_163_er_combined_with_trend_direction_d2": {"inputs": ["close"], "func": f28_ttcf_163_er_combined_with_trend_direction_d2},
    "f28_ttcf_164_rwi_high_14_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_164_rwi_high_14_d2},
    "f28_ttcf_165_rwi_low_14_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_165_rwi_low_14_d2},
    "f28_ttcf_166_rwi_diff_high_minus_low_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_166_rwi_diff_high_minus_low_d2},
    "f28_ttcf_167_rwi_high_above_1_state_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_167_rwi_high_above_1_state_d2},
    "f28_ttcf_168_rwi_high_just_exited_above_1_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_168_rwi_high_just_exited_above_1_d2},
    "f28_ttcf_169_rwi_high_dwell_above_1_63_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_169_rwi_high_dwell_above_1_63_d2},
    "f28_ttcf_170_rwi_div_vs_price_63_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_170_rwi_div_vs_price_63_d2},
    "f28_ttcf_171_vqi_5_9_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_171_vqi_5_9_d2},
    "f28_ttcf_172_vqi_above_zero_state_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_172_vqi_above_zero_state_d2},
    "f28_ttcf_173_vqi_zero_cross_down_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_173_vqi_zero_cross_down_d2},
    "f28_ttcf_174_vqi_zscore_252_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_174_vqi_zscore_252_d2},
    "f28_ttcf_175_vqi_div_vs_price_63_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_175_vqi_div_vs_price_63_d2},
    "f28_ttcf_176_vqi_bars_since_252_max_d2": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_176_vqi_bars_since_252_max_d2},
    "f28_ttcf_177_cog_oscillator_10_d2": {"inputs": ["high", "low"], "func": f28_ttcf_177_cog_oscillator_10_d2},
    "f28_ttcf_178_cog_signal_cross_down_d2": {"inputs": ["high", "low"], "func": f28_ttcf_178_cog_signal_cross_down_d2},
    "f28_ttcf_179_cog_div_vs_price_63_d2": {"inputs": ["high", "low"], "func": f28_ttcf_179_cog_div_vs_price_63_d2},
    "f28_ttcf_180_cyber_cycle_alpha_07_proxy_d2": {"inputs": ["close"], "func": f28_ttcf_180_cyber_cycle_alpha_07_proxy_d2},
    "f28_ttcf_181_cyber_cycle_above_zero_state_d2": {"inputs": ["close"], "func": f28_ttcf_181_cyber_cycle_above_zero_state_d2},
    "f28_ttcf_182_cyber_cycle_zero_cross_down_d2": {"inputs": ["close"], "func": f28_ttcf_182_cyber_cycle_zero_cross_down_d2},
    "f28_ttcf_183_cyber_cycle_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_183_cyber_cycle_zscore_252_d2},
    "f28_ttcf_184_inertia_oscillator_20_14_d2": {"inputs": ["close"], "func": f28_ttcf_184_inertia_oscillator_20_14_d2},
    "f28_ttcf_185_inertia_above_50_state_d2": {"inputs": ["close"], "func": f28_ttcf_185_inertia_above_50_state_d2},
    "f28_ttcf_186_inertia_dwell_above_50_63_d2": {"inputs": ["close"], "func": f28_ttcf_186_inertia_dwell_above_50_63_d2},
    "f28_ttcf_187_inertia_just_exited_above_50_d2": {"inputs": ["close"], "func": f28_ttcf_187_inertia_just_exited_above_50_d2},
    "f28_ttcf_188_inertia_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_188_inertia_zscore_252_d2},
    "f28_ttcf_189_inertia_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f28_ttcf_189_inertia_div_vs_price_63_d2},
    "f28_ttcf_190_spearman_rank_corr_close_time_21_d2": {"inputs": ["close"], "func": f28_ttcf_190_spearman_rank_corr_close_time_21_d2},
    "f28_ttcf_191_spearman_rank_corr_close_time_63_d2": {"inputs": ["close"], "func": f28_ttcf_191_spearman_rank_corr_close_time_63_d2},
    "f28_ttcf_192_spearman_in_extreme_pos_state_d2": {"inputs": ["close"], "func": f28_ttcf_192_spearman_in_extreme_pos_state_d2},
    "f28_ttcf_193_spearman_dwell_above_07_63_d2": {"inputs": ["close"], "func": f28_ttcf_193_spearman_dwell_above_07_63_d2},
    "f28_ttcf_194_spearman_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_194_spearman_zscore_252_d2},
    "f28_ttcf_195_spearman_just_exited_above_07_d2": {"inputs": ["close"], "func": f28_ttcf_195_spearman_just_exited_above_07_d2},
    "f28_ttcf_196_trix_hma_smoothed_15_d2": {"inputs": ["close"], "func": f28_ttcf_196_trix_hma_smoothed_15_d2},
    "f28_ttcf_197_tsi_volume_weighted_d2": {"inputs": ["close", "volume"], "func": f28_ttcf_197_tsi_volume_weighted_d2},
    "f28_ttcf_198_cci_with_close_replacing_typical_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_198_cci_with_close_replacing_typical_d2},
    "f28_ttcf_199_cci_log_normalized_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_199_cci_log_normalized_d2},
    "f28_ttcf_200_dpo_atr_normalized_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_200_dpo_atr_normalized_d2},
    "f28_ttcf_201_kst_smoothed_with_hma_d2": {"inputs": ["close"], "func": f28_ttcf_201_kst_smoothed_with_hma_d2},
    "f28_ttcf_202_cmo_volume_weighted_d2": {"inputs": ["close", "volume"], "func": f28_ttcf_202_cmo_volume_weighted_d2},
    "f28_ttcf_203_trix_squared_residual_5_d2": {"inputs": ["close"], "func": f28_ttcf_203_trix_squared_residual_5_d2},
    "f28_ttcf_204_tsi_kama_smoothed_d2": {"inputs": ["close"], "func": f28_ttcf_204_tsi_kama_smoothed_d2},
    "f28_ttcf_205_cci_robust_with_iqr_replacing_mad_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_205_cci_robust_with_iqr_replacing_mad_d2},
    "f28_ttcf_206_dpo_zscore_signal_cross_d2": {"inputs": ["close"], "func": f28_ttcf_206_dpo_zscore_signal_cross_d2},
    "f28_ttcf_207_kst_normalized_by_atr_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_207_kst_normalized_by_atr_d2},
    "f28_ttcf_208_cmo_double_smoothed_3_3_d2": {"inputs": ["close"], "func": f28_ttcf_208_cmo_double_smoothed_3_3_d2},
    "f28_ttcf_209_oscillator_basket_rotation_indicator_d2": {"inputs": ["close"], "func": f28_ttcf_209_oscillator_basket_rotation_indicator_d2},
    "f28_ttcf_210_cross_indicator_dispersion_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_210_cross_indicator_dispersion_zscore_252_d2},
    "f28_ttcf_211_triple_top_in_basket_count_63_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_211_triple_top_in_basket_count_63_d2},
    "f28_ttcf_212_lock_step_oscillator_correlation_63_d2": {"inputs": ["close"], "func": f28_ttcf_212_lock_step_oscillator_correlation_63_d2},
    "f28_ttcf_213_lock_step_decoupling_indicator_d2": {"inputs": ["close"], "func": f28_ttcf_213_lock_step_decoupling_indicator_d2},
    "f28_ttcf_214_count_indicators_at_extreme_zscore_252_d2": {"inputs": ["close"], "func": f28_ttcf_214_count_indicators_at_extreme_zscore_252_d2},
    "f28_ttcf_215_count_indicators_with_failure_pattern_63_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_215_count_indicators_with_failure_pattern_63_d2},
    "f28_ttcf_216_weighted_basket_avg_zscore_recent_21_d2": {"inputs": ["close"], "func": f28_ttcf_216_weighted_basket_avg_zscore_recent_21_d2},
    "f28_ttcf_217_max_basket_z_score_252_d2": {"inputs": ["close"], "func": f28_ttcf_217_max_basket_z_score_252_d2},
    "f28_ttcf_218_min_basket_z_score_63_d2": {"inputs": ["close"], "func": f28_ttcf_218_min_basket_z_score_63_d2},
    "f28_ttcf_219_range_of_basket_z_scores_63_d2": {"inputs": ["close"], "func": f28_ttcf_219_range_of_basket_z_scores_63_d2},
    "f28_ttcf_220_rotation_speed_indicator_63_d2": {"inputs": ["close"], "func": f28_ttcf_220_rotation_speed_indicator_63_d2},
    "f28_ttcf_221_regime_alignment_score_252_d2": {"inputs": ["close"], "func": f28_ttcf_221_regime_alignment_score_252_d2},
    "f28_ttcf_222_terminal_regime_indicator_count_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_222_terminal_regime_indicator_count_d2},
    "f28_ttcf_223_basket_persistence_of_topping_252_d2": {"inputs": ["close"], "func": f28_ttcf_223_basket_persistence_of_topping_252_d2},
    "f28_ttcf_224_basket_decay_velocity_after_extreme_d2": {"inputs": ["close"], "func": f28_ttcf_224_basket_decay_velocity_after_extreme_d2},
    "f28_ttcf_225_extended_terminal_topping_composite_d2": {"inputs": ["high", "low", "close"], "func": f28_ttcf_225_extended_terminal_topping_composite_d2},
}
