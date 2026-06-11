"""volatility_clustering d2 features 151-225 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the 150 in __base__001_075.py and __base__076_150.py.
Drawn from gap analysis of the GARCH-family / vol-clustering literature: GJR
threshold-asymmetry, APARCH δ, Taylor effect, EGARCH log-vol persistence,
Engle-Ng sign/size bias tests, Engle-Lee component decomposition, FIGARCH
long-memory, MF-DFA τ(q) on r, wavelet-variance scaling, OHLC-vol persistence
(GK / RS / YZ AR1, overnight-vs-intraday), jump-robust vol persistence (MinRV /
MedRV AR1), SV-leverage proxies, Markov-switching on σ_21, Inclán-Tiao on σ,
Bai-Perron / Andrews breaks on σ, Burghardt vol-cone, range-implied variance
gap (vol-risk-premium proxy), Engle-Ng news-impact convexity, regime-conditional
moments.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers at top — no cross-
family imports.
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


def _ewma_vol(r, lam):
    return np.sqrt((r ** 2).ewm(alpha=1.0 - lam, min_periods=21).mean())


def _gk_sigma(high, low, open, close, n=21):
    a = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2
    b = (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open)) ** 2
    return np.sqrt((a - b).rolling(n, min_periods=max(n // 3, 2)).mean())


def _parkinson_sigma(high, low, n=21):
    return np.sqrt(((_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0)))
                   .rolling(n, min_periods=max(n // 3, 2)).mean())


def _rs_sigma(high, low, open, close, n=21):
    a = (_safe_log(high) - _safe_log(close)) * (_safe_log(high) - _safe_log(open))
    b = (_safe_log(low) - _safe_log(close)) * (_safe_log(low) - _safe_log(open))
    return np.sqrt((a + b).rolling(n, min_periods=max(n // 3, 2)).mean())


def _yz_sigma(open, high, low, close, n=21):
    log_oc1 = _safe_log(open) - _safe_log(close.shift(1))
    log_co = _safe_log(close) - _safe_log(open)
    sig_o = log_oc1.rolling(n, min_periods=max(n // 3, 2)).var()
    sig_c = log_co.rolling(n, min_periods=max(n // 3, 2)).var()
    rs2 = _rs_sigma(high, low, open, close, n) ** 2
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    return np.sqrt(sig_o + k * sig_c + (1 - k) * rs2)


def _bv(r, n):
    pr = r.abs() * r.abs().shift(1)
    return (np.pi / 2.0) * pr.rolling(n, min_periods=max(n // 3, 2)).sum()


def _rv(r, n):
    return (r ** 2).rolling(n, min_periods=max(n // 3, 2)).sum()


# ============================================================
# Bucket Z1 — Asymmetric / Non-linear GARCH (151-158)
# ============================================================

def f39_vclu_151_gjr_threshold_asymmetry_252d(close: pd.Series) -> pd.Series:
    """GJR-threshold asymmetry γ: rolling 252d OLS β on r²_{t-1}·1{r_{t-1}<0} controlling for r²_{t-1}."""
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
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _gam(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_152_aparch_delta_proxy_252d(close: pd.Series) -> pd.Series:
    """APARCH δ proxy: argmax_δ of |corr(|r|^δ_t, |r|^δ_{t-1})| over δ∈{0.5,1,1.5,2,2.5} on 252d."""
    a = _log_ret(close).abs()

    def _arg(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        best_d = np.nan; best_c = -1.0
        for d in (0.5, 1.0, 1.5, 2.0, 2.5):
            x = ww ** d
            c = np.corrcoef(x[1:], x[:-1])[0, 1] if len(x) > 1 else np.nan
            if np.isfinite(c) and abs(c) > best_c:
                best_c = abs(c); best_d = d
        return float(best_d)
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_arg, raw=True)


def f39_vclu_153_taylor_effect_252d(close: pd.Series) -> pd.Series:
    """Taylor effect: argmax_d of autocorr(|r|^d) over d∈{0.5,1,1.5,2,2.5} on 252d (often d≈1)."""
    return f39_vclu_152_aparch_delta_proxy_252d(close)


def f39_vclu_154_egarch_log_vol_ar1_252d(close: pd.Series) -> pd.Series:
    """EGARCH log-vol persistence β̂: AR(1) of log σ²_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ls2 = _safe_log(s ** 2 + 1e-12)
    return ls2.rolling(YDAYS, min_periods=QDAYS).corr(ls2.shift(1))


