"""27_macd_topping_dynamics d1 features 301-375 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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

def _slope_inner(w):
    valid = ~np.isnan(w)
    if valid.sum() < 2:
        return np.nan
    x = np.arange(len(w), dtype=float)
    if valid.all():
        wv = w
    else:
        x = x[valid]
        wv = w[valid]
    xm = x.mean()
    wm = wv.mean()
    num = ((x - xm) * (wv - wm)).sum()
    den = ((x - xm) ** 2).sum()
    return num / den if den != 0 else np.nan

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(_slope_inner, raw=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()

def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return (macd, sig, histo)

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

def _obv(close, volume):
    """On-Balance Volume."""
    sign = np.sign(close.diff().fillna(0))
    return (sign * volume).cumsum()

def _money_flow_cum(high, low, close, volume):
    """Cumulative money flow (MFM * volume) — Chaikin Money Flow building block."""
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    return (mfm.fillna(0) * volume).cumsum()

def _kama_simple(s, n=10, fast=2, slow=30):
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
        else:
            prev = prev + sca[i] * (x[i] - prev)
        out[i] = prev
    return pd.Series(out, index=s.index)

def _vwap_rolling(close, volume, n):
    pv = close * volume
    return _safe_div(pv.rolling(n, min_periods=max(n // 3, 2)).sum(), volume.rolling(n, min_periods=max(n // 3, 2)).sum())

def _keltner_upper(close, high, low, n=20, mult=2.0):
    mid = _ema(close, n)
    return mid + mult * _atr(high, low, close, n)

def _donchian_upper(high, n=20):
    return high.rolling(n, min_periods=max(n // 3, 2)).max()

def _bb_upper(close, n=20, k=2.0):
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return m + k * sd

def _bb_lower(close, n=20, k=2.0):
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return m - k * sd

def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(up, dn)
    return 100.0 - 100.0 / (1.0 + rs)

def _williams_r(high, low, close, n=14):
    hi = high.rolling(n, min_periods=max(n // 3, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return -100.0 * _safe_div(hi - close, hi - lo)

def _stoch_k(high, low, close, n=14):
    hi = high.rolling(n, min_periods=max(n // 3, 2)).max()
    lo = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - lo, hi - lo)

def _pivot_high_mask(high, left=5, right=5):
    """True at bar t when high[t-right] is a local max over [t-right-left, t-right+right] window.
    PIT-safe: uses only data through bar t. Marks pivots with a 'right' bar lag."""
    n = left + right + 1
    rmax = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return (high.shift(right) == rmax) & high.shift(right).notna()

def _chaikin_osc(high, low, close, volume):
    """Chaikin Oscillator: EMA3(ADL) - EMA10(ADL)."""
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    adl = (mfm.fillna(0) * volume).cumsum()
    return _ema(adl, 3) - _ema(adl, 10)

def _vol_avg_50(volume):
    return volume.rolling(50, min_periods=10).mean()

def _bbands_in_keltner_mask(close, high, low, n=20):
    """TTM Squeeze: BB(20,2) inside Keltner(20,1.5)."""
    bbu = _bb_upper(close, n, 2.0)
    bbl = _bb_lower(close, n, 2.0)
    mid = _ema(close, n)
    katr = _atr(high, low, close, n)
    ku = mid + 1.5 * katr
    kl = mid - 1.5 * katr
    return (bbu < ku) & (bbl > kl)

def f27_mcdt_301_macd_bearish_cross_with_above_avg_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if bearish MACD/signal cross AND volume > 1.3x prior 50d avg — vol-confirmed bearish trigger."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = _vol_avg_50(volume).shift(1)
    return (cross & (volume > 1.3 * va)).astype(float).where(d.notna() & va.notna(), np.nan).diff()

def f27_mcdt_302_macd_bearish_cross_high_vol_count_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of vol-confirmed bearish MACD/signal crosses in past 252 — annual confirmed-cross count."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = _vol_avg_50(volume).shift(1)
    ev = (cross & (volume > 1.3 * va)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan).diff()

def f27_mcdt_303_macd_bearish_cross_high_vol_recency_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most-recent vol-confirmed bearish MACD/signal cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = _vol_avg_50(volume).shift(1)
    ev = cross & (volume > 1.3 * va)
    return _bars_since_true(ev).diff()

def f27_mcdt_304_macd_div_with_volume_confirmation_63_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish MACD div (63d) AND volume on down days > volume on up days in trailing 21 — vol-confirmed div."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = p_new & (m < prior_max)
    sign = np.sign(close.diff())
    vol_up = volume.where(sign > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    vol_dn = volume.where(sign < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return (div & (vol_dn > vol_up)).astype(float).where(m.notna() & vol_up.notna(), np.nan).diff()

def f27_mcdt_305_macd_div_volume_confirmed_count_252_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of vol-confirmed bearish MACD divergences."""
    m, _, _ = _macd(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = p_new & (m < prior_max)
    sign = np.sign(close.diff())
    vol_up = volume.where(sign > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    vol_dn = volume.where(sign < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    ev = (div & (vol_dn > vol_up)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan).diff()

def f27_mcdt_306_money_flow_macd_12_26_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD(12,26) on cumulative money flow — order-flow trend signal."""
    mf = _money_flow_cum(high, low, close, volume)
    return (_ema(mf, 12) - _ema(mf, 26)).diff()

def f27_mcdt_307_money_flow_macd_above_zero_state_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if money-flow MACD > 0 — flow-bullish regime."""
    mf = _money_flow_cum(high, low, close, volume)
    m = _ema(mf, 12) - _ema(mf, 26)
    return (m > 0).astype(float).where(m.notna(), np.nan).diff()

def f27_mcdt_308_money_flow_macd_signal_cross_down_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if money-flow MACD crossed below its 9-EMA signal — bearish flow-MACD cross."""
    mf = _money_flow_cum(high, low, close, volume)
    m = _ema(mf, 12) - _ema(mf, 26)
    s = _ema(m, 9)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan).diff()

def f27_mcdt_309_obv_macd_12_26_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD(12,26) on OBV series — volume-flow trend signal."""
    obv = _obv(close, volume)
    return (_ema(obv, 12) - _ema(obv, 26)).diff()

def f27_mcdt_310_obv_macd_bearish_cross_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if OBV-MACD crossed below its 9-EMA signal — OBV-MACD bearish cross."""
    obv = _obv(close, volume)
    m = _ema(obv, 12) - _ema(obv, 26)
    s = _ema(m, 9)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan).diff()

def f27_mcdt_311_obv_macd_div_vs_price_63_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish divergence: price new 63d high but OBV-MACD below prior 63d max."""
    obv = _obv(close, volume)
    m = _ema(obv, 12) - _ema(obv, 26)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & m_below).astype(float).where(m.notna(), np.nan).diff()

def f27_mcdt_312_macd_signal_cross_with_volume_climax_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if bearish MACD/signal cross on a day with volume > 2x 50d avg — climax-vol bearish cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    va = _vol_avg_50(volume).shift(1)
    return (cross & (volume > 2.0 * va)).astype(float).where(d.notna() & va.notna(), np.nan).diff()

def f27_mcdt_313_macd_adaptive_signal_kama_period_d1(close: pd.Series) -> pd.Series:
    """KAMA-period adaptive signal line on MACD: signal = KAMA(MACD, 9)."""
    m, _, _ = _macd(close)
    return _kama_simple(m, n=9).diff()

def f27_mcdt_314_macd_adaptive_signal_above_macd_state_d1(close: pd.Series) -> pd.Series:
    """1 if KAMA-adaptive signal > MACD — bearish flipped state under adaptive signal."""
    m, _, _ = _macd(close)
    s = _kama_simple(m, n=9)
    return (s > m).astype(float).where(m.notna() & s.notna(), np.nan).diff()

def f27_mcdt_315_macd_signal_vol_adaptive_period_d1(close: pd.Series) -> pd.Series:
    """Signal line where period scales inversely with realized vol: in high vol use 5-EMA, in low
    vol use 13-EMA; output MACD - adaptive-signal."""
    m, _, _ = _macd(close)
    s5 = _ema(m, 5)
    s13 = _ema(m, 13)
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    z = _rolling_zscore(rv, YDAYS, min_periods=QDAYS)
    w = (z.clip(-2.0, 2.0) + 2.0) / 4.0
    sig = w * s5 + (1.0 - w) * s13
    return (m - sig).diff()

def f27_mcdt_316_macd_signal_cycle_adaptive_period_d1(close: pd.Series) -> pd.Series:
    """Signal period uses dominant-cycle estimate via 63d auto-correlation: short cycle -> faster signal.
    Output MACD - signal (signal-period proxy = 5 if autocorr>0.5 else 13)."""
    m, _, _ = _macd(close)
    ac = m.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(WDAYS))
    fast = _ema(m, 5)
    slow = _ema(m, 13)
    sig = fast.where(ac > 0.5, slow)
    return (m - sig).diff()

def f27_mcdt_317_macd_adaptive_threshold_zero_line_d1(close: pd.Series) -> pd.Series:
    """Adaptive zero-line: replace zero with 252d EMA of MACD (drift). Output: MACD - drift."""
    m, _, _ = _macd(close)
    drift = m.ewm(span=YDAYS, adjust=False, min_periods=QDAYS).mean()
    return (m - drift).diff()

def f27_mcdt_318_macd_adaptive_above_drift_threshold_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > its 252d EMA (adaptive drift threshold)."""
    m, _, _ = _macd(close)
    drift = m.ewm(span=YDAYS, adjust=False, min_periods=QDAYS).mean()
    return (m > drift).astype(float).where(m.notna() & drift.notna(), np.nan).diff()

def f27_mcdt_319_macd_adaptive_bearish_cross_indicator_d1(close: pd.Series) -> pd.Series:
    """1 if MACD crossed below its KAMA-adaptive signal line — adaptive bearish cross."""
    m, _, _ = _macd(close)
    s = _kama_simple(m, n=9)
    d = m - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan).diff()

def f27_mcdt_320_macd_adaptive_signal_cross_count_252_d1(close: pd.Series) -> pd.Series:
    """Annual count of bearish crosses against KAMA-adaptive signal — adaptive cross frequency."""
    m, _, _ = _macd(close)
    s = _kama_simple(m, n=9)
    d = m - s
    ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan).diff()

def f27_mcdt_321_macd_at_sma50_cross_above_value_d1(close: pd.Series) -> pd.Series:
    """MACD value at the bar when close crossed above SMA50. Forward-fills until next cross."""
    m, _, _ = _macd(close)
    sma = close.rolling(50, min_periods=20).mean()
    cross = (close.shift(1) <= sma.shift(1)) & (close > sma)
    return m.where(cross, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_322_macd_at_sma200_cross_above_value_d1(close: pd.Series) -> pd.Series:
    """MACD value at bar when close crossed above SMA200 — golden-cross-proxy MACD."""
    m, _, _ = _macd(close)
    sma = close.rolling(200, min_periods=50).mean()
    cross = (close.shift(1) <= sma.shift(1)) & (close > sma)
    return m.where(cross, np.nan).ffill(limit=DDAYS_2Y).diff()

def f27_mcdt_323_macd_at_252h_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at bars where high hits its 252d max — MACD at new annual highs."""
    m, _, _ = _macd(close)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return m.where(at_max, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_324_macd_at_first_252h_in_504d_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at the FIRST new 252d high in a 504d window (first new high after long drought)."""
    m, _, _ = _macd(close)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(at_252h.shift(1).fillna(False))
    first_after_drought = at_252h & (bs >= YDAYS)
    return m.where(first_after_drought, np.nan).ffill(limit=DDAYS_2Y).diff()

def f27_mcdt_325_macd_at_first_close_below_sma50_post_peak_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at first close below SMA50 after a 252d high (within prior 63d) — initial breakdown MACD."""
    m, _, _ = _macd(close)
    sma = close.rolling(50, min_periods=20).mean()
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_high = _bars_since_true(at_252h)
    below = close < sma
    first_below = below & ~below.shift(1).fillna(False) & (bs_high <= QDAYS)
    return m.where(first_below, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_326_macd_at_first_close_below_sma200_post_peak_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at first close below SMA200 after a 252d high (within prior 126d) — major breakdown MACD."""
    m, _, _ = _macd(close)
    sma = close.rolling(200, min_periods=50).mean()
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_high = _bars_since_true(at_252h)
    below = close < sma
    first_below = below & ~below.shift(1).fillna(False) & (bs_high <= 126)
    return m.where(first_below, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_327_macd_at_volume_climax_event_value_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD value at volume-climax bars (volume > 3x 50d avg)."""
    m, _, _ = _macd(close)
    va = _vol_avg_50(volume).shift(1)
    climax = volume > 3.0 * va
    return m.where(climax, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_328_macd_at_gap_up_event_value_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at gap-up events (open > prior-close * 1.02)."""
    m, _, _ = _macd(close)
    pc = close.shift(1)
    gap = open > pc * 1.02
    return m.where(gap, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_329_macd_at_gap_down_event_value_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at gap-down events (open < prior-close * 0.98)."""
    m, _, _ = _macd(close)
    pc = close.shift(1)
    gap = open < pc * 0.98
    return m.where(gap, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_330_macd_during_atr_expanding_regime_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND 21d ATR expanding (above its 63d mean by >20%)."""
    m, _, _ = _macd(close)
    atr21 = _atr(high, low, close, MDAYS)
    atr63 = _atr(high, low, close, QDAYS)
    expanding = atr21 > 1.2 * atr63
    return ((m > 0) & expanding).astype(float).where(m.notna() & atr21.notna(), np.nan).diff()

def f27_mcdt_331_macd_during_atr_contracting_regime_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND 21d ATR contracting (below its 63d mean by >20%)."""
    m, _, _ = _macd(close)
    atr21 = _atr(high, low, close, MDAYS)
    atr63 = _atr(high, low, close, QDAYS)
    contracting = atr21 < 0.8 * atr63
    return ((m > 0) & contracting).astype(float).where(m.notna() & atr21.notna(), np.nan).diff()

def f27_mcdt_332_macd_in_high_vol_regime_above_zero_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND realized vol (21d std of pct change) above its 252d q70 — high-vol bullish state."""
    m, _, _ = _macd(close)
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    q70 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.7)
    return ((m > 0) & (rv > q70)).astype(float).where(m.notna() & q70.notna(), np.nan).diff()

def f27_mcdt_333_macd_in_low_vol_regime_above_zero_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND realized vol below its 252d q30 — low-vol bullish state."""
    m, _, _ = _macd(close)
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    q30 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.3)
    return ((m > 0) & (rv < q30)).astype(float).where(m.notna() & q30.notna(), np.nan).diff()

def f27_mcdt_334_macd_in_uptrend_regime_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND close > SMA200 AND SMA50 > SMA200 — confirmed-uptrend MACD-positive state."""
    m, _, _ = _macd(close)
    sma50 = close.rolling(50, min_periods=20).mean()
    sma200 = close.rolling(200, min_periods=50).mean()
    up = (close > sma200) & (sma50 > sma200)
    return ((m > 0) & up).astype(float).where(m.notna() & sma200.notna(), np.nan).diff()

def f27_mcdt_335_macd_in_downtrend_regime_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > 0 AND close < SMA200 AND SMA50 < SMA200 — bullish MACD in downtrend regime (paradox)."""
    m, _, _ = _macd(close)
    sma50 = close.rolling(50, min_periods=20).mean()
    sma200 = close.rolling(200, min_periods=50).mean()
    dn = (close < sma200) & (sma50 < sma200)
    return ((m > 0) & dn).astype(float).where(m.notna() & sma200.notna(), np.nan).diff()

def f27_mcdt_336_macd_at_atr_extreme_high_event_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at bars where 21d ATR hits its 252d max — MACD at vol-extreme bars."""
    m, _, _ = _macd(close)
    atr21 = _atr(high, low, close, MDAYS)
    at_max = atr21 == atr21.rolling(YDAYS, min_periods=QDAYS).max()
    return m.where(at_max, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_337_macd_at_widerange_red_bar_event_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at wide-range red bars: (high-low) > 2x 21d ATR AND close < open (proxied close<prior_close)."""
    m, _, _ = _macd(close)
    atr21 = _atr(high, low, close, MDAYS)
    wr_red = (high - low > 2.0 * atr21) & (close < close.shift(1))
    return m.where(wr_red, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_338_macd_at_distribution_day_event_value_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD value at distribution days: close down > 0.2% AND volume > prior-day volume."""
    m, _, _ = _macd(close)
    pc = close.shift(1)
    dist = (close < pc * 0.998) & (volume > volume.shift(1))
    return m.where(dist, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_339_macd_at_consolidation_break_event_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD value at consolidation-break events: range/ATR drops below 0.5 then close breaks 21d high."""
    m, _, _ = _macd(close)
    atr21 = _atr(high, low, close, MDAYS)
    rng21 = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    cons = rng21 / (atr21 * MDAYS) < 0.5
    cons_recent = cons.rolling(WDAYS, min_periods=1).sum() > 0
    brk = close > high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    ev = cons_recent.shift(1).fillna(False) & brk
    return m.where(ev, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_340_macd_post_breakdown_recovery_failure_count_63_d1(close: pd.Series) -> pd.Series:
    """Count of recovery failures in past 63d: MACD<0 then crossed above 0 then crossed below within 21 bars."""
    m, _, _ = _macd(close)
    up = ((m.shift(1) <= 0) & (m > 0)).astype(float)
    dn = ((m.shift(1) >= 0) & (m < 0)).astype(float)
    up_21_ago = up.shift(MDAYS)
    dn_in_21 = dn.rolling(MDAYS, min_periods=1).sum()
    fail = (up_21_ago > 0) & (dn_in_21 > 0)
    return fail.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(m.notna(), np.nan).diff()

def f27_mcdt_341_macd_pct_rank_within_504d_d1(close: pd.Series) -> pd.Series:
    """504d (2y) percentile rank of MACD — multi-year distribution-position."""
    m, _, _ = _macd(close)
    return m.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank_window, raw=True).diff()

def f27_mcdt_342_macd_pct_rank_within_1260d_d1(close: pd.Series) -> pd.Series:
    """1260d (5y) percentile rank of MACD — full-cycle distribution-position."""
    m, _, _ = _macd(close)
    return m.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_pct_rank_window, raw=True).diff()

def f27_mcdt_343_macd_above_own_q90_504_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > its trailing 504d 90th-pct — multi-year self-relative OB."""
    m, _, _ = _macd(close)
    q = m.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_344_macd_above_own_q99_504_state_d1(close: pd.Series) -> pd.Series:
    """1 if MACD > its trailing 504d 99th-pct — multi-year self-relative extreme OB."""
    m, _, _ = _macd(close)
    q = m.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.99)
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_345_macd_dwell_above_own_q90_504_63_d1(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with MACD above its trailing 504d q90 — quarterly extreme-dwell."""
    m, _, _ = _macd(close)
    q = m.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return (m > q).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(m.notna(), np.nan).diff()

def f27_mcdt_346_macd_within_vol_bucketed_history_q90_d1(close: pd.Series) -> pd.Series:
    """Self-relative rank in history filtered to similar-vol regime: MACD over bars where 21d vol is within 0.25 sd of current."""
    m, _, _ = _macd(close)
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    rv_z = _rolling_zscore(rv, YDAYS, min_periods=QDAYS)
    bucket = pd.cut(rv_z, bins=[-99, -0.5, 0.5, 99], labels=[0, 1, 2]).astype(float)
    df = pd.concat([m.rename('m'), bucket.rename('b')], axis=1)
    q = df.groupby('b')['m'].transform(lambda x: x.expanding(min_periods=YDAYS).quantile(0.9))
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_347_macd_within_trend_bucketed_history_q90_d1(close: pd.Series) -> pd.Series:
    """Self-relative rank in same trend-regime: bucket by sign of 50d slope of close."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(close, 50)
    bucket = np.sign(sl).fillna(0).astype(int).astype(float)
    df = pd.concat([m.rename('m'), bucket.rename('b')], axis=1)
    q = df.groupby('b')['m'].transform(lambda x: x.expanding(min_periods=YDAYS).quantile(0.9))
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_348_macd_within_price_bucketed_history_q90_d1(close: pd.Series) -> pd.Series:
    """Self-relative rank in same price-level bucket: bucket by quartile of trailing 252d close."""
    m, _, _ = _macd(close)
    q25 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q50 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    q75 = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    bucket = pd.Series(0.0, index=close.index)
    bucket = bucket.where(close < q25, 1.0)
    bucket = bucket.where(close < q50, 2.0)
    bucket = bucket.where(close < q75, 3.0)
    df = pd.concat([m.rename('m'), bucket.rename('b')], axis=1)
    q = df.groupby('b')['m'].transform(lambda x: x.expanding(min_periods=YDAYS).quantile(0.9))
    return (m > q).astype(float).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_349_macd_distance_from_own_504d_median_d1(close: pd.Series) -> pd.Series:
    """MACD - its trailing 504d median — multi-year centered deviation."""
    m, _, _ = _macd(close)
    return (m - m.rolling(DDAYS_2Y, min_periods=YDAYS).median()).diff()

def f27_mcdt_350_macd_skew_within_own_252d_d1(close: pd.Series) -> pd.Series:
    """Skewness of MACD over 252d — annual distribution asymmetry."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).skew().diff()

def f27_mcdt_351_macd_kurt_within_own_252d_d1(close: pd.Series) -> pd.Series:
    """Excess kurtosis of MACD over 252d — annual tail-behavior."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).kurt().diff()

def f27_mcdt_352_macd_distribution_shift_zscore_252_d1(close: pd.Series) -> pd.Series:
    """Distribution-shift z-score: (mean of MACD over recent 63d - mean over prior 189d) / std over 252d."""
    m, _, _ = _macd(close)
    recent = m.rolling(QDAYS, min_periods=MDAYS).mean()
    prior_full = m.rolling(YDAYS, min_periods=QDAYS).mean()
    prior = m.shift(QDAYS).rolling(189, min_periods=QDAYS).mean()
    sd252 = m.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(recent - prior, sd252).diff()

def f27_mcdt_353_macd_first_breach_of_own_q99_504_age_d1(close: pd.Series) -> pd.Series:
    """Age (bars since) of the FIRST breach of own 504d q99 within trailing 504d window."""
    m, _, _ = _macd(close)
    q = m.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.99)
    breach = m > q
    return _bars_since_true(breach).diff()

def f27_mcdt_354_macd_pct_rank_decay_velocity_63_d1(close: pd.Series) -> pd.Series:
    """5d slope of 252d pct-rank of MACD — recency of distribution-rank decay."""
    m, _, _ = _macd(close)
    pr = m.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    return _rolling_slope(pr, WDAYS).diff()

def f27_mcdt_355_macd_consecutive_above_own_q90_504_streak_d1(close: pd.Series) -> pd.Series:
    """Current consecutive streak of bars where MACD > its 504d q90."""
    m, _, _ = _macd(close)
    q = m.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return _streak_true(m > q).where(m.notna() & q.notna(), np.nan).diff()

def f27_mcdt_356_elder_triple_screen_macd_consensus_d1(close: pd.Series) -> pd.Series:
    """Elder triple-screen: weekly MACD > 0 AND daily MACD < 0 (sell-setup state, 1/0)."""
    m_d, _, _ = _macd(close, 12, 26, 9)
    w = close.rolling(WDAYS, min_periods=WDAYS).mean()
    m_w = _ema(w, 12) - _ema(w, 26)
    return ((m_w > 0) & (m_d < 0)).astype(float).where(m_d.notna() & m_w.notna(), np.nan).diff()

def f27_mcdt_357_ttm_squeeze_release_macd_bearish_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM-Squeeze release with bearish MACD: was-in-squeeze last bar AND not-in-squeeze this bar AND
    MACD turning down (5d slope < 0)."""
    sq = _bbands_in_keltner_mask(close, high, low, 20)
    release = sq.shift(1).fillna(False) & ~sq.fillna(False)
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, WDAYS)
    return (release & (sl < 0)).astype(float).where(m.notna() & sl.notna(), np.nan).diff()

def f27_mcdt_358_ttm_squeeze_macd_failure_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Squeeze release fails: was-in-squeeze in 21d ago AND now MACD<0 AND close below 21d-mean — failed-breakout."""
    sq = _bbands_in_keltner_mask(close, high, low, 20)
    sq_recent = sq.shift(MDAYS).fillna(False)
    m, _, _ = _macd(close)
    sma21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return (sq_recent & (m < 0) & (close < sma21)).astype(float).where(m.notna(), np.nan).diff()

def f27_mcdt_359_bbands_macd_filter_bearish_d1(close: pd.Series) -> pd.Series:
    """1 if close > BB(20,2) upper AND MACD < signal — overbought-with-momentum-fail filter."""
    m, s, _ = _macd(close)
    bbu = _bb_upper(close, 20, 2.0)
    return ((close > bbu) & (m < s)).astype(float).where(m.notna() & bbu.notna(), np.nan).diff()

def f27_mcdt_360_macd_with_vwap_filter_bearish_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close < 20d VWAP AND bearish MACD/signal cross fired today — VWAP-filtered bearish trigger."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    vw = _vwap_rolling(close, volume, 20)
    return (cross & (close < vw)).astype(float).where(d.notna() & vw.notna(), np.nan).diff()

def f27_mcdt_361_macd_pivot_filter_bearish_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if bearish MACD/signal cross AND close near a recent pivot high (within 21d)."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    piv = _pivot_high_mask(high, left=5, right=5)
    piv_recent = piv.rolling(MDAYS, min_periods=1).sum() > 0
    return (cross & piv_recent).astype(float).where(d.notna(), np.nan).diff()

def f27_mcdt_362_macd_with_keltner_filter_bearish_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close > Keltner upper (20,2) AND bearish MACD/signal cross — Keltner-OB filtered cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    ku = _keltner_upper(close, high, low, 20, 2.0)
    return (cross & (close > ku)).astype(float).where(d.notna() & ku.notna(), np.nan).diff()

def f27_mcdt_363_macd_with_donchian_filter_bearish_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close at 20d Donchian upper AND bearish MACD/signal cross — Donchian-top filter."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    du = _donchian_upper(high, 20)
    at_top = close >= du * 0.995
    return (cross & at_top).astype(float).where(d.notna() & du.notna(), np.nan).diff()

def f27_mcdt_364_dorsey_macd_relative_strength_vs_self_d1(close: pd.Series) -> pd.Series:
    """Dorsey relative-strength: MACD now / 252d rolling-mean of MACD — own-history-relative momentum."""
    m, _, _ = _macd(close)
    return _safe_div(m, m.rolling(YDAYS, min_periods=QDAYS).mean().abs()).diff()

def f27_mcdt_365_worden_macd_4_period_consensus_d1(close: pd.Series) -> pd.Series:
    """Worden 4-period MACD consensus: count of MACD configs (4-8, 8-16, 16-32, 32-64) with positive line."""
    a = _ema(close, 4) - _ema(close, 8)
    b = _ema(close, 8) - _ema(close, 16)
    c = _ema(close, 16) - _ema(close, 32)
    d = _ema(close, 32) - _ema(close, 64)
    return ((a > 0).astype(float).fillna(0) + (b > 0).astype(float).fillna(0) + (c > 0).astype(float).fillna(0) + (d > 0).astype(float).fillna(0)).where(close.notna(), np.nan).diff()

def f27_mcdt_366_weinstein_stage_4_macd_confirmation_d1(close: pd.Series) -> pd.Series:
    """1 if MACD < 0 AND close < SMA30 AND SMA30 declining (5d slope < 0) — Weinstein Stage 4."""
    m, _, _ = _macd(close)
    sma30 = close.rolling(30, min_periods=10).mean()
    sl = _rolling_slope(sma30, WDAYS)
    return ((m < 0) & (close < sma30) & (sl < 0)).astype(float).where(m.notna() & sl.notna(), np.nan).diff()

def f27_mcdt_367_cansil_macd_failure_signal_d1(close: pd.Series) -> pd.Series:
    """CANSLIM-style MACD-failure: bullish MACD/signal cross fired and price failed to make a new 21d high
    within next 5 bars (look back: bullish cross 5 bars ago AND high today < 21d high 5 days ago)."""
    m, s, _ = _macd(close)
    d = m - s
    bu = ((d.shift(1) <= 0) & (d > 0)).astype(float)
    bu_5_ago = bu.shift(WDAYS).fillna(0)
    high21_5_ago = close.shift(WDAYS).rolling(MDAYS, min_periods=WDAYS).max()
    fail = (bu_5_ago > 0) & (close < high21_5_ago)
    return fail.astype(float).where(d.notna(), np.nan).diff()

def f27_mcdt_368_macd_with_obv_filter_bearish_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if OBV declining (21d slope < 0) AND classical MACD bearish cross — OBV-confirmed bearish MACD."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    obv = _obv(close, volume)
    obv_sl = _rolling_slope(obv, MDAYS)
    return (cross & (obv_sl < 0)).astype(float).where(d.notna() & obv_sl.notna(), np.nan).diff()

def f27_mcdt_369_macd_with_chaikin_filter_bearish_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Chaikin Oscillator < 0 AND classical MACD bearish cross — Chaikin-confirmed bearish MACD."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    co = _chaikin_osc(high, low, close, volume)
    return (cross & (co < 0)).astype(float).where(d.notna() & co.notna(), np.nan).diff()

def f27_mcdt_370_macd_with_atr_expansion_filter_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d ATR expanding (above its 63d mean) AND classical bearish MACD cross — ATR-expansion bearish."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    atr21 = _atr(high, low, close, MDAYS)
    atr63 = _atr(high, low, close, QDAYS)
    return (cross & (atr21 > atr63)).astype(float).where(d.notna() & atr21.notna(), np.nan).diff()

def f27_mcdt_371_macd_with_williams_r_filter_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R > -20 (OB) AND bearish MACD/signal cross — Williams-OB filtered cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    wr = _williams_r(high, low, close, 14)
    return (cross & (wr > -20.0)).astype(float).where(d.notna() & wr.notna(), np.nan).diff()

def f27_mcdt_372_macd_with_rsi_filter_bearish_d1(close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 70 AND bearish MACD/signal cross — RSI-OB filtered cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    rsi = _rsi(close, 14)
    return (cross & (rsi > 70.0)).astype(float).where(d.notna() & rsi.notna(), np.nan).diff()

def f27_mcdt_373_macd_with_stoch_filter_bearish_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch %K > 80 AND bearish MACD/signal cross — Stoch-OB filtered cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0)
    k = _stoch_k(high, low, close, 14)
    return (cross & (k > 80.0)).astype(float).where(d.notna() & k.notna(), np.nan).diff()

def f27_mcdt_374_macd_at_first_signal_cross_below_zero_value_d1(close: pd.Series) -> pd.Series:
    """MACD value at first bearish MACD/signal cross that occurs while MACD < 0 — confirming bearish state cross."""
    m, s, _ = _macd(close)
    d = m - s
    cross = (d.shift(1) > 0) & (d <= 0) & (m < 0)
    return m.where(cross, np.nan).ffill(limit=YDAYS).diff()

def f27_mcdt_375_macd_failure_after_long_above_zero_252_d1(close: pd.Series) -> pd.Series:
    """1 if MACD was above zero for >= 126 of past 252 bars AND bearish MACD/signal cross fired in past 21
    — failure-of-long-bull MACD."""
    m, s, _ = _macd(close)
    long_above = (m > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() >= 126
    d = m - s
    cross = ((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return (long_above & cross).astype(float).where(m.notna(), np.nan).diff()
MACD_TOPPING_DYNAMICS_D1_REGISTRY_301_375 = {'f27_mcdt_301_macd_bearish_cross_with_above_avg_volume_indicator_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_301_macd_bearish_cross_with_above_avg_volume_indicator_d1}, 'f27_mcdt_302_macd_bearish_cross_high_vol_count_252_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_302_macd_bearish_cross_high_vol_count_252_d1}, 'f27_mcdt_303_macd_bearish_cross_high_vol_recency_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_303_macd_bearish_cross_high_vol_recency_d1}, 'f27_mcdt_304_macd_div_with_volume_confirmation_63_d1': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_304_macd_div_with_volume_confirmation_63_d1}, 'f27_mcdt_305_macd_div_volume_confirmed_count_252_d1': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_305_macd_div_volume_confirmed_count_252_d1}, 'f27_mcdt_306_money_flow_macd_12_26_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_306_money_flow_macd_12_26_d1}, 'f27_mcdt_307_money_flow_macd_above_zero_state_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_307_money_flow_macd_above_zero_state_d1}, 'f27_mcdt_308_money_flow_macd_signal_cross_down_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_308_money_flow_macd_signal_cross_down_d1}, 'f27_mcdt_309_obv_macd_12_26_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_309_obv_macd_12_26_d1}, 'f27_mcdt_310_obv_macd_bearish_cross_indicator_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_310_obv_macd_bearish_cross_indicator_d1}, 'f27_mcdt_311_obv_macd_div_vs_price_63_d1': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_311_obv_macd_div_vs_price_63_d1}, 'f27_mcdt_312_macd_signal_cross_with_volume_climax_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_312_macd_signal_cross_with_volume_climax_d1}, 'f27_mcdt_313_macd_adaptive_signal_kama_period_d1': {'inputs': ['close'], 'func': f27_mcdt_313_macd_adaptive_signal_kama_period_d1}, 'f27_mcdt_314_macd_adaptive_signal_above_macd_state_d1': {'inputs': ['close'], 'func': f27_mcdt_314_macd_adaptive_signal_above_macd_state_d1}, 'f27_mcdt_315_macd_signal_vol_adaptive_period_d1': {'inputs': ['close'], 'func': f27_mcdt_315_macd_signal_vol_adaptive_period_d1}, 'f27_mcdt_316_macd_signal_cycle_adaptive_period_d1': {'inputs': ['close'], 'func': f27_mcdt_316_macd_signal_cycle_adaptive_period_d1}, 'f27_mcdt_317_macd_adaptive_threshold_zero_line_d1': {'inputs': ['close'], 'func': f27_mcdt_317_macd_adaptive_threshold_zero_line_d1}, 'f27_mcdt_318_macd_adaptive_above_drift_threshold_state_d1': {'inputs': ['close'], 'func': f27_mcdt_318_macd_adaptive_above_drift_threshold_state_d1}, 'f27_mcdt_319_macd_adaptive_bearish_cross_indicator_d1': {'inputs': ['close'], 'func': f27_mcdt_319_macd_adaptive_bearish_cross_indicator_d1}, 'f27_mcdt_320_macd_adaptive_signal_cross_count_252_d1': {'inputs': ['close'], 'func': f27_mcdt_320_macd_adaptive_signal_cross_count_252_d1}, 'f27_mcdt_321_macd_at_sma50_cross_above_value_d1': {'inputs': ['close'], 'func': f27_mcdt_321_macd_at_sma50_cross_above_value_d1}, 'f27_mcdt_322_macd_at_sma200_cross_above_value_d1': {'inputs': ['close'], 'func': f27_mcdt_322_macd_at_sma200_cross_above_value_d1}, 'f27_mcdt_323_macd_at_252h_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_323_macd_at_252h_value_d1}, 'f27_mcdt_324_macd_at_first_252h_in_504d_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_324_macd_at_first_252h_in_504d_value_d1}, 'f27_mcdt_325_macd_at_first_close_below_sma50_post_peak_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_325_macd_at_first_close_below_sma50_post_peak_value_d1}, 'f27_mcdt_326_macd_at_first_close_below_sma200_post_peak_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_326_macd_at_first_close_below_sma200_post_peak_value_d1}, 'f27_mcdt_327_macd_at_volume_climax_event_value_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_327_macd_at_volume_climax_event_value_d1}, 'f27_mcdt_328_macd_at_gap_up_event_value_d1': {'inputs': ['open', 'close'], 'func': f27_mcdt_328_macd_at_gap_up_event_value_d1}, 'f27_mcdt_329_macd_at_gap_down_event_value_d1': {'inputs': ['open', 'close'], 'func': f27_mcdt_329_macd_at_gap_down_event_value_d1}, 'f27_mcdt_330_macd_during_atr_expanding_regime_state_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_330_macd_during_atr_expanding_regime_state_d1}, 'f27_mcdt_331_macd_during_atr_contracting_regime_state_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_331_macd_during_atr_contracting_regime_state_d1}, 'f27_mcdt_332_macd_in_high_vol_regime_above_zero_state_d1': {'inputs': ['close'], 'func': f27_mcdt_332_macd_in_high_vol_regime_above_zero_state_d1}, 'f27_mcdt_333_macd_in_low_vol_regime_above_zero_state_d1': {'inputs': ['close'], 'func': f27_mcdt_333_macd_in_low_vol_regime_above_zero_state_d1}, 'f27_mcdt_334_macd_in_uptrend_regime_state_d1': {'inputs': ['close'], 'func': f27_mcdt_334_macd_in_uptrend_regime_state_d1}, 'f27_mcdt_335_macd_in_downtrend_regime_state_d1': {'inputs': ['close'], 'func': f27_mcdt_335_macd_in_downtrend_regime_state_d1}, 'f27_mcdt_336_macd_at_atr_extreme_high_event_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_336_macd_at_atr_extreme_high_event_value_d1}, 'f27_mcdt_337_macd_at_widerange_red_bar_event_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_337_macd_at_widerange_red_bar_event_value_d1}, 'f27_mcdt_338_macd_at_distribution_day_event_value_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_338_macd_at_distribution_day_event_value_d1}, 'f27_mcdt_339_macd_at_consolidation_break_event_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_339_macd_at_consolidation_break_event_value_d1}, 'f27_mcdt_340_macd_post_breakdown_recovery_failure_count_63_d1': {'inputs': ['close'], 'func': f27_mcdt_340_macd_post_breakdown_recovery_failure_count_63_d1}, 'f27_mcdt_341_macd_pct_rank_within_504d_d1': {'inputs': ['close'], 'func': f27_mcdt_341_macd_pct_rank_within_504d_d1}, 'f27_mcdt_342_macd_pct_rank_within_1260d_d1': {'inputs': ['close'], 'func': f27_mcdt_342_macd_pct_rank_within_1260d_d1}, 'f27_mcdt_343_macd_above_own_q90_504_state_d1': {'inputs': ['close'], 'func': f27_mcdt_343_macd_above_own_q90_504_state_d1}, 'f27_mcdt_344_macd_above_own_q99_504_state_d1': {'inputs': ['close'], 'func': f27_mcdt_344_macd_above_own_q99_504_state_d1}, 'f27_mcdt_345_macd_dwell_above_own_q90_504_63_d1': {'inputs': ['close'], 'func': f27_mcdt_345_macd_dwell_above_own_q90_504_63_d1}, 'f27_mcdt_346_macd_within_vol_bucketed_history_q90_d1': {'inputs': ['close'], 'func': f27_mcdt_346_macd_within_vol_bucketed_history_q90_d1}, 'f27_mcdt_347_macd_within_trend_bucketed_history_q90_d1': {'inputs': ['close'], 'func': f27_mcdt_347_macd_within_trend_bucketed_history_q90_d1}, 'f27_mcdt_348_macd_within_price_bucketed_history_q90_d1': {'inputs': ['close'], 'func': f27_mcdt_348_macd_within_price_bucketed_history_q90_d1}, 'f27_mcdt_349_macd_distance_from_own_504d_median_d1': {'inputs': ['close'], 'func': f27_mcdt_349_macd_distance_from_own_504d_median_d1}, 'f27_mcdt_350_macd_skew_within_own_252d_d1': {'inputs': ['close'], 'func': f27_mcdt_350_macd_skew_within_own_252d_d1}, 'f27_mcdt_351_macd_kurt_within_own_252d_d1': {'inputs': ['close'], 'func': f27_mcdt_351_macd_kurt_within_own_252d_d1}, 'f27_mcdt_352_macd_distribution_shift_zscore_252_d1': {'inputs': ['close'], 'func': f27_mcdt_352_macd_distribution_shift_zscore_252_d1}, 'f27_mcdt_353_macd_first_breach_of_own_q99_504_age_d1': {'inputs': ['close'], 'func': f27_mcdt_353_macd_first_breach_of_own_q99_504_age_d1}, 'f27_mcdt_354_macd_pct_rank_decay_velocity_63_d1': {'inputs': ['close'], 'func': f27_mcdt_354_macd_pct_rank_decay_velocity_63_d1}, 'f27_mcdt_355_macd_consecutive_above_own_q90_504_streak_d1': {'inputs': ['close'], 'func': f27_mcdt_355_macd_consecutive_above_own_q90_504_streak_d1}, 'f27_mcdt_356_elder_triple_screen_macd_consensus_d1': {'inputs': ['close'], 'func': f27_mcdt_356_elder_triple_screen_macd_consensus_d1}, 'f27_mcdt_357_ttm_squeeze_release_macd_bearish_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_357_ttm_squeeze_release_macd_bearish_d1}, 'f27_mcdt_358_ttm_squeeze_macd_failure_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_358_ttm_squeeze_macd_failure_indicator_d1}, 'f27_mcdt_359_bbands_macd_filter_bearish_d1': {'inputs': ['close'], 'func': f27_mcdt_359_bbands_macd_filter_bearish_d1}, 'f27_mcdt_360_macd_with_vwap_filter_bearish_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_360_macd_with_vwap_filter_bearish_d1}, 'f27_mcdt_361_macd_pivot_filter_bearish_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_361_macd_pivot_filter_bearish_d1}, 'f27_mcdt_362_macd_with_keltner_filter_bearish_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_362_macd_with_keltner_filter_bearish_d1}, 'f27_mcdt_363_macd_with_donchian_filter_bearish_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_363_macd_with_donchian_filter_bearish_d1}, 'f27_mcdt_364_dorsey_macd_relative_strength_vs_self_d1': {'inputs': ['close'], 'func': f27_mcdt_364_dorsey_macd_relative_strength_vs_self_d1}, 'f27_mcdt_365_worden_macd_4_period_consensus_d1': {'inputs': ['close'], 'func': f27_mcdt_365_worden_macd_4_period_consensus_d1}, 'f27_mcdt_366_weinstein_stage_4_macd_confirmation_d1': {'inputs': ['close'], 'func': f27_mcdt_366_weinstein_stage_4_macd_confirmation_d1}, 'f27_mcdt_367_cansil_macd_failure_signal_d1': {'inputs': ['close'], 'func': f27_mcdt_367_cansil_macd_failure_signal_d1}, 'f27_mcdt_368_macd_with_obv_filter_bearish_d1': {'inputs': ['close', 'volume'], 'func': f27_mcdt_368_macd_with_obv_filter_bearish_d1}, 'f27_mcdt_369_macd_with_chaikin_filter_bearish_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_369_macd_with_chaikin_filter_bearish_d1}, 'f27_mcdt_370_macd_with_atr_expansion_filter_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_370_macd_with_atr_expansion_filter_d1}, 'f27_mcdt_371_macd_with_williams_r_filter_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_371_macd_with_williams_r_filter_d1}, 'f27_mcdt_372_macd_with_rsi_filter_bearish_d1': {'inputs': ['close'], 'func': f27_mcdt_372_macd_with_rsi_filter_bearish_d1}, 'f27_mcdt_373_macd_with_stoch_filter_bearish_d1': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_373_macd_with_stoch_filter_bearish_d1}, 'f27_mcdt_374_macd_at_first_signal_cross_below_zero_value_d1': {'inputs': ['close'], 'func': f27_mcdt_374_macd_at_first_signal_cross_below_zero_value_d1}, 'f27_mcdt_375_macd_failure_after_long_above_zero_252_d1': {'inputs': ['close'], 'func': f27_mcdt_375_macd_failure_after_long_above_zero_252_d1}}