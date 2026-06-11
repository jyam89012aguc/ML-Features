"""
28_return_distribution — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: acceleration of extended return-distribution 2nd-derivative features —
        second diff / slope-of-slope / diff-of-slope of Omega ratio, gain-to-pain,
        Cornish-Fisher VaR, Hill tail index, conditional drawdown, max-to-mean loss,
        quantile spread, runs-test statistic, sample/approximate entropy,
        DFA multi-scale Hurst, return clustering, squared-return autocorrelation,
        and permutation entropy (order 4).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Scalar helpers for rolling.apply (raw=True) ───────────────────────────────

def _omega_ratio_scalar_0(arr: np.ndarray) -> float:
    """Omega ratio (threshold = 0)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    gains = np.sum(np.maximum(a, 0.0))
    losses = np.sum(np.maximum(-a, 0.0))
    if losses < _EPS:
        return np.nan
    return gains / losses


def _gain_to_pain_scalar(arr: np.ndarray) -> float:
    """Gain-to-pain: sum(gains) / |sum(losses)|."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    gains = np.sum(a[a > 0])
    losses = np.abs(np.sum(a[a < 0]))
    if losses < _EPS:
        return np.nan
    return gains / losses


def _norm_ppf(p: float) -> float:
    """Rational approximation of the standard normal quantile."""
    if p <= 0.0 or p >= 1.0:
        return np.nan
    if p < 0.5:
        sign = -1.0
        q = p
    else:
        sign = 1.0
        q = 1.0 - p
    t = np.sqrt(-2.0 * np.log(q))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    num = c0 + c1 * t + c2 * t * t
    den = 1.0 + d1 * t + d2 * t * t + d3 * t * t * t
    z = t - num / den
    return sign * z


def _cf_var_5pct(arr: np.ndarray) -> float:
    """Cornish-Fisher VaR at 5%."""
    a = arr[~np.isnan(arr)]
    if len(a) < 8:
        return np.nan
    mu = a.mean()
    sigma = a.std(ddof=1)
    if sigma < _EPS:
        return np.nan
    s3 = np.mean(((a - mu) / sigma) ** 3)
    s4 = np.mean(((a - mu) / sigma) ** 4) - 3.0
    z = _norm_ppf(0.05)
    if np.isnan(z):
        return np.nan
    z_cf = (z + (z ** 2 - 1.0) / 6.0 * s3
            + (z ** 3 - 3.0 * z) / 24.0 * s4
            - (2.0 * z ** 3 - 5.0 * z) / 36.0 * (s3 ** 2))
    return mu + sigma * z_cf


def _cf_var_1pct(arr: np.ndarray) -> float:
    """Cornish-Fisher VaR at 1%."""
    a = arr[~np.isnan(arr)]
    if len(a) < 8:
        return np.nan
    mu = a.mean()
    sigma = a.std(ddof=1)
    if sigma < _EPS:
        return np.nan
    s3 = np.mean(((a - mu) / sigma) ** 3)
    s4 = np.mean(((a - mu) / sigma) ** 4) - 3.0
    z = _norm_ppf(0.01)
    if np.isnan(z):
        return np.nan
    z_cf = (z + (z ** 2 - 1.0) / 6.0 * s3
            + (z ** 3 - 3.0 * z) / 24.0 * s4
            - (2.0 * z ** 3 - 5.0 * z) / 36.0 * (s3 ** 2))
    return mu + sigma * z_cf


def _hill_10pct(arr: np.ndarray) -> float:
    """Hill tail index, bottom 10%."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 10:
        return np.nan
    k = max(2, int(n * 0.10))
    sorted_a = np.sort(a)
    tail_abs = np.abs(sorted_a[:k])
    sorted_abs = np.sort(tail_abs)[::-1]
    threshold_h = sorted_abs[-1]
    if threshold_h < _EPS:
        return np.nan
    log_ratios = np.log(sorted_abs / threshold_h)
    mean_log = log_ratios[:-1].mean() if len(log_ratios) > 1 else np.nan
    if np.isnan(mean_log) or mean_log < _EPS:
        return np.nan
    return 1.0 / mean_log


