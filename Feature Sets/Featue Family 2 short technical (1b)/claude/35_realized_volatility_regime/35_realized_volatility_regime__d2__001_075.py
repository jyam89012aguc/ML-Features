"""realized_volatility_regime d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the realized-volatility-regime theme:
multi-horizon close-to-close RV, realized variance, vol-cone percentiles,
robust vol, regime classifiers, vol-of-vol, vol persistence (AR/autocorr),
vol-expansion ratios, sign-symmetric vol, term-structure slope, vol entropy,
structural-break / CUSUM detectors, annualized normalizations, volume-weighted
vol, multi-frequency vol, vol-distribution moments, vol clustering / run length,
cumulative variance, overnight/intraday RV split.

Asymmetry (upside/downside semi-variance, skew) is OWNED by family 36 and is
deliberately absent here. Range-based estimators (Parkinson, GK, RS, YZ) are
owned by family 37 and are absent here. This family is strictly close-to-close
(plus, for two bucket-S features, open-to-close overnight/intraday split).

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

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


def _log_returns(close: pd.Series) -> pd.Series:
    return _safe_log(close).diff()


# ============================================================
# Bucket A — Multi-horizon close-to-close RV (sigma of log returns) 001-007
# Each horizon = different hypothesis (spike vs regime)
# ============================================================

def f35_rvre_001_rv_sigma_5d(close: pd.Series) -> pd.Series:
    """Realized volatility (std of log returns) over trailing 5d — weekly spike scale."""
    r = _log_returns(close)
    return r.rolling(WDAYS, min_periods=2).std()


def f35_rvre_002_rv_sigma_21d(close: pd.Series) -> pd.Series:
    """RV (std of log returns) over trailing 21d — monthly regime scale."""
    r = _log_returns(close)
    return r.rolling(MDAYS, min_periods=WDAYS).std()


def f35_rvre_003_rv_sigma_63d(close: pd.Series) -> pd.Series:
    """RV over trailing 63d — quarterly regime."""
    r = _log_returns(close)
    return r.rolling(QDAYS, min_periods=MDAYS).std()


def f35_rvre_004_rv_sigma_126d(close: pd.Series) -> pd.Series:
    """RV over trailing 126d — semi-annual regime."""
    r = _log_returns(close)
    return r.rolling(126, min_periods=QDAYS).std()


def f35_rvre_005_rv_sigma_252d(close: pd.Series) -> pd.Series:
    """RV over trailing 252d — annual regime baseline."""
    r = _log_returns(close)
    return r.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_006_rv_sigma_504d(close: pd.Series) -> pd.Series:
    """RV over trailing 504d — biennial macro-cycle regime."""
    r = _log_returns(close)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f35_rvre_007_rv_sigma_1260d(close: pd.Series) -> pd.Series:
    """RV over trailing 1260d (5y) — long-horizon structural regime."""
    r = _log_returns(close)
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).std()


# ============================================================
# Bucket B — Realized variance & log-variance 008-015
# Distinct concept from sigma — variance compounds linearly under iid
# ============================================================

def f35_rvre_008_rvar_21d(close: pd.Series) -> pd.Series:
    """Realized variance (sigma^2) of log returns over 21d."""
    r = _log_returns(close)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return s ** 2


def f35_rvre_009_rvar_63d(close: pd.Series) -> pd.Series:
    """Realized variance over 63d."""
    r = _log_returns(close)
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return s ** 2


def f35_rvre_010_rvar_252d(close: pd.Series) -> pd.Series:
    """Realized variance over 252d — annualized variance proxy."""
    r = _log_returns(close)
    s = r.rolling(YDAYS, min_periods=QDAYS).std()
    return s ** 2


def f35_rvre_011_log_rvar_21d(close: pd.Series) -> pd.Series:
    """Log realized variance 21d — log-space heteroscedasticity scaling."""
    r = _log_returns(close)
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_log(s ** 2)


def f35_rvre_012_log_rvar_63d(close: pd.Series) -> pd.Series:
    """Log realized variance 63d."""
    r = _log_returns(close)
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_log(s ** 2)


def f35_rvre_013_log_rvar_252d(close: pd.Series) -> pd.Series:
    """Log realized variance 252d — annual log-variance."""
    r = _log_returns(close)
    s = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_log(s ** 2)


def f35_rvre_014_sum_rsq_21d(close: pd.Series) -> pd.Series:
    """Cumulative sum of squared log returns over 21d — additive variance proxy."""
    r = _log_returns(close)
    return (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()


def f35_rvre_015_sum_rsq_252d(close: pd.Series) -> pd.Series:
    """Cumulative sum of squared log returns over 252d — annual additive variance."""
    r = _log_returns(close)
    return (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Vol-cone percentile rank 016-027
# Current N-day RV ranked in trailing M-day distribution of N-day RVs
# ============================================================

def _percentile_rank(s: pd.Series, window: int, min_periods: int) -> pd.Series:
    """Empirical percentile rank of last value in trailing window."""
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def f35_rvre_016_vol_cone_21d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21d-RV within trailing 252d distribution of 21d-RVs."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _percentile_rank(rv21, YDAYS, QDAYS)


def f35_rvre_017_vol_cone_21d_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21d-RV within trailing 504d distribution of 21d-RVs."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _percentile_rank(rv21, DDAYS_2Y, YDAYS)


def f35_rvre_018_vol_cone_63d_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 63d-RV within trailing 504d distribution of 63d-RVs."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _percentile_rank(rv63, DDAYS_2Y, YDAYS)


def f35_rvre_019_vol_cone_63d_in_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 63d-RV within trailing 1260d (5y) distribution."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _percentile_rank(rv63, DDAYS_5Y, YDAYS)


def f35_rvre_020_vol_cone_5d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5d-RV within trailing 252d distribution of 5d-RVs."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    return _percentile_rank(rv5, YDAYS, QDAYS)


def f35_rvre_021_vol_cone_252d_in_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 252d-RV within trailing 1260d distribution of 252d-RVs."""
    r = _log_returns(close)
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _percentile_rank(rv252, DDAYS_5Y, YDAYS)


