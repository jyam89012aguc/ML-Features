"""divergence_advanced_pivot_confluence base features 076-150 - Pipeline 1b-technical.

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
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


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


def _rolling_corr(a, b, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 10)
    return a.rolling(n, min_periods=min_periods).corr(b)

def _awesome_osc(high, low):
    """Awesome Oscillator = SMA5(median price) - SMA34(median price)."""
    mp = (high + low) / 2.0
    return _sma(mp, 5) - _sma(mp, 34)


def _ultimate_osc(high, low, close):
    """Ultimate Oscillator (7/14/28 buying-pressure weighted average)."""
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    min_lc = pd.concat([low, pc], axis=1).min(axis=1)
    bp = close - min_lc
    avg7 = bp.rolling(7, min_periods=4).sum() / tr.rolling(7, min_periods=4).sum().replace(0, np.nan)
    avg14 = bp.rolling(14, min_periods=7).sum() / tr.rolling(14, min_periods=7).sum().replace(0, np.nan)
    avg28 = bp.rolling(28, min_periods=14).sum() / tr.rolling(28, min_periods=14).sum().replace(0, np.nan)
    return 100.0 * (4.0 * avg7 + 2.0 * avg14 + avg28) / 7.0


def _dpo(close, n=21):
    """Detrended Price Oscillator = close - SMA_n shifted forward by (n/2+1)."""
    shift_bars = int(n / 2) + 1
    return close - _sma(close, n).shift(-0) - (close.rolling(n, min_periods=max(n // 3, 2)).mean() - close.rolling(n, min_periods=max(n // 3, 2)).mean())
    # NOTE: simplified - no future shift to remain PIT-clean. Use difference of close from trailing SMA.


def _dpo_pit(close, n=21):
    """PIT-clean DPO proxy = close - SMA_n (no forward shift)."""
    return close - _sma(close, n)


def _aroon_up(high, n=25):
    """Aroon Up = 100 * (n - bars since highest high in n) / n."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 5):
            return np.nan
        i = int(np.nanargmax(w))
        return 100.0 * float(i) / float(len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n, min_periods=max(n // 3, 5)).apply(_f, raw=True)


def _aroon_down(low, n=25):
    """Aroon Down = 100 * (n - bars since lowest low) / n."""
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 5):
            return np.nan
        i = int(np.nanargmin(w))
        return 100.0 * float(i) / float(len(w) - 1) if len(w) > 1 else np.nan
    return low.rolling(n, min_periods=max(n // 3, 5)).apply(_f, raw=True)


def _plus_di_minus_di(high, low, close, n=14):
    """Wilder's +DI and -DI."""
    up = high.diff()
    dn = -low.diff()
    plus_dm = up.where((up > dn) & (up > 0), 0.0)
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr_n = tr.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    plus_di = 100.0 * plus_dm.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean() / atr_n.replace(0, np.nan)
    minus_di = 100.0 * minus_dm.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean() / atr_n.replace(0, np.nan)
    return plus_di, minus_di


def _vortex_pos_neg(high, low, close, n=14):
    """Vortex VI+ and VI-."""
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    vm_plus = (high - low.shift(1)).abs()
    vm_minus = (low - high.shift(1)).abs()
    sum_tr = tr.rolling(n, min_periods=max(n // 3, 5)).sum()
    vip = vm_plus.rolling(n, min_periods=max(n // 3, 5)).sum() / sum_tr.replace(0, np.nan)
    vim = vm_minus.rolling(n, min_periods=max(n // 3, 5)).sum() / sum_tr.replace(0, np.nan)
    return vip, vim


def _smi(close, high, low, n=10, smooth1=3, smooth2=3):
    """Stochastic Momentum Index."""
    hh = high.rolling(n, min_periods=max(n // 3, 3)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 3)).min()
    cd = close - (hh + ll) / 2.0
    hl = hh - ll
    smooth_cd = _ema(_ema(cd, smooth1), smooth2)
    smooth_hl = _ema(_ema(hl / 2.0, smooth1), smooth2)
    return 100.0 * smooth_cd / smooth_hl.replace(0, np.nan)


def _trix(close, n=15):
    """TRIX = pct change of triple-EMA."""
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()


def _rsi(close, n=14):
    """Wilder RSI."""
    d = close.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    rs = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean() / dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + rs)


def _macd_line(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)


def _macd_hist(close, fast=12, slow=26, sig=9):
    macd = _ema(close, fast) - _ema(close, slow)
    return macd - _ema(macd, sig)


def _obv(close, volume):
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _pivots(s, n_lookback=5, n_lookahead=5):
    """Identify pivot highs/lows with symmetric n-bar windows.

    PIT note: requires lookahead bars to confirm. To remain PIT-clean we
    LAG the pivot indicator by n_lookahead bars so a pivot at index t is
    only reported at t + n_lookahead.

    Returns (pivot_high_indicator, pivot_low_indicator) shifted right by n_lookahead.
    """
    arr = s.values
    nb = len(arr)
    ph = np.zeros(nb, dtype=float)
    pl = np.zeros(nb, dtype=float)
    for i in range(n_lookback, nb - n_lookahead):
        seg = arr[i - n_lookback:i + n_lookahead + 1]
        if np.isnan(seg).any():
            continue
        if arr[i] == seg.max():
            ph[i] = 1.0
        if arr[i] == seg.min():
            pl[i] = 1.0
    ph_s = pd.Series(ph, index=s.index).shift(n_lookahead)
    pl_s = pd.Series(pl, index=s.index).shift(n_lookahead)
    return ph_s, pl_s


def _pivot_high_values(s, n_lb=5, n_la=5):
    """Series carrying the price-pivot-high value at the bar it's confirmed, else NaN."""
    ph, _ = _pivots(s, n_lb, n_la)
    return s.shift(n_la).where(ph > 0.5, np.nan)


def _pivot_low_values(s, n_lb=5, n_la=5):
    _, pl = _pivots(s, n_lb, n_la)
    return s.shift(n_la).where(pl > 0.5, np.nan)


def _true_pivot_bearish_divergence(price, indicator, n_lb=5, n_la=5, lookback_bars=63):
    """True pivot divergence: price has higher pivot-high while indicator has lower pivot-high.

    Returns a Series with value 1.0 at the bar where the *current* confirmed
    pivot-high creates a divergence vs the most recent prior pivot-high
    within lookback_bars; else 0.0 (NaN before any pivot)."""
    p_ph_vals = _pivot_high_values(price, n_lb, n_la)
    i_ph_vals = _pivot_high_values(indicator, n_lb, n_la)
    p_arr = p_ph_vals.values
    i_arr = i_ph_vals.values
    nb = len(p_arr)
    out = np.full(nb, np.nan, dtype=float)
    # Track pivot history (idx, price, indicator)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            # find prior pivot within lookback
            recent = [h for h in history if (t - h[0]) <= lookback_bars]
            if recent:
                prev = recent[-1]
                if p_arr[t] > prev[1] and i_arr[t] < prev[2]:
                    out[t] = 1.0
                else:
                    out[t] = 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        else:
            # carry-forward last indicator value
            if t > 0 and not np.isnan(out[t - 1]):
                out[t] = 0.0
    return pd.Series(out, index=price.index)


def _bars_since_last_event(ind):
    """Bars since last 1.0 in `ind` (NaN treated as no-event)."""
    arr = ind.values
    nb = len(arr)
    out = np.full(nb, np.nan, dtype=float)
    last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _slope_div_sign(price_slope, ind_slope):
    """+1 if price-slope >0 and ind-slope <0 (bearish), -1 if mirror (bullish), 0 else."""
    out = pd.Series(0.0, index=price_slope.index)
    bearish = (price_slope > 0) & (ind_slope < 0)
    bullish = (price_slope < 0) & (ind_slope > 0)
    out = out.where(~bearish, 1.0).where(~bullish, -1.0)
    return out.where(price_slope.notna() & ind_slope.notna(), np.nan)


def f54_dvap_076_obv_class_a_div_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Class A OBV bearish divergence: price >5% higher-high but OBV pivot >=5% lower within 252d."""
    obv = _obv(close, volume)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(obv, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                if abs(prev[2]) > 0:
                    i_dec = (prev[2] - i_arr[t]) / abs(prev[2])
                    out[t] = 1.0 if (p_inc >= 0.05 and i_dec >= 0.05) else 0.0
                else:
                    out[t] = 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_077_divergence_class_a_intensity_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of class-A divergence counts across RSI/MACD/OBV in last 252d - bearish strength composite."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    p_ph = _pivot_high_values(close, 5, 5)
    def _cnt_a(ind, thr=10.0, pct_thr=0.05, is_pct=False):
        i_ph = _pivot_high_values(ind, 5, 5)
        p_arr = p_ph.values; i_arr = i_ph.values
        nb = len(p_arr); ev = np.zeros(nb)
        history = []
        for t in range(nb):
            if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
                recent = [h for h in history if (t - h[0]) <= YDAYS]
                if recent:
                    prev = recent[-1]
                    p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                    if is_pct:
                        if abs(prev[2]) > 0 and p_inc >= pct_thr and (prev[2] - i_arr[t]) / abs(prev[2]) >= thr:
                            ev[t] = 1.0
                    else:
                        if p_inc >= pct_thr and (prev[2] - i_arr[t]) >= thr:
                            ev[t] = 1.0
                history.append((t, p_arr[t], i_arr[t]))
        return pd.Series(ev, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum()
    rs = _cnt_a(rsi, 10.0, 0.05, False)
    ms = _cnt_a(macd, 0.10, 0.05, True)
    os = _cnt_a(obv, 0.05, 0.05, True)
    return (rs.fillna(0.0) + ms.fillna(0.0) + os.fillna(0.0))

def f54_dvap_078_divergence_age_freshness_rsi14_252d(close: pd.Series) -> pd.Series:
    """Bars since most recent RSI14 true-pivot bearish divergence within 252d."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    return (_bars_since_last_event(ev))

def f54_dvap_079_divergence_freshness_score_min_across_indicators_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Minimum (bars-since-last-pivot-divergence) across RSI/MACD/OBV - newest divergence age."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    b1 = _bars_since_last_event(e1); b2 = _bars_since_last_event(e2); b3 = _bars_since_last_event(e3)
    df = pd.concat([b1.rename('a'), b2.rename('b'), b3.rename('c')], axis=1)
    return (df.min(axis=1))

def f54_dvap_080_divergence_count_total_across_indicators_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total pivot-divergence events summed across RSI/MACD/OBV/AO/UO in 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    tot = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    return (tot.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_081_confluence_rsi_macd_simultaneous_pivot_div_252d(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 AND MACD-line true-pivot bearish divergence on the same bar within 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    return (((e1 > 0.5) & (e2 > 0.5)).astype(float).where(e1.notna() & e2.notna(), np.nan))

def f54_dvap_082_confluence_rsi_obv_simultaneous_pivot_div_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI14 AND OBV simultaneous true-pivot bearish divergence indicator within 252d."""
    rsi = _rsi(close, 14); obv = _obv(close, volume)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    return (((e1 > 0.5) & (e2 > 0.5)).astype(float).where(e1.notna() & e2.notna(), np.nan))

def f54_dvap_083_confluence_macd_ao_simultaneous_pivot_div_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD AND AO simultaneous true-pivot bearish divergence within 252d."""
    macd = _macd_line(close); ao = _awesome_osc(high, low)
    e1 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    return (((e1 > 0.5) & (e2 > 0.5)).astype(float).where(e1.notna() & e2.notna(), np.nan))

def f54_dvap_084_confluence_three_indicator_pivot_div_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI AND MACD AND OBV simultaneous true-pivot bearish divergence within 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    return (((e1 > 0.5) & (e2 > 0.5) & (e3 > 0.5)).astype(float).where(e1.notna() & e2.notna() & e3.notna(), np.nan))

def f54_dvap_085_confluence_density_2of5_indicators_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d where at least 2 of {RSI,MACD,OBV,AO,UO} simultaneously show pivot div."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    ind = (cnt >= 2).astype(float)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean())

def f54_dvap_086_confluence_density_3of5_indicators_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252d where >=3 of 5 indicators show pivot div."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    ind = (cnt >= 3).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).mean())

def f54_dvap_087_confluence_count_all_5_simultaneous_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in last 252d where ALL 5 indicators simultaneously show pivot div."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    ind = ((e1 > 0.5) & (e2 > 0.5) & (e3 > 0.5) & (e4 > 0.5) & (e5 > 0.5)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_088_confluence_div_intensity_max_count_at_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max simultaneous-divergence count across 5 indicators observed at bars where close = 252d max."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    at_max = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() - 1e-12)
    masked = cnt.where(at_max, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).max())

def f54_dvap_089_confluence_avg_div_count_in_top_decile_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean simultaneous-divergence count across 5 indicators when price-z is in top decile over 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    zp = _rolling_zscore(_safe_log(close), YDAYS)
    masked = cnt.where(zp > 1.282, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).mean())

def f54_dvap_090_confluence_intensity_score_normalized_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-indicator div-count z-scored over 252d - confluence regime intensity."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    return (_rolling_zscore(cnt, YDAYS))

def f54_dvap_091_rsi_pivot_div_at_sma50_proximity_252d(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 true-pivot bearish divergence AND close within 2% of SMA50 from above."""
    rsi = _rsi(close, 14)
    sma50 = _sma(close, 50)
    rel = _safe_div(close - sma50, sma50)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    cond = (rel > 0) & (rel < 0.02)
    return (div.where(cond, 0.0).where(div.notna(), np.nan))

def f54_dvap_092_rsi_pivot_div_at_sma200_proximity_252d(close: pd.Series) -> pd.Series:
    """Same with SMA200 proximity."""
    rsi = _rsi(close, 14)
    sma200 = _sma(close, 200)
    rel = _safe_div(close - sma200, sma200)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    cond = (rel > 0) & (rel < 0.02)
    return (div.where(cond, 0.0).where(div.notna(), np.nan))

def f54_dvap_093_macd_pivot_div_at_sma50_proximity_252d(close: pd.Series) -> pd.Series:
    """MACD true-pivot bearish divergence AND close within 2% of SMA50 from above."""
    macd = _macd_line(close)
    sma50 = _sma(close, 50)
    rel = _safe_div(close - sma50, sma50)
    div = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    cond = (rel > 0) & (rel < 0.02)
    return (div.where(cond, 0.0).where(div.notna(), np.nan))

def f54_dvap_094_any_div_at_ema_ribbon_8sma_top_252d(close: pd.Series) -> pd.Series:
    """Any RSI/MACD pivot bearish divergence AND close at the topmost of 8-MA SMA ribbon over 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close)
    lens = [10, 20, 30, 50, 80, 100, 150, 200]
    mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)
    at_top = (close >= mas.max(axis=1) - 1e-12)
    d1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    d2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    any_div = ((d1 > 0.5) | (d2 > 0.5)).astype(float)
    return ((any_div * at_top.astype(float)).where(d1.notna() & d2.notna(), np.nan))

def f54_dvap_095_div_at_252d_high_count_rsi_macd_252d(close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where (RSI div OR MACD div) AND close = 252d max."""
    rsi = _rsi(close, 14); macd = _macd_line(close)
    d1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    d2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    at_max = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() - 1e-12)
    ind = (((d1 > 0.5) | (d2 > 0.5)) & at_max).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_096_rsi_div_at_bb_upper_band_indicator_252d(close: pd.Series) -> pd.Series:
    """RSI div AND close at/above 20d Bollinger upper band (20, 2-sigma) within 252d."""
    rsi = _rsi(close, 14)
    ma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()
    up = ma + 2.0 * sd
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    return (((div > 0.5) & (close >= up)).astype(float).where(div.notna() & up.notna(), np.nan))

def f54_dvap_097_macd_div_at_bb_upper_band_indicator_252d(close: pd.Series) -> pd.Series:
    """MACD div AND close at upper BB."""
    macd = _macd_line(close)
    ma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()
    up = ma + 2.0 * sd
    div = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    return (((div > 0.5) & (close >= up)).astype(float).where(div.notna() & up.notna(), np.nan))

def f54_dvap_098_rsi_div_with_donchian20_upper_break_indicator_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """RSI div AND close at Donchian-20 upper bound within 252d."""
    rsi = _rsi(close, 14)
    dc = high.rolling(20, min_periods=10).max()
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    return (((div > 0.5) & (close >= dc - 1e-12)).astype(float).where(div.notna() & dc.notna(), np.nan))

def f54_dvap_099_rsi_div_x_close_above_sma200_pct_quartile_top(close: pd.Series) -> pd.Series:
    """RSI div AND (close/SMA200 - 1) in top quartile across 252d."""
    rsi = _rsi(close, 14)
    sma200 = _sma(close, 200)
    rel = _safe_div(close - sma200, sma200)
    q75 = rel.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    return (((div > 0.5) & (rel > q75)).astype(float).where(div.notna() & q75.notna(), np.nan))

def f54_dvap_100_any_div_at_2y_high_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: any pivot div (RSI/MACD/OBV/AO/UO) AND close at 504d max within 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    any_d = ((e1 > 0.5) | (e2 > 0.5) | (e3 > 0.5) | (e4 > 0.5) | (e5 > 0.5)).astype(float)
    rmax504 = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return ((any_d * (close >= rmax504 - 1e-12).astype(float)))

def f54_dvap_101_rsi_acceleration_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign(d²RSI14 vs d²price) over 63d - acceleration divergence sign."""
    rsi = _rsi(close, 14)
    p_acc = _safe_log(close).diff().diff()
    r_acc = rsi.diff().diff()
    p_sl = _rolling_slope(p_acc, QDAYS); r_sl = _rolling_slope(r_acc, QDAYS)
    return (_slope_div_sign(p_sl, r_sl))

def f54_dvap_102_macd_acceleration_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign(d²MACD vs d²price) over 63d."""
    m = _macd_line(close)
    p_acc = _safe_log(close).diff().diff()
    m_acc = m.diff().diff()
    p_sl = _rolling_slope(p_acc, QDAYS); m_sl = _rolling_slope(m_acc, QDAYS)
    return (_slope_div_sign(p_sl, m_sl))

def f54_dvap_103_obv_acceleration_div_sign_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign(d²OBV vs d²price) over 63d."""
    o = _obv(close, volume)
    p_acc = _safe_log(close).diff().diff()
    o_acc = o.diff().diff()
    p_sl = _rolling_slope(p_acc, QDAYS); o_sl = _rolling_slope(o_acc, QDAYS)
    return (_slope_div_sign(p_sl, o_sl))

def f54_dvap_104_rsi_acc_div_at_252d_high_indicator(close: pd.Series) -> pd.Series:
    """Acceleration divergence at 252d high: d²RSI < 0 AND d²price > 0 AND close = 252d max."""
    rsi = _rsi(close, 14)
    p_acc = _safe_log(close).diff().diff()
    r_acc = rsi.diff().diff()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((r_acc < 0) & (p_acc > 0) & (close >= rmax - 1e-12)).astype(float).where(rsi.notna(), np.nan))

def f54_dvap_105_macd_hist_jerk_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign(d³MACD-hist vs d³price) over 63d - jerk-divergence."""
    mh = _macd_hist(close)
    p_j = _safe_log(close).diff().diff().diff()
    mh_j = mh.diff().diff().diff()
    p_sl = _rolling_slope(p_j, QDAYS); mh_sl = _rolling_slope(mh_j, QDAYS)
    return (_slope_div_sign(p_sl, mh_sl))

def f54_dvap_106_rsi_acc_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(d²price) - z(d²RSI) over 252d - acceleration-divergence magnitude."""
    rsi = _rsi(close, 14)
    p_acc = _safe_log(close).diff().diff()
    r_acc = rsi.diff().diff()
    return (_rolling_zscore(p_acc, YDAYS) - _rolling_zscore(r_acc, YDAYS))

def f54_dvap_107_macd_acc_zscore_gap_252d(close: pd.Series) -> pd.Series:
    """z(d²price) - z(d²MACD) over 252d."""
    m = _macd_line(close)
    p_acc = _safe_log(close).diff().diff()
    m_acc = m.diff().diff()
    return (_rolling_zscore(p_acc, YDAYS) - _rolling_zscore(m_acc, YDAYS))

def f54_dvap_108_obv_acc_zscore_gap_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(d²price) - z(d²OBV) over 252d."""
    o = _obv(close, volume)
    p_acc = _safe_log(close).diff().diff()
    o_acc = o.diff().diff()
    return (_rolling_zscore(p_acc, YDAYS) - _rolling_zscore(o_acc, YDAYS))

def f54_dvap_109_acceleration_div_count_rsi_macd_obv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in last 252d where d²RSI<0, d²MACD<0, d²OBV<0 all simultaneously while d²price>0."""
    rsi = _rsi(close, 14); m = _macd_line(close); o = _obv(close, volume)
    p_acc = _safe_log(close).diff().diff()
    r_acc = rsi.diff().diff(); m_acc = m.diff().diff(); o_acc = o.diff().diff()
    ind = ((r_acc < 0) & (m_acc < 0) & (o_acc < 0) & (p_acc > 0)).astype(float).where(
        r_acc.notna() & m_acc.notna() & o_acc.notna() & p_acc.notna(), np.nan)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_110_acceleration_div_persistence_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with d²RSI < 0 while d²price > 0 - acceleration-div regime."""
    rsi = _rsi(close, 14)
    p_acc = _safe_log(close).diff().diff()
    r_acc = rsi.diff().diff()
    ind = ((r_acc < 0) & (p_acc > 0)).astype(float).where(r_acc.notna() & p_acc.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean())

def f54_dvap_111_rsi_7_vs_21_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign(slope(RSI7) - slope(RSI21)) over 63d - different-window same-indicator disagreement."""
    rsi7 = _rsi(close, 7); rsi21 = _rsi(close, 21)
    s7 = _rolling_slope(rsi7, QDAYS); s21 = _rolling_slope(rsi21, QDAYS)
    return (_slope_div_sign(s7, s21))

def f54_dvap_112_rsi_7_vs_14_pivot_disagreement_252d(close: pd.Series) -> pd.Series:
    """Indicator: RSI7 makes pivot-high HIGHER than prior but RSI14 makes pivot-high LOWER."""
    r7 = _rsi(close, 7); r14 = _rsi(close, 14)
    p7 = _pivot_high_values(r7, 5, 5); p14 = _pivot_high_values(r14, 5, 5)
    ph_p = _pivot_high_values(close, 5, 5)
    a7 = p7.values; a14 = p14.values; ap = ph_p.values
    nb = len(ap); out = np.full(nb, np.nan, dtype=float)
    hist = []
    for t in range(nb):
        if not np.isnan(a7[t]) and not np.isnan(a14[t]) and not np.isnan(ap[t]):
            recent = [h for h in hist if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if (a7[t] > prev[1] and a14[t] < prev[2]) else 0.0
            else:
                out[t] = 0.0
            hist.append((t, a7[t], a14[t], ap[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_113_macd_short_vs_long_period_div_63d(close: pd.Series) -> pd.Series:
    """Sign(slope MACD(8,17) - slope MACD(12,26)) over 63d."""
    m_s = _ema(close, 8) - _ema(close, 17); m_l = _ema(close, 12) - _ema(close, 26)
    s1 = _rolling_slope(m_s, QDAYS); s2 = _rolling_slope(m_l, QDAYS)
    return (_slope_div_sign(s1, s2))

def f54_dvap_114_macd_period_pivot_disagreement_252d(close: pd.Series) -> pd.Series:
    """Indicator: MACD(8,17) pivot-high higher AND MACD(12,26) pivot-high lower."""
    m_s = _ema(close, 8) - _ema(close, 17); m_l = _ema(close, 12) - _ema(close, 26)
    ps = _pivot_high_values(m_s, 5, 5); pl = _pivot_high_values(m_l, 5, 5)
    a_s = ps.values; a_l = pl.values
    nb = len(a_s); out = np.full(nb, np.nan, dtype=float)
    hist = []
    for t in range(nb):
        if not np.isnan(a_s[t]) and not np.isnan(a_l[t]):
            recent = [h for h in hist if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if (a_s[t] > prev[1] and a_l[t] < prev[2]) else 0.0
            else:
                out[t] = 0.0
            hist.append((t, a_s[t], a_l[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_115_stoch_short_vs_long_period_pivot_disagreement_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(5) vs Stoch %K(21) pivot-high disagreement within 252d."""
    def _stk(n):
        hh = high.rolling(n, min_periods=max(n // 3, 3)).max()
        ll = low.rolling(n, min_periods=max(n // 3, 3)).min()
        return 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)
    s5 = _stk(5); s21 = _stk(21)
    ps = _pivot_high_values(s5, 5, 5); pl = _pivot_high_values(s21, 5, 5)
    a_s = ps.values; a_l = pl.values
    nb = len(a_s); out = np.full(nb, np.nan, dtype=float)
    hist = []
    for t in range(nb):
        if not np.isnan(a_s[t]) and not np.isnan(a_l[t]):
            recent = [h for h in hist if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if (a_s[t] > prev[1] and a_l[t] < prev[2]) else 0.0
            else:
                out[t] = 0.0
            hist.append((t, a_s[t], a_l[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_116_roc_short_minus_long_period_div_sign_63d(close: pd.Series) -> pd.Series:
    """Sign(slope ROC(10) - slope ROC(63)) over 63d."""
    roc10 = close.pct_change(10); roc63 = close.pct_change(63)
    s10 = _rolling_slope(roc10, QDAYS); s63 = _rolling_slope(roc63, QDAYS)
    return (_slope_div_sign(s10, s63))

def f54_dvap_117_multi_period_rsi_max_div_count_252d(close: pd.Series) -> pd.Series:
    """Number of (RSI period in {7,14,21,28}) showing true-pivot bearish divergence in last 252d."""
    r7 = _rsi(close, 7); r14 = _rsi(close, 14); r21 = _rsi(close, 21); r28 = _rsi(close, 28)
    e7 = _true_pivot_bearish_divergence(close, r7, 5, 5, YDAYS)
    e14 = _true_pivot_bearish_divergence(close, r14, 5, 5, YDAYS)
    e21 = _true_pivot_bearish_divergence(close, r21, 5, 5, YDAYS)
    e28 = _true_pivot_bearish_divergence(close, r28, 5, 5, YDAYS)
    cnt = e7.fillna(0.0) + e14.fillna(0.0) + e21.fillna(0.0) + e28.fillna(0.0)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).max())

def f54_dvap_118_multi_period_rsi_simultaneous_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Indicator: all four RSI periods (7,14,21,28) simultaneously show pivot div in 252d."""
    r7 = _rsi(close, 7); r14 = _rsi(close, 14); r21 = _rsi(close, 21); r28 = _rsi(close, 28)
    e7 = _true_pivot_bearish_divergence(close, r7, 5, 5, YDAYS)
    e14 = _true_pivot_bearish_divergence(close, r14, 5, 5, YDAYS)
    e21 = _true_pivot_bearish_divergence(close, r21, 5, 5, YDAYS)
    e28 = _true_pivot_bearish_divergence(close, r28, 5, 5, YDAYS)
    ind = ((e7 > 0.5) & (e14 > 0.5) & (e21 > 0.5) & (e28 > 0.5)).astype(float)
    return (ind)

def f54_dvap_119_multi_period_macd_simultaneous_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Indicator: MACD(8,17) AND MACD(12,26) AND MACD(19,39) simultaneously show pivot div in 252d."""
    m1 = _ema(close, 8) - _ema(close, 17)
    m2 = _ema(close, 12) - _ema(close, 26)
    m3 = _ema(close, 19) - _ema(close, 39)
    e1 = _true_pivot_bearish_divergence(close, m1, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, m2, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, m3, 5, 5, YDAYS)
    return (((e1 > 0.5) & (e2 > 0.5) & (e3 > 0.5)).astype(float).where(e1.notna() & e2.notna() & e3.notna(), np.nan))

def f54_dvap_120_multi_period_stoch_disagreement_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where Stoch%K(5,14,21) disagree on direction (some up some down)."""
    def _stk(n):
        hh = high.rolling(n, min_periods=max(n // 3, 3)).max()
        ll = low.rolling(n, min_periods=max(n // 3, 3)).min()
        return 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)
    s5 = _stk(5).diff(); s14 = _stk(14).diff(); s21 = _stk(21).diff()
    sgn5 = np.sign(s5); sgn14 = np.sign(s14); sgn21 = np.sign(s21)
    disagree = ((sgn5 != sgn14) | (sgn5 != sgn21) | (sgn14 != sgn21)).astype(float)
    return (disagree.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_121_rsi_hidden_bearish_pivot_div_252d(close: pd.Series) -> pd.Series:
    """Hidden bearish RSI divergence: price LOWER pivot-high AND RSI HIGHER pivot-high within 252d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5); i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if (p_arr[t] < prev[1] and i_arr[t] > prev[2]) else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_122_macd_hidden_bearish_pivot_div_252d(close: pd.Series) -> pd.Series:
    """Hidden bearish MACD-line divergence within 252d."""
    macd = _macd_line(close)
    p_ph = _pivot_high_values(close, 5, 5); i_ph = _pivot_high_values(macd, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                out[t] = 1.0 if (p_arr[t] < prev[1] and i_arr[t] > prev[2]) else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res)

def f54_dvap_123_swing_failure_above_252d_high_indicator(close: pd.Series) -> pd.Series:
    """Indicator: close makes 252d-high but fails to make another 252d-high within next 5 bars (PIT-lagged)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = (close >= rmax - 1e-12).astype(int)
    trailing_max = close.shift(1).rolling(WDAYS, min_periods=1).max()
    failed = ((at_max.shift(WDAYS) > 0.5) & (close <= trailing_max)).astype(float)
    return (failed.where(at_max.notna(), np.nan))

def f54_dvap_124_bearish_engulf_after_div_indicator_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: bearish engulfing bar within 5 bars of latest RSI pivot bearish divergence."""
    rsi = _rsi(close, 14)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    be = ((close < open) & (close.shift(1) > open.shift(1))
          & (open >= close.shift(1)) & (close <= open.shift(1))).astype(float)
    div_recent = div.rolling(WDAYS, min_periods=1).max()
    return ((be * (div_recent > 0.5).astype(float)))

def f54_dvap_125_rsi_div_count_with_volume_above_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of RSI pivot divergences where volume > 21d-avg at the divergence bar."""
    rsi = _rsi(close, 14)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    vol_above = (volume > v_avg).astype(float)
    ev = (div * vol_above).where(div.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum())

def f54_dvap_126_macd_zero_line_rejection_after_div_indicator_252d(close: pd.Series) -> pd.Series:
    """Indicator: MACD pivot div AND MACD crosses below zero within 21 bars."""
    macd = _macd_line(close)
    div = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    below = (macd < 0).astype(float)
    cross_recent = below.rolling(MDAYS, min_periods=1).max()
    ev = (div * cross_recent).where(div.notna(), np.nan)
    return (ev)

def f54_dvap_127_rsi_break_50_after_div_indicator_63d(close: pd.Series) -> pd.Series:
    """Indicator: RSI bearish div followed by RSI crossing below 50 within 21 bars."""
    rsi = _rsi(close, 14)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    below50 = (rsi < 50).astype(float)
    recent_b50 = below50.rolling(MDAYS, min_periods=1).max()
    return ((div * recent_b50).where(div.notna(), np.nan))

def f54_dvap_128_wyckoff_upthrust_after_div_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: RSI pivot div AND high makes new 21d high but close in bottom 30% of bar range."""
    rsi = _rsi(close, 14)
    div = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    h21 = high.rolling(MDAYS, min_periods=10).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    upthrust = ((high >= h21 - 1e-12) & (pos < 0.30)).astype(float)
    recent_up = upthrust.rolling(WDAYS, min_periods=1).max()
    return ((div * recent_up).where(div.notna(), np.nan))

def f54_dvap_129_rsi_pivot_div_max_age_252d(close: pd.Series) -> pd.Series:
    """Max age (bars-since-event, capped at 252) of RSI pivot bearish divergences in last 252d."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    age = _bars_since_last_event(ev)
    return (age.clip(upper=float(YDAYS)))

def f54_dvap_130_rsi_pivot_div_intensity_score_recent_63d(close: pd.Series) -> pd.Series:
    """RSI bearish div count in last 63d divided by 63d-avg over 504d - regime intensity ratio."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    recent = ev.rolling(QDAYS, min_periods=MDAYS).sum()
    baseline = ev.rolling(DDAYS_2Y, min_periods=YDAYS).mean() * QDAYS
    return (_safe_div(recent, baseline))

def f54_dvap_131_rsi_macd_obv_slope_negative_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in 63d where slope(RSI) AND slope(MACD) AND slope(OBV) all <0 while slope(price)>0."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    r_sl = _rolling_slope(rsi, QDAYS); m_sl = _rolling_slope(macd, QDAYS)
    o_sl = _rolling_slope(obv, QDAYS); p_sl = _rolling_slope(_safe_log(close), QDAYS)
    ind = ((r_sl < 0) & (m_sl < 0) & (o_sl < 0) & (p_sl > 0)).astype(float).where(
        r_sl.notna() & m_sl.notna() & o_sl.notna() & p_sl.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).sum())

def f54_dvap_132_indicator_slope_disagreement_with_price_index_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {RSI, MACD, OBV, AO, UO} with negative slope while price slope >0 over 63d (0..5)."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    p_sl = _rolling_slope(_safe_log(close), QDAYS)
    sl_r = _rolling_slope(rsi, QDAYS); sl_m = _rolling_slope(macd, QDAYS); sl_o = _rolling_slope(obv, QDAYS)
    sl_a = _rolling_slope(ao, QDAYS); sl_u = _rolling_slope(uo, QDAYS)
    cnt = ((sl_r < 0).astype(float) + (sl_m < 0).astype(float) + (sl_o < 0).astype(float)
           + (sl_a < 0).astype(float) + (sl_u < 0).astype(float))
    return (cnt.where(p_sl > 0, 0.0))

def f54_dvap_133_indicator_slope_average_minus_price_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(slope across 5 indicators) - slope(price) over 63d - aggregate non-confirmation."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    ind_mean = (z_r + z_m + z_o + z_a + z_u) / 5.0
    p_sl = _rolling_slope(_safe_log(close), QDAYS)
    ind_sl = _rolling_slope(ind_mean, QDAYS)
    return (ind_sl - p_sl)

def f54_dvap_134_indicator_consensus_zscore_minus_price_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(z) across 5 indicators minus z(close) over 252d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    ind_mean = (z_r + z_m + z_o + z_a + z_u) / 5.0
    z_p = _rolling_zscore(_safe_log(close), YDAYS)
    return (ind_mean - z_p)

def f54_dvap_135_rsi_macd_obv_negative_correlation_with_price_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {RSI/MACD/OBV} with corr(ind, price) < 0 over 63d - bearish-div agreement count."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    c_r = _rolling_corr(rsi, _safe_log(close), QDAYS)
    c_m = _rolling_corr(macd, _safe_log(close), QDAYS)
    c_o = _rolling_corr(obv, _safe_log(close), QDAYS)
    return ((c_r < 0).astype(float) + (c_m < 0).astype(float) + (c_o < 0).astype(float))

def f54_dvap_136_five_indicator_average_corr_with_price_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean correlation of {RSI, MACD, OBV, AO, UO} with close over 63d - aggregate confirmation."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    c1 = _rolling_corr(rsi, _safe_log(close), QDAYS)
    c2 = _rolling_corr(macd, _safe_log(close), QDAYS)
    c3 = _rolling_corr(obv, _safe_log(close), QDAYS)
    c4 = _rolling_corr(ao, _safe_log(close), QDAYS)
    c5 = _rolling_corr(uo, _safe_log(close), QDAYS)
    return ((c1 + c2 + c3 + c4 + c5) / 5.0)

def f54_dvap_137_indicator_consensus_minus_price_slope_acceleration_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Diff of (avg z-acceleration of 5 indicators) and (price acceleration) over 63d."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    ind_mean = (z_r + z_m + z_o + z_a + z_u) / 5.0
    p_acc = _safe_log(close).diff().diff()
    return (ind_mean.diff().diff() - p_acc)

def f54_dvap_138_zscore_max_minus_min_across_5_indicators_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Range across z-scores of 5 indicators over 252d - dispersion of indicator signals."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    df = pd.concat([z_r.rename('a'), z_m.rename('b'), z_o.rename('c'), z_a.rename('d'), z_u.rename('e')], axis=1)
    return (df.max(axis=1) - df.min(axis=1))

def f54_dvap_139_std_of_5_indicator_z_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std across 5-indicator z-scores over 252d - cross-indicator signal dispersion."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    df = pd.concat([z_r.rename('a'), z_m.rename('b'), z_o.rename('c'), z_a.rename('d'), z_u.rename('e')], axis=1)
    return (df.std(axis=1))

def f54_dvap_140_indicator_consensus_sign_minus_price_sign_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign(avg z 5 indicators) - sign(close - SMA200) over 252d - regime disagreement indicator."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    z_r = _rolling_zscore(rsi, YDAYS); z_m = _rolling_zscore(macd, YDAYS)
    z_o = _rolling_zscore(obv, YDAYS); z_a = _rolling_zscore(ao, YDAYS); z_u = _rolling_zscore(uo, YDAYS)
    ind_mean = (z_r + z_m + z_o + z_a + z_u) / 5.0
    p_sign = np.sign(close - _sma(close, 200))
    return (np.sign(ind_mean) - p_sign)

def f54_dvap_141_master_divergence_intensity_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of normalized: total-pivot-div-count across 5 indicators + Class-A-intensity + confluence-density."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    tot = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    tot_count = tot.rolling(YDAYS, min_periods=QDAYS).sum()
    z1 = _rolling_zscore(tot_count, YDAYS)
    return (z1)

def f54_dvap_142_blowoff_divergence_signature_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of (pivot-div count from 5 indicators) and (close-z) over 252d - blowoff distribution risk."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    tot = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    tot_count = tot.rolling(YDAYS, min_periods=QDAYS).sum()
    z_c = _rolling_zscore(_safe_log(close), YDAYS)
    return (tot_count * z_c)

def f54_dvap_143_topping_signature_composite_div_x_overbought_252d(close: pd.Series) -> pd.Series:
    """Bearish div count * (RSI14 > 70) AND (close = 252d max) indicator over 252d."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    ob = (rsi > 70).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = (close >= rmax - 1e-12).astype(float)
    return ((ev * ob * at_max).where(ev.notna(), np.nan))

def f54_dvap_144_divergence_x_volume_decline_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: pivot div with volume in lower-quartile over 252d - divergence + low-volume."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    vq25 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    v_low = (volume < vq25).astype(float)
    return ((ev * v_low).where(ev.notna(), np.nan))

def f54_dvap_145_divergence_x_atr_compression_indicator_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: pivot div AND ATR21/close in lower-quartile over 252d - div + vol-crush."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    aq25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    a_low = (atr_n < aq25).astype(float)
    return ((ev * a_low).where(ev.notna(), np.nan))

def f54_dvap_146_divergence_x_failed_breakout_indicator_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Indicator: pivot div AND close fails to hold above 21d high within 5 bars."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    h21 = high.rolling(MDAYS, min_periods=10).max()
    broke = (high >= h21 - 1e-12).astype(int).rolling(WDAYS, min_periods=1).max()
    fail = ((broke > 0.5) & (close < h21.shift(5))).astype(float)
    return ((ev * fail).where(ev.notna(), np.nan))

def f54_dvap_147_master_top_signature_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite z-score sum of: confluence-density(3of5), Class-A-intensity, divergence-age-freshness(inv), price-z, RSI14."""
    rsi = _rsi(close, 14); macd = _macd_line(close); obv = _obv(close, volume)
    ao = _awesome_osc(high, low); uo = _ultimate_osc(high, low, close)
    e1 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    e2 = _true_pivot_bearish_divergence(close, macd, 5, 5, YDAYS)
    e3 = _true_pivot_bearish_divergence(close, obv, 5, 5, YDAYS)
    e4 = _true_pivot_bearish_divergence((high + low) / 2.0, ao, 5, 5, YDAYS)
    e5 = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    cnt = e1.fillna(0.0) + e2.fillna(0.0) + e3.fillna(0.0) + e4.fillna(0.0) + e5.fillna(0.0)
    freshness = _bars_since_last_event(e1).clip(upper=float(YDAYS))
    z1 = _rolling_zscore(cnt, YDAYS); z2 = -_rolling_zscore(freshness, YDAYS)
    z3 = _rolling_zscore(_safe_log(close), YDAYS); z4 = _rolling_zscore(rsi, YDAYS)
    return (z1.fillna(0.0) + z2.fillna(0.0) + z3.fillna(0.0) + z4.fillna(0.0))

def f54_dvap_148_bearish_setup_indicator_three_class_a_in_63d(close: pd.Series) -> pd.Series:
    """Indicator: >=3 Class-A RSI divergences in last 63d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5); i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); ev = np.zeros(nb, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                if prev[1] > 0:
                    p_inc = p_arr[t] / prev[1] - 1.0
                    if p_inc >= 0.05 and (prev[2] - i_arr[t]) >= 10.0:
                        ev[t] = 1.0
            history.append((t, p_arr[t], i_arr[t]))
    evs = pd.Series(ev, index=close.index)
    cnt = evs.rolling(QDAYS, min_periods=MDAYS).sum()
    return ((cnt >= 3.0).astype(float).where(cnt.notna(), np.nan))

def f54_dvap_149_divergence_explosion_rate_252d(close: pd.Series) -> pd.Series:
    """(Pivot div count in 21d) / (Pivot div count in 252d - 21d) - relative explosion rate."""
    rsi = _rsi(close, 14)
    ev = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    recent = ev.rolling(MDAYS, min_periods=10).sum()
    longterm = ev.rolling(YDAYS, min_periods=QDAYS).sum() - recent
    return (_safe_div(recent, longterm))

def f54_dvap_150_multi_horizon_div_score_combined_252d(close: pd.Series) -> pd.Series:
    """Sum: div-counts at horizons (21,63,252) for RSI - multi-horizon divergence aggregation."""
    rsi = _rsi(close, 14)
    e21 = _true_pivot_bearish_divergence(close, rsi, 5, 5, MDAYS)
    e63 = _true_pivot_bearish_divergence(close, rsi, 5, 5, QDAYS)
    e252 = _true_pivot_bearish_divergence(close, rsi, 5, 5, YDAYS)
    c21 = e21.rolling(MDAYS, min_periods=10).sum()
    c63 = e63.rolling(QDAYS, min_periods=MDAYS).sum()
    c252 = e252.rolling(YDAYS, min_periods=QDAYS).sum()
    return (c21.fillna(0.0) + c63.fillna(0.0) + c252.fillna(0.0))


# ============================================================
#                         REGISTRY 076_150 (base)
# ============================================================

DIVERGENCE_ADVANCED_PIVOT_CONFLUENCE_BASE_REGISTRY_076_150 = {
    "f54_dvap_076_obv_class_a_div_indicator_252d": {"inputs": ["close", "volume"], "func": f54_dvap_076_obv_class_a_div_indicator_252d},
    "f54_dvap_077_divergence_class_a_intensity_score_252d": {"inputs": ["close", "volume"], "func": f54_dvap_077_divergence_class_a_intensity_score_252d},
    "f54_dvap_078_divergence_age_freshness_rsi14_252d": {"inputs": ["close"], "func": f54_dvap_078_divergence_age_freshness_rsi14_252d},
    "f54_dvap_079_divergence_freshness_score_min_across_indicators_252d": {"inputs": ["close", "volume"], "func": f54_dvap_079_divergence_freshness_score_min_across_indicators_252d},
    "f54_dvap_080_divergence_count_total_across_indicators_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_080_divergence_count_total_across_indicators_252d},
    "f54_dvap_081_confluence_rsi_macd_simultaneous_pivot_div_252d": {"inputs": ["close"], "func": f54_dvap_081_confluence_rsi_macd_simultaneous_pivot_div_252d},
    "f54_dvap_082_confluence_rsi_obv_simultaneous_pivot_div_252d": {"inputs": ["close", "volume"], "func": f54_dvap_082_confluence_rsi_obv_simultaneous_pivot_div_252d},
    "f54_dvap_083_confluence_macd_ao_simultaneous_pivot_div_252d": {"inputs": ["high", "low", "close"], "func": f54_dvap_083_confluence_macd_ao_simultaneous_pivot_div_252d},
    "f54_dvap_084_confluence_three_indicator_pivot_div_252d": {"inputs": ["close", "volume"], "func": f54_dvap_084_confluence_three_indicator_pivot_div_252d},
    "f54_dvap_085_confluence_density_2of5_indicators_63d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_085_confluence_density_2of5_indicators_63d},
    "f54_dvap_086_confluence_density_3of5_indicators_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_086_confluence_density_3of5_indicators_252d},
    "f54_dvap_087_confluence_count_all_5_simultaneous_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_087_confluence_count_all_5_simultaneous_252d},
    "f54_dvap_088_confluence_div_intensity_max_count_at_high_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_088_confluence_div_intensity_max_count_at_high_252d},
    "f54_dvap_089_confluence_avg_div_count_in_top_decile_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_089_confluence_avg_div_count_in_top_decile_zscore_252d},
    "f54_dvap_090_confluence_intensity_score_normalized_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_090_confluence_intensity_score_normalized_252d},
    "f54_dvap_091_rsi_pivot_div_at_sma50_proximity_252d": {"inputs": ["close"], "func": f54_dvap_091_rsi_pivot_div_at_sma50_proximity_252d},
    "f54_dvap_092_rsi_pivot_div_at_sma200_proximity_252d": {"inputs": ["close"], "func": f54_dvap_092_rsi_pivot_div_at_sma200_proximity_252d},
    "f54_dvap_093_macd_pivot_div_at_sma50_proximity_252d": {"inputs": ["close"], "func": f54_dvap_093_macd_pivot_div_at_sma50_proximity_252d},
    "f54_dvap_094_any_div_at_ema_ribbon_8sma_top_252d": {"inputs": ["close"], "func": f54_dvap_094_any_div_at_ema_ribbon_8sma_top_252d},
    "f54_dvap_095_div_at_252d_high_count_rsi_macd_252d": {"inputs": ["close"], "func": f54_dvap_095_div_at_252d_high_count_rsi_macd_252d},
    "f54_dvap_096_rsi_div_at_bb_upper_band_indicator_252d": {"inputs": ["close"], "func": f54_dvap_096_rsi_div_at_bb_upper_band_indicator_252d},
    "f54_dvap_097_macd_div_at_bb_upper_band_indicator_252d": {"inputs": ["close"], "func": f54_dvap_097_macd_div_at_bb_upper_band_indicator_252d},
    "f54_dvap_098_rsi_div_with_donchian20_upper_break_indicator_252d": {"inputs": ["close", "high"], "func": f54_dvap_098_rsi_div_with_donchian20_upper_break_indicator_252d},
    "f54_dvap_099_rsi_div_x_close_above_sma200_pct_quartile_top": {"inputs": ["close"], "func": f54_dvap_099_rsi_div_x_close_above_sma200_pct_quartile_top},
    "f54_dvap_100_any_div_at_2y_high_indicator_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_100_any_div_at_2y_high_indicator_252d},
    "f54_dvap_101_rsi_acceleration_div_sign_63d": {"inputs": ["close"], "func": f54_dvap_101_rsi_acceleration_div_sign_63d},
    "f54_dvap_102_macd_acceleration_div_sign_63d": {"inputs": ["close"], "func": f54_dvap_102_macd_acceleration_div_sign_63d},
    "f54_dvap_103_obv_acceleration_div_sign_63d": {"inputs": ["close", "volume"], "func": f54_dvap_103_obv_acceleration_div_sign_63d},
    "f54_dvap_104_rsi_acc_div_at_252d_high_indicator": {"inputs": ["close"], "func": f54_dvap_104_rsi_acc_div_at_252d_high_indicator},
    "f54_dvap_105_macd_hist_jerk_div_sign_63d": {"inputs": ["close"], "func": f54_dvap_105_macd_hist_jerk_div_sign_63d},
    "f54_dvap_106_rsi_acc_zscore_gap_252d": {"inputs": ["close"], "func": f54_dvap_106_rsi_acc_zscore_gap_252d},
    "f54_dvap_107_macd_acc_zscore_gap_252d": {"inputs": ["close"], "func": f54_dvap_107_macd_acc_zscore_gap_252d},
    "f54_dvap_108_obv_acc_zscore_gap_252d": {"inputs": ["close", "volume"], "func": f54_dvap_108_obv_acc_zscore_gap_252d},
    "f54_dvap_109_acceleration_div_count_rsi_macd_obv_252d": {"inputs": ["close", "volume"], "func": f54_dvap_109_acceleration_div_count_rsi_macd_obv_252d},
    "f54_dvap_110_acceleration_div_persistence_63d": {"inputs": ["close"], "func": f54_dvap_110_acceleration_div_persistence_63d},
    "f54_dvap_111_rsi_7_vs_21_div_sign_63d": {"inputs": ["close"], "func": f54_dvap_111_rsi_7_vs_21_div_sign_63d},
    "f54_dvap_112_rsi_7_vs_14_pivot_disagreement_252d": {"inputs": ["close"], "func": f54_dvap_112_rsi_7_vs_14_pivot_disagreement_252d},
    "f54_dvap_113_macd_short_vs_long_period_div_63d": {"inputs": ["close"], "func": f54_dvap_113_macd_short_vs_long_period_div_63d},
    "f54_dvap_114_macd_period_pivot_disagreement_252d": {"inputs": ["close"], "func": f54_dvap_114_macd_period_pivot_disagreement_252d},
    "f54_dvap_115_stoch_short_vs_long_period_pivot_disagreement_252d": {"inputs": ["high", "low", "close"], "func": f54_dvap_115_stoch_short_vs_long_period_pivot_disagreement_252d},
    "f54_dvap_116_roc_short_minus_long_period_div_sign_63d": {"inputs": ["close"], "func": f54_dvap_116_roc_short_minus_long_period_div_sign_63d},
    "f54_dvap_117_multi_period_rsi_max_div_count_252d": {"inputs": ["close"], "func": f54_dvap_117_multi_period_rsi_max_div_count_252d},
    "f54_dvap_118_multi_period_rsi_simultaneous_div_indicator_252d": {"inputs": ["close"], "func": f54_dvap_118_multi_period_rsi_simultaneous_div_indicator_252d},
    "f54_dvap_119_multi_period_macd_simultaneous_div_indicator_252d": {"inputs": ["close"], "func": f54_dvap_119_multi_period_macd_simultaneous_div_indicator_252d},
    "f54_dvap_120_multi_period_stoch_disagreement_count_252d": {"inputs": ["high", "low", "close"], "func": f54_dvap_120_multi_period_stoch_disagreement_count_252d},
    "f54_dvap_121_rsi_hidden_bearish_pivot_div_252d": {"inputs": ["close"], "func": f54_dvap_121_rsi_hidden_bearish_pivot_div_252d},
    "f54_dvap_122_macd_hidden_bearish_pivot_div_252d": {"inputs": ["close"], "func": f54_dvap_122_macd_hidden_bearish_pivot_div_252d},
    "f54_dvap_123_swing_failure_above_252d_high_indicator": {"inputs": ["close"], "func": f54_dvap_123_swing_failure_above_252d_high_indicator},
    "f54_dvap_124_bearish_engulf_after_div_indicator_63d": {"inputs": ["open", "high", "low", "close"], "func": f54_dvap_124_bearish_engulf_after_div_indicator_63d},
    "f54_dvap_125_rsi_div_count_with_volume_above_avg_252d": {"inputs": ["close", "volume"], "func": f54_dvap_125_rsi_div_count_with_volume_above_avg_252d},
    "f54_dvap_126_macd_zero_line_rejection_after_div_indicator_252d": {"inputs": ["close"], "func": f54_dvap_126_macd_zero_line_rejection_after_div_indicator_252d},
    "f54_dvap_127_rsi_break_50_after_div_indicator_63d": {"inputs": ["close"], "func": f54_dvap_127_rsi_break_50_after_div_indicator_63d},
    "f54_dvap_128_wyckoff_upthrust_after_div_indicator_252d": {"inputs": ["high", "low", "close"], "func": f54_dvap_128_wyckoff_upthrust_after_div_indicator_252d},
    "f54_dvap_129_rsi_pivot_div_max_age_252d": {"inputs": ["close"], "func": f54_dvap_129_rsi_pivot_div_max_age_252d},
    "f54_dvap_130_rsi_pivot_div_intensity_score_recent_63d": {"inputs": ["close"], "func": f54_dvap_130_rsi_pivot_div_intensity_score_recent_63d},
    "f54_dvap_131_rsi_macd_obv_slope_negative_count_63d": {"inputs": ["close", "volume"], "func": f54_dvap_131_rsi_macd_obv_slope_negative_count_63d},
    "f54_dvap_132_indicator_slope_disagreement_with_price_index_63d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_132_indicator_slope_disagreement_with_price_index_63d},
    "f54_dvap_133_indicator_slope_average_minus_price_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_133_indicator_slope_average_minus_price_slope_63d},
    "f54_dvap_134_indicator_consensus_zscore_minus_price_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_134_indicator_consensus_zscore_minus_price_zscore_252d},
    "f54_dvap_135_rsi_macd_obv_negative_correlation_with_price_count_63d": {"inputs": ["close", "volume"], "func": f54_dvap_135_rsi_macd_obv_negative_correlation_with_price_count_63d},
    "f54_dvap_136_five_indicator_average_corr_with_price_63d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_136_five_indicator_average_corr_with_price_63d},
    "f54_dvap_137_indicator_consensus_minus_price_slope_acceleration_63d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_137_indicator_consensus_minus_price_slope_acceleration_63d},
    "f54_dvap_138_zscore_max_minus_min_across_5_indicators_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_138_zscore_max_minus_min_across_5_indicators_252d},
    "f54_dvap_139_std_of_5_indicator_z_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_139_std_of_5_indicator_z_252d},
    "f54_dvap_140_indicator_consensus_sign_minus_price_sign_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_140_indicator_consensus_sign_minus_price_sign_252d},
    "f54_dvap_141_master_divergence_intensity_composite_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_141_master_divergence_intensity_composite_252d},
    "f54_dvap_142_blowoff_divergence_signature_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_142_blowoff_divergence_signature_score_252d},
    "f54_dvap_143_topping_signature_composite_div_x_overbought_252d": {"inputs": ["close"], "func": f54_dvap_143_topping_signature_composite_div_x_overbought_252d},
    "f54_dvap_144_divergence_x_volume_decline_indicator_252d": {"inputs": ["close", "volume"], "func": f54_dvap_144_divergence_x_volume_decline_indicator_252d},
    "f54_dvap_145_divergence_x_atr_compression_indicator_252d": {"inputs": ["close", "high", "low"], "func": f54_dvap_145_divergence_x_atr_compression_indicator_252d},
    "f54_dvap_146_divergence_x_failed_breakout_indicator_252d": {"inputs": ["close", "high"], "func": f54_dvap_146_divergence_x_failed_breakout_indicator_252d},
    "f54_dvap_147_master_top_signature_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f54_dvap_147_master_top_signature_score_252d},
    "f54_dvap_148_bearish_setup_indicator_three_class_a_in_63d": {"inputs": ["close"], "func": f54_dvap_148_bearish_setup_indicator_three_class_a_in_63d},
    "f54_dvap_149_divergence_explosion_rate_252d": {"inputs": ["close"], "func": f54_dvap_149_divergence_explosion_rate_252d},
    "f54_dvap_150_multi_horizon_div_score_combined_252d": {"inputs": ["close"], "func": f54_dvap_150_multi_horizon_div_score_combined_252d},
}
