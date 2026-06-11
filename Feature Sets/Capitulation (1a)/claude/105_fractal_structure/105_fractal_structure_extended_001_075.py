"""
105_fractal_structure — Extended Features 001-075
Domain: fractal / self-similarity structure of the price decline — deeper variants:
        Hurst over volume-weighted price, high/low midpoint, log-volume series;
        additional window/lag combinations for DFA, Higuchi, Katz;
        cross-series fractal comparisons (close vs volume);
        higher-order autocorrelation lags; multiscale entropy; composite indices.
        Texture of the decline ONLY — not its depth or speed.
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


# ─── Scalar fractal helpers ────────────────────────────────────────────────────

def _hurst_rs(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    rs_vals, span_sizes = [], []
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


def _dfa_alpha(x: np.ndarray, scales: list) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    y = np.cumsum(x - x.mean())
    f_vals, valid_scales = [], []
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
    return float(np.polyfit(np.log(valid_scales), np.log(np.maximum(f_vals, _EPS)), 1)[0])


def _higuchi_fd(x: np.ndarray, k_max: int = 4) -> float:
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


def _katz_fd(x: np.ndarray) -> float:
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


def _autocorr_lagk(x: np.ndarray, lag: int) -> float:
    """Lag-k autocorrelation; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < lag + 4:
        return np.nan
    xm = x - x.mean()
    denom = np.sum(xm ** 2)
    if denom < _EPS:
        return np.nan
    return float(np.dot(xm[:-lag], xm[lag:]) / denom)


def _sample_entropy(x: np.ndarray, m: int = 2, r_frac: float = 0.2) -> float:
    """Sample Entropy; drops NaNs."""
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * m + 2:
        return np.nan
    r = r_frac * np.std(x, ddof=1)
    if r < _EPS:
        return np.nan

    def _count(m_len):
        cnt = 0
        for i in range(n - m_len):
            for j in range(i + 1, n - m_len):
                if np.max(np.abs(x[i:i + m_len] - x[j:j + m_len])) <= r:
                    cnt += 1
        return cnt

    A = _count(m + 1)
    B = _count(m)
    if B == 0:
        return np.nan
    return float(-np.log((A + _EPS) / (B + _EPS)))


def _variance_ratio(x: np.ndarray, q: int = 5) -> float:
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

