"""coppock_curve_kst base features 451-525 — Pipeline 1b-technical (precision extension).

Individual signals: RSI applied to long-smoothed momentum, MACD on Coppock (momentum-
of-momentum), Chande Momentum Oscillator (CMO) at long horizons individually, Ehlers
Roofing Filter (cycle isolator), KAMA-smoothed Coppock variants, Vortex Indicator at
long horizons individual, standard deviation of long-momentum as regime gauges.

Each feature = single discrete signal. PIT-clean. Self-contained.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


# ---------------------------- standard helpers ----------------------------

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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _wma(s, n):
    weights = np.arange(1, n + 1, dtype=float)
    wsum = weights.sum()
    def _ww(w):
        if np.isnan(w).any():
            return np.nan
        return float(np.dot(w, weights) / wsum)
    return s.rolling(n, min_periods=n).apply(_ww, raw=True)


def _roc_pct(s, n):
    return s.pct_change(n) * 100.0


# ---------------------------- existing-style cycle helpers ----------------------------

def _coppock(close, n_long, n_short, n_wma):
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)


def _coppock_annual(close):
    return _coppock(close, 294, 231, 210)


def _coppock_quarterly(close):
    return _coppock(close, QDAYS, 42, MDAYS)


def _coppock_semi_annual(close):
    return _coppock(close, 126, 84, 42)


def _coppock_biennial(close):
    return _coppock(close, DDAYS_2Y, 378, 210)


def _kst(close):
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_long_term(close):
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


# ---------------------------- new indicator helpers ----------------------------

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0); loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(ag, al))


def _rsi_generic(series, n=14):
    """RSI applied to any series (not just close). Useful for momentum-of-momentum constructions."""
    delta = series.diff()
    gain = delta.clip(lower=0); loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(ag, al))


def _cmo(close, n=14):
    """Chande Momentum Oscillator: 100 × (sum-up - sum-dn) / (sum-up + sum-dn) over n bars."""
    delta = close.diff()
    sum_up = delta.clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    sum_dn = (-delta).clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(sum_up - sum_dn, sum_up + sum_dn)


def _kama(close, n=10, fast=2, slow=30):
    """Kaufman Adaptive Moving Average: adapts smoothing constant based on Efficiency Ratio."""
    change = (close - close.shift(n)).abs()
    volatility = close.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(change, volatility).fillna(0)
    fast_sc = 2.0 / (fast + 1.0)
    slow_sc = 2.0 / (slow + 1.0)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    kama = pd.Series(np.nan, index=close.index)
    cl = close.values; sc_arr = sc.values
    nb = len(close)
    if nb > n:
        kama.iloc[n] = cl[n]
        prev = cl[n]
        for i in range(n + 1, nb):
            if np.isnan(prev) or np.isnan(sc_arr[i]) or np.isnan(cl[i]):
                continue
            prev = prev + sc_arr[i] * (cl[i] - prev)
            kama.iloc[i] = prev
    return kama


def _kama_coppock_cycle(close, n_long, n_short, n_kama=21):
    """Coppock-style computation but with KAMA smoothing instead of WMA."""
    return _kama(_roc_pct(close, n_long) + _roc_pct(close, n_short), n=n_kama)


def _ehlers_roofing_filter(close, hp_period=48, ss_period=10):
    """Ehlers Roofing Filter: 2-pole high-pass filter then 2-pole super smoother low-pass.
    Isolates cycles between ss_period and hp_period."""
    n = len(close)
    cl = close.values
    # 2-pole high-pass coefficient
    alpha1 = (np.cos(0.707 * 2 * np.pi / hp_period) + np.sin(0.707 * 2 * np.pi / hp_period) - 1.0) / np.cos(0.707 * 2 * np.pi / hp_period)
    hp = np.full(n, np.nan)
    # Super smoother coefficients
    a1 = np.exp(-1.414 * np.pi / ss_period)
    b1 = 2.0 * a1 * np.cos(1.414 * np.pi / ss_period)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    ss = np.full(n, np.nan)
    for i in range(n):
        if i < 2 or np.isnan(cl[i]) or np.isnan(cl[i - 1]) or np.isnan(cl[i - 2]):
            continue
        hp_prev1 = hp[i - 1] if not np.isnan(hp[i - 1]) else 0.0
        hp_prev2 = hp[i - 2] if not np.isnan(hp[i - 2]) else 0.0
        hp[i] = ((1.0 - alpha1 / 2.0) ** 2) * (cl[i] - 2.0 * cl[i - 1] + cl[i - 2]) \
                + 2.0 * (1.0 - alpha1) * hp_prev1 - ((1.0 - alpha1) ** 2) * hp_prev2
        ss_prev1 = ss[i - 1] if not np.isnan(ss[i - 1]) else 0.0
        ss_prev2 = ss[i - 2] if not np.isnan(ss[i - 2]) else 0.0
        ss[i] = c1 * (hp[i] + hp[i - 1] if not np.isnan(hp[i - 1]) else hp[i]) / 2.0 + c2 * ss_prev1 + c3 * ss_prev2
    return pd.Series(ss, index=close.index)


def _vortex_pos(high, low, close, n=14):
    vm_pos = (high - low.shift(1)).abs()
    tr = _true_range(high, low, close)
    return _safe_div(vm_pos.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     tr.rolling(n, min_periods=max(n // 3, 2)).sum())


def _vortex_neg(high, low, close, n=14):
    vm_neg = (low - high.shift(1)).abs()
    tr = _true_range(high, low, close)
    return _safe_div(vm_neg.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     tr.rolling(n, min_periods=max(n // 3, 2)).sum())


# ============================================================
# Bucket A — RSI applied to long-smoothed momentum (451-460)
# ============================================================

def f33_cpkt_451_rsi14_on_coppock_annual(close: pd.Series) -> pd.Series:
    """RSI(14) applied to the annual Coppock series itself — momentum-of-momentum oscillator."""
    return _rsi_generic(_coppock_annual(close), 14)


def f33_cpkt_452_rsi14_on_coppock_quarterly(close: pd.Series) -> pd.Series:
    """RSI(14) applied to quarterly Coppock."""
    return _rsi_generic(_coppock_quarterly(close), 14)


def f33_cpkt_453_rsi14_on_kst(close: pd.Series) -> pd.Series:
    """RSI(14) applied to standard KST."""
    return _rsi_generic(_kst(close), 14)


def f33_cpkt_454_rsi14_on_kst_long_term(close: pd.Series) -> pd.Series:
    """RSI(14) applied to long-term KST."""
    return _rsi_generic(_kst_long_term(close), 14)


def f33_cpkt_455_rsi14_on_coppock_annual_above_70_indicator(close: pd.Series) -> pd.Series:
    """+1 when RSI(14) on annual Coppock > 70 (overbought momentum-of-momentum)."""
    r = _rsi_generic(_coppock_annual(close), 14)
    return (r > 70).astype(float).where(r.notna(), np.nan)


def f33_cpkt_456_rsi14_on_kst_above_70_indicator(close: pd.Series) -> pd.Series:
    """+1 when RSI(14) on KST > 70."""
    r = _rsi_generic(_kst(close), 14)
    return (r > 70).astype(float).where(r.notna(), np.nan)


def f33_cpkt_457_rsi14_on_coppock_annual_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of RSI(14) on annual Coppock."""
    return _rolling_slope(_rsi_generic(_coppock_annual(close), 14), MDAYS)


