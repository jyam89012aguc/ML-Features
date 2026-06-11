"""divergence_advanced_pivot_confluence d3 features 001-075 - Pipeline 1b-technical.

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


def f54_dvap_001_ao_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Awesome Oscillator slope divergence sign vs price slope over 63d."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    ps = _rolling_slope(_safe_log(px), QDAYS)
    as_ = _rolling_slope(ao, QDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_002_ao_slope_div_sign_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """AO slope divergence sign at 252d horizon."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    ps = _rolling_slope(_safe_log(px), YDAYS)
    as_ = _rolling_slope(ao, YDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_003_ao_pivot_true_bearish_div_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """AO true-pivot bearish divergence: price-pivot-high higher AND AO-pivot-high lower within 63d."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    return (_true_pivot_bearish_divergence(px, ao, 5, 5, QDAYS)).diff().diff().diff()

def f54_dvap_004_ao_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """AO true-pivot bearish divergence at 252d lookback."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    return (_true_pivot_bearish_divergence(px, ao, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_005_ao_rolling_corr_with_price_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 63d correlation between AO and median-price log - negative = divergence."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    return (_rolling_corr(ao, _safe_log(px), QDAYS)).diff().diff().diff()

def f54_dvap_006_ao_rolling_corr_with_price_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 252d correlation between AO and price."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    return (_rolling_corr(ao, _safe_log(px), YDAYS)).diff().diff().diff()

def f54_dvap_007_ao_zscore_gap_at_252d_high_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """AO z-score minus price-high z-score at 252d-high bars over 63d - extension gap."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    rmax = px.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (px >= rmax - 1e-12)
    z_ao = _rolling_zscore(ao, QDAYS); z_px = _rolling_zscore(_safe_log(px), QDAYS)
    gap = (z_px - z_ao).where(at_high, np.nan)
    return (gap.rolling(QDAYS, min_periods=10).mean()).diff().diff().diff()

def f54_dvap_008_ao_bars_since_pivot_div_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last true-pivot bearish AO divergence (within 252d lookback)."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    ev = _true_pivot_bearish_divergence(px, ao, 5, 5, YDAYS)
    return (_bars_since_last_event(ev)).diff().diff().diff()

def f54_dvap_009_ao_pivot_div_count_in_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of true-pivot bearish AO divergences in last 252d."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    ev = _true_pivot_bearish_divergence(px, ao, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_010_ao_pivot_div_at_sma200_proximity_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AO pivot bearish divergence indicator restricted to bars within 2% of SMA200 from above."""
    ao = _awesome_osc(high, low)
    px = (high + low) / 2.0
    sma200 = _sma(close, 200)
    rel = _safe_div(close - sma200, sma200)
    div = _true_pivot_bearish_divergence(px, ao, 5, 5, YDAYS)
    cond = (rel > 0) & (rel < 0.02)
    return (div.where(cond, 0.0).where(div.notna(), np.nan)).diff().diff().diff()

def f54_dvap_011_uo_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ultimate Oscillator slope divergence sign vs price slope over 63d."""
    uo = _ultimate_osc(high, low, close)
    ps = _rolling_slope(_safe_log(close), QDAYS)
    uos = _rolling_slope(uo, QDAYS)
    return (_slope_div_sign(ps, uos)).diff().diff().diff()

def f54_dvap_012_uo_slope_div_sign_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO slope divergence sign at 252d horizon."""
    uo = _ultimate_osc(high, low, close)
    ps = _rolling_slope(_safe_log(close), YDAYS)
    uos = _rolling_slope(uo, YDAYS)
    return (_slope_div_sign(ps, uos)).diff().diff().diff()

def f54_dvap_013_uo_pivot_true_bearish_div_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ultimate Osc true-pivot bearish divergence within 63d."""
    uo = _ultimate_osc(high, low, close)
    return (_true_pivot_bearish_divergence(close, uo, 5, 5, QDAYS)).diff().diff().diff()

def f54_dvap_014_uo_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """UO true-pivot bearish divergence within 252d."""
    uo = _ultimate_osc(high, low, close)
    return (_true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_015_uo_rolling_corr_price_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between UO and close."""
    uo = _ultimate_osc(high, low, close)
    return (_rolling_corr(uo, _safe_log(close), QDAYS)).diff().diff().diff()

def f54_dvap_016_uo_pivot_div_count_in_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of UO true-pivot bearish divergences in 252d."""
    uo = _ultimate_osc(high, low, close)
    ev = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_017_uo_bars_since_pivot_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last UO true-pivot bearish divergence."""
    uo = _ultimate_osc(high, low, close)
    ev = _true_pivot_bearish_divergence(close, uo, 5, 5, YDAYS)
    return (_bars_since_last_event(ev)).diff().diff().diff()

def f54_dvap_018_uo_overbought_70_persistence_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with UO > 70 (overbought zone)."""
    uo = _ultimate_osc(high, low, close)
    return ((uo > 70.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f54_dvap_019_uo_overbought_x_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: UO > 70 AND close = 252d max."""
    uo = _ultimate_osc(high, low, close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((uo > 70.0) & (close >= rmax - 1e-12)).astype(float).where(uo.notna(), np.nan)).diff().diff().diff()

def f54_dvap_020_uo_zscore_gap_close_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """z(close) - z(UO) over 252d - measure of divergence magnitude."""
    uo = _ultimate_osc(high, low, close)
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    zu = _rolling_zscore(uo, YDAYS)
    return (zc - zu).diff().diff().diff()

def f54_dvap_021_dpo21_slope_div_sign_63d_d3(close: pd.Series) -> pd.Series:
    """DPO(21) slope divergence sign vs price slope over 63d."""
    dpo = _dpo_pit(close, 21)
    ps = _rolling_slope(_safe_log(close), QDAYS)
    ds = _rolling_slope(dpo, QDAYS)
    return (_slope_div_sign(ps, ds)).diff().diff().diff()

def f54_dvap_022_dpo21_pivot_true_bearish_div_252d_d3(close: pd.Series) -> pd.Series:
    """DPO(21) true-pivot bearish divergence within 252d."""
    dpo = _dpo_pit(close, 21)
    return (_true_pivot_bearish_divergence(close, dpo, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_023_dpo63_slope_div_sign_252d_d3(close: pd.Series) -> pd.Series:
    """DPO(63) slope divergence sign vs price slope over 252d."""
    dpo = _dpo_pit(close, 63)
    ps = _rolling_slope(_safe_log(close), YDAYS)
    ds = _rolling_slope(dpo, YDAYS)
    return (_slope_div_sign(ps, ds)).diff().diff().diff()

def f54_dvap_024_dpo63_pivot_true_bearish_div_252d_d3(close: pd.Series) -> pd.Series:
    """DPO(63) true-pivot bearish divergence within 252d."""
    dpo = _dpo_pit(close, 63)
    return (_true_pivot_bearish_divergence(close, dpo, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_025_dpo126_slope_div_sign_252d_d3(close: pd.Series) -> pd.Series:
    """DPO(126) (half-year) slope divergence sign over 252d."""
    dpo = _dpo_pit(close, 126)
    ps = _rolling_slope(_safe_log(close), YDAYS)
    ds = _rolling_slope(dpo, YDAYS)
    return (_slope_div_sign(ps, ds)).diff().diff().diff()

def f54_dvap_026_dpo21_rolling_corr_price_63d_d3(close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between DPO(21) and close."""
    dpo = _dpo_pit(close, 21)
    return (_rolling_corr(dpo, _safe_log(close), QDAYS)).diff().diff().diff()

def f54_dvap_027_dpo63_rolling_corr_price_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d correlation between DPO(63) and close."""
    dpo = _dpo_pit(close, 63)
    return (_rolling_corr(dpo, _safe_log(close), YDAYS)).diff().diff().diff()

def f54_dvap_028_dpo_multi_horizon_div_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of true-pivot DPO bearish divergences across 21/63/126d simultaneously in 252d window."""
    d21 = _dpo_pit(close, 21)
    d63 = _dpo_pit(close, 63)
    d126 = _dpo_pit(close, 126)
    ev21 = _true_pivot_bearish_divergence(close, d21, 5, 5, YDAYS)
    ev63 = _true_pivot_bearish_divergence(close, d63, 5, 5, YDAYS)
    ev126 = _true_pivot_bearish_divergence(close, d126, 5, 5, YDAYS)
    joint = ((ev21 > 0.5) & (ev63 > 0.5) & (ev126 > 0.5)).astype(float)
    return (joint.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_029_dpo21_zscore_div_gap_252d_d3(close: pd.Series) -> pd.Series:
    """z(close) - z(DPO21) over 252d - magnitude of DPO divergence."""
    dpo = _dpo_pit(close, 21)
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    zd = _rolling_zscore(dpo, YDAYS)
    return (zc - zd).diff().diff().diff()

def f54_dvap_030_dpo63_negative_at_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: DPO(63) < 0 AND close = 252d max - distribution while topping."""
    dpo = _dpo_pit(close, 63)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((dpo < 0) & (close >= rmax - 1e-12)).astype(float).where(dpo.notna(), np.nan)).diff().diff().diff()

def f54_dvap_031_aroon_up_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Up slope divergence sign vs price slope over 63d."""
    au = _aroon_up(high, 25)
    ps = _rolling_slope(_safe_log(high), QDAYS)
    as_ = _rolling_slope(au, QDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_032_aroon_up_slope_div_sign_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Up slope divergence sign vs price slope over 252d."""
    au = _aroon_up(high, 25)
    ps = _rolling_slope(_safe_log(high), YDAYS)
    as_ = _rolling_slope(au, YDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_033_aroon_up_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-Up true-pivot bearish divergence (price higher pivot-high, Aroon-Up lower pivot-high) within 252d."""
    au = _aroon_up(high, 25)
    return (_true_pivot_bearish_divergence(high, au, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_034_aroon_osc_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator (Up - Down) slope divergence sign over 63d."""
    au = _aroon_up(high, 25); ad = _aroon_down(low, 25); aosc = au - ad
    ps = _rolling_slope(_safe_log(high), QDAYS)
    as_ = _rolling_slope(aosc, QDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_035_aroon_osc_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator true-pivot bearish divergence in 252d."""
    au = _aroon_up(high, 25); ad = _aroon_down(low, 25); aosc = au - ad
    return (_true_pivot_bearish_divergence(high, aosc, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_036_aroon_up_drop_below_50_after_high_indicator_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: Aroon-Up drops below 50 within 5 bars after a 252d high - momentum loss event."""
    au = _aroon_up(high, 25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (high >= rmax - 1e-12).astype(int)
    recent_high = at_high.rolling(WDAYS, min_periods=1).max()
    below = (au < 50).astype(float)
    return (((recent_high > 0.5) & (below > 0.5)).astype(float).where(au.notna(), np.nan)).diff().diff().diff()

def f54_dvap_037_aroon_osc_rolling_corr_price_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 252d correlation between Aroon-Osc and close."""
    au = _aroon_up(high, 25); ad = _aroon_down(low, 25); aosc = au - ad
    return (_rolling_corr(aosc, _safe_log(high), YDAYS)).diff().diff().diff()

def f54_dvap_038_aroon_up_zscore_div_gap_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """z(high) - z(Aroon-Up) over 252d - divergence magnitude."""
    au = _aroon_up(high, 25)
    zc = _rolling_zscore(_safe_log(high), YDAYS); za = _rolling_zscore(au, YDAYS)
    return (zc - za).diff().diff().diff()

def f54_dvap_039_aroon_pivot_div_count_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Aroon-Up true-pivot bearish divergences in 252d."""
    au = _aroon_up(high, 25)
    ev = _true_pivot_bearish_divergence(high, au, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_040_aroon_up_max_minus_aroon_down_min_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max Aroon-Up - Min Aroon-Down over 252d - trend amplitude."""
    au = _aroon_up(high, 25); ad = _aroon_down(low, 25)
    umax = au.rolling(YDAYS, min_periods=QDAYS).max()
    dmin = ad.rolling(YDAYS, min_periods=QDAYS).min()
    return (umax - dmin).diff().diff().diff()

def f54_dvap_041_plus_di_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DI slope divergence sign vs price slope over 63d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    ps = _rolling_slope(_safe_log(close), QDAYS); pdis = _rolling_slope(pdi, QDAYS)
    return (_slope_div_sign(ps, pdis)).diff().diff().diff()

def f54_dvap_042_plus_di_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DI true-pivot bearish divergence in 252d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    return (_true_pivot_bearish_divergence(close, pdi, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_043_minus_di_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """-DI slope vs negative-price-slope divergence sign over 63d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    ps = -_rolling_slope(_safe_log(close), QDAYS); ndis = _rolling_slope(ndi, QDAYS)
    return (_slope_div_sign(ps, ndis)).diff().diff().diff()

def f54_dvap_044_di_spread_pdi_minus_ndi_slope_div_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(+DI minus -DI) slope vs price slope divergence sign over 63d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    spread = pdi - ndi
    ps = _rolling_slope(_safe_log(close), QDAYS); ss = _rolling_slope(spread, QDAYS)
    return (_slope_div_sign(ps, ss)).diff().diff().diff()

def f54_dvap_045_di_spread_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DI - -DI true-pivot bearish divergence in 252d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    spread = pdi - ndi
    return (_true_pivot_bearish_divergence(close, spread, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_046_adx_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX slope divergence sign vs price slope over 63d."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    dx = 100.0 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    adx = dx.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    ps = _rolling_slope(_safe_log(close), QDAYS); as_ = _rolling_slope(adx, QDAYS)
    return (_slope_div_sign(ps, as_)).diff().diff().diff()

def f54_dvap_047_adx_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX true-pivot bearish divergence in 252d - ADX falling while price still rising."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    dx = 100.0 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    adx = dx.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    return (_true_pivot_bearish_divergence(close, adx, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_048_adx_below_20_at_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX < 20 AND close = 252d max - weak trend at new high."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    dx = 100.0 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    adx = dx.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((adx < 20.0) & (close >= rmax - 1e-12)).astype(float).where(adx.notna(), np.nan)).diff().diff().diff()

def f54_dvap_049_pdi_minus_ndi_zero_cross_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of +DI minus -DI sign-flips over 63d - DI-cross chop."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    spread = pdi - ndi
    sgn = np.sign(spread.fillna(0.0))
    fl = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float)
    return (fl.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f54_dvap_050_adx_max_minus_current_252d_decay_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max(ADX in last 252d) minus current ADX - ADX decay from peak."""
    pdi, ndi = _plus_di_minus_di(high, low, close, 14)
    dx = 100.0 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    adx = dx.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    mx = adx.rolling(YDAYS, min_periods=QDAYS).max()
    return (mx - adx).diff().diff().diff()

def f54_dvap_051_vortex_pos_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+ slope divergence sign vs price slope over 63d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    ps = _rolling_slope(_safe_log(close), QDAYS); vs = _rolling_slope(vip, QDAYS)
    return (_slope_div_sign(ps, vs)).diff().diff().diff()

def f54_dvap_052_vortex_pos_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+ true-pivot bearish divergence in 252d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    return (_true_pivot_bearish_divergence(close, vip, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_053_vortex_neg_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI- slope vs price-negative-slope divergence sign over 63d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    ps = -_rolling_slope(_safe_log(close), QDAYS); ns = _rolling_slope(vim, QDAYS)
    return (_slope_div_sign(ps, ns)).diff().diff().diff()

def f54_dvap_054_vortex_spread_pos_minus_neg_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(VI+ - VI-) spread slope divergence sign over 63d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    spread = vip - vim
    ps = _rolling_slope(_safe_log(close), QDAYS); ss = _rolling_slope(spread, QDAYS)
    return (_slope_div_sign(ps, ss)).diff().diff().diff()

def f54_dvap_055_vortex_spread_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+ - VI- true-pivot bearish divergence in 252d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    spread = vip - vim
    return (_true_pivot_bearish_divergence(close, spread, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_056_vortex_pos_below_1_at_252d_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VI+ < 1.0 AND close = 252d max - bullish vortex weakness at high."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((vip < 1.0) & (close >= rmax - 1e-12)).astype(float).where(vip.notna(), np.nan)).diff().diff().diff()

def f54_dvap_057_vortex_spread_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score over 252d of (VI+ - VI-) - relative trend strength regime."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    return (_rolling_zscore(vip - vim, YDAYS)).diff().diff().diff()

def f54_dvap_058_vortex_rolling_corr_with_price_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between (VI+ - VI-) and close."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    return (_rolling_corr(vip - vim, _safe_log(close), QDAYS)).diff().diff().diff()

def f54_dvap_059_vortex_pos_to_neg_cross_count_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of VI+/VI- sign-flips in last 63d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    spread = vip - vim
    sgn = np.sign(spread.fillna(0.0))
    fl = ((sgn != sgn.shift(1)) & (sgn != 0)).astype(float)
    return (fl.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f54_dvap_060_vortex_pivot_div_count_in_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of VI+ true-pivot bearish divergences in 252d."""
    vip, vim = _vortex_pos_neg(high, low, close, 14)
    ev = _true_pivot_bearish_divergence(close, vip, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_061_smi_slope_div_sign_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic Momentum Index slope divergence sign vs price slope over 63d."""
    smi = _smi(close, high, low, 10, 3, 3)
    ps = _rolling_slope(_safe_log(close), QDAYS); ss = _rolling_slope(smi, QDAYS)
    return (_slope_div_sign(ps, ss)).diff().diff().diff()

def f54_dvap_062_smi_pivot_true_bearish_div_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """SMI true-pivot bearish divergence in 252d."""
    smi = _smi(close, high, low, 10, 3, 3)
    return (_true_pivot_bearish_divergence(close, smi, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_063_smi_overbought_above_40_persistence_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with SMI > 40."""
    smi = _smi(close, high, low, 10, 3, 3)
    return ((smi > 40.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f54_dvap_064_smi_pivot_div_count_in_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of SMI true-pivot bearish divergences in 252d."""
    smi = _smi(close, high, low, 10, 3, 3)
    ev = _true_pivot_bearish_divergence(close, smi, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_065_trix_slope_div_sign_63d_d3(close: pd.Series) -> pd.Series:
    """TRIX slope divergence sign vs price slope over 63d."""
    tr = _trix(close, 15)
    ps = _rolling_slope(_safe_log(close), QDAYS); ts = _rolling_slope(tr, QDAYS)
    return (_slope_div_sign(ps, ts)).diff().diff().diff()

def f54_dvap_066_trix_pivot_true_bearish_div_252d_d3(close: pd.Series) -> pd.Series:
    """TRIX true-pivot bearish divergence in 252d."""
    tr = _trix(close, 15)
    return (_true_pivot_bearish_divergence(close, tr, 5, 5, YDAYS)).diff().diff().diff()

def f54_dvap_067_trix_signal_line_cross_below_at_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: TRIX(15) crosses below signal-EMA9 AND close = 252d max."""
    tr = _trix(close, 15)
    sig = _ema(tr, 9)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    cross_down = ((tr < sig) & (tr.shift(1) >= sig.shift(1))).astype(float)
    return ((cross_down * (close >= rmax - 1e-12).astype(float)).where(tr.notna(), np.nan)).diff().diff().diff()

def f54_dvap_068_trix_pivot_div_count_in_252d_d3(close: pd.Series) -> pd.Series:
    """Count of TRIX true-pivot bearish divergences in 252d."""
    tr = _trix(close, 15)
    ev = _true_pivot_bearish_divergence(close, tr, 5, 5, YDAYS)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_069_trix_zscore_gap_close_252d_d3(close: pd.Series) -> pd.Series:
    """z(close) - z(TRIX) over 252d."""
    tr = _trix(close, 15)
    zc = _rolling_zscore(_safe_log(close), YDAYS); zt = _rolling_zscore(tr, YDAYS)
    return (zc - zt).diff().diff().diff()

def f54_dvap_070_trix_failed_to_make_new_high_at_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: close = 252d max but TRIX(15) NOT at 252d max - momentum non-confirmation."""
    tr = _trix(close, 15)
    px_at_max = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() - 1e-12)
    tr_at_max = (tr >= tr.rolling(YDAYS, min_periods=QDAYS).max() - 1e-12)
    return ((px_at_max & ~tr_at_max).astype(float).where(tr.notna(), np.nan)).diff().diff().diff()

def f54_dvap_071_rsi14_class_a_div_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Class A divergence (sharp): RSI14 lower-high>=10 pts AND price higher-high>=5% within 252d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                i_dec = prev[2] - i_arr[t]
                out[t] = 1.0 if (p_inc >= 0.05 and i_dec >= 10.0) else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f54_dvap_072_rsi14_class_b_div_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Class B (double-top): RSI14 small diff AND price equal-high (within 1%) within 252d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_eq = abs(p_arr[t] / prev[1] - 1.0) <= 0.01 if prev[1] > 0 else False
                i_dec = (prev[2] - i_arr[t]) >= 5.0
                out[t] = 1.0 if (p_eq and i_dec) else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f54_dvap_073_rsi14_class_c_div_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Class C (weak): RSI14 lower-high AND price slightly-higher-high (<5%) within 252d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                i_dec = prev[2] - i_arr[t]
                out[t] = 1.0 if (0 < p_inc < 0.05 and i_dec > 0) else 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()

def f54_dvap_074_rsi14_class_a_div_count_252d_d3(close: pd.Series) -> pd.Series:
    """Count of Class A RSI divergences in last 252d."""
    rsi = _rsi(close, 14)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(rsi, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); ev = np.full(nb, 0.0, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                if p_inc >= 0.05 and (prev[2] - i_arr[t]) >= 10.0:
                    ev[t] = 1.0
            history.append((t, p_arr[t], i_arr[t]))
    evs = pd.Series(ev, index=close.index)
    return (evs.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f54_dvap_075_macd_class_a_div_indicator_252d_d3(close: pd.Series) -> pd.Series:
    """Class A MACD bearish divergence: price >5% higher pivot, MACD pivot >=10% lower within 252d."""
    macd = _macd_line(close)
    p_ph = _pivot_high_values(close, 5, 5)
    i_ph = _pivot_high_values(macd, 5, 5)
    p_arr = p_ph.values; i_arr = i_ph.values
    nb = len(p_arr); out = np.full(nb, np.nan, dtype=float)
    history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]) and not np.isnan(i_arr[t]):
            recent = [h for h in history if (t - h[0]) <= YDAYS]
            if recent:
                prev = recent[-1]
                p_inc = (p_arr[t] / prev[1] - 1.0) if prev[1] > 0 else 0.0
                if prev[2] > 0:
                    i_dec = (prev[2] - i_arr[t]) / abs(prev[2])
                    out[t] = 1.0 if (p_inc >= 0.05 and i_dec >= 0.10) else 0.0
                else:
                    out[t] = 0.0
            else:
                out[t] = 0.0
            history.append((t, p_arr[t], i_arr[t]))
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=close.index)
    return (res).diff().diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d3)
# ============================================================

DIVERGENCE_ADVANCED_PIVOT_CONFLUENCE_D3_REGISTRY_001_075 = {
    "f54_dvap_001_ao_slope_div_sign_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_001_ao_slope_div_sign_63d_d3},
    "f54_dvap_002_ao_slope_div_sign_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_002_ao_slope_div_sign_252d_d3},
    "f54_dvap_003_ao_pivot_true_bearish_div_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_003_ao_pivot_true_bearish_div_63d_d3},
    "f54_dvap_004_ao_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_004_ao_pivot_true_bearish_div_252d_d3},
    "f54_dvap_005_ao_rolling_corr_with_price_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_005_ao_rolling_corr_with_price_63d_d3},
    "f54_dvap_006_ao_rolling_corr_with_price_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_006_ao_rolling_corr_with_price_252d_d3},
    "f54_dvap_007_ao_zscore_gap_at_252d_high_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_007_ao_zscore_gap_at_252d_high_63d_d3},
    "f54_dvap_008_ao_bars_since_pivot_div_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_008_ao_bars_since_pivot_div_252d_d3},
    "f54_dvap_009_ao_pivot_div_count_in_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_009_ao_pivot_div_count_in_252d_d3},
    "f54_dvap_010_ao_pivot_div_at_sma200_proximity_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_010_ao_pivot_div_at_sma200_proximity_252d_d3},
    "f54_dvap_011_uo_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_011_uo_slope_div_sign_63d_d3},
    "f54_dvap_012_uo_slope_div_sign_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_012_uo_slope_div_sign_252d_d3},
    "f54_dvap_013_uo_pivot_true_bearish_div_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_013_uo_pivot_true_bearish_div_63d_d3},
    "f54_dvap_014_uo_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_014_uo_pivot_true_bearish_div_252d_d3},
    "f54_dvap_015_uo_rolling_corr_price_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_015_uo_rolling_corr_price_63d_d3},
    "f54_dvap_016_uo_pivot_div_count_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_016_uo_pivot_div_count_in_252d_d3},
    "f54_dvap_017_uo_bars_since_pivot_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_017_uo_bars_since_pivot_div_252d_d3},
    "f54_dvap_018_uo_overbought_70_persistence_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_018_uo_overbought_70_persistence_63d_d3},
    "f54_dvap_019_uo_overbought_x_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_019_uo_overbought_x_252d_high_indicator_d3},
    "f54_dvap_020_uo_zscore_gap_close_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_020_uo_zscore_gap_close_252d_d3},
    "f54_dvap_021_dpo21_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f54_dvap_021_dpo21_slope_div_sign_63d_d3},
    "f54_dvap_022_dpo21_pivot_true_bearish_div_252d_d3": {"inputs": ["close"], "func": f54_dvap_022_dpo21_pivot_true_bearish_div_252d_d3},
    "f54_dvap_023_dpo63_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f54_dvap_023_dpo63_slope_div_sign_252d_d3},
    "f54_dvap_024_dpo63_pivot_true_bearish_div_252d_d3": {"inputs": ["close"], "func": f54_dvap_024_dpo63_pivot_true_bearish_div_252d_d3},
    "f54_dvap_025_dpo126_slope_div_sign_252d_d3": {"inputs": ["close"], "func": f54_dvap_025_dpo126_slope_div_sign_252d_d3},
    "f54_dvap_026_dpo21_rolling_corr_price_63d_d3": {"inputs": ["close"], "func": f54_dvap_026_dpo21_rolling_corr_price_63d_d3},
    "f54_dvap_027_dpo63_rolling_corr_price_252d_d3": {"inputs": ["close"], "func": f54_dvap_027_dpo63_rolling_corr_price_252d_d3},
    "f54_dvap_028_dpo_multi_horizon_div_count_252d_d3": {"inputs": ["close"], "func": f54_dvap_028_dpo_multi_horizon_div_count_252d_d3},
    "f54_dvap_029_dpo21_zscore_div_gap_252d_d3": {"inputs": ["close"], "func": f54_dvap_029_dpo21_zscore_div_gap_252d_d3},
    "f54_dvap_030_dpo63_negative_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f54_dvap_030_dpo63_negative_at_252d_high_indicator_d3},
    "f54_dvap_031_aroon_up_slope_div_sign_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_031_aroon_up_slope_div_sign_63d_d3},
    "f54_dvap_032_aroon_up_slope_div_sign_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_032_aroon_up_slope_div_sign_252d_d3},
    "f54_dvap_033_aroon_up_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_033_aroon_up_pivot_true_bearish_div_252d_d3},
    "f54_dvap_034_aroon_osc_slope_div_sign_63d_d3": {"inputs": ["high", "low"], "func": f54_dvap_034_aroon_osc_slope_div_sign_63d_d3},
    "f54_dvap_035_aroon_osc_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_035_aroon_osc_pivot_true_bearish_div_252d_d3},
    "f54_dvap_036_aroon_up_drop_below_50_after_high_indicator_d3": {"inputs": ["high", "low"], "func": f54_dvap_036_aroon_up_drop_below_50_after_high_indicator_d3},
    "f54_dvap_037_aroon_osc_rolling_corr_price_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_037_aroon_osc_rolling_corr_price_252d_d3},
    "f54_dvap_038_aroon_up_zscore_div_gap_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_038_aroon_up_zscore_div_gap_252d_d3},
    "f54_dvap_039_aroon_pivot_div_count_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_039_aroon_pivot_div_count_252d_d3},
    "f54_dvap_040_aroon_up_max_minus_aroon_down_min_252d_d3": {"inputs": ["high", "low"], "func": f54_dvap_040_aroon_up_max_minus_aroon_down_min_252d_d3},
    "f54_dvap_041_plus_di_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_041_plus_di_slope_div_sign_63d_d3},
    "f54_dvap_042_plus_di_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_042_plus_di_pivot_true_bearish_div_252d_d3},
    "f54_dvap_043_minus_di_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_043_minus_di_slope_div_sign_63d_d3},
    "f54_dvap_044_di_spread_pdi_minus_ndi_slope_div_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_044_di_spread_pdi_minus_ndi_slope_div_63d_d3},
    "f54_dvap_045_di_spread_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_045_di_spread_pivot_true_bearish_div_252d_d3},
    "f54_dvap_046_adx_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_046_adx_slope_div_sign_63d_d3},
    "f54_dvap_047_adx_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_047_adx_pivot_true_bearish_div_252d_d3},
    "f54_dvap_048_adx_below_20_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_048_adx_below_20_at_252d_high_indicator_d3},
    "f54_dvap_049_pdi_minus_ndi_zero_cross_count_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_049_pdi_minus_ndi_zero_cross_count_63d_d3},
    "f54_dvap_050_adx_max_minus_current_252d_decay_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_050_adx_max_minus_current_252d_decay_d3},
    "f54_dvap_051_vortex_pos_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_051_vortex_pos_slope_div_sign_63d_d3},
    "f54_dvap_052_vortex_pos_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_052_vortex_pos_pivot_true_bearish_div_252d_d3},
    "f54_dvap_053_vortex_neg_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_053_vortex_neg_slope_div_sign_63d_d3},
    "f54_dvap_054_vortex_spread_pos_minus_neg_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_054_vortex_spread_pos_minus_neg_slope_div_sign_63d_d3},
    "f54_dvap_055_vortex_spread_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_055_vortex_spread_pivot_true_bearish_div_252d_d3},
    "f54_dvap_056_vortex_pos_below_1_at_252d_high_indicator_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_056_vortex_pos_below_1_at_252d_high_indicator_d3},
    "f54_dvap_057_vortex_spread_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_057_vortex_spread_zscore_252d_d3},
    "f54_dvap_058_vortex_rolling_corr_with_price_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_058_vortex_rolling_corr_with_price_63d_d3},
    "f54_dvap_059_vortex_pos_to_neg_cross_count_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_059_vortex_pos_to_neg_cross_count_63d_d3},
    "f54_dvap_060_vortex_pivot_div_count_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_060_vortex_pivot_div_count_in_252d_d3},
    "f54_dvap_061_smi_slope_div_sign_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_061_smi_slope_div_sign_63d_d3},
    "f54_dvap_062_smi_pivot_true_bearish_div_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_062_smi_pivot_true_bearish_div_252d_d3},
    "f54_dvap_063_smi_overbought_above_40_persistence_63d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_063_smi_overbought_above_40_persistence_63d_d3},
    "f54_dvap_064_smi_pivot_div_count_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f54_dvap_064_smi_pivot_div_count_in_252d_d3},
    "f54_dvap_065_trix_slope_div_sign_63d_d3": {"inputs": ["close"], "func": f54_dvap_065_trix_slope_div_sign_63d_d3},
    "f54_dvap_066_trix_pivot_true_bearish_div_252d_d3": {"inputs": ["close"], "func": f54_dvap_066_trix_pivot_true_bearish_div_252d_d3},
    "f54_dvap_067_trix_signal_line_cross_below_at_high_indicator_d3": {"inputs": ["close"], "func": f54_dvap_067_trix_signal_line_cross_below_at_high_indicator_d3},
    "f54_dvap_068_trix_pivot_div_count_in_252d_d3": {"inputs": ["close"], "func": f54_dvap_068_trix_pivot_div_count_in_252d_d3},
    "f54_dvap_069_trix_zscore_gap_close_252d_d3": {"inputs": ["close"], "func": f54_dvap_069_trix_zscore_gap_close_252d_d3},
    "f54_dvap_070_trix_failed_to_make_new_high_at_252d_high_indicator_d3": {"inputs": ["close"], "func": f54_dvap_070_trix_failed_to_make_new_high_at_252d_high_indicator_d3},
    "f54_dvap_071_rsi14_class_a_div_indicator_252d_d3": {"inputs": ["close"], "func": f54_dvap_071_rsi14_class_a_div_indicator_252d_d3},
    "f54_dvap_072_rsi14_class_b_div_indicator_252d_d3": {"inputs": ["close"], "func": f54_dvap_072_rsi14_class_b_div_indicator_252d_d3},
    "f54_dvap_073_rsi14_class_c_div_indicator_252d_d3": {"inputs": ["close"], "func": f54_dvap_073_rsi14_class_c_div_indicator_252d_d3},
    "f54_dvap_074_rsi14_class_a_div_count_252d_d3": {"inputs": ["close"], "func": f54_dvap_074_rsi14_class_a_div_count_252d_d3},
    "f54_dvap_075_macd_class_a_div_indicator_252d_d3": {"inputs": ["close"], "func": f54_dvap_075_macd_class_a_div_indicator_252d_d3},
}
