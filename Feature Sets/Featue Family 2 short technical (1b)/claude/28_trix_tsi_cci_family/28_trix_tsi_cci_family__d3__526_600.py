"""28_trix_tsi_cci_family d3 features 526-600 — order-3 difference of corresponding base features.

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

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

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

def _basket_classical(high, low, close):
    return [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20), _cmo(close, 14), _dpo(close, MDAYS), _kst(close)]

def _hl_range_pct(high, low, close):
    return _safe_div(high - low, close)

def _amihud_proxy(close, volume, n=MDAYS):
    """Amihud illiquidity = mean(|return| / $vol). Higher = less liquid."""
    ret = close.pct_change().abs()
    dvol = (close * volume).replace(0, np.nan)
    return (ret / dvol).rolling(n, min_periods=max(n // 3, 2)).mean()

def _spread_proxy_hl(high, low, close, n=MDAYS):
    """Spread proxy from HL range / close, smoothed."""
    return _hl_range_pct(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()

def _effective_tick(close, n=MDAYS):
    """Effective tick proxy = std of returns over n bars."""
    return close.pct_change().rolling(n, min_periods=max(n // 3, 2)).std()

def _vwap_intraday_proxy(high, low, close, volume):
    """Cumulative typical-price-weighted VWAP proxy reset daily — but daily data => use tp."""
    return (high + low + close) / 3.0

def _detrend(w):
    n = len(w)
    x = np.arange(n, dtype=float)
    p = np.polyfit(x, w, 1)
    return w - (p[0] * x + p[1])

def _fft_power_spectrum(w):
    if np.isnan(w).any() or len(w) < 8:
        return None
    w = _detrend(w)
    if np.std(w) == 0:
        return None
    f = np.fft.rfft(w)
    p = np.abs(f) ** 2
    return p

def _dominant_period_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    k = int(np.argmax(p)) + 1
    if k <= 0:
        return np.nan
    return float(len(w)) / float(k)

def _cycle_amplitude_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    return float(np.sqrt(p.max())) / float(len(w))

def _spectral_entropy_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    s = p.sum()
    if s == 0:
        return np.nan
    p = p / s
    p = p[p > 0]
    se = -(p * np.log(p)).sum()
    return float(se / np.log(len(p))) if len(p) > 1 else 0.0

def _spectral_flatness_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    if (p <= 0).all():
        return np.nan
    pp = p[p > 0]
    if len(pp) == 0:
        return np.nan
    geo = np.exp(np.log(pp).mean())
    ari = pp.mean()
    return float(geo / ari) if ari > 0 else np.nan

def _band_power_inner(w, lo_period, hi_period):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    n = len(w)
    p_band = 0.0
    for k in range(1, len(p)):
        period = n / k
        if lo_period <= period < hi_period:
            p_band += p[k]
    return float(p_band)

def _power_ratio_short_long_inner(w):
    sb = _band_power_inner(w, 5, 21)
    lb = _band_power_inner(w, 21, 63)
    if np.isnan(sb) or np.isnan(lb) or lb == 0:
        return np.nan
    return float(sb / lb)

def _frequency_centroid_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    s = p.sum()
    if s == 0:
        return np.nan
    freqs = np.arange(1, len(p) + 1, dtype=float)
    return float((p * freqs).sum() / s)

def _spectral_skewness_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    s = p.sum()
    if s == 0:
        return np.nan
    pn = p / s
    freqs = np.arange(1, len(p) + 1, dtype=float)
    m = (pn * freqs).sum()
    sd = np.sqrt((pn * (freqs - m) ** 2).sum())
    if sd == 0:
        return np.nan
    sk = (pn * ((freqs - m) / sd) ** 3).sum()
    return float(sk)

def _spectral_kurtosis_inner(w):
    p = _fft_power_spectrum(w)
    if p is None or len(p) < 3:
        return np.nan
    p = p[1:]
    s = p.sum()
    if s == 0:
        return np.nan
    pn = p / s
    freqs = np.arange(1, len(p) + 1, dtype=float)
    m = (pn * freqs).sum()
    sd = np.sqrt((pn * (freqs - m) ** 2).sum())
    if sd == 0:
        return np.nan
    kt = (pn * ((freqs - m) / sd) ** 4).sum()
    return float(kt)

def _rolling_apply(s, n, fn):
    return s.rolling(n, min_periods=max(n // 2, 8)).apply(fn, raw=True)

def _is_local_max(arr, i, k=2):
    if i - k < 0 or i + k >= len(arr):
        return False
    return arr[i] == np.max(arr[i - k:i + k + 1])

def _is_local_min(arr, i, k=2):
    if i - k < 0 or i + k >= len(arr):
        return False
    return arr[i] == np.min(arr[i - k:i + k + 1])

def _three_drives_pattern_inner(w):
    """Three-drives: three successive higher highs followed by a lower close.
    Returns 1 at end of window if pattern found."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    n = len(w)
    maxima = [i for i in range(2, n - 2) if _is_local_max(w, i, 2)]
    if len(maxima) < 3:
        return 0.0
    last3 = maxima[-3:]
    if w[last3[0]] < w[last3[1]] < w[last3[2]] and w[-1] < w[last3[2]]:
        return 1.0
    return 0.0

def _bat_pattern_inner(w):
    """Bat pattern proxy: 5-point XABCD where AB/XA ~0.38-0.50 and CD/AB ~1.27-1.61.
    Returns 1 if rough match, else 0."""
    if np.isnan(w).any() or len(w) < 20:
        return np.nan
    n = len(w)
    piv = []
    for i in range(2, n - 2):
        if _is_local_max(w, i, 2) or _is_local_min(w, i, 2):
            piv.append((i, w[i]))
    if len(piv) < 5:
        return 0.0
    p = piv[-5:]
    XA = p[1][1] - p[0][1]
    AB = p[2][1] - p[1][1]
    BC = p[3][1] - p[2][1]
    CD = p[4][1] - p[3][1]
    if XA == 0 or AB == 0:
        return 0.0
    r1 = abs(AB / XA)
    r2 = abs(CD / AB)
    if 0.38 < r1 < 0.55 and 1.27 < r2 < 1.65:
        return 1.0
    return 0.0

def _gartley_pattern_inner(w):
    """Gartley proxy: AB/XA ~0.618 and CD/AB ~1.27."""
    if np.isnan(w).any() or len(w) < 20:
        return np.nan
    n = len(w)
    piv = []
    for i in range(2, n - 2):
        if _is_local_max(w, i, 2) or _is_local_min(w, i, 2):
            piv.append((i, w[i]))
    if len(piv) < 5:
        return 0.0
    p = piv[-5:]
    XA = p[1][1] - p[0][1]
    AB = p[2][1] - p[1][1]
    CD = p[4][1] - p[3][1]
    if XA == 0 or AB == 0:
        return 0.0
    r1 = abs(AB / XA)
    r2 = abs(CD / AB)
    if 0.55 < r1 < 0.68 and 1.2 < r2 < 1.4:
        return 1.0
    return 0.0

