"""
11_decline_path_entropy — Base Features 001-075
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


# ── Scalar helpers for .apply (raw=True arrays → single scalar) ───────────────

def _shannon_entropy_raw(x: np.ndarray, n_bins: int = _N_BINS) -> float:
    """Shannon entropy of binned values in x."""
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
    """Fraction of consecutive pairs with opposite sign (excluding zeros)."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    changes = np.sum(signs[1:] != signs[:-1])
    return float(changes / (len(x) - 1))


def _run_length_mean_raw(x: np.ndarray) -> float:
    """Mean run length of same-sign sequences."""
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
    """Max run length of same-sign sequences."""
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


def _turning_point_density_raw(x: np.ndarray) -> float:
    """Fraction of interior points that are local extrema."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    tp = 0
    for i in range(1, len(x) - 1):
        if (x[i] > x[i - 1] and x[i] > x[i + 1]) or (x[i] < x[i - 1] and x[i] < x[i + 1]):
            tp += 1
    return float(tp / (len(x) - 2))


def _path_efficiency_raw(x: np.ndarray) -> float:
    """Ratio of net displacement to total absolute path length."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    net = abs(x[-1] - x[0])
    total = np.sum(np.abs(np.diff(x)))
    if total < _EPS:
        return 1.0
    return float(net / total)


def _permutation_entropy_raw(x: np.ndarray, order: int = 3) -> float:
    """Permutation entropy of order `order`."""
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
    """Simplified R/S Hurst exponent estimate (log2 lags)."""
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
    """Lag-1 autocorrelation of x."""
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


def _return_dispersion_raw(x: np.ndarray) -> float:
    """IQR / median-absolute-value of return distribution."""
    x = x[~np.isnan(x)]
    if len(x) < 4:
        return np.nan
    q75, q25 = np.percentile(x, 75), np.percentile(x, 25)
    iqr = q75 - q25
    med_abs = np.median(np.abs(x))
    if med_abs < _EPS:
        return np.nan
    return float(iqr / med_abs)


def _neg_fraction_raw(x: np.ndarray) -> float:
    """Fraction of values that are strictly negative."""
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.nan
    return float(np.sum(x < 0) / len(x))