def _rolling_hurst_rs_series(s: pd.Series, w: int) -> pd.Series:
    """Generic: R/S Hurst on first-differences of an arbitrary series s."""
    diff_s = s.diff(1)
    return diff_s.rolling(w, min_periods=w // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_dfa_series(s: pd.Series, w: int, scales: list) -> pd.Series:
    diff_s = s.diff(1)
    sc = scales
    return diff_s.rolling(w, min_periods=w // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), sc), raw=True
    )


def _rolling_higuchi_raw(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=w // 2).apply(
        lambda x: _higuchi_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_katz_raw(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=w // 2).apply(
        lambda x: _katz_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_autocorr_lagk(s: pd.Series, w: int, lag: int) -> pd.Series:
    diff_s = s.diff(1)
    k = lag
    return diff_s.rolling(w, min_periods=w // 2).apply(
        lambda x: _autocorr_lagk(np.asarray(x, dtype=float), k), raw=True
    )


def _rolling_sampen(s: pd.Series, w: int) -> pd.Series:
    diff_s = s.diff(1)
    return diff_s.rolling(w, min_periods=w // 2).apply(
        lambda x: _sample_entropy(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_vr(s: pd.Series, w: int, q: int) -> pd.Series:
    diff_s = s.diff(1)
    return diff_s.rolling(w, min_periods=w // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), q), raw=True
    )


# ── Feature functions 001-075 (extended) ─────────────────────────────────────

# --- Group A (001-010): R/S Hurst on alternative price series ---

def fct_ext_001_hurst_rs_hlmid_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """R/S Hurst of high-low midpoint returns over 63 days."""
    mid = np.log(((high + low) / 2.0).clip(lower=_EPS))
    return _rolling_hurst_rs_series(mid, _TD_QTR)


def fct_ext_002_hurst_rs_wclose_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """R/S Hurst of weighted-close (H+L+2C)/4 returns over 63 days."""
    wc = np.log(((high + low + 2.0 * close) / 4.0).clip(lower=_EPS))
    return _rolling_hurst_rs_series(wc, _TD_QTR)


def fct_ext_003_hurst_rs_open_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """R/S Hurst of open-price returns over 63 days."""
    lo = np.log(open.clip(lower=_EPS))
    return _rolling_hurst_rs_series(lo, _TD_QTR)


def fct_ext_004_hurst_rs_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R/S Hurst of log-volume changes over 63 days (volume fractal texture)."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_hurst_rs_series(lv, _TD_QTR)


def fct_ext_005_hurst_rs_logvol_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """R/S Hurst of log-volume changes over 126 days."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_hurst_rs_series(lv, _TD_HALF)


def fct_ext_006_hurst_rs_close_logvol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close R/S Hurst minus volume R/S Hurst, 63d (price vs volume texture divergence)."""
    lr = np.log(close / close.shift(1))
    h_close = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    lv = np.log(volume.clip(lower=1.0))
    h_vol = _rolling_hurst_rs_series(lv, _TD_QTR)
    return h_close - h_vol


def fct_ext_007_hurst_rs_hlmid_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """R/S Hurst of high-low midpoint returns over 126 days."""
    mid = np.log(((high + low) / 2.0).clip(lower=_EPS))
    return _rolling_hurst_rs_series(mid, _TD_HALF)


def fct_ext_008_hurst_rs_hlmid_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """R/S Hurst of high-low midpoint returns over 252 days."""
    mid = np.log(((high + low) / 2.0).clip(lower=_EPS))
    return _rolling_hurst_rs_series(mid, _TD_YEAR)


def fct_ext_009_hurst_rs_close_hlmid_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Spread: close R/S Hurst minus HL-midpoint R/S Hurst over 63d."""
    lr = np.log(close / close.shift(1))
    h_close = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    mid = np.log(((high + low) / 2.0).clip(lower=_EPS))
    h_mid = _rolling_hurst_rs_series(mid, _TD_QTR)
    return h_close - h_mid


def fct_ext_010_hurst_rs_wclose_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of weighted-close 63d R/S Hurst within trailing 252d distribution."""
    wc = np.log(((high + low + 2.0 * close) / 4.0).clip(lower=_EPS))
    h = _rolling_hurst_rs_series(wc, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): DFA on alternative windows and series ---

def fct_ext_011_dfa_alpha_21d(close: pd.Series) -> pd.Series:
    """DFA alpha over trailing 21-day window."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_MON, min_periods=_TD_MON // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8]), raw=True
    )


def fct_ext_012_dfa_alpha_189d(close: pd.Series) -> pd.Series:
    """DFA alpha over trailing 189-day window (3/4-year)."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(189, min_periods=189 // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16, 32, 63]), raw=True
    )


def fct_ext_013_dfa_alpha_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DFA alpha of log-volume changes over 63 days (volume fractal scaling)."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_dfa_series(lv, _TD_QTR, [4, 8, 16])


def fct_ext_014_dfa_alpha_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """DFA alpha of normalized H-L range series over 63 days."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_dfa_series(hl, _TD_QTR, [4, 8, 16])


def fct_ext_015_dfa_close_vol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close DFA alpha minus volume DFA alpha over 63d."""
    lr = np.log(close / close.shift(1))
    d_close = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    lv = np.log(volume.clip(lower=1.0))
    d_vol = _rolling_dfa_series(lv, _TD_QTR, [4, 8, 16])
    return d_close - d_vol


def fct_ext_016_dfa_alpha_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21d DFA alpha within its 252-day rolling distribution."""
    lr = np.log(close / close.shift(1))
    a21 = lr.rolling(_TD_MON, min_periods=_TD_MON // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8]), raw=True
    )
    m = _rolling_mean(a21, _TD_YEAR)
    s = _rolling_std(a21, _TD_YEAR)
    return _safe_div(a21 - m, s)


def fct_ext_017_dfa_alpha_126d_zscore_hist(close: pd.Series) -> pd.Series:
    """Expanding z-score of 126d DFA alpha across all history."""
    lr = np.log(close / close.shift(1))
    a126 = lr.rolling(_TD_HALF, min_periods=_TD_HALF // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16, 32]), raw=True
    )
    m = a126.expanding(min_periods=_TD_HALF).mean()
    s = a126.expanding(min_periods=_TD_HALF).std()
    return _safe_div(a126 - m, s)


def fct_ext_018_dfa_alpha_42d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 42d DFA alpha within trailing 252-day distribution."""
    lr = np.log(close / close.shift(1))
    a42 = lr.rolling(42, min_periods=21).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8]), raw=True
    )
    return a42.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_019_dfa_alpha_logvol_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of volume DFA alpha (63d) within trailing 252d distribution."""
    lv = np.log(volume.clip(lower=1.0))
    d = _rolling_dfa_series(lv, _TD_QTR, [4, 8, 16])
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_020_dfa_alpha_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d DFA alpha over trailing 252 days."""
    lr = np.log(close / close.shift(1))
    a = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    return _rolling_min(a, _TD_YEAR)


# --- Group C (021-030): Higuchi FD — additional windows and series ---

def fct_ext_021_higuchi_fd_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Higuchi FD of log-volume series over 63 days (volume path roughness)."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_higuchi_raw(lv, _TD_QTR)


def fct_ext_022_higuchi_fd_logvol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Higuchi FD of log-volume series over 21 days."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_higuchi_raw(lv, _TD_MON)


def fct_ext_023_higuchi_fd_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Higuchi FD of log(H-L range) series over 63 days."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_higuchi_raw(hl, _TD_QTR)


def fct_ext_024_higuchi_fd_close_vol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close Higuchi FD minus volume Higuchi FD over 63d."""
    lp = np.log(close.clip(lower=_EPS))
    lv = np.log(volume.clip(lower=1.0))
    hc = _rolling_higuchi_raw(lp, _TD_QTR)
    hv = _rolling_higuchi_raw(lv, _TD_QTR)
    return hc - hv


def fct_ext_025_higuchi_fd_252d_zscore_hist(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252d Higuchi FD across all history."""
    lp = np.log(close.clip(lower=_EPS))
    h252 = _rolling_higuchi_raw(lp, _TD_YEAR)
    m = h252.expanding(min_periods=_TD_HALF).mean()
    s = h252.expanding(min_periods=_TD_HALF).std()
    return _safe_div(h252 - m, s)


def fct_ext_026_higuchi_fd_63d_min_252d(close: pd.Series) -> pd.Series:
    """Minimum 63d Higuchi FD over trailing 252 days."""
    lp = np.log(close.clip(lower=_EPS))
    h = _rolling_higuchi_raw(lp, _TD_QTR)
    return _rolling_min(h, _TD_YEAR)


def fct_ext_027_higuchi_fd_63d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum 63d Higuchi FD over trailing 252 days."""
    lp = np.log(close.clip(lower=_EPS))
    h = _rolling_higuchi_raw(lp, _TD_QTR)
    return _rolling_max(h, _TD_YEAR)


def fct_ext_028_higuchi_fd_logvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of volume Higuchi FD (63d) within trailing 252d distribution."""
    lv = np.log(volume.clip(lower=1.0))
    h = _rolling_higuchi_raw(lv, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_029_higuchi_fd_hlrange_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of H-L range Higuchi FD (63d) within trailing 252d distribution."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    h = _rolling_higuchi_raw(hl, _TD_QTR)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_030_higuchi_fd_189d(close: pd.Series) -> pd.Series:
    """Higuchi FD of log-price over trailing 189-day window."""
    lp = np.log(close.clip(lower=_EPS))
    return _rolling_higuchi_raw(lp, 189)


# --- Group D (031-040): Katz FD — additional series and windows ---

def fct_ext_031_katz_fd_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Katz FD of log-volume series over 63 days."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_katz_raw(lv, _TD_QTR)


def fct_ext_032_katz_fd_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Katz FD of log(H-L range) over 63 days."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_katz_raw(hl, _TD_QTR)


def fct_ext_033_katz_fd_close_vol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close Katz FD minus volume Katz FD over 63d."""
    lp = np.log(close.clip(lower=_EPS))
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_katz_raw(lp, _TD_QTR) - _rolling_katz_raw(lv, _TD_QTR)


def fct_ext_034_katz_fd_189d(close: pd.Series) -> pd.Series:
    """Katz FD of log-price over trailing 189-day window."""
    lp = np.log(close.clip(lower=_EPS))
    return _rolling_katz_raw(lp, 189)


def fct_ext_035_katz_fd_logvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of volume Katz FD (63d) within trailing 252d distribution."""
    lv = np.log(volume.clip(lower=1.0))
    k = _rolling_katz_raw(lv, _TD_QTR)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_036_katz_fd_252d_zscore_hist(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252d Katz FD across all history."""
    lp = np.log(close.clip(lower=_EPS))
    k252 = _rolling_katz_raw(lp, _TD_YEAR)
    m = k252.expanding(min_periods=_TD_HALF).mean()
    s = k252.expanding(min_periods=_TD_HALF).std()
    return _safe_div(k252 - m, s)


def fct_ext_037_katz_fd_hlrange_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Katz FD of log(H-L range) over 21 days."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_katz_raw(hl, _TD_MON)


def fct_ext_038_katz_fd_wclose_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Katz FD of log weighted-close (H+L+2C)/4 over 63 days."""
    wc = np.log(((high + low + 2.0 * close) / 4.0).clip(lower=_EPS))
    return _rolling_katz_raw(wc, _TD_QTR)


def fct_ext_039_katz_fd_close_hlrange_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Spread: close Katz FD minus H-L range Katz FD over 63d."""
    lp = np.log(close.clip(lower=_EPS))
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_katz_raw(lp, _TD_QTR) - _rolling_katz_raw(hl, _TD_QTR)


def fct_ext_040_katz_fd_63d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63d Katz FD across all history."""
    lp = np.log(close.clip(lower=_EPS))
    k = _rolling_katz_raw(lp, _TD_QTR)
    return k.expanding(min_periods=_TD_HALF).min()


# --- Group E (041-050): Higher-order autocorrelation lags ---

def fct_ext_041_autocorr_lag2_63d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of log-returns over trailing 63 days."""
    return _rolling_autocorr_lagk(close, _TD_QTR, 2)


def fct_ext_042_autocorr_lag3_63d(close: pd.Series) -> pd.Series:
    """Lag-3 autocorrelation of log-returns over trailing 63 days."""
    return _rolling_autocorr_lagk(close, _TD_QTR, 3)


def fct_ext_043_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of log-returns over trailing 63 days (weekly lag)."""
    return _rolling_autocorr_lagk(close, _TD_QTR, 5)


def fct_ext_044_autocorr_lag2_126d(close: pd.Series) -> pd.Series:
    """Lag-2 autocorrelation of log-returns over trailing 126 days."""
    return _rolling_autocorr_lagk(close, _TD_HALF, 2)


def fct_ext_045_autocorr_lag1_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log-volume changes over trailing 63 days."""
    lv = np.log(volume.clip(lower=1.0))
    return _rolling_autocorr_lagk(lv, _TD_QTR, 1)


def fct_ext_046_autocorr_lag1_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log(H-L range) changes over 63 days."""
    hl = np.log((high - low + _EPS).clip(lower=_EPS))
    return _rolling_autocorr_lagk(hl, _TD_QTR, 1)


def fct_ext_047_autocorr_lag2_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d lag-2 autocorr within trailing 252d distribution."""
    ac = _rolling_autocorr_lagk(close, _TD_QTR, 2)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_048_autocorr_lag5_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d lag-5 autocorr within trailing 252d distribution."""
    ac = _rolling_autocorr_lagk(close, _TD_QTR, 5)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_049_autocorr_composite_lags123_63d(close: pd.Series) -> pd.Series:
    """Average of lag-1, lag-2, lag-3 autocorrelations over 63 days (multi-lag texture)."""
    a1 = _rolling_autocorr_lagk(close, _TD_QTR, 1)
    a2 = _rolling_autocorr_lagk(close, _TD_QTR, 2)
    a3 = _rolling_autocorr_lagk(close, _TD_QTR, 3)
    return (a1 + a2 + a3) / 3.0


def fct_ext_050_autocorr_close_vol_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lag-1 autocorr close minus lag-1 autocorr volume over 63d (divergence)."""
    ac_close = _rolling_autocorr_lagk(close, _TD_QTR, 1)
    lv = np.log(volume.clip(lower=1.0))
    ac_vol = _rolling_autocorr_lagk(lv, _TD_QTR, 1)
    return ac_close - ac_vol


# --- Group F (051-060): Sample entropy on alternative series ---

def fct_ext_051_sampen_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sample entropy of log-volume changes over 63 days (volume regularity)."""
    return _rolling_sampen(np.log(volume.clip(lower=1.0)), _TD_QTR)


def fct_ext_052_sampen_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sample entropy of log(H-L range) changes over 63 days."""
    return _rolling_sampen(np.log((high - low + _EPS).clip(lower=_EPS)), _TD_QTR)


def fct_ext_053_sampen_close_vol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close SampEn minus volume SampEn over 63d."""
    sc = _rolling_sampen(np.log(close.clip(lower=_EPS)), _TD_QTR)
    sv = _rolling_sampen(np.log(volume.clip(lower=1.0)), _TD_QTR)
    return sc - sv


def fct_ext_054_sampen_63d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of 63d SampEn across all history."""
    se = _rolling_sampen(np.log(close.clip(lower=_EPS)), _TD_QTR)
    return se.expanding(min_periods=_TD_HALF).min()


def fct_ext_055_sampen_logvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of volume SampEn (63d) within trailing 252d distribution."""
    sv = _rolling_sampen(np.log(volume.clip(lower=1.0)), _TD_QTR)
    return sv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (056-065): Variance-ratio on alternative series ---

def fct_ext_056_vr5_logvol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Variance ratio VR(5) of log-volume changes over 63 days."""
    return _rolling_vr(np.log(volume.clip(lower=1.0)), _TD_QTR, 5)


def fct_ext_057_vr5_hlrange_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance ratio VR(5) of log(H-L range) changes over 63 days."""
    return _rolling_vr(np.log((high - low + _EPS).clip(lower=_EPS)), _TD_QTR, 5)


def fct_ext_058_vr5_close_vol_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread: close VR(5,63d) minus volume VR(5,63d)."""
    vrc = _rolling_vr(np.log(close.clip(lower=_EPS)), _TD_QTR, 5)
    vrv = _rolling_vr(np.log(volume.clip(lower=1.0)), _TD_QTR, 5)
    return vrc - vrv


def fct_ext_059_vr10_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of VR(10,63d) within trailing 252d distribution."""
    vr = _rolling_vr(np.log(close.clip(lower=_EPS)), _TD_QTR, 10)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_060_vr5_logvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of volume VR(5,63d) within trailing 252d distribution."""
    vrv = _rolling_vr(np.log(volume.clip(lower=1.0)), _TD_QTR, 5)
    return vrv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (061-067): Multi-series fractal composite features ---

def fct_ext_061_fractal_3series_hurst_avg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average R/S Hurst across close, HL-midpoint, and open (=close proxy) over 63d."""
    lr = np.log(close / close.shift(1))
    h_close = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    mid = np.log(((high + low) / 2.0).clip(lower=_EPS))
    h_mid = _rolling_hurst_rs_series(mid, _TD_QTR)
    wc = np.log(((high + low + 2.0 * close) / 4.0).clip(lower=_EPS))
    h_wc = _rolling_hurst_rs_series(wc, _TD_QTR)
    return (h_close + h_mid + h_wc) / 3.0


def fct_ext_062_fractal_hurst_dfa_katz_avg_63d(close: pd.Series) -> pd.Series:
    """Average of (R/S Hurst, DFA alpha, Katz FD normalized) over 63d.
    Provides consensus fractal measure across methods."""
    lr = np.log(close / close.shift(1))
    h_rs = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    dfa = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    lp = np.log(close.clip(lower=_EPS))
    katz = _rolling_katz_raw(lp, _TD_QTR)
    return (h_rs + dfa + (katz / 2.0)) / 3.0


def fct_ext_063_fractal_anti_persist_flag_3methods(close: pd.Series) -> pd.Series:
    """Flag: all three measures agree on anti-persistence: VR5<1, autocorr<0, HurstRS<0.5."""
    lr = np.log(close / close.shift(1))
    h_rs = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    vr5 = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), 5), raw=True
    )
    ac1 = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _autocorr_lagk(np.asarray(x, dtype=float), 1), raw=True
    )
    return ((h_rs < 0.5) & (vr5 < 1.0) & (ac1 < 0.0)).astype(float)


