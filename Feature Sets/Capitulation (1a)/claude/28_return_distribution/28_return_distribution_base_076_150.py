"""
28_return_distribution — Base Features 076-150
Domain: shape of the trailing return distribution — multi-day return moments, intraday
        return distribution, range-based tail measures, quantile spreads, interquantile
        ranges, cross-window comparisons, Hurst exponent (R/S + DFA-style),
        Shannon entropy of binned returns, permutation entropy of return series.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _pct_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Hurst scalar helpers (R/S analysis) ─────────────────────────────────────

def _hurst_rs_scalar(arr: np.ndarray) -> float:
    """Hurst exponent via rescaled range (R/S) analysis on a raw returns array.
    Values <0.5 = mean-reverting; >0.5 = trending; =0.5 = random walk.
    Uses the single-interval R/S estimator: H = log(R/S) / log(n).
    """
    n = len(arr)
    if n < 8:
        return np.nan
    # Remove NaN
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
    rs = r / s
    return np.log(rs) / np.log(n)


def _hurst_dfa_scalar(arr: np.ndarray) -> float:
    """Lightweight DFA-style Hurst estimate: slope of log(F) vs log(scale)
    using two sub-window sizes (n//4 and n//2).
    """
    n = len(arr)
    if n < 16:
        return np.nan
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < 16:
        return np.nan
    profile = np.cumsum(a - a.mean())

    def _rms_fluctuation(profile, scale):
        nblocks = len(profile) // scale
        if nblocks < 2:
            return np.nan
        flucts = []
        for i in range(nblocks):
            seg = profile[i * scale:(i + 1) * scale]
            x = np.arange(scale, dtype=float)
            # detrend: OLS residuals
            xm = x.mean()
            ym = seg.mean()
            denom = ((x - xm) ** 2).sum()
            if denom < _EPS:
                flucts.append(seg.std())
                continue
            slope = ((x - xm) * (seg - ym)).sum() / denom
            trend = xm * slope + (ym - xm * slope) + slope * x
            # recompute: intercept = ym - slope*xm
            intercept = ym - slope * xm
            trend2 = intercept + slope * x
            residuals = seg - trend2
            flucts.append(np.sqrt((residuals ** 2).mean()))
        if len(flucts) == 0:
            return np.nan
        return np.mean(flucts)

    s1 = max(4, n // 4)
    s2 = max(8, n // 2)
    f1 = _rms_fluctuation(profile, s1)
    f2 = _rms_fluctuation(profile, s2)
    if f1 is None or f2 is None or np.isnan(f1) or np.isnan(f2):
        return np.nan
    if f1 < _EPS or f2 < _EPS:
        return np.nan
    return np.log(f2 / f1) / np.log(s2 / s1)


# ── Shannon entropy scalar helpers ───────────────────────────────────────────

def _shannon_entropy_scalar(arr: np.ndarray, n_bins: int) -> float:
    """Shannon entropy of binned returns (base-2 bits)."""
    a = arr[~np.isnan(arr)]
    if len(a) < n_bins:
        return np.nan
    mn, mx = a.min(), a.max()
    if mx - mn < _EPS:
        return 0.0
    bins = np.linspace(mn, mx, n_bins + 1)
    counts, _ = np.histogram(a, bins=bins)
    total = counts.sum()
    if total == 0:
        return np.nan
    probs = counts / total
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log2(probs)))


def _make_shannon_helper(n_bins: int):
    def _helper(arr: np.ndarray) -> float:
        return _shannon_entropy_scalar(arr, n_bins)
    return _helper


_shannon_8bins = _make_shannon_helper(8)
_shannon_16bins = _make_shannon_helper(16)


# ── Permutation entropy scalar helper ────────────────────────────────────────

def _perm_entropy_scalar(arr: np.ndarray, order: int = 3) -> float:
    """Permutation entropy of order `order` (disorder of ordinal patterns).
    Normalized to [0,1]: 1 = maximally disordered (random); 0 = perfectly ordered.
    """
    a = arr[~np.isnan(arr)]
    n = len(a)
    if n < order + 2:
        return np.nan
    from math import factorial
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


def _perm_entropy_order3(arr: np.ndarray) -> float:
    return _perm_entropy_scalar(arr, order=3)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Multi-day return distribution shape ---

def rds_076_skew_5d_ret_63d(close: pd.Series) -> pd.Series:
    """63-day rolling skewness of non-overlapping 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_skew(r5, _TD_QTR)


def rds_077_skew_5d_ret_252d(close: pd.Series) -> pd.Series:
    """252-day rolling skewness of 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_skew(r5, _TD_YEAR)


def rds_078_kurt_5d_ret_63d(close: pd.Series) -> pd.Series:
    """63-day rolling excess kurtosis of 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_kurt(r5, _TD_QTR)


def rds_079_kurt_5d_ret_252d(close: pd.Series) -> pd.Series:
    """252-day rolling excess kurtosis of 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_kurt(r5, _TD_YEAR)


def rds_080_skew_21d_ret_252d(close: pd.Series) -> pd.Series:
    """252-day rolling skewness of 21-day log-returns (monthly return shape)."""
    r21 = np.log(close.clip(lower=_EPS)).diff(21)
    return _rolling_skew(r21, _TD_YEAR)


def rds_081_kurt_21d_ret_252d(close: pd.Series) -> pd.Series:
    """252-day rolling kurtosis of 21-day log-returns."""
    r21 = np.log(close.clip(lower=_EPS)).diff(21)
    return _rolling_kurt(r21, _TD_YEAR)


def rds_082_var_5pct_5d_ret_63d(close: pd.Series) -> pd.Series:
    """63-day 5% VaR of 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_quantile(r5, _TD_QTR, 0.05)


def rds_083_cvar_5pct_5d_ret_63d(close: pd.Series) -> pd.Series:
    """63-day CVaR-5% of 5-day log-returns."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    q05 = _rolling_quantile(r5, _TD_QTR, 0.05)
    tail = r5.where(r5 < q05, np.nan)
    return tail.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()


def rds_084_skew_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day 5-day-return skewness within its 252-day distribution."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    sk = _rolling_skew(r5, _TD_QTR)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_085_5d_ret_mean_minus_median_63d(close: pd.Series) -> pd.Series:
    """63-day mean minus median of 5-day log-returns (location skew proxy)."""
    r5 = np.log(close.clip(lower=_EPS)).diff(5)
    return _rolling_mean(r5, _TD_QTR) - _rolling_median(r5, _TD_QTR)


# --- Group I (086-095): Intraday return distribution (open-to-close, intraday range) ---

def rds_086_skew_oc_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day skewness of open-to-close daily returns."""
    oc = _safe_div(close - open, open)
    return _rolling_skew(oc, _TD_QTR)


def rds_087_kurt_oc_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day kurtosis of open-to-close daily returns."""
    oc = _safe_div(close - open, open)
    return _rolling_kurt(oc, _TD_QTR)


def rds_088_var_5pct_oc_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day 5% VaR of open-to-close daily returns."""
    oc = _safe_div(close - open, open)
    return _rolling_quantile(oc, _TD_QTR, 0.05)


def rds_089_skew_oc_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day skewness of open-to-close daily returns."""
    oc = _safe_div(close - open, open)
    return _rolling_skew(oc, _TD_MON)


def rds_090_kurt_oc_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day kurtosis of open-to-close daily returns."""
    oc = _safe_div(close - open, open)
    return _rolling_kurt(oc, _TD_MON)


def rds_091_skew_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day skewness of daily high-low range normalized by prior close."""
    rng = _safe_div(high - low, close.shift(1))
    return _rolling_skew(rng, _TD_QTR)


def rds_092_kurt_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day kurtosis of daily high-low range (fat-tailed volatility days)."""
    rng = _safe_div(high - low, close.shift(1))
    return _rolling_kurt(rng, _TD_QTR)


def rds_093_var_5pct_hl_range_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day 5th-percentile of high-low range (low end of range distribution)."""
    rng = _safe_div(high - low, close.shift(1))
    return _rolling_quantile(rng, _TD_QTR, 0.05)


def rds_094_oc_skew_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 63-day open-to-close skewness in 252-day distribution."""
    oc = _safe_div(close - open, open)
    sk = _rolling_skew(oc, _TD_QTR)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_095_hl_range_kurt_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63-day high-low range kurtosis in 252-day distribution."""
    rng = _safe_div(high - low, close.shift(1))
    kt = _rolling_kurt(rng, _TD_QTR)
    return kt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group J (096-105): Interquantile range and quantile spread measures ---

def rds_096_iqr_25_75_logret_21d(close: pd.Series) -> pd.Series:
    """21-day interquartile range (75th - 25th pct) of daily log-returns."""
    r = _log_ret(close)
    q75 = _rolling_quantile(r, _TD_MON, 0.75)
    q25 = _rolling_quantile(r, _TD_MON, 0.25)
    return q75 - q25


def rds_097_iqr_25_75_logret_63d(close: pd.Series) -> pd.Series:
    """63-day interquartile range of daily log-returns."""
    r = _log_ret(close)
    q75 = _rolling_quantile(r, _TD_QTR, 0.75)
    q25 = _rolling_quantile(r, _TD_QTR, 0.25)
    return q75 - q25


def rds_098_iqr_10_90_logret_63d(close: pd.Series) -> pd.Series:
    """63-day 10-90 percentile spread of daily log-returns."""
    r = _log_ret(close)
    q90 = _rolling_quantile(r, _TD_QTR, 0.90)
    q10 = _rolling_quantile(r, _TD_QTR, 0.10)
    return q90 - q10


def rds_099_iqr_5_95_logret_252d(close: pd.Series) -> pd.Series:
    """252-day 5-95 percentile spread of daily log-returns."""
    r = _log_ret(close)
    q95 = _rolling_quantile(r, _TD_YEAR, 0.95)
    q05 = _rolling_quantile(r, _TD_YEAR, 0.05)
    return q95 - q05


def rds_100_left_iqr_share_63d(close: pd.Series) -> pd.Series:
    """63-day share of IQR attributable to the left half (25th to median)."""
    r = _log_ret(close)
    q50 = _rolling_quantile(r, _TD_QTR, 0.50)
    q25 = _rolling_quantile(r, _TD_QTR, 0.25)
    q75 = _rolling_quantile(r, _TD_QTR, 0.75)
    left_half = q50 - q25
    full_iqr = (q75 - q25).replace(0, np.nan)
    return _safe_div(left_half.abs(), full_iqr)


def rds_101_iqr_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day IQR within its 252-day distribution."""
    iqr = rds_096_iqr_25_75_logret_21d(close)
    return iqr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_102_iqr_ratio_21d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day IQR to 252-day IQR (recent dispersion vs long-term)."""
    r = _log_ret(close)
    iqr21 = _rolling_quantile(r, _TD_MON, 0.75) - _rolling_quantile(r, _TD_MON, 0.25)
    iqr252 = _rolling_quantile(r, _TD_YEAR, 0.75) - _rolling_quantile(r, _TD_YEAR, 0.25)
    return _safe_div(iqr21, iqr252)


def rds_103_q10_logret_21d(close: pd.Series) -> pd.Series:
    """21-day 10th-percentile of daily log-returns."""
    return _rolling_quantile(_log_ret(close), _TD_MON, 0.10)


def rds_104_q90_logret_21d(close: pd.Series) -> pd.Series:
    """21-day 90th-percentile of daily log-returns."""
    return _rolling_quantile(_log_ret(close), _TD_MON, 0.90)


def rds_105_quantile_asymmetry_63d(close: pd.Series) -> pd.Series:
    """63-day quantile asymmetry: (q75 - q50) - (q50 - q25) of log-returns."""
    r = _log_ret(close)
    q25 = _rolling_quantile(r, _TD_QTR, 0.25)
    q50 = _rolling_quantile(r, _TD_QTR, 0.50)
    q75 = _rolling_quantile(r, _TD_QTR, 0.75)
    return (q75 - q50) - (q50 - q25)


# --- Group K (106-115): Return distribution vs its own history (cross-window) ---

def rds_106_skew_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day skewness to 252-day skewness (recent vs long-term shape)."""
    r = _log_ret(close)
    sk21 = _rolling_skew(r, _TD_MON)
    sk252 = _rolling_skew(r, _TD_YEAR)
    return _safe_div(sk21, sk252)


def rds_107_kurt_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day kurtosis to 252-day kurtosis."""
    r = _log_ret(close)
    kt21 = _rolling_kurt(r, _TD_MON)
    kt252 = _rolling_kurt(r, _TD_YEAR)
    return _safe_div(kt21, kt252)


def rds_108_var5pct_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day VaR-5% to 252-day VaR-5% (recent tail vs long-term)."""
    r = _log_ret(close)
    v21 = _rolling_quantile(r, _TD_MON, 0.05)
    v252 = _rolling_quantile(r, _TD_YEAR, 0.05)
    return _safe_div(v21, v252)


def rds_109_skew_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day skewness to 252-day skewness."""
    r = _log_ret(close)
    sk63 = _rolling_skew(r, _TD_QTR)
    sk252 = _rolling_skew(r, _TD_YEAR)
    return _safe_div(sk63, sk252)


def rds_110_downstd_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day downside std to 252-day downside std."""
    r = _log_ret(close)
    ds21 = r.where(r < 0, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    ds252 = r.where(r < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    return _safe_div(ds21, ds252)


def rds_111_iqr_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day IQR to 63-day IQR."""
    r = _log_ret(close)
    iqr21 = _rolling_quantile(r, _TD_MON, 0.75) - _rolling_quantile(r, _TD_MON, 0.25)
    iqr63 = _rolling_quantile(r, _TD_QTR, 0.75) - _rolling_quantile(r, _TD_QTR, 0.25)
    return _safe_div(iqr21, iqr63)


def rds_112_cvar_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day CVaR-5% to 252-day CVaR-5%."""
    r = _log_ret(close)
    q05_21 = _rolling_quantile(r, _TD_MON, 0.05)
    q05_252 = _rolling_quantile(r, _TD_YEAR, 0.05)
    cv21 = r.where(r < q05_21, np.nan).rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).mean()
    cv252 = r.where(r < q05_252, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(cv21, cv252)


def rds_113_skew_21d_minus_63d(close: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day log-return skewness."""
    r = _log_ret(close)
    return _rolling_skew(r, _TD_MON) - _rolling_skew(r, _TD_QTR)


def rds_114_kurt_21d_minus_63d(close: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day log-return kurtosis."""
    r = _log_ret(close)
    return _rolling_kurt(r, _TD_MON) - _rolling_kurt(r, _TD_QTR)


def rds_115_var5pct_21d_minus_252d(close: pd.Series) -> pd.Series:
    """Difference: 21-day VaR-5% minus 252-day VaR-5% (short vs long tail level)."""
    r = _log_ret(close)
    return _rolling_quantile(r, _TD_MON, 0.05) - _rolling_quantile(r, _TD_YEAR, 0.05)


# --- Group L (116-120): Return distribution shape with volume conditioning ---

def rds_116_skew_logret_on_highvol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day skewness of log-returns on days with above-median volume."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    high_vol_ret = r.where(volume > avg_vol, np.nan)
    return _rolling_skew(high_vol_ret, _TD_QTR)


def rds_117_kurt_logret_on_highvol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day kurtosis of log-returns on days with above-median volume."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    high_vol_ret = r.where(volume > avg_vol, np.nan)
    return _rolling_kurt(high_vol_ret, _TD_QTR)


def rds_118_skew_logret_on_lowvol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day skewness of log-returns on days with below-median volume."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    low_vol_ret = r.where(volume <= avg_vol, np.nan)
    return _rolling_skew(low_vol_ret, _TD_QTR)


def rds_119_skew_highvol_vs_lowvol_diff_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day difference in skewness: high-volume days minus low-volume days."""
    return (rds_116_skew_logret_on_highvol_days_63d(close, volume)
            - rds_118_skew_logret_on_lowvol_days_63d(close, volume))


def rds_120_cvar5pct_highvol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day CVaR-5% of log-returns on high-volume days only."""
    r = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    hv = r.where(volume > avg_vol, np.nan)
    q05 = hv.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.05)
    tail = hv.where(hv < q05, np.nan)
    return tail.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()


# --- Group M (121-129): Hurst exponent via R/S analysis (mean-reversion vs trending) ---

def rds_121_hurst_rs_63d(close: pd.Series) -> pd.Series:
    """63-day Hurst exponent via R/S analysis. <0.5=mean-reverting, >0.5=trending."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )


def rds_122_hurst_rs_126d(close: pd.Series) -> pd.Series:
    """126-day Hurst exponent via R/S analysis."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(16, _TD_HALF // 2)).apply(
        _hurst_rs_scalar, raw=True
    )


def rds_123_hurst_rs_252d(close: pd.Series) -> pd.Series:
    """252-day Hurst exponent via R/S analysis."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(16, _TD_YEAR // 2)).apply(
        _hurst_rs_scalar, raw=True
    )


def rds_124_hurst_dfa_63d(close: pd.Series) -> pd.Series:
    """63-day Hurst exponent via DFA-style two-scale fluctuation analysis."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _hurst_dfa_scalar, raw=True
    )


def rds_125_hurst_dfa_126d(close: pd.Series) -> pd.Series:
    """126-day Hurst exponent via DFA-style two-scale fluctuation analysis."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(16, _TD_HALF // 2)).apply(
        _hurst_dfa_scalar, raw=True
    )


def rds_126_hurst_dfa_252d(close: pd.Series) -> pd.Series:
    """252-day Hurst exponent via DFA-style two-scale fluctuation analysis."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(16, _TD_YEAR // 2)).apply(
        _hurst_dfa_scalar, raw=True
    )


