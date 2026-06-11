"""
105_fractal_structure — Base Features 001-075
Domain: fractal / self-similarity structure of the price decline — Hurst exponent
        (R/S and variance-ratio), detrended fluctuation analysis (DFA), Higuchi and
        Katz fractal dimension, multifractal width, self-affinity and roughness of
        the price path across multiple windows.  Texture of the decline ONLY —
        not its depth or speed.
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


def _hurst_rs(x: np.ndarray) -> float:
    """Classic R/S Hurst exponent for a 1-D array of log-returns.
    Drops NaNs before computing.  Returns NaN when insufficient data."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    # Use two sub-period lengths: n//2 and n//4 (>= 4 each)
    rs_vals = []
    span_sizes = []
    for size in [n // 4, n // 2, n]:
        if size < 4:
            continue
        n_chunks = n // size
        if n_chunks < 1:
            continue
        rs_chunk = []
        for k in range(n_chunks):
            seg = x[k * size: (k + 1) * size]
            if len(seg) < 4:
                continue
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r = dev.max() - dev.min()
            s = seg.std(ddof=1)
            if s < _EPS:
                continue
            rs_chunk.append(r / s)
        if rs_chunk:
            rs_vals.append(np.mean(rs_chunk))
            span_sizes.append(size)
    if len(rs_vals) < 2:
        return np.nan
    log_n = np.log(span_sizes)
    log_rs = np.log(np.maximum(rs_vals, _EPS))
    if log_n[-1] - log_n[0] < _EPS:
        return np.nan
    return float(np.polyfit(log_n, log_rs, 1)[0])


def _hurst_vr(x: np.ndarray) -> float:
    """Variance-ratio Hurst estimator for log-returns array.
    H ≈ 0.5 * log(Var(q-period) / Var(1-period)) / log(q) for q=4."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    q = 4
    var1 = np.var(x, ddof=1)
    if var1 < _EPS:
        return np.nan
    # q-period returns
    agg = np.array([x[i:i + q].sum() for i in range(0, n - q + 1, 1)])
    varq = np.var(agg, ddof=1)
    if varq < _EPS or q < 2:
        return np.nan
    ratio = varq / (q * var1)
    if ratio <= 0:
        return np.nan
    return float(0.5 * np.log(ratio) / np.log(q) + 0.5)


def _dfa_alpha(x: np.ndarray, scales: list) -> float:
    """Detrended Fluctuation Analysis alpha (scaling exponent).
    x should be log-returns; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    y = np.cumsum(x - x.mean())
    f_vals = []
    valid_scales = []
    for s in scales:
        if s < 4 or s > n // 2:
            continue
        n_seg = n // s
        if n_seg < 2:
            continue
        rms_list = []
        for k in range(n_seg):
            seg = y[k * s: (k + 1) * s]
            xi = np.arange(len(seg), dtype=float)
            coeffs = np.polyfit(xi, seg, 1)
            trend = np.polyval(coeffs, xi)
            rms_list.append(np.sqrt(np.mean((seg - trend) ** 2)))
        f_vals.append(np.mean(rms_list))
        valid_scales.append(s)
    if len(f_vals) < 2:
        return np.nan
    log_s = np.log(valid_scales)
    log_f = np.log(np.maximum(f_vals, _EPS))
    return float(np.polyfit(log_s, log_f, 1)[0])


def _higuchi_fd(x: np.ndarray, k_max: int = 4) -> float:
    """Higuchi fractal dimension for a time-series window; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    lk = []
    ks = []
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
    log_k = np.log(ks)
    log_l = np.log(np.maximum(lk, _EPS))
    return float(-np.polyfit(log_k, log_l, 1)[0])


def _katz_fd(x: np.ndarray) -> float:
    """Katz fractal dimension; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    diffs = np.diff(x)
    L = np.sum(np.abs(diffs))
    d = np.max(np.abs(x - x[0]))
    if L < _EPS or d < _EPS:
        return np.nan
    avg_step = L / (n - 1)
    return float(np.log10(n) / (np.log10(d / avg_step) + np.log10(n) + _EPS))


def _rolling_hurst_rs(close: pd.Series, w: int) -> pd.Series:
    """Rolling R/S Hurst exponent of log-returns over window w."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_hurst_vr(close: pd.Series, w: int) -> pd.Series:
    """Rolling variance-ratio Hurst estimator of log-returns over window w."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _hurst_vr(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_dfa(close: pd.Series, w: int, scales: list) -> pd.Series:
    """Rolling DFA alpha of log-returns over window w."""
    lr = np.log(close / close.shift(1))
    sc = scales
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), sc), raw=True
    )