def fct_ext_064_fractal_roughness_4fd_avg_63d(close: pd.Series) -> pd.Series:
    """Average of Higuchi, Katz, Petrosian (0 if unavailable) FD over 63d."""
    lp = np.log(close.clip(lower=_EPS))

    def _petrosian(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 4:
            return np.nan
        delta = np.diff(x)
        sign_changes = np.sum(np.diff(np.sign(delta)) != 0)
        denom = np.log10(n) + np.log10(n / (n + 0.4 * sign_changes + _EPS))
        if abs(denom) < _EPS:
            return np.nan
        return float(np.log10(n) / denom)

    hig = _rolling_higuchi_raw(lp, _TD_QTR)
    katz = _rolling_katz_raw(lp, _TD_QTR)
    petro = lp.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _petrosian(np.asarray(x, dtype=float)), raw=True
    )
    return (hig + katz + petro) / 3.0


def fct_ext_065_fractal_texture_zscore_composite_63d(close: pd.Series) -> pd.Series:
    """Z-score composite: sum of z-scores of (Higuchi FD, Katz FD, VR5) over 63d
    each z-scored against its own 252d rolling distribution.  Higher = rougher/anti-pers."""
    lp = np.log(close.clip(lower=_EPS))
    hig = _rolling_higuchi_raw(lp, _TD_QTR)
    katz = _rolling_katz_raw(lp, _TD_QTR)
    lr = np.log(close / close.shift(1))
    vr5 = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), 5), raw=True
    )
    for feat in [hig, katz, vr5]:
        m = _rolling_mean(feat, _TD_YEAR)
        s = _rolling_std(feat, _TD_YEAR)
    # re-compute individually to avoid overwrite
    hig_z = _safe_div(hig - _rolling_mean(hig, _TD_YEAR), _rolling_std(hig, _TD_YEAR))
    katz_z = _safe_div(katz - _rolling_mean(katz, _TD_YEAR), _rolling_std(katz, _TD_YEAR))
    vr5_z = _safe_div(vr5 - _rolling_mean(vr5, _TD_YEAR), _rolling_std(vr5, _TD_YEAR))
    return hig_z + katz_z + vr5_z


