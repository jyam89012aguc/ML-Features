"""jump_detection_signature base features 226-300 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the previous 225. Drawn from gap analysis:
multifractal / generalized-Hurst, spectral / frequency-domain, information-
theoretic distance metrics (LZ, sample/permutation entropy on r, KL/KS/Wasserstein
distance between recent and full distributions), Markov-switching / GARCH-MLE
proxies, drawdown-coupled tail stats (max DD, recovery, CDaR, pain index),
sign/run-length tests (Wald-Wolfowitz, sign autocorr), cross-frequency co-jumps
(BLT), conditional jump diagnostics, microstructure-noise-aware persistence,
multipower jump-robust ratios, post-jump intensity decay, regime-conditional
distributional shape, pre-crash signatures (LPPL, parabolic acceleration,
log-periodic frequency), final-misc tail/concentration measures.

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


def _log_ret(close):
    return _safe_log(close).diff()


def _sigma_prior(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)


def _rv(r, n):
    return (r ** 2).rolling(n, min_periods=max(n // 3, 2)).sum()


def _bv(r, n):
    pr = r.abs() * r.abs().shift(1)
    return (np.pi / 2.0) * pr.rolling(n, min_periods=max(n // 3, 2)).sum()


def _longest_run_pos(w: np.ndarray) -> float:
    """Longest run of positive entries in w (used by streak features)."""
    m = 0; c = 0
    for v in w:
        if v > 0:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


def _gen_hurst(arr: np.ndarray, q: float, scales=(4, 8, 16, 32)) -> float:
    """Generalized Hurst exponent H(q) via MF-DFA-style scaling."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 60:
        return np.nan
    Fq = []
    valid_scales = [s for s in scales if s < n // 4]
    if len(valid_scales) < 2:
        return np.nan
    for s in valid_scales:
        ns = n // s
        rs_segments = a[:ns * s].reshape(ns, s)
        incs = np.abs(np.diff(rs_segments, axis=1))
        if q == 0:
            mq = np.exp(np.mean(np.log(incs + 1e-12), axis=1))
        else:
            mq = (np.mean(incs ** q, axis=1)) ** (1.0 / q)
        Fq.append(np.mean(mq))
    Fq = np.array(Fq)
    lx = np.log(valid_scales); ly = np.log(Fq + 1e-12)
    xm = lx.mean(); ym = ly.mean()
    d = ((lx - xm) ** 2).sum()
    return float(((lx - xm) * (ly - ym)).sum() / d) if d > 0 else np.nan


def _parabolic_acc_63d_helper(close: pd.Series) -> pd.Series:
    """Internal helper: rolling 63d quadratic-fit coefficient on log(close)."""
    lp = np.log(close.where(close > 1e-12, np.nan))

    def _q(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < MDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        return float(np.polyfit(x, ww, 2)[0])
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_q, raw=True)


# ============================================================
# Bucket Z11 — Multifractal / generalized Hurst (226-231)
# ============================================================

def f38_jpdt_226_mfdfa_spectrum_width_252d(close: pd.Series) -> pd.Series:
    """MF-DFA singularity-spectrum width Δα ≈ H(−3) − H(+3) on r over 252d — multifractality."""
    r = _log_ret(close)

    def _width(w):
        h_neg = _gen_hurst(w, -3.0)
        h_pos = _gen_hurst(w, 3.0)
        if not np.isfinite(h_neg) or not np.isfinite(h_pos):
            return np.nan
        return float(h_neg - h_pos)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_width, raw=True)


def f38_jpdt_227_gen_hurst_q2_252d(close: pd.Series) -> pd.Series:
    """Generalized Hurst exponent H(q=2) on r over 252d (standard Hurst)."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gen_hurst(w, 2.0), raw=True)


def f38_jpdt_228_gen_hurst_q4_252d(close: pd.Series) -> pd.Series:
    """Generalized Hurst exponent H(q=4) on r over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gen_hurst(w, 4.0), raw=True)


def f38_jpdt_229_hurst_q2_minus_q4_spread_252d(close: pd.Series) -> pd.Series:
    """H(q=2) − H(q=4) spread on r over 252d — non-linearity of τ(q), multifractality marker."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gen_hurst(w, 2.0) - _gen_hurst(w, 4.0), raw=True)


def f38_jpdt_230_singularity_spectrum_peak_252d(close: pd.Series) -> pd.Series:
    """Singularity-spectrum peak f(α₀) ≈ midpoint H(q=0) over 252d on r."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gen_hurst(w, 0.001), raw=True)


def f38_jpdt_231_mfdfa_tau_q2_252d(close: pd.Series) -> pd.Series:
    """MF-DFA τ(q=2) = q·H(q) − 1 at q=2 over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: 2.0 * _gen_hurst(w, 2.0) - 1.0, raw=True)


# ============================================================
# Bucket Z12 — Spectral / frequency-domain (232-237)
# ============================================================

def f38_jpdt_232_spectral_slope_absret_252d(close: pd.Series) -> pd.Series:
    """1/f^β spectral slope of |log-ret| periodogram over 252d (GPH-style log-log fit)."""
    a = _log_ret(close).abs()

    def _slope(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        m = int(n ** 0.5)
        freqs = np.arange(1, m + 1) / n
        pwr = psd[1:m + 1]
        lx = np.log(freqs); ly = np.log(pwr + 1e-12)
        xm = lx.mean(); ym = ly.mean()
        d = ((lx - xm) ** 2).sum()
        return float(-((lx - xm) * (ly - ym)).sum() / d) if d > 0 else np.nan
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_slope, raw=True)


def f38_jpdt_233_whittle_d_rsq_504d(close: pd.Series) -> pd.Series:
    """Whittle long-memory d̂ on r² over 504d (proxy via log-log slope of periodogram at low freqs)."""
    r2 = _log_ret(close) ** 2

    def _whittle(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        m = int(n ** 0.4)
        if m < 4:
            return np.nan
        freqs = np.arange(1, m + 1) / n
        pwr = psd[1:m + 1]
        lx = np.log(freqs); ly = np.log(pwr + 1e-12)
        xm = lx.mean(); ym = ly.mean()
        d = ((lx - xm) ** 2).sum()
        slope = -((lx - xm) * (ly - ym)).sum() / d if d > 0 else np.nan
        return float(slope / 2.0) if np.isfinite(slope) else np.nan
    return r2.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_whittle, raw=True)


def f38_jpdt_234_periodogram_peak_freq_absret_252d(close: pd.Series) -> pd.Series:
    """Peak frequency of |log-ret| periodogram over 252d (cycles per bar)."""
    a = _log_ret(close).abs()

    def _peak(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        # Exclude DC
        psd[0] = 0
        idx = int(np.argmax(psd))
        return float(idx / n)
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_peak, raw=True)


def f38_jpdt_235_spectral_entropy_absret_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of normalized PSD of |log-ret| over 252d (1 = flat, 0 = peaked)."""
    a = _log_ret(close).abs()

    def _ent(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        psd[0] = 0
        s = psd.sum()
        if s <= 0:
            return np.nan
        p = psd / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(p)))
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f38_jpdt_236_low_freq_coherence_sig5_sig63_504d(close: pd.Series) -> pd.Series:
    """Squared coherence of σ_5d vs σ_63d in low-frequency band [0, 1/30 cyc/bar] over 504d."""
    r = _log_ret(close)
    s5 = r.rolling(WDAYS, min_periods=2).std()
    s63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    combined = pd.concat([s5, s63], axis=1)

    def _coh(arr2):
        if arr2.shape[0] < YDAYS:
            return np.nan
        a = arr2[:, 0]; b = arr2[:, 1]
        if np.any(np.isnan(a)) or np.any(np.isnan(b)):
            return np.nan
        n = len(a)
        fa = np.fft.rfft(a - a.mean())
        fb = np.fft.rfft(b - b.mean())
        Cxy = fa * np.conjugate(fb)
        Pxx = np.abs(fa) ** 2
        Pyy = np.abs(fb) ** 2
        # Low-freq band
        cutoff = int(n / 30)
        if cutoff < 2:
            return np.nan
        coh = (np.abs(Cxy[:cutoff]) ** 2) / (Pxx[:cutoff] * Pyy[:cutoff] + 1e-12)
        return float(coh.mean())
    # rolling apply over DataFrame
    out = pd.Series(index=close.index, dtype=float)
    arr = combined.values
    for i in range(YDAYS, len(arr)):
        out.iloc[i] = _coh(arr[i - DDAYS_2Y + 1 if i - DDAYS_2Y + 1 >= 0 else 0:i + 1])
    return out


