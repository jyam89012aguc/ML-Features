"""
28_return_distribution — Extended Features 001-075
Domain: deeper return-distribution coverage — Omega ratio, gain-to-pain, Cornish-Fisher VaR,
        peak-over-threshold tail index / Hill estimator, conditional drawdown, max-to-mean
        ratios, distribution mode / quantile-spread, runs-test & sign statistics, sample /
        approximate entropy, DFA multi-scale exponent variants, return-clustering measures,
        and rate-of-change / acceleration variants of these statistics.
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


# ── Scalar helpers for rolling.apply (raw=True) ───────────────────────────────

def _omega_ratio_scalar(arr: np.ndarray, threshold: float = 0.0) -> float:
    """Omega ratio: sum of gains above threshold / |sum of losses below threshold|."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    gains = np.sum(np.maximum(a - threshold, 0.0))
    losses = np.sum(np.maximum(threshold - a, 0.0))
    if losses < _EPS:
        return np.nan
    return gains / losses


def _omega_ratio_scalar_0(arr: np.ndarray) -> float:
    return _omega_ratio_scalar(arr, 0.0)


def _gain_to_pain_scalar(arr: np.ndarray) -> float:
    """Gain-to-pain ratio: sum of all gains / |sum of all losses|."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    gains = np.sum(a[a > 0])
    losses = np.abs(np.sum(a[a < 0]))
    if losses < _EPS:
        return np.nan
    return gains / losses


def _hill_estimator_scalar(arr: np.ndarray, k_frac: float = 0.10) -> float:
    """Hill estimator of the tail index using bottom k_frac fraction of returns.
    Returns the tail exponent alpha (larger = lighter tail).
    """
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 10:
        return np.nan
    k = max(2, int(n * k_frac))
    sorted_a = np.sort(a)
    tail = sorted_a[:k]          # k smallest (most negative) values
    tail_abs = np.abs(tail)
    threshold = tail_abs[-1]     # k-th largest absolute value (smallest in tail_abs sorted asc)
    # Hill: 1/alpha = (1/k) * sum(log(|x_i|/threshold)) for |x_i| >= threshold
    # Using bottom k: sort ascending, take first k, reference is tail_abs[k-1]
    sorted_abs = np.sort(tail_abs)[::-1]  # descending
    threshold_h = sorted_abs[-1]
    if threshold_h < _EPS:
        return np.nan
    log_ratios = np.log(sorted_abs / threshold_h)
    mean_log = log_ratios[:-1].mean() if len(log_ratios) > 1 else np.nan
    if np.isnan(mean_log) or mean_log < _EPS:
        return np.nan
    return 1.0 / mean_log


def _hill_10pct(arr: np.ndarray) -> float:
    return _hill_estimator_scalar(arr, 0.10)


def _hill_15pct(arr: np.ndarray) -> float:
    return _hill_estimator_scalar(arr, 0.15)


def _norm_ppf(p: float) -> float:
    """Pure-numpy rational approximation of the standard normal quantile (Beasley-Springer-Moro)."""
    # Abramowitz & Stegun 26.2.17 rational approximation; max error ~ 4.5e-4
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


def _cornish_fisher_var_scalar(arr: np.ndarray, p: float = 0.05) -> float:
    """Cornish-Fisher adjusted VaR incorporating skewness and excess kurtosis."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    mu = a.mean()
    sigma = a.std(ddof=1)
    if sigma < _EPS:
        return np.nan
    # skewness
    s3 = np.mean(((a - mu) / sigma) ** 3)
    # excess kurtosis
    s4 = np.mean(((a - mu) / sigma) ** 4) - 3.0
    # z-score for p via rational approximation (no scipy/erfinv needed)
    z = _norm_ppf(p)
    if np.isnan(z):
        return np.nan
    # Cornish-Fisher expansion
    z_cf = (z
            + (z ** 2 - 1.0) / 6.0 * s3
            + (z ** 3 - 3.0 * z) / 24.0 * s4
            - (2.0 * z ** 3 - 5.0 * z) / 36.0 * (s3 ** 2))
    return mu + sigma * z_cf


def _cf_var_5pct(arr: np.ndarray) -> float:
    return _cornish_fisher_var_scalar(arr, 0.05)


def _cf_var_1pct(arr: np.ndarray) -> float:
    return _cornish_fisher_var_scalar(arr, 0.01)


