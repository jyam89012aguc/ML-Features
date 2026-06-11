"""
11_decline_path_entropy — Base Features 076-150
Domain: smooth-vs-jagged structure of the decline path (disorder/randomness/regularity)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9
_N_BINS  = 8

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Scalar helpers for .apply (raw=True) ──────────────────────────────────────

def _shannon_entropy_raw(x: np.ndarray, n_bins: int = _N_BINS) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mn, mx = x.min(), x.max()
    if mx - mn < _EPS:
        return 0.0
    bins = np.linspace(mn, mx, n_bins + 1)
    counts, _ = np.histogram(x, bins=bins)
    total = counts.sum()
    if total == 0:
        return np.nan
    probs = counts[counts > 0] / total
    return float(-np.sum(probs * np.log(probs + _EPS)))


def _sign_change_rate_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    changes = np.sum(signs[1:] != signs[:-1])
    return float(changes / (len(x) - 1))


def _turning_point_density_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    tp = 0
    for i in range(1, len(x) - 1):
        if (x[i] > x[i - 1] and x[i] > x[i + 1]) or (x[i] < x[i - 1] and x[i] < x[i + 1]):
            tp += 1
    return float(tp / (len(x) - 2))


def _path_efficiency_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    net = abs(x[-1] - x[0])
    total = np.sum(np.abs(np.diff(x)))
    if total < _EPS:
        return 1.0
    return float(net / total)


def _permutation_entropy_raw(x: np.ndarray, order: int = 3) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < order + 1:
        return np.nan
    from math import factorial
    count = {}
    for i in range(n - order):
        pat = tuple(np.argsort(x[i:i + order]))
        count[pat] = count.get(pat, 0) + 1
    total = sum(count.values())
    if total == 0:
        return np.nan
    probs = np.array(list(count.values())) / total
    max_ent = np.log(factorial(order))
    if max_ent < _EPS:
        return 0.0
    ent = -np.sum(probs * np.log(probs + _EPS))
    return float(ent / max_ent)


def _hurst_rs_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    half = n // 2
    sub = [x[:half], x[half:half * 2]]
    rs_vals = []
    for seg in sub:
        mean_s = seg.mean()
        dev = np.cumsum(seg - mean_s)
        r = dev.max() - dev.min()
        s = seg.std()
        if s < _EPS:
            continue
        rs_vals.append(r / s)
    if len(rs_vals) == 0:
        return np.nan
    rs = np.mean(rs_vals)
    if rs <= 0:
        return np.nan
    return float(np.log(rs) / np.log(half + _EPS))


def _autocorr_lag1_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    s = pd.Series(x)
    c = s.autocorr(lag=1)
    return float(c) if not np.isnan(c) else np.nan


def _autocorr_lag2_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    s = pd.Series(x)
    c = s.autocorr(lag=2)
    return float(c) if not np.isnan(c) else np.nan


def _autocorr_lag5_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 7:
        return np.nan
    s = pd.Series(x)
    c = s.autocorr(lag=5)
    return float(c) if not np.isnan(c) else np.nan


def _neg_fraction_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.nan
    return float(np.sum(x < 0) / len(x))


def _return_dispersion_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    q75, q25 = np.percentile(x, 75), np.percentile(x, 25)
    iqr = q75 - q25
    med_abs = np.median(np.abs(x))
    if med_abs < _EPS:
        return np.nan
    return float(iqr / med_abs)


def _choppiness_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    rng = x.max() - x.min()
    atr_sum = np.sum(np.abs(np.diff(x)))
    if rng < _EPS or atr_sum < _EPS:
        return np.nan
    return float(np.log10(atr_sum) - np.log10(rng))


def _fractal_dim_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    def lm(k):
        total = 0.0
        for m_ in range(1, k + 1):
            idxs = np.arange(m_ - 1, n, k)
            if len(idxs) < 2:
                continue
            seg = x[idxs]
            lm_val = np.sum(np.abs(np.diff(seg))) * (n - 1) / (k * len(idxs))
            total += lm_val
        return total / k if k > 0 else np.nan
    l1, l2 = lm(1), lm(2)
    if l1 is None or l2 is None or l1 <= 0 or l2 <= 0:
        return np.nan
    return float(np.log(l1 / l2) / np.log(2.0))


def _run_length_mean_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    runs, cur = 1, 1
    count = 1
    for i in range(1, len(signs)):
        if signs[i] == signs[i - 1]:
            cur += 1
        else:
            runs += cur
            cur = 1
            count += 1
    runs += cur
    return float(runs / count) if count > 0 else np.nan


def _run_length_max_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    max_run, cur = 1, 1
    for i in range(1, len(signs)):
        if signs[i] == signs[i - 1]:
            cur += 1
            max_run = max(max_run, cur)
        else:
            cur = 1
    return float(max_run)


def _entropy_4bin_raw(x: np.ndarray) -> float:
    return _shannon_entropy_raw(x, n_bins=4)


def _entropy_16bin_raw(x: np.ndarray) -> float:
    return _shannon_entropy_raw(x, n_bins=16)


def _zero_crossing_rate_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    crosses = np.sum((x[:-1] * x[1:]) < 0)
    return float(crosses / (len(x) - 1))


def _sample_entropy_raw(x: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Sample entropy (simplified, m=2)."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < m + 2:
        return np.nan
    r = r_frac * (np.std(x) + _EPS)

    def count_matches(m_):
        c = 0
        for i in range(n - m_):
            for j in range(n - m_):
                if i != j and np.max(np.abs(x[i:i + m_] - x[j:j + m_])) <= r:
                    c += 1
        return c

    A = count_matches(m + 1)
    B = count_matches(m)
    if B == 0:
        return np.nan
    return float(-np.log((A + _EPS) / (B + _EPS)))


def _lyapunov_proxy_raw(x: np.ndarray) -> float:
    """Proxy for Lyapunov exponent: mean log |Δx(t+1)/Δx(t)|."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    dx = np.abs(np.diff(x))
    dx = np.where(dx < _EPS, _EPS, dx)
    ratios = dx[1:] / dx[:-1]
    return float(np.mean(np.log(ratios)))