def rds_127_hurst_rs_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day R/S Hurst in its 252-day distribution."""
    h = rds_121_hurst_rs_63d(close)
    return h.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_128_hurst_mean_reverting_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: 63-day R/S Hurst < 0.45 (strong mean-reversion; capitulation bounce signal)."""
    h = rds_121_hurst_rs_63d(close)
    return (h < 0.45).astype(float)


def rds_129_hurst_rs_minus_dfa_63d(close: pd.Series) -> pd.Series:
    """Difference: 63-day R/S Hurst minus DFA Hurst (estimator divergence)."""
    return rds_121_hurst_rs_63d(close) - rds_124_hurst_dfa_63d(close)


# --- Group N (130-138): Shannon entropy of binned returns ---

def rds_130_shannon_entropy_8bins_63d(close: pd.Series) -> pd.Series:
    """63-day Shannon entropy of log-returns binned into 8 equal-width bins (bits)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(16, _TD_QTR // 2)).apply(
        _shannon_8bins, raw=True
    )


def rds_131_shannon_entropy_8bins_126d(close: pd.Series) -> pd.Series:
    """126-day Shannon entropy of log-returns binned into 8 bins."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(16, _TD_HALF // 2)).apply(
        _shannon_8bins, raw=True
    )


def rds_132_shannon_entropy_8bins_252d(close: pd.Series) -> pd.Series:
    """252-day Shannon entropy of log-returns binned into 8 bins."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(16, _TD_YEAR // 2)).apply(
        _shannon_8bins, raw=True
    )


def rds_133_shannon_entropy_16bins_63d(close: pd.Series) -> pd.Series:
    """63-day Shannon entropy of log-returns binned into 16 equal-width bins."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(20, _TD_QTR // 2)).apply(
        _shannon_16bins, raw=True
    )


