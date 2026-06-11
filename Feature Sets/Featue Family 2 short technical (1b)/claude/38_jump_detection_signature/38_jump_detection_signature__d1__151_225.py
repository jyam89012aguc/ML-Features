"""jump_detection_signature d1 features 151-225 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the 150 in __base__001_075.py and __base__076_150.py.
Drawn from gap analysis of the academic jump-detection literature: realized
higher moments, multipower / MinRV / MedRV jump-robust estimators, formal
BNS / AS-J / ABD / Mancini / Lee-Hannig jump tests, EVT / POT-GPD / GEV tail
estimators, Hawkes diagnostics (branching ratio, Fano, Allan-var, Ogata),
CUSUM / Bai-Perron / Andrews structural-break tests, distributional GoF
(JB / AD / KS), Lévy α-stable index, OHLC-rich bar-shape, volume-coupled
jump intensities, classic chart-shape blow-off signatures (parabolic-acc,
buying-climax, 3-bar reversal, island-reversal, ulcer, calmar, drawdown).

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


def _pot_gpd_fit(arr: np.ndarray, top_frac: float = 0.10):
    """Method-of-moments POT-GPD fit. Returns (sigma_hat, xi_hat) for excesses over p(1-top_frac)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 60:
        return (np.nan, np.nan)
    threshold = np.quantile(a, 1.0 - top_frac)
    excesses = a[a > threshold] - threshold
    if len(excesses) < 15:
        return (np.nan, np.nan)
    m = excesses.mean()
    v = excesses.var()
    if m == 0 or v == 0:
        return (np.nan, np.nan)
    xi = 0.5 * (1.0 - (m ** 2) / v)
    sigma = 0.5 * m * (1.0 + (m ** 2) / v)
    return (float(sigma), float(xi))