def _conditional_dd_scalar(arr: np.ndarray) -> float:
    """Conditional drawdown: mean drawdown above 75th pct."""
    a = arr[~np.isnan(arr)]
    if len(a) < 8:
        return np.nan
    cum = np.cumsum(a)
    running_max = np.maximum.accumulate(cum)
    dd = running_max - cum
    q75 = np.percentile(dd, 75)
    tail_dd = dd[dd >= q75]
    if len(tail_dd) == 0:
        return np.nan
    return float(tail_dd.mean())


def _max_to_mean_loss_scalar(arr: np.ndarray) -> float:
    """Worst return / mean negative return."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    losses = a[a < 0]
    if len(losses) == 0:
        return np.nan
    mean_loss = losses.mean()
    if abs(mean_loss) < _EPS:
        return np.nan
    return a.min() / mean_loss


def _runs_test_stat_scalar(arr: np.ndarray) -> float:
    """Wald-Wolfowitz runs test z-statistic."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    signs = (a > 0).astype(int)
    n1 = signs.sum()
    n2 = n - n1
    if n1 < 2 or n2 < 2:
        return np.nan
    runs = 1 + np.sum(signs[1:] != signs[:-1])
    expected = (2.0 * n1 * n2) / n + 1.0
    denom = (2.0 * n1 * n2 * (2.0 * n1 * n2 - n)) / (n * n * (n - 1.0))
    if denom <= 0:
        return np.nan
    return (runs - expected) / np.sqrt(denom)


def _sign_bias_scalar(arr: np.ndarray) -> float:
    """Fraction of positive returns."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    return float(np.sum(a > 0)) / len(a)


def _approx_entropy_m2(arr: np.ndarray) -> float:
    """Approximate entropy order 2."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    m = 2
    if n < m + 2:
        return np.nan
    r = 0.2 * (a.std() if a.std() > _EPS else 1.0)

    def _phi(m_):
        templates = np.array([a[i:i + m_] for i in range(n - m_ + 1)])
        count = 0
        for i in range(len(templates)):
            diffs = np.max(np.abs(templates - templates[i]), axis=1)
            count += np.sum(diffs <= r)
        return np.log(count / (n - m_ + 1)) if count > 0 else np.nan

    phi_m = _phi(m)
    phi_m1 = _phi(m + 1)
    if np.isnan(phi_m) or np.isnan(phi_m1):
        return np.nan
    return phi_m - phi_m1