def _runs_test_stat_scalar(arr: np.ndarray) -> float:
    """Wald-Wolfowitz runs test statistic (z-score). Positive = fewer runs than expected."""
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
    """Fraction of positive returns (sign bias; >0.5 = more up days)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    return float(np.sum(a > 0)) / len(a)


def _consec_loss_max_scalar(arr: np.ndarray) -> float:
    """Maximum consecutive loss streak length."""
    a = arr[~np.isnan(arr)]
    if len(a) < 2:
        return np.nan
    max_streak = 0
    cur = 0
    for v in a:
        if v < 0:
            cur += 1
            if cur > max_streak:
                max_streak = cur
        else:
            cur = 0
    return float(max_streak)


def _approx_entropy_scalar(arr: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Approximate entropy (ApEn) of order m. Lower = more regular."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < m + 2:
        return np.nan
    r = r_frac * (a.std() if a.std() > _EPS else 1.0)

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


def _approx_entropy_m2(arr: np.ndarray) -> float:
    return _approx_entropy_scalar(arr, m=2, r_frac=0.2)


def _sample_entropy_scalar(arr: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Sample entropy (SampEn): like ApEn but without self-matches."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < m + 3:
        return np.nan
    r = r_frac * (a.std() if a.std() > _EPS else 1.0)

    def _count_matches(m_):
        templates = np.array([a[i:i + m_] for i in range(n - m_)])
        total = 0
        for i in range(len(templates)):
            diffs = np.max(np.abs(templates - templates[i]), axis=1)
            total += np.sum(diffs <= r) - 1  # exclude self
        return total

    b = _count_matches(m)
    a_ = _count_matches(m + 1)
    if b == 0:
        return np.nan
    ratio = a_ / b
    if ratio <= 0:
        return np.nan
    return -np.log(ratio)


def _sample_entropy_m2(arr: np.ndarray) -> float:
    return _sample_entropy_scalar(arr, m=2, r_frac=0.2)


def _dfa_multiscale_scalar(arr: np.ndarray) -> float:
    """DFA Hurst using three scales (n//5, n//3, n//2) for a more robust slope estimate."""
    n = len(arr)
    if n < 20:
        return np.nan
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
    log_s = []
    log_f = []
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


def _conditional_dd_scalar(arr: np.ndarray) -> float:
    """Conditional drawdown: mean of drawdown values that exceed the 75th pct of drawdowns."""
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    # Build running drawdown sequence
    cum = np.cumsum(a)
    running_max = np.maximum.accumulate(cum)
    dd = running_max - cum  # drawdown in log-return units (non-negative)
    if len(dd) == 0:
        return np.nan
    q75 = np.percentile(dd, 75)
    tail_dd = dd[dd >= q75]
    if len(tail_dd) == 0:
        return np.nan
    return float(tail_dd.mean())


def _max_to_mean_loss_scalar(arr: np.ndarray) -> float:
    """Ratio of worst single return to mean of negative returns (extreme loss concentration)."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    losses = a[a < 0]
    if len(losses) == 0:
        return np.nan
    mean_loss = losses.mean()
    if abs(mean_loss) < _EPS:
        return np.nan
    return a.min() / mean_loss  # both negative, ratio > 1 means extreme outlier


def _return_clustering_scalar(arr: np.ndarray) -> float:
    """Return clustering: fraction of large-move days (|r| > 1.5*std) that occur in runs."""
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
    # count large-move days adjacent to another large-move day
    clustered = 0
    for i in range(1, n):
        if large[i] and large[i - 1]:
            clustered += 1
    return float(clustered) / float(large.sum())


def _pot_exceed_rate_scalar(arr: np.ndarray, threshold_sigma: float = 1.5) -> float:
    """Peak-over-threshold: fraction of returns exceeding threshold_sigma on left tail."""
    a = arr[~np.isnan(arr)]
    if len(a) < 4:
        return np.nan
    sigma = a.std()
    if sigma < _EPS:
        return np.nan
    mu = a.mean()
    return float(np.sum(a < mu - threshold_sigma * sigma)) / len(a)


def _pot_exceed_15sigma(arr: np.ndarray) -> float:
    return _pot_exceed_rate_scalar(arr, 1.5)


def _pot_exceed_20sigma(arr: np.ndarray) -> float:
    return _pot_exceed_rate_scalar(arr, 2.0)


def _mode_gap_scalar(arr: np.ndarray, n_bins: int = 10) -> float:
    """Return mode (center of modal bin) minus mean: distribution center location gap."""
    a = arr[~np.isnan(arr)]
    if len(a) < n_bins:
        return np.nan
    mn, mx = a.min(), a.max()
    if mx - mn < _EPS:
        return 0.0
    counts, edges = np.histogram(a, bins=n_bins)
    modal_bin = np.argmax(counts)
    mode_val = 0.5 * (edges[modal_bin] + edges[modal_bin + 1])
    return mode_val - a.mean()


def _mode_gap_10bins(arr: np.ndarray) -> float:
    return _mode_gap_scalar(arr, 10)


def _quantile_spread_90_10_scalar(arr: np.ndarray) -> float:
    """90th minus 10th percentile spread normalised by |median|."""
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


def _perm_entropy_order4(arr: np.ndarray) -> float:
    """Permutation entropy of order 4 (finer ordinal pattern resolution)."""
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


def _perm_entropy_order5(arr: np.ndarray) -> float:
    """Permutation entropy of order 5."""
    from math import factorial
    a = arr[~np.isnan(arr)]
    n = len(a)
    order = 5
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


def _autocorr_lag_scalar(arr: np.ndarray, lag: int) -> float:
    n = len(arr)
    if n <= lag + 2:
        return np.nan
    x = arr[:-lag]
    y = arr[lag:]
    mx, my = x.mean(), y.mean()
    num = ((x - mx) * (y - my)).sum()
    denom = np.sqrt(((x - mx) ** 2).sum() * ((y - my) ** 2).sum())
    if denom < _EPS:
        return np.nan
    return num / denom


def _ac_lag7(arr: np.ndarray) -> float:
    return _autocorr_lag_scalar(arr, 7)


def _ac_lag15(arr: np.ndarray) -> float:
    return _autocorr_lag_scalar(arr, 15)


def _ac_lag20(arr: np.ndarray) -> float:
    return _autocorr_lag_scalar(arr, 20)


def _sq_ret_autocorr_lag1(arr: np.ndarray) -> float:
    """Autocorrelation of squared returns at lag 1 (GARCH-style volatility persistence)."""
    return _autocorr_lag_scalar(arr ** 2, 1)


def _hurst_rs_scalar(arr: np.ndarray) -> float:
    n = len(arr)
    if n < 8:
        return np.nan
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 8:
        return np.nan
    mean_a = a.mean()
    dev = a - mean_a
    cumdev = np.cumsum(dev)
    r = cumdev.max() - cumdev.min()
    s = a.std(ddof=1)
    if s < _EPS or r < _EPS:
        return np.nan
    return np.log(r / s) / np.log(n)


def _linslope_raw(arr: np.ndarray) -> float:
    """OLS slope of arr vs index (raw array version)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    d = ((x - xm) ** 2).sum()
    if d < _EPS:
        return np.nan
    return ((x - xm) * (arr - ym)).sum() / d


# ── Feature functions ext_001 - ext_075 ──────────────────────────────────────

# --- Group A (001-008): Omega ratio variants ---

def rds_ext_001_omega_ratio_21d(close: pd.Series) -> pd.Series:
    """21-day Omega ratio (gains / losses relative to zero threshold)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )


def rds_ext_002_omega_ratio_63d(close: pd.Series) -> pd.Series:
    """63-day Omega ratio."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )


def rds_ext_003_omega_ratio_126d(close: pd.Series) -> pd.Series:
    """126-day Omega ratio."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(4, _TD_HALF // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )


def rds_ext_004_omega_ratio_252d(close: pd.Series) -> pd.Series:
    """252-day Omega ratio."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).apply(
        _omega_ratio_scalar_0, raw=True
    )


