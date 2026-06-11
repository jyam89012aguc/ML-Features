"""28_trix_tsi_cci_family d3 features 301-375 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _rolling_slope_inner(w):
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
    return s.rolling(n, min_periods=min_periods).apply(_rolling_slope_inner, raw=True)

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

def _adl(high, low, close, volume):
    """Accumulation/Distribution Line. CLV = ((C-L)-(H-C))/(H-L)."""
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    return mfv.cumsum()

def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    ad = _adl(high, low, close, volume)
    return _ema(ad, fast) - _ema(ad, slow)

def _cmf(high, low, close, volume, n=20):
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(), volume.rolling(n, min_periods=max(n // 3, 2)).sum())

def _klinger(high, low, close, volume, fast=34, slow=55):
    """KVO (Klinger). Uses signed volume force vector and double-EMA difference."""
    tp = (high + low + close) / 3.0
    tp_prev = tp.shift(1)
    direction = pd.Series(np.where(tp > tp_prev, 1.0, np.where(tp < tp_prev, -1.0, 0.0)), index=close.index)
    dm = high - low
    cm = dm.rolling(fast, min_periods=max(fast // 3, 2)).sum()
    ratio = _safe_div(dm, cm) * 2.0 - 1.0
    vf = volume * direction * ratio.where(cm > 0, 0.0) * 100.0
    return _ema(vf, fast) - _ema(vf, slow)

def _force_index(close, volume, n=13):
    raw = close.diff() * volume
    return _ema(raw, n)

def _mass_index(high, low, n_smooth=9, n_sum=25):
    rng = high - low
    e1 = _ema(rng, n_smooth)
    e2 = _ema(e1, n_smooth)
    ratio = _safe_div(e1, e2)
    return ratio.rolling(n_sum, min_periods=max(n_sum // 3, 2)).sum()

def _choppiness(high, low, close, n=14):
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    rng = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * (_safe_log(sum_tr) - _safe_log(rng.replace(0, np.nan))) / float(np.log(n))

def _hurst_dominant_period_inner(w):
    """Find lag in [5,21] with peak autocorrelation. Window length up to 63."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    wc = w - w.mean()
    best_p = np.nan
    best_v = -np.inf
    max_lag = min(len(w) // 3, 21)
    for lag in range(5, max_lag + 1):
        a = wc[lag:]
        b = wc[:-lag]
        if len(a) < 3:
            continue
        denom = np.sqrt((a * a).sum() * (b * b).sum())
        if denom == 0:
            continue
        v = (a * b).sum() / denom
        if v > best_v:
            best_v = v
            best_p = float(lag)
    return best_p

def _hurst_amplitude_inner(w):
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    return float(np.max(w) - np.min(w))

def _ehlers_super_smoother(s, n=10):
    """Two-pole low-pass filter — proxy via cascaded EMA pair."""
    return _ema(_ema(s, n), n)

def _ehlers_cyber_cycle(close, alpha=0.07):
    """Simplified cyber-cycle: smooth close, take 2nd-difference cycle component."""
    sm = _ehlers_super_smoother(close, 10)
    return sm - 2.0 * sm.shift(1) + sm.shift(2)

def _ehlers_dominant_phase_inner(w):
    if np.isnan(w).any() or len(w) < 5:
        return np.nan
    n = len(w)
    if n < 4:
        return np.nan
    return float(np.arctan2(w[-1] - w[-3], w[-2] - w[-4]))

def _ehlers_dominant_phase(s, n=21):
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_ehlers_dominant_phase_inner, raw=True)

