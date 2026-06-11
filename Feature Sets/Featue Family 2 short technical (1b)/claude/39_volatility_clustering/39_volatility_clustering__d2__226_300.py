"""volatility_clustering d2 features 226-300 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the previous 225. Drawn from gap analysis:
GJR/TGARCH/PGARCH/STARCH variants, SWARCH high-state ratios, vol-spike
clustering, OHLC bar-anatomy persistence (body, shadows, CLV), multifractal /
DCCA / Higuchi complexity, wavelet & bandpower spectral, cross-horizon variance
ratios, conditional-on-regime moments, higher-order vol-process moments,
return-vs-vol coupling (risk-return, Sharpe/Sortino regimes), pre-crash
signatures, total-variation and clustering-aftermath descriptors.

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


def _rolling_sigma(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std()


def _longest_run_pos(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


def _gen_hurst(arr: np.ndarray, q: float, scales=(4, 8, 16, 32)) -> float:
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


# ============================================================
# Bucket Z19 — GARCH-family / regime extensions (226-240)
# ============================================================

def f39_vclu_226_gjr_full_signal_252d(close: pd.Series) -> pd.Series:
    """GJR signal = γ·|r_{t-1}| via rolling regression (γ coef × |r| on bar t)."""
    r = _log_ret(close)
    r2 = r ** 2
    y = r2
    x1 = r2.shift(1)
    x2 = r2.shift(1) * (r.shift(1) < 0).astype(float)
    combined = pd.concat([y, x1, x2], axis=1).values

    def _gam(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y_, x1_, x2_ = arr[:, 0], arr[:, 1], arr[:, 2]
        m = ~(np.isnan(y_) | np.isnan(x1_) | np.isnan(x2_))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x1_[m], x2_[m]])
        try:
            beta = np.linalg.lstsq(X, y_[m], rcond=None)[0]
            return float(beta[2])
        except Exception:
            return np.nan
    gam = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        gam.iloc[i] = _gam(combined[i - YDAYS + 1:i + 1])
    return gam * r.abs()


def f39_vclu_227_tgarch_absolute_persistence_252d(close: pd.Series) -> pd.Series:
    """Zakoian TGARCH proxy: AR(1) of σ_t fit on |r| absolute values over 252d."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(1))


def f39_vclu_228_pgarch_power_fit_252d(close: pd.Series) -> pd.Series:
    """PGARCH best-fit power: argmax_δ of σ-vs-σ_lag persistence over δ∈{0.5,1,1.5,2}."""
    r = _log_ret(close)

    def _best(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        best_d = np.nan; best_c = -1.0
        for d in (0.5, 1.0, 1.5, 2.0):
            x = np.abs(ww) ** d
            c = np.corrcoef(x[1:], x[:-1])[0, 1] if len(x) > 1 else np.nan
            if np.isfinite(c) and abs(c) > best_c:
                best_c = abs(c); best_d = d
        return float(best_d)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_best, raw=True)


