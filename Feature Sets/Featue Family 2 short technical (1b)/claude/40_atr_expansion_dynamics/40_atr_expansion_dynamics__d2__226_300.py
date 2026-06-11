"""atr_expansion_dynamics d2 features 226-300 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the previous 225. Drawn from gap analysis:
candlestick-anatomy patterns (hammer, shooting-star, doji, engulfing, three-white-
soldiers / three-black-crows), wavelet & spectral decomposition of TR, TR-regime
state durations / runs / crossings, AR(2) and entropy-based persistence of TR,
ATR-volume / dollar-range coupling, conditional-on-event TR (post-gap, near-peak),
compression-then-expansion subtleties, ATR-vs-EMA convergence (Bollinger-on-ATR),
range-of-shadows symmetric & asymmetric, higher-order TR moments (Δ²TR variance,
ARCH-on-TR²), final total-variation and NATR-shape descriptors.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import math
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


def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()


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


def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


def _bars_since(ind: pd.Series) -> pd.Series:
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)


# ============================================================
# Bucket Z22 — More candle anatomy (226-235)
# ============================================================

def f40_atxd_226_upper_shadow_share_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of (upper-shadow / TR) — trend of rejection-wick share."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    us = _safe_div(high - body_hi, _true_range(high, low, close))
    return _rolling_slope(us, QDAYS)


def f40_atxd_227_lower_shadow_share_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of (lower-shadow / TR) — trend of demand-tail share."""
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    ls = _safe_div(body_lo - low, _true_range(high, low, close))
    return _rolling_slope(ls, QDAYS)


def f40_atxd_228_body_share_slope_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of |C-O|/TR — trend of marubozu (trending-bar) share."""
    body = _safe_div((close - open).abs(), _true_range(high, low, close))
    return _rolling_slope(body, QDAYS)


def f40_atxd_229_var_close_pos_in_range_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of close-position-in-range (C-L)/(H-L) over 252d — CLV dispersion."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div(close - low, rng).rolling(YDAYS, min_periods=QDAYS).var()


def f40_atxd_230_hammer_pattern_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of hammer bars (lower-shadow > 2·body AND small upper-shadow) over 252d."""
    body = (close - open).abs()
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    lower_shadow = body_lo - low
    upper_shadow = high - body_hi
    hammer = (lower_shadow > 2.0 * body) & (upper_shadow < 0.5 * body) & (body > 0)
    return hammer.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_231_shooting_star_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of shooting-star bars (upper-shadow > 2·body AND small lower-shadow) over 252d."""
    body = (close - open).abs()
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    lower_shadow = body_lo - low
    upper_shadow = high - body_hi
    star = (upper_shadow > 2.0 * body) & (lower_shadow < 0.5 * body) & (body > 0)
    return star.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_232_doji_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of doji bars (|C-O| / TR < 0.1) over 252d."""
    body = (close - open).abs()
    tr = _true_range(high, low, close)
    doji = _safe_div(body, tr) < 0.1
    return doji.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_233_engulfing_bar_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of engulfing bars (today's body > 1.5·yesterday's body) over 252d."""
    body = (close - open).abs()
    engulf = body > 1.5 * body.shift(1)
    return engulf.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_234_three_white_soldiers_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 3-consecutive-up-bar (three white soldiers) patterns over 252d."""
    up = close > open
    pattern = up & up.shift(1) & up.shift(2)
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_235_three_black_crows_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 3-consecutive-down-bar (three black crows) patterns over 252d."""
    dn = close < open
    pattern = dn & dn.shift(1) & dn.shift(2)
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z23 — TR cycle / spectral (236-243)
# ============================================================

def f40_atxd_236_slope_atr_on_up_bars_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of ATR-restricted-to-up-bars: trend of bull-range expansion."""
    tr = _true_range(high, low, close)
    up_tr = tr.where(close > close.shift(1), np.nan)
    return _rolling_slope(up_tr.rolling(WDAYS, min_periods=2).mean(), QDAYS)