def f39_vclu_155_nic_convexity_252d(close: pd.Series) -> pd.Series:
    """News-impact-curve convexity: rolling 252d quadratic-fit coef of r²_t on r_{t-1}."""
    r = _log_ret(close)
    r2 = r ** 2
    lag = r.shift(1)
    combined = pd.concat([r2, lag], axis=1).values

    def _conv(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(y) | np.isnan(x))
        if m.sum() < QDAYS:
            return np.nan
        try:
            coefs = np.polyfit(x[m], y[m], 2)
            return float(coefs[0])
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _conv(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_156_engle_ng_sign_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng sign-bias t-stat: regression of z²_t on indicator 1{r_{t-1}<0} over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z2 = _safe_div(r ** 2, sig ** 2)
    ind = (r.shift(1) < 0).astype(float)
    combined = pd.concat([z2, ind], axis=1).values

    def _t(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(y) | np.isnan(x))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), x[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            res = y[m] - X @ beta
            sse = (res ** 2).sum()
            n_ = m.sum()
            var = sse / (n_ - 2) * np.linalg.inv(X.T @ X)[1, 1]
            return float(beta[1] / np.sqrt(var)) if var > 0 else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _t(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_157_engle_ng_neg_size_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng negative-size bias t-stat: regression of z²_t on r_{t-1}·1{r_{t-1}<0} over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z2 = _safe_div(r ** 2, sig ** 2)
    x = r.shift(1).where(r.shift(1) < 0, 0.0)
    combined = pd.concat([z2, x], axis=1).values

    def _t(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, xx = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(y) | np.isnan(xx))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), xx[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            res = y[m] - X @ beta
            sse = (res ** 2).sum()
            n_ = m.sum()
            var = sse / (n_ - 2) * np.linalg.inv(X.T @ X)[1, 1]
            return float(beta[1] / np.sqrt(var)) if var > 0 else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _t(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_158_engle_ng_pos_size_bias_252d(close: pd.Series) -> pd.Series:
    """Engle-Ng positive-size bias t-stat: regression of z²_t on r_{t-1}·1{r_{t-1}>0} over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z2 = _safe_div(r ** 2, sig ** 2)
    x = r.shift(1).where(r.shift(1) > 0, 0.0)
    combined = pd.concat([z2, x], axis=1).values

    def _t(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, xx = arr[:, 0], arr[:, 1]
        m = ~(np.isnan(y) | np.isnan(xx))
        if m.sum() < QDAYS:
            return np.nan
        X = np.column_stack([np.ones(m.sum()), xx[m]])
        try:
            beta = np.linalg.lstsq(X, y[m], rcond=None)[0]
            res = y[m] - X @ beta
            sse = (res ** 2).sum()
            n_ = m.sum()
            var = sse / (n_ - 2) * np.linalg.inv(X.T @ X)[1, 1]
            return float(beta[1] / np.sqrt(var)) if var > 0 else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _t(combined[i - YDAYS + 1:i + 1])
    return out


# ============================================================
# Bucket Z2 — Component / multi-component vol (159-162)
# ============================================================

def f39_vclu_159_engle_lee_transitory_gap_252d(close: pd.Series) -> pd.Series:
    """Engle-Lee transitory gap: σ_21 − 252d rolling mean of σ_21 (short-run deviation from trend)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s - s.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_160_engle_lee_permanent_drift_252d(close: pd.Series) -> pd.Series:
    """Engle-Lee permanent-component drift: rolling 252d slope of 252d-rolling-mean-σ_21."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    long_run = s.rolling(YDAYS, min_periods=QDAYS).mean()
    return _rolling_slope(long_run, YDAYS)


def f39_vclu_161_spline_garch_lowfreq_252d(close: pd.Series) -> pd.Series:
    """Spline-GARCH low-frequency vol: rolling 504d mean of log σ²_252 (slowly-varying trend)."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return _safe_log(s ** 2 + 1e-12).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f39_vclu_162_mfgarch_macro_trend_252d(close: pd.Series) -> pd.Series:
    """MFGARCH-style macro trend: beta-weighted past 252 r² (geometric weights w=0.97^k normalized)."""
    r2 = _log_ret(close) ** 2
    weights = np.array([0.97 ** k for k in range(YDAYS)])
    weights = weights / weights.sum()
    weights = weights[::-1]  # most-recent gets weight w_0
    return r2.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float(np.dot(w[-len(weights):], weights[-len(w):])) if len(w) >= len(weights) else np.nan,
        raw=True,
    )


# ============================================================
# Bucket Z3 — Long-memory beyond GPH (163-167)
# ============================================================

def f39_vclu_163_local_whittle_d_absret_252d(close: pd.Series) -> pd.Series:
    """Local Whittle d̂ on |r| over 252d (semi-parametric long-memory via periodogram log-log slope)."""
    a = _log_ret(close).abs()

    def _lw(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        m = int(n ** 0.5)
        if m < 4:
            return np.nan
        freqs = np.arange(1, m + 1) / n
        pwr = psd[1:m + 1]
        lx = np.log(freqs); ly = np.log(pwr + 1e-12)
        xm = lx.mean(); ym = ly.mean()
        d = ((lx - xm) ** 2).sum()
        slope = -((lx - xm) * (ly - ym)).sum() / d if d > 0 else np.nan
        return float(slope / 2.0) if np.isfinite(slope) else np.nan
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_lw, raw=True)


def f39_vclu_164_figarch_d_via_acf_decay_504d(close: pd.Series) -> pd.Series:
    """FIGARCH d via ACF decay rate: log-log slope of |autocorr(|r|)| at lags 10..50 over 504d."""
    a = _log_ret(close).abs()

    def _fi(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        m = ww.mean()
        var = ((ww - m) ** 2).sum()
        if var == 0:
            return np.nan
        ks = np.arange(10, 51)
        acfs = []
        for k in ks:
            c = ((ww[k:] - m) * (ww[:-k] - m)).sum() / var
            acfs.append(abs(c) + 1e-9)
        x = np.log(ks); y = np.log(acfs)
        xm = x.mean(); ym = y.mean()
        d = ((x - xm) ** 2).sum()
        slope = -((x - xm) * (y - ym)).sum() / d if d > 0 else np.nan
        return float((1.0 - slope) / 2.0) if np.isfinite(slope) else np.nan
    return a.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_fi, raw=True)


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


def f39_vclu_165_mfdfa_tau_q2_r_252d(close: pd.Series) -> pd.Series:
    """MF-DFA τ(q=2) = 2·H(q=2) − 1 on r over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: 2.0 * _gen_hurst(w, 2.0) - 1.0, raw=True)


def f39_vclu_166_mfdfa_tau_q4_r_252d(close: pd.Series) -> pd.Series:
    """MF-DFA τ(q=4) = 4·H(q=4) − 1 on r over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).apply(lambda w: 4.0 * _gen_hurst(w, 4.0) - 1.0, raw=True)


def f39_vclu_167_wavelet_variance_scaling_slope_r_252d(close: pd.Series) -> pd.Series:
    """Wavelet-variance scaling slope of r over 252d: log-log slope across Haar scales 2,4,8,16,32."""
    r = _log_ret(close)

    def _wv(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < 100:
            return np.nan
        scales = [2, 4, 8, 16, 32]
        wv = []
        for s in scales:
            if n < s * 4:
                return np.nan
            n_pairs = (n // s) * s
            block = ww[:n_pairs].reshape(-1, s)
            avg = block.mean(axis=1)
            # Haar detail at scale s ~ var of (avg_{i+1} - avg_i)
            d = np.diff(avg)
            wv.append(d.var() if len(d) > 1 else np.nan)
        if any(np.isnan(wv)):
            return np.nan
        lx = np.log(scales); ly = np.log(np.array(wv) + 1e-12)
        xm = lx.mean(); ym = ly.mean()
        dd = ((lx - xm) ** 2).sum()
        return float(((lx - xm) * (ly - ym)).sum() / dd) if dd > 0 else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_wv, raw=True)


# ============================================================
# Bucket Z4 — OHLC vol persistence (168-172)
# ============================================================

def f39_vclu_168_ar1_gk_sigma_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of Garman-Klass σ over 252d."""
    g = _gk_sigma(high, low, open, close, MDAYS)
    return g.rolling(YDAYS, min_periods=QDAYS).corr(g.shift(1))


def f39_vclu_169_ar1_rs_sigma_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of Rogers-Satchell σ over 252d."""
    rs = _rs_sigma(high, low, open, close, MDAYS)
    return rs.rolling(YDAYS, min_periods=QDAYS).corr(rs.shift(1))


def f39_vclu_170_ar1_yz_sigma_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of Yang-Zhang σ (combines overnight + intraday) over 252d."""
    yz = _yz_sigma(open, high, low, close, MDAYS)
    return yz.rolling(YDAYS, min_periods=QDAYS).corr(yz.shift(1))


def f39_vclu_171_ar1_overnight_to_intraday_var_ratio_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) of (overnight² / intraday²) ratio over 252d (overnight-vs-intraday clustering)."""
    co = _safe_log(open) - _safe_log(close.shift(1))
    oc = _safe_log(close) - _safe_log(open)
    ratio = _safe_div(co ** 2, oc ** 2)
    return ratio.rolling(YDAYS, min_periods=QDAYS).corr(ratio.shift(1))


def f39_vclu_172_parkinson_to_c2c_noise_share_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Alizadeh-Brandt-Diebold-style: Parkinson σ_21 / (|c2c-ret| · √(π/2)) — noise-share proxy."""
    pk = _parkinson_sigma(high, low, MDAYS)
    c2c_mag = _log_ret(close).abs() * np.sqrt(np.pi / 2.0)
    return _safe_div(pk, c2c_mag.rolling(MDAYS, min_periods=WDAYS).mean())


# ============================================================
# Bucket Z5 — Jump-robust σ persistence (173-176)
# ============================================================

def f39_vclu_173_har_rv_j_jump_share_21d(close: pd.Series) -> pd.Series:
    """HAR-RV-J jump-share component: max(0, RV-BV) / RV over 21d (vol-clustering-flavored)."""
    r = _log_ret(close)
    jvar = (_rv(r, MDAYS) - _bv(r, MDAYS)).clip(lower=0.0)
    return _safe_div(jvar, _rv(r, MDAYS))


def f39_vclu_174_continuous_vs_jump_variance_21d(close: pd.Series) -> pd.Series:
    """Continuous-vs-jump variance share BV/RV at 21d (distinct horizon from family 38's 63d/252d)."""
    r = _log_ret(close)
    return _safe_div(_bv(r, MDAYS), _rv(r, MDAYS))


def f39_vclu_175_ar1_medrv_sigma_252d(close: pd.Series) -> pd.Series:
    """AR(1) coef of MedRV-σ (jump-robust σ) over 252d."""
    r = _log_ret(close).abs()
    med = pd.concat([r.shift(2), r.shift(1), r], axis=1).median(axis=1)
    k = np.pi / (6.0 - 4.0 * np.sqrt(3.0) + np.pi)
    medrv = k * (med ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    medrv_sigma = np.sqrt(medrv)
    return medrv_sigma.rolling(YDAYS, min_periods=QDAYS).corr(medrv_sigma.shift(1))


def f39_vclu_176_ar1_minrv_sigma_252d(close: pd.Series) -> pd.Series:
    """AR(1) coef of MinRV-σ (jump-robust σ) over 252d."""
    r = _log_ret(close).abs()
    mn = pd.concat([r, r.shift(1)], axis=1).min(axis=1)
    k = np.pi / (np.pi - 2.0)
    minrv = k * (mn ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    minrv_sigma = np.sqrt(minrv)
    return minrv_sigma.rolling(YDAYS, min_periods=QDAYS).corr(minrv_sigma.shift(1))


# ============================================================
# Bucket Z6 — Stochastic-volatility proxies (177-180)
# ============================================================

def f39_vclu_177_sv_log_r2_ar1_504d(close: pd.Series) -> pd.Series:
    """Stochastic-vol log r² AR(1) persistence (proxy for latent log-σ² AR(1)) over 504d."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))
    return lr2.rolling(DDAYS_2Y, min_periods=YDAYS).corr(lr2.shift(1))


def f39_vclu_178_sv_innovation_variance_504d(close: pd.Series) -> pd.Series:
    """SV innovation variance: var(Δ log r²) over 504d (vol-of-log-vol)."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))
    return lr2.diff().rolling(DDAYS_2Y, min_periods=YDAYS).var()


def f39_vclu_179_sv_lagged_leverage_corr_dlogvol_lagr_252d(close: pd.Series) -> pd.Series:
    """SV lagged-leverage: corr(Δlog σ²_t, r_{t-1}) over 252d (distinct from contemporaneous leverage)."""
    r = _log_ret(close)
    s2 = (r ** 2 + 1e-12)
    dls2 = _safe_log(s2).diff()
    return dls2.rolling(YDAYS, min_periods=QDAYS).corr(r.shift(1))


def f39_vclu_180_heston_var_of_sigma_times_r_252d(close: pd.Series) -> pd.Series:
    """Heston-style proxy: var(σ_21·r) over 252d (vol-return interaction)."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    return (s * r).rolling(YDAYS, min_periods=QDAYS).var()


# ============================================================
# Bucket Z7 — Tail / distributional shape on σ (181-184)
# ============================================================

def _hill_estimator(arr: np.ndarray, top_frac: float) -> float:
    a = arr[~np.isnan(arr)]
    if len(a) < 30:
        return np.nan
    k = max(int(len(a) * top_frac), 5)
    top = np.sort(a)[-k:]
    th = top[0]
    if th <= 0:
        return np.nan
    lg = np.log(top / th)
    val = lg[1:].mean() if len(lg) > 1 else np.nan
    return float(val) if np.isfinite(val) and val > 0 else np.nan


def f39_vclu_181_hill_sigma21_top10_1260d(close: pd.Series) -> pd.Series:
    """Hill (top 10%) of σ_21 distribution over 1260d (multi-year vol-tail thickness)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(lambda w: _hill_estimator(w, 0.10), raw=True)


def f39_vclu_182_mcculloch_levy_alpha_sigma_252d(close: pd.Series) -> pd.Series:
    """McCulloch Lévy α-stable index on σ_21 distribution over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _alpha(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        q5, q25, q75, q95 = np.quantile(ww, [0.05, 0.25, 0.75, 0.95])
        denom = q75 - q25
        if denom <= 0:
            return np.nan
        v = (q95 - q5) / denom
        return float(np.interp(v, [2.439, 3.073, 4.451, 11.62], [2.0, 1.5, 1.0, 0.5]))
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_alpha, raw=True)


def f39_vclu_183_es5_persistence_252d(close: pd.Series) -> pd.Series:
    """AR(1) of rolling-21d 5% Expected Shortfall (CARE) of r over 252d — tail-vol clustering."""
    r = _log_ret(close)
    p05 = r.rolling(MDAYS, min_periods=WDAYS).quantile(0.05)
    es = r.where(r < p05, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    return es.rolling(YDAYS, min_periods=QDAYS).corr(es.shift(1))


def f39_vclu_184_cond_skew_zr_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Conditional skew of z=r/σ̂_21-prior in high-vol (σ_21>p75-252d) regime over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z = _safe_div(r, sig)
    s21 = _rolling_sigma(r, MDAYS)
    p75 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = z.where(s21 > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).skew()


# ============================================================
# Bucket Z8 — Regime-switching / structural-break on σ (185-189)
# ============================================================

def f39_vclu_185_ms_high_vol_state_prob_sigma_504d(close: pd.Series) -> pd.Series:
    """2-state Markov-switching high-vol regime probability via EM on σ_21 over 504d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _ms(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        med = np.median(ww)
        mu0 = ww[ww <= med].mean(); mu1 = ww[ww > med].mean()
        var0 = ww[ww <= med].var(); var1 = ww[ww > med].var()
        if var0 == 0 or var1 == 0:
            return np.nan
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
        if mu1 < mu0:
            mu0, mu1 = mu1, mu0; var0, var1 = var1, var0
        x = ww[-1]
        p0 = np.exp(-0.5 * (x - mu0) ** 2 / var0) / np.sqrt(2 * np.pi * var0)
        p1 = np.exp(-0.5 * (x - mu1) ** 2 / var1) / np.sqrt(2 * np.pi * var1)
        return float(p1 / (p0 + p1 + 1e-12))
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_ms, raw=True)


def f39_vclu_186_cusum_sq_sigma_504d(close: pd.Series) -> pd.Series:
    """Inclán-Tiao CUSUM-of-squares on σ_21 over 504d (variance regime change in σ-process)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    s2 = s ** 2

    def _cs(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        total = ww.sum()
        if total == 0:
            return np.nan
        cs = np.cumsum(ww) / total
        idx = np.arange(1, n + 1) / n
        return float(np.max(np.abs(cs - idx)))
    return s2.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_cs, raw=True)


def f39_vclu_187_bai_perron_break_count_sigma_504d(close: pd.Series) -> pd.Series:
    """Bai-Perron breakpoint count on σ_21 over 504d (supF-based, threshold 8.85)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _bp(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        cnt = 0
        for seg_start in range(0, n - QDAYS, QDAYS):
            seg = ww[seg_start:seg_start + QDAYS]
            if len(seg) < 30:
                continue
            mu = seg.mean(); tss = ((seg - mu) ** 2).sum()
            if tss == 0:
                continue
            best = 0.0
            for k in range(int(0.20 * len(seg)), int(0.80 * len(seg))):
                m1 = seg[:k].mean(); m2 = seg[k:].mean()
                rss = ((seg[:k] - m1) ** 2).sum() + ((seg[k:] - m2) ** 2).sum()
                if rss > 0:
                    f = (tss - rss) / (rss / (len(seg) - 2))
                    if f > best:
                        best = f
            if best > 8.85:
                cnt += 1
        return float(cnt)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_bp, raw=True)


def f39_vclu_188_pelt_proxy_changepoint_density_logsigma_504d(close: pd.Series) -> pd.Series:
    """PELT-proxy changepoint density on log σ_21 over 504d (count of |Δσ| > 2σ_of_σ events)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ls = _safe_log(s + 1e-12)
    diff = ls.diff()
    sig_of_sig = diff.rolling(QDAYS, min_periods=MDAYS).std()
    cp = (diff.abs() > 2 * sig_of_sig).astype(float)
    return cp.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f39_vclu_189_andrews_supf_mean_sigma_252d(close: pd.Series) -> pd.Series:
    """Andrews supF on σ_21 over 252d — mean-shift test on σ-process."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _sf(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        mu = ww.mean(); tss = ((ww - mu) ** 2).sum()
        if tss == 0:
            return np.nan
        best = 0.0
        for k in range(int(0.15 * n), int(0.85 * n)):
            m1 = ww[:k].mean(); m2 = ww[k:].mean()
            rss = ((ww[:k] - m1) ** 2).sum() + ((ww[k:] - m2) ** 2).sum()
            if rss > 0:
                f = (tss - rss) / (rss / (n - 2))
                if f > best:
                    best = f
        return float(best)
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_sf, raw=True)


# ============================================================
# Bucket Z9 — Burghardt vol cone (190-193)
# ============================================================

def f39_vclu_190_burghardt_cone_width_504d(close: pd.Series) -> pd.Series:
    """Burghardt cone width: (p90 σ − p10 σ) averaged across horizons {5,21,63,252} over 504d."""
    r = _log_ret(close)
    widths = []
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        s = _rolling_sigma(r, n)
        w = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90) - s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.10)
        widths.append(w)
    return pd.concat(widths, axis=1).mean(axis=1)


def f39_vclu_191_cone_position_score_avg_252d(close: pd.Series) -> pd.Series:
    """Cone-position score: avg percentile of σ_h within own 252d distribution across h∈{5,21,63}."""
    r = _log_ret(close)
    pcts = []
    for n in (WDAYS, MDAYS, QDAYS):
        s = _rolling_sigma(r, n)
        rk = s.rolling(YDAYS, min_periods=QDAYS).apply(
            lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan,
            raw=True,
        )
        pcts.append(rk)
    return pd.concat(pcts, axis=1).mean(axis=1)


def f39_vclu_192_volq_envelope_breach_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 exceeds its rolling 504d p95 within trailing 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p95 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.95)
    return (s > p95).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f39_vclu_193_iqr_width_sigma21_252d(close: pd.Series) -> pd.Series:
    """IQR width of σ_21 (p75 − p25) over 252d — symmetric vol-cone aperture."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)


# ============================================================
# Bucket Z10 — Realized-measure components (194-197)
# ============================================================

def f39_vclu_194_realized_bv_per_bar_21d(close: pd.Series) -> pd.Series:
    """Realized BV per bar at 21d (jump-robust IV estimator)."""
    return _bv(_log_ret(close), MDAYS) / MDAYS


def f39_vclu_195_realized_tripower_quarticity_21d(close: pd.Series) -> pd.Series:
    """Realized tripower quarticity μ_{4/3}^{-3}·Σ|r|^{4/3}|r_-1|^{4/3}|r_-2|^{4/3} over 21d."""
    r = _log_ret(close).abs()
    a = r ** (4.0 / 3.0)
    prod = a * a.shift(1) * a.shift(2)
    mu = 2.0 ** (2.0 / 3.0) * (math.gamma(7.0 / 6.0) / np.sqrt(np.pi))
    return (mu ** -3) * prod.rolling(MDAYS, min_periods=WDAYS).sum()


def f39_vclu_196_harq_quarticity_adj_252d(close: pd.Series) -> pd.Series:
    """HARQ adjustment: daily-HAR-RV scaled by √RQ over 252d — variance-of-variance precision."""
    r = _log_ret(close)
    rq = (r ** 4).rolling(MDAYS, min_periods=WDAYS).sum()
    daily = (r ** 2).shift(1)
    return daily * np.sqrt(rq).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_197_realized_semivariance_ratio_252d(close: pd.Series) -> pd.Series:
    """Realized semi-variance ratio RS+/RS-: Σr²·1{r>0} / Σr²·1{r<0} over 252d."""
    r = _log_ret(close)
    rs_pos = ((r ** 2) * (r > 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    rs_neg = ((r ** 2) * (r < 0).astype(float)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rs_pos, rs_neg)


# ============================================================
# Bucket Z11 — Spectral on σ (198-200)
# ============================================================

def f39_vclu_198_spectral_peak_freq_sigma21_504d(close: pd.Series) -> pd.Series:
    """Peak FFT frequency of σ_21 over 504d (cycles per bar)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _peak(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        f = np.fft.rfft(ww - ww.mean())
        psd = (np.abs(f) ** 2) / n
        psd[0] = 0
        return float(int(np.argmax(psd)) / n)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_peak, raw=True)


def f39_vclu_199_spectral_entropy_sigma21_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of normalized PSD of σ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

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
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f39_vclu_200_lowfreq_coherence_sig21_sig63_504d(close: pd.Series) -> pd.Series:
    """Squared coherence of σ_21 vs σ_63 in low-freq band [0, 1/30 cyc/bar] over 504d."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS)
    s63 = _rolling_sigma(r, QDAYS)
    out = pd.Series(np.nan, index=close.index)
    a_arr = s21.values
    b_arr = s63.values
    for i in range(YDAYS, len(a_arr)):
        a = a_arr[max(0, i - DDAYS_2Y + 1):i + 1]
        b = b_arr[max(0, i - DDAYS_2Y + 1):i + 1]
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < YDAYS:
            continue
        a, b = a[m], b[m]
        n = len(a)
        fa = np.fft.rfft(a - a.mean())
        fb = np.fft.rfft(b - b.mean())
        cutoff = max(int(n / 30), 2)
        Cxy = fa[:cutoff] * np.conjugate(fb[:cutoff])
        Pxx = np.abs(fa[:cutoff]) ** 2
        Pyy = np.abs(fb[:cutoff]) ** 2
        coh = (np.abs(Cxy) ** 2) / (Pxx * Pyy + 1e-12)
        out.iloc[i] = float(coh.mean())
    return out


# ============================================================
# Bucket Z12 — Vol-risk-premium proxies (201-203)
# ============================================================

def f39_vclu_201_parkinson_minus_c2c_var_gap_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson σ² − close-to-close σ² over 21d — variance-risk-premium proxy."""
    pk2 = _parkinson_sigma(high, low, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    return pk2 - c2c2


def f39_vclu_202_parkinson_minus_c2c_var_gap_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson σ² − close-to-close σ² over 63d — VRP proxy at intermediate horizon."""
    pk2 = _parkinson_sigma(high, low, QDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), QDAYS) ** 2
    return pk2 - c2c2


def f39_vclu_203_ar1_var_gap_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) persistence of (Parkinson σ² − c2c σ²) variance gap over 252d."""
    pk2 = _parkinson_sigma(high, low, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    gap = pk2 - c2c2
    return gap.rolling(YDAYS, min_periods=QDAYS).corr(gap.shift(1))


# ============================================================
# Bucket Z13 — More EGARCH-style (204-207)
# ============================================================

def f39_vclu_204_conditional_kurt_residuals_t_dof_proxy_252d(close: pd.Series) -> pd.Series:
    """Conditional kurtosis of z=r/σ̂_21-prior → ν̂ Student-t d.o.f. proxy over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z = _safe_div(r, sig)
    kt = z.rolling(YDAYS, min_periods=QDAYS).kurt() + 3.0
    return _safe_div(4.0 * kt - 6.0, kt - 3.0).where(kt > 3.05, np.nan).clip(lower=4.5, upper=200.0)


def f39_vclu_205_conditional_skew_residuals_252d(close: pd.Series) -> pd.Series:
    """Conditional skewness of standardized residuals z=r/σ̂_21-prior over 252d."""
    r = _log_ret(close)
    sig = _rolling_sigma(r, MDAYS).shift(1)
    z = _safe_div(r, sig)
    return z.rolling(YDAYS, min_periods=QDAYS).skew()


def f39_vclu_206_nic_slope_asymmetry_252d(close: pd.Series) -> pd.Series:
    """News-impact slopes asymmetry: slope σ_t on r_{t-1} when r<0 vs r>0, over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    lag = r.shift(1)
    combined = pd.concat([s, lag], axis=1).values

    def _asym(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x = arr[:, 0], arr[:, 1]
        m_neg = ~np.isnan(y) & ~np.isnan(x) & (x < 0)
        m_pos = ~np.isnan(y) & ~np.isnan(x) & (x > 0)
        if m_neg.sum() < 20 or m_pos.sum() < 20:
            return np.nan
        try:
            beta_neg = np.linalg.lstsq(np.column_stack([np.ones(m_neg.sum()), x[m_neg]]), y[m_neg], rcond=None)[0][1]
            beta_pos = np.linalg.lstsq(np.column_stack([np.ones(m_pos.sum()), x[m_pos]]), y[m_pos], rcond=None)[0][1]
            return float(beta_neg - beta_pos)
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _asym(combined[i - YDAYS + 1:i + 1])
    return out


def f39_vclu_207_nic_kink_magnitude_at_zero_252d(close: pd.Series) -> pd.Series:
    """NIC kink magnitude at r_{t-1}=0: |slope_left − slope_right| in narrow bands around zero."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    lag = r.shift(1)
    combined = pd.concat([s, lag], axis=1).values

    def _kink(arr):
        if arr.shape[0] < QDAYS:
            return np.nan
        y, x = arr[:, 0], arr[:, 1]
        thresh = np.nanstd(x) * 0.5 if np.nanstd(x) > 0 else 0.01
        m_neg = ~np.isnan(y) & ~np.isnan(x) & (x < 0) & (x > -thresh)
        m_pos = ~np.isnan(y) & ~np.isnan(x) & (x > 0) & (x < thresh)
        if m_neg.sum() < 10 or m_pos.sum() < 10:
            return np.nan
        try:
            beta_neg = np.linalg.lstsq(np.column_stack([np.ones(m_neg.sum()), x[m_neg]]), y[m_neg], rcond=None)[0][1]
            beta_pos = np.linalg.lstsq(np.column_stack([np.ones(m_pos.sum()), x[m_pos]]), y[m_pos], rcond=None)[0][1]
            return float(abs(beta_neg - beta_pos))
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _kink(combined[i - YDAYS + 1:i + 1])
    return out


# ============================================================
# Bucket Z14 — Component / SV extras (208-211)
# ============================================================

def f39_vclu_208_permanent_component_innovation_var_504d(close: pd.Series) -> pd.Series:
    """Variance of Δ(252d-rolling-mean-σ_21) over 504d — permanent-component innovation variance."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    long_run = s.rolling(YDAYS, min_periods=QDAYS).mean()
    return long_run.diff().rolling(DDAYS_2Y, min_periods=YDAYS).var()


def f39_vclu_209_mean_reversion_speed_sigma_to_long_252d(close: pd.Series) -> pd.Series:
    """Mean-reversion speed of σ_21 toward 252d mean: −cov(Δσ, σ − μ̄)/var(σ − μ̄) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    dev = s - mu
    cov = s.diff().rolling(YDAYS, min_periods=QDAYS).cov(dev.shift(1))
    var = dev.shift(1).rolling(YDAYS, min_periods=QDAYS).var()
    return -_safe_div(cov, var)


def f39_vclu_210_sv_conditional_var_proxy_252d(close: pd.Series) -> pd.Series:
    """SV-filter conditional variance proxy: var(Δ log r²) over 252d."""
    lr2 = _safe_log((_log_ret(close) ** 2 + 1e-12))
    return lr2.diff().rolling(YDAYS, min_periods=QDAYS).var()


def f39_vclu_211_sv_alpha_leverage_slope_252d(close: pd.Series) -> pd.Series:
    """SV α (leverage) coefficient: rolling 252d slope of log r²_t on r_{t-1}."""
    r = _log_ret(close)
    lr2 = _safe_log((r ** 2 + 1e-12))
    lag = r.shift(1)
    cov = lr2.rolling(YDAYS, min_periods=QDAYS).cov(lag)
    var = lag.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(cov, var)


# ============================================================
# Bucket Z15 — More vol-regime indicators (212-215)
# ============================================================

def f39_vclu_212_time_share_sigma21_outside_iqr_252d(close: pd.Series) -> pd.Series:
    """Fraction of time σ_21 outside [p25, p75] of own past 252d distribution."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((s < p25) | (s > p75)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_213_bars_since_sigma21_above_p90_504d(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last exceeded trailing 504d 90th-pct."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    ind = (s > p90).astype(int).fillna(0).values
    out = np.full(len(ind), np.nan)
    bars = np.nan
    for i, v in enumerate(ind):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


def f39_vclu_214_longest_outside_iqr_run_504d(close: pd.Series) -> pd.Series:
    """Longest run of σ_21 outside trailing-252d IQR within 504d window."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    outside = ((s < p25) | (s > p75)).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return float(m)
    return outside.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_run, raw=True)


def f39_vclu_215_sigma_mean_crossings_63d(close: pd.Series) -> pd.Series:
    """Count of σ_21 crossings of its own 252d mean within trailing 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (s > mu).astype(float)
    return above.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket Z16 — Cross-horizon σ relationships (216-219)
# ============================================================

def _pct_rank_window(s: pd.Series, n: int, min_periods: int) -> pd.Series:
    return s.rolling(n, min_periods=min_periods).apply(
        lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan,
        raw=True,
    )


def f39_vclu_216_pctrank_sigma21_minus_pctrank_sigma252_252d(close: pd.Series) -> pd.Series:
    """pct_rank(σ_21, own 252d) − pct_rank(σ_252, own 1260d) — short-vs-long regime divergence."""
    r = _log_ret(close)
    r21 = _pct_rank_window(_rolling_sigma(r, MDAYS), YDAYS, QDAYS)
    r252 = _pct_rank_window(_rolling_sigma(r, YDAYS), DDAYS_5Y, DDAYS_2Y)
    return r21 - r252


def f39_vclu_217_corr_logsigma21_logsigma252_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(log σ_21, log σ_252) — cross-horizon log-σ coupling."""
    r = _log_ret(close)
    return _safe_log(_rolling_sigma(r, MDAYS)).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(_rolling_sigma(r, YDAYS)))


def f39_vclu_218_logsigma_horizon_spread(close: pd.Series) -> pd.Series:
    """max(log σ_h) − min(log σ_h) across h∈{5,21,63,252} — single-bar cross-horizon spread."""
    r = _log_ret(close)
    sigmas = pd.concat([
        _safe_log(_rolling_sigma(r, WDAYS)),
        _safe_log(_rolling_sigma(r, MDAYS)),
        _safe_log(_rolling_sigma(r, QDAYS)),
        _safe_log(_rolling_sigma(r, YDAYS)),
    ], axis=1)
    return sigmas.max(axis=1) - sigmas.min(axis=1)


def f39_vclu_219_mean_logsigma_divergence_252d(close: pd.Series) -> pd.Series:
    """Mean |log σ_21 − log σ_63| over 252d — vol-term-structure dispersion."""
    r = _log_ret(close)
    div = (_safe_log(_rolling_sigma(r, MDAYS)) - _safe_log(_rolling_sigma(r, QDAYS))).abs()
    return div.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket Z17 — Conditional-on-regime descriptors (220-223)
# ============================================================

def f39_vclu_220_mean_absr_high_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Mean |r| restricted to high-vol regime (σ_21 > own 252d p75) over 252d."""
    r = _log_ret(close).abs()
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    sel = r.where(s > p75, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_221_mean_rsq_low_vol_regime_252d(close: pd.Series) -> pd.Series:
    """Mean r² restricted to low-vol regime (σ_21 < own 252d p25) over 252d."""
    r2 = _log_ret(close) ** 2
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    sel = r2.where(s < p25, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f39_vclu_222_std_sigma21_in_high_sigma252_regime_504d(close: pd.Series) -> pd.Series:
    """Std σ_21 conditional on σ_252 > 504d p75 over 504d — vol-of-vol in long-vol regime."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    p75 = s252.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    sel = s21.where(s252 > p75, np.nan)
    return sel.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f39_vclu_223_skew_sigma21_in_high_sigma252_regime_504d(close: pd.Series) -> pd.Series:
    """Skew σ_21 conditional on σ_252 > 504d p75 over 504d."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    p75 = s252.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.75)
    sel = s21.where(s252 > p75, np.nan)
    return sel.rolling(DDAYS_2Y, min_periods=YDAYS).skew()


# ============================================================
# Bucket Z18 — Final two for 75 (224-225)
# ============================================================

def f39_vclu_224_autocorr_sigma21_lag252_504d(close: pd.Series) -> pd.Series:
    """Rolling 504d corr(σ_21_t, σ_21_{t-252}) — annual-lag seasonality of vol."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(YDAYS))


def f39_vclu_225_rs_hurst_sigma21_252d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of σ_21 over 252d — long-memory of vol process (distinct from |r| Hurst)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

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
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_rs, raw=True)


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f39_vclu_151_gjr_threshold_asymmetry_252d_d2(close):
    return f39_vclu_151_gjr_threshold_asymmetry_252d(close).diff().diff()


def f39_vclu_152_aparch_delta_proxy_252d_d2(close):
    return f39_vclu_152_aparch_delta_proxy_252d(close).diff().diff()


def f39_vclu_153_taylor_effect_252d_d2(close):
    return f39_vclu_153_taylor_effect_252d(close).diff().diff()


def f39_vclu_154_egarch_log_vol_ar1_252d_d2(close):
    return f39_vclu_154_egarch_log_vol_ar1_252d(close).diff().diff()


def f39_vclu_155_nic_convexity_252d_d2(close):
    return f39_vclu_155_nic_convexity_252d(close).diff().diff()


def f39_vclu_156_engle_ng_sign_bias_252d_d2(close):
    return f39_vclu_156_engle_ng_sign_bias_252d(close).diff().diff()


def f39_vclu_157_engle_ng_neg_size_bias_252d_d2(close):
    return f39_vclu_157_engle_ng_neg_size_bias_252d(close).diff().diff()


def f39_vclu_158_engle_ng_pos_size_bias_252d_d2(close):
    return f39_vclu_158_engle_ng_pos_size_bias_252d(close).diff().diff()


def f39_vclu_159_engle_lee_transitory_gap_252d_d2(close):
    return f39_vclu_159_engle_lee_transitory_gap_252d(close).diff().diff()


def f39_vclu_160_engle_lee_permanent_drift_252d_d2(close):
    return f39_vclu_160_engle_lee_permanent_drift_252d(close).diff().diff()


def f39_vclu_161_spline_garch_lowfreq_252d_d2(close):
    return f39_vclu_161_spline_garch_lowfreq_252d(close).diff().diff()


def f39_vclu_162_mfgarch_macro_trend_252d_d2(close):
    return f39_vclu_162_mfgarch_macro_trend_252d(close).diff().diff()


def f39_vclu_163_local_whittle_d_absret_252d_d2(close):
    return f39_vclu_163_local_whittle_d_absret_252d(close).diff().diff()


def f39_vclu_164_figarch_d_via_acf_decay_504d_d2(close):
    return f39_vclu_164_figarch_d_via_acf_decay_504d(close).diff().diff()


def f39_vclu_165_mfdfa_tau_q2_r_252d_d2(close):
    return f39_vclu_165_mfdfa_tau_q2_r_252d(close).diff().diff()


def f39_vclu_166_mfdfa_tau_q4_r_252d_d2(close):
    return f39_vclu_166_mfdfa_tau_q4_r_252d(close).diff().diff()


def f39_vclu_167_wavelet_variance_scaling_slope_r_252d_d2(close):
    return f39_vclu_167_wavelet_variance_scaling_slope_r_252d(close).diff().diff()


def f39_vclu_168_ar1_gk_sigma_252d_d2(open, high, low, close):
    return f39_vclu_168_ar1_gk_sigma_252d(open, high, low, close).diff().diff()


def f39_vclu_169_ar1_rs_sigma_252d_d2(open, high, low, close):
    return f39_vclu_169_ar1_rs_sigma_252d(open, high, low, close).diff().diff()


def f39_vclu_170_ar1_yz_sigma_252d_d2(open, high, low, close):
    return f39_vclu_170_ar1_yz_sigma_252d(open, high, low, close).diff().diff()


def f39_vclu_171_ar1_overnight_to_intraday_var_ratio_252d_d2(open, close):
    return f39_vclu_171_ar1_overnight_to_intraday_var_ratio_252d(open, close).diff().diff()


def f39_vclu_172_parkinson_to_c2c_noise_share_252d_d2(high, low, close):
    return f39_vclu_172_parkinson_to_c2c_noise_share_252d(high, low, close).diff().diff()


def f39_vclu_173_har_rv_j_jump_share_21d_d2(close):
    return f39_vclu_173_har_rv_j_jump_share_21d(close).diff().diff()


def f39_vclu_174_continuous_vs_jump_variance_21d_d2(close):
    return f39_vclu_174_continuous_vs_jump_variance_21d(close).diff().diff()


def f39_vclu_175_ar1_medrv_sigma_252d_d2(close):
    return f39_vclu_175_ar1_medrv_sigma_252d(close).diff().diff()


def f39_vclu_176_ar1_minrv_sigma_252d_d2(close):
    return f39_vclu_176_ar1_minrv_sigma_252d(close).diff().diff()


def f39_vclu_177_sv_log_r2_ar1_504d_d2(close):
    return f39_vclu_177_sv_log_r2_ar1_504d(close).diff().diff()


def f39_vclu_178_sv_innovation_variance_504d_d2(close):
    return f39_vclu_178_sv_innovation_variance_504d(close).diff().diff()


def f39_vclu_179_sv_lagged_leverage_corr_dlogvol_lagr_252d_d2(close):
    return f39_vclu_179_sv_lagged_leverage_corr_dlogvol_lagr_252d(close).diff().diff()


def f39_vclu_180_heston_var_of_sigma_times_r_252d_d2(close):
    return f39_vclu_180_heston_var_of_sigma_times_r_252d(close).diff().diff()


def f39_vclu_181_hill_sigma21_top10_1260d_d2(close):
    return f39_vclu_181_hill_sigma21_top10_1260d(close).diff().diff()


def f39_vclu_182_mcculloch_levy_alpha_sigma_252d_d2(close):
    return f39_vclu_182_mcculloch_levy_alpha_sigma_252d(close).diff().diff()


def f39_vclu_183_es5_persistence_252d_d2(close):
    return f39_vclu_183_es5_persistence_252d(close).diff().diff()


def f39_vclu_184_cond_skew_zr_high_vol_regime_252d_d2(close):
    return f39_vclu_184_cond_skew_zr_high_vol_regime_252d(close).diff().diff()


def f39_vclu_185_ms_high_vol_state_prob_sigma_504d_d2(close):
    return f39_vclu_185_ms_high_vol_state_prob_sigma_504d(close).diff().diff()


def f39_vclu_186_cusum_sq_sigma_504d_d2(close):
    return f39_vclu_186_cusum_sq_sigma_504d(close).diff().diff()


def f39_vclu_187_bai_perron_break_count_sigma_504d_d2(close):
    return f39_vclu_187_bai_perron_break_count_sigma_504d(close).diff().diff()


def f39_vclu_188_pelt_proxy_changepoint_density_logsigma_504d_d2(close):
    return f39_vclu_188_pelt_proxy_changepoint_density_logsigma_504d(close).diff().diff()


def f39_vclu_189_andrews_supf_mean_sigma_252d_d2(close):
    return f39_vclu_189_andrews_supf_mean_sigma_252d(close).diff().diff()


def f39_vclu_190_burghardt_cone_width_504d_d2(close):
    return f39_vclu_190_burghardt_cone_width_504d(close).diff().diff()


def f39_vclu_191_cone_position_score_avg_252d_d2(close):
    return f39_vclu_191_cone_position_score_avg_252d(close).diff().diff()


def f39_vclu_192_volq_envelope_breach_count_63d_d2(close):
    return f39_vclu_192_volq_envelope_breach_count_63d(close).diff().diff()


def f39_vclu_193_iqr_width_sigma21_252d_d2(close):
    return f39_vclu_193_iqr_width_sigma21_252d(close).diff().diff()


def f39_vclu_194_realized_bv_per_bar_21d_d2(close):
    return f39_vclu_194_realized_bv_per_bar_21d(close).diff().diff()


def f39_vclu_195_realized_tripower_quarticity_21d_d2(close):
    return f39_vclu_195_realized_tripower_quarticity_21d(close).diff().diff()


def f39_vclu_196_harq_quarticity_adj_252d_d2(close):
    return f39_vclu_196_harq_quarticity_adj_252d(close).diff().diff()


def f39_vclu_197_realized_semivariance_ratio_252d_d2(close):
    return f39_vclu_197_realized_semivariance_ratio_252d(close).diff().diff()


def f39_vclu_198_spectral_peak_freq_sigma21_504d_d2(close):
    return f39_vclu_198_spectral_peak_freq_sigma21_504d(close).diff().diff()


def f39_vclu_199_spectral_entropy_sigma21_252d_d2(close):
    return f39_vclu_199_spectral_entropy_sigma21_252d(close).diff().diff()


def f39_vclu_200_lowfreq_coherence_sig21_sig63_504d_d2(close):
    return f39_vclu_200_lowfreq_coherence_sig21_sig63_504d(close).diff().diff()


def f39_vclu_201_parkinson_minus_c2c_var_gap_21d_d2(high, low, close):
    return f39_vclu_201_parkinson_minus_c2c_var_gap_21d(high, low, close).diff().diff()


def f39_vclu_202_parkinson_minus_c2c_var_gap_63d_d2(high, low, close):
    return f39_vclu_202_parkinson_minus_c2c_var_gap_63d(high, low, close).diff().diff()


def f39_vclu_203_ar1_var_gap_252d_d2(high, low, close):
    return f39_vclu_203_ar1_var_gap_252d(high, low, close).diff().diff()


def f39_vclu_204_conditional_kurt_residuals_t_dof_proxy_252d_d2(close):
    return f39_vclu_204_conditional_kurt_residuals_t_dof_proxy_252d(close).diff().diff()


def f39_vclu_205_conditional_skew_residuals_252d_d2(close):
    return f39_vclu_205_conditional_skew_residuals_252d(close).diff().diff()


def f39_vclu_206_nic_slope_asymmetry_252d_d2(close):
    return f39_vclu_206_nic_slope_asymmetry_252d(close).diff().diff()


def f39_vclu_207_nic_kink_magnitude_at_zero_252d_d2(close):
    return f39_vclu_207_nic_kink_magnitude_at_zero_252d(close).diff().diff()


def f39_vclu_208_permanent_component_innovation_var_504d_d2(close):
    return f39_vclu_208_permanent_component_innovation_var_504d(close).diff().diff()


def f39_vclu_209_mean_reversion_speed_sigma_to_long_252d_d2(close):
    return f39_vclu_209_mean_reversion_speed_sigma_to_long_252d(close).diff().diff()


def f39_vclu_210_sv_conditional_var_proxy_252d_d2(close):
    return f39_vclu_210_sv_conditional_var_proxy_252d(close).diff().diff()


def f39_vclu_211_sv_alpha_leverage_slope_252d_d2(close):
    return f39_vclu_211_sv_alpha_leverage_slope_252d(close).diff().diff()


def f39_vclu_212_time_share_sigma21_outside_iqr_252d_d2(close):
    return f39_vclu_212_time_share_sigma21_outside_iqr_252d(close).diff().diff()


def f39_vclu_213_bars_since_sigma21_above_p90_504d_d2(close):
    return f39_vclu_213_bars_since_sigma21_above_p90_504d(close).diff().diff()


def f39_vclu_214_longest_outside_iqr_run_504d_d2(close):
    return f39_vclu_214_longest_outside_iqr_run_504d(close).diff().diff()


def f39_vclu_215_sigma_mean_crossings_63d_d2(close):
    return f39_vclu_215_sigma_mean_crossings_63d(close).diff().diff()


def f39_vclu_216_pctrank_sigma21_minus_pctrank_sigma252_252d_d2(close):
    return f39_vclu_216_pctrank_sigma21_minus_pctrank_sigma252_252d(close).diff().diff()


def f39_vclu_217_corr_logsigma21_logsigma252_252d_d2(close):
    return f39_vclu_217_corr_logsigma21_logsigma252_252d(close).diff().diff()


def f39_vclu_218_logsigma_horizon_spread_d2(close):
    return f39_vclu_218_logsigma_horizon_spread(close).diff().diff()


def f39_vclu_219_mean_logsigma_divergence_252d_d2(close):
    return f39_vclu_219_mean_logsigma_divergence_252d(close).diff().diff()


def f39_vclu_220_mean_absr_high_vol_regime_252d_d2(close):
    return f39_vclu_220_mean_absr_high_vol_regime_252d(close).diff().diff()


def f39_vclu_221_mean_rsq_low_vol_regime_252d_d2(close):
    return f39_vclu_221_mean_rsq_low_vol_regime_252d(close).diff().diff()


def f39_vclu_222_std_sigma21_in_high_sigma252_regime_504d_d2(close):
    return f39_vclu_222_std_sigma21_in_high_sigma252_regime_504d(close).diff().diff()


def f39_vclu_223_skew_sigma21_in_high_sigma252_regime_504d_d2(close):
    return f39_vclu_223_skew_sigma21_in_high_sigma252_regime_504d(close).diff().diff()


def f39_vclu_224_autocorr_sigma21_lag252_504d_d2(close):
    return f39_vclu_224_autocorr_sigma21_lag252_504d(close).diff().diff()


def f39_vclu_225_rs_hurst_sigma21_252d_d2(close):
    return f39_vclu_225_rs_hurst_sigma21_252d(close).diff().diff()


VOLATILITY_CLUSTERING_D2_REGISTRY_151_225 = {
    "f39_vclu_151_gjr_threshold_asymmetry_252d_d2": {"inputs": ["close"], "func": f39_vclu_151_gjr_threshold_asymmetry_252d_d2},
    "f39_vclu_152_aparch_delta_proxy_252d_d2": {"inputs": ["close"], "func": f39_vclu_152_aparch_delta_proxy_252d_d2},
    "f39_vclu_153_taylor_effect_252d_d2": {"inputs": ["close"], "func": f39_vclu_153_taylor_effect_252d_d2},
    "f39_vclu_154_egarch_log_vol_ar1_252d_d2": {"inputs": ["close"], "func": f39_vclu_154_egarch_log_vol_ar1_252d_d2},
    "f39_vclu_155_nic_convexity_252d_d2": {"inputs": ["close"], "func": f39_vclu_155_nic_convexity_252d_d2},
    "f39_vclu_156_engle_ng_sign_bias_252d_d2": {"inputs": ["close"], "func": f39_vclu_156_engle_ng_sign_bias_252d_d2},
    "f39_vclu_157_engle_ng_neg_size_bias_252d_d2": {"inputs": ["close"], "func": f39_vclu_157_engle_ng_neg_size_bias_252d_d2},
    "f39_vclu_158_engle_ng_pos_size_bias_252d_d2": {"inputs": ["close"], "func": f39_vclu_158_engle_ng_pos_size_bias_252d_d2},
    "f39_vclu_159_engle_lee_transitory_gap_252d_d2": {"inputs": ["close"], "func": f39_vclu_159_engle_lee_transitory_gap_252d_d2},
    "f39_vclu_160_engle_lee_permanent_drift_252d_d2": {"inputs": ["close"], "func": f39_vclu_160_engle_lee_permanent_drift_252d_d2},
    "f39_vclu_161_spline_garch_lowfreq_252d_d2": {"inputs": ["close"], "func": f39_vclu_161_spline_garch_lowfreq_252d_d2},
    "f39_vclu_162_mfgarch_macro_trend_252d_d2": {"inputs": ["close"], "func": f39_vclu_162_mfgarch_macro_trend_252d_d2},
    "f39_vclu_163_local_whittle_d_absret_252d_d2": {"inputs": ["close"], "func": f39_vclu_163_local_whittle_d_absret_252d_d2},
    "f39_vclu_164_figarch_d_via_acf_decay_504d_d2": {"inputs": ["close"], "func": f39_vclu_164_figarch_d_via_acf_decay_504d_d2},
    "f39_vclu_165_mfdfa_tau_q2_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_165_mfdfa_tau_q2_r_252d_d2},
    "f39_vclu_166_mfdfa_tau_q4_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_166_mfdfa_tau_q4_r_252d_d2},
    "f39_vclu_167_wavelet_variance_scaling_slope_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_167_wavelet_variance_scaling_slope_r_252d_d2},
    "f39_vclu_168_ar1_gk_sigma_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_168_ar1_gk_sigma_252d_d2},
    "f39_vclu_169_ar1_rs_sigma_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_169_ar1_rs_sigma_252d_d2},
    "f39_vclu_170_ar1_yz_sigma_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f39_vclu_170_ar1_yz_sigma_252d_d2},
    "f39_vclu_171_ar1_overnight_to_intraday_var_ratio_252d_d2": {"inputs": ["open", "close"], "func": f39_vclu_171_ar1_overnight_to_intraday_var_ratio_252d_d2},
    "f39_vclu_172_parkinson_to_c2c_noise_share_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_172_parkinson_to_c2c_noise_share_252d_d2},
    "f39_vclu_173_har_rv_j_jump_share_21d_d2": {"inputs": ["close"], "func": f39_vclu_173_har_rv_j_jump_share_21d_d2},
    "f39_vclu_174_continuous_vs_jump_variance_21d_d2": {"inputs": ["close"], "func": f39_vclu_174_continuous_vs_jump_variance_21d_d2},
    "f39_vclu_175_ar1_medrv_sigma_252d_d2": {"inputs": ["close"], "func": f39_vclu_175_ar1_medrv_sigma_252d_d2},
    "f39_vclu_176_ar1_minrv_sigma_252d_d2": {"inputs": ["close"], "func": f39_vclu_176_ar1_minrv_sigma_252d_d2},
    "f39_vclu_177_sv_log_r2_ar1_504d_d2": {"inputs": ["close"], "func": f39_vclu_177_sv_log_r2_ar1_504d_d2},
    "f39_vclu_178_sv_innovation_variance_504d_d2": {"inputs": ["close"], "func": f39_vclu_178_sv_innovation_variance_504d_d2},
    "f39_vclu_179_sv_lagged_leverage_corr_dlogvol_lagr_252d_d2": {"inputs": ["close"], "func": f39_vclu_179_sv_lagged_leverage_corr_dlogvol_lagr_252d_d2},
    "f39_vclu_180_heston_var_of_sigma_times_r_252d_d2": {"inputs": ["close"], "func": f39_vclu_180_heston_var_of_sigma_times_r_252d_d2},
    "f39_vclu_181_hill_sigma21_top10_1260d_d2": {"inputs": ["close"], "func": f39_vclu_181_hill_sigma21_top10_1260d_d2},
    "f39_vclu_182_mcculloch_levy_alpha_sigma_252d_d2": {"inputs": ["close"], "func": f39_vclu_182_mcculloch_levy_alpha_sigma_252d_d2},
    "f39_vclu_183_es5_persistence_252d_d2": {"inputs": ["close"], "func": f39_vclu_183_es5_persistence_252d_d2},
    "f39_vclu_184_cond_skew_zr_high_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_184_cond_skew_zr_high_vol_regime_252d_d2},
    "f39_vclu_185_ms_high_vol_state_prob_sigma_504d_d2": {"inputs": ["close"], "func": f39_vclu_185_ms_high_vol_state_prob_sigma_504d_d2},
    "f39_vclu_186_cusum_sq_sigma_504d_d2": {"inputs": ["close"], "func": f39_vclu_186_cusum_sq_sigma_504d_d2},
    "f39_vclu_187_bai_perron_break_count_sigma_504d_d2": {"inputs": ["close"], "func": f39_vclu_187_bai_perron_break_count_sigma_504d_d2},
    "f39_vclu_188_pelt_proxy_changepoint_density_logsigma_504d_d2": {"inputs": ["close"], "func": f39_vclu_188_pelt_proxy_changepoint_density_logsigma_504d_d2},
    "f39_vclu_189_andrews_supf_mean_sigma_252d_d2": {"inputs": ["close"], "func": f39_vclu_189_andrews_supf_mean_sigma_252d_d2},
    "f39_vclu_190_burghardt_cone_width_504d_d2": {"inputs": ["close"], "func": f39_vclu_190_burghardt_cone_width_504d_d2},
    "f39_vclu_191_cone_position_score_avg_252d_d2": {"inputs": ["close"], "func": f39_vclu_191_cone_position_score_avg_252d_d2},
    "f39_vclu_192_volq_envelope_breach_count_63d_d2": {"inputs": ["close"], "func": f39_vclu_192_volq_envelope_breach_count_63d_d2},
    "f39_vclu_193_iqr_width_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_193_iqr_width_sigma21_252d_d2},
    "f39_vclu_194_realized_bv_per_bar_21d_d2": {"inputs": ["close"], "func": f39_vclu_194_realized_bv_per_bar_21d_d2},
    "f39_vclu_195_realized_tripower_quarticity_21d_d2": {"inputs": ["close"], "func": f39_vclu_195_realized_tripower_quarticity_21d_d2},
    "f39_vclu_196_harq_quarticity_adj_252d_d2": {"inputs": ["close"], "func": f39_vclu_196_harq_quarticity_adj_252d_d2},
    "f39_vclu_197_realized_semivariance_ratio_252d_d2": {"inputs": ["close"], "func": f39_vclu_197_realized_semivariance_ratio_252d_d2},
    "f39_vclu_198_spectral_peak_freq_sigma21_504d_d2": {"inputs": ["close"], "func": f39_vclu_198_spectral_peak_freq_sigma21_504d_d2},
    "f39_vclu_199_spectral_entropy_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_199_spectral_entropy_sigma21_252d_d2},
    "f39_vclu_200_lowfreq_coherence_sig21_sig63_504d_d2": {"inputs": ["close"], "func": f39_vclu_200_lowfreq_coherence_sig21_sig63_504d_d2},
    "f39_vclu_201_parkinson_minus_c2c_var_gap_21d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_201_parkinson_minus_c2c_var_gap_21d_d2},
    "f39_vclu_202_parkinson_minus_c2c_var_gap_63d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_202_parkinson_minus_c2c_var_gap_63d_d2},
    "f39_vclu_203_ar1_var_gap_252d_d2": {"inputs": ["high", "low", "close"], "func": f39_vclu_203_ar1_var_gap_252d_d2},
    "f39_vclu_204_conditional_kurt_residuals_t_dof_proxy_252d_d2": {"inputs": ["close"], "func": f39_vclu_204_conditional_kurt_residuals_t_dof_proxy_252d_d2},
    "f39_vclu_205_conditional_skew_residuals_252d_d2": {"inputs": ["close"], "func": f39_vclu_205_conditional_skew_residuals_252d_d2},
    "f39_vclu_206_nic_slope_asymmetry_252d_d2": {"inputs": ["close"], "func": f39_vclu_206_nic_slope_asymmetry_252d_d2},
    "f39_vclu_207_nic_kink_magnitude_at_zero_252d_d2": {"inputs": ["close"], "func": f39_vclu_207_nic_kink_magnitude_at_zero_252d_d2},
    "f39_vclu_208_permanent_component_innovation_var_504d_d2": {"inputs": ["close"], "func": f39_vclu_208_permanent_component_innovation_var_504d_d2},
    "f39_vclu_209_mean_reversion_speed_sigma_to_long_252d_d2": {"inputs": ["close"], "func": f39_vclu_209_mean_reversion_speed_sigma_to_long_252d_d2},
    "f39_vclu_210_sv_conditional_var_proxy_252d_d2": {"inputs": ["close"], "func": f39_vclu_210_sv_conditional_var_proxy_252d_d2},
    "f39_vclu_211_sv_alpha_leverage_slope_252d_d2": {"inputs": ["close"], "func": f39_vclu_211_sv_alpha_leverage_slope_252d_d2},
    "f39_vclu_212_time_share_sigma21_outside_iqr_252d_d2": {"inputs": ["close"], "func": f39_vclu_212_time_share_sigma21_outside_iqr_252d_d2},
    "f39_vclu_213_bars_since_sigma21_above_p90_504d_d2": {"inputs": ["close"], "func": f39_vclu_213_bars_since_sigma21_above_p90_504d_d2},
    "f39_vclu_214_longest_outside_iqr_run_504d_d2": {"inputs": ["close"], "func": f39_vclu_214_longest_outside_iqr_run_504d_d2},
    "f39_vclu_215_sigma_mean_crossings_63d_d2": {"inputs": ["close"], "func": f39_vclu_215_sigma_mean_crossings_63d_d2},
    "f39_vclu_216_pctrank_sigma21_minus_pctrank_sigma252_252d_d2": {"inputs": ["close"], "func": f39_vclu_216_pctrank_sigma21_minus_pctrank_sigma252_252d_d2},
    "f39_vclu_217_corr_logsigma21_logsigma252_252d_d2": {"inputs": ["close"], "func": f39_vclu_217_corr_logsigma21_logsigma252_252d_d2},
    "f39_vclu_218_logsigma_horizon_spread_d2": {"inputs": ["close"], "func": f39_vclu_218_logsigma_horizon_spread_d2},
    "f39_vclu_219_mean_logsigma_divergence_252d_d2": {"inputs": ["close"], "func": f39_vclu_219_mean_logsigma_divergence_252d_d2},
    "f39_vclu_220_mean_absr_high_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_220_mean_absr_high_vol_regime_252d_d2},
    "f39_vclu_221_mean_rsq_low_vol_regime_252d_d2": {"inputs": ["close"], "func": f39_vclu_221_mean_rsq_low_vol_regime_252d_d2},
    "f39_vclu_222_std_sigma21_in_high_sigma252_regime_504d_d2": {"inputs": ["close"], "func": f39_vclu_222_std_sigma21_in_high_sigma252_regime_504d_d2},
    "f39_vclu_223_skew_sigma21_in_high_sigma252_regime_504d_d2": {"inputs": ["close"], "func": f39_vclu_223_skew_sigma21_in_high_sigma252_regime_504d_d2},
    "f39_vclu_224_autocorr_sigma21_lag252_504d_d2": {"inputs": ["close"], "func": f39_vclu_224_autocorr_sigma21_lag252_504d_d2},
    "f39_vclu_225_rs_hurst_sigma21_252d_d2": {"inputs": ["close"], "func": f39_vclu_225_rs_hurst_sigma21_252d_d2},
}