def f33_cpkt_458_rsi14_on_kst_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of RSI(14) on KST."""
    return _rolling_slope(_rsi_generic(_kst(close), 14), MDAYS)


def f33_cpkt_459_rsi14_on_coppock_annual_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score over 252d of RSI(14) on annual Coppock."""
    return _rolling_zscore(_rsi_generic(_coppock_annual(close), 14), YDAYS)


def f33_cpkt_460_rsi14_on_kst_long_term_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score over 252d of RSI(14) on long-term KST."""
    return _rolling_zscore(_rsi_generic(_kst_long_term(close), 14), YDAYS)


# ============================================================
# Bucket B — MACD on Coppock (10) (461-470)
# ============================================================

def _macd_on(series, fast=12, slow=26):
    return _ema(series, fast) - _ema(series, slow)


def _macd_signal_on(series, fast=12, slow=26, sig=9):
    return _ema(_macd_on(series, fast, slow), sig)


def f33_cpkt_461_macd_line_on_coppock_annual(close: pd.Series) -> pd.Series:
    """MACD-line (12/26) applied to annual Coppock — momentum of long-smoothed momentum."""
    return _macd_on(_coppock_annual(close), 12, 26)


def f33_cpkt_462_macd_signal_on_coppock_annual(close: pd.Series) -> pd.Series:
    """MACD signal-line (9d EMA of MACD) on annual Coppock."""
    return _macd_signal_on(_coppock_annual(close), 12, 26, 9)


def f33_cpkt_463_macd_hist_on_coppock_annual(close: pd.Series) -> pd.Series:
    """MACD histogram on annual Coppock (MACD - signal)."""
    line = _macd_on(_coppock_annual(close), 12, 26)
    return line - _ema(line, 9)


def f33_cpkt_464_macd_on_coppock_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when MACD line on Coppock > 0."""
    m = _macd_on(_coppock_annual(close), 12, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan)