def _haar_variance(w: np.ndarray, scale: int) -> float:
    ww = w[~np.isnan(w)]
    n = len(ww)
    if n < scale * 4:
        return np.nan
    n_p = (n // scale) * scale
    block = ww[:n_p].reshape(-1, scale)
    avg = block.mean(axis=1)
    d = np.diff(avg)
    return float(d.var()) if len(d) > 1 else np.nan


def f40_atxd_237_wavelet_variance_tr_scale4_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wavelet variance of TR at Haar dyadic scale-4 over 252d."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _haar_variance(w, 4), raw=True)


def f40_atxd_238_wavelet_variance_tr_scale8_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wavelet variance of TR at Haar dyadic scale-8 over 252d."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _haar_variance(w, 8), raw=True)


def f40_atxd_239_wavelet_energy_ratio_tr_2_8_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wavelet energy ratio scale-2 / scale-8 of TR over 252d."""
    tr = _true_range(high, low, close)
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _haar_variance(w, 2) / (_haar_variance(w, 8) + 1e-12), raw=True)


def f40_atxd_240_fft_peak_freq_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Peak FFT frequency of TR over 252d (cycles per bar)."""
    tr = _true_range(high, low, close)

    def _peak(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = np.abs(f) ** 2
        psd[0] = 0
        return float(int(np.argmax(psd)) / n)
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_peak, raw=True)


def f40_atxd_241_spectral_entropy_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of normalized PSD of TR over 252d."""
    tr = _true_range(high, low, close)

    def _ent(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        psd[0] = 0
        tot = psd.sum()
        if tot <= 0:
            return np.nan
        p = psd / tot
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(p)))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f40_atxd_242_low_freq_coherence_tr_vol_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Squared coherence of TR vs log(volume) in low-freq band [0, 1/30 cyc/bar] over 252d."""
    tr = _true_range(high, low, close)
    lv = _safe_log(volume)
    combined = pd.concat([tr, lv], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        a = combined[max(0, i - YDAYS + 1):i + 1, 0]
        b = combined[max(0, i - YDAYS + 1):i + 1, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            continue
        a, b = a[m], b[m]
        n = len(a)
        fa = np.fft.rfft(a - a.mean()); fb = np.fft.rfft(b - b.mean())
        cutoff = max(int(n / 30), 2)
        Cxy = fa[:cutoff] * np.conjugate(fb[:cutoff])
        Pxx = np.abs(fa[:cutoff]) ** 2
        Pyy = np.abs(fb[:cutoff]) ** 2
        coh = (np.abs(Cxy) ** 2) / (Pxx * Pyy + 1e-12)
        out.iloc[i] = float(coh.mean())
    return out


def f40_atxd_243_phase_shift_tr_vol_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase shift between TR and log(volume) at peak cross-spectrum coherence, over 252d."""
    tr = _true_range(high, low, close)
    lv = _safe_log(volume)
    combined = pd.concat([tr, lv], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        a = combined[max(0, i - YDAYS + 1):i + 1, 0]
        b = combined[max(0, i - YDAYS + 1):i + 1, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            continue
        a, b = a[m], b[m]
        fa = np.fft.rfft(a - a.mean()); fb = np.fft.rfft(b - b.mean())
        Cxy = fa * np.conjugate(fb)
        idx = int(np.argmax(np.abs(Cxy[1:])) + 1)
        out.iloc[i] = float(np.angle(Cxy[idx]))
    return out


# ============================================================
# Bucket Z24 — TR regime durations / runs (244-251)
# ============================================================

def f40_atxd_244_time_share_tr_above_p75_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where TR > own 252d p75 within 63d."""
    tr = _true_range(high, low, close)
    p75 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return (tr > p75).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_245_time_share_tr_below_p25_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where TR < own 252d p25 within 63d."""
    tr = _true_range(high, low, close)
    p25 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    return (tr < p25).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_246_longest_tr_above_p75_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of TR > 252d p75 within 252d window."""
    tr = _true_range(high, low, close)
    p75 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return (tr > p75).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


def f40_atxd_247_longest_tr_below_p25_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest run of TR < 252d p25 within 252d window."""
    tr = _true_range(high, low, close)
    p25 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    return (tr < p25).astype(float).fillna(0.0).rolling(YDAYS, min_periods=QDAYS).apply(_longest_run, raw=True)


def f40_atxd_248_tr_diff_sign_flip_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of sign-changes in ΔTR over 252d — TR-direction churn."""
    tr = _true_range(high, low, close)
    return np.sign(tr.diff()).diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_249_bars_since_tr_above_p90_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since TR last exceeded own 252d p90."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.90).shift(1)
    return _bars_since((tr > p90).astype(float))


def f40_atxd_250_bars_since_tr_below_p10_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since TR last fell below own 252d p10."""
    tr = _true_range(high, low, close)
    p10 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.10).shift(1)
    return _bars_since((tr < p10).astype(float))


def f40_atxd_251_atr21_sma63_crossings_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR(21) crossings of its own SMA-63 within 252d."""
    a = _atr(high, low, close, MDAYS)
    sma = a.rolling(QDAYS, min_periods=MDAYS).mean()
    above = (a > sma).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z25 — TR persistence / memory (252-258)
# ============================================================

def f40_atxd_252_ar2_phi2_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(2) coef φ_2 of TR over 252d."""
    tr = _true_range(high, low, close)
    combined = pd.concat([tr, tr.shift(1), tr.shift(2)], axis=1).values

    def _phi2(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x1, x2 = arr[:, 0], arr[:, 1], arr[:, 2]
        m = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x1[m], x2[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            return float(beta[2])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _phi2(combined[i - YDAYS + 1:i + 1])
    return out


def f40_atxd_253_halflife_tr_shock_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Half-life of TR shock implied by AR(1) over 252d (clipped 0..200)."""
    tr = _true_range(high, low, close)
    rho = tr.rolling(YDAYS, min_periods=QDAYS).corr(tr.shift(1))
    ar = rho.abs().clip(upper=0.99, lower=1e-3)
    return (-np.log(2.0) / np.log(ar)).clip(upper=200.0)


def f40_atxd_254_rs_hurst_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of TR over 252d — long-memory of range process."""
    tr = _true_range(high, low, close)

    def _rs(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 30:
            return np.nan
        m = x.mean()
        y = (x - m).cumsum()
        r = y.max() - y.min()
        sd = x.std()
        if sd == 0:
            return np.nan
        return float(np.log(r / sd) / np.log(n))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_rs, raw=True)


def f40_atxd_255_sample_entropy_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sample entropy (m=2, r=0.2σ) of TR over 252d."""
    tr = _true_range(high, low, close)

    def _samp(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        tol = 0.2 * ww.std()
        if tol == 0:
            return np.nan
        if n > 100:
            ww = ww[::2]; n = len(ww)
        xs2 = np.array([ww[i:i + 2] for i in range(n - 2)])
        xs3 = np.array([ww[i:i + 3] for i in range(n - 3)])
        cnt_b = 0; cnt_a = 0
        for i in range(len(xs2)):
            cnt_b += (np.max(np.abs(xs2 - xs2[i]), axis=1) <= tol).sum() - 1
        for i in range(len(xs3)):
            cnt_a += (np.max(np.abs(xs3 - xs3[i]), axis=1) <= tol).sum() - 1
        if cnt_b == 0 or cnt_a == 0:
            return np.nan
        return float(-np.log(cnt_a / cnt_b))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_samp, raw=True)


def f40_atxd_256_approximate_entropy_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Approximate entropy (m=2) of TR over 252d."""
    tr = _true_range(high, low, close)

    def _ap(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        tol = 0.2 * ww.std()
        if tol == 0:
            return np.nan
        if n > 100:
            ww = ww[::2]; n = len(ww)

        def _phi(mm):
            xs = np.array([ww[i:i + mm] for i in range(n - mm + 1)])
            c = np.zeros(len(xs))
            for i in range(len(xs)):
                d = np.max(np.abs(xs - xs[i]), axis=1)
                c[i] = (d <= tol).sum() / len(xs)
            return np.mean(np.log(c[c > 0])) if (c > 0).any() else np.nan
        p1 = _phi(2); p2 = _phi(3)
        return float(p1 - p2) if np.isfinite(p1) and np.isfinite(p2) else np.nan
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_ap, raw=True)


def f40_atxd_257_permutation_entropy_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of TR over 252d."""
    tr = _true_range(high, low, close)

    def _perm(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        cnt = {}
        for i in range(n - 2):
            pat = tuple(np.argsort(ww[i:i + 3]))
            cnt[pat] = cnt.get(pat, 0) + 1
        tot = sum(cnt.values())
        ent = 0.0
        for v in cnt.values():
            p = v / tot
            ent -= p * np.log(p)
        return float(ent / np.log(6.0))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_perm, raw=True)


def f40_atxd_258_atr_momentum_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d slope of (ATR/ATR.shift(63)) ratio — ATR-momentum trend."""
    a = _atr(high, low, close, MDAYS)
    return _rolling_slope(_safe_div(a, a.shift(QDAYS)), QDAYS)


# ============================================================
# Bucket Z26 — ATR-volume / liquidity (259-264)
# ============================================================

def f40_atxd_259_volume_weighted_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted ATR: Σ(TR·volume) / Σvolume over 21d."""
    tr = _true_range(high, low, close)
    return _safe_div((tr * volume).rolling(MDAYS, min_periods=WDAYS).sum(),
                     volume.rolling(MDAYS, min_periods=WDAYS).sum())


def f40_atxd_260_atr_per_share_traded_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATR per share traded: ATR / mean volume over 21d — range "cost" per unit volume."""
    return _safe_div(_atr(high, low, close, MDAYS),
                     volume.rolling(MDAYS, min_periods=WDAYS).mean())


def f40_atxd_261_dollar_range_volume_product_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Σ TR · Σ volume over 21d — dollar-range-volume coupling proxy."""
    tr = _true_range(high, low, close)
    return tr.rolling(MDAYS, min_periods=WDAYS).sum() * volume.rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_262_volume_adjusted_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-adjusted ATR: ATR(21) × (volume / mean volume) — vol-flow-weighted range."""
    atr = _atr(high, low, close, MDAYS)
    vol_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return atr * vol_ratio


def f40_atxd_263_dollar_tr_mean_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dollar TR mean: TR × close averaged over 21d — typical dollar-range per bar."""
    return (_true_range(high, low, close) * close).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_264_range_volume_entropy_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of joint (TR-quantile, volume-quantile) over 252d using 4×4 binning."""
    tr = _true_range(high, low, close)
    combined = pd.concat([tr, volume], axis=1).values

    def _je(arr):
        a = arr[:, 0]; b = arr[:, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = a[m], b[m]
        try:
            a_bin = pd.qcut(a, 4, labels=False, duplicates='drop')
            b_bin = pd.qcut(b, 4, labels=False, duplicates='drop')
        except Exception:
            return np.nan
        joint = np.zeros((4, 4))
        for ai, bi in zip(a_bin, b_bin):
            if not (np.isnan(ai) or np.isnan(bi)):
                joint[int(ai), int(bi)] += 1
        tot = joint.sum()
        if tot == 0:
            return np.nan
        p = joint / tot
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _je(combined[i - YDAYS + 1:i + 1])
    return out


# ============================================================
# Bucket Z27 — Conditional / event-driven (265-270)
# ============================================================

def f40_atxd_265_atr21_after_gap_up_mean_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars following gap-up day (open_{t-1} > close_{t-2}) over 252d."""
    atr = _atr(high, low, close, MDAYS)
    gap_up_prior = (open.shift(1) > close.shift(2))
    sel = atr.where(gap_up_prior, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_266_atr21_after_gap_down_mean_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars following gap-down day over 252d."""
    atr = _atr(high, low, close, MDAYS)
    gap_dn_prior = (open.shift(1) < close.shift(2))
    sel = atr.where(gap_dn_prior, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_267_tr_after_shock_persistence_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR_t conditional on TR_{t-1} > 3·ATR(21).shift(2) — post-shock regime over 63d."""
    tr = _true_range(high, low, close)
    shock_prior = (tr.shift(1) > 3.0 * _atr(high, low, close, MDAYS).shift(2))
    sel = tr.where(shock_prior, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_268_tr_at_252d_high_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where close hits 252d-high, over 252d window."""
    tr = _true_range(high, low, close)
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    sel = tr.where(new_high, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_269_atr_spikes_near_252d_high_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR-spikes (TR > 2·ATR_21.shift(1)) within 5 bars of a 252d-high event over 252d."""
    tr = _true_range(high, low, close)
    atr_prior = _atr(high, low, close, MDAYS).shift(1)
    spike = (tr > 2.0 * atr_prior)
    near_high = (close >= close.rolling(YDAYS, min_periods=QDAYS).max())
    near_high_window = near_high.rolling(WDAYS, min_periods=1).max().astype(bool)
    return (spike & near_high_window).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_270_natr_pre_peak_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean NATR(21) in the 21 bars preceding a 252d-high event, over 252d."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    new_high = (close >= close.rolling(YDAYS, min_periods=QDAYS).max())
    # For each bar, look at NATR from 21 bars prior; use shift
    natr_lag21_mean = natr.rolling(MDAYS, min_periods=WDAYS).mean().shift(MDAYS)
    sel = natr_lag21_mean.where(new_high, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket Z28 — Compression-then-expansion subtleties (271-275)
# ============================================================

def f40_atxd_271_atr21_over_min_atr21_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / min(ATR(21), past 21d) — very-short compression release."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a, a.rolling(MDAYS, min_periods=WDAYS).min())


def f40_atxd_272_log_atr21_over_min_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log(ATR(21) / min(ATR(21), past 252d)) — annual log compression release."""
    a = _atr(high, low, close, MDAYS)
    return _safe_log(a) - _safe_log(a.rolling(YDAYS, min_periods=QDAYS).min())


def f40_atxd_273_compression_to_expansion_events_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Compression-to-expansion event count: TR > 1.5·rolling-21d-mean TR within 63d."""
    tr = _true_range(high, low, close)
    expansion = (tr > 1.5 * tr.rolling(MDAYS, min_periods=WDAYS).mean().shift(1))
    return expansion.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_274_bars_from_min_to_max_atr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars between min-ATR(21) and max-ATR(21) within trailing 63d window (compression-to-expansion span)."""
    a = _atr(high, low, close, MDAYS)

    def _span(w):
        ww = w[~np.isnan(w)]
        if len(ww) < MDAYS:
            return np.nan
        i_min = int(np.argmin(ww))
        i_max = int(np.argmax(ww))
        return float(abs(i_max - i_min))
    return a.rolling(QDAYS, min_periods=MDAYS).apply(_span, raw=True)


def f40_atxd_275_atr5_compression_release_q_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(5) compression Q-ratio: ATR(5) / min(ATR(5), past 21d) — fast-compression release."""
    a = _atr(high, low, close, WDAYS)
    return _safe_div(a, a.rolling(MDAYS, min_periods=WDAYS).min())


# ============================================================
# Bucket Z29 — Bollinger-on-ATR / ATR-EMA convergence (276-280)
# ============================================================

def f40_atxd_276_atr21_minus_ema_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) − EMA-21 of ATR(21) — distance from EMA-trend of itself."""
    a = _atr(high, low, close, MDAYS)
    return a - _ema(a, MDAYS)


def f40_atxd_277_atr21_over_ema63_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / EMA-63 of ATR(21) — ratio to longer-horizon EMA."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a, _ema(a, QDAYS))


def f40_atxd_278_atr_bollinger_upper_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger-on-ATR upper band: EMA-21 of ATR(21) + 2·rolling-21d std of ATR(21) over 252d window."""
    a = _atr(high, low, close, MDAYS)
    return _ema(a, MDAYS) + 2.0 * a.rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_279_atr_bollinger_lower_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger-on-ATR lower band: EMA-21 − 2·rolling-21d std of ATR(21)."""
    a = _atr(high, low, close, MDAYS)
    return _ema(a, MDAYS) - 2.0 * a.rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_280_atr_above_bollinger_upper_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) exceeds its own Bollinger-upper-on-ATR band, over 63d."""
    a = _atr(high, low, close, MDAYS)
    upper = _ema(a, MDAYS) + 2.0 * a.rolling(MDAYS, min_periods=WDAYS).std()
    return (a > upper).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket Z30 — Multi-scale ATR variants (281-285)
# ============================================================

def f40_atxd_281_zscore_log_atr5_over_atr63_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of log(ATR(5)/ATR(63)) within own 252d distribution."""
    ratio = _safe_log(_atr(high, low, close, WDAYS)) - _safe_log(_atr(high, low, close, QDAYS))
    return _rolling_zscore(ratio, YDAYS)


def f40_atxd_282_zscore_log_atr21_over_atr252_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of log(ATR(21)/ATR(252)) within own 252d distribution."""
    ratio = _safe_log(_atr(high, low, close, MDAYS)) - _safe_log(_atr(high, low, close, YDAYS))
    return _rolling_zscore(ratio, YDAYS)


def f40_atxd_283_atr21_over_atr5_inverse_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse ATR(21)/ATR(5) — slow-vs-fast regime (different concept from fast-vs-slow)."""
    return _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, WDAYS))


def f40_atxd_284_atr5_minus_atr63_velocity_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of (ATR(5) − ATR(63)) — fast-vs-intermediate vol-gap velocity."""
    gap = _atr(high, low, close, WDAYS) - _atr(high, low, close, QDAYS)
    return _rolling_slope(gap, MDAYS)


def f40_atxd_285_atr5_over_atr252_at_63d_min(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min of (ATR(5)/ATR(252)) within 63d — pre-peak compression detector."""
    return _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, YDAYS)).rolling(QDAYS, min_periods=MDAYS).min()


# ============================================================
# Bucket Z31 — Range-of-shadows (286-290)
# ============================================================

def f40_atxd_286_std_upper_shadow_over_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (upper-shadow / TR) over 21d — rejection-wick dispersion."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    return _safe_div(high - body_hi, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_287_std_lower_shadow_over_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (lower-shadow / TR) over 21d — demand-tail dispersion."""
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    return _safe_div(body_lo - low, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).std()


def f40_atxd_288_shadow_asymmetry_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (upper-shadow − lower-shadow) over 21d — net shadow asymmetry."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    return ((high - body_hi) - (body_lo - low)).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_289_shadow_concentration_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean max(upper,lower) / (upper+lower) over 21d — shadow concentration toward one side."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    upper = high - body_hi
    lower = body_lo - low
    return _safe_div(pd.concat([upper, lower], axis=1).max(axis=1), upper + lower).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_290_shadow_balance_reversal_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of sign-changes in (upper-shadow − lower-shadow) over 63d — shadow-bias flips."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    diff = (high - body_hi) - (body_lo - low)
    return np.sign(diff).diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket Z32 — Higher-order TR moments (291-295)
# ============================================================

def f40_atxd_291_var_delta_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of ΔTR over 252d — TR-acceleration variance."""
    tr = _true_range(high, low, close)
    return tr.diff().rolling(YDAYS, min_periods=QDAYS).var()


def f40_atxd_292_skew_delta_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of ΔTR over 252d."""
    tr = _true_range(high, low, close)
    return tr.diff().rolling(YDAYS, min_periods=QDAYS).skew()


def f40_atxd_293_kurt_delta_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurtosis of ΔTR over 252d."""
    tr = _true_range(high, low, close)
    return tr.diff().rolling(YDAYS, min_periods=QDAYS).kurt()


def f40_atxd_294_autocorr_trsq_lag1_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ARCH-style autocorr of TR² at lag 1 over 252d."""
    tr2 = _true_range(high, low, close) ** 2
    return tr2.rolling(YDAYS, min_periods=QDAYS).corr(tr2.shift(1))


def f40_atxd_295_autocorr_trsq_lag5_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ARCH-style autocorr of TR² at lag 5 over 252d."""
    tr2 = _true_range(high, low, close) ** 2
    return tr2.rolling(YDAYS, min_periods=QDAYS).corr(tr2.shift(WDAYS))


# ============================================================
# Bucket Z33 — Final misc (296-300)
# ============================================================

def f40_atxd_296_total_variation_tr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ|ΔTR| over 21d — short-horizon TR-instability total variation."""
    return _true_range(high, low, close).diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_297_total_variation_tr_normalized_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ|ΔTR| / Σ TR over 252d — normalized total variation."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum(),
                     tr.rolling(YDAYS, min_periods=QDAYS).sum())


def f40_atxd_298_mean_tr_pct_change_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (TR_t − TR_{t-1}) / TR_{t-1} over 21d — TR percentage change."""
    tr = _true_range(high, low, close)
    return tr.pct_change().rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_299_var_natr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of NATR(21) = ATR/close over 252d."""
    return _safe_div(_atr(high, low, close, MDAYS), close).rolling(YDAYS, min_periods=QDAYS).var()


def f40_atxd_300_skew_natr21_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of NATR(21) = ATR/close over 252d."""
    return _safe_div(_atr(high, low, close, MDAYS), close).rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
#                         REGISTRY 226-300
# ============================================================



def f40_atxd_226_upper_shadow_share_slope_63d_d2(open, high, low, close):
    return f40_atxd_226_upper_shadow_share_slope_63d(open, high, low, close).diff().diff()


def f40_atxd_227_lower_shadow_share_slope_63d_d2(open, high, low, close):
    return f40_atxd_227_lower_shadow_share_slope_63d(open, high, low, close).diff().diff()


def f40_atxd_228_body_share_slope_63d_d2(open, high, low, close):
    return f40_atxd_228_body_share_slope_63d(open, high, low, close).diff().diff()


def f40_atxd_229_var_close_pos_in_range_252d_d2(high, low, close):
    return f40_atxd_229_var_close_pos_in_range_252d(high, low, close).diff().diff()


def f40_atxd_230_hammer_pattern_count_252d_d2(open, high, low, close):
    return f40_atxd_230_hammer_pattern_count_252d(open, high, low, close).diff().diff()


def f40_atxd_231_shooting_star_count_252d_d2(open, high, low, close):
    return f40_atxd_231_shooting_star_count_252d(open, high, low, close).diff().diff()


def f40_atxd_232_doji_count_252d_d2(open, high, low, close):
    return f40_atxd_232_doji_count_252d(open, high, low, close).diff().diff()


def f40_atxd_233_engulfing_bar_count_252d_d2(open, close):
    return f40_atxd_233_engulfing_bar_count_252d(open, close).diff().diff()


def f40_atxd_234_three_white_soldiers_count_252d_d2(open, close):
    return f40_atxd_234_three_white_soldiers_count_252d(open, close).diff().diff()


def f40_atxd_235_three_black_crows_count_252d_d2(open, close):
    return f40_atxd_235_three_black_crows_count_252d(open, close).diff().diff()


def f40_atxd_236_slope_atr_on_up_bars_63d_d2(high, low, close):
    return f40_atxd_236_slope_atr_on_up_bars_63d(high, low, close).diff().diff()


def f40_atxd_237_wavelet_variance_tr_scale4_252d_d2(high, low, close):
    return f40_atxd_237_wavelet_variance_tr_scale4_252d(high, low, close).diff().diff()


def f40_atxd_238_wavelet_variance_tr_scale8_252d_d2(high, low, close):
    return f40_atxd_238_wavelet_variance_tr_scale8_252d(high, low, close).diff().diff()


def f40_atxd_239_wavelet_energy_ratio_tr_2_8_252d_d2(high, low, close):
    return f40_atxd_239_wavelet_energy_ratio_tr_2_8_252d(high, low, close).diff().diff()


def f40_atxd_240_fft_peak_freq_tr_252d_d2(high, low, close):
    return f40_atxd_240_fft_peak_freq_tr_252d(high, low, close).diff().diff()


def f40_atxd_241_spectral_entropy_tr_252d_d2(high, low, close):
    return f40_atxd_241_spectral_entropy_tr_252d(high, low, close).diff().diff()


def f40_atxd_242_low_freq_coherence_tr_vol_252d_d2(high, low, close, volume):
    return f40_atxd_242_low_freq_coherence_tr_vol_252d(high, low, close, volume).diff().diff()


def f40_atxd_243_phase_shift_tr_vol_252d_d2(high, low, close, volume):
    return f40_atxd_243_phase_shift_tr_vol_252d(high, low, close, volume).diff().diff()


def f40_atxd_244_time_share_tr_above_p75_63d_d2(high, low, close):
    return f40_atxd_244_time_share_tr_above_p75_63d(high, low, close).diff().diff()


def f40_atxd_245_time_share_tr_below_p25_63d_d2(high, low, close):
    return f40_atxd_245_time_share_tr_below_p25_63d(high, low, close).diff().diff()


def f40_atxd_246_longest_tr_above_p75_252d_d2(high, low, close):
    return f40_atxd_246_longest_tr_above_p75_252d(high, low, close).diff().diff()


def f40_atxd_247_longest_tr_below_p25_252d_d2(high, low, close):
    return f40_atxd_247_longest_tr_below_p25_252d(high, low, close).diff().diff()


def f40_atxd_248_tr_diff_sign_flip_count_252d_d2(high, low, close):
    return f40_atxd_248_tr_diff_sign_flip_count_252d(high, low, close).diff().diff()


def f40_atxd_249_bars_since_tr_above_p90_252d_d2(high, low, close):
    return f40_atxd_249_bars_since_tr_above_p90_252d(high, low, close).diff().diff()


def f40_atxd_250_bars_since_tr_below_p10_252d_d2(high, low, close):
    return f40_atxd_250_bars_since_tr_below_p10_252d(high, low, close).diff().diff()


def f40_atxd_251_atr21_sma63_crossings_252d_d2(high, low, close):
    return f40_atxd_251_atr21_sma63_crossings_252d(high, low, close).diff().diff()


def f40_atxd_252_ar2_phi2_tr_252d_d2(high, low, close):
    return f40_atxd_252_ar2_phi2_tr_252d(high, low, close).diff().diff()


def f40_atxd_253_halflife_tr_shock_252d_d2(high, low, close):
    return f40_atxd_253_halflife_tr_shock_252d(high, low, close).diff().diff()


def f40_atxd_254_rs_hurst_tr_252d_d2(high, low, close):
    return f40_atxd_254_rs_hurst_tr_252d(high, low, close).diff().diff()


def f40_atxd_255_sample_entropy_tr_252d_d2(high, low, close):
    return f40_atxd_255_sample_entropy_tr_252d(high, low, close).diff().diff()


def f40_atxd_256_approximate_entropy_tr_252d_d2(high, low, close):
    return f40_atxd_256_approximate_entropy_tr_252d(high, low, close).diff().diff()


def f40_atxd_257_permutation_entropy_tr_252d_d2(high, low, close):
    return f40_atxd_257_permutation_entropy_tr_252d(high, low, close).diff().diff()


def f40_atxd_258_atr_momentum_slope_63d_d2(high, low, close):
    return f40_atxd_258_atr_momentum_slope_63d(high, low, close).diff().diff()


def f40_atxd_259_volume_weighted_atr_21d_d2(high, low, close, volume):
    return f40_atxd_259_volume_weighted_atr_21d(high, low, close, volume).diff().diff()


def f40_atxd_260_atr_per_share_traded_21d_d2(high, low, close, volume):
    return f40_atxd_260_atr_per_share_traded_21d(high, low, close, volume).diff().diff()


def f40_atxd_261_dollar_range_volume_product_21d_d2(high, low, close, volume):
    return f40_atxd_261_dollar_range_volume_product_21d(high, low, close, volume).diff().diff()


def f40_atxd_262_volume_adjusted_atr_21d_d2(high, low, close, volume):
    return f40_atxd_262_volume_adjusted_atr_21d(high, low, close, volume).diff().diff()


def f40_atxd_263_dollar_tr_mean_21d_d2(high, low, close):
    return f40_atxd_263_dollar_tr_mean_21d(high, low, close).diff().diff()


def f40_atxd_264_range_volume_entropy_252d_d2(high, low, close, volume):
    return f40_atxd_264_range_volume_entropy_252d(high, low, close, volume).diff().diff()


def f40_atxd_265_atr21_after_gap_up_mean_252d_d2(open, high, low, close):
    return f40_atxd_265_atr21_after_gap_up_mean_252d(open, high, low, close).diff().diff()


def f40_atxd_266_atr21_after_gap_down_mean_252d_d2(open, high, low, close):
    return f40_atxd_266_atr21_after_gap_down_mean_252d(open, high, low, close).diff().diff()


def f40_atxd_267_tr_after_shock_persistence_63d_d2(high, low, close):
    return f40_atxd_267_tr_after_shock_persistence_63d(high, low, close).diff().diff()


def f40_atxd_268_tr_at_252d_high_mean_252d_d2(high, low, close):
    return f40_atxd_268_tr_at_252d_high_mean_252d(high, low, close).diff().diff()


def f40_atxd_269_atr_spikes_near_252d_high_252d_d2(high, low, close):
    return f40_atxd_269_atr_spikes_near_252d_high_252d(high, low, close).diff().diff()


def f40_atxd_270_natr_pre_peak_mean_252d_d2(high, low, close):
    return f40_atxd_270_natr_pre_peak_mean_252d(high, low, close).diff().diff()


def f40_atxd_271_atr21_over_min_atr21_21d_d2(high, low, close):
    return f40_atxd_271_atr21_over_min_atr21_21d(high, low, close).diff().diff()


def f40_atxd_272_log_atr21_over_min_252d_d2(high, low, close):
    return f40_atxd_272_log_atr21_over_min_252d(high, low, close).diff().diff()


def f40_atxd_273_compression_to_expansion_events_63d_d2(high, low, close):
    return f40_atxd_273_compression_to_expansion_events_63d(high, low, close).diff().diff()


def f40_atxd_274_bars_from_min_to_max_atr_63d_d2(high, low, close):
    return f40_atxd_274_bars_from_min_to_max_atr_63d(high, low, close).diff().diff()


def f40_atxd_275_atr5_compression_release_q_ratio_d2(high, low, close):
    return f40_atxd_275_atr5_compression_release_q_ratio(high, low, close).diff().diff()


def f40_atxd_276_atr21_minus_ema_atr21_d2(high, low, close):
    return f40_atxd_276_atr21_minus_ema_atr21(high, low, close).diff().diff()


def f40_atxd_277_atr21_over_ema63_atr_d2(high, low, close):
    return f40_atxd_277_atr21_over_ema63_atr(high, low, close).diff().diff()


def f40_atxd_278_atr_bollinger_upper_252d_d2(high, low, close):
    return f40_atxd_278_atr_bollinger_upper_252d(high, low, close).diff().diff()


def f40_atxd_279_atr_bollinger_lower_252d_d2(high, low, close):
    return f40_atxd_279_atr_bollinger_lower_252d(high, low, close).diff().diff()


def f40_atxd_280_atr_above_bollinger_upper_count_63d_d2(high, low, close):
    return f40_atxd_280_atr_above_bollinger_upper_count_63d(high, low, close).diff().diff()


def f40_atxd_281_zscore_log_atr5_over_atr63_252d_d2(high, low, close):
    return f40_atxd_281_zscore_log_atr5_over_atr63_252d(high, low, close).diff().diff()


def f40_atxd_282_zscore_log_atr21_over_atr252_252d_d2(high, low, close):
    return f40_atxd_282_zscore_log_atr21_over_atr252_252d(high, low, close).diff().diff()


def f40_atxd_283_atr21_over_atr5_inverse_ratio_d2(high, low, close):
    return f40_atxd_283_atr21_over_atr5_inverse_ratio(high, low, close).diff().diff()


def f40_atxd_284_atr5_minus_atr63_velocity_21d_d2(high, low, close):
    return f40_atxd_284_atr5_minus_atr63_velocity_21d(high, low, close).diff().diff()


def f40_atxd_285_atr5_over_atr252_at_63d_min_d2(high, low, close):
    return f40_atxd_285_atr5_over_atr252_at_63d_min(high, low, close).diff().diff()


def f40_atxd_286_std_upper_shadow_over_tr_21d_d2(open, high, low, close):
    return f40_atxd_286_std_upper_shadow_over_tr_21d(open, high, low, close).diff().diff()


def f40_atxd_287_std_lower_shadow_over_tr_21d_d2(open, high, low, close):
    return f40_atxd_287_std_lower_shadow_over_tr_21d(open, high, low, close).diff().diff()


def f40_atxd_288_shadow_asymmetry_21d_d2(open, high, low, close):
    return f40_atxd_288_shadow_asymmetry_21d(open, high, low, close).diff().diff()


def f40_atxd_289_shadow_concentration_21d_d2(open, high, low, close):
    return f40_atxd_289_shadow_concentration_21d(open, high, low, close).diff().diff()


def f40_atxd_290_shadow_balance_reversal_count_63d_d2(open, high, low, close):
    return f40_atxd_290_shadow_balance_reversal_count_63d(open, high, low, close).diff().diff()


def f40_atxd_291_var_delta_tr_252d_d2(high, low, close):
    return f40_atxd_291_var_delta_tr_252d(high, low, close).diff().diff()


def f40_atxd_292_skew_delta_tr_252d_d2(high, low, close):
    return f40_atxd_292_skew_delta_tr_252d(high, low, close).diff().diff()


def f40_atxd_293_kurt_delta_tr_252d_d2(high, low, close):
    return f40_atxd_293_kurt_delta_tr_252d(high, low, close).diff().diff()


def f40_atxd_294_autocorr_trsq_lag1_252d_d2(high, low, close):
    return f40_atxd_294_autocorr_trsq_lag1_252d(high, low, close).diff().diff()


def f40_atxd_295_autocorr_trsq_lag5_252d_d2(high, low, close):
    return f40_atxd_295_autocorr_trsq_lag5_252d(high, low, close).diff().diff()


def f40_atxd_296_total_variation_tr_21d_d2(high, low, close):
    return f40_atxd_296_total_variation_tr_21d(high, low, close).diff().diff()


def f40_atxd_297_total_variation_tr_normalized_252d_d2(high, low, close):
    return f40_atxd_297_total_variation_tr_normalized_252d(high, low, close).diff().diff()


def f40_atxd_298_mean_tr_pct_change_21d_d2(high, low, close):
    return f40_atxd_298_mean_tr_pct_change_21d(high, low, close).diff().diff()


def f40_atxd_299_var_natr21_252d_d2(high, low, close):
    return f40_atxd_299_var_natr21_252d(high, low, close).diff().diff()


def f40_atxd_300_skew_natr21_252d_d2(high, low, close):
    return f40_atxd_300_skew_natr21_252d(high, low, close).diff().diff()


ATR_EXPANSION_DYNAMICS_D2_REGISTRY_226_300 = {
    "f40_atxd_226_upper_shadow_share_slope_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_226_upper_shadow_share_slope_63d_d2},
    "f40_atxd_227_lower_shadow_share_slope_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_227_lower_shadow_share_slope_63d_d2},
    "f40_atxd_228_body_share_slope_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_228_body_share_slope_63d_d2},
    "f40_atxd_229_var_close_pos_in_range_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_229_var_close_pos_in_range_252d_d2},
    "f40_atxd_230_hammer_pattern_count_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_230_hammer_pattern_count_252d_d2},
    "f40_atxd_231_shooting_star_count_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_231_shooting_star_count_252d_d2},
    "f40_atxd_232_doji_count_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_232_doji_count_252d_d2},
    "f40_atxd_233_engulfing_bar_count_252d_d2": {"inputs": ["open", "close"], "func": f40_atxd_233_engulfing_bar_count_252d_d2},
    "f40_atxd_234_three_white_soldiers_count_252d_d2": {"inputs": ["open", "close"], "func": f40_atxd_234_three_white_soldiers_count_252d_d2},
    "f40_atxd_235_three_black_crows_count_252d_d2": {"inputs": ["open", "close"], "func": f40_atxd_235_three_black_crows_count_252d_d2},
    "f40_atxd_236_slope_atr_on_up_bars_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_236_slope_atr_on_up_bars_63d_d2},
    "f40_atxd_237_wavelet_variance_tr_scale4_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_237_wavelet_variance_tr_scale4_252d_d2},
    "f40_atxd_238_wavelet_variance_tr_scale8_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_238_wavelet_variance_tr_scale8_252d_d2},
    "f40_atxd_239_wavelet_energy_ratio_tr_2_8_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_239_wavelet_energy_ratio_tr_2_8_252d_d2},
    "f40_atxd_240_fft_peak_freq_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_240_fft_peak_freq_tr_252d_d2},
    "f40_atxd_241_spectral_entropy_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_241_spectral_entropy_tr_252d_d2},
    "f40_atxd_242_low_freq_coherence_tr_vol_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_242_low_freq_coherence_tr_vol_252d_d2},
    "f40_atxd_243_phase_shift_tr_vol_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_243_phase_shift_tr_vol_252d_d2},
    "f40_atxd_244_time_share_tr_above_p75_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_244_time_share_tr_above_p75_63d_d2},
    "f40_atxd_245_time_share_tr_below_p25_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_245_time_share_tr_below_p25_63d_d2},
    "f40_atxd_246_longest_tr_above_p75_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_246_longest_tr_above_p75_252d_d2},
    "f40_atxd_247_longest_tr_below_p25_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_247_longest_tr_below_p25_252d_d2},
    "f40_atxd_248_tr_diff_sign_flip_count_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_248_tr_diff_sign_flip_count_252d_d2},
    "f40_atxd_249_bars_since_tr_above_p90_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_249_bars_since_tr_above_p90_252d_d2},
    "f40_atxd_250_bars_since_tr_below_p10_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_250_bars_since_tr_below_p10_252d_d2},
    "f40_atxd_251_atr21_sma63_crossings_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_251_atr21_sma63_crossings_252d_d2},
    "f40_atxd_252_ar2_phi2_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_252_ar2_phi2_tr_252d_d2},
    "f40_atxd_253_halflife_tr_shock_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_253_halflife_tr_shock_252d_d2},
    "f40_atxd_254_rs_hurst_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_254_rs_hurst_tr_252d_d2},
    "f40_atxd_255_sample_entropy_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_255_sample_entropy_tr_252d_d2},
    "f40_atxd_256_approximate_entropy_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_256_approximate_entropy_tr_252d_d2},
    "f40_atxd_257_permutation_entropy_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_257_permutation_entropy_tr_252d_d2},
    "f40_atxd_258_atr_momentum_slope_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_258_atr_momentum_slope_63d_d2},
    "f40_atxd_259_volume_weighted_atr_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_259_volume_weighted_atr_21d_d2},
    "f40_atxd_260_atr_per_share_traded_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_260_atr_per_share_traded_21d_d2},
    "f40_atxd_261_dollar_range_volume_product_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_261_dollar_range_volume_product_21d_d2},
    "f40_atxd_262_volume_adjusted_atr_21d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_262_volume_adjusted_atr_21d_d2},
    "f40_atxd_263_dollar_tr_mean_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_263_dollar_tr_mean_21d_d2},
    "f40_atxd_264_range_volume_entropy_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_264_range_volume_entropy_252d_d2},
    "f40_atxd_265_atr21_after_gap_up_mean_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_265_atr21_after_gap_up_mean_252d_d2},
    "f40_atxd_266_atr21_after_gap_down_mean_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_266_atr21_after_gap_down_mean_252d_d2},
    "f40_atxd_267_tr_after_shock_persistence_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_267_tr_after_shock_persistence_63d_d2},
    "f40_atxd_268_tr_at_252d_high_mean_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_268_tr_at_252d_high_mean_252d_d2},
    "f40_atxd_269_atr_spikes_near_252d_high_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_269_atr_spikes_near_252d_high_252d_d2},
    "f40_atxd_270_natr_pre_peak_mean_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_270_natr_pre_peak_mean_252d_d2},
    "f40_atxd_271_atr21_over_min_atr21_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_271_atr21_over_min_atr21_21d_d2},
    "f40_atxd_272_log_atr21_over_min_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_272_log_atr21_over_min_252d_d2},
    "f40_atxd_273_compression_to_expansion_events_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_273_compression_to_expansion_events_63d_d2},
    "f40_atxd_274_bars_from_min_to_max_atr_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_274_bars_from_min_to_max_atr_63d_d2},
    "f40_atxd_275_atr5_compression_release_q_ratio_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_275_atr5_compression_release_q_ratio_d2},
    "f40_atxd_276_atr21_minus_ema_atr21_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_276_atr21_minus_ema_atr21_d2},
    "f40_atxd_277_atr21_over_ema63_atr_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_277_atr21_over_ema63_atr_d2},
    "f40_atxd_278_atr_bollinger_upper_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_278_atr_bollinger_upper_252d_d2},
    "f40_atxd_279_atr_bollinger_lower_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_279_atr_bollinger_lower_252d_d2},
    "f40_atxd_280_atr_above_bollinger_upper_count_63d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_280_atr_above_bollinger_upper_count_63d_d2},
    "f40_atxd_281_zscore_log_atr5_over_atr63_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_281_zscore_log_atr5_over_atr63_252d_d2},
    "f40_atxd_282_zscore_log_atr21_over_atr252_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_282_zscore_log_atr21_over_atr252_252d_d2},
    "f40_atxd_283_atr21_over_atr5_inverse_ratio_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_283_atr21_over_atr5_inverse_ratio_d2},
    "f40_atxd_284_atr5_minus_atr63_velocity_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_284_atr5_minus_atr63_velocity_21d_d2},
    "f40_atxd_285_atr5_over_atr252_at_63d_min_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_285_atr5_over_atr252_at_63d_min_d2},
    "f40_atxd_286_std_upper_shadow_over_tr_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_286_std_upper_shadow_over_tr_21d_d2},
    "f40_atxd_287_std_lower_shadow_over_tr_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_287_std_lower_shadow_over_tr_21d_d2},
    "f40_atxd_288_shadow_asymmetry_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_288_shadow_asymmetry_21d_d2},
    "f40_atxd_289_shadow_concentration_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_289_shadow_concentration_21d_d2},
    "f40_atxd_290_shadow_balance_reversal_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_290_shadow_balance_reversal_count_63d_d2},
    "f40_atxd_291_var_delta_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_291_var_delta_tr_252d_d2},
    "f40_atxd_292_skew_delta_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_292_skew_delta_tr_252d_d2},
    "f40_atxd_293_kurt_delta_tr_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_293_kurt_delta_tr_252d_d2},
    "f40_atxd_294_autocorr_trsq_lag1_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_294_autocorr_trsq_lag1_252d_d2},
    "f40_atxd_295_autocorr_trsq_lag5_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_295_autocorr_trsq_lag5_252d_d2},
    "f40_atxd_296_total_variation_tr_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_296_total_variation_tr_21d_d2},
    "f40_atxd_297_total_variation_tr_normalized_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_297_total_variation_tr_normalized_252d_d2},
    "f40_atxd_298_mean_tr_pct_change_21d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_298_mean_tr_pct_change_21d_d2},
    "f40_atxd_299_var_natr21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_299_var_natr21_252d_d2},
    "f40_atxd_300_skew_natr21_252d_d2": {"inputs": ["high", "low", "close"], "func": f40_atxd_300_skew_natr21_252d_d2},
}