def rds_ext_005_omega_ratio_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Omega ratio within its 252-day distribution."""
    om = rds_ext_001_omega_ratio_21d(close)
    return om.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_006_omega_ratio_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day Omega ratio relative to its 252-day distribution."""
    om = rds_ext_001_omega_ratio_21d(close)
    m = _rolling_mean(om, _TD_YEAR)
    s = _rolling_std(om, _TD_YEAR)
    return _safe_div(om - m, s)


def rds_ext_007_omega_ratio_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Omega ratio within its 252-day distribution."""
    om = rds_ext_002_omega_ratio_63d(close)
    return om.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_008_omega_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day Omega ratio (recent vs long-term quality)."""
    return _safe_div(rds_ext_001_omega_ratio_21d(close), rds_ext_004_omega_ratio_252d(close))


# --- Group B (009-013): Gain-to-pain ratio variants ---

def rds_ext_009_gain_to_pain_21d(close: pd.Series) -> pd.Series:
    """21-day gain-to-pain ratio: sum(gains) / |sum(losses)|."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _gain_to_pain_scalar, raw=True
    )


def rds_ext_010_gain_to_pain_63d(close: pd.Series) -> pd.Series:
    """63-day gain-to-pain ratio."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _gain_to_pain_scalar, raw=True
    )


def rds_ext_011_gain_to_pain_252d(close: pd.Series) -> pd.Series:
    """252-day gain-to-pain ratio."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).apply(
        _gain_to_pain_scalar, raw=True
    )


def rds_ext_012_gain_to_pain_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day gain-to-pain in its 252-day distribution."""
    gp = rds_ext_009_gain_to_pain_21d(close)
    return gp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_013_gain_to_pain_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day gain-to-pain (short vs long-term pain balance)."""
    return _safe_div(rds_ext_009_gain_to_pain_21d(close), rds_ext_011_gain_to_pain_252d(close))


# --- Group C (014-019): Cornish-Fisher VaR variants ---

def rds_ext_014_cf_var_5pct_21d(close: pd.Series) -> pd.Series:
    """21-day Cornish-Fisher adjusted VaR at 5% (moment-corrected tail estimate)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _cf_var_5pct, raw=True
    )


def rds_ext_015_cf_var_5pct_63d(close: pd.Series) -> pd.Series:
    """63-day Cornish-Fisher adjusted VaR at 5%."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _cf_var_5pct, raw=True
    )


def rds_ext_016_cf_var_5pct_252d(close: pd.Series) -> pd.Series:
    """252-day Cornish-Fisher adjusted VaR at 5%."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(
        _cf_var_5pct, raw=True
    )