def f35_rvre_022_vol_cone_21d_zscore_in_504d(close: pd.Series) -> pd.Series:
    """Z-score of current 21d-RV vs trailing 504d distribution of 21d-RVs."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(rv21, DDAYS_2Y, min_periods=YDAYS)


def f35_rvre_023_vol_cone_21d_rank_in_252d(close: pd.Series) -> pd.Series:
    """Rank-of-last-value in 252d, normalized to [0,1] — robust to outliers vs raw percentile."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        v = w[~np.isnan(w)]
        if v.size < 2:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((np.argsort(np.argsort(v))[-1])) / float(v.size - 1)
    return rv21.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f35_rvre_024_vol_cone_63d_rank_in_252d(close: pd.Series) -> pd.Series:
    """Rank-of-last-value of 63d-RV in 252d window normalized to [0,1]."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        v = w[~np.isnan(w)]
        if v.size < 2:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((np.argsort(np.argsort(v))[-1])) / float(v.size - 1)
    return rv63.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f35_rvre_025_vol_cone_decile_state_21d_in_504d(close: pd.Series) -> pd.Series:
    """Decile state (1-10) of current 21d-RV in 504d cone distribution."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    pct = _percentile_rank(rv21, DDAYS_2Y, YDAYS)
    return (np.ceil(pct * 10.0)).clip(lower=1.0, upper=10.0)


def f35_rvre_026_vol_cone_5d_vs_252d_cone_position(close: pd.Series) -> pd.Series:
    """Position of 5d-RV in 252d cone (5d-RV minus 252d-cone-median, scaled by IQR)."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    med = rv5.rolling(YDAYS, min_periods=QDAYS).median()
    q1 = rv5.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q3 = rv5.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    iqr = (q3 - q1).replace(0, np.nan)
    return (rv5 - med) / iqr


def f35_rvre_027_vol_cone_252d_pct_in_1260d_logspace(close: pd.Series) -> pd.Series:
    """Percentile rank of current 252d-RV in 1260d distribution of LOG 252d-RVs.
    Distinct from f35_rvre_021 (which ranks in level space) — log-space is more sensitive
    to relative shifts at low-vol baselines."""
    r = _log_returns(close)
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    lrv = _safe_log(rv252)
    return _percentile_rank(lrv, DDAYS_5Y, YDAYS)


# ============================================================
# Bucket D — Robust vol estimators 028-037
# MAD, IQR, trimmed std, Huber-M scale, Q90-Q10
# ============================================================

def f35_rvre_028_mad_returns_63d(close: pd.Series) -> pd.Series:
    """Median absolute deviation of log returns over 63d (robust scale, scaled by 1.4826)."""
    r = _log_returns(close)
    med = r.rolling(QDAYS, min_periods=MDAYS).median()
    return 1.4826 * (r - med).abs().rolling(QDAYS, min_periods=MDAYS).median()


def f35_rvre_029_iqr_returns_63d(close: pd.Series) -> pd.Series:
    """Inter-quartile range of log returns over 63d."""
    r = _log_returns(close)
    q1 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    q3 = r.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    return q3 - q1


def f35_rvre_030_mad_returns_21d(close: pd.Series) -> pd.Series:
    """MAD of log returns over 21d — short-horizon robust scale."""
    r = _log_returns(close)
    med = r.rolling(MDAYS, min_periods=WDAYS).median()
    return 1.4826 * (r - med).abs().rolling(MDAYS, min_periods=WDAYS).median()


def f35_rvre_031_iqr_returns_252d(close: pd.Series) -> pd.Series:
    """IQR of log returns over 252d — annual robust scale."""
    r = _log_returns(close)
    q1 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    q3 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return q3 - q1


def f35_rvre_032_trimmed_std_returns_63d(close: pd.Series) -> pd.Series:
    """Trimmed (10% each tail) standard deviation of log returns over 63d."""
    r = _log_returns(close)
    def _tstd(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        lo = np.quantile(v, 0.10)
        hi = np.quantile(v, 0.90)
        vv = v[(v >= lo) & (v <= hi)]
        if vv.size < 4:
            return np.nan
        return float(np.std(vv, ddof=1))
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_tstd, raw=True)


def f35_rvre_033_trimmed_std_returns_252d(close: pd.Series) -> pd.Series:
    """Trimmed (10% each tail) std of log returns over 252d."""
    r = _log_returns(close)
    def _tstd(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        lo = np.quantile(v, 0.10)
        hi = np.quantile(v, 0.90)
        vv = v[(v >= lo) & (v <= hi)]
        if vv.size < 10:
            return np.nan
        return float(np.std(vv, ddof=1))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_tstd, raw=True)


def f35_rvre_034_huber_m_scale_63d(close: pd.Series) -> pd.Series:
    """Huber-M robust scale of log returns over 63d (k=1.345 * MAD baseline)."""
    r = _log_returns(close)
    def _huber(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        med = np.median(v)
        mad = np.median(np.abs(v - med))
        if mad == 0:
            return float(np.std(v, ddof=1)) if v.size > 1 else np.nan
        scale = 1.4826 * mad
        k = 1.345 * scale
        u = (v - med).clip(-k, k)
        return float(np.sqrt((u ** 2).sum() / (v.size - 1)))
    return r.rolling(QDAYS, min_periods=MDAYS).apply(_huber, raw=True)


def f35_rvre_035_huber_m_scale_21d(close: pd.Series) -> pd.Series:
    """Huber-M robust scale of log returns over 21d."""
    r = _log_returns(close)
    def _huber(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        med = np.median(v)
        mad = np.median(np.abs(v - med))
        if mad == 0:
            return float(np.std(v, ddof=1)) if v.size > 1 else np.nan
        scale = 1.4826 * mad
        k = 1.345 * scale
        u = (v - med).clip(-k, k)
        return float(np.sqrt((u ** 2).sum() / (v.size - 1)))
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_huber, raw=True)


def f35_rvre_036_median_abs_return_63d(close: pd.Series) -> pd.Series:
    """Median |log return| over 63d — robust central tendency of return magnitude."""
    r = _log_returns(close)
    return r.abs().rolling(QDAYS, min_periods=MDAYS).median()


def f35_rvre_037_q90_minus_q10_returns_252d(close: pd.Series) -> pd.Series:
    """Q90 - Q10 of log returns over 252d — 80% inter-decile spread."""
    r = _log_returns(close)
    q10 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    q90 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return q90 - q10


# ============================================================
# Bucket E — Vol regime classifiers 038-047
# Discrete states, indicators
# ============================================================

def f35_rvre_038_ind_rv21_above_p80_in_252d(close: pd.Series) -> pd.Series:
    """Indicator: current 21d-RV above 80th percentile of trailing 252d 21d-RV cone."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    p80 = rv21.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return (rv21 > p80).astype(float).where(rv21.notna() & p80.notna(), np.nan)