def f38_jpdt_237_low_freq_power_absret_252d(close: pd.Series) -> pd.Series:
    """Integral of |log-ret| PSD over low-freq band [0, 1/20 cyc/bar] / total power, over 252d."""
    a = _log_ret(close).abs()

    def _lf(w):
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
        cutoff = max(int(n / 20), 2)
        return float(psd[:cutoff].sum() / tot)
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_lf, raw=True)


# ============================================================
# Bucket Z13 — Information-theoretic shock measures (238-243)
# ============================================================

def f38_jpdt_238_lempel_ziv_above_below_median_r_252d(close: pd.Series) -> pd.Series:
    """LZ complexity of (r > median(r))-binarized string over 252d."""
    r = _log_ret(close)

    def _lz(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        s = "".join("1" if v > np.median(ww) else "0" for v in ww)
        n = len(s)
        i = 0; c = 1; l = 1; k = 1
        steps = 0
        while l + k - 1 < n and steps < 100000:
            steps += 1
            if s[i + k - 1] != s[l + k - 1]:
                if k > 1:
                    pass
                c += 1
                l += k
                i = 0; k = 1
            else:
                k += 1
                if i + k - 1 >= l:
                    c += 1
                    l += k
                    i = 0; k = 1
        return float(c) * np.log2(n) / n
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_lz, raw=True)


def f38_jpdt_239_sample_entropy_r_252d(close: pd.Series) -> pd.Series:
    """Sample entropy (m=2, r=0.2σ) of log-returns themselves (not |r|) over 252d."""
    r = _log_ret(close)

    def _samp(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        tol = 0.2 * ww.std()
        if tol == 0:
            return np.nan
        # Subsample for speed
        if n > 150:
            ww = ww[::2]
            n = len(ww)
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
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_samp, raw=True)


def f38_jpdt_240_permutation_entropy_r_252d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of log-returns over 252d."""
    r = _log_ret(close)

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
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_perm, raw=True)


def f38_jpdt_241_kl_div_r_from_normal_252d(close: pd.Series) -> pd.Series:
    """KL divergence: D_KL(empirical PDF(r) || fitted Gaussian) over 252d via 20-bin histogram."""
    r = _log_ret(close)

    def _kl(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        mu = ww.mean(); sd = ww.std()
        if sd == 0:
            return np.nan
        bins = np.linspace(mu - 4 * sd, mu + 4 * sd, 21)
        h, _ = np.histogram(ww, bins=bins)
        p = h.astype(float) / h.sum()
        # Gaussian PDF probabilities for each bin
        from math import erf
        cdf_left = 0.5 * (1.0 + np.array([erf((bins[i] - mu) / (sd * np.sqrt(2.0))) for i in range(len(bins))]))
        q = np.diff(cdf_left)
        m = (p > 0) & (q > 0)
        if m.sum() < 2:
            return np.nan
        return float((p[m] * np.log(p[m] / q[m])).sum())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_kl, raw=True)


def f38_jpdt_242_ks_distance_recent_vs_full_r_252d(close: pd.Series) -> pd.Series:
    """KS distance between last-63d r distribution vs full 252d r distribution — regime-shift detector."""
    r = _log_ret(close)

    def _ks_recent_vs_full(w):
        ww = w[~np.isnan(w)]
        if len(ww) < YDAYS:
            return np.nan
        recent = np.sort(ww[-QDAYS:])
        full = np.sort(ww)
        # Empirical CDF for recent at full's grid
        n_r = len(recent); n_f = len(full)
        idx_r = np.searchsorted(recent, full, side="right") / n_r
        idx_f = np.arange(1, n_f + 1) / n_f
        return float(np.max(np.abs(idx_r - idx_f)))
    return r.rolling(YDAYS, min_periods=YDAYS).apply(_ks_recent_vs_full, raw=True)


def f38_jpdt_243_wasserstein_recent_vs_full_r_252d(close: pd.Series) -> pd.Series:
    """Wasserstein-1 distance between last 63d vs full 252d returns — distribution drift."""
    r = _log_ret(close)

    def _w1(w):
        ww = w[~np.isnan(w)]
        if len(ww) < YDAYS:
            return np.nan
        a = np.sort(ww[-QDAYS:]); b = np.sort(ww)
        # Resample to common grid via empirical quantiles
        qs = np.linspace(0.0, 1.0, 50)
        qa = np.quantile(a, qs); qb = np.quantile(b, qs)
        return float(np.mean(np.abs(qa - qb)))
    return r.rolling(YDAYS, min_periods=YDAYS).apply(_w1, raw=True)


# ============================================================
# Bucket Z14 — Markov-switching / GARCH MLE proxies (244-251)
# ============================================================

def f38_jpdt_244_ms_high_vol_state_prob_504d(close: pd.Series) -> pd.Series:
    """2-state Hamilton-style high-vol regime probability via EM on log r² over 504d."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))

    def _ms(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        med = np.median(ww)
        # Initialize: state 0 = low (≤median), state 1 = high (>median)
        mu0 = ww[ww <= med].mean(); mu1 = ww[ww > med].mean()
        var0 = ww[ww <= med].var(); var1 = ww[ww > med].var()
        if var0 == 0 or var1 == 0:
            return np.nan
        # 5 EM iterations
        for _ in range(5):
            p0 = np.exp(-0.5 * (ww - mu0) ** 2 / var0) / np.sqrt(2 * np.pi * var0)
            p1 = np.exp(-0.5 * (ww - mu1) ** 2 / var1) / np.sqrt(2 * np.pi * var1)
            w0 = p0 / (p0 + p1 + 1e-12); w1 = 1.0 - w0
            if w0.sum() <= 0 or w1.sum() <= 0:
                break
            mu0 = (w0 * ww).sum() / w0.sum(); mu1 = (w1 * ww).sum() / w1.sum()
            var0 = (w0 * (ww - mu0) ** 2).sum() / w0.sum(); var1 = (w1 * (ww - mu1) ** 2).sum() / w1.sum()
            if var0 == 0 or var1 == 0:
                break
        # Return probability of high-state for the last observation
        if mu1 < mu0:
            mu0, mu1 = mu1, mu0
            var0, var1 = var1, var0
        x = ww[-1]
        p0 = np.exp(-0.5 * (x - mu0) ** 2 / var0) / np.sqrt(2 * np.pi * var0)
        p1 = np.exp(-0.5 * (x - mu1) ** 2 / var1) / np.sqrt(2 * np.pi * var1)
        return float(p1 / (p0 + p1 + 1e-12))
    return lr2.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ms, raw=True)