def _gev_mom_fit(arr: np.ndarray):
    """Method-of-moments GEV fit from block maxima. Returns (location, scale)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 6:
        return (np.nan, np.nan)
    m = a.mean(); s = a.std()
    if s == 0:
        return (np.nan, np.nan)
    scale = s * np.sqrt(6.0) / np.pi
    loc = m - 0.5772 * scale
    return (float(loc), float(scale))


# ============================================================
# Bucket Z1 — Realized higher moments & variance-swap (151-160)
# ============================================================


def f38_jpdt_151_jiang_oomen_swv_diff_21d_d1(close: pd.Series) -> pd.Series:
    """Jiang-Oomen swap-variance test: 2·Σ(r − (e^r − 1)) − RV over 21d — jump asymmetry signal."""
    r = _log_ret(close)
    swv = 2.0 * (r - (np.exp(r) - 1.0))
    return (swv.rolling(MDAYS, min_periods=WDAYS).sum() - _rv(r, MDAYS)).diff()


def f38_jpdt_152_jiang_oomen_swv_ratio_63d_d1(close: pd.Series) -> pd.Series:
    """Normalized Jiang-Oomen SwV/RV ratio over 63d."""
    r = _log_ret(close)
    swv = (2.0 * (r - (np.exp(r) - 1.0))).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(swv, _rv(r, QDAYS))).diff()


def f38_jpdt_153_realized_3rd_moment_21d_d1(close: pd.Series) -> pd.Series:
    """Realized third moment Σ r³ over 21d — raw skewness numerator."""
    return ((_log_ret(close) ** 3).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f38_jpdt_154_realized_3rd_moment_252d_d1(close: pd.Series) -> pd.Series:
    """Realized third moment Σ r³ over 252d — annual skew numerator."""
    return ((_log_ret(close) ** 3).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_155_realized_quarticity_21d_d1(close: pd.Series) -> pd.Series:
    """Realized quarticity Σ r⁴ over 21d — 4th-moment vol-of-vol proxy."""
    return ((_log_ret(close) ** 4).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f38_jpdt_156_realized_quarticity_252d_d1(close: pd.Series) -> pd.Series:
    """Realized quarticity Σ r⁴ over 252d — annual."""
    return ((_log_ret(close) ** 4).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_157_realized_5th_moment_63d_d1(close: pd.Series) -> pd.Series:
    """Realized 5th moment Σ r⁵ over 63d — hyperskewness."""
    return ((_log_ret(close) ** 5).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_158_realized_6th_moment_63d_d1(close: pd.Series) -> pd.Series:
    """Realized 6th moment Σ r⁶ over 63d — hyperkurtosis."""
    return ((_log_ret(close) ** 6).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_159_realized_skewness_amaya_21d_d1(close: pd.Series) -> pd.Series:
    """Realized skewness (Amaya et al.): n·Σ r³ / RV^(3/2) over 21d."""
    r = _log_ret(close)
    num = MDAYS * (r ** 3).rolling(MDAYS, min_periods=WDAYS).sum()
    den = _rv(r, MDAYS).pow(1.5)
    return (_safe_div(num, den)).diff()


def f38_jpdt_160_realized_kurtosis_amaya_63d_d1(close: pd.Series) -> pd.Series:
    """Realized kurtosis (Amaya et al.): n·Σ r⁴ / RV² over 63d."""
    r = _log_ret(close)
    num = QDAYS * (r ** 4).rolling(QDAYS, min_periods=MDAYS).sum()
    den = _rv(r, QDAYS) ** 2
    return (_safe_div(num, den)).diff()


def f38_jpdt_161_tripower_variation_63d_d1(close: pd.Series) -> pd.Series:
    """Tripower variation TPV = μ_{4/3}^{-3} · Σ |r|^{4/3}·|r_-1|^{4/3}·|r_-2|^{4/3} over 63d."""
    r = _log_ret(close).abs()
    a = r ** (4.0 / 3.0)
    prod = a * a.shift(1) * a.shift(2)
    # μ_{4/3} = 2^{2/3}·Γ(7/6)/√π ≈ 1.0837; μ_{4/3}^{-3} ≈ 0.7860
    mu = 2.0 ** (2.0 / 3.0) * (math.gamma(7.0 / 6.0) / np.sqrt(np.pi))
    return ((mu ** -3) * prod.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_162_quadpower_variation_252d_d1(close: pd.Series) -> pd.Series:
    """Quadpower variation QPV = μ_1^{-4} · Σ |r|·|r_-1|·|r_-2|·|r_-3| over 252d."""
    r = _log_ret(close).abs()
    prod = r * r.shift(1) * r.shift(2) * r.shift(3)
    mu1 = np.sqrt(2.0 / np.pi)  # ≈ 0.7979
    return ((mu1 ** -4) * prod.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_163_minrv_63d_d1(close: pd.Series) -> pd.Series:
    """MinRV (Andersen-Dobrev-Schaumburg): (π/(π-2)) · Σ min(|r_t|,|r_{t-1}|)² over 63d."""
    r = _log_ret(close).abs()
    mn = pd.concat([r, r.shift(1)], axis=1).min(axis=1)
    k = np.pi / (np.pi - 2.0)
    return (k * (mn ** 2).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_164_medrv_252d_d1(close: pd.Series) -> pd.Series:
    """MedRV: (π/(6−4√3+π)) · Σ median(|r_{t-2}|,|r_{t-1}|,|r_t|)² over 252d (causal)."""
    r = _log_ret(close).abs()
    med = pd.concat([r.shift(2), r.shift(1), r], axis=1).median(axis=1)
    k = np.pi / (6.0 - 4.0 * np.sqrt(3.0) + np.pi)
    return (k * (med ** 2).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_165_minrv_over_rv_63d_d1(close: pd.Series) -> pd.Series:
    """MinRV / RV ratio at 63d — jump-robust to raw RV; low ratio = jump regime."""
    r = _log_ret(close).abs()
    mn = pd.concat([r, r.shift(1)], axis=1).min(axis=1)
    k = np.pi / (np.pi - 2.0)
    minrv = k * (mn ** 2).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(minrv, _rv(_log_ret(close), QDAYS))).diff()


def f38_jpdt_166_medrv_over_rv_252d_d1(close: pd.Series) -> pd.Series:
    """MedRV / RV ratio at 252d — annual jump-robust-vs-raw vol fraction."""
    r = _log_ret(close).abs()
    med = pd.concat([r.shift(2), r.shift(1), r], axis=1).median(axis=1)
    k = np.pi / (6.0 - 4.0 * np.sqrt(3.0) + np.pi)
    medrv = k * (med ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(medrv, _rv(_log_ret(close), YDAYS))).diff()


def f38_jpdt_167_tpv_over_bv_63d_d1(close: pd.Series) -> pd.Series:
    """Tripower / Bipower ratio at 63d — TPV is more jump-robust than BV; ratio≪1 = jumps."""
    r = _log_ret(close)
    a = r.abs() ** (4.0 / 3.0)
    prod = a * a.shift(1) * a.shift(2)
    mu = 2.0 ** (2.0 / 3.0) * (math.gamma(7.0 / 6.0) / np.sqrt(np.pi))
    tpv = (mu ** -3) * prod.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(tpv, _bv(r, QDAYS))).diff()


def f38_jpdt_168_quadpower_quarticity_252d_d1(close: pd.Series) -> pd.Series:
    """Quadpower quarticity = μ_1^{-4} · Σ |r|·|r_-1|·|r_-2|·|r_-3| in absolute units over 252d."""
    r = _log_ret(close).abs()
    prod = r * r.shift(1) * r.shift(2) * r.shift(3)
    mu1 = np.sqrt(2.0 / np.pi)
    return ((mu1 ** -4) * prod.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_169_bns_z_linear_63d_d1(close: pd.Series) -> pd.Series:
    """BNS z-test linear form: (RV-BV)/sqrt(((π²/4)+π-5)·IQ/n) — uses tripower quarticity at 63d."""
    r = _log_ret(close)
    rv = _rv(r, QDAYS)
    bv = _bv(r, QDAYS)
    # Tripower-quarticity proxy: Σ |r|^{4/3}·|r_-1|^{4/3}·|r_-2|^{4/3}
    a = r.abs() ** (4.0 / 3.0)
    iq = (a * a.shift(1) * a.shift(2)).rolling(QDAYS, min_periods=MDAYS).sum()
    theta = (np.pi ** 2) / 4.0 + np.pi - 5.0
    return (_safe_div(rv - bv, np.sqrt(theta * iq / QDAYS))).diff()


def f38_jpdt_170_bns_z_ratio_63d_d1(close: pd.Series) -> pd.Series:
    """BNS z-test ratio form: (1 - BV/RV)/sqrt(θ·IQ/(n·BV²)) at 63d."""
    r = _log_ret(close)
    rv = _rv(r, QDAYS)
    bv = _bv(r, QDAYS)
    a = r.abs() ** (4.0 / 3.0)
    iq = (a * a.shift(1) * a.shift(2)).rolling(QDAYS, min_periods=MDAYS).sum()
    theta = (np.pi ** 2) / 4.0 + np.pi - 5.0
    return (_safe_div(1.0 - _safe_div(bv, rv), np.sqrt(theta * iq / (QDAYS * bv ** 2)))).diff()


def f38_jpdt_171_bns_z_log_63d_d1(close: pd.Series) -> pd.Series:
    """BNS z-test log form: log(RV/BV)/sqrt(θ·IQ/(n·BV²)) at 63d."""
    r = _log_ret(close)
    rv = _rv(r, QDAYS)
    bv = _bv(r, QDAYS)
    a = r.abs() ** (4.0 / 3.0)
    iq = (a * a.shift(1) * a.shift(2)).rolling(QDAYS, min_periods=MDAYS).sum()
    theta = (np.pi ** 2) / 4.0 + np.pi - 5.0
    return (_safe_div(_safe_log(rv) - _safe_log(bv), np.sqrt(theta * iq / (QDAYS * bv ** 2)))).diff()


def f38_jpdt_172_aitsahalia_jacod_ratio_63d_d1(close: pd.Series) -> pd.Series:
    """Aït-Sahalia-Jacod S(p,q,Δ) ratio: B(p,Δ)/B(p,kΔ) with p=4, k=2 over 63d."""
    r = _log_ret(close).abs()
    bp1 = (r ** 4).rolling(QDAYS, min_periods=MDAYS).sum()
    # Aggregated 2-bar returns for k=2
    r2bar = _safe_log(close).diff(2).abs()
    bp2 = (r2bar ** 4).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(bp1, bp2)).diff()


def f38_jpdt_173_aitsahalia_jacod_activity_index_252d_d1(close: pd.Series) -> pd.Series:
    """A-S-J jump activity index β̂ ≈ log2(B(2)/B(4)) where B(p)=Σ|r|^p over 252d."""
    r = _log_ret(close).abs()
    b2 = (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    b4 = (r ** 4).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(_safe_log(b2) - _safe_log(b4), np.log(2.0))).diff()


def f38_jpdt_174_abd_gumbel_jump_count_21d_d1(close: pd.Series) -> pd.Series:
    """ABD/Andersen-Bollerslev-Dobrev jump count with Gumbel-extreme cutoff over 21d."""
    r = _log_ret(close)
    bv = _bv(r, MDAYS).shift(1)
    scale = np.sqrt(_safe_div(bv, MDAYS) * (np.pi / 2.0))
    stat = _safe_div(r.abs(), scale)
    # Gumbel critical value at α=0.001 for n=21: cn = sqrt(2·ln n), sn ≈ 1/cn; threshold cn − sn·ln(−ln(1−α))
    cn = np.sqrt(2.0 * np.log(MDAYS)); sn = 1.0 / cn
    crit = cn - sn * np.log(-np.log(1.0 - 0.001))
    return ((stat > crit).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f38_jpdt_175_mancini_truncated_power_var_p4_63d_d1(close: pd.Series) -> pd.Series:
    """Mancini truncated power variation at p=4: Σ r⁴·1{|r| ≤ α·n^{-ω}·σ_prior} over 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, QDAYS)
    # Threshold: α=3, ω=0.49 (standard) → u_n ≈ 3·σ·n^{-0.49}
    u = 3.0 * sig * (QDAYS ** -0.49) * np.sqrt(QDAYS)
    trunc = (r ** 4).where(r.abs() <= u, 0.0)
    return (trunc.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_176_lee_hannig_wavelet_jump_count_63d_d1(close: pd.Series) -> pd.Series:
    """Lee-Hannig wavelet-coefficient jump count: Haar-detail z-score > 4 events over 63d."""
    r = _log_ret(close)
    # Haar detail coefficient at scale-2: d = (r_t - r_{t-1}) / sqrt(2)
    d = (r - r.shift(1)) / np.sqrt(2.0)
    sig = d.rolling(QDAYS, min_periods=MDAYS).std().shift(1)
    z = _safe_div(d.abs(), sig)
    return ((z > 4.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_177_pot_gpd_scale_252d_d1(close: pd.Series) -> pd.Series:
    """POT-GPD scale parameter σ̂ on |log-ret| > p90 over 252d (method-of-moments)."""
    a = _log_ret(close).abs()
    return (a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _pot_gpd_fit(w)[0], raw=True)).diff()


def f38_jpdt_178_pot_gpd_shape_252d_d1(close: pd.Series) -> pd.Series:
    """POT-GPD shape parameter ξ̂ on |log-ret| > p90 over 252d — tail-thickness."""
    a = _log_ret(close).abs()
    return (a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _pot_gpd_fit(w)[1], raw=True)).diff()


def f38_jpdt_179_mean_excess_slope_p90_252d_d1(close: pd.Series) -> pd.Series:
    """Mean excess function slope: d/du E[X-u|X>u] estimated at u={p90, p95, p99} over 252d."""
    a = _log_ret(close).abs()

    def _slope(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        us = np.quantile(ww, [0.90, 0.95, 0.99])
        es = []
        for u in us:
            ex = ww[ww > u] - u
            es.append(ex.mean() if len(ex) > 0 else np.nan)
        es = np.array(es)
        if np.any(np.isnan(es)):
            return np.nan
        xm = us.mean(); ym = es.mean()
        d = ((us - xm) ** 2).sum()
        return float(((us - xm) * (es - ym)).sum() / d) if d > 0 else np.nan
    return (a.rolling(YDAYS, min_periods=QDAYS).apply(_slope, raw=True)).diff()


def f38_jpdt_180_gev_location_blockmax_21bars_252d_d1(close: pd.Series) -> pd.Series:
    """GEV location parameter fitted to 21d-block max|log-ret| over rolling 252d (12 blocks)."""
    a = _log_ret(close).abs()
    block_max = a.rolling(MDAYS, min_periods=MDAYS).max().iloc[MDAYS - 1::MDAYS]
    block_max = block_max.reindex(a.index).ffill()
    return (block_max.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gev_mom_fit(w)[0], raw=True)).diff()


def f38_jpdt_181_gev_scale_blockmax_21bars_252d_d1(close: pd.Series) -> pd.Series:
    """GEV scale parameter from 21d-block-max fits over 252d."""
    a = _log_ret(close).abs()
    block_max = a.rolling(MDAYS, min_periods=MDAYS).max().iloc[MDAYS - 1::MDAYS]
    block_max = block_max.reindex(a.index).ffill()
    return (block_max.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _gev_mom_fit(w)[1], raw=True)).diff()


