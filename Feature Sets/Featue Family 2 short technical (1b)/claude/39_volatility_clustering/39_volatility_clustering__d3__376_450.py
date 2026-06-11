"""39_volatility_clustering d3 features 376-450 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _log_ret(close):
    return _safe_log(close).diff()

def _rolling_sigma(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std()

def _parkinson(high, low, n=21):
    return np.sqrt(((_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0))).rolling(n, min_periods=max(n // 3, 2)).mean())

def _gk(high, low, open, close, n=21):
    a = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2
    b = (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open)) ** 2
    return np.sqrt((a - b).rolling(n, min_periods=max(n // 3, 2)).mean())

def _rs(high, low, open, close, n=21):
    a = (_safe_log(high) - _safe_log(close)) * (_safe_log(high) - _safe_log(open))
    b = (_safe_log(low) - _safe_log(close)) * (_safe_log(low) - _safe_log(open))
    return np.sqrt((a + b).rolling(n, min_periods=max(n // 3, 2)).mean())

def _yz(open, high, low, close, n=21):
    log_oc1 = _safe_log(open) - _safe_log(close.shift(1))
    log_co = _safe_log(close) - _safe_log(open)
    sig_o = log_oc1.rolling(n, min_periods=max(n // 3, 2)).var()
    sig_c = log_co.rolling(n, min_periods=max(n // 3, 2)).var()
    rs2 = _rs(high, low, open, close, n) ** 2
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    return np.sqrt(sig_o + k * sig_c + (1 - k) * rs2)

def _ljung_box(s, lag, win, min_periods):
    out = pd.Series(0.0, index=s.index)
    for k in range(1, lag + 1):
        c = s.rolling(win, min_periods=min_periods).corr(s.shift(k))
        out = out + c ** 2 / (win - k)
    return win * (win + 2) * out

def f39_vclu_376_cond_sigma_top_quartile_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean σ_21 restricted to top-quartile-volume bars over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return s.where(volume > p75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_377_cond_sigma_bottom_quartile_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean σ_21 restricted to bottom-quartile-volume bars over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    return s.where(volume < p25, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_378_vol_sigma_co_spike_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-σ co-spike: both > 252d-p95, count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    s_p95 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    v_p95 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    return ((s > s_p95) & (volume > v_p95)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_379_vol_sigma_divergence_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume up but σ down: volume > p75 AND σ_21 < p25 same bar, count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    s_p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    v_p75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return ((volume > v_p75) & (s < s_p25)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_380_vol_sigma_corr_high_volume_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(σ_21, volume) restricted to high-volume regime (volume > p75) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    v_p75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    hi = volume > v_p75
    return s.where(hi, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(volume.where(hi, np.nan)).diff().diff().diff()

def f39_vclu_381_volume_leads_sigma_lag5_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(volume_t-5, σ_21_t) over 252d — volume leading σ by 5 days."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(volume.shift(WDAYS)).diff().diff().diff()

def f39_vclu_382_sigma_leads_volume_lag5_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(σ_21_t-5, volume_t) over 252d — σ leading volume by 5 days."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return volume.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(WDAYS)).diff().diff().diff()

def f39_vclu_383_granger_volume_to_sigma_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Granger-causality: ΔR² from adding volume.shift(1) to AR(1) of σ_21 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    combined = pd.concat([s, s.shift(1), volume.shift(1)], axis=1).values

    def _gc(arr):
        if arr.shape[0] < YDAYS:
            return np.nan
        y, x1, x2 = (arr[:, 0], arr[:, 1], arr[:, 2])
        m = ~(np.isnan(y) | np.isnan(x1) | np.isnan(x2))
        if m.sum() < QDAYS:
            return np.nan
        Xr = np.column_stack([np.ones(m.sum()), x1[m]])
        Xu = np.column_stack([np.ones(m.sum()), x1[m], x2[m]])
        try:
            br = np.linalg.lstsq(Xr, y[m], rcond=None)[0]
            bu = np.linalg.lstsq(Xu, y[m], rcond=None)[0]
            rss_r = ((y[m] - Xr @ br) ** 2).sum()
            rss_u = ((y[m] - Xu @ bu) ** 2).sum()
            return float((rss_r - rss_u) / rss_r) if rss_r > 0 else np.nan
        except Exception:
            return np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _gc(combined[i - YDAYS + 1:i + 1])
    return out.diff().diff().diff()

def f39_vclu_384_corr_sigma5_sigma252_at_lag_max_252d_d3(close: pd.Series) -> pd.Series:
    """Max corr(σ_5, σ_252.shift(k)) for k∈{-21..21} over 252d — strongest cross-scale lead-lag corr."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    combined = pd.concat([s5, s252], axis=1).values

    def _maxc(arr):
        a, b = (arr[:, 0], arr[:, 1])
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = (a[m], b[m])
        best = -np.inf
        for k in range(-MDAYS, MDAYS + 1):
            if k == 0:
                c = np.corrcoef(a, b)[0, 1]
            elif k > 0:
                if len(a) <= k:
                    continue
                c = np.corrcoef(a[k:], b[:-k])[0, 1]
            else:
                if len(a) <= -k:
                    continue
                c = np.corrcoef(a[:k], b[-k:])[0, 1]
            if np.isfinite(c) and c > best:
                best = c
        return float(best) if best > -np.inf else np.nan
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _maxc(combined[i - YDAYS + 1:i + 1])
    return out.diff().diff().diff()