def _gini_coeff_raw(x: np.ndarray) -> float:
    """Gini coefficient of the absolute-return distribution."""
    x = np.abs(x[~np.isnan(x)])
    n = len(x)
    if n < 2:
        return np.nan
    x = np.sort(x)
    idx = np.arange(1, n + 1)
    denom = n * x.sum()
    if denom < _EPS:
        return np.nan
    return float((2 * np.sum(idx * x) - (n + 1) * x.sum()) / denom)


def _kurtosis_raw(x: np.ndarray) -> float:
    """Excess kurtosis of x."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    mu = x.mean()
    s = x.std()
    if s < _EPS:
        return np.nan
    return float(np.mean(((x - mu) / s) ** 4) - 3.0)


def _skewness_raw(x: np.ndarray) -> float:
    """Skewness of x."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    mu = x.mean()
    s = x.std()
    if s < _EPS:
        return np.nan
    return float(np.mean(((x - mu) / s) ** 3))


def _tail_ratio_raw(x: np.ndarray) -> float:
    """95th-percentile abs return / 5th-percentile abs return (heavy tail indicator)."""
    x = np.abs(x[~np.isnan(x)])
    if len(x) < 5:
        return np.nan
    p95 = np.percentile(x, 95)
    p05 = np.percentile(x, 5)
    if p05 < _EPS:
        return np.nan
    return float(p95 / p05)


def _entropy_below_mean_raw(x: np.ndarray) -> float:
    """Shannon entropy of below-mean returns only."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    below = x[x < x.mean()]
    if len(below) < 2:
        return 0.0
    return _shannon_entropy_raw(below)


def _entropy_above_mean_raw(x: np.ndarray) -> float:
    """Shannon entropy of above-mean returns only."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    above = x[x >= x.mean()]
    if len(above) < 2:
        return 0.0
    return _shannon_entropy_raw(above)


def _max_drawdown_path_raw(x: np.ndarray) -> float:
    """Max drawdown within window (peak-to-trough of price path)."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    peak = x[0]
    max_dd = 0.0
    for v in x[1:]:
        if v > peak:
            peak = v
        dd = (v - peak) / (peak + _EPS)
        if dd < max_dd:
            max_dd = dd
    return float(max_dd)


def _mean_abs_dev_raw(x: np.ndarray) -> float:
    """Mean absolute deviation from median."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    return float(np.mean(np.abs(x - np.median(x))))