def f39_vclu_229_starch_smooth_transition_proxy_252d(close: pd.Series) -> pd.Series:
    """STARCH smooth-transition proxy: corr(σ_21, tanh(r_{t-1}/σ_prior)) over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS)
    trans = np.tanh(_safe_div(r.shift(1), sig.shift(1)))
    return sig.rolling(YDAYS, min_periods=QDAYS).corr(trans)


def f39_vclu_230_swarch_high_low_ratio_504d(close: pd.Series) -> pd.Series:
    """SWARCH-style: σ_21 mean conditional on σ > median / mean conditional on σ ≤ median, over 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(DDAYS_2Y, min_periods=YDAYS).median()
    hi = s.where(s > med, np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    lo = s.where(s <= med, np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(hi, lo)


def f39_vclu_231_icss_variance_breaks_within_252d(close: pd.Series) -> pd.Series:
    """ICSS-style variance-break count on r² within 252d (CUSUM-Q exceedances > 1.358)."""
    r2 = _log_ret(close) ** 2

    def _icss(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        total = ww.sum()
        if total == 0:
            return np.nan
        cs = np.cumsum(ww) / total
        idx = np.arange(1, n + 1) / n
        dk = np.abs(cs - idx) * np.sqrt(n / 2.0)
        return float((dk > 1.358).sum())
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_icss, raw=True)


def f39_vclu_232_icss_time_since_last_break_252d(close: pd.Series) -> pd.Series:
    """Bars since the most recent ICSS-CUSUM-Q peak crossing within trailing 252d."""
    r2 = _log_ret(close) ** 2

    def _recency(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        total = ww.sum()
        if total == 0:
            return np.nan
        cs = np.cumsum(ww) / total
        idx = np.arange(1, n + 1) / n
        dk = np.abs(cs - idx) * np.sqrt(n / 2.0)
        crossings = np.where(dk > 1.358)[0]
        if len(crossings) == 0:
            return float(n)
        return float(n - crossings[-1] - 1)
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(_recency, raw=True)


def f39_vclu_233_varmax_cross_sigma_volume_coef_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VARMAX-style cross: rolling regression slope of σ_21 on volume z-score over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS)
    cov = s.rolling(YDAYS, min_periods=QDAYS).cov(vz)
    var = vz.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


def f39_vclu_234_cv_logsigma21_252d(close: pd.Series) -> pd.Series:
    """CV (std/mean) of log σ_21 over 252d."""
    ls = _safe_log(_rolling_sigma(_log_ret(close), MDAYS) + 1e-12)
    return _safe_div(ls.rolling(YDAYS, min_periods=QDAYS).std(),
                     ls.rolling(YDAYS, min_periods=QDAYS).mean().abs())


def f39_vclu_235_halflife_sigma21_vs_sigma252_252d(close: pd.Series) -> pd.Series:
    """Cross-half-life: −log(2) / log(|corr(σ_21, σ_252)|) over 252d."""
    r = _log_ret(close)
    rho = _rolling_sigma(r, MDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_rolling_sigma(r, YDAYS))
    ar = rho.abs().clip(upper=0.99, lower=1e-3)
    return (-np.log(2.0) / np.log(ar)).clip(upper=200.0)


def f39_vclu_236_spike_followed_by_spike_count_63d(close: pd.Series) -> pd.Series:
    """Spike-followed-by-spike: σ_21>p95 events followed within 5d by another σ_21>p95, over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    spike = (s > p95).astype(float)
    follow = (spike.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5).astype(float)
    pair = ((spike > 0.5) & (follow > 0.5)).astype(float)
    return pair.rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_237_spike_followed_by_quiet_count_63d(close: pd.Series) -> pd.Series:
    """Spike-followed-by-quiet (causal): bar t-(1..5) had σ>p95 AND bar t has σ<p25, summed 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    spike = (s > p95).astype(float)
    spike_lag = (spike.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5)
    quiet_now = (s < p25)
    pair = (spike_lag & quiet_now).astype(float)
    return pair.rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_238_spike_aftermath_kurt_252d(close: pd.Series) -> pd.Series:
    """Mean kurt of r within 5d after a σ_21>p95 spike, over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    spike_lag = (s.shift(WDAYS) > p95.shift(WDAYS))
    sel = r.where(spike_lag, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).kurt()


def f39_vclu_239_spike_recovery_bars_252d(close: pd.Series) -> pd.Series:
    """Mean bars to σ_21 < median after a σ_21>p95 spike, over 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    arr_s = s.values; arr_p = p95.values; arr_m = med.values
    out = np.full(len(arr_s), np.nan)
    for i in range(YDAYS, len(arr_s)):
        recovery_times = []
        for j in range(i - YDAYS + 1, i + 1):
            if np.isnan(arr_s[j]) or np.isnan(arr_p[j]) or arr_s[j] <= arr_p[j]:
                continue
            for k in range(j + 1, min(j + MDAYS, len(arr_s))):
                if not np.isnan(arr_s[k]) and not np.isnan(arr_m[k]) and arr_s[k] < arr_m[k]:
                    recovery_times.append(k - j); break
        if recovery_times:
            out[i] = float(np.mean(recovery_times))
    return pd.Series(out, index=close.index)


def f39_vclu_240_var_sigma21_minus_lag63_252d(close: pd.Series) -> pd.Series:
    """Variance of (σ_21 − σ_21.shift(63)) over 252d — vol-momentum dispersion."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s - s.shift(QDAYS)).rolling(YDAYS, min_periods=QDAYS).var()


# ============================================================
# Bucket Z20 — OHLC / range descriptors (241-250)
# ============================================================

def f39_vclu_241_overnight_only_persistence_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of |overnight log-ret| (close-to-open gap magnitude) over 252d."""
    g = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    return g.rolling(YDAYS, min_periods=QDAYS).corr(g.shift(1))


def f39_vclu_242_persistence_hl_over_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of (high-low)/close intraday range fraction over 252d."""
    rng = _safe_div(high - low, close)
    return rng.rolling(YDAYS, min_periods=QDAYS).corr(rng.shift(1))


def f39_vclu_243_skew_hl_over_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of (high-low)/close over 252d."""
    return _safe_div(high - low, close).rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_244_bimodality_coef_hl_over_close_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bimodality coefficient (skew²+1)/(kurt+3·(n-1)²/((n-2)(n-3))) of (H-L)/C over 252d."""
    rng = _safe_div(high - low, close)
    sk = rng.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = rng.rolling(YDAYS, min_periods=QDAYS).kurt()
    n = YDAYS
    corr = 3.0 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return (sk ** 2 + 1.0) / (kt + corr)


def f39_vclu_245_persistence_upper_shadow_ratio_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of (high - max(open,close))/(high-low) — upper-shadow share persistence over 252d."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    rng = (high - low).replace(0, np.nan)
    us = _safe_div(high - body_hi, rng)
    return us.rolling(YDAYS, min_periods=QDAYS).corr(us.shift(1))


def f39_vclu_246_persistence_lower_shadow_ratio_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of (min(open,close) - low)/(high-low) — lower-shadow share persistence over 252d."""
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    rng = (high - low).replace(0, np.nan)
    ls = _safe_div(body_lo - low, rng)
    return ls.rolling(YDAYS, min_periods=QDAYS).corr(ls.shift(1))


def f39_vclu_247_body_share_asymmetry_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |C-O|/range on up-bars (C>O) minus mean on down-bars (C<O), over 252d."""
    rng = (high - low).replace(0, np.nan)
    body = _safe_div((close - open).abs(), rng)
    up = body.where(close > open, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = body.where(close < open, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up - dn


def f39_vclu_248_mean_body_share_top_decile_range_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (|C-O|/range) restricted to top-decile-range bars over 252d."""
    rng = (high - low)
    body = _safe_div((close - open).abs(), rng.replace(0, np.nan))
    p90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return body.where(rng > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_249_mean_body_share_bottom_decile_range_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (|C-O|/range) restricted to bottom-decile-range bars over 252d."""
    rng = (high - low)
    body = _safe_div((close - open).abs(), rng.replace(0, np.nan))
    p10 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return body.where(rng < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_250_persistence_clv_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of close-location-value (2C-H-L)/(H-L) over 252d."""
    rng = (high - low).replace(0, np.nan)
    clv = (2 * close - high - low) / rng
    return clv.rolling(YDAYS, min_periods=QDAYS).corr(clv.shift(1))


# ============================================================
# Bucket Z21 — Multifractal & complexity (251-258)
# ============================================================

def f39_vclu_251_spectrum_width_q_neg2_q2_252d(close: pd.Series) -> pd.Series:
    """Singularity-spectrum width H(-2) - H(2) on r over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _gen_hurst(w, -2.0) - _gen_hurst(w, 2.0), raw=True)


def f39_vclu_252_gen_hurst_q3_r_252d(close: pd.Series) -> pd.Series:
    """Generalized Hurst exponent H(q=3) on r over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gen_hurst(w, 3.0), raw=True)


def f39_vclu_253_mfdfa_q2_minus_qneg2_diff_252d(close: pd.Series) -> pd.Series:
    """MF-DFA H(q=2) − H(q=-2) over 252d (non-linearity marker)."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _gen_hurst(w, 2.0) - _gen_hurst(w, -2.0), raw=True)


def f39_vclu_254_dcca_sigma5_sigma21_252d(close: pd.Series) -> pd.Series:
    """DCCA cross-correlation of σ_5 and σ_21 over 252d via rolling-window fluctuation cross-product."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)

    def _dcca(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        a, b = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        ya = (a[m] - a[m].mean()).cumsum()
        yb = (b[m] - b[m].mean()).cumsum()
        n = len(ya); s = 16
        if n < s * 3:
            return np.nan
        Fxy = 0.0; Fxx = 0.0; Fyy = 0.0; cnt = 0
        for i in range(0, n - s, s):
            xs = np.arange(s, dtype=float)
            ax = np.polyfit(xs, ya[i:i + s], 1); ay = np.polyfit(xs, yb[i:i + s], 1)
            rxa = ya[i:i + s] - np.polyval(ax, xs)
            ryb = yb[i:i + s] - np.polyval(ay, xs)
            Fxy += (rxa * ryb).sum(); Fxx += (rxa ** 2).sum(); Fyy += (ryb ** 2).sum(); cnt += 1
        if cnt == 0 or Fxx <= 0 or Fyy <= 0:
            return np.nan
        return float(Fxy / np.sqrt(Fxx * Fyy))
    combined = pd.concat([s5, s21], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _dcca(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_255_mf_dcca_q2_252d(close: pd.Series) -> pd.Series:
    """MF-DCCA H(q=2) of σ_21 vs r over 252d (multifractal cross-correlation)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close).abs()

    def _mfdcca(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        a, b = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < 60:
            return np.nan
        ya = (a[m] - a[m].mean()).cumsum()
        yb = (b[m] - b[m].mean()).cumsum()
        n = len(ya)
        Fq_list = []
        for s_ in (4, 8, 16, 32):
            if n < s_ * 3:
                continue
            seg_fxy = []
            for i in range(0, n - s_, s_):
                xs = np.arange(s_, dtype=float)
                rxa = ya[i:i + s_] - np.polyval(np.polyfit(xs, ya[i:i + s_], 1), xs)
                ryb = yb[i:i + s_] - np.polyval(np.polyfit(xs, yb[i:i + s_], 1), xs)
                seg_fxy.append(np.abs((rxa * ryb).mean()))
            if seg_fxy:
                Fq_list.append((s_, np.sqrt(np.mean(seg_fxy))))
        if len(Fq_list) < 2:
            return np.nan
        xs = np.log([x[0] for x in Fq_list]); ys = np.log([x[1] + 1e-12 for x in Fq_list])
        xm = xs.mean(); ym = ys.mean()
        d = ((xs - xm) ** 2).sum()
        return float(((xs - xm) * (ys - ym)).sum() / d) if d > 0 else np.nan
    combined = pd.concat([s, r], axis=1).values
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _mfdcca(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_256_coarse_grained_entropy_sigma_scale5_252d(close: pd.Series) -> pd.Series:
    """Coarse-grained Shannon entropy of σ_21 at scale-5 averaging over 252d (multi-scale entropy)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _cge(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        cs = ww[: (n // WDAYS) * WDAYS].reshape(-1, WDAYS).mean(axis=1)
        if len(cs) < 10:
            return np.nan
        h, _ = np.histogram(cs, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_cge, raw=True)


def f39_vclu_257_multiscale_entropy_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of sample entropy at scale 1 vs scale 5 of |r| over 252d."""
    a = _log_ret(close).abs()

    def _mse(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan

        def _samp(x, m=2):
            n_ = len(x)
            if n_ < 30:
                return np.nan
            tol = 0.2 * x.std()
            if tol == 0:
                return np.nan
            # Subsample for speed
            if n_ > 100:
                x = x[::2]; n_ = len(x)
            xs2 = np.array([x[i:i + m] for i in range(n_ - m)])
            xs3 = np.array([x[i:i + m + 1] for i in range(n_ - m - 1)])
            cnt_b = 0; cnt_a = 0
            for i in range(len(xs2)):
                cnt_b += (np.max(np.abs(xs2 - xs2[i]), axis=1) <= tol).sum() - 1
            for i in range(len(xs3)):
                cnt_a += (np.max(np.abs(xs3 - xs3[i]), axis=1) <= tol).sum() - 1
            if cnt_b == 0 or cnt_a == 0:
                return np.nan
            return float(-np.log(cnt_a / cnt_b))
        s1 = _samp(ww)
        cs5 = ww[: (n // WDAYS) * WDAYS].reshape(-1, WDAYS).mean(axis=1)
        s5 = _samp(cs5) if len(cs5) > 30 else np.nan
        if not np.isfinite(s1) or not np.isfinite(s5) or s5 == 0:
            return np.nan
        return float(s1 / s5)
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_mse, raw=True)


def f39_vclu_258_higuchi_fractal_dim_sigma_252d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of σ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _higuchi(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < 60:
            return np.nan
        k_max = 8
        Lk = []
        for k in range(1, k_max + 1):
            Lmk = []
            for m_ in range(k):
                length = 0.0; cnt = 0
                for i in range(1, (n - m_) // k):
                    length += abs(ww[m_ + i * k] - ww[m_ + (i - 1) * k])
                    cnt += 1
                if cnt > 0:
                    norm = (n - 1.0) / (cnt * k)
                    Lmk.append(length * norm / k)
            if Lmk:
                Lk.append(np.mean(Lmk))
        if len(Lk) < 3:
            return np.nan
        xs = np.log(1.0 / np.arange(1, len(Lk) + 1)); ys = np.log(np.array(Lk) + 1e-12)
        xm = xs.mean(); ym = ys.mean()
        d = ((xs - xm) ** 2).sum()
        return float(((xs - xm) * (ys - ym)).sum() / d) if d > 0 else np.nan
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_higuchi, raw=True)


# ============================================================
# Bucket Z22 — Cycle / spectral / time-frequency (259-266)
# ============================================================

def _bandpower(series_window: np.ndarray, lo_freq: float, hi_freq: float) -> float:
    ww = series_window[~np.isnan(series_window)]
    n = len(ww)
    if n < 20:
        return np.nan
    f = np.fft.rfft(ww - ww.mean())
    psd = (np.abs(f) ** 2) / n
    psd[0] = 0
    freqs = np.arange(len(psd)) / n
    mask = (freqs >= lo_freq) & (freqs < hi_freq)
    return float(psd[mask].sum() / (psd.sum() + 1e-12))


def f39_vclu_259_bandpower_low_freq_absret_252d(close: pd.Series) -> pd.Series:
    """Bandpower fraction in [0, 1/63 cyc/bar] of |r| over 252d (low-freq share)."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _bandpower(w, 0.0, 1.0 / QDAYS), raw=True)


def f39_vclu_260_bandpower_mid_freq_absret_252d(close: pd.Series) -> pd.Series:
    """Bandpower fraction in [1/63, 1/21 cyc/bar] of |r| over 252d (mid-freq share)."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _bandpower(w, 1.0 / QDAYS, 1.0 / MDAYS), raw=True)


def f39_vclu_261_spectral_peak_freq_sigma5_252d(close: pd.Series) -> pd.Series:
    """Peak FFT frequency of σ_5d over 252d (cycles/bar)."""
    s = _rolling_sigma(_log_ret(close), WDAYS)

    def _peak(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = np.abs(f) ** 2
        psd[0] = 0
        return float(int(np.argmax(psd)) / n)
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_peak, raw=True)


def f39_vclu_262_phase_shift_sig5_sig21_252d(close: pd.Series) -> pd.Series:
    """Phase shift between σ_5 and σ_21 via cross-spectrum at peak coherent frequency, over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    combined = pd.concat([s5, s21], axis=1).values

    def _phase(arr):
        a, b = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = a[m], b[m]
        n = len(a)
        fa = np.fft.rfft(a - a.mean()); fb = np.fft.rfft(b - b.mean())
        Cxy = fa * np.conjugate(fb)
        idx = int(np.argmax(np.abs(Cxy[1:])) + 1)
        return float(np.angle(Cxy[idx]))
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _phase(combined[i - YDAYS + 1:i + 1])
    return out


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


def f39_vclu_263_wavelet_energy_ratio_2_8_r_252d(close: pd.Series) -> pd.Series:
    """Wavelet-detail energy ratio scale-2 / scale-8 of r over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _haar_variance(w, 2) / (_haar_variance(w, 8) + 1e-12), raw=True)


def f39_vclu_264_wavelet_energy_ratio_4_16_r_252d(close: pd.Series) -> pd.Series:
    """Wavelet-detail energy ratio scale-4 / scale-16 of r over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: _haar_variance(w, 4) / (_haar_variance(w, 16) + 1e-12), raw=True)


def f39_vclu_265_wavelet_variance_scale4_r_252d(close: pd.Series) -> pd.Series:
    """Wavelet variance of r at dyadic scale-4 over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _haar_variance(w, 4), raw=True)


def f39_vclu_266_wavelet_variance_scale8_r_252d(close: pd.Series) -> pd.Series:
    """Wavelet variance of r at dyadic scale-8 over 252d."""
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _haar_variance(w, 8), raw=True)


# ============================================================
# Bucket Z23 — Persistence / memory variants (267-273)
# ============================================================

def f39_vclu_267_ar2_phi2_sigma21_252d(close: pd.Series) -> pd.Series:
    """AR(2) coefficient φ_2 of σ_21 over 252d (rolling regression)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    combined = pd.concat([s, s.shift(1), s.shift(2)], axis=1).values

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


def f39_vclu_268_halflife_sigma5_252d(close: pd.Series) -> pd.Series:
    """Half-life of σ_5 shocks implied by AR(1) over 252d (shorter horizon)."""
    s = _rolling_sigma(_log_ret(close), WDAYS)
    rho = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    ar = rho.abs().clip(upper=0.99, lower=1e-3)
    return (-np.log(2.0) / np.log(ar)).clip(upper=200.0)


def f39_vclu_269_ar1_of_sigma_diff_horizon_252d(close: pd.Series) -> pd.Series:
    """AR(1) of (σ_21 − σ_63) cross-horizon spread over 252d."""
    r = _log_ret(close)
    spread = _rolling_sigma(r, MDAYS) - _rolling_sigma(r, QDAYS)
    return spread.rolling(YDAYS, min_periods=QDAYS).corr(spread.shift(1))


def f39_vclu_270_var_ratio_r_q5_252d(close: pd.Series) -> pd.Series:
    """Variance-ratio of log-returns at lag q=5 over 252d."""
    r = _log_ret(close)
    v1 = r.rolling(YDAYS, min_periods=QDAYS).var()
    rk = _safe_log(close).diff(WDAYS)
    vk = rk.rolling(YDAYS, min_periods=QDAYS).var() / WDAYS
    return _safe_div(vk, v1)


def f39_vclu_271_var_ratio_r_q21_252d(close: pd.Series) -> pd.Series:
    """Variance-ratio of log-returns at lag q=21 over 252d."""
    r = _log_ret(close)
    v1 = r.rolling(YDAYS, min_periods=QDAYS).var()
    rk = _safe_log(close).diff(MDAYS)
    vk = rk.rolling(YDAYS, min_periods=QDAYS).var() / MDAYS
    return _safe_div(vk, v1)


def f39_vclu_272_persistence_vol_zscore_252d(close: pd.Series) -> pd.Series:
    """AR(1) of σ_21 z-score (within own past 252d) — persistence of the vol-anomaly."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    z = _rolling_zscore(s, YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).corr(z.shift(1))


def f39_vclu_273_var_ratio_rsq_q21_504d(close: pd.Series) -> pd.Series:
    """Variance ratio of r² at lag q=21 over 504d."""
    r2 = _log_ret(close) ** 2
    v1 = r2.rolling(DDAYS_2Y, min_periods=YDAYS).var()
    rk = r2.rolling(MDAYS, min_periods=WDAYS).sum()
    vk = rk.rolling(DDAYS_2Y, min_periods=YDAYS).var() / MDAYS
    return _safe_div(vk, v1)


# ============================================================
# Bucket Z24 — Conditional / pre-crash signatures (274-280)
# ============================================================

def f39_vclu_274_sigma_low_at_252d_high_proxy_63d(close: pd.Series) -> pd.Series:
    """Pre-peak compression: σ_21 at multi-year low (1260d) while close near 252d-high (within 1%), in last 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sig_low = (s <= s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).quantile(0.10))
    near_peak = close >= 0.99 * close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (sig_low & near_peak).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_275_garch_next_day_var_forecast_proxy(close: pd.Series) -> pd.Series:
    """GARCH-style next-day var forecast proxy: σ²_t·EWMA(r², λ=0.94)."""
    r = _log_ret(close)
    s2 = _rolling_sigma(r, MDAYS) ** 2
    ewma_r2 = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean()
    return s2 * ewma_r2


def f39_vclu_276_forecast_vs_realized_correlation_21d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(EWMA(r², 21d) forecast, realized r²_{t+1}-style proxy via lag)."""
    r = _log_ret(close)
    forecast = (r ** 2).ewm(alpha=0.06, min_periods=MDAYS).mean().shift(1)
    realized = r ** 2
    return forecast.rolling(YDAYS, min_periods=QDAYS).corr(realized)


def f39_vclu_277_current_vol_cluster_magnitude_252d(close: pd.Series) -> pd.Series:
    """Max σ_21 within current consecutive above-median run (vol cluster), reset on regime change."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int).fillna(0).values
    s_arr = s.values
    out = np.full(len(s_arr), np.nan)
    cur_max = np.nan; in_cluster = False
    for i, v in enumerate(above):
        if v == 1:
            if not in_cluster:
                cur_max = s_arr[i]
            else:
                cur_max = max(cur_max, s_arr[i]) if not np.isnan(cur_max) else s_arr[i]
            in_cluster = True
        else:
            in_cluster = False
            cur_max = np.nan
        out[i] = cur_max
    return pd.Series(out, index=close.index)


def f39_vclu_278_time_since_last_vol_cluster_end_252d(close: pd.Series) -> pd.Series:
    """Bars since last σ_21 dropped below median after being above (end of vol cluster)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(int).fillna(0).values
    end_events = ((above[:-1] == 1) & (above[1:] == 0)).astype(int)
    end_events = np.concatenate([[0], end_events])
    out = np.full(len(end_events), np.nan)
    bars = np.nan
    for i, v in enumerate(end_events):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


def f39_vclu_279_num_vol_clusters_252d(close: pd.Series) -> pd.Series:
    """Count of σ_21-above-median runs of length ≥ 5 within 252d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(float).fillna(0.0)

    def _count(w):
        cnt = 0; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
            else:
                if cur >= WDAYS:
                    cnt += 1
                cur = 0
        if cur >= WDAYS:
            cnt += 1
        return float(cnt)
    return above.rolling(YDAYS, min_periods=QDAYS).apply(_count, raw=True)


def f39_vclu_280_mean_vol_cluster_duration_252d(close: pd.Series) -> pd.Series:
    """Mean duration of σ_21-above-median runs (≥ 1 bar) within 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    above = (s > med).astype(float).fillna(0.0)

    def _mean_dur(w):
        runs = []; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
            elif cur > 0:
                runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        return float(np.mean(runs)) if runs else np.nan
    return above.rolling(YDAYS, min_periods=QDAYS).apply(_mean_dur, raw=True)


# ============================================================
# Bucket Z25 — Higher-order moments of vol process (281-288)
# ============================================================

def f39_vclu_281_coskewness_sigma_r_252d(close: pd.Series) -> pd.Series:
    """Co-skewness E[σ_t · r_t · r_{t-1}] over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    prod = s * r * r.shift(1)
    return prod.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_282_cokurtosis_sigma_rsq_252d(close: pd.Series) -> pd.Series:
    """Co-kurtosis E[σ_t² · r_t² · r_{t-1}²] over 252d."""
    r = _log_ret(close)
    s2 = _rolling_sigma(r, MDAYS) ** 2
    prod = s2 * (r ** 2) * ((r.shift(1)) ** 2)
    return prod.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_283_corr_sigma_r_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Corr(σ_21, r) restricted to high-vol regime (σ_21 > own 252d p75)."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    s_sel = s.where(s > p75, np.nan)
    r_sel = r.where(s > p75, np.nan)
    return s_sel.rolling(YDAYS, min_periods=QDAYS).corr(r_sel)


def f39_vclu_284_skew_logsigma21_252d(close: pd.Series) -> pd.Series:
    """Skewness of log σ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s + 1e-12).rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_285_kurt_logsigma21_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of log σ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s + 1e-12).rolling(YDAYS, min_periods=QDAYS).kurt()


def f39_vclu_286_var_logsigma21_252d(close: pd.Series) -> pd.Series:
    """Variance of log σ_21 over 252d (log-vol-of-log-vol level)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s + 1e-12).rolling(YDAYS, min_periods=QDAYS).var()


def f39_vclu_287_skew_delta_sigma21_252d(close: pd.Series) -> pd.Series:
    """Skew of Δσ_21 over 252d — asymmetry of vol increments (different from existing skew of σ)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_288_kurt_delta_sigma21_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of Δσ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket Z26 — Drift / mean-vs-vol coupling (289-294)
# ============================================================

def f39_vclu_289_risk_return_corr_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(σ_21, 21d-trailing log-ret) — risk-return coupling."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return s.rolling(YDAYS, min_periods=QDAYS).corr(trail)


def f39_vclu_290_sharpe_proxy_21d_mean_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d mean of (21d trailing log-ret / σ_21) annualized — Sharpe proxy."""
    r = _log_ret(close)
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    sharpe = _safe_div(trail / np.sqrt(MDAYS), _rolling_sigma(r, MDAYS)) * np.sqrt(YDAYS)
    return sharpe.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_291_sortino_proxy_252d(close: pd.Series) -> pd.Series:
    """Sortino: rolling 252d (21d-trailing log-ret) / σ-of-negative-r-only-21d annualized."""
    r = _log_ret(close)
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    neg_r = r.where(r < 0, np.nan)
    neg_sig = neg_r.rolling(MDAYS, min_periods=WDAYS).std()
    sortino = _safe_div(trail / np.sqrt(MDAYS), neg_sig) * np.sqrt(YDAYS)
    return sortino.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_292_sharpe_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Sharpe-proxy restricted to high-vol regime (σ_21 > 252d p75) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    sharpe = _safe_div(trail / np.sqrt(MDAYS), s) * np.sqrt(YDAYS)
    sel = sharpe.where(s > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_293_sharpe_low_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Sharpe-proxy restricted to low-vol regime (σ_21 < 252d p25) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    trail = _safe_log(close) - _safe_log(close.shift(MDAYS))
    sharpe = _safe_div(trail / np.sqrt(MDAYS), s) * np.sqrt(YDAYS)
    sel = sharpe.where(s < p25, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_294_vol_targeted_excess_return_252d(close: pd.Series) -> pd.Series:
    """Mean (r/σ_21-prior) over 252d — vol-targeted excess return proxy."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    return _safe_div(r, sig).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket Z27 — Final misc (295-300)
# ============================================================

def f39_vclu_295_slope_sigma252_21d(close: pd.Series) -> pd.Series:
    """Rolling 21d slope of σ_252 — local trend of long-horizon vol."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return _rolling_slope(s, MDAYS)


def f39_vclu_296_num_sigma_trend_reversals_504d(close: pd.Series) -> pd.Series:
    """Count of sign-changes in 63d slope of σ_21 over rolling 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sl = _rolling_slope(s, QDAYS)
    return np.sign(sl).diff().abs().rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f39_vclu_297_sigma_trend_velocity_zscore_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d z-score of 63d-σ_21-slope (velocity of vol-trend)."""
    sl = _rolling_slope(_rolling_sigma(_log_ret(close), MDAYS), QDAYS)
    return _rolling_zscore(sl, YDAYS)


def f39_vclu_298_newey_west_sigma_persistence_252d(close: pd.Series) -> pd.Series:
    """Newey-West HAC-style σ-clustering variance: var(σ_21) + 2·cov(σ_21, σ_21.shift(1)) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    v0 = s.rolling(YDAYS, min_periods=QDAYS).var()
    c1 = s.rolling(YDAYS, min_periods=QDAYS).cov(s.shift(1))
    return v0 + 2.0 * c1


def f39_vclu_299_mean_abs_sigma_shock_multi_horizon(close: pd.Series) -> pd.Series:
    """Mean |Δσ| averaged across horizons {5,21,63} over 252d — multi-horizon shock-mean."""
    r = _log_ret(close)
    shocks = []
    for n in (WDAYS, MDAYS, QDAYS):
        s = _rolling_sigma(r, n)
        shocks.append(s.diff().abs().rolling(YDAYS, min_periods=QDAYS).mean())
    return pd.concat(shocks, axis=1).mean(axis=1)


def f39_vclu_300_total_variation_sigma21_normalized_252d(close: pd.Series) -> pd.Series:
    """Σ |Δσ_21| / Σ σ_21 over 252d — normalized total variation of σ-process."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum(),
                     s.rolling(YDAYS, min_periods=QDAYS).sum())


# ============================================================
#                         REGISTRY 226-300
# ============================================================



def f39_vclu_226_gjr_full_signal_252d_d2(close):
    return f39_vclu_226_gjr_full_signal_252d(close).diff().diff()


def f39_vclu_227_tgarch_absolute_persistence_252d_d2(close):
    return f39_vclu_227_tgarch_absolute_persistence_252d(close).diff().diff()


def f39_vclu_228_pgarch_power_fit_252d_d2(close):
    return f39_vclu_228_pgarch_power_fit_252d(close).diff().diff()


def f39_vclu_229_starch_smooth_transition_proxy_252d_d2(close):
    return f39_vclu_229_starch_smooth_transition_proxy_252d(close).diff().diff()


def f39_vclu_230_swarch_high_low_ratio_504d_d2(close):
    return f39_vclu_230_swarch_high_low_ratio_504d(close).diff().diff()


def f39_vclu_231_icss_variance_breaks_within_252d_d2(close):
    return f39_vclu_231_icss_variance_breaks_within_252d(close).diff().diff()


def f39_vclu_232_icss_time_since_last_break_252d_d2(close):
    return f39_vclu_232_icss_time_since_last_break_252d(close).diff().diff()


def f39_vclu_233_varmax_cross_sigma_volume_coef_252d_d2(close, volume):
    return f39_vclu_233_varmax_cross_sigma_volume_coef_252d(close, volume).diff().diff()


def f39_vclu_234_cv_logsigma21_252d_d2(close):
    return f39_vclu_234_cv_logsigma21_252d(close).diff().diff()


def f39_vclu_235_halflife_sigma21_vs_sigma252_252d_d2(close):
    return f39_vclu_235_halflife_sigma21_vs_sigma252_252d(close).diff().diff()


def f39_vclu_236_spike_followed_by_spike_count_63d_d2(close):
    return f39_vclu_236_spike_followed_by_spike_count_63d(close).diff().diff()


def f39_vclu_237_spike_followed_by_quiet_count_63d_d2(close):
    return f39_vclu_237_spike_followed_by_quiet_count_63d(close).diff().diff()


def f39_vclu_238_spike_aftermath_kurt_252d_d2(close):
    return f39_vclu_238_spike_aftermath_kurt_252d(close).diff().diff()


def f39_vclu_239_spike_recovery_bars_252d_d2(close):
    return f39_vclu_239_spike_recovery_bars_252d(close).diff().diff()


def f39_vclu_240_var_sigma21_minus_lag63_252d_d2(close):
    return f39_vclu_240_var_sigma21_minus_lag63_252d(close).diff().diff()


def f39_vclu_241_overnight_only_persistence_252d_d2(open, close):
    return f39_vclu_241_overnight_only_persistence_252d(open, close).diff().diff()


def f39_vclu_242_persistence_hl_over_close_252d_d2(high, low, close):
    return f39_vclu_242_persistence_hl_over_close_252d(high, low, close).diff().diff()


def f39_vclu_243_skew_hl_over_close_252d_d2(high, low, close):
    return f39_vclu_243_skew_hl_over_close_252d(high, low, close).diff().diff()


def f39_vclu_244_bimodality_coef_hl_over_close_252d_d2(high, low, close):
    return f39_vclu_244_bimodality_coef_hl_over_close_252d(high, low, close).diff().diff()


def f39_vclu_245_persistence_upper_shadow_ratio_252d_d2(open, high, low, close):
    return f39_vclu_245_persistence_upper_shadow_ratio_252d(open, high, low, close).diff().diff()


def f39_vclu_246_persistence_lower_shadow_ratio_252d_d2(open, high, low, close):
    return f39_vclu_246_persistence_lower_shadow_ratio_252d(open, high, low, close).diff().diff()


def f39_vclu_247_body_share_asymmetry_252d_d2(open, high, low, close):
    return f39_vclu_247_body_share_asymmetry_252d(open, high, low, close).diff().diff()


def f39_vclu_248_mean_body_share_top_decile_range_252d_d2(open, high, low, close):
    return f39_vclu_248_mean_body_share_top_decile_range_252d(open, high, low, close).diff().diff()


def f39_vclu_249_mean_body_share_bottom_decile_range_252d_d2(open, high, low, close):
    return f39_vclu_249_mean_body_share_bottom_decile_range_252d(open, high, low, close).diff().diff()


def f39_vclu_250_persistence_clv_252d_d2(high, low, close):
    return f39_vclu_250_persistence_clv_252d(high, low, close).diff().diff()


def f39_vclu_251_spectrum_width_q_neg2_q2_252d_d2(close):
    return f39_vclu_251_spectrum_width_q_neg2_q2_252d(close).diff().diff()


def f39_vclu_252_gen_hurst_q3_r_252d_d2(close):
    return f39_vclu_252_gen_hurst_q3_r_252d(close).diff().diff()


def f39_vclu_253_mfdfa_q2_minus_qneg2_diff_252d_d2(close):
    return f39_vclu_253_mfdfa_q2_minus_qneg2_diff_252d(close).diff().diff()


def f39_vclu_254_dcca_sigma5_sigma21_252d_d2(close):
    return f39_vclu_254_dcca_sigma5_sigma21_252d(close).diff().diff()


def f39_vclu_255_mf_dcca_q2_252d_d2(close):
    return f39_vclu_255_mf_dcca_q2_252d(close).diff().diff()


def f39_vclu_256_coarse_grained_entropy_sigma_scale5_252d_d2(close):
    return f39_vclu_256_coarse_grained_entropy_sigma_scale5_252d(close).diff().diff()


def f39_vclu_257_multiscale_entropy_ratio_252d_d2(close):
    return f39_vclu_257_multiscale_entropy_ratio_252d(close).diff().diff()


def f39_vclu_258_higuchi_fractal_dim_sigma_252d_d2(close):
    return f39_vclu_258_higuchi_fractal_dim_sigma_252d(close).diff().diff()


def f39_vclu_259_bandpower_low_freq_absret_252d_d2(close):
    return f39_vclu_259_bandpower_low_freq_absret_252d(close).diff().diff()


def f39_vclu_260_bandpower_mid_freq_absret_252d_d2(close):
    return f39_vclu_260_bandpower_mid_freq_absret_252d(close).diff().diff()


def f39_vclu_261_spectral_peak_freq_sigma5_252d_d2(close):
    return f39_vclu_261_spectral_peak_freq_sigma5_252d(close).diff().diff()


def f39_vclu_262_phase_shift_sig5_sig21_252d_d2(close):
    return f39_vclu_262_phase_shift_sig5_sig21_252d(close).diff().diff()


def f39_vclu_263_wavelet_energy_ratio_2_8_r_252d_d2(close):
    return f39_vclu_263_wavelet_energy_ratio_2_8_r_252d(close).diff().diff()


def f39_vclu_264_wavelet_energy_ratio_4_16_r_252d_d2(close):
    return f39_vclu_264_wavelet_energy_ratio_4_16_r_252d(close).diff().diff()


def f39_vclu_265_wavelet_variance_scale4_r_252d_d2(close):
    return f39_vclu_265_wavelet_variance_scale4_r_252d(close).diff().diff()


def f39_vclu_266_wavelet_variance_scale8_r_252d_d2(close):
    return f39_vclu_266_wavelet_variance_scale8_r_252d(close).diff().diff()


def f39_vclu_267_ar2_phi2_sigma21_252d_d2(close):
    return f39_vclu_267_ar2_phi2_sigma21_252d(close).diff().diff()


def f39_vclu_268_halflife_sigma5_252d_d2(close):
    return f39_vclu_268_halflife_sigma5_252d(close).diff().diff()


def f39_vclu_269_ar1_of_sigma_diff_horizon_252d_d2(close):
    return f39_vclu_269_ar1_of_sigma_diff_horizon_252d(close).diff().diff()


def f39_vclu_270_var_ratio_r_q5_252d_d2(close):
    return f39_vclu_270_var_ratio_r_q5_252d(close).diff().diff()


def f39_vclu_271_var_ratio_r_q21_252d_d2(close):
    return f39_vclu_271_var_ratio_r_q21_252d(close).diff().diff()


def f39_vclu_272_persistence_vol_zscore_252d_d2(close):
    return f39_vclu_272_persistence_vol_zscore_252d(close).diff().diff()


def f39_vclu_273_var_ratio_rsq_q21_504d_d2(close):
    return f39_vclu_273_var_ratio_rsq_q21_504d(close).diff().diff()


def f39_vclu_274_sigma_low_at_252d_high_proxy_63d_d2(close):
    return f39_vclu_274_sigma_low_at_252d_high_proxy_63d(close).diff().diff()


def f39_vclu_275_garch_next_day_var_forecast_proxy_d2(close):
    return f39_vclu_275_garch_next_day_var_forecast_proxy(close).diff().diff()


def f39_vclu_276_forecast_vs_realized_correlation_21d_d2(close):
    return f39_vclu_276_forecast_vs_realized_correlation_21d(close).diff().diff()


def f39_vclu_277_current_vol_cluster_magnitude_252d_d2(close):
    return f39_vclu_277_current_vol_cluster_magnitude_252d(close).diff().diff()


def f39_vclu_278_time_since_last_vol_cluster_end_252d_d2(close):
    return f39_vclu_278_time_since_last_vol_cluster_end_252d(close).diff().diff()


def f39_vclu_279_num_vol_clusters_252d_d2(close):
    return f39_vclu_279_num_vol_clusters_252d(close).diff().diff()


def f39_vclu_280_mean_vol_cluster_duration_252d_d2(close):
    return f39_vclu_280_mean_vol_cluster_duration_252d(close).diff().diff()


def f39_vclu_281_coskewness_sigma_r_252d_d2(close):
    return f39_vclu_281_coskewness_sigma_r_252d(close).diff().diff()


def f39_vclu_282_cokurtosis_sigma_rsq_252d_d2(close):
    return f39_vclu_282_cokurtosis_sigma_rsq_252d(close).diff().diff()


def f39_vclu_283_corr_sigma_r_high_vol_regime_252d_d2(close):
    return f39_vclu_283_corr_sigma_r_high_vol_regime_252d(close).diff().diff()


def f39_vclu_284_skew_logsigma21_252d_d2(close):
    return f39_vclu_284_skew_logsigma21_252d(close).diff().diff()


def f39_vclu_285_kurt_logsigma21_252d_d2(close):
    return f39_vclu_285_kurt_logsigma21_252d(close).diff().diff()


def f39_vclu_286_var_logsigma21_252d_d2(close):
    return f39_vclu_286_var_logsigma21_252d(close).diff().diff()


def f39_vclu_287_skew_delta_sigma21_252d_d2(close):
    return f39_vclu_287_skew_delta_sigma21_252d(close).diff().diff()


def f39_vclu_288_kurt_delta_sigma21_252d_d2(close):
    return f39_vclu_288_kurt_delta_sigma21_252d(close).diff().diff()


def f39_vclu_289_risk_return_corr_252d_d2(close):
    return f39_vclu_289_risk_return_corr_252d(close).diff().diff()


def f39_vclu_290_sharpe_proxy_21d_mean_252d_d2(close):
    return f39_vclu_290_sharpe_proxy_21d_mean_252d(close).diff().diff()


def f39_vclu_291_sortino_proxy_252d_d2(close):
    return f39_vclu_291_sortino_proxy_252d(close).diff().diff()


def f39_vclu_292_sharpe_high_vol_regime_252d_d2(close):
    return f39_vclu_292_sharpe_high_vol_regime_252d(close).diff().diff()


def f39_vclu_293_sharpe_low_vol_regime_252d_d2(close):
    return f39_vclu_293_sharpe_low_vol_regime_252d(close).diff().diff()


def f39_vclu_294_vol_targeted_excess_return_252d_d2(close):
    return f39_vclu_294_vol_targeted_excess_return_252d(close).diff().diff()


def f39_vclu_295_slope_sigma252_21d_d2(close):
    return f39_vclu_295_slope_sigma252_21d(close).diff().diff()


def f39_vclu_296_num_sigma_trend_reversals_504d_d2(close):
    return f39_vclu_296_num_sigma_trend_reversals_504d(close).diff().diff()


def f39_vclu_297_sigma_trend_velocity_zscore_252d_d2(close):
    return f39_vclu_297_sigma_trend_velocity_zscore_252d(close).diff().diff()


def f39_vclu_298_newey_west_sigma_persistence_252d_d2(close):
    return f39_vclu_298_newey_west_sigma_persistence_252d(close).diff().diff()


def f39_vclu_299_mean_abs_sigma_shock_multi_horizon_d2(close):
    return f39_vclu_299_mean_abs_sigma_shock_multi_horizon(close).diff().diff()


def f39_vclu_300_total_variation_sigma21_normalized_252d_d2(close):
    return f39_vclu_300_total_variation_sigma21_normalized_252d(close).diff().diff()


VOLATILITY_CLUSTERING_D2_REGISTRY_226_300 = {
    "f39_vclu_226_gjr_full_signal_252d_d2": {"inputs": ["close"], "func": f39_vclu_226_gjr_full_signal_252d_d2},
    "f39_vclu_227_tgarch_absolute_persistence_252d_d2": {"inputs": ["close"], "func": f39_vclu_227_tgarch_absolute_persistence_252d_d2},
    "f39_vclu_228_pgarch_power_fit_252d_d2": {"inputs": ["close"], "func": f39_vclu_228_pgarch_power_fit_252d_d2},
    "f39_vclu_229_starch_smooth_transition_proxy_252d_d2": {"inputs": ["close"], "func": f39_vclu_229_starch_smooth_transition_proxy_252d_d2},
    "f39_vclu_230_swarch_high_low_ratio_504d_d2": {"inputs": ["close"], "func": f39_vclu_230_swarch_high_low_ratio_504d_d2},
    "f39_vclu_231_icss_variance_breaks_within_252d_d2": {"inputs": ["close"], "func": f39_vclu_231_icss_variance_breaks_within_252d_d2},
    "f39_vclu_232_icss_time_since_last_break_252d_d2": {"inputs": ["close"], "func": f39_vclu_232_icss_time_since_last_break_252d_d2},
    "f39_vclu_233_varmax_cross_sigma_volume_coef_252d_d2": {"inputs": ["close", "volume"], "func": f39_vclu_233_varmax_cross_sigma_volume_coef_252d_d2},
    "f39_vclu_234_cv_logsigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_234_cv_logsigma21_252d_d2},
    "f39_vclu_235_halflife_sigma21_vs_sigma252_252d_d2": {"inputs": ["close"], "func": f39_vclu_235_halflife_sigma21_vs_sigma252_252d_d2},
    "f39_vclu_236_spike_followed_by_spike_count_63d_d2": {"inputs": ["close"], "func": f39_vclu_236_spike_followed_by_spike_count_63d_d2},
    "f39_vclu_237_spike_followed_by_quiet_count_63d_d2": {"inputs": ["close"], "func": f39_vclu_237_spike_followed_by_quiet_count_63d_d2},
    "f39_vclu_238_spike_aftermath_kurt_252d_d2": {"inputs": ["close"], "func": f39_vclu_238_spike_aftermath_kurt_252d_d2},
    "f39_vclu_239_spike_recovery_bars_252d_d2": {"inputs": ["close"], "func": f39_vclu_239_spike_recovery_bars_252d_d2},
    "f39_vclu_240_var_sigma21_minus_lag63_252d_d2": {"inputs": ["close"], "func": f39_vclu_240_var_sigma21_minus_lag63_252d_d2},
    "f39_vclu_241_overnight_only_persistence_252d_d2": {"inputs": ["open", "close"], "func": f39_vclu_241_overnight_only_persistence_252d_d2},
    "f39_vclu_242_persistence_hl_over_close_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_242_persistence_hl_over_close_252d_d2},
    "f39_vclu_243_skew_hl_over_close_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_243_skew_hl_over_close_252d_d2},
    "f39_vclu_244_bimodality_coef_hl_over_close_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_244_bimodality_coef_hl_over_close_252d_d2},
    "f39_vclu_245_persistence_upper_shadow_ratio_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_245_persistence_upper_shadow_ratio_252d_d2},
    "f39_vclu_246_persistence_lower_shadow_ratio_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_246_persistence_lower_shadow_ratio_252d_d2},
    "f39_vclu_247_body_share_asymmetry_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_247_body_share_asymmetry_252d_d2},
    "f39_vclu_248_mean_body_share_top_decile_range_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_248_mean_body_share_top_decile_range_252d_d2},
    "f39_vclu_249_mean_body_share_bottom_decile_range_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_249_mean_body_share_bottom_decile_range_252d_d2},
    "f39_vclu_250_persistence_clv_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_250_persistence_clv_252d_d2},
    "f39_vclu_251_spectrum_width_q_neg2_q2_252d_d2": {"inputs": ["close"], "func": f39_vclu_251_spectrum_width_q_neg2_q2_252d_d2},
    "f39_vclu_252_gen_hurst_q3_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_252_gen_hurst_q3_r_252d_d2},
    "f39_vclu_253_mfdfa_q2_minus_qneg2_diff_252d_d2": {"inputs": ["close"], "func": f39_vclu_253_mfdfa_q2_minus_qneg2_diff_252d_d2},
    "f39_vclu_254_dcca_sigma5_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_254_dcca_sigma5_sigma21_252d_d2},
    "f39_vclu_255_mf_dcca_q2_252d_d2": {"inputs": ["close"], "func": f39_vclu_255_mf_dcca_q2_252d_d2},
    "f39_vclu_256_coarse_grained_entropy_sigma_scale5_252d_d2": {"inputs": ["close"], "func": f39_vclu_256_coarse_grained_entropy_sigma_scale5_252d_d2},
    "f39_vclu_257_multiscale_entropy_ratio_252d_d2": {"inputs": ["close"], "func": f39_vclu_257_multiscale_entropy_ratio_252d_d2},
    "f39_vclu_258_higuchi_fractal_dim_sigma_252d_d2": {"inputs": ["close"], "func": f39_vclu_258_higuchi_fractal_dim_sigma_252d_d2},
    "f39_vclu_259_bandpower_low_freq_absret_252d_d2": {"inputs": ["close"], "func": f39_vclu_259_bandpower_low_freq_absret_252d_d2},
    "f39_vclu_260_bandpower_mid_freq_absret_252d_d2": {"inputs": ["close"], "func": f39_vclu_260_bandpower_mid_freq_absret_252d_d2},
    "f39_vclu_261_spectral_peak_freq_sigma5_252d_d2": {"inputs": ["close"], "func": f39_vclu_261_spectral_peak_freq_sigma5_252d_d2},
    "f39_vclu_262_phase_shift_sig5_sig21_252d_d2": {"inputs": ["close"], "func": f39_vclu_262_phase_shift_sig5_sig21_252d_d2},
    "f39_vclu_263_wavelet_energy_ratio_2_8_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_263_wavelet_energy_ratio_2_8_r_252d_d2},
    "f39_vclu_264_wavelet_energy_ratio_4_16_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_264_wavelet_energy_ratio_4_16_r_252d_d2},
    "f39_vclu_265_wavelet_variance_scale4_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_265_wavelet_variance_scale4_r_252d_d2},
    "f39_vclu_266_wavelet_variance_scale8_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_266_wavelet_variance_scale8_r_252d_d2},
    "f39_vclu_267_ar2_phi2_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_267_ar2_phi2_sigma21_252d_d2},
    "f39_vclu_268_halflife_sigma5_252d_d2": {"inputs": ["close"], "func": f39_vclu_268_halflife_sigma5_252d_d2},
    "f39_vclu_269_ar1_of_sigma_diff_horizon_252d_d2": {"inputs": ["close"], "func": f39_vclu_269_ar1_of_sigma_diff_horizon_252d_d2},
    "f39_vclu_270_var_ratio_r_q5_252d_d2": {"inputs": ["close"], "func": f39_vclu_270_var_ratio_r_q5_252d_d2},
    "f39_vclu_271_var_ratio_r_q21_252d_d2": {"inputs": ["close"], "func": f39_vclu_271_var_ratio_r_q21_252d_d2},
    "f39_vclu_272_persistence_vol_zscore_252d_d2": {"inputs": ["close"], "func": f39_vclu_272_persistence_vol_zscore_252d_d2},
    "f39_vclu_273_var_ratio_rsq_q21_504d_d2": {"inputs": ["close"], "func": f39_vclu_273_var_ratio_rsq_q21_504d_d2},
    "f39_vclu_274_sigma_low_at_252d_high_proxy_63d_d2": {"inputs": ["close"], "func": f39_vclu_274_sigma_low_at_252d_high_proxy_63d_d2},
    "f39_vclu_275_garch_next_day_var_forecast_proxy_d2": {"inputs": ["close"], "func": f39_vclu_275_garch_next_day_var_forecast_proxy_d2},
    "f39_vclu_276_forecast_vs_realized_correlation_21d_d2": {"inputs": ["close"], "func": f39_vclu_276_forecast_vs_realized_correlation_21d_d2},
    "f39_vclu_277_current_vol_cluster_magnitude_252d_d2": {"inputs": ["close"], "func": f39_vclu_277_current_vol_cluster_magnitude_252d_d2},
    "f39_vclu_278_time_since_last_vol_cluster_end_252d_d2": {"inputs": ["close"], "func": f39_vclu_278_time_since_last_vol_cluster_end_252d_d2},
    "f39_vclu_279_num_vol_clusters_252d_d2": {"inputs": ["close"], "func": f39_vclu_279_num_vol_clusters_252d_d2},
    "f39_vclu_280_mean_vol_cluster_duration_252d_d2": {"inputs": ["close"], "func": f39_vclu_280_mean_vol_cluster_duration_252d_d2},
    "f39_vclu_281_coskewness_sigma_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_281_coskewness_sigma_r_252d_d2},
    "f39_vclu_282_cokurtosis_sigma_rsq_252d_d2": {"inputs": ["close"], "func": f39_vclu_282_cokurtosis_sigma_rsq_252d_d2},
    "f39_vclu_283_corr_sigma_r_high_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_283_corr_sigma_r_high_vol_regime_252d_d2},
    "f39_vclu_284_skew_logsigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_284_skew_logsigma21_252d_d2},
    "f39_vclu_285_kurt_logsigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_285_kurt_logsigma21_252d_d2},
    "f39_vclu_286_var_logsigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_286_var_logsigma21_252d_d2},
    "f39_vclu_287_skew_delta_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_287_skew_delta_sigma21_252d_d2},
    "f39_vclu_288_kurt_delta_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_288_kurt_delta_sigma21_252d_d2},
    "f39_vclu_289_risk_return_corr_252d_d2": {"inputs": ["close"], "func": f39_vclu_289_risk_return_corr_252d_d2},
    "f39_vclu_290_sharpe_proxy_21d_mean_252d_d2": {"inputs": ["close"], "func": f39_vclu_290_sharpe_proxy_21d_mean_252d_d2},
    "f39_vclu_291_sortino_proxy_252d_d2": {"inputs": ["close"], "func": f39_vclu_291_sortino_proxy_252d_d2},
    "f39_vclu_292_sharpe_high_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_292_sharpe_high_vol_regime_252d_d2},
    "f39_vclu_293_sharpe_low_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_293_sharpe_low_vol_regime_252d_d2},
    "f39_vclu_294_vol_targeted_excess_return_252d_d2": {"inputs": ["close"], "func": f39_vclu_294_vol_targeted_excess_return_252d_d2},
    "f39_vclu_295_slope_sigma252_21d_d2": {"inputs": ["close"], "func": f39_vclu_295_slope_sigma252_21d_d2},
    "f39_vclu_296_num_sigma_trend_reversals_504d_d2": {"inputs": ["close"], "func": f39_vclu_296_num_sigma_trend_reversals_504d_d2},
    "f39_vclu_297_sigma_trend_velocity_zscore_252d_d2": {"inputs": ["close"], "func": f39_vclu_297_sigma_trend_velocity_zscore_252d_d2},
    "f39_vclu_298_newey_west_sigma_persistence_252d_d2": {"inputs": ["close"], "func": f39_vclu_298_newey_west_sigma_persistence_252d_d2},
    "f39_vclu_299_mean_abs_sigma_shock_multi_horizon_d2": {"inputs": ["close"], "func": f39_vclu_299_mean_abs_sigma_shock_multi_horizon_d2},
    "f39_vclu_300_total_variation_sigma21_normalized_252d_d2": {"inputs": ["close"], "func": f39_vclu_300_total_variation_sigma21_normalized_252d_d2},
}