def _sample_entropy_m2(arr: np.ndarray) -> float:
    """Sample entropy order 2."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    m = 2
    if n < m + 3:
        return np.nan
    r = 0.2 * (a.std() if a.std() > _EPS else 1.0)

    def _count_matches(m_):
        templates = np.array([a[i:i + m_] for i in range(n - m_)])
        total = 0
        for i in range(len(templates)):
            diffs = np.max(np.abs(templates - templates[i]), axis=1)
            total += np.sum(diffs <= r) - 1
        return total

    b = _count_matches(m)
    a_ = _count_matches(m + 1)
    if b == 0:
        return np.nan
    ratio = a_ / b
    if ratio <= 0:
        return np.nan
    return -np.log(ratio)


def _dfa_multiscale_scalar(arr: np.ndarray) -> float:
    """DFA Hurst using three scales."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 20:
        return np.nan
    profile = np.cumsum(a - a.mean())

    def _rms_fluct(p, scale):
        nb = len(p) // scale
        if nb < 2:
            return np.nan
        flucts = []
        for i in range(nb):
            seg = p[i * scale:(i + 1) * scale]
            x = np.arange(scale, dtype=float)
            xm = x.mean()
            ym = seg.mean()
            d = ((x - xm) ** 2).sum()
            if d < _EPS:
                flucts.append(seg.std())
                continue
            slope_ = ((x - xm) * (seg - ym)).sum() / d
            intercept_ = ym - slope_ * xm
            res = seg - (intercept_ + slope_ * x)
            flucts.append(np.sqrt((res ** 2).mean()))
        return np.mean(flucts) if flucts else np.nan

    scales = [max(4, n // 5), max(6, n // 3), max(8, n // 2)]
    log_s, log_f = [], []
    for s in scales:
        f = _rms_fluct(profile, s)
        if f is not None and not np.isnan(f) and f > _EPS:
            log_s.append(np.log(s))
            log_f.append(np.log(f))
    if len(log_s) < 2:
        return np.nan
    log_s = np.array(log_s)
    log_f = np.array(log_f)
    xm = log_s.mean()
    ym = log_f.mean()
    d = ((log_s - xm) ** 2).sum()
    if d < _EPS:
        return np.nan
    return ((log_s - xm) * (log_f - ym)).sum() / d


def _return_clustering_scalar(arr: np.ndarray) -> float:
    """Fraction of large-move days adjacent to another large-move day."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    sigma = a.std()
    if sigma < _EPS:
        return np.nan
    large = np.abs(a) > 1.5 * sigma
    if large.sum() < 2:
        return 0.0
    clustered = 0
    for i in range(1, n):
        if large[i] and large[i - 1]:
            clustered += 1
    return float(clustered) / float(large.sum())


def _sq_ret_autocorr_lag1(arr: np.ndarray) -> float:
    """Lag-1 autocorrelation of squared returns."""
    sq = arr ** 2
    n = len(sq)
    if n <= 3:
        return np.nan
    x = sq[:-1]
    y = sq[1:]
    mx, my = x.mean(), y.mean()
    num = ((x - mx) * (y - my)).sum()
    denom = np.sqrt(((x - mx) ** 2).sum() * ((y - my) ** 2).sum())
    if denom < _EPS:
        return np.nan
    return num / denom


def _quantile_spread_90_10_scalar(arr: np.ndarray) -> float:
    """(q90 - q10) / |median|."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    q90 = np.percentile(a, 90)
    q10 = np.percentile(a, 10)
    med = np.median(a)
    spread = q90 - q10
    if abs(med) < _EPS:
        return spread
    return spread / abs(med)


def _mode_gap_10bins(arr: np.ndarray) -> float:
    """Return mode minus mean (10-bin histogram)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 10:
        return np.nan
    mn, mx = a.min(), a.max()
    if mx - mn < _EPS:
        return 0.0
    counts, edges = np.histogram(a, bins=10)
    modal_bin = np.argmax(counts)
    mode_val = 0.5 * (edges[modal_bin] + edges[modal_bin + 1])
    return mode_val - a.mean()


def _pot_exceed_15sigma(arr: np.ndarray) -> float:
    """Fraction of returns below mu - 1.5*sigma."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    sigma = a.std()
    if sigma < _EPS:
        return np.nan
    mu = a.mean()
    return float(np.sum(a < mu - 1.5 * sigma)) / len(a)


def _perm_entropy_order4(arr: np.ndarray) -> float:
    """Permutation entropy order 4."""
    from math import factorial
    a = arr[~np.isnan(arr)]
    n = len(a)
    order = 4
    if n < order + 2:
        return np.nan
    counts = {}
    for i in range(n - order + 1):
        pattern = tuple(np.argsort(a[i:i + order], kind='stable'))
        counts[pattern] = counts.get(pattern, 0) + 1
    total = sum(counts.values())
    if total == 0:
        return np.nan
    probs = np.array(list(counts.values()), dtype=float) / total
    probs = probs[probs > 0]
    entropy = -np.sum(probs * np.log2(probs))
    max_entropy = np.log2(float(factorial(order)))
    if max_entropy < _EPS:
        return np.nan
    return entropy / max_entropy


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each = diff-of-diff / slope-of-slope / diff-of-slope of an extended-base
# 2nd-derivative concept.

# --- Group A (001-005): Omega ratio and gain-to-pain acceleration ---

def rds_extdrv3_001_omega_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Omega ratio (acceleration of reward/risk velocity)."""
    r = _log_ret(close)
    om = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )
    vel = om.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_002_omega_ratio_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21-day Omega ratio (Omega jerk)."""
    r = _log_ret(close)
    om = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )
    vel21 = om.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_extdrv3_003_omega_ratio_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Omega ratio (acceleration of quarterly reward/risk)."""
    r = _log_ret(close)
    om = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )
    vel = om.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_004_omega_ratio_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day Omega ratio over 63 days (slope-velocity of Omega)."""
    r = _log_ret(close)
    om = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )
    slp = _linslope(om, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_extdrv3_005_gain_to_pain_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gain-to-pain ratio (acceleration of pain balance change)."""
    r = _log_ret(close)
    gp = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _gain_to_pain_scalar, raw=True
    )
    vel = gp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group B (006-010): Cornish-Fisher VaR acceleration ---

def rds_extdrv3_006_cf_var_5pct_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CF-VaR-5% (acceleration of moment-adjusted tail)."""
    r = _log_ret(close)
    cv = r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _cf_var_5pct, raw=True
    )
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_007_cf_var_5pct_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day CF-VaR-5% (CF-VaR jerk)."""
    r = _log_ret(close)
    cv = r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _cf_var_5pct, raw=True
    )
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_extdrv3_008_cf_var_5pct_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day CF-VaR-5% (acceleration of quarterly CF tail)."""
    r = _log_ret(close)
    cv = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _cf_var_5pct, raw=True
    )
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_009_cf_var_1pct_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day CF-VaR-1% (acceleration of extreme CF tail)."""
    r = _log_ret(close)
    cv = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _cf_var_1pct, raw=True
    )
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_010_cf_var_5pct_21d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day CF-VaR-5% over 63 days (rate of slope change)."""
    r = _log_ret(close)
    cv = r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _cf_var_5pct, raw=True
    )
    slp = _linslope(cv, _TD_QTR)
    return slp.diff(_TD_WEEK)


