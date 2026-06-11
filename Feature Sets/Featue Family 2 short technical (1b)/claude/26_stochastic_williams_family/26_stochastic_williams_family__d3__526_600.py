"""26_stochastic_williams_family d3 features 526-600 — order-3 difference of corresponding base features.

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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()

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

def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k

def _stoch_d(k, n_d):
    return k.rolling(n_d, min_periods=max(n_d // 2, 1)).mean()

def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)

def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_rsi_k(close, n_rsi=14, n_k=14, smooth_k=3):
    r = _rsi(close, n_rsi)
    ll = r.rolling(n_k, min_periods=max(n_k // 3, 2)).min()
    hh = r.rolling(n_k, min_periods=max(n_k // 3, 2)).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    return raw_k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()

def _ultimate_osc(high, low, close):
    bp = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = _true_range(high, low, close)
    a7 = bp.rolling(7, min_periods=3).sum() / tr.rolling(7, min_periods=3).sum().replace(0, np.nan)
    a14 = bp.rolling(14, min_periods=5).sum() / tr.rolling(14, min_periods=5).sum().replace(0, np.nan)
    a28 = bp.rolling(28, min_periods=10).sum() / tr.rolling(28, min_periods=10).sum().replace(0, np.nan)
    return 100.0 * (4 * a7 + 2 * a14 + a28) / 7.0

def _smi_compact(high, low, close, n=14):
    mid = (high.rolling(n, min_periods=max(n // 3, 2)).max() + low.rolling(n, min_periods=max(n // 3, 2)).min()) / 2.0
    diff = close - mid
    hl = high.rolling(n, min_periods=max(n // 3, 2)).max() - low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(_ema(_ema(diff, 3), 3), 0.5 * _ema(_ema(hl, 3), 3))

def _all_oscillators(high, low, close):
    """Return dict of canonical oscillators used across composites."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    sk = _stoch_rsi_k(close, 14, 14, 3)
    uo = _ultimate_osc(high, low, close)
    smi = _smi_compact(high, low, close, 14)
    return {'k': k, 'wr': wr, 'sk': sk, 'uo': uo, 'smi': smi}

