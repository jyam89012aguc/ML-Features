"""return_distribution_moments d1 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Rousseeuw-Croux Sn/Qn / Tukey trimean / biweight midvariance / Hodges-Lehmann /
realized intraday moments / signed jump variation / hyper-skew/kurt /
D-Agostino K2 / Cramer-von-Mises / asymmetric AD / Pearson type / Tukey g-h /
bimodality / Wasserstein distance / conditional moments / skew-of-skew.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _sn_rousseeuw_croux(w):
    """Sn estimator: median over i of median over j!=i of |x_i - x_j|. Times scale = 1.1926."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if n > 80:  # subsample for speed
        step = max(1, n // 80)
        v = v[::step]
        n = v.size
    inner_meds = np.empty(n)
    for i in range(n):
        diffs = np.abs(v - v[i])
        diffs = np.concatenate([diffs[:i], diffs[i+1:]]) if n > 1 else diffs
        inner_meds[i] = np.median(diffs)
    return float(1.1926 * np.median(inner_meds))


def _qn_rousseeuw_croux(w):
    """Qn estimator: c * h-th order statistic of pairwise abs-diffs (i lt j),
    h approx (n choose 2)/4. Scale constant 2.2219 for consistency with normal."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if n > 60:  # subsample
        step = max(1, n // 60)
        v = v[::step]
        n = v.size
    if n < 3:
        return np.nan
    diffs = []
    for i in range(n):
        for j in range(i + 1, n):
            diffs.append(abs(v[i] - v[j]))
    diffs = np.sort(np.asarray(diffs))
    h = int(np.floor(0.25 * n * (n - 1) / 2.0))
    h = max(0, min(h, diffs.size - 1))
    return float(2.2219 * diffs[h])


def _trimean_tukey(w):
    """Tukey trimean: (Q1 + 2*median + Q3) / 4."""
    valid = ~np.isnan(w)
    if valid.sum() < 3:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    q1 = np.percentile(v, 25); q3 = np.percentile(v, 75); med = np.median(v)
    return float((q1 + 2.0 * med + q3) / 4.0)


def _biweight_midvariance(w, c=9.0):
    """Tukey biweight midvariance (robust scale)."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    med = np.median(v)
    mad = np.median(np.abs(v - med))
    if mad == 0:
        return 0.0
    u = (v - med) / (c * mad)
    mask = (np.abs(u) < 1.0)
    if mask.sum() < 3:
        return np.nan
    a = ((v[mask] - med) ** 2) * ((1 - u[mask] ** 2) ** 4)
    b = (1 - u[mask] ** 2) * (1 - 5 * u[mask] ** 2)
    num = n * float(a.sum())
    den = float(b.sum()) ** 2
    if den == 0:
        return np.nan
    return float(num / den)


def _hodges_lehmann(w):
    """Hodges-Lehmann pseudomedian: median of pairwise averages."""
    valid = ~np.isnan(w)
    if valid.sum() < 3:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    if n > 60:
        step = max(1, n // 60)
        v = v[::step]
        n = v.size
    pairs = []
    for i in range(n):
        for j in range(i, n):
            pairs.append(0.5 * (v[i] + v[j]))
    return float(np.median(pairs))


def _huber_m_scale(w, k=1.5):
    """One-step M-estimator scale (Huber-psi) on residuals from median."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    med = np.median(v)
    mad = np.median(np.abs(v - med))
    if mad == 0:
        return 0.0
    sigma = 1.4826 * mad
    u = (v - med) / sigma
    psi = np.where(np.abs(u) <= k, u, k * np.sign(u))
    return float(sigma * np.sqrt(np.mean(psi ** 2)))


def _dagostino_k2(w):
    """D-Agostino-Pearson K2 omnibus normality test stat."""
    valid = ~np.isnan(w)
    if valid.sum() < 8:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    z = (v - m) / sd
    sk = float(np.mean(z ** 3))
    kt = float(np.mean(z ** 4) - 3.0)
    # D-Agostino Z(b1) for skew
    y = sk * np.sqrt(((n + 1) * (n + 3)) / (6.0 * (n - 2)))
    beta2 = 3.0 * (n * n + 27.0 * n - 70.0) * (n + 1) * (n + 3) / ((n - 2) * (n + 5) * (n + 7) * (n + 9))
    if beta2 <= 1.0:
        zb = np.sign(y) * np.sqrt(np.abs(y))
    else:
        W2 = -1.0 + np.sqrt(2.0 * (beta2 - 1.0))
        if W2 <= 1.0:
            return np.nan
        delta = 1.0 / np.sqrt(0.5 * np.log(W2))
        alpha = np.sqrt(2.0 / (W2 - 1.0))
        zb = delta * np.log(y / alpha + np.sqrt((y / alpha) ** 2 + 1.0))
    # D-Agostino Z(b2) for kurt
    e = 3.0 * (n - 1) / (n + 1)
    var_b2 = 24.0 * n * (n - 2) * (n - 3) / ((n + 1) ** 2 * (n + 3) * (n + 5))
    if var_b2 <= 0:
        return np.nan
    x = (kt + 3.0 - e) / np.sqrt(var_b2)
    sqrt_beta1_b2 = 6.0 * (n ** 2 - 5 * n + 2) / ((n + 7) * (n + 9)) * np.sqrt(6.0 * (n + 3) * (n + 5) / (n * (n - 2) * (n - 3)))
    A = 6.0 + 8.0 / sqrt_beta1_b2 * (2.0 / sqrt_beta1_b2 + np.sqrt(1.0 + 4.0 / sqrt_beta1_b2 ** 2))
    if A <= 0:
        return np.nan
    term = 1.0 - 2.0 / (9.0 * A) - ((1.0 - 2.0 / A) / (1.0 + x * np.sqrt(2.0 / (A - 4.0)))) ** (1.0 / 3.0)
    zk = term * np.sqrt(9.0 * A / 2.0)
    return float(zb ** 2 + zk ** 2)


def _cramer_von_mises(w):
    """Cramer-von-Mises test stat against standard normal."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    z = np.sort((v - m) / sd)
    from math import erf, sqrt
    cdf = 0.5 * (1.0 + np.array([erf(zi / sqrt(2.0)) for zi in z]))
    i = np.arange(1, n + 1)
    expected = (2.0 * i - 1.0) / (2.0 * n)
    return float(1.0 / (12.0 * n) + np.sum((cdf - expected) ** 2))


def _ad_asymmetric(w, side='left'):
    """Anderson-Darling-like statistic on one tail only."""
    valid = ~np.isnan(w)
    if valid.sum() < 8:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    z = np.sort((v - m) / sd)
    from math import erf, sqrt
    cdf = 0.5 * (1.0 + np.array([erf(zi / sqrt(2.0)) for zi in z]))
    cdf = np.clip(cdf, 1e-12, 1.0 - 1e-12)
    half = n // 2
    if side == 'left':
        sub = cdf[:half]
        i = np.arange(1, half + 1)
        s = np.sum((2 * i - 1) * np.log(sub) + (2 * (half - i) + 1) * np.log(1.0 - sub))
    else:
        sub = cdf[half:]
        m_sub = sub.size
        i = np.arange(1, m_sub + 1)
        s = np.sum((2 * i - 1) * np.log(sub) + (2 * (m_sub - i) + 1) * np.log(1.0 - sub))
    return float(-(s / max(half, 1)))


def _wasserstein_to_normal(w):
    """1-Wasserstein distance between empirical CDF and N(0,1)."""
    valid = ~np.isnan(w)
    if valid.sum() < 8:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    z = np.sort((v - m) / sd)
    from math import erf, sqrt
    # 1-Wasserstein = integral of |F_emp(x) - F_norm(x)| dx ~= sum of |z_(i) - Phi^-1((i-0.5)/n)|
    pp = (np.arange(1, n + 1) - 0.5) / n
    # Inverse normal CDF approx
    def _norm_ppf(p):
        if p < 0.5:
            return -np.sqrt(-2.0 * np.log(p))
        return np.sqrt(-2.0 * np.log(1.0 - p))
    expected = np.array([_norm_ppf(pi) for pi in pp])
    return float(np.mean(np.abs(z - expected)))


def _bimodality_coefficient(w):
    """SAS bimodality coefficient: (skew^2 + 1) / (kurt + 3 * (n-1)^2 / ((n-2)*(n-3)))."""
    valid = ~np.isnan(w)
    if valid.sum() < 8:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    n = v.size
    m = v.mean(); sd = v.std(ddof=1)
    if sd <= 0:
        return np.nan
    z = (v - m) / sd
    sk = float(np.mean(z ** 3))
    kt = float(np.mean(z ** 4))
    denom = kt + 3.0 * ((n - 1) ** 2) / ((n - 2) * (n - 3))
    if denom == 0:
        return np.nan
    return float((sk ** 2 + 1.0) / denom)


def f41_rdmm_151_sn_rousseeuw_croux_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_sn_rousseeuw_croux, raw=True)
    return out.diff()


def f41_rdmm_152_sn_rousseeuw_croux_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_sn_rousseeuw_croux, raw=True)
    return out.diff()