def _rolling_higuchi(close: pd.Series, w: int) -> pd.Series:
    """Rolling Higuchi fractal dimension of log-price over window w."""
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _higuchi_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_katz(close: pd.Series, w: int) -> pd.Series:
    """Rolling Katz fractal dimension of log-price over window w."""
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _katz_fd(np.asarray(x, dtype=float)), raw=True
    )


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): R/S Hurst exponent at multiple windows ---

def fct_001_hurst_rs_63d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 63-day window."""
    return _rolling_hurst_rs(close, _TD_QTR)


def fct_002_hurst_rs_126d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 126-day window."""
    return _rolling_hurst_rs(close, _TD_HALF)


def fct_003_hurst_rs_252d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 252-day window."""
    return _rolling_hurst_rs(close, _TD_YEAR)


def fct_004_hurst_rs_21d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 21-day window."""
    return _rolling_hurst_rs(close, _TD_MON)


def fct_005_hurst_rs_42d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 42-day window (2-month)."""
    return _rolling_hurst_rs(close, 42)


def fct_006_hurst_rs_189d(close: pd.Series) -> pd.Series:
    """R/S Hurst exponent of log-returns over trailing 189-day window (3/4-year)."""
    return _rolling_hurst_rs(close, 189)


def fct_007_hurst_rs_63d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 63d R/S Hurst below 0.5 (anti-persistent regime strength)."""
    return (0.5 - _rolling_hurst_rs(close, _TD_QTR)).clip(lower=0.0)


def fct_008_hurst_rs_126d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 126d R/S Hurst below 0.5."""
    return (0.5 - _rolling_hurst_rs(close, _TD_HALF)).clip(lower=0.0)


def fct_009_hurst_rs_252d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 252d R/S Hurst below 0.5."""
    return (0.5 - _rolling_hurst_rs(close, _TD_YEAR)).clip(lower=0.0)


def fct_010_hurst_rs_63d_above05_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d R/S Hurst > 0.5 (persistent / trending decline)."""
    return (_rolling_hurst_rs(close, _TD_QTR) > 0.5).astype(float)


def fct_011_hurst_rs_252d_above07_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 252d R/S Hurst > 0.7 (strongly persistent decline)."""
    return (_rolling_hurst_rs(close, _TD_YEAR) > 0.7).astype(float)


def fct_012_hurst_rs_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d R/S Hurst within trailing 252-day distribution."""
    h = _rolling_hurst_rs(close, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (013-022): Variance-ratio Hurst estimator ---

def fct_013_hurst_vr_63d(close: pd.Series) -> pd.Series:
    """Variance-ratio Hurst estimator over trailing 63 days."""
    return _rolling_hurst_vr(close, _TD_QTR)


def fct_014_hurst_vr_126d(close: pd.Series) -> pd.Series:
    """Variance-ratio Hurst estimator over trailing 126 days."""
    return _rolling_hurst_vr(close, _TD_HALF)


def fct_015_hurst_vr_252d(close: pd.Series) -> pd.Series:
    """Variance-ratio Hurst estimator over trailing 252 days."""
    return _rolling_hurst_vr(close, _TD_YEAR)


def fct_016_hurst_vr_42d(close: pd.Series) -> pd.Series:
    """Variance-ratio Hurst estimator over trailing 42 days."""
    return _rolling_hurst_vr(close, 42)


def fct_017_hurst_vr_63d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 63d VR-Hurst below 0.5 (mean-reverting fractal signal)."""
    return (0.5 - _rolling_hurst_vr(close, _TD_QTR)).clip(lower=0.0)


