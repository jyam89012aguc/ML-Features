"""coppock_curve_kst base features 526-600 — Pipeline 1b-technical (precision extension).

Individual signals: Coppock applied to log-returns (instead of ROC of price), cycle-
phase metrics (normalized regime-age, peak-to-peak phase), VWAP-anchored long-momentum,
KST signal-line events with magnitude/persistence, multi-MA-cross signals for adaptive
smoothers (KAMA/HMA/TEMA crosses), and per-set trend-score breadth values.

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


def _hma(s, n):
    half = max(int(n / 2), 1); sqn = max(int(np.sqrt(n)), 1)
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _tema(s, n):
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _kama(close, n=10, fast=2, slow=30):
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


def _roc_pct(s, n):
    return s.pct_change(n) * 100.0


def _coppock(close, n_long, n_short, n_wma):
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)


def _coppock_annual(close):
    return _coppock(close, 294, 231, 210)


def _coppock_quarterly(close):
    return _coppock(close, QDAYS, 42, MDAYS)


def _kst(close):
    return (1.0 * _sma(_roc_pct(close, 10), 10)
            + 2.0 * _sma(_roc_pct(close, 15), 10)
            + 3.0 * _sma(_roc_pct(close, 20), 10)
            + 4.0 * _sma(_roc_pct(close, 30), 15))


def _kst_short_term(close):
    return (1.0 * _sma(_roc_pct(close, 5), 5)
            + 2.0 * _sma(_roc_pct(close, 8), 5)
            + 3.0 * _sma(_roc_pct(close, 12), 5)
            + 4.0 * _sma(_roc_pct(close, 18), 8))


def _kst_long_term(close):
    return (1.0 * _sma(_roc_pct(close, 65), 21)
            + 2.0 * _sma(_roc_pct(close, 130), 21)
            + 3.0 * _sma(_roc_pct(close, 195), 21)
            + 4.0 * _sma(_roc_pct(close, 260), 42))


# ---------------------------- log-return Coppock helper ----------------------------

def _coppock_logret(close, n_long, n_short, n_wma):
    """Coppock variant computed on rolling-sum-of-log-returns instead of ROC of price.
    More symmetric in up vs down moves; less skewed for extreme moves."""
    logret = _safe_log(close).diff().fillna(0)
    long_sum = logret.rolling(n_long, min_periods=max(n_long // 3, 2)).sum() * 100.0
    short_sum = logret.rolling(n_short, min_periods=max(n_short // 3, 2)).sum() * 100.0
    return _wma(long_sum + short_sum, n_wma)


# ---------------------------- VWAP-anchored helpers ----------------------------

def _anchored_vwap_252d_low(close, volume):
    """VWAP anchored at trailing 252d low: cumulative price×vol from the most-recent 252d-low bar."""
    idx = pd.Series(np.arange(len(close)), index=close.index)
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    flag_low = (close == rmin).astype(int)
    last_low_idx = idx.where(flag_low == 1, np.nan).ffill().fillna(0).astype(int)
    pv = (close * volume).values
    v = volume.values
    pv_cum = np.cumsum(pv); v_cum = np.cumsum(v)
    out = np.full(len(close), np.nan)
    for i, anchor in enumerate(last_low_idx.values):
        if i >= anchor and v_cum[i] - (v_cum[anchor - 1] if anchor > 0 else 0) > 0:
            pv_seg = pv_cum[i] - (pv_cum[anchor - 1] if anchor > 0 else 0)
            v_seg = v_cum[i] - (v_cum[anchor - 1] if anchor > 0 else 0)
            out[i] = pv_seg / v_seg
    return pd.Series(out, index=close.index)


# ---------------------------- ROC of return Coppock for VWAP-anchored ----------------------------

def _coppock_on_vwap_anchored(close, volume, n_long, n_short, n_wma):
    """Coppock-style WMA-of-ROCs but on anchored-VWAP instead of close."""
    vwap = _anchored_vwap_252d_low(close, volume)
    return _wma(_roc_pct(vwap, n_long) + _roc_pct(vwap, n_short), n_wma)


# ============================================================
# Bucket H — Coppock on log-returns (526-535)
# ============================================================

def f33_cpkt_526_coppock_logret_annual_value(close: pd.Series) -> pd.Series:
    """Annual-cycle Coppock computed on rolling-sum-log-returns (294/231/210)."""
    return _coppock_logret(close, 294, 231, 210)


def f33_cpkt_527_coppock_logret_quarterly_value(close: pd.Series) -> pd.Series:
    """Quarterly Coppock on log-returns (63/42/21)."""
    return _coppock_logret(close, QDAYS, 42, MDAYS)


def f33_cpkt_528_coppock_logret_semi_annual_value(close: pd.Series) -> pd.Series:
    """Semi-annual Coppock on log-returns (126/84/42)."""
    return _coppock_logret(close, 126, 84, 42)


def f33_cpkt_529_coppock_logret_biennial_value(close: pd.Series) -> pd.Series:
    """Biennial Coppock on log-returns (504/378/210)."""
    return _coppock_logret(close, DDAYS_2Y, 378, 210)


def f33_cpkt_530_coppock_logret_annual_slope_63d(close: pd.Series) -> pd.Series:
    """63d slope of annual log-return Coppock."""
    return _rolling_slope(_coppock_logret(close, 294, 231, 210), QDAYS)


def f33_cpkt_531_coppock_logret_annual_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when annual log-return Coppock > 0."""
    c = _coppock_logret(close, 294, 231, 210)
    return (c > 0).astype(float).where(c.notna(), np.nan)