def f38_jpdt_182_tail_dep_lag1_p90_252d_d1(close: pd.Series) -> pd.Series:
    """Tail dependence λ_U on (|r_t|, |r_{t-1}|) at p90 over 252d — joint extreme persistence."""
    a = _log_ret(close).abs()
    lag = a.shift(1)

    def _td(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        threshold = np.quantile(ww, 0.90)
        # joint exceedance on the original Series via shift — w is the abs returns; we need pairs
        # Approximation: count how many bars themselves >threshold AND prior abs (passed via w shift) is unknown
        # Use simpler approach: fraction of consecutive (>p90, >p90) pairs out of (any >p90)
        return np.nan
    # Implementation in vectorized form:
    p90 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    above = (a > p90)
    joint = (above & above.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    marg = above.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(joint, marg)).diff()


def f38_jpdt_183_reiss_thomas_tail_idx_252d_d1(close: pd.Series) -> pd.Series:
    """Reiss-Thomas (DEdH) bias-corrected tail-index of |log-ret| over 252d (top 10%)."""
    a = _log_ret(close).abs()

    def _dedh(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < 60:
            return np.nan
        ww = np.sort(ww)
        k = max(int(0.10 * n), 5)
        top = ww[-k:]
        if top[0] <= 0:
            return np.nan
        lg = np.log(top / top[0])
        m1 = lg[1:].mean() if len(lg) > 1 else np.nan
        m2 = (lg[1:] ** 2).mean() if len(lg) > 1 else np.nan
        if not np.isfinite(m1) or not np.isfinite(m2) or m2 == 0:
            return np.nan
        return float(m1 + 1.0 - 0.5 / (1.0 - (m1 ** 2) / m2)) if (1.0 - (m1 ** 2) / m2) != 0 else np.nan
    return (a.rolling(YDAYS, min_periods=QDAYS).apply(_dedh, raw=True)).diff()


def f38_jpdt_184_max_absret_63d_over_252d_ratio_d1(close: pd.Series) -> pd.Series:
    """Temporal tail concentration: max|log-ret|, 63d / max|log-ret|, 252d."""
    a = _log_ret(close).abs()
    return (_safe_div(a.rolling(QDAYS, min_periods=MDAYS).max(),

                     a.rolling(YDAYS, min_periods=QDAYS).max())).diff()


def f38_jpdt_185_p99_over_p50_absret_252d_d1(close: pd.Series) -> pd.Series:
    """Ratio 99th-pct |log-ret| / median |log-ret| over 252d — distinct from existing p99/p90."""
    a = _log_ret(close).abs()
    return (_safe_div(a.rolling(YDAYS, min_periods=QDAYS).quantile(0.99),

                     a.rolling(YDAYS, min_periods=QDAYS).quantile(0.50))).diff()


def f38_jpdt_186_p99_count_over_p95_count_252d_d1(close: pd.Series) -> pd.Series:
    """Right-tail concentration: count |r|>p99(own past 252d) / count |r|>p95(own past 252d)."""
    a = _log_ret(close).abs()
    p99 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    p95 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    c99 = (a > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    c95 = (a > p95).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(c99, c95)).diff()


def f38_jpdt_187_hawkes_branching_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """Hawkes branching ratio η̂ via Filimonov-Sornette method-of-moments on jump arrivals over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _bratio(w):
        n = w.sum()
        if n < 5:
            return np.nan
        # Variance / mean ratio of counts in equal sub-windows; for Hawkes:
        # Fano = 1/(1-η)² approx → η ≈ 1 − 1/√Fano
        nbins = 6
        sub = max(len(w) // nbins, 5)
        cnts = np.array([w[i * sub:(i + 1) * sub].sum() for i in range(nbins)])
        m = cnts.mean()
        if m == 0:
            return np.nan
        fano = cnts.var() / m
        if fano < 1.0:
            return 0.0
        return float(np.clip(1.0 - 1.0 / np.sqrt(fano), 0.0, 0.99))
    return (j.rolling(YDAYS, min_periods=QDAYS).apply(_bratio, raw=True)).diff()


def f38_jpdt_188_dist_from_criticality_252d_d1(close: pd.Series) -> pd.Series:
    """Distance from Hawkes criticality: 1 − η̂ from branching-ratio estimate over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _bratio(w):
        n = w.sum()
        if n < 5:
            return np.nan
        nbins = 6
        sub = max(len(w) // nbins, 5)
        cnts = np.array([w[i * sub:(i + 1) * sub].sum() for i in range(nbins)])
        m = cnts.mean()
        if m == 0:
            return np.nan
        fano = cnts.var() / m
        if fano < 1.0:
            return 0.0
        return float(np.clip(1.0 - 1.0 / np.sqrt(fano), 0.0, 0.99))
    eta = j.rolling(YDAYS, min_periods=QDAYS).apply(_bratio, raw=True)
    return (1.0 - eta).diff()


def f38_jpdt_189_intensity_now_over_long_run_avg_63d_d1(close: pd.Series) -> pd.Series:
    """Hawkes intensity now / long-run mean: short-half-life EWMA / 252d mean of indicator over 63d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    alpha = 1.0 - 0.5 ** (1.0 / 21.0)
    now = j.ewm(alpha=alpha, min_periods=21).mean()
    long_avg = j.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(now, long_avg)).diff()


def f38_jpdt_190_fano_factor_jump_counts_252d_d1(close: pd.Series) -> pd.Series:
    """Fano factor (var/mean) of jump counts in 21d sub-bins over 252d window."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _fano(w):
        nbins = 12
        sub = max(len(w) // nbins, 5)
        cnts = np.array([w[i * sub:(i + 1) * sub].sum() for i in range(nbins)])
        m = cnts.mean()
        return float(cnts.var() / m) if m > 0 else np.nan
    return (j.rolling(YDAYS, min_periods=QDAYS).apply(_fano, raw=True)).diff()


def f38_jpdt_191_allan_variance_jump_counts_252d_d1(close: pd.Series) -> pd.Series:
    """Allan-variance of jump counts across nested 5d-vs-21d sub-windows over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    c5 = j.rolling(WDAYS, min_periods=2).sum()
    c21 = j.rolling(MDAYS, min_periods=WDAYS).sum()
    return (((c5 - c21 / (MDAYS / WDAYS)) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f38_jpdt_192_ogata_residual_252d_d1(close: pd.Series) -> pd.Series:
    """Ogata residual: cumulative jump count − fitted intensity ∫λ dt — discrepancy over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)
    alpha = 1.0 - 0.5 ** (1.0 / 21.0)
    lam = j.ewm(alpha=alpha, min_periods=21).mean()
    actual = j.rolling(YDAYS, min_periods=QDAYS).sum()
    expected = lam.rolling(YDAYS, min_periods=QDAYS).sum()
    return (actual - expected).diff()


def f38_jpdt_193_lempel_ziv_sign_complexity_252d_d1(close: pd.Series) -> pd.Series:
    """Lempel-Ziv complexity of sign(r) string over 252d — algorithmic complexity of direction."""
    r = _log_ret(close)

    def _lz(w):
        s = "".join("1" if v > 0 else "0" for v in w if not np.isnan(v))
        if len(s) < 10:
            return np.nan
        i = 0; c = 1; k = 1; l = 1
        while True:
            if i + k > len(s) or l + k > len(s):
                break
            if s[i + k - 1] != s[l + k - 1]:
                if k > 1:
                    pass
                c += 1
                l += k
                if l + 1 > len(s):
                    break
                k = 1; i = 0
            else:
                k += 1
                if l + k > len(s):
                    c += 1
                    break
        return float(c) / (len(s) / np.log2(len(s)))
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_lz, raw=True)).diff()


def f38_jpdt_194_inclan_tiao_cusum_sq_252d_d1(close: pd.Series) -> pd.Series:
    """Inclán-Tiao CUSUM-of-squares max stat on r² over 252d."""
    r2 = _log_ret(close) ** 2

    def _cusum(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        cs = np.cumsum(ww) / ww.sum()
        idx = np.arange(1, n + 1) / n
        return float(np.max(np.abs(cs - idx)))
    return (r2.rolling(YDAYS, min_periods=QDAYS).apply(_cusum, raw=True)).diff()


def f38_jpdt_195_icss_break_count_504d_d1(close: pd.Series) -> pd.Series:
    """ICSS-style variance-breakpoint count over 504d (CUSUM-Q exceeding threshold 1.358)."""
    r2 = _log_ret(close) ** 2

    def _icss(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < YDAYS:
            return np.nan
        cs = np.cumsum(ww) / ww.sum()
        idx = np.arange(1, n + 1) / n
        dk = np.abs(cs - idx) * np.sqrt(n / 2.0)
        return float((dk > 1.358).sum())
    return (r2.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_icss, raw=True)).diff()


def f38_jpdt_196_bai_perron_supF_rsq_252d_d1(close: pd.Series) -> pd.Series:
    """Bai-Perron supF stat on r² (mean-shift test): max F across all single-break points over 252d."""
    r2 = _log_ret(close) ** 2

    def _supf(w):
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
            f = (tss - rss) / (rss / (n - 2)) if rss > 0 else 0.0
            if f > best:
                best = f
        return float(best)
    return (r2.rolling(YDAYS, min_periods=QDAYS).apply(_supf, raw=True)).diff()


def f38_jpdt_197_bai_perron_break_count_rsq_504d_d1(close: pd.Series) -> pd.Series:
    """Approximate Bai-Perron breakpoint count: distinct supF-peaks above 8.85 (α=5%) within 504d."""
    r2 = _log_ret(close) ** 2

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
    return (r2.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_bp, raw=True)).diff()


def f38_jpdt_198_andrews_supf_mean_r_252d_d1(close: pd.Series) -> pd.Series:
    """Andrews supF test for unknown breakpoint in mean(r) over 252d."""
    r = _log_ret(close)

    def _supf(w):
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
            f = (tss - rss) / (rss / (n - 2)) if rss > 0 else 0.0
            if f > best:
                best = f
        return float(best)
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_supf, raw=True)).diff()


