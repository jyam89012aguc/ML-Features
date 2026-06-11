"""
105_fractal_structure — Base Features 076-150
Domain: fractal / self-similarity structure of the price decline — multifractal
        spectrum width, lacunarity, Petrosian FD, sample/approximate entropy of the
        price path, autocorrelation decay, variance scaling, wavelet-based roughness
        proxies, rolling Lyapunov-like divergence, and additional multi-scale Hurst
        cross-comparison features.  Texture of the decline ONLY — not depth or speed.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
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


# ─── Scalar fractal helpers ────────────────────────────────────────────────────

def _multifractal_width(x: np.ndarray) -> float:
    """Approximate multifractal spectrum width via generalised Hurst.
    H(q) estimated at q=-2,0,2; width = H(-2) - H(2).  Drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    results = {}
    for q in [-2, 2]:
        # log-price increments raised to |q| power
        lr = np.abs(np.diff(x))
        if len(lr) < 8:
            return np.nan
        # two time scales: n//4 and n//2
        scales = [max(4, n // 4), max(8, n // 2)]
        hq_list = []
        scale_list = []
        for s in scales:
            if s >= len(lr):
                continue
            n_seg = len(lr) // s
            if n_seg < 1:
                continue
            moments = []
            for k in range(n_seg):
                seg = lr[k * s: (k + 1) * s]
                if len(seg) == 0:
                    continue
                val = np.mean(np.power(np.maximum(seg, _EPS), q))
                moments.append(val)
            if moments:
                hq_list.append(np.mean(moments))
                scale_list.append(s)
        if len(hq_list) < 2 or scale_list[-1] == scale_list[0]:
            return np.nan
        log_s = np.log(scale_list)
        log_hq = np.log(np.maximum(hq_list, _EPS))
        slope = np.polyfit(log_s, log_hq, 1)[0]
        results[q] = slope / q if q != 0 else 0.5
    if -2 not in results or 2 not in results:
        return np.nan
    return float(results[-2] - results[2])


def _petrosian_fd(x: np.ndarray) -> float:
    """Petrosian fractal dimension; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    delta = np.diff(x)
    sign_changes = np.sum(np.diff(np.sign(delta)) != 0)
    if n < 2:
        return np.nan
    denom = np.log10(n) + np.log10(n / (n + 0.4 * sign_changes + _EPS))
    if abs(denom) < _EPS:
        return np.nan
    return float(np.log10(n) / denom)


def _sample_entropy(x: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Sample Entropy (SampEn).  Drops NaNs.  r = r_frac * std(x)."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * m + 2:
        return np.nan
    r = r_frac * np.std(x, ddof=1)
    if r < _EPS:
        return np.nan

    def _template_count(m_len):
        count = 0
        for i in range(n - m_len):
            for j in range(i + 1, n - m_len):
                if np.max(np.abs(x[i:i + m_len] - x[j:j + m_len])) <= r:
                    count += 1
        return count

    A = _template_count(m + 1)
    B = _template_count(m)
    if B == 0:
        return np.nan
    return float(-np.log((A + _EPS) / (B + _EPS)))


def _lacunarity(x: np.ndarray, box_size: int = 4) -> float:
    """Lacunarity of the binary exceedance series (x > median(x)); drops NaNs."""
    x = x[~np.isnan(x)]
    if len(x) < box_size * 2:
        return np.nan
    binary = (x > np.median(x)).astype(float)
    n = len(binary)
    masses = []
    for i in range(0, n - box_size + 1):
        masses.append(binary[i: i + box_size].sum())
    masses = np.array(masses)
    if masses.mean() < _EPS:
        return np.nan
    return float(np.var(masses) / (masses.mean() ** 2 + _EPS))


def _autocorr_lag1(x: np.ndarray) -> float:
    """Lag-1 autocorrelation of x; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    xm = x - x.mean()
    denom = np.sum(xm ** 2)
    if denom < _EPS:
        return np.nan
    return float(np.dot(xm[:-1], xm[1:]) / denom)


def _variance_ratio(x: np.ndarray, q: int = 5) -> float:
    """Variance ratio test statistic VR(q) = Var(q-day) / (q * Var(1-day))."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < q + 4:
        return np.nan
    var1 = np.var(x, ddof=1)
    if var1 < _EPS:
        return np.nan
    agg = np.array([x[i:i + q].sum() for i in range(n - q + 1)])
    varq = np.var(agg, ddof=1)
    return float(varq / (q * var1 + _EPS))


# ─── Rolling wrappers ─────────────────────────────────────────────────────────

def _rolling_multifractal(close: pd.Series, w: int) -> pd.Series:
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _multifractal_width(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_petrosian(close: pd.Series, w: int) -> pd.Series:
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _petrosian_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_sampen(close: pd.Series, w: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _sample_entropy(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_lacunarity(close: pd.Series, w: int) -> pd.Series:
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _lacunarity(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_autocorr1(close: pd.Series, w: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _autocorr_lag1(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_vr(close: pd.Series, w: int, q: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), q), raw=True
    )


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Multifractal spectrum width ---

def fct_076_multifractal_width_63d(close: pd.Series) -> pd.Series:
    """Multifractal spectrum width (H(-2)-H(2)) over trailing 63-day window."""
    return _rolling_multifractal(close, _TD_QTR)


def fct_077_multifractal_width_126d(close: pd.Series) -> pd.Series:
    """Multifractal spectrum width over trailing 126 days."""
    return _rolling_multifractal(close, _TD_HALF)


def fct_078_multifractal_width_252d(close: pd.Series) -> pd.Series:
    """Multifractal spectrum width over trailing 252 days."""
    return _rolling_multifractal(close, _TD_YEAR)


def fct_079_multifractal_width_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d multifractal width within trailing 252-day distribution."""
    mf = _rolling_multifractal(close, _TD_QTR)
    return mf.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_080_multifractal_width_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d multifractal width within its 252-day rolling distribution."""
    mf = _rolling_multifractal(close, _TD_QTR)
    m = _rolling_mean(mf, _TD_YEAR)
    s = _rolling_std(mf, _TD_YEAR)
    return _safe_div(mf - m, s)


def fct_081_multifractal_width_63d_126d_spread(close: pd.Series) -> pd.Series:
    """Spread: 63d multifractal width minus 126d multifractal width."""
    return _rolling_multifractal(close, _TD_QTR) - _rolling_multifractal(close, _TD_HALF)


def fct_082_multifractal_width_63d_above02_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d multifractal width > 0.2 (strongly multifractal path)."""
    return (_rolling_multifractal(close, _TD_QTR) > 0.2).astype(float)


def fct_083_multifractal_width_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d multifractal width over trailing 252 days."""
    mf = _rolling_multifractal(close, _TD_QTR)
    return _rolling_min(mf, _TD_YEAR)


def fct_084_multifractal_width_63d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d multifractal width over trailing 252 days."""
    mf = _rolling_multifractal(close, _TD_QTR)
    return _rolling_max(mf, _TD_YEAR)


def fct_085_multifractal_width_63d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d multifractal width across all history."""
    mf = _rolling_multifractal(close, _TD_QTR)
    return mf.expanding(min_periods=_TD_HALF).rank(pct=True)


# --- Group I (086-095): Petrosian fractal dimension ---

def fct_086_petrosian_fd_21d(close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of log-price over trailing 21-day window."""
    return _rolling_petrosian(close, _TD_MON)


def fct_087_petrosian_fd_63d(close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of log-price over trailing 63-day window."""
    return _rolling_petrosian(close, _TD_QTR)


def fct_088_petrosian_fd_126d(close: pd.Series) -> pd.Series:
    """Petrosian fractal dimension of log-price over trailing 126-day window."""
    return _rolling_petrosian(close, _TD_HALF)


def fct_089_petrosian_fd_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d Petrosian FD within trailing 252-day distribution."""
    p = _rolling_petrosian(close, _TD_QTR)
    return p.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_090_petrosian_fd_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d Petrosian FD within its 252-day rolling distribution."""
    p = _rolling_petrosian(close, _TD_QTR)
    m = _rolling_mean(p, _TD_YEAR)
    s = _rolling_std(p, _TD_YEAR)
    return _safe_div(p - m, s)


def fct_091_petrosian_higuchi_spread_63d(close: pd.Series) -> pd.Series:
    """Spread: Petrosian FD minus Higuchi FD over 63d (method divergence)."""
    lp = np.log(close.clip(lower=_EPS))
    petro = _rolling_petrosian(close, _TD_QTR)
    hig = lp.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _higuchi_fd_local(np.asarray(x, dtype=float)), raw=True
    )
    return petro - hig


def _higuchi_fd_local(x: np.ndarray, k_max: int = 4) -> float:
    """Higuchi FD (local copy for use inside apply)."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    lk, ks = [], []
    for k in range(1, min(k_max + 1, n // 2)):
        Lm = []
        for m in range(1, k + 1):
            idx = np.arange(m - 1, n, k)
            if len(idx) < 2:
                continue
            diff_sum = np.sum(np.abs(np.diff(x[idx])))
            norm = (n - 1) / (((len(idx) - 1) * k) * k + _EPS)
            Lm.append(diff_sum * norm)
        if Lm:
            lk.append(np.mean(Lm))
            ks.append(k)
    if len(ks) < 2:
        return np.nan
    return float(-np.polyfit(np.log(ks), np.log(np.maximum(lk, _EPS)), 1)[0])


def fct_092_petrosian_fd_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d Petrosian FD minus 63d Petrosian FD."""
    return _rolling_petrosian(close, _TD_MON) - _rolling_petrosian(close, _TD_QTR)


def fct_093_petrosian_fd_63d_above15_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d Petrosian FD > 1.5."""
    return (_rolling_petrosian(close, _TD_QTR) > 1.5).astype(float)


def fct_094_petrosian_fd_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d Petrosian FD over trailing 252 days."""
    p = _rolling_petrosian(close, _TD_QTR)
    return _rolling_min(p, _TD_YEAR)


def fct_095_petrosian_fd_63d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d Petrosian FD over trailing 252 days."""
    p = _rolling_petrosian(close, _TD_QTR)
    return _rolling_max(p, _TD_YEAR)


# --- Group J (096-105): Sample entropy of log-returns ---

def fct_096_sampen_63d(close: pd.Series) -> pd.Series:
    """Sample entropy of log-returns over trailing 63-day window."""
    return _rolling_sampen(close, _TD_QTR)


def fct_097_sampen_126d(close: pd.Series) -> pd.Series:
    """Sample entropy of log-returns over trailing 126-day window."""
    return _rolling_sampen(close, _TD_HALF)


def fct_098_sampen_21d(close: pd.Series) -> pd.Series:
    """Sample entropy of log-returns over trailing 21-day window."""
    return _rolling_sampen(close, _TD_MON)


def fct_099_sampen_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d SampEn within trailing 252-day distribution."""
    se = _rolling_sampen(close, _TD_QTR)
    return se.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_100_sampen_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d SampEn within its 252-day rolling distribution."""
    se = _rolling_sampen(close, _TD_QTR)
    m = _rolling_mean(se, _TD_YEAR)
    s = _rolling_std(se, _TD_YEAR)
    return _safe_div(se - m, s)


def fct_101_sampen_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d SampEn minus 63d SampEn (short-vs-medium entropy change)."""
    return _rolling_sampen(close, _TD_MON) - _rolling_sampen(close, _TD_QTR)


def fct_102_sampen_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d SampEn over trailing 252 days (most regular stretch)."""
    se = _rolling_sampen(close, _TD_QTR)
    return _rolling_min(se, _TD_YEAR)


def fct_103_sampen_63d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d SampEn over trailing 252 days (most irregular stretch)."""
    se = _rolling_sampen(close, _TD_QTR)
    return _rolling_max(se, _TD_YEAR)


def fct_104_sampen_63d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d SampEn across all history."""
    se = _rolling_sampen(close, _TD_QTR)
    return se.expanding(min_periods=_TD_HALF).rank(pct=True)


def fct_105_sampen_126d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 126d SampEn across all history."""
    se = _rolling_sampen(close, _TD_HALF)
    return se.expanding(min_periods=_TD_HALF).rank(pct=True)


# --- Group K (106-115): Lacunarity of price path ---

def fct_106_lacunarity_63d(close: pd.Series) -> pd.Series:
    """Lacunarity of log-price binary exceedance over trailing 63-day window."""
    return _rolling_lacunarity(close, _TD_QTR)


def fct_107_lacunarity_126d(close: pd.Series) -> pd.Series:
    """Lacunarity of log-price binary exceedance over trailing 126-day window."""
    return _rolling_lacunarity(close, _TD_HALF)


def fct_108_lacunarity_21d(close: pd.Series) -> pd.Series:
    """Lacunarity of log-price binary exceedance over trailing 21-day window."""
    return _rolling_lacunarity(close, _TD_MON)


def fct_109_lacunarity_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d lacunarity within trailing 252-day distribution."""
    la = _rolling_lacunarity(close, _TD_QTR)
    return la.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_110_lacunarity_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d lacunarity within its 252-day rolling distribution."""
    la = _rolling_lacunarity(close, _TD_QTR)
    m = _rolling_mean(la, _TD_YEAR)
    s = _rolling_std(la, _TD_YEAR)
    return _safe_div(la - m, s)


def fct_111_lacunarity_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d lacunarity minus 63d lacunarity (short-vs-medium gap structure)."""
    return _rolling_lacunarity(close, _TD_MON) - _rolling_lacunarity(close, _TD_QTR)


def fct_112_lacunarity_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d lacunarity over trailing 252 days."""
    la = _rolling_lacunarity(close, _TD_QTR)
    return _rolling_min(la, _TD_YEAR)


def fct_113_lacunarity_63d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d lacunarity over trailing 252 days."""
    la = _rolling_lacunarity(close, _TD_QTR)
    return _rolling_max(la, _TD_YEAR)


def fct_114_lacunarity_63d_above05_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d lacunarity > 0.5 (highly clustered / gappy price structure)."""
    return (_rolling_lacunarity(close, _TD_QTR) > 0.5).astype(float)


def fct_115_lacunarity_63d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d lacunarity across all history."""
    la = _rolling_lacunarity(close, _TD_QTR)
    return la.expanding(min_periods=_TD_HALF).rank(pct=True)


# --- Group L (116-125): Autocorrelation of log-returns (mean-reversion texture) ---

def fct_116_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-returns over trailing 21-day window."""
    return _rolling_autocorr1(close, _TD_MON)


def fct_117_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-returns over trailing 63-day window."""
    return _rolling_autocorr1(close, _TD_QTR)


def fct_118_autocorr_lag1_126d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-returns over trailing 126-day window."""
    return _rolling_autocorr1(close, _TD_HALF)


def fct_119_autocorr_lag1_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d lag-1 autocorr within trailing 252-day distribution."""
    ac = _rolling_autocorr1(close, _TD_QTR)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_120_autocorr_lag1_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d lag-1 autocorr within its 252-day rolling distribution."""
    ac = _rolling_autocorr1(close, _TD_QTR)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def fct_121_autocorr_lag1_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d lag-1 autocorr minus 63d lag-1 autocorr."""
    return _rolling_autocorr1(close, _TD_MON) - _rolling_autocorr1(close, _TD_QTR)


def fct_122_autocorr_lag1_63d_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d lag-1 autocorr < 0 (mean-reverting return texture)."""
    return (_rolling_autocorr1(close, _TD_QTR) < 0.0).astype(float)


def fct_123_autocorr_lag1_63d_depth_below_neg01(close: pd.Series) -> pd.Series:
    """Depth of 63d lag-1 autocorr below -0.1 (stronger mean-reversion texture)."""
    return (-0.1 - _rolling_autocorr1(close, _TD_QTR)).clip(lower=0.0)


def fct_124_autocorr_lag1_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d lag-1 autocorr over trailing 252 days."""
    ac = _rolling_autocorr1(close, _TD_QTR)
    return _rolling_min(ac, _TD_YEAR)


def fct_125_autocorr_lag1_126d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 126d lag-1 autocorr across all history."""
    ac = _rolling_autocorr1(close, _TD_HALF)
    return ac.expanding(min_periods=_TD_HALF).rank(pct=True)


# --- Group M (126-135): Variance-ratio test statistic (scaling behaviour) ---

def fct_126_variance_ratio_5_63d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(5) of log-returns over trailing 63-day window."""
    return _rolling_vr(close, _TD_QTR, 5)


def fct_127_variance_ratio_10_63d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(10) of log-returns over trailing 63-day window."""
    return _rolling_vr(close, _TD_QTR, 10)


def fct_128_variance_ratio_5_126d(close: pd.Series) -> pd.Series:
    """Variance ratio VR(5) of log-returns over trailing 126-day window."""
    return _rolling_vr(close, _TD_HALF, 5)


def fct_129_variance_ratio_5_63d_depth_below1(close: pd.Series) -> pd.Series:
    """Depth of VR(5,63d) below 1.0 (mean-reverting scaling signal)."""
    return (1.0 - _rolling_vr(close, _TD_QTR, 5)).clip(lower=0.0)


def fct_130_variance_ratio_5_63d_above1_flag(close: pd.Series) -> pd.Series:
    """Binary flag: VR(5,63d) > 1.0 (momentum / trending scaling)."""
    return (_rolling_vr(close, _TD_QTR, 5) > 1.0).astype(float)


def fct_131_variance_ratio_5_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of VR(5,63d) within trailing 252-day distribution."""
    vr = _rolling_vr(close, _TD_QTR, 5)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_132_variance_ratio_5_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of VR(5,63d) within its 252-day rolling distribution."""
    vr = _rolling_vr(close, _TD_QTR, 5)
    m = _rolling_mean(vr, _TD_YEAR)
    s = _rolling_std(vr, _TD_YEAR)
    return _safe_div(vr - m, s)


def fct_133_variance_ratio_10_126d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of VR(10,126d) within trailing 252-day distribution."""
    vr = _rolling_vr(close, _TD_HALF, 10)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_134_variance_ratio_vr5_vr10_spread_63d(close: pd.Series) -> pd.Series:
    """Spread: VR(5,63d) minus VR(10,63d) (short vs medium variance scaling)."""
    return _rolling_vr(close, _TD_QTR, 5) - _rolling_vr(close, _TD_QTR, 10)


def fct_135_variance_ratio_5_63d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of VR(5,63d) across all history."""
    vr = _rolling_vr(close, _TD_QTR, 5)
    return vr.expanding(min_periods=_TD_HALF).min()


# --- Group N (136-145): Composite / cross-measure fractal features ---

def fct_136_fractal_roughness_composite_63d(close: pd.Series) -> pd.Series:
    """Composite roughness: average of normalized Higuchi FD and Petrosian FD over 63d."""
    hig = _rolling_lacunarity(close, _TD_QTR)  # lacunarity as texture proxy
    pet = _rolling_petrosian(close, _TD_QTR)
    return (hig + pet) / 2.0


def fct_137_fractal_texture_index_63d(close: pd.Series) -> pd.Series:
    """Fractal texture index: product of SampEn and multifractal width over 63d."""
    se = _rolling_sampen(close, _TD_QTR)
    mf = _rolling_multifractal(close, _TD_QTR)
    return se * mf.abs()


def fct_138_fractal_regime_anti_persistent_flag(close: pd.Series) -> pd.Series:
    """Flag: both 63d R/S Hurst < 0.5 AND 63d DFA alpha < 0.5 (consensus anti-persistent)."""
    lr = np.log(close / close.shift(1))
    h_rs = _rolling_vr(close, _TD_QTR, 5)  # VR < 1 ↔ anti-persistent
    ac = _rolling_autocorr1(close, _TD_QTR)
    return ((h_rs < 1.0) & (ac < 0.0)).astype(float)


def fct_139_fractal_roughness_std_ratio_21d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d log-return std to 252d log-return std (scale-dependent roughness)."""
    lr = np.log(close / close.shift(1))
    r21 = _rolling_std(lr, _TD_MON)
    r252 = _rolling_std(lr, _TD_YEAR)
    return _safe_div(r21, r252)


def fct_140_fractal_roughness_std_ratio_5d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 5d log-return std to 252d log-return std."""
    lr = np.log(close / close.shift(1))
    r5 = _rolling_std(lr, _TD_WEEK)
    r252 = _rolling_std(lr, _TD_YEAR)
    return _safe_div(r5, r252)


def fct_141_variance_scaling_exponent_63d(close: pd.Series) -> pd.Series:
    """Variance scaling exponent: log(Var(5d)/Var(1d)) / log(5), proxy for H.
    Over trailing 63-day window."""
    lr = np.log(close / close.shift(1))

    def _vscale(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 10:
            return np.nan
        v1 = np.var(x, ddof=1)
        if v1 < _EPS:
            return np.nan
        agg5 = np.array([x[i:i + 5].sum() for i in range(0, n - 4, 1)])
        v5 = np.var(agg5, ddof=1)
        if v5 < _EPS:
            return np.nan
        return float(np.log(v5 / v1) / np.log(5.0))

    return lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _vscale(np.asarray(x, dtype=float)), raw=True
    )


def fct_142_fractal_entropy_ratio_sampen_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio: 21d SampEn / 63d SampEn (entropy compression signal)."""
    se21 = _rolling_sampen(close, _TD_MON)
    se63 = _rolling_sampen(close, _TD_QTR)
    return _safe_div(se21, se63.clip(lower=_EPS))


def fct_143_fractal_4measure_consensus_63d(close: pd.Series) -> pd.Series:
    """Count of fractal measures consistent with anti-persistence over 63d.
    Counts: (VR5<1, autocorr<0, lacunarity>0.3, SampEn < its 252d median).
    Range 0-4."""
    vr = _rolling_vr(close, _TD_QTR, 5)
    ac = _rolling_autocorr1(close, _TD_QTR)
    la = _rolling_lacunarity(close, _TD_QTR)
    se = _rolling_sampen(close, _TD_QTR)
    se_med = se.rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    flags = (
        (vr < 1.0).astype(float)
        + (ac < 0.0).astype(float)
        + (la > 0.3).astype(float)
        + (se < se_med).astype(float)
    )
    return flags


def fct_144_fractal_texture_change_5d(close: pd.Series) -> pd.Series:
    """5-day change in 63d Higuchi FD (texture velocity)."""
    lp = np.log(close.clip(lower=_EPS))
    hig = lp.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _higuchi_fd_local(np.asarray(x, dtype=float)), raw=True
    )
    return hig.diff(_TD_WEEK)


def fct_145_fractal_texture_change_21d(close: pd.Series) -> pd.Series:
    """21-day change in 63d Higuchi FD (medium-term texture evolution)."""
    lp = np.log(close.clip(lower=_EPS))
    hig = lp.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _higuchi_fd_local(np.asarray(x, dtype=float)), raw=True
    )
    return hig.diff(_TD_MON)


# --- Group O (146-150): Wavelet-proxy and residual roughness features ---

def fct_146_wavelet_proxy_roughness_ratio_21d(close: pd.Series) -> pd.Series:
    """Wavelet-proxy roughness: ratio of odd-lag to even-lag variance of log-returns, 21d."""
    lr = np.log(close / close.shift(1))

    def _odd_even_ratio(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 8:
            return np.nan
        odd = x[0::2]
        even = x[1::2]
        vo = np.var(odd, ddof=1) if len(odd) > 1 else np.nan
        ve = np.var(even, ddof=1) if len(even) > 1 else np.nan
        if ve is np.nan or ve < _EPS:
            return np.nan
        return float(vo / ve)

    return lr.rolling(_TD_MON, min_periods=_TD_MON // 2).apply(
        lambda x: _odd_even_ratio(np.asarray(x, dtype=float)), raw=True
    )


def fct_147_wavelet_proxy_roughness_ratio_63d(close: pd.Series) -> pd.Series:
    """Wavelet-proxy roughness: odd-lag/even-lag log-return variance ratio, 63d."""
    lr = np.log(close / close.shift(1))

    def _odd_even_ratio(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 8:
            return np.nan
        odd = x[0::2]
        even = x[1::2]
        vo = np.var(odd, ddof=1) if len(odd) > 1 else np.nan
        ve = np.var(even, ddof=1) if len(even) > 1 else np.nan
        if ve is np.nan or ve < _EPS:
            return np.nan
        return float(vo / ve)

    return lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _odd_even_ratio(np.asarray(x, dtype=float)), raw=True
    )


def fct_148_detrended_roughness_63d(close: pd.Series) -> pd.Series:
    """Detrended roughness: std-dev of detrended log-price over 63 days."""
    lp = np.log(close.clip(lower=_EPS))

    def _detrended_std(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 4:
            return np.nan
        xi = np.arange(n, dtype=float)
        coeffs = np.polyfit(xi, x, 1)
        resid = x - np.polyval(coeffs, xi)
        return float(np.std(resid, ddof=1))

    return lp.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _detrended_std(np.asarray(x, dtype=float)), raw=True
    )


def fct_149_detrended_roughness_126d(close: pd.Series) -> pd.Series:
    """Detrended roughness: std-dev of detrended log-price over 126 days."""
    lp = np.log(close.clip(lower=_EPS))

    def _detrended_std(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 4:
            return np.nan
        xi = np.arange(n, dtype=float)
        coeffs = np.polyfit(xi, x, 1)
        resid = x - np.polyval(coeffs, xi)
        return float(np.std(resid, ddof=1))

    return lp.rolling(_TD_HALF, min_periods=_TD_HALF // 2).apply(
        lambda x: _detrended_std(np.asarray(x, dtype=float)), raw=True
    )


def fct_150_fractal_summary_anti_persist_score(close: pd.Series) -> pd.Series:
    """Summary anti-persistence fractal score over 63d: standardised sum of
    (1-VR5), (-autocorr1), and (1-Hurst_VR) signals; higher = more anti-persistent."""
    vr = _rolling_vr(close, _TD_QTR, 5)
    ac = _rolling_autocorr1(close, _TD_QTR)
    lr = np.log(close / close.shift(1))
    hvr = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_vr_local(np.asarray(x, dtype=float)), raw=True
    )
    return (1.0 - vr.fillna(1.0)) + (-ac.fillna(0.0)) + (1.0 - hvr.fillna(0.5))


def _hurst_vr_local(x: np.ndarray) -> float:
    """Variance-ratio Hurst (local copy for use inside apply)."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    q = 4
    var1 = np.var(x, ddof=1)
    if var1 < _EPS:
        return np.nan
    agg = np.array([x[i:i + q].sum() for i in range(n - q + 1)])
    varq = np.var(agg, ddof=1)
    if varq < _EPS:
        return np.nan
    ratio = varq / (q * var1)
    if ratio <= 0:
        return np.nan
    return float(0.5 * np.log(ratio) / np.log(q) + 0.5)


# ── Registry ──────────────────────────────────────────────────────────────────

FRACTAL_STRUCTURE_REGISTRY_076_150 = {
    "fct_076_multifractal_width_63d":                  {"inputs": ["close"], "func": fct_076_multifractal_width_63d},
    "fct_077_multifractal_width_126d":                 {"inputs": ["close"], "func": fct_077_multifractal_width_126d},
    "fct_078_multifractal_width_252d":                 {"inputs": ["close"], "func": fct_078_multifractal_width_252d},
    "fct_079_multifractal_width_63d_pct_rank_252d":    {"inputs": ["close"], "func": fct_079_multifractal_width_63d_pct_rank_252d},
    "fct_080_multifractal_width_63d_zscore_252d":      {"inputs": ["close"], "func": fct_080_multifractal_width_63d_zscore_252d},
    "fct_081_multifractal_width_63d_126d_spread":      {"inputs": ["close"], "func": fct_081_multifractal_width_63d_126d_spread},
    "fct_082_multifractal_width_63d_above02_flag":     {"inputs": ["close"], "func": fct_082_multifractal_width_63d_above02_flag},
    "fct_083_multifractal_width_63d_min_252d":         {"inputs": ["close"], "func": fct_083_multifractal_width_63d_min_252d},
    "fct_084_multifractal_width_63d_max_252d":         {"inputs": ["close"], "func": fct_084_multifractal_width_63d_max_252d},
    "fct_085_multifractal_width_63d_expanding_pct_rank": {"inputs": ["close"], "func": fct_085_multifractal_width_63d_expanding_pct_rank},
    "fct_086_petrosian_fd_21d":                        {"inputs": ["close"], "func": fct_086_petrosian_fd_21d},
    "fct_087_petrosian_fd_63d":                        {"inputs": ["close"], "func": fct_087_petrosian_fd_63d},
    "fct_088_petrosian_fd_126d":                       {"inputs": ["close"], "func": fct_088_petrosian_fd_126d},
    "fct_089_petrosian_fd_63d_pct_rank_252d":          {"inputs": ["close"], "func": fct_089_petrosian_fd_63d_pct_rank_252d},
    "fct_090_petrosian_fd_63d_zscore_252d":            {"inputs": ["close"], "func": fct_090_petrosian_fd_63d_zscore_252d},
    "fct_091_petrosian_higuchi_spread_63d":            {"inputs": ["close"], "func": fct_091_petrosian_higuchi_spread_63d},
    "fct_092_petrosian_fd_21d_63d_spread":             {"inputs": ["close"], "func": fct_092_petrosian_fd_21d_63d_spread},
    "fct_093_petrosian_fd_63d_above15_flag":           {"inputs": ["close"], "func": fct_093_petrosian_fd_63d_above15_flag},
    "fct_094_petrosian_fd_63d_min_252d":               {"inputs": ["close"], "func": fct_094_petrosian_fd_63d_min_252d},
    "fct_095_petrosian_fd_63d_max_252d":               {"inputs": ["close"], "func": fct_095_petrosian_fd_63d_max_252d},
    "fct_096_sampen_63d":                              {"inputs": ["close"], "func": fct_096_sampen_63d},
    "fct_097_sampen_126d":                             {"inputs": ["close"], "func": fct_097_sampen_126d},
    "fct_098_sampen_21d":                              {"inputs": ["close"], "func": fct_098_sampen_21d},
    "fct_099_sampen_63d_pct_rank_252d":                {"inputs": ["close"], "func": fct_099_sampen_63d_pct_rank_252d},
    "fct_100_sampen_63d_zscore_252d":                  {"inputs": ["close"], "func": fct_100_sampen_63d_zscore_252d},
    "fct_101_sampen_21d_63d_spread":                   {"inputs": ["close"], "func": fct_101_sampen_21d_63d_spread},
    "fct_102_sampen_63d_min_252d":                     {"inputs": ["close"], "func": fct_102_sampen_63d_min_252d},
    "fct_103_sampen_63d_max_252d":                     {"inputs": ["close"], "func": fct_103_sampen_63d_max_252d},
    "fct_104_sampen_63d_expanding_pct_rank":           {"inputs": ["close"], "func": fct_104_sampen_63d_expanding_pct_rank},
    "fct_105_sampen_126d_expanding_pct_rank":          {"inputs": ["close"], "func": fct_105_sampen_126d_expanding_pct_rank},
    "fct_106_lacunarity_63d":                          {"inputs": ["close"], "func": fct_106_lacunarity_63d},
    "fct_107_lacunarity_126d":                         {"inputs": ["close"], "func": fct_107_lacunarity_126d},
    "fct_108_lacunarity_21d":                          {"inputs": ["close"], "func": fct_108_lacunarity_21d},
    "fct_109_lacunarity_63d_pct_rank_252d":            {"inputs": ["close"], "func": fct_109_lacunarity_63d_pct_rank_252d},
    "fct_110_lacunarity_63d_zscore_252d":              {"inputs": ["close"], "func": fct_110_lacunarity_63d_zscore_252d},
    "fct_111_lacunarity_21d_63d_spread":               {"inputs": ["close"], "func": fct_111_lacunarity_21d_63d_spread},
    "fct_112_lacunarity_63d_min_252d":                 {"inputs": ["close"], "func": fct_112_lacunarity_63d_min_252d},
    "fct_113_lacunarity_63d_max_252d":                 {"inputs": ["close"], "func": fct_113_lacunarity_63d_max_252d},
    "fct_114_lacunarity_63d_above05_flag":             {"inputs": ["close"], "func": fct_114_lacunarity_63d_above05_flag},
    "fct_115_lacunarity_63d_expanding_pct_rank":       {"inputs": ["close"], "func": fct_115_lacunarity_63d_expanding_pct_rank},
    "fct_116_autocorr_lag1_21d":                       {"inputs": ["close"], "func": fct_116_autocorr_lag1_21d},
    "fct_117_autocorr_lag1_63d":                       {"inputs": ["close"], "func": fct_117_autocorr_lag1_63d},
    "fct_118_autocorr_lag1_126d":                      {"inputs": ["close"], "func": fct_118_autocorr_lag1_126d},
    "fct_119_autocorr_lag1_63d_pct_rank_252d":         {"inputs": ["close"], "func": fct_119_autocorr_lag1_63d_pct_rank_252d},
    "fct_120_autocorr_lag1_63d_zscore_252d":           {"inputs": ["close"], "func": fct_120_autocorr_lag1_63d_zscore_252d},
    "fct_121_autocorr_lag1_21d_63d_spread":            {"inputs": ["close"], "func": fct_121_autocorr_lag1_21d_63d_spread},
    "fct_122_autocorr_lag1_63d_negative_flag":         {"inputs": ["close"], "func": fct_122_autocorr_lag1_63d_negative_flag},
    "fct_123_autocorr_lag1_63d_depth_below_neg01":     {"inputs": ["close"], "func": fct_123_autocorr_lag1_63d_depth_below_neg01},
    "fct_124_autocorr_lag1_63d_min_252d":              {"inputs": ["close"], "func": fct_124_autocorr_lag1_63d_min_252d},
    "fct_125_autocorr_lag1_126d_expanding_pct_rank":   {"inputs": ["close"], "func": fct_125_autocorr_lag1_126d_expanding_pct_rank},
    "fct_126_variance_ratio_5_63d":                    {"inputs": ["close"], "func": fct_126_variance_ratio_5_63d},
    "fct_127_variance_ratio_10_63d":                   {"inputs": ["close"], "func": fct_127_variance_ratio_10_63d},
    "fct_128_variance_ratio_5_126d":                   {"inputs": ["close"], "func": fct_128_variance_ratio_5_126d},
    "fct_129_variance_ratio_5_63d_depth_below1":       {"inputs": ["close"], "func": fct_129_variance_ratio_5_63d_depth_below1},
    "fct_130_variance_ratio_5_63d_above1_flag":        {"inputs": ["close"], "func": fct_130_variance_ratio_5_63d_above1_flag},
    "fct_131_variance_ratio_5_63d_pct_rank_252d":      {"inputs": ["close"], "func": fct_131_variance_ratio_5_63d_pct_rank_252d},
    "fct_132_variance_ratio_5_63d_zscore_252d":        {"inputs": ["close"], "func": fct_132_variance_ratio_5_63d_zscore_252d},
    "fct_133_variance_ratio_10_126d_pct_rank_252d":    {"inputs": ["close"], "func": fct_133_variance_ratio_10_126d_pct_rank_252d},
    "fct_134_variance_ratio_vr5_vr10_spread_63d":      {"inputs": ["close"], "func": fct_134_variance_ratio_vr5_vr10_spread_63d},
    "fct_135_variance_ratio_5_63d_expanding_min":      {"inputs": ["close"], "func": fct_135_variance_ratio_5_63d_expanding_min},
    "fct_136_fractal_roughness_composite_63d":         {"inputs": ["close"], "func": fct_136_fractal_roughness_composite_63d},
    "fct_137_fractal_texture_index_63d":               {"inputs": ["close"], "func": fct_137_fractal_texture_index_63d},
    "fct_138_fractal_regime_anti_persistent_flag":     {"inputs": ["close"], "func": fct_138_fractal_regime_anti_persistent_flag},
    "fct_139_fractal_roughness_std_ratio_21d_252d":    {"inputs": ["close"], "func": fct_139_fractal_roughness_std_ratio_21d_252d},
    "fct_140_fractal_roughness_std_ratio_5d_252d":     {"inputs": ["close"], "func": fct_140_fractal_roughness_std_ratio_5d_252d},
    "fct_141_variance_scaling_exponent_63d":           {"inputs": ["close"], "func": fct_141_variance_scaling_exponent_63d},
    "fct_142_fractal_entropy_ratio_sampen_21d_63d":    {"inputs": ["close"], "func": fct_142_fractal_entropy_ratio_sampen_21d_63d},
    "fct_143_fractal_4measure_consensus_63d":          {"inputs": ["close"], "func": fct_143_fractal_4measure_consensus_63d},
    "fct_144_fractal_texture_change_5d":               {"inputs": ["close"], "func": fct_144_fractal_texture_change_5d},
    "fct_145_fractal_texture_change_21d":              {"inputs": ["close"], "func": fct_145_fractal_texture_change_21d},
    "fct_146_wavelet_proxy_roughness_ratio_21d":       {"inputs": ["close"], "func": fct_146_wavelet_proxy_roughness_ratio_21d},
    "fct_147_wavelet_proxy_roughness_ratio_63d":       {"inputs": ["close"], "func": fct_147_wavelet_proxy_roughness_ratio_63d},
    "fct_148_detrended_roughness_63d":                 {"inputs": ["close"], "func": fct_148_detrended_roughness_63d},
    "fct_149_detrended_roughness_126d":                {"inputs": ["close"], "func": fct_149_detrended_roughness_126d},
    "fct_150_fractal_summary_anti_persist_score":      {"inputs": ["close"], "func": fct_150_fractal_summary_anti_persist_score},
}
