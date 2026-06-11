"""
120_information_decay — Extended Features 001-075
Domain: information decay — deeper variants: fractional integration, long-memory DFA,
        cross-series MI decay, multi-scale entropy, higher-lag AC structure,
        volume-augmented decay, range-based memory, nonlinear decay proxies
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation at given lag over window w. NaN-safe."""
    def _ac(x):
        x = x[~np.isnan(x)]
        if len(x) < lag + 3:
            return np.nan
        x0, x1 = x[:-lag], x[lag:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    return s.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _decay_rate_from_two_lags(ac1: pd.Series, ac2: pd.Series) -> pd.Series:
    ratio = _safe_div(ac2.abs(), ac1.abs().clip(lower=_EPS))
    ratio_c = ratio.clip(lower=_EPS, upper=1.0 - _EPS)
    return -np.log(ratio_c)


def _halflife_from_decay(rate: pd.Series) -> pd.Series:
    return np.log(2.0) / rate.clip(lower=_EPS)


def _hurst_rs(x: np.ndarray) -> float:
    """R/S Hurst exponent. NaN-safe."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 10:
        return np.nan
    lags, rs_vals = [], []
    for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
        if w > n:
            continue
        seg = x[:w]
        dev = np.cumsum(seg - seg.mean())
        r_val = dev.max() - dev.min()
        s_val = seg.std()
        if s_val < _EPS:
            continue
        lags.append(np.log(w))
        rs_vals.append(np.log(r_val / s_val))
    if len(lags) < 2:
        return np.nan
    lags, rs_vals = np.array(lags), np.array(rs_vals)
    if lags.std() < _EPS:
        return np.nan
    return float(np.polyfit(lags, rs_vals, 1)[0])


def _dfa_alpha(x: np.ndarray, min_w: int = 6, max_w: int = None) -> float:
    """
    Detrended Fluctuation Analysis scaling exponent alpha.
    alpha~0.5 = random walk; alpha>0.5 = persistent; alpha<0.5 = anti-persistent.
    """
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    if max_w is None:
        max_w = n // 2
    max_w = max(min_w + 1, min(max_w, n // 2))
    y = np.cumsum(x - x.mean())
    scales = []
    flucts = []
    for w in np.unique(np.round(np.geomspace(min_w, max_w, 8)).astype(int)):
        w = int(w)
        if w < 4 or w > n:
            continue
        n_segs = n // w
        if n_segs < 2:
            continue
        f2 = []
        for i in range(n_segs):
            seg = y[i * w:(i + 1) * w]
            xi = np.arange(len(seg), dtype=float)
            if xi.std() < _EPS:
                continue
            coeffs = np.polyfit(xi, seg, 1)
            trend = np.polyval(coeffs, xi)
            f2.append(np.mean((seg - trend) ** 2))
        if len(f2) == 0:
            continue
        scales.append(np.log(w))
        flucts.append(0.5 * np.log(np.mean(f2) + _EPS))
    if len(scales) < 2:
        return np.nan
    scales, flucts = np.array(scales), np.array(flucts)
    if scales.std() < _EPS:
        return np.nan
    return float(np.polyfit(scales, flucts, 1)[0])


def _mi_proxy(x: np.ndarray, y: np.ndarray, bins: int = 5) -> float:
    """Normalized mutual information proxy."""
    valid = np.isfinite(x) & np.isfinite(y)
    x, y = x[valid], y[valid]
    if len(x) < bins * 2:
        return np.nan
    try:
        hist_xy, _, _ = np.histogram2d(x, y, bins=bins)
        n = hist_xy.sum()
        if n == 0:
            return np.nan
        px = hist_xy.sum(axis=1) / n
        py = hist_xy.sum(axis=0) / n
        pxy = hist_xy / n
        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if pxy[i, j] > 0 and px[i] > 0 and py[j] > 0:
                    mi += pxy[i, j] * np.log(pxy[i, j] / (px[i] * py[j]))
        hx = -np.sum(px[px > 0] * np.log(px[px > 0]))
        hy = -np.sum(py[py > 0] * np.log(py[py > 0]))
        denom = max(hx, hy, _EPS)
        return float(mi / denom)
    except Exception:
        return np.nan


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-015): DFA scaling exponent (long-memory measure) ---

def idc_ext_001_dfa_alpha_63d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent alpha over 63-day window (long-memory depth)."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_002_dfa_alpha_126d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent alpha over 126-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_003_dfa_alpha_252d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent alpha over 252-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_YEAR
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_004_dfa_alpha_deviation_from_half(close: pd.Series) -> pd.Series:
    """DFA alpha - 0.5: negative = anti-persistent (fast decay), positive = persistent."""
    return idc_ext_001_dfa_alpha_63d(close) - 0.5


def idc_ext_005_dfa_alpha_abs_returns_63d(close: pd.Series) -> pd.Series:
    """DFA alpha of absolute returns (volatility long-memory) over 63-day window."""
    r = _returns(close).abs().values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_006_dfa_alpha_abs_returns_126d(close: pd.Series) -> pd.Series:
    """DFA alpha of absolute returns over 126-day window."""
    r = _returns(close).abs().values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_007_dfa_alpha_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day DFA alpha in trailing 252-day distribution."""
    alpha = idc_ext_001_dfa_alpha_63d(close)
    return alpha.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_ext_008_dfa_alpha_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day DFA alpha vs 252-day distribution."""
    alpha = idc_ext_001_dfa_alpha_63d(close)
    m = _rolling_mean(alpha, _TD_YEAR)
    s = _rolling_std(alpha, _TD_YEAR)
    return _safe_div(alpha - m, s)


def idc_ext_009_dfa_alpha_vs_hurst_divergence(close: pd.Series) -> pd.Series:
    """Difference: DFA alpha minus Hurst exponent (both 63-day). Measures estimator disagreement."""
    dfa = idc_ext_001_dfa_alpha_63d(close)
    hurst_vals = _returns(close).values
    n = len(hurst_vals)
    hurst_result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        hurst_result[i] = _hurst_rs(hurst_vals[max(0, i - w + 1):i + 1])
    h = pd.Series(hurst_result, index=close.index)
    return dfa - h


def idc_ext_010_dfa_alpha_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day DFA alpha (velocity of long-memory change)."""
    return idc_ext_001_dfa_alpha_63d(close).diff(_TD_WEEK)


def idc_ext_011_dfa_alpha_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day DFA alpha."""
    return idc_ext_001_dfa_alpha_63d(close).diff(_TD_MON)


def idc_ext_012_dfa_vol_alpha_vs_returns_alpha(close: pd.Series) -> pd.Series:
    """Difference: DFA alpha of |returns| minus DFA alpha of returns (vol vs return memory)."""
    alpha_r = idc_ext_001_dfa_alpha_63d(close)
    alpha_ar = idc_ext_005_dfa_alpha_abs_returns_63d(close)
    return alpha_ar - alpha_r


def idc_ext_013_dfa_alpha_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day DFA alpha to 252-day DFA alpha (short vs long memory scaling)."""
    a63 = idc_ext_001_dfa_alpha_63d(close)
    a252 = idc_ext_003_dfa_alpha_252d(close)
    return _safe_div(a63, a252.clip(lower=_EPS))


def idc_ext_014_dfa_alpha_regime_flag_persistent(close: pd.Series) -> pd.Series:
    """Binary: DFA alpha > 0.5 (persistent / slow-decay regime)."""
    return (idc_ext_001_dfa_alpha_63d(close) > 0.5).astype(float)


def idc_ext_015_dfa_alpha_regime_flag_antipersistent(close: pd.Series) -> pd.Series:
    """Binary: DFA alpha < 0.5 (anti-persistent / fast-decay regime)."""
    return (idc_ext_001_dfa_alpha_63d(close) < 0.5).astype(float)


# --- Group B (016-030): Multi-scale entropy and deeper complexity measures ---

def idc_ext_016_sample_entropy_63d(close: pd.Series) -> pd.Series:
    """
    Sample entropy of log returns over 63-day window (m=2, r=0.2*std).
    Higher = more random / faster information decay.
    """
    def _sampen(x, m=2, r_frac=0.2):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < m + 3:
            return np.nan
        r = r_frac * (x.std() + _EPS)
        def _count_matches(template, data, lag):
            count = 0
            for j in range(len(data) - lag + 1):
                if np.max(np.abs(data[j:j + lag] - template)) <= r:
                    count += 1
            return count
        A = 0
        B = 0
        for i in range(n - m - 1):
            template_m = x[i:i + m]
            template_m1 = x[i:i + m + 1]
            for j in range(i + 1, n - m):
                if np.max(np.abs(x[j:j + m] - template_m)) <= r:
                    B += 1
                    if j < n - m and np.max(np.abs(x[j:j + m + 1] - template_m1)) <= r:
                        A += 1
        if B == 0:
            return np.nan
        return float(-np.log((A + _EPS) / (B + _EPS)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) >= 15:
            result[i] = _sampen(seg[-15:])
    return pd.Series(result, index=close.index)


def idc_ext_017_permutation_entropy_63d(close: pd.Series) -> pd.Series:
    """
    Permutation entropy of returns over 63-day window (order=3).
    Measures ordinal complexity of return sequence.
    """
    def _perm_ent(x, order=3):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < order + 2:
            return np.nan
        from itertools import permutations
        perms = list(permutations(range(order)))
        perm_counts = {p: 0 for p in perms}
        count = 0
        for i in range(n - order + 1):
            seg = x[i:i + order]
            rank = tuple(np.argsort(seg))
            if rank in perm_counts:
                perm_counts[rank] += 1
                count += 1
        if count == 0:
            return np.nan
        freqs = np.array(list(perm_counts.values()), dtype=float) / count
        freqs = freqs[freqs > 0]
        return float(-np.sum(freqs * np.log2(freqs + _EPS)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) >= 10:
            result[i] = _perm_ent(seg)
    return pd.Series(result, index=close.index)


def idc_ext_018_permutation_entropy_21d(close: pd.Series) -> pd.Series:
    """Permutation entropy of returns over 21-day window (order=3)."""
    def _perm_ent(x, order=3):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < order + 2:
            return np.nan
        from itertools import permutations
        perms = list(permutations(range(order)))
        perm_counts = {p: 0 for p in perms}
        count = 0
        for i in range(n - order + 1):
            seg = x[i:i + order]
            rank = tuple(np.argsort(seg))
            if rank in perm_counts:
                perm_counts[rank] += 1
                count += 1
        if count == 0:
            return np.nan
        freqs = np.array(list(perm_counts.values()), dtype=float) / count
        freqs = freqs[freqs > 0]
        return float(-np.sum(freqs * np.log2(freqs + _EPS)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_MON
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) >= 6:
            result[i] = _perm_ent(seg)
    return pd.Series(result, index=close.index)


def idc_ext_019_multi_scale_entropy_ratio_63d(close: pd.Series) -> pd.Series:
    """
    Multi-scale entropy: ratio of coarse-grained (scale=2) return entropy
    to original (scale=1) entropy over 63-day window. > 1 = multi-scale complexity.
    """
    def _ent_sign(x):
        x = x[~np.isnan(x)]
        if len(x) < 4:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) < 10:
            continue
        e1 = _ent_sign(seg)
        coarse = (seg[:-1:2] + seg[1::2]) / 2.0
        e2 = _ent_sign(coarse)
        if e1 is None or e2 is None or np.isnan(e1) or e1 < _EPS:
            result[i] = np.nan
        else:
            result[i] = e2 / e1
    return pd.Series(result, index=close.index)


def idc_ext_020_entropy_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day permutation entropy in trailing 252-day distribution."""
    pe = idc_ext_017_permutation_entropy_63d(close)
    return pe.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_ext_021_entropy_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day permutation entropy vs 252-day distribution."""
    pe = idc_ext_017_permutation_entropy_63d(close)
    m = _rolling_mean(pe, _TD_YEAR)
    s = _rolling_std(pe, _TD_YEAR)
    return _safe_div(pe - m, s)


def idc_ext_022_entropy_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day permutation entropy (velocity of complexity change)."""
    return idc_ext_017_permutation_entropy_63d(close).diff(_TD_WEEK)


def idc_ext_023_entropy_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day permutation entropy."""
    return idc_ext_017_permutation_entropy_63d(close).diff(_TD_MON)


def idc_ext_024_complexity_decay_composite(close: pd.Series) -> pd.Series:
    """Composite: z(DFA alpha deviation) + z(permutation entropy) over 252-day windows."""
    dfa_dev = idc_ext_004_dfa_alpha_deviation_from_half(close)
    dfa_z = _safe_div(dfa_dev - _rolling_mean(dfa_dev, _TD_YEAR),
                      _rolling_std(dfa_dev, _TD_YEAR).clip(lower=_EPS))
    pe = idc_ext_017_permutation_entropy_63d(close)
    pe_z = _safe_div(pe - _rolling_mean(pe, _TD_YEAR),
                     _rolling_std(pe, _TD_YEAR).clip(lower=_EPS))
    return (dfa_z.fillna(0.0) + pe_z.fillna(0.0)) / 2.0


def idc_ext_025_lz_complexity_126d(close: pd.Series) -> pd.Series:
    """Lempel-Ziv complexity of binary return sequence over 126-day window."""
    def _lz(seq):
        if len(seq) < 4:
            return np.nan
        n = len(seq)
        s = ''.join('1' if v >= 0 else '0' for v in seq)
        i, k, l = 0, 1, 1
        c, k_max = 1, 1
        while True:
            if s[i + k - 1] == s[l + k - 1]:
                k += 1
                if l + k > n:
                    c += 1
                    break
            else:
                if k > k_max:
                    k_max = k
                i += 1
                if i == l:
                    c += 1
                    l += k_max
                    if l + 1 > n:
                        break
                    i, k, k_max = 0, 1, 1
                else:
                    k = 1
        b = n / np.log2(n + 1 + _EPS)
        return float(c / b)
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        seg = seg[~np.isnan(seg)]
        if len(seg) >= 4:
            result[i] = _lz(seg)
    return pd.Series(result, index=close.index)


# --- Group C (026-045): Higher-lag AC structure and long-range correlation ---

def idc_ext_026_ac_lag15_returns_126d(close: pd.Series) -> pd.Series:
    """AC(15) of log returns over 126-day window (3-week lag persistence)."""
    return _rolling_autocorr(_returns(close), _TD_HALF, 15)


def idc_ext_027_ac_lag21_returns_252d(close: pd.Series) -> pd.Series:
    """AC(21) of log returns over 252-day window (monthly lag persistence)."""
    return _rolling_autocorr(_returns(close), _TD_YEAR, _TD_MON)


def idc_ext_028_ac_lag5_sq_returns_252d(close: pd.Series) -> pd.Series:
    """AC(5) of squared returns over 252-day window (weekly variance memory)."""
    return _rolling_autocorr(_returns(close) ** 2, _TD_YEAR, _TD_WEEK)


def idc_ext_029_ac_lag21_sq_returns_252d(close: pd.Series) -> pd.Series:
    """AC(21) of squared returns over 252-day window (monthly GARCH effect)."""
    return _rolling_autocorr(_returns(close) ** 2, _TD_YEAR, _TD_MON)


def idc_ext_030_ac_abs_sum_lags_1_to_21_252d(close: pd.Series) -> pd.Series:
    """Sum of |AC(k)| for k=1..21 over 252-day window (total memory content)."""
    r = _returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 22):
        total = total + _rolling_autocorr(r, _TD_YEAR, lag).abs().fillna(0.0)
    return total


def idc_ext_031_ac_decay_slope_lags_1_to_10_126d(close: pd.Series) -> pd.Series:
    """OLS slope of AC(k) for k=1..10 over 126-day window (breadth of memory decay)."""
    def _slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 20:
            return np.nan
        lags = list(range(1, 11))
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs)
        if valid.sum() < 3:
            return np.nan
        lags_v = np.array(lags, dtype=float)[valid]
        if lags_v.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags_v, acs[valid], 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _slope(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_032_halflife_ols_252d(close: pd.Series) -> pd.Series:
    """Memory half-life from OLS fit of log|AC(k)| vs k=1..10 over 252-day window."""
    def _hl(x):
        x = x[~np.isnan(x)]
        if len(x) < 25:
            return np.nan
        lags = [1, 2, 3, 5, 7, 10]
        acs = []
        for lag in lags:
            if len(x) <= lag + 2:
                acs.append(np.nan)
                continue
            x0, x1 = x[:-lag], x[lag:]
            if len(x0) < 3:
                acs.append(np.nan)
                continue
            std0, std1 = x0.std(), x1.std()
            if std0 < _EPS or std1 < _EPS:
                acs.append(np.nan)
                continue
            acs.append(float(np.corrcoef(x0, x1)[0, 1]))
        acs = np.array(acs)
        valid = np.isfinite(acs) & (np.abs(acs) > _EPS)
        if valid.sum() < 2:
            return np.nan
        lags_v = np.array(lags)[valid]
        log_ac = np.log(np.abs(acs[valid]) + _EPS)
        if lags_v.std() < _EPS:
            return np.nan
        slope = np.polyfit(lags_v, log_ac, 1)[0]
        if slope >= 0:
            return np.nan
        return float(np.log(2.0) / (-slope))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_YEAR
    for i in range(w - 1, n):
        result[i] = _hl(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_033_ac_lag1_returns_21d(close: pd.Series) -> pd.Series:
    """AC(1) of log returns over 21-day window (very short-run persistence)."""
    return _rolling_autocorr(_returns(close), _TD_MON, 1)


def idc_ext_034_ac_lag2_returns_21d(close: pd.Series) -> pd.Series:
    """AC(2) of log returns over 21-day window."""
    return _rolling_autocorr(_returns(close), _TD_MON, 2)


def idc_ext_035_ac_ratio_63d_vs_252d_lag1(close: pd.Series) -> pd.Series:
    """Ratio of AC(1) over 63-day vs AC(1) over 252-day (short vs long persistence ratio)."""
    r = _returns(close)
    ac_63 = _rolling_autocorr(r, _TD_QTR, 1)
    ac_252 = _rolling_autocorr(r, _TD_YEAR, 1)
    return _safe_div(ac_63.abs(), ac_252.abs().clip(lower=_EPS))


def idc_ext_036_ac_decay_rate_126d(close: pd.Series) -> pd.Series:
    """Decay rate from AC(1)/AC(2) over 126-day window (medium-horizon decay)."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1)
    ac2 = _rolling_autocorr(r, _TD_HALF, 2)
    return _decay_rate_from_two_lags(ac1, ac2)


def idc_ext_037_halflife_126d(close: pd.Series) -> pd.Series:
    """Half-life from AC(1)/AC(2) over 126-day window."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_HALF, 1)
    ac2 = _rolling_autocorr(r, _TD_HALF, 2)
    return _halflife_from_decay(_decay_rate_from_two_lags(ac1, ac2))


def idc_ext_038_halflife_ratio_63d_vs_126d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day half-life to 126-day half-life (consistency of decay scale)."""
    hl63 = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    hl126 = idc_ext_037_halflife_126d(close)
    return _safe_div(hl63, hl126.clip(lower=_EPS))


def idc_ext_039_ac_lag10_sq_returns_63d(close: pd.Series) -> pd.Series:
    """AC(10) of squared returns over 63-day window (volatility clustering at 2-week lag)."""
    return _rolling_autocorr(_returns(close) ** 2, _TD_QTR, 10)


def idc_ext_040_ac_lag21_abs_returns_252d(close: pd.Series) -> pd.Series:
    """AC(21) of absolute returns over 252-day window (monthly vol persistence)."""
    return _rolling_autocorr(_returns(close).abs(), _TD_YEAR, _TD_MON)


# --- Group D (041-055): Cross-series and volume-augmented memory measures ---

def idc_ext_041_mi_lag1_returns_21d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-1] over 21-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_MON
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy(seg[1:], seg[:-1])
    return pd.Series(result, index=close.index)


def idc_ext_042_mi_lag1_returns_252d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-1] over 252-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_YEAR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy(seg[1:], seg[:-1])
    return pd.Series(result, index=close.index)


def idc_ext_043_mi_lag21_returns_252d(close: pd.Series) -> pd.Series:
    """MI proxy between return[t] and return[t-21] over 252-day window."""
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_YEAR
    lag = _TD_MON
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy(seg[lag:], seg[:-lag])
    return pd.Series(result, index=close.index)


def idc_ext_044_mi_decay_halflife_63d(close: pd.Series) -> pd.Series:
    """
    Half-life from MI decay: using MI(lag=1) and MI(lag=5) to estimate decay rate,
    then half-life = -5*log(2)/log(MI5/MI1 + EPS).
    """
    r = _returns(close).values
    n = len(r)
    mi1 = np.full(n, np.nan)
    mi5 = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        mi1[i] = _mi_proxy(seg[1:], seg[:-1])
        mi5[i] = _mi_proxy(seg[5:], seg[:-5])
    s1 = pd.Series(mi1, index=close.index).clip(lower=_EPS)
    s5 = pd.Series(mi5, index=close.index).clip(lower=_EPS)
    ratio = _safe_div(s5, s1).clip(lower=_EPS, upper=1.0 - _EPS)
    return -5.0 * np.log(2.0) / np.log(ratio + _EPS)


def idc_ext_045_mi_lag2_sq_returns_63d(close: pd.Series) -> pd.Series:
    """MI proxy between squared return[t] and squared return[t-2] over 63-day window."""
    r = (_returns(close) ** 2).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        seg = r[max(0, i - w + 1):i + 1]
        result[i] = _mi_proxy(seg[2:], seg[:-2])
    return pd.Series(result, index=close.index)


def idc_ext_046_vwac_lag2_returns_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted AC(2) of returns over 63-day window."""
    def _vwac2(x, v):
        valid = np.isfinite(x) & np.isfinite(v)
        x, v = x[valid], v[valid]
        if len(x) < 6:
            return np.nan
        vn = v / (v.sum() + _EPS)
        x_mean = (x * vn).sum()
        y = x - x_mean
        if len(y) < 3:
            return np.nan
        num = (vn[2:] * y[:-2] * y[2:]).sum()
        denom = (vn * y ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(num / denom)
    r = _returns(close).values
    v = volume.values.astype(float)
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _vwac2(r[max(0, i - w + 1):i + 1], v[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_047_vwac_halflife_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted AC half-life from AC(1)/AC(2) over 126-day window."""
    def _vwac(x, v, lag):
        valid = np.isfinite(x) & np.isfinite(v)
        x, v = x[valid], v[valid]
        if len(x) < lag + 3:
            return np.nan
        vn = v / (v.sum() + _EPS)
        x_mean = (x * vn).sum()
        y = x - x_mean
        num = (vn[lag:] * y[:-lag] * y[lag:]).sum()
        denom = (vn * y ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(num / denom)
    r = _returns(close).values
    v = volume.values.astype(float)
    n = len(r)
    ac1 = np.full(n, np.nan)
    ac2 = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        seg_r = r[max(0, i - w + 1):i + 1]
        seg_v = v[max(0, i - w + 1):i + 1]
        ac1[i] = _vwac(seg_r, seg_v, 1)
        ac2[i] = _vwac(seg_r, seg_v, 2)
    s1 = pd.Series(ac1, index=close.index)
    s2 = pd.Series(ac2, index=close.index)
    return _halflife_from_decay(_decay_rate_from_two_lags(s1, s2))


def idc_ext_048_range_ac_lag3_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC(3) of normalized range (high-low)/close over 63-day window."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_autocorr(rng, _TD_QTR, 3)


def idc_ext_049_range_ac_lag5_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """AC(5) of normalized range over 126-day window (weekly range persistence)."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_autocorr(rng, _TD_HALF, 5)


def idc_ext_050_range_dfa_alpha_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """DFA alpha of normalized range series over 63-day window."""
    rng = _safe_div(high - low, close.clip(lower=_EPS))
    r = rng.values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_051_volume_dfa_alpha_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DFA alpha of log-volume series over 63-day window (volume long-memory)."""
    lv = np.log(volume.clip(lower=1.0)).values
    n = len(lv)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(lv[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_052_volume_dfa_alpha_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DFA alpha of log-volume over 126-day window."""
    lv = np.log(volume.clip(lower=1.0)).values
    n = len(lv)
    result = np.full(n, np.nan)
    w = _TD_HALF
    for i in range(w - 1, n):
        result[i] = _dfa_alpha(lv[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def idc_ext_053_price_vol_dfa_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DFA alpha of returns minus DFA alpha of log-volume (price vs volume memory gap)."""
    return idc_ext_001_dfa_alpha_63d(close) - idc_ext_051_volume_dfa_alpha_63d(close, volume)


def idc_ext_054_overnight_gap_ac_lag2_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """AC(2) of overnight gap returns over 63-day window."""
    gap = np.log(open_ / close.shift(1))
    return _rolling_autocorr(gap, _TD_QTR, 2)


def idc_ext_055_overnight_gap_halflife_126d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Half-life of overnight gap from AC(1)/AC(2) over 126-day window."""
    gap = np.log(open_ / close.shift(1))
    ac1 = _rolling_autocorr(gap, _TD_HALF, 1)
    ac2 = _rolling_autocorr(gap, _TD_HALF, 2)
    return _halflife_from_decay(_decay_rate_from_two_lags(ac1, ac2))


# --- Group E (056-075): Deeper decay variants and composite regime scores ---

def idc_ext_056_halflife_expanding_max(close: pd.Series) -> pd.Series:
    """All-time expanding maximum of 63-day half-life (historical memory peak)."""
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    return hl.expanding(min_periods=_TD_QTR).max()


def idc_ext_057_halflife_expanding_min(close: pd.Series) -> pd.Series:
    """All-time expanding minimum of 63-day half-life (shortest memory ever seen)."""
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    return hl.expanding(min_periods=_TD_QTR).min()


def idc_ext_058_halflife_current_vs_expanding_max(close: pd.Series) -> pd.Series:
    """Current 63-day half-life as fraction of all-time maximum (how low is memory now)."""
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    exp_max = hl.expanding(min_periods=_TD_QTR).max()
    return _safe_div(hl, exp_max.clip(lower=_EPS))


def idc_ext_059_decay_rate_expanding_max(close: pd.Series) -> pd.Series:
    """All-time expanding maximum of 63-day decay rate."""
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    return rate.expanding(min_periods=_TD_QTR).max()


def idc_ext_060_decay_rate_current_vs_expanding_max(close: pd.Series) -> pd.Series:
    """Current decay rate as fraction of all-time maximum decay rate."""
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    exp_max = rate.expanding(min_periods=_TD_QTR).max()
    return _safe_div(rate, exp_max.clip(lower=_EPS))


def idc_ext_061_hurst_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day Hurst exponent (lowest persistence ever)."""
    r = _returns(close).values
    n = len(r)
    hurst_result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        hurst_result[i] = _hurst_rs(r[max(0, i - w + 1):i + 1])
    h = pd.Series(hurst_result, index=close.index)
    return h.expanding(min_periods=_TD_QTR).min()


def idc_ext_062_hurst_current_vs_expanding_min(close: pd.Series) -> pd.Series:
    """Current 63-day Hurst exponent minus its expanding minimum."""
    r = _returns(close).values
    n = len(r)
    hurst_result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        hurst_result[i] = _hurst_rs(r[max(0, i - w + 1):i + 1])
    h = pd.Series(hurst_result, index=close.index)
    return h - h.expanding(min_periods=_TD_QTR).min()


def idc_ext_063_garch_alpha_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding maximum of 63-day GARCH alpha (peak variance persistence)."""
    a = _rolling_autocorr(_returns(close) ** 2, _TD_QTR, 1)
    return a.expanding(min_periods=_TD_QTR).max()


def idc_ext_064_garch_alpha_current_vs_expanding_max(close: pd.Series) -> pd.Series:
    """Current GARCH alpha as fraction of its expanding maximum."""
    a = _rolling_autocorr(_returns(close) ** 2, _TD_QTR, 1)
    exp_max = a.expanding(min_periods=_TD_QTR).max()
    return _safe_div(a, exp_max.clip(lower=_EPS))


def idc_ext_065_ewm_halflife_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day EWM half-life (from AC1) in trailing 252-day distribution."""
    ac1 = _rolling_autocorr(_returns(close), _TD_QTR, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    hl = np.log(2.0) / (-np.log(1.0 - alpha))
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_ext_066_halflife_min_21d(close: pd.Series) -> pd.Series:
    """Minimum 63-day half-life over trailing 21-day window (worst recent memory)."""
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    return _rolling_min(hl, _TD_MON)


def idc_ext_067_halflife_min_63d(close: pd.Series) -> pd.Series:
    """Minimum 63-day half-life over trailing 63-day window."""
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    return _rolling_min(hl, _TD_QTR)


def idc_ext_068_decay_rate_ewm_smooth_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed 63-day AC decay rate (removes noise from decay rate estimate)."""
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    return _ewm_mean(rate, _TD_MON)


def idc_ext_069_decay_rate_ewm_smooth_63d(close: pd.Series) -> pd.Series:
    """EWM(63)-smoothed 63-day AC decay rate (long-run decay signal)."""
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    return _ewm_mean(rate, _TD_QTR)


def idc_ext_070_dfa_alpha_ewm_smooth_21d(close: pd.Series) -> pd.Series:
    """EWM(21)-smoothed 63-day DFA alpha (stable long-memory signal)."""
    return _ewm_mean(idc_ext_001_dfa_alpha_63d(close), _TD_MON)


def idc_ext_071_decay_composite_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of composite decay score in trailing 252-day distribution."""
    comp = idc_ext_024_complexity_decay_composite(close)
    return comp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def idc_ext_072_memory_regime_fast_slow_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day half-life to 252-day half-life (fast vs slow regime memory ratio)."""
    hl21 = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_MON, 1),
            _rolling_autocorr(_returns(close), _TD_MON, 2)
        )
    )
    hl252 = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_YEAR, 1),
            _rolling_autocorr(_returns(close), _TD_YEAR, 2)
        )
    )
    return _safe_div(hl21, hl252.clip(lower=_EPS))


def idc_ext_073_ac_decay_entropy_dfa_composite(close: pd.Series) -> pd.Series:
    """
    Three-way composite: z(decay rate) + z(permutation entropy) + z(-DFA alpha deviation).
    Higher = faster information decay across multiple methodologies.
    """
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    rate_z = _safe_div(rate - _rolling_mean(rate, _TD_YEAR),
                       _rolling_std(rate, _TD_YEAR).clip(lower=_EPS))
    pe = idc_ext_017_permutation_entropy_63d(close)
    pe_z = _safe_div(pe - _rolling_mean(pe, _TD_YEAR),
                     _rolling_std(pe, _TD_YEAR).clip(lower=_EPS))
    dfa_neg = -idc_ext_004_dfa_alpha_deviation_from_half(close)
    dfa_z = _safe_div(dfa_neg - _rolling_mean(dfa_neg, _TD_YEAR),
                      _rolling_std(dfa_neg, _TD_YEAR).clip(lower=_EPS))
    return (rate_z.fillna(0.0) + pe_z.fillna(0.0) + dfa_z.fillna(0.0)) / 3.0


def idc_ext_074_halflife_consec_below_21d(close: pd.Series) -> pd.Series:
    """
    Count of consecutive days the 63-day half-life has been below its 21-day mean
    (persistent short-memory regime duration).
    """
    hl = _halflife_from_decay(
        _decay_rate_from_two_lags(
            _rolling_autocorr(_returns(close), _TD_QTR, 1),
            _rolling_autocorr(_returns(close), _TD_QTR, 2)
        )
    )
    mean21 = _rolling_mean(hl, _TD_MON)
    below = hl < mean21
    c = below.astype(int)
    group = (~below).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def idc_ext_075_decay_rate_vs_vol_interaction(close: pd.Series) -> pd.Series:
    """
    Product of AC decay rate and 21-day realized volatility (both high = rapid chaotic decay).
    """
    rate = _decay_rate_from_two_lags(
        _rolling_autocorr(_returns(close), _TD_QTR, 1),
        _rolling_autocorr(_returns(close), _TD_QTR, 2)
    )
    vol21 = _returns(close).rolling(_TD_MON, min_periods=5).std()
    return rate * vol21


# ── Registry ──────────────────────────────────────────────────────────────────

INFORMATION_DECAY_EXTENDED_REGISTRY_001_075 = {
    "idc_ext_001_dfa_alpha_63d": {"inputs": ["close"], "func": idc_ext_001_dfa_alpha_63d},
    "idc_ext_002_dfa_alpha_126d": {"inputs": ["close"], "func": idc_ext_002_dfa_alpha_126d},
    "idc_ext_003_dfa_alpha_252d": {"inputs": ["close"], "func": idc_ext_003_dfa_alpha_252d},
    "idc_ext_004_dfa_alpha_deviation_from_half": {"inputs": ["close"], "func": idc_ext_004_dfa_alpha_deviation_from_half},
    "idc_ext_005_dfa_alpha_abs_returns_63d": {"inputs": ["close"], "func": idc_ext_005_dfa_alpha_abs_returns_63d},
    "idc_ext_006_dfa_alpha_abs_returns_126d": {"inputs": ["close"], "func": idc_ext_006_dfa_alpha_abs_returns_126d},
    "idc_ext_007_dfa_alpha_pct_rank_252d": {"inputs": ["close"], "func": idc_ext_007_dfa_alpha_pct_rank_252d},
    "idc_ext_008_dfa_alpha_zscore_252d": {"inputs": ["close"], "func": idc_ext_008_dfa_alpha_zscore_252d},
    "idc_ext_009_dfa_alpha_vs_hurst_divergence": {"inputs": ["close"], "func": idc_ext_009_dfa_alpha_vs_hurst_divergence},
    "idc_ext_010_dfa_alpha_5d_diff": {"inputs": ["close"], "func": idc_ext_010_dfa_alpha_5d_diff},
    "idc_ext_011_dfa_alpha_21d_diff": {"inputs": ["close"], "func": idc_ext_011_dfa_alpha_21d_diff},
    "idc_ext_012_dfa_vol_alpha_vs_returns_alpha": {"inputs": ["close"], "func": idc_ext_012_dfa_vol_alpha_vs_returns_alpha},
    "idc_ext_013_dfa_alpha_ratio_63d_to_252d": {"inputs": ["close"], "func": idc_ext_013_dfa_alpha_ratio_63d_to_252d},
    "idc_ext_014_dfa_alpha_regime_flag_persistent": {"inputs": ["close"], "func": idc_ext_014_dfa_alpha_regime_flag_persistent},
    "idc_ext_015_dfa_alpha_regime_flag_antipersistent": {"inputs": ["close"], "func": idc_ext_015_dfa_alpha_regime_flag_antipersistent},
    "idc_ext_016_sample_entropy_63d": {"inputs": ["close"], "func": idc_ext_016_sample_entropy_63d},
    "idc_ext_017_permutation_entropy_63d": {"inputs": ["close"], "func": idc_ext_017_permutation_entropy_63d},
    "idc_ext_018_permutation_entropy_21d": {"inputs": ["close"], "func": idc_ext_018_permutation_entropy_21d},
    "idc_ext_019_multi_scale_entropy_ratio_63d": {"inputs": ["close"], "func": idc_ext_019_multi_scale_entropy_ratio_63d},
    "idc_ext_020_entropy_pct_rank_252d": {"inputs": ["close"], "func": idc_ext_020_entropy_pct_rank_252d},
    "idc_ext_021_entropy_zscore_252d": {"inputs": ["close"], "func": idc_ext_021_entropy_zscore_252d},
    "idc_ext_022_entropy_5d_diff": {"inputs": ["close"], "func": idc_ext_022_entropy_5d_diff},
    "idc_ext_023_entropy_21d_diff": {"inputs": ["close"], "func": idc_ext_023_entropy_21d_diff},
    "idc_ext_024_complexity_decay_composite": {"inputs": ["close"], "func": idc_ext_024_complexity_decay_composite},
    "idc_ext_025_lz_complexity_126d": {"inputs": ["close"], "func": idc_ext_025_lz_complexity_126d},
    "idc_ext_026_ac_lag15_returns_126d": {"inputs": ["close"], "func": idc_ext_026_ac_lag15_returns_126d},
    "idc_ext_027_ac_lag21_returns_252d": {"inputs": ["close"], "func": idc_ext_027_ac_lag21_returns_252d},
    "idc_ext_028_ac_lag5_sq_returns_252d": {"inputs": ["close"], "func": idc_ext_028_ac_lag5_sq_returns_252d},
    "idc_ext_029_ac_lag21_sq_returns_252d": {"inputs": ["close"], "func": idc_ext_029_ac_lag21_sq_returns_252d},
    "idc_ext_030_ac_abs_sum_lags_1_to_21_252d": {"inputs": ["close"], "func": idc_ext_030_ac_abs_sum_lags_1_to_21_252d},
    "idc_ext_031_ac_decay_slope_lags_1_to_10_126d": {"inputs": ["close"], "func": idc_ext_031_ac_decay_slope_lags_1_to_10_126d},
    "idc_ext_032_halflife_ols_252d": {"inputs": ["close"], "func": idc_ext_032_halflife_ols_252d},
    "idc_ext_033_ac_lag1_returns_21d": {"inputs": ["close"], "func": idc_ext_033_ac_lag1_returns_21d},
    "idc_ext_034_ac_lag2_returns_21d": {"inputs": ["close"], "func": idc_ext_034_ac_lag2_returns_21d},
    "idc_ext_035_ac_ratio_63d_vs_252d_lag1": {"inputs": ["close"], "func": idc_ext_035_ac_ratio_63d_vs_252d_lag1},
    "idc_ext_036_ac_decay_rate_126d": {"inputs": ["close"], "func": idc_ext_036_ac_decay_rate_126d},
    "idc_ext_037_halflife_126d": {"inputs": ["close"], "func": idc_ext_037_halflife_126d},
    "idc_ext_038_halflife_ratio_63d_vs_126d": {"inputs": ["close"], "func": idc_ext_038_halflife_ratio_63d_vs_126d},
    "idc_ext_039_ac_lag10_sq_returns_63d": {"inputs": ["close"], "func": idc_ext_039_ac_lag10_sq_returns_63d},
    "idc_ext_040_ac_lag21_abs_returns_252d": {"inputs": ["close"], "func": idc_ext_040_ac_lag21_abs_returns_252d},
    "idc_ext_041_mi_lag1_returns_21d": {"inputs": ["close"], "func": idc_ext_041_mi_lag1_returns_21d},
    "idc_ext_042_mi_lag1_returns_252d": {"inputs": ["close"], "func": idc_ext_042_mi_lag1_returns_252d},
    "idc_ext_043_mi_lag21_returns_252d": {"inputs": ["close"], "func": idc_ext_043_mi_lag21_returns_252d},
    "idc_ext_044_mi_decay_halflife_63d": {"inputs": ["close"], "func": idc_ext_044_mi_decay_halflife_63d},
    "idc_ext_045_mi_lag2_sq_returns_63d": {"inputs": ["close"], "func": idc_ext_045_mi_lag2_sq_returns_63d},
    "idc_ext_046_vwac_lag2_returns_63d": {"inputs": ["close", "volume"], "func": idc_ext_046_vwac_lag2_returns_63d},
    "idc_ext_047_vwac_halflife_126d": {"inputs": ["close", "volume"], "func": idc_ext_047_vwac_halflife_126d},
    "idc_ext_048_range_ac_lag3_63d": {"inputs": ["close", "high", "low"], "func": idc_ext_048_range_ac_lag3_63d},
    "idc_ext_049_range_ac_lag5_126d": {"inputs": ["close", "high", "low"], "func": idc_ext_049_range_ac_lag5_126d},
    "idc_ext_050_range_dfa_alpha_63d": {"inputs": ["close", "high", "low"], "func": idc_ext_050_range_dfa_alpha_63d},
    "idc_ext_051_volume_dfa_alpha_63d": {"inputs": ["close", "volume"], "func": idc_ext_051_volume_dfa_alpha_63d},
    "idc_ext_052_volume_dfa_alpha_126d": {"inputs": ["close", "volume"], "func": idc_ext_052_volume_dfa_alpha_126d},
    "idc_ext_053_price_vol_dfa_divergence": {"inputs": ["close", "volume"], "func": idc_ext_053_price_vol_dfa_divergence},
    "idc_ext_054_overnight_gap_ac_lag2_63d": {"inputs": ["close", "open"], "func": idc_ext_054_overnight_gap_ac_lag2_63d},
    "idc_ext_055_overnight_gap_halflife_126d": {"inputs": ["close", "open"], "func": idc_ext_055_overnight_gap_halflife_126d},
    "idc_ext_056_halflife_expanding_max": {"inputs": ["close"], "func": idc_ext_056_halflife_expanding_max},
    "idc_ext_057_halflife_expanding_min": {"inputs": ["close"], "func": idc_ext_057_halflife_expanding_min},
    "idc_ext_058_halflife_current_vs_expanding_max": {"inputs": ["close"], "func": idc_ext_058_halflife_current_vs_expanding_max},
    "idc_ext_059_decay_rate_expanding_max": {"inputs": ["close"], "func": idc_ext_059_decay_rate_expanding_max},
    "idc_ext_060_decay_rate_current_vs_expanding_max": {"inputs": ["close"], "func": idc_ext_060_decay_rate_current_vs_expanding_max},
    "idc_ext_061_hurst_expanding_min": {"inputs": ["close"], "func": idc_ext_061_hurst_expanding_min},
    "idc_ext_062_hurst_current_vs_expanding_min": {"inputs": ["close"], "func": idc_ext_062_hurst_current_vs_expanding_min},
    "idc_ext_063_garch_alpha_expanding_max": {"inputs": ["close"], "func": idc_ext_063_garch_alpha_expanding_max},
    "idc_ext_064_garch_alpha_current_vs_expanding_max": {"inputs": ["close"], "func": idc_ext_064_garch_alpha_current_vs_expanding_max},
    "idc_ext_065_ewm_halflife_pct_rank_252d": {"inputs": ["close"], "func": idc_ext_065_ewm_halflife_pct_rank_252d},
    "idc_ext_066_halflife_min_21d": {"inputs": ["close"], "func": idc_ext_066_halflife_min_21d},
    "idc_ext_067_halflife_min_63d": {"inputs": ["close"], "func": idc_ext_067_halflife_min_63d},
    "idc_ext_068_decay_rate_ewm_smooth_21d": {"inputs": ["close"], "func": idc_ext_068_decay_rate_ewm_smooth_21d},
    "idc_ext_069_decay_rate_ewm_smooth_63d": {"inputs": ["close"], "func": idc_ext_069_decay_rate_ewm_smooth_63d},
    "idc_ext_070_dfa_alpha_ewm_smooth_21d": {"inputs": ["close"], "func": idc_ext_070_dfa_alpha_ewm_smooth_21d},
    "idc_ext_071_decay_composite_pct_rank_252d": {"inputs": ["close"], "func": idc_ext_071_decay_composite_pct_rank_252d},
    "idc_ext_072_memory_regime_fast_slow_ratio": {"inputs": ["close"], "func": idc_ext_072_memory_regime_fast_slow_ratio},
    "idc_ext_073_ac_decay_entropy_dfa_composite": {"inputs": ["close"], "func": idc_ext_073_ac_decay_entropy_dfa_composite},
    "idc_ext_074_halflife_consec_below_21d": {"inputs": ["close"], "func": idc_ext_074_halflife_consec_below_21d},
    "idc_ext_075_decay_rate_vs_vol_interaction": {"inputs": ["close"], "func": idc_ext_075_decay_rate_vs_vol_interaction},
}