def f38_jpdt_199_lo_mackinlay_var_ratio_q5_252d_d1(close: pd.Series) -> pd.Series:
    """Lo-MacKinlay variance ratio at lag q=5 of log-returns over 252d."""
    r = _log_ret(close)
    v1 = r.rolling(YDAYS, min_periods=QDAYS).var()
    rk = _safe_log(close).diff(WDAYS)
    vk = rk.rolling(YDAYS, min_periods=QDAYS).var() / WDAYS
    return (_safe_div(vk, v1)).diff()


def f38_jpdt_200_jarque_bera_r_252d_d1(close: pd.Series) -> pd.Series:
    """Jarque-Bera statistic on log-returns over 252d: n/6·(S² + (K-3)²/4)."""
    r = _log_ret(close)
    sk = r.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    return ((YDAYS / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)).diff()


def f38_jpdt_201_anderson_darling_normal_r_252d_d1(close: pd.Series) -> pd.Series:
    """Anderson-Darling distance from Gaussian on log-returns over 252d."""
    r = _log_ret(close)

    def _ad(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        from math import erf
        ww = np.sort((ww - ww.mean()) / (ww.std() + 1e-12))
        Phi = 0.5 * (1.0 + np.array([erf(x / np.sqrt(2.0)) for x in ww]))
        Phi = np.clip(Phi, 1e-10, 1.0 - 1e-10)
        i = np.arange(1, n + 1)
        ad = -n - (1.0 / n) * np.sum((2 * i - 1) * (np.log(Phi) + np.log(1.0 - Phi[::-1])))
        return float(ad)
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_ad, raw=True)).diff()