def rds_ext_017_cf_var_1pct_63d(close: pd.Series) -> pd.Series:
    """63-day Cornish-Fisher adjusted VaR at 1%."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _cf_var_1pct, raw=True
    )


def rds_ext_018_cf_var_vs_historical_var_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day CF-VaR-5% to historical VaR-5% (moment-adjustment factor)."""
    cf = rds_ext_015_cf_var_5pct_63d(close)
    hist = _rolling_quantile(_log_ret(close), _TD_QTR, 0.05)
    return _safe_div(cf, hist)


def rds_ext_019_cf_var_5pct_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day CF-VaR-5% in its 252-day distribution."""
    cv = rds_ext_014_cf_var_5pct_21d(close)
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (020-025): Hill estimator / POT tail index ---

def rds_ext_020_hill_tail_index_10pct_63d(close: pd.Series) -> pd.Series:
    """63-day Hill tail index (alpha) using bottom 10% of returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hill_10pct, raw=True
    )


def rds_ext_021_hill_tail_index_15pct_63d(close: pd.Series) -> pd.Series:
    """63-day Hill tail index using bottom 15% of returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hill_15pct, raw=True
    )


def rds_ext_022_hill_tail_index_10pct_252d(close: pd.Series) -> pd.Series:
    """252-day Hill tail index using bottom 10% of returns."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(10, _TD_YEAR // 2)).apply(
        _hill_10pct, raw=True
    )


def rds_ext_023_pot_exceed_15sigma_21d(close: pd.Series) -> pd.Series:
    """21-day fraction of returns below mu - 1.5*sigma (POT exceedance rate)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _pot_exceed_15sigma, raw=True
    )


def rds_ext_024_pot_exceed_15sigma_63d(close: pd.Series) -> pd.Series:
    """63-day fraction of returns below mu - 1.5*sigma."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _pot_exceed_15sigma, raw=True
    )


def rds_ext_025_pot_exceed_20sigma_63d(close: pd.Series) -> pd.Series:
    """63-day fraction of returns below mu - 2.0*sigma (deep tail exceedance)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _pot_exceed_20sigma, raw=True
    )


# --- Group E (026-031): Conditional drawdown ---

def rds_ext_026_conditional_dd_21d(close: pd.Series) -> pd.Series:
    """21-day conditional drawdown: mean of drawdowns exceeding their 75th percentile."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _conditional_dd_scalar, raw=True
    )


def rds_ext_027_conditional_dd_63d(close: pd.Series) -> pd.Series:
    """63-day conditional drawdown."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _conditional_dd_scalar, raw=True
    )


def rds_ext_028_conditional_dd_252d(close: pd.Series) -> pd.Series:
    """252-day conditional drawdown."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(
        _conditional_dd_scalar, raw=True
    )


def rds_ext_029_conditional_dd_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day conditional drawdown in its 252-day distribution."""
    cd = rds_ext_026_conditional_dd_21d(close)
    return cd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_030_conditional_dd_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day conditional drawdown relative to its 252-day distribution."""
    cd = rds_ext_026_conditional_dd_21d(close)
    m = _rolling_mean(cd, _TD_YEAR)
    s = _rolling_std(cd, _TD_YEAR)
    return _safe_div(cd - m, s)


def rds_ext_031_conditional_dd_63d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day to 21-day conditional drawdown (scale of persistent drawdown regime)."""
    return _safe_div(rds_ext_027_conditional_dd_63d(close), rds_ext_026_conditional_dd_21d(close))


# --- Group F (032-036): Max-to-mean ratios ---

def rds_ext_032_max_to_mean_loss_21d(close: pd.Series) -> pd.Series:
    """21-day ratio of worst return to mean negative return (extreme loss concentration)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _max_to_mean_loss_scalar, raw=True
    )


def rds_ext_033_max_to_mean_loss_63d(close: pd.Series) -> pd.Series:
    """63-day ratio of worst return to mean negative return."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _max_to_mean_loss_scalar, raw=True
    )


def rds_ext_034_max_gain_to_mean_gain_21d(close: pd.Series) -> pd.Series:
    """21-day ratio of best return to mean positive return (extreme gain concentration)."""
    r = _log_ret(close)
    def _max_to_mean_gain(arr: np.ndarray) -> float:
        a = arr[~np.isnan(arr)]
        gains = a[a > 0]
        if len(gains) == 0:
            return np.nan
        mean_gain = gains.mean()
        if mean_gain < _EPS:
            return np.nan
        return a.max() / mean_gain
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _max_to_mean_gain, raw=True
    )


def rds_ext_035_max_to_mean_loss_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day max-to-mean-loss ratio in its 252-day distribution."""
    mm = rds_ext_032_max_to_mean_loss_21d(close)
    return mm.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_036_max_loss_vs_cvar_ratio_63d(close: pd.Series) -> pd.Series:
    """63-day worst single return divided by CVaR-5% (single-event tail extremity)."""
    r = _log_ret(close)
    worst = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).min()
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    cv = r.where(r < q05, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return _safe_div(worst, cv)


# --- Group G (037-043): Distribution mode / quantile-spread features ---

def rds_ext_037_mode_gap_21d(close: pd.Series) -> pd.Series:
    """21-day return distribution mode minus mean (modal location gap)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(10, _TD_MON // 2)).apply(
        _mode_gap_10bins, raw=True
    )


def rds_ext_038_mode_gap_63d(close: pd.Series) -> pd.Series:
    """63-day return distribution mode minus mean."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _mode_gap_10bins, raw=True
    )


