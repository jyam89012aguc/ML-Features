"""sma_ema_extension_dynamics base features 151-225 - Pipeline 1b-technical.

75 NEW gap-fill hypotheses extending the smae family with advanced adaptive MAs,
volume-weighted MAs, higher-order derivatives, touch/rejection metrics,
regime-conditional distances, multi-horizon consensus, MA-of-MA, displaced MAs,
and composite scores.

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


# ---------------------------- basic MA helpers ----------------------------

def _sma(s, n, mp=None):
    if mp is None:
        mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _wma(s, n):
    def _f(x):
        valid = ~np.isnan(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        w = np.arange(1, len(x) + 1, dtype=float)
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


# ---------------------------- advanced MA helpers ----------------------------

def _alma(s, n, sigma=6.0, offset=0.85):
    def _f(x):
        valid = ~np.isnan(x)
        L = len(x)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        m = offset * (L - 1)
        w = np.exp(-((np.arange(L) - m) ** 2) / (2 * (L / sigma) ** 2))
        xx = np.where(valid, x, 0.0)
        ww = np.where(valid, w[-len(x):], 0.0)
        ws = ww.sum()
        if ws == 0:
            return np.nan
        return float((xx * ww).sum() / ws)
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _zlema(s, n):
    lag = max((n - 1) // 2, 1)
    de_lagged = 2.0 * s - s.shift(lag)
    return _ema(de_lagged, n)


def _t3(s, n, v=0.7):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    e4 = _ema(e3, n)
    e5 = _ema(e4, n)
    e6 = _ema(e5, n)
    c1 = -v ** 3
    c2 = 3 * v ** 2 + 3 * v ** 3
    c3 = -6 * v ** 2 - 3 * v - 3 * v ** 3
    c4 = 1 + 3 * v + v ** 3 + 3 * v ** 2
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _mcginley(s, n):
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    md = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            md = float(v)
            initialized = True
            out[i] = md
        else:
            denom = n * (float(v) / md) ** 4 if md > 0 else float(n)
            if denom == 0:
                denom = float(n)
            md = md + (float(v) - md) / denom
            out[i] = md
    return pd.Series(out, index=s.index)


def _jma(s, n, phase=0.0, power=2.0):
    """Simplified Jurik-style MA: triple EWM cascade with phase-shifted feedback.
    Not the proprietary JMA exactly, but a numpy-only adaptive smoother."""
    beta = 0.45 * (n - 1) / (0.45 * (n - 1) + 2.0)
    alpha = beta ** power
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    e0 = np.nan
    e1 = np.nan
    jma = np.nan
    initialized = False
    phase_ratio = 1.5 if phase > 100 else (0.5 if phase < -100 else phase / 100 + 1.5)
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            e0 = float(v); e1 = 0.0; jma = float(v)
            initialized = True
            out[i] = jma
        else:
            e0 = (1.0 - alpha) * float(v) + alpha * e0
            e1 = (float(v) - e0) * (1.0 - beta) + beta * e1
            jma_next = e0 + phase_ratio * e1
            jma = (jma_next - jma) * (1.0 - alpha) ** 2 + jma
            out[i] = jma
    return pd.Series(out, index=s.index)


def _cmo(s, n):
    diff = s.diff()
    up = diff.clip(lower=0.0).rolling(n, min_periods=max(n // 3, 2)).sum()
    dn = (-diff.clip(upper=0.0)).rolling(n, min_periods=max(n // 3, 2)).sum()
    return (up - dn) / (up + dn).replace(0, np.nan)


def _vidya(s, n=9, alpha_n=9):
    """Tushar Chande Variable Index Dynamic Average using CMO as volatility index."""
    cmo_abs = _cmo(s, alpha_n).abs()
    k = 2.0 / (n + 1)
    arr = s.values
    cmo_arr = cmo_abs.fillna(0.0).values
    out = np.full(len(arr), np.nan, dtype=float)
    md = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            md = float(v)
            initialized = True
            out[i] = md
        else:
            alpha = k * cmo_arr[i]
            md = alpha * float(v) + (1.0 - alpha) * md
            out[i] = md
    return pd.Series(out, index=s.index)


def _laguerre(s, gamma=0.5):
    """Ehlers adaptive Laguerre filter (fixed gamma)."""
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    L0 = L1 = L2 = L3 = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            L0 = L1 = L2 = L3 = float(v)
            initialized = True
            out[i] = float(v)
        else:
            L0_new = (1.0 - gamma) * float(v) + gamma * L0
            L1_new = -gamma * L0_new + L0 + gamma * L1
            L2_new = -gamma * L1_new + L1 + gamma * L2
            L3_new = -gamma * L2_new + L2 + gamma * L3
            L0, L1, L2, L3 = L0_new, L1_new, L2_new, L3_new
            out[i] = (L0 + 2.0 * L1 + 2.0 * L2 + L3) / 6.0
    return pd.Series(out, index=s.index)


def _mama_proxy(s, alpha=0.05):
    """MESA Adaptive proxy: an EMA with very slow alpha, approximating MAMA in steady state."""
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    md = np.nan
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            md = float(v)
            initialized = True
        else:
            md = alpha * float(v) + (1.0 - alpha) * md
        out[i] = md
    return pd.Series(out, index=s.index)


def _kalman_smoothed(s, q=1e-3, r=1e-2):
    """Scalar Kalman filter (random-walk model) - PIT-safe causal filter."""
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    x = np.nan
    p = 1.0
    initialized = False
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            continue
        if not initialized:
            x = float(v); p = 1.0
            initialized = True
            out[i] = x
        else:
            p = p + q
            k = p / (p + r)
            x = x + k * (float(v) - x)
            p = (1.0 - k) * p
            out[i] = x
    return pd.Series(out, index=s.index)


def _savgol_causal(s, window=21, poly=3):
    """Causal (right-anchored) Savitzky-Golay smoother. Fits poly on past `window` points,
    evaluates at the last index. PIT-safe."""
    coeffs_cache = {}
    def _f(w):
        valid = ~np.isnan(w)
        n_valid = int(valid.sum())
        if n_valid < max(poly + 2, window // 3):
            return np.nan
        if valid.all():
            y = w
            x = np.arange(len(w), dtype=float)
        else:
            y = w[valid]
            x = np.arange(len(w), dtype=float)[valid]
        try:
            coefs = np.polyfit(x, y, deg=poly)
        except Exception:
            return np.nan
        return float(np.polyval(coefs, float(len(w) - 1)))
    return s.rolling(window, min_periods=max(poly + 2, window // 3)).apply(_f, raw=True)


# ---------------------------- volume-weighted helpers ----------------------------

def _vwma(price, volume, n):
    mp = max(n // 3, 2)
    pv = (price * volume).rolling(n, min_periods=mp).sum()
    v = volume.rolling(n, min_periods=mp).sum()
    return _safe_div(pv, v)


# ---------------------------- composite scaffolding ----------------------------

def _consecutive_same_sign(s: pd.Series) -> pd.Series:
    arr = s.values
    out = np.full(len(arr), np.nan, dtype=float)
    run = 0
    last_sign = 0
    for i in range(len(arr)):
        v = arr[i]
        if np.isnan(v):
            run = 0; last_sign = 0
            out[i] = np.nan
            continue
        sgn = 1 if v > 0 else (-1 if v < 0 else 0)
        if sgn == 0:
            run = 0; last_sign = 0
            out[i] = 0.0
        elif sgn == last_sign:
            run += 1
            out[i] = float(run) * sgn
        else:
            run = 1; last_sign = sgn
            out[i] = float(run) * sgn
    return pd.Series(out, index=s.index)


def _bars_since_event(event_bool: pd.Series) -> pd.Series:
    arr = event_bool.fillna(False).astype(bool).values
    out = np.full(len(arr), np.nan, dtype=float)
    last = -1
    for i in range(len(arr)):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=event_bool.index)


# ============================================================================
# BUCKET A - Advanced adaptive MA distance metrics (151-160)
# ============================================================================

def f11_smae_151_log_dist_above_jma_50(close: pd.Series) -> pd.Series:
    """Log distance of close above a Jurik-style adaptive MA (n=50)."""
    ma = _jma(close, 50)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_152_log_dist_above_vidya_50(close: pd.Series) -> pd.Series:
    """Log distance of close above Chande VIDYA (n=50, alpha-n=14)."""
    ma = _vidya(close, n=50, alpha_n=14)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_153_log_dist_above_alma_50_offset85_sigma6(close: pd.Series) -> pd.Series:
    """Log distance above Arnaud Legoux MA (n=50, offset=0.85, sigma=6) - non-defaults."""
    ma = _alma(close, 50, sigma=6.0, offset=0.85)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_154_log_dist_above_zlema_200_long(close: pd.Series) -> pd.Series:
    """Long-horizon zero-lag EMA distance (n=200) - extends ZLEMA50 covered earlier."""
    ma = _zlema(close, 200)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_155_log_dist_above_t3_200_long(close: pd.Series) -> pd.Series:
    """Long-horizon Tillson T3 distance (n=200, v=0.7)."""
    ma = _t3(close, 200, v=0.7)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_156_log_dist_above_mcginley_dynamic_200(close: pd.Series) -> pd.Series:
    """McGinley Dynamic (n=200) distance - long-horizon McGinley extends 010."""
    ma = _mcginley(close, 200)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_157_log_dist_above_laguerre_filter_gamma5(close: pd.Series) -> pd.Series:
    """Ehlers Laguerre filter (gamma=0.5) distance - heavy adaptive smoothing."""
    ma = _laguerre(close, gamma=0.5)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_158_log_dist_above_mama_proxy_alpha005(close: pd.Series) -> pd.Series:
    """MESA Adaptive MA proxy (steady-state EMA alpha=0.05) distance."""
    ma = _mama_proxy(close, alpha=0.05)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_159_log_dist_above_kalman_smoothed_close(close: pd.Series) -> pd.Series:
    """Scalar Kalman-filter-smoothed close distance (q=1e-3, r=1e-2)."""
    ma = _kalman_smoothed(close, q=1e-3, r=1e-2)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_160_log_dist_above_savgol_w21_p3(close: pd.Series) -> pd.Series:
    """Distance above causal Savitzky-Golay smoother (window=21, poly=3)."""
    ma = _savgol_causal(close, window=21, poly=3)
    return _safe_log(close) - _safe_log(ma)


# ============================================================================
# BUCKET B - Volume-weighted & flow-weighted MAs (161-168)
# ============================================================================

def f11_smae_161_log_dist_above_vwma_21_short(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance of close above volume-weighted MA (n=21)."""
    ma = _vwma(close, volume, 21)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_162_log_dist_above_vwma_50_med(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance of close above volume-weighted MA (n=50)."""
    ma = _vwma(close, volume, 50)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_163_log_dist_above_vwma_200_long(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance of close above volume-weighted MA (n=200)."""
    ma = _vwma(close, volume, 200)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_164_vwma50_minus_sma50_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-ratio between volume-weighted and equal-weighted 50-period MAs.
    Positive => volume-weighted trend leads equal-weighted (smart money skew up)."""
    vw = _vwma(close, volume, 50)
    sw = _sma(close, 50)
    return _safe_log(vw) - _safe_log(sw)


def f11_smae_165_log_dist_above_typical_price_vwma_50(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Distance above (H+L+C)/3 weighted by volume - PVWMA50 using typical price."""
    tp = (high + low + close) / 3.0
    ma = _vwma(tp, volume, 50)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_166_log_dist_above_force_weighted_ema_50(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Distance above EMA(close) weighted by Elder's force-index magnitude (|dC|*V).
    Heavy-flow bars carry more weight in the reference level."""
    fi_w = (close.diff().abs() * volume).fillna(0.0)
    num = (close * fi_w).rolling(50, min_periods=max(50 // 3, 2)).sum()
    den = fi_w.rolling(50, min_periods=max(50 // 3, 2)).sum()
    ma = _safe_div(num, den)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_167_log_dist_above_obv_weighted_ema_50(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Distance above an EMA whose weight is the running OBV-step magnitude."""
    obv_step = (np.sign(close.diff()) * volume).abs().fillna(0.0)
    num = (close * obv_step).rolling(50, min_periods=max(50 // 3, 2)).sum()
    den = obv_step.rolling(50, min_periods=max(50 // 3, 2)).sum()
    ma = _safe_div(num, den)
    return _safe_log(close) - _safe_log(ma)


def f11_smae_168_log_dist_above_money_flow_weighted_ma_50(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Distance above a money-flow weighted MA of typical price (n=50)."""
    tp = (high + low + close) / 3.0
    mf = (tp * volume).fillna(0.0)
    num = (tp * mf).rolling(50, min_periods=max(50 // 3, 2)).sum()
    den = mf.rolling(50, min_periods=max(50 // 3, 2)).sum()
    ma = _safe_div(num, den)
    return _safe_log(close) - _safe_log(ma)


# ============================================================================
# BUCKET C - Multi-bar MA derivative dynamics (169-176)
# ============================================================================

def f11_smae_169_sma50_slope_acceleration_21d(close: pd.Series) -> pd.Series:
    """Slope-of-slope of log SMA50 (second derivative measured via two-stage slope)."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    return _rolling_slope(slope, 21)


def f11_smae_170_sma200_slope_jerk_63d(close: pd.Series) -> pd.Series:
    """Third derivative (jerk) of log SMA200 trajectory over 63-bar window."""
    sma = _sma(close, 200)
    s1 = _rolling_slope(_safe_log(sma), 63)
    s2 = _rolling_slope(s1, 63)
    return _rolling_slope(s2, 63)


def f11_smae_171_sma50_curvature_volatility_63d(close: pd.Series) -> pd.Series:
    """Std-dev of curvature (2nd diff of log SMA50) over 63-bar window."""
    sma = _sma(close, 50)
    curv = _safe_log(sma).diff().diff()
    return curv.rolling(63, min_periods=max(63 // 3, 2)).std()


def f11_smae_172_sma200_slope_persistence_signed_streak(close: pd.Series) -> pd.Series:
    """Signed consecutive-bar streak of same-sign slope on SMA200."""
    sma = _sma(close, 200)
    slope = _rolling_slope(_safe_log(sma), 63)
    return _consecutive_same_sign(slope)


def f11_smae_173_sma50_slope_inflection_count_63d(close: pd.Series) -> pd.Series:
    """Count of sign-flips of SMA50 slope over a rolling 63-bar window."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    sign = np.sign(slope.fillna(0.0))
    flips = ((sign != sign.shift(1)) & (sign != 0)).astype(float)
    return flips.rolling(63, min_periods=max(63 // 3, 2)).sum()


def f11_smae_174_sma200_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of SMA200 slope vs its trailing 252-bar distribution."""
    sma = _sma(close, 200)
    slope = _rolling_slope(_safe_log(sma), 63)
    return _rolling_zscore(slope, 252)


def f11_smae_175_sma50_slope_to_sma200_slope_ratio(close: pd.Series) -> pd.Series:
    """Ratio of short-trend slope to long-trend slope (NOT a crossover event).
    Encodes relative speed of nested trends; positive when both same sign."""
    s50 = _rolling_slope(_safe_log(_sma(close, 50)), 21)
    s200 = _rolling_slope(_safe_log(_sma(close, 200)), 63)
    return _safe_div(s50, s200.abs() + 1e-12) * np.sign(s200)


def f11_smae_176_sma50_acceleration_sign_flip_count_63d(close: pd.Series) -> pd.Series:
    """Count of sign-flips in SMA50 acceleration (slope-of-slope) over 63d."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    accel = _rolling_slope(slope, 21)
    sign = np.sign(accel.fillna(0.0))
    flips = ((sign != sign.shift(1)) & (sign != 0)).astype(float)
    return flips.rolling(63, min_periods=max(63 // 3, 2)).sum()


# ============================================================================
# BUCKET D - Touch/rejection/support/resistance metrics (177-186)
# ============================================================================

def f11_smae_177_count_close_within_half_pct_of_sma50_21d(close: pd.Series) -> pd.Series:
    """Number of bars in last 21 where |close/SMA50 - 1| < 0.5%."""
    sma = _sma(close, 50)
    near = (((close - sma) / sma.replace(0, np.nan)).abs() < 0.005).astype(float)
    return near.rolling(21, min_periods=max(21 // 3, 2)).sum()


def f11_smae_178_count_close_within_half_pct_of_sma200_63d(close: pd.Series) -> pd.Series:
    """Number of bars in last 63 where |close/SMA200 - 1| < 0.5%."""
    sma = _sma(close, 200)
    near = (((close - sma) / sma.replace(0, np.nan)).abs() < 0.005).astype(float)
    return near.rolling(63, min_periods=max(63 // 3, 2)).sum()


def f11_smae_179_bars_since_last_sma50_touch_event(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Bars since the SMA50 line was inside the daily [low, high] range (a touch)."""
    sma = _sma(close, 50)
    touch = (sma >= low) & (sma <= high)
    return _bars_since_event(touch)


def f11_smae_180_bars_since_last_sma200_touch_intrabar(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Bars since SMA200 last fell within the bar's [low, high] envelope."""
    sma = _sma(close, 200)
    touch = (sma >= low) & (sma <= high)
    return _bars_since_event(touch)


def f11_smae_181_sma50_rejection_bounce_count_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Count of upward bounces from SMA50 in the last 252 bars: touched
    (intrabar) and the next 3-bar close rose >0.5% from current close."""
    sma = _sma(close, 50)
    touch = (sma >= low) & (sma <= high)
    bounced = touch & ((close - close.shift(3)) / close.shift(3).replace(0, np.nan) > 0.005)
    return bounced.astype(float).rolling(252, min_periods=max(252 // 3, 2)).sum()


def f11_smae_182_sma200_rejection_bounce_count_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """SMA200 rejection-bounce count: intrabar touch + 5-bar close advance >1%."""
    sma = _sma(close, 200)
    touch = (sma >= low) & (sma <= high)
    bounced = touch & ((close - close.shift(5)) / close.shift(5).replace(0, np.nan) > 0.01)
    return bounced.astype(float).rolling(252, min_periods=max(252 // 3, 2)).sum()


def f11_smae_183_sma50_failed_support_break_count_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Failed-support events: intrabar SMA50 touch 3 bars ago AND current close below SMA50."""
    sma = _sma(close, 50)
    touch = (sma >= low) & (sma <= high)
    # PIT-safe: use shift positive to compare a past touch to current break
    touched_past = touch.shift(3).fillna(False)
    failed = touched_past & (close < sma)
    return failed.astype(float).rolling(252, min_periods=max(252 // 3, 2)).sum()


def f11_smae_184_sma200_failed_support_break_count_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """SMA200 failed-support: touch 5 bars ago, current close below SMA200."""
    sma = _sma(close, 200)
    touch = (sma >= low) & (sma <= high)
    touched_past = touch.shift(5).fillna(False)
    failed = touched_past & (close < sma)
    return failed.astype(float).rolling(252, min_periods=max(252 // 3, 2)).sum()


def f11_smae_185_ema21_resistance_rejection_count_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """EMA21-as-resistance count: bar's high pierces EMA21 from below but close stays below it."""
    ma = _ema(close, 21)
    pierced = (high > ma) & (close < ma) & (close.shift(1) < ma.shift(1))
    return pierced.astype(float).rolling(252, min_periods=max(252 // 3, 2)).sum()


def f11_smae_186_multi_ma_simultaneous_touch_event_count_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Count of bars in last 63 where all of SMA50/SMA100/SMA200 lie inside [low, high]."""
    s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    t50 = (s50 >= low) & (s50 <= high)
    t100 = (s100 >= low) & (s100 <= high)
    t200 = (s200 >= low) & (s200 <= high)
    triple = (t50 & t100 & t200).astype(float)
    return triple.rolling(63, min_periods=max(63 // 3, 2)).sum()


# ============================================================================
# BUCKET E - Conditional / regime-aware MA distance (187-196)
# ============================================================================

def f11_smae_187_log_dist_above_sma200_when_near_252d_high(close: pd.Series) -> pd.Series:
    """Log-distance above SMA200 ONLY on bars within 5% of trailing 252d high (else NaN-mean)."""
    sma = _sma(close, 200)
    dist = _safe_log(close) - _safe_log(sma)
    hi252 = close.rolling(252, min_periods=max(252 // 3, 2)).max()
    near_top = (close >= 0.95 * hi252)
    return dist.where(near_top)


def f11_smae_188_log_dist_above_sma50_during_high_vol_regime(close: pd.Series) -> pd.Series:
    """SMA50 distance gated on high-vol regime: rolling realized-vol > median(252)."""
    sma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(sma)
    rv = close.pct_change().rolling(21, min_periods=max(21 // 3, 2)).std()
    med = rv.rolling(252, min_periods=max(252 // 3, 2)).median()
    return dist.where(rv > med)


def f11_smae_189_log_dist_above_sma200_during_low_vol_regime(close: pd.Series) -> pd.Series:
    """SMA200 distance gated on low-vol regime: rolling realized-vol <= median(252)."""
    sma = _sma(close, 200)
    dist = _safe_log(close) - _safe_log(sma)
    rv = close.pct_change().rolling(21, min_periods=max(21 // 3, 2)).std()
    med = rv.rolling(252, min_periods=max(252 // 3, 2)).median()
    return dist.where(rv <= med)


def f11_smae_190_mean_dist_above_sma50_on_new_high_bars_63d(close: pd.Series) -> pd.Series:
    """Mean of SMA50-distance on bars that print a new 63d high, averaged over 63d window."""
    sma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(sma)
    hi63 = close.rolling(63, min_periods=max(63 // 3, 2)).max()
    is_new_hi = (close >= hi63)
    gated = dist.where(is_new_hi)
    return gated.rolling(63, min_periods=2).mean()


def f11_smae_191_mean_dist_above_sma50_during_drawdown_63d(close: pd.Series) -> pd.Series:
    """Mean SMA50-distance on bars whose price is in drawdown >5% from 63d peak."""
    sma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(sma)
    hi63 = close.rolling(63, min_periods=max(63 // 3, 2)).max()
    dd = (close / hi63.replace(0, np.nan) - 1.0)
    in_dd = (dd < -0.05)
    return dist.where(in_dd).rolling(63, min_periods=2).mean()


def f11_smae_192_sma50_distance_skew_conditional_uptrend(close: pd.Series) -> pd.Series:
    """Skewness of SMA50-distance over 252d, conditional on SMA200 slope > 0."""
    sma50 = _sma(close, 50)
    sma200 = _sma(close, 200)
    dist = _safe_log(close) - _safe_log(sma50)
    up = (_rolling_slope(_safe_log(sma200), 63) > 0)
    gated = dist.where(up)
    return gated.rolling(252, min_periods=max(252 // 3, 2)).skew()


def f11_smae_193_sma200_distance_kurt_conditional_uptrend(close: pd.Series) -> pd.Series:
    """Kurtosis of SMA200-distance over 252d gated on SMA200 slope > 0."""
    sma = _sma(close, 200)
    dist = _safe_log(close) - _safe_log(sma)
    up = (_rolling_slope(_safe_log(sma), 63) > 0)
    gated = dist.where(up)
    return gated.rolling(252, min_periods=max(252 // 3, 2)).kurt()


def f11_smae_194_distance_decay_speed_post_252d_high(close: pd.Series) -> pd.Series:
    """Mean-reversion speed: regress current SMA50-distance on past 21-bar distance.
    Beta < 1 indicates decay. Reports (1 - beta)/21 as half-life proxy."""
    sma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(sma)
    lag = dist.shift(21)
    win = 63
    mp = max(win // 3, 2)
    cov = (dist * lag).rolling(win, min_periods=mp).mean() - dist.rolling(win, min_periods=mp).mean() * lag.rolling(win, min_periods=mp).mean()
    var = lag.rolling(win, min_periods=mp).var()
    beta = _safe_div(cov, var)
    return (1.0 - beta) / 21.0


def f11_smae_195_distance_expansion_velocity_post_breakout(close: pd.Series) -> pd.Series:
    """21-bar change in SMA50-distance, gated on the existence of a breakout
    (close making a new 63d high in the last 21 bars)."""
    sma = _sma(close, 50)
    dist = _safe_log(close) - _safe_log(sma)
    hi63 = close.rolling(63, min_periods=max(63 // 3, 2)).max()
    is_new_hi = (close >= hi63).astype(float)
    breakout_recent = is_new_hi.rolling(21, min_periods=2).max() > 0
    change = dist - dist.shift(21)
    return change.where(breakout_recent)


def f11_smae_196_distance_dispersion_across_horizons_at_extension(close: pd.Series) -> pd.Series:
    """Std-dev of log-distance across 5 SMA horizons (21/50/100/200/500),
    gated on the SMA50-distance being in its top-quintile vs 252d."""
    d21 = _safe_log(close) - _safe_log(_sma(close, 21))
    d50 = _safe_log(close) - _safe_log(_sma(close, 50))
    d100 = _safe_log(close) - _safe_log(_sma(close, 100))
    d200 = _safe_log(close) - _safe_log(_sma(close, 200))
    d500 = _safe_log(close) - _safe_log(_sma(close, 500))
    stk = pd.concat([d21.rename("a"), d50.rename("b"), d100.rename("c"),
                     d200.rename("d"), d500.rename("e")], axis=1)
    disp = stk.std(axis=1)
    q80 = d50.rolling(252, min_periods=max(252 // 3, 2)).quantile(0.80)
    return disp.where(d50 >= q80)


# ============================================================================
# BUCKET F - Multi-horizon distance dispersion / consensus (197-204)
# ============================================================================

def f11_smae_197_multi_horizon_extension_consensus_count_above_5pct(close: pd.Series) -> pd.Series:
    """Count of MA horizons (21/50/100/200/500) where close is >5% above SMA."""
    horizons = [21, 50, 100, 200, 500]
    flags = []
    for h in horizons:
        sma = _sma(close, h)
        flags.append(((close / sma.replace(0, np.nan) - 1.0) > 0.05).astype(float))
    frame = pd.concat([f.rename(f"h{i}") for i, f in enumerate(flags)], axis=1)
    return frame.sum(axis=1)


def f11_smae_198_multi_horizon_extension_dispersion_stddev_5h(close: pd.Series) -> pd.Series:
    """Std-dev across log-distances to 5 SMA horizons (21/50/100/200/500)."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        pieces.append((_safe_log(close) - _safe_log(sma)).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    return frame.std(axis=1)


def f11_smae_199_multi_horizon_extension_mean_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the cross-horizon-mean distance over a 252d window."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        pieces.append((_safe_log(close) - _safe_log(sma)).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    mean_dist = frame.mean(axis=1)
    return _rolling_zscore(mean_dist, 252)


def f11_smae_200_multi_horizon_extension_skewness_across_horizons(close: pd.Series) -> pd.Series:
    """Cross-sectional skew of distances across 5 SMA horizons (instantaneous).
    Positive => extension concentrated in short horizons."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        pieces.append((_safe_log(close) - _safe_log(sma)).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    return frame.skew(axis=1)


def f11_smae_201_multi_horizon_extension_breadth_in_top_decile(close: pd.Series) -> pd.Series:
    """Fraction of 5 horizons whose distance is in its own 252d top decile."""
    horizons = [21, 50, 100, 200, 500]
    flags = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        dist = _safe_log(close) - _safe_log(sma)
        q90 = dist.rolling(252, min_periods=max(252 // 3, 2)).quantile(0.90)
        flags.append((dist >= q90).astype(float).rename(f"h{i}"))
    frame = pd.concat(flags, axis=1)
    return frame.mean(axis=1)


def f11_smae_202_dist_to_nearest_sma_below_signed(close: pd.Series) -> pd.Series:
    """Signed log-distance to the highest SMA still below close (nearest support).
    NaN when no SMA is below close."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        d = _safe_log(close) - _safe_log(sma)
        d = d.where(d > 0)
        pieces.append(d.rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    return frame.min(axis=1)


def f11_smae_203_dist_to_nearest_sma_above_signed(close: pd.Series) -> pd.Series:
    """Signed log-distance to the lowest SMA still above close (nearest resistance).
    NaN when no SMA is above close."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        d = _safe_log(sma) - _safe_log(close)
        d = d.where(d > 0)
        pieces.append(d.rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    return frame.min(axis=1)


def f11_smae_204_multi_horizon_extension_velocity_21d(close: pd.Series) -> pd.Series:
    """21-bar change in the cross-horizon mean distance."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        sma = _sma(close, h)
        pieces.append((_safe_log(close) - _safe_log(sma)).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    mean_dist = frame.mean(axis=1)
    return mean_dist - mean_dist.shift(21)


# ============================================================================
# BUCKET G - MA-of-MA structures (205-212)
# ============================================================================

def f11_smae_205_triple_ema_smoothed_reference_dist_50(close: pd.Series) -> pd.Series:
    """Distance above a 50-period EMA cascaded 3 times (smoothed reference,
    distinct from TEMA which is 3e1-3e2+e3)."""
    e1 = _ema(close, 50)
    e2 = _ema(e1, 50)
    e3 = _ema(e2, 50)
    return _safe_log(close) - _safe_log(e3)


def f11_smae_206_sma_of_sma_accumulated_lag_50(close: pd.Series) -> pd.Series:
    """Lag between SMA50 and SMA-of-SMA50 (a second smoothing pass) - measures
    how much extra smoothing lag accumulates."""
    s = _sma(close, 50)
    ss = _sma(s, 50)
    return _safe_log(s) - _safe_log(ss)


def f11_smae_207_median_of_5mas_distance(close: pd.Series) -> pd.Series:
    """Distance above the cross-horizon median of 5 MAs (robust reference)."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        pieces.append(_sma(close, h).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    med = frame.median(axis=1)
    return _safe_log(close) - _safe_log(med)


def f11_smae_208_trimmed_mean_of_mas_distance_5h(close: pd.Series) -> pd.Series:
    """Distance above 20%-trimmed mean of 5 MAs (drop highest and lowest)."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        pieces.append(_sma(close, h).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    # trimmed mean: drop max and min per row
    arr = frame.values
    sorted_arr = np.sort(arr, axis=1)
    trimmed = sorted_arr[:, 1:-1].mean(axis=1)
    tm = pd.Series(trimmed, index=close.index)
    return _safe_log(close) - _safe_log(tm)


def f11_smae_209_dispersion_weighted_ma_distance(close: pd.Series) -> pd.Series:
    """Distance above an MA whose component-weights are inverse to 252d distance dispersion.
    When all horizons agree, single-horizon MAs all get similar weight."""
    horizons = [21, 50, 100, 200, 500]
    mas = {}
    dists = {}
    for h in horizons:
        mas[h] = _sma(close, h)
        dists[h] = (_safe_log(close) - _safe_log(mas[h]))
    # rolling std of each horizon's distance over 252
    weights = {}
    for h in horizons:
        sd = dists[h].rolling(252, min_periods=max(252 // 3, 2)).std()
        weights[h] = 1.0 / (sd + 1e-6)
    wsum = sum(weights.values())
    weighted = sum(weights[h] * mas[h] for h in horizons) / wsum
    return _safe_log(close) - _safe_log(weighted)


def f11_smae_210_ma_of_ma_curvature_50(close: pd.Series) -> pd.Series:
    """Second-diff curvature of (SMA50 of SMA50), capturing slow-trend acceleration."""
    s = _sma(close, 50)
    ss = _sma(s, 50)
    return _safe_log(ss).diff().diff()


def f11_smae_211_exponentially_increasing_lookback_ma_distance(close: pd.Series) -> pd.Series:
    """Distance above an MA blend whose weights grow exponentially with horizon:
    w_h = exp(h/200) for h in {21,50,100,200,500}."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    weights_w = []
    for i, h in enumerate(horizons):
        pieces.append(_sma(close, h).rename(f"h{i}"))
        weights_w.append(np.exp(h / 200.0))
    frame = pd.concat(pieces, axis=1)
    w = np.array(weights_w, dtype=float)
    w = w / w.sum()
    blended = (frame * w).sum(axis=1)
    return _safe_log(close) - _safe_log(blended)


def f11_smae_212_harmonic_mean_of_ma_lookbacks_distance(close: pd.Series) -> pd.Series:
    """Distance above the harmonic mean of 5 SMAs (emphasizes smaller values =>
    emphasizes faster-reacting MAs in downtrends)."""
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        pieces.append(_sma(close, h).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    # harmonic mean: N / sum(1/x)
    inv = 1.0 / frame.replace(0, np.nan)
    hmean = inv.shape[1] / inv.sum(axis=1).replace(0, np.nan)
    return _safe_log(close) - _safe_log(hmean)


# ============================================================================
# BUCKET H - Displaced / projected MAs (213-218)
# ============================================================================

def f11_smae_213_log_dist_above_sma50_extrapolated_5fwd(close: pd.Series) -> pd.Series:
    """Distance above a 5-bar-forward extrapolation of SMA50 using its current slope.
    PIT-SAFE: only uses current and past values (no .shift(N))."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    projected_log = _safe_log(sma) + slope * 5.0
    return _safe_log(close) - projected_log


def f11_smae_214_log_dist_above_sma200_extrapolated_21fwd(close: pd.Series) -> pd.Series:
    """Distance above a 21-bar-forward extrapolation of SMA200 from current slope.
    PIT-safe: uses current SMA + (current slope * 21)."""
    sma = _sma(close, 200)
    slope = _rolling_slope(_safe_log(sma), 63)
    projected_log = _safe_log(sma) + slope * 21.0
    return _safe_log(close) - projected_log


def f11_smae_215_displaced_ma_envelope_breach_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where close lies OUTSIDE [-2%, +2%] band around the
    21-bar-forward extrapolation of SMA50."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    projected = sma * np.exp(slope * 21.0)
    upper = projected * 1.02
    lower = projected * 0.98
    breach = ((close > upper) | (close < lower)).astype(float)
    return breach.rolling(63, min_periods=max(63 // 3, 2)).sum()


def f11_smae_216_forward_projection_residual_sma50_5fwd(close: pd.Series) -> pd.Series:
    """Difference between close today and a 5-bar-forward extrapolation made 5 bars ago.
    Encodes how much today's close exceeded the past projection of where it should be."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    projected = _safe_log(sma) + slope * 5.0
    past_projection = projected.shift(5)
    return _safe_log(close) - past_projection


def f11_smae_217_multi_horizon_displaced_ma_consensus_above(close: pd.Series) -> pd.Series:
    """Count of horizons (21/50/100/200) whose 10-bar-extrapolated MA lies below close."""
    horizons = [21, 50, 100, 200]
    flags = []
    for h in horizons:
        sma = _sma(close, h)
        slope = _rolling_slope(_safe_log(sma), max(h // 3, 21))
        projected = _safe_log(sma) + slope * 10.0
        flags.append((_safe_log(close) > projected).astype(float))
    frame = pd.concat([f.rename(f"h{i}") for i, f in enumerate(flags)], axis=1)
    return frame.sum(axis=1)


def f11_smae_218_displaced_ma_slope_extrapolation_error_21d(close: pd.Series) -> pd.Series:
    """Std-dev of (close - past extrapolation) over 21 bars - how unstable forward
    projections from SMA50 slope have been recently."""
    sma = _sma(close, 50)
    slope = _rolling_slope(_safe_log(sma), 21)
    projected = _safe_log(sma) + slope * 5.0
    err = _safe_log(close) - projected.shift(5)
    return err.rolling(21, min_periods=max(21 // 3, 2)).std()


# ============================================================================
# BUCKET I - Compound MA composite scores (219-225)
# ============================================================================

def f11_smae_219_adaptive_ma_consensus_distance(close: pd.Series) -> pd.Series:
    """Mean log-distance across JMA, VIDYA, ALMA, ZLEMA, T3 (all at n=50)."""
    pieces = []
    pieces.append((_safe_log(close) - _safe_log(_jma(close, 50))).rename("jma"))
    pieces.append((_safe_log(close) - _safe_log(_vidya(close, 50, 14))).rename("vidya"))
    pieces.append((_safe_log(close) - _safe_log(_alma(close, 50, 6.0, 0.85))).rename("alma"))
    pieces.append((_safe_log(close) - _safe_log(_zlema(close, 50))).rename("zlema"))
    pieces.append((_safe_log(close) - _safe_log(_t3(close, 50, 0.7))).rename("t3"))
    frame = pd.concat(pieces, axis=1)
    return frame.mean(axis=1)


def f11_smae_220_volflow_vs_equalweight_distance_divergence_composite(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Composite: |VWMA-distance| - |SMA-distance|, averaged over 21/50/200 horizons.
    Positive => volume-weighted MAs show larger extension than equal-weighted (asymmetric flow)."""
    pieces = []
    for h in [21, 50, 200]:
        vw = _vwma(close, volume, h)
        sw = _sma(close, h)
        diff = (_safe_log(close) - _safe_log(vw)).abs() - (_safe_log(close) - _safe_log(sw)).abs()
        pieces.append(diff.rename(f"h{h}"))
    frame = pd.concat(pieces, axis=1)
    return frame.mean(axis=1)


def f11_smae_221_multi_method_ma_distance_terminal_score(close: pd.Series) -> pd.Series:
    """Sum of z-scored (252d) distances across SMA50, EMA50, HMA-proxy via WMA,
    and Kalman-smoothed close. Higher => terminal extension across diverse smoothers."""
    d_sma = _safe_log(close) - _safe_log(_sma(close, 50))
    d_ema = _safe_log(close) - _safe_log(_ema(close, 50))
    d_wma = _safe_log(close) - _safe_log(_wma(close, 50))
    d_kal = _safe_log(close) - _safe_log(_kalman_smoothed(close))
    z1 = _rolling_zscore(d_sma, 252)
    z2 = _rolling_zscore(d_ema, 252)
    z3 = _rolling_zscore(d_wma, 252)
    z4 = _rolling_zscore(d_kal, 252)
    return z1.add(z2, fill_value=np.nan).add(z3, fill_value=np.nan).add(z4, fill_value=np.nan)


def f11_smae_222_ma_distance_acceleration_composite(close: pd.Series) -> pd.Series:
    """Composite acceleration: sum of slopes-of-slopes of distance series across
    SMA50/EMA50/HMA(via wma) - measures whether multi-method extension is speeding up."""
    pieces = []
    for ma_func, name in [(_sma, "sma"), (_ema, "ema"), (_wma, "wma")]:
        d = _safe_log(close) - _safe_log(ma_func(close, 50))
        s = _rolling_slope(d, 21)
        a = _rolling_slope(s, 21)
        pieces.append(a.rename(name))
    frame = pd.concat(pieces, axis=1)
    return frame.sum(axis=1)


def f11_smae_223_touch_bounce_failedsupport_composite_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Composite distress: failed-support count minus bounce count at SMA50, normalized
    by total touch count over 252d. Positive => support failing more than holding."""
    sma = _sma(close, 50)
    touch = ((sma >= low) & (sma <= high)).astype(float)
    bounce = (touch.astype(bool) & ((close - close.shift(3)) / close.shift(3).replace(0, np.nan) > 0.005)).astype(float)
    touched_past = touch.shift(3).fillna(0.0)
    failed = ((touched_past > 0) & (close < sma)).astype(float)
    win = 252
    mp = max(win // 3, 2)
    tc = touch.rolling(win, min_periods=mp).sum()
    bc = bounce.rolling(win, min_periods=mp).sum()
    fc = failed.rolling(win, min_periods=mp).sum()
    return _safe_div(fc - bc, tc)


def f11_smae_224_conditional_distance_regime_consistency_composite(close: pd.Series) -> pd.Series:
    """Consistency: 1 if sign of SMA50-distance matches sign of SMA200-distance AND
    sign of SMA50 slope AND sign of SMA200 slope, smoothed by 21-bar mean."""
    d50 = _safe_log(close) - _safe_log(_sma(close, 50))
    d200 = _safe_log(close) - _safe_log(_sma(close, 200))
    s50 = _rolling_slope(_safe_log(_sma(close, 50)), 21)
    s200 = _rolling_slope(_safe_log(_sma(close, 200)), 63)
    signs = pd.concat([np.sign(d50).rename("a"), np.sign(d200).rename("b"),
                       np.sign(s50).rename("c"), np.sign(s200).rename("d")], axis=1)
    # all four same direction
    pos = (signs > 0).all(axis=1).astype(float)
    neg = (signs < 0).all(axis=1).astype(float)
    consistent = pos - neg
    return consistent.rolling(21, min_periods=max(21 // 3, 2)).mean()


def f11_smae_225_terminal_ma_extension_distress_score(close: pd.Series) -> pd.Series:
    """Terminal distress composite: distance-zscore of SMA50 + distance-zscore of SMA200 +
    slope acceleration of SMA50 + cross-horizon dispersion, all 252d-normalized.
    Tail values indicate parabolic-but-narrowing extension."""
    d50 = _safe_log(close) - _safe_log(_sma(close, 50))
    d200 = _safe_log(close) - _safe_log(_sma(close, 200))
    z50 = _rolling_zscore(d50, 252)
    z200 = _rolling_zscore(d200, 252)
    slope50 = _rolling_slope(_safe_log(_sma(close, 50)), 21)
    acc50 = _rolling_slope(slope50, 21)
    z_acc = _rolling_zscore(acc50, 252)
    horizons = [21, 50, 100, 200, 500]
    pieces = []
    for i, h in enumerate(horizons):
        pieces.append((_safe_log(close) - _safe_log(_sma(close, h))).rename(f"h{i}"))
    frame = pd.concat(pieces, axis=1)
    disp = frame.std(axis=1)
    z_disp = _rolling_zscore(disp, 252)
    return z50.add(z200, fill_value=np.nan).add(z_acc, fill_value=np.nan).add(z_disp, fill_value=np.nan)


# ============================================================================
# Registry
# ============================================================================

SMA_EMA_EXTENSION_DYNAMICS_BASE_REGISTRY_151_225 = {
    "f11_smae_151_log_dist_above_jma_50": {"inputs": ["close"], "func": f11_smae_151_log_dist_above_jma_50},
    "f11_smae_152_log_dist_above_vidya_50": {"inputs": ["close"], "func": f11_smae_152_log_dist_above_vidya_50},
    "f11_smae_153_log_dist_above_alma_50_offset85_sigma6": {"inputs": ["close"], "func": f11_smae_153_log_dist_above_alma_50_offset85_sigma6},
    "f11_smae_154_log_dist_above_zlema_200_long": {"inputs": ["close"], "func": f11_smae_154_log_dist_above_zlema_200_long},
    "f11_smae_155_log_dist_above_t3_200_long": {"inputs": ["close"], "func": f11_smae_155_log_dist_above_t3_200_long},
    "f11_smae_156_log_dist_above_mcginley_dynamic_200": {"inputs": ["close"], "func": f11_smae_156_log_dist_above_mcginley_dynamic_200},
    "f11_smae_157_log_dist_above_laguerre_filter_gamma5": {"inputs": ["close"], "func": f11_smae_157_log_dist_above_laguerre_filter_gamma5},
    "f11_smae_158_log_dist_above_mama_proxy_alpha005": {"inputs": ["close"], "func": f11_smae_158_log_dist_above_mama_proxy_alpha005},
    "f11_smae_159_log_dist_above_kalman_smoothed_close": {"inputs": ["close"], "func": f11_smae_159_log_dist_above_kalman_smoothed_close},
    "f11_smae_160_log_dist_above_savgol_w21_p3": {"inputs": ["close"], "func": f11_smae_160_log_dist_above_savgol_w21_p3},
    "f11_smae_161_log_dist_above_vwma_21_short": {"inputs": ["close", "volume"], "func": f11_smae_161_log_dist_above_vwma_21_short},
    "f11_smae_162_log_dist_above_vwma_50_med": {"inputs": ["close", "volume"], "func": f11_smae_162_log_dist_above_vwma_50_med},
    "f11_smae_163_log_dist_above_vwma_200_long": {"inputs": ["close", "volume"], "func": f11_smae_163_log_dist_above_vwma_200_long},
    "f11_smae_164_vwma50_minus_sma50_divergence": {"inputs": ["close", "volume"], "func": f11_smae_164_vwma50_minus_sma50_divergence},
    "f11_smae_165_log_dist_above_typical_price_vwma_50": {"inputs": ["high", "low", "close", "volume"], "func": f11_smae_165_log_dist_above_typical_price_vwma_50},
    "f11_smae_166_log_dist_above_force_weighted_ema_50": {"inputs": ["close", "volume"], "func": f11_smae_166_log_dist_above_force_weighted_ema_50},
    "f11_smae_167_log_dist_above_obv_weighted_ema_50": {"inputs": ["close", "volume"], "func": f11_smae_167_log_dist_above_obv_weighted_ema_50},
    "f11_smae_168_log_dist_above_money_flow_weighted_ma_50": {"inputs": ["high", "low", "close", "volume"], "func": f11_smae_168_log_dist_above_money_flow_weighted_ma_50},
    "f11_smae_169_sma50_slope_acceleration_21d": {"inputs": ["close"], "func": f11_smae_169_sma50_slope_acceleration_21d},
    "f11_smae_170_sma200_slope_jerk_63d": {"inputs": ["close"], "func": f11_smae_170_sma200_slope_jerk_63d},
    "f11_smae_171_sma50_curvature_volatility_63d": {"inputs": ["close"], "func": f11_smae_171_sma50_curvature_volatility_63d},
    "f11_smae_172_sma200_slope_persistence_signed_streak": {"inputs": ["close"], "func": f11_smae_172_sma200_slope_persistence_signed_streak},
    "f11_smae_173_sma50_slope_inflection_count_63d": {"inputs": ["close"], "func": f11_smae_173_sma50_slope_inflection_count_63d},
    "f11_smae_174_sma200_slope_zscore_252d": {"inputs": ["close"], "func": f11_smae_174_sma200_slope_zscore_252d},
    "f11_smae_175_sma50_slope_to_sma200_slope_ratio": {"inputs": ["close"], "func": f11_smae_175_sma50_slope_to_sma200_slope_ratio},
    "f11_smae_176_sma50_acceleration_sign_flip_count_63d": {"inputs": ["close"], "func": f11_smae_176_sma50_acceleration_sign_flip_count_63d},
    "f11_smae_177_count_close_within_half_pct_of_sma50_21d": {"inputs": ["close"], "func": f11_smae_177_count_close_within_half_pct_of_sma50_21d},
    "f11_smae_178_count_close_within_half_pct_of_sma200_63d": {"inputs": ["close"], "func": f11_smae_178_count_close_within_half_pct_of_sma200_63d},
    "f11_smae_179_bars_since_last_sma50_touch_event": {"inputs": ["high", "low", "close"], "func": f11_smae_179_bars_since_last_sma50_touch_event},
    "f11_smae_180_bars_since_last_sma200_touch_intrabar": {"inputs": ["high", "low", "close"], "func": f11_smae_180_bars_since_last_sma200_touch_intrabar},
    "f11_smae_181_sma50_rejection_bounce_count_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_181_sma50_rejection_bounce_count_252d},
    "f11_smae_182_sma200_rejection_bounce_count_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_182_sma200_rejection_bounce_count_252d},
    "f11_smae_183_sma50_failed_support_break_count_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_183_sma50_failed_support_break_count_252d},
    "f11_smae_184_sma200_failed_support_break_count_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_184_sma200_failed_support_break_count_252d},
    "f11_smae_185_ema21_resistance_rejection_count_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_185_ema21_resistance_rejection_count_252d},
    "f11_smae_186_multi_ma_simultaneous_touch_event_count_63d": {"inputs": ["high", "low", "close"], "func": f11_smae_186_multi_ma_simultaneous_touch_event_count_63d},
    "f11_smae_187_log_dist_above_sma200_when_near_252d_high": {"inputs": ["close"], "func": f11_smae_187_log_dist_above_sma200_when_near_252d_high},
    "f11_smae_188_log_dist_above_sma50_during_high_vol_regime": {"inputs": ["close"], "func": f11_smae_188_log_dist_above_sma50_during_high_vol_regime},
    "f11_smae_189_log_dist_above_sma200_during_low_vol_regime": {"inputs": ["close"], "func": f11_smae_189_log_dist_above_sma200_during_low_vol_regime},
    "f11_smae_190_mean_dist_above_sma50_on_new_high_bars_63d": {"inputs": ["close"], "func": f11_smae_190_mean_dist_above_sma50_on_new_high_bars_63d},
    "f11_smae_191_mean_dist_above_sma50_during_drawdown_63d": {"inputs": ["close"], "func": f11_smae_191_mean_dist_above_sma50_during_drawdown_63d},
    "f11_smae_192_sma50_distance_skew_conditional_uptrend": {"inputs": ["close"], "func": f11_smae_192_sma50_distance_skew_conditional_uptrend},
    "f11_smae_193_sma200_distance_kurt_conditional_uptrend": {"inputs": ["close"], "func": f11_smae_193_sma200_distance_kurt_conditional_uptrend},
    "f11_smae_194_distance_decay_speed_post_252d_high": {"inputs": ["close"], "func": f11_smae_194_distance_decay_speed_post_252d_high},
    "f11_smae_195_distance_expansion_velocity_post_breakout": {"inputs": ["close"], "func": f11_smae_195_distance_expansion_velocity_post_breakout},
    "f11_smae_196_distance_dispersion_across_horizons_at_extension": {"inputs": ["close"], "func": f11_smae_196_distance_dispersion_across_horizons_at_extension},
    "f11_smae_197_multi_horizon_extension_consensus_count_above_5pct": {"inputs": ["close"], "func": f11_smae_197_multi_horizon_extension_consensus_count_above_5pct},
    "f11_smae_198_multi_horizon_extension_dispersion_stddev_5h": {"inputs": ["close"], "func": f11_smae_198_multi_horizon_extension_dispersion_stddev_5h},
    "f11_smae_199_multi_horizon_extension_mean_zscore_252d": {"inputs": ["close"], "func": f11_smae_199_multi_horizon_extension_mean_zscore_252d},
    "f11_smae_200_multi_horizon_extension_skewness_across_horizons": {"inputs": ["close"], "func": f11_smae_200_multi_horizon_extension_skewness_across_horizons},
    "f11_smae_201_multi_horizon_extension_breadth_in_top_decile": {"inputs": ["close"], "func": f11_smae_201_multi_horizon_extension_breadth_in_top_decile},
    "f11_smae_202_dist_to_nearest_sma_below_signed": {"inputs": ["close"], "func": f11_smae_202_dist_to_nearest_sma_below_signed},
    "f11_smae_203_dist_to_nearest_sma_above_signed": {"inputs": ["close"], "func": f11_smae_203_dist_to_nearest_sma_above_signed},
    "f11_smae_204_multi_horizon_extension_velocity_21d": {"inputs": ["close"], "func": f11_smae_204_multi_horizon_extension_velocity_21d},
    "f11_smae_205_triple_ema_smoothed_reference_dist_50": {"inputs": ["close"], "func": f11_smae_205_triple_ema_smoothed_reference_dist_50},
    "f11_smae_206_sma_of_sma_accumulated_lag_50": {"inputs": ["close"], "func": f11_smae_206_sma_of_sma_accumulated_lag_50},
    "f11_smae_207_median_of_5mas_distance": {"inputs": ["close"], "func": f11_smae_207_median_of_5mas_distance},
    "f11_smae_208_trimmed_mean_of_mas_distance_5h": {"inputs": ["close"], "func": f11_smae_208_trimmed_mean_of_mas_distance_5h},
    "f11_smae_209_dispersion_weighted_ma_distance": {"inputs": ["close"], "func": f11_smae_209_dispersion_weighted_ma_distance},
    "f11_smae_210_ma_of_ma_curvature_50": {"inputs": ["close"], "func": f11_smae_210_ma_of_ma_curvature_50},
    "f11_smae_211_exponentially_increasing_lookback_ma_distance": {"inputs": ["close"], "func": f11_smae_211_exponentially_increasing_lookback_ma_distance},
    "f11_smae_212_harmonic_mean_of_ma_lookbacks_distance": {"inputs": ["close"], "func": f11_smae_212_harmonic_mean_of_ma_lookbacks_distance},
    "f11_smae_213_log_dist_above_sma50_extrapolated_5fwd": {"inputs": ["close"], "func": f11_smae_213_log_dist_above_sma50_extrapolated_5fwd},
    "f11_smae_214_log_dist_above_sma200_extrapolated_21fwd": {"inputs": ["close"], "func": f11_smae_214_log_dist_above_sma200_extrapolated_21fwd},
    "f11_smae_215_displaced_ma_envelope_breach_count_63d": {"inputs": ["close"], "func": f11_smae_215_displaced_ma_envelope_breach_count_63d},
    "f11_smae_216_forward_projection_residual_sma50_5fwd": {"inputs": ["close"], "func": f11_smae_216_forward_projection_residual_sma50_5fwd},
    "f11_smae_217_multi_horizon_displaced_ma_consensus_above": {"inputs": ["close"], "func": f11_smae_217_multi_horizon_displaced_ma_consensus_above},
    "f11_smae_218_displaced_ma_slope_extrapolation_error_21d": {"inputs": ["close"], "func": f11_smae_218_displaced_ma_slope_extrapolation_error_21d},
    "f11_smae_219_adaptive_ma_consensus_distance": {"inputs": ["close"], "func": f11_smae_219_adaptive_ma_consensus_distance},
    "f11_smae_220_volflow_vs_equalweight_distance_divergence_composite": {"inputs": ["close", "volume"], "func": f11_smae_220_volflow_vs_equalweight_distance_divergence_composite},
    "f11_smae_221_multi_method_ma_distance_terminal_score": {"inputs": ["close"], "func": f11_smae_221_multi_method_ma_distance_terminal_score},
    "f11_smae_222_ma_distance_acceleration_composite": {"inputs": ["close"], "func": f11_smae_222_ma_distance_acceleration_composite},
    "f11_smae_223_touch_bounce_failedsupport_composite_252d": {"inputs": ["high", "low", "close"], "func": f11_smae_223_touch_bounce_failedsupport_composite_252d},
    "f11_smae_224_conditional_distance_regime_consistency_composite": {"inputs": ["close"], "func": f11_smae_224_conditional_distance_regime_consistency_composite},
    "f11_smae_225_terminal_ma_extension_distress_score": {"inputs": ["close"], "func": f11_smae_225_terminal_ma_extension_distress_score},
}