def _roll_spread_proxy(close, n=21):
    """Roll spread proxy: 2*sqrt(-cov(dC_t, dC_{t-1})) when negative, else 0."""
    dc = close.diff()
    cov = dc.rolling(n, min_periods=max(n // 3, 2)).cov(dc.shift(1))
    neg = (-cov).clip(lower=0)
    return 2.0 * np.sqrt(neg)

def _amihud(close, volume, n=21):
    """Amihud illiquidity: avg |ret| / dollar volume over n."""
    ret = close.pct_change().abs()
    dv = (close * volume).replace(0, np.nan)
    return (ret / dv).rolling(n, min_periods=max(n // 3, 2)).mean()

def _quantile_rolling(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)

def _vwap_n(close, volume, n):
    pv = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    vv = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(pv, vv)

def _autocorr_rolling(s, n, lag, min_periods=None):
    """Rolling autocorr of s at lag, using window n."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(lambda w: np.corrcoef(w[:-lag], w[lag:])[0, 1] if np.isfinite(w).all() and len(w) > lag + 2 and (np.std(w[:-lag]) > 0) and (np.std(w[lag:]) > 0) else np.nan, raw=True)

def _dominant_period_acf(s, window, lag_lo=5, lag_hi=63):
    """Per-window: argmax_{lag in [lag_lo, lag_hi]} autocorr — proxy for dominant cycle."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < lag_hi + 3:
            return np.nan
        best_lag = np.nan
        best_v = -np.inf
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        for L in range(lag_lo, lag_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            ac = num / denom
            if ac > best_v:
                best_v = ac
                best_lag = float(L)
        return best_lag
    return s.rolling(window, min_periods=max(window // 2, lag_hi + 3)).apply(_fn, raw=True)

def _spectral_band_metrics(s, window, lag_lo=5, lag_hi=63):
    """Per-window: compute simplified spectral metrics using ACF coeffs as proxy.
    Returns dict-like via DataFrame -- here used internally; returns dataframe of metrics."""
    raise NotImplementedError('Use individual helpers; placeholder.')

def _spectral_entropy_acf(s, window, lag_lo=2, lag_hi=63):
    """Spectral entropy proxy = entropy of normalized |ACF|^2 over lag band."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < lag_hi + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        acs = []
        for L in range(lag_lo, lag_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            acs.append((num / denom) ** 2)
        acs = np.asarray(acs)
        s_sum = acs.sum()
        if s_sum <= 0:
            return np.nan
        p = acs / s_sum
        p = p[p > 0]
        return float(-(p * np.log2(p)).sum())
    return s.rolling(window, min_periods=max(window // 2, lag_hi + 3)).apply(_fn, raw=True)

def _spectral_flatness_acf(s, window, lag_lo=2, lag_hi=63):
    """Spectral flatness = geometric_mean / arithmetic_mean of |ACF|^2 weights."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < lag_hi + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        acs = []
        for L in range(lag_lo, lag_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            acs.append((num / denom) ** 2)
        acs = np.asarray(acs)
        acs = acs[acs > 0]
        if acs.size == 0:
            return np.nan
        gm = float(np.exp(np.log(acs).mean()))
        am = float(acs.mean())
        return gm / am if am > 0 else np.nan
    return s.rolling(window, min_periods=max(window // 2, lag_hi + 3)).apply(_fn, raw=True)

def _power_in_band(s, window, band_lo, band_hi):
    """Sum of |ACF|^2 over lag band [band_lo, band_hi]."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < band_hi + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        tot = 0.0
        for L in range(band_lo, band_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            tot += (num / denom) ** 2
        return tot
    return s.rolling(window, min_periods=max(window // 2, band_hi + 3)).apply(_fn, raw=True)

def _freq_centroid_acf(s, window, lag_lo=2, lag_hi=63):
    """Frequency centroid proxy: weighted mean of (1/lag) by |ACF|^2."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < lag_hi + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        wts = []
        freqs = []
        for L in range(lag_lo, lag_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            wts.append((num / denom) ** 2)
            freqs.append(1.0 / float(L))
        wts = np.asarray(wts)
        freqs = np.asarray(freqs)
        s_sum = wts.sum()
        return float((wts * freqs).sum() / s_sum) if s_sum > 0 else np.nan
    return s.rolling(window, min_periods=max(window // 2, lag_hi + 3)).apply(_fn, raw=True)

def _spectral_moment(s, window, order, lag_lo=2, lag_hi=63):
    """Central moment of (1/lag) weighted by |ACF|^2: order 3 = skewness numerator, 4 = kurtosis numerator."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < lag_hi + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        wts = []
        freqs = []
        for L in range(lag_lo, lag_hi + 1):
            num = float((v[:-L] * v[L:]).sum())
            wts.append((num / denom) ** 2)
            freqs.append(1.0 / float(L))
        wts = np.asarray(wts)
        freqs = np.asarray(freqs)
        s_sum = wts.sum()
        if s_sum <= 0:
            return np.nan
        wn = wts / s_sum
        mu = float((wn * freqs).sum())
        var = float((wn * (freqs - mu) ** 2).sum())
        if var <= 0:
            return np.nan
        mn = float((wn * (freqs - mu) ** order).sum())
        return mn / var ** (order / 2.0)
    return s.rolling(window, min_periods=max(window // 2, lag_hi + 3)).apply(_fn, raw=True)

def _rolling_hurst_rs(s, window):
    """Rescaled-range Hurst estimator over rolling window."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < 16:
            return np.nan
        n = len(w)
        m = w.mean()
        z = np.cumsum(w - m)
        R = z.max() - z.min()
        S = w.std()
        if S <= 0 or R <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(n))
    return s.rolling(window, min_periods=max(window // 3, 16)).apply(_fn, raw=True)

def _rolling_hurst_dfa(s, window):
    """DFA Hurst estimator (single-scale-pair simplification): compare RMS at two scales."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < 32:
            return np.nan
        n = len(w)
        m = w.mean()
        z = np.cumsum(w - m)

        def _rms(scale):
            if scale * 2 >= n:
                return np.nan
            nseg = n // scale
            r = 0.0
            cnt = 0
            for j in range(nseg):
                seg = z[j * scale:(j + 1) * scale]
                xs = np.arange(scale, dtype=float)
                xm = xs.mean()
                sm = seg.mean()
                num = ((xs - xm) * (seg - sm)).sum()
                den = ((xs - xm) ** 2).sum()
                if den <= 0:
                    return np.nan
                b = num / den
                a = sm - b * xm
                fit = a + b * xs
                r += ((seg - fit) ** 2).mean()
                cnt += 1
            if cnt == 0:
                return np.nan
            return float(np.sqrt(r / cnt))
        s1 = 8
        s2 = max(16, n // 4)
        r1 = _rms(s1)
        r2 = _rms(s2)
        if r1 is None or r2 is None or np.isnan(r1) or np.isnan(r2) or (r1 <= 0) or (r2 <= 0):
            return np.nan
        return float(np.log(r2 / r1) / np.log(s2 / s1))
    return s.rolling(window, min_periods=max(window // 4, 32)).apply(_fn, raw=True)

def _half_life_acf(s, window, max_lag=30):
    """Half-life of autocorrelation: smallest lag where ACF drops below 0.5."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < max_lag + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        for L in range(1, max_lag + 1):
            num = float((v[:-L] * v[L:]).sum())
            ac = num / denom
            if ac < 0.5:
                return float(L)
        return float(max_lag)
    return s.rolling(window, min_periods=max(window // 2, max_lag + 3)).apply(_fn, raw=True)

def _autocorr_decay_rate(s, window, max_lag=10):
    """Linear regression slope of log|ACF| vs lag over [1..max_lag] — decay rate (neg slope = decay)."""

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < max_lag + 3:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        lags = []
        logacs = []
        for L in range(1, max_lag + 1):
            num = float((v[:-L] * v[L:]).sum())
            ac = abs(num / denom)
            if ac > 1e-06:
                lags.append(L)
                logacs.append(np.log(ac))
        if len(lags) < 3:
            return np.nan
        x = np.asarray(lags, dtype=float)
        y = np.asarray(logacs, dtype=float)
        xm = x.mean()
        ym = y.mean()
        num = ((x - xm) * (y - ym)).sum()
        den = ((x - xm) ** 2).sum()
        return float(num / den) if den > 0 else np.nan
    return s.rolling(window, min_periods=max(window // 2, max_lag + 3)).apply(_fn, raw=True)

def _cycle_phase_4(close, n=YDAYS):
    """Approx cycle-phase by close vs n-day max/min, returns 0..3:
    0=accumulation (near min), 1=markup (rising), 2=distribution (near max), 3=markdown (falling)."""
    rmax = close.rolling(n, min_periods=max(n // 3, 2)).max()
    rmin = close.rolling(n, min_periods=max(n // 3, 2)).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    slp = _rolling_slope(close, MDAYS)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask((pos < 0.25) & (slp <= 0), 0.0)
    phase = phase.mask((pos < 0.75) & (slp > 0), 1.0)
    phase = phase.mask(pos >= 0.75, 2.0)
    phase = phase.mask((pos >= 0.25) & (pos < 0.75) & (slp < 0), 3.0)
    return phase

def _cond_mean(value, mask, window):
    v = value.where(mask, np.nan)
    return v.rolling(window, min_periods=max(window // 4, 2)).mean()

def _is_local_extreme(s, n=3):
    """Per-bar: True if s[t-n] is a local max in (t-2n..t)."""
    rmax = s.rolling(2 * n + 1, min_periods=2 * n + 1).max()
    return (s.shift(n) == rmax) & rmax.notna()

def _is_local_min(s, n=3):
    rmin = s.rolling(2 * n + 1, min_periods=2 * n + 1).min()
    return (s.shift(n) == rmin) & rmin.notna()

def _bracket_high(close, n=QDAYS):
    return close >= close.rolling(n, min_periods=MDAYS).max()

def _bb_ratio(s, n=20, k=2.0):
    """(s - middle) / (k*sigma) — bollinger position; 0 = mid, 1 = upper."""
    m = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = s.rolling(n, min_periods=max(n // 3, 2)).std()
    return _safe_div(s - m, k * sd)

def f26_stwf_526_spread_adjusted_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) divided by Roll-spread proxy (21d) — spread-adjusted momentum."""
    k = _stoch_k(high, low, close, 14)
    sp = _roll_spread_proxy(close, MDAYS) + 1e-06
    return _safe_div(k, sp).diff().diff().diff()

def f26_stwf_527_volume_density_normalized_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """%K weighted by volume density = volume / range — high density = clean trend."""
    k = _stoch_k(high, low, close, 14)
    rng = (high - low).replace(0, np.nan)
    dens = _safe_div(volume, rng).rolling(MDAYS, min_periods=WDAYS).mean()
    dens_z = _rolling_zscore(dens, YDAYS, min_periods=QDAYS)
    return (k * (1.0 + dens_z.fillna(0).clip(-2, 2) * 0.25)).diff().diff().diff()

def f26_stwf_528_trade_intensity_weighted_williams_r_14_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R weighted by trade intensity (vol/range)."""
    wr = _williams_r(high, low, close, 14)
    rng = (high - low).replace(0, np.nan)
    intens = _safe_div(volume, rng).rolling(MDAYS, min_periods=WDAYS).mean()
    z = _rolling_zscore(intens, YDAYS, min_periods=QDAYS).fillna(0)
    return (wr * (1.0 + z.clip(-2, 2) * 0.25)).diff().diff().diff()

def f26_stwf_529_liquidity_weighted_oscillator_14_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """%K weighted by 1/Amihud illiquidity — penalizes low-liquidity oscillator state."""
    k = _stoch_k(high, low, close, 14)
    am = _amihud(close, volume, MDAYS)
    inv = _safe_div(1.0, am + 1e-12)
    inv_z = _rolling_zscore(inv, YDAYS, min_periods=QDAYS).fillna(0)
    return (k * (1.0 + inv_z.clip(-2, 2) * 0.25)).diff().diff().diff()

def f26_stwf_530_spread_conditional_oscillator_above_q70_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if %K > 70 AND Roll spread > 252d-q70 — high-momentum-with-wide-spread regime."""
    k = _stoch_k(high, low, close, 14)
    sp = _roll_spread_proxy(close, MDAYS)
    sp_q70 = _quantile_rolling(sp, YDAYS, 0.7, min_periods=QDAYS)
    return ((k > 70.0) & (sp > sp_q70)).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f26_stwf_531_microstructure_noise_filtered_stoch_5_21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between %K(5) and 21d-smoothed %K — short-vs-smoothed noise filter."""
    k5 = _stoch_k(high, low, close, WDAYS)
    k_sm = k5.rolling(MDAYS, min_periods=WDAYS).mean()
    return (k5 - k_sm).diff().diff().diff()

def f26_stwf_532_effective_tick_adjusted_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%K divided by effective-tick proxy (median |dC|/C over 21d) — tick-size-normalized."""
    k = _stoch_k(high, low, close, 14)
    tick = _safe_div(close.diff().abs(), close.shift(1)).rolling(MDAYS, min_periods=WDAYS).median() + 1e-08
    return _safe_div(k, tick).diff().diff().diff()

def f26_stwf_533_vwap_distance_weighted_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """%K weighted by |close - VWAP(21)| / close — extension-from-VWAP amplification."""
    k = _stoch_k(high, low, close, 14)
    vwap = _vwap_n(close, volume, MDAYS)
    ext = _safe_div((close - vwap).abs(), close).fillna(0)
    return (k * (1.0 + ext.clip(0, 0.25))).diff().diff().diff()

def f26_stwf_534_high_low_impact_normalized_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """%K normalized by Kyle-lambda proxy = avg(|ret| / sqrt(vol)) over 21d."""
    k = _stoch_k(high, low, close, 14)
    impact = _safe_div(close.pct_change().abs(), np.sqrt(volume.replace(0, np.nan))).rolling(MDAYS, min_periods=WDAYS).mean()
    iz = _rolling_zscore(impact, YDAYS, min_periods=QDAYS).fillna(0)
    return (k * (1.0 - iz.clip(-2, 2) * 0.25)).diff().diff().diff()

def f26_stwf_535_microstructure_regime_conditional_oscillator_avg_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K conditional on spread regime > 252d-median — momentum behavior in wide-spread regime."""
    k = _stoch_k(high, low, close, 14)
    sp = _roll_spread_proxy(close, MDAYS)
    sp_med = sp.rolling(YDAYS, min_periods=QDAYS).median()
    mask = sp > sp_med
    return _cond_mean(k, mask, YDAYS).diff().diff().diff()

def f26_stwf_536_dominant_period_of_stoch_in_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dominant cycle lag of %K in past 63 bars (ACF argmax in lags 5-63)."""
    k = _stoch_k(high, low, close, 14)
    return _dominant_period_acf(k, QDAYS, lag_lo=5, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_537_cycle_amplitude_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cycle amplitude proxy = (q90 - q10) of %K over 63 bars."""
    k = _stoch_k(high, low, close, 14)
    q90 = _quantile_rolling(k, QDAYS, 0.9, min_periods=MDAYS)
    q10 = _quantile_rolling(k, QDAYS, 0.1, min_periods=MDAYS)
    return (q90 - q10).diff().diff().diff()

def f26_stwf_538_spectral_entropy_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spectral entropy (bits) of %K over 63 — broadband vs concentrated cycles."""
    k = _stoch_k(high, low, close, 14)
    return _spectral_entropy_acf(k, QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_539_spectral_flatness_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spectral flatness of %K over 63."""
    k = _stoch_k(high, low, close, 14)
    return _spectral_flatness_acf(k, QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_540_power_in_5_to_21_band_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Power in short-period band (lag 5-21) for %K over 63."""
    k = _stoch_k(high, low, close, 14)
    return _power_in_band(k, QDAYS, 5, 21).diff().diff().diff()

def f26_stwf_541_power_in_21_to_63_band_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Power in medium-period band (lag 21-63 -> capped at QDAYS-3)."""
    k = _stoch_k(high, low, close, 14)
    hi = min(QDAYS - 3, 30)
    return _power_in_band(k, QDAYS, 21, hi).diff().diff().diff()

def f26_stwf_542_power_ratio_short_long_band_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of short-band to long-band power."""
    k = _stoch_k(high, low, close, 14)
    hi = min(QDAYS - 3, 30)
    p_short = _power_in_band(k, QDAYS, 5, 21)
    p_long = _power_in_band(k, QDAYS, 21, hi)
    return _safe_div(p_short, p_long).diff().diff().diff()

def f26_stwf_543_frequency_centroid_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency centroid (1/lag-weighted) of %K over 63."""
    k = _stoch_k(high, low, close, 14)
    return _freq_centroid_acf(k, QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_544_spectral_skewness_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spectral skewness of %K (asymmetry of power distribution across frequencies)."""
    k = _stoch_k(high, low, close, 14)
    return _spectral_moment(k, QDAYS, 3, lag_lo=2, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_545_spectral_kurtosis_of_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spectral kurtosis of %K (peakedness of power distribution)."""
    k = _stoch_k(high, low, close, 14)
    return _spectral_moment(k, QDAYS, 4, lag_lo=2, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_546_three_drives_pattern_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of local maxima in %K over 63 bars with each subsequent max higher (3-drive proxy)."""
    k = _stoch_k(high, low, close, 14)
    is_max = _is_local_extreme(k, n=3)
    peaks = k.where(is_max, np.nan).ffill(limit=2)
    rising = (peaks > peaks.shift(MDAYS)) & (peaks.shift(MDAYS) > peaks.shift(2 * MDAYS))
    return rising.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f26_stwf_547_bat_pattern_proxy_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bat-pattern proxy: peak then retracement ~50%, then push to lower high in %K over 63."""
    k = _stoch_k(high, low, close, 14)
    peak = k.rolling(QDAYS, min_periods=MDAYS).max()
    trough = k.rolling(MDAYS, min_periods=WDAYS).min()
    retrace = _safe_div(peak - k, peak - trough + 1e-06)
    in_zone = (retrace > 0.4) & (retrace < 0.65)
    return in_zone.astype(float).rolling(MDAYS, min_periods=1).sum().diff().diff().diff()

def f26_stwf_548_gartley_pattern_proxy_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gartley proxy: retracement ~61.8% from peak."""
    k = _stoch_k(high, low, close, 14)
    peak = k.rolling(QDAYS, min_periods=MDAYS).max()
    trough = k.rolling(MDAYS, min_periods=WDAYS).min()
    retrace = _safe_div(peak - k, peak - trough + 1e-06)
    in_zone = (retrace > 0.55) & (retrace < 0.7)
    return in_zone.astype(float).rolling(MDAYS, min_periods=1).sum().diff().diff().diff()

def f26_stwf_549_cypher_pattern_proxy_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cypher proxy: deep retracement (~78.6%) from peak."""
    k = _stoch_k(high, low, close, 14)
    peak = k.rolling(QDAYS, min_periods=MDAYS).max()
    trough = k.rolling(MDAYS, min_periods=WDAYS).min()
    retrace = _safe_div(peak - k, peak - trough + 1e-06)
    in_zone = (retrace > 0.72) & (retrace < 0.85)
    return in_zone.astype(float).rolling(MDAYS, min_periods=1).sum().diff().diff().diff()

def f26_stwf_550_ab_cd_pattern_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AB=CD proxy: |C-D| swing ~ |A-B| earlier swing in %K (within 25%)."""
    k = _stoch_k(high, low, close, 14)
    leg_now = (k - k.shift(QDAYS // 2)).abs()
    leg_prev = (k.shift(QDAYS // 2) - k.shift(QDAYS)).abs()
    ratio = _safe_div(leg_now, leg_prev + 1e-06)
    return ((ratio > 0.75) & (ratio < 1.25)).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_551_wolfe_wave_pattern_proxy_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wolfe-wave proxy: 5 alternating extremes in %K over 63 bars."""
    k = _stoch_k(high, low, close, 14)
    is_max = _is_local_extreme(k, n=3).astype(int)
    is_min = _is_local_min(k, n=3).astype(int)
    n_max = is_max.rolling(QDAYS, min_periods=MDAYS).sum()
    n_min = is_min.rolling(QDAYS, min_periods=MDAYS).sum()
    return ((n_max >= 3) & (n_min >= 2)).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_552_quintuple_top_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Five-peak top: count of local maxima in K above 70 over 63."""
    k = _stoch_k(high, low, close, 14)
    is_max = _is_local_extreme(k, n=2)
    cond = is_max & (k.shift(2) > 70.0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f26_stwf_553_rounded_top_in_stoch_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rounded-top: K is bounded above 60 for 21 bars without making new high."""
    k = _stoch_k(high, low, close, 14)
    above60 = (k > 60.0).rolling(MDAYS, min_periods=WDAYS).sum()
    new_hi = (k >= k.rolling(QDAYS, min_periods=MDAYS).max()).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((above60 >= int(MDAYS * 0.75)) & (new_hi <= 1)).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_554_oscillator_descending_channel_break_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K crosses below the lower bound of its 63d descending linear channel (mean - 2*std of slope_fit residuals)."""
    k = _stoch_k(high, low, close, 14)
    slp = _rolling_slope(k, QDAYS, min_periods=MDAYS)
    sd = k.rolling(QDAYS, min_periods=MDAYS).std()
    fitted = k.rolling(QDAYS, min_periods=MDAYS).mean() + slp * (QDAYS - 1) / 2.0
    lower = fitted - 2.0 * sd
    return ((slp < 0) & (k < lower)).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_555_oscillator_inside_day_at_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inside-bar in oscillator: K-range today < K-range yesterday, while close at 63d high."""
    k = _stoch_k(high, low, close, 14)
    k_rng = (k - k.shift(1)).abs()
    inside = k_rng < k_rng.shift(1)
    at_top = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    return (inside & at_top).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f26_stwf_556_stoch_in_early_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K when in cycle phase 0 (accumulation) over 252."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    return _cond_mean(k, ph == 0, YDAYS).diff().diff().diff()

def f26_stwf_557_stoch_in_mid_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K when in markup phase (1) over 252."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    return _cond_mean(k, ph == 1, YDAYS).diff().diff().diff()

def f26_stwf_558_stoch_in_late_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K when in distribution (2) over 252."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    return _cond_mean(k, ph == 2, YDAYS).diff().diff().diff()

def f26_stwf_559_stoch_in_distribution_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K in distribution (proxy: pos>0.75 and falling slope)."""
    k = _stoch_k(high, low, close, 14)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    slp = _rolling_slope(close, MDAYS)
    mask = (pos >= 0.75) & (slp <= 0)
    return _cond_mean(k, mask, YDAYS).diff().diff().diff()

def f26_stwf_560_stoch_in_markdown_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean %K when in markdown phase (3) over 252."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    return _cond_mean(k, ph == 3, YDAYS).diff().diff().diff()

def f26_stwf_561_cycle_conditional_ob_threshold_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Adaptive OB threshold: 252d q90 of K restricted to distribution-phase bars."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    v = k.where(ph == 2, np.nan)
    return v.rolling(YDAYS, min_periods=MDAYS).quantile(0.9).diff().diff().diff()

def f26_stwf_562_cycle_conditional_dwell_ratio_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dwell fraction above 80 conditional on distribution phase, over 252."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    ob = (k > 80.0) & (ph == 2)
    base = (ph == 2).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().replace(0, np.nan)
    return _safe_div(ob.astype(float).rolling(YDAYS, min_periods=QDAYS).sum(), base).diff().diff().diff()

def f26_stwf_563_cycle_phase_persistence_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of same cycle phase in past 252 bars."""
    ph = _cycle_phase_4(close, YDAYS)
    same = (ph == ph.shift(1)).astype(int)

    def _longest_run(w):
        if np.isnan(w).all():
            return np.nan
        v = w.astype(int)
        best = 0
        c = 0
        for x in v:
            if x == 1:
                c += 1
                if c > best:
                    best = c
            else:
                c = 0
        return float(best)
    return same.rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True).diff().diff().diff()

def f26_stwf_564_cycle_phase_shift_indicator_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of phase transitions in past 252 bars."""
    ph = _cycle_phase_4(close, YDAYS)
    shifts = (ph != ph.shift(1)).astype(float)
    return shifts.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f26_stwf_565_cycle_end_stoch_behavior_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (phase shifted from 2 to 3 in past 21 bars) AND (%K still > 50) — distribution-into-markdown not yet confirmed."""
    k = _stoch_k(high, low, close, 14)
    ph = _cycle_phase_4(close, YDAYS)
    transition = ((ph == 3) & (ph.shift(MDAYS) == 2)).astype(float)
    recent = transition.rolling(MDAYS, min_periods=1).max()
    return ((recent > 0) & (k > 50.0)).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_566_stoch_hurst_rs_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rescaled-range Hurst of %K over 252 bars."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_hurst_rs(k, YDAYS).diff().diff().diff()

def f26_stwf_567_stoch_hurst_dfa_504_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DFA Hurst of %K over 504 bars."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_hurst_dfa(k, DDAYS_2Y).diff().diff().diff()

def f26_stwf_568_stoch_hurst_dfa_1260_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DFA Hurst of %K over 1260 bars."""
    k = _stoch_k(high, low, close, 14)
    return _rolling_hurst_dfa(k, DDAYS_5Y).diff().diff().diff()

def f26_stwf_569_stoch_acf_integral_long_range_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of |ACF| at lags 1..30 over 252 — long-range memory proxy."""
    k = _stoch_k(high, low, close, 14)

    def _fn(w):
        if not np.isfinite(w).all() or len(w) < 35:
            return np.nan
        m = w.mean()
        v = w - m
        denom = float((v * v).sum())
        if denom <= 0:
            return np.nan
        tot = 0.0
        for L in range(1, 31):
            num = float((v[:-L] * v[L:]).sum())
            tot += abs(num / denom)
        return tot
    return k.rolling(YDAYS, min_periods=64).apply(_fn, raw=True).diff().diff().diff()

def f26_stwf_570_stoch_lagged_corr_profile_max_lag_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lag (1..min(QDAYS-3,30)) at which |ACF(K)| is maximum within 63."""
    k = _stoch_k(high, low, close, 14)
    return _dominant_period_acf(k, QDAYS, lag_lo=1, lag_hi=min(QDAYS - 3, 30)).diff().diff().diff()

def f26_stwf_571_stoch_memory_half_life_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-life of K's ACF over 252."""
    k = _stoch_k(high, low, close, 14)
    return _half_life_acf(k, YDAYS, max_lag=30).diff().diff().diff()

def f26_stwf_572_stoch_decay_rate_autocorr_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decay rate (slope of log|ACF| vs lag) of K over 63."""
    k = _stoch_k(high, low, close, 14)
    return _autocorr_decay_rate(k, QDAYS, max_lag=10).diff().diff().diff()

def f26_stwf_573_stoch_arfima_d_proxy_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ARFIMA d proxy: d ~ H - 0.5, using RS Hurst over 252."""
    k = _stoch_k(high, low, close, 14)
    return (_rolling_hurst_rs(k, YDAYS) - 0.5).diff().diff().diff()

def f26_stwf_574_stoch_multi_scale_hurst_stability_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of Hurst estimates across 3 scales (63/126/252) using RS."""
    k = _stoch_k(high, low, close, 14)
    h63 = _rolling_hurst_rs(k, QDAYS)
    h126 = _rolling_hurst_rs(k, MDAYS * 6)
    h252 = _rolling_hurst_rs(k, YDAYS)
    return pd.concat([h63.rename('h63'), h126.rename('h126'), h252.rename('h252')], axis=1).std(axis=1).diff().diff().diff()

def f26_stwf_575_stoch_memory_regime_indicator_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Hurst > 0.6 over 252 (persistent regime), 0 if < 0.4 (anti-persistent), else 0.5."""
    k = _stoch_k(high, low, close, 14)
    h = _rolling_hurst_rs(k, YDAYS)
    out = pd.Series(0.5, index=close.index)
    out = out.mask(h > 0.6, 1.0)
    out = out.mask(h < 0.4, 0.0)
    return out.where(close.notna(), np.nan).diff().diff().diff()

def f26_stwf_576_stoch_key_reversal_day_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Key reversal: K makes new 21d high but closes below previous K — bearish key reversal in oscillator."""
    k = _stoch_k(high, low, close, 14)
    new_hi = k > k.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    close_lower = k < k.shift(1)
    return (new_hi & close_lower).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_577_stoch_hook_failure_at_top_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hook failure: K above 80 then declines two consecutive bars while close near 63d max."""
    k = _stoch_k(high, low, close, 14)
    above_recent = k.shift(2) > 80.0
    decline = (k < k.shift(1)) & (k.shift(1) < k.shift(2))
    at_top = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    return (above_recent & decline & at_top).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_578_stoch_cookie_cutter_setup_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cookie-cutter: K oscillates in narrow band [60,80] for 5 bars then drops below 50."""
    k = _stoch_k(high, low, close, 14)
    in_band = ((k > 60.0) & (k < 80.0)).rolling(WDAYS, min_periods=WDAYS).sum() >= 4
    drop = k < 50.0
    setup = in_band.shift(1) & drop
    return setup.astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_579_stoch_bowl_pattern_detection_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bowl pattern: K trough in middle of 63d window, with start and end > middle min."""
    k = _stoch_k(high, low, close, 14)
    rmin = k.rolling(QDAYS, min_periods=MDAYS).min()
    start = k.shift(QDAYS - 1)
    end = k
    middle_low = (start > rmin + 10.0) & (end > rmin + 10.0)
    return middle_low.astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_580_stoch_cup_with_handle_failure_in_oscillator_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cup-handle fail in oscillator: bowl shape then small pullback then break below cup rim."""
    k = _stoch_k(high, low, close, 14)
    rim = k.shift(QDAYS - 1)
    cup_low = k.shift(QDAYS // 2).rolling(MDAYS, min_periods=WDAYS).min()
    handle_pullback = k.shift(5)
    fail = (rim > 60.0) & (cup_low < rim - 20.0) & (handle_pullback < rim) & (k < cup_low)
    return fail.astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_581_stoch_knife_edge_break_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Knife-edge: K drops > 30 points in one bar."""
    k = _stoch_k(high, low, close, 14)
    return (k.diff() <= -30.0).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_582_stoch_extension_then_failure_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Extension-then-failure: K > 90 in past 5 bars, now < 60."""
    k = _stoch_k(high, low, close, 14)
    ext = k.shift(1).rolling(WDAYS, min_periods=1).max() > 90.0
    fail = k < 60.0
    return (ext & fail).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_583_stoch_multi_bar_reversal_pattern_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multi-bar reversal: 3 consecutive lower-K bars after 3 consecutive higher-K bars."""
    k = _stoch_k(high, low, close, 14)
    up3 = (k.shift(3) < k.shift(2)) & (k.shift(2) < k.shift(1)) & (k.shift(1) > k.shift(4))
    down3 = (k.shift(2) > k.shift(1)) & (k.shift(1) > k)
    return (up3.shift(3).fillna(False) & down3).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_584_stoch_outside_day_at_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Outside bar in K: K range > yesterday range AND yesterday at 63d high AND today closes lower."""
    k = _stoch_k(high, low, close, 14)
    rng_today = (k - k.shift(1)).abs()
    rng_yest = (k.shift(1) - k.shift(2)).abs()
    outside = rng_today > rng_yest
    yest_at_top = close.shift(1) >= close.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    today_lower = k < k.shift(1)
    return (outside & yest_at_top & today_lower).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_585_stoch_reversal_day_at_extreme_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Reversal day: K hits >= 252d q95 then closes below the prior bar's K."""
    k = _stoch_k(high, low, close, 14)
    q95 = _quantile_rolling(k, YDAYS, 0.95, min_periods=QDAYS)
    touched = k.shift(1) >= q95
    rev = k < k.shift(1)
    return (touched & rev).astype(float).where(k.notna(), np.nan).diff().diff().diff()

def f26_stwf_586_batch_4_modern_aggregate_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V4 modern aggregate: sum of 252-z of (spectral entropy) + (Hurst) + (cycle dwell)
    + (pattern density)."""
    k = _stoch_k(high, low, close, 14)
    se = _spectral_entropy_acf(k, QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30))
    h = _rolling_hurst_rs(k, YDAYS)
    ph = _cycle_phase_4(close, YDAYS)
    dwell = ((k > 80.0) & (ph == 2)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    new_hi = k > k.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    close_lower = k < k.shift(1)
    pd_cnt = (new_hi & close_lower).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return (nz(se) + nz(h) + nz(dwell) + nz(pd_cnt)).diff().diff().diff()

def f26_stwf_587_universe_wide_topping_auc_optimized_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AUC-optimized blend across basket: extreme-z + chronic-OB + post-peak-decay,
    each rolling-rank-normalized then summed."""
    o = _all_oscillators(high, low, close)
    parts = []
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        parts.append(z)
        ob = (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
        parts.append(ob)
        peak = s.rolling(QDAYS, min_periods=MDAYS).max().replace(0, np.nan)
        parts.append(_safe_div(peak - s, peak))
    df = pd.concat([p.rename(i) for i, p in enumerate(parts)], axis=1)
    return df.fillna(0).sum(axis=1).diff().diff().diff()

def f26_stwf_588_universe_wide_stuck_prediction_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """V4 stuck prediction: weighted sum of (basket weakness count) + (chronic-OB count)
    + (post-blowoff fail count) + (Hurst > 0.6) over 252."""
    o = _all_oscillators(high, low, close)
    wk = pd.Series(0.0, index=close.index)
    chr_ob = pd.Series(0.0, index=close.index)
    pf = pd.Series(0.0, index=close.index)
    for s in o.values():
        wk = wk + (s < 30.0).astype(float).fillna(0)
        chr_ob = chr_ob + (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        pf = pf + ((z.shift(MDAYS) > 3.0).astype(float) * (z < 0).astype(float)).fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS).fillna(0)
    persist = (h > 0.6).astype(float)
    return (0.25 * wk + 0.25 * chr_ob + 0.3 * pf + 0.2 * persist).diff().diff().diff()

def f26_stwf_589_cross_batch_consensus_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consensus: count of (K > 80) + (Williams R > -20) + (SRSI K > 80) + (Hurst > 0.6)
    + (entropy < median) — broad agreement of momentum extremes."""
    o = _all_oscillators(high, low, close)
    score = (o['k'] > 80.0).astype(float).fillna(0) + (o['wr'] > -20.0).astype(float).fillna(0) + (o['sk'] > 80.0).astype(float).fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS).fillna(0)
    score = score + (h > 0.6).astype(float)
    se = _spectral_entropy_acf(o['k'], QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30))
    se_med = se.rolling(YDAYS, min_periods=QDAYS).median()
    score = score + (se < se_med).astype(float).fillna(0)
    return score.diff().diff().diff()

def f26_stwf_590_multi_feature_alignment_score_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Alignment: sign-agreement among basket z-scores over 252 (max=1 all agree, 0 = neutral)."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    pos = (df > 0).sum(axis=1)
    neg = (df < 0).sum(axis=1)
    return ((pos - neg).abs() / float(len(z_list))).diff().diff().diff()

def f26_stwf_591_orthogonal_batch_4_aggregate_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Orthogonal aggregate: PC2-proxy (K-z minus mean-z) + spectral kurtosis + Hurst — independent axes."""
    o = _all_oscillators(high, low, close)
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in o.values()]
    df = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1)
    pc1 = df.mean(axis=1)
    k_z = _rolling_zscore(o['k'], YDAYS, min_periods=QDAYS)
    pc2 = k_z - pc1
    sk = _spectral_moment(o['k'], QDAYS, 4, lag_lo=2, lag_hi=min(QDAYS - 3, 30))
    h = _rolling_hurst_rs(o['k'], YDAYS)
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return (nz(pc2) + nz(sk) + nz(h)).diff().diff().diff()

def f26_stwf_592_cross_pattern_terminal_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cross-pattern: count of (key-reversal) + (hook-failure) + (knife-edge) + (extension-then-fail) over 21."""
    k = _stoch_k(high, low, close, 14)
    new_hi = k > k.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    cl = k < k.shift(1)
    kr = (new_hi & cl).astype(float)
    above = k.shift(2) > 80.0
    decline = (k < k.shift(1)) & (k.shift(1) < k.shift(2))
    at_top = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    hf = (above & decline & at_top).astype(float)
    ke = (k.diff() <= -30.0).astype(float)
    ext = k.shift(1).rolling(WDAYS, min_periods=1).max() > 90.0
    fail = k < 60.0
    ef = (ext & fail).astype(float)
    tot = kr.fillna(0) + hf.fillna(0) + ke.fillna(0) + ef.fillna(0)
    return tot.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f26_stwf_593_multi_resolution_stuck_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multi-resolution: %K state across (5/21/63/252) horizons — count weak states."""
    k5 = _stoch_k(high, low, close, WDAYS)
    k21 = _stoch_k(high, low, close, MDAYS)
    k63 = _stoch_k(high, low, close, QDAYS)
    k252 = _stoch_k(high, low, close, YDAYS)
    score = (k5 < 30.0).astype(float).fillna(0) + (k21 < 30.0).astype(float).fillna(0) + (k63 < 30.0).astype(float).fillna(0) + (k252 < 30.0).astype(float).fillna(0)
    return score.diff().diff().diff()

def f26_stwf_594_final_topping_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final topping master: extreme-z + cycle-distribution-dwell + Hurst persistence + volume-z."""
    o = _all_oscillators(high, low, close)
    ec = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        ec = ec + (z > 2.0).astype(float).fillna(0)
    ph = _cycle_phase_4(close, YDAYS)
    dist_dwell = (ph == 2).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS)
    persist = (h > 0.6).astype(float).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(-2, 3)
    return (ec + 2.0 * dist_dwell + persist + 0.5 * v_z).diff().diff().diff()

def f26_stwf_595_final_breakdown_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final breakdown master: descending-channel-break + key-reversal density + price 252d-drawdown + volume-z."""
    k = _stoch_k(high, low, close, 14)
    slp = _rolling_slope(k, QDAYS, min_periods=MDAYS)
    sd = k.rolling(QDAYS, min_periods=MDAYS).std()
    fitted = k.rolling(QDAYS, min_periods=MDAYS).mean() + slp * (QDAYS - 1) / 2.0
    lower = fitted - 2.0 * sd
    chan = ((slp < 0) & (k < lower)).astype(float).fillna(0)
    new_hi = k > k.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    cl = k < k.shift(1)
    kr = (new_hi & cl).astype(float).rolling(MDAYS, min_periods=1).sum().fillna(0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (1.0 - _safe_div(close, rmax)).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(-2, 3)
    return (chan + 0.5 * kr + 5.0 * dd + 0.5 * v_z).diff().diff().diff()

def f26_stwf_596_final_blowoff_collapse_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final blowoff-collapse: z>3 then collapse + knife-edge events + volume z."""
    k = _stoch_k(high, low, close, 14)
    z = _rolling_zscore(k, YDAYS, min_periods=QDAYS)
    bo = (z.shift(MDAYS) > 3.0).astype(float)
    now_low = (z < 0).astype(float)
    bo_fail = (bo * now_low).fillna(0)
    ke = (k.diff() <= -30.0).astype(float).fillna(0).rolling(MDAYS, min_periods=1).sum()
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(-2, 3)
    return (bo_fail + 0.5 * ke + 0.5 * v_z).diff().diff().diff()

def f26_stwf_597_final_distribution_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final distribution master: basket-in-60-80 + lower-high count + chronic-OB + volume z."""
    o = _all_oscillators(high, low, close)
    in_zone = pd.Series(0.0, index=close.index)
    lh = pd.Series(0.0, index=close.index)
    chr_ob = pd.Series(0.0, index=close.index)
    for s in o.values():
        in_zone = in_zone + ((s >= 60.0) & (s <= 80.0)).astype(float).fillna(0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        lh = lh + (mx21 < mx21.shift(MDAYS)).astype(float).fillna(0)
        chr_ob = chr_ob + (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(-2, 3)
    return (in_zone + lh + chr_ob + 0.5 * v_z).diff().diff().diff()

def f26_stwf_598_stuck_probability_proxy_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stuck probability v4: weakness + chronic-OB-no-progress + Hurst + drawdown + (low entropy = predictable decline)."""
    o = _all_oscillators(high, low, close)
    wk = pd.Series(0.0, index=close.index)
    chr_ob_nop = pd.Series(0.0, index=close.index)
    for s in o.values():
        wk = wk + (s < 30.0).astype(float).fillna(0)
        ob_days = (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
        p_max = close.rolling(QDAYS, min_periods=MDAYS).max()
        chr_ob_nop = chr_ob_nop + ((ob_days > 40.0) & (close < p_max)).astype(float).fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS).fillna(0.5)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (1.0 - _safe_div(close, rmax)).fillna(0)
    se = _spectral_entropy_acf(o['k'], QDAYS, lag_lo=2, lag_hi=min(QDAYS - 3, 30))
    se_med = se.rolling(YDAYS, min_periods=QDAYS).median()
    low_se = (se < se_med).astype(float).fillna(0)
    return (0.25 * wk + 0.25 * chr_ob_nop + 0.2 * h + 0.2 * (5.0 * dd) + 0.1 * low_se).diff().diff().diff()

def f26_stwf_599_absolute_terminal_master_v4_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute terminal v4: 1 if (basket extreme z>2 count >= 3) AND (Hurst > 0.55)
    AND (volume z > 1) AND (close at 252d high) AND (cycle phase = distribution)."""
    o = _all_oscillators(high, low, close)
    ec = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        ec = ec + (z > 2.0).astype(float).fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    is_top = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    ph = _cycle_phase_4(close, YDAYS)
    return ((ec >= 3) & (h > 0.55) & (v_z > 1.0) & is_top & (ph == 2)).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f26_stwf_600_oscillator_extended_universe_v4_aggregate_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final aggregate: sum of z-scored (topping master) + (breakdown master) + (blowoff-collapse) +
    (distribution master) — universe-wide composite of v4 masters (inlined, no cross-fn calls)."""
    o = _all_oscillators(high, low, close)
    ec = pd.Series(0.0, index=close.index)
    for s in o.values():
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        ec = ec + (z > 2.0).astype(float).fillna(0)
    ph = _cycle_phase_4(close, YDAYS)
    dist_dwell = (ph == 2).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
    h = _rolling_hurst_rs(o['k'], YDAYS)
    persist = (h > 0.6).astype(float).fillna(0)
    v_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).fillna(0).clip(-2, 3)
    top = ec + 2.0 * dist_dwell + persist + 0.5 * v_z
    k = o['k']
    slp = _rolling_slope(k, QDAYS, min_periods=MDAYS)
    sd = k.rolling(QDAYS, min_periods=MDAYS).std()
    fitted = k.rolling(QDAYS, min_periods=MDAYS).mean() + slp * (QDAYS - 1) / 2.0
    lower = fitted - 2.0 * sd
    chan = ((slp < 0) & (k < lower)).astype(float).fillna(0)
    new_hi = k > k.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    cl = k < k.shift(1)
    kr = (new_hi & cl).astype(float).rolling(MDAYS, min_periods=1).sum().fillna(0)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (1.0 - _safe_div(close, rmax)).fillna(0)
    brk = chan + 0.5 * kr + 5.0 * dd + 0.5 * v_z
    z_k = _rolling_zscore(k, YDAYS, min_periods=QDAYS)
    bo = (z_k.shift(MDAYS) > 3.0).astype(float)
    now_low = (z_k < 0).astype(float)
    bo_fail = (bo * now_low).fillna(0)
    ke = (k.diff() <= -30.0).astype(float).fillna(0).rolling(MDAYS, min_periods=1).sum()
    blow = bo_fail + 0.5 * ke + 0.5 * v_z
    in_zone = pd.Series(0.0, index=close.index)
    lh = pd.Series(0.0, index=close.index)
    chr_ob = pd.Series(0.0, index=close.index)
    for s in o.values():
        in_zone = in_zone + ((s >= 60.0) & (s <= 80.0)).astype(float).fillna(0)
        mx21 = s.rolling(MDAYS, min_periods=WDAYS).max()
        lh = lh + (mx21 < mx21.shift(MDAYS)).astype(float).fillna(0)
        chr_ob = chr_ob + (s > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().fillna(0)
    dist = in_zone + lh + chr_ob + 0.5 * v_z
    nz = lambda x: _rolling_zscore(x, YDAYS, min_periods=QDAYS).fillna(0)
    return (nz(top) + nz(brk) + nz(blow) + nz(dist)).diff().diff().diff()
STOCHASTIC_WILLIAMS_FAMILY_D3_REGISTRY_526_600 = {'f26_stwf_526_spread_adjusted_stoch_14_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_526_spread_adjusted_stoch_14_d3}, 'f26_stwf_527_volume_density_normalized_stoch_14_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_527_volume_density_normalized_stoch_14_d3}, 'f26_stwf_528_trade_intensity_weighted_williams_r_14_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_528_trade_intensity_weighted_williams_r_14_d3}, 'f26_stwf_529_liquidity_weighted_oscillator_14_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_529_liquidity_weighted_oscillator_14_d3}, 'f26_stwf_530_spread_conditional_oscillator_above_q70_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_530_spread_conditional_oscillator_above_q70_state_d3}, 'f26_stwf_531_microstructure_noise_filtered_stoch_5_21_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_531_microstructure_noise_filtered_stoch_5_21_d3}, 'f26_stwf_532_effective_tick_adjusted_stoch_14_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_532_effective_tick_adjusted_stoch_14_d3}, 'f26_stwf_533_vwap_distance_weighted_stoch_14_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_533_vwap_distance_weighted_stoch_14_d3}, 'f26_stwf_534_high_low_impact_normalized_stoch_14_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_534_high_low_impact_normalized_stoch_14_d3}, 'f26_stwf_535_microstructure_regime_conditional_oscillator_avg_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_535_microstructure_regime_conditional_oscillator_avg_d3}, 'f26_stwf_536_dominant_period_of_stoch_in_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_536_dominant_period_of_stoch_in_63_d3}, 'f26_stwf_537_cycle_amplitude_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_537_cycle_amplitude_of_stoch_63_d3}, 'f26_stwf_538_spectral_entropy_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_538_spectral_entropy_of_stoch_63_d3}, 'f26_stwf_539_spectral_flatness_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_539_spectral_flatness_of_stoch_63_d3}, 'f26_stwf_540_power_in_5_to_21_band_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_540_power_in_5_to_21_band_of_stoch_63_d3}, 'f26_stwf_541_power_in_21_to_63_band_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_541_power_in_21_to_63_band_of_stoch_63_d3}, 'f26_stwf_542_power_ratio_short_long_band_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_542_power_ratio_short_long_band_63_d3}, 'f26_stwf_543_frequency_centroid_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_543_frequency_centroid_of_stoch_63_d3}, 'f26_stwf_544_spectral_skewness_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_544_spectral_skewness_of_stoch_63_d3}, 'f26_stwf_545_spectral_kurtosis_of_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_545_spectral_kurtosis_of_stoch_63_d3}, 'f26_stwf_546_three_drives_pattern_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_546_three_drives_pattern_in_stoch_63_d3}, 'f26_stwf_547_bat_pattern_proxy_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_547_bat_pattern_proxy_in_stoch_63_d3}, 'f26_stwf_548_gartley_pattern_proxy_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_548_gartley_pattern_proxy_in_stoch_63_d3}, 'f26_stwf_549_cypher_pattern_proxy_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_549_cypher_pattern_proxy_in_stoch_63_d3}, 'f26_stwf_550_ab_cd_pattern_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_550_ab_cd_pattern_in_stoch_63_d3}, 'f26_stwf_551_wolfe_wave_pattern_proxy_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_551_wolfe_wave_pattern_proxy_in_stoch_63_d3}, 'f26_stwf_552_quintuple_top_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_552_quintuple_top_in_stoch_63_d3}, 'f26_stwf_553_rounded_top_in_stoch_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_553_rounded_top_in_stoch_63_d3}, 'f26_stwf_554_oscillator_descending_channel_break_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_554_oscillator_descending_channel_break_indicator_d3}, 'f26_stwf_555_oscillator_inside_day_at_high_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_555_oscillator_inside_day_at_high_indicator_d3}, 'f26_stwf_556_stoch_in_early_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_556_stoch_in_early_cycle_phase_avg_252_d3}, 'f26_stwf_557_stoch_in_mid_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_557_stoch_in_mid_cycle_phase_avg_252_d3}, 'f26_stwf_558_stoch_in_late_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_558_stoch_in_late_cycle_phase_avg_252_d3}, 'f26_stwf_559_stoch_in_distribution_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_559_stoch_in_distribution_phase_avg_252_d3}, 'f26_stwf_560_stoch_in_markdown_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_560_stoch_in_markdown_phase_avg_252_d3}, 'f26_stwf_561_cycle_conditional_ob_threshold_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_561_cycle_conditional_ob_threshold_252_d3}, 'f26_stwf_562_cycle_conditional_dwell_ratio_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_562_cycle_conditional_dwell_ratio_252_d3}, 'f26_stwf_563_cycle_phase_persistence_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_563_cycle_phase_persistence_252_d3}, 'f26_stwf_564_cycle_phase_shift_indicator_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_564_cycle_phase_shift_indicator_252_d3}, 'f26_stwf_565_cycle_end_stoch_behavior_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_565_cycle_end_stoch_behavior_indicator_d3}, 'f26_stwf_566_stoch_hurst_rs_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_566_stoch_hurst_rs_252_d3}, 'f26_stwf_567_stoch_hurst_dfa_504_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_567_stoch_hurst_dfa_504_d3}, 'f26_stwf_568_stoch_hurst_dfa_1260_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_568_stoch_hurst_dfa_1260_d3}, 'f26_stwf_569_stoch_acf_integral_long_range_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_569_stoch_acf_integral_long_range_252_d3}, 'f26_stwf_570_stoch_lagged_corr_profile_max_lag_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_570_stoch_lagged_corr_profile_max_lag_63_d3}, 'f26_stwf_571_stoch_memory_half_life_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_571_stoch_memory_half_life_252_d3}, 'f26_stwf_572_stoch_decay_rate_autocorr_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_572_stoch_decay_rate_autocorr_63_d3}, 'f26_stwf_573_stoch_arfima_d_proxy_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_573_stoch_arfima_d_proxy_252_d3}, 'f26_stwf_574_stoch_multi_scale_hurst_stability_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_574_stoch_multi_scale_hurst_stability_252_d3}, 'f26_stwf_575_stoch_memory_regime_indicator_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_575_stoch_memory_regime_indicator_252_d3}, 'f26_stwf_576_stoch_key_reversal_day_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_576_stoch_key_reversal_day_indicator_d3}, 'f26_stwf_577_stoch_hook_failure_at_top_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_577_stoch_hook_failure_at_top_indicator_d3}, 'f26_stwf_578_stoch_cookie_cutter_setup_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_578_stoch_cookie_cutter_setup_indicator_d3}, 'f26_stwf_579_stoch_bowl_pattern_detection_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_579_stoch_bowl_pattern_detection_63_d3}, 'f26_stwf_580_stoch_cup_with_handle_failure_in_oscillator_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_580_stoch_cup_with_handle_failure_in_oscillator_63_d3}, 'f26_stwf_581_stoch_knife_edge_break_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_581_stoch_knife_edge_break_indicator_d3}, 'f26_stwf_582_stoch_extension_then_failure_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_582_stoch_extension_then_failure_indicator_d3}, 'f26_stwf_583_stoch_multi_bar_reversal_pattern_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_583_stoch_multi_bar_reversal_pattern_indicator_d3}, 'f26_stwf_584_stoch_outside_day_at_high_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_584_stoch_outside_day_at_high_indicator_d3}, 'f26_stwf_585_stoch_reversal_day_at_extreme_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_585_stoch_reversal_day_at_extreme_indicator_d3}, 'f26_stwf_586_batch_4_modern_aggregate_zscore_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_586_batch_4_modern_aggregate_zscore_252_d3}, 'f26_stwf_587_universe_wide_topping_auc_optimized_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_587_universe_wide_topping_auc_optimized_score_d3}, 'f26_stwf_588_universe_wide_stuck_prediction_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_588_universe_wide_stuck_prediction_v4_score_d3}, 'f26_stwf_589_cross_batch_consensus_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_589_cross_batch_consensus_score_d3}, 'f26_stwf_590_multi_feature_alignment_score_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_590_multi_feature_alignment_score_252_d3}, 'f26_stwf_591_orthogonal_batch_4_aggregate_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_591_orthogonal_batch_4_aggregate_d3}, 'f26_stwf_592_cross_pattern_terminal_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_592_cross_pattern_terminal_v4_score_d3}, 'f26_stwf_593_multi_resolution_stuck_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f26_stwf_593_multi_resolution_stuck_v4_score_d3}, 'f26_stwf_594_final_topping_master_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_594_final_topping_master_v4_score_d3}, 'f26_stwf_595_final_breakdown_master_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_595_final_breakdown_master_v4_score_d3}, 'f26_stwf_596_final_blowoff_collapse_master_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_596_final_blowoff_collapse_master_v4_score_d3}, 'f26_stwf_597_final_distribution_master_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_597_final_distribution_master_v4_score_d3}, 'f26_stwf_598_stuck_probability_proxy_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_598_stuck_probability_proxy_v4_score_d3}, 'f26_stwf_599_absolute_terminal_master_v4_indicator_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_599_absolute_terminal_master_v4_indicator_d3}, 'f26_stwf_600_oscillator_extended_universe_v4_aggregate_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f26_stwf_600_oscillator_extended_universe_v4_aggregate_d3}}