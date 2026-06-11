"""parabolic_blowoff_signature d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d2__076_150.py. Each feature
encodes a *different concept* in the parabolic / blow-off / curvature theme:
higher-order polynomial fits, advanced goodness-of-fit, LPPL proxies, regime-conditional
curvature, transition events, phase-space embedding, wavelets, robust estimators, and
narrow parabolic-internal composites.

Differentiates from 1a `f37_bpsg_*` family by focusing on aspects bpsg does NOT cover:
higher-order polynomials, model-selection criteria, LPPL frequency/phase, conditional
regimes, phase-space embedding, robust estimators.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


# ---------- polynomial-fit helpers (raw=True window callables) ----------

def _poly_coef(w, deg, idx):
    """Return polyfit coefficient at index `idx` (where coeffs are ordered
    highest-degree-first per numpy convention). NaN-safe + try/except."""
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]
        w = w[valid]
    try:
        c = np.polyfit(x, w, deg)
        return float(c[idx])
    except Exception:
        return np.nan


def _poly_residuals(w, deg):
    """Return residual array (y - yhat); or None on failure."""
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return None
    x = np.arange(len(w), dtype=float)
    yv = w
    if not valid.all():
        x = x[valid]
        yv = w[valid]
    try:
        c = np.polyfit(x, yv, deg)
        yhat = np.polyval(c, x)
        return yv - yhat
    except Exception:
        return None


def _poly_rss(w, deg):
    r = _poly_residuals(w, deg)
    if r is None:
        return np.nan
    return float((r * r).sum())


def _poly_r2(w, deg):
    valid = ~np.isnan(w)
    n = int(valid.sum())
    if n < (deg + 2):
        return np.nan
    yv = w[valid] if not valid.all() else w
    tss = float(((yv - yv.mean()) ** 2).sum())
    if tss <= 0:
        return np.nan
    rss = _poly_rss(w, deg)
    if not np.isfinite(rss):
        return np.nan
    return 1.0 - rss / tss


def _aic_gauss(rss, n, k):
    """AIC for a Gaussian-error model, k = number of fitted parameters."""
    if rss is None or not np.isfinite(rss) or rss <= 0 or n <= 0:
        return np.nan
    return float(n * np.log(rss / n) + 2.0 * k)


def _bic_gauss(rss, n, k):
    if rss is None or not np.isfinite(rss) or rss <= 0 or n <= 0:
        return np.nan
    return float(n * np.log(rss / n) + k * np.log(n))


def _rolling_logclose(close):
    return _safe_log(close)


def f02_pblo_001_cubic_a3_log_close_63d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_002_cubic_a3_log_close_126d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    out = lc.rolling(126, min_periods=42).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_003_cubic_a3_log_close_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_004_cubic_a3_log_close_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=126).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_005_quartic_a4_log_close_126d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 4, 0)
    lc = _safe_log(close)
    out = lc.rolling(126, min_periods=42).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_006_quartic_a4_log_close_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 4, 0)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_007_quartic_a4_log_close_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 4, 0)
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=126).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_008_quintic_a5_log_close_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 5, 0)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_009_quintic_a5_log_close_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 5, 0)
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_010_cubic_a3_sign_change_event_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    c3 = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    sgn = np.sign(c3)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(c3.notna() & c3.shift(1).notna(), np.nan)
    out = flip
    return out.diff().diff()


def f02_pblo_011_dominant_polynomial_degree_bic_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        bics = []
        n = int((~np.isnan(w)).sum())
        if n < 30:
            return np.nan
        for d in (1, 2, 3, 4):
            rss = _poly_rss(w, d)
            bics.append(_bic_gauss(rss, n, d + 1))
        arr = np.array(bics, dtype=float)
        if np.isnan(arr).all():
            return np.nan
        return float(1 + int(np.nanargmin(arr)))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_012_cubic_over_quad_r2_gain_126d_d2(close: pd.Series) -> pd.Series:
    def _fq(w):
        return _poly_r2(w, 2)
    def _fc(w):
        return _poly_r2(w, 3)
    lc = _safe_log(close)
    r2q = lc.rolling(126, min_periods=42).apply(_fq, raw=True)
    r2c = lc.rolling(126, min_periods=42).apply(_fc, raw=True)
    out = r2c - r2q
    return out.diff().diff()


def f02_pblo_013_parab_residual_std_63d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 3:
            return np.nan
        return float(np.nanstd(r, ddof=1))
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_014_parab_residual_std_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 3:
            return np.nan
        return float(np.nanstd(r, ddof=1))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_015_parab_residual_std_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 3:
            return np.nan
        return float(np.nanstd(r, ddof=1))
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_016_aic_quadratic_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        n = int((~np.isnan(w)).sum())
        return _aic_gauss(_poly_rss(w, 2), n, 3)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_017_aic_cubic_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        n = int((~np.isnan(w)).sum())
        return _aic_gauss(_poly_rss(w, 3), n, 4)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_018_bic_quad_minus_cubic_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        n = int((~np.isnan(w)).sum())
        return _bic_gauss(_poly_rss(w, 2), n, 3) - _bic_gauss(_poly_rss(w, 3), n, 4)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_019_bic_quartic_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        n = int((~np.isnan(w)).sum())
        return _bic_gauss(_poly_rss(w, 4), n, 5)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_020_parab_mean_abs_resid_norm_close_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 3:
            return np.nan
        return float(np.nanmean(np.abs(r)))
    lc = _safe_log(close)
    mar = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    out = _safe_div(mar, _safe_log(close).abs().rolling(252, min_periods=84).mean())
    return out.diff().diff()


def f02_pblo_021_parab_durbin_watson_resid_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 5:
            return np.nan
        d = np.diff(r)
        num = float((d * d).sum())
        den = float((r * r).sum())
        if den <= 0:
            return np.nan
        return num / den
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_022_parab_resid_ad_normality_proxy_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 8:
            return np.nan
        rr = r[~np.isnan(r)]
        if rr.size < 8:
            return np.nan
        m = rr.mean(); s = rr.std(ddof=1)
        if s <= 0:
            return np.nan
        z = (rr - m) / s
        # Anderson-Darling A^2 proxy via cumulative deviation
        z_sorted = np.sort(z)
        n = z_sorted.size
        from math import erf, sqrt
        # Standard-normal cdf via vectorized math
        cdf = 0.5 * (1.0 + np.array([erf(v / sqrt(2.0)) for v in z_sorted]))
        cdf = np.clip(cdf, 1e-12, 1.0 - 1e-12)
        i = np.arange(1, n + 1)
        s_val = np.sum((2 * i - 1) * (np.log(cdf) + np.log(1.0 - cdf[::-1])))
        return float(-n - s_val / n)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_023_parab_resid_skew_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        rr = r[~np.isnan(r)]
        if rr.size < 5:
            return np.nan
        m = rr.mean(); s = rr.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((rr - m) / s) ** 3))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_024_parab_resid_kurt_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None:
            return np.nan
        rr = r[~np.isnan(r)]
        if rr.size < 5:
            return np.nan
        m = rr.mean(); s = rr.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((rr - m) / s) ** 4) - 3.0)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_025_lppl_omega_proxy_residual_zcr_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum()
        return float(nz) / float(r.size)
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_026_lppl_omega_proxy_residual_zcr_1260d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum()
        return float(nz) / float(r.size)
    lc = _safe_log(close)
    out = lc.rolling(1260, min_periods=252).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_027_lppl_beta_singularity_strength_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 30:
            return np.nan
        n = r.size
        # Fit log|r_max running| vs log(n-t)
        y = np.abs(r) + 1e-12
        yy = np.log(y)
        xx = np.log(np.arange(n, 0, -1, dtype=float))
        mask = np.isfinite(yy) & np.isfinite(xx)
        if mask.sum() < 10:
            return np.nan
        xv = xx[mask]; yv = yy[mask]
        xm = xv.mean(); ym = yv.mean()
        den = float(((xv - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((xv - xm) * (yv - ym)).sum() / den)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_028_lppl_phi_phase_proxy_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 5:
            return np.nan
        last = r[-1]
        slope = r[-1] - r[-5]
        return float(np.arctan2(slope, last))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_029_lppl_critical_time_confidence_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 10:
            return np.nan
        band = float(np.nanstd(r, ddof=1))
        last = float(r[-1])
        if band <= 0:
            return np.nan
        return last / band
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_030_log_periodic_oscillation_amplitude_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 5:
            return np.nan
        rr = r[~np.isnan(r)]
        if rr.size < 5:
            return np.nan
        return float(np.percentile(rr, 95) - np.percentile(rr, 5))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_031_log_periodic_freq_stability_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum()
        return float(nz) / float(r.size)
    lc = _safe_log(close)
    omega = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    out = omega.rolling(252, min_periods=84).std()
    return out.diff().diff()


def f02_pblo_032_lppl_resid_r2_quad_504d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_r2(w, 2)
    lc = _safe_log(close)
    out = lc.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_033_lppl_bubble_probability_proxy_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r2 = _poly_r2(w, 2)
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20 or not np.isfinite(r2):
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum() / float(r.size)
        return float(r2 * nz)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_034_lppl_omega_harmonic_ratio_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 40:
            return np.nan
        m = r.size // 2
        s1 = np.sign(r[:m]); s2 = np.sign(r[m:])
        z1 = (s1[1:] != s1[:-1]).sum() / float(m)
        z2 = (s2[1:] != s2[:-1]).sum() / float(r.size - m)
        if z1 <= 0:
            return np.nan
        return float(z2 / z1)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_035_lppl_omega_evolution_63d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        sgn = np.sign(r)
        nz = (sgn[1:] != sgn[:-1]).sum()
        return float(nz) / float(r.size)
    lc = _safe_log(close)
    omega = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    out = omega - omega.shift(63)
    return out.diff().diff()


def f02_pblo_036_lppl_phase_entropy_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 10:
            return np.nan
        pos = (r > 0).sum() / float(r.size)
        neg = 1.0 - pos
        p = np.array([pos, neg])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_037_exp_fit_b_logclose_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = _rolling_slope(lc, 252, min_periods=84)
    return out.diff().diff()


def f02_pblo_038_power_law_exp_log_log_126d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 30:
            return np.nan
        x = np.arange(len(w), dtype=float) + 1.0
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        lx = np.log(x); ly = yv
        xm = lx.mean(); ym = ly.mean()
        den = float(((lx - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((lx - xm) * (ly - ym)).sum() / den)
    lc = _safe_log(close)
    out = lc.rolling(126, min_periods=42).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_039_power_law_exp_log_log_756d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 60:
            return np.nan
        x = np.arange(len(w), dtype=float) + 1.0
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        lx = np.log(x); ly = yv
        xm = lx.mean(); ym = ly.mean()
        den = float(((lx - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((lx - xm) * (ly - ym)).sum() / den)
    lc = _safe_log(close)
    out = lc.rolling(756, min_periods=168).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_040_power_law_minus_exp_aic_252d_d2(close: pd.Series) -> pd.Series:
    def _exp_aic(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 10:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        # Linear fit on yv (= log-close) vs x is exponential model on close
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = ((x - xm) * (yv - ym)).sum() / den
        a = ym - b * xm
        yhat = a + b * x
        rss = float(((yv - yhat) ** 2).sum())
        return _aic_gauss(rss, n, 2)
    def _pl_aic(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 10:
            return np.nan
        x = np.arange(len(w), dtype=float) + 1.0
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        lx = np.log(x); ly = yv
        xm = lx.mean(); ym = ly.mean()
        den = float(((lx - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = ((lx - xm) * (ly - ym)).sum() / den
        a = ym - b * xm
        yhat = a + b * lx
        rss = float(((ly - yhat) ** 2).sum())
        return _aic_gauss(rss, n, 2)
    lc = _safe_log(close)
    aic_pl = lc.rolling(252, min_periods=84).apply(_pl_aic, raw=True)
    aic_ex = lc.rolling(252, min_periods=84).apply(_exp_aic, raw=True)
    out = aic_pl - aic_ex
    return out.diff().diff()


def f02_pblo_041_stretched_exp_kohlrausch_b_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 20:
            return np.nan
        p0 = w[valid][0] if valid.any() else np.nan
        if not np.isfinite(p0) or p0 <= 0:
            return np.nan
        ratio = np.exp(w - p0)
        yv = -np.log(np.where(ratio > 0, ratio, np.nan))
        yv = np.where(yv > 0, np.log(yv), np.nan)
        x = np.arange(len(w), dtype=float) + 1.0
        xv = np.log(x)
        mask = np.isfinite(yv) & np.isfinite(xv)
        if mask.sum() < 8:
            return np.nan
        xx = xv[mask]; yy = yv[mask]
        xm = xx.mean(); ym = yy.mean()
        den = float(((xx - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((xx - xm) * (yy - ym)).sum() / den)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_042_double_exp_fast_slow_rate_ratio_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    slope_fast = _rolling_slope(lc, 21, min_periods=7)
    slope_slow = _rolling_slope(lc, 252, min_periods=84)
    out = _safe_div(slope_fast, slope_slow)
    return out.diff().diff()


def f02_pblo_043_logistic_curve_topping_resid_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 20:
            return np.nan
        yv = w[valid] if not valid.all() else w
        # Logistic in log space approximated by quadratic detrend
        c = np.polyfit(np.arange(yv.size, dtype=float), yv, 2)
        yhat = np.polyval(c, np.arange(yv.size, dtype=float))
        # logistic top: residual flattens vs quadratic; measure last residual / mean prior
        r = yv - yhat
        if r.size < 5:
            return np.nan
        return float(r[-1] - np.mean(r[:-1]))
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_044_gompertz_curve_fit_resid_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        valid = ~np.isnan(w)
        n = int(valid.sum())
        if n < 20:
            return np.nan
        yv = w[valid] if not valid.all() else w
        # Gompertz in log space: log(log(p/p0)) linear in t
        p0 = yv[0]
        z = yv - p0
        z = np.where(z > 0, np.log(z), np.nan)
        x = np.arange(yv.size, dtype=float)
        mask = np.isfinite(z)
        if mask.sum() < 10:
            return np.nan
        xx = x[mask]; yy = z[mask]
        xm = xx.mean(); ym = yy.mean()
        den = float(((xx - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = ((xx - xm) * (yy - ym)).sum() / den
        a = ym - b * xm
        yhat = a + b * xx
        r = yy - yhat
        return float(r[-1])
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_045_faber_hyperbolic_singularity_fit_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 5:
            return np.nan
        sd = float(np.nanstd(r, ddof=1))
        if sd <= 0:
            return np.nan
        return float(np.abs(r[-1]) / sd)
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_046_mean_curvature_minus_exp_baseline_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    exp_b = _rolling_slope(lc, 252, min_periods=84)
    out = c - (exp_b * exp_b)
    return out.diff().diff()


def f02_pblo_047_inflection_point_count_smoothed_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(d2.notna() & d2.shift(1).notna(), np.nan)
    out = flip.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f02_pblo_048_inflection_point_count_smoothed_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(d2.notna() & d2.shift(1).notna(), np.nan)
    out = flip.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f02_pblo_049_inflection_point_count_smoothed_504d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(d2.notna() & d2.shift(1).notna(), np.nan)
    out = flip.rolling(504, min_periods=168).sum()
    return out.diff().diff()


def f02_pblo_050_bars_since_last_inflection_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)) & d2.notna() & d2.shift(1).notna()
    def _f(w):
        if w.size == 0:
            return np.nan
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return float(w.size)
        return float(w.size - 1 - idx[-1])
    out = flip.astype(float).rolling(252, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_051_inflection_cluster_density_per_quarter_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(d2.notna() & d2.shift(1).notna(), np.nan)
    count = flip.rolling(252, min_periods=84).sum()
    out = count / 4.0
    return out.diff().diff()


def f02_pblo_052_cubic_a3_sign_change_event_21d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        return _poly_coef(w, 3, 0)
    lc = _safe_log(close)
    c3 = lc.rolling(126, min_periods=42).apply(_f, raw=True)
    sgn = np.sign(c3)
    flip = (sgn != sgn.shift(21)).astype(float)
    flip = flip.where(c3.notna() & c3.shift(21).notna(), np.nan)
    out = flip
    return out.diff().diff()


def f02_pblo_053_concavity_flip_event_count_63d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    sgn = np.sign(c)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(c.notna() & c.shift(1).notna(), np.nan)
    out = flip.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f02_pblo_054_accel_flip_then_extension_indicator_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip_recent = ((sgn != sgn.shift(1)) & d2.notna() & d2.shift(1).notna()).astype(float).rolling(21, min_periods=5).sum()
    ret_63 = lc.diff(63)
    out = (flip_recent > 0).astype(float) * np.sign(ret_63)
    out = out.where(flip_recent.notna() & ret_63.notna(), np.nan)
    return out.diff().diff()


def f02_pblo_055_inflection_to_peak_distance_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = (sgn != sgn.shift(1)) & d2.notna() & d2.shift(1).notna()
    def _last_idx(w):
        if w.size == 0:
            return np.nan
        idx = np.where(w > 0.5)[0]
        if idx.size == 0:
            return np.nan
        return float(w.size - 1 - idx[-1])
    bars_since_flip = flip.astype(float).rolling(252, min_periods=21).apply(_last_idx, raw=True)
    rmax_idx = lc.rolling(252, min_periods=21).apply(lambda w: float(w.size - 1 - int(np.nanargmax(w))) if np.any(~np.isnan(w)) else np.nan, raw=True)
    out = bars_since_flip - rmax_idx
    return out.diff().diff()


def f02_pblo_056_pre_peak_inflection_count_63d_before_252d_max_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff().rolling(5, min_periods=2).mean()
    sgn = np.sign(d2)
    flip = ((sgn != sgn.shift(1)) & d2.notna() & d2.shift(1).notna()).astype(float)
    rmax = lc.rolling(252, min_periods=21).max()
    is_peak = (lc >= rmax).astype(float)
    # Count flips in last 63d *only* on bars where the current price is at the 252d max
    count = flip.rolling(63, min_periods=21).sum()
    out = count.where(is_peak > 0.5, np.nan)
    return out.diff().diff()


def f02_pblo_057_std_of_logquad_c_63d_over_21d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    out = c.rolling(21, min_periods=7).std()
    return out.diff().diff()


def f02_pblo_058_std_of_logquad_c_252d_over_63d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    out = c.rolling(63, min_periods=21).std()
    return out.diff().diff()


def f02_pblo_059_std_of_logquad_c_252d_over_126d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    out = c.rolling(126, min_periods=42).std()
    return out.diff().diff()


def f02_pblo_060_cv_of_logquad_c_252d_over_63d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    m = c.rolling(63, min_periods=21).mean()
    s = c.rolling(63, min_periods=21).std()
    out = _safe_div(s, m.abs())
    return out.diff().diff()


def f02_pblo_061_cv_of_logquad_c_252d_over_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(252, min_periods=84).apply(_fc, raw=True)
    m = c.rolling(252, min_periods=84).mean()
    s = c.rolling(252, min_periods=84).std()
    out = _safe_div(s, m.abs())
    return out.diff().diff()


def f02_pblo_062_longest_pos_c_streak_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    pos = (c > 0).astype(float)
    def _max_streak(w):
        if w.size == 0:
            return np.nan
        if np.isnan(w).all():
            return np.nan
        best = 0; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = pos.rolling(252, min_periods=63).apply(_max_streak, raw=True)
    return out.diff().diff()


def f02_pblo_063_halflife_curvature_autocorr_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    def _hl(w):
        valid = ~np.isnan(w)
        if valid.sum() < 20:
            return np.nan
        v = w[valid]
        m = v.mean()
        num = float(((v[1:] - m) * (v[:-1] - m)).sum())
        den = float(((v - m) ** 2).sum())
        if den <= 0:
            return np.nan
        rho = num / den
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(2) / np.log(rho))
    out = c.rolling(252, min_periods=84).apply(_hl, raw=True)
    return out.diff().diff()


def f02_pblo_064_hurst_exponent_of_curvature_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    def _hurst(w):
        valid = ~np.isnan(w)
        if valid.sum() < 40:
            return np.nan
        v = w[valid]
        n = v.size
        lags = [2, 4, 8, 16]
        tau = []
        for L in lags:
            if L >= n:
                continue
            d = v[L:] - v[:-L]
            if d.size < 2:
                continue
            s = float(np.std(d, ddof=1))
            if s > 0:
                tau.append((np.log(L), np.log(s)))
        if len(tau) < 3:
            return np.nan
        xs = np.array([t[0] for t in tau]); ys = np.array([t[1] for t in tau])
        xm = xs.mean(); ym = ys.mean()
        den = float(((xs - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((xs - xm) * (ys - ym)).sum() / den)
    out = c.rolling(252, min_periods=84).apply(_hurst, raw=True)
    return out.diff().diff()


def f02_pblo_065_ar1_of_curvature_increments_252d_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    dc = c.diff()
    def _ar1(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean()
        num = float(((v[1:] - m) * (v[:-1] - m)).sum())
        den = float(((v - m) ** 2).sum())
        if den <= 0:
            return np.nan
        return num / den
    out = dc.rolling(252, min_periods=84).apply(_ar1, raw=True)
    return out.diff().diff()


def f02_pblo_066_current_curvature_regime_duration_d2(close: pd.Series) -> pd.Series:
    def _fc(w):
        return _poly_coef(w, 2, 0)
    lc = _safe_log(close)
    c = lc.rolling(63, min_periods=21).apply(_fc, raw=True)
    sgn = np.sign(c)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    out = sgn.groupby(block).cumcount().astype(float)
    out = out.where(c.notna(), np.nan)
    return out.diff().diff()


def f02_pblo_067_haar_wavelet_curvature_scale_5d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    short_m = lc.rolling(2, min_periods=1).mean()
    long_m = lc.rolling(5, min_periods=2).mean()
    out = short_m - long_m
    return out.diff().diff()


def f02_pblo_068_haar_wavelet_curvature_scale_21d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    short_m = lc.rolling(5, min_periods=1).mean()
    long_m = lc.rolling(21, min_periods=7).mean()
    out = short_m - long_m
    return out.diff().diff()


def f02_pblo_069_haar_wavelet_curvature_scale_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    short_m = lc.rolling(21, min_periods=1).mean()
    long_m = lc.rolling(63, min_periods=21).mean()
    out = short_m - long_m
    return out.diff().diff()


def f02_pblo_070_haar_wavelet_curvature_scale_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    short_m = lc.rolling(63, min_periods=1).mean()
    long_m = lc.rolling(252, min_periods=84).mean()
    out = short_m - long_m
    return out.diff().diff()


def f02_pblo_071_daubechies4_high_pass_at_top_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    # Daub-4 high-pass coefficients (approx)
    h = np.array([-0.4830, 0.8365, -0.2241, -0.1294])
    def _f(w):
        if w.size < 4:
            return np.nan
        return float(np.nansum(w[-4:] * h))
    out = lc.rolling(63, min_periods=4).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_072_wavelet_high_freq_energy_at_top_21d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d2 = lc.diff().diff()
    out = (d2 * d2).rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f02_pblo_073_wavelet_entropy_residual_252d_d2(close: pd.Series) -> pd.Series:
    def _f(w):
        r = _poly_residuals(w, 2)
        if r is None or r.size < 20:
            return np.nan
        a = np.abs(r)
        total = float(a.sum())
        if total <= 0:
            return np.nan
        bins, _ = np.histogram(a, bins=10)
        p = bins / bins.sum() if bins.sum() > 0 else None
        if p is None:
            return np.nan
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f02_pblo_074_emd_imf1_amplitude_proxy_21d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    low = lc.rolling(21, min_periods=7).mean()
    hf = lc - low
    out = hf.abs().rolling(21, min_periods=7).max()
    return out.diff().diff()


def f02_pblo_075_emd_imf2_over_imf3_amplitude_ratio_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m21 = lc.rolling(21, min_periods=7).mean()
    m63 = lc.rolling(63, min_periods=21).mean()
    m252 = lc.rolling(252, min_periods=84).mean()
    imf2 = (m21 - m63).abs().rolling(63, min_periods=21).max()
    imf3 = (m63 - m252).abs().rolling(63, min_periods=21).max()
    out = _safe_div(imf2, imf3)
    return out.diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

PARABOLIC_BLOWOFF_SIGNATURE_D2_REGISTRY_001_075 = {
    "f02_pblo_001_cubic_a3_log_close_63d_d2": {"inputs": ["close"], "func": f02_pblo_001_cubic_a3_log_close_63d_d2},
    "f02_pblo_002_cubic_a3_log_close_126d_d2": {"inputs": ["close"], "func": f02_pblo_002_cubic_a3_log_close_126d_d2},
    "f02_pblo_003_cubic_a3_log_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_003_cubic_a3_log_close_252d_d2},
    "f02_pblo_004_cubic_a3_log_close_504d_d2": {"inputs": ["close"], "func": f02_pblo_004_cubic_a3_log_close_504d_d2},
    "f02_pblo_005_quartic_a4_log_close_126d_d2": {"inputs": ["close"], "func": f02_pblo_005_quartic_a4_log_close_126d_d2},
    "f02_pblo_006_quartic_a4_log_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_006_quartic_a4_log_close_252d_d2},
    "f02_pblo_007_quartic_a4_log_close_504d_d2": {"inputs": ["close"], "func": f02_pblo_007_quartic_a4_log_close_504d_d2},
    "f02_pblo_008_quintic_a5_log_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_008_quintic_a5_log_close_252d_d2},
    "f02_pblo_009_quintic_a5_log_close_504d_d2": {"inputs": ["close"], "func": f02_pblo_009_quintic_a5_log_close_504d_d2},
    "f02_pblo_010_cubic_a3_sign_change_event_252d_d2": {"inputs": ["close"], "func": f02_pblo_010_cubic_a3_sign_change_event_252d_d2},
    "f02_pblo_011_dominant_polynomial_degree_bic_252d_d2": {"inputs": ["close"], "func": f02_pblo_011_dominant_polynomial_degree_bic_252d_d2},
    "f02_pblo_012_cubic_over_quad_r2_gain_126d_d2": {"inputs": ["close"], "func": f02_pblo_012_cubic_over_quad_r2_gain_126d_d2},
    "f02_pblo_013_parab_residual_std_63d_d2": {"inputs": ["close"], "func": f02_pblo_013_parab_residual_std_63d_d2},
    "f02_pblo_014_parab_residual_std_252d_d2": {"inputs": ["close"], "func": f02_pblo_014_parab_residual_std_252d_d2},
    "f02_pblo_015_parab_residual_std_504d_d2": {"inputs": ["close"], "func": f02_pblo_015_parab_residual_std_504d_d2},
    "f02_pblo_016_aic_quadratic_252d_d2": {"inputs": ["close"], "func": f02_pblo_016_aic_quadratic_252d_d2},
    "f02_pblo_017_aic_cubic_252d_d2": {"inputs": ["close"], "func": f02_pblo_017_aic_cubic_252d_d2},
    "f02_pblo_018_bic_quad_minus_cubic_252d_d2": {"inputs": ["close"], "func": f02_pblo_018_bic_quad_minus_cubic_252d_d2},
    "f02_pblo_019_bic_quartic_252d_d2": {"inputs": ["close"], "func": f02_pblo_019_bic_quartic_252d_d2},
    "f02_pblo_020_parab_mean_abs_resid_norm_close_252d_d2": {"inputs": ["close"], "func": f02_pblo_020_parab_mean_abs_resid_norm_close_252d_d2},
    "f02_pblo_021_parab_durbin_watson_resid_252d_d2": {"inputs": ["close"], "func": f02_pblo_021_parab_durbin_watson_resid_252d_d2},
    "f02_pblo_022_parab_resid_ad_normality_proxy_252d_d2": {"inputs": ["close"], "func": f02_pblo_022_parab_resid_ad_normality_proxy_252d_d2},
    "f02_pblo_023_parab_resid_skew_252d_d2": {"inputs": ["close"], "func": f02_pblo_023_parab_resid_skew_252d_d2},
    "f02_pblo_024_parab_resid_kurt_252d_d2": {"inputs": ["close"], "func": f02_pblo_024_parab_resid_kurt_252d_d2},
    "f02_pblo_025_lppl_omega_proxy_residual_zcr_504d_d2": {"inputs": ["close"], "func": f02_pblo_025_lppl_omega_proxy_residual_zcr_504d_d2},
    "f02_pblo_026_lppl_omega_proxy_residual_zcr_1260d_d2": {"inputs": ["close"], "func": f02_pblo_026_lppl_omega_proxy_residual_zcr_1260d_d2},
    "f02_pblo_027_lppl_beta_singularity_strength_252d_d2": {"inputs": ["close"], "func": f02_pblo_027_lppl_beta_singularity_strength_252d_d2},
    "f02_pblo_028_lppl_phi_phase_proxy_252d_d2": {"inputs": ["close"], "func": f02_pblo_028_lppl_phi_phase_proxy_252d_d2},
    "f02_pblo_029_lppl_critical_time_confidence_252d_d2": {"inputs": ["close"], "func": f02_pblo_029_lppl_critical_time_confidence_252d_d2},
    "f02_pblo_030_log_periodic_oscillation_amplitude_252d_d2": {"inputs": ["close"], "func": f02_pblo_030_log_periodic_oscillation_amplitude_252d_d2},
    "f02_pblo_031_log_periodic_freq_stability_252d_d2": {"inputs": ["close"], "func": f02_pblo_031_log_periodic_freq_stability_252d_d2},
    "f02_pblo_032_lppl_resid_r2_quad_504d_d2": {"inputs": ["close"], "func": f02_pblo_032_lppl_resid_r2_quad_504d_d2},
    "f02_pblo_033_lppl_bubble_probability_proxy_252d_d2": {"inputs": ["close"], "func": f02_pblo_033_lppl_bubble_probability_proxy_252d_d2},
    "f02_pblo_034_lppl_omega_harmonic_ratio_252d_d2": {"inputs": ["close"], "func": f02_pblo_034_lppl_omega_harmonic_ratio_252d_d2},
    "f02_pblo_035_lppl_omega_evolution_63d_d2": {"inputs": ["close"], "func": f02_pblo_035_lppl_omega_evolution_63d_d2},
    "f02_pblo_036_lppl_phase_entropy_252d_d2": {"inputs": ["close"], "func": f02_pblo_036_lppl_phase_entropy_252d_d2},
    "f02_pblo_037_exp_fit_b_logclose_252d_d2": {"inputs": ["close"], "func": f02_pblo_037_exp_fit_b_logclose_252d_d2},
    "f02_pblo_038_power_law_exp_log_log_126d_d2": {"inputs": ["close"], "func": f02_pblo_038_power_law_exp_log_log_126d_d2},
    "f02_pblo_039_power_law_exp_log_log_756d_d2": {"inputs": ["close"], "func": f02_pblo_039_power_law_exp_log_log_756d_d2},
    "f02_pblo_040_power_law_minus_exp_aic_252d_d2": {"inputs": ["close"], "func": f02_pblo_040_power_law_minus_exp_aic_252d_d2},
    "f02_pblo_041_stretched_exp_kohlrausch_b_252d_d2": {"inputs": ["close"], "func": f02_pblo_041_stretched_exp_kohlrausch_b_252d_d2},
    "f02_pblo_042_double_exp_fast_slow_rate_ratio_d2": {"inputs": ["close"], "func": f02_pblo_042_double_exp_fast_slow_rate_ratio_d2},
    "f02_pblo_043_logistic_curve_topping_resid_252d_d2": {"inputs": ["close"], "func": f02_pblo_043_logistic_curve_topping_resid_252d_d2},
    "f02_pblo_044_gompertz_curve_fit_resid_252d_d2": {"inputs": ["close"], "func": f02_pblo_044_gompertz_curve_fit_resid_252d_d2},
    "f02_pblo_045_faber_hyperbolic_singularity_fit_252d_d2": {"inputs": ["close"], "func": f02_pblo_045_faber_hyperbolic_singularity_fit_252d_d2},
    "f02_pblo_046_mean_curvature_minus_exp_baseline_252d_d2": {"inputs": ["close"], "func": f02_pblo_046_mean_curvature_minus_exp_baseline_252d_d2},
    "f02_pblo_047_inflection_point_count_smoothed_63d_d2": {"inputs": ["close"], "func": f02_pblo_047_inflection_point_count_smoothed_63d_d2},
    "f02_pblo_048_inflection_point_count_smoothed_252d_d2": {"inputs": ["close"], "func": f02_pblo_048_inflection_point_count_smoothed_252d_d2},
    "f02_pblo_049_inflection_point_count_smoothed_504d_d2": {"inputs": ["close"], "func": f02_pblo_049_inflection_point_count_smoothed_504d_d2},
    "f02_pblo_050_bars_since_last_inflection_252d_d2": {"inputs": ["close"], "func": f02_pblo_050_bars_since_last_inflection_252d_d2},
    "f02_pblo_051_inflection_cluster_density_per_quarter_252d_d2": {"inputs": ["close"], "func": f02_pblo_051_inflection_cluster_density_per_quarter_252d_d2},
    "f02_pblo_052_cubic_a3_sign_change_event_21d_d2": {"inputs": ["close"], "func": f02_pblo_052_cubic_a3_sign_change_event_21d_d2},
    "f02_pblo_053_concavity_flip_event_count_63d_d2": {"inputs": ["close"], "func": f02_pblo_053_concavity_flip_event_count_63d_d2},
    "f02_pblo_054_accel_flip_then_extension_indicator_63d_d2": {"inputs": ["close"], "func": f02_pblo_054_accel_flip_then_extension_indicator_63d_d2},
    "f02_pblo_055_inflection_to_peak_distance_252d_d2": {"inputs": ["close"], "func": f02_pblo_055_inflection_to_peak_distance_252d_d2},
    "f02_pblo_056_pre_peak_inflection_count_63d_before_252d_max_d2": {"inputs": ["close"], "func": f02_pblo_056_pre_peak_inflection_count_63d_before_252d_max_d2},
    "f02_pblo_057_std_of_logquad_c_63d_over_21d_d2": {"inputs": ["close"], "func": f02_pblo_057_std_of_logquad_c_63d_over_21d_d2},
    "f02_pblo_058_std_of_logquad_c_252d_over_63d_d2": {"inputs": ["close"], "func": f02_pblo_058_std_of_logquad_c_252d_over_63d_d2},
    "f02_pblo_059_std_of_logquad_c_252d_over_126d_d2": {"inputs": ["close"], "func": f02_pblo_059_std_of_logquad_c_252d_over_126d_d2},
    "f02_pblo_060_cv_of_logquad_c_252d_over_63d_d2": {"inputs": ["close"], "func": f02_pblo_060_cv_of_logquad_c_252d_over_63d_d2},
    "f02_pblo_061_cv_of_logquad_c_252d_over_252d_d2": {"inputs": ["close"], "func": f02_pblo_061_cv_of_logquad_c_252d_over_252d_d2},
    "f02_pblo_062_longest_pos_c_streak_252d_d2": {"inputs": ["close"], "func": f02_pblo_062_longest_pos_c_streak_252d_d2},
    "f02_pblo_063_halflife_curvature_autocorr_252d_d2": {"inputs": ["close"], "func": f02_pblo_063_halflife_curvature_autocorr_252d_d2},
    "f02_pblo_064_hurst_exponent_of_curvature_252d_d2": {"inputs": ["close"], "func": f02_pblo_064_hurst_exponent_of_curvature_252d_d2},
    "f02_pblo_065_ar1_of_curvature_increments_252d_d2": {"inputs": ["close"], "func": f02_pblo_065_ar1_of_curvature_increments_252d_d2},
    "f02_pblo_066_current_curvature_regime_duration_d2": {"inputs": ["close"], "func": f02_pblo_066_current_curvature_regime_duration_d2},
    "f02_pblo_067_haar_wavelet_curvature_scale_5d_d2": {"inputs": ["close"], "func": f02_pblo_067_haar_wavelet_curvature_scale_5d_d2},
    "f02_pblo_068_haar_wavelet_curvature_scale_21d_d2": {"inputs": ["close"], "func": f02_pblo_068_haar_wavelet_curvature_scale_21d_d2},
    "f02_pblo_069_haar_wavelet_curvature_scale_63d_d2": {"inputs": ["close"], "func": f02_pblo_069_haar_wavelet_curvature_scale_63d_d2},
    "f02_pblo_070_haar_wavelet_curvature_scale_252d_d2": {"inputs": ["close"], "func": f02_pblo_070_haar_wavelet_curvature_scale_252d_d2},
    "f02_pblo_071_daubechies4_high_pass_at_top_63d_d2": {"inputs": ["close"], "func": f02_pblo_071_daubechies4_high_pass_at_top_63d_d2},
    "f02_pblo_072_wavelet_high_freq_energy_at_top_21d_d2": {"inputs": ["close"], "func": f02_pblo_072_wavelet_high_freq_energy_at_top_21d_d2},
    "f02_pblo_073_wavelet_entropy_residual_252d_d2": {"inputs": ["close"], "func": f02_pblo_073_wavelet_entropy_residual_252d_d2},
    "f02_pblo_074_emd_imf1_amplitude_proxy_21d_d2": {"inputs": ["close"], "func": f02_pblo_074_emd_imf1_amplitude_proxy_21d_d2},
    "f02_pblo_075_emd_imf2_over_imf3_amplitude_ratio_d2": {"inputs": ["close"], "func": f02_pblo_075_emd_imf2_over_imf3_amplitude_ratio_d2},
}