def f33_cpkt_532_coppock_logret_annual_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of annual log-return Coppock over 252d."""
    return _rolling_zscore(_coppock_logret(close, 294, 231, 210), YDAYS)


def f33_cpkt_533_coppock_logret_annual_minus_std_coppock_diff(close: pd.Series) -> pd.Series:
    """Log-return-Coppock minus ROC-based-Coppock (annual) — captures distributional skew effect."""
    return _coppock_logret(close, 294, 231, 210) - _coppock_annual(close)


def f33_cpkt_534_coppock_logret_quarterly_slope_21d(close: pd.Series) -> pd.Series:
    """21d slope of quarterly log-return Coppock."""
    return _rolling_slope(_coppock_logret(close, QDAYS, 42, MDAYS), MDAYS)


def f33_cpkt_535_coppock_logret_biennial_above_zero_indicator(close: pd.Series) -> pd.Series:
    """+1 when biennial log-return Coppock > 0."""
    c = _coppock_logret(close, DDAYS_2Y, 378, 210)
    return (c > 0).astype(float).where(c.notna(), np.nan)


# ============================================================
# Bucket I — Cycle phase metrics (536-545)
# ============================================================

def _zero_cross_period_mean(series, win=DDAYS_2Y):
    """Mean bar-gap between zero-crossings over win, computed in a rolling fashion."""
    flag = ((np.sign(series.shift(1)) != np.sign(series)) & series.notna() & series.shift(1).notna()).astype(int)
    idx = pd.Series(np.arange(len(series)), index=series.index)
    last_x = idx.where(flag == 1, np.nan).ffill()
    gap = idx - last_x
    return gap.where(flag == 1, np.nan).rolling(win, min_periods=max(win // 3, 2)).mean()


def _peak_to_peak_period_mean(series, win=DDAYS_2Y):
    """Mean bar-gap between local-21d-peaks over win."""
    is_pk = ((series == series.rolling(MDAYS, min_periods=WDAYS).max()) & (series > series.shift(3))).astype(int)
    idx = pd.Series(np.arange(len(series)), index=series.index)
    last_pk = idx.where(is_pk == 1, np.nan).ffill()
    gap = idx - last_pk
    return gap.where(is_pk == 1, np.nan).rolling(win, min_periods=max(win // 3, 2)).mean()


def _coppock_annual_phase_normalized(close):
    """Helper: bars-since-last-zero-cross / mean-cycle-period for annual Coppock."""
    c = _coppock_annual(close)
    flag = ((np.sign(c.shift(1)) != np.sign(c)) & c.notna() & c.shift(1).notna()).astype(int)
    age = _bars_since_true(flag.astype(float))
    period = _zero_cross_period_mean(c, DDAYS_2Y)
    return _safe_div(age, period)


def f33_cpkt_536_coppock_annual_phase_normalized(close: pd.Series) -> pd.Series:
    """Bars-since-last-zero-cross / mean-period — normalized phase position within cycle [0..many]."""
    return _coppock_annual_phase_normalized(close)


def f33_cpkt_537_kst_phase_normalized(close: pd.Series) -> pd.Series:
    """Phase position within KST cycle (bars-since-cross / mean-period)."""
    k = _kst(close)
    flag = ((np.sign(k.shift(1)) != np.sign(k)) & k.notna() & k.shift(1).notna()).astype(int)
    age = _bars_since_true(flag.astype(float))
    period = _zero_cross_period_mean(k, DDAYS_2Y)
    return _safe_div(age, period)


def f33_cpkt_538_coppock_annual_peak_to_peak_phase(close: pd.Series) -> pd.Series:
    """Bars since last local-21d-peak / mean-peak-to-peak-period for annual Coppock."""
    c = _coppock_annual(close)
    is_pk = ((c == c.rolling(MDAYS, min_periods=WDAYS).max()) & (c > c.shift(3))).astype(int)
    age = _bars_since_true(is_pk.astype(float))
    period = _peak_to_peak_period_mean(c, DDAYS_2Y)
    return _safe_div(age, period)


def f33_cpkt_539_kst_peak_to_peak_phase(close: pd.Series) -> pd.Series:
    """Peak-to-peak phase for KST."""
    k = _kst(close)
    is_pk = ((k == k.rolling(MDAYS, min_periods=WDAYS).max()) & (k > k.shift(3))).astype(int)
    age = _bars_since_true(is_pk.astype(float))
    period = _peak_to_peak_period_mean(k, DDAYS_2Y)
    return _safe_div(age, period)


def f33_cpkt_540_coppock_annual_quadrant_top_rising_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock-annual > 0 AND slope_21d > 0 (top-right quadrant: bullish acceleration)."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    return ((c > 0) & (s > 0)).astype(float).where(c.notna() & s.notna(), np.nan)


def f33_cpkt_541_coppock_annual_quadrant_top_falling_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock-annual > 0 AND slope_21d < 0 (top-left quadrant: bullish but decelerating — top forming)."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    return ((c > 0) & (s < 0)).astype(float).where(c.notna() & s.notna(), np.nan)


def f33_cpkt_542_coppock_annual_quadrant_bot_rising_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock-annual < 0 AND slope_21d > 0 (bottom-right: bearish but improving)."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    return ((c < 0) & (s > 0)).astype(float).where(c.notna() & s.notna(), np.nan)


def f33_cpkt_543_coppock_annual_quadrant_bot_falling_indicator(close: pd.Series) -> pd.Series:
    """+1 when Coppock-annual < 0 AND slope_21d < 0 (bottom-left: bearish accelerating)."""
    c = _coppock_annual(close)
    s = _rolling_slope(c, MDAYS)
    return ((c < 0) & (s < 0)).astype(float).where(c.notna() & s.notna(), np.nan)


def f33_cpkt_544_kst_quadrant_top_falling_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST > 0 AND slope_21d < 0 (KST topping quadrant)."""
    k = _kst(close)
    s = _rolling_slope(k, MDAYS)
    return ((k > 0) & (s < 0)).astype(float).where(k.notna() & s.notna(), np.nan)


