"""trix_tsi_cci_family base features 076-150 — Pipeline 1b-technical.

Continues 001-075 with:
G: multi-horizon TRIX (5/50/100 + fast-vs-classical).
H: multi-horizon CCI (5/100/252 + ensemble).
I: multi-horizon CMO + multi-horizon TSI.
J: DPO multi-period + ensemble.
K: KST variants + short-KST.
L: cross-indicator alignment / ensemble counts.
M: composite topping + decay signals.
N: stationarity / detrending of indicators.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
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


def _short_kst(close):
    """Short-cycle KST using ROCs 5/10/15/20 with shorter MAs — distinct hypothesis from classic KST."""
    r1 = close.pct_change(5).rolling(5, min_periods=3).mean()
    r2 = close.pct_change(10).rolling(5, min_periods=3).mean()
    r3 = close.pct_change(15).rolling(5, min_periods=3).mean()
    r4 = close.pct_change(20).rolling(10, min_periods=5).mean()
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


# ============================================================
# Bucket G — multi-horizon TRIX (076-082)
# ============================================================

def f28_ttcf_076_trix_5_short(close: pd.Series) -> pd.Series:
    """Short-cycle TRIX(5) — weekly triple-smoothed momentum (distinct cycle)."""
    return _trix(close, 5)


def f28_ttcf_077_trix_50_long(close: pd.Series) -> pd.Series:
    """TRIX(50) — multi-month triple-smoothed momentum."""
    return _trix(close, 50)


def f28_ttcf_078_trix_100_very_long(close: pd.Series) -> pd.Series:
    """TRIX(100) — multi-quarter triple-smoothed momentum (distinct slow-cycle)."""
    return _trix(close, 100)


def f28_ttcf_079_trix_50_minus_trix_15(close: pd.Series) -> pd.Series:
    """TRIX(50) - TRIX(15) — slow-vs-classical cycle gap."""
    return _trix(close, 50) - _trix(close, 15)


def f28_ttcf_080_all_trix_horizons_above_zero(close: pd.Series) -> pd.Series:
    """1 if TRIX(15), TRIX(30), TRIX(50) all > 0 — confirmed multi-cycle bullish."""
    t1 = _trix(close, 15)
    t2 = _trix(close, 30)
    t3 = _trix(close, 50)
    return ((t1 > 0) & (t2 > 0) & (t3 > 0)).astype(float).where(
        t1.notna() & t2.notna() & t3.notna(), np.nan)


def f28_ttcf_081_count_trix_horizons_decline_63(close: pd.Series) -> pd.Series:
    """Count of TRIX horizons {15, 30, 50} with 63d slope < 0 — multi-cycle decline breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (15, 30, 50):
        sl = _rolling_slope(_trix(close, n), QDAYS)
        cnt = cnt + (sl < 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_082_trix_50_persistence_above_zero_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with TRIX(50) > 0 — long-cycle annual dwell."""
    t = _trix(close, 50)
    return (t > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(t.notna(), np.nan)


# ============================================================
# Bucket H — multi-horizon CCI (083-092)
# ============================================================

def f28_ttcf_083_cci_5_weekly(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(5) — weekly horizon (distinct concept)."""
    return _cci(high, low, close, 5)


def f28_ttcf_084_cci_100_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(100) — multi-quarter horizon."""
    return _cci(high, low, close, 100)


def f28_ttcf_085_cci_252_annual(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(252) — annual horizon."""
    return _cci(high, low, close, YDAYS)


def f28_ttcf_086_cci_50_minus_cci_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(50) - CCI(20) — medium-vs-classical cycle gap."""
    return _cci(high, low, close, 50) - _cci(high, low, close, 20)


def f28_ttcf_087_cci_100_minus_cci_20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(100) - CCI(20) — long-vs-classical cycle gap."""
    return _cci(high, low, close, 100) - _cci(high, low, close, 20)


def f28_ttcf_088_all_cci_horizons_above_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20), CCI(50), CCI(100) all > 100 — confirmed multi-horizon CCI OB."""
    c1 = _cci(high, low, close, 20)
    c2 = _cci(high, low, close, 50)
    c3 = _cci(high, low, close, 100)
    return ((c1 > 100.0) & (c2 > 100.0) & (c3 > 100.0)).astype(float).where(
        c1.notna() & c2.notna() & c3.notna(), np.nan)


def f28_ttcf_089_count_cci_horizons_above_100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of horizons in {20, 50, 100, 252} with CCI > 100 — CCI breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (20, 50, 100, YDAYS):
        c = _cci(high, low, close, n)
        cnt = cnt + (c > 100.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_090_cci_50_div_vs_price_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish CCI(50) divergence vs price (63d horizon) — distinct from CCI(20) divergence."""
    c = _cci(high, low, close, 50)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan)