def f33_cpkt_465_macd_on_coppock_bearish_cross_event_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where MACD-on-Coppock crosses below its signal line."""
    line = _macd_on(_coppock_annual(close), 12, 26)
    sig = _ema(line, 9)
    diff = line - sig
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_466_days_since_macd_on_coppock_bearish_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent MACD-on-Coppock bearish signal-line cross."""
    line = _macd_on(_coppock_annual(close), 12, 26)
    sig = _ema(line, 9)
    diff = line - sig
    flag = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_467_macd_line_on_kst(close: pd.Series) -> pd.Series:
    """MACD-line (12/26) applied to standard KST."""
    return _macd_on(_kst(close), 12, 26)


def f33_cpkt_468_macd_hist_on_kst(close: pd.Series) -> pd.Series:
    """MACD histogram on standard KST."""
    line = _macd_on(_kst(close), 12, 26)
    return line - _ema(line, 9)


def f33_cpkt_469_macd_on_kst_bearish_cross_event_indicator(close: pd.Series) -> pd.Series:
    """+1 on bar where MACD-on-KST crosses below its signal line."""
    line = _macd_on(_kst(close), 12, 26)
    sig = _ema(line, 9)
    diff = line - sig
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_470_macd_on_coppock_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of MACD-on-Coppock over 252d."""
    return _rolling_zscore(_macd_on(_coppock_annual(close), 12, 26), YDAYS)


# ============================================================
# Bucket C — Chande Momentum Oscillator (CMO) at long horizons (471-480)
# ============================================================

def f33_cpkt_471_cmo_63d_value(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator at 63d horizon (quarterly)."""
    return _cmo(close, QDAYS)


def f33_cpkt_472_cmo_126d_value(close: pd.Series) -> pd.Series:
    """CMO at 126d horizon (semi-annual)."""
    return _cmo(close, 126)


def f33_cpkt_473_cmo_252d_value(close: pd.Series) -> pd.Series:
    """CMO at 252d horizon (annual)."""
    return _cmo(close, YDAYS)


def f33_cpkt_474_cmo_63d_above_50_indicator(close: pd.Series) -> pd.Series:
    """+1 when CMO(63) > 50 (overbought momentum)."""
    c = _cmo(close, QDAYS)
    return (c > 50).astype(float).where(c.notna(), np.nan)


def f33_cpkt_475_cmo_252d_above_50_indicator(close: pd.Series) -> pd.Series:
    """+1 when CMO(252) > 50 (annual overbought)."""
    c = _cmo(close, YDAYS)
    return (c > 50).astype(float).where(c.notna(), np.nan)


def f33_cpkt_476_cmo_63d_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of CMO(63)."""
    return _rolling_slope(_cmo(close, QDAYS), MDAYS)


def f33_cpkt_477_cmo_252d_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of CMO(252)."""
    return _rolling_slope(_cmo(close, YDAYS), QDAYS)