def _coefficient_variation_raw(x: np.ndarray) -> float:
    """Coefficient of variation (std/mean) of absolute returns."""
    x = np.abs(x[~np.isnan(x)])
    if len(x) < 2:
        return np.nan
    mu = x.mean()
    if mu < _EPS:
        return np.nan
    return float(x.std() / mu)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-087): Autocorrelation structure ---

def dpe_076_autocorr_lag2_ret_21d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of daily returns (21-day rolling)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag2_raw, raw=True)


def dpe_077_autocorr_lag2_ret_63d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of daily returns (63-day rolling)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _autocorr_lag2_raw, raw=True)


def dpe_078_autocorr_lag5_ret_21d(close: pd.Series) -> pd.Series:
    """Lag-5 (weekly) autocorrelation of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _autocorr_lag5_raw, raw=True)


def dpe_079_autocorr_lag5_ret_63d(close: pd.Series) -> pd.Series:
    """Lag-5 (weekly) autocorrelation of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _autocorr_lag5_raw, raw=True)


def dpe_080_autocorr_lag1_logret_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-returns (21-day)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_081_autocorr_lag1_logret_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-returns (63-day)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_082_autocorr_lag1_vol_21d(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of volume (21-day)."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_083_autocorr_lag1_hl_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of H-L range (21-day)."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_084_autocorr_lag2_logret_63d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of log-returns (63-day)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _autocorr_lag2_raw, raw=True)


def dpe_085_autocorr_lag1_absret_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of absolute daily returns (21-day) — ARCH proxy."""
    ret = _daily_ret(close).abs()
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_086_autocorr_lag1_absret_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of absolute daily returns (63-day)."""
    ret = _daily_ret(close).abs()
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_087_autocorr_decay_21d(close: pd.Series) -> pd.Series:
    """Difference between lag-1 and lag-2 autocorrelation of returns (21-day)."""
    ret = _daily_ret(close)
    ac1 = ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)
    ac2 = ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag2_raw, raw=True)
    return ac1 - ac2


# --- Group I (088-098): Return distribution shape ---

def dpe_088_return_kurtosis_21d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _kurtosis_raw, raw=True)


def dpe_089_return_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _kurtosis_raw, raw=True)


def dpe_090_return_skewness_21d(close: pd.Series) -> pd.Series:
    """Skewness of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _skewness_raw, raw=True)


def dpe_091_return_skewness_63d(close: pd.Series) -> pd.Series:
    """Skewness of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _skewness_raw, raw=True)


def dpe_092_return_tail_ratio_21d(close: pd.Series) -> pd.Series:
    """Tail ratio (p95/p5 of |returns|) over 21-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(6, _TD_MON // 2)).apply(
        _tail_ratio_raw, raw=True)


def dpe_093_return_tail_ratio_63d(close: pd.Series) -> pd.Series:
    """Tail ratio (p95/p5 of |returns|) over 63-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _tail_ratio_raw, raw=True)


def dpe_094_return_dispersion_iqr_21d(close: pd.Series) -> pd.Series:
    """IQR/median-abs return dispersion (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _return_dispersion_raw, raw=True)


def dpe_095_return_dispersion_iqr_63d(close: pd.Series) -> pd.Series:
    """IQR/median-abs return dispersion (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _return_dispersion_raw, raw=True)


def dpe_096_gini_absret_21d(close: pd.Series) -> pd.Series:
    """Gini coefficient of absolute daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _gini_coeff_raw, raw=True)


def dpe_097_gini_absret_63d(close: pd.Series) -> pd.Series:
    """Gini coefficient of absolute daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _gini_coeff_raw, raw=True)


def dpe_098_coeff_var_absret_21d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of absolute returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _coefficient_variation_raw, raw=True)


# --- Group J (099-110): Hurst & fractal variants ---