def f39_vclu_385_coherence_sigma5_sigma63_mid_band_252d_d3(close: pd.Series) -> pd.Series:
    """Squared coherence of σ_5 vs σ_63 in mid-freq band [1/30, 1/10 cyc/bar] over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s63 = _rolling_sigma(r, QDAYS)
    combined = pd.concat([s5, s63], axis=1).values

    def _coh(arr):
        a, b = (arr[:, 0], arr[:, 1])
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = (a[m], b[m])
        n = len(a)
        fa = np.fft.rfft(a - a.mean())
        fb = np.fft.rfft(b - b.mean())
        lo = max(int(n / 30), 1)
        hi = max(int(n / 10), 2)
        Cxy = fa[lo:hi] * np.conjugate(fb[lo:hi])
        Pxx = np.abs(fa[lo:hi]) ** 2
        Pyy = np.abs(fb[lo:hi]) ** 2
        if Pxx.sum() == 0 or Pyy.sum() == 0:
            return np.nan
        coh = np.abs(Cxy) ** 2 / (Pxx * Pyy + 1e-12)
        return float(coh.mean())
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _coh(combined[i - YDAYS + 1:i + 1])
    return out.diff().diff().diff()

def f39_vclu_386_coherence_sigma21_sigma252_low_band_252d_d3(close: pd.Series) -> pd.Series:
    """Squared coherence of σ_21 vs σ_252 in low-freq band [0, 1/63 cyc/bar] over 252d."""
    r = _log_ret(close)
    s21 = _rolling_sigma(r, MDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    combined = pd.concat([s21, s252], axis=1).values

    def _coh(arr):
        a, b = (arr[:, 0], arr[:, 1])
        m = ~(np.isnan(a) | np.isnan(b))
        if m.sum() < QDAYS:
            return np.nan
        a, b = (a[m], b[m])
        n = len(a)
        fa = np.fft.rfft(a - a.mean())
        fb = np.fft.rfft(b - b.mean())
        cutoff = max(int(n / QDAYS), 2)
        Cxy = fa[:cutoff] * np.conjugate(fb[:cutoff])
        Pxx = np.abs(fa[:cutoff]) ** 2
        Pyy = np.abs(fb[:cutoff]) ** 2
        coh = np.abs(Cxy) ** 2 / (Pxx * Pyy + 1e-12)
        return float(coh.mean())
    out = pd.Series(np.nan, index=close.index)
    for i in range(YDAYS, len(combined)):
        out.iloc[i] = _coh(combined[i - YDAYS + 1:i + 1])
    return out.diff().diff().diff()

def f39_vclu_387_cross_bicoherence_sigma5_sigma21_252d_d3(close: pd.Series) -> pd.Series:
    """Cross-bicoherence proxy: corr((σ_5 - mean)·(σ_21 - mean)² , (σ_21 - mean)) over 252d (3rd-moment-style)."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    cross = (s5 - s5.rolling(YDAYS, min_periods=QDAYS).mean()) * (s21 - s21.rolling(YDAYS, min_periods=QDAYS).mean()) ** 2
    return cross.rolling(YDAYS, min_periods=QDAYS).corr(s21).diff().diff().diff()