def f35_rvre_039_ind_rv21_above_p90_in_504d(close: pd.Series) -> pd.Series:
    """Indicator: 21d-RV above 90th percentile of trailing 504d 21d-RV distribution."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    p90 = rv21.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    return (rv21 > p90).astype(float).where(rv21.notna() & p90.notna(), np.nan)


def f35_rvre_040_vol_quintile_state_21d_in_504d(close: pd.Series) -> pd.Series:
    """Quintile state (1-5) of current 21d-RV in trailing 504d cone."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    pct = _percentile_rank(rv21, DDAYS_2Y, YDAYS)
    return (np.ceil(pct * 5.0)).clip(lower=1.0, upper=5.0)


def f35_rvre_041_ind_rv21_above_2x_rv252(close: pd.Series) -> pd.Series:
    """Indicator: 21d-RV exceeds 2x the contemporaneous 252d-RV — fast vol spike vs base."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    ratio = _safe_div(rv21, rv252)
    return (ratio > 2.0).astype(float).where(ratio.notna(), np.nan)


def f35_rvre_042_vol_tercile_state_63d_in_252d(close: pd.Series) -> pd.Series:
    """Tercile state (1-3) of 63d-RV within trailing 252d 63d-RV distribution."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    pct = _percentile_rank(rv63, YDAYS, QDAYS)
    return (np.ceil(pct * 3.0)).clip(lower=1.0, upper=3.0)


def f35_rvre_043_ind_rv63_above_p95_in_1260d(close: pd.Series) -> pd.Series:
    """Indicator: 63d-RV above 95th percentile of 1260d cone (5y rare-high-vol regime)."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    p95 = rv63.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    return (rv63 > p95).astype(float).where(rv63.notna() & p95.notna(), np.nan)


def f35_rvre_044_count_regime_flips_above_p80_in_252d(close: pd.Series) -> pd.Series:
    """Count of transitions into 'above-p80' state in trailing 252d — vol regime instability."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    p80 = rv21.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    state = (rv21 > p80).astype(float)
    enters = ((state.diff() > 0)).astype(float)
    return enters.rolling(YDAYS, min_periods=QDAYS).sum()


def f35_rvre_045_binary_high_vol_cluster_21d(close: pd.Series) -> pd.Series:
    """1 if 21d count of |r|>p80 returns >= 5 (i.e. clustered tail-vol month)."""
    r = _log_returns(close)
    p80 = r.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    is_tail = (r.abs() > p80).astype(float)
    cnt = is_tail.rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= 5).astype(float).where(cnt.notna(), np.nan)


def f35_rvre_046_quartile_state_63d_in_252d(close: pd.Series) -> pd.Series:
    """Quartile (1-4) of 63d-RV in trailing 252d distribution."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    pct = _percentile_rank(rv63, YDAYS, QDAYS)
    return (np.ceil(pct * 4.0)).clip(lower=1.0, upper=4.0)


def f35_rvre_047_ind_rv21_above_mean_plus_sigma_252d(close: pd.Series) -> pd.Series:
    """Indicator: 21d-RV exceeds rolling-mean + 1*rolling-sd of 21d-RVs over 252d."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    m = rv21.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = rv21.rolling(YDAYS, min_periods=QDAYS).std()
    thr = m + sd
    return (rv21 > thr).astype(float).where(thr.notna() & rv21.notna(), np.nan)


# ============================================================
# Bucket F — Vol of vol 048-057
# std (and dispersion) of rolling vol — vol regime instability
# ============================================================

def f35_rvre_048_vol_of_vol_21d_over_63d(close: pd.Series) -> pd.Series:
    """Std of 21d-RV measurements over a trailing 63d window — fast vol-of-vol."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(QDAYS, min_periods=MDAYS).std()


def f35_rvre_049_vol_of_vol_21d_over_252d(close: pd.Series) -> pd.Series:
    """Std of 21d-RV over trailing 252d — annual vol-of-vol."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_050_vol_of_vol_63d_over_252d(close: pd.Series) -> pd.Series:
    """Std of 63d-RV over trailing 252d — slower vol-of-vol."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return rv63.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_051_vol_of_vol_63d_over_504d(close: pd.Series) -> pd.Series:
    """Std of 63d-RV over trailing 504d — biennial vol-of-vol."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return rv63.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f35_rvre_052_vol_of_vol_21d_over_504d(close: pd.Series) -> pd.Series:
    """Std of 21d-RV over trailing 504d — 2y vol-of-vol for 21d series."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f35_rvre_053_vol_range_21d_in_252d(close: pd.Series) -> pd.Series:
    """Range (max-min) of 21d-RV across trailing 252d — peak-to-trough vol travel."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(YDAYS, min_periods=QDAYS).max() - rv21.rolling(YDAYS, min_periods=QDAYS).min()


def f35_rvre_054_persistence_of_vol_of_vol_252d(close: pd.Series) -> pd.Series:
    """Std (over 252d) of the 63d vol-of-vol series — persistence of vol-of-vol regime."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    vov_63 = rv21.rolling(QDAYS, min_periods=MDAYS).std()
    return vov_63.rolling(YDAYS, min_periods=QDAYS).std()


def f35_rvre_055_zscore_vol_of_vol_21d_in_504d(close: pd.Series) -> pd.Series:
    """Z-score of the current 21d-RV vol-of-vol (63d window) within trailing 504d."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv21.rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_zscore(vov, DDAYS_2Y, min_periods=YDAYS)