def rds_ext_039_quantile_spread_norm_21d(close: pd.Series) -> pd.Series:
    """21-day (q90 - q10) / |median| return spread (normalized dispersion)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _quantile_spread_90_10_scalar, raw=True
    )


def rds_ext_040_quantile_spread_norm_63d(close: pd.Series) -> pd.Series:
    """63-day (q90 - q10) / |median| return spread."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _quantile_spread_90_10_scalar, raw=True
    )


def rds_ext_041_q25_logret_63d(close: pd.Series) -> pd.Series:
    """63-day 25th-percentile of daily log-returns (lower quartile)."""
    return _rolling_quantile(_log_ret(close), _TD_QTR, 0.25)


def rds_ext_042_q75_logret_63d(close: pd.Series) -> pd.Series:
    """63-day 75th-percentile of daily log-returns (upper quartile)."""
    return _rolling_quantile(_log_ret(close), _TD_QTR, 0.75)


def rds_ext_043_quantile_skew_63d(close: pd.Series) -> pd.Series:
    """63-day quantile skewness: (q90 + q10 - 2*q50) / (q90 - q10) (robust skew)."""
    r = _log_ret(close)
    q10 = _rolling_quantile(r, _TD_QTR, 0.10)
    q50 = _rolling_quantile(r, _TD_QTR, 0.50)
    q90 = _rolling_quantile(r, _TD_QTR, 0.90)
    spread = (q90 - q10).replace(0, np.nan)
    return _safe_div(q90 + q10 - 2.0 * q50, spread)


# --- Group H (044-049): Runs-test and sign statistics ---

def rds_ext_044_runs_test_stat_21d(close: pd.Series) -> pd.Series:
    """21-day Wald-Wolfowitz runs test z-statistic (serial independence of signs)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _runs_test_stat_scalar, raw=True
    )


def rds_ext_045_runs_test_stat_63d(close: pd.Series) -> pd.Series:
    """63-day Wald-Wolfowitz runs test z-statistic."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _runs_test_stat_scalar, raw=True
    )


def rds_ext_046_sign_bias_21d(close: pd.Series) -> pd.Series:
    """21-day fraction of positive return days (sign bias)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_bias_scalar, raw=True
    )


def rds_ext_047_sign_bias_63d(close: pd.Series) -> pd.Series:
    """63-day fraction of positive return days."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _sign_bias_scalar, raw=True
    )


def rds_ext_048_consec_loss_max_21d(close: pd.Series) -> pd.Series:
    """21-day maximum consecutive loss streak length."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _consec_loss_max_scalar, raw=True
    )


def rds_ext_049_consec_loss_max_63d(close: pd.Series) -> pd.Series:
    """63-day maximum consecutive loss streak length."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        _consec_loss_max_scalar, raw=True
    )


# --- Group I (050-055): Sample / approximate entropy ---

def rds_ext_050_approx_entropy_21d(close: pd.Series) -> pd.Series:
    """21-day approximate entropy (ApEn, order 2) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _approx_entropy_m2, raw=True
    )


def rds_ext_051_approx_entropy_63d(close: pd.Series) -> pd.Series:
    """63-day approximate entropy (ApEn, order 2) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _approx_entropy_m2, raw=True
    )


def rds_ext_052_sample_entropy_21d(close: pd.Series) -> pd.Series:
    """21-day sample entropy (SampEn, order 2) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _sample_entropy_m2, raw=True
    )


def rds_ext_053_sample_entropy_63d(close: pd.Series) -> pd.Series:
    """63-day sample entropy (SampEn, order 2) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _sample_entropy_m2, raw=True
    )


def rds_ext_054_approx_entropy_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ApEn in its 252-day distribution."""
    ae = rds_ext_050_approx_entropy_21d(close)
    return ae.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_055_sample_entropy_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day SampEn relative to its 252-day distribution."""
    se = rds_ext_053_sample_entropy_63d(close)
    m = _rolling_mean(se, _TD_YEAR)
    s = _rolling_std(se, _TD_YEAR)
    return _safe_div(se - m, s)


# --- Group J (056-059): DFA multi-scale exponent variants ---

def rds_ext_056_dfa_multiscale_63d(close: pd.Series) -> pd.Series:
    """63-day DFA Hurst using three scales (n//5, n//3, n//2) for robust OLS slope."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(20, _TD_QTR // 2)).apply(
        _dfa_multiscale_scalar, raw=True
    )


def rds_ext_057_dfa_multiscale_126d(close: pd.Series) -> pd.Series:
    """126-day DFA Hurst using three scales."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(20, _TD_HALF // 2)).apply(
        _dfa_multiscale_scalar, raw=True
    )