def f38_jpdt_202_ks_distance_normal_r_252d_d1(close: pd.Series) -> pd.Series:
    """KS distance of log-returns from standard-Gaussian CDF over 252d."""
    r = _log_ret(close)

    def _ks(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        from math import erf
        z = np.sort((ww - ww.mean()) / (ww.std() + 1e-12))
        F = 0.5 * (1.0 + np.array([erf(x / np.sqrt(2.0)) for x in z]))
        emp = np.arange(1, n + 1) / n
        d = np.max(np.maximum(np.abs(emp - F), np.abs((emp - 1.0 / n) - F)))
        return float(d)
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_ks, raw=True)).diff()


def f38_jpdt_203_student_t_dof_mom_r_252d_d1(close: pd.Series) -> pd.Series:
    """Estimated Student-t d.o.f. via method-of-moments on kurtosis of r over 252d."""
    r = _log_ret(close)
    kt = r.rolling(YDAYS, min_periods=QDAYS).kurt() + 3.0  # convert excess kurt to raw kurt
    # For Student-t with ν d.o.f., kurt = 3·(ν−2)/(ν−4) for ν>4 → ν = (4·kurt−6)/(kurt−3)
    return (_safe_div(4.0 * kt - 6.0, kt - 3.0).where(kt > 3.05, np.nan).clip(lower=4.5, upper=200.0)).diff()


def f38_jpdt_204_cornish_fisher_var_adj_252d_d1(close: pd.Series) -> pd.Series:
    """Cornish-Fisher VaR adjustment magnitude at α=99% over 252d (skew/kurt correction)."""
    r = _log_ret(close)
    sk = r.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    z = 2.3263  # 99% Gaussian quantile
    adj = (z ** 2 - 1.0) * sk / 6.0 + (z ** 3 - 3 * z) * kt / 24.0 - (2 * z ** 3 - 5 * z) * (sk ** 2) / 36.0
    return (adj.abs()).diff()


def f38_jpdt_205_mcculloch_levy_alpha_252d_d1(close: pd.Series) -> pd.Series:
    """Lévy α-stable index via McCulloch quantile ratio over 252d: clipped to α∈(0.5, 2.0)."""
    r = _log_ret(close)

    def _alpha(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        q5, q25, q75, q95 = np.quantile(ww, [0.05, 0.25, 0.75, 0.95])
        denom = q75 - q25
        if denom <= 0:
            return np.nan
        v_alpha = (q95 - q5) / denom
        # Linear interp from McCulloch (1986) Table I (selected points):
        # alpha=2.0 → v=2.439, alpha=1.5 → v=3.073, alpha=1.0 → v=4.451, alpha=0.5 → v=11.62
        return float(np.interp(v_alpha,
                               [2.439, 3.073, 4.451, 11.62],
                               [2.0, 1.5, 1.0, 0.5]))
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_alpha, raw=True)).diff()