def f35_rvre_056_vol_of_vol_annualized_63d(close: pd.Series) -> pd.Series:
    """sqrt(252)-annualized 63d vol-of-vol of the 21d-RV — scale-aligned magnitude."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv21.rolling(QDAYS, min_periods=MDAYS).std() * np.sqrt(float(YDAYS))


def f35_rvre_057_cv_of_rv21_in_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of 21d-RV over 252d — scale-invariant vol-of-vol."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    m = rv21.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = rv21.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd, m)


# ============================================================
# Bucket G — Vol persistence 058-067
# AR(1) of r^2, autocorr of |r|, half-life of vol decay
# ============================================================

def _rolling_autocorr(s: pd.Series, lag: int, window: int, min_periods: int) -> pd.Series:
    """Rolling autocorrelation at given lag."""
    a = s
    b = s.shift(lag)
    ma = a.rolling(window, min_periods=min_periods).mean()
    mb = b.rolling(window, min_periods=min_periods).mean()
    sa = a.rolling(window, min_periods=min_periods).std()
    sb = b.rolling(window, min_periods=min_periods).std()
    cov = ((a - ma) * (b - mb)).rolling(window, min_periods=min_periods).mean()
    return _safe_div(cov, sa * sb)


def f35_rvre_058_ar1_rsq_252d(close: pd.Series) -> pd.Series:
    """AR(1) coefficient (autocorr lag 1) of squared log returns over 252d — vol persistence."""
    r = _log_returns(close)
    rsq = r ** 2
    return _rolling_autocorr(rsq, 1, YDAYS, QDAYS)


def f35_rvre_059_ar1_rsq_504d(close: pd.Series) -> pd.Series:
    """AR(1) of squared log returns over 504d — long-horizon vol persistence."""
    r = _log_returns(close)
    rsq = r ** 2
    return _rolling_autocorr(rsq, 1, DDAYS_2Y, YDAYS)


def f35_rvre_060_autocorr_abs_r_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorr lag-1 of |log returns| over 252d — vol persistence via abs-returns."""
    r = _log_returns(close).abs()
    return _rolling_autocorr(r, 1, YDAYS, QDAYS)


def f35_rvre_061_autocorr_abs_r_lag5_252d(close: pd.Series) -> pd.Series:
    """Autocorr lag-5 of |log returns| over 252d — weekly vol echo."""
    r = _log_returns(close).abs()
    return _rolling_autocorr(r, 5, YDAYS, QDAYS)


def f35_rvre_062_autocorr_rsq_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorr lag-1 of squared log returns over 63d — short-horizon vol persistence."""
    r = _log_returns(close)
    return _rolling_autocorr(r ** 2, 1, QDAYS, MDAYS)


def f35_rvre_063_vol_half_life_from_ar1_rsq_252d(close: pd.Series) -> pd.Series:
    """Half-life (in bars) of squared-return AR(1) decay: ln(0.5)/ln(rho) when 0<rho<1."""
    r = _log_returns(close)
    rho = _rolling_autocorr(r ** 2, 1, YDAYS, QDAYS)
    rho_clip = rho.where((rho > 1e-6) & (rho < 1.0), np.nan)
    return np.log(0.5) / np.log(rho_clip)


def f35_rvre_064_ljung_box_lag5_rsq_252d(close: pd.Series) -> pd.Series:
    """Ljung-Box statistic (lag 5) on squared returns over 252d — multi-lag vol persistence."""
    r = _log_returns(close)
    rsq = r ** 2
    def _lb(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < 30:
            return np.nan
        m = v.mean()
        x = v - m
        denom = (x ** 2).sum()
        if denom == 0:
            return np.nan
        stat = 0.0
        for k in range(1, 6):
            if k >= n:
                break
            num = (x[k:] * x[:-k]).sum()
            rho_k = num / denom
            stat += (rho_k ** 2) / (n - k)
        return float(n * (n + 2) * stat)
    return rsq.rolling(YDAYS, min_periods=QDAYS).apply(_lb, raw=True)


def f35_rvre_065_vol_clustering_index_252d(close: pd.Series) -> pd.Series:
    """Vol-clustering: cov(|r|, |r_{-1}|) / var(|r|) over 252d — alt formulation of vol persistence."""
    r = _log_returns(close).abs()
    rp = r.shift(1)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    mp = rp.rolling(YDAYS, min_periods=QDAYS).mean()
    cov = ((r - m) * (rp - mp)).rolling(YDAYS, min_periods=QDAYS).mean()
    var = ((r - m) ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(cov, var)


def f35_rvre_066_hurst_like_exponent_abs_r_504d(close: pd.Series) -> pd.Series:
    """Hurst-like exponent of |log returns| over 504d via two-point R/S regression
    (slope of log R/S vs log n at n=21 and n=63)."""
    r = _log_returns(close).abs()
    def _hurst(w):
        v = w[~np.isnan(w)]
        if v.size < 200:
            return np.nan
        def _rs(arr, n):
            k = arr.size // n
            if k < 2:
                return np.nan
            chunks = arr[: k * n].reshape(k, n)
            mean = chunks.mean(axis=1, keepdims=True)
            dev = chunks - mean
            cum = dev.cumsum(axis=1)
            rng = cum.max(axis=1) - cum.min(axis=1)
            sd = chunks.std(axis=1, ddof=1)
            sd_safe = np.where(sd == 0, np.nan, sd)
            rs = rng / sd_safe
            rs = rs[np.isfinite(rs)]
            if rs.size == 0:
                return np.nan
            return float(rs.mean())
        rs1 = _rs(v, 21)
        rs2 = _rs(v, 63)
        if rs1 is np.nan or rs2 is np.nan or not np.isfinite(rs1) or not np.isfinite(rs2) or rs1 <= 0 or rs2 <= 0:
            return np.nan
        return float((np.log(rs2) - np.log(rs1)) / (np.log(63.0) - np.log(21.0)))
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_hurst, raw=True)


def f35_rvre_067_rs_stat_abs_r_252d(close: pd.Series) -> pd.Series:
    """Rescaled-range R/S statistic of |log returns| over 252d (single horizon)."""
    r = _log_returns(close).abs()
    def _rs(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        m = v.mean()
        dev = v - m
        cum = np.cumsum(dev)
        rng = cum.max() - cum.min()
        sd = v.std(ddof=1)
        if sd == 0:
            return np.nan
        return float(rng / sd)
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_rs, raw=True)


# ============================================================
# Bucket H — Vol-expansion ratios 068-075
# Each ratio = distinct regime hypothesis
# ============================================================

def f35_rvre_068_ratio_rv21_to_rv63(close: pd.Series) -> pd.Series:
    """Ratio of 21d-RV to 63d-RV — short-over-medium vol expansion."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(rv21, rv63)


def f35_rvre_069_ratio_rv63_to_rv252(close: pd.Series) -> pd.Series:
    """Ratio of 63d-RV to 252d-RV — medium-over-annual vol expansion."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(rv63, rv252)


def f35_rvre_070_ratio_rv21_to_rv252(close: pd.Series) -> pd.Series:
    """Ratio of 21d-RV to 252d-RV — short-over-annual vol regime shift."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    rv252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(rv21, rv252)