def f39_vclu_388_cascade_sigma5_then_sigma21_count_252d_d3(close: pd.Series) -> pd.Series:
    """σ_5 spike (>252d-p95) followed within 5d by σ_21 spike (>252d-p95), count over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    p5 = s5.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    p21 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    s5_lag = s5.shift(1).rolling(WDAYS, min_periods=1).max() > p5.rolling(WDAYS, min_periods=1).max()
    return (s5_lag & (s21 > p21)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_389_cascade_sigma252_trend_down_count_252d_d3(close: pd.Series) -> pd.Series:
    """σ_252 trend down preceding σ_21 trend down: slope(σ_252,21d)<0 AND slope(σ_21,21d)<0, count over 252d."""
    r = _log_ret(close)
    sl252 = _rolling_slope(_rolling_sigma(r, YDAYS), MDAYS)
    sl21 = _rolling_slope(_rolling_sigma(r, MDAYS), MDAYS)
    return ((sl252 < 0) & (sl21 < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_390_parkinson_rel_gap_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|Parkinson σ² − close-to-close σ²| / σ²(c2c) over 252d — relative gap."""
    pk2 = _parkinson(high, low, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    return _safe_div((pk2 - c2c2).abs().rolling(YDAYS, min_periods=QDAYS).mean(), c2c2.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f39_vclu_391_gk_minus_c2c_var_gap_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass σ² − close-to-close σ² over 252d (vol-info gap)."""
    gk2 = _gk(high, low, open, close, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    return (gk2 - c2c2).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_392_yz_minus_c2c_var_gap_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang σ² − close-to-close σ² over 252d (combined overnight+intraday gap)."""
    yz2 = _yz(open, high, low, close, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    return (yz2 - c2c2).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_393_rs_minus_c2c_var_gap_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell σ² − close-to-close σ² over 252d (drift-independent vol gap)."""
    rs2 = _rs(high, low, open, close, MDAYS) ** 2
    c2c2 = _rolling_sigma(_log_ret(close), MDAYS) ** 2
    return (rs2 - c2c2).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_394_estimator_dispersion_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range of σ-estimators (max − min across {Parkinson, GK, YZ, RS, c2c}) at each bar, mean over 252d."""
    pk = _parkinson(high, low, MDAYS)
    gk = _gk(high, low, open, close, MDAYS)
    yz = _yz(open, high, low, close, MDAYS)
    rs = _rs(high, low, open, close, MDAYS)
    c2c = _rolling_sigma(_log_ret(close), MDAYS)
    stacked = pd.concat([pk, gk, yz, rs, c2c], axis=1)
    return (stacked.max(axis=1) - stacked.min(axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_395_sigma_doubling_count_63d_d3(close: pd.Series) -> pd.Series:
    """σ_21_t+1 / σ_21_t > 2 (σ-doubling) events count over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    doubled = (s > 2 * s.shift(1)).astype(float)
    return doubled.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f39_vclu_396_sigma_tripling_count_252d_d3(close: pd.Series) -> pd.Series:
    """σ_21_t+1 / σ_21_t > 3 (σ-tripling) events count over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s > 3 * s.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_397_sigma_halving_count_63d_d3(close: pd.Series) -> pd.Series:
    """σ_21_t+1 / σ_21_t < 0.5 (σ-halving collapses) events count over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s < 0.5 * s.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f39_vclu_398_mean_dsigma_on_doubling_days_252d_d3(close: pd.Series) -> pd.Series:
    """Mean Δσ_21 on σ-doubling days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    doubled = s > 2 * s.shift(1)
    return s.diff().where(doubled, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_399_mean_post_dsigma_spike_return_252d_d3(close: pd.Series) -> pd.Series:
    """Mean next-bar log-return after a Δσ_21 > 2σ-of-Δσ (vol-shock) day, over 252d (causal)."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    ds = s.diff()
    sigma_of_ds = ds.rolling(MDAYS, min_periods=WDAYS).std()
    shock_lag = ds.shift(1) > 2 * sigma_of_ds.shift(1)
    return r.where(shock_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_400_skew_returns_high_sigma_regime_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of r restricted to high-σ regime (σ_21 > 252d p75) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return r.where(s > p75, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f39_vclu_401_skew_returns_low_sigma_regime_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of r restricted to low-σ regime (σ_21 < 252d p25) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return r.where(s < p25, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f39_vclu_402_kurt_evolution_21d_vs_252d_d3(close: pd.Series) -> pd.Series:
    """kurt(r, 21d) − kurt(r, 252d) — tail-evolution direction (short-vs-long horizon)."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=WDAYS).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff().diff()

def f39_vclu_403_cond_skew_vol_up_day_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of r restricted to σ-up bars (σ_21 > σ_21.shift(1)) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    rising = s.diff() > 0
    return r.where(rising, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f39_vclu_404_cond_skew_vol_down_day_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of r restricted to σ-down bars over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    falling = s.diff() < 0
    return r.where(falling, np.nan).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f39_vclu_405_bpv_over_rv_5d_d3(close: pd.Series) -> pd.Series:
    """BPV / RV ratio at 5d (very-short-horizon jump fraction)."""
    r = _log_ret(close)
    pr = r.abs() * r.abs().shift(1)
    bpv = np.pi / 2.0 * pr.rolling(WDAYS, min_periods=2).sum()
    rv = (r ** 2).rolling(WDAYS, min_periods=2).sum()
    return _safe_div(bpv, rv).diff().diff().diff()

def f39_vclu_406_bpv_over_rv_21d_d3(close: pd.Series) -> pd.Series:
    """BPV / RV ratio at 21d (short-horizon)."""
    r = _log_ret(close)
    pr = r.abs() * r.abs().shift(1)
    bpv = np.pi / 2.0 * pr.rolling(MDAYS, min_periods=WDAYS).sum()
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(bpv, rv).diff().diff().diff()

def f39_vclu_407_bpv_over_rv_252d_d3(close: pd.Series) -> pd.Series:
    """BPV / RV ratio at 252d (annual)."""
    r = _log_ret(close)
    pr = r.abs() * r.abs().shift(1)
    bpv = np.pi / 2.0 * pr.rolling(YDAYS, min_periods=QDAYS).sum()
    rv = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(bpv, rv).diff().diff().diff()

def f39_vclu_408_jump_frac_short_horizon_5d_d3(close: pd.Series) -> pd.Series:
    """1 − BPV/RV at 5d — very-short-horizon jump-variance fraction."""
    r = _log_ret(close)
    pr = r.abs() * r.abs().shift(1)
    bpv = np.pi / 2.0 * pr.rolling(WDAYS, min_periods=2).sum()
    rv = (r ** 2).rolling(WDAYS, min_periods=2).sum()
    return (1.0 - _safe_div(bpv, rv)).clip(lower=0.0).diff().diff().diff()

def f39_vclu_409_arch_lm_lag1_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM at lag 1: rolling 252d R² from r²_t on r²_{t-1}."""
    r2 = _log_ret(close) ** 2
    c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(1))
    return (YDAYS * c ** 2).diff().diff().diff()

def f39_vclu_410_mcleod_li_q5_252d_d3(close: pd.Series) -> pd.Series:
    """McLeod-Li statistic at lags 1..5 over 252d."""
    r2 = _log_ret(close) ** 2
    return _ljung_box(r2, WDAYS, YDAYS, QDAYS).diff().diff().diff()

def f39_vclu_411_mcleod_li_q10_252d_d3(close: pd.Series) -> pd.Series:
    """McLeod-Li statistic at lags 1..10 over 252d."""
    r2 = _log_ret(close) ** 2
    return _ljung_box(r2, 10, YDAYS, QDAYS).diff().diff().diff()

def f39_vclu_412_arch_lm_lag21_252d_d3(close: pd.Series) -> pd.Series:
    """ARCH-LM-like at lag 21: rolling 252d R² of r²_t on r²_{t-21}."""
    r2 = _log_ret(close) ** 2
    c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(MDAYS))
    return (YDAYS * c ** 2).diff().diff().diff()

def f39_vclu_413_rsq_acf_aggregate_252d_d3(close: pd.Series) -> pd.Series:
    """Sum of squared autocorrelations of r² at lags 1..21 over 252d."""
    r2 = _log_ret(close) ** 2
    out = pd.Series(0.0, index=close.index)
    for k in range(1, MDAYS + 1):
        c = r2.rolling(YDAYS, min_periods=QDAYS).corr(r2.shift(k))
        out = out + c ** 2
    return out.diff().diff().diff()

def f39_vclu_414_sigma_spike_preceding_252d_high_count_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of σ_21 > 252d-p90 in 5 bars before 252d-high events, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    spike = s > p90
    spike_in_prev5 = spike.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (spike_in_prev5 & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_415_sigma_in_lowest_decile_at_252d_high_count_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count: σ_21 in lowest decile (≤252d-p10) AND close at 252d-high, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    lo = s <= p10
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (lo & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_416_sigma_expansion_post_252d_high_ratio_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean σ_21 in 21 bars after 252d-high events / σ_21 21d before, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_high_lag = high.shift(MDAYS) >= high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    ratio = _safe_div(s, s.shift(MDAYS * 2))
    return ratio.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_417_sigma_cv_post_peak_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """CV of σ_21 in 21 bars after a 252d-high event, mean over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_high_lag = high.shift(MDAYS) >= high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    post_mean = s.rolling(MDAYS, min_periods=WDAYS).mean()
    post_std = s.rolling(MDAYS, min_periods=WDAYS).std()
    cv = _safe_div(post_std, post_mean)
    return cv.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_418_mean_sigma_pre_252d_high_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean σ_21 in the 21 bars before a 252d-high event, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    pre_mean = s.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    return pre_mean.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_419_sigma_5d_accel_after_252d_high_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (σ_5_t − σ_5_t-5) on bars 5 days after 252d-high events, over 252d."""
    s5 = _rolling_sigma(_log_ret(close), WDAYS)
    accel = s5 - s5.shift(WDAYS)
    new_high_lag = high.shift(WDAYS) >= high.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    return accel.where(new_high_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_420_bar_bar_sigma_change_at_252d_high_252d_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean Δσ_21 at 252d-high events over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return s.diff().where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f39_vclu_421_mean_range_estimators_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (Parkinson, GK, YZ, RS) at 21d — robust ensemble σ estimate."""
    pk = _parkinson(high, low, MDAYS)
    gk = _gk(high, low, open, close, MDAYS)
    yz = _yz(open, high, low, close, MDAYS)
    rs = _rs(high, low, open, close, MDAYS)
    return pd.concat([pk, gk, yz, rs], axis=1).mean(axis=1).diff().diff().diff()

def f39_vclu_422_median_range_estimators_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median across range estimators at 21d (robust to one-off estimator anomalies)."""
    pk = _parkinson(high, low, MDAYS)
    gk = _gk(high, low, open, close, MDAYS)
    yz = _yz(open, high, low, close, MDAYS)
    rs = _rs(high, low, open, close, MDAYS)
    return pd.concat([pk, gk, yz, rs], axis=1).median(axis=1).diff().diff().diff()

def f39_vclu_423_min_range_estimators_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min across range estimators at 21d (compression view)."""
    pk = _parkinson(high, low, MDAYS)
    gk = _gk(high, low, open, close, MDAYS)
    yz = _yz(open, high, low, close, MDAYS)
    rs = _rs(high, low, open, close, MDAYS)
    return pd.concat([pk, gk, yz, rs], axis=1).min(axis=1).diff().diff().diff()

def f39_vclu_424_max_range_estimators_21d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max across range estimators at 21d (worst-case vol view)."""
    pk = _parkinson(high, low, MDAYS)
    gk = _gk(high, low, open, close, MDAYS)
    yz = _yz(open, high, low, close, MDAYS)
    rs = _rs(high, low, open, close, MDAYS)
    return pd.concat([pk, gk, yz, rs], axis=1).max(axis=1).diff().diff().diff()

def f39_vclu_425_sigma_outlier_count_p99_252d_d3(close: pd.Series) -> pd.Series:
    """Count of σ_21 > p99 of own past 252d, summed 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p99 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (s > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_426_consecutive_sigma_outlier_days_252d_d3(close: pd.Series) -> pd.Series:
    """Count of consecutive-bar σ_21 > p99 events over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p99 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    outlier = s > p99
    consec = (outlier & outlier.shift(1).fillna(False)).astype(float)
    return consec.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_427_persistent_top_quartile_sigma_60d_d3(close: pd.Series) -> pd.Series:
    """Indicator: σ_21 in top quartile for >30 of last 60 days (persistent high-vol regime)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    days_in_top = (s > p75).astype(float).rolling(60, min_periods=20).sum()
    return (days_in_top > 30).astype(float).diff().diff().diff()

def f39_vclu_428_vol_freeze_indicator_21d_d3(close: pd.Series) -> pd.Series:
    """Vol "freeze": |max σ_21 − min σ_21| / mean σ_21 < 0.05 over 21d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rng = s.rolling(MDAYS, min_periods=WDAYS).max() - s.rolling(MDAYS, min_periods=WDAYS).min()
    m = s.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(rng, m) < 0.05).astype(float).diff().diff().diff()

def f39_vclu_429_sigma_jump_count_pct_change_63d_d3(close: pd.Series) -> pd.Series:
    """Count of |Δσ_21 / σ_21.shift(1)| > 0.20 (vol-jumps) over 63d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    pct = _safe_div(s.diff().abs(), s.shift(1))
    return (pct > 0.2).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f39_vclu_430_sigma_pos_top10_vs_bot10_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """σ on top-10% positive r days vs σ on bottom-10% negative r days, over 252d (asymmetric tail-vol)."""
    r = _log_ret(close)
    p_pos = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    p_neg = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    pos_sig = _rolling_sigma(r.where(r > p_pos, np.nan), YDAYS)
    neg_sig = _rolling_sigma(r.where(r < p_neg, np.nan), YDAYS)
    return _safe_div(pos_sig, neg_sig).diff().diff().diff()

def f39_vclu_431_symmetric_tail_sigma_252d_d3(close: pd.Series) -> pd.Series:
    """σ of r restricted to |r| > 252d-p90 over 252d — symmetric extreme-tail σ."""
    r = _log_ret(close)
    p90_abs = r.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return r.where(r.abs() > p90_abs, np.nan).rolling(YDAYS, min_periods=QDAYS).std().diff().diff().diff()

def f39_vclu_432_weekly_over_daily_sigma_252d_d3(close: pd.Series) -> pd.Series:
    """σ(weekly returns) / σ(daily returns) over 252d — vol-decomposition ratio."""
    rw = _safe_log(close).diff(WDAYS)
    rd = _log_ret(close)
    return _safe_div(rw.rolling(YDAYS, min_periods=QDAYS).std() / np.sqrt(WDAYS), rd.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f39_vclu_433_monthly_over_weekly_sigma_252d_d3(close: pd.Series) -> pd.Series:
    """σ(monthly returns) / σ(weekly returns) over 252d."""
    rm = _safe_log(close).diff(MDAYS)
    rw = _safe_log(close).diff(WDAYS)
    return _safe_div(rm.rolling(YDAYS, min_periods=QDAYS).std() / np.sqrt(MDAYS / WDAYS), rw.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f39_vclu_434_cross_vol_stability_252d_d3(close: pd.Series) -> pd.Series:
    """1 − rolling std of (σ_21/σ_5) over 252d — stability of vol-ratio."""
    r = _log_ret(close)
    ratio = _safe_div(_rolling_sigma(r, MDAYS), _rolling_sigma(r, WDAYS))
    return (1.0 - ratio.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f39_vclu_435_sigma252_over_1260d_min_d3(close: pd.Series) -> pd.Series:
    """σ_252 / min(σ_252, past 1260d) — multi-year vol compression release."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return _safe_div(s, s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).min()).diff().diff().diff()

def f39_vclu_436_sigma252_over_1260d_max_d3(close: pd.Series) -> pd.Series:
    """σ_252 / max(σ_252, past 1260d) — proximity to multi-year vol peak (0..1)."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return _safe_div(s, s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).max()).diff().diff().diff()

def f39_vclu_437_bars_since_sigma21_504d_low_d3(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last printed its trailing-504d minimum."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mn = s.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    arr = (s <= mn * 1.001).astype(int).fillna(0).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, v in enumerate(arr):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index).diff().diff().diff()

def f39_vclu_438_bars_since_sigma21_504d_high_d3(close: pd.Series) -> pd.Series:
    """Bars since σ_21 last printed its trailing-504d maximum."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mx = s.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    arr = (s >= mx * 0.999).astype(int).fillna(0).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, v in enumerate(arr):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index).diff().diff().diff()

def f39_vclu_439_long_vol_drift_sign_504d_d3(close: pd.Series) -> pd.Series:
    """Sign of 504d slope of σ_252 — long-vol-trend direction."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return np.sign(_rolling_slope(s, DDAYS_2Y)).diff().diff().diff()

def f39_vclu_440_sigma21_curent_half_vs_prior_half_252d_d3(close: pd.Series) -> pd.Series:
    """Mean σ_21 in last 126d / mean σ_21 in prior 126d — semi-annual regime shift."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    recent = s.rolling(126, min_periods=63).mean()
    prior = s.shift(126).rolling(126, min_periods=63).mean()
    return _safe_div(recent, prior).diff().diff().diff()

def f39_vclu_441_sigma21_quartile_transitions_252d_d3(close: pd.Series) -> pd.Series:
    """Count of σ_21 transitions between quartiles (Q1↔Q2↔Q3↔Q4) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _q(w):
        v = w[-1]
        if np.isnan(v):
            return np.nan
        q25, q50, q75 = np.quantile(w[~np.isnan(w)], [0.25, 0.5, 0.75])
        if v < q25:
            return 1
        if v < q50:
            return 2
        if v < q75:
            return 3
        return 4
    q = s.rolling(YDAYS, min_periods=QDAYS).apply(_q, raw=True)
    transitions = (q.diff() != 0) & q.notna() & q.shift(1).notna()
    return transitions.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_442_sigma_rank_median_crossings_252d_d3(close: pd.Series) -> pd.Series:
    """Count of σ-rank crossings of 0.5 within trailing 252d (regime crossings via rank)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rk = s.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    above = (rk > 0.5).astype(float)
    return above.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f39_vclu_443_stable_sigma_run_max_252d_d3(close: pd.Series) -> pd.Series:
    """Max run-length of σ_21 staying in [p25, p75] within 252d (stable regime persistence)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    stable = ((s >= p25) & (s <= p75)).astype(float).fillna(0.0)

    def _run(w):
        m = 0
        c = 0
        for v in w:
            if v > 0.5:
                c += 1
                m = c if c > m else m
            else:
                c = 0
        return float(m)
    return stable.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True).diff().diff().diff()

def f39_vclu_444_sigma_of_delta_sigma_252d_d3(close: pd.Series) -> pd.Series:
    """Std of Δσ_21 over 252d — vol-of-Δσ (different from σ-of-σ; this is change-driven)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).std().diff().diff().diff()

def f39_vclu_445_rv_bootstrap_p90_252d_d3(close: pd.Series) -> pd.Series:
    """Rolling 252d p90 of RV(5d) values — realized-vol bootstrap percentile."""
    r2 = _log_ret(close) ** 2
    rv5 = r2.rolling(WDAYS, min_periods=2).sum()
    return rv5.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).diff().diff().diff()

def f39_vclu_446_sigma_stability_score_252d_d3(close: pd.Series) -> pd.Series:
    """1 − CV(σ_21) over 252d (higher = more stable)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (1.0 - _safe_div(s.rolling(YDAYS, min_periods=QDAYS).std(), s.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()

def f39_vclu_447_ewma21_minus_ewma63_sigma_signal_d3(close: pd.Series) -> pd.Series:
    """EWMA-21d − EWMA-63d of σ_21 (MACD-style signal for vol)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s.ewm(span=MDAYS, min_periods=MDAYS, adjust=False).mean() - s.ewm(span=QDAYS, min_periods=QDAYS, adjust=False).mean()).diff().diff().diff()

def f39_vclu_448_ema21_sigma_slope_21d_d3(close: pd.Series) -> pd.Series:
    """Rolling 21d slope of EMA-21 of σ_21 — vol-trend velocity."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    ema = s.ewm(span=MDAYS, min_periods=MDAYS, adjust=False).mean()
    return _rolling_slope(ema, MDAYS).diff().diff().diff()

def f39_vclu_449_sigma_trend_strength_252d_d3(close: pd.Series) -> pd.Series:
    """|σ-trend slope| / mean σ over 252d (normalized trend strength)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sl = _rolling_slope(s, YDAYS)
    return _safe_div(sl.abs(), s.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()

def f39_vclu_450_sigma_outlier_z_range_21d_d3(close: pd.Series) -> pd.Series:
    """(max σ_21 − min σ_21) over 21d normalized by 252d std of σ_21 — outlier-z range."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rng = s.rolling(MDAYS, min_periods=WDAYS).max() - s.rolling(MDAYS, min_periods=WDAYS).min()
    return _safe_div(rng, s.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()
VOLATILITY_CLUSTERING_D3_REGISTRY_376_450 = {'f39_vclu_376_cond_sigma_top_quartile_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_376_cond_sigma_top_quartile_volume_252d_d3}, 'f39_vclu_377_cond_sigma_bottom_quartile_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_377_cond_sigma_bottom_quartile_volume_252d_d3}, 'f39_vclu_378_vol_sigma_co_spike_count_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_378_vol_sigma_co_spike_count_252d_d3}, 'f39_vclu_379_vol_sigma_divergence_count_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_379_vol_sigma_divergence_count_252d_d3}, 'f39_vclu_380_vol_sigma_corr_high_volume_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_380_vol_sigma_corr_high_volume_252d_d3}, 'f39_vclu_381_volume_leads_sigma_lag5_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_381_volume_leads_sigma_lag5_252d_d3}, 'f39_vclu_382_sigma_leads_volume_lag5_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_382_sigma_leads_volume_lag5_252d_d3}, 'f39_vclu_383_granger_volume_to_sigma_252d_d3': {'inputs': ['close', 'volume'], 'func': f39_vclu_383_granger_volume_to_sigma_252d_d3}, 'f39_vclu_384_corr_sigma5_sigma252_at_lag_max_252d_d3': {'inputs': ['close'], 'func': f39_vclu_384_corr_sigma5_sigma252_at_lag_max_252d_d3}, 'f39_vclu_385_coherence_sigma5_sigma63_mid_band_252d_d3': {'inputs': ['close'], 'func': f39_vclu_385_coherence_sigma5_sigma63_mid_band_252d_d3}, 'f39_vclu_386_coherence_sigma21_sigma252_low_band_252d_d3': {'inputs': ['close'], 'func': f39_vclu_386_coherence_sigma21_sigma252_low_band_252d_d3}, 'f39_vclu_387_cross_bicoherence_sigma5_sigma21_252d_d3': {'inputs': ['close'], 'func': f39_vclu_387_cross_bicoherence_sigma5_sigma21_252d_d3}, 'f39_vclu_388_cascade_sigma5_then_sigma21_count_252d_d3': {'inputs': ['close'], 'func': f39_vclu_388_cascade_sigma5_then_sigma21_count_252d_d3}, 'f39_vclu_389_cascade_sigma252_trend_down_count_252d_d3': {'inputs': ['close'], 'func': f39_vclu_389_cascade_sigma252_trend_down_count_252d_d3}, 'f39_vclu_390_parkinson_rel_gap_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f39_vclu_390_parkinson_rel_gap_252d_d3}, 'f39_vclu_391_gk_minus_c2c_var_gap_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_391_gk_minus_c2c_var_gap_252d_d3}, 'f39_vclu_392_yz_minus_c2c_var_gap_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_392_yz_minus_c2c_var_gap_252d_d3}, 'f39_vclu_393_rs_minus_c2c_var_gap_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_393_rs_minus_c2c_var_gap_252d_d3}, 'f39_vclu_394_estimator_dispersion_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_394_estimator_dispersion_252d_d3}, 'f39_vclu_395_sigma_doubling_count_63d_d3': {'inputs': ['close'], 'func': f39_vclu_395_sigma_doubling_count_63d_d3}, 'f39_vclu_396_sigma_tripling_count_252d_d3': {'inputs': ['close'], 'func': f39_vclu_396_sigma_tripling_count_252d_d3}, 'f39_vclu_397_sigma_halving_count_63d_d3': {'inputs': ['close'], 'func': f39_vclu_397_sigma_halving_count_63d_d3}, 'f39_vclu_398_mean_dsigma_on_doubling_days_252d_d3': {'inputs': ['close'], 'func': f39_vclu_398_mean_dsigma_on_doubling_days_252d_d3}, 'f39_vclu_399_mean_post_dsigma_spike_return_252d_d3': {'inputs': ['close'], 'func': f39_vclu_399_mean_post_dsigma_spike_return_252d_d3}, 'f39_vclu_400_skew_returns_high_sigma_regime_252d_d3': {'inputs': ['close'], 'func': f39_vclu_400_skew_returns_high_sigma_regime_252d_d3}, 'f39_vclu_401_skew_returns_low_sigma_regime_252d_d3': {'inputs': ['close'], 'func': f39_vclu_401_skew_returns_low_sigma_regime_252d_d3}, 'f39_vclu_402_kurt_evolution_21d_vs_252d_d3': {'inputs': ['close'], 'func': f39_vclu_402_kurt_evolution_21d_vs_252d_d3}, 'f39_vclu_403_cond_skew_vol_up_day_252d_d3': {'inputs': ['close'], 'func': f39_vclu_403_cond_skew_vol_up_day_252d_d3}, 'f39_vclu_404_cond_skew_vol_down_day_252d_d3': {'inputs': ['close'], 'func': f39_vclu_404_cond_skew_vol_down_day_252d_d3}, 'f39_vclu_405_bpv_over_rv_5d_d3': {'inputs': ['close'], 'func': f39_vclu_405_bpv_over_rv_5d_d3}, 'f39_vclu_406_bpv_over_rv_21d_d3': {'inputs': ['close'], 'func': f39_vclu_406_bpv_over_rv_21d_d3}, 'f39_vclu_407_bpv_over_rv_252d_d3': {'inputs': ['close'], 'func': f39_vclu_407_bpv_over_rv_252d_d3}, 'f39_vclu_408_jump_frac_short_horizon_5d_d3': {'inputs': ['close'], 'func': f39_vclu_408_jump_frac_short_horizon_5d_d3}, 'f39_vclu_409_arch_lm_lag1_252d_d3': {'inputs': ['close'], 'func': f39_vclu_409_arch_lm_lag1_252d_d3}, 'f39_vclu_410_mcleod_li_q5_252d_d3': {'inputs': ['close'], 'func': f39_vclu_410_mcleod_li_q5_252d_d3}, 'f39_vclu_411_mcleod_li_q10_252d_d3': {'inputs': ['close'], 'func': f39_vclu_411_mcleod_li_q10_252d_d3}, 'f39_vclu_412_arch_lm_lag21_252d_d3': {'inputs': ['close'], 'func': f39_vclu_412_arch_lm_lag21_252d_d3}, 'f39_vclu_413_rsq_acf_aggregate_252d_d3': {'inputs': ['close'], 'func': f39_vclu_413_rsq_acf_aggregate_252d_d3}, 'f39_vclu_414_sigma_spike_preceding_252d_high_count_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_414_sigma_spike_preceding_252d_high_count_d3}, 'f39_vclu_415_sigma_in_lowest_decile_at_252d_high_count_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_415_sigma_in_lowest_decile_at_252d_high_count_d3}, 'f39_vclu_416_sigma_expansion_post_252d_high_ratio_252d_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_416_sigma_expansion_post_252d_high_ratio_252d_d3}, 'f39_vclu_417_sigma_cv_post_peak_252d_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_417_sigma_cv_post_peak_252d_d3}, 'f39_vclu_418_mean_sigma_pre_252d_high_252d_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_418_mean_sigma_pre_252d_high_252d_d3}, 'f39_vclu_419_sigma_5d_accel_after_252d_high_252d_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_419_sigma_5d_accel_after_252d_high_252d_d3}, 'f39_vclu_420_bar_bar_sigma_change_at_252d_high_252d_d3': {'inputs': ['close', 'high'], 'func': f39_vclu_420_bar_bar_sigma_change_at_252d_high_252d_d3}, 'f39_vclu_421_mean_range_estimators_21d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_421_mean_range_estimators_21d_d3}, 'f39_vclu_422_median_range_estimators_21d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_422_median_range_estimators_21d_d3}, 'f39_vclu_423_min_range_estimators_21d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_423_min_range_estimators_21d_d3}, 'f39_vclu_424_max_range_estimators_21d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f39_vclu_424_max_range_estimators_21d_d3}, 'f39_vclu_425_sigma_outlier_count_p99_252d_d3': {'inputs': ['close'], 'func': f39_vclu_425_sigma_outlier_count_p99_252d_d3}, 'f39_vclu_426_consecutive_sigma_outlier_days_252d_d3': {'inputs': ['close'], 'func': f39_vclu_426_consecutive_sigma_outlier_days_252d_d3}, 'f39_vclu_427_persistent_top_quartile_sigma_60d_d3': {'inputs': ['close'], 'func': f39_vclu_427_persistent_top_quartile_sigma_60d_d3}, 'f39_vclu_428_vol_freeze_indicator_21d_d3': {'inputs': ['close'], 'func': f39_vclu_428_vol_freeze_indicator_21d_d3}, 'f39_vclu_429_sigma_jump_count_pct_change_63d_d3': {'inputs': ['close'], 'func': f39_vclu_429_sigma_jump_count_pct_change_63d_d3}, 'f39_vclu_430_sigma_pos_top10_vs_bot10_ratio_252d_d3': {'inputs': ['close'], 'func': f39_vclu_430_sigma_pos_top10_vs_bot10_ratio_252d_d3}, 'f39_vclu_431_symmetric_tail_sigma_252d_d3': {'inputs': ['close'], 'func': f39_vclu_431_symmetric_tail_sigma_252d_d3}, 'f39_vclu_432_weekly_over_daily_sigma_252d_d3': {'inputs': ['close'], 'func': f39_vclu_432_weekly_over_daily_sigma_252d_d3}, 'f39_vclu_433_monthly_over_weekly_sigma_252d_d3': {'inputs': ['close'], 'func': f39_vclu_433_monthly_over_weekly_sigma_252d_d3}, 'f39_vclu_434_cross_vol_stability_252d_d3': {'inputs': ['close'], 'func': f39_vclu_434_cross_vol_stability_252d_d3}, 'f39_vclu_435_sigma252_over_1260d_min_d3': {'inputs': ['close'], 'func': f39_vclu_435_sigma252_over_1260d_min_d3}, 'f39_vclu_436_sigma252_over_1260d_max_d3': {'inputs': ['close'], 'func': f39_vclu_436_sigma252_over_1260d_max_d3}, 'f39_vclu_437_bars_since_sigma21_504d_low_d3': {'inputs': ['close'], 'func': f39_vclu_437_bars_since_sigma21_504d_low_d3}, 'f39_vclu_438_bars_since_sigma21_504d_high_d3': {'inputs': ['close'], 'func': f39_vclu_438_bars_since_sigma21_504d_high_d3}, 'f39_vclu_439_long_vol_drift_sign_504d_d3': {'inputs': ['close'], 'func': f39_vclu_439_long_vol_drift_sign_504d_d3}, 'f39_vclu_440_sigma21_curent_half_vs_prior_half_252d_d3': {'inputs': ['close'], 'func': f39_vclu_440_sigma21_curent_half_vs_prior_half_252d_d3}, 'f39_vclu_441_sigma21_quartile_transitions_252d_d3': {'inputs': ['close'], 'func': f39_vclu_441_sigma21_quartile_transitions_252d_d3}, 'f39_vclu_442_sigma_rank_median_crossings_252d_d3': {'inputs': ['close'], 'func': f39_vclu_442_sigma_rank_median_crossings_252d_d3}, 'f39_vclu_443_stable_sigma_run_max_252d_d3': {'inputs': ['close'], 'func': f39_vclu_443_stable_sigma_run_max_252d_d3}, 'f39_vclu_444_sigma_of_delta_sigma_252d_d3': {'inputs': ['close'], 'func': f39_vclu_444_sigma_of_delta_sigma_252d_d3}, 'f39_vclu_445_rv_bootstrap_p90_252d_d3': {'inputs': ['close'], 'func': f39_vclu_445_rv_bootstrap_p90_252d_d3}, 'f39_vclu_446_sigma_stability_score_252d_d3': {'inputs': ['close'], 'func': f39_vclu_446_sigma_stability_score_252d_d3}, 'f39_vclu_447_ewma21_minus_ewma63_sigma_signal_d3': {'inputs': ['close'], 'func': f39_vclu_447_ewma21_minus_ewma63_sigma_signal_d3}, 'f39_vclu_448_ema21_sigma_slope_21d_d3': {'inputs': ['close'], 'func': f39_vclu_448_ema21_sigma_slope_21d_d3}, 'f39_vclu_449_sigma_trend_strength_252d_d3': {'inputs': ['close'], 'func': f39_vclu_449_sigma_trend_strength_252d_d3}, 'f39_vclu_450_sigma_outlier_z_range_21d_d3': {'inputs': ['close'], 'func': f39_vclu_450_sigma_outlier_z_range_21d_d3}}