def fct_018_hurst_vr_126d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 126d VR-Hurst below 0.5."""
    return (0.5 - _rolling_hurst_vr(close, _TD_HALF)).clip(lower=0.0)


def fct_019_hurst_vr_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d VR-Hurst within trailing 252-day distribution."""
    h = _rolling_hurst_vr(close, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_020_hurst_vr_rs_spread_63d(close: pd.Series) -> pd.Series:
    """Spread between VR-Hurst and R/S Hurst over 63-day window (method divergence)."""
    return _rolling_hurst_vr(close, _TD_QTR) - _rolling_hurst_rs(close, _TD_QTR)


def fct_021_hurst_vr_rs_spread_126d(close: pd.Series) -> pd.Series:
    """Spread between VR-Hurst and R/S Hurst over 126-day window."""
    return _rolling_hurst_vr(close, _TD_HALF) - _rolling_hurst_rs(close, _TD_HALF)


def fct_022_hurst_vr_252d_zscore_hist(close: pd.Series) -> pd.Series:
    """Z-score of 252d VR-Hurst relative to its own 252-day rolling distribution."""
    h = _rolling_hurst_vr(close, _TD_YEAR)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


# --- Group C (023-033): DFA scaling exponent ---

def fct_023_dfa_alpha_63d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent (alpha) of log-returns over 63-day window."""
    return _rolling_dfa(close, _TD_QTR, [4, 8, 16])


def fct_024_dfa_alpha_126d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent over 126-day window."""
    return _rolling_dfa(close, _TD_HALF, [4, 8, 16, 32])


def fct_025_dfa_alpha_252d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent over 252-day window."""
    return _rolling_dfa(close, _TD_YEAR, [4, 8, 16, 32, 63])


def fct_026_dfa_alpha_42d(close: pd.Series) -> pd.Series:
    """DFA scaling exponent over 42-day window."""
    return _rolling_dfa(close, 42, [4, 8])


def fct_027_dfa_alpha_63d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 63d DFA alpha below 0.5 (sub-diffusive / anti-persistent path)."""
    return (0.5 - _rolling_dfa(close, _TD_QTR, [4, 8, 16])).clip(lower=0.0)


def fct_028_dfa_alpha_126d_depth_below05(close: pd.Series) -> pd.Series:
    """Depth of 126d DFA alpha below 0.5."""
    return (0.5 - _rolling_dfa(close, _TD_HALF, [4, 8, 16, 32])).clip(lower=0.0)


def fct_029_dfa_alpha_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d DFA alpha within trailing 252-day distribution."""
    a = _rolling_dfa(close, _TD_QTR, [4, 8, 16])
    return a.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_030_dfa_alpha_252d_pct_rank_hist(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d DFA alpha across all history."""
    a = _rolling_dfa(close, _TD_YEAR, [4, 8, 16, 32, 63])
    return a.expanding(min_periods=_TD_HALF).rank(pct=True)


def fct_031_dfa_hurst_rs_spread_63d(close: pd.Series) -> pd.Series:
    """Spread: DFA alpha minus R/S Hurst over 63 days (method agreement signal)."""
    return _rolling_dfa(close, _TD_QTR, [4, 8, 16]) - _rolling_hurst_rs(close, _TD_QTR)


def fct_032_dfa_alpha_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d DFA alpha within its 252-day rolling distribution."""
    a = _rolling_dfa(close, _TD_QTR, [4, 8, 16])
    m = _rolling_mean(a, _TD_YEAR)
    s = _rolling_std(a, _TD_YEAR)
    return _safe_div(a - m, s)


def fct_033_dfa_alpha_126d_above05_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 126d DFA alpha > 0.5 (super-diffusive / persistent path)."""
    return (_rolling_dfa(close, _TD_HALF, [4, 8, 16, 32]) > 0.5).astype(float)


# --- Group D (034-044): Higuchi fractal dimension ---

def fct_034_higuchi_fd_21d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of log-price over trailing 21-day window."""
    return _rolling_higuchi(close, _TD_MON)


def fct_035_higuchi_fd_63d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of log-price over trailing 63-day window."""
    return _rolling_higuchi(close, _TD_QTR)


def fct_036_higuchi_fd_126d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of log-price over trailing 126-day window."""
    return _rolling_higuchi(close, _TD_HALF)


def fct_037_higuchi_fd_252d(close: pd.Series) -> pd.Series:
    """Higuchi fractal dimension of log-price over trailing 252-day window."""
    return _rolling_higuchi(close, _TD_YEAR)


def fct_038_higuchi_fd_63d_depth_below15(close: pd.Series) -> pd.Series:
    """Depth of 63d Higuchi FD below 1.5 (smoother / less fractal path)."""
    return (1.5 - _rolling_higuchi(close, _TD_QTR)).clip(lower=0.0)


def fct_039_higuchi_fd_63d_above15_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d Higuchi FD > 1.5 (rougher-than-Brownian path)."""
    return (_rolling_higuchi(close, _TD_QTR) > 1.5).astype(float)


def fct_040_higuchi_fd_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d Higuchi FD within trailing 252-day distribution."""
    h = _rolling_higuchi(close, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_041_higuchi_fd_126d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 126d Higuchi FD within trailing 252-day distribution."""
    h = _rolling_higuchi(close, _TD_HALF)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_042_higuchi_fd_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d Higuchi FD within its 252-day rolling distribution."""
    h = _rolling_higuchi(close, _TD_QTR)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def fct_043_higuchi_fd_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d Higuchi FD minus 63d Higuchi FD (short-vs-medium roughness)."""
    return _rolling_higuchi(close, _TD_MON) - _rolling_higuchi(close, _TD_QTR)


def fct_044_higuchi_fd_252d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 252d Higuchi FD (all-time smoothest price path)."""
    h = _rolling_higuchi(close, _TD_YEAR)
    return h.expanding(min_periods=_TD_HALF).min()


# --- Group E (045-055): Katz fractal dimension ---

def fct_045_katz_fd_21d(close: pd.Series) -> pd.Series:
    """Katz fractal dimension of log-price over trailing 21-day window."""
    return _rolling_katz(close, _TD_MON)


def fct_046_katz_fd_63d(close: pd.Series) -> pd.Series:
    """Katz fractal dimension of log-price over trailing 63-day window."""
    return _rolling_katz(close, _TD_QTR)


def fct_047_katz_fd_126d(close: pd.Series) -> pd.Series:
    """Katz fractal dimension of log-price over trailing 126-day window."""
    return _rolling_katz(close, _TD_HALF)


def fct_048_katz_fd_252d(close: pd.Series) -> pd.Series:
    """Katz fractal dimension of log-price over trailing 252-day window."""
    return _rolling_katz(close, _TD_YEAR)


def fct_049_katz_fd_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d Katz FD within trailing 252-day distribution."""
    k = _rolling_katz(close, _TD_QTR)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_050_katz_fd_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d Katz FD within its 252-day rolling distribution."""
    k = _rolling_katz(close, _TD_QTR)
    m = _rolling_mean(k, _TD_YEAR)
    s = _rolling_std(k, _TD_YEAR)
    return _safe_div(k - m, s)


def fct_051_katz_higuchi_spread_63d(close: pd.Series) -> pd.Series:
    """Spread: Katz FD minus Higuchi FD over 63 days (method divergence)."""
    return _rolling_katz(close, _TD_QTR) - _rolling_higuchi(close, _TD_QTR)


def fct_052_katz_fd_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: 21d Katz FD minus 63d Katz FD."""
    return _rolling_katz(close, _TD_MON) - _rolling_katz(close, _TD_QTR)


def fct_053_katz_fd_63d_above15_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 63d Katz FD > 1.5 (highly jagged path)."""
    return (_rolling_katz(close, _TD_QTR) > 1.5).astype(float)


def fct_054_katz_fd_252d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 252d Katz FD (historically smoothest path)."""
    k = _rolling_katz(close, _TD_YEAR)
    return k.expanding(min_periods=_TD_HALF).min()


def fct_055_katz_fd_252d_pct_rank_hist(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d Katz FD across all history."""
    k = _rolling_katz(close, _TD_YEAR)
    return k.expanding(min_periods=_TD_HALF).rank(pct=True)


# --- Group F (056-065): Price-path roughness (variance of log-returns) ---

def fct_056_logret_roughness_21d(close: pd.Series) -> pd.Series:
    """Std-dev of log-returns over trailing 21 days (short-window roughness)."""
    lr = np.log(close / close.shift(1))
    return _rolling_std(lr, _TD_MON)


def fct_057_logret_roughness_63d(close: pd.Series) -> pd.Series:
    """Std-dev of log-returns over trailing 63 days."""
    lr = np.log(close / close.shift(1))
    return _rolling_std(lr, _TD_QTR)


def fct_058_logret_roughness_126d(close: pd.Series) -> pd.Series:
    """Std-dev of log-returns over trailing 126 days."""
    lr = np.log(close / close.shift(1))
    return _rolling_std(lr, _TD_HALF)


def fct_059_roughness_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21d roughness to 63d roughness (rising = recent roughness spike)."""
    lr = np.log(close / close.shift(1))
    r21 = _rolling_std(lr, _TD_MON)
    r63 = _rolling_std(lr, _TD_QTR)
    return _safe_div(r21, r63)


def fct_060_roughness_ratio_63d_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63d roughness to 252d roughness."""
    lr = np.log(close / close.shift(1))
    r63 = _rolling_std(lr, _TD_QTR)
    r252 = _rolling_std(lr, _TD_YEAR)
    return _safe_div(r63, r252)


def fct_061_roughness_zscore_21d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d log-return roughness within 252-day distribution."""
    lr = np.log(close / close.shift(1))
    r21 = _rolling_std(lr, _TD_MON)
    m = _rolling_mean(r21, _TD_YEAR)
    s = _rolling_std(r21, _TD_YEAR)
    return _safe_div(r21 - m, s)


def fct_062_roughness_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d roughness within trailing 252-day distribution."""
    lr = np.log(close / close.shift(1))
    r63 = _rolling_std(lr, _TD_QTR)
    return r63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_063_roughness_acceleration_21d(close: pd.Series) -> pd.Series:
    """5-day change in 21d log-return roughness (roughness velocity)."""
    lr = np.log(close / close.shift(1))
    r21 = _rolling_std(lr, _TD_MON)
    return r21.diff(_TD_WEEK)


def fct_064_roughness_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Roughness proxy: std-dev of (H-L)/close over trailing 63 days."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_std(hl_range, _TD_QTR)


def fct_065_roughness_hl_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Roughness proxy: std-dev of (H-L)/close over trailing 21 days."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_std(hl_range, _TD_MON)


# --- Group G (066-075): Self-affinity / scaling consistency ---

def fct_066_scaling_consistency_63d(close: pd.Series) -> pd.Series:
    """Scaling consistency: abs(R/S Hurst minus DFA alpha) over 63d; near 0 = consistent."""
    h_rs = _rolling_hurst_rs(close, _TD_QTR)
    h_dfa = _rolling_dfa(close, _TD_QTR, [4, 8, 16])
    return (h_rs - h_dfa).abs()


def fct_067_scaling_consistency_126d(close: pd.Series) -> pd.Series:
    """Scaling consistency: abs(R/S Hurst minus DFA alpha) over 126d."""
    h_rs = _rolling_hurst_rs(close, _TD_HALF)
    h_dfa = _rolling_dfa(close, _TD_HALF, [4, 8, 16, 32])
    return (h_rs - h_dfa).abs()


def fct_068_hurst_rs_min_63d_in_252d(close: pd.Series) -> pd.Series:
    """Minimum R/S Hurst (63d) over trailing 252-day window (most anti-persistent stretch)."""
    h = _rolling_hurst_rs(close, _TD_QTR)
    return _rolling_min(h, _TD_YEAR)


def fct_069_hurst_rs_max_63d_in_252d(close: pd.Series) -> pd.Series:
    """Maximum R/S Hurst (63d) over trailing 252-day window (most persistent stretch)."""
    h = _rolling_hurst_rs(close, _TD_QTR)
    return _rolling_max(h, _TD_YEAR)


def fct_070_hurst_rs_range_63d_in_252d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 63d R/S Hurst values over trailing 252 days (Hurst instability)."""
    h = _rolling_hurst_rs(close, _TD_QTR)
    return _rolling_max(h, _TD_YEAR) - _rolling_min(h, _TD_YEAR)


def fct_071_hurst_rs_21d_63d_spread(close: pd.Series) -> pd.Series:
    """Spread: R/S Hurst over 21d minus R/S Hurst over 63d (short vs medium scaling)."""
    return _rolling_hurst_rs(close, _TD_MON) - _rolling_hurst_rs(close, _TD_QTR)


def fct_072_hurst_rs_63d_126d_spread(close: pd.Series) -> pd.Series:
    """Spread: R/S Hurst over 63d minus R/S Hurst over 126d (medium vs long scaling)."""
    return _rolling_hurst_rs(close, _TD_QTR) - _rolling_hurst_rs(close, _TD_HALF)


def fct_073_fractal_composite_score_63d(close: pd.Series) -> pd.Series:
    """Composite fractal roughness: average of Higuchi FD, Katz FD (normalized) over 63d."""
    hfd = _rolling_higuchi(close, _TD_QTR)
    kfd = _rolling_katz(close, _TD_QTR)
    return (hfd + kfd) / 2.0


def fct_074_hurst_rs_63d_consec_below05(close: pd.Series) -> pd.Series:
    """Consecutive days 63d R/S Hurst has been below 0.5 (persistent anti-persistent streak)."""
    h = _rolling_hurst_rs(close, _TD_QTR)
    cond = h < 0.5
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def fct_075_dfa_alpha_63d_consec_below05(close: pd.Series) -> pd.Series:
    """Consecutive days 63d DFA alpha has been below 0.5 (sub-diffusive regime streak)."""
    a = _rolling_dfa(close, _TD_QTR, [4, 8, 16])
    cond = a < 0.5
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

FRACTAL_STRUCTURE_REGISTRY_001_075 = {
    "fct_001_hurst_rs_63d":                  {"inputs": ["close"], "func": fct_001_hurst_rs_63d},
    "fct_002_hurst_rs_126d":                 {"inputs": ["close"], "func": fct_002_hurst_rs_126d},
    "fct_003_hurst_rs_252d":                 {"inputs": ["close"], "func": fct_003_hurst_rs_252d},
    "fct_004_hurst_rs_21d":                  {"inputs": ["close"], "func": fct_004_hurst_rs_21d},
    "fct_005_hurst_rs_42d":                  {"inputs": ["close"], "func": fct_005_hurst_rs_42d},
    "fct_006_hurst_rs_189d":                 {"inputs": ["close"], "func": fct_006_hurst_rs_189d},
    "fct_007_hurst_rs_63d_depth_below05":    {"inputs": ["close"], "func": fct_007_hurst_rs_63d_depth_below05},
    "fct_008_hurst_rs_126d_depth_below05":   {"inputs": ["close"], "func": fct_008_hurst_rs_126d_depth_below05},
    "fct_009_hurst_rs_252d_depth_below05":   {"inputs": ["close"], "func": fct_009_hurst_rs_252d_depth_below05},
    "fct_010_hurst_rs_63d_above05_flag":     {"inputs": ["close"], "func": fct_010_hurst_rs_63d_above05_flag},
    "fct_011_hurst_rs_252d_above07_flag":    {"inputs": ["close"], "func": fct_011_hurst_rs_252d_above07_flag},
    "fct_012_hurst_rs_63d_pct_rank_252d":    {"inputs": ["close"], "func": fct_012_hurst_rs_63d_pct_rank_252d},
    "fct_013_hurst_vr_63d":                  {"inputs": ["close"], "func": fct_013_hurst_vr_63d},
    "fct_014_hurst_vr_126d":                 {"inputs": ["close"], "func": fct_014_hurst_vr_126d},
    "fct_015_hurst_vr_252d":                 {"inputs": ["close"], "func": fct_015_hurst_vr_252d},
    "fct_016_hurst_vr_42d":                  {"inputs": ["close"], "func": fct_016_hurst_vr_42d},
    "fct_017_hurst_vr_63d_depth_below05":    {"inputs": ["close"], "func": fct_017_hurst_vr_63d_depth_below05},
    "fct_018_hurst_vr_126d_depth_below05":   {"inputs": ["close"], "func": fct_018_hurst_vr_126d_depth_below05},
    "fct_019_hurst_vr_63d_pct_rank_252d":    {"inputs": ["close"], "func": fct_019_hurst_vr_63d_pct_rank_252d},
    "fct_020_hurst_vr_rs_spread_63d":        {"inputs": ["close"], "func": fct_020_hurst_vr_rs_spread_63d},
    "fct_021_hurst_vr_rs_spread_126d":       {"inputs": ["close"], "func": fct_021_hurst_vr_rs_spread_126d},
    "fct_022_hurst_vr_252d_zscore_hist":     {"inputs": ["close"], "func": fct_022_hurst_vr_252d_zscore_hist},
    "fct_023_dfa_alpha_63d":                 {"inputs": ["close"], "func": fct_023_dfa_alpha_63d},
    "fct_024_dfa_alpha_126d":                {"inputs": ["close"], "func": fct_024_dfa_alpha_126d},
    "fct_025_dfa_alpha_252d":                {"inputs": ["close"], "func": fct_025_dfa_alpha_252d},
    "fct_026_dfa_alpha_42d":                 {"inputs": ["close"], "func": fct_026_dfa_alpha_42d},
    "fct_027_dfa_alpha_63d_depth_below05":   {"inputs": ["close"], "func": fct_027_dfa_alpha_63d_depth_below05},
    "fct_028_dfa_alpha_126d_depth_below05":  {"inputs": ["close"], "func": fct_028_dfa_alpha_126d_depth_below05},
    "fct_029_dfa_alpha_63d_pct_rank_252d":   {"inputs": ["close"], "func": fct_029_dfa_alpha_63d_pct_rank_252d},
    "fct_030_dfa_alpha_252d_pct_rank_hist":  {"inputs": ["close"], "func": fct_030_dfa_alpha_252d_pct_rank_hist},
    "fct_031_dfa_hurst_rs_spread_63d":       {"inputs": ["close"], "func": fct_031_dfa_hurst_rs_spread_63d},
    "fct_032_dfa_alpha_63d_zscore_252d":     {"inputs": ["close"], "func": fct_032_dfa_alpha_63d_zscore_252d},
    "fct_033_dfa_alpha_126d_above05_flag":   {"inputs": ["close"], "func": fct_033_dfa_alpha_126d_above05_flag},
    "fct_034_higuchi_fd_21d":                {"inputs": ["close"], "func": fct_034_higuchi_fd_21d},
    "fct_035_higuchi_fd_63d":                {"inputs": ["close"], "func": fct_035_higuchi_fd_63d},
    "fct_036_higuchi_fd_126d":               {"inputs": ["close"], "func": fct_036_higuchi_fd_126d},
    "fct_037_higuchi_fd_252d":               {"inputs": ["close"], "func": fct_037_higuchi_fd_252d},
    "fct_038_higuchi_fd_63d_depth_below15":  {"inputs": ["close"], "func": fct_038_higuchi_fd_63d_depth_below15},
    "fct_039_higuchi_fd_63d_above15_flag":   {"inputs": ["close"], "func": fct_039_higuchi_fd_63d_above15_flag},
    "fct_040_higuchi_fd_63d_pct_rank_252d":  {"inputs": ["close"], "func": fct_040_higuchi_fd_63d_pct_rank_252d},
    "fct_041_higuchi_fd_126d_pct_rank_252d": {"inputs": ["close"], "func": fct_041_higuchi_fd_126d_pct_rank_252d},
    "fct_042_higuchi_fd_63d_zscore_252d":    {"inputs": ["close"], "func": fct_042_higuchi_fd_63d_zscore_252d},
    "fct_043_higuchi_fd_21d_63d_spread":     {"inputs": ["close"], "func": fct_043_higuchi_fd_21d_63d_spread},
    "fct_044_higuchi_fd_252d_expanding_min": {"inputs": ["close"], "func": fct_044_higuchi_fd_252d_expanding_min},
    "fct_045_katz_fd_21d":                   {"inputs": ["close"], "func": fct_045_katz_fd_21d},
    "fct_046_katz_fd_63d":                   {"inputs": ["close"], "func": fct_046_katz_fd_63d},
    "fct_047_katz_fd_126d":                  {"inputs": ["close"], "func": fct_047_katz_fd_126d},
    "fct_048_katz_fd_252d":                  {"inputs": ["close"], "func": fct_048_katz_fd_252d},
    "fct_049_katz_fd_63d_pct_rank_252d":     {"inputs": ["close"], "func": fct_049_katz_fd_63d_pct_rank_252d},
    "fct_050_katz_fd_63d_zscore_252d":       {"inputs": ["close"], "func": fct_050_katz_fd_63d_zscore_252d},
    "fct_051_katz_higuchi_spread_63d":       {"inputs": ["close"], "func": fct_051_katz_higuchi_spread_63d},
    "fct_052_katz_fd_21d_63d_spread":        {"inputs": ["close"], "func": fct_052_katz_fd_21d_63d_spread},
    "fct_053_katz_fd_63d_above15_flag":      {"inputs": ["close"], "func": fct_053_katz_fd_63d_above15_flag},
    "fct_054_katz_fd_252d_expanding_min":    {"inputs": ["close"], "func": fct_054_katz_fd_252d_expanding_min},
    "fct_055_katz_fd_252d_pct_rank_hist":    {"inputs": ["close"], "func": fct_055_katz_fd_252d_pct_rank_hist},
    "fct_056_logret_roughness_21d":          {"inputs": ["close"], "func": fct_056_logret_roughness_21d},
    "fct_057_logret_roughness_63d":          {"inputs": ["close"], "func": fct_057_logret_roughness_63d},
    "fct_058_logret_roughness_126d":         {"inputs": ["close"], "func": fct_058_logret_roughness_126d},
    "fct_059_roughness_ratio_21d_63d":       {"inputs": ["close"], "func": fct_059_roughness_ratio_21d_63d},
    "fct_060_roughness_ratio_63d_252d":      {"inputs": ["close"], "func": fct_060_roughness_ratio_63d_252d},
    "fct_061_roughness_zscore_21d_in_252d":  {"inputs": ["close"], "func": fct_061_roughness_zscore_21d_in_252d},
    "fct_062_roughness_pct_rank_63d_in_252d": {"inputs": ["close"], "func": fct_062_roughness_pct_rank_63d_in_252d},
    "fct_063_roughness_acceleration_21d":    {"inputs": ["close"], "func": fct_063_roughness_acceleration_21d},
    "fct_064_roughness_hl_range_63d":        {"inputs": ["close", "high", "low"], "func": fct_064_roughness_hl_range_63d},
    "fct_065_roughness_hl_range_21d":        {"inputs": ["close", "high", "low"], "func": fct_065_roughness_hl_range_21d},
    "fct_066_scaling_consistency_63d":       {"inputs": ["close"], "func": fct_066_scaling_consistency_63d},
    "fct_067_scaling_consistency_126d":      {"inputs": ["close"], "func": fct_067_scaling_consistency_126d},
    "fct_068_hurst_rs_min_63d_in_252d":      {"inputs": ["close"], "func": fct_068_hurst_rs_min_63d_in_252d},
    "fct_069_hurst_rs_max_63d_in_252d":      {"inputs": ["close"], "func": fct_069_hurst_rs_max_63d_in_252d},
    "fct_070_hurst_rs_range_63d_in_252d":    {"inputs": ["close"], "func": fct_070_hurst_rs_range_63d_in_252d},
    "fct_071_hurst_rs_21d_63d_spread":       {"inputs": ["close"], "func": fct_071_hurst_rs_21d_63d_spread},
    "fct_072_hurst_rs_63d_126d_spread":      {"inputs": ["close"], "func": fct_072_hurst_rs_63d_126d_spread},
    "fct_073_fractal_composite_score_63d":   {"inputs": ["close"], "func": fct_073_fractal_composite_score_63d},
    "fct_074_hurst_rs_63d_consec_below05":   {"inputs": ["close"], "func": fct_074_hurst_rs_63d_consec_below05},
    "fct_075_dfa_alpha_63d_consec_below05":  {"inputs": ["close"], "func": fct_075_dfa_alpha_63d_consec_below05},
}