def _cypher_pattern_inner(w):
    """Cypher proxy: AB/XA ~0.382-0.618 and CD/XC ~1.272-1.414."""
    if np.isnan(w).any() or len(w) < 20:
        return np.nan
    n = len(w)
    piv = []
    for i in range(2, n - 2):
        if _is_local_max(w, i, 2) or _is_local_min(w, i, 2):
            piv.append((i, w[i]))
    if len(piv) < 5:
        return 0.0
    p = piv[-5:]
    XA = p[1][1] - p[0][1]
    AB = p[2][1] - p[1][1]
    XC = p[3][1] - p[0][1]
    CD = p[4][1] - p[3][1]
    if XA == 0 or XC == 0:
        return 0.0
    r1 = abs(AB / XA)
    r2 = abs(CD / XC)
    if 0.38 < r1 < 0.62 and 1.2 < r2 < 1.45:
        return 1.0
    return 0.0

def _ab_cd_pattern_inner(w):
    """AB=CD: equal swings (AB and CD have similar length and proportional time)."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    n = len(w)
    piv = []
    for i in range(2, n - 2):
        if _is_local_max(w, i, 2) or _is_local_min(w, i, 2):
            piv.append((i, w[i]))
    if len(piv) < 4:
        return 0.0
    p = piv[-4:]
    AB = p[1][1] - p[0][1]
    CD = p[3][1] - p[2][1]
    if AB == 0:
        return 0.0
    if 0.85 < abs(CD / AB) < 1.15:
        return 1.0
    return 0.0

def _wolfe_wave_inner(w):
    """Wolfe-wave proxy: 5-point pattern where line through (1,3) extended meets the close."""
    if np.isnan(w).any() or len(w) < 16:
        return np.nan
    n = len(w)
    piv = []
    for i in range(2, n - 2):
        if _is_local_max(w, i, 2) or _is_local_min(w, i, 2):
            piv.append((i, w[i]))
    if len(piv) < 5:
        return 0.0
    p = piv[-5:]
    slope = (p[2][1] - p[0][1]) / max(p[2][0] - p[0][0], 1)
    proj = p[0][1] + slope * (p[4][0] - p[0][0])
    if abs(p[4][1] - proj) > abs(p[0][1] - p[2][1]):
        return 1.0
    return 0.0

def _quintuple_top_inner(w):
    """5+ consecutive local maxima at similar level."""
    if np.isnan(w).any() or len(w) < 25:
        return np.nan
    n = len(w)
    maxima = [w[i] for i in range(2, n - 2) if _is_local_max(w, i, 2)]
    if len(maxima) < 5:
        return 0.0
    last5 = np.array(maxima[-5:])
    if last5.std() / max(abs(last5.mean()), 1.0) < 0.1:
        return 1.0
    return 0.0

def _rounded_top_inner(w):
    """Rounded top: smooth dome — fit quadratic, check concave-down and apex inside window."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    n = len(w)
    x = np.arange(n, dtype=float)
    p = np.polyfit(x, w, 2)
    if p[0] >= 0:
        return 0.0
    apex = -p[1] / (2.0 * p[0]) if p[0] != 0 else -1
    if 0.25 * n <= apex <= 0.75 * n:
        return 1.0
    return 0.0

def _descending_channel_break_inner(w):
    """Detect descending channel: upper line slope < 0 over window and last value broke below lower line."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    n = len(w)
    x = np.arange(n, dtype=float)
    p = np.polyfit(x, w, 1)
    if p[0] >= 0:
        return 0.0
    trend = p[0] * x + p[1]
    resid = w - trend
    sd = resid.std()
    lower = trend[-1] - 1.5 * sd
    if w[-1] < lower:
        return 1.0
    return 0.0

def _bowl_pattern_inner(w):
    """1 if quadratic fit has positive curvature (U-shape) over window."""
    if np.isnan(w).any() or len(w) < 12:
        return np.nan
    x = np.arange(len(w), dtype=float)
    p = np.polyfit(x, w, 2)
    if p[0] <= 0:
        return 0.0
    return 1.0

def _cup_with_handle_failure_inner(w):
    """1 if rounded-up (positive curvature) over window AND last value < 0."""
    if np.isnan(w).any() or len(w) < 50:
        return np.nan
    x = np.arange(len(w), dtype=float)
    p = np.polyfit(x, w, 2)
    if p[0] <= 0:
        return 0.0
    if w[-1] < 0:
        return 1.0
    return 0.0

def _cycle_phase_inner(w):
    """Approximate cycle phase: angle of dominant FFT bin at end of window. Returns radians in [-pi, pi]."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    w = _detrend(w)
    if np.std(w) == 0:
        return np.nan
    f = np.fft.rfft(w)
    p = np.abs(f) ** 2
    if len(p) < 3:
        return np.nan
    p[0] = 0
    k = int(np.argmax(p))
    if k == 0:
        return np.nan
    return float(np.angle(f[k]))