def dpe_099_hurst_rs_ret_21d(close: pd.Series) -> pd.Series:
    """Hurst R/S of daily returns (21-day window)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_100_hurst_rs_ret_63d(close: pd.Series) -> pd.Series:
    """Hurst R/S of daily returns (63-day window)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_101_hurst_rs_volume_21d(volume: pd.Series) -> pd.Series:
    """Hurst R/S of daily volume (21-day window)."""
    return volume.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_102_hurst_rs_logprice_63d(close: pd.Series) -> pd.Series:
    """Hurst R/S of log-close (63-day window)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_103_fractal_dim_logprice_21d(close: pd.Series) -> pd.Series:
    """Fractal dimension proxy of log-close (21-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_104_fractal_dim_logprice_63d(close: pd.Series) -> pd.Series:
    """Fractal dimension proxy of log-close (63-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_105_fractal_dim_hl_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fractal dimension proxy of H-L range (21-day)."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_106_fractal_dim_volume_21d(volume: pd.Series) -> pd.Series:
    """Fractal dimension proxy of volume (21-day)."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_107_lyapunov_proxy_ret_21d(close: pd.Series) -> pd.Series:
    """Lyapunov-exponent proxy of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _lyapunov_proxy_raw, raw=True)


def dpe_108_lyapunov_proxy_ret_63d(close: pd.Series) -> pd.Series:
    """Lyapunov-exponent proxy of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _lyapunov_proxy_raw, raw=True)


def dpe_109_lyapunov_proxy_close_21d(close: pd.Series) -> pd.Series:
    """Lyapunov-exponent proxy of close price (21-day)."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _lyapunov_proxy_raw, raw=True)


def dpe_110_fractal_dim_ret_63d(close: pd.Series) -> pd.Series:
    """Fractal dimension proxy of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _fractal_dim_raw, raw=True)


# --- Group K (111-121): Entropy of sub-series variants ---

def dpe_111_entropy_absret_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of absolute daily returns (21-day, 8-bin)."""
    ret = _daily_ret(close).abs()
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_112_entropy_absret_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of absolute daily returns (63-day, 8-bin)."""
    ret = _daily_ret(close).abs()
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_113_entropy_below_mean_ret_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of below-mean returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _entropy_below_mean_raw, raw=True)


def dpe_114_entropy_above_mean_ret_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of above-mean returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _entropy_above_mean_raw, raw=True)


def dpe_115_entropy_oc_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of open-to-close returns (21-day, 8-bin)."""
    oc = _safe_div(close - open, open)
    return oc.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_116_entropy_oc_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of open-to-close returns (63-day, 8-bin)."""
    oc = _safe_div(close - open, open)
    return oc.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_117_entropy_low_21d(low: pd.Series) -> pd.Series:
    """Shannon entropy of daily low price levels (21-day, 8-bin)."""
    return low.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_118_entropy_high_21d(high: pd.Series) -> pd.Series:
    """Shannon entropy of daily high price levels (21-day, 8-bin)."""
    return high.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_119_entropy_volume_63d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of daily volume distribution (63-day, 8-bin)."""
    return volume.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_120_entropy_volume_4bin_21d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of daily volume (21-day, 4-bin)."""
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _entropy_4bin_raw, raw=True)