# --- Group C (011-015): Hill, conditional drawdown acceleration ---

def rds_extdrv3_011_hill_tail_index_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Hill tail index (acceleration of tail-heaviness velocity)."""
    r = _log_ret(close)
    hi = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hill_10pct, raw=True
    )
    vel = hi.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_012_hill_tail_index_63d_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day Hill tail index over 63 days (Hill slope jerk)."""
    r = _log_ret(close)
    hi = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hill_10pct, raw=True
    )
    slp = _linslope(hi, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rds_extdrv3_013_conditional_dd_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day conditional drawdown (acceleration of CDD velocity)."""
    r = _log_ret(close)
    cd = r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _conditional_dd_scalar, raw=True
    )
    vel = cd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_014_conditional_dd_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day conditional drawdown (CDD jerk)."""
    r = _log_ret(close)
    cd = r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _conditional_dd_scalar, raw=True
    )
    vel21 = cd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rds_extdrv3_015_conditional_dd_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day conditional drawdown (acceleration of quarterly CDD)."""
    r = _log_ret(close)
    cd = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _conditional_dd_scalar, raw=True
    )
    vel = cd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group D (016-018): Max-to-mean loss, mode gap, quantile spread acceleration ---

def rds_extdrv3_016_max_to_mean_loss_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day max-to-mean-loss (acceleration of loss concentration)."""
    r = _log_ret(close)
    mm = r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _max_to_mean_loss_scalar, raw=True
    )
    vel = mm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_017_mode_gap_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day mode-gap (acceleration of modal distribution shift)."""
    r = _log_ret(close)
    mg = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _mode_gap_10bins, raw=True
    )
    vel = mg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_018_quantile_spread_norm_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day normalized quantile spread (acceleration of dispersion)."""
    r = _log_ret(close)
    qs = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _quantile_spread_90_10_scalar, raw=True
    )
    vel = qs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group E (019-021): Runs-test, sign bias, POT acceleration ---