def _rolling_cycle_phase(s, n):
    return s.rolling(n, min_periods=max(n // 2, 8)).apply(_cycle_phase_inner, raw=True)

def _phase_bucket(phase):
    """Bucket phase in [-pi, pi] into 5 cycle-quadrants:
    early(rising, 0..pi/2), mid(near pi/2), late(falling, pi/2..pi), distribution(pi..-pi/2), markdown(-pi/2..0)."""
    pi = np.pi
    early = (phase > 0) & (phase <= pi / 4)
    mid = (phase > pi / 4) & (phase <= 3 * pi / 4)
    late = (phase > 3 * pi / 4) | (phase <= -3 * pi / 4)
    distribution = (phase > -3 * pi / 4) & (phase <= -pi / 4)
    markdown = (phase > -pi / 4) & (phase <= 0)
    return (early, mid, late, distribution, markdown)

def _hurst_rs_inner(w):
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 12:
        return np.nan
    lags = [2, 4, 8, 16, 32] if n >= 32 else [2, 4, 8, 16] if n >= 16 else [2, 4, 8] if n >= 8 else [2, 4]
    rs = []
    log_n = []
    for lag in lags:
        if lag >= n:
            continue
        chunks = n // lag
        if chunks == 0:
            continue
        rs_vals = []
        for c in range(chunks):
            ch = w[c * lag:(c + 1) * lag]
            mean = ch.mean()
            dev = ch - mean
            cdev = np.cumsum(dev)
            R = cdev.max() - cdev.min()
            S = ch.std()
            if S > 0:
                rs_vals.append(R / S)
        if len(rs_vals) > 0:
            rs.append(np.log(np.mean(rs_vals)))
            log_n.append(np.log(lag))
    if len(rs) < 2:
        return np.nan
    return float(np.polyfit(log_n, rs, 1)[0])

def _dfa_inner(w):
    if np.isnan(w).any():
        return np.nan
    n = len(w)
    if n < 16:
        return np.nan
    y = np.cumsum(w - w.mean())
    scales = [4, 8, 16, 32, 64] if n >= 64 else [4, 8, 16, 32] if n >= 32 else [4, 8, 16] if n >= 16 else [4, 8]
    f = []
    log_s = []
    for s in scales:
        if s >= n:
            continue
        chunks = n // s
        if chunks < 2:
            continue
        rms = []
        for c in range(chunks):
            seg = y[c * s:(c + 1) * s]
            x = np.arange(s, dtype=float)
            p = np.polyfit(x, seg, 1)
            trend = np.polyval(p, x)
            rms.append(np.sqrt(np.mean((seg - trend) ** 2)))
        if len(rms) > 0:
            f.append(np.log(np.mean(rms)))
            log_s.append(np.log(s))
    if len(f) < 2:
        return np.nan
    return float(np.polyfit(log_s, f, 1)[0])

def _acf_integral_inner(w, max_lag=60):
    if np.isnan(w).any() or len(w) < max_lag + 2:
        return np.nan
    w = w - w.mean()
    denom = (w * w).sum()
    if denom == 0:
        return np.nan
    s = 0.0
    for L in range(1, max_lag + 1):
        if L >= len(w):
            break
        s += (w[:-L] * w[L:]).sum() / denom
    return float(s)

def _lagged_corr_max_inner(w, max_lag=20):
    if np.isnan(w).any() or len(w) < max_lag + 4:
        return np.nan
    best = 0.0
    for L in range(1, max_lag + 1):
        if L >= len(w):
            break
        a = w[:-L]
        b = w[L:]
        if np.std(a) == 0 or np.std(b) == 0:
            continue
        c = np.corrcoef(a, b)[0, 1]
        if not np.isnan(c) and abs(c) > abs(best):
            best = c
    return float(best)

def _memory_half_life_inner(w):
    """Half-life of autocorrelation = log(0.5) / log(rho1)."""
    if np.isnan(w).any() or len(w) < 5:
        return np.nan
    a = w[:-1]
    b = w[1:]
    if np.std(a) == 0 or np.std(b) == 0:
        return np.nan
    rho = np.corrcoef(a, b)[0, 1]
    if rho <= 0 or rho >= 1:
        return np.nan
    return float(np.log(0.5) / np.log(rho))

def _decay_rate_inner(w, max_lag=10):
    """Slope of log|acf(L)| vs L over short lags."""
    if np.isnan(w).any() or len(w) < max_lag + 2:
        return np.nan
    w = w - w.mean()
    denom = (w * w).sum()
    if denom == 0:
        return np.nan
    lags = []
    log_acfs = []
    for L in range(1, max_lag + 1):
        if L >= len(w):
            break
        a = (w[:-L] * w[L:]).sum() / denom
        if abs(a) > 1e-06:
            lags.append(L)
            log_acfs.append(np.log(abs(a)))
    if len(lags) < 3:
        return np.nan
    return float(np.polyfit(lags, log_acfs, 1)[0])

def _arfima_d_proxy_inner(w):
    """ARFIMA d ≈ Hurst - 0.5 (heuristic)."""
    h = _hurst_rs_inner(w)
    if np.isnan(h):
        return np.nan
    return float(h - 0.5)

def _h_basket_avg_zscore_252(high, low, close):
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1)

def _h_basket_avg_zscore_504(high, low, close):
    zs = pd.concat([_rolling_zscore(sig, DDAYS_2Y, min_periods=YDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.mean(axis=1)

def _h_basket_dispersion_252(high, low, close):
    zs = pd.concat([_rolling_zscore(sig, YDAYS, min_periods=QDAYS).rename(i) for i, sig in enumerate(_basket_classical(high, low, close))], axis=1)
    return zs.std(axis=1)

def _h_basket_chronic_weak_252(high, low, close):
    out = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        out = out + (sig < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    return out.where(close.notna(), np.nan)

def _h_basket_spectral_entropy_avg_63(high, low, close):
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        out = out + sig.rolling(QDAYS, min_periods=max(QDAYS // 2, 8)).apply(_spectral_entropy_inner, raw=True).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_basket_hurst_dfa_252_avg(high, low, close):
    out = pd.Series(0.0, index=close.index)
    nb = 0
    for sig in _basket_classical(high, low, close):
        out = out + sig.rolling(YDAYS, min_periods=max(YDAYS // 2, 16)).apply(_dfa_inner, raw=True).fillna(0)
        nb += 1
    return (out / float(nb)).where(close.notna(), np.nan)

def _h_basket_lower_high_count_63(high, low, close):
    cnt = pd.Series(0.0, index=close.index)
    for sig in _basket_classical(high, low, close):
        mx = sig.rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (mx < mx.shift(QDAYS)).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)

def _h_basket_terminal_v4(high, low, close):
    lhc = _h_basket_lower_high_count_63(high, low, close)
    chro = _h_basket_chronic_weak_252(high, low, close)
    avg = _h_basket_avg_zscore_252(high, low, close)
    disp = _h_basket_dispersion_252(high, low, close)
    return ((lhc >= 4) & (chro >= 3) & (avg < -0.5) & (disp > 1.0)).astype(float).where(avg.notna(), np.nan)

def _h_basket_blowoff_collapse_252(high, low, close):
    avg = _h_basket_avg_zscore_252(high, low, close)
    had_blow = (avg.shift(1) > 2.0).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    return ((had_blow > 0) & (avg < -0.5)).astype(float).where(avg.notna(), np.nan)

def _h_basket_distribution_v4(high, low, close, volume):
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    lhc = _h_basket_lower_high_count_63(high, low, close).fillna(0)
    rng = (high - low).replace(0, np.nan)
    clv = (close - low - (high - close)) / rng
    mfv = (clv * volume).fillna(0.0)
    cmf = _safe_div(mfv.rolling(20, min_periods=7).sum(), volume.rolling(20, min_periods=7).sum())
    return (chro + lhc + (cmf < -0.1).astype(float) * 2.0).where(close.notna(), np.nan)

def _h_basket_stuck_v4(high, low, close):
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    avg = _h_basket_avg_zscore_252(high, low, close)
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    hu = _h_basket_hurst_dfa_252_avg(high, low, close).fillna(0)
    return (chro + (avg < -1.0).astype(float) * 3.0 + (disp > 1.0).astype(float) + (hu > 0.6).astype(float) * 2.0).where(close.notna(), np.nan)

def _h_basket_multi_resolution_avg(high, low, close):
    """Average of basket-z at 21d, 63d, 252d windows."""
    sigs = _basket_classical(high, low, close)
    z21 = pd.concat([_rolling_zscore(s, MDAYS, min_periods=7).rename(i) for i, s in enumerate(sigs)], axis=1).mean(axis=1)
    z63 = pd.concat([_rolling_zscore(s, QDAYS, min_periods=MDAYS).rename(i) for i, s in enumerate(sigs)], axis=1).mean(axis=1)
    z252 = pd.concat([_rolling_zscore(s, YDAYS, min_periods=QDAYS).rename(i) for i, s in enumerate(sigs)], axis=1).mean(axis=1)
    return pd.concat([z21.rename('a'), z63.rename('b'), z252.rename('c')], axis=1).mean(axis=1)

def f28_ttcf_526_spread_adjusted_cci_20_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI(20) divided by 21d HL-range spread proxy — penalizes CCI when noise is high."""
    c = _cci(high, low, close, 20)
    sp = _spread_proxy_hl(high, low, close, MDAYS)
    return _safe_div(c, 1.0 + 100.0 * sp).diff().diff().diff()

def f28_ttcf_527_volume_density_normalized_trix_15_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TRIX divided by volume density z-score — TRIX per unit of volume regime."""
    t = _trix(close, 15)
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return _safe_div(t, 1.0 + vz.abs()).diff().diff().diff()

def f28_ttcf_528_trade_intensity_weighted_cmo_14_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMO weighted by 21d-rolling volume rank in [0,1] — emphasizes high-activity bars."""
    c = _cmo(close, 14)
    w = volume.rolling(MDAYS, min_periods=7).rank(pct=True)
    return (c * w).diff().diff().diff()

def f28_ttcf_529_liquidity_weighted_cci_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI weighted by 1 / Amihud(21d) — emphasizes CCI during liquid periods."""
    c = _cci(high, low, close, 20)
    am = _amihud_proxy(close, volume, MDAYS)
    return _safe_div(c, 1.0 + am * 1000000.0).diff().diff().diff()

def f28_ttcf_530_spread_conditional_basket_above_q70_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z > 0 AND spread proxy > 252d 70th percentile — extension during wide-spread regime."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    sp = _spread_proxy_hl(high, low, close, MDAYS)
    q70 = sp.rolling(YDAYS, min_periods=QDAYS).quantile(0.7)
    return ((avg > 0) & (sp > q70)).astype(float).where(avg.notna(), np.nan).diff().diff().diff()

def f28_ttcf_531_microstructure_noise_filtered_cci_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI - effective_tick z * 0.5 (denoised CCI proxy)."""
    c = _cci(high, low, close, 20)
    et = _rolling_zscore(_effective_tick(close, MDAYS), YDAYS, min_periods=QDAYS)
    return (c - et.fillna(0) * 0.5).diff().diff().diff()

def f28_ttcf_532_effective_tick_adjusted_trix_d3(close: pd.Series) -> pd.Series:
    """TRIX divided by (1 + effective_tick / median effective_tick) — TRIX scaled by tick noise."""
    t = _trix(close, 15)
    et = _effective_tick(close, MDAYS)
    med = et.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(t, 1.0 + _safe_div(et, med)).diff().diff().diff()

def f28_ttcf_533_vwap_distance_weighted_cci_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI weighted by (1 - |close - typical_price|/typical_price) — emphasizes CCI when close ~ VWAP."""
    tp = _vwap_intraday_proxy(high, low, close, volume)
    d = (close - tp).abs() / tp.replace(0, np.nan)
    w = (1.0 - d).clip(0, 1)
    return (_cci(high, low, close, 20) * w).diff().diff().diff()

def f28_ttcf_534_high_low_impact_normalized_cmo_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CMO divided by (1 + 21d-mean of (H-L)/C) — impact-normalized CMO."""
    c = _cmo(close, 14)
    hl = _hl_range_pct(high, low, close).rolling(MDAYS, min_periods=7).mean()
    return _safe_div(c, 1.0 + 10.0 * hl).diff().diff().diff()

def f28_ttcf_535_microstructure_regime_conditional_basket_avg_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Basket-avg-z conditional on spread regime: only emit when spread > 252d median."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    sp = _spread_proxy_hl(high, low, close, MDAYS)
    med = sp.rolling(YDAYS, min_periods=QDAYS).median()
    return avg.where(sp > med, np.nan).diff().diff().diff()

def f28_ttcf_536_dominant_period_of_cci_in_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dominant period (bars) of CCI computed from 63d FFT (excluding DC)."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _dominant_period_inner).diff().diff().diff()

def f28_ttcf_537_cycle_amplitude_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cycle amplitude proxy = sqrt(peak FFT power) / N over 63d window of CCI."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _cycle_amplitude_inner).diff().diff().diff()

def f28_ttcf_538_spectral_entropy_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized spectral entropy of 63d CCI FFT spectrum (excl. DC)."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _spectral_entropy_inner).diff().diff().diff()

def f28_ttcf_539_spectral_flatness_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spectral flatness (geometric/arithmetic power mean) of 63d CCI spectrum."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _spectral_flatness_inner).diff().diff().diff()

def f28_ttcf_540_power_in_5_to_21_band_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of FFT power in periods 5..21 over 63d window of CCI (short-cycle energy)."""
    c = _cci(high, low, close, 20)
    return c.rolling(QDAYS, min_periods=max(QDAYS // 2, 8)).apply(lambda w: _band_power_inner(w, 5, 21), raw=True).diff().diff().diff()

def f28_ttcf_541_power_in_21_to_63_band_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of FFT power in periods 21..63 over 63d window of CCI (medium-cycle energy)."""
    c = _cci(high, low, close, 20)
    return c.rolling(QDAYS, min_periods=max(QDAYS // 2, 8)).apply(lambda w: _band_power_inner(w, 21, 63), raw=True).diff().diff().diff()

def f28_ttcf_542_power_ratio_short_long_band_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Short-band / Long-band power ratio of CCI over 63d — high = noisy regime."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _power_ratio_short_long_inner).diff().diff().diff()

def f28_ttcf_543_frequency_centroid_of_trix_63_d3(close: pd.Series) -> pd.Series:
    """Power-weighted mean frequency bin of TRIX FFT over 63d (spectral 'center-of-mass')."""
    return _rolling_apply(_trix(close, 15), QDAYS, _frequency_centroid_inner).diff().diff().diff()

def f28_ttcf_544_spectral_skewness_of_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of FFT-power distribution over 63d CCI spectrum."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _spectral_skewness_inner).diff().diff().diff()

def f28_ttcf_545_spectral_kurtosis_of_trix_63_d3(close: pd.Series) -> pd.Series:
    """Kurtosis of FFT-power distribution over 63d TRIX spectrum."""
    return _rolling_apply(_trix(close, 15), QDAYS, _spectral_kurtosis_inner).diff().diff().diff()

def f28_ttcf_546_three_drives_pattern_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3 successive higher-high pivots in CCI over 63d and last < third pivot."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _three_drives_pattern_inner).diff().diff().diff()

def f28_ttcf_547_bat_pattern_proxy_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if bat-pattern Fibonacci proxy detected over 63d CCI pivots."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _bat_pattern_inner).diff().diff().diff()

def f28_ttcf_548_gartley_pattern_proxy_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Gartley-pattern Fibonacci proxy detected over 63d CCI pivots."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _gartley_pattern_inner).diff().diff().diff()

def f28_ttcf_549_cypher_pattern_proxy_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Cypher-pattern proxy detected over 63d CCI pivots."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _cypher_pattern_inner).diff().diff().diff()

def f28_ttcf_550_ab_cd_pattern_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if AB=CD equal-swings pattern detected over 63d CCI pivots."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _ab_cd_pattern_inner).diff().diff().diff()

def f28_ttcf_551_wolfe_wave_pattern_proxy_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Wolfe-wave 5-point pattern proxy detected over 63d CCI pivots."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _wolfe_wave_inner).diff().diff().diff()

def f28_ttcf_552_quintuple_top_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5+ similar-level local maxima in CCI over 63d (rel-std < 0.10) — quintuple top."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _quintuple_top_inner).diff().diff().diff()

def f28_ttcf_553_rounded_top_in_cci_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if quadratic fit of CCI is concave-down with apex inside middle 50% of 63d window."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _rounded_top_inner).diff().diff().diff()

def f28_ttcf_554_cci_descending_channel_break_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if CCI shows descending-channel pattern over 63d AND last value broke lower envelope."""
    return _rolling_apply(_cci(high, low, close, 20), QDAYS, _descending_channel_break_inner).diff().diff().diff()

def f28_ttcf_555_cci_inside_day_at_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's high < yesterday's high AND today's low > yesterday's low AND close near 252d-high (within 5%)."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    near_high = close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max()
    return (inside & near_high).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_556_cci_in_early_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d mean of CCI restricted to early-cycle phase bars (FFT phase in [0, pi/4])."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    early, _, _, _, _ = _phase_bucket(ph)
    return c.where(early).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_557_cci_in_mid_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d mean of CCI restricted to mid-cycle phase bars (phase in (pi/4, 3pi/4])."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    _, mid, _, _, _ = _phase_bucket(ph)
    return c.where(mid).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_558_cci_in_late_cycle_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d mean of CCI restricted to late-cycle phase bars (phase > 3pi/4 or <= -3pi/4)."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    _, _, late, _, _ = _phase_bucket(ph)
    return c.where(late).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_559_cci_in_distribution_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d mean of CCI restricted to distribution-phase bars (phase in (-3pi/4, -pi/4])."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    _, _, _, distribution, _ = _phase_bucket(ph)
    return c.where(distribution).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_560_cci_in_markdown_phase_avg_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d mean of CCI restricted to markdown-phase bars (phase in (-pi/4, 0])."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    _, _, _, _, markdown = _phase_bucket(ph)
    return c.where(markdown).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_561_cycle_conditional_cci_ob_threshold_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frac of past 252d where CCI > 100 AND late-cycle phase — phase-conditioned OB."""
    c = _cci(high, low, close, 20)
    ph = _rolling_cycle_phase(c, QDAYS)
    _, _, late, _, _ = _phase_bucket(ph)
    cond = ((c > 100.0) & late).astype(float)
    return cond.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_562_cycle_conditional_basket_dwell_ratio_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: (basket-avg-z > 0 dwell in distribution phase) / (basket-avg-z > 0 dwell overall) over 252d."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    ph = _rolling_cycle_phase(avg, QDAYS)
    _, _, _, distribution, _ = _phase_bucket(ph)
    pos = avg > 0
    pos_d = (pos & distribution).astype(float)
    pos_f = pos.astype(float)
    return _safe_div(pos_d.rolling(YDAYS, min_periods=QDAYS).sum(), pos_f.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f28_ttcf_563_cycle_phase_persistence_basket_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252d where phase change |Δphase| < pi/8 (stable cycle)."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    ph = _rolling_cycle_phase(avg, QDAYS)
    dph = (ph - ph.shift(1)).abs()
    stable = (dph < np.pi / 8).astype(float)
    return stable.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f28_ttcf_564_cycle_phase_shift_basket_indicator_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if |Δphase| > pi/2 over past 21d (major phase shift)."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    ph = _rolling_cycle_phase(avg, QDAYS)
    shift = (ph - ph.shift(MDAYS)).abs()
    return (shift > np.pi / 2).astype(float).where(ph.notna(), np.nan).diff().diff().diff()

def f28_ttcf_565_cycle_end_basket_behavior_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg-z just transitioned from late-cycle phase to distribution phase (terminal indicator)."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    ph = _rolling_cycle_phase(avg, QDAYS)
    _, _, late, distribution, _ = _phase_bucket(ph)
    return (late.shift(1).fillna(False) & distribution).astype(float).where(ph.notna(), np.nan).diff().diff().diff()

def f28_ttcf_566_cci_hurst_rs_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of CCI over 252d window."""
    return _cci(high, low, close, 20).rolling(YDAYS, min_periods=max(YDAYS // 2, 16)).apply(_hurst_rs_inner, raw=True).diff().diff().diff()

def f28_ttcf_567_trix_hurst_dfa_504_d3(close: pd.Series) -> pd.Series:
    """DFA exponent of TRIX over 504d window."""
    return _trix(close, 15).rolling(DDAYS_2Y, min_periods=max(DDAYS_2Y // 2, 32)).apply(_dfa_inner, raw=True).diff().diff().diff()

def f28_ttcf_568_cmo_hurst_dfa_1260_d3(close: pd.Series) -> pd.Series:
    """DFA exponent of CMO over 1260d (5y) window."""
    return _cmo(close, 14).rolling(DDAYS_5Y, min_periods=max(DDAYS_5Y // 2, 64)).apply(_dfa_inner, raw=True).diff().diff().diff()

def f28_ttcf_569_cci_acf_integral_long_range_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of ACF(1)..ACF(60) of CCI over 252d (long-range dependence)."""
    return _cci(high, low, close, 20).rolling(YDAYS, min_periods=max(YDAYS // 2, 64)).apply(lambda w: _acf_integral_inner(w, 60), raw=True).diff().diff().diff()

def f28_ttcf_570_trix_lagged_corr_profile_max_lag_63_d3(close: pd.Series) -> pd.Series:
    """Max(|ACF(L)|) for L in 1..20 over 63d window of TRIX — dominant short-lag persistence."""
    return _trix(close, 15).rolling(QDAYS, min_periods=max(QDAYS // 2, 20)).apply(lambda w: _lagged_corr_max_inner(w, 20), raw=True).diff().diff().diff()

def f28_ttcf_571_cci_memory_half_life_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-life of CCI lag-1 autocorrelation over 252d (in bars)."""
    return _cci(high, low, close, 20).rolling(YDAYS, min_periods=max(YDAYS // 2, 16)).apply(_memory_half_life_inner, raw=True).diff().diff().diff()

def f28_ttcf_572_trix_decay_rate_autocorr_63_d3(close: pd.Series) -> pd.Series:
    """Slope of log|ACF| vs lag over short lags (1..10) for TRIX over 63d."""
    return _trix(close, 15).rolling(QDAYS, min_periods=max(QDAYS // 2, 12)).apply(lambda w: _decay_rate_inner(w, 10), raw=True).diff().diff().diff()

def f28_ttcf_573_cci_arfima_d_proxy_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ARFIMA-d proxy = Hurst - 0.5 over 252d window of CCI."""
    return _cci(high, low, close, 20).rolling(YDAYS, min_periods=max(YDAYS // 2, 16)).apply(_arfima_d_proxy_inner, raw=True).diff().diff().diff()

def f28_ttcf_574_basket_multi_scale_hurst_stability_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std across basket of 252d-Hurst-DFA (lower = more stable across indicators)."""
    out = []
    for s in _basket_classical(high, low, close):
        out.append(s.rolling(YDAYS, min_periods=max(YDAYS // 2, 16)).apply(_dfa_inner, raw=True))
    df = pd.concat([o.rename(i) for i, o in enumerate(out)], axis=1)
    return df.std(axis=1).diff().diff().diff()

def f28_ttcf_575_basket_memory_regime_indicator_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if basket-avg Hurst-DFA > 0.65 over 252d (persistent long-memory regime)."""
    avg_h = _h_basket_hurst_dfa_252_avg(high, low, close)
    return (avg_h > 0.65).astype(float).where(avg_h.notna(), np.nan).diff().diff().diff()

def f28_ttcf_576_cci_key_reversal_day_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Key-reversal day in CCI: today's high > yesterday's high but CCI closes < yesterday's CCI."""
    c = _cci(high, low, close, 20)
    return ((high > high.shift(1)) & (c < c.shift(1)) & (c.shift(1) > 100.0)).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_577_trix_hook_failure_at_top_indicator_d3(close: pd.Series) -> pd.Series:
    """TRIX rose then turned down within 2 bars AND prior TRIX > 252d 90th pct."""
    t = _trix(close, 15)
    q90 = t.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    rose = t.shift(2) < t.shift(1)
    fell = t.shift(1) > t
    extreme = t.shift(1) > q90.shift(1)
    return (rose & fell & extreme).astype(float).where(t.notna(), np.nan).diff().diff().diff()

def f28_ttcf_578_cci_cookie_cutter_setup_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI tight-range 5d (max-min < 50) after extreme (CCI > 150 5d ago)."""
    c = _cci(high, low, close, 20)
    tight = c.rolling(WDAYS, min_periods=2).max() - c.rolling(WDAYS, min_periods=2).min() < 50.0
    prior_ext = c.shift(WDAYS) > 150.0
    return (tight & prior_ext).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_579_trix_bowl_pattern_detection_63_d3(close: pd.Series) -> pd.Series:
    """1 if TRIX shows U-shape over 63d (concave-up quadratic fit) — inverse of rounded top."""
    return _trix(close, 15).rolling(QDAYS, min_periods=MDAYS).apply(_bowl_pattern_inner, raw=True).diff().diff().diff()

def f28_ttcf_580_cci_cup_with_handle_failure_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cup with handle (rounded-bottom CCI then break-down): 1 if rounded-bottom 50d then current CCI<0."""
    return _cci(high, low, close, 20).rolling(QDAYS, min_periods=50).apply(_cup_with_handle_failure_inner, raw=True).diff().diff().diff()

def f28_ttcf_581_cci_knife_edge_break_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI fell from > 200 to < 0 within 5 bars — knife-edge break."""
    c = _cci(high, low, close, 20)
    prior_high = c.shift(WDAYS) > 200.0
    now_low = c < 0
    return (prior_high & now_low).astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_582_trix_extension_then_failure_indicator_d3(close: pd.Series) -> pd.Series:
    """TRIX > 252d q95 in past 21 bars AND TRIX now < 0 — extension-then-failure."""
    t = _trix(close, 15)
    q95 = t.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    prior_ext = (t.shift(1) > q95.shift(1)).rolling(MDAYS, min_periods=1).max().fillna(0)
    return ((prior_ext > 0) & (t < 0)).astype(float).where(t.notna(), np.nan).diff().diff().diff()

def f28_ttcf_583_cci_multi_bar_reversal_pattern_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3 consecutive bars: rising CCI then 2 consecutive falling — sharp reversal."""
    c = _cci(high, low, close, 20)
    cond = (c.shift(3) < c.shift(2)) & (c.shift(2) > c.shift(1)) & (c.shift(1) > c)
    return cond.astype(float).where(c.notna(), np.nan).diff().diff().diff()

def f28_ttcf_584_cci_outside_day_at_high_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Outside day (high > prev_high AND low < prev_low) within 5% of 252d-high — outside-day-at-top."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    near_high = close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max()
    return (outside & near_high).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_585_trix_reversal_day_at_extreme_indicator_d3(close: pd.Series) -> pd.Series:
    """TRIX-down day after TRIX was > 252d q95 AND TRIX-now < TRIX-yest — reversal at extreme."""
    t = _trix(close, 15)
    q95 = t.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    prior_ext = t.shift(1) > q95.shift(1)
    return (prior_ext & (t < t.shift(1))).astype(float).where(t.notna(), np.nan).diff().diff().diff()

def f28_ttcf_586_batch_4_basket_modern_aggregate_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Modern-aggregate v4: 252d z-score of (avg-z + dispersion + chronic-weak)."""
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    raw = avg + disp + chro
    return _rolling_zscore(raw, YDAYS, min_periods=QDAYS).diff().diff().diff()

def f28_ttcf_587_basket_universe_wide_topping_auc_optimized_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AUC-oriented topping score = (avg-z > 0) * dispersion + chronic-weak/6."""
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    return ((avg > 0).astype(float) * disp + chro / 6.0).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_588_basket_universe_wide_stuck_prediction_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck-prediction v4 = stuck_v4 (uses chronic + dispersion + Hurst)."""
    return _h_basket_stuck_v4(high, low, close).diff().diff().diff()

def f28_ttcf_589_basket_cross_batch_consensus_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cross-batch consensus: avg of (avg-z + multi-resolution-avg) — high consensus across windows."""
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    mra = _h_basket_multi_resolution_avg(high, low, close).fillna(0)
    return ((avg + mra) / 2.0).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_590_basket_multi_feature_alignment_score_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Alignment score = 1 / (1 + dispersion). High = features aligned."""
    disp = _h_basket_dispersion_252(high, low, close)
    return (1.0 / (1.0 + disp.fillna(0))).diff().diff().diff()

def f28_ttcf_591_basket_orthogonal_batch_4_aggregate_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Orthogonal aggregate = avg-z - multi-resolution-avg (residual across windows)."""
    avg = _h_basket_avg_zscore_252(high, low, close)
    mra = _h_basket_multi_resolution_avg(high, low, close)
    return (avg - mra).diff().diff().diff()

def f28_ttcf_592_basket_cross_pattern_terminal_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal-v4 score = terminal_v4_state * 10 + blowoff_collapse * 5 + chronic-weak."""
    tv = _h_basket_terminal_v4(high, low, close).fillna(0) * 10.0
    bc = _h_basket_blowoff_collapse_252(high, low, close).fillna(0) * 5.0
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    return (tv + bc + chro).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_593_basket_multi_resolution_stuck_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Multi-resolution stuck: stuck_v4 + |multi-res-avg| when multi-res-avg < 0."""
    sk = _h_basket_stuck_v4(high, low, close).fillna(0)
    mra = _h_basket_multi_resolution_avg(high, low, close).fillna(0)
    return (sk + mra.abs() * (mra < 0).astype(float)).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_594_basket_final_topping_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final topping master v4 = terminal_v4 * 8 + (avg-z > 1) * dispersion * 4 + chronic-weak * 2."""
    tv = _h_basket_terminal_v4(high, low, close).fillna(0) * 8.0
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    return (tv + (avg > 1.0).astype(float) * disp * 4.0 + chro * 2.0).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_595_basket_final_breakdown_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final breakdown master v4 = lower-high-count * 3 + chronic-weak * 2 + (avg-z < -1) * 5."""
    lhc = _h_basket_lower_high_count_63(high, low, close).fillna(0) * 3.0
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0) * 2.0
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    return (lhc + chro + (avg < -1.0).astype(float) * 5.0).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_596_basket_final_blowoff_collapse_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final blowoff-collapse master v4 = blowoff_collapse * 10 + post-peak-velocity * 5."""
    bc = _h_basket_blowoff_collapse_252(high, low, close).fillna(0) * 10.0
    avg = _h_basket_avg_zscore_252(high, low, close)
    pmax = avg.rolling(QDAYS, min_periods=MDAYS).max()
    pv = ((pmax - avg) / float(QDAYS)).fillna(0) * 5.0
    return (bc + pv).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_597_basket_final_distribution_master_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final distribution master v4 = distribution_v4 * 3 + chronic-weak * 2 + dispersion."""
    di = _h_basket_distribution_v4(high, low, close, volume).fillna(0) * 3.0
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0) * 2.0
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    return (di + chro + disp).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_598_basket_stuck_probability_proxy_v4_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stuck-probability v4 = normalize(stuck_v4) by 252d max → [0,1] proxy."""
    sk = _h_basket_stuck_v4(high, low, close)
    mx = sk.rolling(YDAYS, min_periods=QDAYS).max().replace(0, np.nan)
    return (sk / mx).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_599_absolute_terminal_basket_master_v4_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if terminal_v4 = 1 AND blowoff_collapse = 1 AND stuck_v4 >= 6 — absolute terminal master v4."""
    tv = _h_basket_terminal_v4(high, low, close).fillna(0)
    bc = _h_basket_blowoff_collapse_252(high, low, close).fillna(0)
    sk = _h_basket_stuck_v4(high, low, close).fillna(0)
    return ((tv > 0) & (bc > 0) & (sk >= 6.0)).astype(float).where(close.notna(), np.nan).diff().diff().diff()

def f28_ttcf_600_basket_extended_universe_v4_aggregate_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended-universe aggregate v4 = topping_master + breakdown_master + blowoff_master + distribution_master, scaled by 1/4."""
    tv = _h_basket_terminal_v4(high, low, close).fillna(0) * 8.0
    avg = _h_basket_avg_zscore_252(high, low, close).fillna(0)
    disp = _h_basket_dispersion_252(high, low, close).fillna(0)
    chro = _h_basket_chronic_weak_252(high, low, close).fillna(0)
    lhc = _h_basket_lower_high_count_63(high, low, close).fillna(0)
    bc = _h_basket_blowoff_collapse_252(high, low, close).fillna(0)
    di = _h_basket_distribution_v4(high, low, close, volume).fillna(0)
    tm = tv + (avg > 1.0).astype(float) * disp * 4.0 + chro * 2.0
    bm = lhc * 3.0 + chro * 2.0 + (avg < -1.0).astype(float) * 5.0
    bo = bc * 10.0
    dm = di * 3.0 + chro * 2.0 + disp
    return ((tm + bm + bo + dm) / 4.0).where(close.notna(), np.nan).diff().diff().diff()
TRIX_TSI_CCI_FAMILY_D3_REGISTRY_526_600 = {'f28_ttcf_526_spread_adjusted_cci_20_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_526_spread_adjusted_cci_20_d3}, 'f28_ttcf_527_volume_density_normalized_trix_15_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_527_volume_density_normalized_trix_15_d3}, 'f28_ttcf_528_trade_intensity_weighted_cmo_14_d3': {'inputs': ['close', 'volume'], 'func': f28_ttcf_528_trade_intensity_weighted_cmo_14_d3}, 'f28_ttcf_529_liquidity_weighted_cci_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_529_liquidity_weighted_cci_d3}, 'f28_ttcf_530_spread_conditional_basket_above_q70_state_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_530_spread_conditional_basket_above_q70_state_d3}, 'f28_ttcf_531_microstructure_noise_filtered_cci_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_531_microstructure_noise_filtered_cci_d3}, 'f28_ttcf_532_effective_tick_adjusted_trix_d3': {'inputs': ['close'], 'func': f28_ttcf_532_effective_tick_adjusted_trix_d3}, 'f28_ttcf_533_vwap_distance_weighted_cci_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_533_vwap_distance_weighted_cci_d3}, 'f28_ttcf_534_high_low_impact_normalized_cmo_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_534_high_low_impact_normalized_cmo_d3}, 'f28_ttcf_535_microstructure_regime_conditional_basket_avg_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_535_microstructure_regime_conditional_basket_avg_d3}, 'f28_ttcf_536_dominant_period_of_cci_in_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_536_dominant_period_of_cci_in_63_d3}, 'f28_ttcf_537_cycle_amplitude_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_537_cycle_amplitude_of_cci_63_d3}, 'f28_ttcf_538_spectral_entropy_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_538_spectral_entropy_of_cci_63_d3}, 'f28_ttcf_539_spectral_flatness_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_539_spectral_flatness_of_cci_63_d3}, 'f28_ttcf_540_power_in_5_to_21_band_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_540_power_in_5_to_21_band_of_cci_63_d3}, 'f28_ttcf_541_power_in_21_to_63_band_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_541_power_in_21_to_63_band_of_cci_63_d3}, 'f28_ttcf_542_power_ratio_short_long_band_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_542_power_ratio_short_long_band_cci_63_d3}, 'f28_ttcf_543_frequency_centroid_of_trix_63_d3': {'inputs': ['close'], 'func': f28_ttcf_543_frequency_centroid_of_trix_63_d3}, 'f28_ttcf_544_spectral_skewness_of_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_544_spectral_skewness_of_cci_63_d3}, 'f28_ttcf_545_spectral_kurtosis_of_trix_63_d3': {'inputs': ['close'], 'func': f28_ttcf_545_spectral_kurtosis_of_trix_63_d3}, 'f28_ttcf_546_three_drives_pattern_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_546_three_drives_pattern_in_cci_63_d3}, 'f28_ttcf_547_bat_pattern_proxy_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_547_bat_pattern_proxy_in_cci_63_d3}, 'f28_ttcf_548_gartley_pattern_proxy_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_548_gartley_pattern_proxy_in_cci_63_d3}, 'f28_ttcf_549_cypher_pattern_proxy_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_549_cypher_pattern_proxy_in_cci_63_d3}, 'f28_ttcf_550_ab_cd_pattern_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_550_ab_cd_pattern_in_cci_63_d3}, 'f28_ttcf_551_wolfe_wave_pattern_proxy_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_551_wolfe_wave_pattern_proxy_in_cci_63_d3}, 'f28_ttcf_552_quintuple_top_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_552_quintuple_top_in_cci_63_d3}, 'f28_ttcf_553_rounded_top_in_cci_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_553_rounded_top_in_cci_63_d3}, 'f28_ttcf_554_cci_descending_channel_break_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_554_cci_descending_channel_break_indicator_d3}, 'f28_ttcf_555_cci_inside_day_at_high_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_555_cci_inside_day_at_high_indicator_d3}, 'f28_ttcf_556_cci_in_early_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_556_cci_in_early_cycle_phase_avg_252_d3}, 'f28_ttcf_557_cci_in_mid_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_557_cci_in_mid_cycle_phase_avg_252_d3}, 'f28_ttcf_558_cci_in_late_cycle_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_558_cci_in_late_cycle_phase_avg_252_d3}, 'f28_ttcf_559_cci_in_distribution_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_559_cci_in_distribution_phase_avg_252_d3}, 'f28_ttcf_560_cci_in_markdown_phase_avg_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_560_cci_in_markdown_phase_avg_252_d3}, 'f28_ttcf_561_cycle_conditional_cci_ob_threshold_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_561_cycle_conditional_cci_ob_threshold_252_d3}, 'f28_ttcf_562_cycle_conditional_basket_dwell_ratio_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_562_cycle_conditional_basket_dwell_ratio_252_d3}, 'f28_ttcf_563_cycle_phase_persistence_basket_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_563_cycle_phase_persistence_basket_252_d3}, 'f28_ttcf_564_cycle_phase_shift_basket_indicator_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_564_cycle_phase_shift_basket_indicator_252_d3}, 'f28_ttcf_565_cycle_end_basket_behavior_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_565_cycle_end_basket_behavior_indicator_d3}, 'f28_ttcf_566_cci_hurst_rs_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_566_cci_hurst_rs_252_d3}, 'f28_ttcf_567_trix_hurst_dfa_504_d3': {'inputs': ['close'], 'func': f28_ttcf_567_trix_hurst_dfa_504_d3}, 'f28_ttcf_568_cmo_hurst_dfa_1260_d3': {'inputs': ['close'], 'func': f28_ttcf_568_cmo_hurst_dfa_1260_d3}, 'f28_ttcf_569_cci_acf_integral_long_range_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_569_cci_acf_integral_long_range_252_d3}, 'f28_ttcf_570_trix_lagged_corr_profile_max_lag_63_d3': {'inputs': ['close'], 'func': f28_ttcf_570_trix_lagged_corr_profile_max_lag_63_d3}, 'f28_ttcf_571_cci_memory_half_life_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_571_cci_memory_half_life_252_d3}, 'f28_ttcf_572_trix_decay_rate_autocorr_63_d3': {'inputs': ['close'], 'func': f28_ttcf_572_trix_decay_rate_autocorr_63_d3}, 'f28_ttcf_573_cci_arfima_d_proxy_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_573_cci_arfima_d_proxy_252_d3}, 'f28_ttcf_574_basket_multi_scale_hurst_stability_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_574_basket_multi_scale_hurst_stability_252_d3}, 'f28_ttcf_575_basket_memory_regime_indicator_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_575_basket_memory_regime_indicator_252_d3}, 'f28_ttcf_576_cci_key_reversal_day_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_576_cci_key_reversal_day_indicator_d3}, 'f28_ttcf_577_trix_hook_failure_at_top_indicator_d3': {'inputs': ['close'], 'func': f28_ttcf_577_trix_hook_failure_at_top_indicator_d3}, 'f28_ttcf_578_cci_cookie_cutter_setup_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_578_cci_cookie_cutter_setup_indicator_d3}, 'f28_ttcf_579_trix_bowl_pattern_detection_63_d3': {'inputs': ['close'], 'func': f28_ttcf_579_trix_bowl_pattern_detection_63_d3}, 'f28_ttcf_580_cci_cup_with_handle_failure_63_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_580_cci_cup_with_handle_failure_63_d3}, 'f28_ttcf_581_cci_knife_edge_break_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_581_cci_knife_edge_break_indicator_d3}, 'f28_ttcf_582_trix_extension_then_failure_indicator_d3': {'inputs': ['close'], 'func': f28_ttcf_582_trix_extension_then_failure_indicator_d3}, 'f28_ttcf_583_cci_multi_bar_reversal_pattern_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_583_cci_multi_bar_reversal_pattern_indicator_d3}, 'f28_ttcf_584_cci_outside_day_at_high_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_584_cci_outside_day_at_high_indicator_d3}, 'f28_ttcf_585_trix_reversal_day_at_extreme_indicator_d3': {'inputs': ['close'], 'func': f28_ttcf_585_trix_reversal_day_at_extreme_indicator_d3}, 'f28_ttcf_586_batch_4_basket_modern_aggregate_zscore_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_586_batch_4_basket_modern_aggregate_zscore_252_d3}, 'f28_ttcf_587_basket_universe_wide_topping_auc_optimized_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_587_basket_universe_wide_topping_auc_optimized_score_d3}, 'f28_ttcf_588_basket_universe_wide_stuck_prediction_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_588_basket_universe_wide_stuck_prediction_v4_score_d3}, 'f28_ttcf_589_basket_cross_batch_consensus_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_589_basket_cross_batch_consensus_score_d3}, 'f28_ttcf_590_basket_multi_feature_alignment_score_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_590_basket_multi_feature_alignment_score_252_d3}, 'f28_ttcf_591_basket_orthogonal_batch_4_aggregate_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_591_basket_orthogonal_batch_4_aggregate_d3}, 'f28_ttcf_592_basket_cross_pattern_terminal_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_592_basket_cross_pattern_terminal_v4_score_d3}, 'f28_ttcf_593_basket_multi_resolution_stuck_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_593_basket_multi_resolution_stuck_v4_score_d3}, 'f28_ttcf_594_basket_final_topping_master_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_594_basket_final_topping_master_v4_score_d3}, 'f28_ttcf_595_basket_final_breakdown_master_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_595_basket_final_breakdown_master_v4_score_d3}, 'f28_ttcf_596_basket_final_blowoff_collapse_master_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_596_basket_final_blowoff_collapse_master_v4_score_d3}, 'f28_ttcf_597_basket_final_distribution_master_v4_score_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_597_basket_final_distribution_master_v4_score_d3}, 'f28_ttcf_598_basket_stuck_probability_proxy_v4_score_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_598_basket_stuck_probability_proxy_v4_score_d3}, 'f28_ttcf_599_absolute_terminal_basket_master_v4_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f28_ttcf_599_absolute_terminal_basket_master_v4_indicator_d3}, 'f28_ttcf_600_basket_extended_universe_v4_aggregate_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f28_ttcf_600_basket_extended_universe_v4_aggregate_d3}}