def f33_cpkt_478_cmo_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of CMO(63) over 252d."""
    return _rolling_zscore(_cmo(close, QDAYS), YDAYS)


def f33_cpkt_479_cmo_252d_above_50_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when CMO(252) > 50 AND close within 1% of 252d max."""
    c = _cmo(close, YDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((c > 50) & (near == 1)).astype(float).where(c.notna() & near.notna(), np.nan)


def f33_cpkt_480_cmo_252d_days_since_above_50(close: pd.Series) -> pd.Series:
    """Bars since CMO(252) was last above 50."""
    return _bars_since_true((_cmo(close, YDAYS) > 50).astype(float))


# ============================================================
# Bucket D — Ehlers Roofing Filter (481-490)
# ============================================================

def f33_cpkt_481_ehlers_roofing_value_48_10(close: pd.Series) -> pd.Series:
    """Ehlers Roofing Filter (HP=48, SS=10) — isolates cycles between 10 and 48 bars."""
    return _ehlers_roofing_filter(close, 48, 10)


def f33_cpkt_482_ehlers_roofing_value_125_20(close: pd.Series) -> pd.Series:
    """Ehlers Roofing Filter (HP=125, SS=20) — semi-annual cycle isolator."""
    return _ehlers_roofing_filter(close, 125, 20)


def f33_cpkt_483_ehlers_roofing_value_250_40(close: pd.Series) -> pd.Series:
    """Ehlers Roofing Filter (HP=250, SS=40) — annual cycle isolator."""
    return _ehlers_roofing_filter(close, 250, 40)


def f33_cpkt_484_ehlers_roofing_above_zero_indicator_48_10(close: pd.Series) -> pd.Series:
    """+1 when Roofing-48/10 > 0 (cycle component positive)."""
    rf = _ehlers_roofing_filter(close, 48, 10)
    return (rf > 0).astype(float).where(rf.notna(), np.nan)


def f33_cpkt_485_ehlers_roofing_slope_21d_48_10(close: pd.Series) -> pd.Series:
    """21d slope of Ehlers Roofing(48,10)."""
    return _rolling_slope(_ehlers_roofing_filter(close, 48, 10), MDAYS)


def f33_cpkt_486_ehlers_roofing_zero_cross_bearish_event_48_10(close: pd.Series) -> pd.Series:
    """+1 on bar where Ehlers Roofing(48,10) crosses + → 0."""
    rf = _ehlers_roofing_filter(close, 48, 10)
    return ((rf.shift(1) > 0) & (rf <= 0)).astype(float).where(rf.notna() & rf.shift(1).notna(), np.nan)


def f33_cpkt_487_days_since_ehlers_roofing_bearish_cross_48_10(close: pd.Series) -> pd.Series:
    """Bars since most recent Ehlers Roofing(48,10) bearish zero-cross."""
    rf = _ehlers_roofing_filter(close, 48, 10)
    flag = ((rf.shift(1) > 0) & (rf <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_488_ehlers_roofing_zscore_252d_48_10(close: pd.Series) -> pd.Series:
    """Z-score of Ehlers Roofing(48,10) over 252d."""
    return _rolling_zscore(_ehlers_roofing_filter(close, 48, 10), YDAYS)


def f33_cpkt_489_ehlers_roofing_zero_cross_count_252d_48_10(close: pd.Series) -> pd.Series:
    """Count of trailing 252d zero-crossings (either direction) of Ehlers Roofing(48,10)."""
    rf = _ehlers_roofing_filter(close, 48, 10)
    flag = ((np.sign(rf.shift(1)) != np.sign(rf)) & rf.notna() & rf.shift(1).notna()).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_490_ehlers_roofing_above_zero_indicator_250_40(close: pd.Series) -> pd.Series:
    """+1 when Ehlers Roofing(250,40) > 0."""
    rf = _ehlers_roofing_filter(close, 250, 40)
    return (rf > 0).astype(float).where(rf.notna(), np.nan)


# ============================================================
# Bucket E — KAMA-Coppock variants (491-500)
# ============================================================

def f33_cpkt_491_kama_value_close_n10(close: pd.Series) -> pd.Series:
    """Kaufman Adaptive Moving Average (n=10) on close."""
    return _kama(close, 10)


def f33_cpkt_492_kama_value_close_n21(close: pd.Series) -> pd.Series:
    """KAMA(n=21) on close (monthly-cycle adaptive)."""
    return _kama(close, MDAYS)


def f33_cpkt_493_kama_coppock_annual_value(close: pd.Series) -> pd.Series:
    """Coppock-style computation using KAMA(21) smoothing instead of WMA: ROC(294)+ROC(231) smoothed via KAMA."""
    return _kama_coppock_cycle(close, 294, 231, MDAYS)


def f33_cpkt_494_kama_coppock_quarterly_value(close: pd.Series) -> pd.Series:
    """KAMA-smoothed quarterly Coppock (63/42, KAMA(10))."""
    return _kama_coppock_cycle(close, QDAYS, 42, 10)


def f33_cpkt_495_kama_coppock_annual_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of KAMA-annual-Coppock."""
    return _rolling_slope(_kama_coppock_cycle(close, 294, 231, MDAYS), MDAYS)


def f33_cpkt_496_kama_coppock_annual_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when KAMA-annual-Coppock > 0."""
    k = _kama_coppock_cycle(close, 294, 231, MDAYS)
    return (k > 0).astype(float).where(k.notna(), np.nan)


def f33_cpkt_497_kama_close_minus_kama_long_diff(close: pd.Series) -> pd.Series:
    """KAMA(10) - KAMA(63) — adaptive MA separation."""
    return _kama(close, 10) - _kama(close, QDAYS)


def f33_cpkt_498_kama_close_n21_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of KAMA(21) — adaptive monthly trend."""
    return _rolling_slope(_kama(close, MDAYS), MDAYS)


def f33_cpkt_499_kama_coppock_annual_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of KAMA-annual-Coppock over 252d."""
    return _rolling_zscore(_kama_coppock_cycle(close, 294, 231, MDAYS), YDAYS)


def f33_cpkt_500_kama_coppock_annual_vs_std_coppock_diff(close: pd.Series) -> pd.Series:
    """KAMA-annual-Coppock minus standard annual Coppock (smoother-method divergence)."""
    return _kama_coppock_cycle(close, 294, 231, MDAYS) - _coppock_annual(close)


# ============================================================
# Bucket F — Vortex at long horizons (501-510)
# ============================================================

def f33_cpkt_501_vortex_pos_63d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(63d) — quarterly vortex positive."""
    return _vortex_pos(high, low, close, QDAYS)


def f33_cpkt_502_vortex_neg_63d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(63d) — quarterly vortex negative."""
    return _vortex_neg(high, low, close, QDAYS)


def f33_cpkt_503_vortex_pos_126d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(126d) — semi-annual vortex positive."""
    return _vortex_pos(high, low, close, 126)


def f33_cpkt_504_vortex_neg_126d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(126d) — semi-annual vortex negative."""
    return _vortex_neg(high, low, close, 126)


def f33_cpkt_505_vortex_pos_252d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(252d) — annual vortex positive."""
    return _vortex_pos(high, low, close, YDAYS)


def f33_cpkt_506_vortex_neg_252d_value(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(252d) — annual vortex negative."""
    return _vortex_neg(high, low, close, YDAYS)


def f33_cpkt_507_vortex_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(63d) - VI-(63d)."""
    return _vortex_pos(high, low, close, QDAYS) - _vortex_neg(high, low, close, QDAYS)


def f33_cpkt_508_vortex_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(252d) - VI-(252d) — secular vortex direction strength."""
    return _vortex_pos(high, low, close, YDAYS) - _vortex_neg(high, low, close, YDAYS)


def f33_cpkt_509_vortex_pos_63d_above_neg_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when VI+(63d) > VI-(63d) (quarterly bullish vortex regime)."""
    vp = _vortex_pos(high, low, close, QDAYS); vn = _vortex_neg(high, low, close, QDAYS)
    return (vp > vn).astype(float).where(vp.notna() & vn.notna(), np.nan)


def f33_cpkt_510_vortex_252d_bearish_cross_event(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where 252d-vortex VI- crosses above VI+ (secular bearish vortex cross)."""
    vp = _vortex_pos(high, low, close, YDAYS); vn = _vortex_neg(high, low, close, YDAYS)
    return ((vp.shift(1) > vn.shift(1)) & (vp <= vn)).astype(float).where(vp.notna() & vn.notna(), np.nan)


# ============================================================
# Bucket G — Stdev of long-momentum as regime gauge (511-525)
# ============================================================

def f33_cpkt_511_std_of_coppock_annual_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of annual Coppock — short-window volatility-of-momentum."""
    return _coppock_annual(close).rolling(QDAYS, min_periods=MDAYS).std()


def f33_cpkt_512_std_of_coppock_annual_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d std of annual Coppock — annual volatility-of-momentum."""
    return _coppock_annual(close).rolling(YDAYS, min_periods=QDAYS).std()


def f33_cpkt_513_std_of_coppock_quarterly_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of quarterly Coppock."""
    return _coppock_quarterly(close).rolling(QDAYS, min_periods=MDAYS).std()


def f33_cpkt_514_std_of_kst_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of standard KST."""
    return _kst(close).rolling(QDAYS, min_periods=MDAYS).std()


def f33_cpkt_515_std_of_kst_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d std of standard KST."""
    return _kst(close).rolling(YDAYS, min_periods=QDAYS).std()


def f33_cpkt_516_std_of_kst_long_term_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d std of long-term KST."""
    return _kst_long_term(close).rolling(YDAYS, min_periods=QDAYS).std()


def f33_cpkt_517_coppock_annual_std_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d-std of annual Coppock over 252d."""
    s = _coppock_annual(close).rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_zscore(s, YDAYS)


def f33_cpkt_518_kst_std_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d-std of KST over 252d."""
    s = _kst(close).rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_zscore(s, YDAYS)


def f33_cpkt_519_coppock_annual_std_compression_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-std of annual Coppock is below 30th-percentile of 252d (vol-of-mom compression)."""
    s = _coppock_annual(close).rolling(QDAYS, min_periods=MDAYS).std()
    rk = _pct_rank(s, YDAYS)
    return (rk < 0.3).astype(float).where(rk.notna(), np.nan)


def f33_cpkt_520_kst_std_compression_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-std of KST is below 30th-percentile of 252d."""
    s = _kst(close).rolling(QDAYS, min_periods=MDAYS).std()
    rk = _pct_rank(s, YDAYS)
    return (rk < 0.3).astype(float).where(rk.notna(), np.nan)


def f33_cpkt_521_coppock_annual_std_expansion_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-std of annual Coppock is above 70th-percentile of 252d (vol-of-mom expansion)."""
    s = _coppock_annual(close).rolling(QDAYS, min_periods=MDAYS).std()
    rk = _pct_rank(s, YDAYS)
    return (rk > 0.7).astype(float).where(rk.notna(), np.nan)


def f33_cpkt_522_coppock_annual_std_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of 63d-std of annual Coppock — vol-of-mom trend."""
    s = _coppock_annual(close).rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_slope(s, MDAYS)


def f33_cpkt_523_coppock_quarterly_std_expansion_indicator(close: pd.Series) -> pd.Series:
    """+1 when 63d-std of quarterly Coppock is above 70th-percentile of 252d."""
    s = _coppock_quarterly(close).rolling(QDAYS, min_periods=MDAYS).std()
    rk = _pct_rank(s, YDAYS)
    return (rk > 0.7).astype(float).where(rk.notna(), np.nan)


def f33_cpkt_524_std_of_macd_on_coppock_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of MACD-on-Coppock series."""
    return _macd_on(_coppock_annual(close), 12, 26).rolling(QDAYS, min_periods=MDAYS).std()


def f33_cpkt_525_std_of_cmo_252d_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of CMO(252) — annual-momentum-stability metric."""
    return _cmo(close, YDAYS).rolling(QDAYS, min_periods=MDAYS).std()


# ============================================================
# REGISTRY
# ============================================================

COPPOCK_CURVE_KST_BASE_REGISTRY_451_525 = {
    "f33_cpkt_451_rsi14_on_coppock_annual": {"inputs": ["close"], "func": f33_cpkt_451_rsi14_on_coppock_annual},
    "f33_cpkt_452_rsi14_on_coppock_quarterly": {"inputs": ["close"], "func": f33_cpkt_452_rsi14_on_coppock_quarterly},
    "f33_cpkt_453_rsi14_on_kst": {"inputs": ["close"], "func": f33_cpkt_453_rsi14_on_kst},
    "f33_cpkt_454_rsi14_on_kst_long_term": {"inputs": ["close"], "func": f33_cpkt_454_rsi14_on_kst_long_term},
    "f33_cpkt_455_rsi14_on_coppock_annual_above_70_indicator": {"inputs": ["close"], "func": f33_cpkt_455_rsi14_on_coppock_annual_above_70_indicator},
    "f33_cpkt_456_rsi14_on_kst_above_70_indicator": {"inputs": ["close"], "func": f33_cpkt_456_rsi14_on_kst_above_70_indicator},
    "f33_cpkt_457_rsi14_on_coppock_annual_slope_21d": {"inputs": ["close"], "func": f33_cpkt_457_rsi14_on_coppock_annual_slope_21d},
    "f33_cpkt_458_rsi14_on_kst_slope_21d": {"inputs": ["close"], "func": f33_cpkt_458_rsi14_on_kst_slope_21d},
    "f33_cpkt_459_rsi14_on_coppock_annual_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_459_rsi14_on_coppock_annual_zscore_252d},
    "f33_cpkt_460_rsi14_on_kst_long_term_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_460_rsi14_on_kst_long_term_zscore_252d},
    "f33_cpkt_461_macd_line_on_coppock_annual": {"inputs": ["close"], "func": f33_cpkt_461_macd_line_on_coppock_annual},
    "f33_cpkt_462_macd_signal_on_coppock_annual": {"inputs": ["close"], "func": f33_cpkt_462_macd_signal_on_coppock_annual},
    "f33_cpkt_463_macd_hist_on_coppock_annual": {"inputs": ["close"], "func": f33_cpkt_463_macd_hist_on_coppock_annual},
    "f33_cpkt_464_macd_on_coppock_above_zero_indicator": {"inputs": ["close"], "func": f33_cpkt_464_macd_on_coppock_above_zero_indicator},
    "f33_cpkt_465_macd_on_coppock_bearish_cross_event_indicator": {"inputs": ["close"], "func": f33_cpkt_465_macd_on_coppock_bearish_cross_event_indicator},
    "f33_cpkt_466_days_since_macd_on_coppock_bearish_cross": {"inputs": ["close"], "func": f33_cpkt_466_days_since_macd_on_coppock_bearish_cross},
    "f33_cpkt_467_macd_line_on_kst": {"inputs": ["close"], "func": f33_cpkt_467_macd_line_on_kst},
    "f33_cpkt_468_macd_hist_on_kst": {"inputs": ["close"], "func": f33_cpkt_468_macd_hist_on_kst},
    "f33_cpkt_469_macd_on_kst_bearish_cross_event_indicator": {"inputs": ["close"], "func": f33_cpkt_469_macd_on_kst_bearish_cross_event_indicator},
    "f33_cpkt_470_macd_on_coppock_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_470_macd_on_coppock_zscore_252d},
    "f33_cpkt_471_cmo_63d_value": {"inputs": ["close"], "func": f33_cpkt_471_cmo_63d_value},
    "f33_cpkt_472_cmo_126d_value": {"inputs": ["close"], "func": f33_cpkt_472_cmo_126d_value},
    "f33_cpkt_473_cmo_252d_value": {"inputs": ["close"], "func": f33_cpkt_473_cmo_252d_value},
    "f33_cpkt_474_cmo_63d_above_50_indicator": {"inputs": ["close"], "func": f33_cpkt_474_cmo_63d_above_50_indicator},
    "f33_cpkt_475_cmo_252d_above_50_indicator": {"inputs": ["close"], "func": f33_cpkt_475_cmo_252d_above_50_indicator},
    "f33_cpkt_476_cmo_63d_slope_21d": {"inputs": ["close"], "func": f33_cpkt_476_cmo_63d_slope_21d},
    "f33_cpkt_477_cmo_252d_slope_63d": {"inputs": ["close"], "func": f33_cpkt_477_cmo_252d_slope_63d},
    "f33_cpkt_478_cmo_63d_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_478_cmo_63d_zscore_252d},
    "f33_cpkt_479_cmo_252d_above_50_at_252d_high_indicator": {"inputs": ["close"], "func": f33_cpkt_479_cmo_252d_above_50_at_252d_high_indicator},
    "f33_cpkt_480_cmo_252d_days_since_above_50": {"inputs": ["close"], "func": f33_cpkt_480_cmo_252d_days_since_above_50},
    "f33_cpkt_481_ehlers_roofing_value_48_10": {"inputs": ["close"], "func": f33_cpkt_481_ehlers_roofing_value_48_10},
    "f33_cpkt_482_ehlers_roofing_value_125_20": {"inputs": ["close"], "func": f33_cpkt_482_ehlers_roofing_value_125_20},
    "f33_cpkt_483_ehlers_roofing_value_250_40": {"inputs": ["close"], "func": f33_cpkt_483_ehlers_roofing_value_250_40},
    "f33_cpkt_484_ehlers_roofing_above_zero_indicator_48_10": {"inputs": ["close"], "func": f33_cpkt_484_ehlers_roofing_above_zero_indicator_48_10},
    "f33_cpkt_485_ehlers_roofing_slope_21d_48_10": {"inputs": ["close"], "func": f33_cpkt_485_ehlers_roofing_slope_21d_48_10},
    "f33_cpkt_486_ehlers_roofing_zero_cross_bearish_event_48_10": {"inputs": ["close"], "func": f33_cpkt_486_ehlers_roofing_zero_cross_bearish_event_48_10},
    "f33_cpkt_487_days_since_ehlers_roofing_bearish_cross_48_10": {"inputs": ["close"], "func": f33_cpkt_487_days_since_ehlers_roofing_bearish_cross_48_10},
    "f33_cpkt_488_ehlers_roofing_zscore_252d_48_10": {"inputs": ["close"], "func": f33_cpkt_488_ehlers_roofing_zscore_252d_48_10},
    "f33_cpkt_489_ehlers_roofing_zero_cross_count_252d_48_10": {"inputs": ["close"], "func": f33_cpkt_489_ehlers_roofing_zero_cross_count_252d_48_10},
    "f33_cpkt_490_ehlers_roofing_above_zero_indicator_250_40": {"inputs": ["close"], "func": f33_cpkt_490_ehlers_roofing_above_zero_indicator_250_40},
    "f33_cpkt_491_kama_value_close_n10": {"inputs": ["close"], "func": f33_cpkt_491_kama_value_close_n10},
    "f33_cpkt_492_kama_value_close_n21": {"inputs": ["close"], "func": f33_cpkt_492_kama_value_close_n21},
    "f33_cpkt_493_kama_coppock_annual_value": {"inputs": ["close"], "func": f33_cpkt_493_kama_coppock_annual_value},
    "f33_cpkt_494_kama_coppock_quarterly_value": {"inputs": ["close"], "func": f33_cpkt_494_kama_coppock_quarterly_value},
    "f33_cpkt_495_kama_coppock_annual_slope_21d": {"inputs": ["close"], "func": f33_cpkt_495_kama_coppock_annual_slope_21d},
    "f33_cpkt_496_kama_coppock_annual_above_zero_indicator": {"inputs": ["close"], "func": f33_cpkt_496_kama_coppock_annual_above_zero_indicator},
    "f33_cpkt_497_kama_close_minus_kama_long_diff": {"inputs": ["close"], "func": f33_cpkt_497_kama_close_minus_kama_long_diff},
    "f33_cpkt_498_kama_close_n21_slope_21d": {"inputs": ["close"], "func": f33_cpkt_498_kama_close_n21_slope_21d},
    "f33_cpkt_499_kama_coppock_annual_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_499_kama_coppock_annual_zscore_252d},
    "f33_cpkt_500_kama_coppock_annual_vs_std_coppock_diff": {"inputs": ["close"], "func": f33_cpkt_500_kama_coppock_annual_vs_std_coppock_diff},
    "f33_cpkt_501_vortex_pos_63d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_501_vortex_pos_63d_value},
    "f33_cpkt_502_vortex_neg_63d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_502_vortex_neg_63d_value},
    "f33_cpkt_503_vortex_pos_126d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_503_vortex_pos_126d_value},
    "f33_cpkt_504_vortex_neg_126d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_504_vortex_neg_126d_value},
    "f33_cpkt_505_vortex_pos_252d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_505_vortex_pos_252d_value},
    "f33_cpkt_506_vortex_neg_252d_value": {"inputs": ["high", "low", "close"], "func": f33_cpkt_506_vortex_neg_252d_value},
    "f33_cpkt_507_vortex_gap_63d": {"inputs": ["high", "low", "close"], "func": f33_cpkt_507_vortex_gap_63d},
    "f33_cpkt_508_vortex_gap_252d": {"inputs": ["high", "low", "close"], "func": f33_cpkt_508_vortex_gap_252d},
    "f33_cpkt_509_vortex_pos_63d_above_neg_indicator": {"inputs": ["high", "low", "close"], "func": f33_cpkt_509_vortex_pos_63d_above_neg_indicator},
    "f33_cpkt_510_vortex_252d_bearish_cross_event": {"inputs": ["high", "low", "close"], "func": f33_cpkt_510_vortex_252d_bearish_cross_event},
    "f33_cpkt_511_std_of_coppock_annual_63d": {"inputs": ["close"], "func": f33_cpkt_511_std_of_coppock_annual_63d},
    "f33_cpkt_512_std_of_coppock_annual_252d": {"inputs": ["close"], "func": f33_cpkt_512_std_of_coppock_annual_252d},
    "f33_cpkt_513_std_of_coppock_quarterly_63d": {"inputs": ["close"], "func": f33_cpkt_513_std_of_coppock_quarterly_63d},
    "f33_cpkt_514_std_of_kst_63d": {"inputs": ["close"], "func": f33_cpkt_514_std_of_kst_63d},
    "f33_cpkt_515_std_of_kst_252d": {"inputs": ["close"], "func": f33_cpkt_515_std_of_kst_252d},
    "f33_cpkt_516_std_of_kst_long_term_252d": {"inputs": ["close"], "func": f33_cpkt_516_std_of_kst_long_term_252d},
    "f33_cpkt_517_coppock_annual_std_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_517_coppock_annual_std_zscore_252d},
    "f33_cpkt_518_kst_std_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_518_kst_std_zscore_252d},
    "f33_cpkt_519_coppock_annual_std_compression_indicator": {"inputs": ["close"], "func": f33_cpkt_519_coppock_annual_std_compression_indicator},
    "f33_cpkt_520_kst_std_compression_indicator": {"inputs": ["close"], "func": f33_cpkt_520_kst_std_compression_indicator},
    "f33_cpkt_521_coppock_annual_std_expansion_indicator": {"inputs": ["close"], "func": f33_cpkt_521_coppock_annual_std_expansion_indicator},
    "f33_cpkt_522_coppock_annual_std_slope_21d": {"inputs": ["close"], "func": f33_cpkt_522_coppock_annual_std_slope_21d},
    "f33_cpkt_523_coppock_quarterly_std_expansion_indicator": {"inputs": ["close"], "func": f33_cpkt_523_coppock_quarterly_std_expansion_indicator},
    "f33_cpkt_524_std_of_macd_on_coppock_63d": {"inputs": ["close"], "func": f33_cpkt_524_std_of_macd_on_coppock_63d},
    "f33_cpkt_525_std_of_cmo_252d_63d": {"inputs": ["close"], "func": f33_cpkt_525_std_of_cmo_252d_63d},
}