def _approx_entropy_raw(x: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Approximate entropy (lightweight, fixed m=2)."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < m + 2:
        return np.nan
    r = r_frac * (np.std(x) + _EPS)

    def phi(m_):
        count = 0
        total = 0
        for i in range(n - m_ + 1):
            template = x[i:i + m_]
            for j in range(n - m_ + 1):
                if np.max(np.abs(template - x[j:j + m_])) <= r:
                    count += 1
            total += 1
        if total == 0:
            return np.nan
        return np.log((count / total) + _EPS)

    p1 = phi(m)
    p2 = phi(m + 1)
    if p1 is None or p2 is None or np.isnan(p1) or np.isnan(p2):
        return np.nan
    return float(p1 - p2)


def _choppiness_raw(x: np.ndarray) -> float:
    """Choppiness index: log(sum|Δx|) / log(range), normalised."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2:
        return np.nan
    rng = x.max() - x.min()
    atr_sum = np.sum(np.abs(np.diff(x)))
    if rng < _EPS or atr_sum < _EPS:
        return np.nan
    return float(np.log10(atr_sum) - np.log10(rng))


def _fractal_dim_raw(x: np.ndarray) -> float:
    """Higuchi-style fractal dimension proxy (2 lags)."""
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
    fd = np.log(l1 / l2) / np.log(2.0)
    return float(fd)


def _entropy_4bin_raw(x: np.ndarray) -> float:
    return _shannon_entropy_raw(x, n_bins=4)


def _entropy_16bin_raw(x: np.ndarray) -> float:
    return _shannon_entropy_raw(x, n_bins=16)


def _run_length_std_raw(x: np.ndarray) -> float:
    """Std of run lengths of same-sign sequences."""
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    signs = np.sign(x)
    runs = []
    cur = 1
    for i in range(1, len(signs)):
        if signs[i] == signs[i - 1]:
            cur += 1
        else:
            runs.append(cur)
            cur = 1
    runs.append(cur)
    if len(runs) < 2:
        return 0.0
    return float(np.std(runs))


def _down_run_mean_raw(x: np.ndarray) -> float:
    """Mean length of consecutive down (negative) runs."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    runs = []
    cur = 0
    in_down = False
    for s in signs:
        if s < 0:
            cur += 1
            in_down = True
        else:
            if in_down:
                runs.append(cur)
            cur = 0
            in_down = False
    if in_down:
        runs.append(cur)
    if len(runs) == 0:
        return 0.0
    return float(np.mean(runs))


def _up_run_mean_raw(x: np.ndarray) -> float:
    """Mean length of consecutive up (positive) runs."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    runs = []
    cur = 0
    in_up = False
    for s in signs:
        if s > 0:
            cur += 1
            in_up = True
        else:
            if in_up:
                runs.append(cur)
            cur = 0
            in_up = False
    if in_up:
        runs.append(cur)
    if len(runs) == 0:
        return 0.0
    return float(np.mean(runs))


def _zero_crossing_rate_raw(x: np.ndarray) -> float:
    """Fraction of consecutive pairs that cross zero."""
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    crosses = np.sum((x[:-1] * x[1:]) < 0)
    return float(crosses / (len(x) - 1))


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Shannon entropy of return distributions ---

def dpe_001_shannon_entropy_ret_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 21-day daily return distribution (8-bin)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_002_shannon_entropy_ret_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 63-day daily return distribution (8-bin)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_003_shannon_entropy_ret_126d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 126-day daily return distribution (8-bin)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_004_shannon_entropy_ret_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 252-day daily return distribution (8-bin)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_YEAR, min_periods=max(20, _TD_YEAR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_005_shannon_entropy_ret_21d_4bin(close: pd.Series) -> pd.Series:
    """Shannon entropy of 21-day returns (4-bin coarser discretisation)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _entropy_4bin_raw, raw=True)


def dpe_006_shannon_entropy_ret_63d_4bin(close: pd.Series) -> pd.Series:
    """Shannon entropy of 63-day returns (4-bin)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _entropy_4bin_raw, raw=True)


def dpe_007_shannon_entropy_ret_21d_16bin(close: pd.Series) -> pd.Series:
    """Shannon entropy of 21-day returns (16-bin finer discretisation)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _entropy_16bin_raw, raw=True)


def dpe_008_shannon_entropy_logret_21d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 21-day log-return distribution (8-bin)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_009_shannon_entropy_logret_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 63-day log-return distribution (8-bin)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_010_shannon_entropy_hl_range_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of daily H-L range distribution (21-day)."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_011_shannon_entropy_hl_range_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Shannon entropy of daily H-L range distribution (63-day)."""
    rng = high - low
    return rng.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def dpe_012_shannon_entropy_volume_21d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of daily volume distribution (21-day, 8-bin)."""
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


# --- Group B (013-024): Sign-change frequency of returns ---

def dpe_013_sign_change_rate_ret_10d(close: pd.Series) -> pd.Series:
    """Fraction of consecutive-day return sign flips (10-day window)."""
    ret = _daily_ret(close)
    return ret.rolling(10, min_periods=4).apply(_sign_change_rate_raw, raw=True)


def dpe_014_sign_change_rate_ret_21d(close: pd.Series) -> pd.Series:
    """Fraction of consecutive-day return sign flips (21-day window)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_015_sign_change_rate_ret_63d(close: pd.Series) -> pd.Series:
    """Fraction of consecutive-day return sign flips (63-day window)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_016_sign_change_rate_ret_126d(close: pd.Series) -> pd.Series:
    """Sign-flip rate in 126-day return window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_017_sign_change_rate_logret_21d(close: pd.Series) -> pd.Series:
    """Sign-flip rate of log-returns (21-day)."""
    logret = _log_safe(close).diff(1)
    return logret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_018_sign_change_rate_hl_diff_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign-flip rate of first-difference of H-L range (21-day)."""
    rng_diff = (high - low).diff(1)
    return rng_diff.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_019_zero_crossing_rate_ret_21d(close: pd.Series) -> pd.Series:
    """Zero-crossing rate of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _zero_crossing_rate_raw, raw=True)


