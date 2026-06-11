"""27_macd_topping_dynamics d3 features 526-600 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260
_BFS = [(5, 35), (12, 26), (19, 39), (50, 200)]

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

def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return (ppo, sig, histo)

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

def _roll_spread(close, n=MDAYS):
    """Roll's effective-spread proxy: 2*sqrt(-cov(dp_t, dp_{t-1})) over n bars."""
    dp = close.diff()
    cov = dp.rolling(n, min_periods=max(n // 3, 2)).apply(lambda w: float(np.cov(w[1:], w[:-1])[0, 1]) if w.size > 2 else np.nan, raw=True)
    sp = 2.0 * np.sqrt((-cov).clip(lower=0.0))
    return sp

def _amihud_illiq(close, volume, n=MDAYS):
    r = close.pct_change().abs()
    dv = (close * volume).replace(0, np.nan)
    raw = _safe_div(r, dv) * 1000000.0
    return raw.rolling(n, min_periods=max(n // 3, 2)).mean()

def _dominant_period_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    sd = v0.std()
    if sd <= 0:
        return np.nan
    best_lag = 0
    best_ac = 0.0
    for lag in range(2, min(nn // 2, MDAYS * 2)):
        a = v0[:-lag]
        b = v0[lag:]
        ac = float((a * b).mean() / (sd * sd))
        if ac > best_ac:
            best_ac = ac
            best_lag = lag
    return float(best_lag) if best_lag > 0 else np.nan

def _cycle_amplitude_window(w):
    v = w[~np.isnan(w)]
    if v.size < MDAYS:
        return np.nan
    v0 = v - v.mean()
    F = np.fft.rfft(v0)
    P = np.abs(F)
    if P.size < 2:
        return np.nan
    return float(P[1:].max())

def _spectral_entropy_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    F = np.fft.rfft(v0)
    P = (np.abs(F) ** 2)[1:]
    if P.sum() <= 0:
        return np.nan
    p = P / P.sum()
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())

def _spectral_flatness_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    P = (np.abs(np.fft.rfft(v0)) ** 2)[1:]
    P = P[P > 0]
    if P.size == 0:
        return np.nan
    gm = float(np.exp(np.log(P).mean()))
    am = float(P.mean())
    if am <= 0:
        return np.nan
    return gm / am

def _power_in_band_window(w, lo_period, hi_period):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    P = np.abs(np.fft.rfft(v0)) ** 2
    freqs = np.fft.rfftfreq(nn, d=1.0)
    band = (freqs > 1.0 / hi_period) & (freqs <= 1.0 / lo_period)
    if not band.any():
        return np.nan
    if P.sum() <= 0:
        return np.nan
    return float(P[band].sum() / P.sum())

def _frequency_centroid_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    P = (np.abs(np.fft.rfft(v0)) ** 2)[1:]
    freqs = np.fft.rfftfreq(nn, d=1.0)[1:]
    if P.sum() <= 0:
        return np.nan
    return float((freqs * P).sum() / P.sum())

def _spectral_skewness_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    P = (np.abs(np.fft.rfft(v0)) ** 2)[1:]
    freqs = np.fft.rfftfreq(nn, d=1.0)[1:]
    if P.sum() <= 0:
        return np.nan
    p = P / P.sum()
    mu = (freqs * p).sum()
    sd = np.sqrt(((freqs - mu) ** 2 * p).sum())
    if sd <= 0:
        return np.nan
    return float((((freqs - mu) / sd) ** 3 * p).sum())

def _spectral_kurtosis_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    P = (np.abs(np.fft.rfft(v0)) ** 2)[1:]
    freqs = np.fft.rfftfreq(nn, d=1.0)[1:]
    if P.sum() <= 0:
        return np.nan
    p = P / P.sum()
    mu = (freqs * p).sum()
    sd = np.sqrt(((freqs - mu) ** 2 * p).sum())
    if sd <= 0:
        return np.nan
    return float((((freqs - mu) / sd) ** 4 * p).sum() - 3.0)

def _local_extrema(v, k=3):
    """Return (peaks_idx, troughs_idx) using k-bar pivot definition."""
    nn = v.size
    peaks, troughs = ([], [])
    for i in range(k, nn - k):
        seg = v[i - k:i + k + 1]
        if v[i] == seg.max() and seg.argmax() == k:
            peaks.append(i)
        if v[i] == seg.min() and seg.argmin() == k:
            troughs.append(i)
    return (peaks, troughs)

def _three_drives_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    peaks, _ = _local_extrema(v, k=2)
    if len(peaks) < 3:
        return 0.0
    p1, p2, p3 = (peaks[-3], peaks[-2], peaks[-1])
    a, b, c = (v[p1], v[p2], v[p3])
    if a < b < c:
        return 1.0
    return 0.0

def _harmonic_ratio_window(w, lo, hi):
    """Generic harmonic: 4 points (X-A-B-C), checks if retracement ratio of B-from-A lies in [lo, hi]."""
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    peaks, troughs = _local_extrema(v, k=2)
    pts = sorted(peaks + troughs)
    if len(pts) < 4:
        return 0.0
    X, A, B, C = pts[-4:]
    xa = abs(v[A] - v[X])
    ab = abs(v[B] - v[A])
    if xa <= 0:
        return 0.0
    r = ab / xa
    if lo <= r <= hi:
        return 1.0
    return 0.0

def _ab_cd_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    peaks, troughs = _local_extrema(v, k=2)
    pts = sorted(peaks + troughs)
    if len(pts) < 4:
        return 0.0
    A, B, C, D = pts[-4:]
    ab = abs(v[B] - v[A])
    cd = abs(v[D] - v[C])
    if ab <= 0:
        return 0.0
    r = cd / ab
    if 0.9 <= r <= 1.1:
        return 1.0
    return 0.0

def _wolfe_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    peaks, troughs = _local_extrema(v, k=2)
    if len(peaks) < 3 or len(troughs) < 2:
        return 0.0
    p = peaks[-3:]
    t = troughs[-2:]
    if v[p[0]] < v[p[1]] < v[p[2]] and v[t[0]] < v[t[1]]:
        return 1.0
    return 0.0

def _quintuple_top_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    peaks, _ = _local_extrema(v, k=2)
    if len(peaks) < 5:
        return 0.0
    p5 = peaks[-5:]
    vals = np.array([v[i] for i in p5])
    rng = vals.max() - vals.min()
    if vals.mean() == 0:
        return 0.0
    if rng / abs(vals.mean() + 1e-12) < 0.1:
        return 1.0
    return 0.0

def _rounded_top_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    x = np.arange(nn, dtype=float)
    if nn < 5:
        return 0.0
    coef = np.polyfit(x, v, 2)
    a = coef[0]
    fit_quality = 1.0 - np.var(v - np.polyval(coef, x)) / (np.var(v) + 1e-12)
    if a < 0 and fit_quality > 0.7:
        return 1.0
    return 0.0

def _hurst_rs_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 32:
        return np.nan
    m0 = v.mean()
    y = np.cumsum(v - m0)
    R = y.max() - y.min()
    S = v.std()
    if S <= 0 or R <= 0:
        return np.nan
    return float(np.log(R / S) / np.log(nn))

def _hurst_dfa_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 32:
        return np.nan
    y = np.cumsum(v - v.mean())
    scales = [4, 8, 16, 32, 64]
    F = []
    sc_used = []
    for s in scales:
        if nn < s * 2:
            continue
        segs = nn // s
        f_s = []
        for i in range(segs):
            seg = y[i * s:(i + 1) * s]
            x = np.arange(s, dtype=float)
            p = np.polyfit(x, seg, 1)
            fit = np.polyval(p, x)
            f_s.append(np.sqrt(((seg - fit) ** 2).mean()))
        if f_s:
            F.append(np.mean(f_s))
            sc_used.append(s)
    if len(F) < 2:
        return np.nan
    return float(np.polyfit(np.log(np.array(sc_used, dtype=float)), np.log(F), 1)[0])

def _acf_integral_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    sd = v0.std()
    if sd <= 0:
        return np.nan
    acs = []
    for lag in range(1, min(MDAYS, nn // 2)):
        a = v0[:-lag]
        b = v0[lag:]
        acs.append(float((a * b).mean() / (sd * sd)))
    return float(np.sum(np.abs(acs)))

def _max_acf_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    sd = v0.std()
    if sd <= 0:
        return np.nan
    best = 0.0
    for lag in range(1, min(MDAYS, nn // 2)):
        a = v0[:-lag]
        b = v0[lag:]
        c = abs(float((a * b).mean() / (sd * sd)))
        if c > best:
            best = c
    return best

def _half_life_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    sd = v0.std()
    if sd <= 0:
        return np.nan
    for lag in range(1, min(MDAYS, nn // 2)):
        a = v0[:-lag]
        b = v0[lag:]
        c = float((a * b).mean() / (sd * sd))
        if c < 0.5:
            return float(lag)
    return float(min(MDAYS, nn // 2))

def _acf_decay_rate_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    v0 = v - v.mean()
    sd = v0.std()
    if sd <= 0:
        return np.nan
    lags = list(range(1, min(MDAYS, nn // 2)))
    acs = []
    for lag in lags:
        a = v0[:-lag]
        b = v0[lag:]
        acs.append(float((a * b).mean() / (sd * sd)))
    acs = np.array(acs)
    if (acs <= 0).all() or (acs > 0).sum() < 3:
        return np.nan
    pos = acs > 0
    return float(np.polyfit(np.array(lags)[pos], np.log(acs[pos] + 1e-12), 1)[0])

def _arfima_d_proxy_window(w):
    h = _hurst_dfa_window(w)
    if h is None or np.isnan(h):
        return np.nan
    return float(h - 0.5)

def _multi_scale_hurst_stability_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 64:
        return np.nan
    h1 = _hurst_rs_window(v[:nn // 2])
    h2 = _hurst_rs_window(v[nn // 2:])
    if np.isnan(h1) or np.isnan(h2):
        return np.nan
    return float(abs(h1 - h2))

def _h_orthogonal_score(close):
    m, _, h = _macd(close)
    z_m = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    z_h = _rolling_zscore(h, YDAYS, min_periods=QDAYS)
    sl = _rolling_slope(m, MDAYS)
    z_sl = _rolling_zscore(sl, YDAYS, min_periods=QDAYS)
    return ((-z_m).fillna(0) + (-z_h).fillna(0) + (-z_sl).fillna(0)) / 3.0

def _h_basket_zscore_max(close):
    zs = []
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    return pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).max(axis=1)

def _h_basket_zscore_avg(close):
    zs = []
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    return pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).mean(axis=1)

def _h_basket_blowoff_count(close):
    cnt = pd.Series(0.0, index=close.index)
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        rmax = mm.rolling(YDAYS, min_periods=QDAYS).max()
        bs = _bars_since_true(mm == rmax)
        drop = rmax - mm > 0.5 * rmax.abs()
        cnt = cnt + ((bs <= QDAYS) & drop).astype(float).fillna(0)
    return cnt

def _h_chronic_neg(close):
    m, _, _ = _macd(close)
    return (m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()

def _h_terminal_bool(high, close):
    m, _, h = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = at_252h.rolling(126, min_periods=MDAYS).sum() > 0
    histo_neg = (h < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum() > 40
    return (m < 0) & (sl < 0) & recent_peak & histo_neg

def _h_distribution_score(close):
    m, _, h = _macd(close)
    sd = m.rolling(MDAYS, min_periods=WDAYS).std()
    near = (m.abs() < 0.5 * sd).astype(float)
    rmax21 = m.rolling(MDAYS, min_periods=WDAYS).max()
    decl = (rmax21 < rmax21.shift(QDAYS)).astype(float)
    return (near + decl).fillna(0)

def _h_breakdown_score(close):
    m, _, h = _macd(close)
    return ((m < 0).astype(float) + (h < 0).astype(float) + (_rolling_slope(m, MDAYS) < 0).astype(float)).fillna(0)

def _h_blowoff_collapse_score(close):
    parts = []
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        rmax = mm.rolling(YDAYS, min_periods=QDAYS).max()
        decay = (rmax - mm) / rmax.abs().replace(0, np.nan)
        parts.append(decay.fillna(0))
    return sum(parts) / float(len(parts))

def _h_cycle_phase_label(close):
    """Returns categorical 0-4 phase label per bar:
    0=early (close < SMA200, slope+); 1=mid (close > SMA200, slope+); 2=late (close > SMA200, slope-);
    3=distribution (close ~ SMA200 plateau); 4=markdown (close < SMA200, slope-).
    """
    sma200 = close.rolling(200, min_periods=50).mean()
    sl = _rolling_slope(close, MDAYS)
    above = close > sma200
    pos_sl = sl > 0
    out = pd.Series(np.nan, index=close.index)
    out = out.where(~(~above & pos_sl), 0)
    out = out.where(~(above & pos_sl), 1)
    out = out.where(~(above & ~pos_sl), 2)
    out = out.where(~(~above & ~pos_sl), 4)
    near = (close - sma200).abs() / sma200.abs().replace(0, np.nan) < 0.03
    out = out.where(~near, 3)
    return out

def f27_mcdt_526_spread_adjusted_macd_12_26_d3(close: pd.Series) -> pd.Series:
    """MACD / Roll-spread proxy (21d) — spread-normalized momentum."""
    m, _, _ = _macd(close)
    sp = _roll_spread(close, MDAYS)
    return _safe_div(m, sp).diff().diff().diff()

def f27_mcdt_527_volume_density_normalized_macd_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD divided by 21d avg dollar-volume rolling rank — density-normalized."""
    m, _, _ = _macd(close)
    dv = close * volume
    vr = dv.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    return _safe_div(m, vr.replace(0, np.nan)).diff().diff().diff()

def f27_mcdt_528_trade_intensity_weighted_macd_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD weighted by trade intensity = volume / (high-low+eps), rolling-mean over 21d, then scale MACD."""
    m, _, _ = _macd(close)
    rng = (high - low).replace(0, np.nan)
    ti = _safe_div(volume, rng)
    ti_avg = ti.rolling(MDAYS, min_periods=WDAYS).mean()
    w_t = ti_avg.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    return (m * w_t).diff().diff().diff()

def f27_mcdt_529_liquidity_weighted_macd_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD weighted by 1 / Amihud illiquidity 21d — high-liquidity MACD scaled up."""
    m, _, _ = _macd(close)
    illiq = _amihud_illiq(close, volume, MDAYS)
    liq = _safe_div(1.0, illiq)
    liq_rank = liq.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    return (m * liq_rank).diff().diff().diff()

def f27_mcdt_530_spread_conditional_macd_above_q70_state_d3(close: pd.Series) -> pd.Series:
    """1 if MACD<0 AND 21d Roll spread > its 252d 70th percentile — stress-state MACD."""
    m, _, _ = _macd(close)
    sp = _roll_spread(close, MDAYS)
    q70 = sp.rolling(YDAYS, min_periods=QDAYS).quantile(0.7)
    return ((m < 0) & (sp > q70)).astype(float).where(m.notna() & sp.notna(), np.nan).diff().diff().diff()

def f27_mcdt_531_microstructure_noise_filtered_macd_5_21_d3(close: pd.Series) -> pd.Series:
    """MACD computed on a 5d EMA of close (noise filter): EMA12(EMA5(close)) - EMA26(EMA5(close))."""
    smoothed = _ema(close, 5)
    return (_ema(smoothed, 12) - _ema(smoothed, 26)).diff().diff().diff()

def f27_mcdt_532_effective_tick_adjusted_macd_d3(close: pd.Series) -> pd.Series:
    """MACD divided by 21d median |close.diff()| — effective-tick scale normalizer."""
    m, _, _ = _macd(close)
    tick = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(m, tick).diff().diff().diff()

def f27_mcdt_533_vwap_distance_weighted_macd_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD * |close - VWAP21| / close — emphasizes MACD when price diverges from VWAP."""
    m, _, _ = _macd(close)
    tp = (high + low + close) / 3.0
    pv = tp * volume
    vwap = pv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    d = (close - vwap).abs() / close.replace(0, np.nan)
    return (m * d).diff().diff().diff()

def f27_mcdt_534_high_low_impact_normalized_macd_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MACD / 21d avg (high-low)/close — range-impact normalized."""
    m, _, _ = _macd(close)
    imp = ((high - low) / close.replace(0, np.nan)).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(m, imp).diff().diff().diff()

def f27_mcdt_535_microstructure_regime_conditional_macd_avg_d3(close: pd.Series) -> pd.Series:
    """Average MACD over 63d conditioned on Roll-spread regime being in top 252d-quartile (stressed)."""
    m, _, _ = _macd(close)
    sp = _roll_spread(close, MDAYS)
    q75 = sp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    cond = sp > q75
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f27_mcdt_536_dominant_period_of_macd_in_63_d3(close: pd.Series) -> pd.Series:
    """63d dominant period of MACD via autocorrelation peak."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_dominant_period_window, raw=True).diff().diff().diff()

def f27_mcdt_537_cycle_amplitude_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d cycle amplitude of MACD = max FFT magnitude excluding DC."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_cycle_amplitude_window, raw=True).diff().diff().diff()

def f27_mcdt_538_spectral_entropy_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d spectral entropy of MACD's power spectrum."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_spectral_entropy_window, raw=True).diff().diff().diff()

def f27_mcdt_539_spectral_flatness_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d spectral flatness (geometric mean / arithmetic mean of power) of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_spectral_flatness_window, raw=True).diff().diff().diff()

def f27_mcdt_540_power_in_5_to_21_band_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d fractional power in the period-band 5-21 bars of MACD spectrum."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _power_in_band_window(w, 5.0, 21.0)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_541_power_in_21_to_63_band_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d fractional power in the period-band 21-63 bars of MACD spectrum."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _power_in_band_window(w, 21.0, 63.0)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_542_power_ratio_short_long_band_macd_63_d3(close: pd.Series) -> pd.Series:
    """Ratio of 5-21 power to 21-63 power in 63d MACD spectrum — short-vs-long-cycle dominance."""
    m, _, _ = _macd(close)

    def _fs(w):
        return _power_in_band_window(w, 5.0, 21.0)

    def _fl(w):
        return _power_in_band_window(w, 21.0, 63.0)
    s = m.rolling(QDAYS, min_periods=MDAYS).apply(_fs, raw=True)
    l = m.rolling(QDAYS, min_periods=MDAYS).apply(_fl, raw=True)
    return _safe_div(s, l).diff().diff().diff()

def f27_mcdt_543_frequency_centroid_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d frequency centroid (power-weighted mean frequency) of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_frequency_centroid_window, raw=True).diff().diff().diff()

def f27_mcdt_544_spectral_skewness_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d skewness of the MACD power spectrum (power-weighted)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_spectral_skewness_window, raw=True).diff().diff().diff()

def f27_mcdt_545_spectral_kurtosis_of_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d excess-kurtosis of MACD power spectrum."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_spectral_kurtosis_window, raw=True).diff().diff().diff()

def f27_mcdt_546_three_drives_pattern_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d three-drives pattern in MACD line (3 successively higher pivot peaks)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_three_drives_window, raw=True).diff().diff().diff()

def f27_mcdt_547_bat_pattern_proxy_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d Bat-pattern proxy: 4-pivot retracement of XA in B at 0.382-0.50."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _harmonic_ratio_window(w, 0.382, 0.5)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_548_gartley_pattern_proxy_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d Gartley-pattern proxy: B retracement of XA in 0.55-0.65 (≈0.618)."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _harmonic_ratio_window(w, 0.55, 0.65)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_549_cypher_pattern_proxy_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d Cypher pattern: B retracement of XA in 0.38-0.62 — broad cypher."""
    m, _, _ = _macd(close)

    def _fn(w):
        return _harmonic_ratio_window(w, 0.38, 0.62)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_550_ab_cd_pattern_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d AB=CD pattern: 4 pivots, |CD| / |AB| in 0.9-1.1."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_ab_cd_window, raw=True).diff().diff().diff()

def f27_mcdt_551_wolfe_wave_pattern_proxy_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d Wolfe wave proxy: ascending peaks + ascending troughs."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_wolfe_window, raw=True).diff().diff().diff()

def f27_mcdt_552_quintuple_top_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d quintuple top in MACD: 5 peaks within 10% range — multi-test exhaustion."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_quintuple_top_window, raw=True).diff().diff().diff()

def f27_mcdt_553_rounded_top_in_macd_63_d3(close: pd.Series) -> pd.Series:
    """63d rounded-top in MACD via concave parabola fit (good R²)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_rounded_top_window, raw=True).diff().diff().diff()

def f27_mcdt_554_macd_descending_channel_break_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD breaks below 63d linear-regression channel lower band (mean - 2*resid_std)."""
    m, _, _ = _macd(close)
    sl = _rolling_slope(m, QDAYS)
    mean = m.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = m.rolling(QDAYS, min_periods=MDAYS).std()
    lower = mean - 2.0 * sd
    return ((m < lower) & (sl < 0)).astype(float).where(m.notna() & sl.notna(), np.nan).diff().diff().diff()

def f27_mcdt_555_macd_inside_day_at_high_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD daily range (max-min over the day proxy: |MACD - MACD.shift(1)|) is contained
    within prior bar's range AND MACD near 252d high — inside-bar at MACD top."""
    m, _, _ = _macd(close)
    today_range = (m - m.shift(1)).abs()
    yesterday_range = (m.shift(1) - m.shift(2)).abs()
    near_max = m >= 0.95 * m.rolling(YDAYS, min_periods=QDAYS).max()
    return ((today_range < yesterday_range) & near_max).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_556_macd_in_early_cycle_phase_avg_252_d3(close: pd.Series) -> pd.Series:
    """252d average MACD when cycle phase = early (0)."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    return m.where(ph == 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f27_mcdt_557_macd_in_mid_cycle_phase_avg_252_d3(close: pd.Series) -> pd.Series:
    """252d average MACD when cycle phase = mid (1)."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    return m.where(ph == 1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f27_mcdt_558_macd_in_late_cycle_phase_avg_252_d3(close: pd.Series) -> pd.Series:
    """252d average MACD when cycle phase = late (2)."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    return m.where(ph == 2, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f27_mcdt_559_macd_in_distribution_phase_avg_252_d3(close: pd.Series) -> pd.Series:
    """252d average MACD when cycle phase = distribution (3)."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    return m.where(ph == 3, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f27_mcdt_560_macd_in_markdown_phase_avg_252_d3(close: pd.Series) -> pd.Series:
    """252d average MACD when cycle phase = markdown (4)."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    return m.where(ph == 4, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f27_mcdt_561_cycle_conditional_macd_zero_line_252_d3(close: pd.Series) -> pd.Series:
    """Fraction of late/distribution/markdown phase bars in 252d with MACD<0 — terminal-zone weakness."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    cond = ph.isin([2, 3, 4])
    neg_in_late = ((m < 0) & cond).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    late_total = cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(neg_in_late, late_total).diff().diff().diff()

def f27_mcdt_562_cycle_conditional_macd_dwell_ratio_252_d3(close: pd.Series) -> pd.Series:
    """Ratio (252d dwell in late/distribution/markdown) / (252d dwell in early/mid)."""
    ph = _h_cycle_phase_label(close)
    late = ph.isin([2, 3, 4]).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    early = ph.isin([0, 1]).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(late, early).diff().diff().diff()

def f27_mcdt_563_cycle_phase_persistence_macd_252_d3(close: pd.Series) -> pd.Series:
    """Mean run-length of same phase label over 252d — phase persistence index."""
    ph = _h_cycle_phase_label(close)
    change = (ph != ph.shift(1)).astype(float)
    n_changes = change.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(float(YDAYS), n_changes).diff().diff().diff()

def f27_mcdt_564_cycle_phase_shift_macd_indicator_252_d3(close: pd.Series) -> pd.Series:
    """1 if dominant cycle phase shifted from {0,1} to {2,3,4} within past 63 bars."""
    ph = _h_cycle_phase_label(close)
    early_recent = ph.isin([0, 1]).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    late_recent = ph.isin([2, 3, 4]).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    shift = (late_recent > early_recent) & (early_recent.shift(QDAYS) > late_recent.shift(QDAYS))
    return shift.astype(float).where(ph.notna(), np.nan).diff().diff().diff()

def f27_mcdt_565_cycle_end_macd_behavior_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if past 21d phase was {2,3,4} AND MACD slope < 0 AND MACD < 0 — cycle-end stuck-state."""
    m, _, _ = _macd(close)
    ph = _h_cycle_phase_label(close)
    late_persist = ph.isin([2, 3, 4]).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 15
    sl = _rolling_slope(m, MDAYS)
    return (late_persist & (sl < 0) & (m < 0)).astype(float).where(m.notna() & sl.notna(), np.nan).diff().diff().diff()

def f27_mcdt_566_macd_hurst_rs_252_d3(close: pd.Series) -> pd.Series:
    """252d R/S Hurst exponent of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_hurst_rs_window, raw=True).diff().diff().diff()

def f27_mcdt_567_macd_hurst_dfa_504_d3(close: pd.Series) -> pd.Series:
    """504d DFA Hurst exponent of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_hurst_dfa_window, raw=True).diff().diff().diff()

def f27_mcdt_568_macd_hurst_dfa_1260_d3(close: pd.Series) -> pd.Series:
    """1260d (5y) DFA Hurst exponent of MACD."""
    m, _, _ = _macd(close)
    return m.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_hurst_dfa_window, raw=True).diff().diff().diff()

def f27_mcdt_569_macd_acf_integral_long_range_252_d3(close: pd.Series) -> pd.Series:
    """252d sum of |autocorrelations| from lag 1 to 21 of MACD — long-range memory integral."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_acf_integral_window, raw=True).diff().diff().diff()

def f27_mcdt_570_macd_lagged_corr_profile_max_lag_63_d3(close: pd.Series) -> pd.Series:
    """63d maximum |autocorrelation| over lags 1..21 of MACD — peak short-term memory."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_max_acf_window, raw=True).diff().diff().diff()

def f27_mcdt_571_macd_memory_half_life_252_d3(close: pd.Series) -> pd.Series:
    """252d lag at which MACD autocorr falls below 0.5 — half-life of memory."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_half_life_window, raw=True).diff().diff().diff()

def f27_mcdt_572_macd_decay_rate_autocorr_63_d3(close: pd.Series) -> pd.Series:
    """63d slope of log(autocorrelation+eps) vs lag — exponential decay rate."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_acf_decay_rate_window, raw=True).diff().diff().diff()

def f27_mcdt_573_macd_arfima_d_proxy_252_d3(close: pd.Series) -> pd.Series:
    """252d fractional-d proxy from Hurst-DFA: d = H - 0.5."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_arfima_d_proxy_window, raw=True).diff().diff().diff()

def f27_mcdt_574_macd_multi_scale_hurst_stability_252_d3(close: pd.Series) -> pd.Series:
    """252d stability: |H(first half) - H(second half)| — non-stationarity of memory."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_multi_scale_hurst_stability_window, raw=True).diff().diff().diff()

def f27_mcdt_575_macd_memory_regime_indicator_252_d3(close: pd.Series) -> pd.Series:
    """1 if 252d Hurst RS of MACD < 0.4 (mean-reverting regime) — anti-persistence flag."""
    m, _, _ = _macd(close)
    h = m.rolling(YDAYS, min_periods=QDAYS).apply(_hurst_rs_window, raw=True)
    return (h < 0.4).astype(float).where(h.notna(), np.nan).diff().diff().diff()

def f27_mcdt_576_macd_key_reversal_day_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD made a new 21d max prior day AND today closes below prior MACD bar — key reversal."""
    m, _, _ = _macd(close)
    rmax21 = m.rolling(MDAYS, min_periods=WDAYS).max()
    new_max_y = m.shift(1) == rmax21.shift(1)
    rev = m < m.shift(1)
    return (new_max_y & rev).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_577_macd_hook_failure_at_top_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD hooked up 2 bars AND immediately turned down 3 bars after near 21d max — hook failure."""
    m, _, _ = _macd(close)
    up_run = (m.diff() > 0) & (m.diff().shift(1) > 0)
    near_max = m.shift(2) >= 0.95 * m.rolling(MDAYS, min_periods=WDAYS).max().shift(2)
    dn_run = (m.diff() < 0) & (m.diff().shift(1) < 0) & (m.diff().shift(2) < 0)
    return (up_run.shift(3) & near_max & dn_run).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_578_macd_cookie_cutter_setup_indicator_d3(close: pd.Series) -> pd.Series:
    """Cookie-cutter: MACD made tight range (21d std < 252d 10%-tile) AND just broke down (1d return MACD < -1 std)."""
    m, _, _ = _macd(close)
    sd21 = m.rolling(MDAYS, min_periods=WDAYS).std()
    q10 = sd21.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    tight = sd21 < q10
    sd252 = m.rolling(YDAYS, min_periods=QDAYS).std()
    brk = m.diff() < -1.0 * sd252
    return (tight.shift(1) & brk).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_579_macd_bowl_pattern_detection_63_d3(close: pd.Series) -> pd.Series:
    """63d bowl (rounded-bottom-then-fail): convex parabola fit with R²>0.6 but recent 21d slope<0."""
    m, _, _ = _macd(close)

    def _fn(w):
        v = w[~np.isnan(w)]
        nn = v.size
        if nn < MDAYS:
            return np.nan
        x = np.arange(nn, dtype=float)
        coef = np.polyfit(x, v, 2)
        fit_quality = 1.0 - np.var(v - np.polyval(coef, x)) / (np.var(v) + 1e-12)
        if coef[0] > 0 and fit_quality > 0.6:
            recent = v[-WDAYS:]
            if recent.size >= 2 and recent[-1] < recent[0]:
                return 1.0
        return 0.0
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_580_macd_cup_with_handle_failure_63_d3(close: pd.Series) -> pd.Series:
    """Cup-with-handle FAILURE: MACD formed a U then a small consolidation, but broke down rather than up."""
    m, _, _ = _macd(close)

    def _fn(w):
        v = w[~np.isnan(w)]
        nn = v.size
        if nn < MDAYS * 2:
            return np.nan
        body = v[:2 * nn // 3]
        handle = v[2 * nn // 3:]
        if body.size < 5 or handle.size < 3:
            return 0.0
        u_shape = body[0] > body[body.size // 2] and body[-1] > body[body.size // 2]
        handle_break = handle[-1] < handle[0]
        if u_shape and handle_break:
            return 1.0
        return 0.0
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_fn, raw=True).diff().diff().diff()

def f27_mcdt_581_macd_knife_edge_break_indicator_d3(close: pd.Series) -> pd.Series:
    """Knife-edge: MACD makes a >2 std move down within 1 bar near a 252d high (within last 21 bars)."""
    m, _, _ = _macd(close)
    sd252 = m.rolling(YDAYS, min_periods=QDAYS).std()
    big_drop = m.diff() < -2.0 * sd252
    near_max = m.shift(1) >= 0.95 * m.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    return (big_drop & near_max).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_582_macd_extension_then_failure_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD reached 252d 95th percentile within past 21 bars AND now is below 50th percentile."""
    m, _, _ = _macd(close)
    q95 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    q50 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    reached = (m >= q95).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    now_below = m < q50
    return (reached.shift(1) & now_below).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_583_macd_multi_bar_reversal_pattern_indicator_d3(close: pd.Series) -> pd.Series:
    """Multi-bar reversal: 3 up bars followed by 3 down bars, with cumulative down > cumulative up."""
    m, _, _ = _macd(close)
    d = m.diff()
    up3 = (d.shift(3) > 0) & (d.shift(4) > 0) & (d.shift(5) > 0)
    dn3 = (d > 0) & (d.shift(1) < 0) & (d.shift(2) < 0)
    cum_up = d.shift(3).fillna(0) + d.shift(4).fillna(0) + d.shift(5).fillna(0)
    cum_dn = d.fillna(0) + d.shift(1).fillna(0) + d.shift(2).fillna(0)
    return (up3 & dn3 & (cum_dn.abs() > cum_up)).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_584_macd_outside_day_at_high_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if today's MACD range (|MACD - MACD.shift(1)|) engulfs prior 2-bar range AND MACD near 252d max."""
    m, _, _ = _macd(close)
    today_range = (m - m.shift(2)).abs()
    yesterday_range = (m.shift(1) - m.shift(2)).abs()
    near_max = m.shift(1) >= 0.95 * m.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    return ((today_range > yesterday_range) & near_max & (m < m.shift(1))).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_585_macd_reversal_day_at_extreme_indicator_d3(close: pd.Series) -> pd.Series:
    """1 if MACD is at 252d top decile (>q90) AND today closed below prior MACD bar by > 1 std (252d std)."""
    m, _, _ = _macd(close)
    q90 = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    sd = m.rolling(YDAYS, min_periods=QDAYS).std()
    at_top = m.shift(1) > q90.shift(1)
    drop = m - m.shift(1) < -sd
    return (at_top & drop).astype(float).where(m.notna(), np.nan).diff().diff().diff()

def f27_mcdt_586_batch_4_macd_modern_aggregate_zscore_252_d3(close: pd.Series) -> pd.Series:
    """252d z-score of (basket-z-avg + orthogonal-score + breakdown-score)/3."""
    a = _h_basket_zscore_avg(close).fillna(0)
    b = _h_orthogonal_score(close).fillna(0)
    c = _h_breakdown_score(close)
    agg = (a + b + c) / 3.0
    return _rolling_zscore(agg, YDAYS, min_periods=QDAYS).diff().diff().diff()

def f27_mcdt_587_macd_universe_wide_topping_auc_optimized_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """AUC-optimized topping score: sum of {basket-z-max>1.5, breakdown-score>=2, terminal-bool, chronic-neg>0.5}."""
    a = (_h_basket_zscore_max(close) > 1.5).astype(float).fillna(0)
    b = (_h_breakdown_score(close) >= 2).astype(float).fillna(0)
    c = _h_terminal_bool(high, close).astype(float).fillna(0)
    d = (_h_chronic_neg(close) > 0.5).astype(float).fillna(0)
    return (a + b + c + d).diff().diff().diff()

def f27_mcdt_588_macd_universe_wide_stuck_prediction_v4_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck prediction v4: weighted combination of basket-z-max, blowoff count, chronic-neg, terminal-bool."""
    z = _h_basket_zscore_max(close).fillna(0).clip(-3, 3)
    bo = _h_basket_blowoff_count(close).fillna(0)
    cn = _h_chronic_neg(close).fillna(0)
    tb = _h_terminal_bool(high, close).astype(float).fillna(0)
    return (0.35 * (z / 3.0) + 0.25 * (bo / 4.0) + 0.25 * cn + 0.15 * tb).diff().diff().diff()

def f27_mcdt_589_macd_cross_batch_consensus_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Alignment between batch-1-style aggregate (orthogonal-score) and batch-4-style aggregate (modern-aggregate).
    Range: positive when both agree on weakness."""
    s1 = _h_orthogonal_score(close).fillna(0)
    a = _h_basket_zscore_avg(close).fillna(0)
    b = _h_breakdown_score(close).fillna(0)
    s2 = (a + b) / 2.0
    return ((s1 + s2) / 2.0).diff().diff().diff()

def f27_mcdt_590_macd_multi_feature_alignment_score_252_d3(close: pd.Series) -> pd.Series:
    """252d count of bars where MACD-line, MACD-histo, and slope all have the same negative sign."""
    m, _, h = _macd(close)
    sl = _rolling_slope(m, MDAYS)
    all_neg = ((m < 0) & (h < 0) & (sl < 0)).astype(float)
    return all_neg.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f27_mcdt_591_macd_orthogonal_batch_4_aggregate_d3(close: pd.Series) -> pd.Series:
    """Batch-4 orthogonal aggregate: 252d rolling sum of orthogonal-score."""
    s = _h_orthogonal_score(close).fillna(0)
    return s.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f27_mcdt_592_macd_cross_pattern_terminal_v4_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal v4 cross-pattern: terminal-bool AND blowoff-count>=2 AND chronic-neg>0.5."""
    a = _h_terminal_bool(high, close)
    b = _h_basket_blowoff_count(close) >= 2
    c = _h_chronic_neg(close) > 0.5
    return (a & b & c).astype(float).diff().diff().diff()

def f27_mcdt_593_macd_multi_resolution_stuck_v4_score_d3(close: pd.Series) -> pd.Series:
    """Multi-resolution stuck v4: weighted sum of MACD z-scores at 63d/252d/504d windows."""
    m, _, _ = _macd(close)
    z63 = _rolling_zscore(m, QDAYS, min_periods=MDAYS).fillna(0).clip(-3, 3)
    z252 = _rolling_zscore(m, YDAYS, min_periods=QDAYS).fillna(0).clip(-3, 3)
    z504 = _rolling_zscore(m, DDAYS_2Y, min_periods=YDAYS).fillna(0).clip(-3, 3)
    return (-(0.2 * z63 + 0.4 * z252 + 0.4 * z504)).diff().diff().diff()

def f27_mcdt_594_macd_final_topping_master_v4_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Final topping master v4: at 252d-high bars, sum of {basket-z-max>1.5, blowoff>=2, terminal, chronic-neg>0.5,
    distribution-score>=1}."""
    m, _, _ = _macd(close)
    at_max = close == close.rolling(YDAYS, min_periods=QDAYS).max()
    a = (_h_basket_zscore_max(close) > 1.5).astype(float).fillna(0)
    b = (_h_basket_blowoff_count(close) >= 2).astype(float).fillna(0)
    c = _h_terminal_bool(high, close).astype(float).fillna(0)
    d = (_h_chronic_neg(close) > 0.5).astype(float).fillna(0)
    e = (_h_distribution_score(close) >= 1).astype(float).fillna(0)
    return (a + b + c + d + e).where(at_max, np.nan).diff().diff().diff()

def f27_mcdt_595_macd_final_breakdown_master_v4_score_d3(close: pd.Series) -> pd.Series:
    """Final breakdown master v4: breakdown-score (m<0 + h<0 + slope<0) + (chronic-neg>0.6) + (basket-z-avg<-1)."""
    a = _h_breakdown_score(close)
    b = (_h_chronic_neg(close) > 0.6).astype(float).fillna(0)
    c = (_h_basket_zscore_avg(close) < -1.0).astype(float).fillna(0)
    return (a + b + c).diff().diff().diff()

def f27_mcdt_596_macd_final_blowoff_collapse_master_v4_score_d3(close: pd.Series) -> pd.Series:
    """Final blowoff-collapse master v4: blowoff-collapse-score (avg decay) * basket-blowoff-count."""
    a = _h_blowoff_collapse_score(close).fillna(0)
    b = _h_basket_blowoff_count(close).fillna(0)
    return (a * b).diff().diff().diff()

def f27_mcdt_597_macd_final_distribution_master_v4_score_d3(close: pd.Series) -> pd.Series:
    """Final distribution master v4: distribution-score + (chronic-neg>0.4) + (orthogonal-score>0.5)."""
    a = _h_distribution_score(close)
    b = (_h_chronic_neg(close) > 0.4).astype(float).fillna(0)
    c = (_h_orthogonal_score(close) > 0.5).astype(float).fillna(0)
    return (a + b + c).diff().diff().diff()

def f27_mcdt_598_macd_stuck_probability_proxy_v4_score_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck probability v4: weighted sum normalized to (0,1) of {chronic-neg, blowoff/4,
    terminal-bool, breakdown-score/3, basket-z-max<-1.5}."""
    a = _h_chronic_neg(close).fillna(0)
    b = (_h_basket_blowoff_count(close) / 4.0).fillna(0)
    c = _h_terminal_bool(high, close).astype(float).fillna(0)
    d = (_h_breakdown_score(close) / 3.0).fillna(0)
    e = (_h_basket_zscore_max(close) < -1.5).astype(float).fillna(0)
    raw = 0.25 * a + 0.2 * b + 0.2 * c + 0.2 * d + 0.15 * e
    return raw.clip(0.0, 1.0).diff().diff().diff()

def f27_mcdt_599_absolute_terminal_macd_master_v4_indicator_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute terminal master v4: 1 only when ALL of {terminal-bool, blowoff>=3, chronic-neg>0.55,
    breakdown-score==3, basket-z-max<-1.0}."""
    a = _h_terminal_bool(high, close)
    b = _h_basket_blowoff_count(close) >= 3
    c = _h_chronic_neg(close) > 0.55
    d = _h_breakdown_score(close) == 3
    e = _h_basket_zscore_max(close) < -1.0
    return (a & b & c & d & e).astype(float).diff().diff().diff()

def f27_mcdt_600_macd_extended_universe_v4_aggregate_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended universe v4 aggregate: weighted blend across all batch-4 master scores."""
    m, _, h = _macd(close)
    sg = _ema(m, 9)
    d = m - sg
    cross = (d.shift(1) > 0) & (d <= 0)
    va = volume.rolling(50, min_periods=10).mean().shift(1)
    vcc = (cross & (volume > 1.3 * va)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    s1 = _h_breakdown_score(close).fillna(0)
    s2 = _h_chronic_neg(close).fillna(0)
    s3 = _h_basket_blowoff_count(close).fillna(0)
    s4 = _h_distribution_score(close).fillna(0)
    s5 = _h_terminal_bool(high, close).astype(float).fillna(0)
    s6 = vcc.astype(float).fillna(0)
    return (0.2 * s1 + 0.2 * s2 + 0.15 * (s3 / 4.0) + 0.1 * s4 + 0.2 * s5 + 0.15 * s6).diff().diff().diff()
MACD_TOPPING_DYNAMICS_D3_REGISTRY_526_600 = {'f27_mcdt_526_spread_adjusted_macd_12_26_d3': {'inputs': ['close'], 'func': f27_mcdt_526_spread_adjusted_macd_12_26_d3}, 'f27_mcdt_527_volume_density_normalized_macd_d3': {'inputs': ['close', 'volume'], 'func': f27_mcdt_527_volume_density_normalized_macd_d3}, 'f27_mcdt_528_trade_intensity_weighted_macd_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_528_trade_intensity_weighted_macd_d3}, 'f27_mcdt_529_liquidity_weighted_macd_d3': {'inputs': ['close', 'volume'], 'func': f27_mcdt_529_liquidity_weighted_macd_d3}, 'f27_mcdt_530_spread_conditional_macd_above_q70_state_d3': {'inputs': ['close'], 'func': f27_mcdt_530_spread_conditional_macd_above_q70_state_d3}, 'f27_mcdt_531_microstructure_noise_filtered_macd_5_21_d3': {'inputs': ['close'], 'func': f27_mcdt_531_microstructure_noise_filtered_macd_5_21_d3}, 'f27_mcdt_532_effective_tick_adjusted_macd_d3': {'inputs': ['close'], 'func': f27_mcdt_532_effective_tick_adjusted_macd_d3}, 'f27_mcdt_533_vwap_distance_weighted_macd_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f27_mcdt_533_vwap_distance_weighted_macd_d3}, 'f27_mcdt_534_high_low_impact_normalized_macd_d3': {'inputs': ['high', 'low', 'close'], 'func': f27_mcdt_534_high_low_impact_normalized_macd_d3}, 'f27_mcdt_535_microstructure_regime_conditional_macd_avg_d3': {'inputs': ['close'], 'func': f27_mcdt_535_microstructure_regime_conditional_macd_avg_d3}, 'f27_mcdt_536_dominant_period_of_macd_in_63_d3': {'inputs': ['close'], 'func': f27_mcdt_536_dominant_period_of_macd_in_63_d3}, 'f27_mcdt_537_cycle_amplitude_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_537_cycle_amplitude_of_macd_63_d3}, 'f27_mcdt_538_spectral_entropy_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_538_spectral_entropy_of_macd_63_d3}, 'f27_mcdt_539_spectral_flatness_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_539_spectral_flatness_of_macd_63_d3}, 'f27_mcdt_540_power_in_5_to_21_band_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_540_power_in_5_to_21_band_of_macd_63_d3}, 'f27_mcdt_541_power_in_21_to_63_band_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_541_power_in_21_to_63_band_of_macd_63_d3}, 'f27_mcdt_542_power_ratio_short_long_band_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_542_power_ratio_short_long_band_macd_63_d3}, 'f27_mcdt_543_frequency_centroid_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_543_frequency_centroid_of_macd_63_d3}, 'f27_mcdt_544_spectral_skewness_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_544_spectral_skewness_of_macd_63_d3}, 'f27_mcdt_545_spectral_kurtosis_of_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_545_spectral_kurtosis_of_macd_63_d3}, 'f27_mcdt_546_three_drives_pattern_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_546_three_drives_pattern_in_macd_63_d3}, 'f27_mcdt_547_bat_pattern_proxy_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_547_bat_pattern_proxy_in_macd_63_d3}, 'f27_mcdt_548_gartley_pattern_proxy_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_548_gartley_pattern_proxy_in_macd_63_d3}, 'f27_mcdt_549_cypher_pattern_proxy_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_549_cypher_pattern_proxy_in_macd_63_d3}, 'f27_mcdt_550_ab_cd_pattern_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_550_ab_cd_pattern_in_macd_63_d3}, 'f27_mcdt_551_wolfe_wave_pattern_proxy_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_551_wolfe_wave_pattern_proxy_in_macd_63_d3}, 'f27_mcdt_552_quintuple_top_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_552_quintuple_top_in_macd_63_d3}, 'f27_mcdt_553_rounded_top_in_macd_63_d3': {'inputs': ['close'], 'func': f27_mcdt_553_rounded_top_in_macd_63_d3}, 'f27_mcdt_554_macd_descending_channel_break_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_554_macd_descending_channel_break_indicator_d3}, 'f27_mcdt_555_macd_inside_day_at_high_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_555_macd_inside_day_at_high_indicator_d3}, 'f27_mcdt_556_macd_in_early_cycle_phase_avg_252_d3': {'inputs': ['close'], 'func': f27_mcdt_556_macd_in_early_cycle_phase_avg_252_d3}, 'f27_mcdt_557_macd_in_mid_cycle_phase_avg_252_d3': {'inputs': ['close'], 'func': f27_mcdt_557_macd_in_mid_cycle_phase_avg_252_d3}, 'f27_mcdt_558_macd_in_late_cycle_phase_avg_252_d3': {'inputs': ['close'], 'func': f27_mcdt_558_macd_in_late_cycle_phase_avg_252_d3}, 'f27_mcdt_559_macd_in_distribution_phase_avg_252_d3': {'inputs': ['close'], 'func': f27_mcdt_559_macd_in_distribution_phase_avg_252_d3}, 'f27_mcdt_560_macd_in_markdown_phase_avg_252_d3': {'inputs': ['close'], 'func': f27_mcdt_560_macd_in_markdown_phase_avg_252_d3}, 'f27_mcdt_561_cycle_conditional_macd_zero_line_252_d3': {'inputs': ['close'], 'func': f27_mcdt_561_cycle_conditional_macd_zero_line_252_d3}, 'f27_mcdt_562_cycle_conditional_macd_dwell_ratio_252_d3': {'inputs': ['close'], 'func': f27_mcdt_562_cycle_conditional_macd_dwell_ratio_252_d3}, 'f27_mcdt_563_cycle_phase_persistence_macd_252_d3': {'inputs': ['close'], 'func': f27_mcdt_563_cycle_phase_persistence_macd_252_d3}, 'f27_mcdt_564_cycle_phase_shift_macd_indicator_252_d3': {'inputs': ['close'], 'func': f27_mcdt_564_cycle_phase_shift_macd_indicator_252_d3}, 'f27_mcdt_565_cycle_end_macd_behavior_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_565_cycle_end_macd_behavior_indicator_d3}, 'f27_mcdt_566_macd_hurst_rs_252_d3': {'inputs': ['close'], 'func': f27_mcdt_566_macd_hurst_rs_252_d3}, 'f27_mcdt_567_macd_hurst_dfa_504_d3': {'inputs': ['close'], 'func': f27_mcdt_567_macd_hurst_dfa_504_d3}, 'f27_mcdt_568_macd_hurst_dfa_1260_d3': {'inputs': ['close'], 'func': f27_mcdt_568_macd_hurst_dfa_1260_d3}, 'f27_mcdt_569_macd_acf_integral_long_range_252_d3': {'inputs': ['close'], 'func': f27_mcdt_569_macd_acf_integral_long_range_252_d3}, 'f27_mcdt_570_macd_lagged_corr_profile_max_lag_63_d3': {'inputs': ['close'], 'func': f27_mcdt_570_macd_lagged_corr_profile_max_lag_63_d3}, 'f27_mcdt_571_macd_memory_half_life_252_d3': {'inputs': ['close'], 'func': f27_mcdt_571_macd_memory_half_life_252_d3}, 'f27_mcdt_572_macd_decay_rate_autocorr_63_d3': {'inputs': ['close'], 'func': f27_mcdt_572_macd_decay_rate_autocorr_63_d3}, 'f27_mcdt_573_macd_arfima_d_proxy_252_d3': {'inputs': ['close'], 'func': f27_mcdt_573_macd_arfima_d_proxy_252_d3}, 'f27_mcdt_574_macd_multi_scale_hurst_stability_252_d3': {'inputs': ['close'], 'func': f27_mcdt_574_macd_multi_scale_hurst_stability_252_d3}, 'f27_mcdt_575_macd_memory_regime_indicator_252_d3': {'inputs': ['close'], 'func': f27_mcdt_575_macd_memory_regime_indicator_252_d3}, 'f27_mcdt_576_macd_key_reversal_day_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_576_macd_key_reversal_day_indicator_d3}, 'f27_mcdt_577_macd_hook_failure_at_top_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_577_macd_hook_failure_at_top_indicator_d3}, 'f27_mcdt_578_macd_cookie_cutter_setup_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_578_macd_cookie_cutter_setup_indicator_d3}, 'f27_mcdt_579_macd_bowl_pattern_detection_63_d3': {'inputs': ['close'], 'func': f27_mcdt_579_macd_bowl_pattern_detection_63_d3}, 'f27_mcdt_580_macd_cup_with_handle_failure_63_d3': {'inputs': ['close'], 'func': f27_mcdt_580_macd_cup_with_handle_failure_63_d3}, 'f27_mcdt_581_macd_knife_edge_break_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_581_macd_knife_edge_break_indicator_d3}, 'f27_mcdt_582_macd_extension_then_failure_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_582_macd_extension_then_failure_indicator_d3}, 'f27_mcdt_583_macd_multi_bar_reversal_pattern_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_583_macd_multi_bar_reversal_pattern_indicator_d3}, 'f27_mcdt_584_macd_outside_day_at_high_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_584_macd_outside_day_at_high_indicator_d3}, 'f27_mcdt_585_macd_reversal_day_at_extreme_indicator_d3': {'inputs': ['close'], 'func': f27_mcdt_585_macd_reversal_day_at_extreme_indicator_d3}, 'f27_mcdt_586_batch_4_macd_modern_aggregate_zscore_252_d3': {'inputs': ['close'], 'func': f27_mcdt_586_batch_4_macd_modern_aggregate_zscore_252_d3}, 'f27_mcdt_587_macd_universe_wide_topping_auc_optimized_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_587_macd_universe_wide_topping_auc_optimized_score_d3}, 'f27_mcdt_588_macd_universe_wide_stuck_prediction_v4_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_588_macd_universe_wide_stuck_prediction_v4_score_d3}, 'f27_mcdt_589_macd_cross_batch_consensus_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_589_macd_cross_batch_consensus_score_d3}, 'f27_mcdt_590_macd_multi_feature_alignment_score_252_d3': {'inputs': ['close'], 'func': f27_mcdt_590_macd_multi_feature_alignment_score_252_d3}, 'f27_mcdt_591_macd_orthogonal_batch_4_aggregate_d3': {'inputs': ['close'], 'func': f27_mcdt_591_macd_orthogonal_batch_4_aggregate_d3}, 'f27_mcdt_592_macd_cross_pattern_terminal_v4_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_592_macd_cross_pattern_terminal_v4_score_d3}, 'f27_mcdt_593_macd_multi_resolution_stuck_v4_score_d3': {'inputs': ['close'], 'func': f27_mcdt_593_macd_multi_resolution_stuck_v4_score_d3}, 'f27_mcdt_594_macd_final_topping_master_v4_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_594_macd_final_topping_master_v4_score_d3}, 'f27_mcdt_595_macd_final_breakdown_master_v4_score_d3': {'inputs': ['close'], 'func': f27_mcdt_595_macd_final_breakdown_master_v4_score_d3}, 'f27_mcdt_596_macd_final_blowoff_collapse_master_v4_score_d3': {'inputs': ['close'], 'func': f27_mcdt_596_macd_final_blowoff_collapse_master_v4_score_d3}, 'f27_mcdt_597_macd_final_distribution_master_v4_score_d3': {'inputs': ['close'], 'func': f27_mcdt_597_macd_final_distribution_master_v4_score_d3}, 'f27_mcdt_598_macd_stuck_probability_proxy_v4_score_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_598_macd_stuck_probability_proxy_v4_score_d3}, 'f27_mcdt_599_absolute_terminal_macd_master_v4_indicator_d3': {'inputs': ['high', 'close'], 'func': f27_mcdt_599_absolute_terminal_macd_master_v4_indicator_d3}, 'f27_mcdt_600_macd_extended_universe_v4_aggregate_d3': {'inputs': ['high', 'close', 'volume'], 'func': f27_mcdt_600_macd_extended_universe_v4_aggregate_d3}}