def f41_rdmm_153_qn_rousseeuw_croux_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_qn_rousseeuw_croux, raw=True)
    return out.diff()


def f41_rdmm_154_qn_rousseeuw_croux_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_qn_rousseeuw_croux, raw=True)
    return out.diff()


def f41_rdmm_155_tukey_trimean_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_trimean_tukey, raw=True)
    return out.diff()


def f41_rdmm_156_tukey_trimean_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_trimean_tukey, raw=True)
    return out.diff()


def f41_rdmm_157_interdecile_range_over_128_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    q90 = r.rolling(63, min_periods=21).quantile(0.9)
    q10 = r.rolling(63, min_periods=21).quantile(0.1)
    out = (q90 - q10) / 1.2816
    return out.diff()


def f41_rdmm_158_biweight_midvariance_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_biweight_midvariance, raw=True)
    return out.diff()


def f41_rdmm_159_hodges_lehmann_pseudomedian_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_hodges_lehmann, raw=True)
    return out.diff()


def f41_rdmm_160_huber_m_scale_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_huber_m_scale, raw=True)
    return out.diff()


def f41_rdmm_161_robust_z_HL_over_Sn_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    hl = r.rolling(63, min_periods=21).apply(_hodges_lehmann, raw=True)
    sn = r.rolling(63, min_periods=21).apply(_sn_rousseeuw_croux, raw=True)
    out = _safe_div(r - hl, sn)
    return out.diff()


def f41_rdmm_162_winsorized_10pct_std_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        lo = np.percentile(v, 10); hi = np.percentile(v, 90)
        v = np.clip(v, lo, hi)
        return float(np.std(v, ddof=1))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_163_trimean_over_std_ratio_log_ret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    tm = r.rolling(63, min_periods=21).apply(_trimean_tukey, raw=True)
    sd = r.rolling(63, min_periods=21).std()
    out = _safe_div(tm, sd)
    return out.diff()