def dpe_020_zero_crossing_rate_ret_63d(close: pd.Series) -> pd.Series:
    """Zero-crossing rate of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _zero_crossing_rate_raw, raw=True)


def dpe_021_sign_change_rate_open_close_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sign-flip rate of open-to-close return (21-day)."""
    oc_ret = _safe_div(close - open, open)
    return oc_ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_022_sign_change_rate_open_close_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sign-flip rate of open-to-close return (63-day)."""
    oc_ret = _safe_div(close - open, open)
    return oc_ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_023_sign_change_rate_volume_diff_21d(volume: pd.Series) -> pd.Series:
    """Sign-flip rate of volume first-differences (21-day)."""
    vd = volume.diff(1)
    return vd.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def dpe_024_neg_return_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of negative daily returns in 21-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _neg_fraction_raw, raw=True)


# --- Group C (025-034): Run-length statistics ---

def dpe_025_run_length_mean_21d(close: pd.Series) -> pd.Series:
    """Mean same-sign run length of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _run_length_mean_raw, raw=True)


def dpe_026_run_length_mean_63d(close: pd.Series) -> pd.Series:
    """Mean same-sign run length of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _run_length_mean_raw, raw=True)


def dpe_027_run_length_max_21d(close: pd.Series) -> pd.Series:
    """Max same-sign run length of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _run_length_max_raw, raw=True)


def dpe_028_run_length_max_63d(close: pd.Series) -> pd.Series:
    """Max same-sign run length of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _run_length_max_raw, raw=True)


def dpe_029_run_length_std_21d(close: pd.Series) -> pd.Series:
    """Std of same-sign run lengths (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _run_length_std_raw, raw=True)