def f28_ttcf_091_cci_50_dwell_above_100_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CCI(50) > 100 — medium-horizon CCI OB dwell."""
    c = _cci(high, low, close, 50)
    return (c > 100.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)


def f28_ttcf_092_cci_100_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of CCI(100) over 252d — distribution-based long-horizon CCI position."""
    return _rolling_zscore(_cci(high, low, close, 100), YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket I — multi-horizon CMO + multi-horizon TSI (093-102)
# ============================================================

def f28_ttcf_093_cmo_5_weekly(close: pd.Series) -> pd.Series:
    """CMO(5) — weekly horizon (distinct concept)."""
    return _cmo(close, 5)


def f28_ttcf_094_cmo_100_long(close: pd.Series) -> pd.Series:
    """CMO(100) — multi-quarter horizon."""
    return _cmo(close, 100)


def f28_ttcf_095_cmo_252_annual(close: pd.Series) -> pd.Series:
    """CMO(252) — annual horizon."""
    return _cmo(close, YDAYS)


def f28_ttcf_096_all_cmo_horizons_above_50(close: pd.Series) -> pd.Series:
    """1 if CMO(14), CMO(63), CMO(252) all > 50 — confirmed multi-horizon CMO OB."""
    c1 = _cmo(close, 14)
    c2 = _cmo(close, QDAYS)
    c3 = _cmo(close, YDAYS)
    return ((c1 > 50.0) & (c2 > 50.0) & (c3 > 50.0)).astype(float).where(
        c1.notna() & c2.notna() & c3.notna(), np.nan)


def f28_ttcf_097_count_cmo_horizons_above_50(close: pd.Series) -> pd.Series:
    """Count of CMO horizons in {14, 21, 63, 100, 252} with CMO > 50 — CMO breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (14, MDAYS, QDAYS, 100, YDAYS):
        c = _cmo(close, n)
        cnt = cnt + (c > 50.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_098_cmo_50_minus_cmo_14_diff(close: pd.Series) -> pd.Series:
    """CMO(50) - CMO(14) — medium-vs-classical CMO cycle gap."""
    return _cmo(close, 50) - _cmo(close, 14)


def f28_ttcf_099_tsi_5_3_fast(close: pd.Series) -> pd.Series:
    """Fast TSI(5, 3) — short-horizon double-smoothed momentum (distinct from classical 25/13)."""
    return _tsi(close, 5, 3)


def f28_ttcf_100_tsi_50_25_slow(close: pd.Series) -> pd.Series:
    """Slow TSI(50, 25) — long-horizon double-smoothed momentum."""
    return _tsi(close, 50, 25)


def f28_ttcf_101_count_tsi_horizons_above_zero(close: pd.Series) -> pd.Series:
    """Count of TSI horizons in {(5,3), (25,13), (50,25)} with TSI > 0 — TSI breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n1, n2 in ((5, 3), (25, 13), (50, 25)):
        t = _tsi(close, n1, n2)
        cnt = cnt + (t > 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_102_cmo_252_div_vs_price_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual CMO divergence vs price (252d horizon) — long-cycle CMO divergence."""
    c = _cmo(close, YDAYS)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    c_below = c < c.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan)


# ============================================================
# Bucket J — DPO multi-period + ensemble (103-110)
# ============================================================

def f28_ttcf_103_dpo_5_weekly(close: pd.Series) -> pd.Series:
    """DPO(5) — weekly displaced-MA detrended (distinct cycle)."""
    return _dpo(close, 5)


def f28_ttcf_104_dpo_252_annual(close: pd.Series) -> pd.Series:
    """DPO(252) — annual displaced-MA detrended."""
    return _dpo(close, YDAYS)


def f28_ttcf_105_dpo_504_2y(close: pd.Series) -> pd.Series:
    """DPO(504) — bi-annual displaced-MA detrended (very-long cycle)."""
    return _dpo(close, DDAYS_2Y)


def f28_ttcf_106_dpo_lead_lag_21_vs_63(close: pd.Series) -> pd.Series:
    """DPO(21) - DPO(63) — short-vs-quarterly DPO (cycle disagreement)."""
    return _dpo(close, MDAYS) - _dpo(close, QDAYS)


def f28_ttcf_107_count_dpo_horizons_above_zero(close: pd.Series) -> pd.Series:
    """Count of DPO horizons in {5, 21, 63, 252} above zero — DPO breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for n in (5, MDAYS, QDAYS, YDAYS):
        d = _dpo(close, n)
        cnt = cnt + (d > 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_108_dpo_persistence_above_q90_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where DPO above its 252d 90th percentile — distribution-DPO persistence."""
    d = _dpo(close, MDAYS)
    q = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (d > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(d.notna() & q.notna(), np.nan)


def f28_ttcf_109_dpo_amplitude_decay_63(close: pd.Series) -> pd.Series:
    """DPO(21) 63d max - 63d-max from 63 bars ago — quarterly DPO amplitude decay."""
    d = _dpo(close, MDAYS)
    pmax = d.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_110_dpo_sign_flip_count_63(close: pd.Series) -> pd.Series:
    """Count of DPO sign flips (zero crosses) in past 63 — cycle-instability count."""
    d = _dpo(close, MDAYS)
    flip = (d * d.shift(1)) < 0
    return flip.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(d.notna(), np.nan)


# ============================================================
# Bucket K — KST variants & multi-horizon (111-118)
# ============================================================

def f28_ttcf_111_short_kst(close: pd.Series) -> pd.Series:
    """Short-cycle KST using shorter ROCs (5/10/15/20) — distinct hypothesis from classical KST."""
    return _short_kst(close)


def f28_ttcf_112_kst_persistence_above_zero_504(close: pd.Series) -> pd.Series:
    """Fraction of past 504 bars (2y) with KST > 0 — bi-annual long-momentum-bullish dwell."""
    k = _kst(close)
    return (k > 0).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean().where(k.notna(), np.nan)


def f28_ttcf_113_kst_div_vs_price_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual KST divergence vs price (252d horizon)."""
    k = _kst(close)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    k_below = k < k.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & k_below).astype(float).where(k.notna(), np.nan)


def f28_ttcf_114_kst_above_q90_dist_252(close: pd.Series) -> pd.Series:
    """1 if KST above its 252d 90th percentile — distribution-KST OB."""
    k = _kst(close)
    q = k.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (k > q).astype(float).where(k.notna() & q.notna(), np.nan)


def f28_ttcf_115_kst_peak_decay_252(close: pd.Series) -> pd.Series:
    """KST 252d max - KST from 252 bars ago — annual KST peak decay."""
    k = _kst(close)
    pmax = k.rolling(YDAYS, min_periods=QDAYS).max()
    return pmax - pmax.shift(YDAYS)


def f28_ttcf_116_kst_zero_cross_down_count_252(close: pd.Series) -> pd.Series:
    """Count of KST bearish zero-crosses in past 252 — annual long-momentum sign-flip frequency."""
    k = _kst(close)
    ev = ((k.shift(1) >= 0) & (k < 0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(k.notna(), np.nan)


def f28_ttcf_117_kst_residual_vs_ema21(close: pd.Series) -> pd.Series:
    """KST - EMA21(KST) — short-smoothing residual of long-momentum."""
    k = _kst(close)
    return k - _ema(k, MDAYS)


def f28_ttcf_118_kst_acceleration_21(close: pd.Series) -> pd.Series:
    """First diff of 21d slope of KST — monthly KST acceleration."""
    return _rolling_slope(_kst(close), MDAYS).diff()


# ============================================================
# Bucket L — cross-indicator alignment / ensemble (119-128)
# ============================================================

def f28_ttcf_119_count_oscillators_above_ob_thresholds(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of OB-state indicators: {TRIX(15)>0, TSI(25,13)>25, CCI(20)>100, KST>0, CMO(14)>50}."""
    t = _trix(close, 15)
    ts = _tsi(close, 25, 13)
    c = _cci(high, low, close, 20)
    k = _kst(close)
    cm = _cmo(close, 14)
    s = ((t > 0).astype(float).fillna(0)
         + (ts > 25.0).astype(float).fillna(0)
         + (c > 100.0).astype(float).fillna(0)
         + (k > 0).astype(float).fillna(0)
         + (cm > 50.0).astype(float).fillna(0))
    return s.where(t.notna(), np.nan)


def f28_ttcf_120_count_oscillators_in_extreme_ob(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of extreme-OB indicators: {TRIX z>2, TSI>40, CCI>200, KST z>2, CMO>75}."""
    t = _trix(close, 15)
    ts = _tsi(close, 25, 13)
    c = _cci(high, low, close, 20)
    k = _kst(close)
    cm = _cmo(close, 14)
    zt = _rolling_zscore(t, YDAYS, min_periods=QDAYS)
    zk = _rolling_zscore(k, YDAYS, min_periods=QDAYS)
    s = ((zt > 2.0).astype(float).fillna(0)
         + (ts > 40.0).astype(float).fillna(0)
         + (c > 200.0).astype(float).fillna(0)
         + (zk > 2.0).astype(float).fillna(0)
         + (cm > 75.0).astype(float).fillna(0))
    return s.where(t.notna(), np.nan)


def f28_ttcf_121_count_oscillators_bearish_cross_in_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators with a bearish signal-line cross in past 21 bars (TRIX, TSI, KST, CMO)."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _kst(close), _cmo(close, 14)):
        if sig is _trix(close, 15):
            pass  # noqa: same as below; readability only
        s = _ema(sig, 9)
        d = sig - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=1).sum() > 0).astype(float)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_122_count_oscillators_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators currently showing bearish divergence vs 63d-price-high."""
    cnt = pd.Series(0.0, index=close.index)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        below = sig < sig.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (p_new & below).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_123_count_oscillators_decaying_from_peak_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators where current value < (63d max - 50% of that peak's absolute value)."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        decayed = (pmax - sig) > 0.5 * pmax.abs()
        cnt = cnt + decayed.astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_124_oscillator_ensemble_avg_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average z-score (over 252d) across {TRIX, TSI, CCI, KST, CMO} — ensemble extension."""
    z = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        z = z + _rolling_zscore(sig, YDAYS, min_periods=QDAYS).fillna(0)
    return (z / 5.0).where(close.notna(), np.nan)


def f28_ttcf_125_oscillator_ensemble_dispersion(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std across {TRIX, TSI, CCI, KST, CMO} z-scores — multi-oscillator disagreement."""
    cols = []
    for i, sig in enumerate((_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                             _kst(close), _cmo(close, 14))):
        cols.append(_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(f"z{i}"))
    return pd.concat(cols, axis=1).std(axis=1)


def f28_ttcf_126_pair_corr_break_trix_cci_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between TRIX(15) and CCI(20) — drops sharply when oscillators disagree."""
    return _trix(close, 15).rolling(QDAYS, min_periods=MDAYS).corr(_cci(high, low, close, 20))


def f28_ttcf_127_dominant_oscillator_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Argmax over {TRIX, TSI, CCI, KST, CMO} of their 252d z-scores — which oscillator is most extreme.
    Encoded as 0..4."""
    z1 = _rolling_zscore(_trix(close, 15), YDAYS, min_periods=QDAYS).rename(0)
    z2 = _rolling_zscore(_tsi(close, 25, 13), YDAYS, min_periods=QDAYS).rename(1)
    z3 = _rolling_zscore(_cci(high, low, close, 20), YDAYS, min_periods=QDAYS).rename(2)
    z4 = _rolling_zscore(_kst(close), YDAYS, min_periods=QDAYS).rename(3)
    z5 = _rolling_zscore(_cmo(close, 14), YDAYS, min_periods=QDAYS).rename(4)
    cat = pd.concat([z1, z2, z3, z4, z5], axis=1)
    return cat.fillna(-np.inf).idxmax(axis=1).where(cat.notna().any(axis=1), np.nan).astype(float)


def f28_ttcf_128_oscillator_consensus_bearish_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(# oscillators with bearish cross in 21d) + (# with bearish div in 63d) + (# decaying from peak).
    High = multi-oscillator consensus bearish."""
    a = f28_ttcf_121_count_oscillators_bearish_cross_in_21d(high, low, close).fillna(0)
    b = f28_ttcf_122_count_oscillators_bearish_div_63(high, low, close).fillna(0)
    c = f28_ttcf_123_count_oscillators_decaying_from_peak_63(high, low, close).fillna(0)
    return (a + b + c).where(close.notna(), np.nan)


# ============================================================
# Bucket M — composite topping + decay (129-138)
# ============================================================

def f28_ttcf_129_topping_score_at_price_peak_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At price=252d max: sum of OB-state indicators (TRIX>0, TSI>25, CCI>100, KST>0, CMO>50). Else NaN."""
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    score = f28_ttcf_119_count_oscillators_above_ob_thresholds(high, low, close)
    return score.where(at_max, np.nan)


def f28_ttcf_130_pre_topping_extreme_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At price=252d max: count of extreme-OB triggers (z>2 / >q95) fired in past 63 bars across basket."""
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        ev = (z > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).max() > 0
        cnt = cnt + ev.astype(float).fillna(0)
    return cnt.where(at_max, np.nan)


def f28_ttcf_131_post_peak_decay_velocity_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum across basket of (63d max - current) / |63d max| — aggregate fractional decay from quarterly peak."""
    out = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + _safe_div(pmax - sig, pmax.abs()).fillna(0)
    return out.where(close.notna(), np.nan)


def f28_ttcf_132_cycle_alignment_at_peak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if short-cycle (TRIX(5)) AND long-cycle (TRIX(50)) both at their 252d max within past 21 bars — multi-cycle peak alignment."""
    t_short = _trix(close, 5)
    t_long = _trix(close, 50)
    at_max_s = (t_short == t_short.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).rolling(MDAYS, min_periods=1).max() > 0
    at_max_l = (t_long == t_long.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).rolling(MDAYS, min_periods=1).max() > 0
    return (at_max_s & at_max_l).astype(float).where(t_short.notna() & t_long.notna(), np.nan)


def f28_ttcf_133_failure_after_high_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of bars where price was at 252d max AND CCI(20) declined > 50 from its 21d max — failure-at-peak count."""
    at_max = (high == high.rolling(YDAYS, min_periods=QDAYS).max())
    c = _cci(high, low, close, 20)
    c21max = c.rolling(MDAYS, min_periods=WDAYS).max()
    fail = at_max & ((c21max - c) > 50.0)
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(c.notna(), np.nan)


def f28_ttcf_134_blowoff_then_collapse_oscillator_basket(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators where the 252d max was within last 63 bars AND value has decayed > 50% of peak abs."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _kst(close), _cmo(close, 14)):
        pmax252 = sig.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(sig == pmax252)
        decayed = (pmax252 - sig) > 0.5 * pmax252.abs()
        cnt = cnt + ((bs <= QDAYS) & decayed).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_135_multi_horizon_persist_then_div_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TRIX(15) was > 0 for > 50% of past 252 AND a TRIX bearish div fired in past 21 — long-bullish + recent-div."""
    t = _trix(close, 15)
    persist = (t > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() > 0.5
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    t_below = t < t.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div_ev = (p_new & t_below).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return (persist & div_ev).astype(float).where(t.notna(), np.nan)


def f28_ttcf_136_oscillator_extreme_to_zero_velocity_basket(close: pd.Series) -> pd.Series:
    """Sum over basket of (max in last 63 - current) / 63 — average velocity from quarterly peak to current."""
    out = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _kst(close), _cmo(close, 14)):
        pmax63 = sig.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + ((pmax63 - sig) / float(QDAYS)).fillna(0)
    return out.where(close.notna(), np.nan)


def f28_ttcf_137_ob_re_entry_after_exit_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in past 63 where CCI(20) re-entered OB-100 within 21 bars of exiting it — failed cooling/retest."""
    c = _cci(high, low, close, 20)
    exited = (c.shift(1) > 100.0) & (c <= 100.0)
    entered = (c.shift(1) <= 100.0) & (c > 100.0)
    recent_exit = exited.rolling(MDAYS, min_periods=1).sum().shift(1) > 0
    return (entered & recent_exit).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(c.notna(), np.nan)


def f28_ttcf_138_oscillator_failed_to_recover_post_exit_indicator(close: pd.Series) -> pd.Series:
    """1 if TSI exited above-25 (in past 63 bars) AND has not re-entered above-25 since — extended cool-off."""
    t = _tsi(close, 25, 13)
    in_ob = (t > 25.0)
    recent_in_ob = in_ob.rolling(QDAYS, min_periods=MDAYS).sum() == 0
    had_ob_before = in_ob.rolling(YDAYS, min_periods=QDAYS).sum() > 0
    return (recent_in_ob & had_ob_before).astype(float).where(t.notna(), np.nan)


# ============================================================
# Bucket N — stationarity / detrending of indicators (139-150)
# ============================================================

def f28_ttcf_139_trix_minus_252d_mean(close: pd.Series) -> pd.Series:
    """TRIX(15) minus its 252d rolling mean — annual centered TRIX deviation."""
    t = _trix(close, 15)
    return t - t.rolling(YDAYS, min_periods=QDAYS).mean()


def f28_ttcf_140_tsi_minus_252d_mean(close: pd.Series) -> pd.Series:
    """TSI(25,13) minus its 252d rolling mean — annual centered TSI deviation."""
    t = _tsi(close, 25, 13)
    return t - t.rolling(YDAYS, min_periods=QDAYS).mean()


def f28_ttcf_141_cci_minus_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) minus its 252d rolling mean — annual centered CCI deviation."""
    c = _cci(high, low, close, 20)
    return c - c.rolling(YDAYS, min_periods=QDAYS).mean()


def f28_ttcf_142_kst_minus_252d_mean(close: pd.Series) -> pd.Series:
    """KST minus its 252d rolling mean — annual centered KST deviation."""
    k = _kst(close)
    return k - k.rolling(YDAYS, min_periods=QDAYS).mean()


def f28_ttcf_143_cmo_minus_252d_mean(close: pd.Series) -> pd.Series:
    """CMO(14) minus its 252d rolling mean — annual centered CMO deviation."""
    c = _cmo(close, 14)
    return c - c.rolling(YDAYS, min_periods=QDAYS).mean()


def f28_ttcf_144_cci_dpo_proxy_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) - SMA21(CCI).shift(11) — DPO-style detrended CCI."""
    c = _cci(high, low, close, 20)
    sma = c.rolling(MDAYS, min_periods=WDAYS).mean()
    return c - sma.shift(11)


def f28_ttcf_145_tsi_residual_vs_ema21(close: pd.Series) -> pd.Series:
    """TSI minus EMA21(TSI) — short-smoothing residual of TSI."""
    t = _tsi(close, 25, 13)
    return t - _ema(t, MDAYS)


def f28_ttcf_146_cmo_residual_vs_ema21(close: pd.Series) -> pd.Series:
    """CMO minus EMA21(CMO) — short-smoothing residual of CMO."""
    c = _cmo(close, 14)
    return c - _ema(c, MDAYS)


def f28_ttcf_147_trix_acceleration_21(close: pd.Series) -> pd.Series:
    """First diff of 21d slope of TRIX — monthly TRIX acceleration."""
    return _rolling_slope(_trix(close, 15), MDAYS).diff()


def f28_ttcf_148_cci_acceleration_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """First diff of 21d slope of CCI(20) — monthly CCI acceleration."""
    return _rolling_slope(_cci(high, low, close, 20), MDAYS).diff()


def f28_ttcf_149_bars_since_basket_all_in_ob(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since {TRIX>0, TSI>25, CCI>100, KST>0, CMO>50} were all simultaneously true — recency of full-basket OB."""
    t = _trix(close, 15)
    ts = _tsi(close, 25, 13)
    c = _cci(high, low, close, 20)
    k = _kst(close)
    cm = _cmo(close, 14)
    all_ob = (t > 0) & (ts > 25.0) & (c > 100.0) & (k > 0) & (cm > 50.0)
    return _bars_since_true(all_ob)


def f28_ttcf_150_terminal_topping_aggregate_score_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate terminal-pattern score: blowoff-collapse basket + extreme-OB count + persist-then-div + failure-after-high count."""
    a = f28_ttcf_134_blowoff_then_collapse_oscillator_basket(high, low, close).fillna(0)
    b = f28_ttcf_120_count_oscillators_in_extreme_ob(high, low, close).fillna(0)
    d = f28_ttcf_135_multi_horizon_persist_then_div_indicator(high, close).fillna(0)
    e = f28_ttcf_133_failure_after_high_count_252(high, low, close).fillna(0)
    return (a + b + d + e).where(close.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

TRIX_TSI_CCI_FAMILY_BASE_REGISTRY_076_150 = {
    "f28_ttcf_076_trix_5_short": {"inputs": ["close"], "func": f28_ttcf_076_trix_5_short},
    "f28_ttcf_077_trix_50_long": {"inputs": ["close"], "func": f28_ttcf_077_trix_50_long},
    "f28_ttcf_078_trix_100_very_long": {"inputs": ["close"], "func": f28_ttcf_078_trix_100_very_long},
    "f28_ttcf_079_trix_50_minus_trix_15": {"inputs": ["close"], "func": f28_ttcf_079_trix_50_minus_trix_15},
    "f28_ttcf_080_all_trix_horizons_above_zero": {"inputs": ["close"], "func": f28_ttcf_080_all_trix_horizons_above_zero},
    "f28_ttcf_081_count_trix_horizons_decline_63": {"inputs": ["close"], "func": f28_ttcf_081_count_trix_horizons_decline_63},
    "f28_ttcf_082_trix_50_persistence_above_zero_252": {"inputs": ["close"], "func": f28_ttcf_082_trix_50_persistence_above_zero_252},
    "f28_ttcf_083_cci_5_weekly": {"inputs": ["high", "low", "close"], "func": f28_ttcf_083_cci_5_weekly},
    "f28_ttcf_084_cci_100_long": {"inputs": ["high", "low", "close"], "func": f28_ttcf_084_cci_100_long},
    "f28_ttcf_085_cci_252_annual": {"inputs": ["high", "low", "close"], "func": f28_ttcf_085_cci_252_annual},
    "f28_ttcf_086_cci_50_minus_cci_20": {"inputs": ["high", "low", "close"], "func": f28_ttcf_086_cci_50_minus_cci_20},
    "f28_ttcf_087_cci_100_minus_cci_20": {"inputs": ["high", "low", "close"], "func": f28_ttcf_087_cci_100_minus_cci_20},
    "f28_ttcf_088_all_cci_horizons_above_100": {"inputs": ["high", "low", "close"], "func": f28_ttcf_088_all_cci_horizons_above_100},
    "f28_ttcf_089_count_cci_horizons_above_100": {"inputs": ["high", "low", "close"], "func": f28_ttcf_089_count_cci_horizons_above_100},
    "f28_ttcf_090_cci_50_div_vs_price_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_090_cci_50_div_vs_price_63},
    "f28_ttcf_091_cci_50_dwell_above_100_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_091_cci_50_dwell_above_100_63},
    "f28_ttcf_092_cci_100_zscore_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_092_cci_100_zscore_252},
    "f28_ttcf_093_cmo_5_weekly": {"inputs": ["close"], "func": f28_ttcf_093_cmo_5_weekly},
    "f28_ttcf_094_cmo_100_long": {"inputs": ["close"], "func": f28_ttcf_094_cmo_100_long},
    "f28_ttcf_095_cmo_252_annual": {"inputs": ["close"], "func": f28_ttcf_095_cmo_252_annual},
    "f28_ttcf_096_all_cmo_horizons_above_50": {"inputs": ["close"], "func": f28_ttcf_096_all_cmo_horizons_above_50},
    "f28_ttcf_097_count_cmo_horizons_above_50": {"inputs": ["close"], "func": f28_ttcf_097_count_cmo_horizons_above_50},
    "f28_ttcf_098_cmo_50_minus_cmo_14_diff": {"inputs": ["close"], "func": f28_ttcf_098_cmo_50_minus_cmo_14_diff},
    "f28_ttcf_099_tsi_5_3_fast": {"inputs": ["close"], "func": f28_ttcf_099_tsi_5_3_fast},
    "f28_ttcf_100_tsi_50_25_slow": {"inputs": ["close"], "func": f28_ttcf_100_tsi_50_25_slow},
    "f28_ttcf_101_count_tsi_horizons_above_zero": {"inputs": ["close"], "func": f28_ttcf_101_count_tsi_horizons_above_zero},
    "f28_ttcf_102_cmo_252_div_vs_price_252": {"inputs": ["high", "close"], "func": f28_ttcf_102_cmo_252_div_vs_price_252},
    "f28_ttcf_103_dpo_5_weekly": {"inputs": ["close"], "func": f28_ttcf_103_dpo_5_weekly},
    "f28_ttcf_104_dpo_252_annual": {"inputs": ["close"], "func": f28_ttcf_104_dpo_252_annual},
    "f28_ttcf_105_dpo_504_2y": {"inputs": ["close"], "func": f28_ttcf_105_dpo_504_2y},
    "f28_ttcf_106_dpo_lead_lag_21_vs_63": {"inputs": ["close"], "func": f28_ttcf_106_dpo_lead_lag_21_vs_63},
    "f28_ttcf_107_count_dpo_horizons_above_zero": {"inputs": ["close"], "func": f28_ttcf_107_count_dpo_horizons_above_zero},
    "f28_ttcf_108_dpo_persistence_above_q90_252": {"inputs": ["close"], "func": f28_ttcf_108_dpo_persistence_above_q90_252},
    "f28_ttcf_109_dpo_amplitude_decay_63": {"inputs": ["close"], "func": f28_ttcf_109_dpo_amplitude_decay_63},
    "f28_ttcf_110_dpo_sign_flip_count_63": {"inputs": ["close"], "func": f28_ttcf_110_dpo_sign_flip_count_63},
    "f28_ttcf_111_short_kst": {"inputs": ["close"], "func": f28_ttcf_111_short_kst},
    "f28_ttcf_112_kst_persistence_above_zero_504": {"inputs": ["close"], "func": f28_ttcf_112_kst_persistence_above_zero_504},
    "f28_ttcf_113_kst_div_vs_price_252": {"inputs": ["high", "close"], "func": f28_ttcf_113_kst_div_vs_price_252},
    "f28_ttcf_114_kst_above_q90_dist_252": {"inputs": ["close"], "func": f28_ttcf_114_kst_above_q90_dist_252},
    "f28_ttcf_115_kst_peak_decay_252": {"inputs": ["close"], "func": f28_ttcf_115_kst_peak_decay_252},
    "f28_ttcf_116_kst_zero_cross_down_count_252": {"inputs": ["close"], "func": f28_ttcf_116_kst_zero_cross_down_count_252},
    "f28_ttcf_117_kst_residual_vs_ema21": {"inputs": ["close"], "func": f28_ttcf_117_kst_residual_vs_ema21},
    "f28_ttcf_118_kst_acceleration_21": {"inputs": ["close"], "func": f28_ttcf_118_kst_acceleration_21},
    "f28_ttcf_119_count_oscillators_above_ob_thresholds": {"inputs": ["high", "low", "close"], "func": f28_ttcf_119_count_oscillators_above_ob_thresholds},
    "f28_ttcf_120_count_oscillators_in_extreme_ob": {"inputs": ["high", "low", "close"], "func": f28_ttcf_120_count_oscillators_in_extreme_ob},
    "f28_ttcf_121_count_oscillators_bearish_cross_in_21d": {"inputs": ["high", "low", "close"], "func": f28_ttcf_121_count_oscillators_bearish_cross_in_21d},
    "f28_ttcf_122_count_oscillators_bearish_div_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_122_count_oscillators_bearish_div_63},
    "f28_ttcf_123_count_oscillators_decaying_from_peak_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_123_count_oscillators_decaying_from_peak_63},
    "f28_ttcf_124_oscillator_ensemble_avg_zscore_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_124_oscillator_ensemble_avg_zscore_252},
    "f28_ttcf_125_oscillator_ensemble_dispersion": {"inputs": ["high", "low", "close"], "func": f28_ttcf_125_oscillator_ensemble_dispersion},
    "f28_ttcf_126_pair_corr_break_trix_cci_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_126_pair_corr_break_trix_cci_63},
    "f28_ttcf_127_dominant_oscillator_indicator": {"inputs": ["high", "low", "close"], "func": f28_ttcf_127_dominant_oscillator_indicator},
    "f28_ttcf_128_oscillator_consensus_bearish_score": {"inputs": ["high", "low", "close"], "func": f28_ttcf_128_oscillator_consensus_bearish_score},
    "f28_ttcf_129_topping_score_at_price_peak_aggregate": {"inputs": ["high", "low", "close"], "func": f28_ttcf_129_topping_score_at_price_peak_aggregate},
    "f28_ttcf_130_pre_topping_extreme_count_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_130_pre_topping_extreme_count_63},
    "f28_ttcf_131_post_peak_decay_velocity_aggregate": {"inputs": ["high", "low", "close"], "func": f28_ttcf_131_post_peak_decay_velocity_aggregate},
    "f28_ttcf_132_cycle_alignment_at_peak": {"inputs": ["high", "low", "close"], "func": f28_ttcf_132_cycle_alignment_at_peak},
    "f28_ttcf_133_failure_after_high_count_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_133_failure_after_high_count_252},
    "f28_ttcf_134_blowoff_then_collapse_oscillator_basket": {"inputs": ["high", "low", "close"], "func": f28_ttcf_134_blowoff_then_collapse_oscillator_basket},
    "f28_ttcf_135_multi_horizon_persist_then_div_indicator": {"inputs": ["high", "close"], "func": f28_ttcf_135_multi_horizon_persist_then_div_indicator},
    "f28_ttcf_136_oscillator_extreme_to_zero_velocity_basket": {"inputs": ["close"], "func": f28_ttcf_136_oscillator_extreme_to_zero_velocity_basket},
    "f28_ttcf_137_ob_re_entry_after_exit_count_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_137_ob_re_entry_after_exit_count_63},
    "f28_ttcf_138_oscillator_failed_to_recover_post_exit_indicator": {"inputs": ["close"], "func": f28_ttcf_138_oscillator_failed_to_recover_post_exit_indicator},
    "f28_ttcf_139_trix_minus_252d_mean": {"inputs": ["close"], "func": f28_ttcf_139_trix_minus_252d_mean},
    "f28_ttcf_140_tsi_minus_252d_mean": {"inputs": ["close"], "func": f28_ttcf_140_tsi_minus_252d_mean},
    "f28_ttcf_141_cci_minus_252d_mean": {"inputs": ["high", "low", "close"], "func": f28_ttcf_141_cci_minus_252d_mean},
    "f28_ttcf_142_kst_minus_252d_mean": {"inputs": ["close"], "func": f28_ttcf_142_kst_minus_252d_mean},
    "f28_ttcf_143_cmo_minus_252d_mean": {"inputs": ["close"], "func": f28_ttcf_143_cmo_minus_252d_mean},
    "f28_ttcf_144_cci_dpo_proxy_21": {"inputs": ["high", "low", "close"], "func": f28_ttcf_144_cci_dpo_proxy_21},
    "f28_ttcf_145_tsi_residual_vs_ema21": {"inputs": ["close"], "func": f28_ttcf_145_tsi_residual_vs_ema21},
    "f28_ttcf_146_cmo_residual_vs_ema21": {"inputs": ["close"], "func": f28_ttcf_146_cmo_residual_vs_ema21},
    "f28_ttcf_147_trix_acceleration_21": {"inputs": ["close"], "func": f28_ttcf_147_trix_acceleration_21},
    "f28_ttcf_148_cci_acceleration_21": {"inputs": ["high", "low", "close"], "func": f28_ttcf_148_cci_acceleration_21},
    "f28_ttcf_149_bars_since_basket_all_in_ob": {"inputs": ["high", "low", "close"], "func": f28_ttcf_149_bars_since_basket_all_in_ob},
    "f28_ttcf_150_terminal_topping_aggregate_score_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_150_terminal_topping_aggregate_score_252},
}