def rds_134_shannon_entropy_16bins_126d(close: pd.Series) -> pd.Series:
    """126-day Shannon entropy of log-returns binned into 16 bins."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(20, _TD_HALF // 2)).apply(
        _shannon_16bins, raw=True
    )


def rds_135_shannon_entropy_16bins_252d(close: pd.Series) -> pd.Series:
    """252-day Shannon entropy of log-returns binned into 16 bins."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(20, _TD_YEAR // 2)).apply(
        _shannon_16bins, raw=True
    )


def rds_136_shannon_entropy_8bins_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Shannon entropy (8-bin) in its 252-day distribution."""
    e = rds_130_shannon_entropy_8bins_63d(close)
    return e.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_137_shannon_entropy_low_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: 63-day Shannon entropy (8-bin) below its 252-day 25th percentile (regime concentration)."""
    e = rds_130_shannon_entropy_8bins_63d(close)
    q25 = e.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return (e < q25).astype(float)


def rds_138_shannon_entropy_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day Shannon entropy (8-bin) relative to its 252-day distribution."""
    e = rds_130_shannon_entropy_8bins_63d(close)
    m = _rolling_mean(e, _TD_YEAR)
    s = _rolling_std(e, _TD_YEAR)
    return _safe_div(e - m, s)


# --- Group O (139-141): Permutation entropy (ordinal disorder of return stream) ---

def rds_139_perm_entropy_order3_63d(close: pd.Series) -> pd.Series:
    """63-day normalized permutation entropy (order 3) of log-returns. 1=random, 0=ordered."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _perm_entropy_order3, raw=True
    )