def _robust_cci_iqr(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    med = tp.rolling(n, min_periods=max(n // 3, 2)).median()
    q75 = tp.rolling(n, min_periods=max(n // 3, 2)).quantile(0.75)
    q25 = tp.rolling(n, min_periods=max(n // 3, 2)).quantile(0.25)
    iqr = (q75 - q25).replace(0, np.nan)
    return _safe_div(tp - med, 0.015 * iqr)

def _trimmed_mean_inner(w, pct=0.2):
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    k = int(pct * n)
    if n - 2 * k <= 0:
        return float(np.mean(w))
    s = np.sort(w)
    return float(np.mean(s[k:n - k]))

def _trimmed_mean(s, n=21, pct=0.2):
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(lambda w: _trimmed_mean_inner(w, pct), raw=True)

def _winsorize_inner(w, p=0.03):
    if np.isnan(w).any() or len(w) < 10:
        return w[-1] if len(w) > 0 else np.nan
    lo = np.quantile(w, p)
    hi = np.quantile(w, 1.0 - p)
    return float(np.clip(w[-1], lo, hi))

def _winsorize(s, n=252, p=0.03):
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(lambda w: _winsorize_inner(w, p), raw=True)

def _nvi(close, volume):
    ret = close.pct_change().fillna(0.0)
    vd = volume.diff()
    factor = np.where(vd < 0, 1.0 + ret, 1.0)
    factor = pd.Series(factor, index=close.index)
    factor.iloc[0] = 1000.0
    return factor.cumprod()

def _pvi(close, volume):
    ret = close.pct_change().fillna(0.0)
    vd = volume.diff()
    factor = np.where(vd > 0, 1.0 + ret, 1.0)
    factor = pd.Series(factor, index=close.index)
    factor.iloc[0] = 1000.0
    return factor.cumprod()

def _eom(high, low, volume, n=14):
    mid_now = (high + low) / 2.0
    mid_prev = mid_now.shift(1)
    move = mid_now - mid_prev
    rng = (high - low).replace(0, np.nan)
    box = _safe_div(volume, rng)
    raw = _safe_div(move, box)
    return raw.rolling(n, min_periods=max(n // 3, 2)).mean()

def _basket_classical(high, low, close):
    return [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20), _cmo(close, 14), _dpo(close, MDAYS), _kst(close)]

def f28_ttcf_301_chaikin_oscillator_3_10_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Oscillator(3, 10): EMA3(ADL) - EMA10(ADL). Money-flow momentum."""
    return _chaikin_osc(high, low, close, volume, 3, 10).diff().diff().diff()

def f28_ttcf_302_chaikin_oscillator_above_zero_state_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Chaikin Osc > 0 — accumulation regime."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    return (c > 0).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_303_chaikin_osc_bearish_cross_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Chaikin Osc crossed below zero — distribution-onset trigger."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    return ((c.shift(1) >= 0) & (c < 0)).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_304_chaikin_osc_div_vs_price_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish divergence: price new 63d high but Chaikin Osc below prior 63d max."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & c_below).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_305_chaikin_money_flow_20_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMF(20): sum(MFV)/sum(Vol). Money-flow strength over rolling 20d."""
    return _cmf(high, low, close, volume, 20).diff().diff().diff()

def f28_ttcf_306_cmf_below_zero_state_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if CMF(20) < 0 — distribution regime."""
    c = _cmf(high, low, close, volume, 20)
    return (c < 0).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_307_cmf_dwell_below_zero_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CMF < 0 — quarterly distribution dwell."""
    c = _cmf(high, low, close, volume, 20)
    return (c < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_308_cmf_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d z-score of CMF — distribution-context CMF position."""
    return _rolling_zscore(_cmf(high, low, close, volume, 20), YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_309_klinger_oscillator_34_55_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """KVO(34, 55): signed-volume-force EMA differential — classical Klinger setup."""
    return _klinger(high, low, close, volume, 34, 55).diff().diff().diff()

def f28_ttcf_310_klinger_signal_13_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """KVO signal line = EMA13 of KVO."""
    return _ema(_klinger(high, low, close, volume, 34, 55), 13).diff().diff().diff()

def f28_ttcf_311_klinger_bearish_cross_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if KVO crossed below its EMA13 signal — KVO bearish trigger."""
    k = _klinger(high, low, close, volume, 34, 55)
    s = _ema(k, 13)
    d = k - s
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan).diff().diff().diff()

def f28_ttcf_312_klinger_above_zero_state_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if KVO > 0 — bullish volume-flow regime."""
    k = _klinger(high, low, close, volume, 34, 55)
    return (k > 0).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f28_ttcf_313_klinger_div_vs_price_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish KVO divergence vs price at 63d horizon."""
    k = _klinger(high, low, close, volume, 34, 55)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    k_below = k < k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & k_below).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f28_ttcf_314_klinger_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d z-score of KVO — distribution-context KVO."""
    return _rolling_zscore(_klinger(high, low, close, volume, 34, 55), YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_315_klinger_persistence_below_zero_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with KVO < 0 — annual distribution dwell."""
    k = _klinger(high, low, close, volume, 34, 55)
    return (k < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna(), np.nan).diff().diff().diff()

def f28_ttcf_316_force_index_5_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index (EMA5 of ret*vol) — short-horizon force."""
    return _force_index(close, volume, 5).diff().diff().diff()

def f28_ttcf_317_force_index_20_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index (EMA20) — monthly horizon force."""
    return _force_index(close, volume, 20).diff().diff().diff()

def f28_ttcf_318_force_index_above_zero_state_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if EMA13 Force Index > 0 — net-positive force."""
    f = _force_index(close, volume, 13)
    return (f > 0).astype(float).where(f.notna(), np.nan).diff().diff().diff()

def f28_ttcf_319_force_index_zero_cross_down_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if EMA13 Force Index crossed below zero — force-flip-bearish trigger."""
    f = _force_index(close, volume, 13)
    return ((f.shift(1) >= 0) & (f < 0)).astype(float).where(f.notna(), np.nan).diff().diff().diff()

def f28_ttcf_320_force_index_div_vs_price_63_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish Force Index divergence vs price at 63d horizon."""
    f = _force_index(close, volume, 13)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    f_below = f < f.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & f_below).astype(float).where(f.notna(), np.nan).diff().diff().diff()

def f28_ttcf_321_force_index_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d z-score of EMA13 Force Index — distribution-context force."""
    return _rolling_zscore(_force_index(close, volume, 13), YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_322_mass_index_25_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index(25,9): sum-of-range-EMA-ratio over 25 — range-expansion topping indicator."""
    return _mass_index(high, low, 9, 25).diff().diff().diff()

def f28_ttcf_323_mass_index_reversal_bulge_indicator_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if Mass Index crossed above 27 then back below 26.5 — Donald-Dorsey reversal-bulge."""
    m = _mass_index(high, low, 9, 25)
    crossed_up = (m > 27.0).rolling(MDAYS, min_periods=1).max()
    fell_back = m < 26.5
    return (fell_back & (crossed_up > 0)).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f28_ttcf_324_mass_index_above_27_state_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if Mass Index > 27 — range-expansion regime."""
    m = _mass_index(high, low, 9, 25)
    return (m > 27.0).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f28_ttcf_325_mass_index_dwell_above_27_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with Mass Index > 27 — quarterly range-expansion dwell."""
    m = _mass_index(high, low, 9, 25)
    return (m > 27.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(m.notna(), np.nan).diff().diff().diff()

def f28_ttcf_326_mass_index_zscore_252_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """252d z-score of Mass Index — distribution-context mass."""
    return _rolling_zscore(_mass_index(high, low, 9, 25), YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_327_choppiness_index_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Choppiness Index(14): 100 * log10(sum(TR)/range) / log10(n)."""
    return _choppiness(high, low, close, 14).diff().diff().diff()

def f28_ttcf_328_choppiness_above_61_8_trend_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Choppiness > 61.8 — consolidation / trend-ending state."""
    c = _choppiness(high, low, close, 14)
    return (c > 61.8).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_329_choppiness_below_38_2_trend_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Choppiness < 38.2 — strong-trend state."""
    c = _choppiness(high, low, close, 14)
    return (c < 38.2).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_330_choppiness_dwell_above_61_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with Choppiness > 61.8 — quarterly consolidation dwell."""
    c = _choppiness(high, low, close, 14)
    return (c > 61.8).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_331_choppiness_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d z-score of Choppiness — distribution-context chop."""
    return _rolling_zscore(_choppiness(high, low, close, 14), YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_332_hurst_cycles_dominant_period_252_d3(close: pd.Series) -> pd.Series:
    """Dominant cycle period from rolling 63d autocorrelation peak in lag [5,21]."""
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_dominant_period_inner, raw=True).diff().diff().diff()

def f28_ttcf_333_hurst_cycles_period_zscore_252_d3(close: pd.Series) -> pd.Series:
    """252d z-score of dominant cycle period — cycle-length distribution position."""
    p = close.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_dominant_period_inner, raw=True)
    return _rolling_zscore(p, YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_334_hurst_cycles_period_stability_63_d3(close: pd.Series) -> pd.Series:
    """63d std of dominant cycle period — lower = more stable cycle structure."""
    p = close.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_dominant_period_inner, raw=True)
    return p.rolling(QDAYS, min_periods=MDAYS).std().diff().diff().diff()

def f28_ttcf_335_hurst_cycles_amplitude_decay_63_d3(close: pd.Series) -> pd.Series:
    """Decay in 63d-window amplitude (max-min) vs 63 bars ago — cycle-amplitude decay."""
    amp = close.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_amplitude_inner, raw=True)
    return (amp - amp.shift(QDAYS)).diff().diff().diff()

def f28_ttcf_336_ehlers_sinewave_indicator_proxy_d3(close: pd.Series) -> pd.Series:
    """Ehlers sinewave proxy: sin of dominant cycle phase. In [-1, 1]."""
    phase = _ehlers_dominant_phase(close, MDAYS)
    return np.sin(phase).diff().diff().diff()

def f28_ttcf_337_ehlers_sinewave_lead_cross_down_d3(close: pd.Series) -> pd.Series:
    """1 if sinewave proxy crossed below its 1-bar lead (sin(phase + pi/4)) — turn-trigger."""
    phase = _ehlers_dominant_phase(close, MDAYS)
    sw = np.sin(phase)
    lead = np.sin(phase + np.pi / 4.0)
    d = sw - lead
    return ((d.shift(1) > 0) & (d <= 0)).astype(float).where(d.notna(), np.nan).diff().diff().diff()

def f28_ttcf_338_ehlers_even_better_sinewave_d3(close: pd.Series) -> pd.Series:
    """Ehlers "even-better sinewave": sinewave normalized by trailing signal power (63d std)."""
    phase = _ehlers_dominant_phase(close, MDAYS)
    sw = np.sin(phase)
    pw = close.diff().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sw, pw).diff().diff().diff()

def f28_ttcf_339_ehlers_stochastic_cyber_cycle_proxy_d3(close: pd.Series) -> pd.Series:
    """Stochastic of cyber-cycle: (cc - min)/(max - min) over 21d."""
    cc = _ehlers_cyber_cycle(close)
    mn = cc.rolling(MDAYS, min_periods=WDAYS).min()
    mx = cc.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(cc - mn, (mx - mn).replace(0, np.nan)).diff().diff().diff()

def f28_ttcf_340_ehlers_snake_indicator_proxy_d3(close: pd.Series) -> pd.Series:
    """Snake indicator proxy: signed smoothed momentum direction (sign of cyber-cycle, smoothed)."""
    cc = _ehlers_cyber_cycle(close)
    return _ehlers_super_smoother(np.sign(cc).astype(float), 10).diff().diff().diff()

def f28_ttcf_341_ehlers_adaptive_rsi_proxy_d3(close: pd.Series) -> pd.Series:
    """Adaptive RSI proxy: blend RSI(7), RSI(14), RSI(21) weighted by closeness of
    each fixed period to half the rolling dominant cycle. PIT-clean, vectorized."""
    dc = close.rolling(QDAYS, min_periods=MDAYS).apply(_hurst_dominant_period_inner, raw=True)
    half = (dc / 2.0).clip(lower=5.0, upper=30.0)
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    rsis = {}
    for n in (7, 14, 21):
        su = up.rolling(n, min_periods=max(n // 3, 2)).sum()
        sd_ = dn.rolling(n, min_periods=max(n // 3, 2)).sum()
        rsis[n] = 100.0 * _safe_div(su, su + sd_)
    w7 = 1.0 / ((half - 7.0).abs() + 1.0)
    w14 = 1.0 / ((half - 14.0).abs() + 1.0)
    w21 = 1.0 / ((half - 21.0).abs() + 1.0)
    wsum = w7 + w14 + w21
    return _safe_div(rsis[7] * w7 + rsis[14] * w14 + rsis[21] * w21, wsum).diff().diff().diff()

def f28_ttcf_342_ehlers_emd_trend_component_proxy_63_d3(close: pd.Series) -> pd.Series:
    """Simplified EMD trend component: 63d super-smoother of close (trend)."""
    return _ehlers_super_smoother(close, QDAYS).diff().diff().diff()

def f28_ttcf_343_ehlers_emd_cycle_component_proxy_63_d3(close: pd.Series) -> pd.Series:
    """Simplified EMD cycle component: close - 63d super-smoother."""
    return (close - _ehlers_super_smoother(close, QDAYS)).diff().diff().diff()

def f28_ttcf_344_ehlers_zero_lag_macd_proxy_d3(close: pd.Series) -> pd.Series:
    """Zero-lag MACD proxy: 2*EMA(close,12) - EMA(EMA(close,12),12), minus same for 26."""
    e12 = _ema(close, 12)
    zl12 = 2.0 * e12 - _ema(e12, 12)
    e26 = _ema(close, 26)
    zl26 = 2.0 * e26 - _ema(e26, 26)
    return (zl12 - zl26).diff().diff().diff()

def f28_ttcf_345_ehlers_predictive_filter_lead_proxy_d3(close: pd.Series) -> pd.Series:
    """Predictive filter: forecast = current + slope*1. Lead = forecast - close. Slope from EMA21."""
    sm = _ehlers_super_smoother(close, MDAYS)
    sl = sm.diff()
    forecast = sm + sl
    return (forecast - close).diff().diff().diff()

def f28_ttcf_346_robust_cci_iqr_20_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) using IQR (q75-q25) instead of MAD for normalization — outlier-resistant CCI."""
    return _robust_cci_iqr(high, low, close, 20).diff().diff().diff()

def f28_ttcf_347_robust_cci_iqr_above_100_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if robust-CCI-IQR > 100 — robust-OB state."""
    c = _robust_cci_iqr(high, low, close, 20)
    return (c > 100.0).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_348_trimmed_mean_smoothed_close_distance_21_d3(close: pd.Series) -> pd.Series:
    """Distance: close - trimmed-mean(20%) of close over 21d. Outlier-resistant trend distance."""
    tm = _trimmed_mean(close, MDAYS, 0.2)
    return (close - tm).diff().diff().diff()

def f28_ttcf_349_quantile_oscillator_q90_q10_band_position_63_d3(close: pd.Series) -> pd.Series:
    """(close - q10) / (q90 - q10) over past 63d — close position in quantile band."""
    q90 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    q10 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.1)
    return _safe_div(close - q10, (q90 - q10).replace(0, np.nan)).diff().diff().diff()

def f28_ttcf_350_quantile_oscillator_band_breakout_above_state_d3(close: pd.Series) -> pd.Series:
    """1 if close > 63d q90 — quantile-band breakout up."""
    q90 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    return (close > q90).astype(float).where(q90.notna(), np.nan).diff().diff().diff()

def f28_ttcf_351_winsorized_trix_15_3pct_d3(close: pd.Series) -> pd.Series:
    """TRIX(15) applied to winsorized (3% tail) close over 252d — extreme-bar resistance."""
    cw = _winsorize(close, YDAYS, 0.03)
    return _trix(cw, 15).diff().diff().diff()

def f28_ttcf_352_winsorized_returns_zscore_63_d3(close: pd.Series) -> pd.Series:
    """63d z-score of winsorized 1-bar returns — bounded-return distribution position."""
    r = close.pct_change()
    rw = _winsorize(r, YDAYS, 0.03)
    return _rolling_zscore(rw, QDAYS, min_periods=MDAYS).diff().diff().diff()

def f28_ttcf_353_median_absolute_deviation_normalized_close_21_d3(close: pd.Series) -> pd.Series:
    """(close - median21) / MAD21*1.4826 — MAD-normalized close (robust z)."""
    med = close.rolling(MDAYS, min_periods=WDAYS).median()
    mad = (close - med).abs().rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(close - med, 1.4826 * mad).diff().diff().diff()

def f28_ttcf_354_negative_volume_index_value_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """NVI: compounded return on declining-volume bars (smart-money proxy)."""
    return _nvi(close, volume).diff().diff().diff()

def f28_ttcf_355_negative_volume_index_signal_ema255_below_state_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if NVI < EMA255(NVI) — NVI below long signal (smart-money distribution)."""
    n = _nvi(close, volume)
    s = _ema(n, 255)
    return (n < s).astype(float).where(s.notna(), np.nan).diff().diff().diff()

def f28_ttcf_356_positive_volume_index_value_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVI: compounded return on increasing-volume bars (crowd-money proxy)."""
    return _pvi(close, volume).diff().diff().diff()

def f28_ttcf_357_pvi_signal_ema255_below_state_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if PVI < EMA255(PVI) — crowd-money in distribution."""
    p = _pvi(close, volume)
    s = _ema(p, 255)
    return (p < s).astype(float).where(s.notna(), np.nan).diff().diff().diff()

def f28_ttcf_358_ease_of_movement_14_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EOM(14): (midpoint move) / (volume / range). Higher = easier moves."""
    return _eom(high, low, volume, 14).diff().diff().diff()

def f28_ttcf_359_ease_of_movement_below_zero_state_d3(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if EOM(14) < 0 — heavy / downward-biased moves."""
    e = _eom(high, low, volume, 14)
    return (e < 0).astype(float).where(e.notna(), np.nan).diff().diff().diff()

def f28_ttcf_360_trade_intensity_index_proxy_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite trade-intensity = z(EOM21) - z(volume21) + z(range21) — sustained-strong-trade proxy."""
    e = _eom(high, low, volume, MDAYS)
    rng = high - low
    return (_rolling_zscore(e, QDAYS, min_periods=MDAYS) - _rolling_zscore(volume, QDAYS, min_periods=MDAYS) + _rolling_zscore(rng, QDAYS, min_periods=MDAYS)).diff().diff().diff()

def f28_ttcf_361_turnover_velocity_decay_63_d3(volume: pd.Series, close: pd.Series) -> pd.Series:
    """63d decay rate of turnover (volume*close): EMA21(turn) / EMA63(turn) — turnover-velocity shift."""
    turn = volume * close
    return _safe_div(_ema(turn, MDAYS), _ema(turn, QDAYS)).diff().diff().diff()

def f28_ttcf_362_trix_adaptive_zero_line_504_d3(close: pd.Series) -> pd.Series:
    """TRIX minus its 504d (2y) rolling median — adaptive-zero-line TRIX."""
    t = _trix(close, 15)
    med = t.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    return (t - med).diff().diff().diff()

def f28_ttcf_363_trix_above_adaptive_zero_state_d3(close: pd.Series) -> pd.Series:
    """1 if TRIX > its 504d median — bullish on adaptive zero."""
    t = _trix(close, 15)
    med = t.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    return (t > med).astype(float).where(med.notna(), np.nan).diff().diff().diff()

def f28_ttcf_364_tsi_adaptive_ob_threshold_q90_504_d3(close: pd.Series) -> pd.Series:
    """504d q90 of TSI — adaptive OB threshold (use as TSI's own dynamic ceiling)."""
    t = _tsi(close, 25, 13)
    return t.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9).diff().diff().diff()

def f28_ttcf_365_tsi_above_adaptive_ob_state_d3(close: pd.Series) -> pd.Series:
    """1 if TSI > its 504d q90 — adaptive-OB state."""
    t = _tsi(close, 25, 13)
    q = t.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return (t > q).astype(float).where(q.notna(), np.nan).diff().diff().diff()

def f28_ttcf_366_cci_adaptive_ob_threshold_q90_504_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """504d q90 of CCI(20) — adaptive OB threshold."""
    c = _cci(high, low, close, 20)
    return c.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9).diff().diff().diff()

def f28_ttcf_367_cci_above_adaptive_ob_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI(20) > its 504d q90 — adaptive CCI-OB state."""
    c = _cci(high, low, close, 20)
    q = c.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return (c > q).astype(float).where(q.notna(), np.nan).diff().diff().diff()

def f28_ttcf_368_cmo_adaptive_ob_threshold_q90_504_d3(close: pd.Series) -> pd.Series:
    """504d q90 of CMO(14) — adaptive OB threshold."""
    c = _cmo(close, 14)
    return c.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9).diff().diff().diff()

def f28_ttcf_369_cmo_above_adaptive_ob_state_d3(close: pd.Series) -> pd.Series:
    """1 if CMO(14) > its 504d q90 — adaptive CMO-OB state."""
    c = _cmo(close, 14)
    q = c.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
    return (c > q).astype(float).where(q.notna(), np.nan).diff().diff().diff()

def f28_ttcf_370_dpo_adaptive_above_zero_state_d3(close: pd.Series) -> pd.Series:
    """1 if DPO(21) > its 504d median — DPO above adaptive zero."""
    d = _dpo(close, MDAYS)
    med = d.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    return (d > med).astype(float).where(med.notna(), np.nan).diff().diff().diff()

def f28_ttcf_371_kst_adaptive_above_zero_state_d3(close: pd.Series) -> pd.Series:
    """1 if KST > its 504d median — KST above adaptive zero."""
    k = _kst(close)
    med = k.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    return (k > med).astype(float).where(med.notna(), np.nan).diff().diff().diff()

def f28_ttcf_372_oscillator_basket_adaptive_consensus_count_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators above their adaptive (504d median) zero — adaptive bullish breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        med = sig.rolling(DDAYS_2Y, min_periods=YDAYS).median()
        cnt = cnt + (sig > med).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_373_oscillator_basket_adaptive_extreme_count_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators above their adaptive (504d) q90 — adaptive-extreme breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        q = sig.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.9)
        cnt = cnt + (sig > q).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_374_vol_regime_adaptive_oscillator_consensus_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Basket adaptive-consensus count, scaled by vol regime (1/ATR21-rank vs 252) — vol-adjusted breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        med = sig.rolling(DDAYS_2Y, min_periods=YDAYS).median()
        cnt = cnt + (sig > med).astype(float).fillna(0)
    atr = _atr(high, low, close, MDAYS)
    rank = atr.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (cnt * (1.0 - rank)).diff().diff().diff()

def f28_ttcf_375_trend_regime_adaptive_oscillator_consensus_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Basket adaptive-consensus count, scaled by trend regime (sign(slope(close,63))) — trend-adjusted breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        med = sig.rolling(DDAYS_2Y, min_periods=YDAYS).median()
        cnt = cnt + (sig > med).astype(float).fillna(0)
    sl = _rolling_slope(close, QDAYS)
    return (cnt * np.sign(sl).astype(float)).diff().diff().diff()
TRIX_TSI_CCI_FAMILY_D3_REGISTRY_301_375 = {'f28_ttcf_301_chaikin_oscillator_3_10_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_301_chaikin_oscillator_3_10_d3}, 'f28_ttcf_302_chaikin_oscillator_above_zero_state_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_302_chaikin_oscillator_above_zero_state_d3}, 'f28_ttcf_303_chaikin_osc_bearish_cross_indicator_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_303_chaikin_osc_bearish_cross_indicator_d3}, 'f28_ttcf_304_chaikin_osc_div_vs_price_63_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_304_chaikin_osc_div_vs_price_63_d3}, 'f28_ttcf_305_chaikin_money_flow_20_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_305_chaikin_money_flow_20_d3}, 'f28_ttcf_306_cmf_below_zero_state_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_306_cmf_below_zero_state_d3}, 'f28_ttcf_307_cmf_dwell_below_zero_63_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_307_cmf_dwell_below_zero_63_d3}, 'f28_ttcf_308_cmf_zscore_252_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_308_cmf_zscore_252_d3}, 'f28_ttcf_309_klinger_oscillator_34_55_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_309_klinger_oscillator_34_55_d3}, 'f28_ttcf_310_klinger_signal_13_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_310_klinger_signal_13_d3}, 'f28_ttcf_311_klinger_bearish_cross_indicator_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_311_klinger_bearish_cross_indicator_d3}, 'f28_ttcf_312_klinger_above_zero_state_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_312_klinger_above_zero_state_d3}, 'f28_ttcf_313_klinger_div_vs_price_63_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_313_klinger_div_vs_price_63_d3}, 'f28_ttcf_314_klinger_zscore_252_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_314_klinger_zscore_252_d3}, 'f28_ttcf_315_klinger_persistence_below_zero_252_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_315_klinger_persistence_below_zero_252_d3}, 'f28_ttcf_316_force_index_5_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_316_force_index_5_d3}, 'f28_ttcf_317_force_index_20_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_317_force_index_20_d3}, 'f28_ttcf_318_force_index_above_zero_state_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_318_force_index_above_zero_state_d3}, 'f28_ttcf_319_force_index_zero_cross_down_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_319_force_index_zero_cross_down_d3}, 'f28_ttcf_320_force_index_div_vs_price_63_d3': {'inputs': ['high', 'close', 'volume'], 'func': f28_ttcf_320_force_index_div_vs_price_63_d3}, 'f28_ttcf_321_force_index_zscore_252_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_321_force_index_zscore_252_d3}, 'f28_ttcf_322_mass_index_25_d3': {'inputs': ['high', 'low'], 'func': f28_ttcf_322_mass_index_25_d3}, 'f28_ttcf_323_mass_index_reversal_bulge_indicator_d3': {'inputs': ['high', 'low'], 'func': f28_ttcf_323_mass_index_reversal_bulge_indicator_d3}, 'f28_ttcf_324_mass_index_above_27_state_d3': {'inputs': ['high', 'low'], 'func': f28_ttcf_324_mass_index_above_27_state_d3}, 'f28_ttcf_325_mass_index_dwell_above_27_63_d3': {'inputs': ['high', 'low'], 'func': f28_ttcf_325_mass_index_dwell_above_27_63_d3}, 'f28_ttcf_326_mass_index_zscore_252_d3': {'inputs': ['high', 'low'], 'func': f28_ttcf_326_mass_index_zscore_252_d3}, 'f28_ttcf_327_choppiness_index_14_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_327_choppiness_index_14_d3}, 'f28_ttcf_328_choppiness_above_61_8_trend_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_328_choppiness_above_61_8_trend_state_d3}, 'f28_ttcf_329_choppiness_below_38_2_trend_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_329_choppiness_below_38_2_trend_state_d3}, 'f28_ttcf_330_choppiness_dwell_above_61_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_330_choppiness_dwell_above_61_63_d3}, 'f28_ttcf_331_choppiness_zscore_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_331_choppiness_zscore_252_d3}, 'f28_ttcf_332_hurst_cycles_dominant_period_252_d3': {'inputs': ['close'], 'func': f28_ttcf_332_hurst_cycles_dominant_period_252_d3}, 'f28_ttcf_333_hurst_cycles_period_zscore_252_d3': {'inputs': ['close'], 'func': f28_ttcf_333_hurst_cycles_period_zscore_252_d3}, 'f28_ttcf_334_hurst_cycles_period_stability_63_d3': {'inputs': ['close'], 'func': f28_ttcf_334_hurst_cycles_period_stability_63_d3}, 'f28_ttcf_335_hurst_cycles_amplitude_decay_63_d3': {'inputs': ['close'], 'func': f28_ttcf_335_hurst_cycles_amplitude_decay_63_d3}, 'f28_ttcf_336_ehlers_sinewave_indicator_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_336_ehlers_sinewave_indicator_proxy_d3}, 'f28_ttcf_337_ehlers_sinewave_lead_cross_down_d3': {'inputs': ['close'], 'func': f28_ttcf_337_ehlers_sinewave_lead_cross_down_d3}, 'f28_ttcf_338_ehlers_even_better_sinewave_d3': {'inputs': ['close'], 'func': f28_ttcf_338_ehlers_even_better_sinewave_d3}, 'f28_ttcf_339_ehlers_stochastic_cyber_cycle_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_339_ehlers_stochastic_cyber_cycle_proxy_d3}, 'f28_ttcf_340_ehlers_snake_indicator_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_340_ehlers_snake_indicator_proxy_d3}, 'f28_ttcf_341_ehlers_adaptive_rsi_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_341_ehlers_adaptive_rsi_proxy_d3}, 'f28_ttcf_342_ehlers_emd_trend_component_proxy_63_d3': {'inputs': ['close'], 'func': f28_ttcf_342_ehlers_emd_trend_component_proxy_63_d3}, 'f28_ttcf_343_ehlers_emd_cycle_component_proxy_63_d3': {'inputs': ['close'], 'func': f28_ttcf_343_ehlers_emd_cycle_component_proxy_63_d3}, 'f28_ttcf_344_ehlers_zero_lag_macd_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_344_ehlers_zero_lag_macd_proxy_d3}, 'f28_ttcf_345_ehlers_predictive_filter_lead_proxy_d3': {'inputs': ['close'], 'func': f28_ttcf_345_ehlers_predictive_filter_lead_proxy_d3}, 'f28_ttcf_346_robust_cci_iqr_20_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_346_robust_cci_iqr_20_d3}, 'f28_ttcf_347_robust_cci_iqr_above_100_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_347_robust_cci_iqr_above_100_state_d3}, 'f28_ttcf_348_trimmed_mean_smoothed_close_distance_21_d3': {'inputs': ['close'], 'func': f28_ttcf_348_trimmed_mean_smoothed_close_distance_21_d3}, 'f28_ttcf_349_quantile_oscillator_q90_q10_band_position_63_d3': {'inputs': ['close'], 'func': f28_ttcf_349_quantile_oscillator_q90_q10_band_position_63_d3}, 'f28_ttcf_350_quantile_oscillator_band_breakout_above_state_d3': {'inputs': ['close'], 'func': f28_ttcf_350_quantile_oscillator_band_breakout_above_state_d3}, 'f28_ttcf_351_winsorized_trix_15_3pct_d3': {'inputs': ['close'], 'func': f28_ttcf_351_winsorized_trix_15_3pct_d3}, 'f28_ttcf_352_winsorized_returns_zscore_63_d3': {'inputs': ['close'], 'func': f28_ttcf_352_winsorized_returns_zscore_63_d3}, 'f28_ttcf_353_median_absolute_deviation_normalized_close_21_d3': {'inputs': ['close'], 'func': f28_ttcf_353_median_absolute_deviation_normalized_close_21_d3}, 'f28_ttcf_354_negative_volume_index_value_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_354_negative_volume_index_value_d3}, 'f28_ttcf_355_negative_volume_index_signal_ema255_below_state_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_355_negative_volume_index_signal_ema255_below_state_d3}, 'f28_ttcf_356_positive_volume_index_value_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_356_positive_volume_index_value_d3}, 'f28_ttcf_357_pvi_signal_ema255_below_state_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_357_pvi_signal_ema255_below_state_d3}, 'f28_ttcf_358_ease_of_movement_14_d3': {'inputs': ['high', 'low', 'volume'], 'func': f28_ttcf_358_ease_of_movement_14_d3}, 'f28_ttcf_359_ease_of_movement_below_zero_state_d3': {'inputs': ['high', 'low', 'volume'], 'func': f28_ttcf_359_ease_of_movement_below_zero_state_d3}, 'f28_ttcf_360_trade_intensity_index_proxy_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_360_trade_intensity_index_proxy_d3}, 'f28_ttcf_361_turnover_velocity_decay_63_d3': {'inputs': ['volume', 'close'], 'func': f28_ttcf_361_turnover_velocity_decay_63_d3}, 'f28_ttcf_362_trix_adaptive_zero_line_504_d3': {'inputs': ['close'], 'func': f28_ttcf_362_trix_adaptive_zero_line_504_d3}, 'f28_ttcf_363_trix_above_adaptive_zero_state_d3': {'inputs': ['close'], 'func': f28_ttcf_363_trix_above_adaptive_zero_state_d3}, 'f28_ttcf_364_tsi_adaptive_ob_threshold_q90_504_d3': {'inputs': ['close'], 'func': f28_ttcf_364_tsi_adaptive_ob_threshold_q90_504_d3}, 'f28_ttcf_365_tsi_above_adaptive_ob_state_d3': {'inputs': ['close'], 'func': f28_ttcf_365_tsi_above_adaptive_ob_state_d3}, 'f28_ttcf_366_cci_adaptive_ob_threshold_q90_504_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_366_cci_adaptive_ob_threshold_q90_504_d3}, 'f28_ttcf_367_cci_above_adaptive_ob_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_367_cci_above_adaptive_ob_state_d3}, 'f28_ttcf_368_cmo_adaptive_ob_threshold_q90_504_d3': {'inputs': ['close'], 'func': f28_ttcf_368_cmo_adaptive_ob_threshold_q90_504_d3}, 'f28_ttcf_369_cmo_above_adaptive_ob_state_d3': {'inputs': ['close'], 'func': f28_ttcf_369_cmo_above_adaptive_ob_state_d3}, 'f28_ttcf_370_dpo_adaptive_above_zero_state_d3': {'inputs': ['close'], 'func': f28_ttcf_370_dpo_adaptive_above_zero_state_d3}, 'f28_ttcf_371_kst_adaptive_above_zero_state_d3': {'inputs': ['close'], 'func': f28_ttcf_371_kst_adaptive_above_zero_state_d3}, 'f28_ttcf_372_oscillator_basket_adaptive_consensus_count_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_372_oscillator_basket_adaptive_consensus_count_d3}, 'f28_ttcf_373_oscillator_basket_adaptive_extreme_count_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_373_oscillator_basket_adaptive_extreme_count_252_d3}, 'f28_ttcf_374_vol_regime_adaptive_oscillator_consensus_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_374_vol_regime_adaptive_oscillator_consensus_d3}, 'f28_ttcf_375_trend_regime_adaptive_oscillator_consensus_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_375_trend_regime_adaptive_oscillator_consensus_d3}}