def dpe_121_entropy_hl_range_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of H-L range (126-day, 8-bin)."""
    rng = high - low
    return rng.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(
        _shannon_entropy_raw, raw=True)


# --- Group L (122-133): Choppiness & smoothness variants ---

def dpe_122_choppiness_low_21d(low: pd.Series) -> pd.Series:
    """Choppiness index of daily low price path (21-day)."""
    return low.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_123_choppiness_high_21d(high: pd.Series) -> pd.Series:
    """Choppiness index of daily high price path (21-day)."""
    return high.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_124_choppiness_volume_21d(volume: pd.Series) -> pd.Series:
    """Choppiness index of daily volume (21-day)."""
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_125_choppiness_logprice_63d(close: pd.Series) -> pd.Series:
    """Choppiness index of log-close (63-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_126_smoothness_ratio_63d(close: pd.Series) -> pd.Series:
    """Smoothness ratio (std FD / mean abs FD) of close (63-day)."""
    fd = close.diff(1)
    std_fd = _rolling_std(fd, _TD_QTR)
    mean_abs = _rolling_mean(fd.abs(), _TD_QTR)
    return _safe_div(std_fd, mean_abs + _EPS)


def dpe_127_smoothness_ratio_ret_21d(close: pd.Series) -> pd.Series:
    """Smoothness ratio of daily returns (21-day)."""
    ret = _daily_ret(close)
    fd = ret.diff(1)
    std_fd = _rolling_std(fd, _TD_MON)
    mean_abs = _rolling_mean(fd.abs(), _TD_MON)
    return _safe_div(std_fd, mean_abs + _EPS)


def dpe_128_path_efficiency_open_63d(open: pd.Series) -> pd.Series:
    """Path efficiency of daily open price (63-day)."""
    return open.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_129_mean_abs_dev_ret_21d(close: pd.Series) -> pd.Series:
    """Mean absolute deviation from median return (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _mean_abs_dev_raw, raw=True)


def dpe_130_mean_abs_dev_ret_63d(close: pd.Series) -> pd.Series:
    """Mean absolute deviation from median return (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _mean_abs_dev_raw, raw=True)


def dpe_131_max_drawdown_path_21d(close: pd.Series) -> pd.Series:
    """Max drawdown within 21-day close-price path."""
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _max_drawdown_path_raw, raw=True)


def dpe_132_max_drawdown_path_63d(close: pd.Series) -> pd.Series:
    """Max drawdown within 63-day close-price path."""
    return close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _max_drawdown_path_raw, raw=True)


def dpe_133_choppiness_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Choppiness index of H-L range sequence (21-day)."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


# --- Group M (134-143): Multi-window entropy/disorder ratios ---

def dpe_134_entropy_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day return Shannon entropy."""
    ret = _daily_ret(close)
    e21 = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    e63 = ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)
    return _safe_div(e21, e63.replace(0, np.nan))


def dpe_135_sign_change_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day sign-change rates."""
    ret = _daily_ret(close)
    sc21 = ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)
    sc63 = ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _sign_change_rate_raw, raw=True)
    return _safe_div(sc21, sc63.replace(0, np.nan))


def dpe_136_tp_density_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day turning-point density."""
    tp21 = close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)
    tp63 = close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _turning_point_density_raw, raw=True)
    return _safe_div(tp21, tp63.replace(0, np.nan))


def dpe_137_perm_entropy_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day permutation entropy (order 3)."""
    pe21 = close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)
    pe63 = close.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _permutation_entropy_raw, raw=True)
    return _safe_div(pe21, pe63.replace(0, np.nan))


def dpe_138_path_eff_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day path efficiency."""
    pe21 = close.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)
    pe63 = close.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _path_efficiency_raw, raw=True)
    return _safe_div(pe21, pe63.replace(0, np.nan))


def dpe_139_neg_frac_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day negative-return fraction."""
    ret = _daily_ret(close)
    nf21 = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _neg_fraction_raw, raw=True)
    nf63 = ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _neg_fraction_raw, raw=True)
    return _safe_div(nf21, nf63.replace(0, np.nan))


def dpe_140_choppiness_diff_21d_63d(close: pd.Series) -> pd.Series:
    """Difference: 21-day minus 63-day choppiness index."""
    ch21 = close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)
    ch63 = close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _choppiness_raw, raw=True)
    return ch21 - ch63


def dpe_141_hurst_diff_21d_63d(close: pd.Series) -> pd.Series:
    """Difference: 21-day minus 63-day Hurst R/S estimate."""
    h21 = close.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)
    h63 = close.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hurst_rs_raw, raw=True)
    return h21 - h63


def dpe_142_entropy_vol_close_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume entropy to close-return entropy (21-day)."""
    ret = _daily_ret(close)
    ev = volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    er = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    return _safe_div(ev, er.replace(0, np.nan))


def dpe_143_perm_entropy_order3_logprice_21d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 21-day log-price sequence."""
    lp = _log_safe(close)
    return lp.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


# --- Group N (144-150): Sample entropy & disorder tail features ---