def dpe_030_run_length_std_63d(close: pd.Series) -> pd.Series:
    """Std of same-sign run lengths (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _run_length_std_raw, raw=True)


def dpe_031_down_run_mean_21d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive down-day runs (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _down_run_mean_raw, raw=True)


def dpe_032_down_run_mean_63d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive down-day runs (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _down_run_mean_raw, raw=True)


def dpe_033_up_run_mean_21d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive up-day runs (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _up_run_mean_raw, raw=True)


def dpe_034_up_run_mean_63d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive up-day runs (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _up_run_mean_raw, raw=True)


# --- Group D (035-044): Permutation entropy ---

def dpe_035_perm_entropy_order3_21d(close: pd.Series) -> pd.Series:
    """Normalised permutation entropy (order 3, 21-day window) of close prices."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_036_perm_entropy_order3_63d(close: pd.Series) -> pd.Series:
    """Normalised permutation entropy (order 3, 63-day window) of close prices."""
    return close.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_037_perm_entropy_order4_21d(close: pd.Series) -> pd.Series:
    """Normalised permutation entropy (order 4, 21-day window)."""
    def _pe4(x):
        return _permutation_entropy_raw(x, order=4)
    return close.rolling(_TD_MON, min_periods=max(6, _TD_MON // 2)).apply(
        _pe4, raw=True)


def dpe_038_perm_entropy_order3_ret_21d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 21-day daily-return sequence."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_039_perm_entropy_order3_ret_63d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 63-day daily-return sequence."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_040_perm_entropy_order3_volume_21d(volume: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 21-day volume sequence."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_041_perm_entropy_order3_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 21-day H-L range sequence."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_042_perm_entropy_order3_logprice_63d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 63-day log-price sequence."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_043_perm_entropy_order3_openclose_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Permutation entropy (order 3) of 21-day open-to-close return sequence."""
    oc = _safe_div(close - open, open)
    return oc.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def dpe_044_perm_entropy_order4_ret_63d(close: pd.Series) -> pd.Series:
    """Permutation entropy (order 4) of 63-day daily-return sequence."""
    def _pe4(x):
        return _permutation_entropy_raw(x, order=4)
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _pe4, raw=True)


# --- Group E (045-054): Path efficiency / directional efficiency ---

def dpe_045_path_efficiency_close_21d(close: pd.Series) -> pd.Series:
    """Net displacement / total path length of close price (21-day)."""
    return close.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_046_path_efficiency_close_63d(close: pd.Series) -> pd.Series:
    """Net displacement / total path length of close price (63-day)."""
    return close.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_047_path_efficiency_close_126d(close: pd.Series) -> pd.Series:
    """Path efficiency of close price (126-day)."""
    return close.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_048_path_efficiency_log_21d(close: pd.Series) -> pd.Series:
    """Path efficiency of log-close price (21-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_049_path_efficiency_log_63d(close: pd.Series) -> pd.Series:
    """Path efficiency of log-close price (63-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_050_path_efficiency_low_21d(low: pd.Series) -> pd.Series:
    """Path efficiency of daily low price (21-day)."""
    return low.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_051_path_efficiency_low_63d(low: pd.Series) -> pd.Series:
    """Path efficiency of daily low price (63-day)."""
    return low.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _path_efficiency_raw, raw=True)


def dpe_052_net_ret_vs_total_abs_ret_21d(close: pd.Series) -> pd.Series:
    """Net 21-day return divided by sum of absolute daily returns."""
    ret = _daily_ret(close)
    net_ret = (close / close.shift(20) - 1).abs()
    sum_abs = _rolling_sum(ret.abs(), _TD_MON)
    return _safe_div(net_ret, sum_abs)


def dpe_053_net_ret_vs_total_abs_ret_63d(close: pd.Series) -> pd.Series:
    """Net 63-day return divided by sum of absolute daily returns."""
    ret = _daily_ret(close)
    net_ret = (close / close.shift(62) - 1).abs()
    sum_abs = _rolling_sum(ret.abs(), _TD_QTR)
    return _safe_div(net_ret, sum_abs)


def dpe_054_smoothness_ratio_21d(close: pd.Series) -> pd.Series:
    """Smoothness: std of first-differences / mean abs first-difference (21-day)."""
    fd = close.diff(1)
    std_fd = _rolling_std(fd, _TD_MON)
    mean_abs = _rolling_mean(fd.abs(), _TD_MON)
    return _safe_div(std_fd, mean_abs + _EPS)


# --- Group F (055-064): Turning-point density & local extrema ---

def dpe_055_turning_point_density_21d(close: pd.Series) -> pd.Series:
    """Fraction of days that are local price extrema (21-day window)."""
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_056_turning_point_density_63d(close: pd.Series) -> pd.Series:
    """Turning-point density of close price (63-day window)."""
    return close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_057_turning_point_density_ret_21d(close: pd.Series) -> pd.Series:
    """Turning-point density of daily returns (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_058_turning_point_density_ret_63d(close: pd.Series) -> pd.Series:
    """Turning-point density of daily returns (63-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_059_turning_point_density_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Turning-point density of H-L range (21-day)."""
    rng = high - low
    return rng.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_060_tp_density_low_21d(low: pd.Series) -> pd.Series:
    """Turning-point density of intraday lows (21-day)."""
    return low.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_061_tp_density_volume_21d(volume: pd.Series) -> pd.Series:
    """Turning-point density of daily volume (21-day)."""
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_062_tp_density_volume_63d(volume: pd.Series) -> pd.Series:
    """Turning-point density of daily volume (63-day)."""
    return volume.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_063_tp_density_openclose_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Turning-point density of open-to-close returns (21-day)."""
    oc = _safe_div(close - open, open)
    return oc.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def dpe_064_tp_density_logprice_63d(close: pd.Series) -> pd.Series:
    """Turning-point density of log-close prices (63-day)."""
    lp = _log_safe(close)
    return lp.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _turning_point_density_raw, raw=True)


# --- Group G (065-075): Choppiness, fractal dimension, autocorrelation, Hurst ---

def dpe_065_choppiness_index_21d(close: pd.Series) -> pd.Series:
    """Choppiness index of close-price path (21-day)."""
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_066_choppiness_index_63d(close: pd.Series) -> pd.Series:
    """Choppiness index of close-price path (63-day)."""
    return close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_067_choppiness_ret_21d(close: pd.Series) -> pd.Series:
    """Choppiness index of daily-return sequence (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def dpe_068_fractal_dim_close_21d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension proxy of close-price path (21-day)."""
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_069_fractal_dim_close_63d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension proxy of close-price path (63-day)."""
    return close.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_070_fractal_dim_ret_21d(close: pd.Series) -> pd.Series:
    """Fractal dimension proxy of daily-return sequence (21-day)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def dpe_071_hurst_rs_21d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent estimate from 21-day close-price window."""
    return close.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_072_hurst_rs_63d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent estimate from 63-day close-price window."""
    return close.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hurst_rs_raw, raw=True)