# --- Group I (066-075): Additional Hurst/DFA window combos and regime flags ---

def fct_ext_066_hurst_rs_5d(close: pd.Series) -> pd.Series:
    """R/S Hurst of log-returns over trailing 5-day window (ultra-short fractal texture)."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(_TD_WEEK, min_periods=_TD_WEEK // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )


def fct_ext_067_hurst_rs_10d(close: pd.Series) -> pd.Series:
    """R/S Hurst of log-returns over trailing 10-day window (2-week)."""
    lr = np.log(close / close.shift(1))
    return lr.rolling(10, min_periods=5).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )


def fct_ext_068_hurst_rs_63d_consec_above05(close: pd.Series) -> pd.Series:
    """Consecutive days 63d R/S Hurst has been above 0.5 (trending fractal streak)."""
    lr = np.log(close / close.shift(1))
    h = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    cond = h > 0.5
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def fct_ext_069_dfa_alpha_63d_consec_above05(close: pd.Series) -> pd.Series:
    """Consecutive days 63d DFA alpha has been above 0.5 (super-diffusive streak)."""
    lr = np.log(close / close.shift(1))
    a = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    cond = a > 0.5
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def fct_ext_070_hurst_rs_63d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 63d R/S Hurst across all history."""
    lr = np.log(close / close.shift(1))
    h = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    m = h.expanding(min_periods=_TD_HALF).mean()
    s = h.expanding(min_periods=_TD_HALF).std()
    return _safe_div(h - m, s)