def f41_rdmm_164_qn_over_std_ratio_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    qn = r.rolling(252, min_periods=84).apply(_qn_rousseeuw_croux, raw=True)
    sd = r.rolling(252, min_periods=84).std()
    out = _safe_div(qn, sd)
    return out.diff()


def f41_rdmm_165_mad_vs_qn_disagreement_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    mad = (r - r.rolling(252, min_periods=84).median()).abs().rolling(252, min_periods=84).median() * 1.4826
    qn = r.rolling(252, min_periods=84).apply(_qn_rousseeuw_croux, raw=True)
    out = _safe_div((mad - qn).abs(), qn)
    return out.diff()


def f41_rdmm_166_realized_intraday_skew_OHLC_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    out = intr.rolling(63, min_periods=21).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_167_realized_intraday_kurt_OHLC_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 21:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 4) - 3.0)
    out = intr.rolling(63, min_periods=21).apply(_kt, raw=True)
    return out.diff()


def f41_rdmm_168_signed_jump_var_pos_63d_log_ret_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    pos_jumps = (r ** 2).where(r > 2.0 * sd, 0.0)
    out = pos_jumps.rolling(63, min_periods=21).sum()
    return out.diff()


def f41_rdmm_169_signed_jump_var_neg_63d_log_ret_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    neg_jumps = (r ** 2).where(r < -2.0 * sd, 0.0)
    out = neg_jumps.rolling(63, min_periods=21).sum()
    return out.diff()


def f41_rdmm_170_jump_asym_pos_over_total_252d_log_ret_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    pos = (r ** 2).where(r > 2.0 * sd, 0.0).rolling(252, min_periods=84).sum()
    neg = (r ** 2).where(r < -2.0 * sd, 0.0).rolling(252, min_periods=84).sum()
    out = _safe_div(pos, pos + neg)
    return out.diff()


def f41_rdmm_171_l_skew_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _ls(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = np.sort(w[valid] if not valid.all() else w)
        n = v.size
        if n < 4:
            return np.nan
        i = np.arange(1, n + 1, dtype=float)
        b0 = float(v.mean())
        b1 = float(np.sum((i - 1) * v) / (n * (n - 1)))
        b2 = float(np.sum((i - 1) * (i - 2) * v) / (n * (n - 1) * (n - 2)))
        L1 = b0
        L2 = 2 * b1 - b0
        L3 = 6 * b2 - 6 * b1 + b0
        if L2 == 0:
            return np.nan
        return float(L3 / L2)
    out = r.rolling(504, min_periods=168).apply(_ls, raw=True)
    return out.diff()


def f41_rdmm_172_l_kurt_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _lk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = np.sort(w[valid] if not valid.all() else w)
        n = v.size
        if n < 5:
            return np.nan
        i = np.arange(1, n + 1, dtype=float)
        b0 = float(v.mean())
        b1 = float(np.sum((i - 1) * v) / (n * (n - 1)))
        b2 = float(np.sum((i - 1) * (i - 2) * v) / (n * (n - 1) * (n - 2)))
        b3 = float(np.sum((i - 1) * (i - 2) * (i - 3) * v) / (n * (n - 1) * (n - 2) * (n - 3)))
        L2 = 2 * b1 - b0
        L4 = 20 * b3 - 30 * b2 + 12 * b1 - b0
        if L2 == 0:
            return np.nan
        return float(L4 / L2)
    out = r.rolling(504, min_periods=168).apply(_lk, raw=True)
    return out.diff()


def f41_rdmm_173_coskew_log_ret_vs_lag1_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rl = r.shift(1)
    sd_r = r.rolling(252, min_periods=84).std()
    sd_l = rl.rolling(252, min_periods=84).std()
    dev_r = r - r.rolling(252, min_periods=84).mean()
    dev_l = rl - rl.rolling(252, min_periods=84).mean()
    coskew = (dev_r * dev_l * dev_l).rolling(252, min_periods=84).mean()
    out = _safe_div(coskew, sd_r * sd_l * sd_l)
    return out.diff()


def f41_rdmm_174_coskew_log_ret_vs_lag5_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rl = r.shift(5)
    sd_r = r.rolling(252, min_periods=84).std()
    sd_l = rl.rolling(252, min_periods=84).std()
    dev_r = r - r.rolling(252, min_periods=84).mean()
    dev_l = rl - rl.rolling(252, min_periods=84).mean()
    coskew = (dev_r * dev_l * dev_l).rolling(252, min_periods=84).mean()
    out = _safe_div(coskew, sd_r * sd_l * sd_l)
    return out.diff()


def f41_rdmm_175_hyper_skew_5th_moment_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _h(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 5))
    out = r.rolling(504, min_periods=168).apply(_h, raw=True)
    return out.diff()


def f41_rdmm_176_hyper_kurt_6th_moment_log_ret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _h(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 6))
    out = r.rolling(504, min_periods=168).apply(_h, raw=True)
    return out.diff()


def f41_rdmm_177_cond_skew_given_abs_above_1sigma_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    big = r.where(r.abs() > sd, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); ssd = v.std(ddof=1)
        if ssd <= 0:
            return np.nan
        return float(np.mean(((v - m) / ssd) ** 3))
    out = big.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_178_cond_kurt_given_abs_above_1sigma_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    big = r.where(r.abs() > sd, np.nan)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); ssd = v.std(ddof=1)
        if ssd <= 0:
            return np.nan
        return float(np.mean(((v - m) / ssd) ** 4) - 3.0)
    out = big.rolling(252, min_periods=84).apply(_kt, raw=True)
    return out.diff()