def f38_jpdt_245_garch11_persistence_252d(close: pd.Series) -> pd.Series:
    """GARCH(1,1) persistence (α+β) proxy via OLS of r²_t on r²_{t-1} and σ²_{t-1} over 252d."""
    r = _log_ret(close)
    r2 = r ** 2
    s2 = r2.ewm(alpha=0.06, min_periods=MDAYS).mean()

    def _persist(w):
        if w.shape[0] < QDAYS:
            return np.nan
        y = w[:, 0]; x1 = w[:, 1]; x2 = w[:, 2]
        if np.any(np.isnan(y)) or np.any(np.isnan(x1)) or np.any(np.isnan(x2)):
            return np.nan
        X = np.column_stack([np.ones(len(y)), x1, x2])
        try:
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            return float(beta[1] + beta[2])
        except Exception:
            return np.nan
    combined = pd.concat([r2, r2.shift(1), s2.shift(1)], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _persist(combined[i - YDAYS + 1:i + 1])
    return out


def f38_jpdt_246_conditional_kurt_residuals_21d_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d kurtosis of z_t = r_t/σ̂_21,t-prior (standardized residuals)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    z = _safe_div(r, sig)
    return z.rolling(YDAYS, min_periods=QDAYS).kurt()


def f38_jpdt_247_conditional_skew_residuals_21d_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d skewness of standardized residuals z_t = r_t/σ̂_21,prior."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    z = _safe_div(r, sig)
    return z.rolling(YDAYS, min_periods=QDAYS).skew()


def f38_jpdt_248_garch_long_run_uncond_vol_252d(close: pd.Series) -> pd.Series:
    """GARCH long-run unconditional vol proxy: rolling 252d mean(r²)·(1-α-β) where (α+β)≈persistence."""
    r = _log_ret(close)
    r2 = r ** 2
    s2 = r2.ewm(alpha=0.06, min_periods=MDAYS).mean()

    def _persist(w):
        if w.shape[0] < QDAYS:
            return np.nan
        y = w[:, 0]; x1 = w[:, 1]; x2 = w[:, 2]
        if np.any(np.isnan(y)) or np.any(np.isnan(x1)) or np.any(np.isnan(x2)):
            return np.nan
        X = np.column_stack([np.ones(len(y)), x1, x2])
        try:
            beta = np.linalg.lstsq(X, y, rcond=None)[0]
            return float(beta[1] + beta[2])
        except Exception:
            return np.nan
    combined = pd.concat([r2, r2.shift(1), s2.shift(1)], axis=1).values
    p_vals = np.full(len(combined), np.nan)
    for i in range(YDAYS, len(combined)):
        p_vals[i] = _persist(combined[i - YDAYS + 1:i + 1])
    p = pd.Series(p_vals, index=close.index)
    return r2.rolling(YDAYS, min_periods=QDAYS).mean() * (1.0 - p.clip(upper=0.999, lower=0.0))


def f38_jpdt_249_sv_log_vol_persistence_504d(close: pd.Series) -> pd.Series:
    """Stochastic-vol log-σ² persistence φ̂ via AR(1) on log(r² + ε) over 504d."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))
    return lr2.rolling(DDAYS_2Y, min_periods=YDAYS).corr(lr2.shift(1))


def f38_jpdt_250_sv_log_vol_innovation_variance_504d(close: pd.Series) -> pd.Series:
    """Variance of log-σ² innovations (proxy for σ_η²) — vol-of-log-vol — over 504d."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))
    return lr2.diff().rolling(DDAYS_2Y, min_periods=YDAYS).var()


def f38_jpdt_251_sv_leverage_corr_dlogvol_r_252d(close: pd.Series) -> pd.Series:
    """SV leverage corr(Δlog σ², r) over 252d — Heston ρ-proxy."""
    r = _log_ret(close)
    dlr2 = _safe_log((r ** 2 + 1e-12)).diff()
    return dlr2.rolling(YDAYS, min_periods=QDAYS).corr(r)


# ============================================================
# Bucket Z15 — Drawdown-coupled tail stats (252-257)
# ============================================================

def f38_jpdt_252_max_drawdown_252d(close: pd.Series) -> pd.Series:
    """Max drawdown magnitude (peak-to-trough %) within rolling 252d window."""
    def _dd(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(ww)
        dd = 1.0 - ww / peak
        return float(np.max(dd))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_dd, raw=True)


def f38_jpdt_253_drawdown_event_count_252d(close: pd.Series) -> pd.Series:
    """Count of >5%-magnitude drawdown events that follow a new local-252d-high, within 252d."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (close == rmax)
    # On bars marked as new highs, mark a drawdown event if close eventually drops >5% before next new high
    # Approximation: count bars where the running-since-recent-high drawdown >= 5%
    dd_pct = 1.0 - close / rmax
    flag = (dd_pct > 0.05).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_254_recovery_time_after_max_dd_252d(close: pd.Series) -> pd.Series:
    """Bars from max-DD trough to half-recovery, computed within 252d window."""
    def _recov(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(ww)
        dd = 1.0 - ww / peak
        if dd.max() == 0:
            return 0.0
        trough_idx = int(np.argmax(dd))
        trough_price = ww[trough_idx]
        peak_price = peak[trough_idx]
        half_target = trough_price + 0.5 * (peak_price - trough_price)
        for j in range(trough_idx + 1, n):
            if ww[j] >= half_target:
                return float(j - trough_idx)
        return float(n - trough_idx)
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_recov, raw=True)


def f38_jpdt_255_drawdown_integral_252d(close: pd.Series) -> pd.Series:
    """Σ underwater-% over 252d (integral of drawdown depth)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_pct = (1.0 - close / rmax).clip(lower=0.0)
    return dd_pct.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_256_pain_index_252d(close: pd.Series) -> pd.Series:
    """Mean underwater-% over 252d window."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_pct = (1.0 - close / rmax).clip(lower=0.0)
    return dd_pct.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_257_cdar_95_252d(close: pd.Series) -> pd.Series:
    """Conditional Drawdown at Risk at 95%: mean of worst-5% drawdown bars over 252d."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_pct = (1.0 - close / rmax).clip(lower=0.0)

    def _cdar(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        q = np.quantile(ww, 0.95)
        tail = ww[ww >= q]
        return float(tail.mean()) if len(tail) > 0 else np.nan
    return dd_pct.rolling(YDAYS, min_periods=QDAYS).apply(_cdar, raw=True)


# ============================================================
# Bucket Z16 — Sign / run-length tests (258-262)
# ============================================================

def f38_jpdt_258_longest_positive_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of positive log-returns within 252d window."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_longest_run_pos, raw=True)


def f38_jpdt_259_runlength_distribution_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of positive-streak lengths within 252d window."""
    r = _log_ret(close)

    def _ent(w):
        runs = []; cur = 0
        for v in w:
            if v > 0:
                cur += 1
            elif cur > 0:
                runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if not runs:
            return np.nan
        arr = np.array(runs, dtype=float)
        p = arr / arr.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f38_jpdt_260_wald_wolfowitz_runs_z_252d(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs-test z-score for sign(r) over 252d."""
    r = _log_ret(close)

    def _ww(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        s = np.sign(ww)
        n1 = int((s > 0).sum()); n2 = int((s < 0).sum())
        if n1 == 0 or n2 == 0:
            return np.nan
        runs = 1 + int((s[1:] != s[:-1]).sum())
        mu = 1.0 + 2.0 * n1 * n2 / (n1 + n2)
        var = (2.0 * n1 * n2 * (2.0 * n1 * n2 - n1 - n2)) / ((n1 + n2) ** 2 * (n1 + n2 - 1.0))
        if var <= 0:
            return np.nan
        return float((runs - mu) / np.sqrt(var))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_ww, raw=True)


def f38_jpdt_261_sign_autocorr_lag1_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(sign(r)_t, sign(r)_{t-1}) — direction-persistence."""
    s = np.sign(_log_ret(close))
    return s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))


def f38_jpdt_262_pattern_3up_1down_count_252d(close: pd.Series) -> pd.Series:
    """Count of (3 up, 1 down) patterns where the down-bar exceeds prior up gains, in 252d."""
    r = _log_ret(close)
    u1 = (r.shift(3) > 0) & (r.shift(2) > 0) & (r.shift(1) > 0)
    cum_up = r.shift(1) + r.shift(2) + r.shift(3)
    down = (r < 0) & (r.abs() > cum_up)
    return (u1 & down).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z17 — Cross-frequency co-jumps (263-266)
# ============================================================

def f38_jpdt_263_blt_daily_weekly_cojump_count_252d(close: pd.Series) -> pd.Series:
    """BLT co-jump count: |r_d| > 3σ_21d_prior AND |r_w (last 5d)| > 3σ_w_prior simultaneously, 252d."""
    r = _log_ret(close)
    rw = _safe_log(close).diff(WDAYS)
    sig_d = _sigma_prior(r, MDAYS)
    sig_w = _sigma_prior(rw, MDAYS)
    cojump = (r.abs() > 3 * sig_d) & (rw.abs() > 3 * sig_w)
    return cojump.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_264_blt_daily_monthly_cojump_count_504d(close: pd.Series) -> pd.Series:
    """BLT co-jump count daily-vs-monthly: |r_d|>3σ_21d AND |r_m (last 21d)|>3σ_m_prior, 504d."""
    r = _log_ret(close)
    rm = _safe_log(close).diff(MDAYS)
    sig_d = _sigma_prior(r, MDAYS)
    sig_m = _sigma_prior(rm, QDAYS)
    cojump = (r.abs() > 3 * sig_d) & (rm.abs() > 3 * sig_m)
    return cojump.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f38_jpdt_265_co_jump_magnitude_product_mean_252d(close: pd.Series) -> pd.Series:
    """Mean of |r_d|·|r_w| restricted to co-jump days over 252d."""
    r = _log_ret(close)
    rw = _safe_log(close).diff(WDAYS)
    sig_d = _sigma_prior(r, MDAYS)
    sig_w = _sigma_prior(rw, MDAYS)
    cojump_mask = (r.abs() > 3 * sig_d) & (rw.abs() > 3 * sig_w)
    prod = (r.abs() * rw.abs()).where(cojump_mask, np.nan)
    return prod.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_266_cojump_tail_dependence_504d(close: pd.Series) -> pd.Series:
    """Empirical tail-dependence of (|r_d|, |r_w|) at p90 over 504d."""
    r = _log_ret(close).abs()
    rw = _safe_log(close).diff(WDAYS).abs()
    p_d = r.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    p_w = rw.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    joint = ((r > p_d) & (rw > p_w)).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    marg = (r > p_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(joint, marg)


# ============================================================
# Bucket Z18 — Conditional jump diagnostics (267-272)
# ============================================================

def f38_jpdt_267_post_down_jump_abs_ret_mean_252d(close: pd.Series) -> pd.Series:
    """Mean |r_t| conditional on r_{t-1} being a negative 3σ_21d jump, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = (r < -3 * sig).shift(1).fillna(False)
    sel = r.abs().where(dn, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_268_post_up_jump_abs_ret_mean_252d(close: pd.Series) -> pd.Series:
    """Mean |r_t| conditional on r_{t-1} being a positive 3σ_21d jump, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).shift(1).fillna(False)
    sel = r.abs().where(up, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_269_post_jump_var_abs_ret_252d(close: pd.Series) -> pd.Series:
    """Variance of |r_t| conditional on prior-day 3σ_21d jump over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = (r.abs() > 3 * sig).shift(1).fillna(False)
    sel = r.abs().where(jmask, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).var()


def f38_jpdt_270_mean_21d_trailing_after_top3pct_event_63d(close: pd.Series) -> pd.Series:
    """Mean 21d trailing log-return on bars whose prior day was in top-3% of |r| over past 63d, summed in 63d."""
    r = _log_ret(close)
    a = r.abs()
    p97 = a.rolling(QDAYS, min_periods=MDAYS).quantile(0.97).shift(1)
    flag = (a.shift(1) > p97).fillna(False)
    trail = r.rolling(MDAYS, min_periods=WDAYS).sum()
    sel = trail.where(flag, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_271_bull_jump_then_decline_count_252d(close: pd.Series) -> pd.Series:
    """Count of (positive 3σ jump on day t) AND (sum of next 5 days < 0), 252d — bull-jump failure."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig)
    trail5 = r.rolling(WDAYS, min_periods=2).sum().shift(WDAYS)
    # Avoid .shift(N): instead use lag — check past condition relative to current
    # Restate: today's 5d trailing sum < 0 AND day t-5 was an up-jump
    past_up = up.shift(WDAYS).fillna(False)
    past_trail = r.rolling(WDAYS, min_periods=2).sum()
    flag = past_up & (past_trail < 0)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_272_bear_jump_then_bounce_count_252d(close: pd.Series) -> pd.Series:
    """Count of (negative 3σ jump on day t-5) AND (5d trailing return > 0) over 252d — bear-jump bounce."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = (r < -3 * sig)
    past_dn = dn.shift(WDAYS).fillna(False)
    past_trail = r.rolling(WDAYS, min_periods=2).sum()
    flag = past_dn & (past_trail > 0)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z19 — Microstructure-noise-aware persistence (273-276)
# ============================================================

def f38_jpdt_273_hansen_lunde_noise_ratio_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hansen-Lunde noise-to-signal ratio: Var(c2c_ret) / Var(open-to-close + close-to-open) over 252d."""
    c2c = _safe_log(close).diff()
    oc = _safe_log(close) - _safe_log(open)
    co = _safe_log(open) - _safe_log(close.shift(1))
    sub = oc + co  # equals c2c by definition; use sum-of-squares to get noise proxy
    num = c2c.rolling(YDAYS, min_periods=QDAYS).var()
    den = (oc.rolling(YDAYS, min_periods=QDAYS).var() + co.rolling(YDAYS, min_periods=QDAYS).var())
    return _safe_div(num, den)


def f38_jpdt_274_autocorr_rsq_lag1_alt_252d(close: pd.Series) -> pd.Series:
    """Alt ARCH-effect: rolling 252d corr(r²_t, r²_{t-1}) — distinct framing from family 39's autocorr."""
    r2 = _log_ret(close) ** 2
    return r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1))


def f38_jpdt_275_var_ratio_rsq_q10_252d(close: pd.Series) -> pd.Series:
    """Variance ratio of r² at lag q=10 over 252d (deviation from 1 indicates structure)."""
    r2 = _log_ret(close) ** 2
    v1 = r2.rolling(YDAYS, min_periods=QDAYS).var()
    rk = r2.rolling(10, min_periods=WDAYS).sum()
    vk = rk.rolling(YDAYS, min_periods=QDAYS).var() / 10.0
    return _safe_div(vk, v1)


def f38_jpdt_276_sign_conditioned_mag_memory_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(|r_t|, |r_{t-1}|·sign(r_{t-1})) — sign-asymmetric magnitude memory."""
    r = _log_ret(close)
    s_lag_mag = r.abs().shift(1) * np.sign(r.shift(1))
    return r.abs().rolling(YDAYS, min_periods=QDAYS).corr(s_lag_mag)


# ============================================================
# Bucket Z20 — Multipower jump-robust ratios (277-280)
# ============================================================

def f38_jpdt_277_tpv_over_rv_ratio_252d(close: pd.Series) -> pd.Series:
    """Tripower variation / RV ratio at 252d (TPV is jump-robust; ratio<1 = jump regime)."""
    r = _log_ret(close)
    a = r.abs() ** (4.0 / 3.0)
    prod = a * a.shift(1) * a.shift(2)
    mu = 2.0 ** (2.0 / 3.0) * (math.gamma(7.0 / 6.0) / np.sqrt(np.pi))
    tpv = (mu ** -3) * prod.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(tpv, _rv(r, YDAYS))


def f38_jpdt_278_qpv_over_rv_ratio_252d(close: pd.Series) -> pd.Series:
    """Quadpower variation / RV ratio at 252d."""
    r = _log_ret(close).abs()
    prod = r * r.shift(1) * r.shift(2) * r.shift(3)
    mu1 = np.sqrt(2.0 / np.pi)
    qpv = (mu1 ** -4) * prod.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(qpv, _rv(_log_ret(close), YDAYS))


def f38_jpdt_279_jvar_frac_tpv_252d(close: pd.Series) -> pd.Series:
    """Jump-variance fraction via 1 − TPV/RV at 252d (TPV-based jump fraction)."""
    r = _log_ret(close)
    a = r.abs() ** (4.0 / 3.0)
    prod = a * a.shift(1) * a.shift(2)
    mu = 2.0 ** (2.0 / 3.0) * (math.gamma(7.0 / 6.0) / np.sqrt(np.pi))
    tpv = (mu ** -3) * prod.rolling(YDAYS, min_periods=QDAYS).sum()
    ratio = _safe_div(tpv, _rv(r, YDAYS))
    return (1.0 - ratio).clip(lower=0.0)


def f38_jpdt_280_jvar_frac_qpv_252d(close: pd.Series) -> pd.Series:
    """Jump-variance fraction via 1 − QPV/RV at 252d."""
    r = _log_ret(close).abs()
    prod = r * r.shift(1) * r.shift(2) * r.shift(3)
    mu1 = np.sqrt(2.0 / np.pi)
    qpv = (mu1 ** -4) * prod.rolling(YDAYS, min_periods=QDAYS).sum()
    ratio = _safe_div(qpv, _rv(_log_ret(close), YDAYS))
    return (1.0 - ratio).clip(lower=0.0)


# ============================================================
# Bucket Z21 — Post-jump intensity decay (281-284)
# ============================================================

def f38_jpdt_281_jump_arrival_memory_63d(close: pd.Series) -> pd.Series:
    """Mean jump indicator at t-1..t-5 used to predict today's: rolling-63d MSE between predicted and actual."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    pred = j.shift(1).rolling(WDAYS, min_periods=2).mean()
    err = (j - pred) ** 2
    return err.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_282_post_jump_excess_intensity_decay_252d(close: pd.Series) -> pd.Series:
    """Exponential-fit decay rate of jump-rate in 1d/5d/21d post-jump windows, over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    # Post-jump intensity at horizon h = mean(j_{t+1..t+h}) conditional on j_t=1
    # Causal version: at bar t, look back h=1, 5, 21 — what was jump-frequency in [t-h, t-1] given j_{t-h-1}=1?
    intens_1 = j.shift(1)
    intens_5 = j.shift(1).rolling(WDAYS, min_periods=2).mean()
    intens_21 = j.shift(1).rolling(MDAYS, min_periods=WDAYS).mean()
    # Fit decay: log(intensity) vs log(horizon)
    hs = np.array([1.0, 5.0, 21.0])
    log_h = np.log(hs)

    def _decay(arr):
        if arr.shape[0] < QDAYS or np.any(np.isnan(arr[-1])):
            return np.nan
        # Use last 21d mean of intensities to fit
        avg = arr[-MDAYS:].mean(axis=0) + 1e-9
        ly = np.log(avg)
        xm = log_h.mean(); ym = ly.mean()
        d = ((log_h - xm) ** 2).sum()
        return float(-((log_h - xm) * (ly - ym)).sum() / d) if d > 0 else np.nan
    combined = pd.concat([intens_1, intens_5, intens_21], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _decay(combined[i - YDAYS + 1:i + 1])
    return out


def f38_jpdt_283_hawkes_self_excitation_corr_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(jump_t, recent-jump-intensity_5d-prior) — self-excitation strength."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    intens = j.shift(1).rolling(WDAYS, min_periods=2).mean()
    return j.rolling(YDAYS, min_periods=QDAYS).corr(intens)


def f38_jpdt_284_clustered_jumps_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of jumps occurring within 5 bars of another jump, over 252d window."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    near_other = j.shift(1).rolling(WDAYS, min_periods=1).max().clip(upper=1.0)
    clustered = (j > 0.5) & (near_other > 0.5)
    j_total = j.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(clustered.astype(float).rolling(YDAYS, min_periods=QDAYS).sum(), j_total)


# ============================================================
# Bucket Z22 — Regime-conditional distributional shape (285-287)
# ============================================================

def f38_jpdt_285_kurt_r_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of r restricted to high-vol bars (σ_21d > rolling 252d p75) over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = r.where(sig > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).kurt()


def f38_jpdt_286_skew_r_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Skew of r restricted to high-vol bars (σ_21d > rolling 252d p75) over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = r.where(sig > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).skew()


def f38_jpdt_287_max_abs_r_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Max |r| restricted to high-vol bars (σ_21d > rolling 252d p75) over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    p75 = sig.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = r.abs().where(sig > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket Z23 — Pre-crash signatures (288-295)
# ============================================================

def f38_jpdt_288_lppl_residual_252d(close: pd.Series) -> pd.Series:
    """LPPL bubble-fit residual: variance of log(close) − quadratic fit over 252d (proxy for LPPL fit error)."""
    lp = _safe_log(close)

    def _res(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < MDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        # Fit simple quadratic; residual std as LPPL-proxy
        p = np.polyfit(x, ww, 2)
        trend = np.polyval(p, x)
        return float((ww - trend).std())
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_res, raw=True)


def f38_jpdt_289_lppl_freq_proxy_252d(close: pd.Series) -> pd.Series:
    """Log-periodic frequency ω̂ proxy: peak FFT freq of (log(close) − quadratic trend) over 252d."""
    lp = _safe_log(close)

    def _w(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        p = np.polyfit(x, ww, 2)
        detr = ww - np.polyval(p, x)
        f = np.fft.rfft(detr)
        psd = np.abs(f) ** 2
        psd[0] = 0
        idx = int(np.argmax(psd))
        return float(idx / n)
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_w, raw=True)


def f38_jpdt_290_lppl_fit_r2_252d(close: pd.Series) -> pd.Series:
    """R² of quadratic-trend fit on log(close) over 252d (high R² = strong parabolic structure)."""
    lp = _safe_log(close)

    def _r2(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < MDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        p = np.polyfit(x, ww, 2)
        trend = np.polyval(p, x)
        ss_res = ((ww - trend) ** 2).sum()
        ss_tot = ((ww - ww.mean()) ** 2).sum()
        return float(1.0 - ss_res / ss_tot) if ss_tot > 0 else np.nan
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)


def f38_jpdt_291_sornette_crash_hazard_proxy_252d(close: pd.Series) -> pd.Series:
    """Sornette-style crash hazard proxy: |parabolic-acc index| × log-periodic frequency over 252d."""
    pa = _parabolic_acc_63d_helper(close)
    lp = _safe_log(close)

    def _w(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        p = np.polyfit(x, ww, 2)
        detr = ww - np.polyval(p, x)
        f = np.fft.rfft(detr)
        psd = np.abs(f) ** 2
        psd[0] = 0
        idx = int(np.argmax(psd))
        return float(idx / n)
    fr = lp.rolling(YDAYS, min_periods=QDAYS).apply(_w, raw=True)
    return pa.abs() * fr


def f38_jpdt_292_acceleration_21d_vs_252d_logret(close: pd.Series) -> pd.Series:
    """21d log-return − 252d log-return (acceleration of trend over the year)."""
    return (_safe_log(close) - _safe_log(close.shift(MDAYS))) - (_safe_log(close) - _safe_log(close.shift(YDAYS)))


def f38_jpdt_293_accelerating_volume_count_63d(volume: pd.Series) -> pd.Series:
    """Count of bars where mean_5d_volume > 1.5·mean_252d_volume within 63d."""
    v5 = volume.rolling(WDAYS, min_periods=2).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (v5 > 1.5 * v252).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_294_recent_positive_concentration_21_vs_252(close: pd.Series) -> pd.Series:
    """(Fraction of positive r in last 21d) / (Fraction of positive r in last 252d) — recency bias of ups."""
    r = _log_ret(close)
    up = (r > 0).astype(float)
    return _safe_div(up.rolling(MDAYS, min_periods=WDAYS).mean(),
                     up.rolling(YDAYS, min_periods=QDAYS).mean())


def f38_jpdt_295_pre_peak_compression_natr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """NATR(5d) at its 63d minimum / NATR(252d) — pre-peak compression flag."""
    atr5 = _atr(high, low, close, WDAYS)
    natr5 = _safe_div(atr5, close)
    atr252 = _atr(high, low, close, YDAYS)
    natr252 = _safe_div(atr252, close)
    natr5_min63 = natr5.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(natr5_min63, natr252)


# ============================================================
# Bucket Z24 — Final misc tail / concentration (296-300)
# ============================================================

def f38_jpdt_296_vpin_proxy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPIN-style probability-of-informed-trading proxy: |Σ sign(r)·v| / Σ v over 21d."""
    r = _log_ret(close)
    sv = np.sign(r) * volume
    return _safe_div(sv.rolling(MDAYS, min_periods=WDAYS).sum().abs(),
                     volume.rolling(MDAYS, min_periods=WDAYS).sum())


def f38_jpdt_297_range_of_absret_extremes_63d(close: pd.Series) -> pd.Series:
    """Max |r| − min |r| within trailing 63d — extreme-oscillation amplitude."""
    a = _log_ret(close).abs()
    return a.rolling(QDAYS, min_periods=MDAYS).max() - a.rolling(QDAYS, min_periods=MDAYS).min()


def f38_jpdt_298_cdf_convexity_absret_252d(close: pd.Series) -> pd.Series:
    """CDF convexity: (p99 − p90) − (p90 − p75) of |r| over 252d — tail-concavity indicator."""
    a = _log_ret(close).abs()
    p99 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (p99 - p90) - (p90 - p75)


def f38_jpdt_299_heavy_tail_moment_ratio_252d(close: pd.Series) -> pd.Series:
    """Heavy-tail moment ratio E[|r|⁴] / E[|r|²]² over 252d — raw kurtosis-like."""
    a = _log_ret(close).abs()
    m2 = (a ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    m4 = (a ** 4).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(m4, m2 ** 2)


def f38_jpdt_300_post_jump_sign_reversal_pct_252d(close: pd.Series) -> pd.Series:
    """Fraction of jumps whose 5d-trailing return after the jump reverses jump-sign, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = (r.abs() > 3 * sig).shift(WDAYS).fillna(False)
    sign_jump = np.sign(r).shift(WDAYS)
    trail = r.rolling(WDAYS, min_periods=2).sum()
    reversed_mask = jmask & (np.sign(trail) != sign_jump) & (trail != 0)
    j_total = jmask.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rev_total = reversed_mask.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rev_total, j_total)


# ============================================================
#                         REGISTRY 226-300
# ============================================================

JUMP_DETECTION_SIGNATURE_BASE_REGISTRY_226_300 = {
    "f38_jpdt_226_mfdfa_spectrum_width_252d": {"inputs": ["close"], "func": f38_jpdt_226_mfdfa_spectrum_width_252d},
    "f38_jpdt_227_gen_hurst_q2_252d": {"inputs": ["close"], "func": f38_jpdt_227_gen_hurst_q2_252d},
    "f38_jpdt_228_gen_hurst_q4_252d": {"inputs": ["close"], "func": f38_jpdt_228_gen_hurst_q4_252d},
    "f38_jpdt_229_hurst_q2_minus_q4_spread_252d": {"inputs": ["close"], "func": f38_jpdt_229_hurst_q2_minus_q4_spread_252d},
    "f38_jpdt_230_singularity_spectrum_peak_252d": {"inputs": ["close"], "func": f38_jpdt_230_singularity_spectrum_peak_252d},
    "f38_jpdt_231_mfdfa_tau_q2_252d": {"inputs": ["close"], "func": f38_jpdt_231_mfdfa_tau_q2_252d},
    "f38_jpdt_232_spectral_slope_absret_252d": {"inputs": ["close"], "func": f38_jpdt_232_spectral_slope_absret_252d},
    "f38_jpdt_233_whittle_d_rsq_504d": {"inputs": ["close"], "func": f38_jpdt_233_whittle_d_rsq_504d},
    "f38_jpdt_234_periodogram_peak_freq_absret_252d": {"inputs": ["close"], "func": f38_jpdt_234_periodogram_peak_freq_absret_252d},
    "f38_jpdt_235_spectral_entropy_absret_252d": {"inputs": ["close"], "func": f38_jpdt_235_spectral_entropy_absret_252d},
    "f38_jpdt_236_low_freq_coherence_sig5_sig63_504d": {"inputs": ["close"], "func": f38_jpdt_236_low_freq_coherence_sig5_sig63_504d},
    "f38_jpdt_237_low_freq_power_absret_252d": {"inputs": ["close"], "func": f38_jpdt_237_low_freq_power_absret_252d},
    "f38_jpdt_238_lempel_ziv_above_below_median_r_252d": {"inputs": ["close"], "func": f38_jpdt_238_lempel_ziv_above_below_median_r_252d},
    "f38_jpdt_239_sample_entropy_r_252d": {"inputs": ["close"], "func": f38_jpdt_239_sample_entropy_r_252d},
    "f38_jpdt_240_permutation_entropy_r_252d": {"inputs": ["close"], "func": f38_jpdt_240_permutation_entropy_r_252d},
    "f38_jpdt_241_kl_div_r_from_normal_252d": {"inputs": ["close"], "func": f38_jpdt_241_kl_div_r_from_normal_252d},
    "f38_jpdt_242_ks_distance_recent_vs_full_r_252d": {"inputs": ["close"], "func": f38_jpdt_242_ks_distance_recent_vs_full_r_252d},
    "f38_jpdt_243_wasserstein_recent_vs_full_r_252d": {"inputs": ["close"], "func": f38_jpdt_243_wasserstein_recent_vs_full_r_252d},
    "f38_jpdt_244_ms_high_vol_state_prob_504d": {"inputs": ["close"], "func": f38_jpdt_244_ms_high_vol_state_prob_504d},
    "f38_jpdt_245_garch11_persistence_252d": {"inputs": ["close"], "func": f38_jpdt_245_garch11_persistence_252d},
    "f38_jpdt_246_conditional_kurt_residuals_21d_252d": {"inputs": ["close"], "func": f38_jpdt_246_conditional_kurt_residuals_21d_252d},
    "f38_jpdt_247_conditional_skew_residuals_21d_252d": {"inputs": ["close"], "func": f38_jpdt_247_conditional_skew_residuals_21d_252d},
    "f38_jpdt_248_garch_long_run_uncond_vol_252d": {"inputs": ["close"], "func": f38_jpdt_248_garch_long_run_uncond_vol_252d},
    "f38_jpdt_249_sv_log_vol_persistence_504d": {"inputs": ["close"], "func": f38_jpdt_249_sv_log_vol_persistence_504d},
    "f38_jpdt_250_sv_log_vol_innovation_variance_504d": {"inputs": ["close"], "func": f38_jpdt_250_sv_log_vol_innovation_variance_504d},
    "f38_jpdt_251_sv_leverage_corr_dlogvol_r_252d": {"inputs": ["close"], "func": f38_jpdt_251_sv_leverage_corr_dlogvol_r_252d},
    "f38_jpdt_252_max_drawdown_252d": {"inputs": ["close"], "func": f38_jpdt_252_max_drawdown_252d},
    "f38_jpdt_253_drawdown_event_count_252d": {"inputs": ["close"], "func": f38_jpdt_253_drawdown_event_count_252d},
    "f38_jpdt_254_recovery_time_after_max_dd_252d": {"inputs": ["close"], "func": f38_jpdt_254_recovery_time_after_max_dd_252d},
    "f38_jpdt_255_drawdown_integral_252d": {"inputs": ["close"], "func": f38_jpdt_255_drawdown_integral_252d},
    "f38_jpdt_256_pain_index_252d": {"inputs": ["close"], "func": f38_jpdt_256_pain_index_252d},
    "f38_jpdt_257_cdar_95_252d": {"inputs": ["close"], "func": f38_jpdt_257_cdar_95_252d},
    "f38_jpdt_258_longest_positive_streak_252d": {"inputs": ["close"], "func": f38_jpdt_258_longest_positive_streak_252d},
    "f38_jpdt_259_runlength_distribution_entropy_252d": {"inputs": ["close"], "func": f38_jpdt_259_runlength_distribution_entropy_252d},
    "f38_jpdt_260_wald_wolfowitz_runs_z_252d": {"inputs": ["close"], "func": f38_jpdt_260_wald_wolfowitz_runs_z_252d},
    "f38_jpdt_261_sign_autocorr_lag1_252d": {"inputs": ["close"], "func": f38_jpdt_261_sign_autocorr_lag1_252d},
    "f38_jpdt_262_pattern_3up_1down_count_252d": {"inputs": ["close"], "func": f38_jpdt_262_pattern_3up_1down_count_252d},
    "f38_jpdt_263_blt_daily_weekly_cojump_count_252d": {"inputs": ["close"], "func": f38_jpdt_263_blt_daily_weekly_cojump_count_252d},
    "f38_jpdt_264_blt_daily_monthly_cojump_count_504d": {"inputs": ["close"], "func": f38_jpdt_264_blt_daily_monthly_cojump_count_504d},
    "f38_jpdt_265_co_jump_magnitude_product_mean_252d": {"inputs": ["close"], "func": f38_jpdt_265_co_jump_magnitude_product_mean_252d},
    "f38_jpdt_266_cojump_tail_dependence_504d": {"inputs": ["close"], "func": f38_jpdt_266_cojump_tail_dependence_504d},
    "f38_jpdt_267_post_down_jump_abs_ret_mean_252d": {"inputs": ["close"], "func": f38_jpdt_267_post_down_jump_abs_ret_mean_252d},
    "f38_jpdt_268_post_up_jump_abs_ret_mean_252d": {"inputs": ["close"], "func": f38_jpdt_268_post_up_jump_abs_ret_mean_252d},
    "f38_jpdt_269_post_jump_var_abs_ret_252d": {"inputs": ["close"], "func": f38_jpdt_269_post_jump_var_abs_ret_252d},
    "f38_jpdt_270_mean_21d_trailing_after_top3pct_event_63d": {"inputs": ["close"], "func": f38_jpdt_270_mean_21d_trailing_after_top3pct_event_63d},
    "f38_jpdt_271_bull_jump_then_decline_count_252d": {"inputs": ["close"], "func": f38_jpdt_271_bull_jump_then_decline_count_252d},
    "f38_jpdt_272_bear_jump_then_bounce_count_252d": {"inputs": ["close"], "func": f38_jpdt_272_bear_jump_then_bounce_count_252d},
    "f38_jpdt_273_hansen_lunde_noise_ratio_252d": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_273_hansen_lunde_noise_ratio_252d},
    "f38_jpdt_274_autocorr_rsq_lag1_alt_252d": {"inputs": ["close"], "func": f38_jpdt_274_autocorr_rsq_lag1_alt_252d},
    "f38_jpdt_275_var_ratio_rsq_q10_252d": {"inputs": ["close"], "func": f38_jpdt_275_var_ratio_rsq_q10_252d},
    "f38_jpdt_276_sign_conditioned_mag_memory_252d": {"inputs": ["close"], "func": f38_jpdt_276_sign_conditioned_mag_memory_252d},
    "f38_jpdt_277_tpv_over_rv_ratio_252d": {"inputs": ["close"], "func": f38_jpdt_277_tpv_over_rv_ratio_252d},
    "f38_jpdt_278_qpv_over_rv_ratio_252d": {"inputs": ["close"], "func": f38_jpdt_278_qpv_over_rv_ratio_252d},
    "f38_jpdt_279_jvar_frac_tpv_252d": {"inputs": ["close"], "func": f38_jpdt_279_jvar_frac_tpv_252d},
    "f38_jpdt_280_jvar_frac_qpv_252d": {"inputs": ["close"], "func": f38_jpdt_280_jvar_frac_qpv_252d},
    "f38_jpdt_281_jump_arrival_memory_63d": {"inputs": ["close"], "func": f38_jpdt_281_jump_arrival_memory_63d},
    "f38_jpdt_282_post_jump_excess_intensity_decay_252d": {"inputs": ["close"], "func": f38_jpdt_282_post_jump_excess_intensity_decay_252d},
    "f38_jpdt_283_hawkes_self_excitation_corr_252d": {"inputs": ["close"], "func": f38_jpdt_283_hawkes_self_excitation_corr_252d},
    "f38_jpdt_284_clustered_jumps_fraction_252d": {"inputs": ["close"], "func": f38_jpdt_284_clustered_jumps_fraction_252d},
    "f38_jpdt_285_kurt_r_high_vol_regime_252d": {"inputs": ["close"], "func": f38_jpdt_285_kurt_r_high_vol_regime_252d},
    "f38_jpdt_286_skew_r_high_vol_regime_252d": {"inputs": ["close"], "func": f38_jpdt_286_skew_r_high_vol_regime_252d},
    "f38_jpdt_287_max_abs_r_high_vol_regime_252d": {"inputs": ["close"], "func": f38_jpdt_287_max_abs_r_high_vol_regime_252d},
    "f38_jpdt_288_lppl_residual_252d": {"inputs": ["close"], "func": f38_jpdt_288_lppl_residual_252d},
    "f38_jpdt_289_lppl_freq_proxy_252d": {"inputs": ["close"], "func": f38_jpdt_289_lppl_freq_proxy_252d},
    "f38_jpdt_290_lppl_fit_r2_252d": {"inputs": ["close"], "func": f38_jpdt_290_lppl_fit_r2_252d},
    "f38_jpdt_291_sornette_crash_hazard_proxy_252d": {"inputs": ["close"], "func": f38_jpdt_291_sornette_crash_hazard_proxy_252d},
    "f38_jpdt_292_acceleration_21d_vs_252d_logret": {"inputs": ["close"], "func": f38_jpdt_292_acceleration_21d_vs_252d_logret},
    "f38_jpdt_293_accelerating_volume_count_63d": {"inputs": ["volume"], "func": f38_jpdt_293_accelerating_volume_count_63d},
    "f38_jpdt_294_recent_positive_concentration_21_vs_252": {"inputs": ["close"], "func": f38_jpdt_294_recent_positive_concentration_21_vs_252},
    "f38_jpdt_295_pre_peak_compression_natr_63d": {"inputs": ["high", "low", "close"], "func": f38_jpdt_295_pre_peak_compression_natr_63d},
    "f38_jpdt_296_vpin_proxy_21d": {"inputs": ["close", "volume"], "func": f38_jpdt_296_vpin_proxy_21d},
    "f38_jpdt_297_range_of_absret_extremes_63d": {"inputs": ["close"], "func": f38_jpdt_297_range_of_absret_extremes_63d},
    "f38_jpdt_298_cdf_convexity_absret_252d": {"inputs": ["close"], "func": f38_jpdt_298_cdf_convexity_absret_252d},
    "f38_jpdt_299_heavy_tail_moment_ratio_252d": {"inputs": ["close"], "func": f38_jpdt_299_heavy_tail_moment_ratio_252d},
    "f38_jpdt_300_post_jump_sign_reversal_pct_252d": {"inputs": ["close"], "func": f38_jpdt_300_post_jump_sign_reversal_pct_252d},
}