def rds_ext_058_dfa_multiscale_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day multi-scale DFA in its 252-day distribution."""
    h = rds_ext_056_dfa_multiscale_63d(close)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_ext_059_dfa_multiscale_vs_rs_diff_63d(close: pd.Series) -> pd.Series:
    """63-day multi-scale DFA Hurst minus R/S Hurst (three-scale vs single-scale divergence)."""
    h_ms = rds_ext_056_dfa_multiscale_63d(close)
    r = _log_ret(close)
    h_rs = r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )
    return h_ms - h_rs


# --- Group K (060-064): Return-clustering measures ---

def rds_ext_060_return_clustering_21d(close: pd.Series) -> pd.Series:
    """21-day fraction of large-move days (|r|>1.5*sigma) that occur in consecutive pairs."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _return_clustering_scalar, raw=True
    )


def rds_ext_061_return_clustering_63d(close: pd.Series) -> pd.Series:
    """63-day large-move clustering fraction."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _return_clustering_scalar, raw=True
    )


def rds_ext_062_sq_ret_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    """21-day lag-1 autocorrelation of squared returns (GARCH-style persistence)."""
    r = _log_ret(close)
    return r.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _sq_ret_autocorr_lag1, raw=True
    )


def rds_ext_063_sq_ret_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """63-day lag-1 autocorrelation of squared returns."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _sq_ret_autocorr_lag1, raw=True
    )


def rds_ext_064_return_clustering_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day large-move clustering in its 252-day distribution."""
    cl = rds_ext_061_return_clustering_63d(close)
    return cl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group L (065-069): Additional autocorrelation window variants ---

def rds_ext_065_autocorr_lag7_63d(close: pd.Series) -> pd.Series:
    """63-day autocorrelation of log-returns at lag 7."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _ac_lag7, raw=True
    )


def rds_ext_066_autocorr_lag15_126d(close: pd.Series) -> pd.Series:
    """126-day autocorrelation of log-returns at lag 15."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(20, _TD_HALF // 2)).apply(
        _ac_lag15, raw=True
    )


def rds_ext_067_autocorr_lag20_252d(close: pd.Series) -> pd.Series:
    """252-day autocorrelation of log-returns at lag 20 (monthly periodicity)."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(25, _TD_YEAR // 2)).apply(
        _ac_lag20, raw=True
    )


def rds_ext_068_sq_ret_autocorr_lag1_252d(close: pd.Series) -> pd.Series:
    """252-day lag-1 autocorrelation of squared returns."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(8, _TD_YEAR // 2)).apply(
        _sq_ret_autocorr_lag1, raw=True
    )


def rds_ext_069_autocorr_lag7_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day lag-7 autocorrelation in its 252-day distribution."""
    ac = rds_ext_065_autocorr_lag7_63d(close)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group M (070-072): Higher-order permutation entropy ---

def rds_ext_070_perm_entropy_order4_63d(close: pd.Series) -> pd.Series:
    """63-day normalized permutation entropy of order 4 (finer ordinal resolution)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(12, _TD_QTR // 2)).apply(
        _perm_entropy_order4, raw=True
    )


def rds_ext_071_perm_entropy_order5_126d(close: pd.Series) -> pd.Series:
    """126-day normalized permutation entropy of order 5."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(15, _TD_HALF // 2)).apply(
        _perm_entropy_order5, raw=True
    )


def rds_ext_072_perm_entropy_order4_vs_order3_63d(close: pd.Series) -> pd.Series:
    """63-day difference: permutation entropy order 4 minus order 3 (resolution gap)."""
    r = _log_ret(close)
    def _pe3(arr: np.ndarray) -> float:
        from math import factorial
        a = arr[~np.isnan(arr)]
        n = len(a)
        order = 3
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
    pe3 = r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(_pe3, raw=True)
    pe4 = rds_ext_070_perm_entropy_order4_63d(close)
    return pe4 - pe3


# --- Group N (073-075): Rate-of-change variants of extended statistics ---

def rds_ext_073_omega_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Omega ratio (velocity of reward/risk balance)."""
    om = rds_ext_001_omega_ratio_21d(close)
    return om.diff(_TD_WEEK)


def rds_ext_074_cf_var_5pct_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Cornish-Fisher VaR-5% (velocity of CF tail estimate)."""
    cv = rds_ext_014_cf_var_5pct_21d(close)
    return cv.diff(_TD_WEEK)