def f41_rdmm_179_cond_mean_given_large_down_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    big_dn = r.where(r < -sd, np.nan)
    out = big_dn.rolling(252, min_periods=84).mean()
    return out.diff()


def f41_rdmm_180_cond_mean_given_large_up_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    big_up = r.where(r > sd, np.nan)
    out = big_up.rolling(252, min_periods=84).mean()
    return out.diff()


def f41_rdmm_181_dagostino_skew_z_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 8:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3))
        y = sk * np.sqrt(((n + 1) * (n + 3)) / (6.0 * (n - 2)))
        beta2 = 3.0 * (n * n + 27.0 * n - 70.0) * (n + 1) * (n + 3) / ((n - 2) * (n + 5) * (n + 7) * (n + 9))
        if beta2 <= 1.0:
            return float(np.sign(y) * np.sqrt(np.abs(y)))
        W2 = -1.0 + np.sqrt(2.0 * (beta2 - 1.0))
        if W2 <= 1.0:
            return np.nan
        delta = 1.0 / np.sqrt(0.5 * np.log(W2))
        alpha = np.sqrt(2.0 / (W2 - 1.0))
        return float(delta * np.log(y / alpha + np.sqrt((y / alpha) ** 2 + 1.0)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_182_dagostino_kurt_z_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 8:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        kt = float(np.mean(z ** 4) - 3.0)
        e = 3.0 * (n - 1) / (n + 1)
        var_b2 = 24.0 * n * (n - 2) * (n - 3) / ((n + 1) ** 2 * (n + 3) * (n + 5))
        if var_b2 <= 0:
            return np.nan
        x = (kt + 3.0 - e) / np.sqrt(var_b2)
        sqrt_beta1_b2 = 6.0 * (n ** 2 - 5 * n + 2) / ((n + 7) * (n + 9)) * np.sqrt(6.0 * (n + 3) * (n + 5) / (n * (n - 2) * (n - 3)))
        A = 6.0 + 8.0 / sqrt_beta1_b2 * (2.0 / sqrt_beta1_b2 + np.sqrt(1.0 + 4.0 / sqrt_beta1_b2 ** 2))
        if A <= 0:
            return np.nan
        term = 1.0 - 2.0 / (9.0 * A) - ((1.0 - 2.0 / A) / (1.0 + x * np.sqrt(2.0 / (A - 4.0)))) ** (1.0 / 3.0)
        return float(term * np.sqrt(9.0 * A / 2.0))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_183_dagostino_k2_omnibus_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_dagostino_k2, raw=True)
    return out.diff()


def f41_rdmm_184_cramer_von_mises_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_cramer_von_mises, raw=True)
    return out.diff()


def f41_rdmm_185_geary_a_test_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 8:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(np.abs(v - m)) / sd)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_186_ad_left_tail_only_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _ad_asymmetric(w, 'left'), raw=True)
    return out.diff()


def f41_rdmm_187_ad_right_tail_only_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _ad_asymmetric(w, 'right'), raw=True)
    return out.diff()


def f41_rdmm_188_ad_asymmetry_left_minus_right_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    left = r.rolling(252, min_periods=84).apply(lambda w: _ad_asymmetric(w, 'left'), raw=True)
    right = r.rolling(252, min_periods=84).apply(lambda w: _ad_asymmetric(w, 'right'), raw=True)
    out = left - right
    return out.diff()