def f35_rvre_071_ratio_rv5_to_rv63(close: pd.Series) -> pd.Series:
    """Ratio of 5d-RV to 63d-RV — weekly-over-quarterly vol expansion (spike detector)."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(rv5, rv63)


def f35_rvre_072_ratio_rv126_to_rv504(close: pd.Series) -> pd.Series:
    """Ratio of 126d-RV to 504d-RV — half-year over 2y vol regime."""
    r = _log_returns(close)
    rv126 = r.rolling(126, min_periods=QDAYS).std()
    rv504 = r.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _safe_div(rv126, rv504)


def f35_rvre_073_ratio_rv21_to_rv504(close: pd.Series) -> pd.Series:
    """Ratio of 21d-RV to 504d-RV — short over biennial regime."""
    r = _log_returns(close)
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    rv504 = r.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _safe_div(rv21, rv504)


def f35_rvre_074_ratio_rv5_to_rv21(close: pd.Series) -> pd.Series:
    """Ratio of 5d-RV to 21d-RV — intra-month vol acceleration."""
    r = _log_returns(close)
    rv5 = r.rolling(WDAYS, min_periods=2).std()
    rv21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(rv5, rv21)


def f35_rvre_075_ratio_rv63_to_rv1260(close: pd.Series) -> pd.Series:
    """Ratio of 63d-RV to 1260d-RV — quarterly over 5y structural regime."""
    r = _log_returns(close)
    rv63 = r.rolling(QDAYS, min_periods=MDAYS).std()
    rv1260 = r.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    return _safe_div(rv63, rv1260)


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f35_rvre_001_rv_sigma_5d_d2(close):
    return f35_rvre_001_rv_sigma_5d(close).diff().diff()


def f35_rvre_002_rv_sigma_21d_d2(close):
    return f35_rvre_002_rv_sigma_21d(close).diff().diff()


def f35_rvre_003_rv_sigma_63d_d2(close):
    return f35_rvre_003_rv_sigma_63d(close).diff().diff()


def f35_rvre_004_rv_sigma_126d_d2(close):
    return f35_rvre_004_rv_sigma_126d(close).diff().diff()


def f35_rvre_005_rv_sigma_252d_d2(close):
    return f35_rvre_005_rv_sigma_252d(close).diff().diff()


def f35_rvre_006_rv_sigma_504d_d2(close):
    return f35_rvre_006_rv_sigma_504d(close).diff().diff()


def f35_rvre_007_rv_sigma_1260d_d2(close):
    return f35_rvre_007_rv_sigma_1260d(close).diff().diff()


def f35_rvre_008_rvar_21d_d2(close):
    return f35_rvre_008_rvar_21d(close).diff().diff()


def f35_rvre_009_rvar_63d_d2(close):
    return f35_rvre_009_rvar_63d(close).diff().diff()


def f35_rvre_010_rvar_252d_d2(close):
    return f35_rvre_010_rvar_252d(close).diff().diff()


def f35_rvre_011_log_rvar_21d_d2(close):
    return f35_rvre_011_log_rvar_21d(close).diff().diff()


def f35_rvre_012_log_rvar_63d_d2(close):
    return f35_rvre_012_log_rvar_63d(close).diff().diff()


def f35_rvre_013_log_rvar_252d_d2(close):
    return f35_rvre_013_log_rvar_252d(close).diff().diff()


def f35_rvre_014_sum_rsq_21d_d2(close):
    return f35_rvre_014_sum_rsq_21d(close).diff().diff()


def f35_rvre_015_sum_rsq_252d_d2(close):
    return f35_rvre_015_sum_rsq_252d(close).diff().diff()


def f35_rvre_016_vol_cone_21d_in_252d_d2(close):
    return f35_rvre_016_vol_cone_21d_in_252d(close).diff().diff()


def f35_rvre_017_vol_cone_21d_in_504d_d2(close):
    return f35_rvre_017_vol_cone_21d_in_504d(close).diff().diff()


def f35_rvre_018_vol_cone_63d_in_504d_d2(close):
    return f35_rvre_018_vol_cone_63d_in_504d(close).diff().diff()


def f35_rvre_019_vol_cone_63d_in_1260d_d2(close):
    return f35_rvre_019_vol_cone_63d_in_1260d(close).diff().diff()


def f35_rvre_020_vol_cone_5d_in_252d_d2(close):
    return f35_rvre_020_vol_cone_5d_in_252d(close).diff().diff()


def f35_rvre_021_vol_cone_252d_in_1260d_d2(close):
    return f35_rvre_021_vol_cone_252d_in_1260d(close).diff().diff()


def f35_rvre_022_vol_cone_21d_zscore_in_504d_d2(close):
    return f35_rvre_022_vol_cone_21d_zscore_in_504d(close).diff().diff()


def f35_rvre_023_vol_cone_21d_rank_in_252d_d2(close):
    return f35_rvre_023_vol_cone_21d_rank_in_252d(close).diff().diff()


def f35_rvre_024_vol_cone_63d_rank_in_252d_d2(close):
    return f35_rvre_024_vol_cone_63d_rank_in_252d(close).diff().diff()


def f35_rvre_025_vol_cone_decile_state_21d_in_504d_d2(close):
    return f35_rvre_025_vol_cone_decile_state_21d_in_504d(close).diff().diff()


def f35_rvre_026_vol_cone_5d_vs_252d_cone_position_d2(close):
    return f35_rvre_026_vol_cone_5d_vs_252d_cone_position(close).diff().diff()


def f35_rvre_027_vol_cone_252d_pct_in_1260d_logspace_d2(close):
    return f35_rvre_027_vol_cone_252d_pct_in_1260d_logspace(close).diff().diff()


def f35_rvre_028_mad_returns_63d_d2(close):
    return f35_rvre_028_mad_returns_63d(close).diff().diff()


def f35_rvre_029_iqr_returns_63d_d2(close):
    return f35_rvre_029_iqr_returns_63d(close).diff().diff()


def f35_rvre_030_mad_returns_21d_d2(close):
    return f35_rvre_030_mad_returns_21d(close).diff().diff()


def f35_rvre_031_iqr_returns_252d_d2(close):
    return f35_rvre_031_iqr_returns_252d(close).diff().diff()


def f35_rvre_032_trimmed_std_returns_63d_d2(close):
    return f35_rvre_032_trimmed_std_returns_63d(close).diff().diff()


def f35_rvre_033_trimmed_std_returns_252d_d2(close):
    return f35_rvre_033_trimmed_std_returns_252d(close).diff().diff()


def f35_rvre_034_huber_m_scale_63d_d2(close):
    return f35_rvre_034_huber_m_scale_63d(close).diff().diff()


def f35_rvre_035_huber_m_scale_21d_d2(close):
    return f35_rvre_035_huber_m_scale_21d(close).diff().diff()


def f35_rvre_036_median_abs_return_63d_d2(close):
    return f35_rvre_036_median_abs_return_63d(close).diff().diff()


def f35_rvre_037_q90_minus_q10_returns_252d_d2(close):
    return f35_rvre_037_q90_minus_q10_returns_252d(close).diff().diff()


def f35_rvre_038_ind_rv21_above_p80_in_252d_d2(close):
    return f35_rvre_038_ind_rv21_above_p80_in_252d(close).diff().diff()


def f35_rvre_039_ind_rv21_above_p90_in_504d_d2(close):
    return f35_rvre_039_ind_rv21_above_p90_in_504d(close).diff().diff()


def f35_rvre_040_vol_quintile_state_21d_in_504d_d2(close):
    return f35_rvre_040_vol_quintile_state_21d_in_504d(close).diff().diff()


def f35_rvre_041_ind_rv21_above_2x_rv252_d2(close):
    return f35_rvre_041_ind_rv21_above_2x_rv252(close).diff().diff()


def f35_rvre_042_vol_tercile_state_63d_in_252d_d2(close):
    return f35_rvre_042_vol_tercile_state_63d_in_252d(close).diff().diff()


def f35_rvre_043_ind_rv63_above_p95_in_1260d_d2(close):
    return f35_rvre_043_ind_rv63_above_p95_in_1260d(close).diff().diff()


def f35_rvre_044_count_regime_flips_above_p80_in_252d_d2(close):
    return f35_rvre_044_count_regime_flips_above_p80_in_252d(close).diff().diff()


def f35_rvre_045_binary_high_vol_cluster_21d_d2(close):
    return f35_rvre_045_binary_high_vol_cluster_21d(close).diff().diff()


def f35_rvre_046_quartile_state_63d_in_252d_d2(close):
    return f35_rvre_046_quartile_state_63d_in_252d(close).diff().diff()


def f35_rvre_047_ind_rv21_above_mean_plus_sigma_252d_d2(close):
    return f35_rvre_047_ind_rv21_above_mean_plus_sigma_252d(close).diff().diff()


def f35_rvre_048_vol_of_vol_21d_over_63d_d2(close):
    return f35_rvre_048_vol_of_vol_21d_over_63d(close).diff().diff()


def f35_rvre_049_vol_of_vol_21d_over_252d_d2(close):
    return f35_rvre_049_vol_of_vol_21d_over_252d(close).diff().diff()


def f35_rvre_050_vol_of_vol_63d_over_252d_d2(close):
    return f35_rvre_050_vol_of_vol_63d_over_252d(close).diff().diff()


def f35_rvre_051_vol_of_vol_63d_over_504d_d2(close):
    return f35_rvre_051_vol_of_vol_63d_over_504d(close).diff().diff()


def f35_rvre_052_vol_of_vol_21d_over_504d_d2(close):
    return f35_rvre_052_vol_of_vol_21d_over_504d(close).diff().diff()


def f35_rvre_053_vol_range_21d_in_252d_d2(close):
    return f35_rvre_053_vol_range_21d_in_252d(close).diff().diff()


def f35_rvre_054_persistence_of_vol_of_vol_252d_d2(close):
    return f35_rvre_054_persistence_of_vol_of_vol_252d(close).diff().diff()


def f35_rvre_055_zscore_vol_of_vol_21d_in_504d_d2(close):
    return f35_rvre_055_zscore_vol_of_vol_21d_in_504d(close).diff().diff()


def f35_rvre_056_vol_of_vol_annualized_63d_d2(close):
    return f35_rvre_056_vol_of_vol_annualized_63d(close).diff().diff()


def f35_rvre_057_cv_of_rv21_in_252d_d2(close):
    return f35_rvre_057_cv_of_rv21_in_252d(close).diff().diff()


def f35_rvre_058_ar1_rsq_252d_d2(close):
    return f35_rvre_058_ar1_rsq_252d(close).diff().diff()


def f35_rvre_059_ar1_rsq_504d_d2(close):
    return f35_rvre_059_ar1_rsq_504d(close).diff().diff()


def f35_rvre_060_autocorr_abs_r_lag1_252d_d2(close):
    return f35_rvre_060_autocorr_abs_r_lag1_252d(close).diff().diff()


def f35_rvre_061_autocorr_abs_r_lag5_252d_d2(close):
    return f35_rvre_061_autocorr_abs_r_lag5_252d(close).diff().diff()


def f35_rvre_062_autocorr_rsq_lag1_63d_d2(close):
    return f35_rvre_062_autocorr_rsq_lag1_63d(close).diff().diff()


def f35_rvre_063_vol_half_life_from_ar1_rsq_252d_d2(close):
    return f35_rvre_063_vol_half_life_from_ar1_rsq_252d(close).diff().diff()


def f35_rvre_064_ljung_box_lag5_rsq_252d_d2(close):
    return f35_rvre_064_ljung_box_lag5_rsq_252d(close).diff().diff()


def f35_rvre_065_vol_clustering_index_252d_d2(close):
    return f35_rvre_065_vol_clustering_index_252d(close).diff().diff()


def f35_rvre_066_hurst_like_exponent_abs_r_504d_d2(close):
    return f35_rvre_066_hurst_like_exponent_abs_r_504d(close).diff().diff()


def f35_rvre_067_rs_stat_abs_r_252d_d2(close):
    return f35_rvre_067_rs_stat_abs_r_252d(close).diff().diff()


def f35_rvre_068_ratio_rv21_to_rv63_d2(close):
    return f35_rvre_068_ratio_rv21_to_rv63(close).diff().diff()


def f35_rvre_069_ratio_rv63_to_rv252_d2(close):
    return f35_rvre_069_ratio_rv63_to_rv252(close).diff().diff()


def f35_rvre_070_ratio_rv21_to_rv252_d2(close):
    return f35_rvre_070_ratio_rv21_to_rv252(close).diff().diff()


def f35_rvre_071_ratio_rv5_to_rv63_d2(close):
    return f35_rvre_071_ratio_rv5_to_rv63(close).diff().diff()


def f35_rvre_072_ratio_rv126_to_rv504_d2(close):
    return f35_rvre_072_ratio_rv126_to_rv504(close).diff().diff()


def f35_rvre_073_ratio_rv21_to_rv504_d2(close):
    return f35_rvre_073_ratio_rv21_to_rv504(close).diff().diff()


def f35_rvre_074_ratio_rv5_to_rv21_d2(close):
    return f35_rvre_074_ratio_rv5_to_rv21(close).diff().diff()


def f35_rvre_075_ratio_rv63_to_rv1260_d2(close):
    return f35_rvre_075_ratio_rv63_to_rv1260(close).diff().diff()


REALIZED_VOLATILITY_REGIME_D2_REGISTRY_001_075 = {
    "f35_rvre_001_rv_sigma_5d_d2": {"inputs": ["close"], "func": f35_rvre_001_rv_sigma_5d_d2},
    "f35_rvre_002_rv_sigma_21d_d2": {"inputs": ["close"], "func": f35_rvre_002_rv_sigma_21d_d2},
    "f35_rvre_003_rv_sigma_63d_d2": {"inputs": ["close"], "func": f35_rvre_003_rv_sigma_63d_d2},
    "f35_rvre_004_rv_sigma_126d_d2": {"inputs": ["close"], "func": f35_rvre_004_rv_sigma_126d_d2},
    "f35_rvre_005_rv_sigma_252d_d2": {"inputs": ["close"], "func": f35_rvre_005_rv_sigma_252d_d2},
    "f35_rvre_006_rv_sigma_504d_d2": {"inputs": ["close"], "func": f35_rvre_006_rv_sigma_504d_d2},
    "f35_rvre_007_rv_sigma_1260d_d2": {"inputs": ["close"], "func": f35_rvre_007_rv_sigma_1260d_d2},
    "f35_rvre_008_rvar_21d_d2": {"inputs": ["close"], "func": f35_rvre_008_rvar_21d_d2},
    "f35_rvre_009_rvar_63d_d2": {"inputs": ["close"], "func": f35_rvre_009_rvar_63d_d2},
    "f35_rvre_010_rvar_252d_d2": {"inputs": ["close"], "func": f35_rvre_010_rvar_252d_d2},
    "f35_rvre_011_log_rvar_21d_d2": {"inputs": ["close"], "func": f35_rvre_011_log_rvar_21d_d2},
    "f35_rvre_012_log_rvar_63d_d2": {"inputs": ["close"], "func": f35_rvre_012_log_rvar_63d_d2},
    "f35_rvre_013_log_rvar_252d_d2": {"inputs": ["close"], "func": f35_rvre_013_log_rvar_252d_d2},
    "f35_rvre_014_sum_rsq_21d_d2": {"inputs": ["close"], "func": f35_rvre_014_sum_rsq_21d_d2},
    "f35_rvre_015_sum_rsq_252d_d2": {"inputs": ["close"], "func": f35_rvre_015_sum_rsq_252d_d2},
    "f35_rvre_016_vol_cone_21d_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_016_vol_cone_21d_in_252d_d2},
    "f35_rvre_017_vol_cone_21d_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_017_vol_cone_21d_in_504d_d2},
    "f35_rvre_018_vol_cone_63d_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_018_vol_cone_63d_in_504d_d2},
    "f35_rvre_019_vol_cone_63d_in_1260d_d2": {"inputs": ["close"], "func": f35_rvre_019_vol_cone_63d_in_1260d_d2},
    "f35_rvre_020_vol_cone_5d_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_020_vol_cone_5d_in_252d_d2},
    "f35_rvre_021_vol_cone_252d_in_1260d_d2": {"inputs": ["close"], "func": f35_rvre_021_vol_cone_252d_in_1260d_d2},
    "f35_rvre_022_vol_cone_21d_zscore_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_022_vol_cone_21d_zscore_in_504d_d2},
    "f35_rvre_023_vol_cone_21d_rank_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_023_vol_cone_21d_rank_in_252d_d2},
    "f35_rvre_024_vol_cone_63d_rank_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_024_vol_cone_63d_rank_in_252d_d2},
    "f35_rvre_025_vol_cone_decile_state_21d_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_025_vol_cone_decile_state_21d_in_504d_d2},
    "f35_rvre_026_vol_cone_5d_vs_252d_cone_position_d2": {"inputs": ["close"], "func": f35_rvre_026_vol_cone_5d_vs_252d_cone_position_d2},
    "f35_rvre_027_vol_cone_252d_pct_in_1260d_logspace_d2": {"inputs": ["close"], "func": f35_rvre_027_vol_cone_252d_pct_in_1260d_logspace_d2},
    "f35_rvre_028_mad_returns_63d_d2": {"inputs": ["close"], "func": f35_rvre_028_mad_returns_63d_d2},
    "f35_rvre_029_iqr_returns_63d_d2": {"inputs": ["close"], "func": f35_rvre_029_iqr_returns_63d_d2},
    "f35_rvre_030_mad_returns_21d_d2": {"inputs": ["close"], "func": f35_rvre_030_mad_returns_21d_d2},
    "f35_rvre_031_iqr_returns_252d_d2": {"inputs": ["close"], "func": f35_rvre_031_iqr_returns_252d_d2},
    "f35_rvre_032_trimmed_std_returns_63d_d2": {"inputs": ["close"], "func": f35_rvre_032_trimmed_std_returns_63d_d2},
    "f35_rvre_033_trimmed_std_returns_252d_d2": {"inputs": ["close"], "func": f35_rvre_033_trimmed_std_returns_252d_d2},
    "f35_rvre_034_huber_m_scale_63d_d2": {"inputs": ["close"], "func": f35_rvre_034_huber_m_scale_63d_d2},
    "f35_rvre_035_huber_m_scale_21d_d2": {"inputs": ["close"], "func": f35_rvre_035_huber_m_scale_21d_d2},
    "f35_rvre_036_median_abs_return_63d_d2": {"inputs": ["close"], "func": f35_rvre_036_median_abs_return_63d_d2},
    "f35_rvre_037_q90_minus_q10_returns_252d_d2": {"inputs": ["close"], "func": f35_rvre_037_q90_minus_q10_returns_252d_d2},
    "f35_rvre_038_ind_rv21_above_p80_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_038_ind_rv21_above_p80_in_252d_d2},
    "f35_rvre_039_ind_rv21_above_p90_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_039_ind_rv21_above_p90_in_504d_d2},
    "f35_rvre_040_vol_quintile_state_21d_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_040_vol_quintile_state_21d_in_504d_d2},
    "f35_rvre_041_ind_rv21_above_2x_rv252_d2": {"inputs": ["close"], "func": f35_rvre_041_ind_rv21_above_2x_rv252_d2},
    "f35_rvre_042_vol_tercile_state_63d_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_042_vol_tercile_state_63d_in_252d_d2},
    "f35_rvre_043_ind_rv63_above_p95_in_1260d_d2": {"inputs": ["close"], "func": f35_rvre_043_ind_rv63_above_p95_in_1260d_d2},
    "f35_rvre_044_count_regime_flips_above_p80_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_044_count_regime_flips_above_p80_in_252d_d2},
    "f35_rvre_045_binary_high_vol_cluster_21d_d2": {"inputs": ["close"], "func": f35_rvre_045_binary_high_vol_cluster_21d_d2},
    "f35_rvre_046_quartile_state_63d_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_046_quartile_state_63d_in_252d_d2},
    "f35_rvre_047_ind_rv21_above_mean_plus_sigma_252d_d2": {"inputs": ["close"], "func": f35_rvre_047_ind_rv21_above_mean_plus_sigma_252d_d2},
    "f35_rvre_048_vol_of_vol_21d_over_63d_d2": {"inputs": ["close"], "func": f35_rvre_048_vol_of_vol_21d_over_63d_d2},
    "f35_rvre_049_vol_of_vol_21d_over_252d_d2": {"inputs": ["close"], "func": f35_rvre_049_vol_of_vol_21d_over_252d_d2},
    "f35_rvre_050_vol_of_vol_63d_over_252d_d2": {"inputs": ["close"], "func": f35_rvre_050_vol_of_vol_63d_over_252d_d2},
    "f35_rvre_051_vol_of_vol_63d_over_504d_d2": {"inputs": ["close"], "func": f35_rvre_051_vol_of_vol_63d_over_504d_d2},
    "f35_rvre_052_vol_of_vol_21d_over_504d_d2": {"inputs": ["close"], "func": f35_rvre_052_vol_of_vol_21d_over_504d_d2},
    "f35_rvre_053_vol_range_21d_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_053_vol_range_21d_in_252d_d2},
    "f35_rvre_054_persistence_of_vol_of_vol_252d_d2": {"inputs": ["close"], "func": f35_rvre_054_persistence_of_vol_of_vol_252d_d2},
    "f35_rvre_055_zscore_vol_of_vol_21d_in_504d_d2": {"inputs": ["close"], "func": f35_rvre_055_zscore_vol_of_vol_21d_in_504d_d2},
    "f35_rvre_056_vol_of_vol_annualized_63d_d2": {"inputs": ["close"], "func": f35_rvre_056_vol_of_vol_annualized_63d_d2},
    "f35_rvre_057_cv_of_rv21_in_252d_d2": {"inputs": ["close"], "func": f35_rvre_057_cv_of_rv21_in_252d_d2},
    "f35_rvre_058_ar1_rsq_252d_d2": {"inputs": ["close"], "func": f35_rvre_058_ar1_rsq_252d_d2},
    "f35_rvre_059_ar1_rsq_504d_d2": {"inputs": ["close"], "func": f35_rvre_059_ar1_rsq_504d_d2},
    "f35_rvre_060_autocorr_abs_r_lag1_252d_d2": {"inputs": ["close"], "func": f35_rvre_060_autocorr_abs_r_lag1_252d_d2},
    "f35_rvre_061_autocorr_abs_r_lag5_252d_d2": {"inputs": ["close"], "func": f35_rvre_061_autocorr_abs_r_lag5_252d_d2},
    "f35_rvre_062_autocorr_rsq_lag1_63d_d2": {"inputs": ["close"], "func": f35_rvre_062_autocorr_rsq_lag1_63d_d2},
    "f35_rvre_063_vol_half_life_from_ar1_rsq_252d_d2": {"inputs": ["close"], "func": f35_rvre_063_vol_half_life_from_ar1_rsq_252d_d2},
    "f35_rvre_064_ljung_box_lag5_rsq_252d_d2": {"inputs": ["close"], "func": f35_rvre_064_ljung_box_lag5_rsq_252d_d2},
    "f35_rvre_065_vol_clustering_index_252d_d2": {"inputs": ["close"], "func": f35_rvre_065_vol_clustering_index_252d_d2},
    "f35_rvre_066_hurst_like_exponent_abs_r_504d_d2": {"inputs": ["close"], "func": f35_rvre_066_hurst_like_exponent_abs_r_504d_d2},
    "f35_rvre_067_rs_stat_abs_r_252d_d2": {"inputs": ["close"], "func": f35_rvre_067_rs_stat_abs_r_252d_d2},
    "f35_rvre_068_ratio_rv21_to_rv63_d2": {"inputs": ["close"], "func": f35_rvre_068_ratio_rv21_to_rv63_d2},
    "f35_rvre_069_ratio_rv63_to_rv252_d2": {"inputs": ["close"], "func": f35_rvre_069_ratio_rv63_to_rv252_d2},
    "f35_rvre_070_ratio_rv21_to_rv252_d2": {"inputs": ["close"], "func": f35_rvre_070_ratio_rv21_to_rv252_d2},
    "f35_rvre_071_ratio_rv5_to_rv63_d2": {"inputs": ["close"], "func": f35_rvre_071_ratio_rv5_to_rv63_d2},
    "f35_rvre_072_ratio_rv126_to_rv504_d2": {"inputs": ["close"], "func": f35_rvre_072_ratio_rv126_to_rv504_d2},
    "f35_rvre_073_ratio_rv21_to_rv504_d2": {"inputs": ["close"], "func": f35_rvre_073_ratio_rv21_to_rv504_d2},
    "f35_rvre_074_ratio_rv5_to_rv21_d2": {"inputs": ["close"], "func": f35_rvre_074_ratio_rv5_to_rv21_d2},
    "f35_rvre_075_ratio_rv63_to_rv1260_d2": {"inputs": ["close"], "func": f35_rvre_075_ratio_rv63_to_rv1260_d2},
}