def rds_140_perm_entropy_order3_126d(close: pd.Series) -> pd.Series:
    """126-day normalized permutation entropy (order 3) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(10, _TD_HALF // 2)).apply(
        _perm_entropy_order3, raw=True
    )


def rds_141_perm_entropy_order3_252d(close: pd.Series) -> pd.Series:
    """252-day normalized permutation entropy (order 3) of log-returns."""
    r = _log_ret(close)
    return r.rolling(_TD_YEAR, min_periods=max(10, _TD_YEAR // 2)).apply(
        _perm_entropy_order3, raw=True
    )


# --- Group P (142-150): Additional composite/regime features ---

def rds_142_tail_distress_composite_63d(close: pd.Series) -> pd.Series:
    """63-day composite: (-skew) * (kurtosis + 3) * |VaR-5%| (multi-moment tail score)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    v5 = _rolling_quantile(r, _TD_QTR, 0.05).abs()
    return (-sk) * (kt + 3.0) * v5


def rds_143_tail_distress_composite_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day tail distress composite in trailing 252-day distribution."""
    td = rds_142_tail_distress_composite_63d(close)
    return td.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_144_down_day_ret_skew_63d(close: pd.Series) -> pd.Series:
    """63-day skewness of log-returns on down days only (shape of loss distribution)."""
    r = _log_ret(close)
    down = r.where(r < 0, np.nan)
    return _rolling_skew(down, _TD_QTR)


def rds_145_down_day_ret_kurt_63d(close: pd.Series) -> pd.Series:
    """63-day kurtosis of log-returns on down days only."""
    r = _log_ret(close)
    down = r.where(r < 0, np.nan)
    return _rolling_kurt(down, _TD_QTR)


def rds_146_hurst_rs_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day R/S Hurst relative to its 252-day distribution."""
    h = rds_121_hurst_rs_63d(close)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def rds_147_perm_entropy_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day permutation entropy in its 252-day distribution."""
    e = rds_139_perm_entropy_order3_63d(close)
    return e.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_148_hurst_entropy_composite_63d(close: pd.Series) -> pd.Series:
    """63-day composite: Hurst(RS) * Shannon_entropy_8bins (regime-disorder product)."""
    h = rds_121_hurst_rs_63d(close)
    e = rds_130_shannon_entropy_8bins_63d(close)
    return h * e


def rds_149_var5pct_63d_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63-day VaR-5% (all-history worst-tail level)."""
    v = _rolling_quantile(_log_ret(close), _TD_QTR, 0.05)
    return v.expanding(min_periods=10).rank(pct=True)