def f41_rdmm_189_normality_reject_count_4tests_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3))
        kt = float(np.mean(z ** 4) - 3.0)
        jb = (n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
        geary = float(np.mean(np.abs(v - m)) / sd)
        cvm = _cramer_von_mises(w)
        k2 = _dagostino_k2(w)
        rej = 0
        if jb > 5.991: rej += 1
        if geary > 0.7979 + 1.96 * np.sqrt(0.2146 / n): rej += 1
        if not np.isnan(cvm) and cvm > 0.461: rej += 1
        if not np.isnan(k2) and k2 > 5.991: rej += 1
        return float(rej)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_190_normality_rejected_5pct_any_test_indicator_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3))
        kt = float(np.mean(z ** 4) - 3.0)
        jb = (n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
        k2 = _dagostino_k2(w)
        if jb > 5.991:
            return 1.0
        if not np.isnan(k2) and k2 > 5.991:
            return 1.0
        return 0.0
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_191_bars_since_normality_rejection_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        jb = (n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
        return 1.0 if jb > 5.991 else 0.0
    rej = r.rolling(252, min_periods=84).apply(_f, raw=True).fillna(0).astype(bool)
    arr = rej.values
    n_total = arr.size
    out_arr = np.full(n_total, np.nan)
    last = -1
    for i in range(n_total):
        if arr[i]: last = i
        if last >= 0: out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=r.index)
    return out.diff()


def f41_rdmm_192_current_normality_rejection_streak_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        jb = (n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
        return 1.0 if jb > 5.991 else 0.0
    rej = r.rolling(252, min_periods=84).apply(_f, raw=True)
    ri = rej.fillna(0).astype(int)
    block = (ri != ri.shift(1)).fillna(False).cumsum()
    st = ri.groupby(block).cumcount().astype(float)
    out = (st * (ri > 0)).where(rej.notna(), np.nan)
    return out.diff()


def f41_rdmm_193_jb_minus_dagostino_k2_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _jb(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        return float((n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0))
    jb = r.rolling(252, min_periods=84).apply(_jb, raw=True)
    k2 = r.rolling(252, min_periods=84).apply(_dagostino_k2, raw=True)
    out = jb - k2
    return out.diff()


def f41_rdmm_194_wasserstein_distance_to_normal_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_wasserstein_to_normal, raw=True)
    return out.diff()


def f41_rdmm_195_ks_left_half_vs_right_half_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = np.sort((v - m) / sd)
        half = n // 2
        from math import erf, sqrt
        cdf = 0.5 * (1.0 + np.array([erf(zi / sqrt(2.0)) for zi in z]))
        expected = (np.arange(1, n + 1) - 0.5) / n
        diff = np.abs(cdf - expected)
        left_max = float(diff[:half].max()) if half > 0 else 0.0
        right_max = float(diff[half:].max()) if half < n else 0.0
        return left_max - right_max
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_196_bimodality_coefficient_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_bimodality_coefficient, raw=True)
    return out.diff()


def f41_rdmm_197_gen_lambda_lambda3_skew_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        p25 = np.percentile(v, 25); p75 = np.percentile(v, 75); p50 = np.percentile(v, 50)
        iqr = p75 - p25
        if iqr == 0:
            return np.nan
        return float((p25 + p75 - 2 * p50) / iqr)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_198_gen_lambda_lambda4_kurt_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        p10 = np.percentile(v, 10); p90 = np.percentile(v, 90); p25 = np.percentile(v, 25); p75 = np.percentile(v, 75)
        iqr = p75 - p25
        if iqr == 0:
            return np.nan
        return float((p90 - p10) / iqr)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_199_tukey_g_skew_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        med = np.median(v)
        pl = np.percentile(v, 25); pu = np.percentile(v, 75)
        if abs(pu - med) < 1e-12 or abs(med - pl) < 1e-12:
            return np.nan
        return float(np.log((pu - med) / (med - pl)) / 0.6745)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_200_tukey_h_kurt_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        z_sorted = np.sort(np.abs(z))
        n = z.size
        pp = np.percentile(z_sorted, 90)
        if pp < 1.5:
            return 0.0
        return float((np.log(pp / 1.5)) / (0.5 * pp * pp))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_201_asymmetric_laplace_asym_param_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        pos = v[v > 0]; neg = v[v < 0]
        if pos.size < 3 or neg.size < 3:
            return np.nan
        return float(np.mean(pos) / (-np.mean(neg)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_202_nig_kurt_adj_skew_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4))
        if kt <= 3:
            return np.nan
        return float(sk / np.sqrt(kt - 3))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_203_lambert_w_gauss_heavy_tail_delta_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        kt = float(np.mean(((v - m) / sd) ** 4))
        if kt <= 3:
            return 0.0
        return float(0.25 * np.log(max(kt - 3.0, 1e-9) / 3.0 + 1.0))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_204_pareto_upper_tail_alpha_inv_hill_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = np.sort(w[valid] if not valid.all() else w)[::-1]
        k = max(5, v.size // 20)
        if k >= v.size:
            return np.nan
        vk = v[k]
        if vk <= 0:
            return np.nan
        log_v = np.log(np.maximum(v[:k] / vk, 1e-12))
        if log_v.size == 0:
            return np.nan
        return float(np.mean(log_v))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_205_stable_alpha_tail_thickness_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        kt = float(np.mean(((v - m) / sd) ** 4))
        if kt <= 3.0:
            return 2.0
        return float(2.0 / (1.0 + np.log1p(kt - 3.0)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_206_stable_beta_skew_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        sk = float(np.mean(((v - m) / sd) ** 3))
        return float(np.tanh(sk))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_207_wasserstein_distance_to_t5_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = np.sort((v - m) / sd)
        pp = (np.arange(1, n + 1) - 0.5) / n
        # t(5) quantile approx via inverse-CDF heuristic
        def _t5_ppf(p):
            if p < 0.5: return -1.476 * np.sqrt(-2.0 * np.log(p))
            return 1.476 * np.sqrt(-2.0 * np.log(1.0 - p))
        expected = np.array([_t5_ppf(pi) for pi in pp])
        return float(np.mean(np.abs(z - expected)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_208_ks_distance_to_t5_log_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = np.sort((v - m) / sd)
        pp = (np.arange(1, n + 1) - 0.5) / n
        def _t5_ppf(p):
            if p < 0.5: return -1.476 * np.sqrt(-2.0 * np.log(p))
            return 1.476 * np.sqrt(-2.0 * np.log(1.0 - p))
        expected = np.array([_t5_ppf(pi) for pi in pp])
        return float(np.max(np.abs(z - expected)))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_209_bowley_moors_agreement_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        moment_sk = float(np.mean(((v - m) / sd) ** 3))
        q25 = np.percentile(v, 25); q50 = np.percentile(v, 50); q75 = np.percentile(v, 75)
        iqr = q75 - q25
        if iqr == 0:
            return np.nan
        bowley = (q25 + q75 - 2 * q50) / iqr
        return float(np.sign(moment_sk) == np.sign(bowley))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_210_multimodal_indicator_BC_above_555_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bc = r.rolling(252, min_periods=84).apply(_bimodality_coefficient, raw=True)
    out = (bc > 0.555).astype(float).where(bc.notna(), np.nan)
    return out.diff()


def f41_rdmm_211_mean_return_high_vol_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    med_v = volume.rolling(63, min_periods=21).median()
    high_v = r.where(volume > med_v, np.nan)
    out = high_v.rolling(63, min_periods=21).mean()
    return out.diff()


def f41_rdmm_212_mean_return_low_vol_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    med_v = volume.rolling(63, min_periods=21).median()
    low_v = r.where(volume < med_v, np.nan)
    out = low_v.rolling(63, min_periods=21).mean()
    return out.diff()


def f41_rdmm_213_std_return_high_vol_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    med_v = volume.rolling(63, min_periods=21).median()
    high_v = r.where(volume > med_v, np.nan)
    out = high_v.rolling(63, min_periods=21).std()
    return out.diff()


def f41_rdmm_214_std_return_low_vol_days_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    med_v = volume.rolling(63, min_periods=21).median()
    low_v = r.where(volume < med_v, np.nan)
    out = low_v.rolling(63, min_periods=21).std()
    return out.diff()


def f41_rdmm_215_skew_return_high_vol_days_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    med_v = volume.rolling(252, min_periods=84).median()
    high_v = r.where(volume > med_v, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    out = high_v.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_216_cond_skew_after_neg_ret_day_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cond_r = r.where(r.shift(1) < 0, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    out = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_217_cond_skew_after_pos_ret_day_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    cond_r = r.where(r.shift(1) > 0, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    out = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_218_cond_kurt_given_high_vol_regime_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    high_rv = r.where(rv21 > med_rv, np.nan)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 4) - 3.0)
    out = high_rv.rolling(252, min_periods=84).apply(_kt, raw=True)
    return out.diff()


def f41_rdmm_219_mean_shift_2sigma_indicator_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    m21 = r.rolling(21, min_periods=7).mean()
    m252 = r.rolling(252, min_periods=84).mean()
    sd252 = r.rolling(252, min_periods=84).std() / np.sqrt(21.0)
    out = ((m21 - m252).abs() > 2.0 * sd252).astype(float).where(sd252.notna(), np.nan)
    return out.diff()


def f41_rdmm_220_ks_distshift_63d_vs_prior_63d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 80:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        half = n // 2
        a = np.sort(v[:half]); b = np.sort(v[half:])
        grid = np.linspace(min(a.min(), b.min()), max(a.max(), b.max()), 50)
        cdf_a = np.searchsorted(a, grid, 'right') / float(a.size)
        cdf_b = np.searchsorted(b, grid, 'right') / float(b.size)
        return float(np.max(np.abs(cdf_a - cdf_b)))
    out = r.rolling(126, min_periods=42).apply(_f, raw=True)
    return out.diff()


def f41_rdmm_221_mean_vs_median_divergence_pct_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    m = r.rolling(252, min_periods=84).mean()
    med = r.rolling(252, min_periods=84).median()
    sd = r.rolling(252, min_periods=84).std()
    out = _safe_div(m - med, sd)
    return out.diff()


def f41_rdmm_222_cond_skew_at_252d_high_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rmax = high.rolling(252, min_periods=84).max()
    near_high = (high >= 0.95 * rmax)
    cond_r = r.where(near_high, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    out = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f41_rdmm_223_skew_of_rolling_21d_skew_over_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    rolling_sk = r.rolling(21, min_periods=7).apply(_sk, raw=True)
    out = rolling_sk.rolling(252, min_periods=84).std()
    return out.diff()


def f41_rdmm_224_kurt_of_rolling_21d_kurt_over_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 4) - 3.0)
    rolling_kt = r.rolling(21, min_periods=7).apply(_kt, raw=True)
    out = rolling_kt.rolling(252, min_periods=84).std()
    return out.diff()


def f41_rdmm_225_comp_distribution_pathology_score_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        n = v.size
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        z = (v - m) / sd
        sk = float(np.mean(z ** 3)); kt = float(np.mean(z ** 4) - 3.0)
        jb = (n / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
        score = 0
        if jb > 5.991: score += 1
        if abs(sk) > 1.0: score += 1
        if kt > 3.0: score += 1
        p90 = np.percentile(v, 90); p10 = np.percentile(v, 10)
        if (p90 - p10) / (sd if sd > 0 else 1) > 3.0: score += 1
        return float(score)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


# ============================================================
#                         REGISTRY 151_225 (d1)
# ============================================================

RETURN_DISTRIBUTION_MOMENTS_D1_REGISTRY_151_225 = {
    "f41_rdmm_151_sn_rousseeuw_croux_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_151_sn_rousseeuw_croux_log_ret_63d_d1},
    "f41_rdmm_152_sn_rousseeuw_croux_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_152_sn_rousseeuw_croux_log_ret_252d_d1},
    "f41_rdmm_153_qn_rousseeuw_croux_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_153_qn_rousseeuw_croux_log_ret_63d_d1},
    "f41_rdmm_154_qn_rousseeuw_croux_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_154_qn_rousseeuw_croux_log_ret_252d_d1},
    "f41_rdmm_155_tukey_trimean_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_155_tukey_trimean_log_ret_63d_d1},
    "f41_rdmm_156_tukey_trimean_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_156_tukey_trimean_log_ret_252d_d1},
    "f41_rdmm_157_interdecile_range_over_128_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_157_interdecile_range_over_128_log_ret_63d_d1},
    "f41_rdmm_158_biweight_midvariance_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_158_biweight_midvariance_log_ret_63d_d1},
    "f41_rdmm_159_hodges_lehmann_pseudomedian_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_159_hodges_lehmann_pseudomedian_log_ret_63d_d1},
    "f41_rdmm_160_huber_m_scale_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_160_huber_m_scale_log_ret_63d_d1},
    "f41_rdmm_161_robust_z_HL_over_Sn_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_161_robust_z_HL_over_Sn_log_ret_63d_d1},
    "f41_rdmm_162_winsorized_10pct_std_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_162_winsorized_10pct_std_log_ret_252d_d1},
    "f41_rdmm_163_trimean_over_std_ratio_log_ret_63d_d1": {"inputs": ["close"], "func": f41_rdmm_163_trimean_over_std_ratio_log_ret_63d_d1},
    "f41_rdmm_164_qn_over_std_ratio_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_164_qn_over_std_ratio_log_ret_252d_d1},
    "f41_rdmm_165_mad_vs_qn_disagreement_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_165_mad_vs_qn_disagreement_log_ret_252d_d1},
    "f41_rdmm_166_realized_intraday_skew_OHLC_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f41_rdmm_166_realized_intraday_skew_OHLC_63d_d1},
    "f41_rdmm_167_realized_intraday_kurt_OHLC_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f41_rdmm_167_realized_intraday_kurt_OHLC_63d_d1},
    "f41_rdmm_168_signed_jump_var_pos_63d_log_ret_d1": {"inputs": ["close"], "func": f41_rdmm_168_signed_jump_var_pos_63d_log_ret_d1},
    "f41_rdmm_169_signed_jump_var_neg_63d_log_ret_d1": {"inputs": ["close"], "func": f41_rdmm_169_signed_jump_var_neg_63d_log_ret_d1},
    "f41_rdmm_170_jump_asym_pos_over_total_252d_log_ret_d1": {"inputs": ["close"], "func": f41_rdmm_170_jump_asym_pos_over_total_252d_log_ret_d1},
    "f41_rdmm_171_l_skew_log_ret_504d_d1": {"inputs": ["close"], "func": f41_rdmm_171_l_skew_log_ret_504d_d1},
    "f41_rdmm_172_l_kurt_log_ret_504d_d1": {"inputs": ["close"], "func": f41_rdmm_172_l_kurt_log_ret_504d_d1},
    "f41_rdmm_173_coskew_log_ret_vs_lag1_252d_d1": {"inputs": ["close"], "func": f41_rdmm_173_coskew_log_ret_vs_lag1_252d_d1},
    "f41_rdmm_174_coskew_log_ret_vs_lag5_252d_d1": {"inputs": ["close"], "func": f41_rdmm_174_coskew_log_ret_vs_lag5_252d_d1},
    "f41_rdmm_175_hyper_skew_5th_moment_log_ret_504d_d1": {"inputs": ["close"], "func": f41_rdmm_175_hyper_skew_5th_moment_log_ret_504d_d1},
    "f41_rdmm_176_hyper_kurt_6th_moment_log_ret_504d_d1": {"inputs": ["close"], "func": f41_rdmm_176_hyper_kurt_6th_moment_log_ret_504d_d1},
    "f41_rdmm_177_cond_skew_given_abs_above_1sigma_252d_d1": {"inputs": ["close"], "func": f41_rdmm_177_cond_skew_given_abs_above_1sigma_252d_d1},
    "f41_rdmm_178_cond_kurt_given_abs_above_1sigma_252d_d1": {"inputs": ["close"], "func": f41_rdmm_178_cond_kurt_given_abs_above_1sigma_252d_d1},
    "f41_rdmm_179_cond_mean_given_large_down_252d_d1": {"inputs": ["close"], "func": f41_rdmm_179_cond_mean_given_large_down_252d_d1},
    "f41_rdmm_180_cond_mean_given_large_up_252d_d1": {"inputs": ["close"], "func": f41_rdmm_180_cond_mean_given_large_up_252d_d1},
    "f41_rdmm_181_dagostino_skew_z_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_181_dagostino_skew_z_log_ret_252d_d1},
    "f41_rdmm_182_dagostino_kurt_z_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_182_dagostino_kurt_z_log_ret_252d_d1},
    "f41_rdmm_183_dagostino_k2_omnibus_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_183_dagostino_k2_omnibus_log_ret_252d_d1},
    "f41_rdmm_184_cramer_von_mises_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_184_cramer_von_mises_log_ret_252d_d1},
    "f41_rdmm_185_geary_a_test_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_185_geary_a_test_log_ret_252d_d1},
    "f41_rdmm_186_ad_left_tail_only_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_186_ad_left_tail_only_log_ret_252d_d1},
    "f41_rdmm_187_ad_right_tail_only_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_187_ad_right_tail_only_log_ret_252d_d1},
    "f41_rdmm_188_ad_asymmetry_left_minus_right_252d_d1": {"inputs": ["close"], "func": f41_rdmm_188_ad_asymmetry_left_minus_right_252d_d1},
    "f41_rdmm_189_normality_reject_count_4tests_252d_d1": {"inputs": ["close"], "func": f41_rdmm_189_normality_reject_count_4tests_252d_d1},
    "f41_rdmm_190_normality_rejected_5pct_any_test_indicator_252d_d1": {"inputs": ["close"], "func": f41_rdmm_190_normality_rejected_5pct_any_test_indicator_252d_d1},
    "f41_rdmm_191_bars_since_normality_rejection_252d_d1": {"inputs": ["close"], "func": f41_rdmm_191_bars_since_normality_rejection_252d_d1},
    "f41_rdmm_192_current_normality_rejection_streak_252d_d1": {"inputs": ["close"], "func": f41_rdmm_192_current_normality_rejection_streak_252d_d1},
    "f41_rdmm_193_jb_minus_dagostino_k2_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_193_jb_minus_dagostino_k2_log_ret_252d_d1},
    "f41_rdmm_194_wasserstein_distance_to_normal_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_194_wasserstein_distance_to_normal_log_ret_252d_d1},
    "f41_rdmm_195_ks_left_half_vs_right_half_252d_d1": {"inputs": ["close"], "func": f41_rdmm_195_ks_left_half_vs_right_half_252d_d1},
    "f41_rdmm_196_bimodality_coefficient_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_196_bimodality_coefficient_log_ret_252d_d1},
    "f41_rdmm_197_gen_lambda_lambda3_skew_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_197_gen_lambda_lambda3_skew_proxy_252d_d1},
    "f41_rdmm_198_gen_lambda_lambda4_kurt_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_198_gen_lambda_lambda4_kurt_proxy_252d_d1},
    "f41_rdmm_199_tukey_g_skew_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_199_tukey_g_skew_proxy_252d_d1},
    "f41_rdmm_200_tukey_h_kurt_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_200_tukey_h_kurt_proxy_252d_d1},
    "f41_rdmm_201_asymmetric_laplace_asym_param_252d_d1": {"inputs": ["close"], "func": f41_rdmm_201_asymmetric_laplace_asym_param_252d_d1},
    "f41_rdmm_202_nig_kurt_adj_skew_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_202_nig_kurt_adj_skew_proxy_252d_d1},
    "f41_rdmm_203_lambert_w_gauss_heavy_tail_delta_252d_d1": {"inputs": ["close"], "func": f41_rdmm_203_lambert_w_gauss_heavy_tail_delta_252d_d1},
    "f41_rdmm_204_pareto_upper_tail_alpha_inv_hill_252d_d1": {"inputs": ["close"], "func": f41_rdmm_204_pareto_upper_tail_alpha_inv_hill_252d_d1},
    "f41_rdmm_205_stable_alpha_tail_thickness_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_205_stable_alpha_tail_thickness_proxy_252d_d1},
    "f41_rdmm_206_stable_beta_skew_proxy_252d_d1": {"inputs": ["close"], "func": f41_rdmm_206_stable_beta_skew_proxy_252d_d1},
    "f41_rdmm_207_wasserstein_distance_to_t5_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_207_wasserstein_distance_to_t5_log_ret_252d_d1},
    "f41_rdmm_208_ks_distance_to_t5_log_ret_252d_d1": {"inputs": ["close"], "func": f41_rdmm_208_ks_distance_to_t5_log_ret_252d_d1},
    "f41_rdmm_209_bowley_moors_agreement_252d_d1": {"inputs": ["close"], "func": f41_rdmm_209_bowley_moors_agreement_252d_d1},
    "f41_rdmm_210_multimodal_indicator_BC_above_555_252d_d1": {"inputs": ["close"], "func": f41_rdmm_210_multimodal_indicator_BC_above_555_252d_d1},
    "f41_rdmm_211_mean_return_high_vol_days_63d_d1": {"inputs": ["close", "volume"], "func": f41_rdmm_211_mean_return_high_vol_days_63d_d1},
    "f41_rdmm_212_mean_return_low_vol_days_63d_d1": {"inputs": ["close", "volume"], "func": f41_rdmm_212_mean_return_low_vol_days_63d_d1},
    "f41_rdmm_213_std_return_high_vol_days_63d_d1": {"inputs": ["close", "volume"], "func": f41_rdmm_213_std_return_high_vol_days_63d_d1},
    "f41_rdmm_214_std_return_low_vol_days_63d_d1": {"inputs": ["close", "volume"], "func": f41_rdmm_214_std_return_low_vol_days_63d_d1},
    "f41_rdmm_215_skew_return_high_vol_days_252d_d1": {"inputs": ["close", "volume"], "func": f41_rdmm_215_skew_return_high_vol_days_252d_d1},
    "f41_rdmm_216_cond_skew_after_neg_ret_day_252d_d1": {"inputs": ["close"], "func": f41_rdmm_216_cond_skew_after_neg_ret_day_252d_d1},
    "f41_rdmm_217_cond_skew_after_pos_ret_day_252d_d1": {"inputs": ["close"], "func": f41_rdmm_217_cond_skew_after_pos_ret_day_252d_d1},
    "f41_rdmm_218_cond_kurt_given_high_vol_regime_252d_d1": {"inputs": ["close"], "func": f41_rdmm_218_cond_kurt_given_high_vol_regime_252d_d1},
    "f41_rdmm_219_mean_shift_2sigma_indicator_63d_in_252d_d1": {"inputs": ["close"], "func": f41_rdmm_219_mean_shift_2sigma_indicator_63d_in_252d_d1},
    "f41_rdmm_220_ks_distshift_63d_vs_prior_63d_252d_d1": {"inputs": ["close"], "func": f41_rdmm_220_ks_distshift_63d_vs_prior_63d_252d_d1},
    "f41_rdmm_221_mean_vs_median_divergence_pct_252d_d1": {"inputs": ["close"], "func": f41_rdmm_221_mean_vs_median_divergence_pct_252d_d1},
    "f41_rdmm_222_cond_skew_at_252d_high_252d_d1": {"inputs": ["high", "close"], "func": f41_rdmm_222_cond_skew_at_252d_high_252d_d1},
    "f41_rdmm_223_skew_of_rolling_21d_skew_over_252d_d1": {"inputs": ["close"], "func": f41_rdmm_223_skew_of_rolling_21d_skew_over_252d_d1},
    "f41_rdmm_224_kurt_of_rolling_21d_kurt_over_252d_d1": {"inputs": ["close"], "func": f41_rdmm_224_kurt_of_rolling_21d_kurt_over_252d_d1},
    "f41_rdmm_225_comp_distribution_pathology_score_252d_d1": {"inputs": ["close"], "func": f41_rdmm_225_comp_distribution_pathology_score_252d_d1},
}