def f33_cpkt_545_coppock_annual_phase_above_half_indicator(close: pd.Series) -> pd.Series:
    """+1 when normalized phase > 0.5 (past mid-cycle — closer to next zero-cross than to last)."""
    p = _coppock_annual_phase_normalized(close)
    return (p > 0.5).astype(float).where(p.notna(), np.nan)


# ============================================================
# Bucket J — VWAP-anchored long-momentum (546-555)
# ============================================================

def f33_cpkt_546_anchored_vwap_252d_low_value(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWAP anchored at the most-recent 252d-trailing-low bar."""
    return _anchored_vwap_252d_low(close, volume)


def f33_cpkt_547_close_minus_anchored_vwap_252d_low_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - anchored-VWAP-252d-low) / anchored-VWAP-252d-low (× 100)."""
    vwap = _anchored_vwap_252d_low(close, volume)
    return 100.0 * _safe_div(close - vwap, vwap)


def f33_cpkt_548_anchored_vwap_252d_low_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of anchored VWAP."""
    return _rolling_slope(_anchored_vwap_252d_low(close, volume), MDAYS)


def f33_cpkt_549_close_above_anchored_vwap_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when close > anchored-VWAP-252d-low."""
    vwap = _anchored_vwap_252d_low(close, volume)
    return (close > vwap).astype(float).where(vwap.notna(), np.nan)


def f33_cpkt_550_close_above_anchored_vwap_persistence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where close > anchored-VWAP-252d-low."""
    vwap = _anchored_vwap_252d_low(close, volume)
    return (close > vwap).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_551_coppock_on_vwap_anchored_value(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual-cycle Coppock computed on anchored-VWAP-252d-low instead of close."""
    return _coppock_on_vwap_anchored(close, volume, 294, 231, 210)


def f33_cpkt_552_coppock_on_vwap_anchored_minus_std_coppock_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coppock-on-anchored-VWAP minus standard Coppock (anchored-cumulative-flow effect)."""
    return _coppock_on_vwap_anchored(close, volume, 294, 231, 210) - _coppock_annual(close)


def f33_cpkt_553_coppock_on_vwap_anchored_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of Coppock-on-anchored-VWAP."""
    return _rolling_slope(_coppock_on_vwap_anchored(close, volume, 294, 231, 210), QDAYS)


def f33_cpkt_554_coppock_on_vwap_anchored_above_zero_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when Coppock-on-anchored-VWAP > 0."""
    c = _coppock_on_vwap_anchored(close, volume, 294, 231, 210)
    return (c > 0).astype(float).where(c.notna(), np.nan)


def f33_cpkt_555_anchored_vwap_dist_pct_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score over 252d of (close - anchored-VWAP)/anchored-VWAP%."""
    vwap = _anchored_vwap_252d_low(close, volume)
    dist = 100.0 * _safe_div(close - vwap, vwap)
    return _rolling_zscore(dist, YDAYS)


# ============================================================
# Bucket K — KST signal/slope distinct events (556-570)
# ============================================================

def f33_cpkt_556_kst_signal_cross_magnitude_at_event(close: pd.Series) -> pd.Series:
    """KST value at moment of last bearish signal-line cross (held forward) — cross altitude."""
    k = _kst(close); sig = _sma(k, 9)
    diff = k - sig
    flag = ((diff.shift(1) > 0) & (diff <= 0))
    return k.where(flag, np.nan).ffill()


def f33_cpkt_557_kst_signal_cross_magnitude_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of KST-at-cross over 252d."""
    k = _kst(close); sig = _sma(k, 9)
    diff = k - sig
    flag = ((diff.shift(1) > 0) & (diff <= 0))
    altitude = k.where(flag, np.nan).ffill()
    return _rolling_zscore(altitude, YDAYS)


def f33_cpkt_558_kst_long_term_signal_cross_magnitude(close: pd.Series) -> pd.Series:
    """Long-term KST value at moment of last bearish signal cross."""
    lk = _kst_long_term(close); sig = _sma(lk, 21)
    diff = lk - sig
    flag = ((diff.shift(1) > 0) & (diff <= 0))
    return lk.where(flag, np.nan).ffill()


def f33_cpkt_559_kst_short_term_signal_cross_magnitude(close: pd.Series) -> pd.Series:
    """Short-term KST value at moment of last bearish signal cross."""
    sk = _kst_short_term(close); sig = _sma(sk, 5)
    diff = sk - sig
    flag = ((diff.shift(1) > 0) & (diff <= 0))
    return sk.where(flag, np.nan).ffill()


def f33_cpkt_560_kst_signal_cross_at_overbought_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST bearish signal cross fires AND KST in top 90th-percentile of 252d (cross at OB)."""
    k = _kst(close); sig = _sma(k, 9)
    flag = ((k.shift(1) - sig.shift(1) > 0) & (k - sig <= 0)).astype(float)
    rk = _pct_rank(k, YDAYS)
    return (flag * (rk > 0.9).astype(float)).where(flag.notna() & rk.notna(), np.nan)


def f33_cpkt_561_kst_consec_below_signal_streak(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where KST < signal line."""
    k = _kst(close); sig = _sma(k, 9)
    flag = (k - sig < 0).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_562_kst_long_consec_below_signal_streak(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where long-term KST < its 21d signal."""
    lk = _kst_long_term(close); sig = _sma(lk, 21)
    flag = (lk - sig < 0).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_563_kst_short_consec_above_signal_streak(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where short-term KST > its 5d signal."""
    sk = _kst_short_term(close); sig = _sma(sk, 5)
    flag = (sk - sig > 0).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float)


def f33_cpkt_564_kst_signal_cross_count_504d(close: pd.Series) -> pd.Series:
    """Count of KST bearish signal-line crosses in trailing 504d (long-cycle instability)."""
    k = _kst(close); sig = _sma(k, 9)
    flag = ((k.shift(1) - sig.shift(1) > 0) & (k - sig <= 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f33_cpkt_565_kst_long_term_signal_cross_count_504d(close: pd.Series) -> pd.Series:
    """Count of long-term-KST bearish signal-line crosses in trailing 504d."""
    lk = _kst_long_term(close); sig = _sma(lk, 21)
    flag = ((lk.shift(1) - sig.shift(1) > 0) & (lk - sig <= 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f33_cpkt_566_kst_signal_diff_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (KST - signal-line) over 252d."""
    k = _kst(close); sig = _sma(k, 9)
    return _rolling_zscore(k - sig, YDAYS)


def f33_cpkt_567_kst_long_term_signal_diff_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of (long-term-KST - 21d-signal) over 504d."""
    lk = _kst_long_term(close); sig = _sma(lk, 21)
    return _rolling_zscore(lk - sig, DDAYS_2Y)


def f33_cpkt_568_kst_signal_diff_negative_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where KST - signal < 0."""
    k = _kst(close); sig = _sma(k, 9)
    return (k - sig < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_569_kst_signal_cross_at_close_252d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when KST bearish signal cross fires AND close within 1% of 252d max."""
    k = _kst(close); sig = _sma(k, 9)
    flag = ((k.shift(1) - sig.shift(1) > 0) & (k - sig <= 0)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan)


def f33_cpkt_570_kst_long_term_signal_cross_at_close_1260d_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when long-term-KST bearish signal cross fires AND close within 2% of 1260d max."""
    lk = _kst_long_term(close); sig = _sma(lk, 21)
    flag = ((lk.shift(1) - sig.shift(1) > 0) & (lk - sig <= 0)).astype(float)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan)


# ============================================================
# Bucket L — Multi-MA-cross for long-smoothed momentum (571-585)
# ============================================================

def f33_cpkt_571_kama_10_vs_kama_63_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where KAMA(10) crosses below KAMA(63) — adaptive-MA bearish cross."""
    k10 = _kama(close, 10); k63 = _kama(close, QDAYS)
    diff = k10 - k63
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_572_days_since_kama_10_below_63_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent KAMA(10) bearish cross below KAMA(63)."""
    k10 = _kama(close, 10); k63 = _kama(close, QDAYS)
    flag = ((k10.shift(1) - k63.shift(1) > 0) & (k10 - k63 <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_573_kama_10_above_63_indicator(close: pd.Series) -> pd.Series:
    """+1 when KAMA(10) > KAMA(63)."""
    k10 = _kama(close, 10); k63 = _kama(close, QDAYS)
    return (k10 > k63).astype(float).where(k10.notna() & k63.notna(), np.nan)


def f33_cpkt_574_hma_21_vs_hma_63_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where HMA(21) crosses below HMA(63) — Hull-MA bearish cross."""
    h21 = _hma(close, MDAYS); h63 = _hma(close, QDAYS)
    diff = h21 - h63
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_575_days_since_hma_21_below_63_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent HMA(21) bearish cross below HMA(63)."""
    h21 = _hma(close, MDAYS); h63 = _hma(close, QDAYS)
    flag = ((h21.shift(1) - h63.shift(1) > 0) & (h21 - h63 <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_576_hma_21_above_63_indicator(close: pd.Series) -> pd.Series:
    """+1 when HMA(21) > HMA(63)."""
    h21 = _hma(close, MDAYS); h63 = _hma(close, QDAYS)
    return (h21 > h63).astype(float).where(h21.notna() & h63.notna(), np.nan)


def f33_cpkt_577_tema_21_vs_tema_63_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where TEMA(21) crosses below TEMA(63) — triple-EMA bearish cross."""
    t21 = _tema(close, MDAYS); t63 = _tema(close, QDAYS)
    diff = t21 - t63
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_578_days_since_tema_21_below_63_cross(close: pd.Series) -> pd.Series:
    """Bars since most recent TEMA(21) bearish cross below TEMA(63)."""
    t21 = _tema(close, MDAYS); t63 = _tema(close, QDAYS)
    flag = ((t21.shift(1) - t63.shift(1) > 0) & (t21 - t63 <= 0)).astype(float)
    return _bars_since_true(flag)


def f33_cpkt_579_tema_21_above_63_indicator(close: pd.Series) -> pd.Series:
    """+1 when TEMA(21) > TEMA(63)."""
    t21 = _tema(close, MDAYS); t63 = _tema(close, QDAYS)
    return (t21 > t63).astype(float).where(t21.notna() & t63.notna(), np.nan)


def f33_cpkt_580_kama_63_vs_kama_252_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where KAMA(63) crosses below KAMA(252) — long-cycle adaptive-MA bearish cross."""
    k63 = _kama(close, QDAYS); k252 = _kama(close, YDAYS)
    diff = k63 - k252
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_581_hma_63_vs_hma_252_cross_bearish_event(close: pd.Series) -> pd.Series:
    """+1 on bar where HMA(63) crosses below HMA(252)."""
    h63 = _hma(close, QDAYS); h252 = _hma(close, YDAYS)
    diff = h63 - h252
    return ((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna() & diff.shift(1).notna(), np.nan)


def f33_cpkt_582_kama_below_long_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where KAMA(10) < KAMA(63)."""
    k10 = _kama(close, 10); k63 = _kama(close, QDAYS)
    return (k10 < k63).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f33_cpkt_583_kama_10_minus_63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (KAMA(10) - KAMA(63)) over 252d."""
    return _rolling_zscore(_kama(close, 10) - _kama(close, QDAYS), YDAYS)


def f33_cpkt_584_hma_21_minus_63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (HMA(21) - HMA(63)) over 252d."""
    return _rolling_zscore(_hma(close, MDAYS) - _hma(close, QDAYS), YDAYS)


def f33_cpkt_585_tema_21_minus_63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (TEMA(21) - TEMA(63)) over 252d."""
    return _rolling_zscore(_tema(close, MDAYS) - _tema(close, QDAYS), YDAYS)


# ============================================================
# Bucket M — Trend score breadth (586-600)
# ============================================================

def _coppock_semi_annual(close):
    return _coppock(close, 126, 84, 42)


def _coppock_biennial(close):
    return _coppock(close, DDAYS_2Y, 378, 210)


def _trend_score_4cycle_frac(close):
    """Helper: fraction of 4 Coppock cycles with value > 0."""
    parts = [(_coppock_quarterly(close) > 0).astype(float),
             (_coppock_semi_annual(close) > 0).astype(float),
             (_coppock_annual(close) > 0).astype(float),
             (_coppock_biennial(close) > 0).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def _trend_score_3kst_frac(close):
    """Helper: fraction of 3 KST variants with value > 0."""
    parts = [(_kst_short_term(close) > 0).astype(float),
             (_kst(close) > 0).astype(float),
             (_kst_long_term(close) > 0).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_586_trend_score_4cycle_coppock_fraction_positive(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of 4 Coppock cycles (quarterly/semi/annual/biennial) with value > 0."""
    return _trend_score_4cycle_frac(close)


def f33_cpkt_587_trend_score_3kst_fraction_positive(close: pd.Series) -> pd.Series:
    """Fraction (0..1) of 3 KST variants (short/std/long) with value > 0."""
    return _trend_score_3kst_frac(close)


def f33_cpkt_588_trend_score_3smoothers_fraction_positive_ROC21(close: pd.Series) -> pd.Series:
    """Fraction of 3 smoothers (TEMA(21)/DEMA-no, HMA(21)/EMA(21)) on close that are > close 21 ago."""
    parts = [(_tema(close, MDAYS) > close.shift(MDAYS)).astype(float),
             (_hma(close, MDAYS) > close.shift(MDAYS)).astype(float),
             (_ema(close, MDAYS) > close.shift(MDAYS)).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def _trend_score_long_frac(close):
    """Helper: fraction of 6 long-momentum indicators currently positive."""
    cmo = _cmo_local(close, YDAYS)
    dpo = close - _sma(close, YDAYS)
    parts = [(_coppock_annual(close) > 0).astype(float),
             (_coppock_biennial(close) > 0).astype(float),
             (_kst(close) > 0).astype(float),
             (_kst_long_term(close) > 0).astype(float),
             (cmo > 0).astype(float),
             (dpo > 0).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_589_trend_score_long_indicator_fraction_positive(close: pd.Series) -> pd.Series:
    """Fraction of 6 long-momentum indicators currently positive: Coppock-annual, Coppock-biennial,
    KST, KST-long, CMO(252), DPO(252)."""
    return _trend_score_long_frac(close)


def _cmo_local(close, n):
    delta = close.diff()
    sum_up = delta.clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    sum_dn = (-delta).clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(sum_up - sum_dn, sum_up + sum_dn)


def f33_cpkt_590_trend_score_4cycle_coppock_fraction_rising(close: pd.Series) -> pd.Series:
    """Fraction of 4 Coppock cycles with 21d slope > 0."""
    parts = [(_rolling_slope(_coppock_quarterly(close), MDAYS) > 0).astype(float),
             (_rolling_slope(_coppock_semi_annual(close), MDAYS) > 0).astype(float),
             (_rolling_slope(_coppock_annual(close), MDAYS) > 0).astype(float),
             (_rolling_slope(_coppock_biennial(close), MDAYS) > 0).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_591_trend_score_3kst_fraction_rising(close: pd.Series) -> pd.Series:
    """Fraction of 3 KST variants with 21d slope > 0."""
    parts = [(_rolling_slope(_kst_short_term(close), MDAYS) > 0).astype(float),
             (_rolling_slope(_kst(close), MDAYS) > 0).astype(float),
             (_rolling_slope(_kst_long_term(close), MDAYS) > 0).astype(float)]
    df = pd.concat([p.rename(f"p{i}") for i, p in enumerate(parts)], axis=1)
    return df.mean(axis=1)


def f33_cpkt_592_trend_score_4cycle_coppock_value_drop_below_half_at_high_indicator(close: pd.Series) -> pd.Series:
    """+1 when 4cycle-positive-fraction drops <= 0.5 AND close near 252d max."""
    frac = _trend_score_4cycle_frac(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((frac <= 0.5) & (near == 1)).astype(float).where(frac.notna() & near.notna(), np.nan)


def f33_cpkt_593_trend_score_zero_indicator_breadth_collapse_event(close: pd.Series) -> pd.Series:
    """+1 on bar where 4cycle-positive-fraction was > 0.75 21d ago AND is < 0.5 today (breadth collapse)."""
    frac = _trend_score_4cycle_frac(close)
    return ((frac.shift(MDAYS) > 0.75) & (frac < 0.5)).astype(float).where(frac.notna() & frac.shift(MDAYS).notna(), np.nan)


def f33_cpkt_594_trend_score_change_21d(close: pd.Series) -> pd.Series:
    """21d change in 4cycle-Coppock-positive-fraction."""
    frac = _trend_score_4cycle_frac(close)
    return frac - frac.shift(MDAYS)


def f33_cpkt_595_trend_score_change_63d(close: pd.Series) -> pd.Series:
    """63d change in 4cycle-Coppock-positive-fraction."""
    frac = _trend_score_4cycle_frac(close)
    return frac - frac.shift(QDAYS)


def f33_cpkt_596_trend_score_kst_change_21d(close: pd.Series) -> pd.Series:
    """21d change in 3KST-positive-fraction."""
    frac = _trend_score_3kst_frac(close)
    return frac - frac.shift(MDAYS)


def f33_cpkt_597_trend_score_long_indicator_change_21d(close: pd.Series) -> pd.Series:
    """21d change in 6-long-indicator-positive-fraction."""
    frac = _trend_score_long_frac(close)
    return frac - frac.shift(MDAYS)


def f33_cpkt_598_trend_score_3kst_all_positive_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where ALL 3 KST variants > 0."""
    flag = ((_kst_short_term(close) > 0) & (_kst(close) > 0) & (_kst_long_term(close) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_599_trend_score_4cycle_all_positive_persistence_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where ALL 4 Coppock cycles > 0."""
    flag = ((_coppock_quarterly(close) > 0) & (_coppock_semi_annual(close) > 0)
            & (_coppock_annual(close) > 0) & (_coppock_biennial(close) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f33_cpkt_600_trend_score_long_indicator_zero_persistence_indicator_at_high(close: pd.Series) -> pd.Series:
    """+1 when 6-long-indicator-fraction drops to 0 AND close within 1% of 252d max (regime collapse at top)."""
    frac = _trend_score_long_frac(close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((frac < 0.1) & (near == 1)).astype(float).where(frac.notna() & near.notna(), np.nan)


# ============================================================
# REGISTRY
# ============================================================

COPPOCK_CURVE_KST_BASE_REGISTRY_526_600 = {
    "f33_cpkt_526_coppock_logret_annual_value": {"inputs": ["close"], "func": f33_cpkt_526_coppock_logret_annual_value},
    "f33_cpkt_527_coppock_logret_quarterly_value": {"inputs": ["close"], "func": f33_cpkt_527_coppock_logret_quarterly_value},
    "f33_cpkt_528_coppock_logret_semi_annual_value": {"inputs": ["close"], "func": f33_cpkt_528_coppock_logret_semi_annual_value},
    "f33_cpkt_529_coppock_logret_biennial_value": {"inputs": ["close"], "func": f33_cpkt_529_coppock_logret_biennial_value},
    "f33_cpkt_530_coppock_logret_annual_slope_63d": {"inputs": ["close"], "func": f33_cpkt_530_coppock_logret_annual_slope_63d},
    "f33_cpkt_531_coppock_logret_annual_above_zero_indicator": {"inputs": ["close"], "func": f33_cpkt_531_coppock_logret_annual_above_zero_indicator},
    "f33_cpkt_532_coppock_logret_annual_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_532_coppock_logret_annual_zscore_252d},
    "f33_cpkt_533_coppock_logret_annual_minus_std_coppock_diff": {"inputs": ["close"], "func": f33_cpkt_533_coppock_logret_annual_minus_std_coppock_diff},
    "f33_cpkt_534_coppock_logret_quarterly_slope_21d": {"inputs": ["close"], "func": f33_cpkt_534_coppock_logret_quarterly_slope_21d},
    "f33_cpkt_535_coppock_logret_biennial_above_zero_indicator": {"inputs": ["close"], "func": f33_cpkt_535_coppock_logret_biennial_above_zero_indicator},
    "f33_cpkt_536_coppock_annual_phase_normalized": {"inputs": ["close"], "func": f33_cpkt_536_coppock_annual_phase_normalized},
    "f33_cpkt_537_kst_phase_normalized": {"inputs": ["close"], "func": f33_cpkt_537_kst_phase_normalized},
    "f33_cpkt_538_coppock_annual_peak_to_peak_phase": {"inputs": ["close"], "func": f33_cpkt_538_coppock_annual_peak_to_peak_phase},
    "f33_cpkt_539_kst_peak_to_peak_phase": {"inputs": ["close"], "func": f33_cpkt_539_kst_peak_to_peak_phase},
    "f33_cpkt_540_coppock_annual_quadrant_top_rising_indicator": {"inputs": ["close"], "func": f33_cpkt_540_coppock_annual_quadrant_top_rising_indicator},
    "f33_cpkt_541_coppock_annual_quadrant_top_falling_indicator": {"inputs": ["close"], "func": f33_cpkt_541_coppock_annual_quadrant_top_falling_indicator},
    "f33_cpkt_542_coppock_annual_quadrant_bot_rising_indicator": {"inputs": ["close"], "func": f33_cpkt_542_coppock_annual_quadrant_bot_rising_indicator},
    "f33_cpkt_543_coppock_annual_quadrant_bot_falling_indicator": {"inputs": ["close"], "func": f33_cpkt_543_coppock_annual_quadrant_bot_falling_indicator},
    "f33_cpkt_544_kst_quadrant_top_falling_indicator": {"inputs": ["close"], "func": f33_cpkt_544_kst_quadrant_top_falling_indicator},
    "f33_cpkt_545_coppock_annual_phase_above_half_indicator": {"inputs": ["close"], "func": f33_cpkt_545_coppock_annual_phase_above_half_indicator},
    "f33_cpkt_546_anchored_vwap_252d_low_value": {"inputs": ["close", "volume"], "func": f33_cpkt_546_anchored_vwap_252d_low_value},
    "f33_cpkt_547_close_minus_anchored_vwap_252d_low_pct": {"inputs": ["close", "volume"], "func": f33_cpkt_547_close_minus_anchored_vwap_252d_low_pct},
    "f33_cpkt_548_anchored_vwap_252d_low_slope_21d": {"inputs": ["close", "volume"], "func": f33_cpkt_548_anchored_vwap_252d_low_slope_21d},
    "f33_cpkt_549_close_above_anchored_vwap_indicator": {"inputs": ["close", "volume"], "func": f33_cpkt_549_close_above_anchored_vwap_indicator},
    "f33_cpkt_550_close_above_anchored_vwap_persistence_63d": {"inputs": ["close", "volume"], "func": f33_cpkt_550_close_above_anchored_vwap_persistence_63d},
    "f33_cpkt_551_coppock_on_vwap_anchored_value": {"inputs": ["close", "volume"], "func": f33_cpkt_551_coppock_on_vwap_anchored_value},
    "f33_cpkt_552_coppock_on_vwap_anchored_minus_std_coppock_diff": {"inputs": ["close", "volume"], "func": f33_cpkt_552_coppock_on_vwap_anchored_minus_std_coppock_diff},
    "f33_cpkt_553_coppock_on_vwap_anchored_slope_63d": {"inputs": ["close", "volume"], "func": f33_cpkt_553_coppock_on_vwap_anchored_slope_63d},
    "f33_cpkt_554_coppock_on_vwap_anchored_above_zero_indicator": {"inputs": ["close", "volume"], "func": f33_cpkt_554_coppock_on_vwap_anchored_above_zero_indicator},
    "f33_cpkt_555_anchored_vwap_dist_pct_zscore_252d": {"inputs": ["close", "volume"], "func": f33_cpkt_555_anchored_vwap_dist_pct_zscore_252d},
    "f33_cpkt_556_kst_signal_cross_magnitude_at_event": {"inputs": ["close"], "func": f33_cpkt_556_kst_signal_cross_magnitude_at_event},
    "f33_cpkt_557_kst_signal_cross_magnitude_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_557_kst_signal_cross_magnitude_zscore_252d},
    "f33_cpkt_558_kst_long_term_signal_cross_magnitude": {"inputs": ["close"], "func": f33_cpkt_558_kst_long_term_signal_cross_magnitude},
    "f33_cpkt_559_kst_short_term_signal_cross_magnitude": {"inputs": ["close"], "func": f33_cpkt_559_kst_short_term_signal_cross_magnitude},
    "f33_cpkt_560_kst_signal_cross_at_overbought_indicator": {"inputs": ["close"], "func": f33_cpkt_560_kst_signal_cross_at_overbought_indicator},
    "f33_cpkt_561_kst_consec_below_signal_streak": {"inputs": ["close"], "func": f33_cpkt_561_kst_consec_below_signal_streak},
    "f33_cpkt_562_kst_long_consec_below_signal_streak": {"inputs": ["close"], "func": f33_cpkt_562_kst_long_consec_below_signal_streak},
    "f33_cpkt_563_kst_short_consec_above_signal_streak": {"inputs": ["close"], "func": f33_cpkt_563_kst_short_consec_above_signal_streak},
    "f33_cpkt_564_kst_signal_cross_count_504d": {"inputs": ["close"], "func": f33_cpkt_564_kst_signal_cross_count_504d},
    "f33_cpkt_565_kst_long_term_signal_cross_count_504d": {"inputs": ["close"], "func": f33_cpkt_565_kst_long_term_signal_cross_count_504d},
    "f33_cpkt_566_kst_signal_diff_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_566_kst_signal_diff_zscore_252d},
    "f33_cpkt_567_kst_long_term_signal_diff_zscore_504d": {"inputs": ["close"], "func": f33_cpkt_567_kst_long_term_signal_diff_zscore_504d},
    "f33_cpkt_568_kst_signal_diff_negative_persistence_63d": {"inputs": ["close"], "func": f33_cpkt_568_kst_signal_diff_negative_persistence_63d},
    "f33_cpkt_569_kst_signal_cross_at_close_252d_high_indicator": {"inputs": ["close"], "func": f33_cpkt_569_kst_signal_cross_at_close_252d_high_indicator},
    "f33_cpkt_570_kst_long_term_signal_cross_at_close_1260d_high_indicator": {"inputs": ["close"], "func": f33_cpkt_570_kst_long_term_signal_cross_at_close_1260d_high_indicator},
    "f33_cpkt_571_kama_10_vs_kama_63_cross_bearish_event": {"inputs": ["close"], "func": f33_cpkt_571_kama_10_vs_kama_63_cross_bearish_event},
    "f33_cpkt_572_days_since_kama_10_below_63_cross": {"inputs": ["close"], "func": f33_cpkt_572_days_since_kama_10_below_63_cross},
    "f33_cpkt_573_kama_10_above_63_indicator": {"inputs": ["close"], "func": f33_cpkt_573_kama_10_above_63_indicator},
    "f33_cpkt_574_hma_21_vs_hma_63_cross_bearish_event": {"inputs": ["close"], "func": f33_cpkt_574_hma_21_vs_hma_63_cross_bearish_event},
    "f33_cpkt_575_days_since_hma_21_below_63_cross": {"inputs": ["close"], "func": f33_cpkt_575_days_since_hma_21_below_63_cross},
    "f33_cpkt_576_hma_21_above_63_indicator": {"inputs": ["close"], "func": f33_cpkt_576_hma_21_above_63_indicator},
    "f33_cpkt_577_tema_21_vs_tema_63_cross_bearish_event": {"inputs": ["close"], "func": f33_cpkt_577_tema_21_vs_tema_63_cross_bearish_event},
    "f33_cpkt_578_days_since_tema_21_below_63_cross": {"inputs": ["close"], "func": f33_cpkt_578_days_since_tema_21_below_63_cross},
    "f33_cpkt_579_tema_21_above_63_indicator": {"inputs": ["close"], "func": f33_cpkt_579_tema_21_above_63_indicator},
    "f33_cpkt_580_kama_63_vs_kama_252_cross_bearish_event": {"inputs": ["close"], "func": f33_cpkt_580_kama_63_vs_kama_252_cross_bearish_event},
    "f33_cpkt_581_hma_63_vs_hma_252_cross_bearish_event": {"inputs": ["close"], "func": f33_cpkt_581_hma_63_vs_hma_252_cross_bearish_event},
    "f33_cpkt_582_kama_below_long_count_252d": {"inputs": ["close"], "func": f33_cpkt_582_kama_below_long_count_252d},
    "f33_cpkt_583_kama_10_minus_63_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_583_kama_10_minus_63_zscore_252d},
    "f33_cpkt_584_hma_21_minus_63_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_584_hma_21_minus_63_zscore_252d},
    "f33_cpkt_585_tema_21_minus_63_zscore_252d": {"inputs": ["close"], "func": f33_cpkt_585_tema_21_minus_63_zscore_252d},
    "f33_cpkt_586_trend_score_4cycle_coppock_fraction_positive": {"inputs": ["close"], "func": f33_cpkt_586_trend_score_4cycle_coppock_fraction_positive},
    "f33_cpkt_587_trend_score_3kst_fraction_positive": {"inputs": ["close"], "func": f33_cpkt_587_trend_score_3kst_fraction_positive},
    "f33_cpkt_588_trend_score_3smoothers_fraction_positive_ROC21": {"inputs": ["close"], "func": f33_cpkt_588_trend_score_3smoothers_fraction_positive_ROC21},
    "f33_cpkt_589_trend_score_long_indicator_fraction_positive": {"inputs": ["close"], "func": f33_cpkt_589_trend_score_long_indicator_fraction_positive},
    "f33_cpkt_590_trend_score_4cycle_coppock_fraction_rising": {"inputs": ["close"], "func": f33_cpkt_590_trend_score_4cycle_coppock_fraction_rising},
    "f33_cpkt_591_trend_score_3kst_fraction_rising": {"inputs": ["close"], "func": f33_cpkt_591_trend_score_3kst_fraction_rising},
    "f33_cpkt_592_trend_score_4cycle_coppock_value_drop_below_half_at_high_indicator": {"inputs": ["close"], "func": f33_cpkt_592_trend_score_4cycle_coppock_value_drop_below_half_at_high_indicator},
    "f33_cpkt_593_trend_score_zero_indicator_breadth_collapse_event": {"inputs": ["close"], "func": f33_cpkt_593_trend_score_zero_indicator_breadth_collapse_event},
    "f33_cpkt_594_trend_score_change_21d": {"inputs": ["close"], "func": f33_cpkt_594_trend_score_change_21d},
    "f33_cpkt_595_trend_score_change_63d": {"inputs": ["close"], "func": f33_cpkt_595_trend_score_change_63d},
    "f33_cpkt_596_trend_score_kst_change_21d": {"inputs": ["close"], "func": f33_cpkt_596_trend_score_kst_change_21d},
    "f33_cpkt_597_trend_score_long_indicator_change_21d": {"inputs": ["close"], "func": f33_cpkt_597_trend_score_long_indicator_change_21d},
    "f33_cpkt_598_trend_score_3kst_all_positive_persistence_63d": {"inputs": ["close"], "func": f33_cpkt_598_trend_score_3kst_all_positive_persistence_63d},
    "f33_cpkt_599_trend_score_4cycle_all_positive_persistence_63d": {"inputs": ["close"], "func": f33_cpkt_599_trend_score_4cycle_all_positive_persistence_63d},
    "f33_cpkt_600_trend_score_long_indicator_zero_persistence_indicator_at_high": {"inputs": ["close"], "func": f33_cpkt_600_trend_score_long_indicator_zero_persistence_indicator_at_high},
}