def rds_150_full_distress_index_63d(close: pd.Series) -> pd.Series:
    """Full distributional distress index: JB-stat * tail_ratio * down_std (all 63-day)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    jb = (_TD_QTR / 6.0) * (sk ** 2 + (kt ** 2) / 4.0)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    q95 = _rolling_quantile(r, _TD_QTR, 0.95)
    tail_ratio = _safe_div(q05.abs(), q95.abs())
    ds = r.where(r < 0, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    return jb * tail_ratio * ds


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_REGISTRY_076_150 = {
    "rds_076_skew_5d_ret_63d": {"inputs": ["close"], "func": rds_076_skew_5d_ret_63d},
    "rds_077_skew_5d_ret_252d": {"inputs": ["close"], "func": rds_077_skew_5d_ret_252d},
    "rds_078_kurt_5d_ret_63d": {"inputs": ["close"], "func": rds_078_kurt_5d_ret_63d},
    "rds_079_kurt_5d_ret_252d": {"inputs": ["close"], "func": rds_079_kurt_5d_ret_252d},
    "rds_080_skew_21d_ret_252d": {"inputs": ["close"], "func": rds_080_skew_21d_ret_252d},
    "rds_081_kurt_21d_ret_252d": {"inputs": ["close"], "func": rds_081_kurt_21d_ret_252d},
    "rds_082_var_5pct_5d_ret_63d": {"inputs": ["close"], "func": rds_082_var_5pct_5d_ret_63d},
    "rds_083_cvar_5pct_5d_ret_63d": {"inputs": ["close"], "func": rds_083_cvar_5pct_5d_ret_63d},
    "rds_084_skew_5d_pct_rank_252d": {"inputs": ["close"], "func": rds_084_skew_5d_pct_rank_252d},
    "rds_085_5d_ret_mean_minus_median_63d": {"inputs": ["close"], "func": rds_085_5d_ret_mean_minus_median_63d},
    "rds_086_skew_oc_ret_63d": {"inputs": ["close", "open"], "func": rds_086_skew_oc_ret_63d},
    "rds_087_kurt_oc_ret_63d": {"inputs": ["close", "open"], "func": rds_087_kurt_oc_ret_63d},
    "rds_088_var_5pct_oc_ret_63d": {"inputs": ["close", "open"], "func": rds_088_var_5pct_oc_ret_63d},
    "rds_089_skew_oc_ret_21d": {"inputs": ["close", "open"], "func": rds_089_skew_oc_ret_21d},
    "rds_090_kurt_oc_ret_21d": {"inputs": ["close", "open"], "func": rds_090_kurt_oc_ret_21d},
    "rds_091_skew_hl_range_63d": {"inputs": ["close", "high", "low"], "func": rds_091_skew_hl_range_63d},
    "rds_092_kurt_hl_range_63d": {"inputs": ["close", "high", "low"], "func": rds_092_kurt_hl_range_63d},
    "rds_093_var_5pct_hl_range_63d": {"inputs": ["close", "high", "low"], "func": rds_093_var_5pct_hl_range_63d},
    "rds_094_oc_skew_pct_rank_252d": {"inputs": ["close", "open"], "func": rds_094_oc_skew_pct_rank_252d},
    "rds_095_hl_range_kurt_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rds_095_hl_range_kurt_pct_rank_252d},
    "rds_096_iqr_25_75_logret_21d": {"inputs": ["close"], "func": rds_096_iqr_25_75_logret_21d},
    "rds_097_iqr_25_75_logret_63d": {"inputs": ["close"], "func": rds_097_iqr_25_75_logret_63d},
    "rds_098_iqr_10_90_logret_63d": {"inputs": ["close"], "func": rds_098_iqr_10_90_logret_63d},
    "rds_099_iqr_5_95_logret_252d": {"inputs": ["close"], "func": rds_099_iqr_5_95_logret_252d},
    "rds_100_left_iqr_share_63d": {"inputs": ["close"], "func": rds_100_left_iqr_share_63d},
    "rds_101_iqr_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_101_iqr_21d_pct_rank_252d},
    "rds_102_iqr_ratio_21d_to_252d": {"inputs": ["close"], "func": rds_102_iqr_ratio_21d_to_252d},
    "rds_103_q10_logret_21d": {"inputs": ["close"], "func": rds_103_q10_logret_21d},
    "rds_104_q90_logret_21d": {"inputs": ["close"], "func": rds_104_q90_logret_21d},
    "rds_105_quantile_asymmetry_63d": {"inputs": ["close"], "func": rds_105_quantile_asymmetry_63d},
    "rds_106_skew_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_106_skew_21d_vs_252d_ratio},
    "rds_107_kurt_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_107_kurt_21d_vs_252d_ratio},
    "rds_108_var5pct_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_108_var5pct_21d_vs_252d_ratio},
    "rds_109_skew_63d_vs_252d_ratio": {"inputs": ["close"], "func": rds_109_skew_63d_vs_252d_ratio},
    "rds_110_downstd_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_110_downstd_21d_vs_252d_ratio},
    "rds_111_iqr_21d_vs_63d_ratio": {"inputs": ["close"], "func": rds_111_iqr_21d_vs_63d_ratio},
    "rds_112_cvar_21d_vs_252d_ratio": {"inputs": ["close"], "func": rds_112_cvar_21d_vs_252d_ratio},
    "rds_113_skew_21d_minus_63d": {"inputs": ["close"], "func": rds_113_skew_21d_minus_63d},
    "rds_114_kurt_21d_minus_63d": {"inputs": ["close"], "func": rds_114_kurt_21d_minus_63d},
    "rds_115_var5pct_21d_minus_252d": {"inputs": ["close"], "func": rds_115_var5pct_21d_minus_252d},
    "rds_116_skew_logret_on_highvol_days_63d": {"inputs": ["close", "volume"], "func": rds_116_skew_logret_on_highvol_days_63d},
    "rds_117_kurt_logret_on_highvol_days_63d": {"inputs": ["close", "volume"], "func": rds_117_kurt_logret_on_highvol_days_63d},
    "rds_118_skew_logret_on_lowvol_days_63d": {"inputs": ["close", "volume"], "func": rds_118_skew_logret_on_lowvol_days_63d},
    "rds_119_skew_highvol_vs_lowvol_diff_63d": {"inputs": ["close", "volume"], "func": rds_119_skew_highvol_vs_lowvol_diff_63d},
    "rds_120_cvar5pct_highvol_days_63d": {"inputs": ["close", "volume"], "func": rds_120_cvar5pct_highvol_days_63d},
    "rds_121_hurst_rs_63d": {"inputs": ["close"], "func": rds_121_hurst_rs_63d},
    "rds_122_hurst_rs_126d": {"inputs": ["close"], "func": rds_122_hurst_rs_126d},
    "rds_123_hurst_rs_252d": {"inputs": ["close"], "func": rds_123_hurst_rs_252d},
    "rds_124_hurst_dfa_63d": {"inputs": ["close"], "func": rds_124_hurst_dfa_63d},
    "rds_125_hurst_dfa_126d": {"inputs": ["close"], "func": rds_125_hurst_dfa_126d},
    "rds_126_hurst_dfa_252d": {"inputs": ["close"], "func": rds_126_hurst_dfa_252d},
    "rds_127_hurst_rs_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_127_hurst_rs_63d_pct_rank_252d},
    "rds_128_hurst_mean_reverting_flag_63d": {"inputs": ["close"], "func": rds_128_hurst_mean_reverting_flag_63d},
    "rds_129_hurst_rs_minus_dfa_63d": {"inputs": ["close"], "func": rds_129_hurst_rs_minus_dfa_63d},
    "rds_130_shannon_entropy_8bins_63d": {"inputs": ["close"], "func": rds_130_shannon_entropy_8bins_63d},
    "rds_131_shannon_entropy_8bins_126d": {"inputs": ["close"], "func": rds_131_shannon_entropy_8bins_126d},
    "rds_132_shannon_entropy_8bins_252d": {"inputs": ["close"], "func": rds_132_shannon_entropy_8bins_252d},
    "rds_133_shannon_entropy_16bins_63d": {"inputs": ["close"], "func": rds_133_shannon_entropy_16bins_63d},
    "rds_134_shannon_entropy_16bins_126d": {"inputs": ["close"], "func": rds_134_shannon_entropy_16bins_126d},
    "rds_135_shannon_entropy_16bins_252d": {"inputs": ["close"], "func": rds_135_shannon_entropy_16bins_252d},
    "rds_136_shannon_entropy_8bins_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_136_shannon_entropy_8bins_63d_pct_rank_252d},
    "rds_137_shannon_entropy_low_flag_63d": {"inputs": ["close"], "func": rds_137_shannon_entropy_low_flag_63d},
    "rds_138_shannon_entropy_63d_zscore_252d": {"inputs": ["close"], "func": rds_138_shannon_entropy_63d_zscore_252d},
    "rds_139_perm_entropy_order3_63d": {"inputs": ["close"], "func": rds_139_perm_entropy_order3_63d},
    "rds_140_perm_entropy_order3_126d": {"inputs": ["close"], "func": rds_140_perm_entropy_order3_126d},
    "rds_141_perm_entropy_order3_252d": {"inputs": ["close"], "func": rds_141_perm_entropy_order3_252d},
    "rds_142_tail_distress_composite_63d": {"inputs": ["close"], "func": rds_142_tail_distress_composite_63d},
    "rds_143_tail_distress_composite_pct_rank_252d": {"inputs": ["close"], "func": rds_143_tail_distress_composite_pct_rank_252d},
    "rds_144_down_day_ret_skew_63d": {"inputs": ["close"], "func": rds_144_down_day_ret_skew_63d},
    "rds_145_down_day_ret_kurt_63d": {"inputs": ["close"], "func": rds_145_down_day_ret_kurt_63d},
    "rds_146_hurst_rs_63d_zscore_252d": {"inputs": ["close"], "func": rds_146_hurst_rs_63d_zscore_252d},
    "rds_147_perm_entropy_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_147_perm_entropy_63d_pct_rank_252d},
    "rds_148_hurst_entropy_composite_63d": {"inputs": ["close"], "func": rds_148_hurst_entropy_composite_63d},
    "rds_149_var5pct_63d_pct_rank_expanding": {"inputs": ["close"], "func": rds_149_var5pct_63d_pct_rank_expanding},
    "rds_150_full_distress_index_63d": {"inputs": ["close"], "func": rds_150_full_distress_index_63d},
}