def f38_jpdt_206_marubozu_count_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where |close−open|/(high−low) > 0.9 AND range in top decile over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_ratio = (close - open).abs() / rng
    p90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (((body_ratio > 0.9) & (rng > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_207_upper_lower_shadow_asym_top_decile_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ((H−max(O,C)) − (min(O,C)−L)) restricted to top-decile-range bars over 252d."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    upper = high - body_hi
    lower = body_lo - low
    rng = (high - low)
    p90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    sel = (upper - lower).where(rng > p90, np.nan)
    return (sel.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f38_jpdt_208_clv_extreme_count_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where |CLV|=(2C−H−L)/(H−L) > 0.8 AND range in top decile over 252d."""
    rng = (high - low).replace(0, np.nan)
    clv = (2.0 * close - high - low) / rng
    p90 = (high - low).rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (((clv.abs() > 0.8) & ((high - low) > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_209_persistent_neg_clv_big_bars_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of CLV<−0.5 (close-near-low) bars in top-decile-range subset over 252d — distribution signature."""
    rng = (high - low).replace(0, np.nan)
    clv = (2.0 * close - high - low) / rng
    p90 = (high - low).rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (((clv < -0.5) & ((high - low) > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_210_parkinson_over_rv_ratio_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson-vol² / RV ratio over 21d — intra-bar-jump detector (>1 indicates intra-bar burst)."""
    pk = (_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0))
    pk_sum = pk.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(pk_sum, _rv(_log_ret(close), MDAYS))).diff()


def f38_jpdt_211_gk_over_parkinson_ratio_21d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass vol² / Parkinson vol² ratio over 21d — captures OHLC asymmetry."""
    a = 0.5 * (_safe_log(high) - _safe_log(low)) ** 2
    b = (2.0 * np.log(2.0) - 1.0) * (_safe_log(close) - _safe_log(open)) ** 2
    gk = (a - b).rolling(MDAYS, min_periods=WDAYS).mean()
    pk = ((_safe_log(high) - _safe_log(low)) ** 2 / (4.0 * np.log(2.0))).rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(gk, pk)).diff()


def f38_jpdt_212_vol_weighted_jump_variation_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted jump variation: Σ r²·log(volume) on top-decile |r| days over 63d."""
    r = _log_ret(close)
    a = r.abs()
    p90 = a.rolling(QDAYS, min_periods=MDAYS).quantile(0.90)
    mask = a > p90
    sel = (r ** 2 * _safe_log(volume)).where(mask, 0.0)
    return (sel.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f38_jpdt_213_amihud_illiquidity_on_jump_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity (|r|/dollar-volume) restricted to 3σ_21d jump days, mean over 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dv = close * volume
    am = _safe_div(r.abs(), dv)
    sel = am.where(r.abs() > 3 * sig, np.nan)
    return (sel.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f38_jpdt_214_kyle_lambda_proxy_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Kyle's-λ proxy: rolling 63d slope of r on signed-dollar-volume (sign(r)·close·volume)."""
    r = _log_ret(close)
    sv = np.sign(r) * close * volume
    cov = r.rolling(QDAYS, min_periods=MDAYS).cov(sv)
    var = sv.rolling(QDAYS, min_periods=MDAYS).var()
    return (_safe_div(cov, var)).diff()


def f38_jpdt_215_obv_slope_around_jumps_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 5d-slope on bars following 3σ_21d jumps, mean over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    obv = (np.sign(r) * volume).cumsum()
    obv_slope = _rolling_slope(obv, WDAYS)
    sel = obv_slope.where(r.abs() > 3 * sig, np.nan)
    return (sel.rolling(YDAYS, min_periods=QDAYS).mean()).diff()


def f38_jpdt_216_var_volz_on_jump_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Variance of volume z-score on 3σ_21d jump days within 63d — dispersion of vol-on-jump."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    sel = vz.where(r.abs() > 3 * sig, np.nan)
    return (sel.rolling(QDAYS, min_periods=MDAYS).var()).diff()


def f38_jpdt_217_parabolic_acceleration_index_63d_d1(close: pd.Series) -> pd.Series:
    """Quadratic-fit coefficient on log(close) vs time over 63d — parabolic acceleration."""
    lp = _safe_log(close)

    def _quad(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < MDAYS:
            return np.nan
        x = np.arange(n, dtype=float)
        a, b, c = np.polyfit(x, ww, 2)
        return float(a)
    return (lp.rolling(QDAYS, min_periods=MDAYS).apply(_quad, raw=True)).diff()


def f38_jpdt_218_vertical_rise_streak_21d_d1(close: pd.Series) -> pd.Series:
    """Longest run of consecutive days with positive r > σ_prior21 within trailing 21d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > sig).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return float(m)
    return (up.rolling(MDAYS, min_periods=WDAYS).apply(_run, raw=True)).diff()


def f38_jpdt_219_buying_climax_count_252d_d1(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff buying-climax count: bar makes 252d-high AND closes red AND volume in top decile over 252d."""
    r = _log_ret(close)
    new_high = (high == high.rolling(YDAYS, min_periods=QDAYS).max())
    red = r < 0
    p90v = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    big_vol = volume > p90v
    flag = (new_high & red & big_vol).astype(float)
    return (flag.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_220_three_bar_reversal_count_252d_d1(close: pd.Series) -> pd.Series:
    """3-bar reversal count: two strong-up bars then a strong-down bar exceeding both, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up1 = r.shift(2) > sig.shift(2)
    up2 = r.shift(1) > sig.shift(1)
    dn = (r < -sig) & (r.abs() > (r.shift(1) + r.shift(2)))
    return ((up1 & up2 & dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_221_island_reversal_count_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Island reversal: gap-up bar followed within 5 days by gap-down with no price overlap, over 252d."""
    pc = close.shift(1)
    gap_up = (open > high.shift(1)) & (low > high.shift(1))
    gap_dn = (open < low.shift(1)) & (high < low.shift(1))
    # Pattern: gap-down on bar t with a gap-up in [t-5..t-1]
    has_recent_gap_up = gap_up.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5
    flag = (gap_dn & has_recent_gap_up).astype(float)
    return (flag.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f38_jpdt_222_drawdown_velocity_21d_d1(close: pd.Series) -> pd.Series:
    """Rolling 21d slope of (running 252d max − close) — drawdown velocity."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = rmax - close
    return (_rolling_slope(dd, MDAYS)).diff()


def f38_jpdt_223_underwater_duration_d1(close: pd.Series) -> pd.Series:
    """Bars below running 252d max (underwater duration)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    underwater = (close < rmax).astype(int).fillna(0).values
    out = np.zeros(len(underwater), dtype=float)
    cur = 0
    for i, v in enumerate(underwater):
        cur = cur + 1 if v == 1 else 0
        out[i] = cur
    return (pd.Series(out, index=close.index)).diff()


def f38_jpdt_224_ulcer_index_252d_d1(close: pd.Series) -> pd.Series:
    """Ulcer Index: RMS of percentage drawdowns from running 252d max over 252d window."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_pct = (close / rmax - 1.0) * 100.0
    return (np.sqrt((dd_pct ** 2).rolling(YDAYS, min_periods=QDAYS).mean())).diff()


def f38_jpdt_225_calmar_ratio_252d_d1(close: pd.Series) -> pd.Series:
    """Calmar ratio: 252d log-return / max drawdown (from 252d-running max) over 252d."""
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (1.0 - close / rmax).rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(r252, dd)).diff()


# ============================================================
#                         REGISTRY 151-225 (d1)
# ============================================================

JUMP_DETECTION_SIGNATURE_D1_REGISTRY_151_225 = {
    "f38_jpdt_151_jiang_oomen_swv_diff_21d_d1": {"inputs": ["close"], "func": f38_jpdt_151_jiang_oomen_swv_diff_21d_d1},
    "f38_jpdt_152_jiang_oomen_swv_ratio_63d_d1": {"inputs": ["close"], "func": f38_jpdt_152_jiang_oomen_swv_ratio_63d_d1},
    "f38_jpdt_153_realized_3rd_moment_21d_d1": {"inputs": ["close"], "func": f38_jpdt_153_realized_3rd_moment_21d_d1},
    "f38_jpdt_154_realized_3rd_moment_252d_d1": {"inputs": ["close"], "func": f38_jpdt_154_realized_3rd_moment_252d_d1},
    "f38_jpdt_155_realized_quarticity_21d_d1": {"inputs": ["close"], "func": f38_jpdt_155_realized_quarticity_21d_d1},
    "f38_jpdt_156_realized_quarticity_252d_d1": {"inputs": ["close"], "func": f38_jpdt_156_realized_quarticity_252d_d1},
    "f38_jpdt_157_realized_5th_moment_63d_d1": {"inputs": ["close"], "func": f38_jpdt_157_realized_5th_moment_63d_d1},
    "f38_jpdt_158_realized_6th_moment_63d_d1": {"inputs": ["close"], "func": f38_jpdt_158_realized_6th_moment_63d_d1},
    "f38_jpdt_159_realized_skewness_amaya_21d_d1": {"inputs": ["close"], "func": f38_jpdt_159_realized_skewness_amaya_21d_d1},
    "f38_jpdt_160_realized_kurtosis_amaya_63d_d1": {"inputs": ["close"], "func": f38_jpdt_160_realized_kurtosis_amaya_63d_d1},
    "f38_jpdt_161_tripower_variation_63d_d1": {"inputs": ["close"], "func": f38_jpdt_161_tripower_variation_63d_d1},
    "f38_jpdt_162_quadpower_variation_252d_d1": {"inputs": ["close"], "func": f38_jpdt_162_quadpower_variation_252d_d1},
    "f38_jpdt_163_minrv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_163_minrv_63d_d1},
    "f38_jpdt_164_medrv_252d_d1": {"inputs": ["close"], "func": f38_jpdt_164_medrv_252d_d1},
    "f38_jpdt_165_minrv_over_rv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_165_minrv_over_rv_63d_d1},
    "f38_jpdt_166_medrv_over_rv_252d_d1": {"inputs": ["close"], "func": f38_jpdt_166_medrv_over_rv_252d_d1},
    "f38_jpdt_167_tpv_over_bv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_167_tpv_over_bv_63d_d1},
    "f38_jpdt_168_quadpower_quarticity_252d_d1": {"inputs": ["close"], "func": f38_jpdt_168_quadpower_quarticity_252d_d1},
    "f38_jpdt_169_bns_z_linear_63d_d1": {"inputs": ["close"], "func": f38_jpdt_169_bns_z_linear_63d_d1},
    "f38_jpdt_170_bns_z_ratio_63d_d1": {"inputs": ["close"], "func": f38_jpdt_170_bns_z_ratio_63d_d1},
    "f38_jpdt_171_bns_z_log_63d_d1": {"inputs": ["close"], "func": f38_jpdt_171_bns_z_log_63d_d1},
    "f38_jpdt_172_aitsahalia_jacod_ratio_63d_d1": {"inputs": ["close"], "func": f38_jpdt_172_aitsahalia_jacod_ratio_63d_d1},
    "f38_jpdt_173_aitsahalia_jacod_activity_index_252d_d1": {"inputs": ["close"], "func": f38_jpdt_173_aitsahalia_jacod_activity_index_252d_d1},
    "f38_jpdt_174_abd_gumbel_jump_count_21d_d1": {"inputs": ["close"], "func": f38_jpdt_174_abd_gumbel_jump_count_21d_d1},
    "f38_jpdt_175_mancini_truncated_power_var_p4_63d_d1": {"inputs": ["close"], "func": f38_jpdt_175_mancini_truncated_power_var_p4_63d_d1},
    "f38_jpdt_176_lee_hannig_wavelet_jump_count_63d_d1": {"inputs": ["close"], "func": f38_jpdt_176_lee_hannig_wavelet_jump_count_63d_d1},
    "f38_jpdt_177_pot_gpd_scale_252d_d1": {"inputs": ["close"], "func": f38_jpdt_177_pot_gpd_scale_252d_d1},
    "f38_jpdt_178_pot_gpd_shape_252d_d1": {"inputs": ["close"], "func": f38_jpdt_178_pot_gpd_shape_252d_d1},
    "f38_jpdt_179_mean_excess_slope_p90_252d_d1": {"inputs": ["close"], "func": f38_jpdt_179_mean_excess_slope_p90_252d_d1},
    "f38_jpdt_180_gev_location_blockmax_21bars_252d_d1": {"inputs": ["close"], "func": f38_jpdt_180_gev_location_blockmax_21bars_252d_d1},
    "f38_jpdt_181_gev_scale_blockmax_21bars_252d_d1": {"inputs": ["close"], "func": f38_jpdt_181_gev_scale_blockmax_21bars_252d_d1},
    "f38_jpdt_182_tail_dep_lag1_p90_252d_d1": {"inputs": ["close"], "func": f38_jpdt_182_tail_dep_lag1_p90_252d_d1},
    "f38_jpdt_183_reiss_thomas_tail_idx_252d_d1": {"inputs": ["close"], "func": f38_jpdt_183_reiss_thomas_tail_idx_252d_d1},
    "f38_jpdt_184_max_absret_63d_over_252d_ratio_d1": {"inputs": ["close"], "func": f38_jpdt_184_max_absret_63d_over_252d_ratio_d1},
    "f38_jpdt_185_p99_over_p50_absret_252d_d1": {"inputs": ["close"], "func": f38_jpdt_185_p99_over_p50_absret_252d_d1},
    "f38_jpdt_186_p99_count_over_p95_count_252d_d1": {"inputs": ["close"], "func": f38_jpdt_186_p99_count_over_p95_count_252d_d1},
    "f38_jpdt_187_hawkes_branching_ratio_252d_d1": {"inputs": ["close"], "func": f38_jpdt_187_hawkes_branching_ratio_252d_d1},
    "f38_jpdt_188_dist_from_criticality_252d_d1": {"inputs": ["close"], "func": f38_jpdt_188_dist_from_criticality_252d_d1},
    "f38_jpdt_189_intensity_now_over_long_run_avg_63d_d1": {"inputs": ["close"], "func": f38_jpdt_189_intensity_now_over_long_run_avg_63d_d1},
    "f38_jpdt_190_fano_factor_jump_counts_252d_d1": {"inputs": ["close"], "func": f38_jpdt_190_fano_factor_jump_counts_252d_d1},
    "f38_jpdt_191_allan_variance_jump_counts_252d_d1": {"inputs": ["close"], "func": f38_jpdt_191_allan_variance_jump_counts_252d_d1},
    "f38_jpdt_192_ogata_residual_252d_d1": {"inputs": ["close"], "func": f38_jpdt_192_ogata_residual_252d_d1},
    "f38_jpdt_193_lempel_ziv_sign_complexity_252d_d1": {"inputs": ["close"], "func": f38_jpdt_193_lempel_ziv_sign_complexity_252d_d1},
    "f38_jpdt_194_inclan_tiao_cusum_sq_252d_d1": {"inputs": ["close"], "func": f38_jpdt_194_inclan_tiao_cusum_sq_252d_d1},
    "f38_jpdt_195_icss_break_count_504d_d1": {"inputs": ["close"], "func": f38_jpdt_195_icss_break_count_504d_d1},
    "f38_jpdt_196_bai_perron_supF_rsq_252d_d1": {"inputs": ["close"], "func": f38_jpdt_196_bai_perron_supF_rsq_252d_d1},
    "f38_jpdt_197_bai_perron_break_count_rsq_504d_d1": {"inputs": ["close"], "func": f38_jpdt_197_bai_perron_break_count_rsq_504d_d1},
    "f38_jpdt_198_andrews_supf_mean_r_252d_d1": {"inputs": ["close"], "func": f38_jpdt_198_andrews_supf_mean_r_252d_d1},
    "f38_jpdt_199_lo_mackinlay_var_ratio_q5_252d_d1": {"inputs": ["close"], "func": f38_jpdt_199_lo_mackinlay_var_ratio_q5_252d_d1},
    "f38_jpdt_200_jarque_bera_r_252d_d1": {"inputs": ["close"], "func": f38_jpdt_200_jarque_bera_r_252d_d1},
    "f38_jpdt_201_anderson_darling_normal_r_252d_d1": {"inputs": ["close"], "func": f38_jpdt_201_anderson_darling_normal_r_252d_d1},
    "f38_jpdt_202_ks_distance_normal_r_252d_d1": {"inputs": ["close"], "func": f38_jpdt_202_ks_distance_normal_r_252d_d1},
    "f38_jpdt_203_student_t_dof_mom_r_252d_d1": {"inputs": ["close"], "func": f38_jpdt_203_student_t_dof_mom_r_252d_d1},
    "f38_jpdt_204_cornish_fisher_var_adj_252d_d1": {"inputs": ["close"], "func": f38_jpdt_204_cornish_fisher_var_adj_252d_d1},
    "f38_jpdt_205_mcculloch_levy_alpha_252d_d1": {"inputs": ["close"], "func": f38_jpdt_205_mcculloch_levy_alpha_252d_d1},
    "f38_jpdt_206_marubozu_count_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_206_marubozu_count_252d_d1},
    "f38_jpdt_207_upper_lower_shadow_asym_top_decile_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_207_upper_lower_shadow_asym_top_decile_252d_d1},
    "f38_jpdt_208_clv_extreme_count_252d_d1": {"inputs": ["high", "low", "close"], "func": f38_jpdt_208_clv_extreme_count_252d_d1},
    "f38_jpdt_209_persistent_neg_clv_big_bars_252d_d1": {"inputs": ["high", "low", "close"], "func": f38_jpdt_209_persistent_neg_clv_big_bars_252d_d1},
    "f38_jpdt_210_parkinson_over_rv_ratio_21d_d1": {"inputs": ["high", "low", "close"], "func": f38_jpdt_210_parkinson_over_rv_ratio_21d_d1},
    "f38_jpdt_211_gk_over_parkinson_ratio_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_211_gk_over_parkinson_ratio_21d_d1},
    "f38_jpdt_212_vol_weighted_jump_variation_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_212_vol_weighted_jump_variation_63d_d1},
    "f38_jpdt_213_amihud_illiquidity_on_jump_days_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_213_amihud_illiquidity_on_jump_days_63d_d1},
    "f38_jpdt_214_kyle_lambda_proxy_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_214_kyle_lambda_proxy_63d_d1},
    "f38_jpdt_215_obv_slope_around_jumps_252d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_215_obv_slope_around_jumps_252d_d1},
    "f38_jpdt_216_var_volz_on_jump_days_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_216_var_volz_on_jump_days_63d_d1},
    "f38_jpdt_217_parabolic_acceleration_index_63d_d1": {"inputs": ["close"], "func": f38_jpdt_217_parabolic_acceleration_index_63d_d1},
    "f38_jpdt_218_vertical_rise_streak_21d_d1": {"inputs": ["close"], "func": f38_jpdt_218_vertical_rise_streak_21d_d1},
    "f38_jpdt_219_buying_climax_count_252d_d1": {"inputs": ["close", "high", "volume"], "func": f38_jpdt_219_buying_climax_count_252d_d1},
    "f38_jpdt_220_three_bar_reversal_count_252d_d1": {"inputs": ["close"], "func": f38_jpdt_220_three_bar_reversal_count_252d_d1},
    "f38_jpdt_221_island_reversal_count_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_221_island_reversal_count_252d_d1},
    "f38_jpdt_222_drawdown_velocity_21d_d1": {"inputs": ["close"], "func": f38_jpdt_222_drawdown_velocity_21d_d1},
    "f38_jpdt_223_underwater_duration_d1": {"inputs": ["close"], "func": f38_jpdt_223_underwater_duration_d1},
    "f38_jpdt_224_ulcer_index_252d_d1": {"inputs": ["close"], "func": f38_jpdt_224_ulcer_index_252d_d1},
    "f38_jpdt_225_calmar_ratio_252d_d1": {"inputs": ["close"], "func": f38_jpdt_225_calmar_ratio_252d_d1},
}