def rds_ext_075_hill_tail_index_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hill tail index (velocity of tail-heaviness change)."""
    hi = rds_ext_020_hill_tail_index_10pct_63d(close)
    return hi.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_EXTENDED_REGISTRY_001_075 = {
    "rds_ext_001_omega_ratio_21d": {"inputs": ["close"], "func": rds_ext_001_omega_ratio_21d},
    "rds_ext_002_omega_ratio_63d": {"inputs": ["close"], "func": rds_ext_002_omega_ratio_63d},
    "rds_ext_003_omega_ratio_126d": {"inputs": ["close"], "func": rds_ext_003_omega_ratio_126d},
    "rds_ext_004_omega_ratio_252d": {"inputs": ["close"], "func": rds_ext_004_omega_ratio_252d},
    "rds_ext_005_omega_ratio_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_005_omega_ratio_21d_pct_rank_252d},
    "rds_ext_006_omega_ratio_21d_zscore_252d": {"inputs": ["close"], "func": rds_ext_006_omega_ratio_21d_zscore_252d},
    "rds_ext_007_omega_ratio_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_007_omega_ratio_63d_pct_rank_252d},
    "rds_ext_008_omega_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_ext_008_omega_21d_vs_252d_ratio},
    "rds_ext_009_gain_to_pain_21d": {"inputs": ["close"], "func": rds_ext_009_gain_to_pain_21d},
    "rds_ext_010_gain_to_pain_63d": {"inputs": ["close"], "func": rds_ext_010_gain_to_pain_63d},
    "rds_ext_011_gain_to_pain_252d": {"inputs": ["close"], "func": rds_ext_011_gain_to_pain_252d},
    "rds_ext_012_gain_to_pain_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_012_gain_to_pain_21d_pct_rank_252d},
    "rds_ext_013_gain_to_pain_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_ext_013_gain_to_pain_21d_vs_252d_ratio},
    "rds_ext_014_cf_var_5pct_21d": {"inputs": ["close"], "func": rds_ext_014_cf_var_5pct_21d},
    "rds_ext_015_cf_var_5pct_63d": {"inputs": ["close"], "func": rds_ext_015_cf_var_5pct_63d},
    "rds_ext_016_cf_var_5pct_252d": {"inputs": ["close"], "func": rds_ext_016_cf_var_5pct_252d},
    "rds_ext_017_cf_var_1pct_63d": {"inputs": ["close"], "func": rds_ext_017_cf_var_1pct_63d},
    "rds_ext_018_cf_var_vs_historical_var_ratio_63d": {"inputs": ["close"], "func": rds_ext_018_cf_var_vs_historical_var_ratio_63d},
    "rds_ext_019_cf_var_5pct_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_019_cf_var_5pct_21d_pct_rank_252d},
    "rds_ext_020_hill_tail_index_10pct_63d": {"inputs": ["close"], "func": rds_ext_020_hill_tail_index_10pct_63d},
    "rds_ext_021_hill_tail_index_15pct_63d": {"inputs": ["close"], "func": rds_ext_021_hill_tail_index_15pct_63d},
    "rds_ext_022_hill_tail_index_10pct_252d": {"inputs": ["close"], "func": rds_ext_022_hill_tail_index_10pct_252d},
    "rds_ext_023_pot_exceed_15sigma_21d": {"inputs": ["close"], "func": rds_ext_023_pot_exceed_15sigma_21d},
    "rds_ext_024_pot_exceed_15sigma_63d": {"inputs": ["close"], "func": rds_ext_024_pot_exceed_15sigma_63d},
    "rds_ext_025_pot_exceed_20sigma_63d": {"inputs": ["close"], "func": rds_ext_025_pot_exceed_20sigma_63d},
    "rds_ext_026_conditional_dd_21d": {"inputs": ["close"], "func": rds_ext_026_conditional_dd_21d},
    "rds_ext_027_conditional_dd_63d": {"inputs": ["close"], "func": rds_ext_027_conditional_dd_63d},
    "rds_ext_028_conditional_dd_252d": {"inputs": ["close"], "func": rds_ext_028_conditional_dd_252d},
    "rds_ext_029_conditional_dd_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_029_conditional_dd_21d_pct_rank_252d},
    "rds_ext_030_conditional_dd_21d_zscore_252d": {"inputs": ["close"], "func": rds_ext_030_conditional_dd_21d_zscore_252d},
    "rds_ext_031_conditional_dd_63d_vs_21d_ratio": {"inputs": ["close"], "func": rds_ext_031_conditional_dd_63d_vs_21d_ratio},
    "rds_ext_032_max_to_mean_loss_21d": {"inputs": ["close"], "func": rds_ext_032_max_to_mean_loss_21d},
    "rds_ext_033_max_to_mean_loss_63d": {"inputs": ["close"], "func": rds_ext_033_max_to_mean_loss_63d},
    "rds_ext_034_max_gain_to_mean_gain_21d": {"inputs": ["close"], "func": rds_ext_034_max_gain_to_mean_gain_21d},
    "rds_ext_035_max_to_mean_loss_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_035_max_to_mean_loss_21d_pct_rank_252d},
    "rds_ext_036_max_loss_vs_cvar_ratio_63d": {"inputs": ["close"], "func": rds_ext_036_max_loss_vs_cvar_ratio_63d},
    "rds_ext_037_mode_gap_21d": {"inputs": ["close"], "func": rds_ext_037_mode_gap_21d},
    "rds_ext_038_mode_gap_63d": {"inputs": ["close"], "func": rds_ext_038_mode_gap_63d},
    "rds_ext_039_quantile_spread_norm_21d": {"inputs": ["close"], "func": rds_ext_039_quantile_spread_norm_21d},
    "rds_ext_040_quantile_spread_norm_63d": {"inputs": ["close"], "func": rds_ext_040_quantile_spread_norm_63d},
    "rds_ext_041_q25_logret_63d": {"inputs": ["close"], "func": rds_ext_041_q25_logret_63d},
    "rds_ext_042_q75_logret_63d": {"inputs": ["close"], "func": rds_ext_042_q75_logret_63d},
    "rds_ext_043_quantile_skew_63d": {"inputs": ["close"], "func": rds_ext_043_quantile_skew_63d},
    "rds_ext_044_runs_test_stat_21d": {"inputs": ["close"], "func": rds_ext_044_runs_test_stat_21d},
    "rds_ext_045_runs_test_stat_63d": {"inputs": ["close"], "func": rds_ext_045_runs_test_stat_63d},
    "rds_ext_046_sign_bias_21d": {"inputs": ["close"], "func": rds_ext_046_sign_bias_21d},
    "rds_ext_047_sign_bias_63d": {"inputs": ["close"], "func": rds_ext_047_sign_bias_63d},
    "rds_ext_048_consec_loss_max_21d": {"inputs": ["close"], "func": rds_ext_048_consec_loss_max_21d},
    "rds_ext_049_consec_loss_max_63d": {"inputs": ["close"], "func": rds_ext_049_consec_loss_max_63d},
    "rds_ext_050_approx_entropy_21d": {"inputs": ["close"], "func": rds_ext_050_approx_entropy_21d},
    "rds_ext_051_approx_entropy_63d": {"inputs": ["close"], "func": rds_ext_051_approx_entropy_63d},
    "rds_ext_052_sample_entropy_21d": {"inputs": ["close"], "func": rds_ext_052_sample_entropy_21d},
    "rds_ext_053_sample_entropy_63d": {"inputs": ["close"], "func": rds_ext_053_sample_entropy_63d},
    "rds_ext_054_approx_entropy_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_054_approx_entropy_21d_pct_rank_252d},
    "rds_ext_055_sample_entropy_63d_zscore_252d": {"inputs": ["close"], "func": rds_ext_055_sample_entropy_63d_zscore_252d},
    "rds_ext_056_dfa_multiscale_63d": {"inputs": ["close"], "func": rds_ext_056_dfa_multiscale_63d},
    "rds_ext_057_dfa_multiscale_126d": {"inputs": ["close"], "func": rds_ext_057_dfa_multiscale_126d},
    "rds_ext_058_dfa_multiscale_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_058_dfa_multiscale_63d_pct_rank_252d},
    "rds_ext_059_dfa_multiscale_vs_rs_diff_63d": {"inputs": ["close"], "func": rds_ext_059_dfa_multiscale_vs_rs_diff_63d},
    "rds_ext_060_return_clustering_21d": {"inputs": ["close"], "func": rds_ext_060_return_clustering_21d},
    "rds_ext_061_return_clustering_63d": {"inputs": ["close"], "func": rds_ext_061_return_clustering_63d},
    "rds_ext_062_sq_ret_autocorr_lag1_21d": {"inputs": ["close"], "func": rds_ext_062_sq_ret_autocorr_lag1_21d},
    "rds_ext_063_sq_ret_autocorr_lag1_63d": {"inputs": ["close"], "func": rds_ext_063_sq_ret_autocorr_lag1_63d},
    "rds_ext_064_return_clustering_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_064_return_clustering_63d_pct_rank_252d},
    "rds_ext_065_autocorr_lag7_63d": {"inputs": ["close"], "func": rds_ext_065_autocorr_lag7_63d},
    "rds_ext_066_autocorr_lag15_126d": {"inputs": ["close"], "func": rds_ext_066_autocorr_lag15_126d},
    "rds_ext_067_autocorr_lag20_252d": {"inputs": ["close"], "func": rds_ext_067_autocorr_lag20_252d},
    "rds_ext_068_sq_ret_autocorr_lag1_252d": {"inputs": ["close"], "func": rds_ext_068_sq_ret_autocorr_lag1_252d},
    "rds_ext_069_autocorr_lag7_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_ext_069_autocorr_lag7_63d_pct_rank_252d},
    "rds_ext_070_perm_entropy_order4_63d": {"inputs": ["close"], "func": rds_ext_070_perm_entropy_order4_63d},
    "rds_ext_071_perm_entropy_order5_126d": {"inputs": ["close"], "func": rds_ext_071_perm_entropy_order5_126d},
    "rds_ext_072_perm_entropy_order4_vs_order3_63d": {"inputs": ["close"], "func": rds_ext_072_perm_entropy_order4_vs_order3_63d},
    "rds_ext_073_omega_ratio_21d_5d_diff": {"inputs": ["close"], "func": rds_ext_073_omega_ratio_21d_5d_diff},
    "rds_ext_074_cf_var_5pct_21d_5d_diff": {"inputs": ["close"], "func": rds_ext_074_cf_var_5pct_21d_5d_diff},
    "rds_ext_075_hill_tail_index_63d_21d_diff": {"inputs": ["close"], "func": rds_ext_075_hill_tail_index_63d_21d_diff},
}