def rds_extdrv3_019_runs_test_stat_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day runs-test z-stat (acceleration of serial independence)."""
    r = _log_ret(close)
    rt = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _runs_test_stat_scalar, raw=True
    )
    vel = rt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_020_sign_bias_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day sign bias (acceleration of up-day fraction change)."""
    r = _log_ret(close)
    sb = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _sign_bias_scalar, raw=True
    )
    vel = sb.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_021_pot_exceed_15sigma_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day POT exceedance rate (acceleration of tail event frequency)."""
    r = _log_ret(close)
    pot = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _pot_exceed_15sigma, raw=True
    )
    vel = pot.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group F (022-025): DFA, clustering, sq-AC, perm-entropy acceleration ---

def rds_extdrv3_022_dfa_multiscale_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day multi-scale DFA Hurst (acceleration of fractal regime)."""
    r = _log_ret(close)
    h = r.rolling(_TD_QTR, min_periods=max(20, _TD_QTR // 2)).apply(
        _dfa_multiscale_scalar, raw=True
    )
    vel = h.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_023_return_clustering_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day large-move clustering (acceleration of vol-clustering)."""
    r = _log_ret(close)
    cl = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _return_clustering_scalar, raw=True
    )
    vel = cl.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_024_sq_ret_autocorr_lag1_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day sq-return lag-1 AC (acceleration of GARCH persistence)."""
    r = _log_ret(close)
    ac = r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _sq_ret_autocorr_lag1, raw=True
    )
    vel = ac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rds_extdrv3_025_perm_entropy_order4_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day perm-entropy order 4 (acceleration of ordinal disorder)."""
    r = _log_ret(close)
    pe = r.rolling(_TD_QTR, min_periods=max(12, _TD_QTR // 2)).apply(
        _perm_entropy_order4, raw=True
    )
    vel = pe.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rds_extdrv3_001_omega_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_001_omega_ratio_21d_5d_diff_5d_diff},
    "rds_extdrv3_002_omega_ratio_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_002_omega_ratio_21d_21d_diff_5d_diff},
    "rds_extdrv3_003_omega_ratio_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_003_omega_ratio_63d_5d_diff_5d_diff},
    "rds_extdrv3_004_omega_ratio_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_004_omega_ratio_21d_slope_63d_5d_diff},
    "rds_extdrv3_005_gain_to_pain_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_005_gain_to_pain_21d_5d_diff_5d_diff},
    "rds_extdrv3_006_cf_var_5pct_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_006_cf_var_5pct_21d_5d_diff_5d_diff},
    "rds_extdrv3_007_cf_var_5pct_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_007_cf_var_5pct_21d_21d_diff_5d_diff},
    "rds_extdrv3_008_cf_var_5pct_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_008_cf_var_5pct_63d_5d_diff_5d_diff},
    "rds_extdrv3_009_cf_var_1pct_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_009_cf_var_1pct_63d_5d_diff_5d_diff},
    "rds_extdrv3_010_cf_var_5pct_21d_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_010_cf_var_5pct_21d_slope_63d_5d_diff},
    "rds_extdrv3_011_hill_tail_index_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_011_hill_tail_index_63d_5d_diff_5d_diff},
    "rds_extdrv3_012_hill_tail_index_63d_slope_63d_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_012_hill_tail_index_63d_slope_63d_5d_diff},
    "rds_extdrv3_013_conditional_dd_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_013_conditional_dd_21d_5d_diff_5d_diff},
    "rds_extdrv3_014_conditional_dd_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_014_conditional_dd_21d_21d_diff_5d_diff},
    "rds_extdrv3_015_conditional_dd_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_015_conditional_dd_63d_5d_diff_5d_diff},
    "rds_extdrv3_016_max_to_mean_loss_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_016_max_to_mean_loss_21d_5d_diff_5d_diff},
    "rds_extdrv3_017_mode_gap_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_017_mode_gap_63d_5d_diff_5d_diff},
    "rds_extdrv3_018_quantile_spread_norm_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_018_quantile_spread_norm_63d_5d_diff_5d_diff},
    "rds_extdrv3_019_runs_test_stat_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_019_runs_test_stat_63d_5d_diff_5d_diff},
    "rds_extdrv3_020_sign_bias_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_020_sign_bias_63d_5d_diff_5d_diff},
    "rds_extdrv3_021_pot_exceed_15sigma_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_021_pot_exceed_15sigma_63d_5d_diff_5d_diff},
    "rds_extdrv3_022_dfa_multiscale_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_022_dfa_multiscale_63d_5d_diff_5d_diff},
    "rds_extdrv3_023_return_clustering_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_023_return_clustering_63d_5d_diff_5d_diff},
    "rds_extdrv3_024_sq_ret_autocorr_lag1_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_024_sq_ret_autocorr_lag1_63d_5d_diff_5d_diff},
    "rds_extdrv3_025_perm_entropy_order4_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": rds_extdrv3_025_perm_entropy_order4_63d_5d_diff_5d_diff},
}