def fct_ext_071_fractal_hurst_regime_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d R/S Hurst in its 252d distribution; <0.5 = anti-pers regime."""
    lr = np.log(close / close.shift(1))
    h = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_072_roughness_hl_range_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Roughness proxy: std-dev of (H-L)/close over trailing 126 days."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_std(hl_range, _TD_HALF)


def fct_ext_073_roughness_hl_range_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d (H-L)/close roughness within trailing 252d distribution."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    r63 = _rolling_std(hl_range, _TD_QTR)
    return r63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fct_ext_074_fractal_anti_pers_score_4methods_63d(close: pd.Series) -> pd.Series:
    """Anti-persistence score 0-4: count of (HurstRS<0.5, DFA<0.5, VR5<1, autocorr<0) over 63d."""
    lr = np.log(close / close.shift(1))
    h_rs = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    dfa = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    vr5 = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), 5), raw=True
    )
    ac1 = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _autocorr_lagk(np.asarray(x, dtype=float), 1), raw=True
    )
    return (
        (h_rs < 0.5).astype(float)
        + (dfa < 0.5).astype(float)
        + (vr5 < 1.0).astype(float)
        + (ac1 < 0.0).astype(float)
    )


def fct_ext_075_fractal_capitulation_texture_index(close: pd.Series) -> pd.Series:
    """Capitulation texture index: depth of 63d R/S Hurst below 0.5 plus depth of DFA below 0.5,
    normalized by their 252d rolling stds.  Higher = more anti-persistent / mean-reverting texture."""
    lr = np.log(close / close.shift(1))
    h = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )
    dfa = lr.rolling(_TD_QTR, min_periods=_TD_QTR // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), [4, 8, 16]), raw=True
    )
    h_depth = (0.5 - h).clip(lower=0.0)
    dfa_depth = (0.5 - dfa).clip(lower=0.0)
    h_s = _rolling_std(h, _TD_YEAR).clip(lower=_EPS)
    dfa_s = _rolling_std(dfa, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(h_depth, h_s) + _safe_div(dfa_depth, dfa_s)


# ── Registry ──────────────────────────────────────────────────────────────────

FRACTAL_STRUCTURE_EXTENDED_REGISTRY_001_075 = {
    "fct_ext_001_hurst_rs_hlmid_63d":               {"inputs": ["close", "high", "low"], "func": fct_ext_001_hurst_rs_hlmid_63d},
    "fct_ext_002_hurst_rs_wclose_63d":              {"inputs": ["close", "high", "low"], "func": fct_ext_002_hurst_rs_wclose_63d},
    "fct_ext_003_hurst_rs_open_63d":                {"inputs": ["close", "open"], "func": fct_ext_003_hurst_rs_open_63d},
    "fct_ext_004_hurst_rs_logvol_63d":              {"inputs": ["close", "volume"], "func": fct_ext_004_hurst_rs_logvol_63d},
    "fct_ext_005_hurst_rs_logvol_126d":             {"inputs": ["close", "volume"], "func": fct_ext_005_hurst_rs_logvol_126d},
    "fct_ext_006_hurst_rs_close_logvol_spread_63d": {"inputs": ["close", "volume"], "func": fct_ext_006_hurst_rs_close_logvol_spread_63d},
    "fct_ext_007_hurst_rs_hlmid_126d":              {"inputs": ["close", "high", "low"], "func": fct_ext_007_hurst_rs_hlmid_126d},
    "fct_ext_008_hurst_rs_hlmid_252d":              {"inputs": ["close", "high", "low"], "func": fct_ext_008_hurst_rs_hlmid_252d},
    "fct_ext_009_hurst_rs_close_hlmid_spread_63d":  {"inputs": ["close", "high", "low"], "func": fct_ext_009_hurst_rs_close_hlmid_spread_63d},
    "fct_ext_010_hurst_rs_wclose_pct_rank_252d":    {"inputs": ["close", "high", "low"], "func": fct_ext_010_hurst_rs_wclose_pct_rank_252d},
    "fct_ext_011_dfa_alpha_21d":                    {"inputs": ["close"], "func": fct_ext_011_dfa_alpha_21d},
    "fct_ext_012_dfa_alpha_189d":                   {"inputs": ["close"], "func": fct_ext_012_dfa_alpha_189d},
    "fct_ext_013_dfa_alpha_logvol_63d":             {"inputs": ["close", "volume"], "func": fct_ext_013_dfa_alpha_logvol_63d},
    "fct_ext_014_dfa_alpha_hlrange_63d":            {"inputs": ["close", "high", "low"], "func": fct_ext_014_dfa_alpha_hlrange_63d},
    "fct_ext_015_dfa_close_vol_spread_63d":         {"inputs": ["close", "volume"], "func": fct_ext_015_dfa_close_vol_spread_63d},
    "fct_ext_016_dfa_alpha_21d_zscore_252d":        {"inputs": ["close"], "func": fct_ext_016_dfa_alpha_21d_zscore_252d},
    "fct_ext_017_dfa_alpha_126d_zscore_hist":       {"inputs": ["close"], "func": fct_ext_017_dfa_alpha_126d_zscore_hist},
    "fct_ext_018_dfa_alpha_42d_pct_rank_252d":      {"inputs": ["close"], "func": fct_ext_018_dfa_alpha_42d_pct_rank_252d},
    "fct_ext_019_dfa_alpha_logvol_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": fct_ext_019_dfa_alpha_logvol_63d_pct_rank_252d},
    "fct_ext_020_dfa_alpha_63d_min_252d":           {"inputs": ["close"], "func": fct_ext_020_dfa_alpha_63d_min_252d},
    "fct_ext_021_higuchi_fd_logvol_63d":            {"inputs": ["close", "volume"], "func": fct_ext_021_higuchi_fd_logvol_63d},
    "fct_ext_022_higuchi_fd_logvol_21d":            {"inputs": ["close", "volume"], "func": fct_ext_022_higuchi_fd_logvol_21d},
    "fct_ext_023_higuchi_fd_hlrange_63d":           {"inputs": ["close", "high", "low"], "func": fct_ext_023_higuchi_fd_hlrange_63d},
    "fct_ext_024_higuchi_fd_close_vol_spread_63d":  {"inputs": ["close", "volume"], "func": fct_ext_024_higuchi_fd_close_vol_spread_63d},
    "fct_ext_025_higuchi_fd_252d_zscore_hist":      {"inputs": ["close"], "func": fct_ext_025_higuchi_fd_252d_zscore_hist},
    "fct_ext_026_higuchi_fd_63d_min_252d":          {"inputs": ["close"], "func": fct_ext_026_higuchi_fd_63d_min_252d},
    "fct_ext_027_higuchi_fd_63d_max_252d":          {"inputs": ["close"], "func": fct_ext_027_higuchi_fd_63d_max_252d},
    "fct_ext_028_higuchi_fd_logvol_pct_rank_252d":  {"inputs": ["close", "volume"], "func": fct_ext_028_higuchi_fd_logvol_pct_rank_252d},
    "fct_ext_029_higuchi_fd_hlrange_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": fct_ext_029_higuchi_fd_hlrange_pct_rank_252d},
    "fct_ext_030_higuchi_fd_189d":                  {"inputs": ["close"], "func": fct_ext_030_higuchi_fd_189d},
    "fct_ext_031_katz_fd_logvol_63d":               {"inputs": ["close", "volume"], "func": fct_ext_031_katz_fd_logvol_63d},
    "fct_ext_032_katz_fd_hlrange_63d":              {"inputs": ["close", "high", "low"], "func": fct_ext_032_katz_fd_hlrange_63d},
    "fct_ext_033_katz_fd_close_vol_spread_63d":     {"inputs": ["close", "volume"], "func": fct_ext_033_katz_fd_close_vol_spread_63d},
    "fct_ext_034_katz_fd_189d":                     {"inputs": ["close"], "func": fct_ext_034_katz_fd_189d},
    "fct_ext_035_katz_fd_logvol_pct_rank_252d":     {"inputs": ["close", "volume"], "func": fct_ext_035_katz_fd_logvol_pct_rank_252d},
    "fct_ext_036_katz_fd_252d_zscore_hist":         {"inputs": ["close"], "func": fct_ext_036_katz_fd_252d_zscore_hist},
    "fct_ext_037_katz_fd_hlrange_21d":              {"inputs": ["close", "high", "low"], "func": fct_ext_037_katz_fd_hlrange_21d},
    "fct_ext_038_katz_fd_wclose_63d":               {"inputs": ["close", "high", "low"], "func": fct_ext_038_katz_fd_wclose_63d},
    "fct_ext_039_katz_fd_close_hlrange_spread_63d": {"inputs": ["close", "high", "low"], "func": fct_ext_039_katz_fd_close_hlrange_spread_63d},
    "fct_ext_040_katz_fd_63d_expanding_min":        {"inputs": ["close"], "func": fct_ext_040_katz_fd_63d_expanding_min},
    "fct_ext_041_autocorr_lag2_63d":                {"inputs": ["close"], "func": fct_ext_041_autocorr_lag2_63d},
    "fct_ext_042_autocorr_lag3_63d":                {"inputs": ["close"], "func": fct_ext_042_autocorr_lag3_63d},
    "fct_ext_043_autocorr_lag5_63d":                {"inputs": ["close"], "func": fct_ext_043_autocorr_lag5_63d},
    "fct_ext_044_autocorr_lag2_126d":               {"inputs": ["close"], "func": fct_ext_044_autocorr_lag2_126d},
    "fct_ext_045_autocorr_lag1_logvol_63d":         {"inputs": ["close", "volume"], "func": fct_ext_045_autocorr_lag1_logvol_63d},
    "fct_ext_046_autocorr_lag1_hlrange_63d":        {"inputs": ["close", "high", "low"], "func": fct_ext_046_autocorr_lag1_hlrange_63d},
    "fct_ext_047_autocorr_lag2_63d_pct_rank_252d":  {"inputs": ["close"], "func": fct_ext_047_autocorr_lag2_63d_pct_rank_252d},
    "fct_ext_048_autocorr_lag5_63d_pct_rank_252d":  {"inputs": ["close"], "func": fct_ext_048_autocorr_lag5_63d_pct_rank_252d},
    "fct_ext_049_autocorr_composite_lags123_63d":   {"inputs": ["close"], "func": fct_ext_049_autocorr_composite_lags123_63d},
    "fct_ext_050_autocorr_close_vol_divergence_63d": {"inputs": ["close", "volume"], "func": fct_ext_050_autocorr_close_vol_divergence_63d},
    "fct_ext_051_sampen_logvol_63d":                {"inputs": ["close", "volume"], "func": fct_ext_051_sampen_logvol_63d},
    "fct_ext_052_sampen_hlrange_63d":               {"inputs": ["close", "high", "low"], "func": fct_ext_052_sampen_hlrange_63d},
    "fct_ext_053_sampen_close_vol_spread_63d":      {"inputs": ["close", "volume"], "func": fct_ext_053_sampen_close_vol_spread_63d},
    "fct_ext_054_sampen_63d_expanding_min":         {"inputs": ["close"], "func": fct_ext_054_sampen_63d_expanding_min},
    "fct_ext_055_sampen_logvol_pct_rank_252d":      {"inputs": ["close", "volume"], "func": fct_ext_055_sampen_logvol_pct_rank_252d},
    "fct_ext_056_vr5_logvol_63d":                   {"inputs": ["close", "volume"], "func": fct_ext_056_vr5_logvol_63d},
    "fct_ext_057_vr5_hlrange_63d":                  {"inputs": ["close", "high", "low"], "func": fct_ext_057_vr5_hlrange_63d},
    "fct_ext_058_vr5_close_vol_spread_63d":         {"inputs": ["close", "volume"], "func": fct_ext_058_vr5_close_vol_spread_63d},
    "fct_ext_059_vr10_63d_pct_rank_252d":           {"inputs": ["close"], "func": fct_ext_059_vr10_63d_pct_rank_252d},
    "fct_ext_060_vr5_logvol_pct_rank_252d":         {"inputs": ["close", "volume"], "func": fct_ext_060_vr5_logvol_pct_rank_252d},
    "fct_ext_061_fractal_3series_hurst_avg_63d":    {"inputs": ["close", "high", "low"], "func": fct_ext_061_fractal_3series_hurst_avg_63d},
    "fct_ext_062_fractal_hurst_dfa_katz_avg_63d":   {"inputs": ["close"], "func": fct_ext_062_fractal_hurst_dfa_katz_avg_63d},
    "fct_ext_063_fractal_anti_persist_flag_3methods": {"inputs": ["close"], "func": fct_ext_063_fractal_anti_persist_flag_3methods},
    "fct_ext_064_fractal_roughness_4fd_avg_63d":    {"inputs": ["close"], "func": fct_ext_064_fractal_roughness_4fd_avg_63d},
    "fct_ext_065_fractal_texture_zscore_composite_63d": {"inputs": ["close"], "func": fct_ext_065_fractal_texture_zscore_composite_63d},
    "fct_ext_066_hurst_rs_5d":                      {"inputs": ["close"], "func": fct_ext_066_hurst_rs_5d},
    "fct_ext_067_hurst_rs_10d":                     {"inputs": ["close"], "func": fct_ext_067_hurst_rs_10d},
    "fct_ext_068_hurst_rs_63d_consec_above05":      {"inputs": ["close"], "func": fct_ext_068_hurst_rs_63d_consec_above05},
    "fct_ext_069_dfa_alpha_63d_consec_above05":     {"inputs": ["close"], "func": fct_ext_069_dfa_alpha_63d_consec_above05},
    "fct_ext_070_hurst_rs_63d_expanding_zscore":    {"inputs": ["close"], "func": fct_ext_070_hurst_rs_63d_expanding_zscore},
    "fct_ext_071_fractal_hurst_regime_pct_rank_252d": {"inputs": ["close"], "func": fct_ext_071_fractal_hurst_regime_pct_rank_252d},
    "fct_ext_072_roughness_hl_range_126d":          {"inputs": ["close", "high", "low"], "func": fct_ext_072_roughness_hl_range_126d},
    "fct_ext_073_roughness_hl_range_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": fct_ext_073_roughness_hl_range_pct_rank_252d},
    "fct_ext_074_fractal_anti_pers_score_4methods_63d": {"inputs": ["close"], "func": fct_ext_074_fractal_anti_pers_score_4methods_63d},
    "fct_ext_075_fractal_capitulation_texture_index": {"inputs": ["close"], "func": fct_ext_075_fractal_capitulation_texture_index},
}