def dpe_073_autocorr_lag1_ret_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns (21-day rolling)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_074_autocorr_lag1_ret_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily returns (63-day rolling)."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(
        _autocorr_lag1_raw, raw=True)


def dpe_075_neg_return_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of negative daily returns in 63-day window."""
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _neg_fraction_raw, raw=True)


# ── Registry ───────────────────────────────────────────────────────────────────

DECLINE_PATH_ENTROPY_REGISTRY_001_075 = {
    "dpe_001_shannon_entropy_ret_21d":          {"inputs": ["close"],             "func": dpe_001_shannon_entropy_ret_21d},
    "dpe_002_shannon_entropy_ret_63d":          {"inputs": ["close"],             "func": dpe_002_shannon_entropy_ret_63d},
    "dpe_003_shannon_entropy_ret_126d":         {"inputs": ["close"],             "func": dpe_003_shannon_entropy_ret_126d},
    "dpe_004_shannon_entropy_ret_252d":         {"inputs": ["close"],             "func": dpe_004_shannon_entropy_ret_252d},
    "dpe_005_shannon_entropy_ret_21d_4bin":     {"inputs": ["close"],             "func": dpe_005_shannon_entropy_ret_21d_4bin},
    "dpe_006_shannon_entropy_ret_63d_4bin":     {"inputs": ["close"],             "func": dpe_006_shannon_entropy_ret_63d_4bin},
    "dpe_007_shannon_entropy_ret_21d_16bin":    {"inputs": ["close"],             "func": dpe_007_shannon_entropy_ret_21d_16bin},
    "dpe_008_shannon_entropy_logret_21d":       {"inputs": ["close"],             "func": dpe_008_shannon_entropy_logret_21d},
    "dpe_009_shannon_entropy_logret_63d":       {"inputs": ["close"],             "func": dpe_009_shannon_entropy_logret_63d},
    "dpe_010_shannon_entropy_hl_range_21d":     {"inputs": ["high", "low"],       "func": dpe_010_shannon_entropy_hl_range_21d},
    "dpe_011_shannon_entropy_hl_range_63d":     {"inputs": ["high", "low"],       "func": dpe_011_shannon_entropy_hl_range_63d},
    "dpe_012_shannon_entropy_volume_21d":       {"inputs": ["volume"],            "func": dpe_012_shannon_entropy_volume_21d},
    "dpe_013_sign_change_rate_ret_10d":         {"inputs": ["close"],             "func": dpe_013_sign_change_rate_ret_10d},
    "dpe_014_sign_change_rate_ret_21d":         {"inputs": ["close"],             "func": dpe_014_sign_change_rate_ret_21d},
    "dpe_015_sign_change_rate_ret_63d":         {"inputs": ["close"],             "func": dpe_015_sign_change_rate_ret_63d},
    "dpe_016_sign_change_rate_ret_126d":        {"inputs": ["close"],             "func": dpe_016_sign_change_rate_ret_126d},
    "dpe_017_sign_change_rate_logret_21d":      {"inputs": ["close"],             "func": dpe_017_sign_change_rate_logret_21d},
    "dpe_018_sign_change_rate_hl_diff_21d":     {"inputs": ["high", "low"],       "func": dpe_018_sign_change_rate_hl_diff_21d},
    "dpe_019_zero_crossing_rate_ret_21d":       {"inputs": ["close"],             "func": dpe_019_zero_crossing_rate_ret_21d},
    "dpe_020_zero_crossing_rate_ret_63d":       {"inputs": ["close"],             "func": dpe_020_zero_crossing_rate_ret_63d},
    "dpe_021_sign_change_rate_open_close_21d":  {"inputs": ["open", "close"],     "func": dpe_021_sign_change_rate_open_close_21d},
    "dpe_022_sign_change_rate_open_close_63d":  {"inputs": ["open", "close"],     "func": dpe_022_sign_change_rate_open_close_63d},
    "dpe_023_sign_change_rate_volume_diff_21d": {"inputs": ["volume"],            "func": dpe_023_sign_change_rate_volume_diff_21d},
    "dpe_024_neg_return_fraction_21d":          {"inputs": ["close"],             "func": dpe_024_neg_return_fraction_21d},
    "dpe_025_run_length_mean_21d":              {"inputs": ["close"],             "func": dpe_025_run_length_mean_21d},
    "dpe_026_run_length_mean_63d":              {"inputs": ["close"],             "func": dpe_026_run_length_mean_63d},
    "dpe_027_run_length_max_21d":               {"inputs": ["close"],             "func": dpe_027_run_length_max_21d},
    "dpe_028_run_length_max_63d":               {"inputs": ["close"],             "func": dpe_028_run_length_max_63d},
    "dpe_029_run_length_std_21d":               {"inputs": ["close"],             "func": dpe_029_run_length_std_21d},
    "dpe_030_run_length_std_63d":               {"inputs": ["close"],             "func": dpe_030_run_length_std_63d},
    "dpe_031_down_run_mean_21d":                {"inputs": ["close"],             "func": dpe_031_down_run_mean_21d},
    "dpe_032_down_run_mean_63d":                {"inputs": ["close"],             "func": dpe_032_down_run_mean_63d},
    "dpe_033_up_run_mean_21d":                  {"inputs": ["close"],             "func": dpe_033_up_run_mean_21d},
    "dpe_034_up_run_mean_63d":                  {"inputs": ["close"],             "func": dpe_034_up_run_mean_63d},
    "dpe_035_perm_entropy_order3_21d":          {"inputs": ["close"],             "func": dpe_035_perm_entropy_order3_21d},
    "dpe_036_perm_entropy_order3_63d":          {"inputs": ["close"],             "func": dpe_036_perm_entropy_order3_63d},
    "dpe_037_perm_entropy_order4_21d":          {"inputs": ["close"],             "func": dpe_037_perm_entropy_order4_21d},
    "dpe_038_perm_entropy_order3_ret_21d":      {"inputs": ["close"],             "func": dpe_038_perm_entropy_order3_ret_21d},
    "dpe_039_perm_entropy_order3_ret_63d":      {"inputs": ["close"],             "func": dpe_039_perm_entropy_order3_ret_63d},
    "dpe_040_perm_entropy_order3_volume_21d":   {"inputs": ["volume"],            "func": dpe_040_perm_entropy_order3_volume_21d},
    "dpe_041_perm_entropy_order3_hl_21d":       {"inputs": ["high", "low"],       "func": dpe_041_perm_entropy_order3_hl_21d},
    "dpe_042_perm_entropy_order3_logprice_63d": {"inputs": ["close"],             "func": dpe_042_perm_entropy_order3_logprice_63d},
    "dpe_043_perm_entropy_order3_openclose_21d":{"inputs": ["open", "close"],     "func": dpe_043_perm_entropy_order3_openclose_21d},
    "dpe_044_perm_entropy_order4_ret_63d":      {"inputs": ["close"],             "func": dpe_044_perm_entropy_order4_ret_63d},
    "dpe_045_path_efficiency_close_21d":        {"inputs": ["close"],             "func": dpe_045_path_efficiency_close_21d},
    "dpe_046_path_efficiency_close_63d":        {"inputs": ["close"],             "func": dpe_046_path_efficiency_close_63d},
    "dpe_047_path_efficiency_close_126d":       {"inputs": ["close"],             "func": dpe_047_path_efficiency_close_126d},
    "dpe_048_path_efficiency_log_21d":          {"inputs": ["close"],             "func": dpe_048_path_efficiency_log_21d},
    "dpe_049_path_efficiency_log_63d":          {"inputs": ["close"],             "func": dpe_049_path_efficiency_log_63d},
    "dpe_050_path_efficiency_low_21d":          {"inputs": ["low"],               "func": dpe_050_path_efficiency_low_21d},
    "dpe_051_path_efficiency_low_63d":          {"inputs": ["low"],               "func": dpe_051_path_efficiency_low_63d},
    "dpe_052_net_ret_vs_total_abs_ret_21d":     {"inputs": ["close"],             "func": dpe_052_net_ret_vs_total_abs_ret_21d},
    "dpe_053_net_ret_vs_total_abs_ret_63d":     {"inputs": ["close"],             "func": dpe_053_net_ret_vs_total_abs_ret_63d},
    "dpe_054_smoothness_ratio_21d":             {"inputs": ["close"],             "func": dpe_054_smoothness_ratio_21d},
    "dpe_055_turning_point_density_21d":        {"inputs": ["close"],             "func": dpe_055_turning_point_density_21d},
    "dpe_056_turning_point_density_63d":        {"inputs": ["close"],             "func": dpe_056_turning_point_density_63d},
    "dpe_057_turning_point_density_ret_21d":    {"inputs": ["close"],             "func": dpe_057_turning_point_density_ret_21d},
    "dpe_058_turning_point_density_ret_63d":    {"inputs": ["close"],             "func": dpe_058_turning_point_density_ret_63d},
    "dpe_059_turning_point_density_hl_21d":     {"inputs": ["high", "low"],       "func": dpe_059_turning_point_density_hl_21d},
    "dpe_060_tp_density_low_21d":               {"inputs": ["low"],               "func": dpe_060_tp_density_low_21d},
    "dpe_061_tp_density_volume_21d":            {"inputs": ["volume"],            "func": dpe_061_tp_density_volume_21d},
    "dpe_062_tp_density_volume_63d":            {"inputs": ["volume"],            "func": dpe_062_tp_density_volume_63d},
    "dpe_063_tp_density_openclose_ret_21d":     {"inputs": ["open", "close"],     "func": dpe_063_tp_density_openclose_ret_21d},
    "dpe_064_tp_density_logprice_63d":          {"inputs": ["close"],             "func": dpe_064_tp_density_logprice_63d},
    "dpe_065_choppiness_index_21d":             {"inputs": ["close"],             "func": dpe_065_choppiness_index_21d},
    "dpe_066_choppiness_index_63d":             {"inputs": ["close"],             "func": dpe_066_choppiness_index_63d},
    "dpe_067_choppiness_ret_21d":               {"inputs": ["close"],             "func": dpe_067_choppiness_ret_21d},
    "dpe_068_fractal_dim_close_21d":            {"inputs": ["close"],             "func": dpe_068_fractal_dim_close_21d},
    "dpe_069_fractal_dim_close_63d":            {"inputs": ["close"],             "func": dpe_069_fractal_dim_close_63d},
    "dpe_070_fractal_dim_ret_21d":              {"inputs": ["close"],             "func": dpe_070_fractal_dim_ret_21d},
    "dpe_071_hurst_rs_21d":                     {"inputs": ["close"],             "func": dpe_071_hurst_rs_21d},
    "dpe_072_hurst_rs_63d":                     {"inputs": ["close"],             "func": dpe_072_hurst_rs_63d},
    "dpe_073_autocorr_lag1_ret_21d":            {"inputs": ["close"],             "func": dpe_073_autocorr_lag1_ret_21d},
    "dpe_074_autocorr_lag1_ret_63d":            {"inputs": ["close"],             "func": dpe_074_autocorr_lag1_ret_63d},
    "dpe_075_neg_return_fraction_63d":          {"inputs": ["close"],             "func": dpe_075_neg_return_fraction_63d},
}