def dpe_144_sample_entropy_ret_21d(close: pd.Series) -> pd.Series:
    """Sample entropy (m=2) of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(6, _TD_MON // 2)).apply(
        _sample_entropy_raw, raw=True)


def dpe_145_sample_entropy_close_21d(close: pd.Series) -> pd.Series:
    """Sample entropy (m=2) of close prices (21-day)."""
    return close.rolling(_TD_MON, min_periods=max(6, _TD_MON // 2)).apply(
        _sample_entropy_raw, raw=True)


def dpe_146_sign_entropy_21d(close: pd.Series) -> pd.Series:
    """Binary (sign) entropy of return direction (21-day): -p*log(p)-(1-p)*log(1-p)."""
    ret = _daily_ret(close)
    def _binary_ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        p = np.sum(x > 0) / len(x)
        p = np.clip(p, _EPS, 1 - _EPS)
        return float(-(p * np.log(p) + (1 - p) * np.log(1 - p)))
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _binary_ent, raw=True)


def dpe_147_sign_entropy_63d(close: pd.Series) -> pd.Series:
    """Binary (sign) entropy of return direction (63-day)."""
    ret = _daily_ret(close)
    def _binary_ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        p = np.sum(x > 0) / len(x)
        p = np.clip(p, _EPS, 1 - _EPS)
        return float(-(p * np.log(p) + (1 - p) * np.log(1 - p)))
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _binary_ent, raw=True)


def dpe_148_coeff_var_absret_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of absolute returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _coefficient_variation_raw, raw=True)


def dpe_149_gini_volume_21d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily volume distribution (21-day)."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _gini_coeff_raw, raw=True)


def dpe_150_perm_entropy_order3_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 63-day H-L range sequence."""
    rng = high - low
    return rng.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _permutation_entropy_raw, raw=True)


# ── Registry ───────────────────────────────────────────────────────────────────

DECLINE_PATH_ENTROPY_REGISTRY_076_150 = {
    "dpe_076_autocorr_lag2_ret_21d":        {"inputs": ["close"],          "func": dpe_076_autocorr_lag2_ret_21d},
    "dpe_077_autocorr_lag2_ret_63d":        {"inputs": ["close"],          "func": dpe_077_autocorr_lag2_ret_63d},
    "dpe_078_autocorr_lag5_ret_21d":        {"inputs": ["close"],          "func": dpe_078_autocorr_lag5_ret_21d},
    "dpe_079_autocorr_lag5_ret_63d":        {"inputs": ["close"],          "func": dpe_079_autocorr_lag5_ret_63d},
    "dpe_080_autocorr_lag1_logret_21d":     {"inputs": ["close"],          "func": dpe_080_autocorr_lag1_logret_21d},
    "dpe_081_autocorr_lag1_logret_63d":     {"inputs": ["close"],          "func": dpe_081_autocorr_lag1_logret_63d},
    "dpe_082_autocorr_lag1_vol_21d":        {"inputs": ["volume"],         "func": dpe_082_autocorr_lag1_vol_21d},
    "dpe_083_autocorr_lag1_hl_range_21d":   {"inputs": ["high", "low"],    "func": dpe_083_autocorr_lag1_hl_range_21d},
    "dpe_084_autocorr_lag2_logret_63d":     {"inputs": ["close"],          "func": dpe_084_autocorr_lag2_logret_63d},
    "dpe_085_autocorr_lag1_absret_21d":     {"inputs": ["close"],          "func": dpe_085_autocorr_lag1_absret_21d},
    "dpe_086_autocorr_lag1_absret_63d":     {"inputs": ["close"],          "func": dpe_086_autocorr_lag1_absret_63d},
    "dpe_087_autocorr_decay_21d":           {"inputs": ["close"],          "func": dpe_087_autocorr_decay_21d},
    "dpe_088_return_kurtosis_21d":          {"inputs": ["close"],          "func": dpe_088_return_kurtosis_21d},
    "dpe_089_return_kurtosis_63d":          {"inputs": ["close"],          "func": dpe_089_return_kurtosis_63d},
    "dpe_090_return_skewness_21d":          {"inputs": ["close"],          "func": dpe_090_return_skewness_21d},
    "dpe_091_return_skewness_63d":          {"inputs": ["close"],          "func": dpe_091_return_skewness_63d},
    "dpe_092_return_tail_ratio_21d":        {"inputs": ["close"],          "func": dpe_092_return_tail_ratio_21d},
    "dpe_093_return_tail_ratio_63d":        {"inputs": ["close"],          "func": dpe_093_return_tail_ratio_63d},
    "dpe_094_return_dispersion_iqr_21d":    {"inputs": ["close"],          "func": dpe_094_return_dispersion_iqr_21d},
    "dpe_095_return_dispersion_iqr_63d":    {"inputs": ["close"],          "func": dpe_095_return_dispersion_iqr_63d},
    "dpe_096_gini_absret_21d":              {"inputs": ["close"],          "func": dpe_096_gini_absret_21d},
    "dpe_097_gini_absret_63d":              {"inputs": ["close"],          "func": dpe_097_gini_absret_63d},
    "dpe_098_coeff_var_absret_21d":         {"inputs": ["close"],          "func": dpe_098_coeff_var_absret_21d},
    "dpe_099_hurst_rs_ret_21d":             {"inputs": ["close"],          "func": dpe_099_hurst_rs_ret_21d},
    "dpe_100_hurst_rs_ret_63d":             {"inputs": ["close"],          "func": dpe_100_hurst_rs_ret_63d},
    "dpe_101_hurst_rs_volume_21d":          {"inputs": ["volume"],         "func": dpe_101_hurst_rs_volume_21d},
    "dpe_102_hurst_rs_logprice_63d":        {"inputs": ["close"],          "func": dpe_102_hurst_rs_logprice_63d},
    "dpe_103_fractal_dim_logprice_21d":     {"inputs": ["close"],          "func": dpe_103_fractal_dim_logprice_21d},
    "dpe_104_fractal_dim_logprice_63d":     {"inputs": ["close"],          "func": dpe_104_fractal_dim_logprice_63d},
    "dpe_105_fractal_dim_hl_range_21d":     {"inputs": ["high", "low"],    "func": dpe_105_fractal_dim_hl_range_21d},
    "dpe_106_fractal_dim_volume_21d":       {"inputs": ["volume"],         "func": dpe_106_fractal_dim_volume_21d},
    "dpe_107_lyapunov_proxy_ret_21d":       {"inputs": ["close"],          "func": dpe_107_lyapunov_proxy_ret_21d},
    "dpe_108_lyapunov_proxy_ret_63d":       {"inputs": ["close"],          "func": dpe_108_lyapunov_proxy_ret_63d},
    "dpe_109_lyapunov_proxy_close_21d":     {"inputs": ["close"],          "func": dpe_109_lyapunov_proxy_close_21d},
    "dpe_110_fractal_dim_ret_63d":          {"inputs": ["close"],          "func": dpe_110_fractal_dim_ret_63d},
    "dpe_111_entropy_absret_21d":           {"inputs": ["close"],          "func": dpe_111_entropy_absret_21d},
    "dpe_112_entropy_absret_63d":           {"inputs": ["close"],          "func": dpe_112_entropy_absret_63d},
    "dpe_113_entropy_below_mean_ret_21d":   {"inputs": ["close"],          "func": dpe_113_entropy_below_mean_ret_21d},
    "dpe_114_entropy_above_mean_ret_21d":   {"inputs": ["close"],          "func": dpe_114_entropy_above_mean_ret_21d},
    "dpe_115_entropy_oc_ret_21d":           {"inputs": ["open", "close"],  "func": dpe_115_entropy_oc_ret_21d},
    "dpe_116_entropy_oc_ret_63d":           {"inputs": ["open", "close"],  "func": dpe_116_entropy_oc_ret_63d},
    "dpe_117_entropy_low_21d":              {"inputs": ["low"],            "func": dpe_117_entropy_low_21d},
    "dpe_118_entropy_high_21d":             {"inputs": ["high"],           "func": dpe_118_entropy_high_21d},
    "dpe_119_entropy_volume_63d":           {"inputs": ["volume"],         "func": dpe_119_entropy_volume_63d},
    "dpe_120_entropy_volume_4bin_21d":      {"inputs": ["volume"],         "func": dpe_120_entropy_volume_4bin_21d},
    "dpe_121_entropy_hl_range_126d":        {"inputs": ["high", "low"],    "func": dpe_121_entropy_hl_range_126d},
    "dpe_122_choppiness_low_21d":           {"inputs": ["low"],            "func": dpe_122_choppiness_low_21d},
    "dpe_123_choppiness_high_21d":          {"inputs": ["high"],           "func": dpe_123_choppiness_high_21d},
    "dpe_124_choppiness_volume_21d":        {"inputs": ["volume"],         "func": dpe_124_choppiness_volume_21d},
    "dpe_125_choppiness_logprice_63d":      {"inputs": ["close"],          "func": dpe_125_choppiness_logprice_63d},
    "dpe_126_smoothness_ratio_63d":         {"inputs": ["close"],          "func": dpe_126_smoothness_ratio_63d},
    "dpe_127_smoothness_ratio_ret_21d":     {"inputs": ["close"],          "func": dpe_127_smoothness_ratio_ret_21d},
    "dpe_128_path_efficiency_open_63d":     {"inputs": ["open"],           "func": dpe_128_path_efficiency_open_63d},
    "dpe_129_mean_abs_dev_ret_21d":         {"inputs": ["close"],          "func": dpe_129_mean_abs_dev_ret_21d},
    "dpe_130_mean_abs_dev_ret_63d":         {"inputs": ["close"],          "func": dpe_130_mean_abs_dev_ret_63d},
    "dpe_131_max_drawdown_path_21d":        {"inputs": ["close"],          "func": dpe_131_max_drawdown_path_21d},
    "dpe_132_max_drawdown_path_63d":        {"inputs": ["close"],          "func": dpe_132_max_drawdown_path_63d},
    "dpe_133_choppiness_hl_21d":            {"inputs": ["high", "low"],    "func": dpe_133_choppiness_hl_21d},
    "dpe_134_entropy_ratio_21d_63d":        {"inputs": ["close"],          "func": dpe_134_entropy_ratio_21d_63d},
    "dpe_135_sign_change_ratio_21d_63d":    {"inputs": ["close"],          "func": dpe_135_sign_change_ratio_21d_63d},
    "dpe_136_tp_density_ratio_21d_63d":     {"inputs": ["close"],          "func": dpe_136_tp_density_ratio_21d_63d},
    "dpe_137_perm_entropy_ratio_21d_63d":   {"inputs": ["close"],          "func": dpe_137_perm_entropy_ratio_21d_63d},
    "dpe_138_path_eff_ratio_21d_63d":       {"inputs": ["close"],          "func": dpe_138_path_eff_ratio_21d_63d},
    "dpe_139_neg_frac_ratio_21d_63d":       {"inputs": ["close"],          "func": dpe_139_neg_frac_ratio_21d_63d},
    "dpe_140_choppiness_diff_21d_63d":      {"inputs": ["close"],          "func": dpe_140_choppiness_diff_21d_63d},
    "dpe_141_hurst_diff_21d_63d":           {"inputs": ["close"],          "func": dpe_141_hurst_diff_21d_63d},
    "dpe_142_entropy_vol_close_ratio_21d":  {"inputs": ["close", "volume"],"func": dpe_142_entropy_vol_close_ratio_21d},
    "dpe_143_perm_entropy_order3_logprice_21d": {"inputs": ["close"],      "func": dpe_143_perm_entropy_order3_logprice_21d},
    "dpe_144_sample_entropy_ret_21d":       {"inputs": ["close"],          "func": dpe_144_sample_entropy_ret_21d},
    "dpe_145_sample_entropy_close_21d":     {"inputs": ["close"],          "func": dpe_145_sample_entropy_close_21d},
    "dpe_146_sign_entropy_21d":             {"inputs": ["close"],          "func": dpe_146_sign_entropy_21d},
    "dpe_147_sign_entropy_63d":             {"inputs": ["close"],          "func": dpe_147_sign_entropy_63d},
    "dpe_148_coeff_var_absret_63d":         {"inputs": ["close"],          "func": dpe_148_coeff_var_absret_63d},
    "dpe_149_gini_volume_21d":              {"inputs": ["volume"],         "func": dpe_149_gini_volume_21d},
    "dpe_150_perm_entropy_order3_hl_63d":   {"inputs": ["high", "low"],    "func": dpe_150_perm_entropy_order3_hl_63d},
}
